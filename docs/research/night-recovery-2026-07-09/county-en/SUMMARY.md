# County election-night data expansion: rollup summary

Program: `docs/superpowers/plans/2026-07-09-county-night-data-expansion.md`. This
is the Task 13 close-out for the 12 preceding recovery/build tasks. No em
dashes in this document.

## Determinism check (RUNBOOK section 3)

Ran the full pipeline from a clean worktree:

```
python3 scripts/research/validate_election_night.py    -> OK: 90 rows (84 sourced)
python3 scripts/build_county_night.py                   -> 16 jurisdictions, 97 rows, 91 with a night share
python3 scripts/research/verify_en_denominators.py       -> 90/90 VERIFIED
python3 scripts/research/verify_en_numerators.py         -> 84/84 VERIFIED
python3 scripts/research/build_en_verification_report.py -> MACHINE_CHECK.md 174 checks, 0 not verified
uv run pytest tests/test_verify_election_night.py -q     -> 17 passed
npx vitest run                                           -> 19 files / 27 tests passed
git status --short                                       -> clean
```

`pnpm vitest run` is known broken in this worktree (a pre-existing, already
logged controller check); `npx vitest run` is the accepted substitute per the
task instructions and passes cleanly. The tree was clean before and after the
run, confirming every derived file (`county_night.json`, `MACHINE_CHECK.md`,
`HUMAN_VERIFY.md`) is reproducible from the committed source JSONs.

## Chart panels: before and after

Screenshot: `chart-after.png` (this directory), the "Election-night share over
time, by county" chart from the live preview harness.

- **Before this program: 6 panels** (San Francisco, Los Angeles, Napa, Nevada,
  Orange, San Mateo).
- **After this program: 11 panels** (adds Fresno, Riverside, San Diego, Santa
  Clara, Ventura). Confirmed by reading the screenshot: all 5 new counties'
  panels render, full 2012-2024 trajectories and adoption-year markers
  except Santa Clara, whose panel draws only its three comparable points
  (2012, 2022, 2024); 2014/2016/2018 are flagged `comparable: false` and
  excluded from the line by design.
- **San Luis Obispo does NOT render**, despite being a complete, CONFIRMED
  control county (Task 12). This is a known chart bug: `CountyNightTimelineChart`
  only ever shows one `control`-flagged jurisdiction (San Francisco); a second
  control (SLO) is silently dropped from the panel grid. This is a deferred
  design decision, not a data gap; see "Deferred items" below.

