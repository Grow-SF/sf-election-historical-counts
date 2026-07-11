# San Bernardino County, CA — statewide-PRIMARY election-night dossier

Scope: 2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05 (pre-e-pollbook adoption
2020), 2022-06-07, 2024-03-05 (post-adoption). Read-only research scaffold for
`data/research/election-night/san-bernardino-ca.json`; this file is NOT that
JSON and is not committed. Methodology: RUNBOOK.md section 1 (plateau, not
first tranche), 5 (null/ceiling conventions), 6 (source routes), 7 (Wayback
gotchas), 8 (plateau evidence standard).

County results-page history (established by the Nov-generals research
already in the repo): pre-2019 San Bernardino served a JS-iframe results
page at `www.sbcounty.gov/rov/elections/Results/<YYYYMMDD>/content/results.aspx`
with NO downloadable report PDF/XLSX and NO morning-after "semi-final
results" registrar press release (the news archive at
elections.sbcounty.gov/news/ is public-notices/certifications only, 2011-2026).
From 2019 on, downloadable `ElectionSummaryReportRPT.pdf`/`.xlsx` exist on
`results.rov.sbcounty.gov`, and the 2022/2024 pattern used
`sbcountyelections.com/Elections/<year>/<mmdd>/...` with an archived
"Results Posting Schedule" page. This dossier retries each primary against
that established topology rather than assuming the generals' dead ends
apply unchanged.

---

## Denominators (CA SoS Statement of Vote, Voter Participation Statistics by County)

All six located and pdftotext-extracted (cache: scratch `sb-primaries/sov*.txt`).
Column order confirmed from header rows: Precincts | Eligible to Register |
Registered Voters | Precinct Voters | Vote-By-Mail Voters | **Total Voters** |
Percent VBM | Turnout/Registered | Turnout/Eligible.

| date | type | SoV URL | Registered | Total Voters (denominator) | Turnout/Reg |
|---|---|---|---:|---:|---:|
| 2012-06-05 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/2012-complete-sov.pdf | 815,087 | 193,517 | 23.74% |
| 2014-06-03 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf | 851,326 | 160,742 | 18.88% |
| 2016-06-07 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf | 784,130 | 339,754 | 43.33% |
| 2018-06-05 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf | 901,081 | 281,045 | 31.19% |
| 2022-06-07 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf | 1,138,004 | 257,580 | 22.63% |
| 2024-03-05 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf | 1,166,450 | 305,853 | 26.22% |

Notes on URL anatomy (differs from generals, and differs year to year even
within primaries — record exact path per year, do not assume a pattern):
- 2012 primary has NO standalone `03-voter-participation-stats-by-county.pdf`
  (403 on `/sov/2012-primary/03-...` and `/sov/2012-primary/pdf/03-...`);
  the only voter-participation table found is inside the 127-page
  `2012-complete-sov.pdf` (table titled "VOTER PARTICIPATION STATISTICS BY
  COUNTY", page 2 internal), San Bernardino row confirmed:
  `1,567  1,253,049  815,087  70,533  122,984  193,517  63.55%  23.74%  15.44%`.
- 2014 uses the misspelled `pdf/03-voter-particpiation-stats-by-county.pdf`
  (same as the Nov-2014 general).
- 2016 primary lives at `/sov/2016-primary/03-voter-participation-stats-by-county.pdf`
  (root of the primary dir, NO `sov/` or `pdf/` subsegment — unlike the 2016
  GENERAL which used `/sov/2016-general/sov/03-...`).
- 2018/2022/2024 all use `/sov/<year>-primary/sov/03-voter-participation-stats-by-county.pdf`
  (same convention as their respective generals).

---

## Item 1 of 6: 2012-06-05 (Presidential Primary)

**Denominator**: 193,517 (CA SoS SoV, `2012-complete-sov.pdf`, San Bernardino row:
`1,567 1,253,049 815,087 70,533 122,984 193,517 63.55% 23.74% 15.44%`).

**Numerator research**: pre-2019 site topology differs from what the existing
generals notes assumed. Live CDX enumeration (`http://web.archive.org/rov/current_elections/060512/`,
86 hits under the parent prefix) surfaces the ACTUAL 2012 results directory:
`www.sbcounty.gov/rov/current_elections/060512/ElectionResults/Includes/Election_Results.htm`
(the general-election notes' assumed path `rov/elections/Results/<date>/content/results.aspx`
did not exist yet in 2012 -- that came later). Earliest and ONLY capture of this
directory: `20120607035454` (Wed June 6, 2012 20:54 PDT).

Fetched and rendered (raw HTML table, no JS needed for this era): internal page
timestamp `Last Updated: June 6, 2012 4:46 PM`, Total turnout **183,726**
(Precinct 65,405 + VBM 118,321), 22.54% of 815,087 registered. The paired
fragment `Includes/MessageDNN.htm` (same crawl) reads verbatim **"Updated
Semi-Official Results"**, and `Includes/NextUpdateTimeDNN.htm` reads **"Next
Update: June 7, 2012 5:00 p.m."** -- i.e. this capture is mid-canvass (a day
after Election Day, Wednesday afternoon, with the canvass continuing into
Thursday), not an election-night report. Confirmed by calibration:
183,726 / 193,517 certified = **94.94%**, far above any plausible election-night
share (SF calibration range ~51-71%) and consistent with a multi-day
canvass state, matching the pattern already documented for this county's Nov
generals (2014's 95.5%, 2018's post-canvass captures).

