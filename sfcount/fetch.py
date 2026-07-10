"""Stages 1+2: probe per-release snapshot URLs and download era source files."""
import csv
import datetime as dt
import time
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Iterator
from zoneinfo import ZoneInfo

BASE = "https://www.sfelections.org/results"
UA = {"User-Agent": "Mozilla/5.0 (research; SF vote-count timeline)"}
DELAY = 0.25          # polite rate limit, seconds between requests
PROBE_DAYS = 35       # election day + 35 covers certification
NIGHT_SUFFIXES = range(1, 7)
ERA_FILES = {"B": "summary.txt", "C": "summary.xml"}
PACIFIC = ZoneInfo("America/Los_Angeles")
MANIFEST_COLS = ["election", "snapshot", "filename", "status", "last_modified"]


def snap_candidates(edate: dt.date) -> Iterator[str]:
    e = edate.strftime("%Y%m%d")
    for n in NIGHT_SUFFIXES:
        yield f"{e}_{n}"
    for i in range(PROBE_DAYS + 1):
        yield (edate + dt.timedelta(days=i)).strftime("%Y%m%d")


def http_date_to_pacific_iso(value: str) -> str:
    """RFC 7231 HTTP date -> naive Pacific-local ISO string."""
    return parsedate_to_datetime(value).astimezone(PACIFIC).replace(tzinfo=None).isoformat()


class MissCache:
    """Probe misses persisted to disk so reruns skip known-404 URLs."""

    def __init__(self, path: Path):
        self.path = path
        self.urls = set(path.read_text().split()) if path.exists() else set()

    def __contains__(self, url: str) -> bool:
        return url in self.urls

    def add(self, url: str) -> None:
        self.urls.add(url)

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text("\n".join(sorted(self.urls)))


def looks_like_source(era: str, content: bytes) -> bool:
    """Guard against soft-404 HTML served with status 200."""
    head = content.lstrip(b"\xef\xbb\xbf")[:64]
    return head.startswith(b"<?xml") if era == "C" else head.startswith(b"CONTEST_ID")


def load_manifest(path: Path) -> dict[tuple[str, str], dict]:
    if not path.exists():
        return {}
    with open(path, newline="") as f:
        return {(r["election"], r["snapshot"]): r for r in csv.DictReader(f)}


def save_manifest(path: Path, manifest: dict[tuple[str, str], dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=MANIFEST_COLS)
        w.writeheader()
        for key in sorted(manifest):
            w.writerow(manifest[key])


def _manifest_row(e, snap, fname, status, headers):
    lm = headers.get("Last-Modified")
    return {
        "election": e, "snapshot": snap, "filename": fname, "status": status,
        "last_modified": http_date_to_pacific_iso(lm) if lm else "",
    }


# Era C elections whose summary.xml lacks the ED/VBM split; their snapshots
# also get the per-precinct statement of the vote ({snap}_psov.xml, ~27 MB).
PSOV_ELECTIONS = {"20191105"}


def _fetch_psov(session, e: str, snap: str, raw_dir: Path,
                cache: MissCache, certifiable: bool) -> None:
    dest = raw_dir / e / snap / f"{snap}_psov.xml"
    if dest.exists():
        return
    url = f"{BASE}/{e}/data/{snap}/{snap}_psov.xml"
    if url in cache:
        return
    r = session.get(url, timeout=120)
    if r.status_code == 200 and looks_like_source("C", r.content):
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(r.content)
    elif certifiable:
        cache.add(url)


def fetch_election(session, edate: dt.date, era: str, raw_dir: Path,
                   cache: MissCache, manifest: dict, today: dt.date) -> int:
    fname = ERA_FILES[era]
    e = edate.strftime("%Y%m%d")
    certifiable = today > edate + dt.timedelta(days=PROBE_DAYS)
    found = 0
    for snap in snap_candidates(edate):
        dest = raw_dir / e / snap / fname
        url = f"{BASE}/{e}/data/{snap}/{fname}"
        if dest.exists():
            if (e, snap) not in manifest:
                # HEAD may 404 if the server no longer serves a file we hold;
                # the row then has last_modified="" and the parse stage falls
                # back to the folder date.
                r = session.head(url, timeout=30)
                manifest[(e, snap)] = _manifest_row(e, snap, fname, "cached", r.headers)
            found += 1
        elif url in cache:
            continue
        else:
            r = session.get(url, timeout=30)
            if r.status_code == 200 and looks_like_source(era, r.content):
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(r.content)
                manifest[(e, snap)] = _manifest_row(e, snap, fname, "downloaded", r.headers)
                found += 1
            else:
                if certifiable:
                    # future report dates of an ongoing count are not permanent misses
                    cache.add(url)
                continue
        # snapshot exists -> also fetch its psov where the summary lacks the split
        if e in PSOV_ELECTIONS:
            _fetch_psov(session, e, snap, raw_dir, cache, certifiable)
    return found


class PoliteSession:
    """requests.Session wrapper with a fixed delay before every request."""

    def __init__(self, session, delay: float = DELAY):
        self._session = session
        self._delay = delay

    def get(self, url, **kw):
        time.sleep(self._delay)
        return self._session.get(url, **kw)

    def head(self, url, **kw):
        time.sleep(self._delay)
        return self._session.head(url, **kw)


def stage_fetch(data_dir: Path, raw_dir: Path, eras: tuple[str, ...]) -> None:
    (data_dir / "pipeline").mkdir(parents=True, exist_ok=True)
    import requests
    from requests.adapters import HTTPAdapter, Retry

    from sfcount.inventory import load_elections

    raw_session = requests.Session()
    raw_session.headers.update(UA)
    # ~2000 requests per cold run: ride out transient drops and 5xx blips
    # instead of aborting the stage (it is resumable, but should not need it).
    raw_session.mount("https://", HTTPAdapter(max_retries=Retry(
        total=3, backoff_factor=1.0, status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "HEAD"])))
    session = PoliteSession(raw_session)
    cache = MissCache(raw_dir / "probe_misses.txt")
    manifest = load_manifest(data_dir / "pipeline" / "manifest.csv")
    today = dt.date.today()
    for el in load_elections(data_dir, eras):
        edate = dt.date.fromisoformat(el["election_date"])
        n = fetch_election(session, edate, el["era"], raw_dir, cache, manifest, today)
        cache.save()
        save_manifest(data_dir / "pipeline" / "manifest.csv", manifest)
        print(f"fetch {edate}: {n} snapshots", flush=True)
