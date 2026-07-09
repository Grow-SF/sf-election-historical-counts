# Wave 4 NewsBank recovery: 1914-1916 SF Chronicle night counts

Agent: night-count recovery, session 2026-07-08.
Method: NewsBank image edition via SFPL ezproxy (Chrome CDP :9222), sweep_section.js captures, vision transcription.
Gate ceilings (official finals, no claim may exceed):
- 1914-08-25 state primary: 97,417
- 1915-09-28 municipal primary: 119,105
- 1915-11-09 general municipal: 83,297
- 1916-05-02 presidential primary: 48,150
- 1916-08-29 state primary: 76,902

Cutoff: E+1 06:00. Morning-edition stamp = E+1 T03:00.

## Status log
- [x] 1914-08-25 (issue 1914-08-26) DEAD END documented
- [x] 1915-09-28 (issue 1915-09-29) floor 27,856
- [x] 1915-11-09 (issue 1915-11-10) 83,138
- [x] 1916-05-02 (issue 1916-05-03) 46,832
- [x] 1916-08-29 (issue 1916-08-30) floor 54,346

## Findings
(appended as discovered)

### 1914-08-25 state primary, Chronicle 1914-08-26 (masthead verified: "SAN FRANCISCO, CAL., WEDNESDAY, AUGUST 26, 1914", VOL. CV NO. 72)
- p1 s0: headline "Captain John D. Fredericks Undoubtedly Nominated for Governor". Box "PROBABLE RESULT / RETURNS MEAGER": "The counting of ballots throughout the State is proceeding slower than at any previous election. At midnight last night it was impossible to obtain sufficient returns upon which forecasts could be made with any certainty. This situation, unparalleled in the State's political history, is due to the fact that in some places only Republican ballots [...]" (verbatim from scan sweep_19140825_issue19140826_p1_s0.png)
- p1 s0 bottom: lead begins "AT 2 o'clock this morning it was possible to tabulate incomplete re[turns]..." Need s1+ for the numbers.
- Capture cmd: node scripts/archive-recovery/sweep_section.js 1914-08-25 1914-08-26 1 3 1