No earlier Wayback capture exists (checked: CDX prefix on the whole
`060512/` directory, 86 rows, earliest timestamp is this same June 6 crawl
session). Checked `elections.sbcounty.gov/elections/2012/0605/results/`
(the modern re-platformed URL for this same election) -- only 2 captures,
both 2024/2025 (i.e., crawled 12+ years later showing the certified final,
`Last Updated: June 22, 2012 4:01PM` -- itself already the certified-final
snapshot, of no election-night value). Checked
`elections.sbcounty.gov/news/` CDX for June 2012 -- zero captures (the
domain did not exist yet at that date; consistent with the established
"no morning-after semi-final press release" finding for this registrar).

**Verdict: NULL per definition.** No election-night-window capture survives;
the only artifact is a labeled "Updated Semi-Official Results" Wednesday-
afternoon canvass state, examined and rejected.

**Draft row:**
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 193517,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/2012-complete-sov.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 193,517 ballots cast (CA SoS Statement of Vote, 2012-complete-sov.pdf, Voter Participation Statistics by County: precinct 70,533 + VBM 122,984; 23.74% of 815,087 registered). Pre-adoption (precinct-based; e-pollbooks not until 2020). Election-night PLATEAU not sourceable: the 2012 primary's live results lived at www.sbcounty.gov/rov/current_elections/060512/ElectionResults/Includes/Election_Results.htm (a different pre-2019 site topology than the Nov-2012 general's Results/<date>/content/results.aspx path). Its ONLY Wayback capture (20120607035454, Wed June 6 2012 20:54 PDT) shows internal timestamp 'Last Updated: June 6, 2012 4:46 PM' with Total turnout 183,726 (22.54% of registered) -- but the paired fragment Includes/MessageDNN.htm reads 'Updated Semi-Official Results' and Includes/NextUpdateTimeDNN.htm reads 'Next Update: June 7, 2012 5:00 p.m.', proving this is a Wednesday-afternoon multi-day-canvass state, not an election-night report (183,726/193,517 = 94.94% of certified final, far above SF's ~51-71% calibration range for election-night shares). No earlier capture exists (checked full CDX prefix of the results directory, 86 rows, earliest is this same crawl). No morning-after 'semi-final results' registrar press release exists (elections.sbcounty.gov/news/ CDX for June 2012 = 0 captures; domain did not yet exist). Null per definition (the 183,726 Wednesday canvass figure is examined and rejected, not substituted). snapshot 20120607035454 (post-night, not usable)."
}
```

**VERIFY.md draft line:** `| 2012 | presidential-primary | — | 193,517 | — | none | — (not sourceable) |`

**plateau_review.json draft:** N/A (null row; no verdict entry needed per existing convention for none-confidence rows -- confirm against existing null rows in plateau_review.json before merge).

---

## Item 2 of 6: 2014-06-03 (Statewide Direct Primary)

**Denominator**: 160,742 (CA SoS SoV, `2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf`
[misspelling intact], San Bernardino row:
`1,662 1,269,053 851,326 47,896 112,846 160,742 70.20% 18.88% 12.67%`).

**Numerator research**: by 2014 the site had moved to the "content/results.aspx"
topology (`www.sbcounty.gov/rov/elections/results/20140603/content/results.aspx`,
77 CDX hits under the directory prefix). All captures cluster around
Fri-Sat June 6-7, 2014 (3-4 days after the Tue June 3 election); earliest is
`default.html` at `20140606072618` (Fri June 6, 00:26 PDT). Fetched
`content/results.aspx` (capture `20140607202905`, Sat June 7, 13:29 PDT):
internal timestamp `Last Updated: June 6, 2014 3:47 PM`, Total **157,067**
(18.45% of 851,326 registered). Paired `content/message.aspx` (same crawl)
reads verbatim **"06/06/2014 4:00 p.m. Posting of Unofficial Results"** --
a Friday-afternoon canvass posting, 3 days after Election Day. Calibration:
157,067 / 160,742 certified = **97.71%** of final, confirming this is a
near-complete multi-day canvass state, not election night.

No capture exists in the actual election-night window (Tue June 3 evening
into Wed June 4). Checked the whole `20140603/` directory CDX (77 rows);
nothing between Election Day and the Friday cluster. No registrar
"semi-final results" press release found (consistent with the established
pattern for this county pre-2019).

**Verdict: NULL per definition.** Only a Friday post-canvass capture
survives, explicitly labeled as an "Unofficial Results" posting continuing
the canvass, not an election-night report; examined and rejected.

**Draft row:**
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 160742,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 160,742 ballots cast (CA SoS SoV; precinct 47,896 + VBM 112,846; 18.88% of 851,326 registered). Pre-adoption, precinct-based. Election-night PLATEAU not sourceable: the live results page (www.sbcounty.gov/rov/elections/results/20140603/content/results.aspx) has no Election-Night Wayback capture; the earliest is default.html at 20140606072618 (Fri June 6 2014 00:26 PDT, 3 days post-election). The fetched content/results.aspx (capture 20140607202905, Sat June 7 13:29 PDT) shows internal timestamp 'Last Updated: June 6, 2014 3:47 PM', Total 157,067 (18.45% of registered) -- and the paired content/message.aspx reads '06/06/2014 4:00 p.m. Posting of Unofficial Results', confirming a Friday-afternoon canvass update, not election night (157,067/160,742 = 97.71% of certified final, far above any plausible election-night share). No earlier capture exists in the 77-row CDX prefix of the results directory. No morning-after 'semi-final results' registrar press release exists (consistent with the established pattern for this county's pre-2019 elections). Null per definition (the 157,067 Friday canvass figure is examined and rejected). snapshot 20140607202905 (post-night, not usable)."
}
```

