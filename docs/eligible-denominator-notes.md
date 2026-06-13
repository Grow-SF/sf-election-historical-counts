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

## Voting-age population over time (rough estimate)

`data/sf_eligible_vap_estimate.csv` — VAP (all adults), every row flagged by basis:
firm anchors from the 1970/1980 census and the 1974/76 SOV; 1960–1968 interpolated
from the decennial census (voting age was 21+ until the 26th Amendment, 1971).
SF VAP sat ~530–560k through the 1960s–80s. **Gap:** clean 1990–2020 decennial VAP
anchors still need the Census API/NHGIS (the API was unreachable in the build
session); the citizen-eligible series (SoS) covers 2000–2026 in the meantime.

## What's left
- Hand-verify the 1978–1998 SOV recoveries against the cited scans.
- 1992 *general* eligible: the Nov-1992 SOV participation table lacks an eligible
  column (only the June primary has one) — captured the primary instead.
- 1990–2020 decennial VAP anchors (Census API / NHGIS) to complete the VAP line.
- 1964–1972 citizen-eligible is only reachable as a Census-derived estimate, not
  SoS primary data.
