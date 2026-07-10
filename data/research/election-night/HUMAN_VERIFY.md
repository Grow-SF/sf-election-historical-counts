# Hand-verification packet (election-night)

Division of labor. The machine pass verified two things only: every
certified final matches the CA SoS Statement of Vote PDF, and every
claimed night count appears at its cited URL (citations intact, nothing
mistyped or fabricated). It CANNOT verify the metric itself: that the
cited report is the LAST report posted on election night (the plateau),
not an earlier tranche or a later canvass update. The claimed numbers
were extracted by research agents, so re-finding them at the same
citation is circular; the plateau judgment is yours on every sourced
row below.

A controller (Fable) plateau verdict now accompanies each sourced row
(full evidence: PLATEAU_REVIEW.md). Treat non-CONFIRMED rows as first
priority and spot-audit CONFIRMED ones; your reading still wins.

Your reading wins: any discrepancy, even one ballot, gets corrected in
the county JSON and VERIFY.md (then rerun scripts/build_county_night.py
and scripts/research/build_en_verification_report.py). The full working
note for any row is its detail bullet in VERIFY.md (same directory).

## 1. Machine check could not verify these (open and eyeball)

## 2. Secondary-confidence rows (weakest sourcing, read closely)

- [ ] **napa-ca 2014-11-04** (secondary confidence)
      claimed: night ballots **18,286**, certified final **38,766**, share **47.17%**
      numerator URL: https://web.archive.org/web/20150916061050/http://www.countyofnapa.org/ElectionResults/20141104/20141104-2230_dtl.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: BEST-AVAILABLE (10:30 PM report; the EXACT final-of-night report is permanently unrecoverable from Wayback). Napa's 11/4/2014 election-night reports ran 8:01 PM (20141104-2001) -> 10:30 PM (20141104-2230) -> 10:42 PM final (20141104-2242). RE-VERIFIED: the 10:42 PM final-of-night report's content fr
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2014-11-04
      controller verdict: PLAUSIBLE (on-night floor; the exact final report is unarchived)

- [ ] **placer-ca 2018-11-06** (secondary confidence)
      claimed: night ballots **113,380**, certified final **177,725**, share **63.8%**
      numerator URL: https://web.archive.org/web/20181113195233/https://www.placerelections.com/election-night-results/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: 113,380 'Cards Cast', the registrar's GEMS 'SEMI-OFFICIAL ELECTION SUMMARY' with all 358 of 358 precincts reporting (48.98% reg turnout). CAVEAT ON PLATEAU: unlike 2014/2016 (whose embedded report data-stamps were ~12:30 a.m. election night), this report's OWN embedded data timestamp is '11/09/18 15
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2018-11-06
      controller verdict: REFUTED_AS_PLATEAU (page provably tracked the canvass)

- [ ] **riverside-ca 2024-11-05** (secondary confidence)
      claimed: night ballots **611,101**, certified final **959,098**, share **63.7%**
      numerator URL: https://web.archive.org/web/20241107034053/https://www.livevoterturnout.com/ENR/riversidecaenr/5/en/Index_5.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: 611,101 'Ballots Counted' from the earliest Wayback capture of Riverside's livevoterturnout ENR, embedded timestamp 'Updated: 11/6/2024 5:35:21 PM' -- the FIRST daily canvass update (afternoon of the day after the Nov 5 election), NOT the ~3 a.m. election-night plateau. Riverside reports hourly unti
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2024-11-05
      controller verdict: REFUTED_AS_PLATEAU (next-day canvass update, already documented in the note)

- [ ] **santa-clara-ca 2014-11-04** (secondary confidence)
      claimed: night ballots **251,620**, certified final **404,166**, share **62.26%**
      numerator URL: https://web.archive.org/web/20141106082527/http://results.enr.clarityelections.com/CA/Santa_Clara/54209/148095/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CEILING (next-day all-precincts report; true overnight plateau modestly lower and not archived). The overnight election-night versions of Clarity event 54209 (Web01 layout; lower version folders 143630, 144518, 147xxx) WERE captured by Wayback as summary.html only -- their electionsettings.json/sum.
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2014-11-04
      controller verdict: PLAUSIBLE (documented ceiling: next-day canvass-start report)

## 3. Blocked-source recoveries (need a real browser)

- [ ] **fresno-ca 2018-11-06** (operator-flagged)
      claimed: night ballots **null (recover if possible)**, certified final **256,972**
      numerator URL: (none)
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Certified final 256,972 ballots cast (CA SoS; election-day 93,581 + VBM 163,391; 56.24% of 456,891 registered). Pre-adoption, precinct-based (last midterm before VCA/e-pollbook/ASV in 2020). Election-night PLATEAU not sourceable. Fresno's 2018 GEMS results were served on the co.fresno.ca.us results 
      full flag: Certified final 256,972 ballots cast (CA SoS; election-day 93,581 + VBM 163,391; 56.24% of 456,891 registered). Pre-adoption, precinct-based (last midterm before VCA/e-pollbook/ASV in 2020). Election-night PLATEAU not sourceable. Fresno's 2018 GEMS results were served on the co.fresno.ca.us results page (/departments/county-clerk-registrar-of-voters/election-information/election-results/2018-november-general-election-results) with an embedded GEMS 'Election Summary Report'; that page's earliest Wayback capture is 2018-11-28, and by then the embed already showed a CANVASS report ('Unofficial Results 11/21/18 14:49:05', Cards Cast 239,032 of 455,662, 100% of 640 precincts) -- a mid-canvass figure 15 days out, NOT the election-night plateau. No no-dash election-night frozen file (Results20181106.htm) and no www2/2850/Post/2018Nov6 summary report were archived. News proxies give only day-after running framings (ABC30 abc30.com/fresno-county-elections-ballots-counting-votes/4642191/ 'more than 100,000 ballots still need to be counted'; GV Wire 11/7/2018) and are now both curl- and WebFetch-blocked (gvwire.com returns 403; McClatchy Fresno Bee blocked) -- FLAG for manual operator browser follow-up. Null per definition.

