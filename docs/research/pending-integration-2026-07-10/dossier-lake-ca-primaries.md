# Dossier: Lake County, CA (slug lake-ca) -- statewide PRIMARY election nights

Control county (never adopted e-pollbook or ASV; `adoption.epollbook`/`adoption.asv`
both null in data/research/election-night/lake-ca.json). This dossier extends the
existing (generals-only) lake-ca.json record to the six statewide primaries:
2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05, 2022-06-07, 2024-03-05.

READ-ONLY research pass. Nothing in this file has been written to the repo.
Build date: 2026-07-10.

---

## Item 1 of 6: 2012-06-05 Presidential Primary

**Certified final (denominator).** CA SoS Statement of Vote, "Voter
Participation Statistics by County" PDF:
`https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf`
(note: filename literally says "voter-reg-stats" despite the page containing
the Voter Participation Statistics table -- confirmed by content, not just
label, since the SOS "Statement of Vote" page for this election lists it
under "Voter Participation Statistics by County"; distinct from the
REGISTRATION-only file `02-voter-reg-stats-by-county.pdf` in the same
directory). Table header: "VOTER PARTICIPATION STATISTICS BY COUNTY". Lake
County line: Precincts 70, Eligible to Register 47,459, Registered Voters
33,553, Precinct Voters 4,781, Vote-By-Mail Voters 9,493, **Total Voters
14,274**, Turnout (Registered) 42.54%, Turnout (Eligible) 30.08%.
**certified_final = 14,274.**

