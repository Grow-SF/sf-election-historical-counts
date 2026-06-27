---
name: researching-election-night-share
description: Use when finding a US county/jurisdiction's ELECTION-NIGHT ballot-count share (share of the certified final counted in the first post-poll-close report) across elections that bracket its adoption of electronic pollbooks and/or automated signature verification — to test whether that tech moved the election-night number. Symptoms: a pre/post-adoption election-night comparison, "did e-pollbooks/ASV speed up the election-night count," filling an election-night row for a county.
---

# Researching a county's election-night share (pre/post tech adoption)

## Overview

Produce, for ONE county, its **election-night %** for the elections that bracket
its e-pollbook and ASV adoption years — so we can see whether the tech moved the
metric it should (election-night, not the one-week rate). Election-night % is the
share counted in the **first report after polls close**; e-pollbooks (ending the
Monday pause) and ASV (faster signature checks) should raise it if they help.

`election-night % = first-post-poll-close-report ballots ÷ certified final ballots`

A value you cannot source to that definition is `null` with a reason — never a
substituted denominator (e.g. "% of registered voters").

## Hard environment constraint (read first)

**The Wayback Machine (web.archive.org / archive.today / archive.ph) is BLOCKED
here** — WebFetch refuses it and the browser fails to load it. The precise 8 p.m.
first-tranche count usually lives only in archived captures of the registrar's
live results page (which is overwritten each update). So in this environment:

- The **numerator** (election-night ballots) comes from the county's
  **election-night press release** (e.g. countynewscenter.com, the registrar's
  newsroom, sf.gov-style releases) or **reputable local news** quoting the first
  count. These are often **approximate** ("nearly 900,000 counted as of …") —
  record them as proxies with `confidence: "secondary"` and a note.
- If no first-report figure can be sourced, set the value `null`,
  `confidence: "none"`, and explain — do NOT guess.

## Output contract — return exactly this object

```json
{
  "jurisdiction": "San Diego County",
  "state": "CA",
  "adoption": { "epollbook": 2022, "asv": 2024 },
  "elections": [
    {
      "date": "2020-11-03", "type": "presidential-general",
      "election_night_ballots": null, "certified_final": 1627753,
      "election_night_pct": null,
      "vs_epollbook": "pre", "vs_asv": "pre",
      "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2020-general/sov/03-voter-participation-stats-by-county.pdf",
      "source_url_night": null, "confidence": "none",
      "note": "first-report count not sourceable without Wayback (blocked); certified final is solid"
    }
  ]
}
```

- Cover the November generals (and the latest odd-year) that **bracket** the
  adoption years: at least one election BEFORE the earliest adoption and the most
  recent ones AFTER.
- `vs_epollbook` / `vs_asv` = `"pre"` / `"post"` relative to that tech's
  `adopted_year` (read it from `packages/data/county_tech.json`, or it's given to
  you). `"n/a"` if the tech was never adopted.

## How to find each field

- **Certified final (denominator) — reliable:** CA Secretary of State
  **"Statement of Vote → Voter Participation Statistics by County"** PDF for that
  election (`elections.cdn.sos.ca.gov/sov/<year>-general/sov/03-voter-participation-stats-by-county.pdf`).
  This is authoritative; always get it.
- **Election-night count (numerator) — best effort:** the county registrar's
  **first-results press release** (newsroom / county news center), then local
  news. State the report time you used (8 p.m. first tranche vs end-of-night).

## Watch the election-type confound

Turnout swings the denominator hugely (presidential ≫ midterm ≫ odd-year), so the
**cleanest pre/post comparison is like-to-like** (presidential vs presidential).
Always record `type`, and note when a comparison mixes election types.

## Confidence

`primary` = official registrar release / SoS · `secondary` = news / a proxy
("end-of-night ~X") · `estimated` = derived · `none` = not found. The certified
final is usually `primary`; the election-night value is usually `secondary` (proxy)
or `none` in this environment.

## Common mistakes (from the baseline)

- Reporting "% of registered voters" because the true first-report count wasn't
  found → use `null`, not the wrong denominator.
- Treating an end-of-election-night running total as the 8 p.m. first tranche
  without noting it → label which report time the number is.
- Relying on Wayback → it's blocked here; go to press releases / news.
- Comparing a presidential to a midterm election-night share as if equivalent →
  note the type mismatch.
