import datetime as dt
from pathlib import Path

from sfcount.fetch import MissCache, http_date_to_pacific_iso, snap_candidates


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
