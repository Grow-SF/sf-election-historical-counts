import datetime as dt
from pathlib import Path

from sfcount.fetch import (
    MissCache, http_date_to_pacific_iso, snap_candidates,
    fetch_election, load_manifest, looks_like_source, save_manifest,
)

XML = b'\xef\xbb\xbf<?xml version="1.0"?><Report></Report>'
TSV = b"CONTEST_ID\tTOTAL\nx\ty\n"


class FakeResponse:
    def __init__(self, status_code=404, content=b"", headers=None):
        self.status_code = status_code
        self.content = content
        self.headers = headers or {}


class FakeSession:
    def __init__(self, responses):
        self.responses = responses
        self.calls = []

    def get(self, url, timeout=None):
        self.calls.append(("GET", url))
        return self.responses.get(url, FakeResponse())

    def head(self, url, timeout=None):
        self.calls.append(("HEAD", url))
        return self.responses.get(url, FakeResponse())


def test_looks_like_source():
    assert looks_like_source("C", XML)
    assert looks_like_source("B", TSV)
    assert not looks_like_source("C", b"<html>soft 404</html>")
    assert not looks_like_source("B", b"<html>soft 404</html>")


def test_fetch_election_downloads_and_records_last_modified(tmp_path):
    edate = dt.date(2024, 11, 5)
    base = "https://www.sfelections.org/results/20241105/data"
    session = FakeSession({
        f"{base}/20241105_1/summary.xml": FakeResponse(
            200, XML, {"Last-Modified": "Wed, 06 Nov 2024 04:41:41 GMT"}),
        f"{base}/20241108/summary.xml": FakeResponse(
            200, XML, {"Last-Modified": "Fri, 08 Nov 2024 23:45:18 GMT"}),
    })
    cache = MissCache(tmp_path / "misses.txt")
    manifest = {}
    n = fetch_election(session, edate, "C", tmp_path / "raw", cache, manifest,
                       today=dt.date(2026, 6, 9))
    assert n == 2
    assert (tmp_path / "raw/20241105/20241105_1/summary.xml").read_bytes() == XML
    assert manifest[("20241105", "20241105_1")]["last_modified"] == "2024-11-05T20:41:41"
    assert manifest[("20241105", "20241108")]["status"] == "downloaded"
    # 40 probes missed; election is long past, so all are cached as permanent
    assert len(cache.urls) == 40


def test_fetch_election_ongoing_election_does_not_cache_misses(tmp_path):
    edate = dt.date(2026, 6, 2)
    session = FakeSession({})
    cache = MissCache(tmp_path / "misses.txt")
    fetch_election(session, edate, "C", tmp_path / "raw", cache, {},
                   today=dt.date(2026, 6, 9))  # within edate + 35 days
    assert len(cache.urls) == 0


def test_fetch_election_skips_existing_and_recovers_header(tmp_path):
    edate = dt.date(2024, 11, 5)
    dest = tmp_path / "raw/20241105/20241108/summary.xml"
    dest.parent.mkdir(parents=True)
    dest.write_bytes(XML)
    url = "https://www.sfelections.org/results/20241105/data/20241108/summary.xml"
    session = FakeSession({
        url: FakeResponse(200, b"", {"Last-Modified": "Fri, 08 Nov 2024 23:45:18 GMT"}),
    })
    cache = MissCache(tmp_path / "misses.txt")
    cache.urls = {  # everything else already known-missed
        u for u in (
            f"https://www.sfelections.org/results/20241105/data/{s}/summary.xml"
            for s in snap_candidates(edate)) if not u.endswith("/20241108/summary.xml")}
    manifest = {}
    fetch_election(session, edate, "C", tmp_path / "raw", cache, manifest,
                   today=dt.date(2026, 6, 9))
    # existing file was not re-downloaded; HEAD recovered its Last-Modified
    assert ("GET", url) not in session.calls
    assert ("HEAD", url) in session.calls
    assert manifest[("20241105", "20241108")]["last_modified"] == "2024-11-08T15:45:18"
    assert manifest[("20241105", "20241108")]["status"] == "cached"


def test_manifest_roundtrip(tmp_path):
    manifest = {("20241105", "20241108"): {
        "election": "20241105", "snapshot": "20241108", "filename": "summary.xml",
        "status": "downloaded", "last_modified": "2024-11-08T15:45:18"}}
    save_manifest(tmp_path / "manifest.csv", manifest)
    assert load_manifest(tmp_path / "manifest.csv") == manifest
    assert load_manifest(tmp_path / "missing.csv") == {}


def test_fetch_election_downloads_psov_for_2019(tmp_path):
    edate = dt.date(2019, 11, 5)
    base = "https://www.sfelections.org/results/20191105/data"
    session = FakeSession({
        f"{base}/20191108/summary.xml": FakeResponse(
            200, XML, {"Last-Modified": "Fri, 08 Nov 2019 23:35:55 GMT"}),
        f"{base}/20191108/20191108_psov.xml": FakeResponse(200, XML, {}),
    })
    cache = MissCache(tmp_path / "misses.txt")
    fetch_election(session, edate, "C", tmp_path / "raw", cache, {},
                   today=dt.date(2026, 6, 9))
    # psov fetched alongside the snapshot whose summary was found, and never
    # probed for snapshots whose summary was missing
    assert (tmp_path / "raw/20191105/20191108/20191108_psov.xml").read_bytes() == XML
    assert len([c for c in session.calls if "psov" in c[1]]) == 1
    # summary misses still cached (41 of 42 candidates missed)
    assert len([u for u in cache.urls if "summary.xml" in u]) == 41


def test_snap_candidates_night_releases_then_daily():
    snaps = list(snap_candidates(dt.date(2024, 11, 5)))
    assert snaps[:6] == [f"20241105_{n}" for n in range(1, 7)]
    assert snaps[6] == "20241105"          # election day itself
    assert snaps[7] == "20241106"
    assert snaps[-1] == "20241210"         # election day + 35
    assert len(snaps) == 6 + 36


def test_http_date_to_pacific_iso():
    # PST (UTC-8): the Nov 2024 election-night first release
    assert http_date_to_pacific_iso("Wed, 06 Nov 2024 04:41:41 GMT") == "2024-11-05T20:41:41"
    # PDT (UTC-7)
    assert http_date_to_pacific_iso("Tue, 11 Jun 2024 00:30:00 GMT") == "2024-06-10T17:30:00"


def test_miss_cache_roundtrip(tmp_path):
    path = tmp_path / "probe_misses.txt"
    cache = MissCache(path)
    assert "http://x/a" not in cache
    cache.add("http://x/a")
    cache.add("http://x/b")
    cache.save()
    reloaded = MissCache(path)
    assert "http://x/a" in reloaded and "http://x/b" in reloaded
