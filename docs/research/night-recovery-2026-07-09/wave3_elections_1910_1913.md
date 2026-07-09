# Wave 3: SF election-night counts 1910-1913 (CDNC / SF Call)

Agent salvage file. Written as-you-go. Repo untouched.

Method: scripts/archive-recovery/cdnc_fetch.js via real Chrome CDP (localhost:9222).
Issue URL pattern: https://cdnc.ucr.edu/cgi-bin/cdnc?a=d&d=SFC<YYYYMMDD> (equivalently https://cdnc.ucr.edu/?a=d&d=SFC<YYYYMMDD>).
Night-count definition: ballots COUNTED by ~E+1 06:00, printed in day-after morning edition. Contest sums w/ partial precincts = floors. Poll lists are NOT counts.

Targets (official final total votes = ceiling): ALL 8 DONE, see FINAL VERDICT TABLE at bottom.
1. 1910-11-15 charter amendments special — final 45,889 — DONE (tiny partial: 35/352 pcts)
2. 1911-09-26 municipal primary — final 79,019 — DONE (186 partial pcts)
3. 1911-10-10 constitutional amendments special (suffrage) — final 59,266 — DONE (220 pcts, 31,032)
4. 1912-05-14 presidential primary — final 62,407 — DONE (356/356 pcts, ~60,700)
5. 1912-09-03 state primary — final 65,948 — DONE (454/463 pcts, floor 41,898 flagged)
6. 1912-12-20 general-utilities bond special — final 47,484 — DONE (complete count 47,238)
7. 1913-09-30 municipal primary — final 65,905 — DONE (documented incomplete-overnight dead end)
8. 1913-11-11 general municipal — final 72,551 — DONE (72,574 first count gate-flagged; contest sums pass)

---

## 1. 1910-11-15 charter-amendments special (final 45,889)

STATUS: DONE. Night COUNT is tiny: only 35-61 precincts of 352 complete by midnight; hard counted numbers printed only for the first 35 precincts on Amendments 7/8. The ~30,000 figure is an explicit PROJECTION ("will approximate"), not a count.

Source issue: SF Call, Wed 1910-11-16. Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19101116

Finds:
- p1, "$5,000,000 PANAMA-PACIFIC FAIR BOND ISSUE AUTHORIZED" (section SFC19101116.2.2): "COMPLETE returns received up to midnight indicate ... The results given below are based on complete returns from 61 scattering precincts out of a total of 3[3/5]2 in the entire city. The total vote indicated will approximate 3[0],000." (OCR garbles: "3«V>OO"; companion articles pin the projection at 30,000.) Also: "Total vote in 35 districts out of 352".
- p2, "BIG EXPOSITION IS INDORSED BY VOTE OF 20 TO 1" (SFC19101116.2.21): "On the showing made in the returns received up to midnight It is estimated that the total vote on the exposition bond issue will approximate 30,000, of which not more than 1,800 votes were cast in opposition"; "Out of only about one-sixth of the total number of precincts in the city, which were all that had been reported in full at midnight"; sample precinct 21st of 32nd AD: 54-0.
- p2, "CITY VOTES FOR MAJORITY NONPARTISAN RULE" (SFC19101116.2.25): HARD COUNT: "The first 35 precincts out of 352 in the city showed 1,860 for No. 7 and 465 against it. The same precincts gave 1,662 for No. 8 and 554 against it." => Amendment 7 counted floor 1,860+465 = 2,325 ballots (35 precincts, ~10% of city). Estimated full-city totals (20,500-5,100 etc.) are explicit extrapolations, not counts.

VERDICT: night count (counted ballots in print, E+1 morning) = 2,325 on Amendment 7 across 35 of 352 precincts (contest floor). Share of final 45,889 ~= 5.1% (floor). The Call's own overnight estimate of total votes cast was ~30,000, an estimate not a count. Gate OK (2,325 < 45,889).

