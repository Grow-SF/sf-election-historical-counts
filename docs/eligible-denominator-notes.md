# The "eligible" denominator for San Francisco — sources, seams, and estimates

This documents how the *franchise* denominators (eligible population, and the
voting-age population) were assembled for the registration-vs-eligible work, and
where the seams and estimates are — so the numbers can be trusted exactly as far
as they should be. Companion to the [archive-recovery runbook](archive-recovery-runbook.md).

## The question and the two denominators

"Did universal vote-by-mail expand the franchise?" needs more than turnout of the
*registered*. It needs:
- **Registration ÷ eligible** — did mail voting pull more eligible people onto the rolls?
- **Eligible / voting-age population over time** — the baseline pool itself.

Finding (consistent across every source): no expansion. SF's registered share of
eligible has held **~70–86% since 1978**, flat through the all-mail transition;
SF was already near the ceiling.

## Where the eligible (citizen) figure comes from, by era

| Era | Source | Notes |
|---|---|---|
| 2000–2026 | CA SoS **Reports of Registration** (county.pdf / .xlsx) | `data/sf_registration_eligible.csv`, via `scripts/fetch_sos_registration.py` |
| 1978–1998 | Printed **Statement of Vote** "Voter Participation by County" tables (archive.org) | `data/sf_registration_eligible_sov_1974_1998.csv`, via `scripts/recover_sov_registration.py` (read off page-image crops; **pending hand-verification**) |
| 1996 (cross-check) | Chronicle/NewsBank (SoS Bill Jones quote) | independent "eligible adult citizens" figure; confirms the denominator = citizen-VAP |

**Hard floor:** the SoS published **no county-level eligible figure before ~1973**
(verified: the 1962-64 and 1970-72 Statement of Vote volumes carry registration
by county but no eligible column). So a citizen-eligible rate cannot run back to
1964 on SoS data — 1978 is the clean start.

## Two seams to respect

1. **Denominator basis shift (~1976→1978).** The 1974 and 1976 SOV participation
   tables denominate by **voting-age population** (all adults: 1974 526,930;
   1976 535,094, the column literally labeled "Voting Age Population"). From 1978
   the figure is the **citizen-eligible** estimate (DOF "eligible to register":
   1978 470,773). VAP runs ~50–70k above citizen-eligible (the non-citizen adult
   gap), so the two are *not* comparable as a rate — 1974/76 are excluded from the
   registration-rate line and live in `data/sf_eligible_vap_estimate.csv` instead.
2. **Pre-NVRA "deadwood" (1994–96).** SF registration approached and then exceeded
   eligible (1994: 96.5%; Oct 1996: 482,541 registered vs 479,127 eligible =
   100.7%). The SoS (Bill Jones, via the Contra Costa Times, 1996-10-25, NewsBank
   docref 1063FBAA6480CFD4) named SF as the state's prime example of deadwood —
   "10 to 20 percent" of names. The 1995 federal motor-voter cleanups pulled the
   rate back into the band. These points are flagged `low` confidence.

Also: rolls **sawtooth** (peak at each general, purged after), and the DOF eligible
estimate is itself revised between reports (it even dips 2011–2013, and the 1988
SOV prints an anomalously high 554,796). Read the band, not single-report wiggles.

## Eligible (citizen voting-age) population over time

The wanted denominator is **eligible adult citizens**, not all-adult voting-age
population — SF has a large non-citizen adult share, so the two differ a lot. A
firm anchor: in 1990 the SoS citizen-eligible (484,956) was only **~80% of the
census's 607,210 adults** (and ~72% of total population in 1980). All-adult VAP
overstates eligible by that ~20-pt gap; don't use it as the franchise denominator.

- **1978–2026 — published, do not estimate.** The eligible (citizen) figure is in
  the Statement of Vote / Reports of Registration: `sf_registration_eligible_sov_1974_1998.csv`
  (1978–1998) and `sf_registration_eligible.csv` (2000–2026; e.g. SF 2020 = 668,567,
  2026 = 658,495 eligible).
- **Pre-1978 — rough estimate only.** `data/sf_eligible_vap_estimate.csv`:
  eligible = decennial total (sourced) × an assumed citizen-of-total share
  (~0.55 in 1900 rising to ~0.68 by 1976, anchored to the 1980/1990 SoS-vs-census
  ratios; voting age 21+ pre-1971). Assumption-based; flagged per row.

**Why not the Census API:** as of 2026 it requires a key (data requests 302 to a
"Missing Key" page) and carries no pre-1990 data — so it can't reach 1899. Exact
pre-1978 citizen figures need Census *citizenship* tables (NHGIS / decennial
volumes), not just age tables.

## What's left
- Hand-verify the 1978–1998 SOV recoveries against the cited scans.
- 1992 *general* eligible: the Nov-1992 SOV participation table lacks an eligible
  column (only the June primary has one) — captured the primary instead.
- Replace the pre-1978 `eligible_citizen_est` rows with exact citizen-voting-age
  counts from NHGIS / archive.org decennial *citizenship* tables (1900–1970).
- 1964–1972 citizen-eligible is only reachable as a Census-derived estimate, not
  SoS primary data.
