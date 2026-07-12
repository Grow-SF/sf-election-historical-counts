# Plateau adjudication (controller read, 2026-07-02)

Every sourced election-night numerator was adjudicated by the controller
model directly (no subagents) for the metric-defining question the
presence checks cannot answer: is the cited report the LAST report
posted on election night (the plateau)? Non-circular evidence was
gathered per row: Clarity CDN version brackets, internal report
timestamps and last-of-night titles, county posting schedules, held
counts in later captures, and Wayback CDX capture histories.

Verdicts: 48 CONFIRMED, 3 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 1 REFUTED_AND_CORRECTED.

UPDATE (2026-07-10, gap-triage recoveries): two newly recovered rows added
(santa-clara-ca 2016 and 2018, both CONFIRMED via live-CDN version
brackets) and santa-clara-ca 2014 re-adjudicated PLAUSIBLE ->
REFUTED_AND_CORRECTED (the live Clarity CDN recovered the true overnight
plateau that supersedes the documented ceiling). Running totals: 50
CONFIRMED, 2 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 2 REFUTED_AND_CORRECTED.

UPDATE (2026-07-10, Lake County control-county integration): six new rows
added for lake-ca (2012, 2014, 2016, 2018, 2022, 2024), a never-adopter
control county. Five verdicts CONFIRMED (2012/2014/2016 via the county's
own overwrite-in-place numbered report page held or superseded across two
independent Wayback captures; 2022/2024 via on-the-record registrar-office
news quotes naming the number as the last election-night count, 2022
additionally corroborated by a held county-page count). One verdict
(2018) downgraded from the source dossier's proposed CONFIRMED to
PLAUSIBLE on review: its only corroborating observation is a single
Wayback capture whose crawl date diverges from the page's own internal
timestamp, not a genuine second independent leg per section 8. Running
totals: 55 CONFIRMED, 3 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 2
REFUTED_AND_CORRECTED.

UPDATE (2026-07-10, Del Norte County control-county integration): five new
rows added for del-norte-ca (2014, 2016, 2018, 2022, 2024; 2012 is a
documented null, no plateau_review entry), a never-adopter control county
(second control alongside Lake). All five verdicts CONFIRMED: 2016/2018/2024
via a document self-labeled 'Election Night Final' (or equivalent) plus the
report series' next file being days later at a higher, differently-labeled
count; 2014 via the county's own dated index page provably listing only two
pre-Final releases (no numbering-pattern inference needed) plus the 3-day
gap to a relabeled Final that matches the certified total exactly; 2022 via
four strictly-increasing same-night numbered reports plus a 6-day gap to a
relabeled Final report. All five numerator PDFs are scanned (no text layer)
Canon-photocopier reports, verified by 150dpi visual render (render_verified.json
entries added). Two dossier corrections made on integration review: the 2016
row's cited numerator URL pointed at the wrong release (Release 6, whose
number is the certified total, not Release 4's night count) and has been
corrected to Release 4's own exact matched Wayback capture; the 2022 row's
PDF was mischaracterized as native-text and is in fact the same
no-text-layer scan template as the other years. Running totals: 60
CONFIRMED, 3 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 2 REFUTED_AND_CORRECTED.

UPDATE (2026-07-10, Mendocino County control-county integration): four new
rows added for mendocino-ca (2014, 2016, 2018, 2024; 2012 and 2022 are
documented nulls, no plateau_review entries), a never-adopter control county
(third control alongside Lake and Del Norte). All four verdicts CONFIRMED:
2016/2018 via the county's own self-labeled 'FINAL ELECTION NIGHT REPORT' /
'Election Night Final Report' held byte-identical (2016) or superseded weeks
later at the certified total (2018) in a later Wayback capture of the same
URL; 2014 via a local-news article quoting the county's own report verbatim
('4th and Final Election Night Report') plus the same report series' next
Wayback state (weeks later, certified) recovered independently of the news
source; 2024 via a news article that explicitly self-describes the number as
election-night-tabulated (both in its body and in an author comment) plus an
independent Wayback capture of the same county report series 8 days later at
a materially higher count. The source dossier's proposed fifth sourced row,
2012 (secondary, PLAUSIBLE, a back-calculated ballot count derived from a
double-rounded percentage in a 2016 retrospective article), was downgraded to
null on integration review: the underlying source states no ballot count for
2012, only a rounded ~51%-of-~36,400 recollection in an unrelated later
article, which fails both the floor test (no actual on-night report exists)
and the direct-citation bar; the derived 18,401-ballot figure would present
false precision from two independently rounded inputs. Flagged for human
review; see the mendocino-ca.json 2012 row note for the full derivation.
Running totals: 63 CONFIRMED, 3 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 2
REFUTED_AND_CORRECTED.

UPDATE (2026-07-10, Tehama County control-county integration): two new
rows added for tehama-ca (2022, 2024; 2012/2014/2016/2018 are documented
nulls, no plateau_review entries), a fifth control county (alongside SF,
Lake, Del Norte, and Mendocino), never having adopted e-pollbooks or ASV.
Both verdicts CONFIRMED: 2022 via the county's own numbered report series
(Third Unofficial Precinct Report, internal timestamp 10:37:39 PM election
night) bracketed by the next report in the series (Fourth) 40 hours later
with nothing interposed; 2024 via the county's own numbered report series
(3rd Unofficial Report, internal timestamp 12:17:11 AM, 40/40 precincts)
bracketed by a 27-day gap to the next surviving report, the canvass-complete
Final Official Report. One dossier correction made on integration review:
the 2022 row's claimed percentage (57.06%) was arithmetically wrong
(11,878/20,819 = 57.05%, not 57.06%) and its note incorrectly asserted the
Third Unofficial Precinct Report does not state 100% of precincts reporting
-- direct re-fetch of the cited Wayback capture (2026-07-10) shows it
already reads 'Precincts Reported: 40 of 40 (100.00%)', identical to the
Fourth report's framing; both the pct and the note's reasoning were
corrected (the VBM-composition explanation for the low share still holds).
Running totals: 66 CONFIRMED, 3 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 2
REFUTED_AND_CORRECTED.

UPDATE (2026-07-10, running-total audit): recounted ALL verdicts directly
from the current plateau_review.json (73 rows total, matching the 73
sourced rows the validator reports). Counts: 66 CONFIRMED, 3 PLAUSIBLE, 2
REFUTED_AS_PLATEAU, 2 REFUTED_AND_CORRECTED -- identical to the Tehama
block's running total immediately above; no new sourced rows landed since
Tehama (the subsequent Colusa County integration added six documented
nulls, no plateau_review entries). Correction to the historical record: the
Mendocino block's stated running total (63 CONFIRMED, above) undercounted
by one -- a direct recount of plateau_review.json at that commit (1ec5652)
gives 64 CONFIRMED (71 rows total: 64/3/2/2), not 63. The error was
isolated to that one arithmetic statement and did not propagate forward:
the Tehama block's total was computed independently from the data and is,
and remains, correct as stated.

UPDATE (2026-07-10, Riverside County statewide-primary integration): the
first batch of PRIMARY election rows lands in the dataset. Three new
sourced rows for riverside-ca (2016-06-07, 2018-06-05, 2022-06-07;
2012-06-05/2014-06-03/2024-03-05 are documented nulls, no plateau_review
entries). All three adjudicated CONFIRMED on integration review; none
downgraded. All three follow the same pattern already CONFIRMED for this
county's Nov 2022 general: a self-labeled 'Official Semi-Final Results' /
'Semi-Official Election Results' report at a late-night/past-midnight
timestamp, with the report series' next file landing days later (2016,
2018) or the following afternoon then daily (2022) at a higher count --
the non-circular report-series leg. Two of the three (2018, 2022) were
recovered not from Wayback (which only preserved mid-canvass captures of
this dated-PDF series) but from docs.voteinfo.net, a still-live document
CDN that continues to serve Riverside's historical dated reports years
after the front-end site was redesigned; both were additionally pushed
through web.archive.org/save/ and content-verified (Total Ballots Cast /
Voters Cast figures re-fetched and matched) so the citations resolve to
permanent snapshots rather than a live, mutable URL. Running totals: 69
CONFIRMED, 3 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 2 REFUTED_AND_CORRECTED (76
sourced rows total).

UPDATE (2026-07-10, San Diego County statewide-primary integration): four
new sourced rows for san-diego-ca (2016-06-07, 2018-06-05, 2022-06-07,
2024-03-05; 2012-06-05/2014-06-03 are documented nulls, no plateau_review
entries), completing the first primaries batch alongside Riverside above.
All four adjudicated CONFIRMED; none downgraded. 2018-06, 2022-06, and
2024-03 follow the same self-describing-header-plus-growth/schedule
pattern already CONFIRMED for this county's Nov generals. 2016-06-07 is
the weakest of the four on first read (only one Wayback capture near
election night exists, so the "held" observation is a single artifact's
internal-timestamp-vs-crawl-time gap, not two independent captures) but is
still legitimately CONFIRMED because its real non-circular leg is
different: the NEXT available capture (12 days later) shows the count
grown substantially, which is the same report-series-next-file-later leg
accepted throughout this file (e.g. del-norte-ca, mendocino-ca). The
intraday-freeze observation is recorded as secondary corroboration only,
not the basis. One classification note carried forward rather than
resolved: san-diego-ca 2024-03-05's vs_epollbook is 'post' (San Diego's
e-pollbook/vote-center/ENR platform launch is independently dated to this
exact primary, ElectionID 15, immediately preceding the Nov 2022 general's
ElectionID 16), but its vs_asv is a coarse adopted_year=2024 inference:
the county's own ASV tech-adoption record could not pin ASV's first
election to March vs November 2024 from primary sources, and that
ambiguity is carried verbatim in the row's note rather than silently
resolved. Running totals: 73 CONFIRMED, 3 PLAUSIBLE, 2 REFUTED_AS_PLATEAU,
2 REFUTED_AND_CORRECTED (80 sourced rows total).

UPDATE (2026-07-10, mega-integration commit 1 -- SoS adjudications + human
verdicts): three committed rows re-adjudicated against the CA SoS
county-reporting-status page and two rows added. napa-ca 2014-11-04
PLAUSIBLE -> CONFIRMED and riverside-ca 2024-11-05 REFUTED_AS_PLATEAU ->
CONFIRMED (both now cite the SoS status page's bracket-confirmed overnight
plateau, replacing a county 10:30 PM floor and a next-day-afternoon ceiling
respectively; riverside's comparable:false and flag removed, making it a
usable pre/post datapoint). del-norte-ca 2016-11-08 stays CONFIRMED with its
numerator moved to the same SoS page (8,155 -> 8,450, frozen 5 days then
jumping to the certified 9,790). Two new sourced rows: mendocino-ca
2012-11-06 PLAUSIBLE (maintainer-approved Anderson Valley Advertiser ~51%
approximation, restored from null; the machine numerator check reports
NOT_FOUND as expected for a derived value) and santa-clara-ca 2012-06-05
REFUTED_AS_PLATEAU (documented ceiling, comparable:false, freeze test failed
on retry). Running totals: 75 CONFIRMED, 3 PLAUSIBLE, 2 REFUTED_AS_PLATEAU,
2 REFUTED_AND_CORRECTED (82 sourced rows total).

