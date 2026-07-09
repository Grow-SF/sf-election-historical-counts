#!/usr/bin/env python3
"""Build data/exports/sf_elections_consolidated.csv — one row per SF election
(1849-present) with registration, total turnout, election-night count, and the
election-day / vote-by-mail split, each value paired with its source citation.

Built to share with the SF Department of Elections. Every value is drawn from
the repo's arbitrated datasets (never recomputed here); source strings are the
per-row citations, compacted to their leading clause — the full verbatim
citations live in the underlying data/*.csv files and docs/sources.md.

Do not edit the output by hand — re-run this script instead.
"""
import csv
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "data" / "exports" / "sf_elections_consolidated.csv"

DOE_TABLE_DATE_FIXES = {"2001-12-10": "2001-12-11", "1899-12-02": "1899-12-29"}

SRC_LABELS = {
    "doe-turnout-table": "SF Dept. of Elections historical turnout table (1899-2019)",
    "doe-turnout-history": "SF Dept. of Elections turnout history (1960-2002)",
    "muni-registrar": "SF Municipal Reports, Registrar of Voters tables",
    "sov-bluebook": "CA Statement of Vote / Blue Book",
    "exact": "SF Dept. of Elections per-release certified results",
    "archival": "recovered canvass records (data/sf_archival_canvass_points.csv)",
    "reused-registration": "nearest general's registration, reused per era registration law (approximate)",
}


def compact(s, cap=200):
    """First clause of a long citation: up to the first '; ' or ' - '/' — '."""
    if not s:
        return ""
    s = " ".join(s.split())
    for sep in ("; ", " — ", " - "):
        i = s.find(sep)
        if 0 < i < cap:
            s = s[:i]
            break
    s = s[:cap].strip()
    if s.count("(") > s.count(")"):  # don't leave a clause-cut paren dangling
        s = s[:s.rfind("(")].strip().rstrip(",")
    return s


