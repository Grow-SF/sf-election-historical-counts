# Wave 4 NewsBank recovery: 1922-11-21 school bonds + 1944-11-07 general

Status: STARTED 2026-07-08. Salvage file, written as I go.

## Targets
- 1922-11-21 school-bonds special. OFFICIAL FINAL 81,363. Need: E+1 night state from SF Chronicle Wed 1922-11-22 (morning + EXTRA plates count as night, stamp T03:00 or printed clock).
- 1944-11-07 consolidated general (FDR-Dewey). OFFICIAL FINAL 352,409. Need: E+1 night state from SF Chronicle Wed 1944-11-08. Machine-count era; expect big partial/complete; candidate races (machine) may lead paper-ballot measures; capture both if split.

Gate: no claimed figure > final. Contest sums = floors. Estimates/poll lists are NOT counts. Cutoff E+1 06:00.

## Log
- 2026-07-08: CDP 9222 alive, ezproxy NewsBank tab live. Launched sweeps:
  - `node scripts/archive-recovery/sweep_section.js 1944-11-07 1944-11-08 1 3 11` (bg bfrslpozo)
  - `node scripts/archive-recovery/sweep_section.js 1922-11-21 1922-11-22 1 3 12` (bg b53na10re)
  - Sweep search URL pattern (copy-pasteable): https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=alltext&val-base-0=election&bln-base-1=AND&fld-nav-0=YMD_date&val-nav-0=11%2F08%2F1944%20-%2011%2F08%2F1944&sort=YMD_date%3AA
  - At least one sweep printed "entry ok". Awaiting slice output in mirror/newsbank/scans/.
  - REMINDER: NewsBank issue labels are NOT fixed offset from masthead (runbook line 85); must masthead-verify p1. If label=masthead+1, re-sweep with label = issue date -1... i.e. check both.

## 1944-11-08 Chronicle
- MASTHEAD VERIFIED (nb_19441108_p1_s0.png): banner "ELECTION EXTRA!" above nameplate; "San Francisco Chronicle ... FOUNDED 1865--VOL. CLIX, NO. 116  CCCC  SAN FRANCISCO, WEDNESDAY, NOVEMBER 8, 1944". Edition mark "CCCC" (folio stars). Headline: "FDR PILING UP A LEAD IN 24 STATES!"
- This is an ELECTION EXTRA plate => counts on it are night state per operator ruling (extras ~3:30-4 a.m. press runs). Stamp T03:00 unless printed clock found.
- Prior wave (data/recovery_ledger_pre1965.md line 39) claimed "Nov 8 paper had NO SF count", SKIP. Re-examining fresh capture p1-3 + June capture p4-16 (mirror/newsbank/scans/sweep_19441107_issue19441108_p*_s*.png, June 13 mtimes).
- Scans of p1-3 flattened to scratchpad/imgs/nb_19441108_p{1,2,3}_s{0..3}.png
- Page-by-page verdicts (visual + OCR triage, June capture p4-16 + fresh p1-3):
  - p1: ELECTION EXTRA front. National FDR/Dewey. "Election Bulletins" (AP national popular vote 7577 of 130,826 units: Roosevelt 1,539,818 / Dewey 1,209,574 / Total 2,729,392). AP CALIFORNIA statewide "908 precincts of 14,841: Roosevelt 82,846; Dewey 55,912". NO SF COUNT. Behrens col "California Voters Jam The Polls" continues p9.
  - p1 VERBATIM (SF, Behrens col, crop nb_19441108_p1_s2_behrens.png): "HUGE TURNOUT / By 3 o'clock, Registrar Cameron H. King estimated that 51 per cent of the registered electorate, or 207,000, had voted. He predicted an 85 per cent vote would be cast. The record was set in 1936, when 85.5 per cent of those registered went to the polls. ... Polls close in San Francisco at 8 p. m., instead of at 7 as in the remainder of the State." => ESTIMATE of ballots cast, not a count. Gate: not ingestible.
  - p2: war news + "More Than Million Vote in Los Angeles" (LA narrative). No SF count.
  - p3: candidates voting (national). p4: Royce Brier + war. p5: war show/imports. p6: war/theatre. p7: Entertainment. p8: women's world/crossword/radio log.
  - p9: "More About State Vote: RECORD CROWDS JAM POLLS---AN 85 PER CENT TURNOUT HERE PREDICTED BY REGISTRAR" (prediction). "Secretary of State Jordan estimated a total State vote of from 70 to 75 per cent"; absentee ballots (753,167 requested, 98,595 returned figures per OCR, digits unverified) "will not be counted until November 21". County % narratives (Hillsborough 45%, Burlingame 46%, Redwood City 40% BY x PM = share VOTED not counted). NO COUNT.
  - p10: war/opinion. p11: Metropolis (Part Two front): local crime/features, Ration Calendar. p12: Editorial page. p13-16: Sporting Green 1H-4H + comics.
  - NO SF vote-count table or SF partial count ANYWHERE p1-16. Consistent with prior wave's SKIP (data/recovery_ledger_pre1965.md:39).
