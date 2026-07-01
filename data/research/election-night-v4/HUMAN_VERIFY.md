# Hand-verification packet (election-night-v4)

Open each URL and compare against the claimed value. Your reading wins:
any discrepancy, even one ballot, gets corrected in the county JSON and
VERIFY.md (then rerun scripts/build_county_night.py).

## 1. Machine check could not verify these (open and eyeball)

- [ ] **sacramento-ca 2012-11-06** (numerator NOT_FOUND)
      claimed: night ballots **328,516**, certified final **522,045**, share **62.93%**
      numerator URL: https://web.archive.org/web/20121109045323/http://www.eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, not the 8 p.m. first tranche). Sacramento County VRE posts a fixed-width Hart 'SUMMARY REPORT' on eresults.saccounty.net. The archived capture embeds the SEMI-OFFICIAL report, Run Date 11/07/12, Run Time 12:49 AM (just after midnight on election night), w

## 2. Secondary-confidence rows (weakest sourcing, read closely)

- [ ] **napa-ca 2014-11-04** (secondary confidence)
      claimed: night ballots **18,286**, certified final **38,766**, share **47.17%**
      numerator URL: https://web.archive.org/web/20150916061050/http://www.countyofnapa.org/ElectionResults/20141104/20141104-2230_dtl.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: BEST-AVAILABLE (10:30 PM report; the EXACT final-of-night report is permanently unrecoverable from Wayback). Napa's 11/4/2014 election-night reports ran 8:01 PM (20141104-2001) -> 10:30 PM (20141104-2230) -> 10:42 PM final (20141104-2242). RE-VERIFIED: the 10:42 PM final-of-night report's content fr

- [ ] **placer-ca 2018-11-06** (secondary confidence)
      claimed: night ballots **113,380**, certified final **177,725**, share **63.8%**
      numerator URL: https://web.archive.org/web/20181113195233/https://www.placerelections.com/election-night-results/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: 113,380 'Cards Cast', the registrar's GEMS 'SEMI-OFFICIAL ELECTION SUMMARY' with all 358 of 358 precincts reporting (48.98% reg turnout). CAVEAT ON PLATEAU: unlike 2014/2016 (whose embedded report data-stamps were ~12:30 a.m. election night), this report's OWN embedded data timestamp is '11/09/18 15

- [ ] **riverside-ca 2024-11-05** (secondary confidence)
      claimed: night ballots **611,101**, certified final **959,098**, share **63.7%**
      numerator URL: https://web.archive.org/web/20241107034053/https://www.livevoterturnout.com/ENR/riversidecaenr/5/en/Index_5.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: 611,101 'Ballots Counted' from the earliest Wayback capture of Riverside's livevoterturnout ENR, embedded timestamp 'Updated: 11/6/2024 5:35:21 PM' -- the FIRST daily canvass update (afternoon of the day after the Nov 5 election), NOT the ~3 a.m. election-night plateau. Riverside reports hourly unti

- [ ] **santa-clara-ca 2014-11-04** (secondary confidence)
      claimed: night ballots **251,620**, certified final **404,166**, share **62.26%**
      numerator URL: https://web.archive.org/web/20141106082527/http://results.enr.clarityelections.com/CA/Santa_Clara/54209/148095/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CEILING (next-day all-precincts report; true overnight plateau modestly lower and not archived). The overnight election-night versions of Clarity event 54209 (Web01 layout; lower version folders 143630, 144518, 147xxx) WERE captured by Wayback as summary.html only -- their electionsettings.json/sum.

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
      full flag: Election-night plateau NOT directly sourceable for 2016 — confirmed exhausted across all three numerator routes. (1) PRESS-RELEASE route (now checked): Sacramento County VRE issued NO morning-after 'semi-official/semi-final results' release stating a ballot total in 2016. The MediaRoom press-release archive (Wayback 20161122005718 of elections.saccounty.net/MediaRoom/Pages/PressReleases.aspx) shows the post-election cadence as releases dated Nov 10, Nov 14, Nov 16 ('Presidential General Election Update – Ballot Count Update to be Released on …'); the FIRST post-election release (NewsReleases/Pages/Ballot-Count-Update---11102016.aspx, earliest capture 20161116003641) carries NO numbers — its full body only states 'Registrar of Voters Jill LaVine will release the next update after 3:00 p.m. on Friday, November 11' and points readers to sacresults.e-cers.com / eresults.saccounty.net. (2) eresults.saccounty.net Hart 'SUMMARY REPORT' route: only two captures bracket this election — 20161107220729 (pre-election, Nov 7, zero/test run) and 20161112083512 (embeds the Friday-canvass Run Date 11/11/16 02:46 PM, PRECINCTS 1,267/1,267, BALLOTS CAST - TOTAL 385,520). No Nov 8-evening / Nov 9-morning capture. (3) sacresults.e-cers.com live app: the only election-window capture is the homepage 20161110162635, which shows 'Precincts Reporting: 1267/1267, Last Refresh 11/9/2016 1:10:20 PM' but the ballots-cast/turnout total loads via AJAX (resultsVoterTurnout.aspx) that Wayback did not archive until the canvass (11/13); NO e-cers turnout or contest sub-page (resultsVoterTurnout.aspx, resultsSW.aspx) was archived anywhere in the Nov 8-11 plateau window. The Friday 11/11 canvass figure 385,520 (= 66.96% of the 575,711 certified) is an UPPER BOUND, not the metric; the true election-night plateau would be lower and, by analogy to the clean 2012 presidential plateau (62.93%), was likely ~60-63%, but it is not directly sourceable, so null/none. FLAG for manual operator follow-up: the Sacramento Bee (McClatchy, curl/WebFetch-blocked) is the most likely place a published Nov 8-9 election-night ballots-cast figure could be recovered. Denominator = CA SoS Voter Participation Statistics by County, Sacramento Total Voters 575,711 (Precinct 203,114 + VBM 372,597).

