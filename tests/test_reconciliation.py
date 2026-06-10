"""Migration gate: the structured-source pipeline must reproduce the archive's
PDF-derived counts exactly. Run after the live fetch: uv run pytest -m migration
"""
import csv
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
COUNT_COLS = ["ballots_counted_total", "registered_voters"]
SPLIT_COLS = ["ballots_vbm", "ballots_election_day"]


def load(path):
    with open(path, newline="") as f:
        return {(r["election_date"], r["snapshot"]): r for r in csv.DictReader(f)}


@pytest.mark.migration
def test_counts_match_archive():
    new = load(ROOT / "data/sf_count_timeline.csv")
    old = load(ROOT / "sf-long-count-archive/sf_count_timeline.csv")
    missing, mismatches = [], []
    for key, o in old.items():
        n = new.get(key)
        if n is None:
            missing.append(key)
            continue
        for col in COUNT_COLS:
            if n[col] != o[col]:
                mismatches.append((key, col, o[col], n[col]))
        for col in SPLIT_COLS:
            # archive blanks (Nov 2019) gain psov-recovered values; non-blanks must match
            if o[col] != "" and n[col] != o[col]:
                mismatches.append((key, col, o[col], n[col]))
    assert not missing, f"archive snapshots absent from new fetch: {missing}"
    assert not mismatches, f"count mismatches vs archive: {mismatches}"


@pytest.mark.migration
def test_2019_rows_gained_the_split_the_pdfs_never_had():
    new = load(ROOT / "data/sf_count_timeline.csv")
    rows = [r for (e, _), r in new.items() if e == "2019-11-05"]
    assert len(rows) >= 13  # the archive had 13 split-less Nov 2019 rows
    for r in rows:
        assert r["parser"] == "era_c_xml+psov", f"{r['snapshot']}: no psov recovery"
        assert r["ballots_vbm"] != "" and r["ballots_election_day"] != ""