- DISCOVERY: NewsBank issue actually has 18 pages (probe of results page: "18 Results", single issue id EANX-NB-15027A0D977AB928@2431403, pages 1-18). June sweep stopped at p16. Sweeping p17-18 now (bg, WIN 13).
- Probe URL (copy-pasteable): https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=alltext&val-base-0=election&bln-base-1=AND&fld-nav-0=YMD_date&val-nav-0=11%2F08%2F1944%20-%2011%2F08%2F1944&sort=YMD_date%3AA
- Single edition on file: all 18 results belong to one issue (the CCCC ELECTION EXTRA). No second Nov 8 plate in NewsBank.
- p17 (fresh capture): folio "WEDNESDAY, NOV. 8, 1944 PAGE 17" = classified ads (help wanted). p18: "PAGE 18 WEDNESDAY, NOV. 8, 1944" = classifieds (real estate/autos). NO returns.
- VERDICT 1944-11-07: the day-after Chronicle (ELECTION EXTRA, CCCC plate, the only Nov 8 edition NewsBank holds) prints NO San Francisco vote count of any kind: no precinct line, no SF candidate tally, no measures tally. All SF content is turnout ESTIMATES (Registrar King 3 p.m. estimate 207,000 voted = 51 pct of registered; 85 pct predicted) and the absentee-count deferral (counted Nov 21). Night state per gate: NULL (no count printed by E+1 06:00). Confirms and STRENGTHENS prior SKIP (ledger line 39): now verified against all 18/18 pages incl. the never-before-captured p17-18, on the EXTRA plate itself.
- Scans: mirror/newsbank/scans/sweep_19441107_issue19441108_p{1..18}_s*.png; flattened review copies scratchpad/imgs/nb_19441108_p*.png

## 1922-11-22 Chronicle (E+1 morning for 1922-11-21 school-bonds special)
- MASTHEAD VERIFIED (nb_19221122_p1_s0.png): "San Francisco Chronicle ... FOUNDED 1865--VOL. CXXI, NO. 130  CC  SAN FRANCISCO, WEDNESDAY, NOVEMBER 22, 1922 -- TWENTY-SIX PAGES". Edition mark "CC". Banner headline: "BONDS WIN BY VOTE OF 7 TO 1".
- Sweep cmd: `node scripts/archive-recovery/sweep_section.js 1922-11-21 1922-11-22 1 3 12`; search URL pattern as above with val-nav-0=11%2F22%2F1922%20-%2011%2F22%2F1922. Story: p1 col 1 "PEOPLE RATIFY SCHOOL, RELIEF HOME ISSUES"; box p1 col 2 "Results of Bond Vote Yesterday".
- VERBATIM BOX (zoom nb_19221122_p1_box.png, every digit read at high zoom, none uncertain):
  "Complete returns from all of the 891 precincts in San Francisco show that a total of 81,502 votes were cast as follows in yesterday's bond election:
   SCHOOL BONDS  For 69,262 / Against 11,504 / Majority for 57,758 / Necessary to pass 53,844
   RELIEF HOME BONDS  For 70,445 / Against 9,989 / Majority for 60,456 / Necessary to pass 53,622"
