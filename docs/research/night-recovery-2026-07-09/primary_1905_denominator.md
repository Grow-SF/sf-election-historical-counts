# 1905-08-08 SF municipal primary: what does 28,951 count? (salvage file)

MISSION: true all-party ballots-cast total for the Aug 8, 1905 SF municipal primary; what 28,951 (FY1915-16 Municipal Reports categorized index p.331, munisanfrancisco65sanfrich leaf n350) denominates.

Known inputs:
- Registrar series (FY1915-16 vol, only printing): 28,951.
- SF Call 1905-08-09 p2 (SFC19050809.2.8.3/2.8.5): "SUMMARY OF THE VOTE ... TOTAL 38,120" = 16,071+15,429+2,575+654+2,955+170+266, header "OFFICIAL FIGURES ARE INCOMPLETE"; claimed record vote ~41,000 estimated.
- Precedent: Aug 11, 1908 registrar row used Republican-only column (22,698) vs all-party 33,331.

## Log (append as you go)

### Step 1: FY1905-06 Municipal Reports volume (archive.org sanfranciscomuni56sanfrich)
- Identified via advancedsearch title query: sanfranciscomuni56sanfrich = "San Francisco municipal reports Fiscal Year 1905-6, Ending June 30, 1906 And Fiscal Year 1906-7, Ending June 30, 1907" (published 1908, post-fire). Also excerptsfromsanf1908sanf/excerptsfromsanf1971sanf (excerpts of same).
- Full-text API (ia800705.us.archive.org, path /27/items/...) queries "28,951", "28951", "38,120", "38120", "16,071", "August 8, 1905", "August, 1905": ZERO hits. "primary"/"primary election" hits are all about the AUGUST 14, 1906 primary and the destroyed Great Register (fire narrative), plus school-teacher classifications.
- DEAD END: the FY1905-06 volume contains NO canvass or total for the Aug 8, 1905 primary. Consistent with fire destroying election records; confirms FY1915-16 categorized index is the only registrar printing.

### Step 2: SF Call 1905-08-09 p2 (mirror/cdnc/SFC19050809/page_2.txt, fetched 2026-07-09 via CDP) — DONE
- SFC19050809.2.8.3 "OFFICIAL FIGURES ARE INCOMPLETE": per-district table, 28th-45th ADs, 7 party lines each + "Total vote". Several districts have DASHES for whole party lines (36th: UL/opp-UL/Soc dashed; 38th: UL/opp-UL/Soc dashed; 39th: UL/opp lines dashed; 43rd: everything except Rep League dashed) yet still print a district Total vote (e.g. 43rd: Rep League 1,197 but Total vote 2,003). So the party-column sums undercount even the printed district totals.
- SUMMARY OF THE VOTE (verbatim OCR): "REPUBLICAN, LEAGUE ... 16,071 / RUEF REPUBLICAN 15,429 / DEMOCRATIC 2.575 / REORGANIZED DEMOCRACY 654 / UNION LABOR 2,955 / UNION LABOR (ANTI-RUEF) 170 / SOCIALISTS 266 / TOTAL 38,120".
  - COMPONENT NAMES (from surrounding articles 2.8.1/2.8.2/2.8.4/2.8.6): 16,071 = Republican League (anti-Ruef reform faction, won 93-delegate lead); 15,429 = Ruef Republicans; 2,575 = regular Democrats; 654 = Reorganized Democracy (bolting Dem faction); 2,955 = Union Labor (regular); 170 = opposition/anti-Ruef Union Labor; 266 = Socialist.
  - The two big components are BOTH Republican factions. Republican-only = 16,071+15,429 = 31,500.
- SFC19050809.2.8.5 "REPUBLICAN VOTE REMARKABLYLARGE" (verbatim OCR, garbled): "the totnl number of vnteii cant at yesterday's election nun not footed up at 2 o'clock thiM morning ... llenred at the Ilepublicnn Leiisiue headquarters last night Hint the vot* approximated 41,000, of which 31,000 accredited to the Republican column ... At the first primary elcrtinn under the Strnttoii Invr in 1898 the number polled wnn nearly 82,000 [OCR; plausibly 32,000]."
- 2.10 GANGSTERS article: "The number of votes cast ua3 the greatest ever known at any primary election here."
- INTERPRETATION so far: 38,120 = incomplete election-night sum of party columns; true total likely ~41,000 per League estimate. 28,951 matches NO night column (Rep-only night = 31,500).

