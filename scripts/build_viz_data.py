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
    modern_src = {}

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
        last_dt = max(r["dt"] for r in rows)
        # collapse intra-night releases: cite only the final election-night
        # release, then every later one
        night_cut = dt.datetime.combine(edate + dt.timedelta(days=1), dt.time(6, 0))
        night_releases = [r for r in rows if r["dt"] <= night_cut]
        cite_rows = ([max(night_releases, key=lambda r: r["dt"])] if night_releases else []) \
            + [r for r in rows if r["dt"] > night_cut]
        modern_src[e] = {
            "n": len(rows),
            "obs": [{"date": r["dt"].date().isoformat(),
                     "days": (r["dt"].date() - edate).days,
                     "night": bool(night_releases) and r["dt"] == max(nr["dt"] for nr in night_releases),
                     "total": r["total"],
                     "pct": pct(r["total"], max(x["total"] for x in rows)),
                     "label": "SF Dept. of Elections results release",
                     "citation": (lambda fn: f"per-release summary report, reported {r['dt'].isoformat()} - https://www.sfelections.org/results/{edate.strftime('%Y%m%d')}/data/{r['snap']}/{fn} (validated against certified totals)")("summary.xml" if edate.year >= 2019 else "summary.txt")}
                    for r in cite_rows],
        }
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
        # Dec 1995 runoff: the only night observation is a mid-count partial
        # (339 of 551 precincts, chad-jammed punch cards) - the true
        # end-of-night share was higher; flag so the chart dims it and
        # keeps it out of the trend fit
        # 2007-11-06: ES&S decertification kept every polling-place ballot out of
        # the night release (48,104 absentee/early only) - operational one-off
        night_partial = e in {"1995-12-12", "1976-11-02", "1973-11-06", "1974-06-04", "1978-06-06", "2007-11-06", "1968-11-05", "2008-02-05"}
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
            "nightPartial": night_partial,
            "vbmShare": pct(fin["vbm"], fin["total"]) if fin["vbm"] else None,
            "pts": [[d_axis(r["dt"], edate), pct(r["total"], final),
                     pct(r["vbm"], final) if r["vbm"] is not None else None,
                     pct(r["ed"], final) if r["ed"] is not None else None]
                    for r in rows],
            "thresholds": thresholds_for(rows, final, edate, archival=True),
        }

    EXTRACT_LABEL = {
        "wayback-html": "Wayback Machine capture",
        "chronicle-subscription": "SF Chronicle archive",
        "newsbank-sfpl": "SF Chronicle via NewsBank (SFPL)",
        "newsbank-image-scan": "SF Chronicle page scan (NewsBank/SFPL)",
        "web-news": "contemporary news report (live web)",
    }
    def short_label(r):
        if r["stamp_kind"] == "minutes-stated":
            return "Elections Commission minutes"
        return EXTRACT_LABEL.get(r["extraction"], r["extraction"])
    # per-election citations + short source labels for tooltips
    sources = []
    for e, rs in aby.items():
        edate = dt.date.fromisoformat(e)
        cutoff = dt.datetime.combine(edate + dt.timedelta(days=1), dt.time(6, 0))
        obs = []
        night_best = None
        for r in sorted(rs, key=lambda r: r["observed_at"]):
            o = {"date": r["observed_at"][:10], "days": int(r["days_since_election"]),
                 "total": int(r["ballots_counted_total"]), "pct": float(r["pct_of_final"]),
                 "label": short_label(r), "citation": r["source_url"]}
            obs.append(o)
            if dt.datetime.fromisoformat(r["observed_at"]) <= cutoff:
                if night_best is None or o["total"] > night_best["total"]:
                    night_best = o
        if e in elections:
            elections[e]["nightSrc"] = night_best["label"] if night_best else None
            elections[e]["srcShort"] = obs[0]["label"] if obs else None
        sources.append({"id": e, "name": rs[0]["election_name"], "final": int(rs[0]["certified_final"]),
                        "finalSource": rs[0]["final_source"], "observations": obs})
    for e in elections.values():
        if e["source"] == "exact":
            e["nightSrc"] = "SF Dept. of Elections results release"
            e["srcShort"] = "SF Dept. of Elections results release"
            if not any(s["id"] == e["id"] for s in sources):
                ms = modern_src[e["id"]]
                sources.append({"id": e["id"], "name": e["name"], "final": e["final"],
                    "finalSource": "SF Dept. of Elections certified results",
                    "observations": ms["obs"]})
    sources.sort(key=lambda s: s["id"], reverse=True)
    (OUT.parent / "sources.json").write_text(json.dumps(sources, indent=1))
    print(f"{len(sources)} election source records -> sources.json")

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
    # DOE's official 1899-2019 turnout table (wayback 2023-02-04 capture):
    # gap-fill only - it agrees exactly with every series above where they
    # overlap, and uniquely covers the 2003-2013 municipal elections + the
    # certified 2019-11-05 split (whose PSOVs were never published)
    # the table dates the Dec 2001 runoff "12/10/2001" - a Monday; the runoff
    # was Tuesday Dec 11 and the table's turnout (75,267) matches our
    # certified final for 2001-12-11 exactly
    # the Dec 1975 runoff really was held Thursday December 11, 1975 - the
    # rare non-Tuesday: masthead-verified, the Thu 12/11 Chronicle front page
    # reads "S.F. Picks A Mayor Today" and the Fri 12/12 paper carries the
    # results (Moscone 101,528 / Barbagelata 97,213, 942/942 precincts)
    DOE_TABLE_DATE_FIXES = {"2001-12-10": "2001-12-11"}
    doe_table = []
    with open(ROOT / "data" / "sf_turnout_history_doe_1899_2019.csv", newline="") as f:
        for r in csv.DictReader(f):
            if r["mail"] == "n/a":
                continue
            r["election_date"] = DOE_TABLE_DATE_FIXES.get(r["election_date"], r["election_date"])
            doe_table.append(r)
    have = {h["date"] for h in hist}
    for r in doe_table:
        if r["election_date"] not in have:
            hist.append({"date": r["election_date"],
                         "share": round(100 * int(r["mail"]) / int(r["ballots_cast"]), 1),
                         "source": "doe-turnout-table"})
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
    for r in doe_table:
        if r["election_date"] not in floor:
            floor[r["election_date"]] = {
                "date": r["election_date"],
                "floorPct": round(100 * int(r["precinct"]) / int(r["ballots_cast"]), 1),
                "source": "doe-turnout-table"}
    fl = sorted(floor.values(), key=lambda x: x["date"])
    F = OUT.parent / "night_floor.json"
    F.write_text(json.dumps(fl, indent=1))
    print(f"{len(fl)} night-floor points -> {F}")


if __name__ == "__main__":
    main()