### 1915-11-09 general municipal, Chronicle 1915-11-10 (masthead verified: "SAN FRANCISCO, CAL., WEDNESDAY, NOVEMBER 10, 1915", VOL. CVII NO. 118)
- p1 s0: top of page dominated by PPIE, Yoshihito coronation, Ancona sinking, GOP convention. No election banner in top band; election returns likely lower on p1 or inside pages.
- p1 s1 (sweep_19140825_issue19140826_p1_s1.png): VERBATIM lead: "AT 2 o'clock this morning it was possible to tabulate incomplete returns from only 419 precincts out of a total in the State of 4,463, and these figures were available for Governor, Lieutenant-Governor and United States Senator only. The precincts heard from include 130 in San Francisco and scattered precincts from the San Joaquin and Santa Clara valleys and a few south of the Tehachapi. The totals are as follows:" Tables that follow are STATEWIDE (419-precinct) not SF-only: GOVERNOR Rep: Fredericks 3971, Belshaw 562, Keesling 2520, Ralston 735; Dem: Curtin 255, Hall 288, King 610, Van Wyck 213, White 4003; Prog: Johnson 1313. LT-GOV Rep: Eshleman 2722, Bauer 1223, Shinn 1792, Ward 614, Williams 397; Dem Snyder 1571; Prog Eshleman 1383. US SENATOR Rep: Knowland 3209, Shortridge 3945; Dem: Griffin 630, Phelan 1423; Prog: Heney 1602, Rowell 579.
- p1 s2 (sweep_19140825_issue19140826_p1_s2.png): VERBATIM: "At 2:30 o'clock this morning the Associated Press was able to give only incomplete returns from 419 precincts out of a total of 4463 owing to unprecedented slowness in the counting of ballots throughout the State." Also "PROBABLE RESULT RETURNS MEAGER" box notes "the two San Francisco morning newspapers worked in conjunction, operating a joint election bureau at the City Hall and co-operating with the Associated Press. It was after midnight before the Associated Press could give out returns on general results that were anywhere near authentic."
- INTERPRETATION: only 130 SF precincts tabulated by 02:00; no SF citywide ballot count printed in these bands. Statewide 419-precinct contest sums are not SF-scoped; NOT usable as SF night floor. Need SF-specific table (maybe p2/p3).
- 1915-11-10 p2: all war/convention news (scan sweep_19151109_issue19151110_p2_s0.png).
- 1915-11-10 p3 (FIND): headline stack (scan sweep_19151109_issue19151110_p3_s0.png, top left): "MIXED RESULT IN VOTING AT CITY ELECTION / Edward J. Brandon in First Place Among Supervisorial Candidates / ONLY 83,138 ENTER POLLS / John Ginty Scores Sweeping Victory for Assessorship; Fitzpatrick Wins". Election WAS Nov 9 (p1 simply carried no election news; mayor not on ballot).
- p3 s1/s2 body VERBATIM: "In a total vote of 83,138, or less than 50 per cent of the registration of the city, which is 180,000, complete returns from yesterday's final municipal election show a mixed result in the Supervisors ticket." (scans ..._p3_s1.png, ..._p3_s2.png)
- Box "CANDIDATES LEADING ON FINAL RETURNS" (p3 s0/s1 left rail): POLICE JUDGE Fitzpatrick 44,240, Bath 35,682. ASSESSOR Ginty 65,480, McCarthy 12,302. SUPERVISORS (18 listed, multi-seat, not a ballot count): Brandon 46,187; Wolfe 45,043; Mulvihill 41,955; Kortick 39,372; Welch 39,008; Lahaney 37,590; Hayden 37,287; Hynes 36,624; Hocks 35,832; Hansen 34,608; McSheehy 34,358; Vogelsang 33,529; Herget 32,515; Webster 31,508; Payot 30,928; Murdock 30,054; Kohlberg 26,562; Hagerty 25,988.
- Body confirms: "Timothy I. Fitzpatrick was elected Police Judge over Edwin G. Bath by the substantial majority of 8,558. Fitzpatrick's vote was 44,240. Bath received 35,682." (8,558 = 44,240-35,682 checks) and "The Assessorship contest was a sweeping victory for John Ginty, who polled 65,480."
- ARITHMETIC: Police Judge sum 44,240+35,682=79,922 <= 83,138. Assessor 65,480+12,302=77,782 <= 83,138. Citywide stated total 83,138 <= official final 83,297 (99.81%). PASSES gates.
- VERDICT 1915-11-09: night count printed E+1 morning = 83,138 total vote, called "complete returns"; floor by contest sum 79,922. observed_at 1915-11-10T03:00:00.

### 1915-09-28 municipal primary, Chronicle 1915-09-29 (masthead verified: "SAN FRANCISCO CAL., WEDNESDAY, SEPTEMBER 29, 1915", VOL. CVII NO. 76)
- p1 banner: "ROLPH IS RE-ELECTED BY OVERWHELMING MAJORITY / MAYOR CHOSEN FOR SECOND TERM WITH RECORD LANDSLIDE" (scan sweep_19150928_issue19150929_p1_s0.png).
- Box "Seven Offices Filled at the Primaries" (p1 s1, scan sweep_19150928_issue19150929_p1_s1.png) VERBATIM: "These returns, covering the vote in 189 complete precincts, show the following ballot cast for the various leading candidates:" MAYOR: Rolph 16,396; Schmitz 8,059; Gallagher 3,401. POLICE JUDGES (SECOND AND THIRD QUALIFY): Oppenheim 16,166; Fitzpatrick 8,135; Bath 6,862; Taaffe 6,387; Brady 5,415. DISTRICT ATTORNEY: Fickert 15,859; Sweigert 10,511. ASSESSOR: Ginty 14,232; McCarthy 7,526; McLaughlin 4,307. SHERIFF: Finn 14,726; McLeran 6,701; Eggers 4,801. SUPERVISORS (EIGHTEEN TO QUALIFY): Hayden 11,367 ... Dwyer 1,706. Then: "Estimated total vote cast, 115,000. Total registration, 179,591."
- Body VERBATIM (p1 s1 left col): "With the complete count tabulated from 189 out of 651 precincts in the city, at an early hour this morning Registrar Zemansky predicted the election at the primary of Ginty for Assessor, Oppenheim for Police Judge, Finn for Sheriff and Fickert for District Attorney, in addition to Mayor Rolph."
- Body (p1 s2): "With the single exception of the gubernatorial election of 1914, when over 134,000 votes were cast in San Francisco, yesterday's vote was the heaviest ever polled in the city, being approximately 60[?] per cent of the registration of 179,591." (subhead reads "68 PER CENT VOTE"); "Four years ago Rolph was elected with 47,427 votes. Yesterday he received approximately 70,000 votes." (ESTIMATES, not counts)
- ARITHMETIC: Mayor sum (single-seat, all 3 listed) 16,396+8,059+3,401=27,856 counted in 189/651 complete precincts = NIGHT FLOOR. Sheriff 26,228; DA 26,370; Assessor 26,065 (all consistent, < Mayor). 27,856 <= gate 119,105. "115,000" is an ESTIMATE (explicitly "Estimated total vote cast"), NOT a count.
- VERDICT 1915-09-28: night_partial; floor 27,856 (Mayor contest, 189/651 precincts complete, clocked "at an early hour this morning"). observed_at 1915-09-29T03:00:00.

