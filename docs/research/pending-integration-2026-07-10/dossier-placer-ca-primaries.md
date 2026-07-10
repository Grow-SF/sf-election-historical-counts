# Placer County, CA — statewide-PRIMARY election-night dossier

Scope: 6 statewide primaries (2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05,
2022-06-07, 2024-03-05). Goal: election-night PLATEAU (last report posted on
election night, NOT the 8pm first tranche, NOT a days-later canvass number)
÷ certified final, per RUNBOOK.md section 1. READ-ONLY research pass; nothing
in this file has been committed to the repo. All draft rows/verdicts below are
DRAFTS for an operator to review and land.

## 2024 e-pollbook rollout-timing finding (headline)

**CONFIRMED: the 2024-03-05 Presidential Primary is Placer's FIRST
post-e-pollbook-adoption election night.** This is already independently
documented in the repo at `data/research/county-tech/placer-ca.json`
(confidence: primary), which is NOT something I had to newly establish, but
worth restating here as the load-bearing fact for this dossier:

- Placer's Board of Supervisors approved transition to the Voter's Choice Act
  (VCA) vote-center model on **June 13, 2023** (board item
  https://www.placer.ca.gov/DocumentCenter/View/70082/11A).
- Registrar page (https://www.placercountyelections.gov/voters-choice-act/):
  "Placer County has made the decision to transition to the Voter's Choice
  Act (VCA) election model, **starting with the 2024 Presidential Primary
  Election in March of 2024**."
- CA SoS "Voting Technologies in Use by County" (Sept 19, 2024 edition,
  https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2024-2.pdf)
  lists Placer's electronic pollbook vendor as **DFM (DFM Associates)**.
  The SoS "Voting Technology by County" list as of **May 9, 2022** shows
  Placer's e-pollbook column as **"Do not use"** — i.e. no e-pollbook before
  VCA.
- `first_election` recorded for the `epollbook` tech record = `"2024-03"`.

So: `vs_epollbook = "pre"` for all five 2012-2022 primaries below, and
`"post"` for 2024-03-05 — this is Placer's FIRST post-adoption primary AND
(per the existing generals file) its first post-adoption election of any
kind, since the Nov 2022 general was still pre-VCA and the Nov 2024 general
(also post) is the only other post-adoption point on record. This single
election is therefore load-bearing for the panel as described in the task.

No ASV adoption on record for Placer (`asv: null`, `status: "not-adopted"`),
so `vs_asv = "n/a"` for every row.

---

## Denominators (CA SoS Statement of Vote, Voter Participation Statistics by County)

All six PDFs fetched and Placer's line extracted directly (confidence: primary
for all).

| Date | Type | SoV URL | Placer "Total Voters" | Registered | Turnout (SoV-printed) |
|---|---|---|---|---|---|
| 2012-06-05 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf | 89,019 | 194,705 | 45.72% |
| 2014-06-03 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf | 70,016 | 200,829 | 34.86% |
| 2016-06-07 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf | 115,266 | 210,913 | 54.65% |
| 2018-06-05 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf | 109,097 | 223,963 | 48.71% |
| 2022-06-07 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf | 128,152 | 276,046 | 46.42% |
| 2024-03-05 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf | 135,869 | 281,556 | 48.26% |

Notes on URL patterns found (for the operator, since primary SoV URLs are not
yet documented anywhere in the repo and vary by year more than the general
URLs do):
- 2012 does NOT resolve at the `sov/2012-primary/03-voter-participation-stats-by-county.pdf`
  or `.../sov/03-...` paths used for generals (403 CloudFront on both) — the
  real path keeps the `/pdf/` segment AND the filename is
  `03-voter-reg-stats-by-county.pdf` (not "...-participation-..."), despite
  the in-page link text reading "Voter Participation Statistics by County".
  Found via the still-live `sov/2012-primary/index.htm` listing page.
- 2014 primary path: `sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf`
  (same misspelling as the 2014 general, confirmed 200).
- 2016 primary drops BOTH the `/sov/` and `/pdf/` subdirectory segments:
  `sov/2016-primary/03-voter-participation-stats-by-county.pdf` (200); the
  `.../sov/03-...` form used by 2016 general 403s for the primary.
- 2018/2022/2024 primaries all resolve at the standard modern form
  `sov/<year>-primary/sov/03-voter-participation-stats-by-county.pdf` (200,
  same shape as their respective generals).

---

## Item 1 of 6: 2012-06-05 Presidential Primary

**Certified final:** 89,019 Total Voters (Registered 194,705, 45.72% turnout).
SoV: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf

**Election-night plateau: FOUND, strong evidence.**

Route used: Wayback CDX of the same GEMS results page used for the 2012-2016
Nov generals in the existing `placer-ca.json` (`placerelections.com/election-night-results.aspx`).

- CDX for that exact URL, `20120601`-`20120715`:
  `curl "http://web.archive.org/cdx/search/cdx?url=placerelections.com/election-night-results.aspx&from=20120601&to=20120715&output=json&filter=statuscode:200&collapse=digest&limit=40"`
  → exactly 2 captures: `20120611040213` and `20120712042544`.
- **20120611040213** (fetched raw via `id_`, not gzipped) renders:
  "GEMS ELECTION RESULTS PLACER COUNTY **SEMI-OFFICIAL ELECTION SUMMARY**
  June 5, 2012 **Election Night Final** `06/05/12 23:54:34` Registered
  Voters 194705 - **Cards Cast 62087** 31.89% Num. Report Precinct 281 -
  Num. Reporting 281 100.00%". The page is explicitly self-labeled "Election
  Night Final" with an embedded timestamp of 11:54:34 p.m. election night
  itself (June 5), 281/281 precincts = 100% reporting. This is the plateau.
- **20120712042544** (a month later) renders: "GEMS ELECTION RESULTS PLACER
  COUNTY **OFFICIAL ELECTION SUMMARY** June 5, 2012 **FINAL** `06/22/12
  16:32:42` Registered Voters 194705 - **Cards Cast 89019** 45.72%" — the
  OFFICIAL FINAL canvass, Cards Cast 89,019, EXACTLY matches the certified SoV
  Total Voters (89,019). This is the bracket proof: the semi-official
  election-night number (62,087) held until superseded by the official
  post-canvass number (89,019) three weeks later — same pattern as the
  CONFIRMED 2014/2016 Nov-general rows in `placer-ca.json`.
- Arithmetic: 62,087 / 89,019 = **69.75%**.
- 69.75% is well above the ~half-of-expected first-tranche trap threshold and
  in the same range as Placer's later semi-official Nov-general plateaus
  (66.1% in 2014, 57.55% in 2016) — plausible for a presidential primary with
  a competitive GOP contest driving in-person turnout.

### Draft row (section 2 schema)
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": 62087,
  "certified_final": 89019,
  "election_night_pct": 69.75,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20120611040213/http://www.placerelections.com/election-night-results.aspx",
  "confidence": "primary",
  "note": "PLATEAU = 62,087 'Cards Cast', the registrar's GEMS 'SEMI-OFFICIAL ELECTION SUMMARY / June 5, 2012 / Election Night Final' with all 281 of 281 precincts reporting (31.89% reg turnout). The report carries its OWN embedded data timestamp '06/05/12 23:54:34' (11:54 p.m. PT election night itself) = the election-night-final semi-official canvass, the plateau. Rendered from Wayback snapshot 20120611040213 (capture June 11; embedded report data frozen at 06/05/12 23:54:34). BRACKET PROOF: the next surviving capture of the same URL, 20120712042544 (July 12), shows the page had been overwritten with 'OFFICIAL ELECTION SUMMARY / FINAL' data-stamped '06/22/12 16:32:42', Cards Cast 89,019 -- EXACTLY the certified SoV Total Voters -- proving the June 5 23:54 semi-official held as the plateau until the June 22 official canvass replaced it. Denominator = certified Total Voters 89,019 (Precinct 21,276 + VBM 67,743), CA SoS 2012 primary Statement of Vote, Voter Participation Statistics by County (elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf; note this filename/path differs from the 2012 general's, found via the still-live sov/2012-primary/index.htm listing). 62,087/89,019 = 69.75%."
}
```

### Draft VERIFY.md line
`| 2012-06-05 | presidential-primary | 62,087 | 89,019 | 69.75% | primary |`

### Draft plateau_review.json verdict
`CONFIRMED` — basis: self-describes as "Election Night Final" with a
same-night embedded timestamp (23:54:34) AND 100% precincts reporting, PLUS
the non-circular leg is the report-series-next-file-being-days-later bracket
(July 12 capture shows OFFICIAL FINAL replacing it, with Cards Cast now
exactly equal to the certified total). Evidence class: same tier as the
CONFIRMED 2014/2016 Nov-general rows already in the dataset.

---

## Item 2 of 6: 2014-06-03 Statewide Primary

**Certified final:** 70,016 Total Voters (Registered 200,829, 34.86% turnout).
SoV: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
(misspelling "particpiation" intact in the live URL, same as the 2014 general).

**Election-night plateau: NOT FOUND. NULL row, per RUNBOOK 5.1.**

Routes tried:
1. Wayback CDX of `placerelections.com/election-night-results.aspx`
   (`20140501`-`20140715` and widened to `20140501`-`20140901`): only ONE
   capture exists in the entire post-election window,
   `20140716121440` (July 16, six weeks out). Rendered (id_, not gzipped):
   "GEMS ELECTION RESULTS PLACER COUNTY 2014 STATEWIDE DIRECT PRIMARY JUNE
   3, 2014 **OFFICIAL ELECTION SUMMARY FINAL** `06/20/14 10:35:29`
   Registered Voters 200829 - Cards Cast 70016 34.86%" — already the OFFICIAL
   FINAL canvass (Cards Cast 70,016 = exactly certified). No semi-official
   election-night snapshot of this URL survives anywhere between poll close
   (8pm June 3) and this July 16 capture.
2. Wayback CDX `matchType=domain` on `placerelections.com`,
   `20140603`-`20140610`, to find any sibling page: turned up
   `electiontracker.placerelections.com/` (capture `20140607092616`, June 7,
   4 days after election). Rendered: it is a DIFFERENT, precinct-level
   drill-down tool, and its own text says "the Placer County Election
   Tracker system ... will not be updated until all precincts have
   reported. You can view election results at
   www.placerelections.com/election-night-results.aspx for updated results
   throughout the evening... The last report of vote totals on Election
   Night is a semi-official report only... issued... around midnight or as
   late as 2:00 am." This CONFIRMS the results.aspx page (route 1) was the
   real semi-official election-night page and describes its own plateau
   timing, but the tracker page itself carries no county-wide ballot count
   and results.aspx was never captured on election night.
3. Registrar's archived document directory for this election
   (`placerelections.com/uploads/documents/06032014/`, enumerated via CDX
   prefix match, ~60 files): contains only pre-election notices/calendars
   plus certified-final artifacts (`06032014_Fiinal_Results.pdf` [sic],
   `06032014_SOV.txt`, `06032014_SOV_Totals By Precinct.pdf`,
   `06032014_Certifications.pdf`) and a pollworker press release — NO
   election-night-dated report PDF and no "semi-final"/"semi-official
   results" press release.
4. Live registrar news-room (`placercountyelections.gov/past-elections-january-2011-to-november-2014/`,
   `placercountyelections.gov/election-results/`) is Cloudflare-bot-walled to
   curl (`Just a moment...` challenge page); tried the Wayback-archived copy
   of the "Past Elections Jan 2011-Nov 2014" listing instead (capture
   20220706154226), which links the SAME `/uploads/documents/06032014/`
   directory examined in route 3 (no additional files).
5. WebSearch for Auburn Journal / Sacramento Bee coverage quoting an
   election-night ballot count for June 3, 2014: no results surfaced any
   article stating a countywide election-night total; only generic
   registrar/Ballotpedia/SoS listing pages.

Per RUNBOOK 5.1, the wrong-stage OFFICIAL FINAL number (70,016, which is
just the certified total repeated, not a distinct night count) is NOT
recorded as the election-night figure; numerator left null rather than
substituting the certified total or a different report time.

**FLAG for manual operator**: `placercountyelections.gov/past-elections-january-2011-to-november-2014/`
and `placercountyelections.gov/election-results/` are Cloudflare-gated to
curl/WebFetch; a human or Claude-in-Chrome session could check whether the
LIVE (non-archived) copies expose an election-night PDF not present in the
2022 Wayback snapshot, though route 3/4 above suggest the directory
genuinely has no such file.

### Draft row (section 2 schema)
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 70016,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Election-night PLATEAU not sourceable. The registrar's GEMS election-night page (placerelections.com/election-night-results.aspx) has exactly ONE Wayback capture in the entire post-election window (20140501-20140901): 20140716121440 (July 16, six weeks after the June 3 poll close), which already shows 'OFFICIAL ELECTION SUMMARY FINAL' data-stamped 06/20/14 10:35:29, Cards Cast 70,016 -- the certified total, not a distinct night count. No semi-official election-night snapshot was ever archived. The sibling electiontracker.placerelections.com subdomain (captured 20140607092616, June 7) is a different precinct drill-down tool whose own text confirms results.aspx was the live election-night page and describes 'the last report of vote totals on Election Night is a semi-official report only... issued... around midnight or as late as 2:00 am' but carries no countywide ballot count itself. The registrar's archived per-election document directory (uploads/documents/06032014/, ~60 files enumerated via CDX prefix) holds only pre-election notices and certified-final artifacts (06032014_Fiinal_Results.pdf, 06032014_SOV.txt, 06032014_Certifications.pdf) -- no dated election-night report PDF, no semi-final/semi-official press release. Live registrar news-room pages (placercountyelections.gov/past-elections-january-2011-to-november-2014/, /election-results/) are Cloudflare-bot-walled to curl; the Wayback-archived copy of the former (20220706154226) links the same empty-of-election-night-artifacts document directory. WebSearch for Auburn Journal/Sacramento Bee coverage stating a countywide election-night total returned nothing usable. Denominator = certified Total Voters 70,016 (Precinct 13,633 + VBM 56,383), CA SoS 2014 primary Statement of Vote, Voter Participation Statistics by County. Per rules, numerator left null rather than substituting the certified/OFFICIAL total or a wrong report time. FLAG for manual operator: the two Cloudflare-gated live registrar pages could be re-tried via a real browser session, though the CDX-enumerated document directory suggests no election-night artifact exists there."
}
```