def main():
    # master list: every election
    master = list(csv.DictReader(open(ROOT / "data" / "elections_master.csv")))

    # registration + (fallback) total: the arbitrated turnout series
    turnout = {p["date"]: p for p in
               json.load(open(ROOT / "packages" / "data" / "turnout_history.json"))}

    # certified finals + their citations
    elections = {e["id"]: e for e in
                 json.load(open(ROOT / "packages" / "data" / "elections.json"))}
    final_src = {}
    for rec in json.load(open(ROOT / "packages" / "data" / "sources.json")):
        fs = rec.get("finalSource")
        if rec.get("id") and fs:
            final_src.setdefault(rec["id"], fs)

    # ballots-only finals (no registration) from the turnout source files
    ballots_only = {}
    for fn in ("sf_turnout_pre1899.csv", "sf_turnout_1891_1907.csv",
               "sf_turnout_registrar_1899_1916.csv"):
        for r in csv.DictReader(open(ROOT / "data" / fn)):
            if r["ballots_cast"]:
                ballots_only.setdefault(
                    r["election_date"],
                    (int(r["ballots_cast"]), compact(r["source"])))

    # night counts: archival canvass observations within the E+1 06:00 cutoff
    night = {}
    for r in csv.DictReader(open(ROOT / "data" / "sf_archival_canvass_points.csv")):
        d = r["election_date"]
        edate = dt.date.fromisoformat(d)
        obs = dt.datetime.fromisoformat(r["observed_at"])
        if obs > dt.datetime.combine(edate + dt.timedelta(days=1), dt.time(6, 0)):
            continue
        total = int(r["ballots_counted_total"])
        if d not in night or total > night[d][0]:
            night[d] = (total, compact(r["source_url"]))
    # ...and the modern per-release night totals
    by_date = {}
    for r in csv.DictReader(open(ROOT / "data" / "sf_count_timeline.csv")):
        if r["parser"] == "archival":
            continue
        by_date.setdefault(r["election_date"], []).append(r)
    modern_split = {}
    for d, rs in by_date.items():
        edate = dt.date.fromisoformat(d)
        cutoff = dt.datetime.combine(edate + dt.timedelta(days=1), dt.time(6, 0))
        nrows = [r for r in rs
                 if dt.datetime.fromisoformat(r["report_datetime"]) <= cutoff]
        if nrows:
            best = max(nrows, key=lambda r: int(r["ballots_counted_total"]))
            night[d] = (int(best["ballots_counted_total"]),
                        f"SF Dept. of Elections results release {best['snapshot']} "
                        f"(reported {best['report_datetime']})")
        fin = max(rs, key=lambda r: int(r["ballots_counted_total"]))
        if fin["ballots_vbm"] or fin["ballots_election_day"]:
            modern_split[d] = (fin["ballots_election_day"], fin["ballots_vbm"],
                               "SF Dept. of Elections per-release certified results "
                               f"(final release {fin['snapshot']})")

    # election-day / VBM splits, most-authoritative first
    split = {}
    for r in csv.DictReader(open(ROOT / "data" / "sf_turnout_history_1960_2002.csv")):
        m, dd, y = r["date"].split("/")
        y = int(y); y += 1900 if y > 26 else 2000
        d = f"{y}-{int(m):02d}-{int(dd):02d}"
        if r["absentee"] not in ("", "n/a"):
            eday = r["precinct"].replace(",", "")
            vbm = r["absentee"].replace(",", "")
            split[d] = (eday, vbm, SRC_LABELS["doe-turnout-history"])
    for r in csv.DictReader(open(ROOT / "data" / "sf_turnout_history_doe_1899_2019.csv")):
        d = DOE_TABLE_DATE_FIXES.get(r["election_date"], r["election_date"])
        if r["precinct"] not in ("", "n/a"):
            split[d] = (r["precinct"], r["mail"], SRC_LABELS["doe-turnout-table"])
    for r in csv.DictReader(open(ROOT / "data" / "sf_vbm_share_sos.csv")):
        split[r["election_date"]] = (r["ballots_polling"], r["ballots_absentee"],
                                     compact(r["source_url"]))
    split.update(modern_split)

    OUT.parent.mkdir(exist_ok=True)
    with open(OUT, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "election_type", "registration", "total_turnout",
                    "night_of_count", "eday_turnout", "vbm_turnout",
                    "registration_source", "total_turnout_source",
                    "night_of_count_source", "eday_turnout_source",
                    "vbm_turnout_source"])
        n_reg = n_tot = n_night = n_split = 0
        for m in sorted(master, key=lambda r: r["election_date"]):
            d = m["election_date"]
            tp = turnout.get(d)
            e = elections.get(d)

            reg = reg_s = ""
            if tp:
                reg = tp["registered"]
                reg_s = compact(tp.get("cite", "")) or SRC_LABELS.get(
                    tp["source"], tp["source"])
                if tp["source"] == "reused-registration":
                    reg_s += (" [reused from the nearest general per era"
                              " registration law; approximate]")

            tot = tot_s = ""
            if e and e.get("final"):
                tot = e["final"]
                tot_s = compact(final_src.get(d, "")) or \
                    SRC_LABELS.get(e.get("source", ""), "")
            elif tp:
                tot = tp["ballots"]
                tot_s = compact(tp.get("cite", "")) or SRC_LABELS.get(
                    tp["source"], tp["source"])
            elif d in ballots_only:
                tot, tot_s = ballots_only[d]

            nt = nt_s = ""
            if d in night:
                nt, nt_s = night[d]
                if e and e.get("nightPartial"):
                    nt_s += " [partial or contest-sum floor - a lower bound]"

            ed = vb = sp_s = ""
            if d in split:
                ed, vb, sp_s = split[d]
                ed = "" if ed in ("n/a",) else ed
                vb = "" if vb in ("n/a",) else vb

            n_reg += reg != ""; n_tot += tot != ""
            n_night += nt != ""; n_split += vb != ""
            w.writerow([d, m["kind"], reg, tot, nt, ed, vb,
                        reg_s, tot_s, nt_s,
                        sp_s if ed else "", sp_s if vb else ""])

    print(f"{len(master)} elections -> {OUT}")
    print(f"  registration: {n_reg} · total: {n_tot} · night: {n_night} · vbm split: {n_split}")


if __name__ == "__main__":
    main()
