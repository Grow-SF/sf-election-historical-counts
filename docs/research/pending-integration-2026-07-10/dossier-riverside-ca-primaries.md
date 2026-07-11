# Riverside County, CA -- primary election-night dossier

Scope: statewide-PRIMARY elections only (2012-06-05, 2014-06-03, 2016-06-07,
2018-06-05, 2022-06-07, 2024-03-05). Built per docs/research/RUNBOOK.md
sections 1, 5, 6, 7, 8. Existing generals in
data/research/election-night/riverside-ca.json establish that Riverside:
- ran Sequoia "eresults" (voteinfo.net) through 2018, never archived by
  Wayback on election night for any general 2012-2018;
- has NO morning-after "semi-official results" press release for any
  general year (checked 2012/2014/2016/2018/2022/2024's
  /Elections/<date>/docs/ archive) -- SKILL route-1 (registrar
  semi-final release) is a confirmed dead end for the county generally,
  but that check was only ever run against the GENERAL date folders. This
  dossier checks the PRIMARY date folders (`/Elections/YYYYMMDD/docs/`
  with the primary's own date) fresh, since the runbook's own guidance is
  that a dead route for Nov doesn't imply dead for June.
- adopted Dominion EMS (ElectionSummaryReportRPT) for the 2022 general,
  proven CONFIRMED primary-evidence plateau at 205,813/604,617 = 34.0%,
  2 a.m. report;
- moved to livevoterturnout.com ENR for 2024 general (611,101 ceiling,
  comparable:false, true plateau unarchived).

Adoption per existing record: `epollbook: 2022` (annual granularity),
`asv: 2025`. This dossier separately investigates WHEN in 2022 the
e-pollbook rollout happened, to classify 2022-06-07 pre/post honestly.

## Denominators (CA SoS Statement of Vote, statewide primaries)

All six primary "Voter Participation Statistics by County" PDFs were
located from the SoS statewide-election-results index
(https://www.sos.ca.gov/elections/prior-elections/statewide-election-results),
each election's own `.../statement-vote` page, which links the PDF at a
per-year path (layout is NOT a fixed pattern year to year -- confirmed
below). Riverside's "Total Voters" line was extracted with
`pdftotext -layout`.

| date | type | SoV URL | Riverside "Total Voters" |
|---|---|---|---|
| 2012-06-05 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf | 238,152 |
| 2014-06-03 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf | 198,102 |
| 2016-06-07 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf | 403,828 |
| 2018-06-05 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf | 346,472 |
| 2022-06-07 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf | 375,610 |
| 2024-03-05 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf | 409,269 |

Notes on the PDFs:
- 2012's file is literally named `03-voter-reg-stats-by-county.pdf` on the
  SoS site (there are TWO similarly-named PDFs, `02-voter-reg-stats...`
  and `03-voter-reg-stats...`; the `03-` one is the Voter Participation
  Statistics table, confirmed by its in-PDF title
  "VOTER PARTICIPATION STATISTICS BY COUNTY" and columns Precinct/VBM/Total
  Voters/Turnout).
- 2014's filename keeps the SoS's well-known misspelling
  "voter-particpiation" (confirmed matches runbook 6.1's note about the
  2014 general PDF sharing this typo).
- 2022/2024 rows carry a `*` next to "Riverside" that is the sheet's
  standard vote-center footnote ("In elections conducted using vote
  centers, Precinct Voters means vote center voters"), not a data-quality
  flag; Riverside ran vote centers in both. Total Voters is unaffected.
- direct curl to `elections.cdn.sos.ca.gov` for primary-year paths 403s
  without a browser User-Agent; a normal Chrome UA string succeeds (200).
  General-year paths do not require this. Recorded here in case a future
  pass hits the same false dead-end.

---

## Item: 2016-06-07 presidential-primary

**Denominator.** Certified final = 403,828 Total Voters (Precinct 127,086 +
VBM 276,742) from CA SoS 2016 Presidential Primary Voter Participation
Statistics by County:
https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf

**Numerator -- CONFIRMED plateau, gold-standard dated report series (runbook
6.3).** Riverside's Sequoia "eresults" directory for this primary
(`voteinfo.net/Elections/20160607/eresults/`) hosts a numbered
`Summary_UpdateN.pdf` series titled "Official Semi-Final Results,
PRESIDENTIAL PRIMARY, Riverside County," each stamped with an internal
`Run Date/Time:` header (report generation time, not crawl time -- runbook
7.3). Enumerated via CDX:
`https://web.archive.org/cdx/search/cdx?url=voteinfo.net/Elections/20160607/eresults/&matchType=prefix&output=json&limit=200&collapse=urlkey`
Fetched every available update (`Summary_Update1.pdf`
.. `Summary_Update17.pdf`, `Update3` not archived/not captured) via Wayback
raw `id_` replay and read the countywide "Riverside County / Total Ballots
Cast" cell + Run Date/Time footer of each with `pdftotext -layout`:

| report | Run Date/Time | countywide Total Ballots Cast |
|---|---|---|
| Update1 | 6/7/16 8:02:47 PM | 157,867 (first tranche -- the classic mistake, NOT used) |
| Update2 | 6/7/16 9:18:04 PM | 164,549 |
| Update3 | not archived | -- |
| Update4 | 6/7/16 11:09:39 PM | 178,788 |
| Update5 | 6/8/16 12:01:52 AM | 195,564 |
| Update6 | 6/8/16 1:03:33 AM | 213,683 |
| Update7 | 6/8/16 2:01:24 AM | 229,746 |
| **Update8** | **6/8/16 3:18:26 AM** | **249,970 -- PLATEAU** |
| Update9 | 6/10/16 4:49:49 PM (2 days later) | 279,815 |
| Update10..17 | 6/14 .. 7/3/16 (daily canvass cadence) | 334,149 .. 403,828 |
| "FINAL" | 7/5/16 9:40:10 AM | 403,828 (exactly equals SoS certified final) |

Update8 (249,970 ballots, 3:18:26 a.m. June 8) is the last report of the
continuous election-night sequence: the run times step roughly hourly from
8:02 p.m. through 3:18 a.m., matching Riverside's known "hourly until ~3
a.m." posting cadence (same cadence independently documented for the 2022
and 2024 GENERALS in riverside-ca.json / county-tech record), then the next
available report (Update9) jumps to 6/10, two days later -- the report
series' next file being days later is one of runbook 8's accepted
independent legs. Update17/"FINAL" both equal 403,828 exactly, matching the
SoS certified total bit-for-bit, confirming the update numbering runs
election night through certification and that Update8 is genuinely
mid-sequence, not an end state.

Arithmetic: 249,970 / 403,828 = **61.90%**.

Calibration: SF's own like-for-like 2016 general figure is ~66%; a June
PRESIDENTIAL primary at 61.9% for a growing inland-empire vote-by-mail-heavy
county is a plausible plateau share, well above a half-of-final first-tranche
artifact (157,867/403,828 = 39.1%, which is what Update1 alone would have
given -- the exact first-tranche trap the runbook warns about).

vs_epollbook: pre (Riverside's e-pollbook/digital-roster adoption is dated
to the June 7, 2022 VCA rollout; 2016 used paper rosters at assigned
precincts). vs_asv: pre (ASV adopted 2025).

**Draft dataset row** (data/research/election-night/riverside-ca.json schema):
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 249970,
  "certified_final": 403828,
  "election_night_pct": 61.9,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20160615020639id_/http://www.voteinfo.net:80/elections/20160607/eresults/Summary_Update8.pdf",
  "confidence": "primary",
  "note": "Election-night plateau = 249,970 ballots ('Total Ballots Cast' countywide, Riverside County column) from the official Riverside Sequoia 'Official Semi-Final Results' report Summary_Update8.pdf, Run Date/Time 6/8/16 3:18:26 AM (the last-of-night report; posting cadence ~hourly from 8:02 PM through 3:18 AM). The next available report in the series, Summary_Update9.pdf, is Run Date/Time 6/10/16 4:49:49 PM -- two days later, proving the canvass had resumed and Update8 was the true election-night plateau (runbook 8 leg: report series' next file being days later). Update17/Summary_FINAL_0705.pdf both show 403,828, exactly the SoS certified total, confirming the series runs night-through-certification. NOT the 8:02 PM first tranche (Update1, 157,867 -- 39.1% of final, the classic mistake). 249,970/403,828 = 61.9%. Certified final 403,828 (Precinct 127,086 + VBM 276,742) from CA SoS 2016 Presidential Primary Voter Participation Statistics by County, primary. Series enumerated via CDX (voteinfo.net/Elections/20160607/eresults/, matchType=prefix); all PDFs fetched via Wayback raw id_ replay."
}
```

**Draft VERIFY.md line:** `| 2016-06-07 | presidential-primary | 249,970 | 403,828 | 61.9% | pre | pre | primary |`

**Plateau verdict:** CONFIRMED (self-describing "Semi-Final Results" +
late-night timestamp + report-series-next-file-days-later leg, per runbook
8).

---

## Item: 2012-06-05 presidential-primary -- NULL

**Denominator.** Certified final = 238,152 Total Voters (Precinct 70,045 +
VBM 168,107) from CA SoS 2012 Presidential Primary Voter Participation
Statistics by County:
https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
(NB: this exact filename is `03-voter-reg-stats-by-county.pdf` on the SoS
site despite being the participation table -- there is a separately-named,
different `02-voter-reg-stats-by-county.pdf` too; confirmed by in-PDF title
"VOTER PARTICIPATION STATISTICS BY COUNTY").

**Numerator -- exhaustive search, genuinely unsourceable.** Routes tried:
- CDX prefix enumeration of the ENTIRE `voteinfo.net/Elections/20120605/`
  tree (docs/ + eresults/ combined):
  `https://web.archive.org/cdx/search/cdx?url=voteinfo.net/Elections/20120605/&matchType=prefix&output=json&limit=300&collapse=urlkey`
  -- returns `[]`, zero captures of any file under this path, ever.
- Domain-wide CDX filtered to the date string, April-August 2012 window
  (`url=voteinfo.net&matchType=domain&from=20120401&to=20120801&filter=urlkey:.*20120605.*`)
  -- also `[]`.
- The one nearby capture found on the bare domain, `currentElection.asp`
  dated 20120606144953 (the day after the election), turned out to be a
  Wayback replay-aliasing case (runbook 7.1): the `id_` raw fetch 302s to a
  DIFFERENT, much earlier capture (20111114140034), i.e. the listed capture
  is not actually servable/is misfiled in the index. No usable content
  recovered.
- Live site check: `docs.voteinfo.net/Elections/20120605/eresults/Summary1.pdf`
  through `Summary20.pdf` and the `www.voteinfo.net` legacy path both 404 --
  unlike 2016/2018, the 2012 files are not still hosted live (they predate
  whatever migration preserved the later years).
- `voteinfo.net/past-elections` (the current registrar site's historical
  index) does not link back to 2012.
- WebSearch for `Riverside County "June 5, 2012" primary election night
  results ballots counted Press-Enterprise` returned only the modern
  registrar homepage/press-release index and an ABC7 statewide results
  page, no county-specific election-night total.
- No morning-after "semi-official results" registrar press release exists
  for this date (consistent with the confirmed dead end already documented
  for every Riverside GENERAL year in the existing riverside-ca.json row
  notes).

**Row:** `election_night_ballots: null, election_night_pct: null,
confidence: "none", source_url_night: null`.

**Draft dataset row:**
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 238152,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final = 238,152 ballots (Precinct 70,045 + VBM 168,107) from CA SoS 2012 Presidential Primary Voter Participation Statistics by County, primary. Election-night plateau not sourceable: CDX prefix enumeration of the entire voteinfo.net/Elections/20120605/ tree (docs/ + eresults/) returns zero captures ever; a domain-wide CDX filtered to the date string across Apr-Aug 2012 is also empty. The one nearby capture, currentElection.asp dated 2012-06-06, is a Wayback replay-aliasing case (id_ raw fetch 302s to an unrelated 2011-11-14 capture per runbook 7.1) -- no usable content. Unlike the 2016/2018 primaries, docs.voteinfo.net does not still host the 2012 eresults Summary PDFs live (404 for Summary1-20.pdf). No morning-after semi-official-results registrar press release exists for this date, matching the confirmed dead end for every Riverside GENERAL year. WebSearch for contemporaneous Press-Enterprise coverage found no county-specific election-night ballot count. Plateau remains unsourceable."
}
```

**Draft VERIFY.md line:** `| 2012-06-05 | presidential-primary | NULL | 238,152 | -- | pre | pre | none |`

**Plateau verdict:** n/a (null row; nothing to verify).

---

## Item: 2014-06-03 statewide-primary -- NULL

**Denominator.** Certified final = 198,102 Total Voters (Precinct 50,111 +
VBM 147,991) from CA SoS 2014 Statewide Direct Primary Voter Participation
Statistics by County:
https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
(SoS's own well-known "particpiation" misspelling, intact in the filename).

**Numerator -- one artifact recovered, but it is the certified total itself,
not an election-night plateau; genuinely unsourceable as a distinct
election-night number.** Riverside's `voteinfo.net/Elections/20140603/eresults/`
directory (enumerated via CDX prefix) contains NO `Summary_UpdateN.pdf` /
`SummaryN.pdf` dated report series at all -- only `20140603_SOV.zip`,
`20140603_SOVBOOK.pdf`, `20140603_WI_RESULTS.pdf`, and the GEMS-style
frameset (`Election Result.htm` / `_dtl.htm` / `_hdr.htm` / `_idx.htm`).
The `_dtl.htm` page was fetched
(`https://web.archive.org/web/20140701120341id_/http://www.voteinfo.net/elections/20140603/eresults/Election%20Result_dtl.htm`)
and reads "Last Updated: June 13, 2014 11:59 AM," Governor race 847/847
precincts (100%), countywide Total 198,102 -- this is EXACTLY the SoS
certified final, i.e. a fully-certified snapshot, not a distinct
election-night count (runbook 7.3's "frozen page" pattern, but frozen at
the FINAL state, not a useful floor). A full CDX history of this exact URL
(`net,voteinfo)/elections/20140603/eresults/election%20result_dtl.htm`)
shows every capture from 2014-07-01 through 2022-05-27 sharing the IDENTICAL
digest `I7XPOTXEMX2RLRBTDCPAJGDCFIMBZIRK` -- the page has been frozen at the
June 13 certified state since the earliest available capture; there is no
earlier (election-night-stage) capture to recover.
- `docs/` press-release archive for this date (full CDX already enumerated)
  runs pre-election releases only (candidate filing, VBM, early voting)
  through `20140613_Release_Certified.pdf` (the June 13 certification
  release matching the frozen page above) -- no morning-after
  "semi-official results" release.