### Step 3 result: THE OFFICIAL COUNT, SF Call 1905-08-15 p10 (SFC19050815.2.110) — THE KEY FIND
Chain of citations (all mirrored under mirror/cdnc/):
- SFC19050810.2.63.2 "BEGIV OFFICIAL COUNT" (p4): commissioners began official count Aug 9; "no changes ... In the Twelfth Precinct of the Thirtieth District the Republican League ticket lost five votes and the Regular Democratic ticket also lost the same number."
- SFC19050811.2.42.1 "Resumes Official Count.": districts 33-38 canvassed Aug 10, "No changes were noted"; election officers of 6 precincts cited for not signing returns.
- SFC19050812.2.101 "No Change In Votes.": "The official canvass ... was completed last night. No changes in the count of the semiofficial results were found. The official figures will be declared at a meeting of the board to be held on Monday afternoon." (= Mon Aug 14)
- SFC19050815.2.110 "BOARD MAKES OFFICIAL COUNT / Commissioners Announce Correct Number of Ballots Cast at the Primary": "The Election Commission met yesterday and declared the official result of the returns of the last primary election. The vote cast follows:" then an 18-district table, columns Republican / Democratic / Socialist / Union Labor / Scattering / Total.
- TABLE READ BY EYE from stitched tiles (scratchpad imgs/cdnc_19050815_p10_2-110_b4.png; tile pipeline cdnc_stitch.js + stitch.py):
  Total row: Republican 31,728 | Democratic 3,732 | Socialist 319 | Union Labor 4,500 | Scattering 838 | TOTAL 41,117.
  Arithmetic: 31,728+3,732+319+4,500+838 = 41,117 EXACT.
  Per-district (by eye): 28th 1,350/116/34/311/38/1,849; 29th 1,280/142/60/439/69/1,990; 30th 1,205/391/28/434/71/2,129; 31st 1,284/200/22/395/110/2,011; 32nd 1,917/277/14/278/50/2,536; 33rd 1,042/200/15/342/14/1,613; 34th 1,810/189/11/299/39/2,348; 35th 1,928/124/15/182/21/2,270; 36th 1,824/165/17/282/42/2,330; 37th 1,971/509/15/212/62/2,769; 38th 2,147/204/14/285/32/2,682; 39th 2,469/80/11/149/62/2,771; 40th 1,976/260/12/62/14/2,324; 41st 1,978/170/1/135/16/2,300; 42nd 2,137/164/17/205/56/2,579; 43rd 2,008/190/11/153/37/2,399; 44th 1,911/167/14/165/74/2,331; 45th 1,491/184/8/172/31/1,886.
  (Article then says "The segregated Republican vote follows:" but NO segregated table is printed in the section; text jumps to voting-machine business. The League/Ruef split thus only exists in the semi-official printings: night 16,071/15,429; next-day 16,200/15,476.)
- The 1905 official Republican column (both factions) = 31,728. NOT 28,951. So the 1908-style "Republican-only" hypothesis FAILS for 1905.

