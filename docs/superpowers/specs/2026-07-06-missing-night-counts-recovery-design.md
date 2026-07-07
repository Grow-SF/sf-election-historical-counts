# Recent-first recovery of missing election-night counts

**Date:** 2026-07-06
**Status:** approved design, pending implementation plan
**Owner:** Claude session, operator Steven

## Goal

Shrink the "83 San Francisco elections still lack an election-night count"
number by recovering night-count floors for the most recent gaps first,
continuing until the digital archive paths are exhausted. Every attempted
election ends in one of two states: a verified night count ingested into the
dataset, or a documented failure mode in the search log so no future
researcher redoes the ground.

## Scope

The worklist is the 16 post-1965 `recovered = no` rows of
`data/elections_master.csv`, attempted in strict recent-first order:

| # | Date | Kind | Notes carried in |
|---|------------|-----------|------------------|
| 1 | 2008-04-08 | Special congressional open primary (CD-12, post-Lantos) | Digital-only paths; certified 19,742 already in DOE table |
| 2 | 1984-06-05 | Primary | E+1 box printed percentages only; try E+2 and other editions |
| 3 | 1980-08-19 | Special | Not yet page-walked |
| 4 | 1980-06-03 | Primary | Not yet page-walked |
| 5 | 1977-08-02 | Special | District map printed percentages only; try day-2 and multi-paper sweep |
| 6 | 1976-06-08 | Primary | "Vote Tally" hi-res re-read was left in flight in June |
| 7 | 1974-11-05 | General | Validation target: same "Final" box that recovered 1958/1962 |
| 8 | 1972-06-06 | Primary | Dem-primary sum already read but below in-person floor; needs GOP presidential sum |
| 9 | 1971-11-02 | Municipal | Not yet page-walked |
| 10 | 1970-11-03 | General | Not yet page-walked |
| 11 | 1970-06-02 | Primary | Not yet page-walked |
| 12 | 1969-11-04 | Municipal | Not yet page-walked |
| 13 | 1968-06-04 | Primary | Not yet page-walked |
| 14 | 1967-11-07 | Municipal | Not yet page-walked |
| 15 | 1966-11-08 | General | Not yet page-walked |
| 16 | 1966-06-07 | Primary | Not yet page-walked |

Eight of the 16 have certified denominators in the DOE historical turnout
table (`data/sf_turnout_history_doe_1899_2019.csv`): 2008-04-08, 1984-06-05,
1980-08-19, 1980-06-03, 1977-08-02, 1976-06-08, 1974-11-05, 1972-06-06.
Those need only a night numerator. The eight 1966-1971 elections are absent
from the DOE table, so each also needs a certified denominator:

- **Statewide even-year (5):** 1970-11-03, 1970-06-02, 1968-06-04,
  1966-11-08, 1966-06-07 take their certified SF totals from the CA
  Statement of Vote via the `sov-certified-turnout` skill (no browser
  session needed; runs in parallel with the NewsBank waves).
- **Odd-year municipals (3):** 1971-11-02, 1969-11-04, 1967-11-07 have no
  statewide SOV; the denominator comes from the paper's complete "total
  vote of city" (E+2 semi-official or official canvass), which the
  `newsbank-election-recovery` skill already captures, or stays
  `needs-2day-capture` and the election is recorded turnout-pending.

The pre-1966 gaps (early-1900s specials, pre-1907 municipals, pre-1892
statewide) are out of scope for this effort; several are already flagged
microfilm-or-nothing.

## Phase 1: 2008-04 digital recovery (no browser session needed)

Three paths, in order, stopping at the first verified hit:

1. **DOE archived results pages** on the live sfelections.org / sf.gov site
   for the April 8, 2008 special primary.
2. **Targeted Wayback CDX sweep**, election night through E+3, across the
   known host/path generations (ci.sf.ca.us, sfgov.org, sfelections.org,
   sf.gov, the Lotus Domino election2.nsf views). The June 2026 sweeps
   covered "thin elections 2000-2012" generically; `docs/missing.md` flags
   the Department's own first-round/night reports as the unresolved angle,
   so this pass targets the Election Summary page for this election
   specifically.
