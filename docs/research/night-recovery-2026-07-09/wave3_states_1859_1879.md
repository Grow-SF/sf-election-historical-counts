# Wave 3: election-night counts, SF state/judicial/constitutional elections 1859-1879

Agent: night-count recovery agent (CDNC via raw-CDP Chrome :9222).
Salvage file, written as I go. Status legend: PENDING / FOUND / PARTIAL / DEAD-END.

Targets (official final totals = gate ceilings):

| # | election | day-after issue | final | status |
|---|----------|-----------------|-------|--------|
| 1 | 1859-09-07 gubernatorial + municipal (Teschemacher) | DAC18590908 | 10,889 | FOUND: midnight per-district counts, floor ~3,008-3,068 (~28%) |
| 2 | 1862-09-03 state general | DAC18620904 | 8,813 | FOUND: midnight per-district counts, floor ~5,765 (~65%, caveats) |
| 3 | 1863-09-02 gubernatorial (Low) | DAC18630903 | 14,866 | FOUND: "Returns up to Two o'Clock", floor ~8,900 (~60%, caveats) |
| 4 | 1870-09-07 state general | DAC18700908 | 19,944 | FOUND: 3:30 a.m. partials; table needs human scan read |
| 5 | 1871-09-06 gubernatorial + municipal (Alvord) | DAC18710907 | 25,094 | FOUND: per-ward counts stamped 1:48-3:30 a.m., ~35% floor |
| 6 | 1873-10-15 judicial special | DAC18731016 | 15,594 | FOUND: COMPLETE same-night count (~100%) |
| 7 | 1877-10-17 judicial special | DAC18771018 | 22,942 | FOUND: COMPLETE same-night count (~100%; total 23,332 vs gate 22,942, flag) |
| 8 | 1878-06-19 Const. Convention delegates | DAC18780620 | 27,098 | FOUND: explicit "~6,000 counted" of ~27,000 (~22%) |
| 9 | 1879-05-07 constitution ratification | DAC18790508 | 38,034 | FOUND: near-COMPLETE count, all but 3 precincts (~98-100%) |

Primary paper: Daily Alta California (DAC), CDNC coverage 1849-1891.
SFC (San Francisco Call) coverage starts 1890 on CDNC, NOT usable for these years.
Backup paper: Sacramento Daily Union (SDU) day-after SF dispatches.

## Method
- Cloudflare cleared once per tab via raw CDP (Page.navigate + DOM.getOuterHTML poll, no Runtime.enable until cleared).
- All search/OCR via Runtime.evaluate fetch() inside cleared tab (same-origin, rides cf_clearance).
- getSectionText URL grammar: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=<OID>&f=AJAX&e=-------en--20--1--txt-txIN--------
- Issue URL grammar: https://cdnc.ucr.edu/?a=d&d=DAC<YYYYMMDD>
- Search URL grammar: https://cdnc.ucr.edu/?a=q&hs=1&r=1&results=1&txq=<PHRASE>&txf=txIN&ssnip=txt&puq=DAC&dafdq=<DD>&dafmq=<MM>&dafyq=<YYYY>&datdq=<DD>&datmq=<MM>&datyq=<YYYY>&e=-------en--20--1--txt-txIN--------

## Findings (appended as discovered)

### Method update (all elections)
Old DAC issues have NO inline article TOC in the issue HTML (unlike 1896 SFC). But:
- getSectionText accepts PAGE-level OIDs (DAC<ymd>.1.<page>) and returns the whole page's OCR (~80k chars).
- date-scoped search returns article OIDs directly. Workflow: search first, page-level OCR as fallback sweep.