### Draft VERIFY.md line
`| 2014-06-03 | statewide-primary | NULL | 70,016 | NULL | none |`

### Draft plateau_review.json verdict
No verdict record needed (null row; RUNBOOK 5.5 requires verdicts only for
sourced rows).

---

## Item 3 of 6: 2016-06-07 Presidential Primary

**Certified final:** 115,266 Total Voters (Registered 210,913, 54.65% turnout).
SoV: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf

**Election-night plateau: FOUND, strong evidence (best-evidenced row in this dossier).**

- CDX for `placerelections.com/election-night-results.aspx`,
  `20160601`-`20160715`: 18 captures. The earliest 6 (all `20160602`,
  i.e. FIVE DAYS BEFORE the June 7 election) render "GEMS ELECTION RESULTS
  Election Summary Report 2016 Presidential Primary Summary ... **Zero
  Report** `06/01/16 13:09:42` ... Cards Cast 0 0.00% ... Num. Reporting 0
  0.00%" — a pre-election test/zero report, correctly excluded (this is the
  "earliest snapshot is 0 ballots" trap the skill warns about).
- The first POST-election capture, **20160608094120** (June 8, 9:41 a.m.,
  the morning after), renders: "GEMS ELECTION RESULTS PLACER COUNTY
  **SEMI-OFFICIAL ELECTION SUMMARY** June 7, 2016 **Election Night Final**
  `06/08/16 02:09:36` Registered Voters 210874 - **Cards Cast 71358**
  33.84% Num. Report Precinct 316 - Num. Reporting 316 100.00%" — embedded
  timestamp 2:09:36 a.m. June 8, i.e. ~6 hours after 8pm June 7 poll close,
  still within the "1am-4am next morning counts as election night" window
  per RUNBOOK section 1. 316/316 precincts = 100%. Self-labeled "Election
  Night Final."