## 4. Spot-check sample of machine-verified rows (trust but verify)

- [ ] **fresno-ca 2016-11-08** (spot-check)
      claimed: night ballots **177,183**, certified final **291,890**, share **60.7%**
      numerator URL: https://web.archive.org/web/20161112171743/http://www2.co.fresno.ca.us/2850/Results/Results20161108.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night PLATEAU = 177,183 ballots ('Registered Voters 437667 - Cards Cast 177183 40.48%', 'Num. Report Precinct 592 - Num. Reporting 592 100.00%'), from Fresno County's official GEMS 'Election Summary Report' headed 'Fresno County Unofficial Final Results ... 11/9/2016 1:42:19 AM' -- the LAST

- [ ] **madera-ca 2022-11-08** (spot-check)
      claimed: night ballots **21,951**, certified final **37,345**, share **58.78%**
      numerator URL: https://web.archive.org/web/20260627203522/https://results.enr.clarityelections.com/CA/Madera/116174/311779/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Numerator 21,951 = total Ballots Cast (Contests[0].BC) from the Madera County Clarity ENR election-night data version 311779 (results.enr.clarityelections.com/CA/Madera/116174/311779/json/sum.json), recovered from the LIVE Clarity CDN (immutable version-pinned data) and freshly archived to Wayback (

- [ ] **nevada-ca 2016-11-08** (spot-check)
      claimed: night ballots **34,728**, certified final **56,800**, share **61.14%**
      numerator URL: https://yubanet.com/regional/nevada-county-ballot-measures-fate-depends-on-remaining-absentee-ballots/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 34,728, the LAST election-night update. YubaNet's morning-after article (published Nov 9 2016 10:08 UTC) reporting the county's official cumulative election-night results on countywide Measure A: 'Measure A received 23,060 Yes votes, 68.99% of the 34,728 ballots counted as of tonight ... i

- [ ] **placer-ca 2014-11-04** (spot-check)
      claimed: night ballots **76,411**, certified final **115,547**, share **66.1%**
      numerator URL: https://web.archive.org/web/20141115000402/http://www.placerelections.com/election-night-results.aspx
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/2014-complete-sov.pdf
      look for: PLATEAU = 76,411 'Cards Cast', the registrar's GEMS 'SEMI-OFFICIAL ELECTION SUMMARY / Election Night Final' with all 369 of 369 precincts reporting (38.13% reg turnout). The report carries its OWN embedded data timestamp '11/05/14 00:36:57' (12:36 a.m. PT Nov 5, i.e. ~4.5 hrs after 8pm Nov 4 poll cl

- [ ] **san-diego-ca 2018-11-06** (spot-check)
      claimed: night ballots **536,734**, certified final **1,173,924**, share **45.72%**
      numerator URL: https://web.archive.org/web/20181107120607/https://www.livevoterturnout.com/SanDiego/LiveResults/en/Index_5.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report). San Diego's live ENR page (livevoterturnout.com/SanDiego/LiveResults/en/Index_5.html) carries an internal 'Website Updated' data timestamp. The only election-night-era Wayback capture, taken 11/7/2018 04:06 PST (Wayback ts 20181107120607), renders 'Websi

- [ ] **santa-clara-ca 2014-11-04** (spot-check)
      claimed: night ballots **251,620**, certified final **404,166**, share **62.26%**
      numerator URL: https://web.archive.org/web/20141106082527/http://results.enr.clarityelections.com/CA/Santa_Clara/54209/148095/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CEILING (next-day all-precincts report; true overnight plateau modestly lower and not archived). The overnight election-night versions of Clarity event 54209 (Web01 layout; lower version folders 143630, 144518, 147xxx) WERE captured by Wayback as summary.html only -- their electionsettings.json/sum.

