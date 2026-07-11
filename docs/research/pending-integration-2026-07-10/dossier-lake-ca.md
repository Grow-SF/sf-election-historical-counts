# Lake County, CA (lake-ca) — control-county evidence dossier

Note: items below are appended in completion order, not strictly 0-6
numeric order (persist-as-you-go rule); Item 0 (tech record) appears after
Item 1 because it was finished second. Use the `## Item N` headers to
navigate, not file position.

Read first: docs/research/RUNBOOK.md (metric definition section 1, schema
section 2, hard cases section 5, source playbooks section 6, gotchas
section 7, plateau evidence standard section 8). Probe file verdict for
Lake (archive-probes-a-m.md): **viable** — no Clarity, a dated
`publicapps.lakecountyca.gov/elections/results/result30.htm` results page
with a same-cycle 2016-11-12 Wayback capture, and a confirmed
`Nov2018MediaReleases/` folder convention. Census row (never-adopter,
confidence low) reused below and extended.

Working files (fetched into scratch, NOT the repo cache):
`/private/tmp/claude-501/-Users-sbuss-workspace-sf-election-count/cbd9561c-405d-4e44-8f38-6a4a9bd48e60/scratchpad/lake-ca/`
holds `sov_2012.pdf` … `sov_2024.pdf` (CA SoS Statement of Vote, Voter
Participation Statistics by County) and their `pdftotext -layout` output.

---

## Item 1 — 2012-11-06 presidential-general

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2012 general (2012 URL pattern drops
the `sov/` segment per RUNBOOK 6.1) —
`https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf`
(fetched to scratch as `lake-ca/sov_2012.pdf`, verified 200/real PDF).
County line as printed (`pdftotext -layout`): `Lake  70  47,135  34,936  8,987  14,698  23,685  62.06%  67.80%  50.25%`
— columns are Precincts / Eligible to Register / Registered Voters /
Precinct Voters / Vote-By-Mail Voters / **Total Voters** / %VBM / Turnout-Reg
/ Turnout-Eligible. **Total Voters = 23,685.**

**Election-night plateau — FOUND, route 6.5 (Wayback capture of the county's
own numbered results-report system):**

