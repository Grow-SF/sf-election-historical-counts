# Wave 3: SF election-night counts 1907-1910 (CDNC, day-after SF Call)

Agent salvage file. Written as I go. Stamp convention: E+1 T03:00 morning edition; cutoff E+1 06:00.
Access: cdnc.ucr.edu via scripts/archive-recovery/cdnc_fetch.js (raw CDP through Chrome :9222).

## Targets and gate ceilings (official final total votes)
| # | election | day-after issue | final (ceiling) | verdict |
|---|----------|-----------------|-----------------|---------|
| 1 | 1907-08-13 municipal primary | SFC19070814 | 22,851 | FOUND: printed partial total 20,801 (91.0%), "*Incomplete", arithmetic-locked |
| 2 | 1908-05-05 state primary | SFC19080506 | 24,178 | GATE FAIL: printed overnight total 24,305 exceeds final by 127; no counted partial below ceiling |
| 3 | 1908-08-11 state primary | SFC19080812 | 22,698 | FOUND: republican-primary partial 22,117 (97.4%), one precinct missing; DENOMINATOR-KIND FLAG (all-party vote >30,000) |
| 4 | 1909-06-22 bond special | SFC19090623 | 24,058 | UPGRADED: hand-summed Prop-1 floor 23,073 (95.9%), pending operator digit check; totals row blank in print |
| 5 | 1909-08-17 municipal primary | SFC19090818 | 38,317 | FOUND: midnight partials 59/149 precincts; rep. mayor contest floor 5,452 (14.2%) |
| 6 | 1909-11-02 general municipal (McCarthy) | SFC19091103 | 65,065 | DEAD END for numeric night count (documented); midnight = "indicated plurality of 10,000", winners called by 10 pm; complete 64,931 only day+1 8pm |
| 7 | 1910-01-14 Spring Valley bond | SFC19100115 | 35,015 | FOUND: COMPLETE overnight count 34,939 (99.8%), triple arithmetic-locked |
| 8 | 1910-08-16 state primary | SFC19100817 | 47,532 | FOUND: midnight partial 100 precincts; rep. governor contest floor 9,236-9,536 (~20%), Anderson digit needs hand-read |

## Findings

### PRIOR-WAVE OVERLAP NOTE
agents/cdnc_1908_1909.md (earlier wave, same scratchpad) already worked targets 4 (1909-06-22) and 6 (1909-11-02) plus the non-target 1908 specials. Its verdicts: 1909-06-22 = prose approximation "approximated 22,000" only, district tables printed with BLANK totals rows; 1909-11-02 = night qualitative only (midnight indicated pluralities), complete unofficial count 64,931 only at day+1 8pm (SFC19091104.2.18). I re-verified the 1909-11-03 issue independently (below) and concur.

