import csv
import datetime as dt
from pathlib import Path

from sfcount.inventory import era_for, extract_elections, load_elections, write_inventory

FIXTURES = Path(__file__).parent / "fixtures"


def test_era_for():
    assert era_for(dt.date(2024, 11, 5)) == "C"
    assert era_for(dt.date(2019, 1, 1)) == "C"
    assert era_for(dt.date(2018, 11, 6)) == "B"
    assert era_for(dt.date(2008, 1, 1)) == "B"
    assert era_for(dt.date(2007, 12, 31)) == "A"
    assert era_for(dt.date(2000, 11, 7)) == "A"


def test_extract_elections_from_real_page():
    html = (FIXTURES / "sfgov_results.html").read_text(encoding="utf-8", errors="replace")
    seen = extract_elections(html)
    assert len(seen) >= 45
    assert seen[dt.date(2024, 11, 5)] == "Consolidated General Election"
    assert dt.date(2000, 11, 7) in seen
    assert min(seen) >= dt.date(2000, 11, 1)


def test_extract_includes_supplemental_elections():
    # Recently-held elections appear on the sf.gov past-results page only
    # after certification; SUPPLEMENTAL covers the gap.
    seen = extract_elections("")
    assert seen[dt.date(2026, 6, 2)] == "Consolidated Statewide Direct Primary Election"


def test_page_listing_overrides_supplemental():
    html = 'June 2, 2026, Renamed Primary Election<'
    assert extract_elections(html)[dt.date(2026, 6, 2)] == "Renamed Primary Election"


def test_write_and_load_roundtrip(tmp_path):
    seen = {
        dt.date(2016, 11, 8): "Consolidated General Election",
        dt.date(2024, 11, 5): "Consolidated General Election",
        dt.date(2001, 11, 6): "Consolidated Municipal Election",
    }
    write_inventory(seen, tmp_path)
    rows = list(csv.DictReader((tmp_path / "elections.csv").open()))
    assert [r["era"] for r in rows] == ["A", "B", "C"]  # sorted by date
    assert load_elections(tmp_path, eras=("B", "C")) == rows[1:]
