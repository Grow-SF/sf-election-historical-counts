# Archive recovery ledger — 2026-06-10 session

Working state + validated recipes, so any fresh session can resume without
transcript access. Everything listed as "committed" is on main.

## Dataset state (end of session)

44 elections in `viz/src/data/elections.json` (18 exact, 26 archival); 59
rows in `data/sf_archival_canvass_points.csv`; 106 night-floor and VBM-share
points (1964–2026, continuous). Commits today: `15fc513` (floor diamonds in
threshold chart), `4a00eca` (DOE 1899–2019 turnout table + 2009 points +
2002-11 final fix), `7679023` (1998 Domino day-17), `cc48c10` (cert dates
from minutes), `cff288e` (Chronicle-derived 1998–99 points), `e6c395b`
(Domino census: Dec 2000 + Dec 2002 runoffs), `f57b058` (March 2000 day-1
via same-contest ratio).

## Elections added today (first-ever count data)

| Election | Points | Source |
|---|---|---|
| 1998-11-03 | 96.8% d3; 100% d17 | Chronicle "8,000 remain" (MN103975); Domino "As of 11/20/98" |
| 1999-11-02 | 90.7% d3 | Chronicle "19,000 to count" (MN82008) |
| 1999-12-14 | 94.3% d2 | Chronicle "13,000 remain" (MN95634) |
| 2000-12-12 | 100% d3 (w/ ED/VBM split) | election2.nsf "as of 12/15/2000 4:18 PM" |
| 2002-12-10 | 100% d6 | results1202 RUN 12/16/02 |
| 2004-03-02 | 100% d23 (cert) | Commission minutes 2004-05-19, file 24595 |
| 2006-06-06 | 100% d27 (cert) | minutes 2006-07-19, file 42915 |
| 2007-11-06 | 100% d35 (cert) | minutes 2008-01-16, file 51883 |
| 2008-11-04 | 100% d28 (cert) | minutes 2008-12-17, file 95751 |
| 2009-11-03 | 90.1% d3; 100% d14 | sfgov page "Updated 11/6/2009 4:00 PM"; minutes 113990 |

Deliberately excluded: 2006-11-07 cert (Jan 17 2007 = day 71, ES&S
equipment-crisis administrative delay, not count duration); election2.nsf's
stale Nov 1999 mayor/DA views (no usable date; "10/16/2001" stamp is a
reindex artifact; "322 of 644 precincts" label contradicts vote totals).

## Validated recipes

- **Chronicle via Wayback/SFGate (free, no subscription)**: CDX prefix
  enumeration by exact date:
  `cdx?url=sfgate.com/cgi-bin/article.cgi%3Ffile%3D/chronicle/archive/YYYY/MM/DD/&matchType=prefix`
  (2004+: `%3Ff%3D/c/a/YYYY/MM/DD/` and `%3Ffile%3D/c/a/...`; 2000-era has
  descriptive names like ballot.DTL with `&type=election`). Fetch
  `web.archive.org/web/{TS}id_/{URL}`. Derive observations as
  certified − stated-remaining = conservative floor ("news-derived").
- **Domino "As of:" stamps**: capture date irrelevant; the page's internal
  stamp is the observation time. Categorized views can hold multiple dated
  snapshots in one page.
- **Cert dates as data**: a canvass-completion/certification date is a 100%
  observation (stamp_kind "minutes-stated"); only ingest when reasonably
  tight and not administratively delayed.
- **DOE official turnout table** (1899–2019, w/ precinct/mail splits):
  wayback capture 20230204064121 of sfelections.sfgov.org/historical-voter-turnout,
  parsed into `data/sf_turnout_history_doe_1899_2019.csv`. Validated 0 diffs
  vs all prior series. Known typo: its 12/10/2001 = our 2001-12-11 (fix
  mapped in `scripts/build_viz_data.py` DOE_TABLE_DATE_FIXES).

## Closed veins (do not re-dig)

- SOS election-night sites (vote96/98/2000/2002/2003/2004.ss.ca.gov):
  pages updated through canvass; all captures are certified data. No
  night-window captures exist.
- Domino .nsf census complete: eresults.nsf = Nov 1998 only;
  election2.nsf = Dec 2000 (+stale undatable Nov 1999); all sibling names
  never captured; campaign-finance .nsfs irrelevant.
- Commission minutes: fully mined twice (counts + cert dates). Nothing
  dated for 2002–03, 2008-02/04/06, 2009-05, 2010–2014.
- CNN: county pages exist only for 2000 (SF = county 038; frozen night data
  Gore 201,482 / Bush 41,746 / Nader 21,609 — votes not ballots, mirrored at
  mirror/night-captures/cnn_2000_ca_sf_county038.html, NOT yet in dataset).
  1996/1998 are statewide-only. LATimes/WaPo: nothing.
- Chronicle 1995–1999 swept (E+1..E+3 + cert windows). 1995-12, 1996-03,
  1996-11, 1997-11, 1997-12 yielded nothing usable.

## Chronicle 2000–2007 outcome (retry agent died; salvaged from disk)

- **2000-03-07: 90.2% by day 1** (commit `f57b058`) — same-contest ratio:
  day-after Prop A table (MN87716) vs certified Prop A in sf000307.xls.
  The ratio method cancels undervote; use it wherever a day-after results
  table + certified SOV contest totals both exist.
- **Cross-validation**: Chronicle Nov 8 2001 "19,000 must still be counted"
  → 115,024 implied vs our captured results page 115,477 (0.4% apart).
- Closed: Nov 2000 (no SF count coverage — Bush/Gore; all "remaining"
  figures are Sonoma/Santa Clara), Dec 2001 (no numbers), Nov 2003
  (zero articles archived for Nov 5–7 2003 — confirmed via CDX).
- 886 articles in mirror/chronicle-sfgate/ (incl. 48 2003sweep_* fetched
  inline). 2003 vein closed: all recall + Dec-runoff day-after articles
  scanned, zero SF count statements (Newsom's margin was settled by
  morning - no count drama, no coverage). 58 of 102 2003 fetches blocked
  by the rate limiter, but both day-after sets are well sampled.

## Open threads

1. **CNN 2000 night estimate** (~83% of contest votes) — needs a design
   decision: "estimated night share" marker type in NightShareChart.
2. **DOE records request** (user-side) — pipeline ingests directly.
3. **Mirror CDN upload** (user-side); manifest committed.
4. Possible: BOS journal declarations (SFPL, offline) for pre-1995 cert
   dates; ProQuest Chronicle for the 1995-12/1996/1997 night-of holes;
   the 58 rate-limited 2003 fetches (low expected value).

## Conventions

- Subagents must write findings to disk incrementally (mirror/ paths),
  not just in their final message — two agents died with findings only in
  transcript today (both salvaged).
- Verify every agent-claimed timestamp against the saved file before
  ingesting (three timestamp errors caught today: 2001 "night" = day 2;
  agent's 94.1% used wrong denominator; NEIGHBOR page has no stamp — the
  stamp lives on the contest views).
- Archival csv schema: stamp_kinds are capture-time | page-self-reported |
  minutes-stated | news-derived.
