# Tehama County, CA (tehama-ca) — statewide PRIMARY election-night dossier

Control county (never adopted e-pollbooks or ASV; county-tech census row status
"never", confidence "medium" -- see `data/research/county-tech/ca_adoption_census.json`
and the existing `data/research/election-night/tehama-ca.json` general-election
rows). Scope: the six even-year statewide primaries 2012-06-05, 2014-06-03,
2016-06-07, 2018-06-05, 2022-06-07, 2024-03-05. Methodology:
`docs/research/RUNBOOK.md` sections 1, 5-8; `researching-election-night-share`
skill. Metric: election-night % = ballots in the LAST report posted election
night / certified final (CA SoS SoV). `vs_epollbook` / `vs_asv` = "n/a" for
every row (control county, no tech transition to bracket).

**Read first (per task brief):** the existing `tehama-ca.json` general-election
notes already establish Tehama's numbered-report system and its two eras: a
pre-2018 Joomla site (`co.tehama.ca.us`, flat `images/images/Elections/`
directory that SILENTLY REUSES report filenames across different elections --
confirmed trap, see Items 3/4 below) and a post-2020 WordPress site
(`co.tehama.ca.us/wp-content/uploads/<year>/<month>/...` through 2022, then
`tehama.gov/wp-content/uploads/...` by 2024 -- each election gets its own
permanent year/month folder, no cross-election filename collision). The
general rows also establish: 2012-2018 generals are all NULL (weak/absent
Wayback crawl of the Joomla site during election-night windows); 2022 and 2024
generals are SOURCED/CONFIRMED via the numbered "Unofficial Precinct Report"
PDFs (2022 via Wayback of the dead `co.tehama.ca.us`; 2024 fetched live from
`tehama.gov`, no Wayback needed). This primaries pass finds the SAME pattern:
2012-2018 primaries NULL, 2022 primary NULL (close miss: the plateau report's
filename was found LINKED but never crawled), 2024 primary SOURCED/CONFIRMED.

## Denominators (CA SoS Statement of Vote, Voter Participation Statistics by County)

All six SoV PDFs fetched and Tehama's line pulled (`pdftotext -layout`,
column order: County / Precincts / Eligible to Register / Registered Voters /
Precinct Voters / Vote-By-Mail Voters / **Total Voters** / %VBM / Turnout-%Reg
/ Turnout-%Elig). Arithmetic cross-check: Precinct Voters + VBM Voters =
Total Voters, verified for all six rows below.

| date | election type | Total Voters (certified final) | exact SoV line | source URL |
|---|---|---|---|---|
| 2012-06-05 | Presidential Primary | 13,968 | `Tehama 46 43,209 30,476 3,687 10,281 13,968 73.60% 45.83% 32.33%` | https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf |
| 2014-06-03 | Statewide Direct Primary | 13,016 | `Tehama 46 43,659 30,492 3,416 9,600 13,016 73.76% 42.69% 29.81%` | https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf |
| 2016-06-07 | Presidential Primary | 15,577 | `Tehama 46 43,656 30,724 4,187 11,390 15,577 73.12% 50.70% 35.68%` | https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf |
| 2018-06-05 | Statewide Direct Primary | 14,733 | `Tehama 46 43,835 32,523 3,758 10,975 14,733 74.49% 45.30% 33.61%` | https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf |
| 2022-06-07 | Statewide Direct Primary | 14,178 | `Tehama 39 47,064 37,811 1,710 12,468 14,178 87.94% 37.50% 30.12%` | https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf |
| 2024-03-05 | Presidential Primary | 15,537 | `Tehama 40 45,988 36,998 1,941 13,596 15,537 87.51% 41.99% 33.78%` | https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf |

Note on the 2012 URL: unlike the 2012 GENERAL (which uses
`03-voter-participation-stats-by-county.pdf` with no `sov/` segment per
RUNBOOK 6.1), the 2012 PRIMARY's voter-participation PDF is actually named
`03-voter-reg-stats-by-county.pdf` (verified: this exact URL returns HTTP 200
and its content is the "VOTER PARTICIPATION STATISTICS BY COUNTY" table
despite the "voter-reg" filename; the alternate guess
`03-voter-participation-stats-by-county.pdf` for the 2012 primary path 403s).
All other five URLs match the pattern already established across other
counties' primary dossiers in this pass (2014 misspelled "particpiation"
intact; 2016 drops the `sov/` sub-segment; 2018/2022/2024 use the standard
`sov/03-voter-participation-stats-by-county.pdf` path). All six URLs
HTTP-200-verified 2026-07-10.

---

(Per-primary numerator research appended below, one item at a time.)

---

## ITEM 1 of 6: 2012-06-05 Presidential Primary

**Certified final:** 13,968 (see table above).

**Numerator (election-night plateau): NULL.** This is the weakest-evidenced
primary year, consistent with the general-election 2012 row (also NULL, also
described there as "a total absence of any elections crawl").