### 1916-05-02 presidential primary, Chronicle 1916-05-03 (masthead verified: "SAN FRANCISCO CAL., WEDNESDAY, MAY 3, 1916", VOL. CVIII NO. 109)
- p1 (scan sweep_19160502_issue19160503_p1_s0.png): banner "SWEEPING VICTORY WON BY REGULAR TICKET OF G.O.P."; box "REGULARS ARE LEADING THREE TO TWO" VERBATIM: "WITH approximately 60 per cent of the vote in the entire State counted at 2 o'clock, when 2429 precincts had been heard from out of 4347 in the State, the lead of the Regular Republican ticket indicated a majority of more than 25,000 for the Regular ticket, with a total vote of over 200,000." (STATEWIDE)
- p1 s2 (SF passage, scan sweep_19160502_issue19160503_p1_s2.png) VERBATIM: "The result in San Francisco at a late hour indicated that the city had been carried by the regular Republicans by a majority of more than 6000 in a total vote for the three parties polled of under 50,000."
- p2 (THE FIND; scans sweep_19160502_issue19160503_p2_s0.png + deep zoom zpt_19160502_issue19160503_p2_sfbox.png, crops nb_19160503_p2_sfbox_zoom.png, nb_19160503_p2_sfbox_deep_top.png): box "Regulars Lead by 6000 Votes in S. F." VERBATIM: "WITH 362 out of 370 precincts complete in San Francisco at midnight the regular Republicans were leading by 6000. Registrar Zemansky estimated that the Democrats had polled 12,000 out of a total vote of 46,832 returned with the count complete, except eight precincts. The Progressives' total in the city, according to the Registrar, will not run more than 1000. The totals on seven candidates on the regular Republican and United Republican or Earl tickets were as follows: Regular - Bordwell, 19,764; Cole, 17,743; Krebs, 17,760; Keesling, 20,297; Crocker, 20,702; Ackerman, 19,656[?]; Chapman, 19,563. Earl ticket - Bulla, 13,727; Anderson, 14,321; Strong, 12,875; Power, 13,681; Boude, 11,560[?]; Crall, 11,569; Collier, 12,397."
- p2 county table "Figures Tell of Republican Victory / Unofficial Returns Up to Midnight": row SAN FRANCISCO 370 precincts, 362 heard from, Bordwell 19,764, Bulla 13,727. State totals row: 4,347 / 2,429 / 74,280 / 53,218.
- DIGIT CHECK on 46,832 ("6" vs "8"): pixels at deep zoom read 46,832; arithmetic: GOP ~33.5k (19,764+13,727) + Dem 12,000 + Prog <1,000 = ~46.5k, matches 46,832; 48,832 would EXCEED official final 48,150. Confirmed 46,832.
- ARITHMETIC GATES: 46,832 <= 48,150 (97.26%). Missing 8/370 precincts (~2.2%) explains the 1,318 gap to final. PASSES.
- VERDICT 1916-05-02: night count = 46,832 total vote returned, 362/370 precincts, clocked "at midnight". Registrar-attributed citywide figure printed E+1 morning. observed_at 1916-05-03T03:00:00 (statement clocked at midnight).