| County | Date | Verdict | Basis | Evidence |
|---|---|---|---|---|
| del-norte-ca | 2014-11-04 | CONFIRMED | last surviving on-night release (provably the last of only 2 pre-Final releases per the county's own dated index page), still labeled Unofficial; next report 3 days later relabeled Final at the exact certified total | Release 2/3, footer timestamp 11/4/2014 10:05 PM, 18/18 precincts (100%), Total Voters 6,539/12,743 (51.31%); the index page (re-verified 2026-07-10) lists exactly Release 1, Release 2, Release 3-Final; Release 3 (11/7/2014, 3 days later) retitled 'General Election Final', Total Voters 7,332/12,743 -- exactly the SoS certified figure -- confirming Release 2 was the last report before the canvass resumed and completed |
| del-norte-ca | 2016-11-08 | CONFIRMED | CA SoS county-reporting-status page FENU-equivalent figure, frozen 5 days then jumping to the exact certified final; supersedes the county's own slightly-earlier Release 4 as the last election-night value fed to the state | CORRECTION 2026-07-10: landed value moved from county Release 4 (8,155, 10:47:49 PM) to the SoS status page's 8,450 (Last Report 'Nov 8 11:38 p.m.'), Del Norte row 18/18 (100%) at capture 20161110185817, byte-identical (frozen) across 6 captures through 20161116014606 (5 days), then jumps to 9,790 = the certified final exactly (matching the county's own Nov 16 Release 6) at Nov 16 9:40 a.m. The 51-minute gap is late-tabulated/provisional ballots folded into the county's EMS feed after it declared Election Night Final on its public page. Release 4's read (8,155) was itself accurate; retained as history in the row note |
| del-norte-ca | 2018-11-06 | CONFIRMED | document explicitly titled 'ELECTION NIGHT FINAL REPORT'; next report 3 days later explicitly retitled to note late VBM additions | Release 4/5, 11/6/2018 9:42:38 PM, 18/18 precincts (100%), Registered Voters 7,127/14,289 (49.88%); Release 5 (11/9/2018, 3 days later) retitled 'Election Results With Late Vote By Mail', Times Cast 8,121/14,289 -- confirms Release 4 was the last report before the canvass resumed |
| del-norte-ca | 2022-11-08 | CONFIRMED | last of 4 same-night numbered reports (strictly increasing timestamps, all election night); next artifact ('Final Unofficial Report' / 5th Report) 6 days later at a much higher count | Release 4/4, internal CreationDate 11/8/2022 9:40:53 PM, page stamp 'Data Refreshed 11/8/2022 9:39 PM', Turnout 6,312/15,024; 'Final Unofficial Report' (11/14/2022, 6 days later) Turnout 8,286/15,024 -- confirms Release 4 was the last report before the canvass resumed. Re-verified 2026-07-10: this PDF is also a no-text-layer scan (a working draft mischaracterized it as native-text), read visually |
| del-norte-ca | 2024-11-05 | CONFIRMED | document explicitly titled 'Election Night Report ... Final Report'; next release 3 days later retitled 'Update' at a much higher count | Release 3/6, 11/5/2024 10:05:17 PM, 19/19 precincts (100%), Voters Cast 6,719/15,117 (44.45%); Release 4 (11/8/2024, 3 days later) retitled '11/08/2024 Update / Unofficial Results', Voters Cast 9,102/15,117 (60.21%) -- confirms Release 3 was the last report before the canvass resumed |
| fresno-ca | 2016-11-08 | CONFIRMED | frozen GEMS live page, held past night | header 'Unofficial Final Results ... 11/9/2016 1:42:19 AM' at 592/592 precincts; the Nov 12 capture (the artifact) still shows the 1:42 AM report |
| fresno-ca | 2024-11-05 | CONFIRMED | official county summary PDF, end of night | internal stamp 11/6/2024 12:30:26 AM at 478/478 (100%); next archived report (11/7 3:28 PM) jumped to 222,324 |
| lake-ca | 2012-11-06 | CONFIRMED | self-described late-night timestamp + later capture of same URL overwritten to the certified final | result24.htm 2012-11-10 capture: 'Preliminary Election Results as of 11/06/2012 at 11:59:41 PM', 70/70 precincts, Total Ballots Cast 16,622; same URL's only later capture (2012-12-25) reads 'Final Results for Election ... Total Ballots Cast 23,685' (= certified final exactly) |
| lake-ca | 2014-11-04 | CONFIRMED | self-described past-midnight timestamp + byte-identical later capture of same URL (digest match) three weeks after election night | result27.htm 2014-11-08 capture: 'Election Results as of 11/05/2014 at 12:41:23 AM', 70/70 precincts, Total Ballots Cast 12,593; the 2014-11-30 capture of the same URL has the IDENTICAL digest AJH6HNMV3OVULKQXIFCRFEJFVHRZPJFN; only the 2015-01-27 capture changes to 'Final Results for Election ... Total Ballots Cast 18,061' (= certified final exactly) |
| lake-ca | 2016-11-08 | CONFIRMED | self-described past-midnight 'PRELIMINARY RESULTS' timestamp + only later capture of same URL (6 weeks on, no intermediate captures) labeled 'FINAL RESULTS' at the certified total | result30.htm 2016-11-12 capture: 'Election Results as of 11/09/2016 at 12:49:48 AM', 'PRELIMINARY RESULTS', 70/70 precincts, Total Ballots Cast 13,484; the 2016-12-24 capture of the same URL (next in CDX, 6 weeks later) reads 'Final Results for Election ... FINAL RESULTS ... Total Ballots Cast 25,094' (matches SoS certified 25,085 within 9 ballots) |
| lake-ca | 2018-11-06 | PLAUSIBLE | self-described past-midnight 'PRELIMINARY RESULTS' timestamp; the only later observation is a single Wayback crawl (not a second independent capture) whose crawl date diverges from the page's own generation timestamp -- suggestive but not one of the section 8 non-circular legs | result37.htm's sole Wayback capture (2018-11-29) reads 'Election Results as of 11/07/2018 at 12:14:30 AM', 'PRELIMINARY RESULTS', 70/70 precincts, Total Ballots Cast 13,522; DOWNGRADED from the dossier's proposed CONFIRMED (2026-07-10 integration review): the crawl-date/internal-timestamp divergence (22 days) is a single-capture inference, not a genuine second data point like the two-capture holds confirmed for this county's 2012/2014/2016 rows; no Clarity bracket, second capture, county posting schedule, or separate official release is obtainable |
| lake-ca | 2022-11-08 | CONFIRMED | on-the-record registrar-office quote naming the number as the last preliminary count of election night, plus the number holding unchanged across two Wayback captures of the county's own results page 12+ days apart | Lake County News (archived): 'By 1 a.m. Wednesday, Valadez's office had issued the last preliminary ballot count of the night... 7,842 ballots, or 21.2% of Lake County's 37,165 registered voters'; publicapps2.lakecountyca.gov/elections/results/results221108.html shows 'Registered Voters 7842 of 37165 = 21.10%, Precincts Reporting 80 of 80' identically in both its 2022-11-18 and 2022-11-30 captures |
| lake-ca | 2024-11-05 | CONFIRMED | on-the-record news report naming the number as the election-night preliminary count for all precincts, with an independent second-article snippet pinning the report to 4 a.m. the morning after election day; the alternative county-page capture was checked and explicitly rejected as already-canvass-contaminated | Lake County News (archived): 'preliminary election results for the 48 precincts ... as of early Wednesday morning ... 7,960 ballots, or 20.99% ... have been counted'; companion article snippet: 'By 4 a.m. on November 6, 2024, initial counts of the county's 48 precincts had been completed'; results241105.html's earliest Wayback capture (2024-11-17, Run Date 11/14/2024) shows a higher 8,641 and was rejected as post-election-night |
| los-angeles-ca | 2012-11-06 | CONFIRMED | RR/CC semi-final press release states the election-night total | 'On Election Night a total of 2,368,283 ballots were counted' plus 792,658 estimated remaining |
| los-angeles-ca | 2014-11-04 | CONFIRMED | RR/CC semi-final press release states the election-night total | 'A total of 1,147,248 ballots were processed and counted' (semi-final official results, Nov 5 release) |
| los-angeles-ca | 2016-11-08 | CONFIRMED | RR/CC semi-final press release states the election-night total | 'A total of 2,306,321 ballots were processed and counted' (semi-final official, Nov 9 release) |
| los-angeles-ca | 2018-11-06 | CONFIRMED | RR/CC semi-final press release states the election-night total | 'A total of 1,975,855 ballots were processed and counted' (semi-official results, Nov 7 release) |
| los-angeles-ca | 2022-11-08 | CONFIRMED | RR/CC semi-final press release states the election-night total | 'A total of 1,318,093 ballots were processed and counted' (Semi-Final Results Announced, Nov 9) |
| los-angeles-ca | 2024-11-05 | CONFIRMED | RR/CC semi-final press release states the election-night total | 'A total of 2,615,541 ballots were processed and counted' (Semi-Final Results Announced, Nov 6) |
| madera-ca | 2016-11-08 | CONFIRMED | static county results page, frozen | 'Election Results as of 11/08/2016 at 11:31:17 PM' at 102/102; the Nov 12 capture still shows it (note documents an identical Dec 30 capture) |
| madera-ca | 2018-11-06 | CONFIRMED | clarity version bracket, re-derived from CDN | cited v220349 stamped 11/6/2018 11:53:23 PM; next v220492 stamped 11/7 9:34 AM with BC held at 28,159 |
| madera-ca | 2022-11-08 | CONFIRMED | clarity version bracket, re-derived | cited v311779 stamped 11/8/2022 10:44:29 PM; v312400's settings enumerate zero versions between it and 11/10 4:11 PM (BC 25,243) |
| madera-ca | 2024-11-05 | CONFIRMED | clarity version bracket, re-derived | cited v353191 stamped 11/5/2024 11:51:26 PM; next v353996 stamped 11/8 3:25 PM (BC 44,900) |
| mendocino-ca | 2012-11-06 | PLAUSIBLE | maintainer-approved approximation; self-description consistent but no independent bracket/hold leg obtainable (RUNBOOK 8) | MAINTAINER OVERRIDE 2026-07-10: restored from null. The Anderson Valley Advertiser election-night-2016 live-blog (theava.com/archives/62338) cites 2012's 'preliminary election night results ... based on about 51% of about 36,400 votes cast', using the same construction as its independently-verified 2016 figure (23.58%, matching the county's own current.htm) in the same article. Value = round(36,080 x 0.51) = 18,401 = 51.00%, secondary, comparable. Coarse whole-percent approximation; machine numerator check reports NOT_FOUND (derived integer not literally in source) as expected and documented. No Wayback bracket exists for 2012 to confirm it was the LAST report of the night, hence PLAUSIBLE not CONFIRMED |
| mendocino-ca | 2014-11-04 | CONFIRMED | county report self-describes (verbatim-quoted by news) + later Wayback capture of the same URL shows a materially higher, weeks-later count | "'4th and Final Election Night Report' 1am 11/05/2014 ... 11,402 votes cast, 24.02% of registered voters" (theava.com); current.htm's next Wayback state (Nov 30 capture, dated 11/21/14 internally) reads 25,017 |
| mendocino-ca | 2016-11-08 | CONFIRMED | county report self-describes + later capture same count | 'THIS IS THE FINAL ELECTION NIGHT REPORT', internal timestamp 11/09/16 01:55:06, Cards Cast 12,032; Nov 23 capture of same URL is byte-identical |
| mendocino-ca | 2018-11-06 | CONFIRMED | county report self-describes + next-captured state is weeks later and materially different | 'Election Night Final Report', internal timestamp 11/07/18 00:48:58, Cards Cast 15,819; Dec 2 capture of same URL headed 'FINAL OFFICIAL RESULTS 11/29/18', Cards Cast 33,966 (= SoV certified) |
| mendocino-ca | 2024-11-05 | CONFIRMED | news source explicitly self-describes as election-night-tabulated + independent Wayback capture of the same county report series shows a materially higher, 8-days-later count | MendoFever: '15,611 ... released shortly before midnight'; author comment: 'tabulated by Election night'; currentFR.pl Nov 22 capture (Run Date 11/13/2024, 'OFFICIAL UPDATE #1') reads 24,062 |
| napa-ca | 2012-11-06 | CONFIRMED | county report self-describes | 'Last Updated: November 6, 2012 11:29 PM (Last of the Night)' |
| napa-ca | 2014-11-04 | CONFIRMED | CA SoS county-reporting-status page's Final Election Night Unofficial (FENU) figure, doubly bracket-confirmed (frozen 2 days, then a correctly-identified CCU jump) | CORRECTION 2026-07-10: landed value moved from the county's 10:30 PM web report (18,286, now retained as a floor in the row note) to the SoS FENU 19,515 (Last Report 'Nov 4 11:14 p.m.'). Napa row 167/167 (100.0%) / 19,515 / 27.7% at capture 20141105141649, byte-identical (frozen) 2 days later at 20141107083801, then jumps to 35,800 (CCU) on Nov 14. The county's own 10:30 PM page showed statewide precinct tallying essentially not yet started (0/164), so the SoS captured a later, fuller moment of the SAME continuous election-night count. Non-circular leg: 2-day freeze before the CCU jump |
| napa-ca | 2016-11-08 | CONFIRMED | county last-report title | 'Unofficial Election Night Last Report', stamp 11/8/2016 11:06:38 PM |
| napa-ca | 2018-11-06 | CONFIRMED | county titled last-of-night series | 'LAST UNOFFICIAL ELECTION NIGHT REPORT', stamp 11/6/2018 10:52:52 PM, 170/170 |
| napa-ca | 2022-11-08 | CONFIRMED | county titled last-of-night series | 'Last Unofficial Election Night Report', stamp 11/8/2022 10:46:50 PM, 200/200 |
| napa-ca | 2024-11-05 | CONFIRMED | county titled last-of-night series | 'Last Unofficial Election Night Report', stamp 11/6/2024 12:35:53 AM, 204/204 |
| nevada-ca | 2012-11-06 | CONFIRMED | county release republished verbatim | 'workers in the election office tabulated a total of 31,275 votes by 1 a.m. that night'; canvass remainder reconciles to certified |
| nevada-ca | 2014-11-04 | CONFIRMED | morning-after report of the official night tally | 'The final election night tally of votes comes in at 22,366 of 61,706' |
| nevada-ca | 2016-11-08 | CONFIRMED | morning-after report of the official cumulative | '34,728 ballots counted as of tonight' described as the final update on election night |
| nevada-ca | 2018-11-06 | CONFIRMED | morning-after county statement | 'At the end of election night, 26,956 ballots have been counted' |
| nevada-ca | 2022-11-08 | CONFIRMED | morning-after county explainer | 'Last night ... 28,824 were counted'; the 26,213 first tranche explicitly distinguished |
| nevada-ca | 2024-11-05 | CONFIRMED | county's own last-of-three night report | 'Third Report - Cumulative Results' 11:24:31 PM at 118/118; sequence First 8:02 PM (11,749), Second 10:03 PM, Third 15,486 |
| orange-ca | 2012-11-06 | CONFIRMED | county-archived night report with past-midnight stamp | UNOFFICIAL RESULTS cumulative stamped 11/07/2012 12:47:06 AM |
| orange-ca | 2014-11-04 | CONFIRMED | county-archived night report with past-midnight stamp | stamp 11/05/2014 01:55:59 AM |
| orange-ca | 2016-11-08 | CONFIRMED | county-archived night report with past-midnight stamp | stamp 11/09/2016 01:55:57 AM |
| orange-ca | 2018-11-06 | CONFIRMED | county-archived night report with past-midnight stamp | stamp 11/07/2018 01:48:27 AM |
| orange-ca | 2022-11-08 | CONFIRMED | county-archived night report with past-midnight stamp | Cumulative Results Report, data stamp 12:04 AM (PDF printed 11/09/2022) |
| orange-ca | 2024-11-05 | CONFIRMED | county-archived night report with past-midnight stamp | data stamp 12:48 AM (PDF printed 11/06/2024) |
| placer-ca | 2014-11-04 | CONFIRMED | GEMS night-final report | stamp 11/05/14 00:36:57 at 369/369; county nav labels it 'Election Night Final' |
| placer-ca | 2016-11-08 | CONFIRMED | GEMS night report | stamp 11/09/16 00:29:40 (12:29 AM after the Nov 8 election) at 363/363 |
| placer-ca | 2018-11-06 | REFUTED_AS_PLATEAU | page provably tracked the canvass | cited render is 11/09/18 15:15 (113,380); NEW EVIDENCE: the Nov 21 capture of the same page shows Cards Cast 162,802, so the page re-rendered with canvass data and the Nov 9 figure likely absorbs early canvass; 113,380 i |
| riverside-ca | 2016-06-07 | CONFIRMED | self-labeled 'Official Semi-Final Results', last of a numbered on-night release series, next report 2 days later at a higher count | Summary_Update8.pdf, Run Date/Time 6/8/16 3:18:26 AM, Total Ballots Cast 249,970; Summary_Update9.pdf (next in series) is 6/10/16 4:49:49 PM, two days later, 279,815 |
| riverside-ca | 2018-06-05 | CONFIRMED | self-labeled 'Official Semi-Final Results', last of a numbered on-night release series, next report 2 days later at a higher count | Summary8.pdf, Run Date/Time 6/6/18 6:25:10 AM, Total Ballots Cast 193,152; Summary9.pdf (next in series) is 6/8/18 5:22:39 PM, two days later, 231,461; recovered from live docs.voteinfo.net CDN, re-archived to Wayback (snapshot 20260710205406) |
| riverside-ca | 2022-06-07 | CONFIRMED | self-labeled 'Semi-Official Election Results', first to reach 100% precincts reported, next report jumps to the following afternoon then daily cadence | ElectionSummaryReportRPT6.pdf, 6/8/2022 12:31:41 AM, Voters Cast 191,996, Precincts 795/795 (100.00%); RPT7 (next) is 6/8/2022 4:52:51 PM then daily through RPT16 = 375,610 (certified); recovered from live docs.voteinfo.net CDN, re-archived to Wayback (snapshot 20260710205902) |
| riverside-ca | 2022-11-08 | CONFIRMED | 2 AM report held until the canvass | Last-Modified 11/09/2022 02:04 PST (inside the hourly-until-3am window); held as the live page until the 11/11 canvass update (300,498); local news corroboration |
| riverside-ca | 2024-11-05 | CONFIRMED | CA SoS county-reporting-status page's ~5 a.m. overnight plateau, frozen 12+ hours across 3 captures before the next-day canvass bump | CORRECTION 2026-07-10: landed value moved from the livevoterturnout ENR next-day-afternoon ceiling (611,101, 'Updated 11/6/2024 5:35:21 PM', comparable=false) to the SoS 547,742 (Last Report 'Nov 6 5:02 a.m.'). SoS timeline: 100% precincts (1,345/1,345) at 466,214, climbing 481,400 (12:05 AM) -> 496,024 -> 510,623 (2:05 AM) -> 547,742 (5:02 AM), which then held byte-identical across 20241106133254 / 154527 / 171813 (~6:32 AM to ~5:18 PM Nov 6) before the next capture jumped to the same 611,101 next-day figure. Non-circular leg: 12+ hour freeze then the canvass bump; comparable:false and flag removed, row now usable |
| sacramento-ca | 2012-11-06 | PLAUSIBLE | distinct on-time capture exists but is currently unservable | CDX shows a distinct Nov 8 2012 8:53 PM PST capture (digest CYR7..., 10,563 bytes) differing from the 2013 FINAL-report capture (10,647 bytes); Wayback replay now 302-aliases it to 2013-02-15, which is why machine fetche |
| sacramento-ca | 2014-11-04 | CONFIRMED | Hart summary with night run time, held | 'Run Date:11/05/14 RUN TIME:12:33 AM', BALLOTS CAST TOTAL 195,317; the Nov 6 capture still shows it |
| sacramento-ca | 2018-11-06 | CONFIRMED | night report held ~22 hours | report stamp 11/7/2018 1:50:09 AM; capture Nov 7 3:44 PM PST still shows it; the county page's ballots-cast mislabel is documented |
| sacramento-ca | 2022-11-08 | CONFIRMED | county schedule plus midnight report | summary stamped 11/9/2022 12:00:20 AM; the county's own schedule text says updates run until about 12:00 am; captured 1:11 AM PST the same night |
| sacramento-ca | 2024-11-05 | CONFIRMED | county schedule plus night report | summary stamped 11/6/2024 1:56:14 AM; captured 7:17 AM PST before any next-day update |
| san-bernardino-ca | 2024-11-05 | CONFIRMED | county posting schedule brackets the capture | header 'Final Unofficial Election Night Results'; the 2:41 PM capture sits between the county's 10 AM final-EN posting and the 4 PM canvass resume; Provisional 0 confirms pre-canvass; render-verified 434,108 at 2,872/2,8 |
| san-diego-ca | 2016-06-07 | CONFIRMED | self-describing overnight UNOFFICIAL timestamp plus growth in the next capture 12 days later (the non-circular leg; single-capture intraday freeze noted but not the basis) | election.xml date=06-08-16 time=03:21:51 etype=UNOFFICIAL, US SENATOR tcounted=468340 (recurs across ~15 universal contests); next capture (06-16-16) shows tcounted 689,612 |
| san-diego-ca | 2018-06-05 | CONFIRMED | self-describing 'ELECTION NIGHT FINAL' header plus growth in the next capture | 'UNOFFICIAL RESULTS - ELECTION NIGHT FINAL', stamp 6/6/2018 04:44:12 AM, Ballots Cast 406,501; next capture (6/7/2018 5:15:43 PM, ~37.5h later) shows 427,779 |
| san-diego-ca | 2018-11-06 | CONFIRMED | night stamp, captured the same night | stamp 11/7/2018 01:42:41 AM; captured 4:06 AM PST |
| san-diego-ca | 2022-06-07 | CONFIRMED | night stamp plus next-post schedule, corroborated by the companion XML feed's next report landing exactly on schedule | stamp 6/8/2022 12:39:38 AM, Ballots Cast 416,748, 'NEXT POST 6/9/22 BY 5PM'; summary_15.xml next report GeneratedDate 2022-06-09T16:49:11-07:00 = 475,054; first election on SD's ENR/e-pollbook platform (ElectionID 15) |
| san-diego-ca | 2022-11-08 | CONFIRMED | self-describing final plus next-post schedule | 'FINAL UNOFFICIAL ELECTION NIGHT RESULTS ... NEXT POST 11/10/2022 BY 5 P.M.', stamp 11/9/2022 2:21:25 AM |
| san-diego-ca | 2024-03-05 | CONFIRMED | self-describing 'FINAL UNOFFICIAL ELECTION NIGHT RESULTS' header, held across three captures spanning 14h, plus canvass resumed exactly on schedule | stamp 3/6/2024 12:46:42 AM, Ballots Counted 425,572 held 20240306103630/145646/223911; 3/8 capture shows stamp 3/7/2024 4:48:18 PM, 492,333 |
| san-diego-ca | 2024-11-05 | CONFIRMED | self-describing final | 'UNOFFICIAL ELECTION NIGHT FINAL (ESTIMATED BALLOTS TO BE PROCESSED: 590,000)', stamp 11/6/2024 2:52:20 AM |
| san-mateo-ca | 2012-11-06 | CONFIRMED | county-archived night turnout report | 'Precinct Turnout Total Voters Unofficial' stamped 11/07/2012 12:07 AM |
| san-mateo-ca | 2014-11-04 | CONFIRMED | county-archived night turnout report | stamped 11/04/2014 11:36 PM |
| san-mateo-ca | 2016-11-08 | CONFIRMED | county-archived night turnout report | stamped 11/09/2016 03:03 AM |
| san-mateo-ca | 2018-11-06 | CONFIRMED | on-night capture of the final report | captured 4:11 AM PST Nov 7; rendered widget shows 'Total Ballots Cast 111,637'; the page defines the 'Final Election Night Report' release; render-verified |
| san-mateo-ca | 2022-11-08 | CONFIRMED | self-describing final plus next-update schedule | 'Semi-Official Results - Final Election Night Report - Next update on Thursday, November 10', stamp 11/9/2022 3:17:37 AM |
| san-mateo-ca | 2024-11-05 | CONFIRMED | self-describing final plus next-update schedule | 'Final Election Night Report - Next update on Thursday, November 7', stamp 11/6/2024 2:18:48 AM |
| santa-clara-ca | 2012-06-05 | REFUTED_AS_PLATEAU | earliest archived capture of the only election-night channel (legacy pre-Clarity sccgov.org page) is already ~23h post-poll-close with precincts at 100% and a once-daily canvass cadence; kept only as a documented ceiling per RUNBOOK 5.2, comparable:false | Wayback CDX for sccgov.org/elections/results/jun2012/ has zero captures before 2012-06-07 12:28 PM PDT; that capture's internal 'Last Updated' is 6/6/2012 7:02:03 PM, Completed Precincts 874/874 (100%), 234,342 ballots. FREEZE TEST (retry 2026-07-10): the very next capture (20120608222327, 6/7 4:43 PM) reads 268,370, then 284,025 (6/8), growing to the certified 292,713 which froze July 3 - Dec 8 -- so 234,342 is a mid-canvass Wednesday-evening ceiling, not a frozen night state. Not-adopted scaling estimate (Nov-2012 own ratio reversed) implies ~223,152/76.24%; maintainer default is the 234,342/80.06% ceiling. FLAG for manual operator: missed June 5-6 capture and/or Mercury News NewsBank quote could upgrade |
| santa-clara-ca | 2012-11-06 | CONFIRMED | long-night report held in a later capture | stamped 11/7/2012 4:14:04 AM PST; the Nov 10 capture still shows it |
| santa-clara-ca | 2014-11-04 | REFUTED_AND_CORRECTED | clarity live-CDN version walk recovers the true overnight plateau, superseding the documented ceiling | cited ceiling ver 148095 (11/5 5:08:58 PM, BC 251,620) is a next-day canvass-start report; the live CDN (unlike Wayback) still serves the overnight versions' JSON -- v147908 (11/5 4:00:59 AM PST, BC 235,062) is the last of the continuous night sequence (pace collapses to +624 in the final 63 min, then a 13-hour gap to 148095); corrected 251,620 -> 235,062, comparable=false removed |
| santa-clara-ca | 2016-11-08 | CONFIRMED | clarity live-CDN version bracket: cadence break in the immediately following version | v182800 (11/9 10:28:40 AM PST, BC 443,269) is the last of a continuous ~hourly overnight sequence from v181922 (11/8 7:43 PM); the next version v182869 (3:41 PM) breaks cadence (+7,333 over 5h13m vs an overnight pace of 5,700-15,400/hr) |
| santa-clara-ca | 2018-11-06 | CONFIRMED | clarity live-CDN version bracket: adjacent official versions in the settings array, 9h22m gap | v220444 (11/7 6:37:33 AM PST, BC 304,303, precincts 1,098/1,098) is immediately followed in the electionsettings versions array by v220630 (3:59:46 PM, BC 306,086, +1,783 only) |
| santa-clara-ca | 2022-11-08 | CONFIRMED | clarity version bracket, re-derived | cited v311769 stamped 11/8/2022 10:41:38 PM; next v312163 stamped 11/9 4:36 PM (BC 309,580) |
| santa-clara-ca | 2024-11-05 | REFUTED_AND_CORRECTED | clarity version walk recovers the true plateau | cited v353583 (11/6 4:46 PM, BC 468,395) is a next-day canvass bump; the night sequence is v353205 11:57 PM BC 459,487 then v353227 12:16 AM BC 460,325 (last of the night, held through v353516 at 1:10 PM); corrected to 4 |
| tehama-ca | 2022-11-08 | CONFIRMED | internal generation timestamp (10:37:39 PM) squarely inside the election-night window plus the county's own posting schedule brackets it: the next report (Fourth) is dated 40 hours later with nothing interposed | 'Third Unofficial Precinct Report', 11/8/2022 10:37:39 PM, Precincts Reported 40 of 40 (100.00%), Voters Cast 11,878 of 37,115; Fourth Unofficial Precinct Report dated 11/10/2022 3:02:05 PM, Voters Cast 14,317 -- both re-fetched and confirmed 2026-07-10 |
| tehama-ca | 2024-11-05 | CONFIRMED | self-describes as end-of-night (3rd of 3 Unofficial Reports, 100.00% precincts, 12:17:11 AM internal timestamp) plus the county's own posting schedule brackets it: no 4th/5th/Final-Unofficial file exists anywhere, and the next file (Final Official Report) is 27 days later at exactly the certified final | '3rd Unofficial Report', 11/6/2024 12:17:11 AM, Precincts Reported 40 of 40 (100.00%), Voters Cast 13,109 of 37,488; Final Official Report dated 12/3/2024 10:26:46 AM, Voters Cast 26,867 (= SoS SoV certified final) -- both re-fetched and confirmed 2026-07-10 |

## Non-CONFIRMED rows (read these first)

### lake-ca 2018-11-06: PLAUSIBLE

self-described past-midnight 'PRELIMINARY RESULTS' timestamp; the only later observation is a single Wayback crawl (not a second independent capture) whose crawl date diverges from the page's own generation timestamp -- suggestive but not one of the section 8 non-circular legs.

result37.htm's sole Wayback capture (2018-11-29) reads 'Election Results as of 11/07/2018 at 12:14:30 AM', 'PRELIMINARY RESULTS', 70/70 precincts, Total Ballots Cast 13,522; DOWNGRADED from the dossier's proposed CONFIRMED (2026-07-10 integration review): the crawl-date/internal-timestamp divergence (22 days) is a single-capture inference, not a genuine second data point like the two-capture holds confirmed for this county's 2012/2014/2016 rows; no Clarity bracket, second capture, county posting schedule, or separate official release is obtainable

### mendocino-ca 2012-11-06: PLAUSIBLE

maintainer-approved approximation; self-description consistent but no independent bracket/hold leg obtainable (RUNBOOK 8).

MAINTAINER OVERRIDE (2026-07-10): restored from null. The Anderson Valley Advertiser election-night-2016 live-blog (theava.com/archives/62338) cites 2012's 'preliminary election night results ... based on about 51% of about 36,400 votes cast', using the same construction as its independently-verified 2016 figure (23.58%, matching the county's own current.htm) in the same article. Value = round(36,080 x 0.51) = 18,401 = 51.00%, secondary, comparable. Coarse whole-percent approximation; the machine numerator check reports NOT_FOUND (the derived integer is not literally in the source) as expected and documented. No Wayback bracket exists for 2012 to confirm it was the LAST report of the night, hence PLAUSIBLE not CONFIRMED.