- [ ] **sacramento-ca 2016-11-08** (operator-flagged)
      claimed: night ballots **null (recover if possible)**, certified final **575,711**
      numerator URL: (none)
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night plateau NOT directly sourceable for 2016 — confirmed exhausted across all three numerator routes. (1) PRESS-RELEASE route (now checked): Sacramento County VRE issued NO morning-after 'semi-official/semi-final results' release stating a ballot total in 2016. The MediaRoom press-release
      full flag: Election-night plateau NOT directly sourceable for 2016 — confirmed exhausted across all three numerator routes. (1) PRESS-RELEASE route (now checked): Sacramento County VRE issued NO morning-after 'semi-official/semi-final results' release stating a ballot total in 2016. The MediaRoom press-release archive (Wayback 20161122005718 of elections.saccounty.net/MediaRoom/Pages/PressReleases.aspx) shows the post-election cadence as releases dated Nov 10, Nov 14, Nov 16 ('Presidential General Election Update – Ballot Count Update to be Released on …'); the FIRST post-election release (NewsReleases/Pages/Ballot-Count-Update---11102016.aspx, earliest capture 20161116003641) carries NO numbers — its full body only states 'Registrar of Voters Jill LaVine will release the next update after 3:00 p.m. on Friday, November 11' and points readers to sacresults.e-cers.com / eresults.saccounty.net. (2) eresults.saccounty.net Hart 'SUMMARY REPORT' route: only two captures bracket this election — 20161107220729 (pre-election, Nov 7, zero/test run) and 20161112083512 (embeds the Friday-canvass Run Date 11/11/16 02:46 PM, PRECINCTS 1,267/1,267, BALLOTS CAST - TOTAL 385,520). No Nov 8-evening / Nov 9-morning capture. (3) sacresults.e-cers.com live app: the only election-window capture is the homepage 20161110162635, which shows 'Precincts Reporting: 1267/1267, Last Refresh 11/9/2016 1:10:20 PM' but the ballots-cast/turnout total loads via AJAX (resultsVoterTurnout.aspx) that Wayback did not archive until the canvass (11/13); NO e-cers turnout or contest sub-page (resultsVoterTurnout.aspx, resultsSW.aspx) was archived anywhere in the Nov 8-11 plateau window. The Friday 11/11 canvass figure 385,520 (= 66.96% of the 575,711 certified) is an UPPER BOUND, not the metric; the true election-night plateau would be lower and, by analogy to the clean 2012 presidential plateau (62.93%), was likely ~60-63%, but it is not directly sourceable, so null/none. FLAG for manual operator follow-up: the Sacramento Bee (McClatchy, curl/WebFetch-blocked) is the most likely place a published Nov 8-9 election-night ballots-cast figure could be recovered. Denominator = CA SoS Voter Participation Statistics by County, Sacramento Total Voters 575,711 (Precinct 203,114 + VBM 372,597). NEWSBANK DEAD-END (2026-07-09): Sacramento Bee, The (CA), Nov 9-10 2016 editions (source-restricted Newspaper/Text search, NewsBank Access World News via SFPL ezproxy) searched with the brief's query list -- "ballots counted", "ballots cast", "votes counted" election night, LaVine ballots, turnout Sacramento County, precincts reporting Sacramento County -- plus broader sweeps (ballots; ballots counted turnout; election night results Sacramento; semi-official Sacramento; unofficial results Sacramento County; LaVine; registrar ballots counted), all restricted to source="Sacramento Bee, The (CA)", Source type=Newspaper. Nine articles opened in full (docrefs news/160D44B84941A100, news/160D44BAB1FDB6D8, news/160D44B7CA8EF8F0, news/160AF31155E01CE8, news/160AF30E34506520, news/160AF30D446FD958, news/160AF311F75538E0, news/160AF310DE119608, news/160B9E00F42AD3F0); no countywide election-night ballots-counted total was published. Every Sacramento County figure found is explicitly labeled the FIRST TRANCHE: Tony Bizjak's Measure B (transit sales tax) story (Nov 9 edition) states the measure "had 66 percent approval among the initial 150,000 absentee ballots" in "early voting returns Tuesday night" (150,000 / 575,711 = 26%, well below the ~40% first-tranche threshold, consistent with a pre-election mail-only dump, not the plateau); the Frost-Kozlowski supervisors race and Elk Grove mayor stories likewise cite only "initial results"/"early returns" percentages (no ballots-counted total or precincts-reporting count attached, so no ratio-floor is computable). The one candidate figure found for a time after election night, Loretta Kalb's school-measures story (Nov 10 edition) quoting Registrar Jill LaVine that "more than 250,000 ballots countywide Tuesday remain uncounted" "as of Wednesday afternoon", is explicitly dated to Wednesday AFTERNOON (post-night, not election night) and is imprecise (a floor on the ballots REMAINING, not an exact counted total), so it fails both the RUNBOOK 5.2 ceiling test (must be dated to a specific post-night report, not a rounded verbal estimate) and the brief's requirement that any post-night figure be explicitly timestamped to election night to count; it is recorded here for completeness and NOT adopted as a value. This NewsBank pass is now exhausted alongside the three prior numerator routes (press release, eresults.saccounty.net, sacresults.e-cers.com); row remains null/none.

