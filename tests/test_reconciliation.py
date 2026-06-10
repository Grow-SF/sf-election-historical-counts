"""Migration gate: the structured-source pipeline must reproduce the archive's
PDF-derived counts exactly. Run after the live fetch: uv run pytest -m migration
"""
import csv
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
COUNT_COLS = ["ballots_counted_total", "registered_voters"]
SPLIT_COLS = ["ballots_vbm", "ballots_election_day"]

# The archive's PDF parser read the FIRST party block (Democratic) of the
# Dominion-era presidential-primary summaries instead of the citywide totals,
# so every archive row for these two elections is wrong. The new pipeline's
# citywide figures are verified against the DOE results pages:
# 2020-03-03 -> 305,184 of 503,899 (60.56%); 2024-03-05 -> 233,465 (46.61%).
KNOWN_ARCHIVE_ERRORS = {"2020-03-03", "2024-03-05"}


def load(path):
    with open(path, newline="") as f:
        return {(r["election_date"], r["snapshot"]): r for r in csv.DictReader(f)}


@pytest.mark.migration
def test_counts_match_archive():
    new = load(ROOT / "data/sf_count_timeline.csv")
    old = load(ROOT / "sf-long-count-archive/sf_count_timeline.csv")
    missing, mismatches = [], []
    for key, o in old.items():
        if key[0] in KNOWN_ARCHIVE_ERRORS:
            continue  # archive values are party-block, not citywide; see above
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
def test_presidential_primaries_corrected_to_citywide_totals():
    new = load(ROOT / "data/sf_count_timeline.csv")
    finals = {}
    for (e, _), r in new.items():
        if e in KNOWN_ARCHIVE_ERRORS:
            finals[e] = max(finals.get(e, 0), int(r["ballots_counted_total"]))
    # citywide ballots cast, verified on the DOE results pages
    assert finals == {"2020-03-03": 305184, "2024-03-05": 233465}


# The DOE published no psov for these three snapshots (verified 404 live,
# 2026-06-09): the 2nd and 3rd election-night releases and the Nov 25 report.
PSOV_UNPUBLISHED = {"20191105_2", "20191105_3", "20191125"}


@pytest.mark.migration
def test_2019_rows_gained_the_split_the_pdfs_never_had():
    new = load(ROOT / "data/sf_count_timeline.csv")
    rows = {snap: r for (e, snap), r in new.items() if e == "2019-11-05"}
    assert len(rows) >= 13  # the archive had 13 split-less Nov 2019 rows
    for snap, r in rows.items():
        if snap in PSOV_UNPUBLISHED:
            assert r["parser"] == "era_c_xml"
            assert r["ballots_vbm"] == "" and r["ballots_election_day"] == ""
        else:
            assert r["parser"] == "era_c_xml+psov", f"{snap}: no psov recovery"
            assert r["ballots_vbm"] != "" and r["ballots_election_day"] != ""
