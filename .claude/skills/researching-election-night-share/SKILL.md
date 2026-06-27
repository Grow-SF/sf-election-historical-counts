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

## Getting the election-night numerator (the hard part)

The precise first-report count lives in an archived capture of the registrar's
live results page (overwritten each update). **`WebFetch` is blocked for
web.archive.org — but `curl` and headless Chrome are NOT.** Those pages are
JS-rendered (curl gets an empty shell), so the reliable recipe is:

1. **Find snapshots — `curl` the Wayback CDX API** (not WebFetch):
   `curl "https://web.archive.org/cdx/search/cdx?url=<results-page>&from=<YYYYMMDD>&to=<+1day>&output=json&filter=statuscode:200&filter=mimetype:text/html&limit=8"`
   (CDX is sometimes slow on `*` prefixes — use the exact page URL and retry.)
2. **Pick the FIRST snapshot after poll close** — 8 p.m. PT ≈ `04:00` UTC the
   next day. The earliest capture is often *pre-close* and renders
   `Ballots Cast 0`; take the first one with a non-zero count.
3. **Render it** with the puppeteer helper:
   `WB_URL="https://web.archive.org/web/<ts>/<original>" NODE_PATH=$(pwd)/node_modules node scripts/research/render_wayback.cjs`
   → prints `Ballots Cast/Counted <N>` = the numerator (`confidence: "primary"`).

**Fallback** (page not archived / not renderable): the county's election-night
**press release** or local **news** quoting the first count — approximate,
`confidence: "secondary"`, note the report time. If nothing sources, `null` +
`confidence: "none"`. Never substitute a different denominator.

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
- Assuming Wayback is unreachable → only `WebFetch` is blocked; `curl` (CDX) + the
  `render_wayback.cjs` puppeteer helper reach it and give the *precise* numerator.
- Taking the earliest snapshot blindly → it's often pre-poll-close (`0` ballots);
  take the first non-zero one after 04:00 UTC.
- Comparing a presidential to a midterm election-night share as if equivalent →
  note the type mismatch.
