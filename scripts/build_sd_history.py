#!/usr/bin/env python3
"""Bake packages/data/sd_night_history.json from the San Diego datasets.

Sources (never hand-edit the output):
  data/research/san-diego-history/sd_night_history.csv   1871-1920 newspaper floors
      (share basis: certified same-contest total)
  data/research/election-night/san-diego-ca.json         2008+ panel plateau rows
      (share basis: certified ballots cast)

Rows are emitted in the chart Election shape (packages/data/types.ts) so
NightShareChart can render them unchanged. The two denominator bases map onto
the chart's existing source encoding: newspaper floors are "archival", panel
plateau rows are "exact"; the SD chart island's caption carries the caveat.
"""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "packages" / "data" / "sd_night_history.json"

# Rows the chart must DIM as lower bounds rather than plot as the night's true
# state. Two families, both keyed off the CSV's own `flags` column so the data
# stays the single source of truth:
#   - newspaper-practice artifacts: the paper printed majorities not votes, or
#     omitted the city entirely, or gave only a city proxy
#   - ap-remote-basis: a REMOTE paper's AP county row, captured at that paper's
#     press time, which lags the county's own compilation badly (1928: 31 of
#     310 precincts had reached the wire)
# News-derived floors (certified minus a stated full remainder) are NOT dimmed:
# they bound the whole night, tightly, and are plotted as real points.
ARTIFACT = {
    "1890-11-04": "the paper printed majorities, not raw votes, for all but 3 precincts — the true night count was far higher",
    "1892-11-08": "the morning paper printed no city returns at all — the true night count was far higher",
    "1900-11-06": "city-only total-vote proxy (the countywide table's total row was left blank) — the county night count was higher",
    "1924-11-04": "a remote paper's AP county row at its press time (158 of 274 precincts) — the San Diego Union's own count that night was higher",
    "1928-11-06": "a remote paper's AP county row at its press time (only 31 of 310 precincts had reached the wire) — a severe undercount of the night, not a slow count",
    "1936-11-03": "a pre-dawn EXTRA that went to press with only 167 precincts in — a genuine night count, but an early-press snapshot, so the end-of-night total was higher",
    # The wire-coverage artifacts. These plot near zero not because San Diego
    # counted nothing, but because a distant paper's wire desk carried almost no
    # San Diego copy overnight. They are the weakest class of point in the
    # dataset; the note text and tooltips must say so plainly.
    "1914-11-03": "a Sacramento paper's wire dispatch carrying just 20 of 178 precincts — it measures the wire's coverage, not San Diego's count, which was far further along",
    "1922-11-07": "a Sacramento paper's wire table carrying just 36 of 240 precincts — the wire's coverage, not San Diego's count (a San Pedro paper's dawn bulletin already had 92 precincts)",
    "1926-11-02": "the Los Angeles wire desk carried just 2 of San Diego's 308 precincts overnight — 22 ballots. This measures LA's coverage of San Diego, not San Diego's count",
    "1930-11-04": "the Los Angeles wire desk carried a SINGLE precinct of San Diego's 384 — 197 ballots. This measures LA's coverage of San Diego, not San Diego's count",
}

NAME = {
    "presidential-general": "Presidential General",
    "gubernatorial-general": "Gubernatorial General",
    "midterm-general": "Midterm General",
    "statewide-primary": "Statewide Primary",
    "presidential-primary": "Presidential Primary",
}

rows = []

for r in csv.DictReader(open(ROOT / "data/research/san-diego-history/sd_night_history.csv")):
    if not r["night_share_pct"]:
        continue  # 1882: no certified denominator exists
    date = r["election_date"]
    if date in ARTIFACT:
        assert r["flags"], f"{date} is dimmed but carries no flags in the CSV"
    rows.append(
        {
            "id": date,
            "name": NAME.get(r["election_type"], r["election_type"]),
            "kind": "General",
            "year": int(date[:4]),
            "final": int(r["certified_contest_total"]),
            "registered": None,
            "source": "archival",
            "provisional": False,
            "nReports": 1,
            "nightPct": float(r["night_share_pct"]),
            "nightPartial": date in ARTIFACT,
            "nightSrc": f"{r['night_source']} — {r['precincts_basis']}",
            "srcShort": r["night_source"],
            "vbmShare": None,
            "pts": [],
            "thresholds": {},
        }
    )

panel = json.load(open(ROOT / "data/research/election-night/san-diego-ca.json"))
for e in panel["elections"]:
    if e["election_night_pct"] is None:
        continue
    rows.append(
        {
            "id": e["date"],
            "name": NAME.get(e["type"], e["type"]),
            "kind": "Primary" if "primary" in e["type"] else "General",
            "year": int(e["date"][:4]),
            "final": e["certified_final"],
            "registered": None,
            "source": "exact",
            "provisional": False,
            "nReports": 1,
            "nightPct": e["election_night_pct"],
            "nightPartial": False,
            "nightSrc": e["source_url_night"],
            "srcShort": "SoS/registrar election-night report (panel row)",
            "vbmShare": None,
            "pts": [],
            "thresholds": {},
        }
    )

rows.sort(key=lambda r: r["id"])
OUT.write_text(json.dumps({"note": "GENERATED by scripts/build_sd_history.py — do not edit", "artifactNotes": ARTIFACT, "elections": rows}, indent=2) + "\n")
print(f"wrote {OUT} ({len(rows)} elections)")
