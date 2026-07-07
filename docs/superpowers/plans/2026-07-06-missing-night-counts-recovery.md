# Missing Night-Counts Recovery Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Recover election-night ballot-count floors for the 16 post-1965 `recovered = no` elections, newest first, ingesting verified figures into `data/sf_archival_canvass_points.csv` and documenting every dry attempt in the public search log.

**Architecture:** Phase 1 attacks 2008-04-08 through web archives (no browser session). Phase 2 drives the SF Chronicle NewsBank image archive through an isolated debug-port Chrome with an operator-supplied SFPL ezproxy session: one validation run, then waves of 2-3 parallel subagent runs of the `newsbank-election-recovery` skill. The main session is the only writer to committed files; subagents only capture and transcribe.

**Tech Stack:** Wayback CDX API, `scripts/archive-recovery/*.js` (puppeteer-core over CDP :9222), vision transcription of page scans, Python stdlib generators (`build_viz_data.py`, `build_elections_master.py`, `gen_docs.py`), `sov-certified-turnout` and `newsbank-election-recovery` skills.

**Spec:** `docs/superpowers/specs/2026-07-06-missing-night-counts-recovery-design.md`

## Global Constraints

- All repo edits and commits happen in the worktree `/Users/sbuss/workspace/sf-election-count/.claude/worktrees/spicy-gathering-starfish`, branch `feat/night-count-recovery`.
- Node capture scripts run from the MAIN checkout `/Users/sbuss/workspace/sf-election-count` (its `node_modules` and gitignored `mirror/` tree); they write only to `mirror/`. Environment for every capture shell:
  `cd /Users/sbuss/workspace/sf-election-count && export PATH="/Users/sbuss/.nvm/versions/node/v22.21.1/bin:$PATH" && export NODE_PATH="$(pwd)/node_modules"`
- Never commit page images. Only figures plus citations (docref / scan filename) enter committed files.
- Never automate SFPL credentials; the operator logs in manually.
- Never hand-edit derived files (`packages/data/*.json`, `docs/missing.md`, `docs/sources.md`, `data/elections_master.csv`). Edit sources (`data/sf_archival_canvass_points.csv`, `docs/analysis/public-search-log.md`, README prose) and rebuild.
- One `newsbank-election-recovery` run per election; distinct `WIN` index per concurrent run; nothing else touches the NewsBank session while captures run.
- A night point requires `observed_at` at or before 06:00 on E+1 (the `build_viz_data.py` cutoff). A contest-sum floor is only worth ingesting if it beats the DOE in-person floor (precinct column) for that election.
- Uncertain digits are marked `[?]`, ingested at reduced confidence only if gates pass, and queued in the human-verification doc (Task 8). The operator's hand-read wins.
- No em dashes in any prose written for this repo.

**Ingestion gates (apply to every candidate figure, from the skill and runbook):**
1. Masthead/page date matches the intended issue or capture date.
2. Largest single-seat contest sum ≤ certified ballot total.
3. Precinct ratio ≤ 1; printed percentages match printed counts within ~1 point.
4. Monotone against neighboring dated observations for the same election.
5. The column/table header actually says San Francisco.

**Standard rebuild-and-verify block** (run in the worktree after every CSV or search-log edit; referenced by tasks below as "REBUILD"):

```bash
cd /Users/sbuss/workspace/sf-election-count/.claude/worktrees/spicy-gathering-starfish
python3 scripts/build_viz_data.py
python3 scripts/build_elections_master.py   # prints recovered/turnout-only/missing counts
python3 scripts/gen_docs.py
uv run pytest -q                            # expect: all pass
pnpm vitest run                             # expect: all pass (needs Task 1's pnpm install)
```

**DOE certified rows for the 8 table-covered targets** (from `data/sf_turnout_history_doe_1899_2019.csv`; format: certified ballots / registration / precinct in-person floor):

| Election | Certified | Registration | In-person floor |
|------------|---------|---------|---------------------|
| 2008-04-08 | 19,742 | 79,340 | 5,332 (27.0%) |
| 1984-06-05 | 180,741 | 375,799 | 151,013 (83.6%) |
| 1980-08-19 | 140,551 | 404,035 | 119,566 (85.1%) |
| 1980-06-03 | 206,366 | 403,382 | 191,196 (92.7%) |
| 1977-08-02 | 178,367 | 336,046 | 161,622 (90.6%) |
| 1976-06-08 | 208,884 | 311,254 | 191,684 (91.8%) |
| 1974-11-05 | 228,586 | 369,005 | 213,114 (93.2%) |
| 1972-06-06 | 234,840 | 368,357 | 218,176 (92.9%) |