- **Bracket proof (the "later capture still shows the same count" leg of
  RUNBOOK section 8):** re-fetched **20160613132607** (June 13, 5 days
  later) and **20160702124833** (July 2, nearly a month later) — BOTH render
  byte-identical GEMS text: same "Election Night Final 06/08/16 02:09:36"
  label, same Cards Cast 71,358. The election-night semi-official number
  held frozen for at least 3+ weeks in the archived record (no later
  transition to an "OFFICIAL" summary was captured in this window, but the
  frozen persistence itself is a stronger form of the same proof used for
  the CONFIRMED 2016 Nov-general row).
- Arithmetic: 71,358 / 115,266 = **61.91%**.
- Sanity: 61.91% is in a similar band to the existing 2016 Nov-general
  CONFIRMED plateau (57.55%) and higher than the 2012 primary plateau found
  above (69.75%) is somewhat higher but this was a highly-contested
  Clinton/Sanders + Trump/Cruz/Kasich primary driving turnout; no red flags.

### Draft row (section 2 schema)
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 71358,
  "certified_final": 115266,
  "election_night_pct": 61.91,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20160608094120/http://www.placerelections.com/election-night-results.aspx",
  "confidence": "primary",
  "note": "PLATEAU = 71,358 'Cards Cast', the registrar's GEMS 'SEMI-OFFICIAL ELECTION SUMMARY / June 7, 2016 / Election Night Final' with all 316 of 316 precincts reporting (33.84% reg turnout). The report carries its OWN embedded data timestamp '06/08/16 02:09:36' (2:09 a.m. PT, ~6 hrs after 8pm June 7 poll close, within the 1am-4am next-morning election-night window) = the election-night-final semi-official canvass, the plateau. Earliest Wayback captures of the same URL (six on 20160602, five days PRE-election) render a 'Zero Report' test page (Cards Cast 0) and are correctly excluded. Rendered from Wayback snapshot 20160608094120 (capture June 8, 9:41am; embedded report data frozen at 06/08/16 02:09:36). BRACKET PROOF: re-fetched captures 20160613132607 (June 13) and 20160702124833 (July 2) both render byte-identical GEMS text, same 'Election Night Final 06/08/16 02:09:36' label, same Cards Cast 71,358 -- the semi-official election-night number held frozen for at least 3+ weeks in the archived record (no OFFICIAL-summary transition captured in this window, but the multi-week frozen persistence is itself the non-circular leg per RUNBOOK 8: 'a later capture of the same URL still showing the same count'). Denominator = certified Total Voters 115,266 (Precinct 30,302 + VBM 84,964), CA SoS 2016 primary Statement of Vote, Voter Participation Statistics by County (elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf -- note this URL drops both the /sov/ and /pdf/ subdirectories present in other years). 71,358/115,266 = 61.91%."
}
```

### Draft VERIFY.md line
`| 2016-06-07 | presidential-primary | 71,358 | 115,266 | 61.91% | primary |`

### Draft plateau_review.json verdict
`CONFIRMED` — basis: self-describes as "Election Night Final" with a
same-morning embedded timestamp (02:09:36, within the 1am-4am rule) AND 100%
precincts reporting, PLUS the non-circular leg is TWO later captures (June
13, July 2) rendering the identical frozen count. Strongest evidence tier of
any row in this dossier: the frozen-for-weeks persistence is a cleaner proof
than a single bracket point.

---

## Item 4 of 6: 2018-06-05 Statewide Primary

**Certified final:** 109,097 Total Voters (Registered 223,963, 48.71% turnout).
SoV: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf

**Election-night plateau: NOT FOUND. NULL row. This is the Placer-2018
gotcha the task called out (RUNBOOK 7.3) — it applies EVEN HARDER to the
primary than to the Nov 2018 general.**

Routes tried:
1. Wayback CDX of `placerelections.com/election-night-results.aspx`,
   `20180501`-`20181001`: only TWO captures exist, both 301 redirects
   (`20180619004630` and `20180819093546`) to the NEW WordPress URL
   `https://www.placerelections.com/election-night-results/` — i.e. by
   mid-June 2018 the old GEMS `.aspx` URL structure documented in the
   existing 2012/2014/2016 rows had already been retired. NO capture of the
   `.aspx` page shows live June 5 data; it was already just a redirect stub
   by the time it was first crawled post-election.
