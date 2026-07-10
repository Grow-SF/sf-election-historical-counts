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
| 2000–2026 | CA SoS **Reports of Registration** (county.pdf / .xlsx) | `data/sources/sf_registration_eligible.csv`, via `scripts/fetch_sos_registration.py` |
| 1978–1998 | Printed **Statement of Vote** "Voter Participation by County" tables (archive.org) | `data/sources/sf_registration_eligible_sov_1974_1998.csv`, via `scripts/recover_sov_registration.py` (read off page-image crops; **pending hand-verification**) |
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
   registration-rate line and live in `data/sources/sf_eligible_vap_estimate.csv` instead.
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
- **1900–2020 — real census voting-age population (IPUMS NHGIS).**
  `data/sources/sf_eligible_vap_estimate.csv` now carries actual NHGIS county counts, not
  estimates (`scripts/nhgis_extract.json` reproduces the pull). Eligible-age basis:
  21+ before 1971, 18+ after; and **women could not vote before 1920** (CA 1911),
  so the 1900/1910 electorate is **male 21+**. Selected: 1900 VAP 128,985 (men);
  1920 366,227; 1960 531,381; 1990 607,076 (matches the Bay Area Census 607,210 ✓);
  2020 **760,738** all-adult — vs the SoS *eligible* 668,567, i.e. ~92k non-citizen
  adults, confirming all-adult VAP is the wrong franchise denominator.
  - **Citizen-eligible (now real, not assumed).** From census citizenship tables
    (`scripts/nhgis_extract_citizenship.json`): **1900 = 100,697 citizen men 21+**;
    1910 ≈ 133,000; **1940 = 443,386, 1950 = 554,171, 1970 = 461,919** are direct
    (VAP minus the census alien count by age — 1970 from a Citizenship-by-Age table);
    1920 (304,136) and 1930 (401,112) use the real foreign-born-21+ count × an alien
    share interpolated from 1910/1940/1970 (Asians counted non-citizen — barred from
    naturalization until 1943/1952); 1960 (490,965) is interpolated because the 1960
    census asked no citizenship question.
  - **The immigrant arc shows in the data:** alien-share-of-foreign-born ran 36.5%
    (1940) → 23.9% (1950, WWII-era naturalization) → 44.0% (1970, post-1965 Latin
    American/Asian wave). Citizen voting-age peaked ~554k (1950), then *fell* to
    ~462k (1970) as the city lost population and non-citizens rose.

**Citation (required).** IPUMS NHGIS data: *Jonathan Schroeder, David Van Riper,
Steven Manson, Katherine Knowles, Tracy Kugler, Finn Roberts, and Steven Ruggles.
IPUMS National Historical Geographic Information System: Version 20.0 [dataset].
Minneapolis, MN: IPUMS. 2025. http://doi.org/10.18128/D050.V20.0* — and this work
should be added to the IPUMS bibliography (https://bibliography.ipums.org/).

**Why not the Census API:** as of 2026 it requires a key and carries no pre-1990
data — NHGIS (above) is the route for the historical county figures.

## What's left
- Hand-verify the 1978–1998 SOV recoveries against the cited scans.
- 1992 *general* eligible: the Nov-1992 SOV participation table lacks an eligible
  column (only the June primary has one) — captured the primary instead.
- Replace the pre-1978 `eligible_citizen_est` rows with exact citizen-voting-age
  counts from NHGIS / archive.org decennial *citizenship* tables (1900–1970).
- 1964–1972 citizen-eligible is only reachable as a Census-derived estimate, not
  SoS primary data.
