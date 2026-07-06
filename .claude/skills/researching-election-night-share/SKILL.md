---
name: researching-election-night-share
description: Use when finding a US county/jurisdiction's ELECTION-NIGHT ballot-count share (share of the certified final counted in the LAST report posted on election night, the plateau, NOT the first post-poll-close tranche) across elections that bracket its adoption of electronic pollbooks and/or automated signature verification — to test whether that tech moved the election-night number. Symptoms: a pre/post-adoption election-night comparison, "did e-pollbooks/ASV speed up the election-night count," filling an election-night row for a county.
---

# Researching a county's election-night share (pre/post tech adoption)

> **READ FIRST: `docs/research/RUNBOOK.md`.** It is the operator manual for
> this dataset: the exact row schema and editing rules, the validation
> pipeline you MUST run after any data change, the shared tooling in
> `scripts/research/` (do not rebuild it), what counts as plateau evidence,
> and the full gotcha catalog (Wayback gzip/replay-aliasing, the Clarity
> versions-array trap, the GEMS render-time trap). This skill is the
> research procedure; the runbook is the contract.

## Overview

Produce, for ONE county, its **election-night %** for the elections that bracket
its e-pollbook and ASV adoption years — so we can see whether the tech moved the
metric it should (election-night, not the one-week rate).

**Use the LAST report posted on election night** — the cumulative total at the
final election-night update, before the county stops and resumes the canvass days
later. **NOT the first 8 p.m. tranche** (that undercounts the night by ~2× and
is the classic mistake) and **NOT a days-later canvass update.**

`election-night % = ballots in the LAST election-night report ÷ certified final ballots`

A value you cannot source to that definition is `null` with a reason — never a
substituted denominator (e.g. "% of registered voters") and never a different
report time. (Calibration: San Francisco's authoritative final-election-night
share is ~59% in 2018 and ~57% in 2024 — if a county comes back near half that,
you grabbed the first tranche, not the last report.)

## Getting the election-night numerator — ranked routes

Try these in order; stop at the first that yields a clean plateau. **The county
registrar's own "semi-final" press release is usually the BEST source** — it
states the election-night total in one sentence, no rendering required.

### 1. County "semi-final / semi-official results" press release (PRIMARY, easiest)

