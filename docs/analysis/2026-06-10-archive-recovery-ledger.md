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

## Chronicle/SFGate vein: CLOSED (final sweep 2026-06-10 evening)

Title-first sweep (front-page captures → headline filter → selective
fetch; ~150 requests vs 800+ brute force). Outcome: **no further count
data exists in Chronicle web coverage.** 1996-11: 14/19 archived articles
are national-focus, zero SF count lines. 2002–2009 morning-after stories
never print count-status numbers (SFGate linked the DOE's live results
instead; count-drama stories only existed in the close-race era
1998–2001). The three percentage-only hits (2006 AG race, 2006 31%-of-
precincts partial, 2007 question-time measure) are not count data.
Final Chronicle yield stands: 1998-11, 1999-11, 1999-12, 2000-03 points
+ the 2001-11 cross-validation. Artifacts: title_queue.tsv (auditable
headline selections), index_*/titled_* in mirror/chronicle-sfgate/.

## Chronicle SUBSCRIPTION recovery (2026-06-10 night, ongoing)

User's sfchronicle.com login + debug-port Chrome (puppeteer-core on
127.0.0.1:9222, throwaway profile /tmp/chrome-chronicle). The Hearst
archive search reaches 1995 (verified: finds both known 1998 and 1995
headlines wayback had). Method: phrase queries on the /search/ page ->
result dates parsed client-side -> logged-in article fetches saved to
mirror/chronicle-sfgate/sub_*.txt (text + provenance header).

Commit `38a2208`: 1995-11-07 NEW (95.4% d3), 1999-12-14 d7 tail,
2002-03-05 first early point (86.4% d3), 2002-11-05 d3, 2007-11-06
first early point (77.5% d3). 45 elections.

Tier 2 in flight: systematic per-election queries for 1995-12, 1996-03,
1996-11, 1997-06 (49ers stadium squeaker - new election candidate),
1997-11, 1998-06, 2000-11, 2003-10/11/12, 2006-11, 2008-04/06, 2009-05.
Queue + articles persist in mirror/chronicle-sfgate/ (tier2_queue.json,
sub2_*.txt) - scan offline with the usual regex if session dies.

Tier 3 (needs user): SFPL eResources login in the same debug Chrome ->
NewsBank SF Chronicle full text reportedly 1985+ -> same method for
1985-1994 (8 elections incl. 1987 Agnos, 1991 Jordan runoff). Pre-1985
has no licensed digital full text (the 1923-1984 Chronicle gap);
candidates: IA-scanned SF Examiner issues, GenealogyBank, microfilm.

## NewsBank unlock (2026-06-11 00:0x, staged - awaiting one user click)

The Chronicle subscription's search page has an "Archives" link ->
sfchronicle.com/archive/search/subscriber/ -> NewsBank handoff
(verify1.newsbank.com/cgi-bin/ngate/NGPA-CASFC) -> sfchronicle.newsbank.com:
"articles back to 1865", date_from/date_to search fields, free for
subscribers. This REOPENS the 1923-1984 era previously written off.
Blocked solely on the NewsBank "I agree" terms gate, which needs the
user's explicit authorization (asked; pending). Sweep plan + 50-election
target list (1960-1995) staged at mirror/newsbank/SWEEP_PLAN.md and
mirror/newsbank_targets.json. Note: only 1960/1964/1968 in the 60s have
certified denominators; odd-year 60s municipals need certified totals
from offline city records first.

