"""Regenerates the embedded data array in artifact/sf-long-count.jsx."""
import csv
import datetime as dt
import json
from pathlib import Path

BEGIN = "// BEGIN GENERATED DATA"
END = "// END GENERATED DATA"
CERTIFICATION_DAYS = 32  # elections newer than this are provisional

# Order matters: "Special Recall" -> Recall, "Consolidated Special Municipal"
# -> Special, "Special General" -> Special (matches the archive's hand labels).
KIND_RULES = [("Primary", "Primary"), ("Recall", "Recall"), ("Special", "Special"),
              ("Municipal", "Municipal"), ("General", "General")]


def kind_for(name: str) -> str:
    for keyword, kind in KIND_RULES:
        if keyword in name:
            return kind
    return "Special"


def d_axis(report_dt: dt.datetime, election_date: dt.date) -> float:
    """Days since 8:00 PM Pacific on election night, clamped at 0."""
    anchor = dt.datetime.combine(election_date, dt.time(20, 0))
    return max(0.0, round((report_dt - anchor).total_seconds() / 86400, 2))


def _pct(part: str, final: int) -> float | None:
    return None if part == "" else round(100 * int(part) / final, 1)


def build_artifact_data(timeline_rows: list[dict], d90_rows: list[dict],
                        today: dt.date) -> list[dict]:
    by_election: dict[str, list[dict]] = {}
    for r in timeline_rows:
        if r["parser"] != "archival":
            by_election.setdefault(r["election_date"], []).append(r)

    out = []
    for d90 in sorted(d90_rows, key=lambda r: r["election_date"]):
        eid = d90["election_date"]
        edate = dt.date.fromisoformat(eid)
        rows = sorted(by_election[eid],
                      key=lambda r: (r["report_datetime"], r["snapshot"]))
        final = int(d90["final_ballots"])
        pts = [[d_axis(dt.datetime.fromisoformat(r["report_datetime"]), edate),
                round(100 * int(r["ballots_counted_total"]) / final, 1),
                _pct(r["ballots_vbm"], final),
                _pct(r["ballots_election_day"], final)]
               for r in rows]
        out.append({
            "id": eid,
            "name": d90["election_name"],
            "kind": kind_for(d90["election_name"]),
            "final": final,
            "night": float(d90["pct_on_election_night"]),
            "d90": int(d90["days_to_90pct"]),
            "pts": pts,
            "prov": (today - edate).days <= CERTIFICATION_DAYS,
        })
    return out


def render_js(data: list[dict]) -> str:
    entries = ",\n".join(json.dumps(e, separators=(",", ":")) for e in data)
    return f"const E = [{entries}];"


def regenerate(jsx_path: Path, data: list[dict]) -> None:
    src = jsx_path.read_text()
    pre, rest = src.split(BEGIN, 1)
    _, post = rest.split(END, 1)
    jsx_path.write_text(pre + BEGIN + "\n" + render_js(data) + "\n" + END + post)


def stage_artifact(data_dir: Path, jsx_path: Path, today: dt.date | None = None) -> None:
    with open(data_dir / "sf_count_timeline.csv", newline="") as f:
        timeline = list(csv.DictReader(f))
    with open(data_dir / "sf_days_to_90.csv", newline="") as f:
        d90 = list(csv.DictReader(f))
    data = build_artifact_data(timeline, d90, today or dt.date.today())
    regenerate(jsx_path, data)
    print(f"artifact: {len(data)} elections -> {jsx_path}", flush=True)
