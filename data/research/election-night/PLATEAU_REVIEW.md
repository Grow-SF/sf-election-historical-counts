# Plateau adjudication (controller read, 2026-07-02)

Every sourced election-night numerator was adjudicated by the controller
model directly (no subagents) for the metric-defining question the
presence checks cannot answer: is the cited report the LAST report
posted on election night (the plateau)? Non-circular evidence was
gathered per row: Clarity CDN version brackets, internal report
timestamps and last-of-night titles, county posting schedules, held
counts in later captures, and Wayback CDX capture histories.

Verdicts: 54 CONFIRMED, 3 PLAUSIBLE, 2 REFUTED_AS_PLATEAU, 1 REFUTED_AND_CORRECTED.

(2026-07-09 addendum: Ventura County's six rows were adjudicated in a
follow-on pass, same method. All six recovered via Clarity CDN version
brackets, three from the Web01-era HTML API (2012, 2014, 2016, no
electionsettings.json for those eids) and three from the JSON API
(2018, 2022, 2024). See the per-row entries appended at the end of
this file and in plateau_review.json.)

| County | Date | Verdict | Basis | Evidence |
|---|---|---|---|---|
| fresno-ca | 2016-11-08 | CONFIRMED | frozen GEMS live page, held past night | header 'Unofficial Final Results ... 11/9/2016 1:42:19 AM' at 592/592 precincts; the Nov 12 capture (the artifact) still shows the 1:42 AM report |
| fresno-ca | 2024-11-05 | CONFIRMED | official county summary PDF, end of night | internal stamp 11/6/2024 12:30:26 AM at 478/478 (100%); next archived report (11/7 3:28 PM) jumped to 222,324 |
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
| santa-clara-ca | 2014-11-04 | PLAUSIBLE | documented ceiling: next-day canvass-start report | ver 148095 'Last updated 11/5/2014 5:08:58 PM'; the overnight versions' JSON was never crawled; note estimates the true plateau near 239,000; ceiling 251,620 flagged comparable=false |
| santa-clara-ca | 2022-11-08 | CONFIRMED | clarity version bracket, re-derived | cited v311769 stamped 11/8/2022 10:41:38 PM; next v312163 stamped 11/9 4:36 PM (BC 309,580) |
| santa-clara-ca | 2024-11-05 | REFUTED_AND_CORRECTED | clarity version walk recovers the true plateau | cited v353583 (11/6 4:46 PM, BC 468,395) is a next-day canvass bump; the night sequence is v353205 11:57 PM BC 459,487 then v353227 12:16 AM BC 460,325 (last of the night, held through v353516 at 1:10 PM); corrected to 4 |

## Non-CONFIRMED rows (read these first)

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

### santa-clara-ca 2014-11-04: PLAUSIBLE

documented ceiling: next-day canvass-start report.

ver 148095 'Last updated 11/5/2014 5:08:58 PM'; the overnight versions' JSON was never crawled; note estimates the true plateau near 239,000; ceiling 251,620 flagged comparable=false

### santa-clara-ca 2024-11-05: REFUTED_AND_CORRECTED

clarity version walk recovers the true plateau.

cited v353583 (11/6 4:46 PM, BC 468,395) is a next-day canvass bump; the night sequence is v353205 11:57 PM BC 459,487 then v353227 12:16 AM BC 460,325 (last of the night, held through v353516 at 1:10 PM); corrected to 460,325


### ventura-ca 2012-11-06: CONFIRMED

clarity version bracket (Web01 HTML, no JSON API).

v110763 '630 of 630 Precincts Completely Reported, Updated 11/7/2012 2:11:37 AM PST', BC 256,927; next v111498 titled 'Semi Official Update #1', dated 11/9/2012 12:12:16 PM PST, BC 270,851

### ventura-ca 2014-11-04: CONFIRMED

clarity version bracket (Web01 HTML, no JSON API).

v147874 '614 of 614 Precincts Completely Reported, Website last updated 11/5/2014 1:01:18 AM PST', BC 153,442; next v148521 dated 11/7/2014 12:17:57 PM PST, BC 166,686

### ventura-ca 2016-11-08: CONFIRMED

clarity version bracket (Web01 HTML, no JSON API).

v182694 '684 of 684 Precincts Completely Reported, Last updated 11/9/2016 12:51:27 AM PST', BC 258,250; next v182919 dated 11/10/2016 2:56:28 PM PST, BC 269,779

### ventura-ca 2018-11-06: CONFIRMED

clarity version bracket, re-derived from CDN.

cited v220414 stamped 11/7/2018 2:19:16 AM PST, PR 742/742, BC 201,298; next v221160 stamped 11/9/2018 3:11:17 PM PST, BC 219,149

### ventura-ca 2022-11-08: CONFIRMED

clarity version bracket, re-derived from CDN.

cited v311920 stamped 11/9/2022 1:27:17 AM PST, PR 1,640/1,640, BC 153,682; next v312263 stamped 11/10/2022 12:04:25 PM PST, BC 172,776

### ventura-ca 2024-11-05: CONFIRMED

clarity version bracket, re-derived from CDN.

cited v353328 stamped 11/6/2024 3:19:32 AM PST, PR 1,115/1,419, BC 267,226; next v353719 stamped 11/7/2024 4:04:33 PM PST, BC 278,636