- Live-site check: `docs.voteinfo.net/Elections/20140603/eresults/Summary1.pdf`
  etc. do not exist for this year (the dated-Summary-series convention that
  rescued 2016/2018 was not yet in use in 2014; this election used the
  older GEMS frameset only, which was never captured before its
  certification-day freeze).

**Row:** null per 5.1. The one recovered number (198,102) is excluded
because it is definitionally the certified final, not a night count; using
it as the numerator would produce a fabricated 100.00% and silently
misrepresent "grabbed the wrong report" as "grabbed the plateau."

**Draft dataset row:**
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 198102,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final = 198,102 ballots (Precinct 50,111 + VBM 147,991) from CA SoS 2014 Statewide Direct Primary Voter Participation Statistics by County, primary. Election-night plateau not sourceable: the eresults/ directory for this date has no dated Summary_Update/SummaryN report series (unlike 2016/2018) -- only a GEMS-style frameset. Its Election Result_dtl.htm is locked to 'Last Updated: June 13, 2014 11:59 AM', Governor 847/847 precincts (100%), Total 198,102 -- exactly the SoS certified final, i.e. a fully-certified post-canvass snapshot, not a distinct election-night count. Full CDX history of that exact URL shows every capture 2014-07-01 through 2022-05-27 sharing an identical digest, i.e. frozen at the certified state since the earliest available crawl; no earlier, election-night-stage capture exists. docs/ press-release archive has no morning-after semi-official-results release (runs to the 20140613_Release_Certified.pdf certification announcement). docs.voteinfo.net does not host a dated Summary-series live for this year the way it does for 2016/2018. Plateau remains unsourceable; the 198,102 figure recovered is the certified final itself and is NOT substituted as a night count (would fabricate a false 100.00% share)."
}
```

**Draft VERIFY.md line:** `| 2014-06-03 | statewide-primary | NULL | 198,102 | -- | pre | pre | none |`

**Plateau verdict:** n/a (null row).

---

## Item: 2018-06-05 statewide-primary

**Denominator.** Certified final = 346,472 Total Voters (Precinct 91,667 +
VBM 254,805) from CA SoS 2018 Statewide Direct Primary Voter Participation
Statistics by County:
https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf

**Numerator -- CONFIRMED plateau, dated report series recovered from the
LIVE site (Wayback only preserved one of thirteen).** Wayback's CDX for
`voteinfo.net/Elections/20180605/eresults/` shows only a single dated
report, `Summary12.pdf` (captured 2023-03-23, itself already mid-canvass:
Run Date/Time 6/19/18 4:32:44 PM, 335,242 ballots). Rather than stop there,
checked whether the registrar's document CDN still serves the historical
files directly: `docs.voteinfo.net/Elections/20180605/eresults/SummaryN.pdf`
(a different subdomain from the redesigned `www.voteinfo.net`, matching the
county-tech record's own citation pattern `docs.voteinfo.net/docs/...`) --
**Summary1.pdf through Summary13.pdf are still live (200), Summary14+ 404**.
Downloaded all 13 and read each `Run Date/Time:` header + countywide
"Riverside County / Total Ballots Cast" cell with `pdftotext -layout`:

| report | Run Date/Time | countywide Total Ballots Cast |
|---|---|---|
| Summary1 | 6/5/18 8:00:55 PM | 119,452 (first tranche -- NOT used) |
| Summary2 | 6/5/18 9:21:21 PM | 129,683 |
| Summary3 | 6/5/18 10:08:46 PM | 132,436 |
| Summary4 | 6/5/18 11:06:04 PM | 138,313 |
| Summary5 | 6/6/18 12:04:25 AM | 148,600 |
| Summary6 | 6/6/18 2:16:21 AM | 153,801 |
| Summary7 | 6/6/18 3:55:15 AM | 171,870 |
| **Summary8** | **6/6/18 6:25:10 AM** | **193,152 -- PLATEAU** |
| Summary9 | 6/8/18 5:22:39 PM (2 days later) | 231,461 |
| Summary10..13 | 6/12 .. 6/22/18 (daily canvass cadence) | 286,955 .. 344,677 |
| (frozen "Election Result_dtl.htm", "Last Updated June 29, 2018") | -- | 346,472 (exactly the SoS certified final) |

Summary8 (193,152 ballots, 6:25:10 a.m. June 6) is the last report of the
continuous overnight sequence: report intervals step from 8:00 p.m. through
6:25 a.m. (roughly hourly, slowing overnight -- 3:55 a.m. to 6:25 a.m. is
the widest overnight gap, still same continuous run), then Summary9 jumps
to 6/8, a 2-day gap, matching the runbook 8 "report series' next file being
days later" leg exactly as in 2016. Titled "Official Semi-Final Results,
STATEWIDE DIRECT PRIMARY ELECTION" on every page (self-describing). The
frozen `Election Result_dtl.htm` page (see 2014 item above for the pattern)
independently confirms 346,472 as the certified final, matching the SoS PDF
exactly.

Archived Summary8.pdf to Wayback for a permanent citation
(`https://web.archive.org/save/https://docs.voteinfo.net/Elections/20180605/eresults/Summary8.pdf`
-> snapshot 20260710205406, confirmed servable via CDX,
`digest 5H47KVRMA5C52AQXIRK5NQLJOZBDXIQW`).