Screenshot provenance note: the port-4317 preview process already running in
this environment turned out to be a stale server for a *different* checkout
(the main repo, started 2026-06-27, well before this program's data landed).
Per the "don't kill other processes" rule it was left alone; a fresh preview
instance was started from this worktree's `packages/charts/preview` on the
next free port (4319) and the screenshot was taken against that instance.

## Rows landed this program (30 rows, 8 counties)

Values below are read directly from `packages/data/county_night.json` /
`data/research/election-night/plateau_review.json`, not from memory. "New"
means the county/year cell was null before this program's base commit
(`8974a23`) and is now filled.

### Fresno (4 new rows; complete county, panel added)
| Year | Ballots | Share | Confidence | Comparable | Verdict |
|---|---:|---:|---|---|---|
| 2012 | 160,400 | 61.30% | secondary | true | CONFIRMED |
| 2014 | 120,820 | 73.93% | secondary | true | PLAUSIBLE |
| 2018 | 156,972 | 61.09% | secondary | true | CONFIRMED |
| 2022 | 126,440 | 57.10% | primary | true | CONFIRMED |

(2016 60.70% and 2024 62.36% were pre-existing, untouched.)

### Riverside (4 new rows; complete county, panel added)
| Year | Ballots | Share | Confidence | Comparable | Verdict |
|---|---:|---:|---|---|---|
| 2012 | 486,627 | 72.67% | secondary | true | CONFIRMED |
| 2014 | 264,764 | 74.01% | secondary | true | CONFIRMED |
| 2016 | 507,193 | 65.94% | secondary | true | CONFIRMED |
| 2018 | 300,000 | 46.12% | secondary | true | CONFIRMED |

(2022 34.00% CONFIRMED and 2024 63.70% REFUTED_AS_PLATEAU/ceiling were
pre-existing, untouched.)

### San Diego (3 new rows; complete county, panel added)
| Year | Ballots | Share | Confidence | Comparable | Verdict |
|---|---:|---:|---|---|---|
| 2012 | 728,265 | 60.52% | secondary | true | CONFIRMED |
| 2014 | 509,214 | 73.54% | secondary | true | CONFIRMED |
| 2016 | 726,513 | 53.96% | secondary | **false** (ceiling) | REFUTED_AS_PLATEAU |

(2018/2022/2024 were pre-existing, untouched.)

### Santa Clara (2 new rows; complete county, panel added)
| Year | Ballots | Share | Confidence | Comparable | Verdict |
|---|---:|---:|---|---|---|
| 2016 | 303,678 | 41.91% | secondary | **false** (non-comparable floor) | PLAUSIBLE |
| 2018 | 304,000 | 48.61% | secondary | **false** (documented ceiling) | PLAUSIBLE |

(2012 CONFIRMED, 2014 PLAUSIBLE, 2022 CONFIRMED, 2024 REFUTED_AND_CORRECTED
were pre-existing, untouched.)

### Ventura (6 new rows, entire county new; complete, panel added)
| Year | Ballots | Share | Confidence | Comparable | Verdict |
|---|---:|---:|---|---|---|
| 2012 | 256,927 | 77.76% | primary | true | CONFIRMED |
| 2014 | 153,442 | 75.30% | primary | true | CONFIRMED |
| 2016 | 258,250 | 71.09% | primary | true | CONFIRMED |
| 2018 | 201,298 | 64.13% | primary | true | CONFIRMED |
| 2022 | 153,682 | 54.11% | primary | true | CONFIRMED |
| 2024 | 267,226 | 67.79% | primary | true | CONFIRMED |

### San Luis Obispo (6 new rows, entire county new; complete, is the
### second `control`, does not get its own panel, see chart bug above)
| Year | Ballots | Share | Confidence | Comparable | Verdict |
|---|---:|---:|---|---|---|
| 2012 | 98,458 | 77.64% | primary | true | CONFIRMED |
| 2014 | 63,180 | 72.04% | primary | true | CONFIRMED |
| 2016 | 95,560 | 68.41% | primary | true | CONFIRMED |
| 2018 | 81,663 | 63.62% | primary | true | CONFIRMED |
| 2022 | 58,096 | 47.95% | primary | true | CONFIRMED |
| 2024 | 82,548 | 53.80% | primary | true | CONFIRMED |

### San Bernardino (4 new rows, all documented ceilings; county stays
### incomplete, no panel, 2016 still null)
| Year | Ballots | Share | Confidence | Comparable | Verdict |
|---|---:|---:|---|---|---|
| 2012 | 484,611 | 82.19% | secondary | **false** (ceiling) | REFUTED_AS_PLATEAU |
| 2014 | 230,806 | 78.70% | secondary | **false** (ceiling) | REFUTED_AS_PLATEAU |
| 2018 | 322,000 | 58.97% | secondary | **false** (ceiling) | REFUTED_AS_PLATEAU |
| 2022 | 218,993 | 47.72% | secondary | **false** (ceiling) | REFUTED_AS_PLATEAU |

(2024 434,108/56.24% CONFIRMED/primary was pre-existing, untouched; 2016
stays null, see below.)

### Madera (1 new row; county stays incomplete, no panel, 2012 still null)
| Year | Ballots | Share | Confidence | Comparable | Verdict |
|---|---:|---:|---|---|---|
| 2014 | 22,012 | 80.42% | secondary | **false** (derived ceiling) | PLAUSIBLE |

(2016/2018/2022/2024 were pre-existing primary/CONFIRMED, untouched.)

## Rows still null (6, all across 3 counties)

- **Madera 2012**: no NewsBank text for this year at all (the Madera Tribune
  has no 2012 coverage in the archive); Fresno Bee alone does not name a
  Madera-specific countywide ballots-counted or outstanding-ballots figure.
  Dead end, thoroughly documented, no live route left.
- **Placer 2012**: registrar's election-night GEMS page has zero archived
  captures between poll close and the certified-final crawl 25 days later;
  no press/social alternative found across four alt-archive families
  (Task 8) or three enumeration families (Task 9).
- **Placer 2022**: same page-never-crawled pattern; only sourceable figure is
  the 8pm first tranche (~49,000, the classic first-tranche trap), rejected
  per rules; no election-night plateau recoverable.
- **Placer 2024**: same pattern again; only sourceable figure is the 8pm
  first tranche (104,382 VBM), rejected; the true plateau is bounded between
  104,382 and the next canvass update (182,129) but not pinned to a number.
- **Sacramento 2016**: no morning-after press release, no archived Hart
  `eresults` capture, and no e-cers AJAX capture in the election-night
  window; NewsBank searched exhaustively (9 articles opened), only
  first-tranche or post-night-imprecise figures found. Dead end.
- **San Bernardino 2016**: SB Sun (7 hits examined) and a Press-Enterprise
  cross-check found only city/precinct-level counts, none countywide. Dead
  end.

## Deferred items (ledger, unresolved by design or by explicit hold)

- **SLO second-control chart bug**: `CountyNightTimelineChart` only renders
  one `control`-flagged county (San Francisco); San Luis Obispo (also
  `control: true`, fully sourced/CONFIRMED) is silently dropped from the
  panel grid. Needs an editorial/design call (own panel? overlay as a second
  faint baseline alongside SF?). Not touched in Task 13 per instructions
  (chart code untouched).
- **Ventura epollbook adoption, EAP vs. SoS conflict**: Ventura's own Election
  Administration Plan describes a real-time e-pollbook-equivalent lookup
  system (adopted 2022), but the CA Secretary of State's October 2025
  "Voting Technologies in Use by County" survey lists Ventura's Electronic
  Pollbook column as "Do not use." Both sources are primary-grade and
  disagree; held at `confidence: secondary` pending a human call. See
  `data/research/county-tech/ventura-ca.json`.
- **`pnpm vitest run` broken in this worktree**: `npx vitest run` is the
  accepted, verified substitute (used throughout this program and in this
  rollup); root cause not diagnosed, flagged for a separate fix outside this
  program's scope.
- **Licensed snippets in git history**: commits `b912769..c118655` (Task 1)
  contain licensed NewsBank article-body text in their history, scrubbed at
  the tip by `66f0a18` but still present in intermediate commits. This branch
  must be squashed or history-rewritten before it is pushed anywhere public,
  and only when no agents are running against this worktree.

## Hand-check priorities

The generated `data/research/election-night/HUMAN_VERIFY.md` is the full
operator verification packet (not rewritten here). Below is the priority
order for a human's limited time, worst-first, with what a FAIL looks like
for each.

### 1. The three San Bernardino ceilings + the SB 2018 ceiling

Rows: SB 2012 (484,611/82.19%), SB 2014 (230,806/78.70%), SB 2018
(322,000/58.97%), SB 2022 (218,993/47.72%). All four are held at
`comparable: false` / `REFUTED_AS_PLATEAU`, i.e. already flagged as NOT
plateau numbers, only upper-bound ceilings. Open:
`data/research/election-night/HUMAN_VERIFY.md`, section 2, the four
`san-bernardino-ca` bullets (lines ~114-144). What a FAIL looks like: if the
cited article's "as of Wednesday/Thursday" framing turns out to describe a
report that in fact HAD NOT been updated since election night (i.e. the
ceiling is actually a true plateau), the row should be promoted back to
`comparable: true` / a plateau verdict, not left as an artificially-low
ceiling; conversely, if the framing is even more clearly post-canvass than
documented, no change is needed but the note should say so explicitly. Two
of the four (2012, 2014) have magnitudes (78-82%) well above every other
county's calibration band, the more urgent pair to eyeball.

### 2. San Diego 2012 (728,265/1,203,265 = 60.52%)

Rests on a restated round "about 475,000" outstanding-ballots figure (not a
directly-counted total). Docs to open: the numerator URL in
`HUMAN_VERIFY.md` section 2 (`san-diego-ca 2012-11-06`, line ~146), and if
available, the mirrored capture at
`mirror/newsbank/docs/sandiego2012_14273902C00B3B00.txt` (main-repo path,
outside this worktree; gitignored). What a FAIL looks like: if the "about
475,000" figure is itself a later restatement of an earlier, different
outstanding-ballot count (i.e. the two cited articles are not independently
confirming the same election-night state), the CONFIRMED verdict should
drop to PLAUSIBLE or the row should be flagged non-comparable.

### 3. Fresno 2014 (120,820/163,420 = 73.93%) and Madera 2014 (22,012/27,370 = 80.42%)

Fresno 2014: the PLAUSIBLE verdict already documents that the ~42,600
outstanding-ballots reconciliation across two articles (Nov 6 "~22,000
mail + 20,400 provisional" vs. Nov 8 "~42,600") is treated as an arithmetic
coincidence, not an explicit bracketing statement; see `HUMAN_VERIFY.md`
section 2, `fresno-ca 2014-11-04` (line ~34). Madera 2014 is a computed
ceiling (certified final minus a clerk-quantified not-yet-counted figure,
snapshot dated Friday, not election night); see the `madera-ca 2014-11-04`
bullet (line ~50). What a FAIL looks like: if either underlying quote is
less precise than the note claims (e.g. the "~42,600" is a rounding of a
much rounder or vaguer verbal estimate), both should stay non-comparable or
drop further to a documented dead end rather than a numeric row.

### 4. The three mirrored San Diego docs flagged by Task 5

Full set: 2012 (`mirror/newsbank/docs/sandiego2012_14273902C00B3B00.txt`,
claims 475,000 outstanding -> 60.52%), 2014
(`mirror/newsbank/docs/sandiego2014_1A43A319608C8500.txt`, claims 509,214
counted directly -> 73.54%), 2016
(`mirror/newsbank/docs/sandiego2016_16871C80DC62E438.txt`, claims 620,000
outstanding -> 53.96%, already downgraded to a ceiling). These mirror paths
live in the main repo checkout, not this worktree (gitignored, per the
project's mirror-file convention). What a FAIL looks like: any of the three
quotes reading differently from the note's transcription, or omitting the
"held/unchanged since election night" framing the CONFIRMED verdicts (2012,
2014) depend on.

### 5. Nevada 2016/2018/2022, the YubaNet-primary question

Pre-existing, deliberately left open by this program (not touched in Tasks
1-12). All three years rest on YubaNet as the sole news source for a
directly-quoted, dated "at the end of election night, N ballots" or "last
night, N ballots" statement (see `data/research/election-night/nevada-ca.json`
notes for 2016-11-08, 2018-11-06, 2022-11-08). What a FAIL looks like: if a
second, independent outlet contradicts YubaNet's stated ballot count or
timing for any of the three years, since the dataset currently has no
corroborating second source for any of them.


UPDATE (2026-07-09, post-rollup): the second-control chart limitation is resolved. CountyNightTimelineChart now renders every complete jurisdiction (San Luis Obispo included, drawn as a control with the SF baseline overlaid), 12 panels total. chart-after.png regenerated from the worktree preview and verified against the live render.