Mirror artifacts: mirror/cdnc/SFC19101116/section_SFC19101116.2.2.txt, .2.21.txt, .2.25.txt, toc.json

---

## 2. 1911-09-26 municipal primary (final 79,019)

STATUS: DONE. Midnight state: "partial and incomplete returns available at midnight indicate a total vote of 75,000" (ESTIMATE, not count; "out of which a probable 47,000 were cast for Rolph, 25,000 for McCarthy and 3,000 for the socialist candidates"). Hard COUNTED tallies printed only from "partial returns from 186 precincts at midnight", compiled by Chief Deputy Registrar Harry Zemansky:
- Sheriff (186 precincts, midnight): "The totals at that time were: Eggers 1,714, Finn 1,657, Dolan 986" (OCR "086"; Holland vote not printed). Contest floor 4,357+.
- District attorney (186 scattered precincts): "give Fickert 1,885 votes and Hathorn 1,719" (others "light", unprinted). Floor 3,604+.
- Coroner ("Latest returns from scattering precincts"): Leland 1,338, Toner 1,075, Glover 755, Apple 551, Crowly 101 (OCR "1017.7", likely 101), O'Connell 84, Fitzgibbon 83. Sum 3,987 (full candidate list; contest floor).

Turnout tally (NOT a count): "More than 50 per cent [of] the record breaking registered vote was cast at noon. At 3 o'clock 67,000 electors had deposited their ballots."

Source: SF Call, Wed 1911-09-27, p1, "ROLPH ELECTED / Next Mayor Has About 47,000 Votes to 25,000 for McCarthy" (section SFC19110927.2.2). Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19110927. No returns table elsewhere in issue (TOC swept, mirror/cdnc/SFC19110927/toc.json).

VERDICT: night COUNT = coroner-contest sum 3,987 ballots across 186 partial precincts (floor); the 75,000/47,000/25,000 figures are the Call's overnight ESTIMATES from those partials, not counts. Share of final 79,019: 3,987 ~= 5.0% (floor). Gate OK.

Mirror artifacts: mirror/cdnc/SFC19110927/section_SFC19110927.2.2.txt, toc.json

---

## 3. 1911-10-10 constitutional-amendments special, woman suffrage (final 59,266)

STATUS: DONE. STRONG overnight partial. SF Call, Wed 1911-10-11, p1, "VOTE SHOWS JUDGMENT AT POLLS" (section SFC19111011.2.9). Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19111011

Verbatim finds (all explicitly clocked overnight):
- "Out of 180 precincts counted by 11 o'clock last night, the recall received 17,173 votes, while 4,932 were registered against it." Amendment 16 (railroad commission): "Out of 180 precincts, it showed a vote of 12,516 to 5,383."
- BEST COUNT, 220 precincts: "In 220 precincts the results showed 19,869 against suffrage and 11,163 in favor of it. At this ratio it was estimated at the registrar's office that suffrage would be defeated in San Francisco by 15,000 votes." => Amendment 4 (woman suffrage) counted sum = 11,163 + 19,869 = 31,032 ballots (contest floor, 220 precincts).
- Same 220 precincts: initiative & referendum 20,134 to 6,049 (sum 26,183); recall 21,613 to 6,242 (sum 27,855).
- Total-vote ESTIMATE (not a count): "The vote in San Francisco was heavier than had been anticipated. It is figured that the total will approximate 50,000."
- Headline crossbar: "50,000 MEN GO TO POLLS TO MAKE LAWS" (estimate).
- Also in-article: SF city per-amendment tally table (garbled OCR) and a statewide by-county suffrage table; SF row of the county table shows an earlier tally 6,816 for / 12,724 against.

VERDICT: night count = 31,032 ballots counted on the suffrage amendment across 220 precincts by press time (E+1 morning edition; recall/init tallies clocked 11 p.m.). Floor label: contest sum, 220 of ~352+ precincts. Share of final 59,266 ~= 52.4% (floor). Gate OK (31,032 < 59,266). The Call's own projected total was ~50,000.