### placer-ca 2018-11-06: REFUTED_AS_PLATEAU

page provably tracked the canvass.

cited render is 11/09/18 15:15 (113,380); NEW EVIDENCE: the Nov 21 capture of the same page shows Cards Cast 162,802, so the page re-rendered with canvass data and the Nov 9 figure likely absorbs early canvass; 113,380 is a ceiling on the unarchived night plateau; flagged comparable=false

### santa-clara-ca 2012-06-05: REFUTED_AS_PLATEAU

earliest archived capture of the only election-night channel (legacy pre-Clarity sccgov.org page) is already ~23h post-poll-close with precincts at 100% and a once-daily canvass cadence; kept only as a documented ceiling per RUNBOOK 5.2, comparable:false.

Wayback CDX for sccgov.org/elections/results/jun2012/ has zero captures before 2012-06-07 12:28 PM PDT; that capture's internal 'Last Updated' is 6/6/2012 7:02:03 PM, Completed Precincts 874/874 (100%), 234,342 ballots. FREEZE TEST (retry 2026-07-10): the very next capture (20120608222327, 6/7 4:43 PM) reads 268,370, then 284,025 (6/8), growing to the certified 292,713 which froze July 3 - Dec 8 -- so 234,342 is a mid-canvass Wednesday-evening ceiling, not a frozen night state. A computed-but-not-adopted scaling estimate (Santa Clara's own Nov-2012 ratio reversed) implies ~223,152/76.24%; maintainer default is the 234,342/80.06% ceiling pending final say. FLAG for manual operator: a missed June 5-6 capture and/or a Mercury News NewsBank quote could upgrade this to a real plateau.