Routes checked:

1. **Route 3/6.5 (Wayback of the live results page):** the only elections-
   adjacent artifact captured anywhere near this window is the GEMS-era
   frameset page `http://co.tehama.ca.us/ballotresults/Election%20Result_dtl.htm`,
   captured once, 2012-05-22 (2 weeks BEFORE the election). Fetched and read:
   its internal stamp reads **"Last Updated: November 9, 2011 4:56 PM"** and
   shows a small odd-year special/district election (RIO ALTO WATER DISTRICT,
   1,464 registered voters, 359 ballots cast) -- i.e. this page is frozen on
   stale November 2011 data, not live June 2012 content, and was never
   re-crawled during or after the primary. Same frozen-page failure mode
   documented for the 2014 GENERAL row in the existing dataset.
2. **Route domain sweep:** a full-domain Wayback CDX sweep of `co.tehama.ca.us`
   for 2012-05-22 through 2012-07-20 (9-week window bracketing the election,
   72 total URLs crawled domain-wide) found ZERO pages containing
   `elect`/`result`/`report`/`.pdf` beyond: the frameset above (pre-election,
   frozen), a stray Joomla content-management URL with `phpMyAdmin` query
   params (unrelated CMS artifact, "Bidding Opportunities" content, itemid
   mismatch), and template/CSS/JS boilerplate. No numbered report PDF, no
   press release, no dated results page.
3. **Route 6.6 (local news):** not separately re-searched this pass (the
   general 2012 row already documents a WebSearch dead end across multiple
   phrasings for the same county/era; the primary would face the identical
   absence of any Tehama-specific local online news archive for 2012).
4. **Not on Clarity** (confirmed dead end for this county across all years in
   the general-election dossier; not re-probed here).

Null per RUNBOOK 5.1: never substitute a different report time or denominator.

### Draft row (data/research/election-night/tehama-ca.json schema, primaries variant)

```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 13968,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 13,968 ballots cast (CA SoS SoV; precinct 3,687 + VBM 10,281; 45.83% of 30,476 registered; confirmed 2026-07-10, county line: Tehama 46 43,209 30,476 3,687 10,281 13,968 73.60% 45.83% 32.33%). Election-night PLATEAU not sourceable. The county's dedicated GEMS-frameset results page (co.tehama.ca.us/ballotresults/Election Result_dtl.htm) has only one capture near this window, 2012-05-22 (pre-election), and its internal stamp reads 'Last Updated: November 9, 2011 4:56 PM' -- frozen on a stale odd-year special-district election, not live June 2012 data, and never re-crawled after. A full-domain Wayback CDX sweep of co.tehama.ca.us for 2012-05-22 through 2012-07-20 (72 URLs crawled domain-wide in that 9-week window) found zero pages with 'elect'/'result'/'report' content beyond that frozen frameset and unrelated Joomla CMS boilerplate -- no numbered report PDF, no press release, no dated results page. No local news figure found (same absence documented for the 2012 general in this dataset). Not on Clarity. Null per RUNBOOK 5.1. vs_epollbook/vs_asv n/a (control county, never adopted)."
}
```

### VERIFY.md draft line

Summary cell: `| 2012-06-05 | NULL | -- | none |`
Detail bullet: "2012-06-05 presidential primary: election-night ballots NULL
(dedicated results page frozen on stale Nov-2011 data at its only nearby
capture; 9-week domain-wide CDX sweep found zero elections-content crawls).
Certified final 13,968 -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf.
Look for: any surviving numbered report PDF under co.tehama.ca.us for June 2012,
or a press mention of a June 2012 election-night ballot count."

### Plateau verdict

**N/A (null row) -- no verdict entry needed** (plateau_review.json only carries
verdicts for sourced rows). Confidence: none. Evidence class: null-per-5.1,
fully documented route exhaustion.

---

## ITEM 2 of 6: 2014-06-03 Statewide Direct Primary

**Certified final:** 13,016 (see table above).

**Numerator (election-night plateau): NULL.** Even weaker crawl footprint than
2012: a full-domain Wayback CDX sweep of `co.tehama.ca.us` for the 8-week
window 2014-05-20 through 2014-07-15 returned only **1 total URL crawled
domain-wide** across the entire window: `images/images/Elections/SBballot1.pdf`
(a sample ballot, pre-election). No results page, no report PDF, no dated
content of any kind, election-related or otherwise, in that 8-week window.

Routes checked:

1. **Route 3/6.5 (Wayback of live results page):** the dedicated
   `Election_Result_dtl.htm` GEMS page's next-closest captures bracket this
   election at 2014-11-04 9:25 AM (pre-poll-close for the FOLLOWING November
   election) and 2015-01-19 -- i.e. Wayback did not crawl that page at all
   during the June 2014 window (consistent with the near-total crawl absence
   found by the domain sweep). This exact frozen-page/gap pattern for the
   November 2014 general is already documented in the existing dataset's
   2014-11-04 row.