## 4. Machine-confirmed rows (number is at the URL; plateau read still owed)

- [ ] **fresno-ca 2016-11-08** (plateau check)
      claimed: night ballots **177,183**, certified final **291,890**, share **60.7%**
      numerator URL: https://web.archive.org/web/20161112171743/http://www2.co.fresno.ca.us/2850/Results/Results20161108.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night PLATEAU = 177,183 ballots ('Registered Voters 437667 - Cards Cast 177183 40.48%', 'Num. Report Precinct 592 - Num. Reporting 592 100.00%'), from Fresno County's official GEMS 'Election Summary Report' headed 'Fresno County Unofficial Final Results ... 11/9/2016 1:42:19 AM' -- the LAST
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2016-11-08
      controller verdict: CONFIRMED (frozen GEMS live page, held past night)

- [ ] **fresno-ca 2024-11-05** (plateau check)
      claimed: night ballots **206,372**, certified final **330,932**, share **62.36%**
      numerator URL: https://web.archive.org/web/20241107003627/https://www.fresnocountyca.gov/files/sharedassets/county/v/5/county-clerk-registrar-of-voters/1_election-results-page-sov-ssov/2024/november-5th-general-election/electionsummaryreportrpt_11_5_24_1231.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night PLATEAU = 206,372 ballots ('Voters Cast: 206,372 of 511,349', 40.36% of registered), from Fresno County's OFFICIAL 'Election Summary Report' dated/internally timestamped 11/6/2024 12:30:26 AM with Precincts Reported 478 of 478 (100.00%) -- the LAST election-night update (file election
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2024-11-05
      controller verdict: CONFIRMED (official county summary PDF, end of night)

- [ ] **los-angeles-ca 2012-11-06** (plateau check)
      claimed: night ballots **2,368,283**, certified final **3,236,704**, share **73.17%**
      numerator URL: https://www.lavote.gov/Documents/News_Releases/11072012-055616.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau. LA County RR/CC 'Semi-Final Official Election Results' news release (Documents/News_Releases/11072012-055616.pdf, released ~5:56 AM Nov 7 2012): 'On Election Night a total of 2,368,283 ballots were counted' (448,470 vote-by-mail + 1,919,813 precinct; the RR/CC estimated 792
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2012-11-06
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **los-angeles-ca 2014-11-04** (plateau check)
      claimed: night ballots **1,147,248**, certified final **1,518,835**, share **75.53%**
      numerator URL: https://www.lavote.gov/Documents/News_Releases/11052014.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PRIMARY official plateau (verified against the release PDF). LA County RR/CC (Dean Logan) 'Semi-Final Official Results Reported for the Nov. 4, 2014 General Election' (Documents/News_Releases/11052014.pdf, morning of Nov 5 2014): 'A total of 1,147,248 ballots were processed and counted, with 25.25% 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2014-11-04
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **los-angeles-ca 2016-11-08** (plateau check)
      claimed: night ballots **2,306,321**, certified final **3,544,115**, share **65.07%**
      numerator URL: https://www.lavote.gov/Documents/News_Releases/11082016-semi-official-results.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau (fills the prior null). LA County RR/CC semi-official results release (Documents/News_Releases/11082016-semi-official-results.pdf): announced semi-final official results for the Nov. 8 General Election, 'A total of 2,306,321 ballots were processed and counted, with 45.19% of
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2016-11-08
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **los-angeles-ca 2018-11-06** (plateau check)
      claimed: night ballots **1,975,855**, certified final **3,023,417**, share **65.35%**
      numerator URL: https://www.lavote.gov/docs/rrcc/news-releases/11062018_semi-official-results.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau (REPLACES the earlier derived lower-bound 2,038,417). LA County RR/CC semi-official results release (docs/rrcc/news-releases/11062018_semi-official-results.pdf): semi-official results for the Nov. 6 General Election, 'A total of 1,975,855 ballots were processed and counted, 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2018-11-06
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **los-angeles-ca 2022-11-08** (plateau check)
      claimed: night ballots **1,318,093**, certified final **2,456,701**, share **53.65%**
      numerator URL: https://www.lavote.gov/docs/rrcc/news-releases/11082022_semi-final-results.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau (verified against the canonical RR/CC release PDF; previously cited via the lacounty.gov blog). LA County RR/CC 'Semi-Final Results Announced for the 2022 General Election' (docs/rrcc/news-releases/11082022_semi-final-results.pdf): 'A total of 1,318,093 ballots were processe
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2022-11-08
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **los-angeles-ca 2024-11-05** (plateau check)
      claimed: night ballots **2,615,541**, certified final **3,793,106**, share **68.96%**
      numerator URL: https://content.lavote.gov/docs/rrcc/documents/11-11062024_pr-11052024_semi-final-results.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau (confirms the earlier derivation EXACTLY). LA County RR/CC 'Semi-Final Results Announced for the 2024 General Election' (content.lavote.gov/docs/rrcc/documents/11-11062024_pr-11052024_semi-final-results.pdf, Nov 6 2024): 'A total of 2,615,541 ballots were processed and count
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2024-11-05
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **madera-ca 2016-11-08** (plateau check)
      claimed: night ballots **35,364**, certified final **44,186**, share **80.0%**
      numerator URL: https://web.archive.org/web/20161112115134/http://votemadera.com/results/Election33/HTML/resultsc33.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Numerator 35,364 = the election-night Semi-Final Official Canvass total from votemadera.com's static results page resultsc33.htm/result33.htm, header 'Election Results as of 11/08/2016 at 11:31:17 PM', 102 of 102 precincts completed: Precinct Ballots Cast 12,803 + Absentee Ballots Cast 22,561 = Tota
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2016-11-08
      controller verdict: CONFIRMED (static county results page, frozen)

