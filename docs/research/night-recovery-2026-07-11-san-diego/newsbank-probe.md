# NewsBank San Diego Union / Union-Tribune image-edition probe (2026-07-12)

PROBE only (not a recovery run). Question: does NewsBank ("Access World News –
Historical and Current", product `p=WORLDNEWS`, via SFPL ezproxy) carry the
*San Diego Union* / *Union-Tribune* as an **image edition** for the historical
morning-after dates this campaign needs, the way it carries the *San Francisco
Chronicle* (image, 1865-2017 per the curated "California Historical
Newspapers" collection, plus current)?

**Short answer: no.** NewsBank's San Diego Union-Tribune image-edition source
starts in **2018**. Every target date (1914-2004) predates it. A separate
text-only source covers roughly 1970-present (with gaps) but never as a
scanned page image — it's wire-style article text, no returns-box layout to
read.

## How the SF Chronicle probe script had to be adapted

`scripts/archive-recovery/coverage_probe.js` runs an ezproxy date-filtered
`alltext=election` search and grabs the first `docref=image` hit. That works
for SF Chronicle dates because the Chronicle is effectively the only
image-edition paper this ezproxy session's default result set surfaces. For
San Diego it silently returns SF Chronicle hits instead (its `alltext`
default search isn't source-scoped) — a naive port would have reported false
positives.

## Source discovery method (reproducible)

1. Advanced-search field list (`/apps/news/results?p=WORLDNEWS&f=advanced`)
   confirmed the internal field code for a source-name filter: `fld-base-0=source`.
2. A-Z Source List (`/apps/news/source-list?p=WORLDNEWS`) has a live filter
   box (`#nbcore-react-browse-table-pane-source-list-page-filter`). Typing
   "san diego union" returns the **complete, authoritative list** of San Diego
   Union/Union-Tribune source records in this NewsBank product, each with its
   own **pubname ID**, date range, and Format column (Text vs Image):

   | pubname       | Source name (as listed)                                   | Dates       | Format  | Language |
   |---------------|-------------------------------------------------------------|-------------|---------|----------|
   | `SDUB`        | San Diego Union-Tribune, The (CA)                            | 1970-2026 (gaps: only 1970, 1971, 1975, 1976, 1977, then continuous 1983-2026) | **Text** | English |
   | `CSD5-EEDT`   | San Diego Union-Tribune, The (CA)                            | **2018-2026** | **Image** | English |
   | `SDUTS`       | San Diego Union-Tribune, The: Web Edition Articles (CA)      | 2009-Current | Text    | English |
   | `UTSDS`       | San Diego Union-Tribune, The: Video (CA)                     | 2017-2025   | Text    | English |
   | `ESSDUT`      | San Diego Union-Tribune en Español, The (CA)                 | 2020-2023   | Text    | Spanish |

   `CSD5-EEDT` is the **only** image-edition record for this paper in the
   whole product. There is no separate pre-1970 "San Diego Union" (pre-merger
   name) source at all — NewsBank never digitized/licensed that paper's
   historical run into this product, image or text.

## Working URL grammar (copy-pasteable)

**A. Source-scoped, date-filtered results search** (mirrors
`coverage_probe.js` / `sweep_section.js`'s `YMD_date` nav-facet pattern, with
a `source` base-field added):

```
https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results
  &fld-base-0=source&val-base-0=<urlencode('San Diego Union-Tribune')>
  &fld-nav-0=YMD_date&val-nav-0=<urlencode('MM/DD/YYYY - MM/DD/YYYY')>
  &sort=YMD_date%3AA
```
Parse: `document.querySelectorAll('a[href*="docref=image"]')` for an image
hit, `a[href*="docref=news"]` for a text hit. Adapted script saved at
`/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/sd_coverage_probe.js`.

**CAVEAT (found the hard way):** this date-filtered results search is
**unreliable for text-format (`docref=news`) issues** — it returned "No
results found" for 1984-11-07, 1996-11-06 and 2004-11-03 on the first pass
even though those issues demonstrably exist (confirmed via method B below).
It appears fine for image-format (`docref=image`) hits (matches
`coverage_probe.js`'s proven SF Chronicle behavior). **Don't trust a "no
results" from method A alone for a text source — cross-check with method B.**

**B. Publication calendar browse (ground truth, more reliable)** — resolve a
publication's internal ID via the A-Z Source List filter, then walk its
issue calendar directly:

```
# 1. Land on the publication's calendar (defaults to current year):
https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/browse-pub?p=WORLDNEWS
  &t=pubname%3A<PUBNAME>!<urlencode(Source+Name)>&action=browse

# 2. Select a year (page has a real <select id="edit-year-select">;
#    call page.select('#edit-year-select', '1984') then re-read the DOM —
#    clicking the year text directly does NOT work, it's a native <select>).

# 3. Each calendar day with an issue renders as a real <a> whose href is:
https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/issue-browse?p=WORLDNEWS
  &t=pubname%3A<PUBNAME>%21<urlencode(Source+Name)>/year%3A<YYYY>%21<YYYY>
  /mody%3A<MMDD>%21<Month>+<DD>&action=browse&year=<YYYY>&format=<text|image>
# Days with NO issue are plain text (no <a>), not a link.
```
`PUBNAME=SDUB` for the text archive, `PUBNAME=CSD5-EEDT` for the image
archive. The `&format=` suffix on the resulting link tells you which type
you landed on without needing to inspect `docref=`.

## Coverage table (all 11 target morning-after dates)

Method: check the `PUBNAME` year-selector option list first (an absent year
= zero coverage, no need to probe further); for present years, confirm the
specific day via method B's calendar link, cross-checked against method A.

| Election date (day-after issue) | SDUB text (1970-2026, gappy) | CSD5-EEDT image (2018-2026) | Verdict |
|---|---|---|---|
| 1914-11-04 | year not in range | year not in range | **NO coverage of any kind** |
| 1922-11-08 | year not in range | year not in range | **NO coverage of any kind** |
| 1924-11-05 | year not in range | year not in range | **NO coverage of any kind** |
| 1932-11-09 | year not in range | year not in range | **NO coverage of any kind** |
| 1944-11-08 | year not in range | year not in range | **NO coverage of any kind** |
| 1952-11-05 | year not in range | year not in range | **NO coverage of any kind** |
| 1960-11-09 | year not in range | year not in range | **NO coverage of any kind** |
| 1972-11-08 | year not in range (gap: archive skips 1972-1974, 1978-1982) | year not in range | **NO coverage of any kind** |
| 1984-11-07 | **issue exists** (calendar link confirmed) | year not in range | **Text only, no image edition** |
| 1996-11-06 | **issue exists** (calendar link confirmed; 101 alltext hits / 40 doc links, all `docref=news`) | year not in range | **Text only, no image edition** |
| 2004-11-03 | **issue exists** (calendar link confirmed; 114 alltext hits / 40 doc links, all `docref=news`) | year not in range | **Text only, no image edition** |

Title string throughout: `San Diego Union-Tribune, The (CA)` (both the text
and image source records use this post-1992-merger name; NewsBank never
labeled a pre-merger "San Diego Union" source separately in this product).

## Proof screenshots

Since **no image edition exists for any target date**, the requested
mid-century (1952) image-edition proof screenshot is not obtainable — there
is nothing to screenshot. Two screenshots were captured instead to document
the actual state of the archive:

- `mirror/newsbank/scans/probe_sd_image_coverage_2018_2026.png` — the
  `CSD5-EEDT` publication landing page, showing the format/date badge
  reading **"2018 - 2026 | Image"** for "San Diego Union-Tribune, The (CA)".
  This is the direct proof that image-edition coverage starts in 2018 (not
  earlier).
- `mirror/newsbank/scans/probe_sd_20181107_image_masthead.png` — an actual
  image-edition document view (`issue-browse` → `document-view`,
  `docref=image/...`) for **November 7, 2018** (day after the 2018 general),
  confirming the grammar and rendering pipeline work end-to-end: masthead
  reads "The San Diego Union-Tribune", dateline "Wednesday, November 7,
  2018", page A001. Chosen as the nearest-available proof-of-format date
  since no historical (pre-2018) hit exists to screenshot.

Both PNGs store the scan in the alpha channel (per the skill's known
gotcha) — flatten onto white before viewing/cropping.

## Session caveats

- Followed the skill's shared-session rule: background tab only
  (`newWindow:true`, window moved off-screen to `left:-32000`), never
  brought to front, closed after each script. No other browsing happened
  during the probe (idle session throughout), so no clobbered-search risk
  observed.
- Session stayed authenticated throughout (no "Articles and Databases" /
  re-login wall encountered); the pre-authorized re-login path was not
  needed.
- The result-count/`docref` scan in method A undercounts real coverage for
  text sources (see caveat above) — always cross-check a "no results" against
  method B's calendar before recording a date as uncovered.

## Recommendation

**None of 1914, 1922, or the mid-century elections (1924-1972) are
recoverable via NewsBank** — the San Diego Union has zero footprint (text or
image) in this NewsBank product before 1970, and even the 1970-2017 window
that does exist is text-only (no scannable returns box). This matches and
reinforces the existing README note that 1914/1922 (and now the whole
pre-1984 span) are "NewsBank/microfilm targets" — NewsBank specifically is
now a dead end for all of them; only physical microfilm (or another digitized
archive, if one exists) remains as a path.

**1984, 1996 and 2004** do have NewsBank coverage, but text-only — usable for
prose-based figures (a reported vote total mentioned in an article body) but
not for a returns-box table read the way the SF Chronicle/CDNC image
workflow depends on. If a night-count floor is needed for those three
elections, the text search that already turned up 40 `docref=news` hits per
date for 1996 and 2004 (109/114 including sub-results) is the place to start
reading prose for a citywide total, not a table sweep.


## CORRECTION (2026-07-12): SDUB's coverage starts 1983, not 1970

A fresh pull of SFPL's full 14,656-title NewsBank master catalog (see
`sd-union-access-hunt.md`) shows the only San Diego title SFPL carries is
"San Diego Union-Tribune, The (CA)" (pubname SDUB), TEXT only, **1983-Current**.
Earlier notes in this campaign said 1970; that was wrong. It does not change any
recovered row (the 1992 and 2004 news-derived floors both sit inside 1983+), but
it does mean the 1970s were never reachable via SDUB in the first place, so the
"empty across most of 1970-1986" phrasing overstated what was ever available.
No standalone pre-merger San Diego Union or Evening Tribune title exists in
SFPL's NewsBank catalog at all.