### 1916-08-29 state primary, Chronicle 1916-08-30 (masthead verified: "SAN FRANCISCO, CAL., WEDNESDAY, AUGUST 30, 1916", VOL. CIX NO. 46)
- p1 banner: "LATEST RETURNS SHOW JOHNSON IS NOMINATED"; left col headline "10,000 IS S.F. LEAD IN FINAL FIGURES" (scan sweep_19160829_issue19160830_p1_s0.png).
- Box "Latest Primary Election Returns" (p1, zoom nb_19160830_p1_returnsbox_zoom.png) VERBATIM: "ENTIRE STATE / 2816 Precincts out of 5443. / Booth 77,866 / Johnson 95,248 / SAN FRANCISCO / Total vote, 575 Precincts. / Booth 22,062 / Johnson 32,284 / ALAMEDA COUNTY / With 382 out of 410 Precincts. / Johnson 21,101 / Booth 16,578 / CONGRESSMAN FOURTH DISTRICT Republican Kahn ... No contest / CONGRESSMAN FIFTH DISTRICT Republican Nolan 18,065[?]; Root 7,708; Democratic Nolan 6,551; Tracy 2,004[?]; JUDGES Cabaniss 38,974; Conlan 32,028..." (judges are multi-candidate/nonpartisan; not used)
- Body (p1 s1/s2, scan sweep_19160829_issue19160830_p1_s1.png): "LEAD OF NEARLY 20,000 IS SHOWN. The figures as they stand on about one-half of the State count at 1:30 o'clock this morning are as follows: Booth 77,866; Johnson 95,248." "FIGURES TABULATED AT 12:45 FAVOR JOHNSON ... These figures ... were tabulated at 1:30 o'clock this morning." "San Francisco gives Johnson 10,000 majority."
- p2 (scan sweep_19160829_issue19160830_p2_s0.png): "JOHNSON WINS NOMINATION IN CLOSE RACE / San Francisco Gives Him Majority of 10,000 in Complete Count"; "Vote in Assembly Districts / Figures Are Nearly Complete: The complete vote in the various Assembly districts of San Francisco on Congressional and Legislative nominees was announced at 1:30 o'clock this morning as follows: [district lists]".
- ARITHMETIC: SF Rep US Senator contest (single-seat) Booth 22,062 + Johnson 32,284 = 54,346 counted in ALL 575 SF precincts ("Total vote, 575 Precincts", "Complete Count"), announced by 1:30 a.m. 54,346 <= gate 76,902 (70.7%). Floor only: Dem/other-party senatorial ballots and blanks not included in the printed pair.
- VERDICT 1916-08-29: night count floor 54,346 (Rep Senate contest, 575/575 precincts complete overnight, clocked 1:30 a.m.). observed_at 1916-08-30T03:00:00.