The morning after the election, most registrars post a release titled
*"Semi-Final Results Announced for the <Election>"* (a.k.a. "Semi-Official
Results"). It states, verbatim, e.g. *"A total of 1,318,093 ballots were
processed and counted, with 23.42% of registered voters casting ballots"* —
**that number is the election-night plateau.** Look on:

- the registrar's **news-room / press-releases** page and its PDF host. These
  archives are gold — one page lists every election. (LA County example:
  `lavote.gov/news-room/press-releases`; PDFs at
  `content.lavote.gov/docs/rrcc/...`, `lavote.gov/docs/rrcc/news-releases/...`,
  and the older `lavote.gov/Documents/News_Releases/MMDDYYYY-HHMMSS.pdf`.)
- the **county's main news feed** (CivicPlus `/CivicAlerts.aspx`, `<county>.gov/news`),
  often **republished by local news** (e.g. YubaNet for Nevada County) quoting
  "the final election-night report."
- Take the FIRST/earliest such release (the morning-after "semi-final"), **not** a
  later "first post-election update" (that already adds canvass ballots). For
  prior elections the release may live only in **Wayback** — CDX the news-room or
  the PDF host for that week (route 3 has the curl recipe).

### 2. County's dated election-night report PDF / ENR feed (PRIMARY)

Many registrars post a sequence of timestamped reports whose filename or embedded
header encodes the report time — take the LAST one dated election night (100% of
precincts, right before the next-day canvass file):

- Fresno: `.../<year>/<election>/electionsummaryreportrpt_<M_D_YY>_<HHMM>.pdf`
  → "Voters Cast: N of R" (e.g. the ~12:30 a.m. report).
- Napa: "Last Unofficial Election Night Report" PDF in DocumentCenter.
- Clarity ENR: `results.enr.clarityelections.com/<ST>/<County>/<id>/<ver>/json/sum.json`
  → field `BC` = ballots cast; the election-night `ver` is the last before a >1-day gap.
  **Prove it is last with the version-bracket recipe in RUNBOOK.md 7.2**
  (`current_ver.txt` → the CURRENT version's `electionsettings.json` → full
  `versions` array; a version-pinned settings file only lists versions up to
  itself). The bracket both confirms plateaus and catches next-day bumps.
- livevoterturnout ENR: `.../ENR/<county>caenr/<N>/en/Index_<N>.html` → "Ballots
  Counted/Cast" + the embedded "Website Updated" timestamp.

A live county CMS often serves only the LATEST version (old filenames redirect to
the certified final), so the historical election-night version usually must come
from **Wayback**.

### 3. Archived live results page via Wayback (PRIMARY/secondary)

`WebFetch` is blocked for web.archive.org — **but `curl` (CDX) and headless
Chrome are NOT.** ENR pages are JS-rendered (curl gets an empty shell), so:

1. **Find snapshots — `curl` the CDX API** (not WebFetch):
   `curl "https://web.archive.org/cdx/search/cdx?url=<results-page>&from=<YYYYMMDD>&to=<+2days>&output=json&filter=statuscode:200&collapse=digest&limit=20"`
   Broad `matchType=domain`/regex CDX queries **time out and return empty** — use
   the exact URL, or a small capture-date window, and filter client-side. PDFs:
   fetch `https://web.archive.org/web/<ts>id_/<url>` with `curl -L` and `pdftotext`.
   Two traps (details: RUNBOOK.md 7.1): `id_` replays serve ORIGINAL bytes,
   often gzip (starts `1f 8b`), so gunzip before reading; and a CDX-listed
   capture can 302-alias to a DIFFERENT timestamp under every modifier, so
   check `curl -sI` Location before trusting fetched content's date.
2. **Pick the LAST election-night snapshot** — highest cumulative count right
   before a `>1`-day gap. NOT the 8 p.m. first tranche (undercounts ~2×), NOT a
   days-later capture.
3. **Render JS pages** with the puppeteer helper (spawns its own headless Chrome —
   parallel-safe):
   `WB_URL="https://web.archive.org/web/<ts>/<original>" NODE_PATH=$(pwd)/node_modules node scripts/research/render_wayback.cjs`

### When a source is BLOCKED — use the real browser

Some sites block `curl` AND `WebFetch` (403 / `ERR_HTTP2_PROTOCOL_ERROR` /
bot-walls / paywalls — e.g. McClatchy papers like the Fresno Bee), and the
headless render helper can also fail on them. **When you're denied, drive the real
browser:** the Claude-in-Chrome MCP tools (`tabs_create_mcp` → `navigate` →
`get_page_text`) read these pages. Create a NEW tab (don't hijack the user's),
and run it from the **main session, not parallel sub-agents** — the real browser
is a single shared Chrome and concurrent navigations collide. Parallel agents
should stick to curl/CDX/`pdftotext`/`render_wayback.cjs` and **flag** any
browser-only source for the operator to fetch.

**Fallback / null:** if nothing sources the plateau to the definition, use `null`
+ a reason — never a substituted denominator (e.g. "% of registered") and never a
different report time.

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
  recent ones AFTER. 2020 is a COVID all-mail outlier: excluded.
- `vs_epollbook` / `vs_asv` = `"pre"` / `"post"` relative to that tech's
  `adopted_year` (read it from `packages/data/county_tech.json`, or it's given to
  you). `"n/a"` if the tech was never adopted.
- `election_night_pct` is a PERCENT with at most 2dp (60.13), never a 0.x
  fraction. A post-night ceiling value additionally carries
  `"comparable": false` (see RUNBOOK.md 5.2); a null row carries
  `source_url_night: null` (examined-but-rejected sources go in the note as
  text, never in that field).
- If the row lands in `data/research/election-night/`, you are not done until
  the full pipeline in RUNBOOK.md section 3 passes (validator, machine
  checks, report regen, pytest, vitest) and the row has a plateau verdict in
  `plateau_review.json` (evidence standards: RUNBOOK.md section 8).

## How to find each field

- **Certified final (denominator) — reliable:** CA Secretary of State
  **"Statement of Vote → Voter Participation Statistics by County"** PDF for that
  election (`elections.cdn.sos.ca.gov/sov/<year>-general/sov/03-voter-participation-stats-by-county.pdf`).
  This is authoritative; always get it.
- **Election-night count (numerator) — best source first:** the registrar's
  **morning-after "semi-final / semi-official results" press release** (states the
  election-night total outright), then a dated election-night report PDF / ENR
  feed, then an archived live results page, then local news. State the report time
  you used (8 p.m. first tranche vs end-of-night plateau).

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
- Jumping straight to Wayback → check the registrar's **"semi-final results" press
  release archive FIRST; it usually states the election-night total in one
  sentence (no rendering), and one news-room page covers every election.
- Giving up when `curl`/`WebFetch` is blocked (403 / HTTP2 / paywall) → drive the
  real browser (Claude-in-Chrome `navigate` + `get_page_text`) from the main session.
- Taking the earliest snapshot blindly → it's often pre-poll-close (`0` ballots);
  take the first non-zero one after 04:00 UTC.
- Comparing a presidential to a midterm election-night share as if equivalent →
  note the type mismatch.
