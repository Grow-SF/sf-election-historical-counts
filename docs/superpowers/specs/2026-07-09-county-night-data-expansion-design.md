# Expanding the county election-night dataset (more panels, harder evidence)

**Date:** 2026-07-09
**Status:** approved design, pending implementation plan
**Owner:** Claude session, operator Steven

## Goal

The "Election-night share over time, by county" chart
(`packages/charts/src/components/CountyNightTimelineChart.tsx`) currently
renders 6 panels: the SF control plus the 5 counties whose series are
complete (LA, Napa, Nevada, Orange, San Mateo). Eight more researched
counties sit invisible in `data/research/election-night/` because one or
more of their November generals (2012-2024, 2020 excluded) has a null
plateau. The goal is to move counties from hidden to shown by filling those
nulls from source routes not yet tried, then to widen the dataset with new
counties chosen for archive-friendliness. Every attempted row ends in one
of two states: a sourced plateau that passes the full RUNBOOK pipeline, or
a dated dead-end note extending the existing one so no future pass redoes
the ground.

Target: 10 or more panels on the chart, including at least one additional
no-new-tech control county alongside SF.

## Gap census (what stands between each county and the chart)

Distance from `complete` (nulls among the six chart years 2012, 2014,
2016, 2018, 2022, 2024), nearest first:

| county | missing years | flagged (comparable=false) | most promising untried route |
|---|---|---|---|
| Sacramento | 2016 | | Sacramento Bee via NewsBank (the row's own note flags this: "FLAG for manual operator ... the Sacramento Bee is the most likely place") |
| Santa Clara | 2016, 2018 | 2014 ceiling | San Jose Mercury News via NewsBank |
| Madera | 2012, 2014 | | Fresno Bee / Madera Tribune via NewsBank |
| San Diego | 2012, 2014, 2016 | | San Diego Union-Tribune via NewsBank |
| Fresno | 2012, 2014, 2018, 2022 | | Fresno Bee via NewsBank |
| Placer | 2012, 2022, 2024 | 2018 ceiling | Sacramento Bee via NewsBank |
| Riverside | 2012, 2014, 2016, 2018 | 2024 ceiling | Press-Enterprise via NewsBank |
| San Bernardino | 2012, 2014, 2016, 2018, 2022 | | SB Sun / Press-Enterprise via NewsBank |

The existing null-row notes show Wayback, Clarity, county report series,
and press-release routes are genuinely exhausted for these rows. What has
NOT been tried, anywhere in the dataset:

1. **NewsBank print archives via SFPL ezproxy.** The repo has proven
   tooling (isolated Chrome, all-publications search) and has already
   recovered SF night counts from the Sacramento Bee and Mercury News for
   other purposes. McClatchy web properties 403 curl, but their print
   archives are fully searchable in NewsBank. Morning-after articles carry
   either an explicit "N ballots counted" or a same-contest ratio floor
   (candidate votes / printed percent), both admissible under RUNBOOK 5.2
   as secondary floors.
2. **Web archives other than Wayback.** The Library of Congress United
   States Elections Web Archive (crawls state and county election sites
   around each November election), CDL Archive-It collections (California
   government sites), archive.today, and the Common Crawl index (monthly
   crawls; a November crawl can hold a live results page). Every existing
   dead-end note enumerates only web.archive.org CDX.
3. **Report-URL and DocumentCenter ID enumeration.** Several counties
   serve archived report PDFs at guessable URLs (Nevada County's
   DocumentCenter View/55078 pattern, Fresno's
   `electionsummaryreportrpt_<M_D_YY>_<HHMM>.pdf`). Neighboring IDs and
   timestamp patterns for the missing years were never probed
   systematically against the live county CMS (only via Wayback).
4. **Registrar social media.** County registrars post election-night
   totals on Twitter/X and Facebook; Wayback holds captures of those
   accounts (e.g. @sacvote, @sdvote) that were never searched.

## Approaches considered

**A. Fill the gaps in the 13 existing counties via the untried routes
(recommended first).** Cheapest visible win: Sacramento is one row from a
panel, Santa Clara and Madera two, San Diego three. Nine rows could add
four panels.

**B. Add new counties end to end.** Six rows each plus tech-adoption
research, but candidates can be CHOSEN for archive-friendliness instead of
inherited: the Clarity CDN serves every version ever published, immutably,
no Wayback needed, so a CA county with Clarity history back to 2012-2014
(to be scouted by enumerating `results.enr.clarityelections.com/CA/...`)
starts with gold-standard plateau evidence for every year. Also scout for
LA-style morning-after press-release archives. Include at least one
no-new-tech control county to corroborate the SF baseline; the county-tech
skill fills the adoption records.

**C. Evidence hardening of shown rows.** Upgrade secondary floors when a
better source surfaces, add plateau verdicts, chase the deliberately open
Nevada yubanet primary-vs-secondary question only if registrar PDFs
surface. Improves rigor, not panel count; done opportunistically alongside
A and B, never as its own pass.

Chosen sequencing: A, then B, with C opportunistic. Rationale: A's rows already have
denominators, tech records, VERIFY.md sections, and dead-end notes to
extend; each recovered row is one surgical edit plus pipeline run.

## Out of scope (editorial, needs Steven's explicit sign-off, not data work)

- Extending the chart window to 2008/2010 (YEARS is fixed in the chart and
  the SoS SOV route covers those years, but the window is a presentation
  choice).
- Relaxing the `complete` gate to show partial series.
- Non-CA jurisdictions (the county_tech NY/PA/WI entries are state
  aggregates, not jurisdictions; the denominator playbook is CA SoS).
- Public records (CPRA) requests: ruled out by the operator on 2026-07-09;
  automated source recovery only.

## Method constraints (all inherited, none new)

- The metric, schema, floor/ceiling rules, note conventions, plateau
  verdicts, and the full verification pipeline are exactly RUNBOOK
  (`docs/research/RUNBOOK.md`) sections 1-8; the per-county procedure is
  the `researching-election-night-share` skill; new-county tech records go
  through the `researching-jurisdiction-counting-tech` skill.
- Newspaper-derived numbers: apply the RUNBOOK calibration checks
  (first-tranche numbers run near HALF the like-for-like SF share); record
  as floor + secondary unless the article states the end-of-night total
  explicitly; the note carries the docref and the exact quoted sentence,
  copy-pasteable, dead ends included (reproducible-provenance rule).
- NewsBank sessions run one at a time in the isolated Chrome profile, never
  from parallel subagents, browser otherwise idle.
- Research subagents persist findings to disk after each item; batch 1-2
  rows per subagent.
- Derived files (`county_night.json`, MACHINE_CHECK, HUMAN_VERIFY) are
  regenerated, never edited; every data change runs the full section-3
  pipeline and ends in a human-verify packet entry.

## Success criteria

- Sacramento reaches `complete` and renders on the chart (single highest
  value row: 2016).
- At least two further counties reach `complete` (any of Santa Clara,
  Madera, San Diego, or a new Clarity-scouted county).
- At least one new no-new-tech control county is added end to end.
- Every attempted row ends sourced-and-verified or with its dead-end note
  extended with the new routes tried (dated, specific queries listed).
- Validator exit 0, machine checks pass, plateau verdicts present,
  VERIFY.md and the human packet regenerated, chart tests green.

## Risks

- Newspaper articles may print first-tranche numbers dressed as night
  totals; the calibration check and the precincts-reporting figure in the
  quote are the defense.
- NewsBank coverage windows: Bee/Mercury/U-T text coverage through
  2012-2018 is believed good but unproven for these counties; the first
  Phase 1 session doubles as a coverage probe.
- archive.today has no API and aggressive bot walls; browser-only, and a
  miss there is cheap to record.
- Clarity scouting may find no CA county with pre-2016 JSON history
  (Web01-era versions are HTML-only); then Phase B counties come from the
  press-release scout instead.
