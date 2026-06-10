#!/usr/bin/env python3
"""Bake the visualization dataset for viz/ from the three committed CSVs.

Output: viz/src/data/elections.json — one record per election with:
- per-release trajectory points (days since 8 PM election night, % of final)
- days-to-threshold for thresholds 50..99 (exact for modern data; for
  archival elections a value is only emitted when a capture brackets it,
  with `bound: true` marking "crossed at or before this day")
- election-night share, VBM share, registration, certified final
"""
import csv
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "viz" / "src" / "data" / "elections.json"
THRESHOLDS = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 98, 99]

KIND_RULES = [("Primary", "Primary"), ("Recall", "Recall"), ("Special", "Special"),
              ("Municipal", "Municipal"), ("General", "General")]


def kind_for(name: str) -> str:
    for kw, kind in KIND_RULES:
        if kw in name:
            return kind
    return "Special"


def d_axis(report_dt: dt.datetime, edate: dt.date) -> float:
    anchor = dt.datetime.combine(edate, dt.time(20, 0))
    return max(0.0, round((report_dt - anchor).total_seconds() / 86400, 2))


def pct(part, total):
    return round(100 * part / total, 1)


def night_total(rows, edate):
    """Max total among election-night releases (snapshot named for election
    day, stamped no later than the following day)."""
    prefix = edate.strftime("%Y%m%d")
    vals = [r["total"] for r in rows
            if r.get("snap", "").startswith(prefix)
            and r["dt"].date() <= edate + dt.timedelta(days=1)]
    return max(vals, default=None)


def thresholds_for(rows, final, edate, archival: bool):
    """days-to-threshold. For archival (sparse) data, only report a crossing
    when we actually observe it, and mark it as an upper bound unless the
    preceding observation is < threshold (which pins the crossing day)."""
    out = {}
    rows = sorted(rows, key=lambda r: r["dt"])
    for t in THRESHOLDS:
        cut = t / 100 * final
        cross_i = next((i for i, r in enumerate(rows) if r["total"] >= cut), None)
        if cross_i is None:
            continue
        days = (rows[cross_i]["dt"].date() - edate).days
        if not archival:
            out[str(t)] = {"days": days, "bound": False}
        else:
            pinned = cross_i > 0 and rows[cross_i - 1]["total"] < cut \
                and (rows[cross_i]["dt"].date() - rows[cross_i - 1]["dt"].date()).days <= 2
            out[str(t)] = {"days": days, "bound": not pinned}
    return out