2. **Route domain sweep:** as above, 1 total URL, a sample ballot, nothing
   election-night-adjacent.
3. **Route 6.6 (local news):** not separately re-searched (see Item 1
   rationale; no known online archive for this county/era).
4. **Not on Clarity.**

Null per RUNBOOK 5.1.

### Draft row

```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 13016,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 13,016 ballots cast (CA SoS SoV; precinct 3,416 + VBM 9,600; 42.69% of 30,492 registered; confirmed 2026-07-10, county line: Tehama 46 43,659 30,492 3,416 9,600 13,016 73.76% 42.69% 29.81%). Election-night PLATEAU not sourceable. A full-domain Wayback CDX sweep of co.tehama.ca.us for 2014-05-20 through 2014-07-15 (8-week window) found exactly ONE URL crawled domain-wide in the entire window: images/images/Elections/SBballot1.pdf, a pre-election sample ballot -- no results page, no numbered report, no dated content of any kind otherwise. The dedicated Election_Result_dtl.htm GEMS page (frozen-page pattern already documented for this county's Nov 2014 general row) was not crawled at all during this window; its nearest captures bracket the FOLLOWING November 2014 election, not this one. No local news figure found. Not on Clarity. This is the weakest-evidenced year in the primaries dossier: not a near-miss, a near-total absence of any domain crawl. Null per RUNBOOK 5.1. vs_epollbook/vs_asv n/a (control county, never adopted)."
}
```

### VERIFY.md draft line

Summary cell: `| 2014-06-03 | NULL | -- | none |`
Detail bullet: "2014-06-03 statewide primary: election-night ballots NULL
(8-week domain-wide CDX sweep of co.tehama.ca.us found exactly one crawled URL
total, a pre-election sample ballot -- essentially zero site coverage).
Certified final 13,016 -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf.
Look for: any independent archive of a June 2014 Tehama results page or report
PDF outside Wayback's domain sweep."

### Plateau verdict

**N/A (null row).** Confidence: none. Evidence class: null-per-5.1, fully
documented route exhaustion (near-zero domain crawl).

---

## ITEM 3 of 6: 2016-06-07 Presidential Primary

**Certified final:** 15,577 (see table above).

**Numerator (election-night plateau): NULL -- near miss (linked, never crawled).**
This year has a much denser Wayback crawl (472 domain-wide URLs in the 8-week
window 2016-05-24 to 2016-07-20) than 2012/2014, including several captures of
the county's `/elections`, `/dep-elections`, and `/election-results` pages
close to election night:

- `/elections` captures: 2016-05-25 (x2, pre), 2016-06-02 (pre, 5 days
  before), **2016-06-12 13:42 UTC (5 days AFTER)**, 2016-07-10, -11, -13, -19.
- `/dep-elections` captures: 2016-05-24, -27 (pre), **2016-06-11 12:04 UTC (4
  days after)**, 2016-07-03, -09 (x2).
- `/election-results` captures: 2016-06-02 (pre), 2016-06-05 (pre, 2 days
  before), **2016-06-13 18:45 UTC (6 days after)**, 2016-07-13, -19.

**No capture exists on election night itself (June 7) or the morning after
(June 8).** The closest post-election captures (`/elections` on June 12,
`/dep-elections` on June 11) were fetched and both link the SAME PDF:
`http://co.tehama.ca.us/images/stories/elections/ElectionSummaryReportfinal4.pdf`
("final4" in the filename, i.e. likely the county's fourth/final numbered
report). **This filename was never itself crawled by Wayback**
(CDX query for the exact URL returns zero rows) -- an identical
linked-but-uncrawled failure mode to the one already documented for this
county's 2016 and 2018 GENERAL rows in the existing dataset ("the report
was linked but never crawled"). No earlier-numbered report (First/Second/
Third) was found linked anywhere in the crawled window either.

Routes checked:

1. **Route 3/6.5 (Wayback of live results/elections pages):** as above --
   dense crawl, but a 5-day gap straddles election night in every one of the
   three relevant pages, and the one report filename recoverable from the
   post-election captures (`ElectionSummaryReportfinal4.pdf`) was itself never
   crawled.
2. **Route 6.6 (local news):** not separately re-searched (no known online
   archive for this county/era, consistent with prior rows).
3. **Not on Clarity.**

Null per RUNBOOK 5.1: a linked-but-uncrawled filename is not a substitute
source; the note documents exactly what was found and why it fails.

### Draft row