Tier-2 lesson: the regular sfchronicle.com search ranks by recency -
generic queries drown in current news; only rare exact phrases work
(that's how Tier 1 scored). NewsBank's date-range search removes this
limitation entirely.

## NewsBank status update (2026-06-11)

User authorized terms; search works but full-doc view requires a
NewsBank account the Chronicle subscription does NOT include. PLAN:
inventory via free search snippets now (running - newest-first per
user, floor at 1960); full-text fetching switches to SFPL's NewsBank
access (America's News) once the user renews their library card. Doc
IDs/headlines/dates in mirror/newsbank/phaseA_snippets.json map onto
SFPL's portal (same backend).

Search mechanics: sfchronicle.newsbank.com/search?text=...&date_from=
MM/DD/YYYY&date_to=...&pub[0]=SFCB (Text 1985+) or
pub[0]=142051F45F422A02 (Image 1865-2017, OCR page scans - the
1923-1984 source). Result snippets carry article lead text - some
count statements derivable from snippets alone.

Early inventory gold: 2000-11-09 "Absentee, Provisional Ballots Left
to Count in S.F." (doc 0EB4F969E1C867F6 - Nov 2000 has NO data);
1995-11 "SAN FRANCISCO ELECTION RESULTS" day-after table (543/543
precincts, doc 0EB4F6FF665242DA); Jun 1997 day-after coverage exists.

## NewsBank inventory COMPLETE (2026-06-11)

mirror/newsbank/master_inventory.csv: 449 hits across 62 elections,
1960-2009, newest-first. Text collection (1985-2009): 284 snippets w/
headlines + doc IDs. Image collection (1960-1984): 165 page-scan hits
w/ issue dates (decoded from Julian day numbers in the v2 doc URLs)
and page numbers - every pre-1985 election in the target list has
hits, incl. the 1983 Feinstein recall, 1979 + 1975 runoffs, and the
1960/1964/1968 generals. Supplementary round pending: '"election
results"' + 'registrar' queries to catch day-after results tables.

NEXT (blocked on user's SFPL card renewal): log into SFPL eResources
in the debug Chrome; fetch full text (Text collection via America's
News) and page scans (Image collection) for the inventory; derive
observations via certified-minus-remaining and same-contest-ratio.

## NewsBank harvest COMPLETE (2026-06-11)

732 Chronicle docs fetched via SFPL ezproxy (4 parallel tabs, zero
failures, full provenance headers incl. SOURCE/ACCESSED). Extraction:
1,290 statements; deep-mine agent proposed 34 derivations (incremental
CSV survived its context death); 21 verified and ingested across two
passes. DATASET: 62 elections, 85 archival observations. Night shares
now recovered for 1988-1997 (86-97% actual), incl. the 1997 stadium
all-nighter (97.5% by dawn) and 1988's 40,000-absentees-in-a-day.
New derivation method validated: top-contest sums from night results
tables are conservative count floors. Corpus + proposals remain in
mirror/newsbank/ (licensed content - NOT for CDN).

## Results-table vein: text-format tables exhausted (2026-06-11)

The Chronicle printed a results table after every election, but in
NewsBank's Text collection many ran as GRAPHICS ('Caption: CHART: SEE
TEXT') with no OCR. Text-format tables exist and are harvested for:
1989-11 (Prop P 94.1% night), 1991-11 (93.6%), 1991-12 (87.8%),
1993-06, 1994-06, 1995-11/12, 2003-11 (84.7% night), 2006-11 (61.7%
d2). Verified dry for the 29 still-missing-night elections via
'"precincts rptg"' / '"HOW SAN FRANCISCO VOTED"' body-text queries
(confirmed working on known-positive windows). The remaining night
values live in: (a) the Image collection page scans incl. the printed
graphic tables - 1865-2017, needs scan access/OCR; (b) the DOE records
request. Today's final state: 63 elections, 87 archival observations.

## Image-scan OCR attempt: blocked by broken proxy backend (2026-06-11)

The pre-1985 page-scan route was tested end to end. Findings:
- The NewsBank image viewer (OpenSeadragon over DZI tiles of bitonal
  TIFF G4 scans - ideal OCR material) loads through SFPL ezproxy, but
  its tile server URL rewrites to aws-maxdac.int.newsbank.com, an
  INTERNAL hostname the proxy cannot resolve: "Unable to locate
  address". The viewer canvas renders blank for any SFPL remote user -
  this is a NewsBank/SFPL proxy configuration bug, not a licensing
  limit. Page thumbnails (public maximus cache, 200px) work but are
  too small to OCR. Download PDF is inert (same backend). The
  Chronicle-subscription side walls image docs entirely.
- RECOURSE: (a) report the broken remote image viewer to SFPL
  eResources support - it is broken for everyone; (b) in-library
  terminals are on NewsBank's network path and likely render scans -
  mirror/newsbank/master_inventory.csv's 165 image citations (exact
  issue dates + page numbers, 1960-1984) are a ready-made library
  session worklist; (c) the DOE records request supersedes all of it
  if fulfilled.

## Scan-reading campaign results (2026-06-11 afternoon)

84 table-candidate pages captured via OCR-index queries ('VOTE PCT'
was the key phrase - user's find; windows E+1..E+5 after E+1..E+2
proved too strict). Vision agents read them with PCT-column
validation; every ingested row re-verified against the scan. Night
floors now: 1960 (91.4), 1973 (57.9 single-candidate floor, dim),
1974-06 (44.9 partial, dim), 1976-11 (59.1 partial, dim), 1978-06
(46.6 partial, dim), 1979-11 (93.9!), 1980-11 (93.0!), 1982-11 day-1
(96.7), 1983-11 (83.6), 1984-11 (94.6) + 1982-06 day-2. 74 elections.

CONTRADICTION (excluded, needs SOS 1978 SOV): the Nov 8 1978 'S.F.
VOTE' box is internally PCT-consistent but its governor sum (223,147)
exceeds the DOE-certified ballots (217,965) under a '62.1% of
precincts' label. Night-feed inflation or DOE-row error.

STILL DRY pre-1985: 1964 (captures clipped before the vote box),
1968, 1972-11, 1975-11, 1975-12, 1977-08 (pct-only page), 1977-11
(captured the election-DAY issue by mistake), 1981-11 (front-page
scan top only), 1983-04 recall (no totals on captured pages),
1984-06 (pct-only box). Each needs issue-page browsing (Page N of 80
navigation) or accepts the floor-only status.

## Open threads

1. **CNN 2000 night estimate** (~83% of contest votes) — needs a design
   decision: "estimated night share" marker type in NightShareChart.
2. **DOE records request** (user-side) — pipeline ingests directly.
3. **Mirror CDN upload** (user-side); manifest committed.
4. Possible: BOS journal declarations (SFPL, offline) for pre-1995 cert
   dates; ProQuest print-Chronicle for the 1995-12/1996/1997 night-of
   holes (print edition carried count tables the web never did).

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

## Session 2026-06-12 — flip round 2 + trailing re-harvest (post auth-wall fix)

The 2026-06-11 ezproxy expiry poisoned two operations; both scripts now
hard-abort (process.exit 2) on the SFPL auth page ('Articles and
Databases - Authentication'). Re-run was clean: 61/61 trailing docs
(corpus now 793), 148 day-after pages captured across all 12 round-2
issues, zero auth garbage.

### Ingested this session (data/sf_archival_canvass_points.csv)

Trailing harvest (2000s):
- 2000-03-07 d2 92.4% — floor, "16,000 more absentee and provisional"
  (doc 0EB4F91262A37D59).
- 2001-12-11 d2 93.3% — printed chart "Ballots counted 70,244"; internally
  consistent (Herrera/Lazarus pcts; 70,244+5,100 ≈ certified 75,267).
- 2007-11-06 NIGHT 32.2% — exact: "only 48,104 absentee and early votes"
  released Tuesday night (ES&S decertification; every polling-place ballot
  hand-checked). Marked night_partial (operational one-off, like 1995-12).

Flip round 2 (the off-by-one fix worked — label E+2 = true day-after paper):
- 1964-11-03 NIGHT 93.5% — president sum 310,193, 1341/1341 precincts.
- 1968-11-05 NIGHT 83.4% — president sum 255,938 at 1140/1282 (press
  deadline); marked night_partial.
- 1972-11-07 NIGHT 92.3% — president sum 292,341, 1308/1351; > certified
  precinct ballots 289,010 ⇒ night count included absentees.
- 1975-11-04 NIGHT 97.4% — 11-candidate mayor sum 209,980 at 99.19% of 942
  precincts; > precinct ballots 206,167 ⇒ absentees in night count;
  Barbagelata−Feinstein gap 1,196 matches "about 1200 votes" narrative.
- 1977-11-08 NIGHT 98.8% — PROSE: "final, unofficial results... 51.2
  percent of the city's 339,306 registered voters"; rounding-safe floor
  0.5115×339,306 = 173,555. Beats every contest sum (no undervote).
- 1981-11-03 NIGHT 91.4% — Prop B (cable car fare) sum 91,078, 100%
  reporting, pct-validated; > precinct ballots 88,783.

Era finding: 1972/1975/1981 night sums each exceed the DOE precinct-ballot
column ⇒ SF counted absentees ON election night through at least 1981.
The in-person "diamond" floors for that era are therefore conservative in
the right direction.

### Rejected / not ingested (with reasons)

- 2001-11-06 "almost 15,000 yet to be counted" (Nov 7 paper) — implies
  ≥119,024 night, but the city's own page showed 115,477 at d2. Registrar
  estimate too low; floor unsafe.
- 1964 SENATE line (Salinger 197,863 + Murphy 125,716 = 323,579) — digits
  re-verified as printed, but sum exceeds certified precinct ballots
  313,134 while the president line fits precinct-only. Internal newspaper
  inconsistency (senate > president). Logged, unused.
- 1972-06 Dem-primary sum 132,109 (56.3%) and 1984-06 Prop 24 sum 135,327
  (74.9%) — both below their in-person floors; recorded in readings only.
- 1972-11 senate sum 278,365 (after digit corrections) — superseded by the
  recovered full president line.
- 1975-12 runoff — Dec 12 paper pages 1-3, 20 carry prose only ("about 66
  per cent" turnout = final estimate, matches certified 66.42%; not a
  count statement). Table location unknown; pages 4-19 OCR lack Moscone.
- 1977-08 — district map prints percentages only, no absolute counts.

### Verification protocol (worked; keep)

Haiku readers (4 parallel + 1 sweep) transcribe with incremental CSVs →
arithmetic gates vs DOE certified columns catch impossible sums (caught:
"Moscone 661,495", Powell 264,424 > total ballots, 1964 senate) → Sonnet
verifiers re-read load-bearing digit strings blind (corrected three 1972
digits, recovered the McGovern line, found the 1977 turnout prose).
Ingestion rule: a contest-sum floor only matters if it beats the
in-person floor (precinct/certified); prose ballots-cast statements beat
contest sums (no undervote).

Readings: scans/readings_F..J.csv (haiku passes), readings_V1/V2.csv
(sonnet verification), readings_R.csv (hi-res 1983/1976 re-read).
Hi-res recaptures: scans/hi_*.png (2400×2600 window).

### Still open after this session

- 1983-04 recall totals (hi-res re-read in flight at ledger time).
- 1976-06 Vote Tally (same).
- 1975-12 runoff numbers — not in captured pages; would need full-issue
  page-walk past p20 or SOV.
- 1960s gaps: 1972-06 GOP primary line could beat its floor if a Republican
  presidential sum is ever recovered; 1977-08 needs a different source.

### Session 2026-06-12, part 2 — user-verified digits, pan captures, runoff resolution

User hand-verified the key scans: confirmed 1964 (incl. the senate
anomaly as-printed), 1968, 1975-11, 1977-11; corrected 1972-11 precincts
to 1300/1351 (was misread 1308).

Pan-capture technique (mouse-drag the OSD canvas, 3 vertical slices/page)
solved the cut-canvas problem - canvas captures only hold the visible
viewport, so front-page ledes below the fold were systematically missing.

New ingestions (part 2):
- 1983-04-26 NIGHT 93.5% — front-page 'FINAL VOTE ON RECALL' box with
  absentee/precinct split: 51,033 absentees counted ELECTION NIGHT of a
  35%-absentee election. Rows/pcts fully internally consistent.
- 1975-12-11 runoff NIGHT 99.0% — Moscone 101,528 / Barbagelata 97,213,
  942/942, victory claimed 11:16 p.m. A 2.2-point race settled by
  midnight: the sharpest old-vs-new contrast in the dataset.
- 2001-11-06 d3 90.3%, 2002-03-05 d2 84.0% + d7 97.3%, 2008-11-04 NIGHT
  65.0% — from the broadened 2000s harvest.

RUNOFF DATE RESOLVED (and a method rule): the Dec 1975 runoff was held
THURSDAY Dec 11, 1975 — masthead-verified: Thu 12/11 front page reads
"S.F. Picks A Mayor Today"; Fri 12/12 carries full results. DOE's date
was right; the Tuesday-law prior does not hold for this charter-era
runoff. RULE: NewsBank issue labels are NOT uniformly offset from
masthead dates (1983 label = masthead+1; 1975-12 label = masthead).
Masthead-verify every issue before assigning observation dates.

2000s harvest gap found by user pressure: the original trailing window
started at E+2, skipping day-after papers entirely; query set too narrow.
Re-harvest E+1..E+14 with 7 queries over 20 thin elections: 113 new docs
(corpus 907). Rejected: 2010-11 "as many as 85,000 left" (implies 70.1%
vs the city's own 67.0% at d3 - estimate too low); 2000-12-12 "early
results showed about 30 percent went to the polls" (projection-vs-counted
ambiguity; logged next to the CNN-2000 estimate thread).

Open: 1964 senate-vs-DOE-split anomaly (needs 1964 SOV - not online; via
HathiTrust or records request); 1977-08 (pct-only); 2009-05/2009-11 (zero
Chronicle hits even with broad queries - likely web-era gap, DOE records
request is the fix).

### Session 2026-06-12, part 3 — section-B print boxes + wayback DOE summary pages

Two veins (both user-instigated) filled most of the remaining 2000s gaps:

Print results boxes (image edition, section B of the day-after paper):
- 2008-02-05 NIGHT 63.1% (partial, 450/580) — Prop A 121,068/48,772, pct
  validates exactly. Found by the user on p B3.
- 2008-06-03 NIGHT 62.8% (partial, 515/580) — Prop A (SFUSD parcel tax)
  75,599/33,012, pct validates. Found by the playbook sweep (pages 20-26,
  pan-until-bottom, tesseract TSV word-coords to locate the SF column).

Wayback DOE "Election Summary" pages (live-stamped, every figure
re-verified against the capture before ingestion):
- 2009-11-03 NIGHT 68.3% — complete 428/428 release stamped 10:14 PM.
- 2009-05-19 d8 97.3% (was: zero observations).
- 2008-06-03 d1 74.0% / d3 84.9% / d10 96.9% (was: zero observations).
- 2008-02-05 d3 89.7% / d6 93.3% / d10 95.9% / d20 99.8%.

Misdated-row correction: the existing 2008-02 "d6 81.4%" row (Unofficial
Summary Report #8 PDF) was stamped with its wayback CAPTURE time; the
PDF's own footer reads "February 06, 2008 3:31 PM" — it is a DAY-1
report. Re-stamped; the 2008-02 curve is now monotone night 169,840 →
d1 219,206 → d3 241,426 → d6 251,150 → d10 258,249 → d20 268,704 →
certified 269,212. (Caught because the new verified d6 contradicted it —
the arithmetic gates work on timestamps too.)

Confirmed dry: 2004-03-02 (no wayback captures of any results page within
21 days; print box not yet swept - TODO). Duplicates skipped: 2009-11 d3
and 2002-12 d6/7 (already in dataset from the same sources).

Remaining 2000s print-box sweep targets: 2002-12-11, 2004-03-03,
2010-06-09, 2010-11-03, 2011-11-09, 2012-06-06, 2012-11-07 (+ night-of
for 2000-11, 2004-11, 2005-11, 2006-06, 2006-11).

### Session 2026-06-12, part 4 — parallel section-B sweeps (12 issues)

Pre-located SF columns via tesseract TSV word coordinates and handed
readers ready-made crops (no crop_helper fumbling). Ingested: 2004-03
NIGHT 75.1% (Measure H 143,244, 577/577 - the wayback-dry election,
print was its only source) and 2006-06 NIGHT 66.3% (Measure B 103,555,
578/578). Rejected: 2012-06 "SF D5 supervisor Tissler 59,830" - that is
San Mateo's District 5 (Tissier); SF had no June 2012 supervisor race.
Sub-citywide contests (CD-8 2006/2010) recorded but can't beat in-person
floors. Boxes NOT in swept ranges (second-pass targets): 2000-11,
2002-12, 2004-11, 2005-11, 2006-11, 2010-06, 2010-11, 2012-06.

### Session 2026-06-12, part 5 — second-pass sweeps close the print vein

Pass 2 (widened ranges, 8 issues): 2010-06 NIGHT 64.7% (Prop 16 SF row,
100,698) and 2012-06 NIGHT 73.2% (Prop 29 SF row, 106,273) - both from
statewide-proposition county tables, pct-validated, press-deadline
partials. 2004-11's box held only elect-4 pools (weaker than the
existing 74.9% d0 release). PRINT VEIN NOW EXHAUSTED for: 2000-11,
2002-12, 2005-11, 2006-11, 2010-11 (ranges swept: 20-40, 12-25, 12-26,
18-33, 15-30 respectively; no SF results box found). Those five night
slots are the remaining ask for the DOE records request.

### Session 2026-06-12, part 6 — the text archive had the tables all along

The Chronicle ran 'HOW SAN FRANCISCO VOTED' as a standing results table
from at least 1986 through 2002, and the NewsBank TEXT archive carries
it as parseable text - no image scanning needed. One harvest (33 thin
elections x E+1/E+2, 52 docs) + a local regex parse (YES/NO pairs,
certified-cap filter to reject statewide/other-county tables, monotone
gates) yielded 16 floors in one pass:

NIGHT (E+1 papers): 1987-11 91.3%, 1990-06 79.5%, 1990-11 82.6%,
1992-06 84.8%, 1996-11 93.4%, 1997-11 87.3%, 2000-03 83.6%,
2001-11 80.5% (629/648).
Day-2 (E+2 papers, conservative): 1986-06 86.0%, 1990-11 86.7%,
1996-03 89.0%, 1998-06 84.4%, 1998-11 74.0%, 2000-11 77.7%,
2002-03 74.9%, 2002-11 78.2%.

Remaining 1985-2005 night gaps (candidate-format tables in harvested
docs, need structured parse or image): 1985-11, 1986-11 (Part I/II
docs), 1987-04, 1987-06, 1987-12 (Agnos landslide, 711/711 doc in
corpus), 1988-06, 1992-11, 1993-11, 1994-11, 1995-11, 1996-03 night,
1998-11 night, 1999-11, 1999-12 runoff, 2002-12, 2003-10, 2005-11.

### Session 2026-06-12, part 7 — round-2 text harvest

1988-06 NIGHT 83.4% ('SAN FRANCISCO' table, 619/619); 1987-12 Agnos
runoff NIGHT 94.4%; 1986-11 d2 93.9%; 2005-11 d2 70.2%; 1999-12
Brown-Ammiano runoff d2 94.3% (DOE-itemized 13,000 remaining).
STILL OPEN (no SF table doc in text archive; image sweep or records
request): 1985-11, 1987-04, 1987-06, 1992-11, 1993-11, 1995-11
(Brown-Jordan), 1996-03 night, 1999-11, 1999-12 night, 2002-12,
2003-10, plus the five 2000s print-exhausted slots.

### Session 2026-06-12, part 8 — 1999-11 and the county-series dead end

1999-11 d1 50.9% floor ingested ('sent home with roughly 100,000
ballots uncounted' - the Ammiano write-in hand-count). CONFIRMED: the
SF edition of the Chronicle's county-by-county results series
(1992-1999) is NOT in the NewsBank text archive (sibling counties all
present; SF ran as a graphic). Remaining night/table gaps need image
sweeps of specific day-after papers: 1985-11, 1987-04, 1987-06,
1992-11, 1993-11, 1995-11, 1996-03(night), 1999-11(night), 1999-12,
2002-12, 2003-10 - or the DOE records request.

### Session 2026-06-12, part 9 — final sweeps wrap

1992-11 NIGHT 80.9% (partial 513/609, masthead-verified day-after) and
1996-03 NIGHT 59.7% (partial 400/650) ingested. E+2 papers for 1968/
1976/1978 carry NO tables - those dim partials are print-final. 1974-06
'complete' table REJECTED: Prop B sum 203,381 > certified 198,508
(printed contradiction, like 1978-11). 1973 single-candidate floor was
already complete-precinct. Label offsets vary PER ISSUE (1995 label =
masthead; 1983 = masthead+1) - masthead-verify always. Still open for
records request: 1985-11, 1987-04/06, 1993-11, 1995-11, 1999-11/12
night, 2000-11, 2002-12, 2003-10, 2005-11/2006-11/2010-11 night.

### Session 2026-06-13 — Examiner vein probed and closed

NewsBank's "San Francisco Examiner" is the post-2006 Examiner.com blog
network (8 harvested docs, all out-of-county blog content); the print
afternoon Examiner is not in Access World News for any year. Print
Examiner = microfilm-only (SFPL / CA State Library) - now listed as the
top researcher ask on the public search log.