1966-06-07, 1966-11-08, 1967-11-07, 1968-06-04, 1969-11-04, 1970-06-02, 1970-11-03, 1971-11-02 have NO DOE row; their denominators come from Task 5 (SOV) or the paper's complete canvass.

**CSV row format** for `data/sf_archival_canvass_points.csv` (header: `election_date,election_name,observed_at,stamp_kind,days_since_election,ballots_counted_total,ballots_vbm,ballots_election_day,registered_voters,certified_final,pct_of_final,source_url,extraction,final_source`). Match the committed 1981-11-03 row's citation style. Template for a NewsBank night point:

```
<YYYY-MM-DD>,<Election Name>,<E+1>T03:00:00,news-derived,1,<night_floor>,,,<registration or empty>,<certified_int>,<round(night/certified*100,1)>,"SF Chronicle (NewsBank image scan via SFPL), <issue> p<N> '<box title>', <precincts> reporting: <contest> sum <floor> (<candidate breakdown>) - conservative night floor (top-contest sum); scan <filename>",newsbank-image-scan,"<where the certified total comes from: DOE turnout table row, SOV citation, or E+2 complete canvass citation>"
```

`certified_final` must be an integer (build_viz_data does `int()` on it); resolve "DOE" to the actual number before appending.

**Wave subagent prompt template** (used verbatim by every wave task; substitute the angle-bracket fields from that task's per-election block):

```
Execute the newsbank-election-recovery skill for one SF election.
1. Read /Users/sbuss/workspace/sf-election-count/.claude/skills/newsbank-election-recovery/SKILL.md and follow it exactly, including its environment block (run capture commands from the MAIN checkout /Users/sbuss/workspace/sf-election-count).
2. Your election: ELECTION_DATE=<date>. ISSUE_DATE=<date plus one day>. WIN=<n>.
3. Gates context: <"certified ballots N, registration N; your contest-sum floor only matters if it beats the in-person floor N" for DOE-covered elections, or "no DOE row: the certified total comes from the SOV (provided in your notes) or from your own E+2 complete-total capture" otherwise>.
4. Election-specific notes: <notes>.
5. Write every scan and an incremental readings CSV under mirror/newsbank/scans/ AS YOU GO; your findings must survive your death.
6. Return ONLY the skill's Step 4 structured record (or a DRY report listing issues/pages walked and what they printed instead). Do not edit any repo CSV.
```

---

### Task 1: Phase 1 digital recovery of 2008-04-08

**Files:**
- Modify: `data/sf_archival_canvass_points.csv` (append 1 row on success)
- Modify: `docs/analysis/public-search-log.md` (on dry outcome)
- Test: gates above + REBUILD; `grep '^2008-04-08' data/elections_master.csv` flips from `no` to `night`

**Interfaces:**
- Consumes: nothing (first task; no browser session needed)
- Produces: one ingested night point or a documented dead end; worktree `node_modules` (pnpm install) for all later vitest runs

- [ ] **Step 1: One-time worktree JS setup**

```bash
cd /Users/sbuss/workspace/sf-election-count/.claude/worktrees/spicy-gathering-starfish && pnpm install
```

Expected: lockfile-clean install, no errors.

- [ ] **Step 2: Probe the live DOE past-results pages**

The election is the June 3, 2008 CD-12 special's OPEN PRIMARY held April 8, 2008 (post-Lantos; `data/elections.csv` names it "Special Congressional Open Primary Election"). WebFetch these, looking for an April 8, 2008 results/summary page or PDF link:

- `https://sfelections.sfgov.org/past-election-results`
- `https://www.sf.gov/departments--city-administrator--department-elections` (follow "results" links)

Expected: either a results page for April 8, 2008 (record its URL) or confirmation the live site starts later.

- [ ] **Step 3: Wayback CDX sweep for the 2008-era results pages**

```bash
curl -s 'https://web.archive.org/cdx/search/cdx?url=sfgov.org/site/elections_index.asp&matchType=prefix&from=20080408&to=20080501&collapse=digest' | head -50
curl -s 'https://web.archive.org/cdx/search/cdx?url=sfgov.org/site/election_index.asp&matchType=prefix&from=20080408&to=20080501&collapse=digest' | head -50
curl -s 'https://web.archive.org/cdx/search/cdx?url=sfelections.org&matchType=domain&from=20080401&to=20080601&collapse=digest&limit=3000' | grep -i '2008\|summary\|result' | head -50
curl -s 'https://web.archive.org/cdx/search/cdx?url=sfgov.org/site/uploadedfiles/elections&matchType=prefix&from=20080401&to=20080701&collapse=digest&limit=3000' | head -80
```

Expected output: CDX lines (`urlkey timestamp original mimetype status digest length`). Shortlist captures timestamped 20080408-20080415 and any "Election Summary" URLs. If a promising `id=` page appears at ANY 2008 timestamp, also query that exact URL without date bounds (the summary page may only be captured later but self-report its Last Updated stamp).

- [ ] **Step 4: Fetch shortlisted captures and extract the night figure**

For each shortlisted `(timestamp, original)`: `curl -s "https://web.archive.org/web/<timestamp>/<original>"` and look for "Election Summary", "Ballots Cast", precincts reporting, and a "Last Updated" stamp. A night point needs a self-reported stamp at or before 2008-04-09 06:00 (stamp_kind `page-self-reported`), or a capture timestamp in that window (stamp_kind `capture-time`). Gate: total ≤ 19,742.

- [ ] **Step 5a (found): Append the row and rebuild**

Append to `data/sf_archival_canvass_points.csv` using the row format from Global Constraints with `extraction` = `wayback-html`, `certified_final` = `19742`, `registered_voters` = `79340`, citation = the full Wayback URL plus the page's own stamp text. Run REBUILD. Verify:

```bash
grep '^2008-04-08' data/elections_master.csv   # expect: ...,night,<pct>,...
```

- [ ] **Step 5b (dry): Document the dead end**

Append to the relevant section of `docs/analysis/public-search-log.md` (prose, no em dashes): which CDX patterns and date windows were swept, which captures were fetched, and what they showed instead of a count. Run REBUILD (ships the log into `ledger.json`/`missing.md`).

- [ ] **Step 6: Commit**

```bash
git add -A data docs packages/data && git commit -m "data: 2008-04-08 night count (Phase 1 digital)"   # or "docs: 2008-04-08 digital paths exhausted"
```

---

### Task 2: Isolated Chrome and SFPL session (operator checkpoint)

**Files:** none committed (session setup only)

**Interfaces:**
- Consumes: operator's one manual SFPL ezproxy login
- Produces: a live NewsBank session on `127.0.0.1:9222` that Tasks 3, 4, 6, 7 consume

- [ ] **Step 1: Launch the isolated Chrome**

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-sfpl \
  --no-first-run \
  --disable-background-timer-throttling \
  --disable-renderer-backgrounding \
  --disable-backgrounding-occluded-windows &
```

(Throwaway profile so the operator's own Chrome is untouched. If :9222 is already bound, check whether an earlier session Chrome is alive and reuse it; do not kill processes you did not start.)

- [ ] **Step 2: Operator logs in**

Ask the operator to log into SFPL eResources → NewsBank (Access World News image edition) in that window. Credentials are never typed by automation.

- [ ] **Step 3: Verify the session**

```bash
cd /Users/sbuss/workspace/sf-election-count && export PATH="/Users/sbuss/.nvm/versions/node/v22.21.1/bin:$PATH" && export NODE_PATH="$(pwd)/node_modules"
node scripts/archive-recovery/session_probe.js
```

Expected: `TITLE:` and `SNIP:` of a real NewsBank document. If the snip shows "Articles and Databases" auth text, the login did not take; ask the operator to retry, then re-probe.

**Session-loss recovery (applies to every later task):** every capture script hard-aborts on the SFPL auth wall rather than saving garbage. If a run aborts mid-capture, ask the operator to re-login in the same Chrome window, re-probe, and re-run only the aborted captures (finished scans on disk stay valid).

---

### Task 3: Validation recovery, 1974-11-05 General

**Files:**
- Modify: `data/sf_archival_canvass_points.csv`, `data/newsbank_issue_docrefs.json` (issue docref, if the sweep logs it)
- Modify: `docs/analysis/public-search-log.md` (only if dry)
- Test: gates + REBUILD; `grep '^1974-11-05' data/elections_master.csv` shows `night`

**Interfaces:**
- Consumes: Task 2's session
- Produces: proof the capture pipeline works end to end; go/no-go for the parallel waves

- [ ] **Step 1: Capture E+1 front pages**

```bash
cd /Users/sbuss/workspace/sf-election-count && export PATH="/Users/sbuss/.nvm/versions/node/v22.21.1/bin:$PATH" && export NODE_PATH="$(pwd)/node_modules"
node scripts/archive-recovery/sweep_section.js 1974-11-05 1974-11-06 1 3 1
```

Expected: `mirror/newsbank/scans/sweep_19741105_issue19741106_p{1,2,3}_s*.png`. On `NO ENTRY`, retry adjacent dates. Scans store the image in the PNG alpha channel; flatten (`scripts/archive-recovery/flatten_scan.py`) before cropping.

- [ ] **Step 2: Transcribe and gate**

Read the scans (vision; crop+upscale ambiguous digits with `sips`). Confirm the masthead says November 6, 1974. Extract the election-night "Final" citywide box (the 1958/1962 generals had one): precincts reported, every single-seat contest (Governor is the marquee), any printed total-ballots line. Apply the ingestion gates; certified is 228,586, and the floor must beat 213,114 to be worth ingesting.

- [ ] **Step 3: If the E+1 box is partial, capture E+2**

```bash
node scripts/archive-recovery/sweep_section.js 1974-11-05 1974-11-07 1 3 1
```

- [ ] **Step 4: Append, rebuild, verify**

Append the row per the CSV template (`certified_final` = `228586`, `registered_voters` = `369005`, `final_source` cites the DOE turnout table row). Run REBUILD. Verify `grep '^1974-11-05' data/elections_master.csv` shows `night`. Add any load-bearing or `[?]` digits to the verification-queue notes for Task 8.

- [ ] **Step 5: Commit**

```bash
git add -A data docs packages/data && git commit -m "data: 1974-11-05 election-night count recovered (NewsBank)"
```

---

### Task 4: Wave A, three parallel recoveries (1984-06-05, 1980-08-19, 1980-06-03)

**Files:**
- Modify: `data/sf_archival_canvass_points.csv` (up to 3 rows), `data/newsbank_issue_docrefs.json`
- Modify: `docs/analysis/public-search-log.md` (dry outcomes)
- Test: gates + REBUILD; each recovered date flips to `night` in `elections_master.csv`

**Interfaces:**
- Consumes: Task 2's session; Task 3's go decision
- Produces: ingested rows / documented dead ends for the three elections

- [ ] **Step 1: Dispatch three parallel subagents** (one Agent message, three tool uses), each with the wave subagent prompt template from Global Constraints and one of these per-election blocks:
- **1984-06-05 Primary** (WIN 1, certified 180741, registration 375799, floor 151013). Notes: the June sweep found the E+1 'S.F. VOTE' box percentage-only and the Prop 24 sum 135,327 is BELOW the floor, so do not return those; page-walk deeper into the E+1 results section and the E+2 (June 7) issue for an absolute-count box or a printed ballots-cast line.
- **1980-08-19 Special** (WIN 2, certified 140551, registration 404035, floor 119566). Notes: never attempted; citywide special, expect a measure YES/NO box (a measure sum is the preferred floor).
- **1980-06-03 Primary** (WIN 3, certified 206366, registration 403382, floor 191196). Notes: never attempted; statewide primary day, look for presidential-primary or measure sums; both parties' presidential lines together do NOT sum across parties, use the largest single contest or a printed total.

If Task 1 came up dry, add a fourth subagent (WIN 4) for **2008-04-08** (certified 19742, registration 79340, floor 5332): instead of image sweeps, search the NewsBank Access World News TEXT archive (SF Chronicle, 2008-04-08 through 2008-04-11) with the count-language queries from the search log ("ballots counted", "absentee ballots", "precincts reporting", "Speier", "Jackie Speier") and return any absolute SF count line with its docref; the spec's third digital path folds in here.

- [ ] **Step 2: Validate each returned record against the gates** (independently re-check the arithmetic and the masthead claim against the scans on disk; salvage from `mirror/newsbank/scans/` if an agent died).

- [ ] **Step 3: Append passing rows, log dry outcomes, REBUILD, verify each date's master row.**

- [ ] **Step 4: Commit**

```bash
git add -A data docs packages/data && git commit -m "data: wave A night counts (1984-06, 1980-08, 1980-06)"
```

---

### Task 5: SOV certified denominators for the five statewide 1966-1970 elections

**Files:**
- Modify: whatever `sov-certified-turnout` prescribes (its skill owns the file conventions)
- Test: each election has a certified SF total with an archive.org citation

**Interfaces:**
- Consumes: nothing (no browser session; parallel-safe with Tasks 4, 6, 7)
- Produces: certified integers for 1970-11-03, 1970-06-02, 1968-06-04, 1966-11-08, 1966-06-07 that Tasks 6 and 7 put in `certified_final`

- [ ] **Step 1:** Invoke the `sov-certified-turnout` skill for 1970-11-03 (statewide general). Record the certified SF total + citation.
- [ ] **Step 2:** Same for 1970-06-02 (statewide primary).
- [ ] **Step 3:** Same for 1968-06-04 (statewide primary).
- [ ] **Step 4:** Same for 1966-11-08 (gubernatorial general).
- [ ] **Step 5:** Same for 1966-06-07 (statewide primary).
- [ ] **Step 6:** Commit per that skill's conventions:

```bash
git add -A data docs && git commit -m "data: SOV certified SF totals for 1966-1970 statewide elections"
```

---

### Task 6: Wave B, three parallel recoveries (1977-08-02, 1976-06-08, 1972-06-06)

**Files:**
- Modify: `data/sf_archival_canvass_points.csv`, `data/newsbank_issue_docrefs.json`, `docs/analysis/public-search-log.md`
- Test: gates + REBUILD; recovered dates flip to `night`

**Interfaces:**
- Consumes: Task 2's session
- Produces: ingested rows / documented dead ends for the three elections

- [ ] **Step 1: Dispatch three parallel subagents** with the wave subagent prompt template from Global Constraints and these blocks:

- **1977-08-02 Special** (WIN 1, certified 178367, registration 336046, floor 161622). Notes: the June capture found only a percentage district map on E+1; page-walk the full E+1 issue beyond the front pages and the E+2 issue for any absolute-count box or prose ballots-cast line; if truly count-free, return DRY with the pages walked (this election is a likely documented dead end).
- **1976-06-08 Primary** (WIN 2, certified 208884, registration 311254, floor 191684). Notes: a 'Vote Tally' hi-res re-read was left in flight in June; FIRST list `ls /Users/sbuss/workspace/sf-election-count/mirror/newsbank/scans/ | grep -i '19760608\|1976'` and read any existing `hi_*.png` before recapturing.
- **1972-06-06 Primary** (WIN 3, certified 234840, registration 368357, floor 218176). Notes: the Dem presidential sum 132,109 is BELOW the floor and already rejected; you need a Republican presidential line, another single-seat statewide contest, a top measure YES/NO, or a printed total-ballots line to beat 218,176; else return DRY.

- [ ] **Step 2: Validate records against gates; salvage from disk if needed.**
- [ ] **Step 3: Append passing rows, log dry outcomes, REBUILD, verify.**
- [ ] **Step 4: Commit**

```bash
git add -A data docs packages/data && git commit -m "data: wave B night counts (1977-08, 1976-06, 1972-06)"
```

---

### Task 7: Waves C and D, the 1966-1971 group (six elections, two waves)

**Files:**
- Modify: `data/sf_archival_canvass_points.csv`, `data/newsbank_issue_docrefs.json`, `docs/analysis/public-search-log.md`
- Test: gates + REBUILD after each wave; recovered dates flip to `night`

**Interfaces:**
- Consumes: Task 2's session; Task 5's certified totals for the statewide dates
- Produces: ingested rows / documented dead ends for the six elections

- [ ] **Step 1: Wave C, dispatch three parallel subagents** (wave subagent prompt template from Global Constraints):

- **1971-11-02 Municipal** (WIN 1, no DOE row). Notes: Mayor race (Alioto re-elect) is the floor contest; sum ALL its candidates. No DOE denominator exists: also capture E+2 (and E+3 if needed) for the complete 'total vote of city'; if none is printed, return the night floor with certified_final=needs-2day-capture.
- **1970-11-03 General** (WIN 2, certified from Task 5, no DOE row). Notes: Governor (Reagan-Unruh) sum is the floor; expect the election-night 'Final' citywide box like other generals.
- **1970-06-02 Primary** (WIN 3, certified from Task 5, no DOE row). Notes: statewide primary; largest single-party contest or printed total; a cross-party sum of the same office's primaries is NOT valid.

- [ ] **Step 2: Validate, append (statewide rows use Task 5 certified integers; cite the SOV in final_source), log dry outcomes, REBUILD, verify, commit:**

```bash
git add -A data docs packages/data && git commit -m "data: wave C night counts (1971-11, 1970-11, 1970-06)"
```

- [ ] **Step 3: Wave D, dispatch three parallel subagents:**

- **1969-11-04 Municipal** (WIN 1, no DOE row). Notes: Mayor (Alioto) sum is the floor; capture E+2 for the complete total; certified_final=needs-2day-capture if absent.
- **1968-06-04 Primary** (WIN 2, certified from Task 5, no DOE row). Notes: presidential primary (RFK assassination night; the papers led with it, the count boxes may sit deeper in the issue); single-party presidential sum or printed total only.
- **1967-11-07 Municipal** (WIN 3, no DOE row). Notes: Mayor race (Alioto first win) sum is the floor; capture E+2 for the complete total.

- [ ] **Step 4: Validate, append, log, REBUILD, verify, commit:**

```bash
git add -A data docs packages/data && git commit -m "data: wave D night counts (1969-11, 1968-06, 1967-11)"
```

---

### Task 8: Wave E (1966-11-08, 1966-06-07) and closeout

**Files:**
- Modify: `data/sf_archival_canvass_points.csv`, `docs/analysis/public-search-log.md`, `README.md` (counts), Create: `docs/analysis/2026-07-06-night-recovery-verification-queue.md`
- Test: full REBUILD green; README counts match `build_elections_master.py` output

**Interfaces:**
- Consumes: everything prior
- Produces: final dataset state, verification queue for the operator, branch ready for integration

- [ ] **Step 1: Wave E, dispatch two parallel subagents** (wave subagent prompt template from Global Constraints):

- **1966-11-08 Gubernatorial** (WIN 1, certified from Task 5, no DOE row). Notes: Governor (Reagan-Brown) sum is the floor; expect a citywide 'Final' box.
- **1966-06-07 Primary** (WIN 2, certified from Task 5, no DOE row). Notes: statewide primary; single-party contest sums only.

- [ ] **Step 2: Validate, append, log dry outcomes, REBUILD, verify, commit** (`"data: wave E night counts (1966-11, 1966-06)"`).

- [ ] **Step 3: Write the human-verification queue**

Create `docs/analysis/2026-07-06-night-recovery-verification-queue.md`: one row per load-bearing or `[?]` digit ingested anywhere in Tasks 1-8 with scan path (main-checkout `mirror/newsbank/scans/...`), the claimed value, the threshold that makes it load-bearing (certified total or in-person floor), and current confidence. Send the file to the operator (SendUserFile).

- [ ] **Step 4: Update README counts**

`python3 scripts/build_elections_master.py` prints the new `recovered / turnout-only / missing` counts. Update the hand-written numbers at `README.md:171` ("**83 San Francisco elections still lack...**") and `README.md:218` ("**164 recovered · 23 turnout-only · 83 still missing**") to match, and reword the roadmap bullets for any recovered/dry elections in the README's mid-century list. Also update the search-log intro line "83 San Francisco elections" source text in `docs/analysis/public-search-log.md` if it states the count.

- [ ] **Step 5: Final full verification**

Run REBUILD one last time; expect pytest and vitest green and stable generated docs (`git status` shows no unexpected diffs after a second consecutive `gen_docs.py` run).

- [ ] **Step 6: Commit and hand off**

```bash
git add -A && git commit -m "docs: recovery closeout, counts + verification queue"
```

Then use the superpowers:finishing-a-development-branch skill to integrate `feat/night-count-recovery` (PR against main per repo convention).
