#!/usr/bin/env python3
"""Build data/exports/sf_elections_consolidated.csv — one row per SF election
(1849-present) with registration, total turnout, election-night count, and the
election-day / vote-by-mail split, each value paired with its source citation.

The one-file rollup most readers want. Every value is drawn from
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

# the nine elections with no recoverable night count (documented dead ends;
# verbatim quotes in docs/analysis/public-search-log.md and
# docs/research/night-recovery-2026-07-09/)
DEAD_ENDS = {
    "1849-11-13": "documented dead end: no day-after paper existed (the Alta was weekly)",
    "1850-10-07": "documented dead end: E+1 Alta printed outcomes only, no count",
    "1902-08-12": "documented dead end: morning Call printed winners-only delegate lists",
    "1908-05-05": "documented dead end: only printed overnight total exceeds the official final",
    "1909-11-02": "documented dead end: winners conceded on prose pluralities; no returns table printed",
    "1913-09-30": "documented dead end: count finished after the 6 AM cutoff (E+1 daytime count on file)",
    "1944-11-07": "documented dead end: the ELECTION EXTRA printed no SF count (all 18 pages verified)",
    "1972-06-06": "documented dead end: punch-card debut, no overnight figures printed",
    "1994-11-08": "documented dead end: the count crashed; no usable night release survives",
}

# finals that are themselves single-contest floors rather than total-ballot
# counts, detected from the final_source citation text
FLOOR_FINAL_PAT = ("contest floor", "contest-sum", "final floor", "contest total",
                   "top-contest", "Sheriff-contest", "field sum", "largest contest",
                   "ballots sum", "proposition sum", "majority-official")

# floor-class finals whose sources.json citation predates the reclassification
FLOOR_FINAL_EXTRA = {"1864-05-17",   # Sheriff-contest total (operator ruling)
                     "1856-11-04"}   # presidential-contest state-canvass sum

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
    source_ids = set()
    for rec in json.load(open(ROOT / "packages" / "data" / "sources.json")):
        if rec.get("id"):
            source_ids.add(rec["id"])
        fs = rec.get("finalSource")
        if rec.get("id") and fs:
            final_src.setdefault(rec["id"], fs)

    # finals that are single-contest floors, per the reuse file's structured notes
    floor_finals = set()
    for r in csv.DictReader(open(ROOT / "data" /
                                 "sf_turnout_reused_registration_1917_1945.csv")):
        if r["ballots_note"]:
            floor_finals.add(r["election_date"])

    # per-election night-count class (floors/partials are dimmed on the charts)
    night_partial = {e["id"] for e in elections.values() if e.get("nightPartial")}

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
            night[d] = (total, compact(r["source_url"]), r["observed_at"])
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
                        f"(reported {best['report_datetime']})",
                        best["report_datetime"])
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
        w.writerow(["date", "election_type", "level", "election_name",
                    "registration", "registration_basis",
                    "total_turnout", "total_turnout_class", "turnout_pct",
                    "night_of_count", "night_count_class", "night_observed_at",
                    "night_pct_of_final",
                    "eday_turnout", "vbm_turnout",
                    "registration_source", "total_turnout_source",
                    "night_of_count_source", "eday_turnout_source",
                    "vbm_turnout_source", "sources_record_id"])
        n_reg = n_tot = n_night = n_split = 0
        for m in sorted(master, key=lambda r: r["election_date"]):
            d = m["election_date"]
            tp = turnout.get(d)
            e = elections.get(d)

            reg = reg_s = ""
            reg_basis = ""
            if tp:
                reg = tp["registered"]
                reg_s = compact(tp.get("cite", "")) or SRC_LABELS.get(
                    tp["source"], tp["source"])
                reg_basis = ("reused from nearest general (approximate)"
                             if tp["source"] == "reused-registration"
                             else "as recorded for this election")

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
            full_fs = final_src.get(d, "") or tot_s
            if (d in floor_finals or d in FLOOR_FINAL_EXTRA
                    or any(pat in full_fs for pat in FLOOR_FINAL_PAT)):
                tot_class = "single-contest floor (a lower bound on ballots cast)"
            elif ("news-derived" in full_fs or "polled statement" in full_fs
                    or "semi-official" in full_fs.lower()):
                tot_class = "news-derived complete count"
            elif tot:
                tot_class = "certified / official canvass"
            else:
                tot_class = ""
            turnout_pct = (round(100 * int(tot) / int(reg), 1)
                           if tot and reg else "")

            nt = nt_s = nt_at = nt_class = nt_pct = ""
            if d in night:
                nt, nt_s, nt_at = night[d]
                nt_class = ("lower bound (partial or contest-sum floor)"
                            if d in night_partial else "as printed")
                if tot:
                    nt_pct = round(100 * nt / int(tot), 1)
            elif d in DEAD_ENDS:
                nt_s = DEAD_ENDS[d]

            ed = vb = sp_s = ""
            if d in split:
                ed, vb, sp_s = split[d]
                ed = "" if ed in ("n/a",) else ed
                vb = "" if vb in ("n/a",) else vb

            n_reg += reg != ""; n_tot += tot != ""
            n_night += nt != ""; n_split += vb != ""
            w.writerow([d, m["kind"], m["level"], m["description"],
                        reg, reg_basis, tot, tot_class, turnout_pct,
                        nt, nt_class, nt_at, nt_pct, ed, vb,
                        reg_s, tot_s, nt_s,
                        sp_s if ed else "", sp_s if vb else "",
                        d if d in source_ids else ""])

    print(f"{len(master)} elections -> {OUT}")
    print(f"  registration: {n_reg} · total: {n_tot} · night: {n_night} · vbm split: {n_split}")


if __name__ == "__main__":
    main()