### 1: 1907-08-13 municipal primary (final 22,851) - FOUND: printed partial total 20,801, marked *Incomplete, morning-after edition
Issue SFC19070814 (https://cdnc.ucr.edu/?a=d&d=SFC19070814), 202 sections.
- THE FIND: p2 SFC19070814.2.10.3 "The Vote by Assembly Districts": 18-district table (28th-45th), party columns (Ryan Republicans, Herrin Republicans, Irregular Republicans, McNab Democrats, Mahoney Democrats, Eagan Union Labor, Casey Union Labor, + delegates columns). Printed totals line, VERIFIED BY MY OWN READ OF THE PAGE IMAGE (screenshot cdnc_19070814_p2_table.png):
  "Total republican vote, 12,019; total democratic vote, 3,293; total union labor vote, 5,310; total socialist vote, 179. Total vote, 20,801. *Incomplete."
  ARITHMETIC LOCK: 12,019 + 3,293 + 5,310 + 179 = 20,801 exactly. (OCR text had garbled these as 12,010 / 0,310 / 20,601; the page image + exact sum pin the true digits.)
  The asterisk marks districts *Thirty-third and *Thirty-seventh as incomplete, so 20,801 is a PARTIAL (counted-so-far), i.e. a true night count, not a complete total.
  Gate: 20,801 <= final 22,851 (91.0%). PASS.
- Night clocking: p1 SFC19070814.2.5 (Van Smith lead), verbatim: "On the face of the incomplete returns available at midnight the Casey-Sweeney independent labor forces had elected but 13 delegates out of a total of 198." and "The total vote of all parties cast yesterday will approximate 22,000, or about twice the primary vote of 1906 and substantially the vote polled at the 1905 primaries. The total republican vote will approximate 13,000, union labor 5,300, democratic 3,200." [approximation class, projection; the table's 20,801 is the counted figure]
- Corroboration of count speed: p2 SFC19070814.2.10 sub-article "Election Is Orderly All Over City": "Good order and thorough organization among the election officers resulted in ... the speedy manner in which the returns were received after the election was over."
- Stamp: E+1 T03:00 (morning-after edition convention). Class: partial, counted ballots, districts 33 and 37 incomplete.
- Provenance:
  - TOC: https://cdnc.ucr.edu/?a=d&d=SFC19070814
  - Table OCR: node scripts/archive-recovery/cdnc_fetch.js SFC19070814 SFC19070814.2.10.3 (AJAX https://cdnc.ucr.edu/?a=da&command=getSectionText&d=SFC19070814.2.10.3&f=AJAX&e=-------en--20--1--txt-txIN--------)
  - Lead OCR: cdnc_fetch.js SFC19070814 SFC19070814.2.2 / 2.5; searches: txq=total+vote, txq=counted (dafdq=14&dafmq=08&dafyq=1907, puq=SFC; URLs in mirror/cdnc/SFC19070814/search_*.txt)
  - Article permalink: https://cdnc.ucr.edu/?a=d&d=SFC19070814.2.10.3
  - Screenshot: scratchpad/imgs/cdnc_19070814_p2_table.png (totals line legible at bottom of table)
  - Mirrors: mirror/cdnc/SFC19070814/section_SFC19070814.2.10.3.txt, search_total_vote.txt, search_counted.txt, toc.json

### 2: 1908-05-05 state primary (final 24,178) - PRINTED OVERNIGHT TOTAL 24,305 EXCEEDS FINAL: GATE FAIL, documented as over-final compilation
Issue SFC19080506 (https://cdnc.ucr.edu/?a=d&d=SFC19080506), 192 sections (issue starts at p9; p1-8 are fleet-arrival pages).
- p11 SFC19080506.2.3 "HERRINISM CRUSHED BY CLEAN VOTE" (Van Smith). Verbatim:
  "Herrin and his strikers were crushed under an avalanche of votes. The vote reached a total of 24,305, of which approximately 18,000 were cast by republicans."
  "The vote cast in San Francisco breaks all primary election records, exceeding the primary votes of 1905 and 1907 by nearly 2,000."
- p9 SFC19080506.2.2 front banner, verbatim: "The vote broke all primary election records, reaching a grand total of 24,305, or about 2,000 more votes than were cast in the mu[nicipal primary of 1907]." Also "The anti-McNab democrats won seven out of eighteen assembly districts, with a total of 19 out of 64 delegates in the state convention."
- GATE: 24,305 > official final 24,178 (by 127, +0.5%). FAIL as a claimable night count. Class: overnight compiled grand total, slightly inflated vs the official canvass. It IS evidence the count was effectively complete by press time (E+1 T03:00), but the figure itself may not be claimed per the ceiling rule.
- Independent cross-check that the true total was ~24,150, not 24,305: SF Call 1908-05-12 (SFC19080512.2.3, mirrored by the earlier wave) on the May 11 bond special: "The vote was only 600 below that cast at the recent primaries" with bond total 23,550 => primaries ~24,150, consistent with official 24,178 and against 24,305.
- Party-level partial below ceiling: only "approximately 18,000 were cast by republicans" (approximation class, not a count).
- NO by-district numeric vote table in this issue (TOC swept for vote/district/return/tabulation titles; searches txq=total+vote (7 hits, all narrative), scoped dafdq=06&dafmq=05&dafyq=1908&puq=SFC). The paper prioritized the Atlantic fleet arrival (p1-8).
- Verdict: night count = none claimable; documented over-final printed total 24,305. Count-complete-overnight evidence stands.
- Provenance:
  - TOC: https://cdnc.ucr.edu/?a=d&d=SFC19080506
  - OCR: cdnc_fetch.js SFC19080506 SFC19080506.2.3 / 2.2 / 2.44; search https://cdnc.ucr.edu/?a=q&hs=1&r=1&results=1&txq=total+vote&txf=txIN&ssnip=txt&puq=SFC&dafdq=06&dafmq=05&dafyq=1908&datdq=06&datmq=05&datyq=1908&e=-------en--20--1--txt-txIN--------
  - Screenshot: scratchpad/imgs/cdnc_19080506_p9_lead.png
  - Mirrors: mirror/cdnc/SFC19080506/section_SFC19080506.2.3.txt, section_SFC19080506.2.2.txt, section_SFC19080506.2.44.txt, search_total_vote.txt, toc.json

### 3: 1908-08-11 state primary (final 22,698) - FOUND republican-primary night partial 22,117 (one precinct missing); DENOMINATOR-KIND FLAG
Issue SFC19080812 (https://cdnc.ucr.edu/?a=d&d=SFC19080812), 220 sections.
- THE FIND: p2 SFC19080812.2.14.2 "The Vote of the City by Districts": 18-district table, columns Assembly Districts | Delegates | L.-R. League | Rep. Machine | McNab | Bell. Printed totals row (read from page image, screenshot cdnc_19080812_p2_table.png):
  "Totals .... 173 | 10,371 | 11,746 | 4,941 | 3,589"
  Footnote verbatim: "*One precinct missing -- ninety-second of the thirty-ninth district." / "Machine delegates in local republican convention, 108. League delegates in local republican convention, 65."
  MY COLUMN SUMS from the page image: League 10,371 EXACT match; Machine 11,746 EXACT match (both arithmetic-locked). McNab col sums 5,136 and Bell col 3,408 vs printed 4,941/3,589: a few low-contrast democratic cells need operator hand-read, but the republican columns are locked.
  District rows (image read): 28th 232/341/82/22; 29th 127/245/36/57; 30th 71/211/231/52; 31st 311/444/232/136; 32nd 1,007/248/530/296; 33rd 604/730/671/344; 34th 1,053/976/424/275; 35th 751/587/379/158; 36th 335/473/96/124; 37th 1,319/1,573/508/350; 38th 816/1,309/421/295; *39th 1,469/975/491/394; 40th 729/1,202/246/193; 41st 755/1,129/367/257; 42nd 209/196/52/50; 43rd 236/281/45/37; 44th 189/319/64/76; 45th 158/507/261/292.
- Night clocking + context: p1 SFC19080812.2.2 (Van Smith lead), verbatim:
  "Completed returns will show that the total vote exceeded 30,000, or about 2,000 less than were cast in the Stratton primaries of 1899, when the record vote of 32,521 was polled. Out of the total of 30,000 approximately 22,000 republican ballots were cast. Corrected returns will probably show that out of a total of 22,000 the machine tickets received approximately 11,600, or a clear majority of 1,300 in the city."
  "the incomplete returns show that the machine won the [thirty-seventh] district by a narrow margin" [night = incomplete returns]
- GATE ANALYSIS (IMPORTANT):
  - Republican primary counted partial = 10,371 + 11,746 = 22,117 <= 22,698 ceiling (97.4%). PASS as a night partial IF the official final 22,698 denominates the REPUBLICAN primary.
  - All-party table total = 22,117 + 4,941 + 3,589 = 30,647 (+ union labor, small, not tabulated: "The union labor vote was not heavy" p2 2.14.1) EXCEEDS 22,698. So the official final CANNOT be all-party ballots. The Call's own projection "exceeded 30,000" corroborates. FLAG for operator: determine what the master's 22,698 counts (likely republican primary only); otherwise the denominator is inconsistent in kind with the Call's returns.
- Verdict: night count (partial, counted, E+1 T03:00) = 22,117 republican-primary ballots tabulated, one precinct (92nd of 39th) missing; democratic factions 4,941+3,589 printed same table. Class: contest/party sums = floors.
- Provenance:
  - TOC: https://cdnc.ucr.edu/?a=d&d=SFC19080812
  - Table permalink: https://cdnc.ucr.edu/?a=d&d=SFC19080812.2.14.2 ; OCR: cdnc_fetch.js SFC19080812 SFC19080812.2.14.2
  - Lead: cdnc_fetch.js SFC19080812 SFC19080812.2.2 ; searches txq=vote+cast, txq=heaviest (dafdq=12&dafmq=08&dafyq=1908, puq=SFC)
  - Screenshot: scratchpad/imgs/cdnc_19080812_p2_table.png (whole table + footnote legible)
  - Mirrors: mirror/cdnc/SFC19080812/section_SFC19080812.2.14.2.txt, section_SFC19080812.2.2.txt, section_SFC19080812.2.14.1.txt, search_vote_cast.txt, search_heaviest.txt, toc.json

### 5: 1909-08-17 municipal primary (final 38,317) - FOUND midnight actual-count partials (59/149 precincts); republican mayor contest floor 5,452
Issue SFC19090818 (https://cdnc.ucr.edu/?a=d&d=SFC19090818), 284 sections. First direct-primary municipal election.
- p2 SFC19090818.2.17.3 "Partial Totals In Republican Race for Office", verbatim: "returns from 59 out of 149 precincts, available at midnight, showed the following totals in the principal republican contests: MAYOR R. H. Countryman 916; William Crocker 2,376; Byron Mauzy 2,160. AUDITOR R. W. Dennis 2,020; H. G. Mathewson 2,138. TAX COLLECTOR David Bush 3,550; John W. Rogers 1,343. CITY ATTORNEY Long 3,666; Benjamin L. McKinley 1,312. SHERIFF [E.J.] Callan 1,035; John J. Dean 1,078; Fred Eggers 1,677."
- p1 SFC19090818.2.9 "PARTIAL COUNT GIVES LINE ON FINAL RESULTS / Figures Tabulated by the Press of Returns From Half the Precincts / Incomplete Record of Votes": fuller candidate list, "These are complete, and partial returns from about half of the 149 precincts gathered by reporters of the press bureau": Mayor 916/2,376/2,160; DA Coghlan 854, Fickert 3,125, Heney 1,028; Auditor 2,020/2,138; Treasurer McDougald 4,925; Tax Coll 3,550/1,343; Recorder Boggs 2,048, Halpin 887, Stern 1,503; City Atty 3,666/1,312; County Clerk Greif 4,837; Sheriff Adams 455, Callan 1,035, Dean 1,078, Eggers 1,677, McComb 175, Noon 331, Simon 479; plus supervisor/police-judge candidate partials.
- p1 SFC19090818.2.2 lead, verbatim: "At midnight partial and complete returns gathered by the newspaper election bureau from 53 out of 149 primary precincts indicated the election of Crocker as the republican candidate for mayor..." "Inasmuch as these returns covered only 5,400 out of an estimated total of 25,000 republican votes, and as they showed an actual lead of only 216 votes for Crocker..." "The incomplete returns on the actual count at midnight, which comprised only 5,500 republican votes, showed a material change in favor of Mauzy, who out of 4,536 had a total of 2,160, or only 216 votes behind Crocker." "Coghlan, who had announced his withdrawal from the race, received 854 out of the first 5,000 votes counted for district [attorney]." (Precinct-count discrepancy in the paper itself: 53 in the lead vs 59 in the box; record both.)
- ARITHMETIC CHECKS: mayor contest sum 916+2,376+2,160 = 5,452; Crocker+Mauzy = 4,536 matches the lead's "out of 4,536"; Crocker-Mauzy = 216 matches "216 votes behind"; DA sum 3,125+1,028+854 = 5,007 matches "first 5,000 votes counted". Internally locked. (The lead's OCR shows "6,125" Fickert / "3,028" Heney once; the DA sum and the 2.9/2.17.3 lists pin 3,125 / 1,028.)
- Cast estimate (NOT a count): p6 editorial SFC19090818.2.69.4: "It is estimated by that most competent of authorities, the registrar, that not less than 40,000 votes were cast. While the total registration was more than 84,000..." [estimate exceeds final 38,317; excluded per gate. Registration per 2.2: 84,671.]
- Verdict: night count = midnight partial, counted ballots, contest sums = FLOORS: republican mayor 5,452 (14.2% of 38,317 final); republican-ballot count in hand at midnight ~5,400-5,500 per the lead. No citywide counted total printed. Gate: all figures well under the 38,317 final. PASS as floors.
- Stamp: E+1 T03:00; the box itself says "available at midnight" (E+1 T00:00).
- Provenance:
  - TOC: https://cdnc.ucr.edu/?a=d&d=SFC19090818
  - Permalinks: https://cdnc.ucr.edu/?a=d&d=SFC19090818.2.17.3 , https://cdnc.ucr.edu/?a=d&d=SFC19090818.2.9 , https://cdnc.ucr.edu/?a=d&d=SFC19090818.2.2
  - Fetched via cleared-tab batch fetch (scratchpad/cdnc_batch.js), raw AJAX getSectionText responses in scratchpad/b1909aug/fetch_00*.html and b1909aug2/
  - Searches: txq=total+vote / votes+cast / registration scoped dafdq=18&dafmq=08&dafyq=1909 puq=SFC
  - Screenshots: scratchpad/imgs/cdnc_19090818_p1_partialcount.png, cdnc_19090818_p2_partialtotals.png

### 7: 1910-01-14 Spring Valley / Hetch Hetchy bond special (final 35,015) - FOUND: COMPLETE overnight count 34,939, triple arithmetic-locked
Issue SFC19100115 (https://cdnc.ucr.edu/?a=d&d=SFC19100115), 324 sections (issue front = p8 in CDNC pagination).
- Front banner SFC19100115.2.2: "Hetch Hetchy Wins by 9,583 - Spring Valley Beaten by 1,234". Summary box verbatim (OCR partly garbled, table pins digits): For Hetch Hetchy 32,876 / Against 1,607 / For Spring Valley 22,059 / Against 11,724 / necessary to carry 23,293.
- THE TABLE: p9 SFC19100115.2.18.4 "Vote Cast For and Against the Hetch Hetchy Project and the Purchase of Spring Valley", 18 assembly districts, columns Total Vote Polled | HH For | HH Against | SV For | SV Against. Printed bottom lines: "Total vote cast 34,939 / Two-thirds necessary to carry 23,293 / Hetch Hetchy carried by 9,583 / Spring Valley lost by 1,234."
- MY IMAGE READ of every district row (screenshot cdnc_19100115_p9_table.png): 489/386/610/1,225/2,708/3,530/3,897/2,431/1,330/3,795/2,566/5,071/2,073/2,263/562/580/645/778.
  ARITHMETIC LOCKS:
  - Total column sums to EXACTLY 34,939.
  - SV-For column sums to EXACTLY 22,059.
  - 2/3 of 34,939 = 23,292.67 -> 23,293 matches printed.
  - 32,876 - 23,293 = 9,583 matches "carried by".
  - 23,293 - 22,059 = 1,234 matches "lost by".
  - (HH-For column sums 32,861 vs printed 32,876, one district cell needs operator eyes; does not affect the total-vote lock.)
- Gate: 34,939 <= final 35,015 (99.8%). PASS. Single-ballot two-proposition special counted to completion overnight (era pattern).
- Night clocking: reactions to the final result quoted "last night" in the same morning-after issue: "'I think that the result complicates the situation,' said former City Engineer C. E. Grunsky last night." and "'We should now prepare to go forward with this project,' said Manson last night. 'The people have spoken.'" Also Percy Long piece on the same page reacting to "the close margin of 1,234 votes in nearly 35,000."
- Stamp: E+1 T03:00 (complete count, effectively night-final).
- Provenance:
  - TOC: https://cdnc.ucr.edu/?a=d&d=SFC19100115
  - Table permalink: https://cdnc.ucr.edu/?a=d&d=SFC19100115.2.18.4 ; banner article https://cdnc.ucr.edu/?a=d&d=SFC19100115.2.2
  - Fetched via cleared-tab batch (scratchpad/b1910jan/fetch_00*.html, AJAX getSectionText URLs in file headers)
  - Screenshot: scratchpad/imgs/cdnc_19100115_p9_table.png (full table + totals legible)

### 8: 1910-08-16 state primary (final 47,532) - FOUND midnight partial: governor contest 9,236-9,536 counted from 100 scattering precincts (floor)
Issue SFC19100817 (https://cdnc.ucr.edu/?a=d&d=SFC19100817), 209 sections. First statewide direct primary (Johnson vs Curry etc.).
- p1 SFC19100817.2.3.1 "CURRY CARRIES CITY BY 4,500 OVER JOHNSON". Verbatim (per page image, screenshot cdnc_19100817_p1_curry.png):
  "ON THE face of incomplete returns at midnight from scattering precincts throughout the city, Charles F. Curry has carried San Francisco over Hiram W. Johnson for governor by an approximate plurality of 4,500 votes. Estimating a total of 40,000 republican votes cast and basing calculations on the comparative ratio shown in the early scattering returns, Curry's total in this city is about 18,000 votes, Johnson's is about 13,500 and Anderson's is about 5,500." [projection class, NOT counts]
  "The vote for governor in San Francisco on partial returns received up until midnight from 100 scattering precincts gives Curry 4,425, Johnson 3,094, Anderson 1,875 [image; OCR variant 1,575 - OPERATOR HAND-READ NEEDED], Ellery 85, and Stanton 57." [ACTUAL COUNTED PARTIAL, midnight-clocked]
  "Indications are that the total vote is the greatest ever polled at any primary election in this city."
  Attorney general midnight returns: "McGowan 2,750 ... Webb 2,509"; equalization "Rolkin 1,543 ... Scott 1,197".
- Contest sum (republican governor, floor): 4,425 + 3,094 + 1,875 + 85 + 57 = 9,536 (or 9,236 if Anderson 1,575). Counted ballots at midnight, 100 precincts, republican ballot only. Gate: well under final 47,532 (about 20%). PASS as floor, labeled contest sum.
- p1 SFC19100817.2.3.1.1 "Leaders in Local Republican Contest": "Leaders in the local republican contest as shown by partial returns at midnight" (names only, no figures).
- No citywide counted total printed on E+1; the 40,000-republican figure is an estimate ("Estimating a total of..."), and the statewide story (2.3) headlines "Direct Primary Brings Out Record Vote in the State" without an SF counted total.
- Stamp: E+1 T03:00; partial clocked "up until midnight" (E+1 T00:00).
- Provenance:
  - TOC: https://cdnc.ucr.edu/?a=d&d=SFC19100817
  - Permalink: https://cdnc.ucr.edu/?a=d&d=SFC19100817.2.3.1 ; AJAX fetches in scratchpad/b1910aug/fetch_00*.html
  - Screenshot: scratchpad/imgs/cdnc_19100817_p1_curry.png (partial-returns paragraph legible mid-column)

### 4: 1909-06-22 bond special (final 24,058) - UPGRADED: hand-summed district-table floor 23,073 ballots expressed on Prop 1 (pending operator digit check); printed totals row BLANK
Prior wave (agents/cdnc_1908_1909.md sec. 3) found: p1 SFC19090623.2.16 verbatim "The whole vote cast approximated 22,000 or a little more than one-half that cast at the special election called for the ratification of the Hetch Hetchy municipal water project" (approximation class); p2 district tables printed with Totals/Majority/Necessary rows BLANK; exact total 24,028 derivable only at day+3.
MY ADDITION: read the existing screenshot mirror/cdnc/SFC19090623/shot_tables_2.22.png ("How Two Bond Issues Fared at City Polls": VOTE BY DISTRICT ON CIVIC CENTER / BALLOTING UPON DETENTION HOME; per-district Total|For|Against; 39th district's Total cell not printed; citywide totals row blank = count/composition incomplete at press time).
- My cell reads, Civic Center (No. 1), For column (28th-45th): 198,124,197,476,1023,1096,1520,823,475,1640,1017,1821,782,782,198,171,203,253 -> SUM 12,799.
- Against column: 134,24,197,351,848,1058,925,673,249,1104,843,1482,815,841,103,167,173,287 -> SUM 10,274.
- FLOOR: 12,799 + 10,274 = 23,073 ballots expressed on Prop 1 across all 18 districts as printed E+1 morning. Gate: 23,073 <= 24,058 (95.9%). PASS as floor. Consistency: Civic Center LOST (12,799 far below two-thirds ~16,000) matches the printed "RESULT OF THE BOND ELECTION" box (all lost except Polytechnic).
- CAUTION / operator check: my Total-column sum for the 17 printed districts (20,914) plus the 39th's For+Against (3,303) = 24,217, slightly OVER the official 24,058 => at least one of my cell reads is off by a digit (half-resolution screenshot). The 23,073 floor claim should be hand-verified cell by cell from mirror/cdnc/SFC19090623/shot_tables_2.22.png (or a fresh zoom) before ingestion; the For-column and Against-column reads are listed above for checking.
- Verdict: night count = counted district partials printed E+1 (T03:00) with blank citywide totals; defensible floor 23,073 (pending digit verification); prose approximation "approximated 22,000" stands as the paper's own night characterization.
- Provenance: TOC https://cdnc.ucr.edu/?a=d&d=SFC19090623 ; tables permalink https://cdnc.ucr.edu/?a=d&d=SFC19090623.2.22 (sections .2.22.1/.2.22.2); screenshot mirror/cdnc/SFC19090623/shot_tables_2.22.png; prior-wave mirrors section_SFC19090623.2.16.1.txt etc.

## OPERATOR HAND-READ QUEUE (paths + claimed values + fail criteria)
1. cdnc_19070814_p2_table.png (scratchpad/imgs/): totals line should read "Total republican vote, 12,019; total democratic vote, 3,293; total union labor vote, 5,310; total socialist vote, 179. Total vote, 20,801. *Incomplete." FAIL if any digit differs (sum must equal the printed total).
2. cdnc_19080812_p2_table.png: totals row "173 | 10,371 | 11,746 | 4,941 | 3,589" and footnote "One precinct missing"; also spot-check McNab/Bell district cells (my column sums disagree with printed totals by 195/181).
3. mirror/cdnc/SFC19090623/shot_tables_2.22.png: verify my Civic Center For/Against cell reads (sec. 4 above); my Total-column cross-check overshoots the official final by 159, so at least one cell is misread. FAIL for the 23,073 floor if For+Against resums above 24,058.
4. cdnc_19100115_p9_table.png: verify HH-For column (my sum 32,861 vs printed 32,876; one district cell off). Total column and SV-For column both lock exactly; no fail risk for the 34,939 claim.
5. cdnc_19100817_p1_curry.png: Anderson's midnight figure, 1,575 vs 1,875 (mid-column paragraph "The vote for governor..."). Ellery 85 vs 88.

## METHOD NOTE
All access per RUNBOOK/cdnc recipe: raw-CDP tabs on the Chrome at :9222 (scripts/archive-recovery/cdnc_fetch.js), own tabs created and closed. Mid-run adopted the coordinator's cleared-tab fetch() optimization (scratchpad/cdnc_batch.js): navigate once to clear Cloudflare without Runtime, then Runtime.evaluate same-origin fetch() for AJAX getSectionText and search URLs; page renders only for verification screenshots. OCR mirrors land in <worktree>/mirror/cdnc/<ISSUE>/ (gitignored, same as prior waves).

### 6: 1909-11-02 general municipal (final 65,065) - DOCUMENTED DEAD END for a numeric night count; qualitative midnight state only (confirms prior wave)
Issue SFC19091103 (https://cdnc.ucr.edu/?a=d&d=SFC19091103), 262 sections, TOC mirrored at mirror/cdnc/SFC19091103/toc.json.
- p1 lead (SFC19091103.2.12, "UNION LABOR LEADER GETS MAYOR'S CHAIR BY LARGE PLURALITY", by George A. Van Smith): key verbatim quotes:
  - "On the face of the incomplete returns available at midnight, McCarthy won by an indicated plurality of 10,000 over Leland, who in turn had a substantial lead over Crocker, republican."
  - "The same incomplete returns indicated that Fickert's majority over Heney might reach a total of from 12,000 to 15,000."
  - "With the single exception of the memorable fight of 1905 all records for municipal elections were broken yesterday... with a total vote of approximately 67,000." [NOTE: turnout ESTIMATE of votes cast, NOT a count; exceeds final 65,065 so unusable as night count]
  - "The reports returned to Registrar Zemansky early in the afternoon showed that 53,000 electors had registered their choices at 1:30 o'clock." [poll-list progress, votes CAST not counted]
  - "McCarthy... figured his plurality at something more than 10,000, upon the face of the incomplete returns available at [9]:30 o'clock"
- No numeric counted-ballots table found in OCR of p1/p2 sections (page_1.txt, page_2.txt mirrored). Searches within issue: "totals" (2 hits, bowling + bulletins article), "McCarthy Leland Crocker" (2 hits, both narrative), "precincts out of" (1 hit = 2.12), "precincts give" (0), "returns from" (9 hits, none tabular). TOC swept for vote/return/precinct/count/tabulation titles across all 16 pages: no returns-table section exists in this issue.
- p4 SFC19091103.2.37 "BULLETINS FLASH RESULTS TO CROWD" confirms the Call compiled precinct returns by phone all night and bulletined them, but the ISSUE prints no compiled numeric totals: "A corps of men was stationed at the registrar's office, others were gathering returns direct from the precinct booths, all sending them into The Call by telephone where experts compiled the totals and threw them on the big screen."
- VERDICT: dead end for a numeric night count, documented. Night state is qualitative: "On the face of the incomplete returns available at midnight, McCarthy won by an indicated plurality of 10,000 over Leland" (2.12); winners conceded "before 10 o'clock". The 67,000 figure is a turnout projection (exceeds final 65,065, gate fail); 53,000 is 1:30 pm ballots CAST (poll-list class). First numeric counted totals appear day+1 8pm, complete unofficial 64,931 (SFC19091104.2.18, prior wave). CONCURS with prior wave verdict.
- Provenance of my re-verification: searches https://cdnc.ucr.edu/?a=q&hs=1&r=1&results=1&txq=totals&txf=txIN&ssnip=txt&puq=SFC&dafdq=03&dafmq=11&dafyq=1909&datdq=03&datmq=11&datyq=1909&e=-------en--20--1--txt-txIN-------- (and variants txq= McCarthy+Leland+Crocker / precincts+out+of / precincts+give / returns+from); full-page OCR mirrors mirror/cdnc/SFC19091103/page_1.txt, page_2.txt; section mirrors listed above.