Arithmetic: 193,152 / 346,472 = **55.75%**.

Calibration: below the 2016 primary's 61.9% (consistent with a
lower-turnout, less-VBM-saturated midterm-year primary vs. a presidential
primary) and well above the first-tranche trap (119,452/346,472 = 34.5%,
what Summary1 alone would have given).

vs_epollbook: pre. vs_asv: pre.

**Draft dataset row:**
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 193152,
  "certified_final": 346472,
  "election_night_pct": 55.75,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20260710205406/https://docs.voteinfo.net/Elections/20180605/eresults/Summary8.pdf",
  "confidence": "primary",
  "note": "Election-night plateau = 193,152 ballots ('Total Ballots Cast' countywide, Riverside County column) from the official Riverside Sequoia 'Official Semi-Final Results' report Summary8.pdf, Run Date/Time 6/6/18 6:25:10 AM. Wayback's own crawl of the eresults/ directory only preserved Summary12.pdf (already mid-canvass); the full Summary1-13 series was instead recovered from docs.voteinfo.net, which still serves these historical files live (Summary14+ 404). Report cadence: 8:00 PM through 6:25 AM roughly hourly (Summary1-8), then Summary9 jumps to 6/8/18 5:22:39 PM -- a 2-day gap proving Summary8 was the last report of the continuous election-night sequence (runbook 8 leg: report series' next file being days later). NOT the 8:00 PM first tranche (Summary1, 119,452 -- 34.5% of final). 193,152/346,472 = 55.75%. Certified final 346,472 (Precinct 91,667 + VBM 254,805) from CA SoS 2018 Statewide Direct Primary Voter Participation Statistics by County, primary; independently corroborated by the eresults GEMS frameset (Election Result_dtl.htm), frozen at 'Last Updated: June 29, 2018', showing the identical 346,472. Summary8.pdf archived to Wayback 2026-07-10 (snapshot 20260710205406) for a stable citation since the source is otherwise only live-hosted."
}
```

**Draft VERIFY.md line:** `| 2018-06-05 | statewide-primary | 193,152 | 346,472 | 55.75% | pre | pre | primary |`

**Plateau verdict:** CONFIRMED (self-describing "Semi-Final Results" +
overnight timestamp run + report-series-next-file-two-days-later leg, per
runbook 8).

---

## Item: 2022-06-07 statewide-primary (+ the e-pollbook rollout-timing finding)

**E-pollbook rollout timing (task's headline question).** This is
DEFINITIVE, not indeterminate: per the county's own tech-adoption record
(`data/research/county-tech/riverside-ca.json`, type `epollbook`,
confidence primary, citing the Registrar's Election Administration Plan
https://docs.voteinfo.net/docs/riverside-eap-final_ADA_EN.pdf), Riverside's
Board of Supervisors approved Voter's Choice Act implementation on
2021-12-14, and **the June 7, 2022 Gubernatorial Primary was explicitly
named as the FIRST election conducted under the new model** ("The first
official election under this new model will be the June 7, 2022
Gubernatorial Primary Election"). The e-pollbook/digital-roster finding
(paper rosters replaced by networked laptops with a direct connection to
the Registrar's election-management system at vote centers) is part of
that same VCA rollout, first used AT this primary, not partway through the
year. There is no "sometime later in 2022" ambiguity to resolve: the
2022-06-07 primary is the epoch-zero e-pollbook election itself, so
`vs_epollbook: "post"` for this row and every later one; every row through
2018 is cleanly `"pre"`.

**Denominator.** Certified final = 375,610 Total Voters (Precinct 23,640 +
VBM 351,970) from CA SoS 2022 Primary Voter Participation Statistics by
County:
https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
(Riverside's row carries the sheet's standard vote-center `*` footnote, not
a data flag.)

**Numerator -- CONFIRMED plateau, same Dominion EMS report series already
proven for the Nov 2022 general.** By 2022 Riverside had replaced Sequoia
with Dominion Democracy Suite (per county-tech record, system replaced
2019); the existing riverside-ca.json 2022-11-08 general row already
establishes the numbered `ElectionSummaryReportRPT<N>.pdf` series at
`voteinfo.net/Elections/<date>/docs/` as Riverside's confirmed
election-night source. The same pattern exists for this primary. Wayback's
CDX for `voteinfo.net/Elections/20220607/` shows only `RPT6.pdf`
(2022-08-18, mid-canvass) and `RPT14.pdf` (2022-06-23) among the numbered
reports plus the raw `ElectionSummaryReportRPT_mhtml.htm` (2022-06-07
13:10, an early-afternoon PRE-poll-close snapshot, not usable). As with
2018, checked whether `docs.voteinfo.net` (the same still-live document CDN
that rescued the 2018 series) hosts the full run:
**ElectionSummaryReportRPT1.pdf through RPT16.pdf are live (200), RPT17+
404.** Downloaded all 16 and read the `Page: 1 of 12` timestamp + "Voters
Cast:" line with `pdftotext -layout`:

| report | timestamp | Voters Cast | Precincts Reported |
|---|---|---|---|
| RPT1 | 6/7/2022 8:03:18 PM | 155,963 (first tranche -- NOT used) | 116/795 (14.6%) |
| RPT2 | 6/7/2022 8:47:05 PM | 167,957 | 118/795 |
| RPT3 | 6/7/2022 9:50:08 PM | 173,157 | 118/795 |
| RPT4 | 6/7/2022 10:53:01 PM | 179,585 | 497/795 |
| RPT5 | 6/7/2022 11:51:24 PM | 184,556 | 643/795 |
| **RPT6** | **6/8/2022 12:31:41 AM** | **191,996 -- PLATEAU** | **795/795 (100.00%)** |
| RPT7 | 6/8/2022 4:52:51 PM (next afternoon) | 205,296 | 795/795 |
| RPT8..16 | 6/9 .. 6/30/2022 (daily canvass cadence) | 226,112 .. 375,610 | 795/795 |

RPT6 (191,996 ballots, 12:31:41 a.m. June 8) is the last report of the
continuous overnight sequence (roughly hourly from 8:03 p.m.) and is the
FIRST report to reach 795/795 = 100% precincts reported -- i.e. election-day
in-person voting was fully tallied by this report, an even stronger
"end of the continuous count" signal than 2016/2018 (which plateaued
mid-precinct-count). RPT7 then jumps 16+ hours to the following afternoon,
and every subsequent report is a once-daily canvass update through RPT16
(6/30/2022), which equals 375,610 -- exactly the SoS certified final,
confirming the numbering runs night-through-certification. Titled "STATEWIDE
DIRECT PRIMARY ELECTION ... Semi-Official Election Results" on every page
(same self-describing title format as the CONFIRMED Nov 2022 general row).

Archived RPT6 to Wayback for a permanent citation
(`https://web.archive.org/save/https://docs.voteinfo.net/Elections/20220607/docs/ElectionSummaryReportRPT6.pdf`
-> snapshot 20260710205902, confirmed via CDX,
digest `7OCW33O6OHORR7R3QZFEFLCFC5WLJYWD`).