2. Wayback CDX of the redirect TARGET,
   `https://www.placerelections.com/election-night-results/`,
   `20180501`-`20181231`: only 4 captures, ALL from **November 2018**
   (`20181113195233`, `20181121195122`, `20181121210754`, `20181128222547`)
   — these are the SAME captures already used (and flagged comparable=false)
   for the Nov 2018 general row in `placer-ca.json`. NOTHING from the June
   primary period exists at this URL at all — not even a contaminated
   later-canvass render, unlike the Nov 2018 case which at least had the
   Nov 9 capture. Zero coverage.
3. Wayback domain-wide CDX (`matchType=domain`) for `placerelections.com`,
   tight window `20180605`-`20180612`: no election-results page of any kind
   captured; only home/contact/register-to-vote/poll-worker pages.
4. Registrar's archived per-election document directory
   (`.../uploads/documents/06052018/`, CDX prefix-enumerated, both `www.`
   and bare host): only PRE-election poll-place-publication PDFs and one
   ballot-measure PDF — no results artifact of any kind, night or canvass.
5. Local news: **foresthillmessenger.com "How Placer County Voted in the
   Primaries"** (found via WebSearch) quotes "Of the 223,919 registered
   voters in Placer only 95,137 actually voted. That's a 42.49% turnout,"
   attributed to "the Placer County elections office." EXAMINED AND
   REJECTED: (a) the article's own `datePublished` meta tag is
   **2018-06-19T21:16:00-07:00** — two weeks after the election, with no
   internal report timestamp quoted, so it cannot be dated to election
   night specifically; (b) the arithmetic doesn't fit either stage cleanly:
   95,137 registered-voter-denominated is a DIFFERENT question than the
   certified-final-denominated share needed here, and re-based against the
   certified final (95,137/109,097 = 87.2%) is implausibly high for an
   election-night plateau (2012 and 2016 Placer primaries plateau at
   69.75%/61.91%) and implausibly low to be the certified total itself
   (109,097) — it reads as a stale or mid-canvass in-progress figure with an
   undetermined as-of date, exactly the trap RUNBOOK 7.3 warns about for
   this county's results page ("a days-later stamp is NOT evidence of a
   frozen count... check a LATER capture; if the number moved, the page
   tracks the canvass"). No independent corroborating source repeats the
   95,137 figure with a firmer date. WebSearch for "95,137" Placer surfaced
   no second source.
