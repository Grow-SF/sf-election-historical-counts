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