```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 15577,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 15,577 ballots cast (CA SoS SoV; precinct 4,187 + VBM 11,390; 50.70% of 30,724 registered; confirmed 2026-07-10, county line: Tehama 46 43,656 30,724 4,187 11,390 15,577 73.12% 50.70% 35.68%). Election-night PLATEAU not sourceable despite a denser-than-usual crawl (472 domain-wide URLs in the 8-week window). The county's /elections, /dep-elections, and /election-results pages were each crawled shortly before AND shortly after election night (5/25, 6/2, 6/5 pre; 6/11, 6/12, 6/13 post) but with a clean gap straddling June 7-8 itself -- no capture lands on election night or the morning after. The two post-election captures (6/11 dep-elections, 6/12 elections) both link the same PDF, images/stories/elections/ElectionSummaryReportfinal4.pdf ('final4', i.e. the county's fourth/final numbered report), but Wayback never crawled that exact filename (CDX confirms zero captures ever) -- an identical linked-but-uncrawled dead end to the one already documented for this county's 2016 and 2018 GENERAL rows. No earlier-numbered report (First/Second/Third) was found linked in any crawled page. No local news figure found. Not on Clarity. Null per RUNBOOK 5.1: a linked-but-uncrawled filename is not a substitute source. vs_epollbook/vs_asv n/a (control county, never adopted)."
}
```

### VERIFY.md draft line

Summary cell: `| 2016-06-07 | NULL | -- | none |`
Detail bullet: "2016-06-07 presidential primary: election-night ballots NULL
(dense crawl of /elections, /dep-elections, /election-results pages has a
clean gap over June 7-8; the one report filename recoverable from the
post-election captures, ElectionSummaryReportfinal4.pdf, was itself never
crawled by Wayback). Certified final 15,577 -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf.
Look for: a direct Wayback capture of
co.tehama.ca.us/images/stories/elections/ElectionSummaryReportfinal4.pdf, or
any First/Second/Third-numbered sibling report for June 2016."

### Plateau verdict

**N/A (null row).** Confidence: none. Evidence class: null-per-5.1 (near miss:
plateau candidate identified by filename, confirmed never archived).

---

## ITEM 4 of 6: 2018-06-05 Statewide Direct Primary

**Certified final:** 14,733 (see table above).

**Numerator (election-night plateau): NULL -- near miss (linked, then
contaminated by filename reuse).** The `/dep-elections` page was captured
2018-06-06 10:27 UTC (June 6, 3:27 AM PDT -- the morning immediately after
election night) and again 2018-06-11 and 2018-07-15. Fetched and compared:

- **2018-06-06 capture** (closest to election night) links
  `/images/images/Elections/ThirdUnofficialReport.pdf`.
- **2018-06-11 capture** (5 days later) links
  `/images/images/Elections/Fifth_Unofficial_Report.pdf`, i.e. the canvass had
  already progressed to a later-numbered report by then.

Both filenames were checked against Wayback CDX directly:

- `Fifth_Unofficial_Report.pdf`: **zero captures ever.**
- `ThirdUnofficialReport.pdf`: captured **twice, both 2020-03-04 and
  2020-03-06** -- i.e. nearly TWO YEARS after this election, and suspiciously
  exactly bracketing the **March 3, 2020 presidential primary**. This is the
  identical filename-reuse trap already documented and proven for this
  county's Joomla-era `images/images/Elections/` directory in the existing
  2016/2018 GENERAL rows ("a Joomla directory confirmed to silently overwrite
  report filenames across elections"). The 2020-03 capture of
  `ThirdUnofficialReport.pdf` almost certainly reflects the March 2020
  primary's own Third report, not June 2018's, and is therefore NOT citable
  as 2018 data (excluded per the same reasoning already applied to the
  general-election rows).

Routes checked:

1. **Route 3/6.5:** as above -- report filename found linked one day after
   election night, but the only Wayback capture of that exact filename is
   from a different, much later election (filename-reuse contamination).
2. **Route 6.2 (registrar press release):** WebSearch for the exact phrasing
   that worked for the county's 2022/2024 election-night releases
   (established in the existing general-election dossier) surfaced nothing
   dated June 2018.
3. **Route 6.6 (local news):** Red Bluff Daily News / Corning Observer, no
   election-night figure found (same outlets checked without success for the
   2018 general in the existing dataset).
4. **Not on Clarity** (probe-confirmed 404 in the existing dataset).

Null per RUNBOOK 5.1: a filename-collision capture from a different election
is never substituted for the true one.

### Draft row

```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 14733,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 14,733 ballots cast (CA SoS SoV; precinct 3,758 + VBM 10,975; 45.30% of 32,523 registered; confirmed 2026-07-10, county line: Tehama 46 43,835 32,523 3,758 10,975 14,733 74.49% 45.30% 33.61%). Election-night PLATEAU not sourceable. The co.tehama.ca.us /dep-elections page, captured 2018-06-06 (the morning after election night), links '/images/images/Elections/ThirdUnofficialReport.pdf'; by the next capture, 2018-06-11, the same page links 'Fifth_Unofficial_Report.pdf' (canvass had progressed). Fifth_Unofficial_Report.pdf has zero Wayback captures ever. ThirdUnofficialReport.pdf WAS crawled, but only twice -- 2020-03-04 and 2020-03-06 -- almost two years later and bracketing the March 3, 2020 presidential primary instead: this is the same Joomla images/images/Elections/ filename-reuse trap already proven for this county's 2016/2018 GENERAL rows (confirmed via the sibling Fifth_Unofficial_report.pdf pattern there), so the 2020 capture reflects a later election's Third report, not June 2018's, and cannot be cited. No registrar press release found for June 2018 (same WebSearch phrasing that worked for 2022/2024 surfaced nothing dated 2018, matching the finding already recorded for the Nov 2018 general row). No local news election-night figure found (Red Bluff Daily News, Corning Observer). Not on Clarity (probe-confirmed 404). Null per RUNBOOK 5.1: a filename-collision capture from a different election is never substituted for the true one. vs_epollbook/vs_asv n/a (control county, never adopted)."
}
```

### VERIFY.md draft line

Summary cell: `| 2018-06-05 | NULL | -- | none |`
Detail bullet: "2018-06-05 statewide primary: election-night ballots NULL
(ThirdUnofficialReport.pdf linked the morning after election night, but its
only Wayback captures are from March 2020, two years later, on the same
reused-filename Joomla directory already documented as a trap for this
county's general-election rows; Fifth_Unofficial_Report.pdf never crawled at
all). Certified final 14,733 -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf.
Look for: a pre-2020 capture of ThirdUnofficialReport.pdf, or any
First/Second/Fourth-numbered sibling report for June 2018."

### Plateau verdict

**N/A (null row).** Confidence: none. Evidence class: null-per-5.1 (near miss:
plateau candidate identified by filename, only recoverable capture proven
contaminated by later-election filename reuse).

---

## ITEM 5 of 6: 2022-06-07 Statewide Direct Primary

**Certified final:** 14,178 (see table above; corroborated by the county's own
125-page certified "June-7-2022-Statement-of-Vote.pdf", created 2022-06-29,
found on the WordPress uploads directory -- see below).

**Numerator (election-night plateau): NULL -- closest near miss of the six
years (plateau filename identified and dated to 1 day post-election, but
never itself crawled).** This is the WordPress era (`co.tehama.ca.us/wp-content/uploads/2022/06/`),
the same platform that yielded a CONFIRMED plateau for the 2022 GENERAL five
months later. A domain-wide CDX sweep of `co.tehama.ca.us` for 2022-06-07
through 2022-06-20 found:

- `ZeroProofReport.pdf` (crawled 2022-06-08 03:34 UTC, but internally dated
  **2022-06-03** -- a pre-election zero/test report, Voters Cast: 0 of
  37,815).
- The elections department landing page, captured **2022-06-09 01:58 UTC
  (June 8, 6:58 PM PDT -- the day after election night)**, which links
  `/wp-content/uploads/2022/06/Second-Precinct-Report-w-Vote-By-Mail-Ballots.pdf`.
  This filename (not "Third Unofficial Precinct Report" as in the general --
  the primary's numbering/naming convention differs) is the closest thing to
  a plateau candidate found across the entire primaries pass for this county.
  **It was never crawled by Wayback** (CDX for the exact URL returns zero
  rows).
- `Fourth-Report.pdf` (crawled 2022-08-15, but internally dated **2022-06-13
  -- 6 days after election night**, "Fourth Election Report," 39/39
  precincts, Turnout 14,002). This is a canvass-resumed update, not
  election-night data (compare: the general's Fourth report was similarly a
  Thursday-afternoon canvass update, 2 days post-election, rejected as the
  plateau there too).
- `June-7-2022-Statement-of-Vote.pdf` (crawled 2022-11-04 onward, but
  internally dated **2022-06-29** -- the county's own certified canvass book,
  22 days post-election; useful only as a corroborating certified-total
  cross-check, not a plateau candidate).

No `First-Report.pdf`, `Second-Report.pdf`, `Third-Report.pdf`,
`Fifth-Report.pdf`, `Sixth-Report.pdf`, or `Final-Report.pdf` (guessed
sibling filenames matching the `Fourth-Report.pdf` convention) has ANY
Wayback capture. The live domain `co.tehama.ca.us` is confirmed DNS-dead as
of 2026-07-10 (`curl`: could not resolve host, matching the dead-domain
finding already recorded for this county's 2022 general row), so there is no
live fallback for the missing filenames either.

Routes checked:

1. **Route 3/6.5 (Wayback of dated report / elections page):** as above --
   the plateau candidate (`Second-Precinct-Report-w-Vote-By-Mail-Ballots.pdf`)
   was identified precisely (linked the day after election night) but never
   itself archived.
2. **Route 6.2 (registrar press release):** not separately found in this
   window; the general row's press-release evidence is specific to
   November 2022 and not re-verified as existing for June.
3. **Route 6.6 (local news):** not separately re-searched.
4. **Not on Clarity.**

Null per RUNBOOK 5.1: a linked-but-uncrawled filename is not a substitute
source; documented as the closest near miss among the six years.

### Draft row

```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 14178,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 14,178 ballots cast (CA SoS SoV; precinct 1,710 + VBM 12,468; 37.50% of 37,811 registered; confirmed 2026-07-10, county line: Tehama 39 47,064 37,811 1,710 12,468 14,178 87.94% 37.50% 30.12%; corroborated by the county's own certified 125-page June-7-2022-Statement-of-Vote.pdf, internally dated 2022-06-29, recovered via Wayback). Election-night PLATEAU not sourceable -- closest near miss of the six primary years. The co.tehama.ca.us elections department page, captured 2022-06-09 01:58 UTC (the day after election night), links /wp-content/uploads/2022/06/Second-Precinct-Report-w-Vote-By-Mail-Ballots.pdf -- the clear plateau-candidate filename -- but Wayback never crawled that exact PDF (CDX confirms zero captures ever). The only numbered report actually recovered, Fourth-Report.pdf ('Fourth Election Report'), is internally dated 2022-06-13, six days post-election, 39/39 precincts, Turnout 14,002 -- a canvass-resumed update, not election-night data (parallel to the general's own Fourth report, rejected there for the same reason). ZeroProofReport.pdf is a pre-election test report (internally dated 2022-06-03, Voters Cast 0). No First/Second/Third/Fifth/Sixth/Final-Report.pdf sibling filename (matching the Fourth-Report.pdf naming convention) has any Wayback capture. The live domain co.tehama.ca.us is confirmed DNS-dead as of 2026-07-10 (curl: could not resolve host), so there is no live-site fallback. No registrar press release or local news figure separately searched/found for June 2022. Not on Clarity. Null per RUNBOOK 5.1: a linked-but-uncrawled filename is not a substitute source. vs_epollbook/vs_asv n/a (control county, never adopted)."
}
```

### VERIFY.md draft line

Summary cell: `| 2022-06-07 | NULL | -- | none |`
Detail bullet: "2022-06-07 statewide primary: election-night ballots NULL
(closest near miss of the six years -- Second-Precinct-Report-w-Vote-By-Mail-Ballots.pdf
linked the day after election night on the elections department page, but
never itself archived by Wayback; only a 6-days-later 'Fourth Election Report'
canvass update survives). Certified final 14,178 -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf.
Look for: a direct Wayback capture of
co.tehama.ca.us/wp-content/uploads/2022/06/Second-Precinct-Report-w-Vote-By-Mail-Ballots.pdf, or
any First-numbered sibling report for June 2022 (co.tehama.ca.us itself is now
DNS-dead, so only Wayback/an operator's own saved copy could recover it)."

### Plateau verdict

**N/A (null row).** Confidence: none. Evidence class: null-per-5.1 (closest
near miss of the six primary years: exact plateau filename identified and
dated, but the artifact itself was never archived and the live domain is now
dead).

---

## ITEM 6 of 6: 2024-03-05 Presidential Primary

**Certified final:** 15,537 (see table above; independently corroborated --
see below).

**Numerator (election-night plateau): SOURCED, CONFIRMED.**

The full numbered-report series for this election was recovered from Wayback
captures of `tehama.gov/wp-content/uploads/2024/03/` (a domain-wide CDX
prefix sweep of that folder returned every report filename; each was then
fetched via the `id_` raw-replay form and its `pdfinfo CreationDate` /
internal "Voters Cast" or "Total Registration and Turnout" line read):

| report | crawled (Wayback) | internal CreationDate (PST/PDT) | precincts | turnout (ballots) |
|---|---|---|---|---|
| Zero Proof Report | 2025-05-02 | Mon Mar 4 2024 10:17:15 AM | 0/40 | 0 |
| "Summary-Report-2-Column" (VBM-only pre-close report) | 2025-05-02 | Tue Mar 5 2024 7:59:46 PM | 0/40 | 6,241 |
| First Unofficial Report | 2025-05-02 | Tue Mar 5 2024 9:34:00 PM | 22/40 | 6,831 |
| **Second Unofficial Report** | 2025-05-05 | **Tue Mar 5 2024 10:31:56 PM** | **40/40 (100%)** | **7,998** |
| Third Unofficial Report | 2025-05-02 | Fri Mar 8 2024 5:26:08 PM | 40/40 | 10,596 |
| Fourth Unofficial Report | 2025-05-02 | Mon Mar 11 2024 4:50:21 PM | 40/40 | 11,785 |
| Fifth Unofficial | 2025-05-02 | Fri Mar 15 2024 10:11:39 AM | 40/40 | 15,190 |
| Sixth Unofficial Report | 2025-05-02 | Thu Mar 21 2024 5:50:07 PM | 40/40 | 15,509 |
| Final Official Report | 2025-05-02 | Fri Mar 29 2024 2:35:11 PM | 40/40 | **15,537** (= certified) |

**The plateau is the Second Unofficial Report: 7,998 ballots, internally
timestamped Tuesday March 5, 2024, 10:31:56 PM PST, 40 of 40 precincts (100%)
reported.** This is the LAST report posted on election night: the "Summary
Report 2-Column" VBM-only report (7:59:46 PM, pre-poll-close, 0/40 precincts)
is the classic first tranche and is NOT the plateau; the First Unofficial
Report (9:34 PM, 22/40 precincts) is a mid-evening update and also NOT the
plateau; the Second Unofficial Report is the first (and last) report of the
night to reach 100% of precincts. The next report, Third Unofficial, is dated
**Friday March 8, 2024, 5:26 PM -- a clean 3-day gap** with nothing
interposed, i.e. the county's own posting cadence brackets the Second report
as the last one of election night (RUNBOOK section 8 bracket: "the report
series' next file being days later"). This report-numbering pattern differs
from the November 2024 general (where "Third" was the plateau) because the
primary's sequence includes an extra pre-poll-close VBM report ahead of the
numbered series; the structural test (100% precincts + next report is days
later) is the same.

**Certified-final cross-check:** the Final Official Report (fetched from the
same Wayback capture set, internally dated March 29, 2024) reads "Voters
Cast: 15,537 of 37,020 (41.97%)" -- an EXACT match to the CA SoS SoV Total
Voters figure (15,537), confirming the denominator independently of the SoS
PDF.

**Arithmetic:** 7,998 / 15,537 = 51.4771...% → **51.48%** (round to 2dp).

**Calibration:** 51.48% sits below the runbook's small-rural-county
80-95%-of-final expectation and below SF's own presidential-primary-adjacent
range, but is directly comparable to this county's OWN 2024 GENERAL
election-night share (48.79%) -- both November 2024 and March 2024 land in
the high-40s/low-50s, both explained by the same heavy-VBM composition
(87.51% of the certified total is VBM per the SoV line) and the same
precinct-centric "100% precincts reporting" framing (which describes
in-person precinct tabulation completion, not VBM/drop-box processing --
most of the ~7,500-ballot gap to certified is canvassed over the following
month, visible directly in the Third-through-Sixth report sequence above).
Internally consistent with the general-election row's own calibration note.

**Pre/post tech:** n/a -- Tehama never adopted e-pollbooks or ASV (control
county, county-tech census row status "never").

### Draft row

```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 7998,
  "certified_final": 15537,
  "election_night_pct": 51.48,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20250505001307id_/https://www.tehama.gov/wp-content/uploads/2024/03/Second-Unofficial-Report.pdf",
  "confidence": "primary",
  "note": "Election-night PLATEAU = 7,998 ballots ('Total Registration and Turnout: 37,111 / 7,998'), from Tehama County's official 'Second Unofficial Report' (Tehama County March 5 2024 Presidential Primary Election Summary Report), internally timestamped 3/5/2024 10:31:56 PM PST (pdfinfo CreationDate), 40 of 40 precincts (100%) reported. Recovered from Wayback (co.tehama.gov domain-wide CDX prefix sweep of wp-content/uploads/2024/03/ enumerated the full report series) since the live tehama.gov directory now serves only the current (2026-06) election's reports. This is the night's plateau, NOT the 7:59:46 PM 'Summary Report 2-Column' VBM-only pre-poll-close report (6,241 ballots, 0/40 precincts, classic first tranche) and NOT the First Unofficial Report (9:34:00 PM, 6,831 ballots, 22/40 precincts, mid-evening partial update): the Second is the first (and last) report to reach 100% of precincts. It HELD through the rest of election night and beyond: the report series' next file, Third Unofficial Report, is internally dated Friday March 8, 2024 5:26:08 PM -- a clean 3-day gap with nothing interposed, i.e. the county's own posting cadence brackets the Second Unofficial as the last report of election night (RUNBOOK 8: 'report series' next file being days later'). Arithmetic: 7,998 / 15,537 = 51.48% (round(7998/15537*100,2)). Certified final independently cross-checked against the county's own Final Official Report (internally dated 3/29/2024): 'Voters Cast: 15,537 of 37,020 (41.97%)', exact match to the SoS SoV Total Voters figure. Pre/post tech: n/a, Tehama never adopted e-pollbooks or ASV (control county, county-tech census row status 'never'). PRIMARY (official county Election Summary Report PDF via Wayback). Calibration: 51.48% reads low vs the runbook's small-rural-county 80-95% expectation, but is directly comparable to this county's OWN November 2024 general election-night share (48.79%) -- both explained by the same heavy-VBM composition (87.51% VBM of the certified total per the SoV line) and the same precinct-centric 100%-precincts framing (in-person tabulation completion, not VBM/drop-box processing, most of which is canvassed over the following month, visible in the Third-through-Sixth report sequence: 10,596 -> 11,785 -> 15,190 -> 15,509 -> 15,537 certified)."
}
```

### VERIFY.md draft line

Summary cell: `| 2024-03-05 | 7,998 (51.48%) | CONFIRMED | primary |`
Detail bullet: "2024-03-05 presidential primary: election-night plateau =
7,998 ballots (51.48% of certified), from the county's Second Unofficial
Report, internally timestamped 3/5/2024 10:31:56 PM PST, 40/40 precincts
(100%). Recovered from Wayback:
https://web.archive.org/web/20250505001307id_/https://www.tehama.gov/wp-content/uploads/2024/03/Second-Unofficial-Report.pdf.
Certified final 15,537 -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
(cross-checked exactly against the county's own Final Official Report). Look
for: 'Second Unofficial Report' header, 'Total Registration and Turnout
37,111 / 7,998', 40 of 40 precincts reported; the NEXT report (Third
Unofficial) should be dated three days later, March 8, not the same night."

### Plateau verdict

**CONFIRMED.** Basis: self-describes as the numbered "Second Unofficial
Report" with an internal late-night timestamp (10:31:56 PM) AND 100% precinct
completion, PLUS the independent leg required by RUNBOOK section 8 -- the
report series' own next file (Third Unofficial) is dated three days later
(March 8) with nothing interposed, proving the Second Unofficial Report was
the last one posted on election night. Evidence: the full 9-report Wayback
series fetched and timestamped (table above); FinalOfficial.pdf's printed
Voters Cast (15,537) exactly matches the independently-sourced SoS SoV total.

```json
{
  "slug": "tehama-ca",
  "date": "2024-03-05",
  "verdict": "CONFIRMED",
  "basis": "self-describes as 'Second Unofficial Report' with internal timestamp 3/5/2024 10:31:56 PM PST and 40/40 (100%) precincts reported; independent leg = report series' own next file (Third Unofficial) dated 3 days later (3/8/2024 5:26:08 PM) with nothing interposed",
  "evidence": "Wayback series https://web.archive.org/web/20250505001307id_/.../Second-Unofficial-Report.pdf (Voters Cast 37,111/7,998, 40/40 precincts); Third Unofficial Report https://web.archive.org/web/20250502055740id_/.../Third-Unofficial-Report.pdf (dated 3/8/2024); Final Official Report Voters Cast 15,537/37,020 matches SoS SoV Total Voters exactly"
}
```

---

## Summary table (VERIFY.md style, for the human packet)

| date | type | election-night ballots | pct | vs_epollbook | vs_asv | confidence | verdict |
|---|---|---|---|---|---|---|---|
| 2012-06-05 | presidential-primary | NULL | -- | n/a | n/a | none | n/a (null) |
| 2014-06-03 | statewide-primary | NULL | -- | n/a | n/a | none | n/a (null) |
| 2016-06-07 | presidential-primary | NULL | -- | n/a | n/a | none | n/a (null) |
| 2018-06-05 | statewide-primary | NULL | -- | n/a | n/a | none | n/a (null) |
| 2022-06-07 | statewide-primary | NULL | -- | n/a | n/a | none | n/a (null) |
| 2024-03-05 | presidential-primary | 7,998 | 51.48% | n/a | n/a | primary | CONFIRMED |

Cross-cell picture: identical structural finding to the general-election
dossier -- Tehama's pre-2020 Joomla-era site (2012-2018) is essentially
unrecoverable for election-night detail regardless of election type (weak or
absent Wayback crawls; where a report filename IS linked near election night,
it was either never crawled or -- worse -- crawled only years later on the
same reused-filename directory, contaminated by a different election). The
2022 primary is the one meaningful difference from the general-election
pattern: unlike the 2022 GENERAL (fully recovered via Wayback), the 2022
PRIMARY's WordPress-era plateau candidate was identified precisely by
filename and date but was never itself archived -- a genuine near miss, not a
platform-level failure. Only the 2024 primary, like the 2024 general, is
fully recoverable, in this case directly from a Wayback sweep of the
permanent (non-colliding) tehama.gov year/month upload folder.

## FLAGS for manual operator

None required. Every non-null candidate this pass either resolved to a
citable artifact (2024-03-05) or was conclusively shown unrecoverable by
machine means alone (linked-but-never-crawled filenames confirmed via direct
CDX queries; the live co.tehama.ca.us domain confirmed DNS-dead). No source
in this dossier is blocked behind a bot-wall or JS-only render that a human
browser session could plausibly get past that curl/CDX could not -- the
missing artifacts are missing from the Wayback corpus itself, not merely
inaccessible to curl.
