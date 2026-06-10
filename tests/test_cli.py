import csv

from sfcount.cli import main


def test_cli_parse_and_validate_on_fixture_tree(mini_pipeline):
    data, raw = mini_pipeline
    rc = main(["--data-dir", str(data), "--raw-dir", str(raw), "parse"])
    assert rc == 0
    with open(data / "sf_count_timeline.csv", newline="") as f:
        assert len(list(csv.DictReader(f))) == 7
    # the mini tree holds mid-count snapshots, so certified totals don't match:
    # validate must catch that and return nonzero
    rc = main(["--data-dir", str(data), "--raw-dir", str(raw), "validate"])
    assert rc == 1