**VERIFY.md draft line:** `| 2014 | statewide-primary | — | 160,742 | — | none | — (not sourceable) |`

---

## Item 3 of 6: 2016-06-07 (Presidential Primary)

**Denominator**: 339,754 (CA SoS SoV, `2016-primary/03-voter-participation-stats-by-county.pdf`
[note: NO `sov/` or `pdf/` subsegment, unlike the 2016 general], San Bernardino row:
`1,772 1,304,484 784,130 139,426 200,328 339,754 58.96% 43.33% 26.05%`).

**Numerator research**: CDX on `www.sbcounty.gov/rov/elections/Results/20160607/`
returns only 4 content hits, ALL from a single crawl session `20160607150236`-
`20160607150410` (Tue June 7, 2016 08:02-08:04 AM PDT -- i.e. election
MORNING, before polls even opened for the day's voting, let alone before
the 8:05 p.m. first posting). Fetched `content/results.aspx`: internal
timestamp `Last Updated: May 24, 2016 5:10 AM` (stale pre-election data).
Fetched `content/message.aspx`: reads verbatim **"This site will provide
election results beginning on Tuesday, June 7, 2016. The first posting of
the Unofficial Election Night Results will take place at 8:05 p.m."** --
confirms this capture predates all election-night reporting.

The only other capture in the directory is `resultsIndex.html` at
`20160611091425` (Sat June 11, 4 days post-election) -- a navigation-frame
fragment with no embedded ballot totals (checked; no `results.aspx` capture
exists at or near that date to pair with it).

