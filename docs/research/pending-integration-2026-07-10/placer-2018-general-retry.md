# Placer County CA 2018-11-06 general — election-night plateau retry

Target: true election-night (plateau) countywide ballot count, Nov 6 2018 general.
Currently committed row (data/research/election-night/placer-ca.json): comparable:false,
election_night_ballots 113,380 (CEILING, Nov 9 15:15 render, refuted as canvass-contaminated
by Nov 21 capture showing 162,802), certified_final 177,725.

Maintainer lead: uploads/documents/11062018/11062018_Results.pdf on
placercountyelections.gov, in-place-overwritten. Each Wayback capture timestamp = distinct
count state; digest column distinguishes without fetching.

## Plan
1. CDX prefix sweep of placercountyelections.gov/uploads/documents/11062018/*
2. CDX prefix sweep of placerelections.com (2018-era host) for same window
3. Check placer.ca.gov and homepage captures around election week to find real 2018 host/links
4. Build state timeline (capture ts, digest, distinct-digest fetch -> internal report ts + ballots)
5. Cross-check SoS status-page vein (none found in sos-status-sweep.md for Placer)

## Log

### Step 1: CDX sweep of placercountyelections.gov/uploads/documents/11062018/*
- Naive `url=...&matchType=prefix` with a literal `*` in url returned [] (empty)
  every time (bad query form — matchType=prefix + trailing `*` conflict).
- Working form: `url=placercountyelections.gov&matchType=domain&filter=urlkey:.*11062018.*`
  (collapse=urlkey). Returned 49 files in the 11062018/ folder — full listing
  saved to placer_gov_11062018_all.json. **Only ONE `_Results.pdf`** in the
  folder (`11062018_Results.pdf`), no siblings (no `_Results_2.pdf`, no
  `_Summary.pdf`, no dated variants). All other files are administrative
  (notices, measure text, press releases, CSQ candidate statements, SOV
  totals-by-precinct/district, SOV.txt).
- `.gov` domain captures of this folder are ALL from 2020-2025 (site
  migration/relaunch era) — the .gov domain did not exist live in 2018.

### Step 2: Full capture history of 11062018_Results.pdf across BOTH hosts
- `.gov` host (placercountyelections.gov): captures 20210505182542,
  20220817221918 — digest HZIBEPOXI7OXAZPYOYXMJTBKZST44PCB (identical) both times.
- `.com` host (placerelections.com, the real 2018-era domain): ONE capture,
  20190805011615 — **same digest** HZIBEPOXI7OXAZPYOYXMJTBKZST44PCB.
- So across 3 captures spanning Aug 2019 - Aug 2022, the file NEVER changed
  (single frozen digest). Earliest capture of this specific file is Aug 5
  2019 — 9 months post-election. No capture anywhere near Nov 2018.
- **Fetched and read it** (placer2018_results_pdf_aug2019.pdf/.txt): header
  reads "PLACER COUNTY / OFFICIAL ELECTION SUMMARY / November 6, 2018 /
  Date:12/06/18 Time:16:07:31 / Registered Voters 235592 - Cards Cast 177725
  75.44% / Num. Reporting 358 100.00%". Cards Cast 177,725 = EXACTLY the
  certified_final already in placer-ca.json. **This file IS the certified
  final canvass PDF** (Dec 6 2018 report), published once, static ever
  since. It is NOT an election-night in-place-overwritten tracker — the
  maintainer's lead resolves to the FINAL, not an interim state. Dead end
  for plateau purposes (confirms denominator, not numerator).

### Step 3: the REAL in-place-overwritten live page
- CDX sweep `placerelections.com&matchType=domain&from=20181101&to=20190101
  &filter=urlkey:.*result.*` (placer_com_nov2018_results_urls.json) found
  the actual live tracker: `/election-night-results/` (note: trailing
  slash, WordPress permalink form; NOT `/election-night-results.aspx`,
  which 301-redirects to it).
- Captures of `/election-night-results/` in the window, 4 DISTINCT digests:
  - 20181113195233 — digest ZUJPZZSBGH5WQO32ONKGV6HUH2MUXAJG — EARLIEST capture.
    This is the exact capture already cited in placer-ca.json's
    source_url_night: Cards Cast 113,380, internal report timestamp
    11/09/18 15:15:00 (already flagged comparable:false / ceiling).
  - 20181121195122 — digest A4UCIDBTOEQJ6RNYYZ5YQLAHHYSAOGA7 (distinct)
  - 20181121210754 — digest 2GY6YXRQEKO3E3PHMCTNZEZPGD4TCT77 (distinct,
    ~1hr later same day — page moved TWICE in one day)
  - 20181128222547 — digest HO4GXNDFWZX66OADTJT6ZYZABJ63O4YC (distinct)
  - (These Nov 21/28 states are the canvass-tracking captures; one of the
    Nov 21 pair is the "162,802" state already noted in the committed row
    as the bracket evidence that refutes the Nov 9/13 render as frozen.)
- **CRITICAL FINDING: there is NO capture of /election-night-results/ (or
  any results artifact on either host) between Nov 6 poll close and Nov 13.**
  20181113195233 is the earliest capture that exists, period. Wayback simply
  never crawled the page during election week itself. This is not a
  replay-aliasing or gzip artifact — verified via matchType=domain sweep
  covering the FULL Nov 2018 window, plus a fresh full-domain results-url
  sweep; nothing earlier turned up under placerelections.com.

### Step 4: ruled-out red herrings
- `/documents/08_GEN_Final_Results.pdf` (captured 20181129082703): opened —
  PDF CreationDate Dec 1 2008. Leftover 2008 election file, "08" = 2008 not
  2018. Not relevant.
- `/documents/GEMS ELECTION RESULTS.pdf` (captured 20181129020805): opened —
  PDF CreationDate Apr 24 2009, content header "February 5, 2008 FINAL".
  Also a stale 2008 leftover. Not relevant.
- No other host variants found live in 2018 window (placer.ca.gov not
  checked further; the county's registrar site in 2018 was confirmed
  placerelections.com via the working /election-night-results/ captures
  and via the 2022-row note in placer-ca.json describing the same lineage).

### Step 5: SoS status-page vein
- Checked scratchpad/sos-status-sweep.md for "placer" — zero hits. No
  overlap/prior coverage to reconcile.

## Conclusion
NOT-RECOVERED. The maintainer's lead (`.../11062018/11062018_Results.pdf`)
resolves to the CERTIFIED FINAL canvass PDF (177,725 Cards Cast, Dec 6 2018
report), confirmed by direct fetch — not an election-night interim state,
and there are no sibling/interim files in that folder. The actual
in-place-overwritten live page (`/election-night-results/`) has its
earliest ever Wayback capture on Nov 13 2018 (7 days post-election), which
is the SAME capture already used for the committed 113,380 ceiling. No
earlier state exists to recover. The comparable:false / ceiling status in
data/research/election-night/placer-ca.json is CORRECT and should stand;
this retry found no new evidence to promote or replace it.