Arithmetic: 191,996 / 375,610 = **51.12%**.

Calibration: lower than the 2016 (61.9%) and 2018 (55.75%) primaries,
consistent with the 2022 VCA all-mail-ballot rollout depressing
election-night share independent of e-pollbooks (same confound the runbook
flags for 2018-2020 generally) -- this is the FIRST primary under the
all-mail vote-center model, so a same-election-night-share test against
2018 is confounded by two simultaneous changes (VCA/all-mail AND
e-pollbooks); record as a confound, not "fixed."

vs_epollbook: **post** (this is the rollout election itself). vs_asv: pre
(ASV adopted 2025).

**Draft dataset row:**
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 191996,
  "certified_final": 375610,
  "election_night_pct": 51.12,
  "vs_epollbook": "post",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20260710205902/https://docs.voteinfo.net/Elections/20220607/docs/ElectionSummaryReportRPT6.pdf",
  "confidence": "primary",
  "note": "Election-night plateau = 191,996 ballots ('Voters Cast: 191,996 of 1,304,447') from the official Riverside Dominion EMS 'Semi-Official Election Results' report ElectionSummaryReportRPT6.pdf, timestamp 6/8/2022 12:31:41 AM -- the first report to reach 795/795 (100.00%) precincts reported, i.e. election-day in-person voting fully tallied. Wayback only preserved RPT6 (mid-canvass, 8/18/2022 crawl) and RPT14 among the numbered series; the full RPT1-16 run was recovered from docs.voteinfo.net, which still serves these historical files live (RPT17+ 404), the same document CDN that also rescued the 2018 primary's Summary series. Report cadence: 8:03 PM through 12:31 AM roughly hourly (RPT1-6), then RPT7 jumps to 6/8/2022 4:52:51 PM (next afternoon, 16+ hour gap) and every subsequent report is a once-daily canvass update through RPT16 (6/30/2022 = 375,610, exactly the SoS certified final). NOT the 8:03 PM first tranche (RPT1, 155,963 -- 41.5% of final). 191,996/375,610 = 51.12%. Certified final 375,610 (Precinct 23,640 + VBM 351,970) from CA SoS 2022 Primary Voter Participation Statistics by County, primary. RPT6.pdf archived to Wayback 2026-07-10 (snapshot 20260710205902) for a stable citation. THE E-POLLBOOK ROLLOUT-TIMING FINDING: this is not an ambiguous mid-year adoption. Per the county-tech record (Riverside EAP, primary source), the Board of Supervisors approved VCA implementation 2021-12-14 and this June 7, 2022 primary is explicitly named the FIRST election under the new model (vote centers + the direct-EMS-connection e-pollbook/digital-roster replacing paper rosters). vs_epollbook is therefore 'post' for this row itself, not merely for elections after it. CONFOUND: this is also the first all-mail VCA election, so any 2018-vs-2022 election-night-share comparison conflates the e-pollbook change with the simultaneous VCA/all-mail-ballot shift; record, do not adjust for."
}
```

**Draft VERIFY.md line:** `| 2022-06-07 | statewide-primary | 191,996 | 375,610 | 51.12% | post | pre | primary |`

**Plateau verdict:** CONFIRMED (self-describing "Semi-Official Election
Results" + late-night timestamp + 100% precincts-reported leg +
report-series-next-file-16-hours-then-daily leg, per runbook 8).

---

## Item: 2024-03-05 presidential-primary -- NULL

**Denominator.** Certified final = 409,269 Total Voters (Precinct 38,699 +
VBM 370,570) from CA SoS 2024 Presidential Primary Voter Participation
Statistics by County:
https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf

**Numerator -- exhaustive search, genuinely unsourceable (matches the
existing Nov 2024 general's finding that Riverside's Dominion-PDF series
route was discontinued by 2024).**
- `voteinfo.net/Elections/20240305/` (docs/ + eresults/, prefix CDX): ZERO
  Wayback captures of any kind.
  `https://web.archive.org/cdx/search/cdx?url=voteinfo.net/Elections/20240305/&matchType=prefix&output=json&limit=300&collapse=urlkey`