**Verdict: NULL per definition.** Zero numeric captures exist anywhere in
the election-night-to-canvass window; the only content is a pre-election
placeholder page.

**Draft row:**
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 339754,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 339,754 ballots cast (CA SoS SoV; precinct 139,426 + VBM 200,328; 43.33% of 784,130 registered). Pre-adoption, precinct-based. Election-night PLATEAU not sourceable: CDX of www.sbcounty.gov/rov/elections/Results/20160607/ returns only 4 content hits, all from a single crawl at 20160607150236-410 (Tue June 7 2016 08:02-08:04 AM PDT, i.e. BEFORE polls opened / before the scheduled 8:05 p.m. first posting). content/results.aspx at that capture shows stale internal timestamp 'Last Updated: May 24, 2016 5:10 AM' (pre-election data), and content/message.aspx reads verbatim 'This site will provide election results beginning on Tuesday, June 7, 2016. The first posting of the Unofficial Election Night Results will take place at 8:05 p.m.' The only other capture in the directory (resultsIndex.html, 20160611091425, Sat June 11, 4 days post-election) is a navigation-frame fragment carrying no ballot totals, with no paired results.aspx capture near that date. No numeric election-night or canvass capture exists anywhere in this directory. No morning-after registrar press release found. Null per definition (never substitute a different report). snapshot none usable (only pre-election placeholder found)."
}
```

**VERIFY.md draft line:** `| 2016 | presidential-primary | — | 339,754 | — | none | — (not sourceable) |`

---

## Item 4 of 6: 2018-06-05 (Statewide Direct Primary)

**Denominator**: 281,045 (CA SoS SoV, `2018-primary/sov/03-voter-participation-stats-by-county.pdf`,
San Bernardino row:
`1,856 1,325,471 901,081 93,181 187,864 281,045 66.84% 31.19% 21.20%`).

**Numerator research**: CDX on `www.sbcounty.gov/rov/elections/results/20180605/`
returns 5 content hits, all from ONE crawl session `20180606065244`
(Tue June 5, 2018 23:52 PDT -- genuinely inside election night). Fetched
`content/results.aspx`: internal timestamp `Last Updated: June 5, 2018 9:51
PM`, Total **112,948** (Precinct 14,987 + VBM 97,961), 12.53% of 902,244
registered (live-page registered count; SoV final registered is 901,081).
Paired `content/message.aspx` reads verbatim **"10:00 p.m. Posting of
Unofficial Election Night Results"** and `content/nextUpdateTime.aspx`
reads **"Next Update: June 6, 2018 12:00 a.m."** -- i.e. this capture is
explicitly labeled as the 10 p.m. posting (an early tranche), with a
midnight update still to come. This is NOT the last report of the night.
112,948 / 281,045 certified = 40.19%, consistent with an early tranche, well
below what a genuine plateau would show.

No capture exists after this single crawl (checked the full 12-row CDX for
the directory); the scheduled midnight-and-later reports, and any "Final
Unofficial" posting, were never archived. No registrar press release found.

**Verdict: NULL per definition.** Only the self-labeled "10:00 p.m."
first/early tranche survives; the plateau (whatever later report followed)
is unarchived.

**Draft row:**
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 281045,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 281,045 ballots cast (CA SoS SoV; precinct 93,181 + VBM 187,864; 31.19% of 901,081 registered). Pre-adoption, precinct-based. Election-night capture DOES exist but is explicitly the FIRST TRANCHE, not the plateau: CDX of www.sbcounty.gov/rov/elections/results/20180605/ returns 5 content hits from one crawl at 20180606065244 (Tue June 5 2018 23:52 PDT). content/results.aspx shows 'Last Updated: June 5, 2018 9:51 PM', Total 112,948 (12.53% of registered) -- but content/message.aspx reads verbatim '10:00 p.m. Posting of Unofficial Election Night Results' and content/nextUpdateTime.aspx reads 'Next Update: June 6, 2018 12:00 a.m.', proving this is an early-evening tranche with a midnight update still pending, not the last-of-night report (112,948/281,045 = 40.19% of certified, consistent with an early tranche per the runbook's ~2x-undercount calibration warning). No later capture exists in the 12-row directory CDX; the midnight/2am/'Final Unofficial' postings implied by other years' schedules were never archived for this election. No morning-after registrar press release found. Null per definition (the 10 p.m. tranche is examined and explicitly rejected as the classic first-tranche trap, not substituted for the plateau). snapshot 20180606065244 (10 p.m. first/early tranche, not the plateau)."
}
```