3. **Chronicle/NewsBank text archive** (1985+) count-language queries as a
   fallback, folded into Phase 2 if it requires the ezproxy session.

Gate: any candidate figure must be at most the certified 19,742 and must
cite the capture URL (or docref) in the source note.

## Phase 2: NewsBank image recovery in waves (elections 2-16)

**Session setup.** Launch an isolated Chrome with
`--remote-debugging-port=9222` and a throwaway profile (precedent:
`/tmp/chrome-chronicle` in `docs/analysis/2026-06-10-archive-recovery-ledger.md`).
The operator performs the single manual SFPL ezproxy login in that window;
credentials are never automated. The operator's own browser is unaffected;
the one constraint is that nothing browses NewsBank on the same SFPL session
while captures run.

**Validation run.** One election first, 1974-11-05 (a general, most likely
to carry the clean election-night "Final" citywide box), driven by the
`newsbank-election-recovery` skill end to end, including ingestion. Only
after that run lands does the fan-out begin.

**Waves.** Batches of 2-3 parallel subagent runs of
`newsbank-election-recovery`, one election per run, each with a distinct
WIN index, on the dedicated session left otherwise idle. Recent-first order
within and across waves. Subagents follow the skill exactly: sweep E+1
pages 1-3 (plus E+2 when the day-after count is partial), transcribe by
vision with crop+upscale on ambiguous digits, apply the gates, and return
the structured record only. Per the dead-agent salvage rule, scans and
intermediate readings go to gitignored `mirror/newsbank/scans/`
incrementally; page images are never committed.

## Verification and ingestion

Per-record gates (from the skill and the June verification protocol):

- Masthead date on the scan equals the intended issue date.
- Largest single-seat contest sum is at most the certified ballot total.
- Precinct ratio is sane (reported/total at most 1).
- Printed percentages match printed counts within a point where both exist.
- Load-bearing digits re-read at high zoom; uncertain digits marked `[?]`.
- A contest-sum floor is only ingested if it beats the existing in-person
  floor; prose ballots-cast statements beat contest sums (no undervote).

**Ingestion.** Passing records are appended (by the main session, not
subagents) to `data/sf_archival_canvass_points.csv` with full citations,
then the derived chain is rebuilt: `scripts/build_viz_data.py`,
`scripts/build_elections_master.py`, `scripts/gen_docs.py`, and the repo
test suites (vitest + pytest) run clean before commit. No derived file is
hand-edited.

**Human verification queue.** Load-bearing digits queue in one file for the
operator's hand-read: scan path, claimed value, and the threshold that
makes the digit load-bearing. Low/medium-confidence points ship flagged in
their source note rather than blocking (1949-11 precedent); the operator's
reading wins and corrections are applied to the CSV plus a rebuild.

**Dead ends.** An election that stays dry gets its failure mode recorded in
the search log: edit `docs/analysis/public-search-log.md` (the curated
source), which `build_viz_data.py` ships into `packages/data/ledger.json`
and `gen_docs.py` embeds verbatim in `docs/missing.md`. Record which issues
and page ranges were walked, what the pages printed instead (percentages
only, prose only, no box), and the remaining non-digital recourse
(microfilm, SOV, DOE records request).

## Stopping condition

An election is dry when its E+1 and E+2 Chronicle issues have been
page-walked (front pages plus the era-appropriate results-section range)
with the pan-capture technique, and its per-election alternates (other
editions, the multi-paper NewsBank sweep for specials) are tried. The
effort ends when all 16 are recovered or dry, or when blocked on operator
resources (SFPL login, microfilm, records request).

## Error handling

- ezproxy expiry: capture scripts already hard-abort on the SFPL auth page;
  a run that aborts mid-capture is re-run after the operator re-logs-in.
- Wrong-issue captures: the masthead gate rejects them; retry with adjacent
  dates or alternate spellings per the skill.
- Dead subagents: findings persist on disk incrementally; salvage from
  `mirror/` rather than re-capturing.
- Parallel-window occlusion: distinct WIN index per concurrent run.

## Expectations

Several recoveries plus a few documented dead ends (1977-08 and 1984-06 are
the likeliest failures). The 83 does not reach zero in this effort; the
README and `docs/missing.md` counts drop by however many records pass the
gates, and the search log grows by every dry attempt.
