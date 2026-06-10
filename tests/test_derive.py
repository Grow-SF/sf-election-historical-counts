import csv

from sfcount.derive import derive_election, stage_derive


def row(snap, rdt, total, edate="2024-11-05", name="Test General Election", parser="era_c_xml"):
    return {
        "election_date": edate, "election_name": name, "snapshot": snap,
        "report_datetime": rdt, "ballots_counted_total": str(total),
        "ballots_vbm": "", "ballots_election_day": "",
        "registered_voters": "1000", "parser": parser, "datetime_source": "header",
    }


def test_derive_election_crossing_and_night_pct():
    rows = [
        row("20241105_1", "2024-11-05T20:30:00", 500),
        row("20241106", "2024-11-06T16:00:00", 800),
        row("20241107", "2024-11-07T16:00:00", 901),   # 901 >= 0.9 * 1000
        row("20241110", "2024-11-10T16:00:00", 1000),
    ]
    d = derive_election("2024-11-05", rows)
    assert d["final_ballots"] == 1000
    assert d["n_reports"] == 4
    assert d["date_90pct"] == "2024-11-07"
    assert d["days_to_90pct"] == 2
    assert d["pct_on_election_night"] == 50.0


def test_derive_election_night_includes_post_midnight_releases():
    rows = [
        row("20241105_1", "2024-11-05T20:30:00", 400),
        row("20241105_4", "2024-11-06T01:30:00", 600),  # after midnight, still "night"
        row("20241112", "2024-11-12T16:00:00", 1000),
    ]
    d = derive_election("2024-11-05", rows)
    assert d["pct_on_election_night"] == 60.0


def test_derive_election_single_report():
    rows = [row("20241110", "2024-11-10T16:00:00", 100)]
    d = derive_election("2024-11-05", rows)
    assert d["days_to_90pct"] == 5
    assert d["pct_on_election_night"] == 0.0


def test_stage_derive_excludes_archival(tmp_path):
    cols = ["election_date", "election_name", "snapshot", "report_datetime",
            "ballots_counted_total", "ballots_vbm", "ballots_election_day",
            "registered_voters", "parser", "datetime_source"]
    rows = [
        row("wb1", "2012-11-11T16:28:21", 325298, edate="2012-11-06", parser="archival"),
        row("20241105_1", "2024-11-05T20:30:00", 950),
        row("20241108", "2024-11-08T16:00:00", 1000),
    ]
    with open(tmp_path / "sf_count_timeline.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    stage_derive(tmp_path)
    with open(tmp_path / "sf_days_to_90.csv", newline="") as f:
        out = list(csv.DictReader(f))
    assert [r["election_date"] for r in out] == ["2024-11-05"]
    assert out[0]["days_to_90pct"] == "0"  # election night already >= 90%
    assert out[0]["pct_on_election_night"] == "95.0"