6. abc10.com "Placer County Primary Election Results: Where the vote stands
   so far" (found via WebSearch, title strongly suggests an in-progress
   quote): live URL 403s to curl; Wayback CDX for the exact article URL
   returns zero captures. Unrecoverable by this route.

Per RUNBOOK 5.1/5.2, with no report carrying a determinable election-night
(or even a clearly-dated post-night ceiling) timestamp, the row is NULL
rather than using the foresthillmessenger figure as an undated
ceiling/floor.

**FLAG for manual operator**: the abc10 "where the vote stands so far"
headline is the most promising un-recovered lead (title implies a live
in-progress quote, plausibly election night); a human or Claude-in-Chrome
session hitting the live abc10.com page (or a Google cache) directly could
still find a dated figure that curl's 403 and Wayback's empty CDX could not.

### Draft row (section 2 schema)
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 109097,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Election-night PLATEAU not sourceable -- worse coverage than the Nov 2018 general's comparable=false row. The GEMS election-night-results.aspx page had ALREADY been retired to a 301 redirect by the first post-election crawl (20180619, 20180819); its target https://www.placerelections.com/election-night-results/ has ZERO Wayback captures anywhere in the June 2018 primary window (only 4 captures exist at that URL total, all from Nov 2018, the same ones already used for the Nov 2018 general row). Domain-wide CDX for placerelections.com, 20180605-20180612, shows no election-results page captured at all. The registrar's archived per-election document directory (uploads/documents/06052018/) holds only pre-election poll-place-publication PDFs, no results artifact. Local news lead foresthillmessenger.com 'How Placer County Voted in the Primaries' quotes 'Of the 223,919 registered voters in Placer only 95,137 actually voted... 42.49% turnout' attributed to the county elections office, but the article's own datePublished is 2018-06-19 (two weeks post-election) with no internal report timestamp, and 95,137 re-based against the certified final (95,137/109,097=87.2%) is implausibly high for an election-night plateau versus this county's other primaries (69.75% in 2012, 61.91% in 2016) -- exactly the canvass-contamination pattern RUNBOOK 7.3 documents for this county's results page (its Nov 2018 general page is independently known to re-render with moving numbers, per the Nov 21 vs Nov 9 comparison already in this file). Examined and REJECTED as undatable/likely-contaminated; not recorded. abc10.com 'Placer County Primary Election Results: Where the vote stands so far' (title suggests a live in-progress quote) 403s to curl and has zero Wayback captures; unrecoverable by this route, FLAG for manual operator (a real browser or Google cache might reach it). Denominator = certified Total Voters 109,097 (Precinct 26,255 + VBM 82,842), CA SoS 2018 primary Statement of Vote, Voter Participation Statistics by County. Numerator left null rather than using the undated/implausible 95,137 figure."
}
```

### Draft VERIFY.md line
`| 2018-06-05 | statewide-primary | NULL | 109,097 | NULL | none |`

### Draft plateau_review.json verdict
No verdict record needed (null row).

---

## Item 5 of 6: 2022-06-07 Statewide Primary

**Certified final:** 128,152 Total Voters (Registered 276,046, 46.42% turnout).
SoV: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf

**Election-night plateau: NOT FOUND. NULL row.** Same structural gap as the
existing `2022-11-08` general row in `placer-ca.json` (registrar had already
moved to an in-place-updated live page that Wayback never captured during
canvass), but for the primary even the first-tranche press release could
not be independently located.

Routes tried:
1. Wayback CDX for `placercountyelections.gov/election-results` (prefix),
   `20220601`-`20220701`: zero captures. Domain-wide CDX for
   `placercountyelections.gov`, tight window `20220605`-`20220615`: many
   captures of the homepage/theme assets but no election-results or
   current-elections page carrying vote totals.
2. **Trap caught and avoided:** WebSearch surfaced
   `placer.ca.gov/1239/First-election-results` with a snippet reading "With
   more than 58,000 mail-in ballots counted of the approximately 90,000
   received so far" and no year attached, which looked at first glance like
   the June 2022 first-tranche release (matching the Nov 2022 general
   row's already-documented "~49,000 of ~100,000" pattern). **Fetched the
   actual archived content (Wayback capture 20220704032412, the closest
   available to June 7, 2022) and found the page text itself says "Published
   on **November 08, 2016**" and "Placer's voter registration rolls grew by
   22,000 people **from the June [2016] primary election** to more than
   227,000."** This is a STALE, permanently-live generic-slug press page
   (`/1239/First-election-results`) that was never overwritten for the June
   2022 primary and was still serving 2016 November-general content as of
   July 2022 (and again in later 2022/2023 captures, per CDX). Would have
   been a serious false-year/false-election error if used without checking
   the rendered content against its own internal date. Rejected outright;
   noted here as a hazard for future passes on this county.
3. abc10.com "Placer County election results: 2022 primary updates" /
   "Placer County Election results: Where the races stand so far"
   (`103-2fc723a8-84a5-4c26-9c8e-9e52cae1acf7`): TWO Wayback captures exist,
   `20220616005201` and `20220622064248` (both gzip-encoded, gunzipped).
   Both render IDENTICAL text: "Published: 4:01 PM PDT June 7, 2022 Updated:
   4:01 PM PDT June 7, 2022" (i.e. never updated post-publication) — a
   pre-poll-close PREVIEW describing the schedule only: "The semi-official
   results start getting posted around 8:10 p.m., just after polls
   close... The remaining vote updates start around 9:30 p.m. New reports
   will be issued and posted around 30 minute intervals until results are
   in from all precincts... an unofficial report will be issued for the
   count" -- confirms Placer's process but contains NO actual ballot count
   for this election (the live numbers presumably lived in an unarchived JS
   widget, same failure mode as the abc10 2024-general article already
   examined-and-rejected in the existing dataset).
4. Registrar's archived per-election document directory
   (`placercountyelections.gov/Uploads/documents/06072022/`, CDX
   prefix-enumerated, ~60 files incl. `can_watch/` subfolder): only
   pre-election notices/checklists/candidate filings and certified-final
   artifacts (`06072022_Final.pdf`, `06072022_Comma_Delimited_SOV.txt`,
   `06072022_TotalsbyPrecinct.pdf`, `06072022_Certs.pdf`) -- no
   election-night-dated report and no semi-final/semi-official press
   release, same as every other primary examined in this dossier.
5. Facebook post "June primary results have been updated on the Placer
   County Elections website" (found via WebSearch): a social post pointing
   back to the live results page, not independently fetchable/parseable by
   curl; not pursued further given routes 1-4 already show the underlying
   page was never archived.

Per RUNBOOK 5.1, with no first-tranche OR plateau number crediblysourced to
this specific election, the row is null (there is not even an examinable
first-tranche number to note as "the wrong-stage number we rejected," unlike
the Nov 2022/2024 general rows).

**FLAG for manual operator**: none of the leads found a human-checkable
dated number; a Claude-in-Chrome session on the live
`placercountyelections.gov/election-results/` page or the Facebook post
history could be tried, but given routes 1 and 4 show the registrar's own
archive has no artifact, expectations should be low.

### Draft row (section 2 schema)
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 128152,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Election-night PLATEAU not sourceable, same structural gap as the existing 2022-11-08 general row: the registrar's results page (placercountyelections.gov/election-results/) has ZERO Wayback captures anywhere near the June 7, 2022 primary (CDX prefix + domain-wide checks, 20220601-20220701 and a tight 20220605-20220615 window). TRAP CAUGHT: a WebSearch hit for placer.ca.gov/1239/First-election-results looked like the June 2022 first-tranche release ('58,000 mail-in ballots... 90,000 received') but the actual archived page content (fetched, not just the search snippet) reads 'Published on November 08, 2016' and references 'the June [2016] primary election' -- this is a permanently-live, never-overwritten generic-slug page still serving stale Nov 2016 content as of its 2020-2023 Wayback captures; REJECTED, not used, flagged here as a hazard. abc10.com's election-day article (103-2fc723a8-84a5-4c26-9c8e-9e52cae1acf7, two Wayback captures 20220616/20220622, both identical) is a pre-poll-close preview only ('Published/Updated: 4:01 PM PDT June 7, 2022'), describing the reporting schedule (8:10pm first tranche, 9:30pm+ updates every 30 min, final unofficial report) but carrying no actual ballot count -- the live numbers lived in an unarchived JS widget. The registrar's archived per-election document directory (Uploads/documents/06072022/, ~60 files enumerated via CDX prefix) holds only pre-election filings and certified-final artifacts (06072022_Final.pdf, 06072022_Comma_Delimited_SOV.txt, 06072022_TotalsbyPrecinct.pdf) -- no election-night report, no semi-final press release. Denominator = certified Total Voters 128,152 (Precinct 13,181 + VBM 114,971), CA SoS 2022 primary Statement of Vote, Voter Participation Statistics by County. Numerator left null; unlike the Nov 2022/2024 general rows, no first-tranche number was even recoverable to record as a rejected candidate."
}
```

