#!/usr/bin/env python3
"""Build a single per-election CSV joining the franchise figures (eligible,
registered) with the certified ballot split (election-day vs vote-by-mail),
each value carrying its own source.

Output: data/sf_franchise_by_election.csv

Two `registered` columns on purpose:
  registered_cor  close-of-registration — the certified turnout denominator
                  (ballots cast / registered_cor = turnout %)
  registered_ror  the Secretary of State's Report of Registration snapshot,
                  taken ~15 days before the election; pairs with `eligible`
                  (registered_ror / eligible = registration rate)

Coverage is sparse by nature: registered_cor reaches 1899; the e-day/vbm split
~1960; eligible/registered_ror only 1978+ (a SoS estimate, revised between
reports). Empty cells mean "not recorded in any source," not zero.
"""
import collections
import csv
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
DATA = ROOT / "data"
VIZ = ROOT / "viz" / "src" / "data"
OUT = DATA / "sf_franchise_by_election.csv"
# the DOE table dates the Dec 2001 runoff a day early (a Monday); the runoff was
# Tue Dec 11 — same fix build_viz_data.py applies
DOE_FIX = {"2001-12-10": "2001-12-11"}


def iso(s):
    return dt.date.fromisoformat(s)


def with_url(label, url):
    return f"{label} ({url})" if url else label


def reg_label(source, url):
    """Classify a registration point by its actual source. `sov-print` lumps two
    very different things — archived Statements of Vote AND a figure read from a
    newspaper (NewsBank) — so distinguish them by URL."""
    u = (url or "").lower()
    if "newsbank" in u or "/news/" in u:
        return "Newspaper (via NewsBank)"
    if source == "sos-ror":
        return "CA Secretary of State — Report of Registration"
    return "Statement of Vote — participation table"


# ---- close-of-registration registered + election kind (turnout_history.json) ----
turnout = {t["date"]: t for t in json.load(open(VIZ / "turnout_history.json"))}
COR_SRC = {
    "doe-turnout-table": "SF Dept. of Elections historical turnout table (1899–2019)",
    "exact": "SF Dept. of Elections certified results",
    "archival": "archival recovery (per-release; see sources.json)",
    "certified-sov": "Certified Statement of Vote",
}

# ---- certified ballot split (e-day = precinct, vbm = mail/absentee) ----
# priority: certified SoV > 1960–2002 turnout history > DOE 1899–2019 table
split = {}  # date -> {e_day, vbm, src, url}
with open(DATA / "sf_turnout_history_doe_1899_2019.csv", newline="") as f:
    for r in csv.DictReader(f):
        if r["mail"] in ("n/a", ""):
            continue
        date = DOE_FIX.get(r["election_date"], r["election_date"])
        split[date] = {"e_day": int(r["precinct"]), "vbm": int(r["mail"]),
                       "src": COR_SRC["doe-turnout-table"], "url": ""}
with open(DATA / "sf_turnout_history_1960_2002.csv", newline="") as f:
    for r in csv.DictReader(f):
        if r["absentee"] in ("n/a", ""):
            continue
        m, day, y = r["date"].split("/")
        year = int(y) + (1900 if int(y) >= 60 else 2000)
        date = f"{year}-{int(m):02d}-{int(day):02d}"
        split[date] = {"e_day": int(r["precinct"].replace(",", "")),
                       "vbm": int(r["absentee"].replace(",", "")),
                       "src": "SF Dept. of Elections turnout history (1960–2002)", "url": ""}
with open(DATA / "sf_vbm_share_sos.csv", newline="") as f:
    for r in csv.DictReader(f):
        split[r["election_date"]] = {"e_day": int(r["ballots_polling"]),
                                     "vbm": int(r["ballots_absentee"]),
                                     "src": "Certified Statement of Vote",
                                     "url": r.get("source_url", "")}
# DOE per-release timeline (2012+): the final release (largest total) is the
# certified split — exact counts, highest priority for the modern era
tl = collections.defaultdict(list)
with open(DATA / "sf_count_timeline.csv", newline="") as f:
    for r in csv.DictReader(f):
        if r["ballots_election_day"] and r["ballots_vbm"]:
            tl[r["election_date"]].append(r)
for date, releases in tl.items():
    last = max(releases, key=lambda r: int(r["ballots_counted_total"]))
    split[date] = {"e_day": int(last["ballots_election_day"]),
                   "vbm": int(last["ballots_vbm"]),
                   "src": "SF Dept. of Elections certified results release",
                   "url": last.get("source_url", "")}

# ---- Report of Registration snapshots: eligible + registered_ror, by URL ----
ror = []
for x in json.load(open(VIZ / "registration_eligible.json")):
    ror.append({
        "sample": x["date"], "eligible": x["eligible"], "registered": x["registered"],
        "src": reg_label(x["source"], x.get("url", "")),
        "url": x.get("url", ""), "confidence": x.get("confidence", ""),
    })
ror.sort(key=lambda r: r["sample"])


def nearest_ror(election_date):
    """The Report of Registration closest before the election, within 45 days
    (the SoS publishes a 15-day report before each statewide election). Odd-year
    interim reports fall outside the window and aren't attached to an election."""
    e = iso(election_date)
    best = None
    for r in ror:
        gap = (e - iso(r["sample"])).days
        if 0 <= gap <= 45 and (best is None or r["sample"] > best["sample"]):
            best = r
    return best


COLS = ["election_date", "kind", "sample_date", "eligible", "registered_cor",
        "registered_ror", "total", "e_day", "vbm", "eligible_source",
        "registered_cor_source", "registered_ror_source", "total_source",
        "e_day_source", "vbm_source", "confidence"]

rows = []
for date, t in turnout.items():
    sp = split.get(date)
    r = nearest_ror(date)
    e_day = sp["e_day"] if sp else None
    vbm = sp["vbm"] if sp else None
    cor_src = COR_SRC.get(t.get("source", ""), t.get("source", ""))
    # total = certified ballots cast (the turnout numerator), known back to 1899;
    # e_day/vbm are its breakdown, only recorded from ~1960. Where both exist they
    # sum to total.
    rows.append({
        "election_date": date,
        "kind": t.get("kind", ""),
        "sample_date": r["sample"] if r else "",
        "eligible": r["eligible"] if r else "",
        "registered_cor": t.get("registered", ""),
        "registered_ror": r["registered"] if r else "",
        "total": t.get("ballots", ""),
        "e_day": e_day if e_day is not None else "",
        "vbm": vbm if vbm is not None else "",
        "eligible_source": with_url(r["src"], r["url"]) if r else "",
        "registered_cor_source": cor_src,
        "registered_ror_source": with_url(r["src"], r["url"]) if r else "",
        "total_source": cor_src,
        "e_day_source": with_url(sp["src"], sp["url"]) if sp else "",
        "vbm_source": with_url(sp["src"], sp["url"]) if sp else "",
        "confidence": r["confidence"] if r else "",
    })

rows.sort(key=lambda x: x["election_date"])
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLS)
    w.writeheader()
    w.writerows(rows)
print(f"{len(rows)} elections -> {OUT}")