### Step 4: what is 28,951 then?
- Re-verified the registrar index page BY EYE (scratchpad imgs/muni65_n350.jpg, https://archive.org/download/munisanfrancisco65sanfrich/page/n350): "MUNICIPAL ELECTIONS. PRIMARY. ... 1905—Aug. 8 ... Registration 87,062, Vote Polled 28,951, Number Precincts 198." Printed exactly as ingested; not a transcription error on our side. (Same page GENERAL: 1905—Nov. 7 ... 97,670 / 71,033 / 198.)
- 28,951 matches NOTHING in the official canvass: not the total (41,117), not Republican (31,728), not any column, not League (16.2k) or Ruef (15.5k), not obvious combinations (Rep+Dem 35,460; total-scattering 40,279; non-Rep sum 9,389).
- CDNC search SFC 1905-08-09..1905-12-31 for "28,951": no hits. For "41,117": no hits (the Aug 15 table digits are OCR-garbled in CDNC's index, so absence of hits means nothing).
- Note the categorized-index primary series neighbors: 1899 32,521 / 1901 22,939 / 1903 26,039 / 1905 28,951 / 1907 22,851 / 1909 38,317. The bogus 28,951 fits this series' scale suspiciously well, while the true 41,117 (a record, per the Call) would stick out. Whoever backfilled the burned 1905 row appears to have used some incomplete or wrong-scope source.

### Step 5: arithmetic soundness of the official table (my sums, from the by-eye district reads)
Every column of the SFC19050815.2.110 table foots EXACTLY:
- Republican: 1,350+1,280+1,205+1,284+1,917+1,042+1,810+1,928+1,824+1,971+2,147+2,469+1,976+1,978+2,137+2,008+1,911+1,491 = 31,728
- Democratic: ... = 3,732 exact; Socialist: ... = 319 exact; Union Labor: ... = 4,500 exact; Scattering: ... = 838 exact
- Total: row totals sum to 41,117 exact; each district row also foots (e.g. 28th: 1,350+116+34+311+38 = 1,849).
Official vs semi-official (Aug 10): Rep 31,728 vs 31,676; Dem(all) 3,732 vs 3,497; UL(all) 4,500 vs 4,269; Soc 319 vs 320; Scattering 838 vs (none); Total 41,117 vs 40,052.

### Step 6: independent same-week corroboration (LA Herald, AP wire)
- LAH19050810.2.22 "SAN FRANCISCO REFORM WINS CLEAN-CUT VICTORY" (By Associated Press, dateline SF Aug 9): "The total vote was 83,968 [OCR; = 38,968], divided as follows: Republican league, 18,103 [likely 16,103]; regular Republicans, 15,505; Democrats, 2790; opposition Democrats, 645; Union labor, 3750; opposition Union labor, 184." Sum with 16,103 = 38,977. Independent ~39k semi-official; consistent with official 41,117, wildly inconsistent with 28,951.
- Also: "the primary election held yesterday to choose delegates to the various municipal nominating conventions was the most exciting event of the kind ever known in this city."

### Step 7: 1903 primary cross-check (series-intent test)
- mirror/cdnc/SFC19030812/page_4.txt (SF Call 1903-08-12 p4): "The total vote at the primary as forecasted by The Call exceeded 2?,000. The oflicial figures at the Registrar's office place the number at :6,CC1 [= 26,0?1]. ... Yesterday the Republicans cast 13,306 votes, the Democrats 7443, the Union Laborites 5066 and the Socialists 206." Sum = 26,021 ~ registrar row 26,039.
- So the registrar primary series' 1903 row IS the all-party total; the series intends all-party totals (1899 32,521 all-party too per repo notes). The 1905 row breaks the pattern.

### Dead ends
- FY1905-06 Municipal Reports (sanfranciscomuni56sanfrich): no Aug 1905 primary canvass at all (fire).
- FY1916-17 volume (munisanfrancisco66sanfrich, server ia801405, path /20/items/...): fulltext "28,951"/"41,117"/"87,062"/"31,728" zero hits.
- FY1915-16 volume fulltext: "28,951" and "87,062" appear ONLY on API page 351 (the p.331 index row); "41,117"/"31,728"/"40,052" nowhere.
- CDNC OCR search for "28,951" (SFC 1905-08-09..12-31) and "41,117": no hits (Aug 15 table digits garbled in OCR; negative not meaningful).
- The Call's promised "segregated Republican vote" table (League vs Ruef split of 31,728) was never printed in SFC19050815.2.110; text jumps straight to voting-machine business. League/Ruef official split unrecovered.
- NewsBank/SFPL Chronicle probe (was 28,951 the Chronicle's morning-after footing?): ezproxy session is LOGGED OUT (sweep_section.js returns NO ENTRY even for known-good 1908-11-04). FLAG for manual operator: after re-login, run `node scripts/archive-recovery/sweep_section.js 1905-08-08 1905-08-09 9 10 7` (pre-1906: SF returns live in the later SF section, often p9) and check whether the Chronicle's summary total = 28,951.
- Web search for 41,117/28,951 in histories (Bean etc.): nothing indexed.

## VERDICT
1. TRUE ALL-PARTY TOTAL of the Aug 8, 1905 municipal primary = 41,117 ballots, the OFFICIAL result declared by the Board of Election Commissioners on Monday Aug 14, 1905, printed SF Call 1905-08-15 p10 (SFC19050815.2.110, "BOARD MAKES OFFICIAL COUNT / Commissioners Announce Correct Number of Ballots Cast at the Primary"): Republican 31,728 / Democratic 3,732 / Socialist 319 / Union Labor 4,500 / Scattering 838 / Total 41,117. Every column and row foots exactly. Read by eye from stitched page tiles (imgs/cdnc_19050815_p10_2-110_b4.png). Corroboration chain: Call night compilation 38,120 (incomplete, dashes in several districts), Call next-day semi-official 40,052, AP wire ~38,968-38,977, official-canvass progress notes Aug 10-12 ("no changes"), declaration Aug 14.
2. 28,951 (FY1915-16 categorized index p.331, the ONLY registrar printing, verified by eye at leaf n350) denominates NOTHING in the official canvass: it is not the all-party total (41,117), not the Republican column (31,728; so NOT a repeat of the 1908 Republican-only slip), not any other column (3,732/319/4,500/838), not a faction (League ~16.1-16.2k, Ruef ~15.4-15.5k), and no simple column/district combination produces it. It is a fire-era backfill (all 1905 election records burned April 1906; the FY1905-06 volume prints no canvass) of unknown source, equal to 70.4% of the true total; its companion registration figure 87,062 may be sound (it is the only other surviving figure) but the vote-polled figure is unsupported by any contemporary official or press number found.
3. RECOMMENDATION for the dataset: certified/official final for 1905-08-08 should be 41,117 (primary source: Election Commissioners' declared official result via SF Call 1905-08-15 p10); 28,951 should be demoted to a noted discredited registrar-series value (same class of series defect as the 1908 Republican-only row, but a different failure mode: wrong-scope/unknown-source backfill rather than wrong-column pick). Registration 87,062 and precincts 198 may stand with a caveat. Night count: the Call's 38,120 night compilation = 92.7% of 41,117 (printed under "OFFICIAL FIGURES ARE INCOMPLETE", 2 a.m. state); next-morning complete semi-official 40,052 = 97.4%.
- SFC19050810 TOC fetched. Page 4: SFC19050810.2.63 "REPUBLICAN LEAGUE HOST PRESENTS FIRM FRONT." / 2.63.1 "FIGURES SHOW HOW GANGSTERS MET DEFEAT AT PRIMARIES" / 2.63.2 "BEGIN OFFICIAL COUNT." (saved mirror/cdnc/SFC19050810/page_4.txt)
- SFC19050810.2.63.1 "FIGURES SHOW HOW GANGSTERS MET DEFEAT AT PRIMARIES" (p4): COMPLETE next-day semi-official per-district table, 18 districts, Totals row (verbatim OCR): "Totals 15,476 16,200 2,837 660 4,024 245 320 40,052". Column order here: Ruef Republican 15,476 / Republican League 16,200 / Democrat 2,837 / Reorganized Dem 660 / Union Labor 4,024 / opp Union Labor 245 / Socialist 320 / TOTAL VOTE 40,052. (Republican-only = 31,676.) NOTE: printed column sum = 39,762, 290 short of printed 40,052; some district cells OCR-garbled/blank (35th, 40th rows); the printed grand total is 40,052.
- SFC19050810.2.63.2 "BEGIV OFFICIAL COUNT." (verbatim): "The Election Commissioners yesterday began the official count of the returns for the primary election. Five districts — the Twenty-eighth, Twentyninth, Thirtieth. Thirty-first and Thir-ty-second — were canvassed during the day, but no changes were noted that would affect the result as already announced on the semi-official returns. In the Twelfth Precinct of the Thirtieth District the Republican League ticket lost five votes and the Regular Democratic ticket also lost the same number. The count will be proceeded with to-day and will probably be completed to-morrow."
- So: semi-official complete total = 40,052 (record); official canvass completion expected Aug 11; chase SFC19050811/12/13 for the certified totals.