### Draft VERIFY.md line
`| 2022-06-07 | statewide-primary | NULL | 128,152 | NULL | none |`

### Draft plateau_review.json verdict
No verdict record needed (null row).

---

## Item 6 of 6: 2024-03-05 Presidential Primary — THE LOAD-BEARING POST-ADOPTION ROW

**Certified final:** 135,869 Total Voters (Registered 281,556, 48.26% turnout
per SoV; the registrar's own certified-results page independently prints
"Registered Voters 281,148 - Cards Cast 135,869 48.33%" — same Cards Cast,
small registered-voter-count discrepancy between the SoV's snapshot and the
county's own count, immaterial to the numerator).
SoV: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf

This is Placer's FIRST post-e-pollbook / post-VCA / post-Sign-Scan-Go
election of any kind (see the headline finding at the top of this dossier).
It is the single most important row in this dossier for the panel's purpose.

**Election-night plateau: NOT FOUND. NULL row**, despite an unusually
thorough search — this county's results page is simply not crawlable at the
right moments, worse even than the already-documented Nov 2024 general gap.

Routes tried:
1. Wayback CDX for `placercountyelections.gov/election-results/`,
   `20240301`-`20240601`: only 5 captures total, and NONE fall in the
   election-night-through-canvass window in a useful way:
   - `20240306024948` (March 6, 02:49:48 UTC = **6:49 p.m. PST March 5**,
     ~70 minutes BEFORE the 8pm poll close) renders "PRESIDENTIAL PRIMARY
     ELECTION MARCH 5, 2024 **ZERO REPORT** `02/29/24 8:53:44 AM`
     Registered Voters 0 - Cards Cast 0 0.00%" — a stale pre-election test
     report, correctly excluded (earliest-snapshot-is-zero trap).
   - The very next capture is **`20240405220948`, a full MONTH later**
     (April 5), which renders "PRESIDENTIAL PRIMARY ELECTION MARCH 5, 2024
     **FINAL RESULTS** `04/02/24 5:33:50 PM` Registered Voters 281,148 -
     **Cards Cast 135,869** 48.33% ... 170/170 100.00%" — already the
     certified FINAL (Cards Cast 135,869 = exactly the certified total),
     posted 3 days after certification (04/02/24 press release, see route
     4). There is a complete GAP of exactly one month between the
     pre-poll-close zero report and the post-certification final; NOTHING
     in between was ever crawled. Unlike the Nov 2024 general (which at
     least had a Nov 8 "Report 7" canvass-update capture as a bound), the
     March 2024 primary has ZERO intermediate captures of any kind.
2. Wayback CDX for `placer.ca.gov/149/News-Releases` (the county's general
   news feed), tight window `20240304`-`20240320`: only ONE capture,
   `20240304232954` — the DAY BEFORE the election, too early to list a
   results release.
3. Wayback CDX for `placer.ca.gov/10016/2024-election-results` (the exact
   page already examined-and-rejected as the Nov 2024 general's 8pm-tranche
   source in the existing `placer-ca.json` row): earliest capture is
   `20241223134200` (Dec 2024) — this page did not exist yet in March 2024;
   it is specific to the Nov 2024 general, not a year-round hub.
4. Registrar's archived per-election document directory
   (`placercountyelections.gov/Uploads/documents/03052024/`, CDX
   prefix-enumerated, ~65 files): contains only pre-election operational
   PDFs (VIG/VBM notices, vote-center-location and manual-tally press
   releases, candidate-filing packets) and certified-final/post-canvass
   artifacts (`03052024_Final_Result.pdf`,
   `03052024_PRESS_RELEASE_Election_Certification_040224_2.pdf` [dated
   04/02/24], `03052024_ResultsCommaDelimited_SOV.txt`,
   `03052024_StatementOfVotesCastRPTByPrecinct_Redacted.pdf`) — NO
   election-night-dated report and no semi-final/first-tranche press
   release, the same total-absence pattern as every other primary in this
   dossier.
5. Local news with embedded live-results widgets — fox40.com "Placer County
   Primary Election Results 2024" (3 Wayback captures, all
   `20240306003634`-`20240306005855`, i.e. all ~4:36-4:58 p.m. **PST** March
   5, BEFORE poll close) and abc10.com "Placer County Election Results: 2024
   Election Updates": fox40 captures render only page chrome (a JS
   results-widget page, structurally identical to the already-documented
   Nov 2024 abc10 failure mode — no numbers in the static HTML); abc10's
   CDX query 504-timed-out (broad/slow endpoint) and was not successfully
   retried within budget.
