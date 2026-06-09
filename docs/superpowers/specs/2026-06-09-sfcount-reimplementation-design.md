# SF Vote-Count Timeline — From-Scratch Reimplementation

**Date:** 2026-06-09
**Status:** Approved design

## Goal

Reimplement `sf-long-count-archive/` as a tested, maintainable, living pipeline
that can be re-run after every future SF election. The archive directory stays
untouched as reference; new code is built from scratch at the repo root using
strict TDD.

## Background

The archive was a one-shot build: a single ~290-line script (`sfcount.py`)
that scraped per-release `summary.pdf` files from sfelections.org, parsed them
with regexes over pdfplumber-extracted text, and produced two CSVs plus a
React/Recharts visualization with a hand-embedded data array. It had zero
tests, no packaging, no preserved raw inputs, and no script to regenerate the
visualization data.

## Key change: structured sources instead of PDFs

Probing (2026-06-09) confirmed SF Elections publishes machine-readable files
at the same snapshot URLs the PDF pipeline used
(`https://www.sfelections.org/results/{election}/data/{snapshot}/`):

| Era | Years | File | Format |
|---|---|---|---|
| C | 2019–present | `summary.xml` | Dominion ElectionSummaryReportRPT XML |
| B | 2008–2018 (snapshots exist from Nov 2015) | `summary.txt` | TSV, one row per contest/candidate |

Verified facts the design rests on:

1. `summary.xml` returns 200 for Era C snapshots (verified 2024-11, 2020-03,
   2019-11); `summary.txt` returns 200 for Era B snapshots (verified 2016-11,
   2016-06). `summary.xlsx` also exists for Era C but XML is preferred
   (stdlib parsing, no openpyxl dependency).
2. HTTP `Last-Modified` headers carry accurate report timestamps: the Nov 2024
   election-night `_1` release shows 2024-11-06 04:41 GMT = 8:41 PM Pacific,
   matching the known first-release time. This replaces the PDF-internal
   timestamp.
3. Era B primary TSVs contain a citywide `Registration & Turnout` block
   (party field empty) alongside per-party blocks — eliminating the old
   "max across party blocks" heuristic.
4. Era C XML separates voters from cards explicitly
   (`RegistrationAndTurnout` block: registered voters, total voters cast, and
   per-counting-group ED/VBM voter counts) — avoiding the 2019-layout
   "Ballots Cast counts cards" trap the PDF parser had to dodge.

## Repo layout

```
sf-election-count/
├── pyproject.toml            # uv-managed; runtime dep: requests only
├── sfcount/
│   ├── cli.py                # argparse: inventory|fetch|parse|validate|derive|artifact|all
│   ├── inventory.py          # Stage 0: scrape sf.gov election list → elections.csv
│   ├── fetch.py              # probe & download xml/txt; manifest records Last-Modified
│   ├── parsers.py            # parse_era_c_xml(), parse_era_b_tsv() — pure functions
│   ├── archival.py           # the two 2012 Wayback rows (data, not code)
│   ├── validate.py           # monotonicity, ED+VBM=total, certified cross-checks
│   ├── derive.py             # days-to-90 stats
│   └── artifact.py           # regenerates the data array in the JSX
├── data/                     # committed output CSVs — the published dataset
├── raw/                      # downloaded xml/txt (gitignored)
├── artifact/sf-long-count.jsx
├── tests/                    # pytest; tests/fixtures/ holds real downloaded xml/txt
├── docs/superpowers/specs/   # this document
└── sf-long-count-archive/    # untouched reference implementation
```

## Pipeline behavior

**Fetch.** Same proven probe strategy as the original: election-night
suffixes `{date}_1` … `{date}_6`, then daily candidates election day through
election day + 35; probe-miss cache on disk makes reruns free; rate-limited
with a polite User-Agent; never re-download an existing file. Downloads
`summary.xml` or `summary.txt` per the election's era. The manifest gains a
`last_modified` column captured from the response header at download time.
Misses for future report dates of an ongoing count are not cached as
permanent.

**Timestamps.** `report_datetime` = `Last-Modified` converted to
America/Los_Angeles via stdlib `zoneinfo`. New `datetime_source` column
(`header` | `archival`) records provenance. Election-night snapshots without a
header timestamp (if any) fall back to the folder date, tagged accordingly.

**Era C parser.** Pure function: XML text in → record out. From the
`RegistrationAndTurnout` block: total ballots cast (voters), registered
voters, ED/VBM split from the per-counting-group details. Uses voters
attributes, never cards attributes. Implementation must check whether the
Nov 2019 XML carries the ED/VBM split its PDF lacked — if so, those 13
previously-blank rows get recovered (a strict improvement over the archive;
the reconciliation gate treats it as such, not as a mismatch).

