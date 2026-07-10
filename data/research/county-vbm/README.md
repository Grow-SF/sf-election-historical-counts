# `data/research/county-vbm/`: county vote-by-mail composition panel

Per-county, per-election vote-by-mail share for the 19-county election-night panel
(see [`../election-night/`](../election-night/) and [`../county-tech/`](../county-tech/)
for the companion counting-technology and night-count datasets this is meant to be
joined against). This dataset answers a narrower question than either of those: for
each county and each statewide election, what fraction of counted ballots arrived by
mail versus in person? That mail/polling split is the composition covariate needed to
separate "the county's mail share shifted" from "the county's counting technology got
faster" when reading a change in election-night reporting share over time.

## File

### `county_vbm_share.csv`

**Coverage:** 228 rows = 19 panel counties x 12 statewide elections (both the primary
and the general in each of 2012, 2014, 2016, 2018, 2022, 2024; 2020 is intentionally
excluded, because it was the pandemic all-mail year and is a poor composition baseline
for every county, not just SF). No gaps: every county has a row for every election.

**Panel counties:** Colusa, Del Norte, Fresno, Lake, Los Angeles, Madera, Mendocino,
Napa, Nevada, Orange, Placer, Riverside, Sacramento, San Bernardino, San Diego, San
Francisco, San Mateo, Santa Clara, Tehama (the same 19 as the election-night and
county-tech panels).

| column | meaning |
|---|---|
| `county_slug` | lowercase, underscore county name (e.g. `san_francisco`, `los_angeles`) |
| `election_date` | `YYYY-MM-DD` |
| `election_type` | `primary` or `general` |
| `ballots_mail` | ballots counted that were cast by mail (vote-by-mail), from the SoS's "Vote-By-Mail Voters" column |
| `ballots_polling` | ballots counted that were cast in person, from the SoS's "Precinct Voters" column (for VCA counties, this is vote-center in-person ballots; for all-mail counties, 0 by design) |
| `ballots_total` | `ballots_mail + ballots_polling`, exactly, for every row (verified, see below) |
| `vbm_share_pct` | `round(100 * ballots_mail / ballots_total, 2)` |
| `source_url` | the exact SoS PDF this row's numbers were read from |
| `source_page_or_table` | the table name inside the PDF (`VOTER PARTICIPATION STATISTICS BY COUNTY` for all 228 rows) |
| `note` | free text; blank except where a source footnote changes the reading of a row (see Colusa below) |

## Source

California Secretary of State, Statement of Vote, "Voter Participation Statistics by
County" table: the SoV's own tally of ballots cast by mode (not a registration or
eligibility table). This single table carries native "Precinct Voters," "Vote-By-Mail
Voters," and "Total Voters" columns, so it directly supplies all three ballot counts
for every county on one page per election. It is the same source-URL family the repo
already uses for `data/sources/sf_vbm_share_sos.csv`.

**URL patterns observed** (exact URLs are in every row's `source_url`; the path is not
fully stable across eras, see the sweep log for the two exceptions):

