"""Stage 5: per-election days-to-90% statistics."""
import csv
import datetime as dt
from pathlib import Path

DERIVE_COLS = ["election_date", "election_name", "final_ballots", "n_reports",
               "date_90pct", "days_to_90pct", "pct_on_election_night"]


def derive_election(election_date: str, rows: list[dict]) -> dict:
    rows = sorted(rows, key=lambda r: (r["report_datetime"], r["snapshot"]))
    edate = dt.date.fromisoformat(election_date)
    final = max(int(r["ballots_counted_total"]) for r in rows)

    # final == max guarantees at least one row crosses 90% of final
    cross = next(r for r in rows if int(r["ballots_counted_total"]) >= 0.9 * final)
    cross_date = dt.datetime.fromisoformat(cross["report_datetime"]).date()

    # "Election night" = releases named for election day, timestamped no later
    # than the following day (the _3/_4 releases land after midnight).
    night = max(
        (int(r["ballots_counted_total"]) for r in rows
         if r["snapshot"].startswith(edate.strftime("%Y%m%d"))
         and dt.datetime.fromisoformat(r["report_datetime"]).date()
         <= edate + dt.timedelta(days=1)),
        default=0)

    return {
        "election_date": election_date,
        "election_name": rows[0]["election_name"],
        "final_ballots": final,
        "n_reports": len(rows),
        "date_90pct": cross_date.isoformat(),
        "days_to_90pct": (cross_date - edate).days,
        "pct_on_election_night": round(100 * night / final, 1),
    }


def stage_derive(data_dir: Path) -> None:
    with open(data_dir / "sf_count_timeline.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    by_election: dict[str, list[dict]] = {}
    for r in rows:
        if r["parser"] == "archival":
            continue  # sparse captures cannot support days-to-90
        by_election.setdefault(r["election_date"], []).append(r)

    out = [derive_election(e, rs) for e, rs in sorted(by_election.items())]
    with open(data_dir / "sf_days_to_90.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=DERIVE_COLS)
        w.writeheader()
        w.writerows(out)
    for r in out:
        print(f"{r['election_date']}  final={r['final_ballots']:>7,}  "
              f"night={r['pct_on_election_night']:>5}%  90% on day {r['days_to_90pct']}",
              flush=True)