**Plateau numerator.** County's own numbered results-report system
(`acm.co.lake.ca.us/elections/results/result23.htm`; report #23 confirmed by
its `index23.htm` title block: "LAKE COUNTY / Presidential Primary Election
/ June 5, 2012" -- same overwrite-in-place system independently used for
this county's 2012/2014/2016 GENERAL rows already in lake-ca.json).
Source URL used (earliest surviving capture):
`https://web.archive.org/web/20120609045640id_/http://acm.co.lake.ca.us:80/elections/results/result23.htm`
Internal header: **"Election Results as of 06/06/2012 at 12:19:31 AM"**
(past-midnight tail of election night, i.e. ~19 minutes after the previous
generals' typical report time). "Completed Precincts: 70 of 70" (100%).
"Total Ballots Cast **10,427** (31.1%)" = Precinct Ballots Cast 4,787 +
Absentee Ballots Cast 5,640.

**Plateau-holding evidence (RUNBOOK 8).**
1. CDX for `result23.htm` shows THREE captures with the IDENTICAL content
   digest `INC3DMJZ3TJ2UU5L3NJ2K5HNI4NWYMJY`: 2012-06-09 04:56:40,
   2012-06-20 15:58:49, and 2012-07-05 21:16:19 UTC -- the page held
   byte-for-byte unchanged for nearly a month after election night (a
   held-count leg on its own, same form as the 2014-general row).
2. The NEXT distinct digest (`U7Q5KZUSVMNQ2IVF5Q6BJOIUHBIX6FXG`) appears at
   the 2012-08-05 02:12:40 UTC capture (also held through 2012-09-05),
   labeled **"Final Results for Election"**, Total Ballots Cast **14,274**
   (42.5%) -- the EXACT certified final from the SoS SoV. This is the
   bracket-proof pattern (self-described late-night report + later capture
   overwritten to the exact certified total) already used for the 2012/2014/
   2016 general rows in this file.

CDX queries used:
`http://web.archive.org/cdx/search/cdx?url=acm.co.lake.ca.us/elections/results/&matchType=prefix&from=20120401&to=20120801&output=json&limit=100`
and a narrower `from=20120501&to=20121231` query scoped to `result23.htm`
directly (both curl, 2s pauses). `index22.htm` (captured same day) was
checked and ruled out: it is report #22, the November 8, 2011 general
district election, not this primary.

**Arithmetic.** 10,427 / 14,274 = **73.05%** (2dp percent units).
This is HIGHER than Lake's own 2012 presidential GENERAL (70.18%), which is
internally plausible for this county (this dossier's later items show the
primary share is consistently close to, and sometimes above, the adjacent
general's share for Lake -- unlike SF's calibration where primaries usually
track lower; treat as a genuine county-level pattern, not an error, since
the arithmetic and both legs of plateau evidence are independently solid).

**Draft row** (for `data/research/election-night/lake-ca.json`, NOT applied):
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": 10427,
  "certified_final": 14274,
  "election_night_pct": 73.05,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20120609045640id_/http://acm.co.lake.ca.us:80/elections/results/result23.htm",
  "confidence": "primary",
  "note": "PLATEAU = county's own numbered results-report system (acm.co.lake.ca.us/elections/results/result23.htm, report #23 = the June 5 2012 Presidential Primary per its index23.htm title block, same overwrite-in-place system as this county's 2012/2014/2016 GENERAL rows). Internal header: 'Election Results as of 06/06/2012 at 12:19:31 AM' (past-midnight tail of election night). 'Completed Precincts: 70 of 70' (100%). 'Total Ballots Cast 10,427 (31.1%)' = Precinct 4,787 + Absentee 5,640. NON-CIRCULAR LEG (RUNBOOK 8): three Wayback captures of the SAME URL (2012-06-09, 2012-06-20, 2012-07-05) carry an IDENTICAL content digest, proving the page held byte-for-byte unchanged for nearly a month after election night; the next distinct capture (2012-08-05, held again through 2012-09-05) is titled 'Final Results for Election', Total Ballots Cast 14,274 (42.5%) -- the exact SoS-certified total, proving the county overwrites this URL in place as the canvass proceeds and that 10,427 is genuinely the pre-canvass, election-night state. Certified final 14,274 voters (CA SoS Voter Participation Statistics by County: 4,781 precinct + 9,493 VBM). Pct = 10,427/14,274 = 73.05%. Lake never adopted epollbook or ASV (n/a both legs, control county)."
}
```

**Draft VERIFY.md line** (Lake County table, if/when a Lake section is added
to VERIFY.md; no such section exists yet -- Lake's generals in lake-ca.json
are not currently in VERIFY.md's table either, per repo state at build
time; flagging this as a pre-existing gap, not something this pass caused):
`| 2012 | presidential-primary | 10,427 | 14,274 | 73.05% | primary | https://web.archive.org/web/20120609045640id_/http://acm.co.lake.ca.us:80/elections/results/result23.htm |`

**Plateau verdict: CONFIRMED.** Self-description (past-midnight "Election
Results as of" timestamp, 100% precincts) PLUS TWO independent legs: (a)
multi-capture digest-identical hold for a month, (b) later capture
overwritten to the exact certified total under the "Final Results for
Election" label. Meets the RUNBOOK 8 bar cleanly, same evidentiary strength
as the 2012/2014-general CONFIRMED rows.

---

## Item 2 of 6: 2014-06-03 Statewide Primary (Governor)

**Certified final (denominator).** CA SoS Statement of Vote, "Voter
Participation Statistics by County" PDF:
`https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf`
(misspelling "particpiation" intact, same as the county-established 2014
GENERAL SoV path already in lake-ca.json). Lake County line: Precincts 70,
Eligible to Register 49,002, Registered Voters 33,987, Precinct Voters
5,153, Vote-By-Mail Voters 10,395, **Total Voters 15,548**, Turnout
(Registered) 45.75%, Turnout (Eligible) 31.73%. **certified_final = 15,548.**

**Plateau numerator.** Same numbered results-report system
(`acm.co.lake.ca.us/elections/results/result26.htm`; report #26; internal
page title itself reads "LAKE COUNTY / Statewide Direct Primary Election /
June 3, 2014", confirming the report without needing a separate index
lookup -- no `index26.htm` capture survives in this window, but the report's
own embedded election name/date is unambiguous).
Source URL used:
`https://web.archive.org/web/20140607235741id_/http://acm.co.lake.ca.us:80/elections/results/result26.htm`
Internal header: **"Election Results as of 06/04/2014 at 12:27:47 AM"**
(past-midnight tail of election night). "Completed Precincts: 70 of 70"
(100%). "Total Ballots Cast **9,703** (28.5%)" = Precinct Ballots Cast
4,542 + Absentee Ballots Cast 5,161.

**Plateau-holding evidence (RUNBOOK 8).** The SAME URL's only later Wayback
capture (2014-07-19 09:21:19 UTC, 6 weeks after election night) is titled
**"Final Results for Election"**, Total Ballots Cast **15,548** (45.7%) --
the EXACT certified final from the SoS SoV -- proving the county overwrites
this URL in place as the canvass proceeds and that 9,703 is genuinely the
pre-canvass, election-night state (its absentee subtotal, 5,161, is far
below the eventual certified 10,395 VBM; ~5,234 more VBM ballots were
processed post-election-night). Same overwrite-in-place pattern
independently confirmed for this county's 2012/2014/2016 GENERAL rows and
this dossier's 2012 PRIMARY item.

CDX query used:
`http://web.archive.org/cdx/search/cdx?url=acm.co.lake.ca.us/elections/results/&matchType=prefix&from=20140401&to=20140801&output=json&limit=200`
(returned exactly two `result26.htm` captures plus one unrelated
`index22.htm`, which was checked and ruled out as report #22 -- a different,
earlier report number, not this primary's index).

**Arithmetic.** 9,703 / 15,548 = **62.41%** (2dp percent units). Notably
lower than this dossier's 2012 primary (73.05%), consistent with Lake's own
generals also showing 2014 slightly below 2012 on the general side (69.72%
vs 70.18%) -- i.e., the primary/general RELATIVE pattern is internally
consistent year to year for this county, not an anomaly.

**Draft row** (for `data/research/election-night/lake-ca.json`, NOT applied):
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": 9703,
  "certified_final": 15548,
  "election_night_pct": 62.41,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20140607235741id_/http://acm.co.lake.ca.us:80/elections/results/result26.htm",
  "confidence": "primary",
  "note": "PLATEAU = county's own numbered results-report system (acm.co.lake.ca.us/elections/results/result26.htm, report #26, self-titled 'LAKE COUNTY / Statewide Direct Primary Election / June 3, 2014'). Internal header: 'Election Results as of 06/04/2014 at 12:27:47 AM' (past-midnight tail of election night). 'Completed Precincts: 70 of 70' (100%). 'Total Ballots Cast 9,703 (28.5%)' = Precinct 4,542 + Absentee 5,161. NON-CIRCULAR LEG (RUNBOOK 8): the SAME URL's only later Wayback capture (2014-07-19, six weeks after election night) is titled 'Final Results for Election', Total Ballots Cast 15,548 (45.7%) -- the exact SoS-certified total, proving the county overwrites this URL in place and that 9,703 is genuinely pre-canvass (absentee subtotal 5,161 is far below the eventual certified 10,395 VBM). Same overwrite-in-place pattern as this county's 2012/2014/2016 GENERAL rows and the 2012 PRIMARY row. Certified final 15,548 voters (CA SoS Voter Participation Statistics by County: 5,153 precinct + 10,395 VBM). Pct = 9,703/15,548 = 62.41%. Lake never adopted epollbook or ASV (n/a both legs, control county)."
}
```

**Draft VERIFY.md line:**
`| 2014 | statewide-primary | 9,703 | 15,548 | 62.41% | primary | https://web.archive.org/web/20140607235741id_/http://acm.co.lake.ca.us:80/elections/results/result26.htm |`

**Plateau verdict: CONFIRMED.** Self-description (past-midnight "Election
Results as of" timestamp, 100% precincts) PLUS the same-URL-overwritten-to-
certified-final leg (identical evidentiary form to the already-CONFIRMED
2012/2014-general rows and this dossier's Item 1).

---

## Item 3 of 6: 2016-06-07 Presidential Primary

**Certified final (denominator).** CA SoS Statement of Vote, "Voter
Participation Statistics by County" PDF:
`https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf`
(drops the extra `sov/` path segment used by the 2016 GENERAL SoV, same
pattern as the 2012 GENERAL SoV path already in lake-ca.json -- confirmed
by direct fetch, 200 OK). Lake County line: Precincts 70, Eligible to
Register 48,604, Registered Voters 32,796, Precinct Voters 5,042,
Vote-By-Mail Voters 11,670, **Total Voters 16,712**, Turnout (Registered)
50.96%, Turnout (Eligible) 34.38%. **certified_final = 16,712.**

**Plateau numerator.** Numbered results-report system, now on
`publicapps.lakecountyca.gov` (the same host migration already documented
for the 2016 GENERAL row; confirmed here as already migrated by June 2016 --
no `acm.co.lake.ca.us` captures exist for this window at all). Report #29
confirmed by its `index29.htm` title block: "LAKE COUNTY / Presidential
Primary Election / June 7, 2016".
Source URL used:
`https://web.archive.org/web/20160611033803id_/http://publicapps.lakecountyca.gov:80/elections/results/result29.htm`
Internal header: **"Election Results as of 06/08/2016 at 01:33:15 AM"**
(past-midnight tail of election night), page explicitly labeled
"Completed Precincts: 70 of 70 - PRELIMINARY RESULTS" (100%). "Total
Ballots Cast **9,049** (27.6%)" = Precinct Ballots Cast 4,296 + Absentee
Ballots Cast 4,753.

**Plateau-holding evidence (RUNBOOK 8).** The SAME URL's only later Wayback
capture (2016-07-12 10:25:56 UTC, five weeks after election night) is
titled **"Final Results for Election"** / "Completed Precincts: 70 of 70 -
FINAL RESULTS", Total Ballots Cast **16,712** (51.0%) -- the EXACT
certified final from the SoS SoV (Registered Voters shown as 32,795 on the
county page vs 32,796 on the SoS PDF, a 1-voter reconciliation difference,
same class of routine county-vs-SoS discrepancy already noted for the 2016
GENERAL row's 9-ballot gap) -- proving the county overwrites this URL in
place as the canvass proceeds and that 9,049 is genuinely the pre-canvass,
election-night state (absentee subtotal 4,753 is far below the eventual
certified 11,670 VBM). Same overwrite-in-place pattern independently
confirmed for this county's 2012/2014/2016 GENERAL rows and this dossier's
2012/2014 PRIMARY items.

CDX queries used:
`http://web.archive.org/cdx/search/cdx?url=publicapps.lakecountyca.gov/elections/results/&matchType=prefix&from=20160401&to=20160801&output=json&limit=200`
(found result29.htm + index29.htm among many unrelated index/result files
for other reports, ruled out by number/title mismatch) and a check of
`acm.co.lake.ca.us/elections/results/` for the same window, which returned
zero captures (confirming the host migration predates June 2016).

**Arithmetic.** 9,049 / 16,712 = **54.15%** (2dp percent units). Close to
Lake's own 2016 presidential GENERAL (53.75%) -- the two presidential-year
contests (primary and general) landed almost identically that year, a
useful internal calibration point.

**Draft row** (for `data/research/election-night/lake-ca.json`, NOT applied):
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 9049,
  "certified_final": 16712,
  "election_night_pct": 54.15,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20160611033803id_/http://publicapps.lakecountyca.gov:80/elections/results/result29.htm",
  "confidence": "primary",
  "note": "PLATEAU = county's own numbered results-report system, on publicapps.lakecountyca.gov (already migrated from acm.co.lake.ca.us by June 2016), report #29 = June 7 2016 Presidential Primary per its index29.htm title block. Internal header: 'Election Results as of 06/08/2016 at 01:33:15 AM' (past-midnight tail of election night), page labeled 'Completed Precincts: 70 of 70 - PRELIMINARY RESULTS'. 'Total Ballots Cast 9,049 (27.6%)' = Precinct 4,296 + Absentee 4,753. NON-CIRCULAR LEG (RUNBOOK 8): the SAME URL's only later Wayback capture (2016-07-12, five weeks after election night) is titled 'Final Results for Election' / 'FINAL RESULTS', Total Ballots Cast 16,712 (51.0%) -- the exact SoS-certified total (Registered Voters 32,795 vs SoS 32,796, a routine 1-voter reconciliation gap), proving overwrite-in-place and that 9,049 is genuinely pre-canvass. Same pattern as this county's 2012/2014/2016 GENERAL rows and the 2012/2014 PRIMARY rows. Certified final 16,712 voters (CA SoS Voter Participation Statistics by County: 5,042 precinct + 11,670 VBM). Pct = 9,049/16,712 = 54.15%. Lake never adopted epollbook or ASV (n/a both legs, control county)."
}
```

**Draft VERIFY.md line:**
`| 2016 | presidential-primary | 9,049 | 16,712 | 54.15% | primary | https://web.archive.org/web/20160611033803id_/http://publicapps.lakecountyca.gov:80/elections/results/result29.htm |`

**Plateau verdict: CONFIRMED.** Self-description (past-midnight timestamp,
explicit "PRELIMINARY RESULTS" label, 100% precincts) PLUS the
same-URL-overwritten-to-certified-final leg.

---

## Item 4 of 6: 2018-06-05 Statewide Primary (Governor)

**Certified final (denominator).** CA SoS Statement of Vote, "Voter
Participation Statistics by County" PDF:
`https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf`.
Lake County line: Precincts 70, Eligible to Register 49,352, Registered
Voters 32,805, Precinct Voters 3,917, Vote-By-Mail Voters 10,202, **Total
Voters 14,119**, Turnout (Registered) 43.04%, Turnout (Eligible) 28.61%.
**certified_final = 14,119.**

**Plateau numerator.** Numbered results-report system on
`publicapps.lakecountyca.gov`. Report #35, self-titled "LAKE COUNTY / 2018
Statewide Direct Primary Election / June 5, 2018" -- this is the SAME
`result35.htm` URL the existing lake-ca.json 2018-GENERAL row's note
mentions checking and ruling out as "a DIFFERENT, earlier June 2018 primary
report, not usable [for the general]"; that earlier finding is confirmed
correct and is exactly the row this dossier item now sources.
Source URL used:
`https://web.archive.org/web/20180610025440id_/http://publicapps.lakecountyca.gov:80/elections/results/result35.htm`
Internal header: **"Election Results as of 06/06/2018 at 12:06:21 AM"**
(past-midnight tail of election night), page labeled "Completed Precincts:
70 of 70 PRELIMINARY RESULTS" (100%). "Total Ballots Cast **8,158** (24.9%)"
= Precinct Ballots Cast 3,397 + Absentee Ballots Cast 4,761.

**Plateau-holding evidence (RUNBOOK 8).** The SAME URL's only later Wayback
capture (2018-07-10 16:37:26 UTC, five weeks after election night) is
titled **"Final Results for Election"** / "COUNTY OF LAKE - Final Results",
Total Ballots Cast **14,119** (43.1%) -- the EXACT certified final from the
SoS SoV -- proving the county overwrites this URL in place as the canvass
proceeds and that 8,158 is genuinely the pre-canvass, election-night state
(absentee subtotal 4,761 is far below the eventual certified 10,202 VBM).
Same overwrite-in-place pattern independently confirmed for this county's
2012/2014/2016/2018 GENERAL rows and this dossier's 2012/2014/2016 PRIMARY
items.

CDX query used:
`http://web.archive.org/cdx/search/cdx?url=publicapps.lakecountyca.gov/elections/results/&matchType=prefix&from=20180401&to=20180801&output=json&limit=200`
(also surfaced `index35F.htm`, a "Final" index variant captured 2018-07-19,
not needed once the two `result35.htm` captures themselves established the
preliminary-to-final bracket).

**Arithmetic.** 8,158 / 14,119 = **57.78%** (2dp percent units). Sits
between this dossier's 2014 (62.41%) and 2016 (54.15%) primaries, and is
notably lower than Lake's own 2018 GENERAL (63.00%) that same year --
unlike 2016 where primary and general nearly matched.

**Draft row** (for `data/research/election-night/lake-ca.json`, NOT applied):
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 8158,
  "certified_final": 14119,
  "election_night_pct": 57.78,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20180610025440id_/http://publicapps.lakecountyca.gov:80/elections/results/result35.htm",
  "confidence": "primary",
  "note": "PLATEAU = county's own numbered results-report system on publicapps.lakecountyca.gov, report #35, self-titled 'LAKE COUNTY / 2018 Statewide Direct Primary Election / June 5, 2018' (this is the same result35.htm the 2018-GENERAL row's note independently identified and ruled OUT for that election, confirming it is this primary's report). Internal header: 'Election Results as of 06/06/2018 at 12:06:21 AM' (past-midnight tail of election night), page labeled 'Completed Precincts: 70 of 70 PRELIMINARY RESULTS'. 'Total Ballots Cast 8,158 (24.9%)' = Precinct 3,397 + Absentee 4,761. NON-CIRCULAR LEG (RUNBOOK 8): the SAME URL's only later Wayback capture (2018-07-10, five weeks after election night) is titled 'Final Results for Election' / 'COUNTY OF LAKE - Final Results', Total Ballots Cast 14,119 (43.1%) -- the exact SoS-certified total, proving overwrite-in-place and that 8,158 is genuinely pre-canvass. Same pattern as this county's 2012/2014/2016/2018 GENERAL rows and the 2012/2014/2016 PRIMARY rows. Certified final 14,119 voters (CA SoS Voter Participation Statistics by County: 3,917 precinct + 10,202 VBM). Pct = 8,158/14,119 = 57.78%. Lake never adopted epollbook or ASV (n/a both legs, control county)."
}
```

**Draft VERIFY.md line:**
`| 2018 | statewide-primary | 8,158 | 14,119 | 57.78% | primary | https://web.archive.org/web/20180610025440id_/http://publicapps.lakecountyca.gov:80/elections/results/result35.htm |`

**Plateau verdict: CONFIRMED.** Self-description (past-midnight timestamp,
explicit "PRELIMINARY RESULTS" label, 100% precincts) PLUS the
same-URL-overwritten-to-certified-final leg. (Note: this is a STRONGER
verdict than the existing 2018-GENERAL row, which was downgraded to
PLAUSIBLE for lacking a second capture of `result37.htm`; here the second
`result35.htm` capture exists and closes exactly that gap.)

---

## Item 5 of 6: 2022-06-07 Statewide Primary (Governor)

**Certified final (denominator).** CA SoS Statement of Vote, "Voter
Participation Statistics by County" PDF:
`https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf`.
Lake County line: Precincts 80, Eligible to Register 51,309, Registered
Voters 37,433, Precinct Voters 1,371, Vote-By-Mail Voters 12,099, **Total
Voters 13,470**, Turnout (Registered) 35.98%, Turnout (Eligible) 26.25%.
**certified_final = 13,470.**

**Plateau numerator.** The county's successor reporting system on
`publicapps2.lakecountyca.gov` (the "Count_HtmlCumulativeReport" Hart-style
cumulative report, the same system independently used for the 2022 GENERAL
row's corroborating page). This election used TWO distinct report URLs
(not a single overwritten URL like the 2012-2018 `acm`/`publicapps` numbered
system): an on-night URL and a separately-named certified-final URL.
Source URL used:
`https://web.archive.org/web/20220703175544id_/https://publicapps2.lakecountyca.gov/elections/results/results220607.html`
Internal header: **"Count_HtmlCumulativeReport / Cumulative-Election Night
Official Results / Run Time 12:16 AM / Run Date 06/08/2022 / County of
Lake, California / June 7, 2022, Statewide Direct Primary Election /
Unofficial Results"**. Precincts Reporting 80 of 80 (100.00%). The
top-of-page summary line reads "Registered Voters 4562 of 37412 = 12.19%"
-- this is the RUNBOOK 7.5 mislabeling gotcha (ballots cast mislabeled as
"Registered Voters"): every per-contest block on the page repeats "Voters
Ballots Registered Percent 4,562 37,412 12.19%" and the GOVERNOR contest's
own "Cast Votes: ... 4,443" + "Undervotes: ... 69" + "Overvotes: ... 50" =
4,562 exactly, confirming **4,562 is total ballots cast**, not registered
voters (37,412 is the registered-voter denominator, matching the SoS figure
37,433 to within 21, a routine county-vs-SoS reconciliation gap). Wayback
crawled this page on 2022-07-03 (26 days after election night), but its
own embedded "Run Date 06/08/2022 at 12:16 AM" proves the underlying report
file itself was never regenerated between election night and the crawl --
i.e. it is a genuinely frozen, unmodified election-night artifact, not a
later canvass state relabeled.

**Plateau-holding evidence (RUNBOOK 8).** A SEPARATE, differently-named URL
for the same election, `results_final_07-07-2022.html`, carries the header
**"Count_HtmlCumulativeReport / Final Cumulative Results Report / Official
Results / Run Time 2:15 PM / Run Date 07/07/2022 / ... / Official Results"**
with "Registered Voters 13470 of 37412 = 36.00%" -- and the GOVERNOR
contest total there (Cast Votes 13,103 + Undervotes 194 + Overvotes 133 +
Unqualified write-ins 40 = 13,470) confirms **13,470 ballots cast = the
EXACT certified final** from the SoS SoV. The county's own naming
convention ("Unofficial ... Election Night Official Results" for the night
file vs "Final Cumulative Results Report ... Official Results" for the
one-month-later file, filename literally containing "final" and dated
07-07-2022, exactly the 30-day post-election certification deadline)
brackets the night report as the true election-night plateau, the same
non-circular bracket-proof form already used across every row in this
dossier.

CDX query used:
`http://web.archive.org/cdx/search/cdx?url=publicapps2.lakecountyca.gov/elections/results/&matchType=prefix&from=20220501&to=20220901&output=json&limit=200`
(returned exactly these two files; no other election-night-dated capture of
`results220607.html` exists to independently corroborate the hold via a
second crawl, so this row rests on the internal-Run-Date argument above plus
the two-file bracket, not a two-crawl digest match).

**Arithmetic.** 4,562 / 13,470 = **33.87%** (2dp percent units). Close to
Lake's own 2022 GENERAL that same cycle (38.51%), both well below this
dossier's 2012/2014/2016/2018 primaries (73.05% / 62.41% / 54.15% / 57.78%)
-- consistent with the reporting-delay pattern the 2022 GENERAL row's
Lake County News source explicitly documents for this county that cycle
("Challenges with the county's website led to results not being posted
online until late Tuesday night"), not a tech-adoption confound (Lake never
adopted epollbook/ASV/VCA, n/a both legs, control county).

**Draft row** (for `data/research/election-night/lake-ca.json`, NOT applied):
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 4562,
  "certified_final": 13470,
  "election_night_pct": 33.87,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20220703175544id_/https://publicapps2.lakecountyca.gov/elections/results/results220607.html",
  "confidence": "primary",
  "note": "PLATEAU = the county's Count_HtmlCumulativeReport results page for this election (publicapps2.lakecountyca.gov/elections/results/results220607.html; the successor system to the acm/publicapps numbered-report series, same system independently used for the 2022 GENERAL row's corroborating page). Internal header: 'Cumulative-Election Night Official Results / Run Time 12:16 AM / Run Date 06/08/2022 / Unofficial Results', Precincts Reporting 80 of 80 (100.00%). Top-line reads 'Registered Voters 4562 of 37412 = 12.19%' -- RUNBOOK 7.5 mislabeling gotcha: 4,562 is actually total ballots cast (confirmed by the GOVERNOR contest's Cast Votes 4,443 + Undervotes 69 + Overvotes 50 = 4,562 exactly), 37,412 is the registered-voter denominator. Wayback crawled this page 2022-07-03, but its own 'Run Date 06/08/2022' proves the file was never regenerated after election night. NON-CIRCULAR LEG (RUNBOOK 8): a separately-named URL for the same election, results_final_07-07-2022.html, is headered 'Final Cumulative Results Report / Official Results / Run Date 07/07/2022' with 'Registered Voters 13470 of 37412 = 36.00%' (GOVERNOR contest ballots cast 13,470 exactly) -- the exact SoS-certified total, bracketing the night file as the true election-night plateau via the county's own naming/dating convention. Certified final 13,470 voters (CA SoS Voter Participation Statistics by County: 1,371 precinct + 12,099 VBM). Pct = 4,562/13,470 = 33.87% -- close to Lake's own 2022 GENERAL (38.51%) that cycle, both depressed by the county's documented website/reporting delays that year (see 2022-GENERAL row note), not a tech-adoption confound. Lake never adopted epollbook or ASV (n/a both legs, control county)."
}
```

**Draft VERIFY.md line:**
`| 2022 | statewide-primary | 4,562 | 13,470 | 33.87% | primary | https://web.archive.org/web/20220703175544id_/https://publicapps2.lakecountyca.gov/elections/results/results220607.html |`

**Plateau verdict: CONFIRMED.** Self-description (explicit "Election Night
Official Results" label with a past-midnight Run Date/Time, 100% precincts,
"Unofficial Results") PLUS the two-file bracket to a separately labeled
"Final ... Official Results" report showing the exact certified total.
Slightly weaker than the acm-system rows in that this is a two-URL bracket
rather than a same-URL multi-capture hold, but it meets the RUNBOOK 8 bar
(an independent, non-circular leg: "an official release stating the number
as the election-night total" / "the county's own posting schedule
bracketing the report").

---

## Item 6 of 6: 2024-03-05 Presidential Primary

**Certified final (denominator).** CA SoS Statement of Vote, "Voter
Participation Statistics by County" PDF:
`https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf`.
Lake County line: Precincts 48, Eligible to Register 50,320, Registered
Voters 36,604, Precinct Voters 1,550, Vote-By-Mail Voters 14,076, **Total
Voters 15,626**, Turnout (Registered) 42.69%, Turnout (Eligible) 31.05%.
**certified_final = 15,626.**

**REJECTED numerator candidate (checked first, ruled out).** The county's
`publicapps2.lakecountyca.gov/elections/results/results240305.html`
Count_HtmlCumulativeReport page: only one Wayback capture exists
(2024-03-18 15:46:25 UTC), and its own internal header reads **"Election
Night Cumulative POST ELECTION / Run Time 12:28 PM / Run Date 03/12/2024"**
-- explicitly labeled "POST ELECTION" with a Run Date SEVEN DAYS after the
March 5 election, "Registered Voters 7859 of 36561 = 21.50%" (same RUNBOOK
7.5 mislabeling as the 2022 primary: 7,859 is ballots cast, not registered
voters; 36,561 is the registered-voter denominator). This is a documented
PARTIAL-CANVASS update, exactly the same trap the 2024-GENERAL row's note
already flags for the sibling `results241105.html` page ("8 days
post-election and already a partial-canvass update ... explicitly NOT used
as the numerator"). NOT used as the numerator here for the identical
reason.

**Plateau numerator (actual source used).** Lake County News, "Pyska,
Rasmussen, Harry top respective races; Hess, Owen in dead heat for
District 1 supervisor seat" (archived copy used; live lakeconews.com blocks
curl per the pattern already documented for this county's 2022/2024
GENERAL rows):
`https://web.archive.org/web/20240312101554id_/https://lakeconews.com/news/78087-pyska-rasmussen-harry-top-respective-races-hess-owen-in-dead-heat-for-district-1-supervisor-seat`
Quoting the Registrar of Voters directly: **"The Lake County Registrar of
Voters issued its final update for the first night of counting at 1:19
a.m. Wednesday."** ... "The initial estimate was that voter turnout for
the Tuesday primary was **19.64%, or 7,181 out of 36,561 registered
voters**." (36,561 registered voters matches the SoS figure 36,604 to
within 43, a routine county-vs-SoS reconciliation gap; 7,181/36,561 =
19.6399...% rounds to the article's stated 19.64%, confirming internal
consistency.) A second, corroborating article from the same batch,
"Aguiar-Curry, Thompson handily wins primary races"
(`https://web.archive.org/web/20240312092438id_/https://lakeconews.com/news/78084-aguiar-curry-thompson-handily-wins-primary-races`),
independently confirms the same reporting cadence: "with 48 of 48 precincts
reporting, ... according to Registrar of Voter tallies posted early
Wednesday" / "as of 1 a.m. Wednesday" -- the same overnight-report pattern
already documented for this county's 2022 (1 a.m.) and 2024-general (4
a.m.) rows.

**Plateau-holding evidence (RUNBOOK 8).** The article explicitly attributes
to the Registrar of Voters (not merely the reporter's judgment) that this
WAS **"its final update for the first night of counting"**, immediately
followed by: "The official canvass period will now begin, with the
Registrar of Voters Office planning to certify the election by April 4."
This is an official release stating the number as the election-night total
(the Registrar's own designation of "final ... first night" mediated
through direct quotation, the same evidentiary form already used and
accepted for the 2022-GENERAL row). The REJECTED county-page capture above
additionally shows the count grew from this night figure (7,181) to a
higher post-election value (7,859) by March 12, consistent with -- but not
formal proof of, per RUNBOOK 8's strict leg list -- the night figure being
a true pre-canvass state; this growth-consistency is noted as corroborating
context, not counted as an independent bracket leg. UNLIKE the 2012/2014/
2016/2018 PRIMARY items and the 2022 PRIMARY item in this dossier, there is
NO same-URL-overwritten-to-certified-final leg and NO multi-capture
digest-hold available here (only one capture of the county page exists, and
it is a different, later, non-matching figure).

CDX queries used:
`http://web.archive.org/cdx/search/cdx?url=publicapps2.lakecountyca.gov/elections/results/&matchType=prefix&from=20240201&to=20240601&output=json&limit=200`
(found the single POST-ELECTION county-page capture, ruled out) and
`http://web.archive.org/cdx/search/cdx?url=lakeconews.com/news/&matchType=prefix&from=20240305&to=20240320&output=json&limit=200&filter=statuscode:200`
(surfaced the two corroborating primary-results articles among ~150
unrelated local-news captures from the same window).

**Arithmetic.** 7,181 / 15,626 = **45.96%** (2dp percent units). Higher
than Lake's own 2024 GENERAL that same year (29.34%) -- plausible given a
much smaller primary ballot (fewer contests to process per ballot) even
under the same documented capacity/backlog conditions that depressed the
2022 and 2024 GENERAL rows; flagged as a genuine within-year primary/
general asymmetry, not treated as an error.

**Draft row** (for `data/research/election-night/lake-ca.json`, NOT applied):
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 7181,
  "certified_final": 15626,
  "election_night_pct": 45.96,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20240312101554id_/https://lakeconews.com/news/78087-pyska-rasmussen-harry-top-respective-races-hess-owen-in-dead-heat-for-district-1-supervisor-seat",
  "confidence": "secondary",
  "note": "PLATEAU = the last election-night preliminary report, per Lake County News ('Pyska, Rasmussen, Harry top respective races...', archived copy used; live lakeconews.com blocks curl) quoting the Registrar of Voters directly: 'The Lake County Registrar of Voters issued its final update for the first night of counting at 1:19 a.m. Wednesday.' ... 'The initial estimate was that voter turnout for the Tuesday primary was 19.64%, or 7,181 out of 36,561 registered voters.' A second article from the same batch (news/78084, 'Aguiar-Curry, Thompson handily wins primary races') corroborates the same reporting cadence ('as of 1 a.m. Wednesday', '48 of 48 precincts reporting ... tallies posted early Wednesday'). REJECTED alternative: the county's own publicapps2.lakecountyca.gov/elections/results/results240305.html page's only surviving Wayback capture (2024-03-18) is internally headered 'Election Night Cumulative POST ELECTION / Run Date 03/12/2024' -- explicitly labeled POST ELECTION, seven days post-election, 'Registered Voters 7859 of 36561' (RUNBOOK 7.5 mislabeling: 7,859 is ballots cast) -- a documented partial-canvass update higher than 7,181, NOT used as the numerator, same trap as the sibling 2024-GENERAL row's results241105.html rejection. Certified final 15,626 voters (CA SoS Voter Participation Statistics by County: 1,550 precinct + 14,076 VBM). Pct = 7,181/15,626 = 45.96% -- higher than Lake's own 2024 GENERAL (29.34%) that year, plausibly reflecting a much smaller primary ballot under the same capacity constraints, not a tech confound. Lake never adopted epollbook or ASV (n/a both legs, control county). (2020 deliberately excluded as a COVID universal-VBM outlier, same as every other row in this dataset.)"
}
```

**Draft VERIFY.md line:**
`| 2024 | presidential-primary | 7,181 | 15,626 | 45.96% | secondary | https://web.archive.org/web/20240312101554id_/https://lakeconews.com/news/78087-pyska-rasmussen-harry-top-respective-races-hess-owen-in-dead-heat-for-district-1-supervisor-seat |`

**Plateau verdict: PLAUSIBLE (not CONFIRMED).** Self-description is solid:
the article directly quotes the Registrar of Voters' own designation of
this as "its final update for the first night of counting," past-midnight
(1:19 a.m.), 48-of-48 precincts. BUT per the same RUNBOOK-8 discipline
already applied to this county's 2018-GENERAL row (downgraded from an
initially-proposed CONFIRMED to PLAUSIBLE for lacking an independent
leg), no strict non-circular leg is obtainable here: the sole county-page
capture is a different (higher, later) figure, not a same-count hold, and
no Clarity/version-bracket system exists for Lake. This is WEAKER evidence
than the 2022-GENERAL row (which had this SAME article-quote form PLUS an
independently-held county-page figure) and WEAKER than every acm/publicapps
numbered-report row in this dossier (which all have the same-URL-
overwritten-to-final bracket). Kept as `confidence: "secondary"` (news
quoting officials, per RUNBOOK 5.3) with a genuine, well-evidenced number,
but flagged for operator review before treating it as CONFIRMED-grade.

---

## Summary table (draft, for a future Lake section of VERIFY.md)

| Date | Type | Night ballots | Certified final | Share | Confidence | Plateau verdict |
|---|---|---:|---:|---:|---|---|
| 2012-06-05 | presidential-primary | 10,427 | 14,274 | 73.05% | primary | CONFIRMED |
| 2014-06-03 | statewide-primary | 9,703 | 15,548 | 62.41% | primary | CONFIRMED |
| 2016-06-07 | presidential-primary | 9,049 | 16,712 | 54.15% | primary | CONFIRMED |
| 2018-06-05 | statewide-primary | 8,158 | 14,119 | 57.78% | primary | CONFIRMED |
| 2022-06-07 | statewide-primary | 4,562 | 13,470 | 33.87% | primary | CONFIRMED |
| 2024-03-05 | presidential-primary | 7,181 | 15,626 | 45.96% | secondary | PLAUSIBLE |

Every row is a control-county (`vs_epollbook`/`vs_asv` = "n/a" both legs;
Lake never adopted e-pollbooks or ASV) statewide PRIMARY, extending the
generals-only record already in `data/research/election-night/lake-ca.json`.
No null rows were needed: a plateau numerator was recoverable for all six
primaries, either from the county's own numbered/dated report system
(2012-2018, 2022) or from a Lake County News article directly quoting the
Registrar of Voters (2024).

**Nothing in this dossier has been applied to the repo.** To promote it:
add the six draft rows to `data/research/election-night/lake-ca.json`
(surgical text edits per RUNBOOK 2, not a whole-file rewrite), add a Lake
County table + detail bullets to `VERIFY.md` (a section that does not
currently exist there for this county's generals either -- a pre-existing
gap, not introduced by this pass), add six verdict records to
`plateau_review.json`, then run the full pipeline in RUNBOOK 3 (validator,
`build_county_night.py`, denominator/numerator verifiers, report
regeneration, pytest, vitest) before committing.