- 2012/2014: `https://elections.cdn.sos.ca.gov/sov/<YYYY>-<primary|general>/[pdf/]03-voter-<participation|reg>-stats-by-county.pdf`
  (2012 primary's filename literally says `voter-reg-stats`; the table inside is the
  same participation-by-mode table. 2014's filename has the misspelling
  "particpiation," intact in the SoS's own filename.)
- 2016 general onward: `.../sov/<election>/sov/03-voter-participation-stats-by-county.pdf`
  (a `sov/` subfolder segment appears from 2016 general on)
- 2016 primary is the one exception to that pattern: no `sov/` subfolder
  (`.../sov/2016-primary/03-voter-participation-stats-by-county.pdf`); the `sov/`-subfolder
  URL for that date 403s.

Full per-election URLs, HTTP status, and extraction notes for all 12 elections are in
`scratchpad/vbm-sweep-log.md` (the sweep log this dataset was promoted from). PDFs were
converted with `pdftotext -layout` and parsed with a per-county regex that strips
thousands separators and footnote asterisks before computing `vbm_share_pct`.

## Verification performed before promotion

- **Identity check:** `ballots_mail + ballots_polling == ballots_total` holds exactly
  for all 228 rows.
- **Recomputation:** `vbm_share_pct` was independently recomputed as
  `round(100 * ballots_mail / ballots_total, 2)` for all 228 rows and matches the
  stored value exactly (no row differs).
- **Fresh re-fetch, 3 elections spanning the panel's eras:** the 2012, 2018, and 2024
  general-election SoV PDFs were re-downloaded directly from `source_url` (not reused
  from the original sweep's cached copies) and re-read with `pdftotext -layout`. Six
  counties' lines per election (18 county-election cells total, including San
  Francisco, Colusa, Del Norte, and at least one VCA/all-mail county per era: Napa/
  Sacramento in 2018, Los Angeles/Placer in 2024) were checked against the CSV
  byte-for-byte on `ballots_mail`, `ballots_polling`, `ballots_total`, and
  `vbm_share_pct`. All 18 matched exactly.
- **SF cross-check against the existing repo dataset:** San Francisco's rows on the 4
  dates that overlap `data/sources/sf_vbm_share_sos.csv` (2012-06-05, 2012-11-06,
  2014-06-03, 2014-11-04) match that file's `vbm_share_pct` to within 0.0-0.05
  percentage points, the expected difference between this file's 2-decimal rounding
  and that file's 1-decimal rounding, not a data discrepancy.

## The Colusa all-mail-2024 footnote

Colusa's two 2024 rows (2024-03-05 primary, 2024-11-05 general) show
`ballots_polling = 0` and `vbm_share_pct = 100.0`. This is not a data gap: the source
SoV PDF marks Colusa with a `**` footnote meaning "all-mail-ballot county" for both
2024 elections: Colusa mailed every ballot and ran no precinct/polling-place voting
that cycle, so the true polling count is zero, not missing. Both rows carry this
explanation in their `note` column. (Colusa's earlier elections, 2012-2022, have
nonzero `ballots_polling`; the all-mail status is specific to 2024 in this panel, not
a standing feature of the county.)

More generally, the source PDFs carry two footnote conventions worth knowing when
extending this panel: `*` marks a Voter's Choice Act (VCA) county (its "Precinct
Voters" column counts vote-center in-person ballots, not traditional precinct
ballots), and `**` marks an all-mail-ballot county (0 precinct/vote-center ballots).
Neither footnote changes the `mail + polling = total` identity; they only change what
"polling" means for that county-election. See `scratchpad/vbm-sweep-log.md` item 7 for
the full footnote-driven VCA-jump cross-check (Napa, Sacramento, San Mateo, Madera,
Nevada all jump sharply in mail share the first general at/after their VCA year,
confirming the footnote reading against `packages/data/county_tech.json`).

## Provenance conventions

Consistent with the rest of `data/research/`: every row cites its exact `source_url`
and `source_page_or_table`, values are read directly from the cited PDF (never
computed from an external total or estimated), and `2020` is deliberately excluded
from this panel rather than included and flagged, because the pandemic universal-mail
year is not a meaningful composition baseline for *any* county in the panel (mail share
spiked for reasons unrelated to each county's underlying voting behavior or counting
technology). The full sweep log with per-election extraction detail, cross-checks, and
the reasoning above lives at `scratchpad/vbm-sweep-log.md` in the authoring session's
scratch space; this README distills what a reader of the committed dataset needs.

## Known limitation

This panel is election-mode composition (mail vs. polling), not counting-*speed*
composition. It answers "how much of the electorate voted by mail" so that a downstream
analysis can separate a composition effect from a technology effect on election-night
reporting share, see
[`../../docs/analysis/2026-07-10-vbm-composition-curve.md`](../../docs/analysis/2026-07-10-vbm-composition-curve.md)
for that application, calibrated on San Francisco and applied to this panel's 10
e-pollbook-adopting treated counties.