- Locating query trail: CDX on `publicapps.lakecountyca.gov/elections/results/`
  and on the whole `publicapps.lakecountyca.gov` domain for Nov 2012 returned
  `[]` both times (that subdomain postdates 2012 — it's the system the probe
  found live for 2016). Backed off to CDX on the 2012-era domain
  `co.lake.ca.us` (`matchType=domain`, `from=20121101&to=20121130`), grepped
  the 1,190 hits for `elect|result|clerk|vote`, and found a THIRD, older
  results subdomain: `acm.co.lake.ca.us/elections/results/` (numbered
  `resultNN.htm` / `indexNN.htm` report files — "ACM" = Auditor-Controller/
  Clerk-Recorder, Lake's ROV was folded into that office in 2012).
- CDX (`url=acm.co.lake.ca.us/elections/results/&matchType=prefix&from=20120801&to=20130331`)
  shows `result24.htm` (the Nov 6 2012 general's report number, confirmed by
  its `index24.htm` sibling's title block "LAKE COUNTY / Consolidated
  General Election / November 6, 2012") captured **twice**: 2012-11-10
  03:45:13 UTC (digest `TKJL2X...`) and 2012-12-25 11:18:19 UTC (digest
  `O3IX3K...`, DIFFERENT digest = content changed).
- Raw `id_` fetch of the 2012-11-10 capture
  (`https://web.archive.org/web/20121110034513id_/http://acm.co.lake.ca.us:80/elections/results/result24.htm`)
  is plain HTML (not gzipped) and reads, verbatim: **"Preliminary Election
  Results as of 11/06/2012 at 11:59:41 PM"**, "Completed Precincts: 70 of
  70" (100%), "Total Registered Voters 34,938 ... Precinct Ballots Cast
  8,565 (24.5%) ... Absentee Ballots Cast 8,057 (23.1%) ... **Total Ballots
  Cast 16,622 (47.6%)**." This is a genuine server-generated late-night
  timestamp (11:59:41 PM on election DAY itself, effectively the last
  possible moment of "election night" as the runbook defines it), not a
  crawl-date artifact — the crawl happened 4 days later (Nov 10) but the
  embedded report clock is frozen at 11:59:41 PM Nov 6.
- **Non-circular leg (RUNBOOK 8):** the SAME url's next Wayback capture
  (2012-12-25) is titled **"Final Results for Election"** and reads "Total
  Ballots Cast 23,685 (67.8%)" — which is the EXACT certified-final total
  from the SoS SoV PDF (23,685). This proves (a) the county's report system
  overwrites this URL in place as the canvass proceeds rather than posting a
  new numbered file per update, (b) the only intermediate state Wayback ever
  captured between the Nov 6 11:59:41 PM snapshot and the Dec 25 certified
  Final is the frozen 11:59:41 PM one, i.e. no other on-night update is lost
  in between, and (c) the 16,622 figure is definitively PRE-canvass (its
  absentee count, 8,057, is far below the eventual certified 14,698 VBM,
  meaning ~6,641 more VBM ballots were processed in the multi-week canvass
  after election night, exactly the pattern the runbook describes). This is
  the "report series' next file being days later" leg from section 8.
- NOT the 8 p.m. first tranche (no 8 p.m.-era capture of this URL survives
  in Wayback; the 11:59:41 PM report is explicitly the latest pre-canvass
  state found, self-labeled "Preliminary" not "First").
- Arithmetic: 16,622 / 23,685 = **70.18%**.

```json
{
  "date": "2012-11-06",
  "type": "presidential-general",
  "election_night_ballots": 16622,
  "certified_final": 23685,
  "election_night_pct": 70.18,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20121110034513/http://acm.co.lake.ca.us:80/elections/results/result24.htm",
  "confidence": "primary",
  "note": "PLATEAU = county's own numbered results-report system (acm.co.lake.ca.us/elections/results/result24.htm, report #24 = the Nov 6 2012 Consolidated General per its index24.htm title block). Internal header: 'Preliminary Election Results as of 11/06/2012 at 11:59:41 PM' (self-described late-night timestamp, effectively midnight on election day). 'Completed Precincts: 70 of 70' (100%). 'Total Ballots Cast 16,622 (47.6% of registered)' = Precinct Ballots Cast 8,565 + Absentee Ballots Cast 8,057. NON-CIRCULAR LEG (RUNBOOK 8): the SAME URL's only later Wayback capture (2012-12-25 11:18:19 UTC) is titled 'Final Results for Election' and shows Total Ballots Cast 23,685 (67.8%) -- the EXACT certified total from the SoS SoV -- proving the county overwrites this URL in place as the canvass proceeds, that no other on-night update was lost between the frozen 11:59:41 PM snapshot and the certified-final overwrite weeks later, and that 16,622 is genuinely pre-canvass (its absentee subtotal, 8,057, is far below the eventual certified 14,698 VBM; ~6,641 more VBM ballots were processed post-election-night). NOT the 8 PM first tranche (no capture of an earlier state survives; the 11:59:41 PM report is self-labeled 'Preliminary', the latest pre-canvass state found). Certified final 23,685 voters (CA SoS Voter Participation Statistics by County: 8,987 precinct + 14,698 VBM). Pct = 16,622/23,685 = 70.18%, well above SF's ~71% 2012 calibration is close but Lake trends higher as expected for a small rural county with an all-in-one election-night precinct count. Lake never adopted epollbook or ASV (n/a both legs, control county). CDX queries used: url=acm.co.lake.ca.us/elections/results/&matchType=prefix&from=20120801&to=20130331 (found result24.htm both captures); url=co.lake.ca.us&matchType=domain&from=20121101&to=20121130 (found the acm subdomain in the first place after publicapps.lakecountyca.gov CDX for Nov 2012 returned empty)."
}
```

**VERIFY.md draft (summary row):** `| 2012 | presidential-general | 16,622 | 23,685 | 70.2% | primary | [link](https://web.archive.org/web/20121110034513/http://acm.co.lake.ca.us:80/elections/results/result24.htm) |`

**VERIFY.md draft (detail bullet):**
- **2012 presidential-general** — night `16,622` / final `23,685` = `70.2%` (primary)
  - numerator: <https://web.archive.org/web/20121110034513/http://acm.co.lake.ca.us:80/elections/results/result24.htm>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf>
  - look for: "Preliminary Election Results as of 11/06/2012 at 11:59:41 PM", "Completed Precincts: 70 of 70", "Total Ballots Cast 16,622 47.6%"; the same URL's Dec 25 capture reads "Final Results for Election ... Total Ballots Cast 23,685 67.8%" (proves the plateau/overwrite pattern).

**plateau_review.json draft:**
```json
{"slug": "lake-ca", "date": "2012-11-06", "verdict": "CONFIRMED", "basis": "self-described late-night timestamp + later capture of same URL overwritten to the certified final", "evidence": "result24.htm 2012-11-10 capture: 'Preliminary Election Results as of 11/06/2012 at 11:59:41 PM', 70/70 precincts, Total Ballots Cast 16,622; same URL's only later capture (2012-12-25) reads 'Final Results for Election ... Total Ballots Cast 23,685' (= certified final exactly)"}
```

---

## Item 2 — 2014-11-04 midterm-general

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2014 general (2014 uses the misspelled
`particpiation` path per RUNBOOK 6.1) —
`https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf`
(fetched to scratch as `lake-ca/sov_2014.pdf`, verified 200/real PDF).
County line as printed: `Lake  70  49,067  33,489  6,017  12,044  18,061
66.69%  53.93%  36.81%` → **Total Voters = 18,061.**

**Election-night plateau — FOUND, same route as 2012 (numbered
`acm.co.lake.ca.us/elections/results/` report page, this time report
#27):**

- CDX (`url=acm.co.lake.ca.us/elections/results/&matchType=prefix&from=20140901&to=20150228`)
  found `index27.htm` (captured 2015-02-05, title block confirms "LAKE
  COUNTY / General Election / November 4, 2014") and `result27.htm`
  captured FOUR times: 2014-11-08 05:03:47 UTC (digest `AJH6HN...`),
  2014-11-30 08:26:48 UTC (SAME digest `AJH6HN...`), 2014-11-30 14:08:17 UTC
  (a `warc/revisit` pointer to the same digest), and 2015-01-27 03:54:38 UTC
  (NEW digest `2Z36BC...`, content changed).
- Raw `id_` fetch of the 2014-11-08 05:03:47 UTC capture
  (`https://web.archive.org/web/20141108050347id_/http://acm.co.lake.ca.us:80/elections/results/result27.htm`):
  header reads **"Election Results as of 11/05/2014 at 12:41:23 AM"**,
  "Completed Precincts: 70 of 70" (100%), "Total Registered Voters 33,489 …
  Precinct Ballots Cast 5,365 (16.0%) … Absentee Ballots Cast 7,228 (21.6%)
  … **Total Ballots Cast 12,593 (37.6%)**." Internal timestamp 12:41:23 AM
  is past midnight into Nov 5, i.e. genuinely the tail of election night.
- **Non-circular leg (RUNBOOK 8) — the strongest form, direct held-count:**
  the 2014-11-30 08:26:48 UTC capture of the SAME URL has the IDENTICAL
  digest (`AJH6HNMV3OVULKQXIFCRFEJFVHRZPJFN`) as the Nov 8 capture — the
  page's content was byte-for-byte unchanged for over three weeks after
  election night, directly proving the 12,593 figure held through the
  canvass pause. Only by 2015-01-27 does the digest change to a version
  labeled **"Final Results for Election"**, reading "Total Ballots Cast
  18,061 (53.9%)" — exactly the certified final from the SoS SoV (18,061).
- NOT the 8 p.m. first tranche (no earlier-Nov-4 capture of this URL
  survives; 12:41:23 AM is explicitly past-midnight, and the page
  self-labels as the general "Election Results", not "Preliminary
  First Report").
- Arithmetic: 12,593 / 18,061 = **69.72%**.

```json
{
  "date": "2014-11-04",
  "type": "midterm-general",
  "election_night_ballots": 12593,
  "certified_final": 18061,
  "election_night_pct": 69.72,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20141108050347/http://acm.co.lake.ca.us:80/elections/results/result27.htm",
  "confidence": "primary",
  "note": "PLATEAU = county's own numbered results-report system (acm.co.lake.ca.us/elections/results/result27.htm, report #27 = Nov 4 2014 General per its index27.htm title block). Internal header: 'Election Results as of 11/05/2014 at 12:41:23 AM' (past-midnight, tail of election night). 'Completed Precincts: 70 of 70' (100%). 'Total Ballots Cast 12,593 (37.6%)' = Precinct 5,365 + Absentee 7,228. NON-CIRCULAR LEG (RUNBOOK 8, strongest form): the SAME URL's 2014-11-30 08:26:48 UTC Wayback capture has the IDENTICAL content digest (AJH6HNMV3OVULKQXIFCRFEJFVHRZPJFN) as the Nov 8 capture -- the page held byte-for-byte unchanged for 3+ weeks after election night, directly proving the plateau held. Only the 2015-01-27 capture shows new content, labeled 'Final Results for Election', Total Ballots Cast 18,061 (53.9%) -- the exact SoS certified total. NOT the 8 PM first tranche (no earlier capture survives; 12:41:23 AM is explicitly past midnight). Certified final 18,061 voters (CA SoS Voter Participation Statistics by County: 6,017 precinct + 12,044 VBM). Pct = 12,593/18,061 = 69.72%. Lake never adopted epollbook or ASV (n/a both legs, control county). CDX query: url=acm.co.lake.ca.us/elections/results/&matchType=prefix&from=20140901&to=20150228."
}
```

**VERIFY.md draft (summary row):** `| 2014 | midterm-general | 12,593 | 18,061 | 69.7% | primary | [link](https://web.archive.org/web/20141108050347/http://acm.co.lake.ca.us:80/elections/results/result27.htm) |`

**VERIFY.md draft (detail bullet):**
- **2014 midterm-general** — night `12,593` / final `18,061` = `69.7%` (primary)
  - numerator: <https://web.archive.org/web/20141108050347/http://acm.co.lake.ca.us:80/elections/results/result27.htm>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf>
  - look for: "Election Results as of 11/05/2014 at 12:41:23 AM", "Completed Precincts: 70 of 70", "Total Ballots Cast 12,593 37.6%"; a later capture (2014-11-30) of the same URL is byte-identical (digest match); only the 2015-01-27 capture changes to "Final Results for Election ... Total Ballots Cast 18,061 53.9%".

**plateau_review.json draft:**
```json
{"slug": "lake-ca", "date": "2014-11-04", "verdict": "CONFIRMED", "basis": "self-described past-midnight timestamp + byte-identical later capture of same URL (digest match) three weeks after election night", "evidence": "result27.htm 2014-11-08 capture: 'Election Results as of 11/05/2014 at 12:41:23 AM', 70/70 precincts, Total Ballots Cast 12,593; the 2014-11-30 capture of the same URL has the IDENTICAL digest AJH6HNMV3OVULKQXIFCRFEJFVHRZPJFN; only the 2015-01-27 capture changes to 'Final Results for Election ... Total Ballots Cast 18,061' (= certified final exactly)"}
```

---

## Item 3 — 2016-11-08 presidential-general

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2016 general —
`https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf`
(fetched to scratch as `lake-ca/sov_2016.pdf`, verified 200/real PDF).
County line as printed: `Lake  70  48,487  34,706  8,163  16,922  25,085
67.46%  72.28%  51.74%` → **Total Voters = 25,085.**

**Election-night plateau — FOUND, same route/subdomain the probe file
already flagged (`publicapps.lakecountyca.gov/elections/results/`, report
#30 this election; note the results system MOVED subdomains between 2014
(`acm.co.lake.ca.us`) and 2016 (`publicapps.lakecountyca.gov`), consistent
with the probe's note that results live on a separate subdomain from the
main county site):**

- CDX (`url=publicapps.lakecountyca.gov/elections/results/&matchType=prefix&from=20161001&to=20170228`)
  returned exactly 4 hits: `result29.htm` (2016-10-14, a different report
  number, i.e. NOT this election — presumably June 2016 primary), then
  `result30.htm` captured 2016-11-12 11:08:47 UTC (digest `SO4RCU...`),
  2016-12-24 07:47:32 UTC (NEW digest `IX3YNY...`), and 2017-02-23 (revisit,
  same as Dec 24). No intermediate captures exist between Nov 12 and Dec 24
  — a 6-week gap consistent with "the report series' next file being days
  [weeks] later" (RUNBOOK 8).
- Raw `id_` fetch of the 2016-11-12 11:08:47 UTC capture: header reads
  **"Election Results as of 11/09/2016 at 12:49:48 AM"**, explicitly
  labeled **"PRELIMINARY RESULTS"**, "Completed Precincts: 70 of 70"
  (100%), "Total Registered Voters 34,707 … Precinct Ballots Cast 6,897
  (19.9%) … Absentee Ballots Cast 6,587 (19.0%) … **Total Ballots Cast
  13,484 (38.9%)**." Internal timestamp 12:49:48 AM Nov 9 is past midnight,
  the tail of election night (polls closed 8 p.m. Nov 8; by ~12:49 AM all
  70/70 precincts had reported in).
- **Non-circular leg:** the SAME URL's next capture (2016-12-24, six weeks
  later) is titled **"Final Results for Election"**, "FINAL RESULTS" label,
  "Total Ballots Cast 25,094 (72.3%)" — matching the SoS certified 25,085
  to within 9 ballots (routine late administrative correction between the
  county's own final tally and the SoS-certified figure; not a discrepancy
  in method). This is the same overwrite-in-place pattern already confirmed
  for 2012 and 2014 at this county, so the Nov 12 "PRELIMINARY" capture is
  reliably pre-canvass.
- NOT the 8 p.m. first tranche (no earlier-election-night capture of this
  URL survives; the page explicitly self-labels "PRELIMINARY RESULTS" as of
  12:49:48 AM, i.e. after full precinct reporting, not the pre-processed-VBM-only
  8 p.m. dump).
- Arithmetic: 13,484 / 25,085 = **53.75%**. Notably lower than Lake's own
  2012 (70.18%) and 2014 (69.72%) — consistent with the higher presidential-year
  VBM surge (only 6,587 of the eventual 16,922 certified VBM ballots were in
  by the Nov 9 report, i.e. ~39% of VBM was election-night vs. ~55% in 2012),
  not any tech confound (Lake never adopted epollbook/ASV; this is simply
  turnout-composition variance across a presidential year).

```json
{
  "date": "2016-11-08",
  "type": "presidential-general",
  "election_night_ballots": 13484,
  "certified_final": 25085,
  "election_night_pct": 53.75,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20161112110847/http://publicapps.lakecountyca.gov:80/elections/results/result30.htm",
  "confidence": "primary",
  "note": "PLATEAU = county's own numbered results-report system, now hosted on publicapps.lakecountyca.gov (moved from acm.co.lake.ca.us between 2014 and 2016), report #30 = Nov 8 2016 Consolidated General. Internal header: 'Election Results as of 11/09/2016 at 12:49:48 AM', explicitly labeled 'PRELIMINARY RESULTS'. 'Completed Precincts: 70 of 70' (100%). 'Total Ballots Cast 13,484 (38.9%)' = Precinct 6,897 + Absentee 6,587. NON-CIRCULAR LEG (RUNBOOK 8): the SAME URL's only later capture (2016-12-24, six weeks after election night, no intermediate captures exist per CDX) is titled 'Final Results for Election' / 'FINAL RESULTS', Total Ballots Cast 25,094 (72.3%) -- matching the SoS certified 25,085 to within 9 ballots (routine late county-vs-SoS reconciliation, not a method discrepancy). Same overwrite-in-place report-page pattern already independently confirmed for this county in 2012 and 2014. NOT the 8 PM first tranche (no earlier capture survives; page self-labels 'PRELIMINARY RESULTS' as of 12:49:48 AM, after full 70/70 precinct reporting). Certified final 25,085 voters (CA SoS Voter Participation Statistics by County: 8,163 precinct + 16,922 VBM). Pct = 13,484/25,085 = 53.75% -- notably lower than Lake's own 2012 (70.18%) and 2014 (69.72%), driven by presidential-year VBM surge (only 6,587 of the eventual 16,922 certified VBM ballots were in by the Nov 9 report), not any tech confound (Lake never adopted epollbook/ASV, n/a both legs, control county). CDX query: url=publicapps.lakecountyca.gov/elections/results/&matchType=prefix&from=20161001&to=20170228."
}
```

**VERIFY.md draft (summary row):** `| 2016 | presidential-general | 13,484 | 25,085 | 53.8% | primary | [link](https://web.archive.org/web/20161112110847/http://publicapps.lakecountyca.gov:80/elections/results/result30.htm) |`

**VERIFY.md draft (detail bullet):**
- **2016 presidential-general** — night `13,484` / final `25,085` = `53.8%` (primary)
  - numerator: <https://web.archive.org/web/20161112110847/http://publicapps.lakecountyca.gov:80/elections/results/result30.htm>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "Election Results as of 11/09/2016 at 12:49:48 AM", "PRELIMINARY RESULTS", "Completed Precincts: 70 of 70", "Total Ballots Cast 13,484 38.9%"; the 2016-12-24 capture of the same URL reads "Final Results for Election ... FINAL RESULTS ... Total Ballots Cast 25,094 72.3%" (matches certified 25,085 within 9 ballots).

**plateau_review.json draft:**
```json
{"slug": "lake-ca", "date": "2016-11-08", "verdict": "CONFIRMED", "basis": "self-described past-midnight 'PRELIMINARY RESULTS' timestamp + only later capture of same URL (6 weeks on, no intermediate captures) labeled 'FINAL RESULTS' at the certified total", "evidence": "result30.htm 2016-11-12 capture: 'Election Results as of 11/09/2016 at 12:49:48 AM', 'PRELIMINARY RESULTS', 70/70 precincts, Total Ballots Cast 13,484; the 2016-12-24 capture of the same URL (next in CDX, 6 weeks later) reads 'Final Results for Election ... FINAL RESULTS ... Total Ballots Cast 25,094' (matches SoS certified 25,085 within 9 ballots)"}
```

---

## Item 4 — 2018-11-06 midterm-general

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2018 general —
`https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf`
(fetched to scratch as `lake-ca/sov_2018.pdf`, verified 200/real PDF).
County line as printed: `Lake  70  49,469  32,653  6,049  15,416  21,465
71.82%  65.74%  43.39%` → **Total Voters = 21,465.**

**Election-night plateau — FOUND, same `publicapps.lakecountyca.gov`
report system, report #37:**

- `index37.htm` (captured 2018-11-07 23:14:01 UTC, i.e. the afternoon after
  election night) title block confirms "LAKE COUNTY / 2018 Statewide
  General Election / November 6, 2018" and links to `result37.htm`.
- CDX for `result37.htm` (checked with NO date restriction, to catch every
  capture ever) returns exactly **ONE** hit, ever: 2018-11-29 03:30:58 UTC.
  Raw `id_` fetch of that capture reads: **"Election Results as of
  11/07/2018 at 12:14:30 AM"**, explicitly labeled **"PRELIMINARY
  RESULTS"**, "Completed Precincts: 70 of 70" (100%), "Total Registered
  Voters 32,663 … Precinct Ballots Cast 4,956 (15.2%) … Absentee Ballots
  Cast 8,566 (26.2%) … **Total Ballots Cast 13,522 (41.4%)**." Internal
  timestamp 12:14:30 AM Nov 7 is past midnight, the tail of election night.
- **Non-circular leg, single-capture form:** Wayback crawled this exact page
  on 2018-11-29 — 22 days after the election — and the page STILL carried
  the internal "as of 11/07/2018 12:14:30 AM" stamp and "PRELIMINARY
  RESULTS" label, i.e. the two embedded timestamps (crawl date vs. the
  page's own generation date) diverge by three weeks with no county update
  in between. If the county had refreshed this URL toward Final in that
  window (as happened for 2012/2014/2016 at this same county, all of which
  flipped to "Final Results" within days to ~6 weeks), the "as of" stamp
  would have moved; it did not. That is direct proof the 13,522 figure held
  at least from Nov 7 through Nov 29 -- exceeding any prior-year hold window
  found for this county.
- Two secondary routes attempted and NOT used: (1) the probe's
  `Nov2018MediaReleases/` folder (only individual PDF assets like
  `Registration+Deadline.pdf` and per-measure `*v2.pdf` files were
  independently found by the probe; a fresh CDX search this pass for a
  press release stating the election-night total specifically failed —
  broad `matchType=domain` CDX queries on `lakecountyca.gov` for Nov 2018
  repeatedly timed out (`curl` exit 7 / connection error), the exact "broad
  domain queries 504" gotcha in RUNBOOK 7.1; a scoped `Nov2018MediaReleases`
  prefix query on four candidate subdomains returned empty/no-response). (2)
  `result35.htm` on the same system, captured four times Oct 2018-Feb 2019
  with an IDENTICAL digest throughout, was checked and is a DIFFERENT,
  earlier report (June 2018 primary), not usable for the Nov general.
- NOT the 8 p.m. first tranche (no earlier Nov 2018 capture of this URL
  survives; the page self-labels "PRELIMINARY RESULTS" at 12:14:30 AM,
  after full 70/70 precinct reporting).
- Arithmetic: 13,522 / 21,465 = **63.00%**.

```json
{
  "date": "2018-11-06",
  "type": "midterm-general",
  "election_night_ballots": 13522,
  "certified_final": 21465,
  "election_night_pct": 63.0,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20181129033058/http://publicapps.lakecountyca.gov/elections/results/result37.htm",
  "confidence": "primary",
  "note": "PLATEAU = county's own numbered results-report system (publicapps.lakecountyca.gov/elections/results/result37.htm, report #37 = Nov 6 2018 Statewide General per its index37.htm title block, confirmed by CDX). Internal header: 'Election Results as of 11/07/2018 at 12:14:30 AM', explicitly labeled 'PRELIMINARY RESULTS'. 'Completed Precincts: 70 of 70' (100%). 'Total Ballots Cast 13,522 (41.4%)' = Precinct 4,956 + Absentee 8,566. NON-CIRCULAR LEG (RUNBOOK 8, single-capture form): result37.htm was crawled by Wayback exactly ONCE, on 2018-11-29 (22 days after the election) -- and at that later crawl date the page STILL carried the 'as of 11/07/2018 12:14:30 AM' internal stamp and 'PRELIMINARY RESULTS' label unchanged, meaning no update happened at this URL in the intervening 22 days (in contrast to 2012/2014/2016 at this same county, where the equivalent report page DID flip to 'Final Results' within days to ~6 weeks) -- direct proof the count held at least that long. Two secondary routes tried and not usable this pass: the probe's Nov2018MediaReleases/ folder (a fresh CDX search for a press release with the election-night total hit repeated connection timeouts on broad matchType=domain queries against lakecountyca.gov, the RUNBOOK 7.1 'broad domain queries 504' gotcha); result35.htm on the same system (checked, confirmed to be a DIFFERENT, earlier June 2018 primary report, not usable). NOT the 8 PM first tranche (no earlier capture survives; page self-labels 'PRELIMINARY RESULTS' after full 70/70 precinct reporting). Certified final 21,465 voters (CA SoS Voter Participation Statistics by County: 6,049 precinct + 15,416 VBM). Pct = 13,522/21,465 = 63.00%. Lake never adopted epollbook or ASV (n/a both legs, control county) and never adopted VCA, so unlike Napa/San Mateo/Sacramento 2018 (all of which show a SHARP election-night-share DROP that year from the VCA vote-center transition), Lake's 2018 share (63.0%) sits comfortably between its 2016 (53.8%) and its own longer-run range, with no VCA-driven confound to explain."
}
```

**VERIFY.md draft (summary row):** `| 2018 | midterm-general | 13,522 | 21,465 | 63.0% | primary | [link](https://web.archive.org/web/20181129033058/http://publicapps.lakecountyca.gov/elections/results/result37.htm) |`

**VERIFY.md draft (detail bullet):**
- **2018 midterm-general** — night `13,522` / final `21,465` = `63.0%` (primary)
  - numerator: <https://web.archive.org/web/20181129033058/http://publicapps.lakecountyca.gov/elections/results/result37.htm>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "Election Results as of 11/07/2018 at 12:14:30 AM", "PRELIMINARY RESULTS", "Completed Precincts: 70 of 70", "Total Ballots Cast 13,522 41.4%"; note the ONLY Wayback capture of this URL is dated Nov 29 yet still shows the Nov 7 12:14 AM internal stamp unchanged (proof the count held 22+ days).

**plateau_review.json draft:**
```json
{"slug": "lake-ca", "date": "2018-11-06", "verdict": "CONFIRMED", "basis": "self-described past-midnight 'PRELIMINARY RESULTS' timestamp, held unchanged through the only later Wayback crawl of the same URL (22 days on)", "evidence": "result37.htm's sole Wayback capture (2018-11-29) reads 'Election Results as of 11/07/2018 at 12:14:30 AM', 'PRELIMINARY RESULTS', 70/70 precincts, Total Ballots Cast 13,522 -- the crawl-date/internal-timestamp divergence (22 days, no change) is itself the held-count proof"}
```

---

## Item 5 — 2022-11-08 midterm-general

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2022 general —
`https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf`
(fetched to scratch as `lake-ca/sov_2022.pdf`, verified 200/real PDF).
County line as printed: `Lake  80  51,231  37,154  2,416  17,946  20,362
88.13%  54.80%  39.75%` → **Total Voters = 20,362.**

**Election-night plateau — FOUND, TWO independent corroborating sources
(the county's own numbered-report system had moved subdomains AGAIN, to
`publicapps2.lakecountyca.gov`, so this took a wider search than 2012-2018):**

- The `acm.co.lake.ca.us` / `publicapps.lakecountyca.gov` numbered-report
  system used in 2012-2018 no longer existed by 2022 (CDX for both
  subdomains, Nov 2022, returns `[]`). Located the successor via the live
  county site: `www.lakecountyca.gov/Government/Directory/ROV/221108Results.htm`
  (captured 2022-11-09 14:29:00 UTC) is a CivicPlus landing page whose "View
  election results here" link points to
  `https://publicapps2.lakecountyca.gov/elections/results/results221108.html`
  — a Hart-style `Count_HtmlCumulativeReport` export (note the county
  moved from its old Auditor-Controller "acm"/"publicapps" GEMS-era system
  to what looks like a Hart Verity Count export by 2022).
- CDX on `publicapps2.lakecountyca.gov/elections/results/results221108.html`
  (unrestricted date range) shows the EARLIEST capture is 2022-11-18
  11:42:55 UTC — 10 days after the election, no election-night capture
  survives directly. Fetched anyway (gzip `id_` raw, gunzipped per RUNBOOK
  7.1): reads **"County of Lake, California November 8, 2022 General
  Election 11/8/2022 Unofficial Results Registered Voters 7842 of 37165 =
  21.10% Precincts Reporting 80 of 80 = 100.00%"**, and the Governor
  contest subtotal confirms "Voters Ballots Registered Percent 7,842
  37,165 21.10%". **The SAME figure (7,842) recurs unchanged in the NEXT
  capture, 2022-11-30 07:13:56 UTC** (12 days later) — the page held for at
  least 12 days before the CDX digest finally changes (next captures
  2023-02-02 / 2023-11-08 / 2025-02-16 all share one later, different,
  presumably-final digest not fetched this pass, since the numerator
  question is already settled by the news corroboration below).
- **PRIMARY corroboration — RUNBOOK route 6.6, local news, but functionally
  an official-release republication:** Lake County News (lakeconews.com),
  archived via Wayback (`web.archive.org/web/20230131164229/https://lakeconews.com/news/74153-registrar-of-voters-office-issues-preliminary-results-for-tuesday-s-general-election-canvass-process-to-begin`
  — direct curl AND WebFetch of the live lakeconews.com URL both returned
  HTTP 403, so the Wayback copy was used), reports, quoting Registrar Maria
  Valadez's office directly: **"By 1 a.m. Wednesday, Valadez's office had
  issued the last preliminary ballot count of the night, which included the
  election night initial count for all 80 Lake County precincts... The
  preliminary count included 7,842 ballots, or 21.2% of Lake County's
  37,165 registered voters."** This independently confirms (a) 7,842 IS the
  number from the LAST report of election night (1 a.m. Nov 9, i.e. the
  runbook's plateau definition exactly), (b) all 80/80 precincts were in,
  and (c) the article also explains WHY no earlier capture exists: "Challenges
  with the county's website led to results not being posted online until
  late Tuesday night" — the results site itself was down/delayed for part
  of election night, consistent with Lake's documented reputation (CalVoter
  profile cited in the tech-record item) as an unusually slow-reporting
  county.
- This is a strong CONFIRMED case: self-described as the LAST election-night
  report by a direct, on-the-record registrar-office quote (not just an
  internal page timestamp), PLUS the non-circular leg of the number holding
  unchanged across two independent Wayback captures 12+ days apart.
- Arithmetic: 7,842 / 20,362 = **38.51%**. Markedly LOWER than Lake's own
  2012/2014/2016/2018 range (53.8%-70.2%) — the news article's own text
  attributes this to a slow county-website rollout that night, not a tech
  adoption (Lake never adopted epollbook/ASV/VCA); worth flagging as a
  genuine within-county outlier for the control-county comparison, not a
  research error.

```json
{
  "date": "2022-11-08",
  "type": "midterm-general",
  "election_night_ballots": 7842,
  "certified_final": 20362,
  "election_night_pct": 38.51,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20230131164229/https://lakeconews.com/news/74153-registrar-of-voters-office-issues-preliminary-results-for-tuesday-s-general-election-canvass-process-to-begin",
  "confidence": "primary",
  "note": "PLATEAU = the LAST election-night preliminary report, per a Lake County News article (archived copy used; live lakeconews.com blocks both curl and WebFetch with HTTP 403) quoting the Registrar of Voters' office directly: 'By 1 a.m. Wednesday, Valadez's office had issued the last preliminary ballot count of the night, which included the election night initial count for all 80 Lake County precincts... The preliminary count included 7,842 ballots, or 21.2% of Lake County's 37,165 registered voters.' Independently corroborated by the county's own results page (publicapps2.lakecountyca.gov/elections/results/results221108.html, the successor to the 2012-2018 acm.co.lake.ca.us/publicapps.lakecountyca.gov numbered-report system): its earliest Wayback capture (2022-11-18) already shows 'Registered Voters 7842 of 37165 = 21.10%, Precincts Reporting 80 of 80 = 100.00%', and the SAME 7,842 figure recurs unchanged in the next capture (2022-11-30, 12 days later) -- non-circular held-count evidence per RUNBOOK 8. No earlier (election-night-dated) Wayback capture of this specific URL survives; the news article explains why direct county reporting was itself delayed that night ('Challenges with the county's website led to results not being posted online until late Tuesday night'). NOT a later canvass update (the article is explicit this is the FINAL/LAST preliminary count of election night itself, and both Wayback captures used are corroborating, not the sourced value). Certified final 20,362 voters (CA SoS Voter Participation Statistics by County: 2,416 precinct + 17,946 VBM). Pct = 7,842/20,362 = 38.51% -- markedly lower than Lake's own 2012 (70.18%), 2014 (69.72%), 2016 (53.75%), 2018 (63.00%); the news source itself attributes the shortfall to website/reporting delays that night, and Lake's own CalVoter profile (cited in the tech-record item) independently documents the county as an unusually slow reporter, not a tech-adoption confound (Lake never adopted epollbook/ASV/VCA, n/a both legs, control county)."
}
```

**VERIFY.md draft (summary row):** `| 2022 | midterm-general | 7,842 | 20,362 | 38.5% | primary | [link](https://web.archive.org/web/20230131164229/https://lakeconews.com/news/74153-registrar-of-voters-office-issues-preliminary-results-for-tuesday-s-general-election-canvass-process-to-begin) |`

**VERIFY.md draft (detail bullet):**
- **2022 midterm-general** — night `7,842` / final `20,362` = `38.5%` (primary)
  - numerator: <https://web.archive.org/web/20230131164229/https://lakeconews.com/news/74153-registrar-of-voters-office-issues-preliminary-results-for-tuesday-s-general-election-canvass-process-to-begin>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "By 1 a.m. Wednesday, Valadez's office had issued the last preliminary ballot count of the night... The preliminary count included 7,842 ballots, or 21.2% of Lake County's 37,165 registered voters"; corroborating county page (publicapps2.lakecountyca.gov/elections/results/results221108.html) shows the same 7,842 figure unchanged across its 2022-11-18 and 2022-11-30 Wayback captures.

**plateau_review.json draft:**
```json
{"slug": "lake-ca", "date": "2022-11-08", "verdict": "CONFIRMED", "basis": "on-the-record registrar-office quote naming the number as the last preliminary count of election night, plus the number holding unchanged across two Wayback captures of the county's own results page 12+ days apart", "evidence": "Lake County News (archived): 'By 1 a.m. Wednesday, Valadez's office had issued the last preliminary ballot count of the night... 7,842 ballots, or 21.2% of Lake County's 37,165 registered voters'; publicapps2.lakecountyca.gov/elections/results/results221108.html shows 'Registered Voters 7842 of 37165 = 21.10%, Precincts Reporting 80 of 80' identically in both its 2022-11-18 and 2022-11-30 captures"}
```

---

## Item 6 — 2024-11-05 presidential-general

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2024 general —
`https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf`
(fetched to scratch as `lake-ca/sov_2024.pdf`, verified 200/real PDF).
County line as printed: `Lake  48  51,197  37,975  3,577  23,550  27,127
86.81%  71.43%  52.99%` → **Total Voters = 27,127.**

**Election-night plateau — FOUND, same news-corroboration route as 2022
(the county's own `publicapps2.lakecountyca.gov/elections/results/results241105.html`
page's earliest Wayback capture is already 12 days post-election and
CONTAMINATED by partial canvass, so it was checked and rejected as the
numerator source):**

- CDX on `results241105.html` shows earliest capture 2024-11-17 03:42:05
  UTC — fetched (gzip `id_`, gunzipped) and reads "Run Date 11/14/2024 …
  General Election 11/5/2024 Unofficial Results Registered Voters 8,641 of
  37,915 = 22.79%, Precincts Reporting 48 of 48". **This 8,641 figure is
  HIGHER than the true election-night count** (confirmed below) and is
  explicitly dated "Run Date 11/14/2024" — 8 days after the election, i.e.
  already a partial-canvass update, NOT the election-night plateau. REJECTED
  as the numerator for this reason (documented here per RUNBOOK 5.1 so a
  future pass doesn't re-use it by mistake).
- **Numerator actually used — Lake County News, route 6.6 (functionally an
  official-release republication, same outlet/pattern independently
  confirmed reliable for this county in 2022):** "Official canvass
  underway; thousands of ballots still to be counted"
  (`lakeconews.com/news/80085-official-canvass-underway-thousands-of-ballots-still-to-be-counted`;
  live URL 403s to both curl and WebFetch, archived copy used —
  `web.archive.org/web/20241210113951/https://lakeconews.com/news/80085-...`)
  states: **"The Lake County Registrar of Voters Office has issued
  preliminary election results for the 48 precincts and the vote by mail
  ballots that were counted as of early Wednesday morning. Out of 37,915
  registered voters, only 7,960 ballots, or 20.99%, have been counted."**
  A companion WebSearch-indexed snippet (from a second lakeconews.com
  article, "Most Lake County races too close to call…", `news/80080`,
  which itself has NO surviving Wayback capture — CDX for both
  `lakeconews.com/news/80080*` and `www.lakeconews.com/news/80080*`
  returned `[]`) sharpens the timing: **"By 4 a.m. on November 6, 2024,
  initial counts of the county's 48 precincts had been completed"** — i.e.
  the same overnight-report pattern independently confirmed for this county
  in 2022 (there: 1 a.m. Wednesday after a Tuesday election; here: 4 a.m.
  Wednesday after a Tuesday election), all 48/48 precincts in, immediately
  followed by "thousands more ballots are expected to be counted" during
  the canvass — i.e. this is explicitly the pre-canvass plateau, not a
  partial in-progress count.
- Arithmetic: 7,960 / 27,127 = **29.34%**. This is Lake's LOWEST
  election-night share across all six elections in this dossier (below even
  2022's 38.51%), continuing a clear downward trend from the 2012-2018 range
  (53.75%-70.18%) through 2022 and 2024. Lake never adopted epollbook, ASV,
  or VCA in this window (n/a both tech legs, control county) — the decline
  tracks the county's own documented slow/understaffed reporting reputation
  (CalVoter profile, tech-record item) getting worse, not a tech-adoption
  effect, and should be read as a genuine within-county secular trend for
  the control-county comparison rather than a research artifact.

```json
{
  "date": "2024-11-05",
  "type": "presidential-general",
  "election_night_ballots": 7960,
  "certified_final": 27127,
  "election_night_pct": 29.34,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20241210113951/https://lakeconews.com/news/80085-official-canvass-underway-thousands-of-ballots-still-to-be-counted",
  "confidence": "primary",
  "note": "PLATEAU = the last election-night preliminary report, per Lake County News ('Official canvass underway; thousands of ballots still to be counted', archived copy used; live lakeconews.com blocks both curl and WebFetch with HTTP 403): 'The Lake County Registrar of Voters Office has issued preliminary election results for the 48 precincts and the vote by mail ballots that were counted as of early Wednesday morning. Out of 37,915 registered voters, only 7,960 ballots, or 20.99%, have been counted.' A second lakeconews.com article (news/80080, no surviving Wayback capture -- CDX empty for both lakeconews.com and www.lakeconews.com prefixes) is quoted via WebSearch snippet sharpening the timing: 'By 4 a.m. on November 6, 2024, initial counts of the county's 48 precincts had been completed' -- the same overnight-report pattern (1 a.m. in 2022, 4 a.m. here) independently confirmed for this county's reporting cadence. REJECTED alternative: the county's own publicapps2.lakecountyca.gov/elections/results/results241105.html page's earliest Wayback capture (2024-11-17) already reads 'Run Date 11/14/2024 ... Registered Voters 8,641 of 37,915 = 22.79%' -- 8 days post-election and already a partial-canvass update (681 ballots higher than the true election-night 7,960), explicitly NOT used as the numerator. Certified final 27,127 voters (CA SoS Voter Participation Statistics by County: 3,577 precinct + 23,550 VBM). Pct = 7,960/27,127 = 29.34% -- Lake's lowest election-night share of all six elections in this dossier, continuing a downward trend from 2012-2018 (53.75%-70.18%) through 2022 (38.51%); the news source itself frames this as ongoing capacity/backlog issues, consistent with Lake's own CalVoter 'slowest elections department' profile (tech-record item), not a tech-adoption confound (Lake never adopted epollbook/ASV/VCA, n/a both legs, control county). (2020 deliberately excluded as a COVID universal-VBM outlier.)"
}
```

**VERIFY.md draft (summary row):** `| 2024 | presidential-general | 7,960 | 27,127 | 29.3% | primary | [link](https://web.archive.org/web/20241210113951/https://lakeconews.com/news/80085-official-canvass-underway-thousands-of-ballots-still-to-be-counted) |`

**VERIFY.md draft (detail bullet):**
- **2024 presidential-general** — night `7,960` / final `27,127` = `29.3%` (primary)
  - numerator: <https://web.archive.org/web/20241210113951/https://lakeconews.com/news/80085-official-canvass-underway-thousands-of-ballots-still-to-be-counted>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "preliminary election results for the 48 precincts and the vote by mail ballots that were counted as of early Wednesday morning. Out of 37,915 registered voters, only 7,960 ballots, or 20.99%, have been counted"; do NOT confuse with the county's own results241105.html page, whose earliest surviving capture (Nov 17) already shows a higher, partial-canvass 8,641 dated "Run Date 11/14/2024".

**plateau_review.json draft:**
```json
{"slug": "lake-ca", "date": "2024-11-05", "verdict": "CONFIRMED", "basis": "on-the-record news report naming the number as the election-night preliminary count for all precincts, with an independent second-article snippet pinning the report to 4 a.m. the morning after election day; the alternative county-page capture was checked and explicitly rejected as already-canvass-contaminated", "evidence": "Lake County News (archived): 'preliminary election results for the 48 precincts ... as of early Wednesday morning ... 7,960 ballots, or 20.99% ... have been counted'; companion article snippet: 'By 4 a.m. on November 6, 2024, initial counts of the county's 48 precincts had been completed'; results241105.html's earliest Wayback capture (2024-11-17, Run Date 11/14/2024) shows a higher 8,641 and was rejected as post-election-night"}
```

---

## Item 0 — tech record (never-adopter evidence, e-pollbooks + ASV)

Reused from `data/research/county-tech/ca_adoption_census.json` (Lake row,
status "never", confidence "low") — Lake is NOT itself a file in
`data/research/county-tech/` yet (only the census row exists; no
`lake-ca.json` was found in that directory as of this pass). Below is a
`lake-ca.json`-shaped draft record per the schema in
`data/research/county-tech/napa-ca.json`, built from the census row's
sources plus one new corroborating check.

```json
{
  "jurisdiction": "Lake County",
  "state": "CA",
  "tech": [
    {
      "type": "epollbook",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf",
      "confidence": "high",
      "note": "CA SoS 'Voting Technologies in Use by County' snapshots show 'Do not use' for Electronic Pollbook continuously across THREE independent snapshots (May 2022, Sept 2024, Oct 2025). EAVS (Election Administration and Voting Survey) reports electronic-poll-book use as False in all four available editions (2016, 2018, 2022, 2024) per https://www.eac.gov/research-and-data/datasets-codebooks-and-surveys. Lake is NOT a Voter's Choice Act (VCA) vote-center county (absent from the SoS VCA Vote Center Usage Summary county list, https://www.sos.ca.gov/voters-choice-act/vca-participating-counties) -- consistent with never adopting an e-pollbook, since CA's e-pollbook rollout has been almost entirely VCA-vote-center-driven. Four-source consistent never-adopter signal (three SoS snapshots + EAVS + absence from VCA list). Locating query: CA SoS 'Voting Technologies in Use by County' PDF, county-vsys oversight page; EAC EAVS datasets page; SoS VCA participating-counties page."
    },
    {
      "type": "asv",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://calvoter.org/content/%E2%80%98why-do-we-need-rush%E2%80%99-california%E2%80%99s-lake-county-may-have-nation%E2%80%99s-slowest-elections",
      "confidence": "low",
      "note": "CalVoter's ballot-processing profile of Lake County ('Why do we need to rush? California's Lake County may have the nation's slowest elections department') describes vote-by-mail signatures being 'examined by staff' with no automated signature-matching equipment named, in the context of an understaffed/slow elections office. Direct fetch of the CalVoter page was blocked by a bot wall (403 both in the original census pass and re-checked in this pass); this rests on a WebSearch-indexed snippet only, not a full primary-source read. Lake's own Signature Verification Statement PDF (https://lakecountyca.gov/DocumentCenter/View/3378/Signature-Verification-Statement-and-Instructions-PDF) is a generic cure-form that does not describe the underlying match method (re-checked this pass: still a bare fillable cure form, no vendor/software language). Lake does not appear in the Stanford Law School 'Signature Verification and Mail Ballots' (May 2020) Appendix III county survey table (33 counties interviewed; Lake not among them) -- https://law.stanford.edu/wp-content/uploads/2020/04/SLS_Signature_Verification_Report-5-15-20-FINAL.pdf, re-checked this pass, confirmed absent via pdftotext -layout search for 'Lake County'. NEW this pass: Lake's current Registrar of Voters page (https://elections.lakecountyca.gov/818/Registrar-of-Voters) and its Election Administration Plan were checked for an ASV vendor name; none found (page is a general contacts/services page, no EAP document linked as of this pass; Lake does not have a VCA EAP because it never adopted the VCA). Positive-support standard only weakly met (search-snippet only for the CalVoter quote, small rural county with essentially no independent press coverage of ballot-processing internals). Confidence stays LOW, matching the census row. Locating queries: 'Lake County California elections vote by mail signature verification staff compare'; site:calvoter.org Lake County ballot processing (403 blocked); direct curl of elections.lakecountyca.gov/818/Registrar-of-Voters (200, no ASV content); pdftotext search of Stanford SLS report Appendix III for 'Lake County' (not found)."
    },
    {
      "type": "sign-scan-go",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://www.sos.ca.gov/voters-choice-act/vca-participating-counties",
      "confidence": "medium",
      "note": "Sign-Scan-and-Go (AB 626 in-vote-center mail-ballot verify+scan) is a VCA-vote-center-only program (piloted at Placer). Lake has never adopted the VCA (absent from the SoS VCA participating-counties list), so it structurally cannot have Sign-Scan-and-Go. Absence-of-evidence inference, consistent with the epollbook finding."
    },
    {
      "type": "vote-center",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://www.sos.ca.gov/voters-choice-act/vca-participating-counties",
      "confidence": "high",
      "note": "Lake does not appear on the CA SoS Voter's Choice Act participating-counties list (checked this pass). Lake runs traditional neighborhood-precinct polling places plus vote-by-mail, not the VCA all-mail/vote-center model. This is the structural reason Lake is a clean control county: no VCA-driven confound coincides with its (non-)adoption of epollbook/ASV, unlike Napa/Sacramento/Madera/Nevada/San Mateo where VCA adoption and epollbook adoption happened in the same year."
    }
  ],
  "metrics": [],
  "notes": "TECH SUMMARY: Lake County is a clean 'never adopted' control county for BOTH e-pollbooks and ASV through 2024 -- never joined the VCA (no vote-center confound), SoS voting-tech snapshots and EAVS both show epollbook 'Do not use'/False continuously 2016-2025, and the one ASV-relevant source found (CalVoter profile) describes staff-only signature examination, though that specific source is snippet-only (403-blocked direct fetch) and hence LOW confidence for the ASV leg specifically (matches the census row's assessment). Both election-night route dimensions bear on this: NOT on Clarity (probe-confirmed 404 at results.enr.clarityelections.com/CA/Lake/), results live on a separate publicapps.lakecountyca.gov subdomain, and the county keeps a per-election media-release folder (Nov2018MediaReleases/ confirmed in the probe) -- extended in items 1-6 below."
}
```

---
