#!/usr/bin/env python3
"""Bake the visualization dataset for packages/data/ from the committed data/*.csv
inputs (nine CSVs; plus docs/analysis/public-search-log.md for ledger.json).

Output: packages/data/elections.json — one record per election with:
- per-release trajectory points (days since 8 PM election night, % of final)
- days-to-threshold for thresholds 50..99 (exact for modern data; for
  archival elections a value is only emitted when a capture brackets it,
  with `bound: true` marking "crossed at or before this day")
- election-night share, VBM share, registration, certified final
"""
import csv
import datetime as dt
import json
import re
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "packages" / "data" / "elections.json"
THRESHOLDS = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 98, 99]
# Elections whose count is effectively complete (100% of precincts/tabulators
# reported) and shown as final ahead of the 32-day provisional default.
FORCE_FINAL = {"2026-06-02"}  # CA primary — 100% reporting as of the DOE's June 17 release

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
            "provisional": (today - edate).days <= 32 and e not in FORCE_FINAL,
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
        night_partial = e in {"1995-12-12", "1976-11-02", "1973-11-06", "1974-06-04", "1978-06-06", "2007-11-06", "1968-11-05", "2008-02-05", "2008-06-03", "2010-06-08", "2012-06-05", "1996-03-26", "1992-11-03", "1978-11-07", "1974-11-05", "1980-06-03", "1976-06-08", "1970-06-02", "1968-06-04", "1966-06-07", "1899-11-07", "1903-11-03", "1901-11-05", "1888-11-06", "1884-11-04", "1879-09-03", "2011-11-08", "2002-12-10", "2002-03-05", "2002-11-05", "2000-12-12", "2003-12-09", "2006-11-07", "2003-10-07", "2000-11-07", "1999-11-02", "1998-06-02", "1986-11-04", "1982-06-08", "1977-08-02", "1984-06-05", "1911-11-07", "1912-03-28", "1872-11-05", "1871-10-18", "1875-10-20", "1867-10-16", "1861-09-04", "1877-09-05", "1873-09-03", "1869-09-01", "1945-11-06", "1944-05-16"}
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

    # readers with SFPL cards can open NewsBank pages directly - synthesize
    # ezproxy links from docref IDs / issue labels embedded in citations
    EZPROXY = "https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref="
    docref_file = ROOT / "data" / "newsbank_issue_docrefs.json"
    ISSUE_DOCREFS = json.loads(docref_file.read_text()) if docref_file.exists() else {}

    def link_citation(cite, extraction):
        out = cite
        if "ezproxy" not in out:
            for did in re.findall(r"\((?:docref )?(?:news/)?([0-9A-F]{16})\)", out):
                out += f" · read at SFPL: {EZPROXY}news/{did}"
            m = re.search(r"image doc (v2:[^ ]+)", out)
            if m:
                out += f" · view the page scan at SFPL: {EZPROXY}image/{urllib.parse.quote(m.group(1))}"
            elif extraction == "newsbank-image-scan":
                mi = re.search(r"issue(\d{8})", out)
                ref = ISSUE_DOCREFS.get(mi.group(1)) if mi else None
                if ref:
                    out += f" · view the scanned issue at SFPL (browse to the cited page): {EZPROXY}image/{urllib.parse.quote(ref)}"
        # bare sfchronicle.com article refs -> absolute URLs for the linkifier
        out = re.sub(r"(?<![/.\w])(sfchronicle\.com/[^\s)]+)", r"https://\1", out)
        return out
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
                 "label": short_label(r), "citation": link_citation(r["source_url"], r["extraction"])}
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
    # sources.json is written later (after the night-floor section), once the
    # certified-turnout-only dates without a recovered night count are appended.

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
    DOE_TABLE_DATE_FIXES = {"2001-12-10": "2001-12-11",
                            # DOE prints 1899-12-02, but the figures match the
                            # Dec 29 1899 sewer-bond special exactly (Municipal
                            # Reports cumulative table); see doe-data-discrepancies.md
                            "1899-12-02": "1899-12-29"}
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
    # date -> (certified total, in-person/precinct count) for the dates whose
    # only record is the certified turnout split, so they can be cited too
    floor_meta = {}
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
            floor_meta[date] = {"final": total, "prec": prec}
    with open(ROOT / "data" / "sf_vbm_share_sos.csv", newline="") as f:
        for r in csv.DictReader(f):
            floor[r["election_date"]] = {
                "date": r["election_date"],
                "floorPct": round(100 * int(r["ballots_polling"]) / int(r["ballots_total"]), 1),
                "source": "certified-sov"}
            floor_meta[r["election_date"]] = {"final": int(r["ballots_total"]),
                                              "prec": int(r["ballots_polling"])}
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
            floor_meta[r["election_date"]] = {"final": int(r["ballots_cast"]),
                                              "prec": int(r["precinct"])}
    # attach election kind so the charts can filter diamonds like dots
    kind_by_id = {e["id"]: e["kind"] for e in out}
    def kind_for_date(d):
        y, m = d.split("-")[0], d.split("-")[1]
        if m == "11":
            return "General" if int(y) % 2 == 0 else "Municipal"
        if m in ("03", "06"):
            return "Primary"
        return "Special"
    for fp in floor.values():
        fp["kind"] = kind_by_id.get(fp["date"]) or kind_for_date(fp["date"])
    # ship the curated public search log (NOT the internal working ledger)
    # so the site documents what has already been searched (/methods)
    ledger = (ROOT / "docs" / "analysis" / "public-search-log.md").read_text()
    (OUT.parent / "ledger.json").write_text(json.dumps({"text": ledger}))

    # a news-derived night floor can be looser than the in-person floor;
    # the night count is >= the BEST floor, so solid dots display max(both)
    for e in out:
        f = floor.get(e["id"])
        if (f and e.get("nightPct") is not None and not e.get("nightPartial")
                and e["nightPct"] < f["floorPct"]):
            e["nightPct"] = f["floorPct"]
            e["nightSrc"] = (e.get("nightSrc") or "") + " (shown at the certified in-person floor, the tighter lower bound)"
    # re-emit elections.json - the floor comparison above can adjust nightPct
    OUT.write_text(json.dumps(out, indent=1))
    fl = sorted(floor.values(), key=lambda x: x["date"])
    F = OUT.parent / "night_floor.json"
    F.write_text(json.dumps(fl, indent=1))
    print(f"{len(fl)} night-floor points -> {F}")

    # sources.json is assembled and written at the very end of main() — once the
    # turnout, registration, and franchise-funnel series exist — so EVERY plotted
    # datapoint gets a provenance record, not just the recovered-count elections.

    # ---- turnout-of-registered series, 1899-2026 ("did the franchise expand?")
    # Ballots cast as a share of registered voters, one point per election.
    # Backbone is the DOE 1899-2019 historical turnout table; modern elections
    # (and any overlap) are overwritten with the certified per-release finals
    # and their registration, the more authoritative figure. This is turnout
    # of the *registered* electorate - not of the eligible population, which
    # needs a Census denominator the repo does not yet carry.
    turnout = {}
    # pre-1899 certified turnout (SF Municipal Reports Registrar master table +
    # Great Register) — extends the turnout-of-registered series back to 1879.
    # Registration is only basis-reliable from 1879 on (earlier Great Register
    # counts are cumulative/gross, so turnout% is omitted before 1879).
    pre1899 = ROOT / "data" / "sf_turnout_pre1899.csv"
    if pre1899.exists():
        with open(pre1899, newline="") as f:
            for r in csv.DictReader(f):
                if not r["registration"]:
                    # non-general elections in the vol47 cumulative table print
                    # ballots but no registration figure, so no turnout share
                    # can be computed; the ballots live in the CSV and the
                    # master index, not on the turnout chart
                    continue
                reg_i, bal = int(r["registration"]), int(r["ballots_cast"])
                turnout[r["election_date"]] = {"date": r["election_date"],
                    "turnoutPct": round(100 * bal / reg_i, 1),
                    "registered": reg_i, "ballots": bal,
                    "source": "muni-registrar",
                    "cite": r["source"]}
    # 1891-1907: the gap between the FY1888-89 Registrar master table and the
    # reliable start of the DOE table, recovered from Municipal Reports volumes
    # (basis muni-registrar) and the CA SOV / Blue Book (basis sov-bluebook)
    gap_csv = ROOT / "data" / "sf_turnout_1891_1907.csv"
    if gap_csv.exists():
        with open(gap_csv, newline="") as f:
            for r in csv.DictReader(f):
                reg_i, bal = int(r["registration"]), int(r["ballots_cast"])
                turnout[r["election_date"]] = {"date": r["election_date"],
                    "turnoutPct": round(100 * bal / reg_i, 1),
                    "registered": reg_i, "ballots": bal,
                    "source": r["basis"],
                    # per-row citation (volume, page, archive id, caveats such
                    # as the rounded fire-era 1905 figures) - threaded through
                    # to sources.json instead of the generic era label
                    "cite": r["source"]}
    with open(ROOT / "data" / "sf_turnout_history_doe_1899_2019.csv", newline="") as f:
        for r in csv.DictReader(f):
            reg = r["registration"]
            if not reg or reg in ("n/a", ""):
                continue  # 1910-11-01 has no registration figure
            date = DOE_TABLE_DATE_FIXES.get(r["election_date"], r["election_date"])
            reg_i, bal = int(reg), int(r["ballots_cast"])
            turnout[date] = {"date": date, "turnoutPct": round(100 * bal / reg_i, 1),
                             "registered": reg_i, "ballots": bal,
                             "source": "doe-turnout-table"}
    # certified finals (exact 2012+, archival 2002-2014) override the table
    for e in out:
        if e["registered"]:
            turnout[e["id"]] = {"date": e["id"],
                                "turnoutPct": round(100 * e["final"] / e["registered"], 1),
                                "registered": e["registered"], "ballots": e["final"],
                                "source": e["source"]}
    for tp in turnout.values():
        tp["kind"] = kind_by_id.get(tp["date"]) or kind_for_date(tp["date"])
    tn = sorted(turnout.values(), key=lambda x: x["date"])
    T = OUT.parent / "turnout_history.json"
    T.write_text(json.dumps(tn, indent=1))
    print(f"{len(tn)} turnout points -> {T}")

    # ---- registration vs eligible, 2001-2026 (the other half of "franchise")
    # SF county rows from the CA SoS Reports of Registration: registered voters
    # against the SoS's eligible-population estimate. See fetch_sos_registration.py.
    # CAVEAT: the eligible denominator is a DOF/Census estimate the state revises
    # between reports (it even dips 2011->2013, which a real population can't do),
    # so the *percent* has a soft discontinuity around 2011-2013 - read the trend,
    # not single-report jumps. Registered counts also sawtooth: rolls peak at each
    # general, then post-general list maintenance purges inactive voters.
    regelig = []
    reg_path = ROOT / "data" / "sf_registration_eligible.csv"
    if reg_path.exists():
        with open(reg_path, newline="") as f:
            for r in csv.DictReader(f):
                if not r["report_date"]:
                    continue
                regelig.append({"date": r["report_date"],
                                "eligible": int(r["eligible"]),
                                "registered": int(r["registered"]),
                                "pct": float(r["pct_registered_of_eligible"]),
                                "context": r["election_context"],
                                "source": "sos-ror", "recovered": False,
                                "url": r.get("source_url", "")})
    # pre-2000 points recovered from printed Statement of Vote participation
    # tables (archive.org), read off page-image crops and pending hand-verification.
    # `confidence: low` marks figures that look anomalous in the source itself
    # (e.g. 1994's ~96% rate: pre-NVRA bloated rolls vs a low DOF eligible estimate).
    sov_path = ROOT / "data" / "sf_registration_eligible_sov_1974_1998.csv"
    if sov_path.exists():
        with open(sov_path, newline="") as f:
            for r in csv.DictReader(f):
                regelig.append({"date": r["report_date"],
                                "eligible": int(r["eligible"]),
                                "registered": int(r["registered"]),
                                "pct": float(r["pct_registered_of_eligible"]),
                                "context": r["election_context"],
                                "source": "sov-print", "recovered": True,
                                "confidence": r["confidence"],
                                "url": r.get("source_url", "")})
    if regelig:
        regelig.sort(key=lambda x: x["date"])
        R = OUT.parent / "registration_eligible.json"
        R.write_text(json.dumps(regelig, indent=1))
        print(f"{len(regelig)} registration-vs-eligible points -> {R}")

    # ---- the franchise funnel: population -> voting-age -> eligible citizen ->
    # registered -> voted, at each presidential general 1900-2024. Census layers
    # (decennial, from sf_eligible_vap_estimate.csv = IPUMS NHGIS) are linearly
    # interpolated to election years; eligible uses census citizen-VAP through 1970
    # then the SoS-published eligible; registered/voted are the real per-election
    # figures. The bands between layers are the story: children, NON-CITIZENS,
    # the unregistered, and non-voters.
    funnel = []  # franchise-funnel points (filled below when census data exists)
    census = {}  # year -> (pop, vap, citizen_elig|None)
    vap_path = ROOT / "data" / "sf_eligible_vap_estimate.csv"
    if vap_path.exists():
        with open(vap_path) as f:
            for r in csv.DictReader(line for line in f if not line.startswith("#")):
                census[int(r["year"])] = (
                    int(r["total_population"]), int(r["voting_age_pop"]),
                    int(r["citizen_eligible"]) if r["citizen_eligible"] else None)

        def interp(anchors, y):
            xs = sorted(anchors)
            if y <= xs[0]:
                return anchors[xs[0]]
            if y >= xs[-1]:
                return anchors[xs[-1]]
            hi = next(x for x in xs if x >= y)
            lo = max(x for x in xs if x <= y)
            if hi == lo:
                return anchors[lo]
            return anchors[lo] + (anchors[hi] - anchors[lo]) * (y - lo) / (hi - lo)

        pop_a = {y: c[0] for y, c in census.items()}
        vap_a = {y: c[1] for y, c in census.items()}
        elig_a = {y: c[2] for y, c in census.items() if c[2]}  # census, 1900-1970
        for p in regelig:  # SoS-published eligible, 1978-2026
            elig_a[int(p["date"][:4])] = p["eligible"]
        funnel = []
        census_min = min(census) if census else 1900
        for t in tn:  # tn = turnout points; presidential generals only
            y = int(t["date"][:4])
            # gate to years with real census bands — interp() clamps below the
            # earliest census year, so pre-census generals (e.g. 1880/84/88) would
            # otherwise get bogus extrapolated population/vap/eligible.
            if y < census_min:
                continue
            if t["date"][5:7] == "11" and y % 4 == 0 and t.get("kind") == "General":
                funnel.append({
                    "year": y,
                    "population": round(interp(pop_a, y)),
                    "vap": round(interp(vap_a, y)),
                    "eligible": round(interp(elig_a, y)),
                    "registered": t["registered"],
                    "voted": t["ballots"],
                })
        funnel.sort(key=lambda x: x["year"])
        F2 = OUT.parent / "franchise_funnel.json"
        F2.write_text(json.dumps(funnel, indent=1))
        print(f"{len(funnel)} franchise-funnel points -> {F2}")

    # ---- sources.json: ONE provenance record for every plotted datapoint.
    # Recovered-count elections were built above; here we add every remaining
    # series so nothing on a chart is unsourced. No election names are invented
    # where the source carries none.
    SRC_LABELS = {
        "doe-turnout-history": "SF Dept. of Elections turnout history (1960–2002)",
        "certified-sov": "Certified Statement of Vote (CA Secretary of State / SF Dept. of Elections)",
        "doe-turnout-table": "SF Dept. of Elections historical turnout table (1899–2019)",
        "muni-registrar": "SF Municipal Reports — Registrar of Voters (1879–1890)",
    }
    have = {s["id"] for s in sources}
    # (a) certified turnout dates without a recovered night count: the in-person
    #     floor (where the precinct/mail split exists) or the turnout figure
    for date, fp in sorted(floor.items()):
        if date in have or date not in floor_meta:
            continue
        meta = floor_meta[date]
        label = SRC_LABELS.get(fp["source"], fp["source"])
        sources.append({
            "id": date,
            "name": "Certified turnout record — night count not yet recovered",
            "final": meta["final"], "finalSource": label,
            "observations": [{"date": date, "days": 0, "night": True,
                "total": meta["prec"], "pct": fp["floorPct"],
                "label": "election-night floor — in-person (precinct) share of the certified total",
                "citation": label}]})
        have.add(date)
    for tp in sorted(turnout.values(), key=lambda x: x["date"]):
        if tp["date"] in have:
            continue
        label = tp.get("cite") or SRC_LABELS.get(tp["source"], tp["source"])
        sources.append({
            "id": tp["date"],
            "name": "Certified turnout record — night count not yet recovered",
            "summary": f"{tp['ballots']:,} ballots cast, {tp['turnoutPct']}% of {tp['registered']:,} registered",
            "finalSource": label, "observations": []})
        have.add(tp["date"])
    # (b) registration vs eligible: each cited to its own Report of Registration
    #     (SoS) or printed Statement of Vote, by URL
    # `sov-print` lumps archived Statements of Vote with a newspaper-read figure;
    # distinguish the newspaper one (NewsBank) by URL so it isn't mislabeled.
    def reg_doc(source, url):
        u = (url or "").lower()
        if "newsbank" in u or "/news/" in u:
            return "Newspaper (via NewsBank)"
        if source == "sos-ror":
            return "California Secretary of State — Report of Registration"
        return "Statement of Vote — participation table"
    for p in regelig:
        if p["date"] in have:
            continue
        doc = reg_doc(p["source"], p.get("url", ""))
        sources.append({
            "id": p["date"], "name": doc,
            "summary": f"{p['registered']:,} registered of {p['eligible']:,} eligible citizens ({p['pct']}%) — {p['context']}",
            "finalSource": doc,
            "observations": [{"date": p["date"], "night": False,
                "total": p["registered"], "pct": p["pct"],
                "label": "registered ÷ eligible citizens",
                "citation": p.get("url") or doc}]})
        have.add(p["date"])
    # (c) franchise funnel: decennial-census bands (IPUMS NHGIS), registered /
    #     voted from the per-election records above
    for fr in funnel:
        sources.append({
            "id": f"funnel-{fr['year']}",
            "name": f"{fr['year']} franchise composition (decennial census)",
            "summary": (f"population {fr['population']:,}; voting-age {fr['vap']:,}; "
                        f"eligible citizens {fr['eligible']:,}; registered {fr['registered']:,}; "
                        f"voted {fr['voted']:,}"),
            "finalSource": "IPUMS NHGIS decennial census (population, voting-age, citizenship), interpolated to the election year; registration and turnout per the records above",
            "observations": []})
    # (d) CountySpeed chart: California county counting-speed comparison — an
    #     external dataset (not SF count data), so cite it here too.
    cs = json.loads((OUT.parent / "county_speed.json").read_text())
    counties = ", ".join(c["county"] for c in cs["counties"])
    years = "/".join(str(y) for y in cs["years"])
    sources.append({
        "id": "county-speed",
        "name": "California county counting speed (CountySpeed chart)",
        "summary": f"{cs['metric']} — {counties}; {years}.",
        "finalSource": f"{cs['source']} — {cs['sourceUrl']}",
        "observations": []})
    # (e) County counting-tech panel: one sourced record per jurisdiction — its
    #     adopted tech (+ first-election year) and reporting-speed metrics, with
    #     EVERY cited URL, so no chart number is unsourced in this doc.
    ct = json.loads((OUT.parent / "county_tech.json").read_text())
    by_j: dict = {}
    for a in ct["adoptions"]:
        d = by_j.setdefault(a["jurisdiction"], {"adopt": [], "ow": {}, "urls": []})
        if a["status"] == "adopted":
            d["adopt"].append(f"{a['tech']} ({a['adopted_year']})")
        if a.get("evidence_url"):
            d["urls"].append(a["evidence_url"])
    for m in ct["metrics"]:
        d = by_j.setdefault(m["jurisdiction"], {"adopt": [], "ow": {}, "urls": []})
        if m["metric"] == "oneweek_pct" and m["value"] is not None:
            d["ow"][m["year"]] = m["value"]
        if m.get("source_url"):
            d["urls"].append(m["source_url"])
    for j, d in by_j.items():
        slug = re.sub(r"[^a-z0-9]+", "-", j.lower()).strip("-")
        ow = ", ".join(f"{y}: {d['ow'][y]}%" for y in sorted(d["ow"]))
        sources.append({
            "id": f"county-tech-{slug}",
            "name": f"{j} — counting technology & reporting speed",
            "summary": (f"Counting tech adopted: {', '.join(d['adopt']) or 'none (control)'}. "
                        f"One-week reporting rate — {ow or 'n/a'}."),
            "finalSource": " · ".join(sorted(set(d["urls"]))),
            "observations": []})
    sources.sort(key=lambda s: s["id"], reverse=True)
    (OUT.parent / "sources.json").write_text(json.dumps(sources, indent=1))
    print(f"{len(sources)} source records -> sources.json")


if __name__ == "__main__":
    main()