- VERBATIM STORY (nb_19221122_p1_story_s2.png): "TOTAL POLL IS 81,502 / Educational Project Gets 57,758 Majority; Other Proposal, 60,456 ... With unmistakable emphasis, and by a ratio of about 7 to 1, San Francisco yesterday voted for the $12,000,000 school bonds and for the $2,000,000 Relief Home bonds. ... The total vote of the city was 81,502." No completion clock printed anywhere in the story => morning-press stamp T03:00.
- ARITHMETIC (self-summed, all lock):
  - School: 69,262+11,504 = 80,766 ballots in contest; 69,262-11,504 = 57,758 = printed majority OK; floor(2/3*80,766) = 53,844 = printed necessary-to-pass OK.
  - Relief: 70,445+9,989 = 80,434; 70,445-9,989 = 60,456 OK; floor(2/3*80,434) = 53,622 (2/3=53,622.67) OK.
  - Cross-source: matches SF Call Nov 22 evening figures exactly (School 69,262/11,504, Relief 70,445/9,989 per CSV row provenance) => same canonical count, now proven already complete by the MORNING press run, i.e. overnight.
- GATE: largest single-question contest sum (School) = 80,766 <= official final 81,363 => valid NIGHT FLOOR. Printed "total votes cast" 81,502 EXCEEDS official 81,363 by 139 => flagged, NOT claimable as the count (semi-official overnight total later revised down in canvass). Relief sum 80,434 also <= final.
- VERDICT 1922-11-21: E+1 morning night state = COMPLETE, 891/891 precincts. Night floor 80,766 (school-bonds contest sum), observed_at 1922-11-22T03:00:00. Share of official final: 80,766/81,363 = 99.27 pct. This upgrades the prior "timing unproven" (Call evening day+1): the Chronicle MORNING paper proves the complete count existed overnight.

## Structured records (operator, per newsbank-election-recovery step 4)

### 1922-11-21
```
election_date:   1922-11-21
election_name:   Special Bond Election (school + Relief Home)
observed_at:     1922-11-22T03:00:00  (morning press; no printed clock)
night_floor:     80766   (School Bonds For 69,262 + Against 11,504)
night_contest:   School Bonds (single question); Relief Home sum 80,434 (70,445/9,989)
precincts:       891/891  complete ("Complete returns from all of the 891 precincts")
certified_final: 81,363 official (BoS Resolution 20564, already on file). Printed paper total 81,502 OVERSHOOTS official by 139 - flag, do not ingest as count.
certified_src:   unchanged (Journal of Proceedings vol.17 pp.1044-45)
night_src:       SF Chronicle 1922-11-22 p1, "Results of Bond Vote Yesterday" box; scans sweep_19221121_issue19221122_p1_s1.png (+_s2), zoom crops nb_19221122_p1_box.png / nb_19221122_p1_story_s2.png
edition:         CC (morning), Vol CXXI No 130, 26 pages
confidence:      high (all digits arithmetic-locked, no [?] digits; cross-matches SF Call evening figures)
```

### 1944-11-07
```
election_date:   1944-11-07
election_name:   Consolidated General (FDR-Dewey)
observed_at:     n/a - NO SF COUNT in E+1 paper
night_floor:     null (night state = no count published by 06:00 E+1)
night_contest:   none printed (only AP national + statewide CA partials: "CALIFORNIA, 908 precincts of 14,841: Roosevelt 82,846; Dewey 55,912")
precincts:       none printed for SF
certified_final: 352,409 official (on file; not questioned here)
night_src:       dead end - SF Chronicle 1944-11-08 ELECTION EXTRA (CCCC), all 18/18 pages verified (incl. p17-18 captured for the first time); SF content = estimates only (Registrar King: 51 pct/207,000 voted BY 3 p.m., 85 pct predicted; absentees counted Nov 21)
edition:         ELECTION EXTRA, CCCC plate, Vol CLIX No 116, 18 pages (only Nov 8 edition in NewsBank)
confidence:      high for the NULL (visual page-by-page + OCR triage; extra edition itself)
```
