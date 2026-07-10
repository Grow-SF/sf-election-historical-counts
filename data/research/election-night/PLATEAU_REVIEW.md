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

| County | Date | Verdict | Basis | Evidence |
|---|---|---|---|---|
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
| napa-ca | 2012-11-06 | CONFIRMED | county report self-describes | 'Last Updated: November 6, 2012 11:29 PM (Last of the Night)' |
| napa-ca | 2014-11-04 | PLAUSIBLE | on-night floor; the exact final report is unarchived | 10:30 PM report is the artifact; the 10:42 PM last-of-night report's frames were never crawled (CDX empty); documented floor, stays secondary |
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
| riverside-ca | 2022-11-08 | CONFIRMED | 2 AM report held until the canvass | Last-Modified 11/09/2022 02:04 PST (inside the hourly-until-3am window); held as the live page until the 11/11 canvass update (300,498); local news corroboration |
| riverside-ca | 2024-11-05 | REFUTED_AS_PLATEAU | next-day canvass update, already documented in the note | cited state is 'Updated: 11/6/2024 5:35:21 PM', the first daily canvass update; the ~3 AM plateau is unarchived; retained as a flagged ceiling (comparable=false, secondary) |
| sacramento-ca | 2012-11-06 | PLAUSIBLE | distinct on-time capture exists but is currently unservable | CDX shows a distinct Nov 8 2012 8:53 PM PST capture (digest CYR7..., 10,563 bytes) differing from the 2013 FINAL-report capture (10,647 bytes); Wayback replay now 302-aliases it to 2013-02-15, which is why machine fetche |
| sacramento-ca | 2014-11-04 | CONFIRMED | Hart summary with night run time, held | 'Run Date:11/05/14 RUN TIME:12:33 AM', BALLOTS CAST TOTAL 195,317; the Nov 6 capture still shows it |
| sacramento-ca | 2018-11-06 | CONFIRMED | night report held ~22 hours | report stamp 11/7/2018 1:50:09 AM; capture Nov 7 3:44 PM PST still shows it; the county page's ballots-cast mislabel is documented |
| sacramento-ca | 2022-11-08 | CONFIRMED | county schedule plus midnight report | summary stamped 11/9/2022 12:00:20 AM; the county's own schedule text says updates run until about 12:00 am; captured 1:11 AM PST the same night |
| sacramento-ca | 2024-11-05 | CONFIRMED | county schedule plus night report | summary stamped 11/6/2024 1:56:14 AM; captured 7:17 AM PST before any next-day update |
| san-bernardino-ca | 2024-11-05 | CONFIRMED | county posting schedule brackets the capture | header 'Final Unofficial Election Night Results'; the 2:41 PM capture sits between the county's 10 AM final-EN posting and the 4 PM canvass resume; Provisional 0 confirms pre-canvass; render-verified 434,108 at 2,872/2,8 |
| san-diego-ca | 2018-11-06 | CONFIRMED | night stamp, captured the same night | stamp 11/7/2018 01:42:41 AM; captured 4:06 AM PST |
| san-diego-ca | 2022-11-08 | CONFIRMED | self-describing final plus next-post schedule | 'FINAL UNOFFICIAL ELECTION NIGHT RESULTS ... NEXT POST 11/10/2022 BY 5 P.M.', stamp 11/9/2022 2:21:25 AM |
| san-diego-ca | 2024-11-05 | CONFIRMED | self-describing final | 'UNOFFICIAL ELECTION NIGHT FINAL (ESTIMATED BALLOTS TO BE PROCESSED: 590,000)', stamp 11/6/2024 2:52:20 AM |
| san-mateo-ca | 2012-11-06 | CONFIRMED | county-archived night turnout report | 'Precinct Turnout Total Voters Unofficial' stamped 11/07/2012 12:07 AM |
| san-mateo-ca | 2014-11-04 | CONFIRMED | county-archived night turnout report | stamped 11/04/2014 11:36 PM |
| san-mateo-ca | 2016-11-08 | CONFIRMED | county-archived night turnout report | stamped 11/09/2016 03:03 AM |
| san-mateo-ca | 2018-11-06 | CONFIRMED | on-night capture of the final report | captured 4:11 AM PST Nov 7; rendered widget shows 'Total Ballots Cast 111,637'; the page defines the 'Final Election Night Report' release; render-verified |
| san-mateo-ca | 2022-11-08 | CONFIRMED | self-describing final plus next-update schedule | 'Semi-Official Results - Final Election Night Report - Next update on Thursday, November 10', stamp 11/9/2022 3:17:37 AM |
| san-mateo-ca | 2024-11-05 | CONFIRMED | self-describing final plus next-update schedule | 'Final Election Night Report - Next update on Thursday, November 7', stamp 11/6/2024 2:18:48 AM |
| santa-clara-ca | 2012-11-06 | CONFIRMED | long-night report held in a later capture | stamped 11/7/2012 4:14:04 AM PST; the Nov 10 capture still shows it |
| santa-clara-ca | 2014-11-04 | REFUTED_AND_CORRECTED | clarity live-CDN version walk recovers the true overnight plateau, superseding the documented ceiling | cited ceiling ver 148095 (11/5 5:08:58 PM, BC 251,620) is a next-day canvass-start report; the live CDN (unlike Wayback) still serves the overnight versions' JSON -- v147908 (11/5 4:00:59 AM PST, BC 235,062) is the last of the continuous night sequence (pace collapses to +624 in the final 63 min, then a 13-hour gap to 148095); corrected 251,620 -> 235,062, comparable=false removed |
| santa-clara-ca | 2016-11-08 | CONFIRMED | clarity live-CDN version bracket: cadence break in the immediately following version | v182800 (11/9 10:28:40 AM PST, BC 443,269) is the last of a continuous ~hourly overnight sequence from v181922 (11/8 7:43 PM); the next version v182869 (3:41 PM) breaks cadence (+7,333 over 5h13m vs an overnight pace of 5,700-15,400/hr) |
| santa-clara-ca | 2018-11-06 | CONFIRMED | clarity live-CDN version bracket: adjacent official versions in the settings array, 9h22m gap | v220444 (11/7 6:37:33 AM PST, BC 304,303, precincts 1,098/1,098) is immediately followed in the electionsettings versions array by v220630 (3:59:46 PM, BC 306,086, +1,783 only) |
| santa-clara-ca | 2022-11-08 | CONFIRMED | clarity version bracket, re-derived | cited v311769 stamped 11/8/2022 10:41:38 PM; next v312163 stamped 11/9 4:36 PM (BC 309,580) |
| santa-clara-ca | 2024-11-05 | REFUTED_AND_CORRECTED | clarity version walk recovers the true plateau | cited v353583 (11/6 4:46 PM, BC 468,395) is a next-day canvass bump; the night sequence is v353205 11:57 PM BC 459,487 then v353227 12:16 AM BC 460,325 (last of the night, held through v353516 at 1:10 PM); corrected to 4 |