6. WebSearch for a March 2024 "first results"/"semi-final" press release
   with a VBM count (the Nov 2024 equivalent was the 104,382-ballot 8pm
   tranche release): surfaced only the April 2 CERTIFICATION press release
   (`placer.ca.gov/9678/Primary-election-results-certified`) and general
   hub/index pages (`/9534/_2024`, `/10016/2024-election-results` — the
   latter confirmed in route 3 to postdate this election). One useful
   context finding: a Feb 16, 2024 press release (pre-election, cited in a
   WebSearch summary, not independently verified against the archived PDF)
   describes Sign-Scan-and-Go: "voters could visit any vote center...to
   have their voted vote-by-mail ballot scanned and counted immediately,
   ensuring their votes were included in the first election results
   released" — corroborates the `county-tech` record's Sign-Scan-Go
   mechanism but gives no count. No first-tranche numeric press release for
   THIS election was located.

Per RUNBOOK 5.1, with neither a plateau NOR even a recoverable first-tranche
figure for this specific election, the row is null. Given how much rides on
this row, this null is the single most consequential gap in the dossier and
should be the operator's top priority to re-attempt with tools this pass
could not use (see FLAG below).

**FLAG for manual operator (high priority):** this is the panel-defining
row. Two concrete un-exhausted leads:
- abc10.com's "Placer County Election Results: 2024 Election Updates"
  (`103-c7babbde-2d77-4bf0-ae62-2add6baaf4df`) CDX query 504-timed-out here;
  retry the CDX query (possibly needs a narrower date window or a retry
  after the transient network issue this session hit) or fetch the live
  page/its Wayback captures directly with `render_wayback.cjs` in case the
  live-results widget's numbers were baked into a captured JS state.
- The registrar's live site or a direct records request could reveal
  whether Placer issued a dated "semi-final"/first-tranche PDF for the
  March 2024 primary at all (the document-directory enumeration says no,
  but a live Google-cache or direct-contact check would close the loop
  definitively, especially given how much this row matters).
- Sign-Scan-and-Go's real-time in-person counting (per the county-tech
  record) plausibly makes this county's TRUE election-night share unusually
  HIGH for a post-2018 VCA county (in-person scans join the tally live,
  unlike other VCA counties where in-person ballots wait for the canvass) —
  worth flagging to the operator as a reason this number, if ever recovered,
  may look different from the pre-adoption primaries' 62-70% range.