- [ ] **madera-ca 2018-11-06** (plateau check)
      claimed: night ballots **28,159**, certified final **38,968**, share **72.26%**
      numerator URL: https://web.archive.org/web/20260627203408/https://results.enr.clarityelections.com/CA/Madera/92458/220349/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Numerator 28,159 = total Ballots Cast (Contests[0].BC) from the Madera County Clarity ENR election-night data version 220349 (results.enr.clarityelections.com/CA/Madera/92458/220349/json/sum.json), recovered from the LIVE Clarity CDN (immutable version-pinned data) and freshly archived to Wayback (s
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2018-11-06
      controller verdict: CONFIRMED (clarity version bracket, re-derived from CDN)

- [ ] **madera-ca 2022-11-08** (plateau check)
      claimed: night ballots **21,951**, certified final **37,345**, share **58.78%**
      numerator URL: https://web.archive.org/web/20260627203522/https://results.enr.clarityelections.com/CA/Madera/116174/311779/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Numerator 21,951 = total Ballots Cast (Contests[0].BC) from the Madera County Clarity ENR election-night data version 311779 (results.enr.clarityelections.com/CA/Madera/116174/311779/json/sum.json), recovered from the LIVE Clarity CDN (immutable version-pinned data) and freshly archived to Wayback (
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2022-11-08
      controller verdict: CONFIRMED (clarity version bracket, re-derived)

- [ ] **madera-ca 2024-11-05** (plateau check)
      claimed: night ballots **37,106**, certified final **55,329**, share **67.1%**
      numerator URL: https://web.archive.org/web/20241108001837/https://results.enr.clarityelections.com/CA/Madera/122832/353191/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Numerator 37,106 = total Ballots Cast (field BC) from the Madera County Clarity ENR election-night data version 353191 (results.enr.clarityelections.com/CA/Madera/122832/353191/json/sum.json), recovered via Wayback (snapshot 20241108001837). The version's electionsettings.json gives websiteupdatedat
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2024-11-05
      controller verdict: CONFIRMED (clarity version bracket, re-derived)

- [ ] **napa-ca 2012-11-06** (plateau check)
      claimed: night ballots **32,715**, certified final **57,672**, share **56.73%**
      numerator URL: https://web.archive.org/web/20121208223758/http://www.countyofnapa.org/ElectionResults/20121106/20101102-1129PM_dtl.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = final-of-night report. County 'Unofficial Election Night Results' detail header reads 'Last Updated: November 6, 2012 11:29 PM (Last of the Night)'. Registration & Turnout block: Vote by Mail Turnout 26,846 + Election Day Turnout 5,869 = Total 32,715 (45.07% of 72,592 reg). Napa released A
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2012-11-06
      controller verdict: CONFIRMED (county report self-describes)

- [ ] **napa-ca 2016-11-08** (plateau check)
      claimed: night ballots **34,108**, certified final **63,255**, share **53.92%**
      numerator URL: https://web.archive.org/web/20161218225536/http://www.countyofnapa.org/ElectionResults/20161108/20161108-2306.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = final-of-night report. County 'Election Summary Report' PDF 20161108-2306.pdf (filename ts = Nov 8 2016, 23:06 = 11:06 PM) is the LAST election-night report (next archived file is the Nov 16 canvass update 20161116-1635.pdf, then the Dec 5 certified Final). Header: 'Precincts Reported: 167
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2016-11-08
      controller verdict: CONFIRMED (county last-report title)