### 1914-08-25 (continued): section front, printed page 9 (NewsBank viewer page 7)
- Section masthead: "GENERAL NEWS ... PAGES 9 to 16 ... SAN FRANCISCO, CAL., WEDNESDAY, AUGUST 26, 1914" (scan sweep_19140825_issue19140826_p7_s0.png)
- Banner VERBATIM: "COUNT OF VOTE IN CITY PROCEEDS SLOWLY / Indications Are That Shortridge-Knowland Race Is Close"
- Box VERBATIM (zoom nb_19140826_p9_4precincts_zoom.png): "Four Complete Precincts / Returns Up to 2 O'Clock: Up to 2:15 o'clock this morning only four precincts in San Francisco had been counted complete. These are the twenty-sixth precinct of the Forty-second district, Twenty-first and Dolores; second of the Twenty-second, Army and Folsom; thirty-sixth of the Twenty-seventh, Ashbury and Frederick; third of the Twenty-second, Twenty-third and Hampshire. The result for the leading State and Congressional offices and the offices of San Francisco county is: ..." 4-precinct totals include GOVERNOR (Rep Belshaw 27, Fredericks 78, Keesling 97, Ralston 30; Dem Curtin 37, Hall 32, King 9, Van Wyck 25, White 8; Prog Johnson 121; sum 464) and CHIEF JUSTICE SUPREME COURT (Angellotti 214, Bordwell 70, Conley 207; sum 491).
- SF color VERBATIM (p7 s2, scan sweep_19140825_issue19140826_p7_s2.png): "Between 60 and 70 per cent of the registration was cast in most of the precincts, the voting being lively late in the afternoon after stores and shops had closed for the day." AND the dead-end sentence: "The count is proceeding slowly, and in the case of the closer contests, it is believed the result will not be known before late tomorrow. Few ballots were voted straight, many writing in names."
- Registrar estimate VERBATIM (p7 s1, "Early Vote Was Much Heavier Than Usual"): "When the polls closed at 7 o'clock last evening Zemansky estimated that the vote would be at least 85,000 out of a total registration of 147,130." (ESTIMATE, not a count; excluded per rules)
- Pages checked with no SF count table: printed p1-p6 (viewer p1-p6), printed p9 (viewer p7), printed p10 (viewer p8, sports). Viewer p9 = printed p11 not fully read (s0-s2 captured; sports/ads continue).
- VERDICT 1914-08-25: SF ELECTION-NIGHT COUNT UNAVAILABLE in day-after Chronicle. Documented: only 4 of SF's precincts counted complete by 02:15; 130 SF precincts folded into 419-precinct STATEWIDE tabulation (not SF-separated); Zemansky poll-close estimate "at least 85,000" is not a count. SF-scoped counted floor is negligible: 491 (Chief Justice contest sum, 4 precincts). Gate 97,417 not approached.

## SUMMARY TABLE
| election | night figure | basis | precincts | source (Chronicle) | pct of official final |
|---|---|---|---|---|---|
| 1914-08-25 state primary | UNAVAILABLE (floor 491) | "COUNT OF VOTE IN CITY PROCEEDS SLOWLY"; 4 precincts complete by 02:15 | 4/(~890?) SF precincts complete; 130 partial in statewide tab | 1914-08-26 p1 + p9 | ~0.5% floor of 97,417 |
| 1915-09-28 muni primary | 27,856 floor (Mayor: Rolph 16,396 + Schmitz 8,059 + Gallagher 3,401) | "complete count tabulated from 189 out of 651 precincts... at an early hour this morning" | 189/651 complete | 1915-09-29 p1 | 23.4% of 119,105 (floor) |
| 1915-11-09 general muni | 83,138 total vote | "In a total vote of 83,138 ... complete returns from yesterday's final municipal election"; headline "ONLY 83,138 ENTER POLLS" | complete (stated) | 1915-11-10 p3 | 99.81% of 83,297 |
| 1916-05-02 pres primary | 46,832 total vote returned | "362 out of 370 precincts complete in San Francisco at midnight... total vote of 46,832 returned with the count complete, except eight precincts" (Registrar Zemansky) | 362/370 | 1916-05-03 p2 | 97.26% of 48,150 |
| 1916-08-29 state primary | 54,346 floor (Rep US Sen: Booth 22,062 + Johnson 32,284) | "SAN FRANCISCO / Total vote, 575 Precincts"; "Complete Count"; assembly-district figures "announced at 1:30 o'clock this morning" | 575/575 complete | 1916-08-30 p1 (+p2) | 70.7% of 76,902 (floor) |

All figures <= their gate ceilings. Reproduce any capture with:
node scripts/archive-recovery/sweep_section.js <ELECTION> <ISSUE> <P0> <P1> <WIN>  (NewsBank WORLDNEWS image edition via https://infoweb-newsbank-com.ezproxy.sfpl.org search alltext=election, YMD_date=<issue-date>, sort YMD_date:A)
Scans in mirror/newsbank/scans/ (gitignored); reading crops in scratchpad/imgs/.