- `docs.voteinfo.net` (the live document CDN that rescued 2018 and 2022):
  `ElectionSummaryReportRPT1.pdf` .. `RPT6.pdf` all 404 for
  `/Elections/20240305/docs/`; no Dominion PDF series exists for this
  election at all -- by March 2024 Riverside had moved off the numbered-PDF
  route onto `livevoterturnout.com` ENR exclusively (same transition
  already documented for the Nov 2024 general).
- `livevoterturnout.com/ENR/riversidecaenr/3/` (ENR ID 3 = this primary,
  confirmed by its `summary_3.xml`'s `<ElectionID>3</ElectionID>` matching
  race data e.g. "President of the US DEM"): Wayback holds exactly ONE
  capture, `en/Index_3.html` at 2024-03-09 05:15:58 -- four days
  post-election, and even that capture is a JS shell with no statically
  embedded ballot totals (the real numbers load via an AJAX call to
  `../summary_<ID>.xml`, traced from the page's
  `LiveResultsScripts_v4.1.js`: `url = '../summary_' + electionID + '.xml'`).
  That XML file itself has ZERO Wayback captures at any date
  (`url=livevoterturnout.com/ENR/riversidecaenr/3/summary_3.xml` -> `[]`).
- The live `summary_3.xml` endpoint still resolves (200) today, but it is
  NOT versioned/timestamped per-report the way Dominion's PDFs or Clarity's
  JSON are -- it is overwritten in place and its embedded
  `<GeneratedDate>2024-04-04T16:46:46...</GeneratedDate>` /
  `<TotalBallotsCast>409269</TotalBallotsCast>` show it is frozen at the
  April 4, 2024 CERTIFICATION state (409,269 exactly equals the SoS
  certified final) -- useless for recovering an election-night value, and
  with no earlier archived version, there is no ceiling or floor to fall
  back on either (unlike the Nov 2024 general, which at least had a Nov-7
  ceiling capture).