- [ ] **napa-ca 2018-11-06** (plateau check)
      claimed: night ballots **21,774**, certified final **57,132**, share **38.11%**
      numerator URL: https://www.napacounty.gov/DocumentCenter/View/10436/Last-Unofficial-Election-Night-Report-11-06-18-PDF
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 'LAST UNOFFICIAL ELECTION NIGHT REPORT' (napacounty.gov DocumentCenter View/10436, the last of First/Last pair published election night). 'Precincts Reported: 170 of 170 (100.00%)', 'Registered Voters: 21,774 of 78,135 (27.87%)', and per-contest 'Times Cast 21,774'. ('Ballots Cast: 43,611'
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2018-11-06
      controller verdict: CONFIRMED (county titled last-of-night series)

- [ ] **napa-ca 2022-11-08** (plateau check)
      claimed: night ballots **21,943**, certified final **50,788**, share **43.21%**
      numerator URL: https://www.napacounty.gov/DocumentCenter/View/26985/Last-Unofficial-Election-Night-Report-1046-PM-11822-PDF
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 'Last Unofficial Election Night Report' timestamped 10:46 PM (napacounty.gov DocumentCenter View/26985; the night's reports ran First 8:01 PM -> Second 9:50 PM -> Last 10:46 PM, then the Nov 14 4:19 PM '1st Post Election Night' canvass report View/26995). Header: 'Precincts Reported: 200 o
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2022-11-08
      controller verdict: CONFIRMED (county titled last-of-night series)

- [ ] **napa-ca 2024-11-05** (plateau check)
      claimed: night ballots **26,160**, certified final **66,634**, share **39.26%**
      numerator URL: https://www.napacounty.gov/DocumentCenter/View/34231/Last-Unofficial-Election-Night-Results-1235AM-11062024-PDF
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 'Last Unofficial Election Night Report' timestamped 12:35 AM Nov 6 (napacounty.gov DocumentCenter View/34231; the night's reports ran First 8:01 PM 22,504 -> Second 9:49 PM -> Third 11:45 PM -> Last 12:35 AM 26,160, monotonic, then the multi-day canvass). Header: 'Precincts Reported: 204 o
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2024-11-05
      controller verdict: CONFIRMED (county titled last-of-night series)

- [ ] **nevada-ca 2012-11-06** (plateau check)
      claimed: night ballots **31,275**, certified final **52,173**, share **59.94%**
      numerator URL: https://web.archive.org/web/20121112105530/http://yubanet.com:80/regional/Nevada-County-Election-Tally-Continues---Turnout-Is-Nearly-80-Mail-Ins-Top-16-000.php
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 31,275, the END-OF-ELECTION-NIGHT tabulation. Official Nevada County Elections Office release (Registrar Gregory Diaz / Assistant Registrar Gail Smith quoted), republished verbatim by YubaNet: 'On Tuesday, Election Day, workers in the election office tabulated a total of 31,275 votes by 1 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2012-11-06
      controller verdict: CONFIRMED (county release republished verbatim)

- [ ] **nevada-ca 2014-11-04** (plateau check)
      claimed: night ballots **22,366**, certified final **39,629**, share **56.44%**
      numerator URL: https://web.archive.org/web/20141108075409/http://yubanet.com:80/regional/Many-Nevada-County-races-too-close-to-call.php
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PLATEAU = 22,366, the FINAL election-night cumulative. YubaNet's 'Many Nevada County races too close to call' (Nov 5 2014) republished the county's official final election-night report: 'The final election night tally of votes comes in at 22,366 of 61,706 - a rather low voter turnout of 36.25%' (61,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2014-11-04
      controller verdict: CONFIRMED (morning-after report of the official night tally)

- [ ] **nevada-ca 2016-11-08** (plateau check)
      claimed: night ballots **34,728**, certified final **56,800**, share **61.14%**
      numerator URL: https://yubanet.com/regional/nevada-county-ballot-measures-fate-depends-on-remaining-absentee-ballots/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 34,728, the LAST election-night update. YubaNet's morning-after article (published Nov 9 2016 10:08 UTC) reporting the county's official cumulative election-night results on countywide Measure A: 'Measure A received 23,060 Yes votes, 68.99% of the 34,728 ballots counted as of tonight ... i
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2016-11-08
      controller verdict: CONFIRMED (morning-after report of the official cumulative)

- [ ] **nevada-ca 2018-11-06** (plateau check)
      claimed: night ballots **26,956**, certified final **54,996**, share **49.01%**
      numerator URL: https://yubanet.com/regional/an-estimated-22000-ballots-remain-to-be-counted-in-nevada-county/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 26,956, the END-OF-ELECTION-NIGHT total stated by the county. YubaNet 'An estimated 22,000 ballots remain to be counted in Nevada County' (published Nov 7 2018 morning): 'NEVADA CITY, Calif. November 7, 2018 - At the end of election night, 26,956 ballots have been counted in Nevada County,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2018-11-06
      controller verdict: CONFIRMED (morning-after county statement)

- [ ] **nevada-ca 2022-11-08** (plateau check)
      claimed: night ballots **28,824**, certified final **51,370**, share **56.11%**
      numerator URL: https://yubanet.com/regional/election-day-is-over-whats-the-holdup-in-results/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 28,824, the end-of-election-night cumulative. YubaNet 'Election Day is over, what's the holdup on results?' (morning after, Nov 9 2022): 'For the November 8th election 74,225 vote by mail ballots were issued ... Last night, 38.83% of those ballots - 28,824 were counted. The first results o
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2022-11-08
      controller verdict: CONFIRMED (morning-after county explainer)

- [ ] **nevada-ca 2024-11-05** (plateau check)
      claimed: night ballots **15,486**, certified final **63,240**, share **24.49%**
      numerator URL: https://www.nevadacountyca.gov/DocumentCenter/View/55078/Third-Report-Cumulative-Results-11-5-2024-11-24-31-PM
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 15,486, CONFIRMED as the LAST of the three election-night reports. Source: Nevada County Elections' own official 'Third Report - Cumulative Results' PDF (DocumentCenter View/55078), Run Date 11/05/2024, Run Time 11:24 PM, Precincts Reporting 118 of 118 = 100.00%, Ballots Counted = 15,486 (
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2024-11-05
      controller verdict: CONFIRMED (county's own last-of-three night report)

- [ ] **orange-ca 2012-11-06** (plateau check)
      claimed: night ballots **862,544**, certified final **1,133,204**, share **76.12%**
      numerator URL: https://ocvote.gov/fileadmin/live/gen2012/Run09/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). OCROV posted sequential 'Cumulative Totals' runs every ~20-40 min through election night: Run 01 (Run Date/Time 11/06/2012 07:45:25 pm) = 385,929 ballots / 0 of 1,977 precincts = vote-by-mail-only first tranche; the count th
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2012-11-06
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **orange-ca 2014-11-04** (plateau check)
      claimed: night ballots **464,313**, certified final **640,358**, share **72.51%**
      numerator URL: https://ocvote.gov/fileadmin/live/gen2014/Run%2009/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Run 01 (Run Date/Time 11/04/2014 07:54:23 pm) = 250,187 ballots / 0 of 1,863 precincts = vote-by-mail-only first tranche; the count climbed and PLATEAUED at Run 09 (Run Date/Time 11/05/2014 01:55:59 am) = 464,313 ballots wit
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2014-11-04
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **orange-ca 2016-11-08** (plateau check)
      claimed: night ballots **825,317**, certified final **1,239,405**, share **66.59%**
      numerator URL: https://ocvote.gov/fileadmin/live/gen2016/Run%2011/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Run 01 (Run Date/Time 11/08/2016 08:03:32 pm) = 430,263 ballots / 0 of 1,668 precincts = vote-by-mail-only first tranche; the count climbed and PLATEAUED at Run 11 (Run Date/Time 11/09/2016 01:55:57 am) = 825,317 ballots wit
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2016-11-08
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **orange-ca 2018-11-06** (plateau check)
      claimed: night ballots **650,671**, certified final **1,106,729**, share **58.79%**
      numerator URL: https://ocvote.gov/fileadmin/live/gen2018/Run_11/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Run 01 (Run Date/Time 11/06/2018 07:49:18 pm) = 362,079 ballots / 0 of 1,546 precincts = vote-by-mail-only first tranche; the count climbed and PLATEAUED at Run 11 (Run Date/Time 11/07/2018 01:48:27 am) = 650,671 ballots wit
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2018-11-06
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **orange-ca 2022-11-08** (plateau check)
      claimed: night ballots **611,060**, certified final **994,277**, share **61.46%**
      numerator URL: https://ocvote.gov/fileadmin/live/Gen2022/Run_08/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Vote-center era (precincts read 100% from Run 02 on, so the plateau is identified by the election-night/next-day TIME GAP, not precinct %). Run 01 (Run Time 8:00 PM, 11/08/2022) = 442,334 ballots = pre-Election-Day mail firs
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2022-11-08
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **orange-ca 2024-11-05** (plateau check)
      claimed: night ballots **1,007,150**, certified final **1,417,397**, share **71.06%**
      numerator URL: https://ocvote.gov/fileadmin/live/GEN2024/Run_09/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Vote-center era (precincts read 100% from Run 02 on, so the plateau is identified by the election-night/next-day TIME GAP, not precinct %). Run 01 (Run Time 8:00 PM, 11/05/2024) = 718,019 ballots = pre-Election-Day mail firs
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2024-11-05
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **placer-ca 2014-11-04** (plateau check)
      claimed: night ballots **76,411**, certified final **115,547**, share **66.1%**
      numerator URL: https://web.archive.org/web/20141115000402/http://www.placerelections.com/election-night-results.aspx
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/2014-complete-sov.pdf
      look for: PLATEAU = 76,411 'Cards Cast', the registrar's GEMS 'SEMI-OFFICIAL ELECTION SUMMARY / Election Night Final' with all 369 of 369 precincts reporting (38.13% reg turnout). The report carries its OWN embedded data timestamp '11/05/14 00:36:57' (12:36 a.m. PT Nov 5, i.e. ~4.5 hrs after 8pm Nov 4 poll cl
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2014-11-04
      controller verdict: CONFIRMED (GEMS night-final report)

- [ ] **placer-ca 2016-11-08** (plateau check)
      claimed: night ballots **109,666**, certified final **190,550**, share **57.55%**
      numerator URL: https://web.archive.org/web/20161113042955/http://www.placerelections.com/election-night-results.aspx
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 109,666 'Cards Cast', the registrar's GEMS 'PLACER COUNTY SEMI-OFFICIAL ELECTION SUMMARY / November 8, 2016 / FINAL' with all 363 of 363 precincts reporting (48.43% reg turnout). The report carries its OWN embedded data timestamp '11/09/16 00:29:40' (12:29 a.m. PT Nov 9, ~4.5 hrs after 8pm
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2016-11-08
      controller verdict: CONFIRMED (GEMS night report)

- [ ] **riverside-ca 2022-11-08** (plateau check)
      claimed: night ballots **205,813**, certified final **604,617**, share **34.0%**
      numerator URL: https://web.archive.org/web/20221109110809/https://www.voteinfo.net/Elections/20221108/docs/ElectionSummaryReportRPT_mhtml.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night plateau = 205,813 ballots ('Voters Cast: 205,813 of 1,310,928 (15.70%)'; Governor Times Cast 205,813) from the official Riverside Dominion EMS 'Semi-Official Election Results' report, Last-Modified 11/09/2022 02:04 PST (the ~2 a.m. final election-night report, within the hourly-until-
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2022-11-08
      controller verdict: CONFIRMED (2 AM report held until the canvass)

- [ ] **sacramento-ca 2012-11-06** (plateau check)
      claimed: night ballots **328,516**, certified final **522,045**, share **62.93%**
      numerator URL: https://web.archive.org/web/20121109045323/http://www.eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, not the 8 p.m. first tranche). Sacramento County VRE posts a fixed-width Hart 'SUMMARY REPORT' on eresults.saccounty.net. The archived capture embeds the SEMI-OFFICIAL report, Run Date 11/07/12, Run Time 12:49 AM (just after midnight on election night), w
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2012-11-06
      controller verdict: PLAUSIBLE (distinct on-time capture exists but is currently unservable)

- [ ] **sacramento-ca 2014-11-04** (plateau check)
      claimed: night ballots **195,317**, certified final **330,817**, share **59.04%**
      numerator URL: https://web.archive.org/web/20141106101214/http://www.eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, not the 8 p.m. first tranche). Archived eresults.saccounty.net capture embeds the Unofficial 'SUMMARY REPORT', Run Date 11/05/14, Run Time 12:33 AM (just after midnight on election night), with PRECINCTS COUNTED 1,263 of 1,263 (100%), BALLOTS CAST - TOTAL
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2014-11-04
      controller verdict: CONFIRMED (Hart summary with night run time, held)

- [ ] **sacramento-ca 2018-11-06** (plateau check)
      claimed: night ballots **185,623**, certified final **522,652**, share **35.52%**
      numerator URL: https://web.archive.org/web/20181107234429/https://eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report). First Voter's Choice Act / vote-center + e-pollbook general for Sacramento. The eresults.saccounty.net page now embeds an 'ElectionSummaryReportRPT'; the archived capture embeds the report stamped 11/7/2018 1:50:09 AM with Total Times Cast (ballots) 185,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2018-11-06
      controller verdict: CONFIRMED (night report held ~22 hours)

- [ ] **sacramento-ca 2022-11-08** (plateau check)
      claimed: night ballots **145,015**, certified final **484,315**, share **29.94%**
      numerator URL: https://web.archive.org/web/20221109091143/https://eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report). The archived eresults.saccounty.net capture embeds the ElectionSummaryReportRPT stamped 11/9/2022 12:00:20 AM (SEMI-FINAL) with Voters Cast 145,015 of 864,814 registered (16.77%). This midnight report is the final election-night report and is verified to
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2022-11-08
      controller verdict: CONFIRMED (county schedule plus midnight report)

- [ ] **sacramento-ca 2024-11-05** (plateau check)
      claimed: night ballots **311,821**, certified final **668,416**, share **46.65%**
      numerator URL: https://web.archive.org/web/20241106151727/https://eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, not the 8:15 p.m. first tranche). The archived eresults.saccounty.net capture (taken 11/6 ~7:17 AM PT, the morning after) embeds the ElectionSummaryReportRPT stamped 11/6/2024 1:56:14 AM (SEMI-FINAL) with Voters Cast 311,821 of 889,465 registered (35.06%)
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2024-11-05
      controller verdict: CONFIRMED (county schedule plus night report)

- [ ] **san-bernardino-ca 2024-11-05** (plateau check)
      claimed: night ballots **434,108**, certified final **771,834**, share **56.24%**
      numerator URL: https://web.archive.org/web/20241106224114/https://elections.sbcounty.gov/elections/2024/1105/results/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night PLATEAU = 434,108 ballots ('Voters Cast: 434,108 of 1,198,556', 36.22% of registered) at Precincts Reported 2,872 of 2,872 (100.00%), from San Bernardino's OFFICIAL Clarity-style results page whose header reads literally 'Final Unofficial Election Night Results' with 'Next Update: Nov
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-bernardino-ca 2024-11-05
      controller verdict: CONFIRMED (county posting schedule brackets the capture)

- [ ] **san-diego-ca 2018-11-06** (plateau check)
      claimed: night ballots **536,734**, certified final **1,173,924**, share **45.72%**
      numerator URL: https://web.archive.org/web/20181107120607/https://www.livevoterturnout.com/SanDiego/LiveResults/en/Index_5.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report). San Diego's live ENR page (livevoterturnout.com/SanDiego/LiveResults/en/Index_5.html) carries an internal 'Website Updated' data timestamp. The only election-night-era Wayback capture, taken 11/7/2018 04:06 PST (Wayback ts 20181107120607), renders 'Websi
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-diego-ca 2018-11-06
      controller verdict: CONFIRMED (night stamp, captured the same night)

- [ ] **san-diego-ca 2022-11-08** (plateau check)
      claimed: night ballots **565,982**, certified final **1,043,490**, share **54.24%**
      numerator URL: https://web.archive.org/web/20221109172128/https://www.livevoterturnout.com/ENR/sandiegocaenr/16/en/Index_16.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report). Vote-center / e-pollbook era; the ENR page shows 'Ballots Cast' with an internal 'Website Updated' data timestamp. Sequence from Wayback captures of Index_16.html: 11/8/2022 8:01:54 PM = 487,957 (first tranche, pre-Election-Day mail + early vote-center);
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-diego-ca 2022-11-08
      controller verdict: CONFIRMED (self-describing final plus next-post schedule)

- [ ] **san-diego-ca 2024-11-05** (plateau check)
      claimed: night ballots **975,373**, certified final **1,503,018**, share **64.89%**
      numerator URL: https://web.archive.org/web/20241106165220/https://www.livevoterturnout.com/ENR/sandiegocaenr/20/en/Index_20.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report) — matches the task's worked example. ENR page Index_20.html shows 'Ballots Counted' with an internal 'Website Updated' data timestamp. Sequence from Wayback captures: 11/5/2024 8:30:32 PM = 855,948 (first tranche, pre-Eday mail + early vote-center); the c
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-diego-ca 2024-11-05
      controller verdict: CONFIRMED (self-describing final)

- [ ] **san-mateo-ca 2012-11-06** (plateau check)
      claimed: night ballots **204,287**, certified final **288,592**, share **70.79%**
      numerator URL: https://smcacre.gov/system/files/migrated/acre/precinct_report_6.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = Final Election Night Report (UPGRADED from prior 'not sourceable'). Official San Mateo County 'Precinct Turnout — Total Voters — Unofficial' report (precinct_report_6.pdf, linked from smcacre.gov/elections/november-6-2012-election-results as the 'Preliminary report available after Semi Fin
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-mateo-ca 2012-11-06
      controller verdict: CONFIRMED (county-archived night turnout report)

- [ ] **san-mateo-ca 2014-11-04** (plateau check)
      claimed: night ballots **112,592**, certified final **164,453**, share **68.46%**
      numerator URL: https://smcacre.gov/system/files/migrated/acre/precinct_turnout_report_0.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PLATEAU = Final Election Night Report (UPGRADED from prior 'not sourceable'). Official San Mateo County 'Precinct Turnout — Total Voters — Unofficial' report (precinct_turnout_report_0.pdf, linked from smcacre.gov/elections/november-4-2014-election-results as the election-night 'Preliminary report..
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-mateo-ca 2014-11-04
      controller verdict: CONFIRMED (county-archived night turnout report)

- [ ] **san-mateo-ca 2016-11-08** (plateau check)
      claimed: night ballots **205,855**, certified final **323,303**, share **63.67%**
      numerator URL: https://smcacre.gov/system/files/migrated/acre/precinctreport.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = Final Election Night Report (UPGRADED from prior 'not sourceable'). Official San Mateo County 'NOV2016_Precinct Turnout — Total Voters — Unofficial' report (precinctreport.pdf, linked from smcacre.gov/elections/november-8-2016-election-results as the election-night 'Preliminary report...po
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-mateo-ca 2016-11-08
      controller verdict: CONFIRMED (county-archived night turnout report)

- [ ] **san-mateo-ca 2018-11-06** (plateau check)
      claimed: night ballots **111,637**, certified final **290,058**, share **38.49%**
      numerator URL: https://web.archive.org/web/20181107121103/https://www.smcacre.org/november-6-2018-election-results
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = last election-night report. County results page captured 2018-11-07 12:11 UTC = Nov 7 4:11 AM PST (the morning AFTER election night, during the pause before the multi-day canvass resumed) shows 'Registration and Turnout': Total Registered Voters 399,591; Precinct Ballots Cast 0; Vote Cente
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-mateo-ca 2018-11-06
      controller verdict: CONFIRMED (on-night capture of the final report)

- [ ] **san-mateo-ca 2022-11-08** (plateau check)
      claimed: night ballots **122,135**, certified final **252,233**, share **48.42%**
      numerator URL: https://web.archive.org/web/20221109174232/https://www.livevoterturnout.com/ENR/sanmateocaenr/11/en/VRcqD_Index_11.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = Final Election Night Report (UPGRADED from prior null/bounded-proxy). Rendered archived San Mateo livevoterturnout ENR (index 11, file VRcqD_Index_11.html) capture 2022-11-09 17:42 UTC — identical across the 17:42 / 20:21 / 22:23 UTC Nov-9 captures — shows the banner 'SEMI-OFFICIAL RESULTS
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-mateo-ca 2022-11-08
      controller verdict: CONFIRMED (self-describing final plus next-update schedule)

- [ ] **san-mateo-ca 2024-11-05** (plateau check)
      claimed: night ballots **213,421**, certified final **337,241**, share **63.28%**
      numerator URL: https://web.archive.org/web/20241107085324/https://www.livevoterturnout.com/ENR/sanmateocaenr/16/en/buXnk_Index_16.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = last election-night report. Rendered livevoterturnout ENR (index 16) capture 2024-11-07 08:53 UTC carries embedded data timestamp 'Website Updated: 11/6/2024 2:18:48 AM' (the final election-night update, ~2:18 AM Nov 6 PST after all vote-center ballots were tallied): VOTER TURNOUT 'Ballots
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-mateo-ca 2024-11-05
      controller verdict: CONFIRMED (self-describing final plus next-update schedule)

- [ ] **santa-clara-ca 2012-11-06** (plateau check)
      claimed: night ballots **438,348**, certified final **653,239**, share **67.1%**
      numerator URL: https://web.archive.org/web/20121110090428/http://results.enr.clarityelections.com/CA/Santa_Clara/43231/110787/en/summary.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = last continuous election-night (overnight) report, NOT the 8 PM first tranche. Full Clarity/SOE ENR trajectory (event 43231, summary.html versions rendered from Wayback id_ raw replay): 109562 'Updated 11/6/2012 7:35:52 PM PST' = 279,357 ballots / 246 of 1000 precincts (pre-processed VBM f
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2012-11-06
      controller verdict: CONFIRMED (long-night report held in a later capture)

- [ ] **santa-clara-ca 2022-11-08** (plateau check)
      claimed: night ballots **293,148**, certified final **550,602**, share **53.24%**
      numerator URL: https://web.archive.org/web/20221109173423/https://results.enr.clarityelections.com/CA/Santa_Clara/115971/311769/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = held election-night (overnight) level. Clarity event 115971 SPA: the Nov 8 election-night data JSON was not crawled, but the EARLIEST archived data version, 311769 (Wayback 20221109173423 = Nov 9 9:34 AM PT), is the held overnight plateau -- sum.json top contest GOVERNOR 'BC' (county-wide 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2022-11-08
      controller verdict: CONFIRMED (clarity version bracket, re-derived)

- [ ] **santa-clara-ca 2024-11-05** (plateau check)
      claimed: night ballots **460,325**, certified final **765,495**, share **60.13%**
      numerator URL: https://web.archive.org/web/20260702055736/https://results.enr.clarityelections.com/CA/Santa_Clara/122582/353227/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = held election-night (overnight) level. Clarity event 122582 SPA: the only archived data version is 353583 (Wayback 20241107034843 = Nov 6 7:48 PM PT), sum.json top contest PRESIDENT AND VICE PRESIDENT 'BC' (county-wide ballots cast; identical across all county-wide contests = total ballots
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2024-11-05
      controller verdict: REFUTED_AND_CORRECTED (clarity version walk recovers the true plateau)