**VERIFY.md draft line:** `| 2018 | statewide-primary | — | 281,045 | — | none | — (not sourceable) |`

---

## Item 5 of 6: 2022-06-07 (Statewide Direct Primary) -- SOURCED, CONFIRMED plateau

**Denominator**: 257,580 (CA SoS SoV, `2022-primary/sov/03-voter-participation-stats-by-county.pdf`,
San Bernardino row:
`2,030 1,471,817 1,138,004 30,919 226,661 257,580 88.00% 22.63% 17.50%`).

**Numerator research**: the archived Results Posting Schedule page
(`sbcountyelections.com/Elections/2022/0607/ResultSchedule`, capture
`20220608165638`) states the full election-night cadence for June 7, 2022:
8:30 p.m. first posting -> 10 p.m. -> 12 a.m. -> 2:30 a.m. -> **3:15 a.m.
Final Unofficial Election Night Results** -> next posting Wed 4 p.m.
(canvass resumes).

The live results wrapper (`sbcountyelections.com/Elections/2022/0607/Results/`)
embeds `rovelectionresults.sbcounty.gov/Results/20220607/`. Wayback's only
capture of that embed (`20220608034508`, Tue 8:45 PM PDT) is explicitly
labeled "**First Posting of Unofficial Election Night Results**" with "Next
Update: 10:00 p.m." -- the classic first tranche, correctly NOT used.

The downloadable report file
`rovelectionresults.sbcounty.gov/uploads/rov/elections/results/20220607/_content/ElectionSummaryReportRPT.pdf`
has a distinct capture at `20220608165638` (Wed June 8, 2022 09:56 AM PDT,
digest `SHYMP5RFLCA2IXE6YFMMJVE3FA3SX4BY`, unique among all captures of this
URL) -- squarely inside the 3:15 a.m.-4 p.m. plateau window. Its content:

```
Election Summary Report / San Bernardino County / Statewide Direct Primary
June 7, 2022 / Summary #5
(report internal timestamp: 6/8/2022 2:56:29 AM)
Precincts Reported: 2,030 of 2,030 (100.00%)
Voters Cast: 119,998 of 1,138,019 (10.54%)
Cards Cast: 239,893
```