Mirror artifacts: mirror/cdnc/SFC19111011/section_SFC19111011.2.9.txt, toc.json

---

## 4. 1912-05-14 presidential primary (final 62,407)

STATUS: DONE. EXCELLENT: the Call printed a FULL-CITY overnight count, all 356 precincts. SF Call, Wed 1912-05-15. Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19120515

Finds:
- p2, "LOCAL RESULTS ANALYZED" (section SFC19120515.2.18): "The 356 precincts of San Francisco gives Roosevelt 19,843 Taft 16,536 La Follette 8,507 Wilson 3,963 Clark [6,777 or 7,777; OCR 'C lark 6.77T']. 354 complete precincts out of 356 in San Francisco give: Roosevelt delegates 21,650 Taft delegates 17,851 La Follette delegates 10,004 Wilson delegates 3,345 Clark delegates 7,850." Also: "The total 356 precincts gave Roosevelt a lead of 3,307" (19,843-16,536=3,307 checks) and "Champ Clark outstripped Woodrow Wilson by 3,814" (implies Clark 7,777; but Wilson pref 3,963 vs delegate 3,345 contradicts the article's own claim that delegate votes always exceeded preference votes, so digits need page-image arbitration: FLAG for manual operator, image SFC19120515 p2, article "LOCAL RESULTS ANALYZED").
- p1 lead (SFC19120515.2.2): "TAFT DEFEATED IN SAN FRANCISCO BY ABOUT 3,300"; "The returns available at midnight indicate that not more than half of the registered vote of the state was polled."

Arithmetic (my sums, not printed):
- Presidential preference, 356/356 precincts: 19,843+16,536+8,507+3,963+Clark(6,777..7,777) = 55,626..56,626 counted ballots expressing a preference (contest floor: some voters skipped the preference line, per article).
- Delegate slates, 354/356 precincts: 21,650+17,851+10,004+3,345+7,850 = 60,700 (best night-count proxy; article says delegate lines outdrew the preference line).

VERDICT: night count = 60,700 ballots (delegate-contest sum, 354 of 356 precincts, printed E+1 morning) = 97.3% of final 62,407. Preference-line sum 55,626..56,626 (89.1-90.7%). Gate OK (both < 62,407). Digit ambiguities (Clark 6,777/7,777; Wilson 3,963 vs 2,963) need human page read.

Mirror artifacts: mirror/cdnc/SFC19120515/section_SFC19120515.2.18.txt, section_SFC19120515.2.2.txt, toc.json

---

## 5. 1912-09-03 state primary (final 65,948)

STATUS: DONE (count basis firm, best absolute number needs page-image arbitration). SF Call, Wed 1912-09-04. Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19120904

Finds:
- p1, "THIS CITY'S VOTE IN DETAIL" (section SFC19120904.2.8): opens verbatim "Returns from 454 out of 463 precincts:" then a full table (congressman by district, state senators, assembly, judges). OCR of the table is heavily scrambled (columns interleaved).
- Overnight clock: p1 "THIRD PARTY MAKES WEAK FIGHT FOR CONGRESS" (SFC19120904.2.11): "the partial and incomplete returns available at 2 o'clock this morning".
- Judges (citywide, multi-seat, so per-candidate <= ballots): OCR gives "Thomas F. Graham 41,898", "James V. Coffey 83,525" (impossible vs final 65,948; almost surely 33,525), "William P. Lawlor 80,084" (likely 30,084), "Edward P. Shortall 85,268" (likely 35,268), Dean 38,454, Dillon (S) 8,994, Sawyer 4,458, Sigourney (S) 8,693, Silverman (S) 3,727.
- Also 463 polling places confirmed in 2.11 ("Out of the 463 polling places yesterday there were 52 tents").

VERDICT: night count basis = 454 of 463 precincts reported in the E+1 morning edition (returns clocked to 2 a.m.). Best single defensible ballot floor: top judicial candidate Thomas F. Graham 41,898 votes (each ballot votes a judge candidate at most once) => >= 41,898 ballots counted overnight, 63.5% of final 65,948 (floor). Several judge figures have a leading-digit OCR garble (8 vs 3); Graham's 41,898 is plausible but FLAG for manual operator: hand-read the p1 table image of SFC19120904 ("THIS CITY'S VOTE IN DETAIL") to confirm 41,898 and recover clean judge totals (a sum/4-seats estimate could approximate total ballots). Gate OK (41,898 < 65,948; the 8x,xxx OCR readings are flagged as garbles, not claims).

Mirror artifacts: mirror/cdnc/SFC19120904/section_SFC19120904.2.8.txt, .2.11.txt, .2.7.txt, .2.2.txt, toc.json

---

## 6. 1912-12-20 general-utilities bond special (final 47,484)

STATUS: DONE. BEST RESULT OF THE SET: the Call printed a COMPLETE unofficial overnight count with a total-ballots figure. SF Call, Sat 1912-12-21, p1. Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19121221

Finds:
- p1 box, "Story of Voting at a Glance / Only 47,238 Ballots Cast" (section SFC19121221.2.3), verbatim: "1 $700,000 for acquisition Sutro properties 28,345 YES 17,489 NO; 2 $1,700,000 for completion [hospital] and jail 35,013-11,142; 3 $800,000 for aquatic park 23,228-22,563; 4 $200,000 [sic; article says park lands] Twin Peaks park lands 21,049-23,299; 5 $750,000 for police and fire alarm system 30,765-15,252. Whole vote cast 47,238." (OCR "X\ nolo rote east 47,238").
- p1 lead, "TWO ONLY OF BOND MEASURES ARE RATIFIED" (SFC19121221.2.2): "Out of a total registration of approximately 128,000, only 47,238 votes were cast." Subhead: "Complete Unofficial Returns Show That All the Park Bond Propositions Lost", followed by per-assembly-district tables for all five propositions (table totals: Sutro 28,616-17,405; Jail/Hospital 35,1?5-11,297; Aquatic 23,201-22,665; Twin Peaks 21,980-23,198; Police/Fire alarm 30,594-15,225; minor OCR noise). Slight box-vs-table differences suggest the glance box froze slightly earlier than the district tables; both are overnight, printed E+1 morning.
- Consistency: every per-measure sum <= 47,238 (e.g. #2: 35,013+11,142 = 46,155).

VERDICT: night count = 47,238 total ballots, printed as "complete unofficial returns" in the E+1 morning edition = 99.5% of official final 47,484. Gate OK (47,238 < 47,484). This is an explicit whole-ballots figure, not a contest floor.

Mirror artifacts: mirror/cdnc/SFC19121221/section_SFC19121221.2.3.txt, .2.2.txt, toc.json

---

## 7. 1913-09-30 municipal primary (final 65,905)

STATUS: DONE, with an explicit overnight-count clock. NOTE: by Oct 1913 the Call was an EVENING paper (issue carries the "Evening Calls" column), so the E+1 issue reports the morning-after state, and it clocks the overnight count explicitly.

Source issue: SF Call, Wed 1913-10-01. Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19131001

Finds (all from the combined p1 story, section SFC19131001.2.3, subheads "6 CITY CANDIDATES ARE ELECTED" / "SHORTALL IS SAFE IN OFFICE" / "Election Officers Work Until 4 A. M. and Resume Check at 8 O'Clock"):
- THE CLOCK (documented overnight halt): "The length of the ballot has made the counting slow. Forty deputies worked on the returns until 4 o'clock this morning and returned again shortly after 8 o'clock. They are now casting totals that probably will be complete some time this afternoon."
- "With the semiofficial count progressing slowly and indications that definite figures will not be available until late this afternoon, the results of yesterday's primary election were, nevertheless, almost positively determined this morning."
- Total-ballots figure: "The total vote amounted to 65,778 and the majority necessary for election to any office at the primary was, therefore, 32,890." (65,778/2 -> 32,890 checks. This is the semiofficial ballots-cast total known the morning after; NOT proven counted by 4 a.m.)
- Tax collector, labeled complete: "Low received 26,892 votes, as against his opponent's 18,860" (p1 box SFC19131001.2.5: "J. O. Low, 26,892 (complete); Edward F. Bryant, 18,860 (complete)"). Sum 45,752.
- Police judge: "Returns, complete except for a few precincts, give Sullivan a vote of 27,896, and Caubu 18,479."
- Supervisors, the lagging count: "The latest figures on the comparative standing of the 64 candidates for supervisor, based on the returns from 233 out of a total of 673 precincts": Gallagher 11,602 leading (full 64-name list printed, OCR noisy).
- Cross-check, LA Herald 1913-10-01 (LAH19131001.2.21, "Bay City Officials Win at Primaries"): "SAN FRANCISCO, Oct. 1. Complete returns today show that all the city officials whose terms expire this year were renominated..." (no numbers; confirms completion happened E+1 DAYTIME, not overnight).

VERDICT: strict night count (by the 4 a.m. halt / 06:00 cutoff) is NOT separately quantified; the paper documents the count as INCOMPLETE overnight (supervisors at 233/673 precincts). Morning-after quantified state: tax-collector contest complete at 45,752 votes (69.4% of final 65,905, floor for that contest; completion may include 8 a.m.-to-press counting, so treat as E+1-morning ceiling on the overnight plateau, not a clean night count). Semiofficial total ballots cast 65,778 (99.8% of final) was known E+1 morning but is a cast tally, not a counted-ballots figure. Gate OK (all figures < 65,905... note 65,778 < 65,905). Dead-end quote captured (count resumed 8 a.m., totals due "late this afternoon").

Mirror artifacts: mirror/cdnc/SFC19131001/section_SFC19131001.2.5.txt, search_primary.txt (contains full 2.3 text), toc.json; mirror/cdnc/LAH19131001/search_San_Francisco_primary.txt

---

## 8. 1913-11-11 general municipal (final 72,551)

STATUS: DONE, with a GATE CAUTION: the day-after "first complete count" total EXCEEDS the certified final by 23 votes, so it may not be claimed as a night count figure; contest sums from the same table pass the gate.

Sources:
- SF Call (evening paper by then), Wed 1913-11-12, p9, "MIXED TICKET IS CHOSEN BY VOTERS IN CITY ELECTION" (section SFC19131112.2.74). Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19131112. Verbatim: "Registrar Zemansky announced this morning that the returns of yester[day]... no change will result from the first complete count, which shows: POLICE JUDGE J. J. SULLIVAN (elected) 39,322, WILLIAM P. CAUBU 31,075; TAX COLLECTOR E. F. BRYANT (elected) 37,590, J. O. LOW 32,852; SUPERVISORS (elected) FRED SUHR JR 41,232, JAMES E. POWER 39,972, JOHN O. WALSH 38,230, CON DEASY 36,443, CHARLES A. NELSON 34,886, RALPH McLERAN 33,417, EDWARD L. NOLAN 32,574, FRED L. HILMER 32,354; (defeated) PHILLIPS 32,054, BATH 32,045, MURPHY 28,992, BURNS 28,217, CAGLIERI 27,912, MAUZY 27,883, CONNOLLY 26,033, KOSHLAND 25,817. Total vote 72,574."
- AP wire, datelined SAN FRANCISCO Nov. 11 (election night), carried by CDNC morning papers of Nov 12: Sacramento Daily Union (SDU19131112.2.132, "Result Is Mixed In Bay Election"), Stockton Independent (SDI19131112.2.9), San Jose Mercury-News (SJMN19131112.2.43), Riverside Daily Press, Chico Record, Humboldt Times. All name the full winner slate (8 supervisors, police judge, tax collector) but print NO vote figures. All-papers search URL: https://cdnc.ucr.edu/?a=q&hs=1&r=1&results=1&txq=San+Francisco+supervisors&txf=txIN&ssnip=txt&dafdq=12&dafmq=11&dafyq=1913&datdq=12&datmq=11&datyq=1913&e=-------en--20--1--txt-txIN--------

Analysis:
- The AP story datelined election night already declares every winner, so the count was substantively finished on election night; but the only quantified record is the registrar's "first complete count" announced E+1 MORNING (evening-paper "this morning", after the 06:00 cutoff), total 72,574.
- GATE: 72,574 > official final 72,551 (unofficial overnight/first count ran 23 high; canvass corrected down). Per mission rule this figure is recorded as an unofficial-complete-count artifact, NOT claimed as the night count.
- Contest sums from the same table (pass gate): police judge 39,322+31,075 = 70,397; tax collector 37,590+32,852 = 70,442. Both < 72,551 (97.0-97.1%), usable as contest-sum floors of the first complete count.
- No overnight-clocked (pre-06:00) partial with numbers found in the Call issue ("midnight" hits SFC19131112.2.148/.2.154 are non-election) or in any CDNC morning paper's AP story: documented dead end for a strictly clocked overnight partial.

VERDICT: night count strictly clocked = NOT PRINTED; best defensible figures: first-complete-count contest sums 70,397 (police judge) / 70,442 (tax collector), announced E+1 morning; headline total 72,574 EXCEEDS final 72,551 and is gate-flagged. Election-night AP wire proves winners were known overnight.

Mirror artifacts: mirror/cdnc/SFC19131112/section_SFC19131112.2.74.txt, toc.json; mirror/cdnc/SDU19131112/section_SDU19131112.2.132.txt; mirror/cdnc/SDI19131112/section_SDI19131112.2.9.txt; mirror/cdnc/SJMN19131112/section_SJMN19131112.2.43.txt

---

## Screenshots (scratchpad imgs/, viewer render of the cited page, 1600x2200)

All taken via raw-CDP background tab (no focus steal, no bringToFront), Page.captureScreenshot after the Veridian viewer rendered. Viewer URL pattern: https://cdnc.ucr.edu/?a=d&d=<pageOid>

- cdnc_19101116_p2.png (SFC19101116.1.2: nonpartisan-rule article w/ 35-precinct counts)
- cdnc_19110927_p1.png (SFC19110927.1.1: ROLPH ELECTED, 186-precinct tallies)
- cdnc_19111011_p1.png (SFC19111011.1.1: VOTE SHOWS JUDGMENT AT POLLS, 220-precinct suffrage count)
- cdnc_19120515_p2.png (SFC19120515.1.2: LOCAL RESULTS ANALYZED, 356-precinct totals; Clark digit to hand-read)
- cdnc_19120904_p1.png (SFC19120904.1.1: THIS CITY'S VOTE IN DETAIL, 454/463 precincts; judges figures to hand-read)
- cdnc_19121221_p1.png (SFC19121221.1.1: Story of Voting at a Glance, 47,238; box visible in capture)
- cdnc_19131001_p1.png (SFC19131001.1.1: THOSE ELECTED box + 6 CANDIDATES ELECTED story)
- cdnc_19131112_p9.png (SFC19131112.1.9: MIXED TICKET table, Total vote 72,574)

Note: direct pageimage endpoint (?a=is&type=pageimage) requires login; tile endpoint is Turnstile-gated. Screenshot-after-render is the working capture path. Operator speed tip (post-clearance same-origin fetch via Runtime.evaluate) validated for HTML/AJAX fetches; image endpoints still auth-gated.

---

## FINAL VERDICT TABLE

| election | official final (gate) | night count recovered | share | basis + citation (SF Call unless noted) |
|---|---|---|---|---|
| 1910-11-15 charter special | 45,889 | 2,325 (Amdt 7 sum, 35 of 352 pcts; floor) | 5.1% | "first 35 precincts... 1,860 for No. 7 and 465 against"; 61 pcts complete by midnight; projected total ~30,000 (estimate, not count). Call 1910-11-16 p1 (SFC19101116.2.2), p2 (.2.21, .2.25) |
| 1911-09-26 muni primary | 79,019 | 3,987 (coroner sum, 186 partial pcts; floor) | 5.0% | Zemansky midnight compilation: sheriff 1,714/1,657/986, DA 1,885/1,719, coroner 7-name list; "total vote of 75,000" is an estimate. Call 1911-09-27 p1 (SFC19110927.2.2) |
| 1911-10-10 suffrage special | 59,266 | 31,032 (suffrage sum, 220 pcts; floor) | 52.4% | "In 220 precincts... 19,869 against suffrage and 11,163 in favor"; recall 17,173-4,932 in 180 pcts "counted by 11 o'clock last night". Call 1911-10-11 p1 (SFC19111011.2.9) |
| 1912-05-14 pres primary | 62,407 | 60,700 (delegate-slate sum, 354/356 pcts; floor) | 97.3% | "354 complete precincts out of 356... Roosevelt delegates 21,650, Taft 17,851, La Follette 10,004, Wilson 3,345, Clark 7,850"; preference line 55,626-56,626 (Clark digit needs page read). Call 1912-05-15 p2 (SFC19120515.2.18) |
| 1912-09-03 state primary | 65,948 | >= 41,898 (top judge Graham, 454/463 pcts; floor, digit flagged) | 63.5% | "Returns from 454 out of 463 precincts"; returns clocked "2 o'clock this morning"; judges table OCR-garbled, hand-read flagged. Call 1912-09-04 p1 (SFC19120904.2.8, .2.11) |
| 1912-12-20 bond special | 47,484 | 47,238 (whole ballots, complete unofficial) | 99.5% | "Story of Voting at a Glance / Only 47,238 Ballots Cast"; "Complete Unofficial Returns" w/ 5 measure tables. Call 1912-12-21 p1 (SFC19121221.2.3, .2.2) |
| 1913-09-30 muni primary | 65,905 | NOT quantified overnight; tax-collector contest 45,752 complete E+1 morning; total cast 65,778 semiofficial | 69.4% (contest floor) | DEAD END for strict night count: "Forty deputies worked on the returns until 4 o'clock this morning and returned... shortly after 8"; supervisors only 233/673 pcts. Call (evening) 1913-10-01 p1 (SFC19131001.2.3, .2.5) |
| 1913-11-11 general muni | 72,551 | GATE-FLAGGED: "first complete count... Total vote 72,574" (E+1 morning) EXCEEDS final by 23; contest sums 70,397 (police judge) / 70,442 (tax collector) pass gate | 97.0% (contest sums) | Registrar Zemansky "announced this morning"; AP wire datelined Nov 11 names all winners (count effectively done overnight) but prints no numbers. Call 1913-11-12 p9 (SFC19131112.2.74); SDU/SDI/SJMN 1913-11-12 |

Human-verification asks (page image reads, screenshots above + viewer URLs):
1. SFC19120515 p2 "LOCAL RESULTS ANALYZED": Clark preference (6,777 vs 7,777) and Wilson preference (3,963 vs 2,963).
2. SFC19120904 p1 "THIS CITY'S VOTE IN DETAIL": judges' totals (Graham 41,898 claim; Coffey/Lawlor/Shortall leading digit 8-vs-3 garbles).
3. SFC19101116 p1: the garbled projected total "3?,000" (companion articles say 30,000).