def main():
    elections = {}

    # ---- modern, exact (2015-present)
    with open(ROOT / "data" / "sf_count_timeline.csv", newline="") as f:
        timeline = [r for r in csv.DictReader(f) if r["parser"] != "archival"]
    by = {}
    for r in timeline:
        by.setdefault(r["election_date"], []).append(r)
    today = dt.date.today()
    for e, rs in by.items():
        edate = dt.date.fromisoformat(e)
        rows = sorted(
            ({"dt": dt.datetime.fromisoformat(r["report_datetime"]),
              "total": int(r["ballots_counted_total"]),
              "vbm": int(r["ballots_vbm"]) if r["ballots_vbm"] else None,
              "ed": int(r["ballots_election_day"]) if r["ballots_election_day"] else None,
              "snap": r["snapshot"]}
             for r in rs), key=lambda r: r["dt"])
        final = max(r["total"] for r in rows)
        fin = max(rows, key=lambda r: r["total"])
        night = night_total(rows, edate)
        elections[e] = {
            "id": e,
            "name": rs[0]["election_name"],
            "kind": kind_for(rs[0]["election_name"]),
            "year": edate.year,
            "final": final,
            "registered": int(rs[0]["registered_voters"]),
            "source": "exact",
            "provisional": (today - edate).days <= 32,
            "nReports": len(rows),
            "nightPct": pct(night, final) if night is not None else None,
            "vbmShare": pct(fin["vbm"], fin["total"]) if fin["vbm"] else None,
            "pts": [[d_axis(r["dt"], edate), pct(r["total"], final),
                     pct(r["vbm"], final) if r["vbm"] is not None else None,
                     pct(r["ed"], final) if r["ed"] is not None else None]
                    for r in rows],
            "thresholds": thresholds_for(rows, final, edate, archival=False),
        }

    # ---- archival, sparse (2002-2014)
    with open(ROOT / "data" / "sf_archival_canvass_points.csv", newline="") as f:
        arch = list(csv.DictReader(f))
    aby = {}
    for r in arch:
        aby.setdefault(r["election_date"], []).append(r)
    # night shares only known where an election-night observation exists
    for e, rs in aby.items():
        edate = dt.date.fromisoformat(e)
        rows = sorted(
            ({"dt": dt.datetime.fromisoformat(r["observed_at"]),
              "total": int(r["ballots_counted_total"]),
              "vbm": int(r["ballots_vbm"]) if r["ballots_vbm"] else None,
              "ed": int(r["ballots_election_day"]) if r["ballots_election_day"] else None,
              "snap": ""}
             for r in rs), key=lambda r: r["dt"])
        final = int(rs[0]["certified_final"])
        cutoff = dt.datetime.combine(edate + dt.timedelta(days=1), dt.time(6, 0))
        night_rows = [r for r in rows if r["dt"] <= cutoff]
        night = max((r["total"] for r in night_rows), default=None)
        fin = max(rows, key=lambda r: r["total"])
        elections[e] = {
            "id": e,
            "name": rs[0]["election_name"],
            "kind": kind_for(rs[0]["election_name"]),
            "year": edate.year,
            "final": final,
            "registered": int(rs[0]["registered_voters"]) if rs[0]["registered_voters"] else None,
            "source": "archival",
            "provisional": False,
            "nReports": len(rows),
            "nightPct": pct(night, final) if night is not None else None,
            "vbmShare": pct(fin["vbm"], fin["total"]) if fin["vbm"] else None,
            "pts": [[d_axis(r["dt"], edate), pct(r["total"], final),
                     pct(r["vbm"], final) if r["vbm"] is not None else None,
                     pct(r["ed"], final) if r["ed"] is not None else None]
                    for r in rows],
            "thresholds": thresholds_for(rows, final, edate, archival=True),
        }

    out = sorted(elections.values(), key=lambda e: e["id"])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=1))
    print(f"{len(out)} elections -> {OUT}")
    n_arch = sum(1 for e in out if e["source"] == "archival")
    print(f"  exact: {len(out) - n_arch}, archival: {n_arch}")

    # ---- absentee/VBM share series, 1964-2026
    hist = []
    with open(ROOT / "data" / "sf_turnout_history_1960_2002.csv", newline="") as f:
        for r in csv.DictReader(f):
            if r["absentee"] in ("n/a", ""):
                continue
            m, d, y = r["date"].split("/")
            year = int(y) + (1900 if int(y) >= 60 else 2000)
            share = 100 * int(r["absentee"].replace(",", "")) / int(r["ballots_cast"].replace(",", ""))
            hist.append({"date": f"{year}-{m}-{d}", "share": round(share, 1),
                         "source": "doe-turnout-history"})
    # certified splits recovered from SoS SOVs / DOE SOV spreadsheets /
    # legacy result pages (fills 2002-2014); preferred over archival page reads
    certified = {}
    with open(ROOT / "data" / "sf_vbm_share_sos.csv", newline="") as f:
        for r in csv.DictReader(f):
            certified[r["election_date"]] = float(r["vbm_share_pct"])
    for date, share in certified.items():
        hist.append({"date": date, "share": share, "source": "certified-sov"})
    for e in out:
        if e["vbmShare"] is not None and e["id"] not in certified:
            hist.append({"date": e["id"], "share": e["vbmShare"], "source": e["source"]})
    # one share per election: certified beats the 2002 turnout-history row too
    dedup = {}
    for h in sorted(hist, key=lambda h: (h["date"], h["source"] != "certified-sov")):
        dedup.setdefault(h["date"], h)
    hist = list(dedup.values())
    hist.sort(key=lambda h: h["date"])
    H = OUT.parent / "vbm_history.json"
    H.write_text(json.dumps(hist, indent=1))
    print(f"{len(hist)} VBM-share points -> {H}")

    # ---- election-night floor: the non-absentee (precinct) share of the
    # certified total. Precinct ballots were reported on election night, so
    # this bounds the night share from below - tightest exactly where no
    # canvass data survives (validated <= actual in all 20 known cases).
    floor = {}
    with open(ROOT / "data" / "sf_turnout_history_1960_2002.csv", newline="") as f:
        for r in csv.DictReader(f):
            if r["absentee"] in ("n/a", ""):
                continue
            m, d, y = r["date"].split("/")
            year = int(y) + (1900 if int(y) >= 60 else 2000)
            date = f"{year}-{m}-{d}"
            total = int(r["ballots_cast"].replace(",", ""))
            prec = int(r["precinct"].replace(",", ""))
            floor[date] = {"date": date, "floorPct": round(100 * prec / total, 1),
                           "source": "doe-turnout-history"}
    with open(ROOT / "data" / "sf_vbm_share_sos.csv", newline="") as f:
        for r in csv.DictReader(f):
            floor[r["election_date"]] = {
                "date": r["election_date"],
                "floorPct": round(100 * int(r["ballots_polling"]) / int(r["ballots_total"]), 1),
                "source": "certified-sov"}
    for e in out:
        if e["vbmShare"] is not None and e["id"] not in floor:
            floor[e["id"]] = {"date": e["id"], "floorPct": round(100 - e["vbmShare"], 1),
                              "source": e["source"]}
    fl = sorted(floor.values(), key=lambda x: x["date"])
    F = OUT.parent / "night_floor.json"
    F.write_text(json.dumps(fl, indent=1))
    print(f"{len(fl)} night-floor points -> {F}")


if __name__ == "__main__":
    main()