### 1: 1859-09-07 gubernatorial + municipal. STATUS: FOUND (partial midnight count + full poll-list table)
- Source: Daily Alta California, 1859-09-08, "CITY ITEMS. / The Election." Section OID DAC18590908.2.17 (page 1 col; via search).
- Locating query (copy-pasteable): https://cdnc.ucr.edu/?a=q&hs=1&r=1&results=1&txq=election&txf=txIN&ssnip=txt&puq=DAC&dafdq=08&dafmq=09&dafyq=1859&datdq=08&datmq=09&datyq=1859&e=-------en--20--1--txt-txIN-------- (srpos 1)
- OCR retrieval URL: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=DAC18590908.2.17&f=AJAX&e=-------en--20--1--txt-txIN--------
- Verbatim (poll list, NOT a count): "The whole number of votes polled in the city was 10,889 ... The following is the number of votes cast in the several districts: 1st District 772 2d 1,374 3d 1,635 [OCR garble; narrative for Third District says 'the whole number of votes cast was 1,035'; with 1,035 the column foots EXACTLY to 10,889] 4th 833 5th 983 6th 817 7th 1,241 8th 619 9th 1,353 10th 1,156 11th 421 12th 285 Total 10,889"
- Verbatim (counting pace): "The unusual number of scratched tickets will greatly delay the countine, and it will probably be several days before the official result is declared in this city."
- ELECTION-NIGHT COUNTED (12 o'clock midnight, per-district, my sums, FLOORS for gov contest):
  1st: "314 straight tickets had been counted, of which Latham received 233; Leland Stanford, 20; John Currey, 121" (stated 314 but gov figures sum 374; OCR ambiguity, flag human)
  2d: Latham 697 + Stanford 315 + Currey 345 = 1,357
  3d: 82+38+55 = 175 (of 1,035 cast)
  4th: "but 61 straight tickets counted"
  5th: 35+26+31 = 92 (of 983)
  6th: "130 votes were counted up to 12 o'clock" (80+27+23=130 checks)
  7th: "only 61 tickets had been counted" (57+0+4=61 checks)
  8th: 33+18+16 = 67
  9th: "282 straight tickets were counted"
  10th: "only 73 straight tickets had been counted"
  11th: "114 straight tickets were counted" (87+13+14=114 checks)
  12th: 124+64+94 = 282 (of 285 cast; "so far as counted")
  SUM COUNTED BY MIDNIGHT: 3,008 (using stated 314) to 3,068 (using 374) = 27.6-28.2% of final 10,889.
  NOTE: these are straight-ticket gubernatorial counts, so a FLOOR on ballots processed.
- Official-final gate: 10,889 polled = official final exactly. Poll list closed at "sunset - 6 o'clock and 17 minutes".
- OCR text saved: wave3/out/sec1859_2_17.txt

### 2: 1862-09-03 state general. STATUS: FOUND (midnight partial count, district-by-district)
- Source: Daily Alta California, 1862-09-04, "The Election." / "The Returns." Section OID DAC18620904.2.3 (via search "returns" srpos 1).
- OCR retrieval URL: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=DAC18620904.2.3&f=AJAX&e=-------en--20--1--txt-txIN--------
- Verbatim (count state at press): "Of course it is impossible to give the returns in tabular form, in this issue, as, at midnight, canvassers in most of the Districts had not finished counting the straight tickets."
- Per-district midnight state (verbatim fragments):
  1st: "the returns could not be made out before this morning" (nothing counted for press)
  2d: "There had been, at midnight, 450 straight Union, and 140 straight Democratic tickets counted. There are at least 300 split tickets remaining to be counted." (=590 counted)
  3d (COMPLETE): "Average Union Administration, 450; Opposition, 140." (=590)
  4th (incomplete): "Whole number, 593. As far as counted (straight tickets) ... Opposition, 114. Constitutional Amendments: Yes, 394; No, 15." (amendment count 409)
  5th: full contest table, Swett 629, Stevenson 142, Fitzgerald 19 (=790); "For the amendments, [660]. Against, 4."
  6th (incomplete): "Whole number, 577. Average Union Administration, 374; Opposition, 89." (=463)
  7th: "Straight Union Administration votes, 562; Opposition, 12i [121?]" (=~683)
  8th (COMPLETE): "Average Union Administration, 480; Opposition, 160. Amendments: Yes, 621; No, 10." (=640)
  9th: "At 12 o'clock, 500 straight Union Administration tickets only were counted, and 100 Opposition." (=600)
  10th: "The total vote for Swett only was counted at 12 o'clock, being 1,000 [OCR '1,0011']."
  11th: "Only the aggregate vote from this District was received up to one o'clock this morning."
  12th (OFFICIAL): table zone did NOT OCR (image); needs human scan read.
- FLOOR sum of counted-by-midnight (superintendent/opposition contests, excl 1st, 11th, 12th): 590+590+409+790+463+683+640+600+1000 = 5,765 = 65.4% of final 8,813. CAUTION: 3d/8th marked complete may include counts finished near press; 10th's 1,000 is one candidate's total (whole-ticket count larger). Treat 5,765 as a rough floor with OCR caveats.
- Aggregate city vote table ("Comparative Vote", section DAC18620904.2.2 tail) exists in print but its table zone did not OCR. Human scan read needed for the printed citywide aggregate.
- OCR saved: wave3/out/sec1862_2_3.txt, sec1862_2_2.txt, page1862_p1.txt

### 3: 1863-09-02 gubernatorial (Low). STATUS: FOUND (explicit "Returns up to Two o'Clock" + total-vote article)
- Source: Daily Alta California, 1863-09-03, "Returns up to Two o'Clock." Section OID DAC18630903.2.4 (search "returns" srpos 1); companion "THE CITY ELECTION." DAC18630903.2.3.
- OCR retrieval URLs: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=DAC18630903.2.4&f=AJAX&e=-------en--20--1--txt-txIN-------- and same with d=DAC18630903.2.3
- Verbatim (clock): "The vote, as far as ascertainable in the various districts at two o'clock this morning, was as follows:"
- Per-district Low/Downey counted at 2 a.m. (OCR-garbled digits flagged []):
  1st: Low [3]35, Downey 400 ("Total vote of District, 736" checks 335+400=735)
  2d: Low 846, Downey 494 (majority 352 checks)
  3d: Low [514], Downey 284 ("230 majority for Low" checks)
  4th: table garbled; "Total Union vote, 659"
  5th (OFFICIAL): Low 801, Downey [326]
  6th: straight tickets Low 603, Downey 169
  7th: "290 tickets counted. 1,665 total vote. Low, 180; Downey, 110." (180+110=290 checks)
  8th: "Whole vote, 1,104. Low, 788; Downey [316]" (788+316=1,104 checks)
  9th: Low [garbled], Downey 99; "Low has 200 majority"
  10th: "Low, 64; Downey, 61 - but Low has two to one, uncounted"
  11th: "Total for Low, 677; total for Downey, 534" (=1,211)
  12th: Low 45, Downey 25 (=70)
- Gov-contest sum counted by 2 a.m. ~ 8,900 (735+1340+798+~1100+1127+772+290+1104+~300+125+1211+70) = ~60% of final 14,866. Several districts garbled; label as approximate floor, human scan read recommended.
- Total-vote gate: "THE TOTAL VOTE. The total vote of the city was 14,8[6]6 - 451 more than were ever cast in the city before." (OCR prints '14,806'; official final 14,866; poll-list total, not a count.)
- Counting pace corroboration (2.2 "The State Election"): "We have incomplete returns from a dozen interior counties; complete, from none."
- OCR saved: wave3/out/sec1863_2_4.txt, sec1863_2_3.txt, sec1863_2_2.txt

### 4: 1870-09-07 state general (municipal officers). STATUS: FOUND (partial returns, press-time 3:30 a.m.)
- Source: Daily Alta California, 1870-09-08: "MUNICIPAL ELECTION, SEPTEMBER 7th, 1870." (returns table, DAC18700908.2.5), "Municipal Election" (DAC18700908.2.6), "Incomplete Returns" (DAC18700908.2.7), "Ward Officers" (DAC18700908.2.8). Found via search "returns" and "election".
- OCR retrieval URL pattern: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=DAC18700908.2.7&f=AJAX&e=-------en--20--1--txt-txIN-------- (and .2.5/.2.6/.2.8)
- Verbatim (press-time clock): "As far as can be gathered from the imperfect returns at hand at this hour (3:30 A.M.,) the Tax-Payers' ticket will have an average majority of 2,0[0]3."
- Verbatim (counting pace): "The wholesale scratching that prevailed at all the polls made it difficult to count the votes and obtain returns, which will not be ready in some of the wards before 9 o'clock this morning. We give the result as far as it could be ascertained."
- Verbatim (what was complete): "The only Wards and Precincts from which we have complete returns are: The 5th, 6th, first precinct of the 7th, second precinct of the 8th, second precinct of the 10th, third of the 10th, second of the 11th, 1st and 2d of the 12th."
- Verbatim (overnight partials): "The returns from the Ninth Ward, in the table, are partial, as far as counted at 12 o'clock this morning ... This return is up to 1:30 A.M."
- "TOTAL VOTES POLLED" ward/precinct poll-list table printed (partially garbled OCR); NOT a count.
- The citywide returns table (2.5) has dense garbled OCR: a numeric floor cannot be summed reliably from OCR; needs human scan read (screenshot saved).
- OCR saved: wave3/out/sec1870_2_5.txt .. sec1870_2_8.txt

### 5: 1871-09-06 gubernatorial + municipal (Alvord). STATUS: FOUND (per-ward counts with 1:48-3:30 a.m. stamps + poll-list total 25,112)
- Source: Daily Alta California, 1871-09-07, "TRIUMPHANT VICTORY." Section OID DAC18710907.2.7 (search "election" srpos 6); corroboration "THE RESULT OF A REPUBLICAN TRIUMPH." DAC18710907.2.2.
- OCR retrieval URL: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=DAC18710907.2.7&f=AJAX&e=-------en--20--1--txt-txIN--------
- Verbatim (poll list): "In the Wards Yesterday ... Total 25,112. Vote of 1870 21,691." (official final 25,094; 25,112 is the same-night poll-list total, 18 higher)
- Verbatim (counting pace): "No definite or full returns can be had before this afternoon, and in some cases the clerks will not have counted the votes before evening, owing to the large number of scratched tickets."
- Verbatim (city returns to 3 a.m., from 2.2): "so far as we can judge from returns received up to three o'clock this morning, has been replaced by a majority in this city of 1,200 for Booth"
- Per-ward overnight count states (verbatim fragments with clocks):
  1st: "straight Democratic, 131; straight Tax-payers' and Republicans, 110. The straight and scratched Democratic votes counted gave Curtis 165, and Alvord 115."
  2d: "At 3 A.M. ... Republicans had 202 straight tickets; Democrats, 297; Democrats, scratched, 400."
  3d: "straight Tax-payers' tickets, 111; straight Republican, 112; straight Democratic, 153."
  4th: "3:15 A.M.- Straight Republican, 223; straight Democratic, 97; Tim McCarty is on 265 Democratic scratched tickets"
  5th: full ticket classification of all 860 votes; "Booth's majority, 80; Alvord's majority, 60."
  6th: "But little progress made up to 2 A.M."
  7th 2d pct: "The count, up to the hour of going to press, gave Booth 263, Haight 201 ..." (1st pct: "no returns as to the count")
  8th 1st pct: "Only 475 scratched tickets had been counted ... Newton Booth, 360; H.H. Haight, 109"
  8th 2d pct: "Half-past two A.M. ... but ten scratched tickets had been counted."
  9th: "1:48 A.M.- Governor's vote counted; Booth has [8]15 majority" (ward fully counted for governor, 1,892 votes cast)
  10th 1st pct: "count up to 3:15 A.M. ... Booth, 200; Haight, 331"
  10th 2d pct: "3:30 A.M.: 220 straight Democratic, 120 Republican."
  10th 3d pct: "returns embrace the count of straight and scratched Democratic tickets only"
  10th 4th pct: "[2:30?] A.M., as far as counted - 1[6]6 straight Republican, 302 Democratic"
  11th 2d pct: "The Tax-payers' ticket was 385 ahead at two A.M., and was gaining by the count."
  12th: supervisor counts given both precincts.
- A citywide counted-ballots total is NOT computable exactly (mixture of straight-ticket classifications and contest counts); demonstrably-counted floor across wards is roughly 8-9k = ~35% of 25,094, with only the 9th Ward fully counted for governor overnight. Recommend quoting ward states rather than a single number.
- OCR saved: wave3/out/sec1871_2_7.txt, sec1871_2_2.txt

### 6: 1873-10-15 judicial special. STATUS: FOUND (COMPLETE same-night city count printed E+1)
- Source: Daily Alta California, 1873-10-16, "THE JUDICIAL ELECTION." DAC18731016.2.14 (search "election" srpos 3); "THE RESULT." DAC18731016.2.15; "BREVITIES." DAC18731016.2.10.
- OCR retrieval URL: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=DAC18731016.2.14&f=AJAX&e=-------en--20--1--txt-txIN--------
- Verbatim (headline): "TUX ALTA AHEAD IN GIVING THE NEWS. Complete [Re]turns from the City." Full precinct-by-precinct table printed "prepared from the official returns".
- Verbatim (total): "The total vote polled is unusually small, being [15,594-ish; OCR 'H.TsS'] against [26,017-ish; OCR 'JS.'JIO'] cast at the September election, a falling off of 10,423." NOTE: 15,594 + 10,423 = 26,017 exactly; the falling-off arithmetic strongly implies the printed total equals the official final 15,594. Human scan read needed to confirm the two garbled numbers.
- Verbatim (speed): "[The vote] was so light that all the returns from forty-five precincts were sent in and placed under lock and key at twenty minutes past ten o'clock in the evening."
- Verbatim (BREVITIES): "The election officers of the Fifth Ward completed the counting of the [800-odd; OCR 'SUI'] votes yesterday in one hour and thirty-five minutes, without making a single mistake or even a blot on the tally list. This is said to be the quickest work of the kind ever done in this city."
- Contest majorities (2.15): "Judge Louderback ... majority of 1,[5]04 ... Judge McKinstry received a majority of 1,70[8] votes over Judge Dwinelle."
- Verdict: single-office light ballot counted SAME NIGHT, complete count in E+1 paper = ~100% election-night count (pending human confirmation of the garbled total).
- OCR saved: wave3/out/sec1873_2_14.txt, sec1873_2_15.txt, sec1873_2_10.txt

### 7: 1877-10-17 judicial special. STATUS: FOUND (COMPLETE same-night city count printed E+1)
- Source: Daily Alta California, 1877-10-18, "THE JUDICIAL ELECTION" DAC18771018.2.14 (search "election" srpos 4).
- OCR retrieval URL: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=DAC18771018.2.14&f=AJAX&e=-------en--20--1--txt-txIN--------
- Verbatim (headline): "Louderback and Ferral Elected ... The Complete Vote From All the Wards Throughout the City." Full precinct table (Louderback, Bradford, Cary, Ferral, Total) printed E+1 morning.
- Verbatim (totals): "Totals ... 1[2],7[2]0 10,403 10,848 12,493 23,336 ... [Loude]rback's majority, 2317. Ferral's majority, 16[45/60]. ... The total vote cast was 23,332. The vote by Wards was as follows: First Ward 1168, Second 1480, Third 667, Fourth 1426, Fifth 9[4]8, Sixth 1060, Seventh 1813, Eighth 2687, Ninth 1790, Tenth 2798, Eleventh 4085, Twelfth 3318." (my ward sum: 23,240; printed 23,332; OCR digit slips)
- CAUTION vs gate: printed total 23,332 EXCEEDS the official-final gate 22,942 by 390. Either the modern official figure counts differently (e.g. one contest's votes vs ballots) or OCR/table garble; 12,720+10,403 = 23,123 (Police Judge contest) and 10,848+12,493 = 23,341 (Criminal Judge contest). FLAG for human: verify printed grand total on scan.
- Verbatim (comparative): "The vote cast was 10,671 less than that of the late Municipal and Legislative election, and 19,176 less than the vote cast at the Presidential election."
- Verdict: complete overnight count printed E+1 = ~100% election-night count.
- OCR saved: wave3/out/sec1877_2_14.txt, sec1877_2_4.txt

### 8: 1878-06-19 Constitutional Convention delegates. STATUS: FOUND (explicit counted-by-press number: ~6,000 of ~27,000)
- Source: Daily Alta California, 1878-06-20, "THE ELECTION." DAC18780620.2.16 (search "election" srpos 3); "THE RESULT." DAC18780620.2.4.
- OCR retrieval URL: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=DAC18780620.2.16&f=AJAX&e=-------en--20--1--txt-txIN--------
- Verbatim (headline): "THE ELECTION. The Kearney Ticket Probably Ahead. About 27,000 Votes Polled. Only a Small Number Counted."
- Verbatim (THE COUNTED NUMBER): "Up to the hour of going to press, about 600[0] votes had been reported as counted, the largest number being in the Kearney Wards, and nearly one-fifth of them in his stronghold of the Tenth Ward."
- Corroboration (2.4): "the returns from the city are scattering, and show only about one-fifth of the whole vote" (~5,400 of 26,973 ~ 20%; consistent with ~6,000 = 22%).
- Verbatim (poll list): "The total number of votes polled reached 2[6],973, and two small precincts to come in" + per-ward poll table (First 1318 ... Twelfth 3060). Official final gate 27,098: 26,973 + 2 missing precincts fits.
- Verbatim (why slow): "In some precincts there were scarcely any straight tickets polled, and more than half of them were badly scratched. This naturally caused the counting to be extremely slow ... nearly [6]00 names to be counted [on 186 precinct ballots]." Also: "the reports sent from by far the largest number of the Precincts were so meagre and imperfect as to be absolutely valueless ... To increase this evil the telephones gave way".
- Per-ward partial counted returns (Non-Partisan vs Kearney) listed; my sum of quoted counted pairs ~ 3.7-3.8k (subset of the ~6,000).
- ELECTION-NIGHT SHARE: ~6,000 / 27,098 = ~22% counted by press (E+1 03:00).
- OCR saved: wave3/out/sec1878_2_16.txt, sec1878_2_4.txt

### 9: 1879-05-07 ratification of 1879 Constitution. STATUS: FOUND (near-COMPLETE overnight count from Registrar's official returns)
- Source: Daily Alta California, 1879-05-08, "YESTERDAY'S ELECTION. / The City Returns." DAC18790508.2.16 (search "returns" srpos 4); statewide "SUMMARY OF THE RETURNS." DAC18790508.2.18; "THE STATE VOTE." DAC18790508.2.17.
- OCR retrieval URL: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=DAC18790508.2.16&f=AJAX&e=-------en--20--1--txt-txIN--------
- Verbatim (completeness): "The following is the summary of votes cast in the various Wards and Precincts of the city, in accordance with the official returns furnished at the Registrar's office. It is complete with the exception of three Precincts of the Second Ward, 2, 6, and 8, which the Inspectors of Election either neglected or refused to furnish to the Registrar."
- Verbatim (headline): "The City Gives a Majority of 2263 Against It, and the Interior 9000 in Its Favor."
- Full precinct-by-precinct For/Against table with ward recapitulation printed E+1. Recap totals line (OCR-garbled): "Totals 1[?],383 17,396 38,8[3]4 3,711 [5],918" and "Total number of votes polled 38,834. Majority against the new Constitution [2,263]".
- CAUTION vs gate: OCR total 38,834 exceeds the official-final gate 38,034 by 800; digits garbled. SoS-certified SF ratification vote is consistent with majority-against 2,263. FLAG for human scan read of the recapitulation totals.
- Statewide: "SUMMARY OF THE RETURNS ... Though necessarily incomplete, the general drift of the vote of each county is shown ... majority for [the Constitution outside SF of about 6,000]."
- Verdict: the suspense election produced an essentially COMPLETE city count overnight (all but 3 of ~200 precincts), printed E+1 = ~98-100% election-night count.
- OCR saved: wave3/out/sec1879_2_16.txt, sec1879_2_18.txt

## Verification screenshots (imgs/, viewer anchored to article; human can zoom via the same URL)
- imgs/shot_1859_DAC18590908_2_17.png  https://cdnc.ucr.edu/?a=d&d=DAC18590908.2.17
- imgs/shot_1862_DAC18620904_2_3.png   https://cdnc.ucr.edu/?a=d&d=DAC18620904.2.3
- imgs/shot_1863_DAC18630903_2_4.png   https://cdnc.ucr.edu/?a=d&d=DAC18630903.2.4
- imgs/shot_1870_DAC18700908_2_5.png   https://cdnc.ucr.edu/?a=d&d=DAC18700908.2.5
- imgs/shot_1871_DAC18710907_2_7.png   https://cdnc.ucr.edu/?a=d&d=DAC18710907.2.7
- imgs/shot_1873_DAC18731016_2_14.png  https://cdnc.ucr.edu/?a=d&d=DAC18731016.2.14
- imgs/shot_1877_DAC18771018_2_14.png  https://cdnc.ucr.edu/?a=d&d=DAC18771018.2.14
- imgs/shot_1878_DAC18780620_2_16.png  https://cdnc.ucr.edu/?a=d&d=DAC18780620.2.16
- imgs/shot_1879_DAC18790508_2_16.png  https://cdnc.ucr.edu/?a=d&d=DAC18790508.2.16

## Human verification asks (paths + claimed values + fail criteria)
1. 1859 1st District: article states "314 straight tickets had been counted" but gov figures sum 374 (233+20+121). Read scan at DAC18590908.2.17 (page 1). Fail if neither 314 nor 374 matches.
2. 1862 12th District (OFFICIAL) table + citywide "Comparative Vote" aggregate: table zones did not OCR. Read scan at DAC18620904.2.3 / .2.2 (page 1). Claimed: aggregate near 8,813.
3. 1863 2 a.m. district figures with [] garbles (1st Low 335 vs 835; 5th Downey 326 vs 826; 8th Downey 316 vs 816). Read scan at DAC18630903.2.4.
4. 1870 citywide returns table (DAC18700908.2.5): OCR unusable; hand-read to build a counted floor. Claimed press-time 3:30 a.m., counting to resume/finish by 9 a.m.
5. 1873 total: claimed printed total = 15,594 (matches gate exactly via 26,017 - 10,423 arithmetic). Read "THE VOTE" paragraph at DAC18731016.2.14. Fail if the printed total is not 15,594.
6. 1877 grand total: OCR says 23,332/23,336, gate says 22,942 (delta +390). Read totals row at DAC18771018.2.14. Fail if scan total is 22,942 (then OCR wrong) or confirm mismatch (then note vs official).
7. 1879 recapitulation: OCR "Total number of votes polled 38,834" vs gate 38,034 (delta +800). Read recap at DAC18790508.2.16. Majority-against should read 2,263.

## Dead ends / notes
- SFC (San Francisco Call) has no CDNC coverage before 1890; DAC was the only same-city CDNC paper for all 9 dates. Sacramento Daily Union backup never needed.
- Old DAC issue pages carry NO inline TOC (unlike 1896-era issues); the TOC anchors of cdnc_fetch.js parse 0 sections. Search + page-level getSectionText (OID DACyyyymmdd.1.<page>) is the working route; documented in Method update above.
- No "no count by press time" dead ends: every one of the 9 day-after issues carried overnight count material.