## Non-CONFIRMED rows (read these first)

### lake-ca 2018-11-06: PLAUSIBLE

self-described past-midnight 'PRELIMINARY RESULTS' timestamp; the only later observation is a single Wayback crawl (not a second independent capture) whose crawl date diverges from the page's own generation timestamp -- suggestive but not one of the section 8 non-circular legs.

result37.htm's sole Wayback capture (2018-11-29) reads 'Election Results as of 11/07/2018 at 12:14:30 AM', 'PRELIMINARY RESULTS', 70/70 precincts, Total Ballots Cast 13,522; DOWNGRADED from the dossier's proposed CONFIRMED (2026-07-10 integration review): the crawl-date/internal-timestamp divergence (22 days) is a single-capture inference, not a genuine second data point like the two-capture holds confirmed for this county's 2012/2014/2016 rows; no Clarity bracket, second capture, county posting schedule, or separate official release is obtainable

### napa-ca 2014-11-04: PLAUSIBLE

on-night floor; the exact final report is unarchived.

10:30 PM report is the artifact; the 10:42 PM last-of-night report's frames were never crawled (CDX empty); documented floor, stays secondary

### placer-ca 2018-11-06: REFUTED_AS_PLATEAU

page provably tracked the canvass.

cited render is 11/09/18 15:15 (113,380); NEW EVIDENCE: the Nov 21 capture of the same page shows Cards Cast 162,802, so the page re-rendered with canvass data and the Nov 9 figure likely absorbs early canvass; 113,380 is a ceiling on the unarchived night plateau; flagged comparable=false

### riverside-ca 2024-11-05: REFUTED_AS_PLATEAU

next-day canvass update, already documented in the note.

cited state is 'Updated: 11/6/2024 5:35:21 PM', the first daily canvass update; the ~3 AM plateau is unarchived; retained as a flagged ceiling (comparable=false, secondary)

### sacramento-ca 2012-11-06: PLAUSIBLE

distinct on-time capture exists but is currently unservable.

CDX shows a distinct Nov 8 2012 8:53 PM PST capture (digest CYR7..., 10,563 bytes) differing from the 2013 FINAL-report capture (10,647 bytes); Wayback replay now 302-aliases it to 2013-02-15, which is why machine fetches see the Nov 30 report; the note's reading (Run Date 11/07/12 12:49 AM, 328,516 at 1,106/1,106) is temporally coherent but machine-unverifiable today

### santa-clara-ca 2014-11-04: REFUTED_AND_CORRECTED

clarity live-CDN version walk recovers the true overnight plateau, superseding the documented ceiling.

Original 2026-07-02 verdict was PLAUSIBLE (documented ceiling: next-day canvass-start report; ver 148095 'Last updated 11/5/2014 5:08:58 PM'; the overnight versions' JSON was never crawled; note estimated the true plateau near 239,000; ceiling 251,620 flagged comparable=false). CORRECTION (2026-07-10, gap-triage): the live Clarity CDN, unlike Wayback, still serves the overnight versions' JSON -- v147908 (11/5 4:00:59 AM PST, BC 235,062) is the last of the continuous night sequence (pace collapses to +624 in the final 63 min, then a 13-hour gap to 148095); corrected 251,620 -> 235,062 (58.16%), comparable=false removed, confidence upgraded to primary.

### santa-clara-ca 2024-11-05: REFUTED_AND_CORRECTED

clarity version walk recovers the true plateau.

cited v353583 (11/6 4:46 PM, BC 468,395) is a next-day canvass bump; the night sequence is v353205 11:57 PM BC 459,487 then v353227 12:16 AM BC 460,325 (last of the night, held through v353516 at 1:10 PM); corrected to 460,325