**Era B parser.** Pure function over TSV. Selects rows where contest is
`Registration & Turnout` and the party field is empty (citywide block):
ED and VBM turnout from the two candidate rows, registered voters from
`CONTEST_TOTAL`, total = ED + VBM.

**Validate.** A real subcommand and CI gate, not an inline warning loop:

- cumulative totals monotonic non-decreasing within each election
  (violations reported, run fails)
- ED + VBM = total on every row that has the split
- certified-final cross-checks: Nov 2024 = 412,231; Nov 2016 = 414,528;
  Nov 2012 = 364,875
- nonzero exit code on any failure

**Derive.** Same definitions as the archive — per election: final ballots
(max total), first release ≥ 90% of final (date and days-since-election),
percent counted by end of election night. Latent bugs fixed: no unguarded
`None` access when no release qualifies; missing datetimes handled
explicitly; warnings emitted through one path. Archival-parser elections
remain excluded from days-to-90.

**Archival rows.** The two Nov 2012 Wayback-recovered rows carry over
verbatim as data with `parser=archival`, `datetime_source=archival`.

**Artifact generator.** The missing link in the old project. Reads the two
output CSVs and rewrites the `const E = [...]` block in
`artifact/sf-long-count.jsx` between explicit marker comments. Encodes the
rules currently buried in the hand-built array:

- `d` (x-axis) = days since 8:00 PM Pacific on election night
- `kind` classified from election name keywords
  (Primary/General/Municipal/Special/Recall)
- `prov: true` for not-yet-certified elections (election date within ~32 days
  of run date)
- `pts` entries carry `[d, pct_total, pct_vbm, pct_ed]` with nulls where the
  source publishes no split
- regeneration is idempotent

**Output schema.** Same columns as the archive's `sf_count_timeline.csv`
plus `datetime_source`. Parser tags: `era_c_xml`, `era_b_tsv`, `archival`.
`source_url` points at the xml/txt file actually parsed.

## TDD and test strategy

Red-green-refactor for every module: write the failing test first, implement
to green, refactor.

**Fixtures:** real downloaded files committed to the repo (small text files):

- Era B general: Nov 2016 snapshot `summary.txt`
- Era B primary: Jun 2016 snapshot `summary.txt` (per-party + citywide blocks)
- Era C current: Nov 2024 snapshot `summary.xml`
- Era C early variant: Nov 2019 snapshot `summary.xml`
- One election-night (`_1`) snapshot

**Test layers:**

| Layer | Coverage |
|---|---|
| Parsers | Exact expected numbers per fixture; malformed/empty input → explicit error, never a silent skip |
| Derive | Synthetic timelines: 90% crossing day, election-night %, single-report election, non-monotonic input |
| Validate | Split-sum and certified-final checks; failing input actually fails with nonzero exit |
| Artifact | The 8 PM `d` math, kind classification, null-split handling, idempotent regeneration |
| Fetch | Probe-candidate generation, miss-cache behavior, Last-Modified capture — `requests` mocked, no network |
| End-to-end | Parse a fixture tree → golden CSV comparison; certified cross-checks against committed `data/` |
| Network | Live smoke tests, opt-in via `pytest -m network`; default suite runs offline and fast |

**Migration acceptance gate:** after the one-time refetch (~25 min,
resumable), every ballot count (`ballots_counted_total`, `ballots_vbm`,
`ballots_election_day`, `registered_voters`) from the new pipeline must match
the archive's PDF-derived `sf_count_timeline.csv` exactly — two independent
source formats agreeing row for row. Expected, documented differences:
`report_datetime` shifts by minutes (header time vs. PDF-internal render
time); Nov 2019 rows may gain a previously-unavailable ED/VBM split. After
the gate passes, the committed `data/` CSVs become the regression baseline.

## Out of scope this round

- Era A (pre-2008) recovery and deeper Wayback work (a local Wayback stage
  could extend the 2012 single-point recovery; future project)
- Deploying the visualization as a website (the JSX remains a self-contained
  artifact)
- RCV rounds, contest-level results, precinct data

## Decisions log

- Living pipeline, not a frozen artifact (user, 2026-06-09)
- Visualization stays a self-contained JSX artifact; data array regenerated
  by script (user, 2026-06-09)
- Ingest structured data files, not PDFs (user, 2026-06-09)
- Full from-scratch reimplementation with TDD; archive is reference only
  (user, 2026-06-09)
- Approach: single structured-file pipeline with one-time reconciliation
  against the PDF-derived archive CSV, not a permanent dual pipeline
  (user, 2026-06-09)