- Registrar press release `rivco.gov/news/march-5-election-night-results-reporting`
  (found via WebSearch, fetched directly) is a pre-election SCHEDULE
  announcement only ("First Tabulation approximately 8:20 p.m. ... results
  will continue to be uploaded every hour until approximately 3 a.m.") --
  it corroborates Riverside's known hourly-until-~3-a.m. cadence but
  contains no actual ballot-count figure, so it cannot serve as either
  numerator or corroboration of a specific number.
- Local news: `riversiderecord.org`'s 2024 primary results article (fetched
  via WebFetch) states only the same pre-election reporting schedule, no
  countywide ballot-count figure at any timing.

**Row:** null per 5.1.

**Draft dataset row:**
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 409269,
  "election_night_pct": null,
  "vs_epollbook": "post",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final = 409,269 ballots (Precinct 38,699 + VBM 370,570) from CA SoS 2024 Presidential Primary Voter Participation Statistics by County, primary. Election-night plateau not sourceable: voteinfo.net/Elections/20240305/ has zero Wayback captures of any kind (docs/ + eresults/, prefix CDX); docs.voteinfo.net (the live CDN that rescued the 2018 and 2022 primary numerator series) 404s for ElectionSummaryReportRPT1-6.pdf under this date -- by 2024 Riverside had discontinued the numbered Dominion-PDF route entirely (same transition already documented for the Nov 2024 general) in favor of livevoterturnout.com ENR only. livevoterturnout's ENR ID 3 (confirmed via its summary_3.xml ElectionID field) has exactly one Wayback capture of its JS-shell index page, 2024-03-09 (4 days post-election), which does not statically embed ballot totals; the AJAX data endpoint it calls (../summary_3.xml, traced from LiveResultsScripts_v4.1.js) has ZERO Wayback captures at any date. That endpoint still resolves live today but is overwritten-in-place (not versioned), frozen at the April 4, 2024 certification state (GeneratedDate 2024-04-04T16:46:46, TotalBallotsCast 409,269 -- exactly the SoS certified final) with no earlier archived version to recover a ceiling or floor from. The registrar's rivco.gov 'March 5 Election Night Results Reporting' press release (dated 2024-03-05) is a pre-election SCHEDULE announcement only (hourly updates until ~3 a.m.), no ballot-count figure. riversiderecord.org's primary-results article likewise states only the reporting schedule, no countywide total at any timing. Plateau remains unsourceable."
}
```

**Draft VERIFY.md line:** `| 2024-03-05 | presidential-primary | NULL | 409,269 | -- | post | pre | none |`

**Plateau verdict:** n/a (null row).

---

## SUMMARY (all six primaries, chronological)

| date | type | plateau ballots | certified final | pct | vs_epollbook | vs_asv | confidence | verdict |
|---|---|---|---|---|---|---|---|---|
| 2012-06-05 | presidential-primary | NULL | 238,152 | -- | pre | pre | none | n/a |
| 2014-06-03 | statewide-primary | NULL | 198,102 | -- | pre | pre | none | n/a |
| 2016-06-07 | presidential-primary | 249,970 | 403,828 | 61.9% | pre | pre | primary | CONFIRMED |
| 2018-06-05 | statewide-primary | 193,152 | 346,472 | 55.75% | pre | pre | primary | CONFIRMED |
| 2022-06-07 | statewide-primary | 191,996 | 375,610 | 51.12% | **post** | pre | primary | CONFIRMED |
| 2024-03-05 | presidential-primary | NULL | 409,269 | -- | post | pre | none | n/a |

Pre/post e-pollbook split now has real data on both sides for the first
time in this county's dataset (the Nov generals are pre-only or
comparable:false): 2016 (61.9%) and 2018 (55.75%) pre-adoption vs. 2022
(51.12%) post-adoption -- a same-direction-as-generals decline, but
CONFOUNDED by the simultaneous VCA/all-mail-ballot rollout at the exact
same election (2022-06-07 is both the first e-pollbook election AND the
first all-mail-ballot election); do not read this as an e-pollbook-only
effect without controlling for VCA.

## Key method note for the integrator

Two of the three CONFIRMED rows (2018, 2022) were recovered not from
Wayback but from **`docs.voteinfo.net`, a still-live document CDN that
continues to serve Riverside's historical dated-report PDF series years
after the front-end site (`www.voteinfo.net`) was redesigned and its own
copies 404'd.** This is a reusable route worth adding to runbook 6.2/6.3
for this county (and worth spot-checking for other counties whose main
site redesigned but may have an old docs subdomain still live): when
Wayback has sparse coverage of a dated report series, check whether the
county's document-hosting subdomain still serves the un-migrated files
directly, live, before concluding the series is unrecoverable. Both
recovered PDFs (2018 Summary8.pdf, 2022 RPT6.pdf) were additionally pushed
through `web.archive.org/save/` and confirmed via CDX so the dossier's
citations resolve to permanent Wayback snapshots rather than a live URL
that could change.

## Routes NOT needed for this county's primaries

Clarity ENR (runbook 6.4) -- Riverside never used Clarity for any of the
six primaries (Sequoia through 2018, Dominion 2019+, livevoterturnout ENR
2024+); no Clarity-specific investigation was performed and none is
needed.

## What's unfinished / for the integrator

- None of the six rows have been written into
  `data/research/election-night/riverside-ca.json`,
  `data/research/election-night/VERIFY.md`, or
  `data/research/election-night/plateau_review.json` -- this is a read-only
  research dossier per the task; the integrator should apply the four
  CONFIRMED/NULL rows (2016, 2018, 2022 sourced; 2012, 2014, 2024 null)
  using the section-3 pipeline (validate -> build_county_night ->
  verify_en_denominators/numerators -> build_en_verification_report ->
  pytest -> vitest), then re-verify the two `web.archive.org/save/`
  snapshots created during this pass (2018 Summary8.pdf snapshot
  20260710205406; 2022 RPT6.pdf snapshot 20260710205902) resolve for the
  automated numerator checker.
- The `type` vocabulary used here (`presidential-primary` for 2012/2016/2024,
  `statewide-primary` for 2014/2018/2022) follows the task's suggestion;
  double check against whatever vocabulary the schema validator already
  enforces for other counties' primary rows (if any exist) before merging.
- No FLAG for manual operator was needed anywhere in this pass -- every
  dead end was a genuine archival gap (zero captures, or a frozen/live
  endpoint with no earlier version), not a bot-wall or JS-rendering
  problem a browser could get around.
- Network to web.archive.org was intermittently flaky during this session
  (sporadic connection-refused on both port 80 and 443, self-resolving
  after 10-60s); all fetches in this dossier were eventually confirmed
  successful (non-empty, correctly-typed content) via retry, but if the
  integrator re-runs any citation and hits a transient failure, retry
  before treating it as a dead link.

---


