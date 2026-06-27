---
name: researching-jurisdiction-counting-tech
description: Use when researching ONE US county/jurisdiction's election counting-technology adoption (electronic pollbooks, automated signature verification, "Sign-Scan-and-Go" / vote-center mail processing) and its ballot-reporting-speed metrics for the Long Count county comparison. Symptoms: a worklist of counties to fill in, a county_speed / county-tech row to source, "find the adoption year and the reporting speedup".
---

# Researching one jurisdiction's counting tech + reporting speed

## Overview

Produce ONE structured record for a single jurisdiction: which counting tech it
adopted, the year, and its reporting-speed metrics — every value tied to a
**primary source**, every value carrying a **confidence**, and metrics that
**never substitute one definition for another**. A value you cannot source to
its required definition is `null` with a reason — never a different number in
its place.

Return the record below. Nothing else is the deliverable.

## Output contract — return exactly this object

```json
{
  "jurisdiction": "Orange County",
  "state": "CA",
  "tech": [
    {"type": "epollbook",    "status": "adopted",     "adopted_year": 2020, "first_election": "2020-03", "vendor": "Tenex Precinct Central", "evidence_url": "<primary>", "confidence": "primary"},
    {"type": "asv",          "status": "not-adopted", "adopted_year": null, "evidence_url": "<primary>", "confidence": "secondary"},
    {"type": "sign-scan-go", "status": "not-adopted", "adopted_year": null, "evidence_url": "<primary>", "confidence": "secondary"},
    {"type": "vote-center",  "status": "adopted",     "adopted_year": 2020, "first_election": "2020-03", "evidence_url": "<primary>", "confidence": "primary"}
  ],
  "metrics": [
    {"metric": "oneweek_pct",      "year": 2024, "value": 91.8, "denominator": "certified final ballots", "source_url": "https://calvoter.org/content/ballot-processing", "confidence": "primary"},
    {"metric": "electionnight_pct","year": 2024, "value": 74.3, "denominator": "certified final ballots (1,052,969 / 1,417,397)", "source_url": "<ocvote primary>", "confidence": "primary"},
    {"metric": "days_to_90",       "year": 2024, "value": null, "denominator": null, "source_url": null, "confidence": "none", "note": "county does not publish per-day canvass totals"}
  ],
  "notes": "free text: ambiguities, what you could not find, anything a verifier should re-check"
}
```

- `tech[]` MUST cover all four types — **including the ones NOT adopted**.
  "not-adopted" is a finding (with evidence), not a missing cell.
- `adopted_year` = the year of the **first election actually conducted with the
  tech**, not the board-vote / contract-award date (note that date in `notes`).
- `metrics[]` is long-form: one entry per (metric, election year). Attempt every
  metric for every recent even-year general (and the latest odd-year) you can.

## Metric definitions — do NOT conflate

| metric | definition | denominator (required) | where to get it |
|---|---|---|---|
| `oneweek_pct` | share counted within **7 days** of Election Day, *as CalVoter publishes it* | CalVoter's basis: ballots counted by day 7 ÷ ballots counted to date (looser than "certified final" — record it as published, don't recompute) | **California Voter Foundation "Ballot Processing"** — per-county, by year; the canonical comparable metric, **always attempt first.** Values are read off CalVoter's per-year charts → mark for the verification pass to read precisely. |
| `electionnight_pct` | ballots in the **first post-poll-close report** ÷ certified final | **certified final ballots** | county election-night report + certified Statement of Vote |
| `days_to_90` | days after Election Day until counted **≥ 90%** of certified final | — | per-release daily canvass updates (many counties don't publish → `null`) |

If the metric's required denominator isn't available (e.g. only "% of
**registered** voters" is published, not % of final), the value is `null`,
confidence `"none"`, with the reason in `note`. Reporting a different
denominator as the metric is the #1 way this dataset goes wrong.

## How to find each field

- **Tech + year:** CA Secretary of State **Voter's Choice Act** adoption page
  (county × year) and **"Voting Technology by County"** / certified-systems
  list; the county Registrar's **Election Administration Plan** + press
  releases; **Verified Voting** (vendor/system). adopted_year = first election
  with the tech.
- **ASV specifically:** search "signature verification software / scanner /
  automated matching". Humans comparing envelope signatures by eye (even from
  scanned images) = `status: "not-adopted"` — a real finding, cite it.
- **Distinguish** e-pollbook (digital roster) from the tabulation/voting system
  (e.g. Hart Verity), from a drop-box ballot scanner, from the vote-center
  model. They are different `type`s or `notes`, not the same thing.

## Confidence

`primary` = official registrar/SoS/CalVoter document · `secondary` =
news / Verified Voting · `estimated` = derived or uncited · `none` = not found.
Every `value`/`status` carries one.

## Common mistakes (observed in baseline runs)

- Skipping CalVoter "Ballot Processing" → no comparable `oneweek_pct`. Attempt it first.
- Substituting "% of registered voters" when election-night "% of final" isn't found → use `null`, not the wrong denominator.
- Returning a prose write-up → return the schema object.
- "Uses e-pollbooks" with no year / first election → `adopted_year` is required.
- Treating "not adopted" as a gap → it is a finding; set `status` and cite it.
- Trusting a prior research summary's numbers → re-verify against the primary; a summary is `secondary` at best.