### sacramento-ca 2012-11-06: PLAUSIBLE

distinct on-time capture exists but is currently unservable.

CDX shows a distinct Nov 8 2012 8:53 PM PST capture (digest CYR7..., 10,563 bytes) differing from the 2013 FINAL-report capture (10,647 bytes); Wayback replay now 302-aliases it to 2013-02-15, which is why machine fetches see the Nov 30 report; the note's reading (Run Date 11/07/12 12:49 AM, 328,516 at 1,106/1,106) is temporally coherent but machine-unverifiable today

### santa-clara-ca 2014-11-04: REFUTED_AND_CORRECTED

clarity live-CDN version walk recovers the true overnight plateau, superseding the documented ceiling.

Original 2026-07-02 verdict was PLAUSIBLE (documented ceiling: next-day canvass-start report; ver 148095 'Last updated 11/5/2014 5:08:58 PM'; the overnight versions' JSON was never crawled; note estimated the true plateau near 239,000; ceiling 251,620 flagged comparable=false). CORRECTION (2026-07-10, gap-triage): the live Clarity CDN, unlike Wayback, still serves the overnight versions' JSON -- v147908 (11/5 4:00:59 AM PST, BC 235,062) is the last of the continuous night sequence (pace collapses to +624 in the final 63 min, then a 13-hour gap to 148095); corrected 251,620 -> 235,062 (58.16%), comparable=false removed, confidence upgraded to primary.

### santa-clara-ca 2024-11-05: REFUTED_AND_CORRECTED

clarity version walk recovers the true plateau.

cited v353583 (11/6 4:46 PM, BC 468,395) is a next-day canvass bump; the night sequence is v353205 11:57 PM BC 459,487 then v353227 12:16 AM BC 460,325 (last of the night, held through v353516 at 1:10 PM); corrected to 460,325

---

UPDATE (2026-07-10, CA SoS status-page sweep integration -- 2012 elections): 16 new sourced rows landed across 11 counties (of the 18 panel counties besides San Francisco, the control), recovered from the CA SoS per-county reporting-status page (`vote.sos.ca.gov/returns/status` 2012-2018, `electionresults.sos.ca.gov/returns/status` 2022+) across 2 statewide election(s) in this batch. 11 CONFIRMED (frozen-capture or single-capture-then-jump bracket per RUNBOOK 8), 5 PLAUSIBLE (self-describing FENU/plateau state but no independent capture available in the CDX window to bracket it). Source: `scratchpad/sos-status-sweep.md` (research sweep) and `scratchpad/sweep_applylist.json` (computed apply-list, this batch's subset); every cell's capture citation and freeze/jump evidence below was independently re-derived from the raw per-capture timeline data (not merely transcribed from the sweep's prose), matching exact ballots-cast values with zero mismatches. Running totals: 86 CONFIRMED, 8 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 2 REFUTED_AND_CORRECTED (98 sourced rows, matching the validator).

### del-norte-ca 2012-06-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Del Norte row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 4,820, Last Report 'Jun 5 11:07 p.m.'. FROZEN: the identical Ballots Cast figure 4,820 recurs across 2 captures, 2012-06-08 22:26:55 UTC through 2012-06-17 19:21:15 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20120608222655->20120617192115 (to end of window)" (scratchpad/sos-status-sweep.md).

### del-norte-ca 2012-11-06: PLAUSIBLE

CA SoS status-page single-capture bracket (RUNBOOK 8).

Del Norte row at capture 20121110102540 (2012-11-10 10:25:40 UTC): 100.0% precincts, Ballots Cast 8,067, Last Report 'Nov 7 12:20 a.m.'. SINGLE CAPTURE at 2012-11-10 10:25:40 UTC carries this value. No later capture is available anywhere in the CDX window for this election to independently confirm the freeze; self-describing but unbracketed, grade PLAUSIBLE per RUNBOOK 8. Sweep bracket-evidence cross-check: "single capture 20121110102540, no later capture to confirm freeze" (scratchpad/sos-status-sweep.md).

### fresno-ca 2012-06-05: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Fresno row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 66,323, Last Report 'Jun 6 1:45 a.m.'. SINGLE CAPTURE at 2012-06-08 22:26:55 UTC carries this value. The next available capture (2012-06-17 19:21:15 UTC) jumps to 107,825 (Last Report 'Jun 15 2:59 p.m.'), confirming 66,323 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 107,825@Jun 15 2:59 p.m." (scratchpad/sos-status-sweep.md).

### fresno-ca 2012-11-06: PLAUSIBLE

CA SoS status-page single-capture bracket (RUNBOOK 8).

Fresno row at capture 20121110102540 (2012-11-10 10:25:40 UTC): 100.0% precincts, Ballots Cast 160,466, Last Report 'Nov 7 2:38 a.m.'. SINGLE CAPTURE at 2012-11-10 10:25:40 UTC carries this value. No later capture is available anywhere in the CDX window for this election to independently confirm the freeze; self-describing but unbracketed, grade PLAUSIBLE per RUNBOOK 8. Sweep bracket-evidence cross-check: "single capture 20121110102540, no later capture to confirm freeze" (scratchpad/sos-status-sweep.md).

### lake-ca 2012-06-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Lake row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 10,427, Last Report 'Jun 6 1:08 a.m.'. FROZEN: the identical Ballots Cast figure 10,427 recurs across 2 captures, 2012-06-08 22:26:55 UTC through 2012-06-17 19:21:15 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20120608222655->20120617192115 (to end of window)" (scratchpad/sos-status-sweep.md).

### los-angeles-ca 2012-06-05: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Los Angeles row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 765,552, Last Report 'Jun 6 4:41 a.m.'. SINGLE CAPTURE at 2012-06-08 22:26:55 UTC carries this value. The next available capture (2012-06-17 19:21:15 UTC) jumps to 920,096 (Last Report 'Jun 15 2:45 p.m.'), confirming 765,552 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 920,096@Jun 15 2:45 p.m." (scratchpad/sos-status-sweep.md).

### madera-ca 2012-06-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Madera row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 16,619, Last Report 'Jun 5 11:20 p.m.'. FROZEN: the identical Ballots Cast figure 16,619 recurs across 2 captures, 2012-06-08 22:26:55 UTC through 2012-06-17 19:21:15 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20120608222655->20120617192115 (to end of window)" (scratchpad/sos-status-sweep.md).

### madera-ca 2012-11-06: PLAUSIBLE

CA SoS status-page single-capture bracket (RUNBOOK 8).

Madera row at capture 20121110102540 (2012-11-10 10:25:40 UTC): 100.0% precincts, Ballots Cast 32,865, Last Report 'Nov 6 11:01 p.m.'. SINGLE CAPTURE at 2012-11-10 10:25:40 UTC carries this value. No later capture is available anywhere in the CDX window for this election to independently confirm the freeze; self-describing but unbracketed, grade PLAUSIBLE per RUNBOOK 8. Sweep bracket-evidence cross-check: "single capture 20121110102540, no later capture to confirm freeze" (scratchpad/sos-status-sweep.md).

### mendocino-ca 2012-06-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Mendocino row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 13,485, Last Report 'Jun 6 1:16 a.m.'. FROZEN: the identical Ballots Cast figure 13,485 recurs across 2 captures, 2012-06-08 22:26:55 UTC through 2012-06-17 19:21:15 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20120608222655->20120617192115 (to end of window)" (scratchpad/sos-status-sweep.md).

### napa-ca 2012-06-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Napa row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 19,147, Last Report 'Jun 5 11:03 p.m.'. FROZEN: the identical Ballots Cast figure 19,147 recurs across 2 captures, 2012-06-08 22:26:55 UTC through 2012-06-17 19:21:15 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20120608222655->20120617192115 (to end of window)" (scratchpad/sos-status-sweep.md).

### nevada-ca 2012-06-05: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Nevada row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 21,763, Last Report 'Jun 6 12:41 a.m.'. SINGLE CAPTURE at 2012-06-08 22:26:55 UTC carries this value. The next available capture (2012-06-17 19:21:15 UTC) jumps to 30,763 (Last Report 'Jun 15 5:36 p.m.'), confirming 21,763 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 30,763@Jun 15 5:36 p.m." (scratchpad/sos-status-sweep.md).

### placer-ca 2012-06-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Placer row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 62,087, Last Report 'Jun 6 12:42 a.m.'. FROZEN: the identical Ballots Cast figure 62,087 recurs across 2 captures, 2012-06-08 22:26:55 UTC through 2012-06-17 19:21:15 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20120608222655->20120617192115 (to end of window)" (scratchpad/sos-status-sweep.md).

### placer-ca 2012-11-06: PLAUSIBLE

CA SoS status-page single-capture bracket (RUNBOOK 8).

Placer row at capture 20121110102540 (2012-11-10 10:25:40 UTC): 100.0% precincts, Ballots Cast 127,593, Last Report 'Nov 6 11:47 p.m.'. SINGLE CAPTURE at 2012-11-10 10:25:40 UTC carries this value. No later capture is available anywhere in the CDX window for this election to independently confirm the freeze; self-describing but unbracketed, grade PLAUSIBLE per RUNBOOK 8. Sweep bracket-evidence cross-check: "single capture 20121110102540, no later capture to confirm freeze" (scratchpad/sos-status-sweep.md).

### riverside-ca 2012-06-05: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Riverside row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 189,087, Last Report 'Jun 6 1:42 a.m.'. SINGLE CAPTURE at 2012-06-08 22:26:55 UTC carries this value. The next available capture (2012-06-17 19:21:15 UTC) jumps to 232,279 (Last Report 'Jun 13 3:18 p.m.'), confirming 189,087 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 232,279@Jun 13 3:18 p.m." (scratchpad/sos-status-sweep.md).

### tehama-ca 2012-06-05: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Tehama row at capture 20120608222655 (2012-06-08 22:26:55 UTC): 100.0% precincts, Ballots Cast 9,993, Last Report 'Jun 6 12:06 a.m.'. SINGLE CAPTURE at 2012-06-08 22:26:55 UTC carries this value. The next available capture (2012-06-17 19:21:15 UTC) jumps to 13,968 (Last Report 'Jun 12 4:04 p.m.'), confirming 9,993 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 13,968@Jun 12 4:04 p.m." (scratchpad/sos-status-sweep.md).

### tehama-ca 2012-11-06: PLAUSIBLE

CA SoS status-page single-capture bracket (RUNBOOK 8).

Tehama row at capture 20121110102540 (2012-11-10 10:25:40 UTC): 100.0% precincts, Ballots Cast 17,559, Last Report 'Nov 7 12:37 a.m.'. SINGLE CAPTURE at 2012-11-10 10:25:40 UTC carries this value. No later capture is available anywhere in the CDX window for this election to independently confirm the freeze; self-describing but unbracketed, grade PLAUSIBLE per RUNBOOK 8. Sweep bracket-evidence cross-check: "single capture 20121110102540, no later capture to confirm freeze" (scratchpad/sos-status-sweep.md).

---

UPDATE (2026-07-10, CA SoS status-page sweep integration -- 2014 elections): 19 new sourced rows landed across 16 counties (of the 18 panel counties besides San Francisco, the control), recovered from the CA SoS per-county reporting-status page (`vote.sos.ca.gov/returns/status` 2012-2018, `electionresults.sos.ca.gov/returns/status` 2022+) across 2 statewide election(s) in this batch. 19 CONFIRMED (frozen-capture or single-capture-then-jump bracket per RUNBOOK 8), 0 PLAUSIBLE (self-describing FENU/plateau state but no independent capture available in the CDX window to bracket it). Source: `scratchpad/sos-status-sweep.md` (research sweep) and `scratchpad/sweep_applylist.json` (computed apply-list, this batch's subset); every cell's capture citation and freeze/jump evidence below was independently re-derived from the raw per-capture timeline data (not merely transcribed from the sweep's prose), matching exact ballots-cast values with zero mismatches. Running totals: 105 CONFIRMED, 8 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 2 REFUTED_AND_CORRECTED (117 sourced rows, matching the validator).

### colusa-ca 2014-11-04: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Colusa row at capture 20141105141649 (2014-11-05 14:16:49 UTC): 100.0% precincts, Ballots Cast 3,628, Last Report 'Nov 4 10:00 p.m.'. SINGLE CAPTURE at 2014-11-05 14:16:49 UTC carries this value. The next available capture (2014-11-07 08:38:01 UTC) jumps to 4,229 (Last Report 'Nov 6 11:19 a.m.'), confirming 3,628 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 4,229@Nov 6 11:19 a.m." (scratchpad/sos-status-sweep.md).

### del-norte-ca 2014-06-03: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Del Norte row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 5,122, Last Report 'Jun 3 10:14 p.m.'. FROZEN: the identical Ballots Cast figure 5,122 recurs across 3 captures, 2014-06-06 20:55:10 UTC through 2014-06-11 17:04:51 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20140606205510->20140611170451 (to end of window)" (scratchpad/sos-status-sweep.md).

### fresno-ca 2014-06-03: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Fresno row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 79,801, Last Report 'Jun 4 1:28 a.m.'. SINGLE CAPTURE at 2014-06-06 20:55:10 UTC carries this value. The next available capture (2014-06-07 07:58:13 UTC) jumps to 92,691 (Last Report 'Jun 6 3:09 p.m.'), confirming 79,801 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 92,691@Jun 6 3:09 p.m." (scratchpad/sos-status-sweep.md).

### fresno-ca 2014-11-04: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Fresno row at capture 20141105141649 (2014-11-05 14:16:49 UTC): 100.0% precincts, Ballots Cast 119,317, Last Report 'Nov 5 1:38 a.m.'. FROZEN: the identical Ballots Cast figure 119,317 recurs across 2 captures, 2014-11-05 14:16:49 UTC through 2014-11-07 08:38:01 UTC, before the next available capture (2014-11-15 02:26:27 UTC) jumps to 154,961 (Last Report 'Nov 14 3:08 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20141105141649->20141107083801 then jumps to 154,961@Nov 14 3:08 p.m." (scratchpad/sos-status-sweep.md).

### lake-ca 2014-06-03: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Lake row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 9,703, Last Report 'Jun 4 12:55 a.m.'. FROZEN: the identical Ballots Cast figure 9,703 recurs across 3 captures, 2014-06-06 20:55:10 UTC through 2014-06-11 17:04:51 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20140606205510->20140611170451 (to end of window)" (scratchpad/sos-status-sweep.md).

### los-angeles-ca 2014-06-03: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Los Angeles row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 636,186, Last Report 'Jun 4 3:07 a.m.'. SINGLE CAPTURE at 2014-06-06 20:55:10 UTC carries this value. The next available capture (2014-06-07 07:58:13 UTC) jumps to 655,432 (Last Report 'Jun 6 2:22 p.m.'), confirming 636,186 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 655,432@Jun 6 2:22 p.m." (scratchpad/sos-status-sweep.md).

### madera-ca 2014-06-03: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Madera row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 15,719, Last Report 'Jun 3 10:40 p.m.'. FROZEN: the identical Ballots Cast figure 15,719 recurs across 3 captures, 2014-06-06 20:55:10 UTC through 2014-06-11 17:04:51 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20140606205510->20140611170451 (to end of window)" (scratchpad/sos-status-sweep.md).

### madera-ca 2014-11-04: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Madera row at capture 20141105141649 (2014-11-05 14:16:49 UTC): 100.0% precincts, Ballots Cast 22,031, Last Report 'Nov 4 11:03 p.m.'. FROZEN: the identical Ballots Cast figure 22,031 recurs across 2 captures, 2014-11-05 14:16:49 UTC through 2014-11-07 08:38:01 UTC, before the next available capture (2014-11-15 02:26:27 UTC) jumps to 26,449 (Last Report 'Nov 7 2:21 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20141105141649->20141107083801 then jumps to 26,449@Nov 7 2:21 p.m." (scratchpad/sos-status-sweep.md).

### mendocino-ca 2014-06-03: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Mendocino row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 8,669, Last Report 'Jun 4 1:29 a.m.'. FROZEN: the identical Ballots Cast figure 8,669 recurs across 3 captures, 2014-06-06 20:55:10 UTC through 2014-06-11 17:04:51 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20140606205510->20140611170451 (to end of window)" (scratchpad/sos-status-sweep.md).

### napa-ca 2014-06-03: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Napa row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 17,431, Last Report 'Jun 3 11:43 p.m.'. FROZEN: the identical Ballots Cast figure 17,431 recurs across 3 captures, 2014-06-06 20:55:10 UTC through 2014-06-11 17:04:51 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20140606205510->20140611170451 (to end of window)" (scratchpad/sos-status-sweep.md).

### nevada-ca 2014-06-03: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Nevada row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 17,752, Last Report 'Jun 4 12:23 a.m.'. FROZEN: the identical Ballots Cast figure 17,752 recurs across 3 captures, 2014-06-06 20:55:10 UTC through 2014-06-11 17:04:51 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20140606205510->20140611170451 (to end of window)" (scratchpad/sos-status-sweep.md).

### placer-ca 2014-06-03: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Placer row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 47,986, Last Report 'Jun 4 2:06 a.m.'. FROZEN: the identical Ballots Cast figure 47,986 recurs across 3 captures, 2014-06-06 20:55:10 UTC through 2014-06-11 17:04:51 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20140606205510->20140611170451 (to end of window)" (scratchpad/sos-status-sweep.md).

### riverside-ca 2014-11-04: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Riverside row at capture 20141105141649 (2014-11-05 14:16:49 UTC): 100.0% precincts, Ballots Cast 265,771, Last Report 'Nov 5 2:26 a.m.'. SINGLE CAPTURE at 2014-11-05 14:16:49 UTC carries this value. The next available capture (2014-11-07 08:38:01 UTC) jumps to 294,055 (Last Report 'Nov 6 6:45 p.m.'), confirming 265,771 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 294,055@Nov 6 6:45 p.m." (scratchpad/sos-status-sweep.md).

### sacramento-ca 2014-06-03: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Sacramento row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 122,053, Last Report 'Jun 4 12:11 a.m.'. SINGLE CAPTURE at 2014-06-06 20:55:10 UTC carries this value. The next available capture (2014-06-07 07:58:13 UTC) jumps to 140,521 (Last Report 'Jun 6 2:08 p.m.'), confirming 122,053 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 140,521@Jun 6 2:08 p.m." (scratchpad/sos-status-sweep.md).

### san-bernardino-ca 2014-11-04: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

San Bernardino row at capture 20141105141649 (2014-11-05 14:16:49 UTC): 100.0% precincts, Ballots Cast 231,219, Last Report 'Nov 5 1:50 a.m.'. SINGLE CAPTURE at 2014-11-05 14:16:49 UTC carries this value. The next available capture (2014-11-07 08:38:01 UTC) jumps to 270,882 (Last Report 'Nov 6 4:07 p.m.'), confirming 231,219 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 270,882@Nov 6 4:07 p.m." (scratchpad/sos-status-sweep.md).

### san-diego-ca 2014-11-04: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

San Diego row at capture 20141105141649 (2014-11-05 14:16:49 UTC): 100.0% precincts, Ballots Cast 509,214, Last Report 'Nov 5 1:14 a.m.'. SINGLE CAPTURE at 2014-11-05 14:16:49 UTC carries this value. The next available capture (2014-11-07 08:38:01 UTC) jumps to 541,370 (Last Report 'Nov 6 5:05 p.m.'), confirming 509,214 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 541,370@Nov 6 5:05 p.m." (scratchpad/sos-status-sweep.md).

### san-mateo-ca 2014-06-03: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

San Mateo row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 70,651, Last Report 'Jun 3 11:30 p.m.'. SINGLE CAPTURE at 2014-06-06 20:55:10 UTC carries this value. The next available capture (2014-06-07 07:58:13 UTC) jumps to 85,537 (Last Report 'Jun 6 4:30 p.m.'), confirming 70,651 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 85,537@Jun 6 4:30 p.m." (scratchpad/sos-status-sweep.md).

### tehama-ca 2014-06-03: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Tehama row at capture 20140606205510 (2014-06-06 20:55:10 UTC): 100.0% precincts, Ballots Cast 8,976, Last Report 'Jun 4 1:28 a.m.'. FROZEN: the identical Ballots Cast figure 8,976 recurs across 2 captures, 2014-06-06 20:55:10 UTC through 2014-06-07 07:58:13 UTC, before the next available capture (2014-06-11 17:04:51 UTC) jumps to 13,016 (Last Report 'Jun 10 5:32 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20140606205510->20140607075813 then jumps to 13,016@Jun 10 5:32 p.m." (scratchpad/sos-status-sweep.md).

### tehama-ca 2014-11-04: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Tehama row at capture 20141105141649 (2014-11-05 14:16:49 UTC): 100.0% precincts, Ballots Cast 10,558, Last Report 'Nov 5 12:26 a.m.'. FROZEN: the identical Ballots Cast figure 10,558 recurs across 2 captures, 2014-11-05 14:16:49 UTC through 2014-11-07 08:38:01 UTC, before the next available capture (2014-11-15 02:26:27 UTC) jumps to 15,791 (Last Report 'Nov 13 8:30 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20141105141649->20141107083801 then jumps to 15,791@Nov 13 8:30 p.m." (scratchpad/sos-status-sweep.md).

---

UPDATE (2026-07-10, CA SoS status-page sweep integration -- 2016-2018 elections): 13 new sourced rows landed across 10 counties (of the 18 panel counties besides San Francisco, the control), recovered from the CA SoS per-county reporting-status page (`vote.sos.ca.gov/returns/status` 2012-2018, `electionresults.sos.ca.gov/returns/status` 2022+) across 3 statewide election(s) in this batch. 10 CONFIRMED (frozen-capture or single-capture-then-jump bracket per RUNBOOK 8), 3 PLAUSIBLE (self-describing FENU/plateau state but no independent capture available in the CDX window to bracket it). Source: `scratchpad/sos-status-sweep.md` (research sweep) and `scratchpad/sweep_applylist.json` (computed apply-list, this batch's subset); every cell's capture citation and freeze/jump evidence below was independently re-derived from the raw per-capture timeline data (not merely transcribed from the sweep's prose), matching exact ballots-cast values with zero mismatches. Running totals: 115 CONFIRMED, 11 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 2 REFUTED_AND_CORRECTED (130 sourced rows, matching the validator).

### colusa-ca 2016-11-08: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Colusa row at capture 20161110185817 (2016-11-10 18:58:17 UTC): 100.0% precincts, Ballots Cast 4,952, Last Report 'Nov 8 10:25 p.m.'. SINGLE CAPTURE at 2016-11-10 18:58:17 UTC carries this value. The next available capture (2016-11-14 19:00:27 UTC) jumps to 6,463 (Last Report 'Nov 10 6:20 p.m.'), confirming 4,952 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 6,463@Nov 10 6:20 p.m." (scratchpad/sos-status-sweep.md).

### lake-ca 2016-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Lake row at capture 20160614032019 (2016-06-14 03:20:19 UTC): 100.0% precincts, Ballots Cast 9,049, Last Report 'Jun 8 2:11 a.m.'. FROZEN: the identical Ballots Cast figure 9,049 recurs across 5 captures, 2016-06-14 03:20:19 UTC through 2016-06-22 03:35:32 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20160614032019->20160622033532 (to end of window)" (scratchpad/sos-status-sweep.md).

### lake-ca 2018-06-05: CONFIRMED

County's own numbered results-report system (result35.htm), self-labeled preliminary results at 100% precincts, same-URL overwritten to the exact certified total 5 weeks later (RUNBOOK 8).

UPGRADE (2026-07-10, primaries batch-1 integration): landed value retained (8,158/14,119 = 57.78%, same figure) but source and verdict upgraded from the SoS status-page single-capture PLAUSIBLE read (capture 20180619011846, Ballots Cast 8,158, Last Report 'Jun 6 1:44 a.m.', no later capture to confirm the freeze; retained in the JSON note as historical corroboration) to Lake County's own numbered results-report system, result35.htm (Wayback https://web.archive.org/web/20180610025440id_/http://publicapps.lakecountyca.gov:80/elections/results/result35.htm): "Election Results as of 06/06/2018 at 12:06:21 AM", "Completed Precincts: 70 of 70 PRELIMINARY RESULTS", Total Ballots Cast 8,158; the same URL's only later capture (2018-07-10, five weeks later) shows "Final Results for Election" / "COUNTY OF LAKE - Final Results", Total Ballots Cast 14,119, the exact certified total -- a same-URL-overwritten-to-certified-final bracket leg the SoS single-capture read lacked. Source: docs/research/pending-integration-2026-07-10/dossier-lake-ca-primaries.md Item 4.

### madera-ca 2016-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Madera row at capture 20160614032019 (2016-06-14 03:20:19 UTC): 100.0% precincts, Ballots Cast 21,553, Last Report 'Jun 7 11:20 p.m.'. FROZEN: the identical Ballots Cast figure 21,553 recurs across 5 captures, 2016-06-14 03:20:19 UTC through 2016-06-22 03:35:32 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20160614032019->20160622033532 (to end of window)" (scratchpad/sos-status-sweep.md).

### madera-ca 2018-06-05: PLAUSIBLE

CA SoS status-page single-capture bracket (RUNBOOK 8).

Madera row at capture 20180619011846 (2018-06-19 01:18:46 UTC): 100.0% precincts, Ballots Cast 18,258, Last Report 'Jun 6 12:20 a.m.'. SINGLE CAPTURE at 2018-06-19 01:18:46 UTC carries this value. No later capture is available anywhere in the CDX window for this election to independently confirm the freeze; self-describing but unbracketed, grade PLAUSIBLE per RUNBOOK 8. Sweep bracket-evidence cross-check: "single capture 20180619011846, no later capture to confirm freeze" (scratchpad/sos-status-sweep.md).

### mendocino-ca 2016-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Mendocino row at capture 20160614032019 (2016-06-14 03:20:19 UTC): 100.0% precincts, Ballots Cast 11,320, Last Report 'Jun 8 4:00 a.m.'. FROZEN: the identical Ballots Cast figure 11,320 recurs across 5 captures, 2016-06-14 03:20:19 UTC through 2016-06-22 03:35:32 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20160614032019->20160622033532 (to end of window)" (scratchpad/sos-status-sweep.md).

UPDATE (2026-07-10, primaries batch-1 integration): CORROBORATED via Mendocino's own "Election Summary Report" page (/acr/current.htm), self-titled "PRESIDENTIAL PRIMARY ELECTION JUNE 7, 2016 ... Final Election Night Report", internal timestamp "06/08/16 02:24:41", Cards Cast 11,320 (24.19%), 250/250 precincts (100%) -- a later capture of the same URL (17 days on) is byte-identical, independently matching this row's value exactly. See docs/research/pending-integration-2026-07-10/dossier-mendocino-ca-primaries.md Item 3.

### mendocino-ca 2018-06-05: PLAUSIBLE

CA SoS status-page single-capture bracket (RUNBOOK 8).

Mendocino row at capture 20180619011846 (2018-06-19 01:18:46 UTC): 100.0% precincts, Ballots Cast 19,049, Last Report 'Jun 6 3:57 a.m.'. SINGLE CAPTURE at 2018-06-19 01:18:46 UTC carries this value. No later capture is available anywhere in the CDX window for this election to independently confirm the freeze; self-describing but unbracketed, grade PLAUSIBLE per RUNBOOK 8. Sweep bracket-evidence cross-check: "single capture 20180619011846, no later capture to confirm freeze" (scratchpad/sos-status-sweep.md).

UPDATE (2026-07-10, primaries batch-1 integration): CORROBORATED (still PLAUSIBLE/secondary, not upgraded -- an independent route with no non-circular second leg either) by Anderson Valley Advertiser, "Mendocino County Today: Wednesday, June 6, 2018" (theava.com/archives/83237): "UPDATE (Wednesday 8:40am) With all precincts reporting and just over 40% of the ballots cast (19,049) the local trends are holding" -- an exact match to this row's value. CALIBRATION FLAG carried forward: 19,049/22,896 = 83.2% is well above this county's other primary years; kept flagged for human review though two independent sources now agree on the number. See docs/research/pending-integration-2026-07-10/dossier-mendocino-ca-primaries.md Item 4.

### napa-ca 2016-06-07: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Napa row at capture 20160614032019 (2016-06-14 03:20:19 UTC): 100.0% precincts, Ballots Cast 20,427, Last Report 'Jun 8 12:08 a.m.'. SINGLE CAPTURE at 2016-06-14 03:20:19 UTC carries this value. The next available capture (2016-06-17 06:35:08 UTC) jumps to 21,406 (Last Report 'Jun 15 9:16 a.m.'), confirming 20,427 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 21,406@Jun 15 9:16 a.m." (scratchpad/sos-status-sweep.md).

### nevada-ca 2016-06-07: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Nevada row at capture 20160614032019 (2016-06-14 03:20:19 UTC): 100.0% precincts, Ballots Cast 27,852, Last Report 'Jun 8 12:08 a.m.'. SINGLE CAPTURE at 2016-06-14 03:20:19 UTC carries this value. The next available capture (2016-06-17 06:35:08 UTC) jumps to 37,816 (Last Report 'Jun 14 12:34 p.m.'), confirming 27,852 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 37,816@Jun 14 12:34 p.m." (scratchpad/sos-status-sweep.md).

### placer-ca 2016-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Placer row at capture 20160614032019 (2016-06-14 03:20:19 UTC): 100.0% precincts, Ballots Cast 71,358, Last Report 'Jun 8 2:27 a.m.'. FROZEN: the identical Ballots Cast figure 71,358 recurs across 5 captures, 2016-06-14 03:20:19 UTC through 2016-06-22 03:35:32 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20160614032019->20160622033532 (to end of window)" (scratchpad/sos-status-sweep.md).

### riverside-ca 2016-11-08: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Riverside row at capture 20161110185817 (2016-11-10 18:58:17 UTC): 100.0% precincts, Ballots Cast 481,315, Last Report 'Nov 9 5:52 a.m.'. SINGLE CAPTURE at 2016-11-10 18:58:17 UTC carries this value. The next available capture (2016-11-14 19:00:27 UTC) jumps to 532,023 (Last Report 'Nov 11 5:30 p.m.'), confirming 481,315 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 532,023@Nov 11 5:30 p.m." (scratchpad/sos-status-sweep.md).

### sacramento-ca 2016-11-08: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

Sacramento row at capture 20161110185817 (2016-11-10 18:58:17 UTC): 100.0% precincts, Ballots Cast 328,744, Last Report 'Nov 9 1:52 a.m.'. SINGLE CAPTURE at 2016-11-10 18:58:17 UTC carries this value. The next available capture (2016-11-14 19:00:27 UTC) jumps to 385,520 (Last Report 'Nov 11 3:02 p.m.'), confirming 328,744 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 385,520@Nov 11 3:02 p.m." (scratchpad/sos-status-sweep.md).

### san-bernardino-ca 2016-11-08: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

San Bernardino row at capture 20161110185817 (2016-11-10 18:58:17 UTC): 100.0% precincts, Ballots Cast 443,517, Last Report 'Nov 9 4:56 a.m.'. SINGLE CAPTURE at 2016-11-10 18:58:17 UTC carries this value. The next available capture (2016-11-14 19:00:27 UTC) jumps to 515,334 (Last Report 'Nov 11 4:29 p.m.'), confirming 443,517 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 515,334@Nov 11 4:29 p.m." (scratchpad/sos-status-sweep.md).

---

UPDATE (2026-07-10, CA SoS status-page sweep integration -- 2022-2024 elections): 39 new sourced rows landed across 17 counties (of the 18 panel counties besides San Francisco, the control), recovered from the CA SoS per-county reporting-status page (`vote.sos.ca.gov/returns/status` 2012-2018, `electionresults.sos.ca.gov/returns/status` 2022+) across 4 statewide election(s) in this batch. 39 CONFIRMED (frozen-capture or single-capture-then-jump bracket per RUNBOOK 8), 0 PLAUSIBLE (self-describing FENU/plateau state but no independent capture available in the CDX window to bracket it). Source: `scratchpad/sos-status-sweep.md` (research sweep) and `scratchpad/sweep_applylist.json` (computed apply-list, this batch's subset); every cell's capture citation and freeze/jump evidence below was independently re-derived from the raw per-capture timeline data (not merely transcribed from the sweep's prose), matching exact ballots-cast values with zero mismatches. Running totals: 154 CONFIRMED, 11 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 2 REFUTED_AND_CORRECTED (169 sourced rows, matching the validator).

### colusa-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Colusa row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 1,693, Last Report 'Jun 7 11:09 p.m.'. FROZEN: the identical Ballots Cast figure 1,693 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 2,126 (Last Report 'Jun 10 1:36 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 2,126@Jun 10 1:36 p.m." (scratchpad/sos-status-sweep.md).

### colusa-ca 2022-11-08: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Colusa row at capture 20221109072903 (2022-11-09 07:29:03 UTC): 100.0% precincts, Ballots Cast 2,958, Last Report 'Nov 8 11:20 p.m.'. FROZEN: the identical Ballots Cast figure 2,958 recurs across 12 captures, 2022-11-09 07:29:03 UTC through 2022-11-10 22:44:53 UTC, before the next available capture (2022-11-11 03:30:58 UTC) jumps to 4,559 (Last Report 'Nov 10 6:58 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20221109072903->20221110224453 then jumps to 4,559@Nov 10 6:58 p.m." (scratchpad/sos-status-sweep.md).

### colusa-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Colusa row at capture 20240306063830 (2024-03-06 06:38:30 UTC): 100.0% precincts, Ballots Cast 1,846, Last Report 'Mar 5 9:14 p.m.'. FROZEN: the identical Ballots Cast figure 1,846 recurs across 7 captures, 2024-03-06 06:38:30 UTC through 2024-03-11 13:59:17 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen ALL 7 remaining captures thru Mar 11 (never moved)" (scratchpad/sos-status-sweep.md).

### colusa-ca 2024-11-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Colusa row at capture 20241106065418 (2024-11-06 06:54:18 UTC): 100.0% precincts, Ballots Cast 2,868, Last Report 'Nov 5 8:38 p.m.'. FROZEN: the identical Ballots Cast figure 2,868 recurs across 8 captures, 2024-11-06 06:54:18 UTC through 2024-11-06 17:18:13 UTC, before the next available capture (2024-11-07 01:54:46 UTC) jumps to 3,342 (Last Report 'Nov 6 5:11 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20241106065418->20241106171813 (to end of window)" (scratchpad/sos-status-sweep.md).

### del-norte-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Del Norte row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 4,019, Last Report 'Jun 7 10:25 p.m.'. FROZEN: the identical Ballots Cast figure 4,019 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 5,929 (Last Report 'Jun 10 3:20 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 5,929@Jun 10 3:20 p.m." (scratchpad/sos-status-sweep.md).

UPDATE (2026-07-10, primaries batch-1 integration): CORROBORATED via Del Norte's own numbered 2022 primary election-night PDF series (Google Drive folder 'June 7, 2022 Statewide Direct Primary Election'), Release 3 of 4 (CreationDate 6/7/2022 10:06:43 PM PDT), self-titled "Final Report - Unoffficial Results / Election Night Totals", Voters Cast 4,019/15,317 (26.24%) -- independently matches this row's value exactly; bracket leg is Release 4 (3 days later), retitled "Election Update", Voters Cast up to 5,929. See docs/research/pending-integration-2026-07-10/dossier-del-norte-ca-primaries.md Item 5.

### del-norte-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Del Norte row at capture 20240306063830 (2024-03-06 06:38:30 UTC): 100.0% precincts, Ballots Cast 3,285, Last Report 'Mar 5 10:25 p.m.'. FROZEN: the identical Ballots Cast figure 3,285 recurs across 5 captures, 2024-03-06 06:38:30 UTC through 2024-03-08 15:51:26 UTC, before the next available capture (2024-03-09 19:45:02 UTC) jumps to 6,055 (Last Report 'Mar 8 3:28 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 4 captures (Mar6-Mar7), jumps Mar9 to 6,055/Mar8 3:28pm" (scratchpad/sos-status-sweep.md).

UPDATE (2026-07-10, primaries batch-1 integration): CORROBORATED via Del Norte's own numbered 2024 primary election-night PDF series (Google Drive folder 'March 5, 2024 Primary Election'), Release 3 of 5 (CreationDate 3/5/2024 9:51:11 PM PST), self-titled "Presidential Primary Election / 19 Precincts Reporting / Unofficial Results", Voters Cast 3,285/14,743 (22.28%) -- independently matches this row's value exactly; bracket leg is Release 4 (3 days later), retitled "Unofficial Results - Friday Report", Voters Cast up to 6,055. See docs/research/pending-integration-2026-07-10/dossier-del-norte-ca-primaries.md Item 6.

### del-norte-ca 2016-06-07: CONFIRMED

Self-titled "Final Election Night Report / Unofficial Results", last of a numbered on-night release series (numbering does NOT equal plateau position -- verified via each file's own CreationDate), next report 3 days later retitled "Friday Report" at a higher count (RUNBOOK 8).

Landed 2026-07-10 (primaries batch-1 integration) from docs/research/pending-integration-2026-07-10/dossier-del-norte-ca-primaries.md Item 3. Release 3 of 5 in the county's numbered 2016 primary election-night PDF series, recovered live from the county's public Google Drive 'Elections Postings (Archive)' folder (drive.google.com/drive/folders/1nwgviB22IuQIVWjSquSY6Y_6APYvMgnH). Plateau determined by checking every release's actual PDF CreationDate: Release 1 9:04:28 PM, Release 2 10:01:22 PM, Release 3 11:09:27 PM (all election night 6/7/2016), Release 4 CreationDate Fri Jun 10 1:35:57 PM (3 days later), Release 5 CreationDate Wed Jun 15 5:05:29 PM (8 days later, filename-suffixed FINAL RESULTS). Release 3 self-titled "Final Election Night Report / Unofficial Results", printed page timestamp 6/7/2016 10:07:46 PM, 18/18 precincts (100.00%), Ballots Cast 5,020 of 13,525 (37.12%), stated directly (no ballot-card mislabel this file). Bracket leg: Release 4, retitled "Friday Report" (dropping "Election Night"), printed timestamp 6/10/2016 10:09:09 AM (3 days later), Ballots Cast 6,178 -- confirms Release 3 was the last report before the canvass resumed.

### del-norte-ca 2018-06-05: CONFIRMED

Late-night internal timestamp (self-description leg), last of a numbered on-night release series before a 2-days-later report explicitly relabeled "Update" at a higher count (bracket leg); front-page ballot figure disambiguated per the runbook's known Del Norte registered-voters/times-cast mislabel using the per-contest Times Cast cross-check (RUNBOOK 7.5, RUNBOOK 8).

Landed 2026-07-10 (primaries batch-1 integration) from docs/research/pending-integration-2026-07-10/dossier-del-norte-ca-primaries.md Item 4. Release 4 of 6 in the county's numbered 2018 primary election-night PDF series (Google Drive folder 'June 5, 2018 Primary Election'). PDF CreationDate metadata: Release 1 8:01:24 PM, Release 2 9:07:40 PM, Release 3 9:28:06 PM, Release 4 9:46:30 PM (all election night 6/5/2018), Release 5 CreationDate Thu Jun 7 11:01:30 AM (2 days later), Release 6 CreationDate Thu Jun 14 4:56:20 PM (9 days later, "Final Uncertified"). Release 4 front page reads "TOTAL RESULT SUMMARY REPORT (UNOFFICIAL)", printed timestamp 6/5/2018 9:42:38 PM, 18/18 precincts (100%); front page prints "Registered Voters: 4,637 of 14,151 (32.77%)" and a separate "Ballots Cast: 9,284" (ballot cards, ~2x, many-contest statewide primary) -- disambiguated via the per-contest Times Cast row (GOVERNOR contest: "Times Cast ... Total 4,637/14,151 32.77%", an exact match), confirming 4,637 is the correct people-count. Bracket leg: Release 5, retitled "1st Update (6/7/2018)", printed timestamp 6/7/2018 10:58:12 AM (2 days later), Registered Voters field up to 5,347/14,151 -- confirms Release 4 was the last report before the canvass resumed. FLAG for manual operator carried in the JSON note (mislabel resolution is a ~2x swing if misread).

### fresno-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Fresno row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 76,241, Last Report 'Jun 7 11:00 p.m.'. FROZEN: the identical Ballots Cast figure 76,241 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 97,487 (Last Report 'Jun 10 4:44 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 97,487@Jun 10 4:44 p.m." (scratchpad/sos-status-sweep.md).

### fresno-ca 2022-11-08: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Fresno row at capture 20221109070432 (2022-11-09 07:04:32 UTC): 100.0% precincts, Ballots Cast 126,440, Last Report 'Nov 8 10:56 p.m.'. FROZEN: the identical Ballots Cast figure 126,440 recurs across 13 captures, 2022-11-09 07:04:32 UTC through 2022-11-10 22:44:53 UTC, before the next available capture (2022-11-11 03:30:58 UTC) jumps to 153,891 (Last Report 'Nov 10 6:49 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20221109070432->20221110224453 then jumps to 153,891@Nov 10 6:49 p.m." (scratchpad/sos-status-sweep.md).

### fresno-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Fresno row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 82,242, Last Report 'Mar 6 12:58 a.m.'. FROZEN: the identical Ballots Cast figure 82,242 recurs across 3 captures, 2024-03-06 14:44:09 UTC through 2024-03-07 03:52:36 UTC, before the next available capture (2024-03-08 15:51:26 UTC) jumps to 105,945 (Last Report 'Mar 7 4:59 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 3 captures (Mar6-Mar7), jumps Mar8 to 105,945/Mar7 4:59pm" (scratchpad/sos-status-sweep.md).

### lake-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Lake row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 4,562, Last Report 'Jun 8 2:32 a.m.'. FROZEN: the identical Ballots Cast figure 4,562 recurs across 6 captures, 2022-06-08 09:42:59 UTC through 2022-06-13 22:59:28 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20220608230118->20220613225928 (to end of window)" (scratchpad/sos-status-sweep.md).

### lake-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Lake row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 7,181, Last Report 'Mar 6 2:01 a.m.'. FROZEN: the identical Ballots Cast figure 7,181 recurs across 6 captures, 2024-03-06 14:44:09 UTC through 2024-03-11 13:59:17 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen ALL 7 remaining captures thru Mar 11 (never moved)" (scratchpad/sos-status-sweep.md).

### los-angeles-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Los Angeles row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 822,545, Last Report 'Jun 8 2:12 a.m.'. FROZEN: the identical Ballots Cast figure 822,545 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 991,883 (Last Report 'Jun 10 3:19 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 991,883@Jun 10 3:19 p.m." (scratchpad/sos-status-sweep.md).

### los-angeles-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Los Angeles row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 910,857, Last Report 'Mar 6 2:06 a.m.'. FROZEN: the identical Ballots Cast figure 910,857 recurs across 2 captures, 2024-03-06 14:44:09 UTC through 2024-03-06 18:05:49 UTC, before the next available capture (2024-03-07 03:52:36 UTC) jumps to 1,016,574 (Last Report 'Mar 6 4:36 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 1 later capture (Mar6 10:05am), jumps same-day 4:36pm" (scratchpad/sos-status-sweep.md).

### madera-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Madera row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 13,417, Last Report 'Jun 7 11:09 p.m.'. FROZEN: the identical Ballots Cast figure 13,417 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 17,214 (Last Report 'Jun 10 2:29 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 17,214@Jun 10 2:29 p.m." (scratchpad/sos-status-sweep.md).

### madera-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Madera row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 16,048, Last Report 'Mar 5 10:32 p.m.'. FROZEN: the identical Ballots Cast figure 16,048 recurs across 4 captures, 2024-03-06 14:44:09 UTC through 2024-03-08 15:51:26 UTC, before the next available capture (2024-03-09 19:45:02 UTC) jumps to 21,214 (Last Report 'Mar 8 3:55 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 4 captures, jumps Mar9 to 21,214/Mar8 3:55pm" (scratchpad/sos-status-sweep.md).

### mendocino-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Mendocino row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 3,864, Last Report 'Jun 8 12:48 a.m.'. FROZEN: the identical Ballots Cast figure 3,864 recurs across 6 captures, 2022-06-08 09:42:59 UTC through 2022-06-13 22:59:28 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen 20220608094259->20220613225928 (to end of window)" (scratchpad/sos-status-sweep.md).

UPDATE (2026-07-10, primaries batch-1 integration): CORROBORATED (secondary, weaker than this landed CONFIRMED bracket, kept for the record) by two news outlets: MendoFever's live-blog tracks 3,461 (8:06pm, first tranche, excluded) -> 3,597 (10:15pm) -> "12:32am, all precincts reporting"; The Mendocino Voice, attributed to county clerk Katrina Bartolomie: "Unofficial election results showed 3,864 registered voters' ballots were counted as of early morning Wednesday, June 8" -- an exact match to this row's value. See docs/research/pending-integration-2026-07-10/dossier-mendocino-ca-primaries.md Item 5.

### mendocino-ca 2022-11-08: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Mendocino row at capture 20221109142729 (2022-11-09 14:27:29 UTC): 100.0% precincts, Ballots Cast 12,597, Last Report 'Nov 9 1:13 a.m.'. FROZEN: the identical Ballots Cast figure 12,597 recurs across 18 captures, 2022-11-09 14:27:29 UTC through 2022-11-18 23:50:49 UTC, before the next available capture (2022-11-23 01:06:32 UTC) jumps to 21,172 (Last Report 'Nov 22 4:48 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20221109142729->20221118235049 then jumps to 21,172@Nov 22 4:48 p.m." (scratchpad/sos-status-sweep.md).

### mendocino-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Mendocino row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 7,418, Last Report 'Mar 6 12:35 a.m.'. FROZEN: the identical Ballots Cast figure 7,418 recurs across 6 captures, 2024-03-06 14:44:09 UTC through 2024-03-11 13:59:17 UTC, holding to the end of the CDX capture window (no later capture available to show a jump). Sweep bracket-evidence cross-check: "frozen ALL 7 remaining captures thru Mar 11 (never moved)" (scratchpad/sos-status-sweep.md).

UPDATE (2026-07-10, primaries batch-1 integration): CORROBORATED (secondary, weaker than this landed CONFIRMED bracket, kept for the record) by The Mendocino Voice: "UPDATE 3/6/24 9:30 a.m.: Mendocino County's election results were updated after midnight on election night, and the current results include a total of 7,418 ballots, just over 14% of the county's 52,602 registered voters" -- an exact match to this row's value; MendoFever's independently-recovered 8:09pm first-tranche checkpoint (7,094) is explicitly excluded there. See docs/research/pending-integration-2026-07-10/dossier-mendocino-ca-primaries.md Item 6.

### napa-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Napa row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 14,658, Last Report 'Jun 7 11:08 p.m.'. FROZEN: the identical Ballots Cast figure 14,658 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 17,685 (Last Report 'Jun 10 3:54 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 17,685@Jun 10 3:54 p.m." (scratchpad/sos-status-sweep.md).

### napa-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Napa row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 15,304, Last Report 'Mar 5 11:34 p.m.'. FROZEN: the identical Ballots Cast figure 15,304 recurs across 4 captures, 2024-03-06 14:44:09 UTC through 2024-03-08 15:51:26 UTC, before the next available capture (2024-03-09 19:45:02 UTC) jumps to 20,504 (Last Report 'Mar 8 4:43 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 4 captures, jumps Mar9 to 20,504/Mar8 4:43pm" (scratchpad/sos-status-sweep.md).

### nevada-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Nevada row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 17,574, Last Report 'Jun 7 10:16 p.m.'. FROZEN: the identical Ballots Cast figure 17,574 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 20,222 (Last Report 'Jun 10 2:58 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 20,222@Jun 10 2:58 p.m." (scratchpad/sos-status-sweep.md).

### nevada-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Nevada row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 21,753, Last Report 'Mar 6 12:08 a.m.'. FROZEN: the identical Ballots Cast figure 21,753 recurs across 4 captures, 2024-03-06 14:44:09 UTC through 2024-03-08 15:51:26 UTC, before the next available capture (2024-03-09 19:45:02 UTC) jumps to 30,094 (Last Report 'Mar 8 3:28 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 4 captures, jumps Mar9 to 30,094/Mar8 3:28pm" (scratchpad/sos-status-sweep.md).

### orange-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Orange row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 325,774, Last Report 'Jun 7 11:42 p.m.'. FROZEN: the identical Ballots Cast figure 325,774 recurs across 2 captures, 2022-06-08 09:42:59 UTC through 2022-06-08 23:01:18 UTC, before the next available capture (2022-06-09 01:58:33 UTC) jumps to 348,130 (Last Report 'Jun 8 5:08 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220608230118 then jumps to 348,130@Jun 8 5:08 p.m." (scratchpad/sos-status-sweep.md).

### orange-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Orange row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 400,430, Last Report 'Mar 6 12:06 a.m.'. FROZEN: the identical Ballots Cast figure 400,430 recurs across 2 captures, 2024-03-06 14:44:09 UTC through 2024-03-06 18:05:49 UTC, before the next available capture (2024-03-07 03:52:36 UTC) jumps to 427,131 (Last Report 'Mar 6 5:10 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 1 later capture (Mar6 10:05am), jumps same-day 5:10pm" (scratchpad/sos-status-sweep.md).

### placer-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Placer row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 39,433, Last Report 'Jun 8 12:34 a.m.'. FROZEN: the identical Ballots Cast figure 39,433 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 40,944 (Last Report 'Jun 10 3:58 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 40,944@Jun 10 3:58 p.m." (scratchpad/sos-status-sweep.md).

### placer-ca 2022-11-08: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Placer row at capture 20221109142729 (2022-11-09 14:27:29 UTC): 100.0% precincts, Ballots Cast 65,224, Last Report 'Nov 9 1:23 a.m.'. FROZEN: the identical Ballots Cast figure 65,224 recurs across 12 captures, 2022-11-09 14:27:29 UTC through 2022-11-11 20:01:00 UTC, before the next available capture (2022-11-12 19:01:19 UTC) jumps to 76,230 (Last Report 'Nov 11 2:38 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20221109142729->20221111200100 then jumps to 76,230@Nov 11 2:38 p.m." (scratchpad/sos-status-sweep.md).

### placer-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Placer row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 69,436, Last Report 'Mar 6 12:04 a.m.'. FROZEN: the identical Ballots Cast figure 69,436 recurs across 4 captures, 2024-03-06 14:44:09 UTC through 2024-03-08 15:51:26 UTC, before the next available capture (2024-03-09 19:45:02 UTC) jumps to 93,100 (Last Report 'Mar 8 4:52 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "(prior recovery, doubly bracketed; see placer-2024-03-retry.md)" (scratchpad/sos-status-sweep.md).

### placer-ca 2024-11-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Placer row at capture 20241106105347 (2024-11-06 10:53:47 UTC): 100.0% precincts, Ballots Cast 165,535, Last Report 'Nov 6 2:14 a.m.'. FROZEN: the identical Ballots Cast figure 165,535 recurs across 10 captures, 2024-11-06 10:53:47 UTC through 2024-11-08 22:47:14 UTC, before the next available capture (2024-11-09 02:21:09 UTC) jumps to 182,129 (Last Report 'Nov 8 4:36 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20241106105347->20241106171813 (to end of window)" (scratchpad/sos-status-sweep.md).

### riverside-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Riverside row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 213,998, Last Report 'Mar 6 3:01 a.m.'. FROZEN: the identical Ballots Cast figure 213,998 recurs across 2 captures, 2024-03-06 14:44:09 UTC through 2024-03-06 18:05:49 UTC, before the next available capture (2024-03-07 03:52:36 UTC) jumps to 228,760 (Last Report 'Mar 6 6:20 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 1 later capture (Mar6 10:05am), jumps same-day 6:20pm" (scratchpad/sos-status-sweep.md).

### sacramento-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Sacramento row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 107,601, Last Report 'Jun 8 12:16 a.m.'. FROZEN: the identical Ballots Cast figure 107,601 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 173,818 (Last Report 'Jun 10 3:24 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 173,818@Jun 10 3:24 p.m." (scratchpad/sos-status-sweep.md).

### sacramento-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Sacramento row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 118,205, Last Report 'Mar 5 11:58 p.m.'. FROZEN: the identical Ballots Cast figure 118,205 recurs across 4 captures, 2024-03-06 14:44:09 UTC through 2024-03-08 15:51:26 UTC, before the next available capture (2024-03-09 19:45:02 UTC) jumps to 180,496 (Last Report 'Mar 8 3:12 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 4 captures, jumps Mar9 to 180,496/Mar8 3:12pm" (scratchpad/sos-status-sweep.md).

### san-bernardino-ca 2022-06-07: CONFIRMED

CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8).

San Bernardino row at capture 20220608230118 (2022-06-08 23:01:18 UTC): 100.0% precincts, Ballots Cast 119,998, Last Report 'Jun 8 3:16 a.m.'. SINGLE CAPTURE at 2022-06-08 23:01:18 UTC carries this value. The next available capture (2022-06-09 01:58:33 UTC) jumps to 126,421 (Last Report 'Jun 8 4:18 p.m.'), confirming 119,998 was election night's last state before the canvass moved (non-circular bracket leg per RUNBOOK 8). Sweep bracket-evidence cross-check: "single capture, next capture jumps to 126,421@Jun 8 4:18 p.m." (scratchpad/sos-status-sweep.md).

### san-bernardino-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

San Bernardino row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 150,018, Last Report 'Mar 6 1:48 a.m.'. FROZEN: the identical Ballots Cast figure 150,018 recurs across 2 captures, 2024-03-06 14:44:09 UTC through 2024-03-06 18:05:49 UTC, before the next available capture (2024-03-07 03:52:36 UTC) jumps to 160,881 (Last Report 'Mar 6 3:48 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 3 captures (Mar6), jumps same-day 3:48pm to 160,881" (scratchpad/sos-status-sweep.md).

### san-mateo-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

San Mateo row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 63,362, Last Report 'Jun 8 1:06 a.m.'. FROZEN: the identical Ballots Cast figure 63,362 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 75,776 (Last Report 'Jun 9 4:50 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 75,776@Jun 9 4:50 p.m." (scratchpad/sos-status-sweep.md).

### san-mateo-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

San Mateo row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 92,359, Last Report 'Mar 6 2:18 a.m.'. FROZEN: the identical Ballots Cast figure 92,359 recurs across 3 captures, 2024-03-06 14:44:09 UTC through 2024-03-07 03:52:36 UTC, before the next available capture (2024-03-08 15:51:26 UTC) jumps to 104,684 (Last Report 'Mar 7 4:25 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 2 later captures (Mar6 10:05am,7:52pm), jumps to 104,684/Mar7 4:25pm" (scratchpad/sos-status-sweep.md).

### santa-clara-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Santa Clara row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 181,257, Last Report 'Jun 7 11:00 p.m.'. FROZEN: the identical Ballots Cast figure 181,257 recurs across 2 captures, 2022-06-08 09:42:59 UTC through 2022-06-08 23:01:18 UTC, before the next available capture (2022-06-09 01:58:33 UTC) jumps to 187,550 (Last Report 'Jun 8 4:32 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220608230118 then jumps to 187,550@Jun 8 4:32 p.m." (scratchpad/sos-status-sweep.md).

### santa-clara-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Santa Clara row at capture 20240306063830 (2024-03-06 06:38:30 UTC): 100.0% precincts, Ballots Cast 182,413, Last Report 'Mar 5 10:26 p.m.'. FROZEN: the identical Ballots Cast figure 182,413 recurs across 3 captures, 2024-03-06 06:38:30 UTC through 2024-03-06 18:05:49 UTC, before the next available capture (2024-03-07 03:52:36 UTC) jumps to 209,664 (Last Report 'Mar 6 6:24 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 2 later captures (Mar6 6:44am,10:05am), jumps same-day 6:24pm" (scratchpad/sos-status-sweep.md).

### tehama-ca 2022-06-07: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Tehama row at capture 20220608094259 (2022-06-08 09:42:59 UTC): 100.0% precincts, Ballots Cast 7,915, Last Report 'Jun 7 11:41 p.m.'. FROZEN: the identical Ballots Cast figure 7,915 recurs across 4 captures, 2022-06-08 09:42:59 UTC through 2022-06-09 03:50:46 UTC, before the next available capture (2022-06-13 05:15:10 UTC) jumps to 12,478 (Last Report 'Jun 9 6:23 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen 20220608094259->20220609035046 then jumps to 12,478@Jun 9 6:23 p.m." (scratchpad/sos-status-sweep.md).

### tehama-ca 2024-03-05: CONFIRMED

CA SoS status-page frozen-capture bracket (RUNBOOK 8).

Tehama row at capture 20240306144409 (2024-03-06 14:44:09 UTC): 100.0% precincts, Ballots Cast 7,998, Last Report 'Mar 5 11:34 p.m.'. FROZEN: the identical Ballots Cast figure 7,998 recurs across 4 captures, 2024-03-06 14:44:09 UTC through 2024-03-08 15:51:26 UTC, before the next available capture (2024-03-09 19:45:02 UTC) jumps to 10,596 (Last Report 'Mar 8 5:52 p.m.'), marking the canvass resuming. Sweep bracket-evidence cross-check: "frozen thru 4 captures, jumps Mar9 to 10,596/Mar8 5:52pm" (scratchpad/sos-status-sweep.md).

UPDATE (2026-07-10, primaries batch-1 integration): CORROBORATED via Tehama's own official "Second Unofficial Report" (tehama.gov/wp-content/uploads/2024/03/), internal timestamp 3/5/2024 10:31:56 PM PST, 40/40 precincts (100%), "Total Registration and Turnout: 37,111 / 7,998" -- an exact match to this row's value; the report series' own next file (Third Unofficial Report) is dated 3 days later with nothing interposed, an independently-derived bracket-proof leg matching the landed SoS bracket's own conclusion. See docs/research/pending-integration-2026-07-10/dossier-tehama-ca-primaries.md Item 6.
