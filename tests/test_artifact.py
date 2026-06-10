import datetime as dt

from sfcount.artifact import (
    build_artifact_data, d_axis, kind_for, regenerate, render_js,
)


def test_kind_for_matches_archive_classification():
    assert kind_for("Consolidated Statewide Direct Primary Election") == "Primary"
    assert kind_for("Special Recall Election") == "Recall"          # Recall before Special
    assert kind_for("California Gubernatorial Recall Election") == "Recall"
    assert kind_for("Consolidated Special Municipal Election") == "Special"  # Special before Municipal
    assert kind_for("Special General Election") == "Special"        # Special before General
    assert kind_for("Consolidated Municipal Election") == "Municipal"
    assert kind_for("Consolidated General Election") == "General"


def test_d_axis_days_since_8pm_election_night():
    edate = dt.date(2024, 11, 5)
    assert d_axis(dt.datetime(2024, 11, 5, 20, 41, 0), edate) == 0.03
    assert d_axis(dt.datetime(2024, 11, 8, 15, 45, 0), edate) == 2.82
    # pre-8pm timestamps (folder-date fallbacks) clamp to 0
    assert d_axis(dt.datetime(2024, 11, 5, 0, 0, 0), edate) == 0.0


def timeline_row(snap, rdt, total, vbm, ed, edate="2024-11-05",
                 name="Consolidated General Election", parser="era_c_xml"):
    return {
        "election_date": edate, "election_name": name, "snapshot": snap,
        "report_datetime": rdt, "ballots_counted_total": str(total),
        "ballots_vbm": str(vbm) if vbm is not None else "",
        "ballots_election_day": str(ed) if ed is not None else "",
        "parser": parser,
    }


D90 = [{"election_date": "2024-11-05", "election_name": "Consolidated General Election",
        "final_ballots": "1000", "n_reports": "2", "date_90pct": "2024-11-08",
        "days_to_90pct": "3", "pct_on_election_night": "50.0"}]


def test_build_artifact_data():
    timeline = [
        timeline_row("20241105_1", "2024-11-05T20:41:00", 500, 500, 0),
        timeline_row("20241108", "2024-11-08T15:45:00", 1000, None, None),
        timeline_row("wb1", "2012-11-11T16:28:21", 325298, 1, 2,
                     edate="2012-11-06", parser="archival"),
    ]
    data = build_artifact_data(timeline, D90, today=dt.date(2026, 6, 9))
    assert len(data) == 1  # archival 2012 election excluded (no d90 row)
    e = data[0]
    assert e["id"] == "2024-11-05"
    assert e["kind"] == "General"
    assert e["final"] == 1000
    assert e["night"] == 50.0
    assert e["d90"] == 3
    assert e["prov"] is False  # long since certified
    assert e["pts"] == [[0.03, 50.0, 50.0, 0.0], [2.82, 100.0, None, None]]


def test_build_artifact_data_provisional_flag():
    timeline = [timeline_row("20241108", "2024-11-08T15:45:00", 1000, 600, 400)]
    data = build_artifact_data(timeline, D90, today=dt.date(2024, 11, 20))
    assert data[0]["prov"] is True  # within 32 days of the election


def test_render_js_nulls_and_shape():
    js = render_js([{"id": "x", "name": "n", "kind": "General", "final": 1,
                     "night": 1.0, "d90": 1, "pts": [[0.0, 1.0, None, None]], "prov": False}])
    assert js.startswith("const E = [")
    assert js.rstrip().endswith("];")
    assert "null" in js and "None" not in js


JSX = """// header
// BEGIN GENERATED DATA
const E = [OLD];
// END GENERATED DATA
function App() {}
"""


def test_regenerate_replaces_between_markers_idempotently(tmp_path):
    path = tmp_path / "viz.jsx"
    path.write_text(JSX)
    data = [{"id": "x", "name": "n", "kind": "General", "final": 1,
             "night": 1.0, "d90": 1, "pts": [], "prov": False}]
    regenerate(path, data)
    once = path.read_text()
    assert "OLD" not in once
    assert '"id": "x"'.replace(" ", "") in once.replace(" ", "")
    assert once.startswith("// header") and once.rstrip().endswith("function App() {}")
    regenerate(path, data)
    assert path.read_text() == once  # idempotent
