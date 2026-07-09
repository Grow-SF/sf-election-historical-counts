# County Election-Night Dataset Expansion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fill the null election-night plateau rows that keep 8 researched counties off the "Election-night share over time, by county" chart, then widen the dataset with 2 new archive-friendly counties (one a no-new-tech control), taking the chart from 6 to 10+ panels.

**Architecture:** This is a research program, not a code change. All data flows through the existing pipeline: `data/research/election-night/<slug>.json` (hand-edited, surgical) -> `scripts/build_county_night.py` -> `packages/data/county_night.json` -> chart. The new work is source routes never tried before: NewsBank print archives via SFPL, non-Wayback web archives, URL enumeration, and registrar social media. Public records (CPRA) requests are ruled out by the operator; automated source recovery only.

**Tech Stack:** curl + jq + pdftotext, puppeteer-core against a debug-port Chrome (NewsBank), the existing `scripts/research/` verifiers, python3, pnpm/vitest.

**Spec:** `docs/superpowers/specs/2026-07-09-county-night-data-expansion-design.md`
**Authority:** `docs/research/RUNBOOK.md`. When this plan and the RUNBOOK disagree, the RUNBOOK wins. Read it in full before executing any task.

## Global Constraints

- Metric: election-night % = ballots in the LAST report posted on election night / certified final ballots from the CA SoS SOV (RUNBOOK section 1). Never the 8 p.m. first tranche, never a post-night canvass number as a plateau, never a registered-voter denominator.
- Calibration: a candidate number near HALF the like-for-like SF share (SF: 71% '12, 66% '16, 59% '18, 51% '22, 57% '24) is the first tranche; a number well ABOVE the county's adjacent elections is canvass-contaminated. Reject both or land them per RUNBOOK 5.2 (floor / ceiling+comparable:false).
- Newspaper-derived numbers are `confidence: "secondary"`. An explicit "N ballots were counted" end-of-night statement is usable directly; a same-contest ratio floor (candidate votes / printed percent, with precincts-reporting quoted) lands as a documented FLOOR.
- County JSON edits are SURGICAL string replacements, never whole-file rewrites (RUNBOOK section 2). Percent units, 2dp max.
- After ANY data change, run the FULL section-3 pipeline (commands in the Row-Landing Procedure below); all green before commit.
- Notes are the evidence trail (RUNBOOK 5.4): exact quote, docref/URL, arithmetic, what it is NOT, dead ends included, copy-pasteable. Corrections APPEND dated sentences.
- Dead ends are deliverables: a row that stays null gets its note EXTENDED with a dated sentence listing the new routes tried and the exact queries.
- NewsBank: one session at a time, isolated debug-port Chrome, never from parallel subagents, browser otherwise idle. Captures go to gitignored `mirror/newsbank/`; only citations and derived numbers are committed.
- Research subagents persist findings to disk after EACH item (one file per item under `docs/research/night-recovery-2026-07-09/county-en/`), 1-2 rows per subagent.
- No em dashes in any prose (notes, VERIFY.md, commit messages).
- Derived files (`packages/data/county_night.json`, `MACHINE_CHECK.md`, `HUMAN_VERIFY.md`) are regenerated, never edited.

## Row-Landing Procedure (referenced by Tasks 2-10; "land the row" means exactly this)

Given: slug, date, plateau ballots N, certified final D (already in the JSON), source URL/docref, evidence quote.

1. Compute pct = round(N / D * 100, 2). Check it against the calibration band in the task.
2. Surgical edit of `data/research/election-night/<slug>.json` for that date's row: set `election_night_ballots`, `election_night_pct`, `source_url_night`, `confidence: "secondary"` (or "primary" if an official release republished verbatim), and APPEND to the note (JSON-escaped) the dated evidence sentence: quote, docref, arithmetic, plateau reasoning, first-tranche number it is NOT. If the value is a floor, say "floor" in the note. Verify old substring occurs exactly once before replacing:
   ```bash
   python3 - <<'EOF'
   import pathlib
   p = pathlib.Path('data/research/election-night/<slug>.json')
   t = p.read_text()
   old = '"election_night_ballots": null'  # scoped: count occurrences first, use a longer context string if >1
   assert t.count(old) == 1, t.count(old)
   EOF
   ```
3. If the source is auth-walled or JS-only (every NewsBank docref is), add an entry to `data/research/election-night/render_verified.json`: `{"slug": ..., "date": ..., "url": <the cited URL>, "evidence": <string containing the claimed number verbatim>, "method": "newsbank-sfpl-manual"}` so the machine numerator pass does not flip the row to NOT_FOUND.
4. Update the county's VERIFY.md summary table cell and detail bullet (numerator URL, denominator URL, "look for" text). The validator cross-checks this; skipping it fails the pipeline.
5. Add/update the row's verdict in `plateau_review.json` (CONFIRMED needs a non-circular leg per RUNBOOK section 8; a morning-after "end of election night" official statement quoted in print qualifies; otherwise PLAUSIBLE).
6. If the row previously cited a different URL, delete the stale numerator cache: `rm -f data/research/election-night/cache/numerators/<slug>-<date>.*`
7. Run the full pipeline; every command must succeed:
   ```bash
   python3 scripts/research/validate_election_night.py
   python3 scripts/build_county_night.py
   python3 scripts/research/verify_en_denominators.py
   python3 scripts/research/verify_en_numerators.py
   python3 scripts/research/build_en_verification_report.py
   uv run pytest tests/test_verify_election_night.py -q
   pnpm vitest run
   ```
8. Commit the county JSON + VERIFY.md + plateau_review.json + render_verified.json (if touched) + regenerated county_night.json/MACHINE_CHECK.md/HUMAN_VERIFY.md together:
   ```bash
   git add data/research/election-night/ packages/data/county_night.json
   git commit -m "data: <county> <year> election-night plateau from <source>"
   ```
9. Note for the end-of-phase report to the operator: which rows landed secondary or non-CONFIRMED, path + claimed value + what a failed hand-check looks like.

A row that stays null follows the same procedure minus the number: append the dated dead-end sentence to the note (step 2), regenerate (step 7), commit as `data: <county> <year> dead-end note, <routes> exhausted`.

---

### Task 1: NewsBank session bring-up and coverage probe

**Files:**
- Create: `docs/research/night-recovery-2026-07-09/county-en/00-newsbank-coverage.md`

**Interfaces:**
- Consumes: `docs/archive-recovery-runbook.md` (prerequisites section), `scripts/archive-recovery/session_probe.js`, `harvest_text.js`.
- Produces: a go/no-go per paper x year that Tasks 2-7 read before searching.

- [ ] **Step 1: Bring up the session.** Ask the operator to log in to SFPL ezproxy, then launch the isolated Chrome:
  ```bash
  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
    --remote-debugging-port=9222 \
    --disable-background-timer-throttling \
    --disable-renderer-backgrounding \
    --disable-backgrounding-occluded-windows
  ```
  Run `node scripts/archive-recovery/session_probe.js`; it must load a known doc, not the auth wall.
- [ ] **Step 2: Probe coverage.** In NewsBank Access World News (all-publications search), confirm each paper exists as a TEXT source for the needed windows, by running one search per paper x election with terms like `ballots counted` restricted to the day after the election. Papers x windows:
  | paper | needed windows (day after) |
  |---|---|
  | Sacramento Bee | 2016-11-09 |
  | San Jose Mercury News | 2016-11-09, 2018-11-07 |
  | Fresno Bee | 2012-11-07, 2014-11-05, 2018-11-07, 2022-11-09 (also covers Madera) |
  | Madera Tribune | 2012-11-07, 2014-11-05 |
  | San Diego Union-Tribune | 2012-11-07, 2014-11-05, 2016-11-09 |
  | Press-Enterprise (Riverside) | 2012-11-07, 2014-11-05, 2016-11-09, 2018-11-07 |
  | San Bernardino Sun | 2012-11-07, 2014-11-05, 2016-11-09, 2018-11-07, 2022-11-09 |
  Record hit/miss per cell in `00-newsbank-coverage.md` as you go (persist after each cell, not at the end).
- [ ] **Step 3: Commit** the coverage file. Tasks 2-7 skip any cell recorded as a miss.

### Task 2: Sacramento 2016 (one row from a new chart panel)

**Files:**
- Modify: `data/research/election-night/sacramento-ca.json` (2016-11-08 row), `VERIFY.md`, `plateau_review.json`, `render_verified.json`
- Create: `docs/research/night-recovery-2026-07-09/county-en/sacramento-2016.md` (findings log, persisted as you go)

**Interfaces:**
- Consumes: Task 1's coverage go/no-go; the live NewsBank session (serialize with Tasks 3-7).
- Produces: possibly the 7th chart panel (Sacramento's only gap).

- [ ] **Step 1: Search the Sacramento Bee, Nov 9-10 2016 editions,** all-publications search restricted to the Bee. Queries, in order: `"ballots counted"`, `"ballots cast"`, `"votes counted" election night`, `LaVine ballots` (Jill LaVine was the registrar), `turnout Sacramento County`. Also try the Nov 9 live-blog/wire pieces: `precincts reporting Sacramento County`.
- [ ] **Step 2: Extract the number.** Accept: an explicit countywide ballots-counted total attributed to election night ("by the end of the night, N ballots..."), or a same-contest ratio floor from a countywide contest with precincts-reporting quoted. The row's note says the true plateau is likely ~60-63% of 575,711 (i.e. ~345k-363k ballots); the Friday canvass upper bound is 385,520; the first tranche would be far lower. Reject anything at or above 385,520 (canvass) unless the article explicitly timestamps it to election night.
- [ ] **Step 3: Save the docref** and full quoted sentences to the findings log and `mirror/newsbank/` per the archive-recovery runbook.
- [ ] **Step 4: Land the row** per the Row-Landing Procedure (calibration band: 55-67% clean; below ~40% = tranche; >=66.96% = canvass ceiling territory). If nothing usable: extend the dead-end note ("Sacramento Bee Nov 9-10 2016 searched via NewsBank/SFPL on 2026-XX-XX, queries listed, no countywide election-night total published") and land the null.

### Task 3: Santa Clara 2016 and 2018 (Mercury News)

**Files:**
- Modify: `data/research/election-night/santa-clara-ca.json` (2016-11-08, 2018-11-06 rows), `VERIFY.md`, `plateau_review.json`, `render_verified.json`
- Create: `docs/research/night-recovery-2026-07-09/county-en/santa-clara-2016.md`, `santa-clara-2018.md`

**Interfaces:**
- Consumes: Task 1 coverage; NewsBank session (after Task 2 finishes with it).
- Produces: possibly the 8th chart panel (these are Santa Clara's only nulls).

- [ ] **Step 1: 2016.** Search San Jose Mercury News Nov 9-10 2016: `"ballots counted" Santa Clara`, `"ballots cast" county`, `registrar of voters ballots`, `precincts reporting Santa Clara County`. The certified final is 724,596 (already in the JSON row; always read the denominator from the row, never re-derive it). Calibration: adjacent clean points are 67.1% (2012) and the 62.26% next-day ceiling (2014); expect roughly 55-65% for a clean 2016 plateau; any number near or above the certified total is canvass.
- [ ] **Step 2: 2018.** Same paper, Nov 7-8 2018: same query set. The row's note establishes 443,266 (Nov 11) is a DEEP CANVASS count at 70.9%; the true plateau is meaningfully lower. Expect a midterm plateau in the 50s-60s.
- [ ] **Step 3: Land each row** independently per the Row-Landing Procedure, one commit per row, findings persisted per row. Null rows get the dated dead-end extension.

### Task 4: Madera 2012 and 2014 (Fresno Bee, Madera Tribune)

**Files:**
- Modify: `data/research/election-night/madera-ca.json` (2012-11-06, 2014-11-04 rows), `VERIFY.md`, `plateau_review.json`, `render_verified.json`
- Create: `docs/research/night-recovery-2026-07-09/county-en/madera-2012.md`, `madera-2014.md`

**Interfaces:**
- Consumes: Task 1 coverage; NewsBank session.
- Produces: possibly the 9th chart panel (Madera's only nulls).

- [ ] **Step 1: 2012.** Search Fresno Bee and Madera Tribune Nov 7-8 2012: `Madera ballots`, `Madera County votes counted`, `Madera turnout`. Certified final 40,325. Calibration: Madera 2016 = 80.0%, so expect a 2012 presidential plateau roughly 70-85% (small precinct-based county, counts fast); the first tranche would be under ~45%.
- [ ] **Step 2: 2014.** Same papers Nov 5-6 2014. Certified final 27,370; expect roughly 65-80% (midterm).
- [ ] **Step 3: Small-county fallback.** If the dailies have nothing, the weekly Madera Tribune's Thursday edition often prints the registrar's semi-final table with precincts reporting; a "with all N precincts reporting" table sum is a valid floor.
- [ ] **Step 4: Land each row** per the Row-Landing Procedure.

### Task 5: San Diego 2012, 2014, 2016 (Union-Tribune)

**Files:**
- Modify: `data/research/election-night/san-diego-ca.json` (three rows), `VERIFY.md`, `plateau_review.json`, `render_verified.json`
- Create: `docs/research/night-recovery-2026-07-09/county-en/san-diego-<year>.md` (one per year)

**Interfaces:**
- Consumes: Task 1 coverage; NewsBank session.
- Produces: possibly the 10th chart panel.

- [ ] **Step 1: Per year (2012-11-07, 2014-11-05, 2016-11-09 editions),** search the U-T: `"ballots counted"`, `registrar Vu ballots` (Michael Vu was ROV from 2013), `"mail ballots" remaining counted`, `precincts reporting San Diego County`. U-T morning-after coverage habitually states both the counted total and the uncounted-mail estimate; the counted total attributed to the end of the night is the plateau. Certified finals: 1,203,265 (2012), 692,434 (2014), 1,346,513 (2016), already in the JSON.
- [ ] **Step 2: Calibration:** SD 2018 = 45.72 and 2022 = 54.24 are post-2018 all-VCA-era; pre-2018 precinct-era SD should look like LA/Orange: roughly 65-78% (2012), 60-75% (2014), 60-70% (2016). A number under ~40% is the first tranche.
- [ ] **Step 3: Land each row** per the Row-Landing Procedure, one commit per row.

### Task 6: Fresno 2012, 2014, 2018, 2022 (Fresno Bee)

**Files:**
- Modify: `data/research/election-night/fresno-ca.json` (four rows), `VERIFY.md`, `plateau_review.json`, `render_verified.json`
- Create: `docs/research/night-recovery-2026-07-09/county-en/fresno-<year>.md` (one per year)

**Interfaces:**
- Consumes: Task 1 coverage; NewsBank session.
- Produces: Fresno needs all four to reach the chart; partial recoveries still improve the dataset and pre/post stats.

- [ ] **Step 1: Per year** (editions of Nov 7 2012, Nov 5 2014, Nov 7 2018, Nov 9 2022), search the Fresno Bee: `"ballots counted"`, `Orth ballots` (Brandi Orth, county clerk 2011-2022), `"votes counted" Fresno County`, `precincts reporting Fresno County`. Certified finals already in the JSON: 261,652 / 163,420 / 256,972 / 221,419.
- [ ] **Step 2: Calibration:** Fresno 2016 = 60.7%, 2024 = 62.36%. Expect ~55-70 (2012), ~50-65 (2014), ~50-65 (2018); 2022 is post-VCA all-mail, expect ~30-50 (compare Sacramento 2022 = 29.94, San Diego 2022 = 54.24).
- [ ] **Step 3: Land each row** per the Row-Landing Procedure, one commit per row.

### Task 7: Riverside 2012-2018 and San Bernardino 2012-2022 (Press-Enterprise, SB Sun)

**Files:**
- Modify: `data/research/election-night/riverside-ca.json`, `san-bernardino-ca.json`, `VERIFY.md`, `plateau_review.json`, `render_verified.json`
- Create: `docs/research/night-recovery-2026-07-09/county-en/riverside-<year>.md`, `san-bernardino-<year>.md`

**Interfaces:**
- Consumes: Task 1 coverage; NewsBank session.
- Produces: dataset depth (these two need too many rows to reach the chart this pass, but every landed row feeds the pre/post comparison).

- [ ] **Step 1: Riverside, per year 2012/2014/2016/2018** (morning-after editions): `"ballots counted" Riverside County`, `registrar of voters ballots`, `precincts reporting Riverside County`. Riverside counted notoriously slowly in this era (2010s "slow count" coverage is extensive); morning-after pieces usually state exactly how many were counted by end of night. Calibration: Riverside 2022 = 34.0%; the precinct-era numbers should be higher, ~55-75.
- [ ] **Step 2: San Bernardino, per year 2012/2014/2016/2018/2022:** same query set against the Sun and the Press-Enterprise (they shared SCNG coverage after 2016). Calibration: SB 2024 = 56.24%.
- [ ] **Step 3: Land rows** per the Row-Landing Procedure, one commit per row, nulls get dated dead-end extensions. This task is the largest; batch it as one subagent per year x county with findings persisted per row.

### Task 8: Alternate web-archive sweep (rows still null after Tasks 2-7)

**Files:**
- Modify: the still-null county JSONs' notes, plus any landed rows' full file set
- Create: `docs/research/night-recovery-2026-07-09/county-en/altarchive-<slug>-<year>.md` per attempted row

**Interfaces:**
- Consumes: the list of still-null rows after the NewsBank phase.
- Produces: landed rows or dead-end note extensions naming each archive checked.

- [ ] **Step 1: Build the target-URL list per row** from the existing dead-end notes; they name the exact live-results URLs that Wayback missed (e.g. Fresno `www2.co.fresno.ca.us/2850/Results/Results20121106.htm`, San Bernardino `www.sbcounty.gov/rov/elections/Results/<date>/content/results.aspx`, Riverside `voteinfo.net/Elections/<date>/eresults/`, Sacramento `eresults.saccounty.net`, `sacresults.e-cers.com`).
- [ ] **Step 2: Library of Congress United States Elections Web Archive.** For each URL: `curl -sI "https://webarchive.loc.gov/all/<Nov-window-ts>*/<url>"` and browse `https://webarchive.loc.gov/all/*/<url>` for a capture list. LoC crawled state/county election sites intensively around each November general; it is a genuinely independent crawl from Wayback's.
- [ ] **Step 3: Common Crawl.** List crawls: `curl -s https://index.commoncrawl.org/collinfo.json | jq -r '.[].id'`. For each election, query the bracketing crawls (e.g. 2016: CC-MAIN-2016-44 and CC-MAIN-2016-50): `curl -s "https://index.commoncrawl.org/CC-MAIN-2016-50-index?url=<url-encoded>&output=json"`. On a hit, fetch the WARC slice: `curl -s -r <offset>-<offset+length-1> "https://data.commoncrawl.org/<filename>" | gunzip | head -200`.
- [ ] **Step 4: Archive-It (CDL California collections).** Capture list: `curl -s "https://wayback.archive-it.org/all/timemap/link/<url>"`; replay `https://wayback.archive-it.org/all/<ts>/<url>`.
- [ ] **Step 5: archive.today.** Browser-only (bot wall): from the main session, load `https://archive.ph/https://<url>` and read the capture list. Cheap to check, record hit/miss.
- [ ] **Step 6:** For any capture found in the election-night window, extract the ballots-cast figure (gunzip if the bytes start `1f 8b`; render JS shells with `WB_URL=... node scripts/research/render_wayback.cjs` adapted to the archive's replay URL), then land the row (confidence primary if it is the county's own page). Rows with no hits get one dated dead-end sentence naming all four archives and the query forms.

### Task 9: URL/ID enumeration probes and registrar social media

**Files:**
- Modify: affected county JSONs on hits; notes on misses
- Create: `docs/research/night-recovery-2026-07-09/county-en/enum-probes.md`

**Interfaces:**
- Consumes: still-null rows; the URL patterns recorded in existing notes.
- Produces: landed rows or note extensions.

- [ ] **Step 1: Fresno report-file enumeration.** The frozen night file pattern is `electionsummaryreportrpt_<M_D_YY>_<HHMM>.pdf` (known-good 2016 instance in the fresno JSON). For 2012/2014/2018/2022, probe plausible timestamps against BOTH the live host and Wayback:
  ```bash
  for t in 2230 2300 2330 0000 0030 0100 0130 0200; do
    curl -s -o /dev/null -w "%{http_code} $t\n" "https://www2.co.fresno.ca.us/2850/Results/electionsummaryreportrpt_11_6_12_${t}.pdf"
  done
  ```
  (2s pause between probes; adjust filename date per year; also try the pattern via Wayback CDX with `matchType=prefix` on the Results/ directory.)
- [ ] **Step 2: DocumentCenter ID walks.** Nevada County's reports live at guessable `DocumentCenter/View/<id>` IDs (55078 = 2024 third report). For counties on the same CMS (check Placer, Madera), CDX-list the DocumentCenter path prefix for the election window and probe +/-50 IDs around any hit for sibling night reports. Log every probe range in `enum-probes.md`.
- [ ] **Step 3: Registrar social media via Wayback.** CDX-enumerate captures of the registrars' accounts for election week:
  ```bash
  curl "http://web.archive.org/cdx/search/cdx?url=twitter.com/sacvote&from=20161108&to=20161112&output=json&limit=40"
  ```
  Accounts to try per county: @sacvote (Sacramento), @sdvote (San Diego), @SBCountyROV (San Bernardino), @RivCoVote (Riverside), @FresnoCoClerk (Fresno). Also the counties' Facebook page captures. A tweeted "final election night report: N ballots counted" is registrar-primary evidence.
- [ ] **Step 4: Land hits / extend notes** per the Row-Landing Procedure.

### Task 10: New-county scouting (Clarity CDN + press-release archives + control candidates)

**Files:**
- Create: `docs/research/night-recovery-2026-07-09/county-en/new-county-scout.md`

**Interfaces:**
- Produces: a ranked candidate memo with, per county: Clarity election IDs per year (or press-release archive URL), tech-adoption sketch, estimated rows recoverable. Tasks 11-12 consume it.

- [ ] **Step 1: Clarity scout.** For each of the 58 CA county names (URL form with underscores): `curl -s "https://results.enr.clarityelections.com/CA/<County>/current_ver.txt"` to detect Clarity use, then CDX-enumerate historical election IDs: `curl "http://web.archive.org/cdx/search/cdx?url=results.enr.clarityelections.com/CA/<County>*&from=20121101&to=20181201&output=json&limit=200&matchType=prefix"`. For each Nov-general election ID found, check JSON availability (`.../json/sum.json` on an early version) since Web01-era HTML-only versions are unrecoverable. Record per county x year: JSON yes/no.
- [ ] **Step 2: Press-release scout.** For 4-6 non-Clarity counties with large-county newsrooms (Alameda, Contra Costa, Ventura, Kern, Sonoma, Stanislaus), check for an LA-style morning-after "semi-final results" release archive: browse `<rov site>/news` current + Wayback captures of the same path for 2012-2018.
- [ ] **Step 3: Control-candidate scout.** Using the `researching-jurisdiction-counting-tech` skill's quick pass, identify 2-3 counties with NO e-pollbooks, NO ASV, and NO VCA through 2024 (SF-like controls). Verify against CA SoS VCA county lists and vendor press releases before nominating.
- [ ] **Step 4: Rank and commit the memo.** Rank = (years recoverable from immutable/official sources) x (fills a gap in the adoption-year spread or adds a control). Commit; report the ranking to the operator.

### Task 11: Add new county #1 end to end

**Files:**
- Create: `data/research/election-night/<new-slug>.json`
- Modify: `VERIFY.md`, `plateau_review.json`, county-tech record files, `packages/data/county_tech.json` (via `merge_county_tech.py`)

**Interfaces:**
- Consumes: Task 10's top-ranked candidate.
- Produces: a new complete county series; chart panel.

- [ ] **Step 1:** Research/record adoption years via the `researching-jurisdiction-counting-tech` skill; run `python3 scripts/research/validate_county_tech.py && python3 scripts/research/merge_county_tech.py`.
- [ ] **Step 2:** Denominators for all six years from the SoS SOV PDFs (RUNBOOK 6.1 URL patterns; note the 2012/2014 URL quirks).
- [ ] **Step 3:** Numerators per year, best route first (Clarity version bracket per RUNBOOK 7.2 where available: `current_ver.txt` -> current version's `electionsettings.json` versions array -> cited night version's `sum.json` BC + next-version post-night stamp as the bracket proof).
- [ ] **Step 4:** Write the county JSON per the RUNBOOK section 2 schema, VERIFY.md section, plateau verdicts; land every row per the Row-Landing Procedure (one pipeline run + commit for the county is fine here since the file is new).
- [ ] **Step 5:** RUNBOOK section 10 definition of done applies verbatim.

### Task 12: Add control county end to end

Same file set and steps as Task 11, for Task 10's best no-new-tech control candidate. The `adoption` fields stay null and the county-tech records must document NON-adoption with sources (status "not-adopted" with evidence, not absence of evidence). The chart marks controls via `control: true` only for SF today; check `scripts/build_county_night.py` for how `control` is set, and if it is SF-hardcoded, extend the builder so any no-adoption county with a note gets `control: true`, with a vitest assertion in `packages/data/index.test.ts` that at least two control jurisdictions exist.

- [ ] **Step 1:** Tech non-adoption records (researching-jurisdiction-counting-tech skill) + merge.
- [ ] **Step 2:** Denominators (SOV), numerators (best routes), county JSON, VERIFY.md, verdicts.
- [ ] **Step 3:** Builder change if needed + test; full pipeline; commit.

### Task 13: Rollup and operator packet

**Files:**
- Modify: `docs/research/night-recovery-2026-07-09/county-en/SUMMARY.md` (create), regenerated `HUMAN_VERIFY.md`

- [ ] **Step 1:** Re-run the full pipeline once from clean; `git status` must be clean after regenerating (determinism check per RUNBOOK section 3).
- [ ] **Step 2:** Screenshot the live chart per the screenshot-live-app recipe (`shoot_charts.cjs` against the :4317 preview harness) and confirm the new panels render; do not claim the chart improved without looking at it.
- [ ] **Step 3:** Write SUMMARY.md: panels before/after, rows landed (with confidence and verdict), rows still null and why.
- [ ] **Step 4:** Hand the operator the verification packet: every newly landed row's HUMAN_VERIFY entry (URL/docref + claimed value + fail criteria), flagging all secondary/PLAUSIBLE rows for hand-reading. The human's reading wins; correct any row they refute via a dated CORRECTION note.

## Self-review notes

- Spec coverage: gap-filling (Tasks 2-9), NewsBank probe risk (Task 1), new counties + control (Tasks 10-12), evidence hardening is folded into landing (verdicts, render_verified) rather than a separate pass, out-of-scope items untouched (including CPRA, ruled out by the operator). Success criteria checked in Task 13.
- The chart itself changes only via regenerated `county_night.json`, except the possible `control` flag generalization in Task 12, which is data-plumbing, not presentation, and carries a test.
- Ordering: Task 1 gates 2-7 (serialized on the shared NewsBank session, highest-value county first), Tasks 8-10 are curl-only and can run parallel to nothing-else-using-the-browser, Tasks 11-12 depend on 10, Task 13 last.