### Draft row (section 2 schema)
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 135869,
  "election_night_pct": null,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "PANEL-DEFINING ROW: Placer's FIRST post-e-pollbook/post-VCA/post-Sign-Scan-Go election (Board approved VCA transition 2023-06-13; first_election recorded as 2024-03 in data/research/county-tech/placer-ca.json for epollbook, vote-center, and sign-scan-go tech records). Election-night PLATEAU not sourceable despite an unusually thorough search -- worse coverage than the already-null Nov 2024 general. The registrar's results page (placercountyelections.gov/election-results/) has only 5 Wayback captures total in 20240301-20240601: the sole pre-April capture (20240306024948, = 6:49pm PST March 5, ~70 min BEFORE 8pm poll close) shows a stale pre-election 'ZERO REPORT' (Cards Cast 0); the NEXT capture is a full month later (20240405220948, April 5) and already shows 'FINAL RESULTS 04/02/24 5:33:50 PM... Cards Cast 135,869' (= exactly certified, posted 3 days after the April 2 certification press release). Zero intermediate captures exist -- a complete one-month gap. The registrar's archived per-election document directory (Uploads/documents/03052024/, ~65 files enumerated via CDX prefix) holds only pre-election operational PDFs and certified-final/post-canvass artifacts (03052024_Final_Result.pdf, 03052024_PRESS_RELEASE_Election_Certification_040224_2.pdf dated 04/02/24) -- no election-night report, no first-tranche/semi-final press release. placer.ca.gov's news-releases feed (149/News-Releases) has only a pre-election (20240304) capture; the page later used as the Nov 2024 general's rejected first-tranche source (10016/2024-election-results) did not exist yet in March 2024 (earliest capture Dec 2024). Local news with embedded live-results widgets (fox40.com 'Placer County Primary Election Results 2024', 3 captures all ~4:36-4:58pm PST March 5, BEFORE poll close) render only page chrome, no numbers; abc10.com's equivalent 2024-updates article CDX query 504-timed-out and was not successfully retried within this pass's budget -- FLAG for manual operator retry. No first-tranche numeric press release for THIS election (unlike Nov 2024's recoverable 104,382-ballot 8pm VBM release) was located by any route. Denominator = certified Total Voters 135,869 (Precinct 15,295 + VBM 120,574), CA SoS 2024 primary Statement of Vote, Voter Participation Statistics by County; independently cross-checked against the registrar's own certified-results page ('Cards Cast 135,869 48.33%', Registered Voters 281,148 vs SoV's 281,556 -- immaterial small discrepancy). Numerator left null. Sign-Scan-and-Go (per county-tech record) counts in-person-scanned VBM ballots into the live tally, so if ever recovered this county's true election-night share may run notably higher than its pre-adoption primaries (62-70% range found above) -- flagged for the operator's interpretation, not assumed."
}
```

### Draft VERIFY.md line
`| 2024-03-05 | presidential-primary | NULL | 135,869 | NULL | none | ⚠️ post-adoption, top-priority re-check |`

### Draft plateau_review.json verdict
No verdict record needed (null row), but recommend the operator track this
row specifically given its panel importance.

---

## Summary table (draft, for VERIFY.md)

| Date | Type | Election-night ballots | Certified final | Election-night % | Confidence | vs_epollbook |
|---|---|---|---|---|---|---|
| 2012-06-05 | presidential-primary | 62,087 | 89,019 | 69.75% | primary | pre |
| 2014-06-03 | statewide-primary | NULL | 70,016 | NULL | none | pre |
| 2016-06-07 | presidential-primary | 71,358 | 115,266 | 61.91% | primary | pre |
| 2018-06-05 | statewide-primary | NULL | 109,097 | NULL | none | pre |
| 2022-06-07 | statewide-primary | NULL | 128,152 | NULL | none | pre |
| 2024-03-05 | presidential-primary | NULL | 135,869 | NULL | none | **post** |

2 of 6 primaries sourced (both CONFIRMED, both pre-adoption); 4 of 6 null,
including the single most important row (2024-03-05, the first
post-adoption election of any kind for this county). The panel gains
Placer's certified-final denominators and a pre-adoption primary baseline
(61.91%-69.75%) from this pass, but the specific "did the tech move
election-night %" comparison this county was recruited for remains
unanswered pending recovery of the 2024-03-05 numerator -- see the FLAG
above for the two concrete un-exhausted leads.

## Unfinished / handed back to the operator

1. **2024-03-05 numerator (top priority)**: retry the abc10.com CDX query
   that 504-timed-out; consider a direct records request to the registrar
   for any semi-final report they may hold outside the web.
2. **2018-06-05 numerator**: the abc10 "where the vote stands so far"
   article 403s to curl and has zero Wayback captures; try a real browser
   session or Google cache.
3. **2014-06-03 and 2022-06-07 numerators**: both Cloudflare-gated live
   registrar "past elections" pages could be re-tried via Claude-in-Chrome;
   low expectation of success given the CDX-enumerated document directories
   already show no election-night artifact exists.
4. All 6 draft rows, the VERIFY.md table/bullets, and plateau_review.json
   verdicts above are DRAFTS only -- nothing has been written to the repo.
   An operator (or a follow-up write-enabled pass) should land the 2
   CONFIRMED rows (2012, 2016) plus the 4 null rows with full notes, then
   run the full pipeline (RUNBOOK section 3) before committing.