100% precincts reporting + report ordinal "Summary #5" matching the
schedule's 5th (Final) posting + internal generation timestamp 2:56:29 AM
(inside the 2:30 a.m.-3:15 a.m. window, consistent with report-generation
lag before the 3:15 a.m. posting label) together satisfy RUNBOOK 8's
"self-describes as end-of-night" leg. The independent non-circular leg: the
**next** capture of the same PDF (`20220701212908`, June 30, "**Summary
#15**") shows **257,004** voters cast (near-certified, 22.58%) -- a large,
un-ambiguous jump from 119,998, proving Summary #5 was NOT itself a
canvass-advanced state (it held at a materially lower count for weeks) and
that the true canvass only caught up much later. This is the Clarity-style
"later capture, materially different, proves the cited version was a real
earlier checkpoint" bracket described in RUNBOOK 7.2/8.

Arithmetic: 119,998 / 257,580 = **46.59%**.

**Verdict: CONFIRMED.** Basis: county's own posting schedule brackets the
capture (3:15 a.m. Final EN posting, next update 4 p.m.) AND a materially
higher later-capture (Summary #15, +137,006 ballots) proves it was not
already canvass-advanced.

**Draft row:**
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 119998,
  "certified_final": 257580,
  "election_night_pct": 46.59,
  "vs_epollbook": "post",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20220608165638/https://rovelectionresults.sbcounty.gov/uploads/rov/elections/results/20220607/_content/ElectionSummaryReportRPT.pdf",
  "confidence": "primary",
  "note": "Election-night PLATEAU = 119,998 ballots ('Voters Cast: 119,998 of 1,138,019', 10.54% of registered) at Precincts Reported 2,030 of 2,030 (100.00%), from San Bernardino's official downloadable Election Summary Report ('Summary #5'), captured 20220608165638 (Wed June 8, 2022 09:56 AM PDT; report internal timestamp 6/8/2022 2:56:29 AM). The county's archived Results Posting Schedule (Elections/2022/0607/ResultSchedule, capture 20220608165638) pins the cadence: 8:30 p.m./10 p.m./12 a.m./2:30 a.m. postings then '3:15 a.m. -- Final Unofficial Election Night Results', next posting Wednesday 4 p.m. (canvass resumes) -- so this capture sits squarely on the plateau, between the 3:15 a.m. final-EN posting and the 4 p.m. canvass resume. The live results wrapper's ONLY election-night capture (20220608034508, Tue 8:45 PM) is explicitly labeled 'First Posting of Unofficial Election Night Results' (the classic first tranche) and was correctly rejected. Bracket proof: the NEXT capture of the same report file (20220701212908, 'Summary #15') shows 257,004 voters cast, +137,006 over Summary #5 -- proving Summary #5 was not itself canvass-advanced. 119,998 / 257,580 certified = 46.59%. Post-epollbook (KNOWiNK PollPad 2020), pre-ASV (2025). snapshot 20220608165638 used."
}
```

**VERIFY.md draft line:** `| 2022 | statewide-primary | 119,998 | 257,580 | 46.6% | primary | [link](https://web.archive.org/web/20220608165638/https://rovelectionresults.sbcounty.gov/uploads/rov/elections/results/20220607/_content/ElectionSummaryReportRPT.pdf) |`

**plateau_review.json draft:**
```json
{
  "slug": "san-bernardino-ca",
  "date": "2022-06-07",
  "verdict": "CONFIRMED",
  "basis": "county posting schedule brackets the capture, plus materially higher later capture",
  "evidence": "Summary #5, 6/8/2022 2:56:29 AM internal timestamp, Precincts Reported 2,030/2,030 (100.00%), Voters Cast 119,998/1,138,019; captured 09:56 AM PDT Wed June 8, inside the schedule's 3:15 a.m. Final-EN-to-4 p.m.-canvass-resume window; Summary #15 (June 30) shows 257,004, proving #5 was not already canvass-advanced"
}
```

---

## Item 6 of 6: 2024-03-05 (Presidential Primary)

**Denominator**: 305,853 (CA SoS SoV, `2024-primary/sov/03-voter-participation-stats-by-county.pdf`,
San Bernardino row:
`2,824 1,469,286 1,166,450 39,160 266,693 305,853 87.20% 26.22% 20.82%`).

**Numerator research**: the archived Results Posting Schedule
(`elections.sbcounty.gov/elections/2024/0305/resultschedule/`, capture
`20240309194756`) states the cadence for March 5, 2024: Tue 8:30 p.m. first
posting -> 10 p.m. -> Wed 12 a.m. -> **2 a.m. Posting of Final Unofficial
Election Night Results** -> 4 p.m. (canvass resumes) -> continues daily
through Fri March 8 and beyond.

The live results wrapper (`elections.sbcounty.gov/elections/2024/0305/results/`)
has only ONE Wayback capture in its whole history, at `20240305134328`
(Tue March 5, 05:43 AM PST -- BEFORE polls opened; a domain-wide CDX sweep
of the entire `elections.sbcounty.gov` host for the Mar 5 6pm-Mar 6 midnight
window confirms zero additional captures of this page or any results-bearing
page in the reporting window).

The underlying embed/report host `results.rov.sbcounty.gov` /
`.../uploads/rov/elections/results/20240305/_content/ElectionSummaryReportRPT.pdf`
has 4 captures total:
- `20240305223804` (Tue 14:38 PST) -- before poll close, not fetched (pre-election by schedule).
- `20240306060123` (Tue 22:01 PST) -- fetched: **Summary #2**, report
  timestamp `3/5/2024 9:45:58 PM`, **Precincts Reported: 449 of 2,824
  (15.90%)**, Voters Cast **116,765** of 1,166,305 (10.01%). This is
  self-evidently a partial/early tranche (only 15.9% precincts in), matching
  the 10 p.m. schedule slot (2nd posting), not the 2 a.m. Final.
- `20240318150401` (12 days later) -- fetched: **Summary #13**, report
  timestamp `3/15/2024 3:03:32 PM`, Voters Cast **301,547** (25.85%,
  post-canvass, near-certified).
- `20240805003222` -- certified-era, not fetched (redundant).

**No capture exists between Summary #2 (Tue 10 p.m. slot) and Summary #13
(post-canvass)** -- the 12 a.m., 2 a.m. "Final Unofficial", and Wednesday
4 p.m. reports were never archived. There is a real, dated gap: the plateau
(the ~2 a.m. Wed March 6 Final Unofficial report, likely Summary #4) is
simply unarchived.

**Verdict: NULL per definition.** Only a self-labeled partial 10 p.m.
tranche (15.9% precincts) and a 12-days-later post-canvass report survive;
neither is the election-night plateau.

**Draft row:**
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 305853,
  "election_night_pct": null,
  "vs_epollbook": "post",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 305,853 ballots cast (CA SoS SoV; precinct 39,160 + VBM 266,693; 26.22% of 1,166,450 registered). Post-epollbook (2020), pre-ASV (2025). Election-night PLATEAU not sourceable despite knowing its exact posting time: the archived Results Posting Schedule (elections.sbcounty.gov/elections/2024/0305/resultschedule/, capture 20240309194756) pins the cadence 8:30 p.m./10 p.m./12 a.m./'2 a.m. -- Posting of Final Unofficial Election Night Results'/4 p.m. (canvass resumes). The live results wrapper has only ONE capture in its entire history (20240305134328, Tue 5:43 AM PST, pre-poll-open; confirmed by a full domain CDX sweep of elections.sbcounty.gov for the Mar 5 6pm-Mar 6 midnight window returning zero additional results-bearing captures). The downloadable ElectionSummaryReportRPT.pdf on results.rov.sbcounty.gov has 4 captures: the fetched 20240306060123 (Tue 10:01 PM PDT) is 'Summary #2' (report stamp 3/5/2024 9:45:58 PM) showing Precincts Reported 449 of 2,824 (15.90%) and Voters Cast 116,765 (10.01%) -- an explicit partial/early tranche matching the 10 p.m. schedule slot, NOT the 2 a.m. Final; the next available capture (20240318150401, 12 days later) is 'Summary #13' (report stamp 3/15/2024) at 301,547 (25.85%), clearly post-canvass. No capture bridges the gap to the actual 2 a.m. Final Unofficial report (likely Summary #4); it is simply unarchived. No morning-after registrar press release found. Null per definition (Summary #2's 116,765 is examined and rejected as the classic partial-precinct first-tranche trap, not substituted). snapshot 20240306060123 (Summary #2, 15.9% precincts, not the plateau)."
}
```

**VERIFY.md draft line:** `| 2024 | presidential-primary | — | 305,853 | — | none | — (not sourceable) |`

---

## Summary table (all 6 primaries)

| Date | Type | Night ballots | Certified final | Share | Conf. | vs e-pollbook |
|---|---|---:|---:|---:|---|---|
| 2012-06-05 | presidential-primary | — | 193,517 | — | none | pre |
| 2014-06-03 | statewide-primary | — | 160,742 | — | none | pre |
| 2016-06-07 | presidential-primary | — | 339,754 | — | none | pre |
| 2018-06-05 | statewide-primary | — | 281,045 | — | none | pre |
| 2022-06-07 | statewide-primary | 119,998 | 257,580 | 46.59% | primary | post |
| 2024-03-05 | presidential-primary | — | 305,853 | — | none | post |

**Result: still no clean pre/post-e-pollbook election-night comparison for
San Bernardino.** All four pre-adoption primaries (2012/2014/2016/2018) and
one post-adoption primary (2024) are null; only 2022-06-07 (post-adoption)
is sourced, at 46.59%, giving San Bernardino a SECOND post-adoption
election-night data point (alongside the existing Nov-2024 general's
56.24%) but still zero pre-adoption points across all 12 elections examined
(6 generals + 6 primaries) in this dataset.

Pattern across all six: this registrar's site was crawled by Wayback only
sporadically pre-2019, almost always missing the actual election-night
window (either far too early -- pre-poll-open/first-tranche -- or far too
late -- multi-day-canvass). The 2018 and 2024 primaries came closest (an
actual within-election-night capture exists for both) but each is
explicitly self-labeled as an EARLY tranche (2018: "10:00 p.m. Posting",
15.9%-of-precincts-equivalent-implied by its low total; 2024: "Summary #2"
literally 15.90% precincts reporting), not the last-of-night report. 2022
succeeded only because the downloadable ElectionSummaryReportRPT.pdf file
(not the JS wrapper page) happened to be crawled once, coincidentally
inside the correct 13-hour plateau window.

## What's unfinished / needs the operator

- **This dossier is a scratch research artifact only.** Nothing has been
  written to `data/research/election-night/san-bernardino-ca.json`,
  `VERIFY.md`, or `plateau_review.json`. To land item 5 (the one sourced
  row), a follow-up pass must: (a) surgically insert the 2022-06-07 row
  into `san-bernardino-ca.json`'s `elections` array in date order, in the
  v4 schema shown above; (b) add the 5 null rows (2012/2014/2016/2018/2024)
  if the project wants primaries tracked as first-class rows alongside the
  generals (confirm with the maintainer whether primaries belong in the
  same per-county file or a separate one -- the existing file's `notes`
  field describes only the November-generals scope, so this is a
  methodology-scope decision, not a research one); (c) update the top-level
  `notes` field to describe the expanded primary coverage; (d) add
  `VERIFY.md`'s San Bernardino section (new rows, in the same table); (e)
  add the one `plateau_review.json` entry above; (f) run the FULL pipeline
  (RUNBOOK.md section 3: validator, `build_county_night.py`,
  `verify_en_denominators.py`, `verify_en_numerators.py`,
  `build_en_verification_report.py`, pytest, vitest).
- **FLAG for manual operator:** none of this research required a browser
  that curl/CDX couldn't reach -- no operator browser step was needed for
  any of the 6 primaries. All findings above are from `curl` + `pdftotext`
  + CDX, no puppeteer render needed (unlike the Nov-2024 general's JS
  wrapper page, every winning artifact here was either a raw HTML fragment
  page from the 2012-2018 era, or a directly-downloadable PDF for 2022).
- The 2024-03-05 null is the most frustrating: the plateau's approximate
  existence and timing (2 a.m. Wed March 6 "Final Unofficial") is known
  from the schedule page, exactly as with the Nov-2022 general's parallel
  case in the existing JSON -- but Wayback simply never crawled it. A human
  with Wayback's "Save Page Now" retroactive access, or a FOIA/records
  request to the registrar for its own retained copy of Summary #4 for
  03/05/2024, would be the only way to close this one.
- Denominator PDFs and all fetched numerator artifacts are cached under
  `/private/tmp/claude-501/.../scratchpad/sb-primaries/` (sov*.txt/.pdf,
  cdx_*.json, essr*.txt/.pdf, r*.txt/.bin, rs*.txt) for anyone re-verifying
  without re-fetching.
