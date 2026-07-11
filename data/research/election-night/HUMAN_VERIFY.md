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

- [ ] **mendocino-ca 2012-11-06** (numerator NOT_FOUND)
      claimed: night ballots **18,401**, certified final **36,080**, share **51.0%**
      numerator URL: https://theava.com/archives/62338
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: NULL PER RUNBOOK 5.1, on integration review (downgraded from the source dossier's proposed 'secondary, PLAUSIBLE' estimate). WAYBACK ROUTE EXHAUSTED: elections.htm CDX (co.mendocino.ca.us, 20121001-20130101) has a single pre-poll-close capture (20121106055757, Nov 5 9:57pm PST) whose live-results li
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2012-11-06
      controller verdict: PLAUSIBLE (maintainer-approved approximation; self-description consistent but no independent bracket/hold leg obtainable (RUNBOOK 8))

## 2. Secondary-confidence rows (weakest sourcing, read closely)

- [ ] **del-norte-ca 2012-11-06** (secondary confidence)
      claimed: night ballots **8,067**, certified final **8,879**, share **90.85%**
      numerator URL: https://web.archive.org/web/20121110102540/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Del Norte County: 100.0% precincts reporting, Ballots Cast 8,067, Last Report stamp 'Nov 7 12:20 a.m.' (First Report 'Nov 6 8:51 p.m.') at Wayback capture 20121110102540 (2012-11-10 10:25:40 UTC). SINGLE CAPTURE at 2012-11-10 10:25:40 UTC c
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2012-11-06
      controller verdict: PLAUSIBLE (CA SoS status-page single-capture bracket (RUNBOOK 8))

- [ ] **fresno-ca 2012-11-06** (secondary confidence)
      claimed: night ballots **160,466**, certified final **261,652**, share **61.33%**
      numerator URL: https://web.archive.org/web/20121110102540/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Fresno County: 100.0% precincts reporting, Ballots Cast 160,466, Last Report stamp 'Nov 7 2:38 a.m.' (First Report 'Nov 6 8:14 p.m.') at Wayback capture 20121110102540 (2012-11-10 10:25:40 UTC). SINGLE CAPTURE at 2012-11-10 10:25:40 UTC car
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2012-11-06
      controller verdict: PLAUSIBLE (CA SoS status-page single-capture bracket (RUNBOOK 8))

- [ ] **madera-ca 2012-11-06** (secondary confidence)
      claimed: night ballots **32,865**, certified final **40,325**, share **81.5%**
      numerator URL: https://web.archive.org/web/20121110102540/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Madera County: 100.0% precincts reporting, Ballots Cast 32,865, Last Report stamp 'Nov 6 11:01 p.m.' (First Report 'Nov 6 8:03 p.m.') at Wayback capture 20121110102540 (2012-11-10 10:25:40 UTC). SINGLE CAPTURE at 2012-11-10 10:25:40 UTC car
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2012-11-06
      controller verdict: PLAUSIBLE (CA SoS status-page single-capture bracket (RUNBOOK 8))

- [ ] **mendocino-ca 2012-11-06** (secondary confidence)
      claimed: night ballots **18,401**, certified final **36,080**, share **51.0%**
      numerator URL: https://theava.com/archives/62338
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: NULL PER RUNBOOK 5.1, on integration review (downgraded from the source dossier's proposed 'secondary, PLAUSIBLE' estimate). WAYBACK ROUTE EXHAUSTED: elections.htm CDX (co.mendocino.ca.us, 20121001-20130101) has a single pre-poll-close capture (20121106055757, Nov 5 9:57pm PST) whose live-results li
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2012-11-06
      controller verdict: PLAUSIBLE (maintainer-approved approximation; self-description consistent but no independent bracket/hold leg obtainable (RUNBOOK 8))

- [ ] **mendocino-ca 2014-11-04** (secondary confidence)
      claimed: night ballots **11,402**, certified final **25,017**, share **45.58%**
      numerator URL: https://theava.com/archives/36750
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: WAYBACK DEAD END: current.htm CDX for Nov 2014 has captures Nov 1 (pre-election stub) and Nov 4 17:35 UTC/9:35am PST (pre-poll-close stub), then jumps straight to Nov 30 (three captures ~8.5KB); the Nov 30 capture (20141130082444id_) already reads 'ELECTION SUMMARY REPORT ... FINAL OFFICIAL RESULTS 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2014-11-04
      controller verdict: CONFIRMED (county report self-describes (verbatim-quoted by news) + later Wayback capture of the same URL shows a materially higher, weeks-later count)

- [ ] **mendocino-ca 2018-06-05** (secondary confidence)
      claimed: night ballots **19,049**, certified final **22,896**, share **83.2%**
      numerator URL: https://web.archive.org/web/20180619011846/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Mendocino County: 100.0% precincts reporting, Ballots Cast 19,049, Last Report stamp 'Jun 6 3:57 a.m.' (First Report 'Jun 5 9:16 p.m.') at Wayback capture 20180619011846 (2018-06-19 01:18:46 UTC). SINGLE CAPTURE at 2018-06-19 01:18:46 UTC car
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2018-06-05
      controller verdict: PLAUSIBLE (CA SoS status-page single-capture bracket (RUNBOOK 8))

- [ ] **mendocino-ca 2024-11-05** (secondary confidence)
      claimed: night ballots **15,611**, certified final **39,837**, share **39.19%**
      numerator URL: https://web.archive.org/web/20241123041721/https://mendofever.com/2024/11/06/election-2024-voter-turnout-tight-races-and-early-results-in-mendocino-county/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: WAYBACK DEAD END (same pattern as 2022): outer CMS page (mendocinocounty.gov/.../current-election-results) CDX for Nov 2024 shows only 403s (Nov 1, Cloudflare-blocked even for the archiver) and a bare 301 (Nov 9) until the first working 200 capture on Nov 22. co.mendocino.ca.us/acr/cgi-bin/currentFR
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2024-11-05
      controller verdict: CONFIRMED (news source explicitly self-describes as election-night-tabulated + independent Wayback capture of the same county report series shows a materially higher, 8-days-later count)

- [ ] **placer-ca 2012-11-06** (secondary confidence)
      claimed: night ballots **127,593**, certified final **172,757**, share **73.86%**
      numerator URL: https://web.archive.org/web/20121110102540/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Placer County: 100.0% precincts reporting, Ballots Cast 127,593, Last Report stamp 'Nov 6 11:47 p.m.' (First Report 'Nov 6 8:04 p.m.') at Wayback capture 20121110102540 (2012-11-10 10:25:40 UTC). SINGLE CAPTURE at 2012-11-10 10:25:40 UTC ca
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2012-11-06
      controller verdict: PLAUSIBLE (CA SoS status-page single-capture bracket (RUNBOOK 8))

- [ ] **placer-ca 2018-11-06** (secondary confidence)
      claimed: night ballots **113,380**, certified final **177,725**, share **63.8%**
      numerator URL: https://web.archive.org/web/20181113195233/https://www.placerelections.com/election-night-results/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: 113,380 'Cards Cast', the registrar's GEMS 'SEMI-OFFICIAL ELECTION SUMMARY' with all 358 of 358 precincts reporting (48.98% reg turnout). CAVEAT ON PLATEAU: unlike 2014/2016 (whose embedded report data-stamps were ~12:30 a.m. election night), this report's OWN embedded data timestamp is '11/09/18 15
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2018-11-06
      controller verdict: REFUTED_AS_PLATEAU (page provably tracked the canvass)

- [ ] **santa-clara-ca 2012-06-05** (secondary confidence)
      claimed: night ballots **234,342**, certified final **292,713**, share **80.06%**
      numerator URL: https://web.archive.org/web/20120607192808/http://www.sccgov.org/elections/results/jun2012/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CEILING (next-day/canvass-mode value; true overnight plateau unarchived), comparable:false. Santa Clara's June 2012 primary predates its Clarity adoption (Clarity electionId 43231 = Nov 2012 general only); the county's legacy sccgov.org GEMS-style live-results page (http://www.sccgov.org/elections/r
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2012-06-05
      controller verdict: REFUTED_AS_PLATEAU (earliest archived capture of the only election-night channel (legacy pre-Clarity sccgov.org page) is already ~23h post-poll-close with precincts at 100% and a once-daily canvass cadence; kept only as a documented ceiling per RUNBOOK 5.2, comparable:false)

- [ ] **tehama-ca 2012-11-06** (secondary confidence)
      claimed: night ballots **17,559**, certified final **23,261**, share **75.49%**
      numerator URL: https://web.archive.org/web/20121110102540/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Tehama County: 100.0% precincts reporting, Ballots Cast 17,559, Last Report stamp 'Nov 7 12:37 a.m.' (First Report 'Nov 6 9:03 p.m.') at Wayback capture 20121110102540 (2012-11-10 10:25:40 UTC). SINGLE CAPTURE at 2012-11-10 10:25:40 UTC car
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for tehama-ca 2012-11-06
      controller verdict: PLAUSIBLE (CA SoS status-page single-capture bracket (RUNBOOK 8))

## 3. Blocked-source recoveries (need a real browser)

- [ ] **del-norte-ca 2018-06-05** (operator-flagged)
      claimed: night ballots **4,637**, certified final **5,472**, share **84.74%**
      numerator URL: https://drive.google.com/uc?export=download&id=1xrb3b2KmuaR0EhVysw--eKyjXANMzy6k
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = Release 4 of 6 in the county's numbered 2018 primary election-night PDF series, recovered LIVE from the county's public Google Drive 'Elections Postings (Archive)' folder, child folder 'June 5, 2018 Primary Election' (drive.google.com/drive/folders/1j_tx1oilfY7jlehwAx8Njwa7WH21-_CQ; a seco
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2018-06-05
      controller verdict: CONFIRMED (late-night internal timestamp (self-description leg), last of a numbered on-night release series before a 2-days-later report explicitly relabeled 'Update' at a higher count (bracket leg); front-page ballot figure disambiguated per the runbook's known Del Norte registered-voters/times-cast mislabel using the per-contest Times Cast cross-check)
      full flag: PLATEAU = Release 4 of 6 in the county's numbered 2018 primary election-night PDF series, recovered LIVE from the county's public Google Drive 'Elections Postings (Archive)' folder, child folder 'June 5, 2018 Primary Election' (drive.google.com/drive/folders/1j_tx1oilfY7jlehwAx8Njwa7WH21-_CQ; a second sibling folder in the archive root with a near-identical name holds only filing/candidate documents, not releases -- disambiguated by filename). PDF CreationDate metadata for the full series: Release 1 8:01:24 PM, Release 2 9:07:40 PM, Release 3 9:28:06 PM, Release 4 9:46:30 PM (all election night 6/5/2018), Release 5 CreationDate Thu Jun 7 11:01:30 AM (2 days later), Release 6 CreationDate Thu Jun 14 4:56:20 PM (9 days later, filename-suffixed 'Final Uncertified'). Release 4 front page reads 'TOTAL RESULT SUMMARY REPORT (UNOFFICIAL)', printed timestamp 6/5/2018 9:42:38 PM, 18/18 precincts (100%). RUNBOOK 7.5 mislabel pattern confirmed present (same as this county's own 2016-general row): front page prints 'Registered Voters: 4,637 of 14,151 (32.77%)' and a separate 'Ballots Cast: 9,284' -- the 9,284 figure is ballot CARDS (~2x, many-contest statewide primary), not voters; disambiguated via the per-contest Times Cast row (GOVERNOR contest, page 2: 'Times Cast ... Total 4,637/14,151 32.77%', an exact match to the front-page 'Registered Voters' field and its own printed percentage) -- 4,637 is the correct people-count and is used here, 9,284 is not. Bracket leg: Release 5, rendered, retitled 'COUNTYWIDE RESULT SUMMARY REPORT / 1st Update (6/7/2018) / (UNOFFICIAL)', printed timestamp 6/7/2018 10:58:12 AM (2 days later), 'Registered Voters' field up to 5,347/14,151 -- confirms Release 4 was the last report before the canvass resumed. Scanned Canon-photocopier PDF (Creator Canon iR-ADV C5240 PDF), no text layer (pdftotext empty, confirmed 2026-07-10); read visually via 150dpi pdftoppm render, recorded in render_verified.json. Arithmetic: 4,637/5,472 = 84.74%, close to this county's 2016-general (83.30%) and 2018-general (84.45%) shares, consistent with the small-rural-county 80-95% calibration band. Del Norte never adopted e-pollbooks or ASV (control county); vs_epollbook and vs_asv both n/a. FLAG for manual operator: the front-page ballot figure required resolving a ~2x mislabel (4,637 voters vs 9,284 ballot cards); please re-open the source PDF and confirm page 1's 'Registered Voters: 4,637 of 14,151 (32.77%)' line and page 2's Governor-contest 'Times Cast ... 4,637 / 14,151 32.77%' line both read as transcribed. Landed 2026-07-10 in the batch-1 primaries backfill from docs/research/pending-integration-2026-07-10/dossier-del-norte-ca-primaries.md Item 4.

- [ ] **fresno-ca 2018-11-06** (operator-flagged)
      claimed: night ballots **null (recover if possible)**, certified final **256,972**
      numerator URL: (none)
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Certified final 256,972 ballots cast (CA SoS; election-day 93,581 + VBM 163,391; 56.24% of 456,891 registered). Pre-adoption, precinct-based (last midterm before VCA/e-pollbook/ASV in 2020). Election-night PLATEAU not sourceable. Fresno's 2018 GEMS results were served on the co.fresno.ca.us results 
      full flag: Certified final 256,972 ballots cast (CA SoS; election-day 93,581 + VBM 163,391; 56.24% of 456,891 registered). Pre-adoption, precinct-based (last midterm before VCA/e-pollbook/ASV in 2020). Election-night PLATEAU not sourceable. Fresno's 2018 GEMS results were served on the co.fresno.ca.us results page (/departments/county-clerk-registrar-of-voters/election-information/election-results/2018-november-general-election-results) with an embedded GEMS 'Election Summary Report'; that page's earliest Wayback capture is 2018-11-28, and by then the embed already showed a CANVASS report ('Unofficial Results 11/21/18 14:49:05', Cards Cast 239,032 of 455,662, 100% of 640 precincts) -- a mid-canvass figure 15 days out, NOT the election-night plateau. No no-dash election-night frozen file (Results20181106.htm) and no www2/2850/Post/2018Nov6 summary report were archived. News proxies give only day-after running framings (ABC30 abc30.com/fresno-county-elections-ballots-counting-votes/4642191/ 'more than 100,000 ballots still need to be counted'; GV Wire 11/7/2018) and are now both curl- and WebFetch-blocked (gvwire.com returns 403; McClatchy Fresno Bee blocked) -- FLAG for manual operator browser follow-up. Null per definition. RE-RESEARCH ATTEMPT (2026-07-10, gap-triage): applied the curl-the-Wayback-archived-copy bypass (runbook 6.7) to both named leads instead of their live-blocked hosts. It works technically (both fetch cleanly), but both turn out to be day-after canvass framings, not election-night reports: ABC30's piece (Wayback 20211021010755) has dateModified 2018-11-08T04:57:12Z = Nov 7 8:57 PM PST (~29 hours post-poll-close) and states the next update is Friday 3pm (canvass cadence); GV Wire's 'A Quick Look at Fresno Voter Turnout' (Wayback 20221204193036) has datePublished 2018-11-10T01:49:07Z = Nov 9 5:49 PM PST (3 days post-election, 'still 77,000 ballots left to process'). A fresh WebSearch for a same-night article with a specific count surfaced no new candidate. The live current county results page (fresnocountyca.gov/.../2018-NOVEMBER-GENERAL-ELECTION-RESULTS) links only the FINAL gems-election-summary-report PDF, no election-night-dated report; a CDX sweep for the runbook 6.3 Fresno filename pattern on fresnocountyca.gov for Nov 2018 returns zero (expected, that domain did not exist until 2024; the period-correct host co.fresno.ca.us was already checked exhaustively above). No same-night ballot count found anywhere; per runbook 6.7 stopping here. Value remains null.

- [ ] **santa-clara-ca 2012-06-05** (operator-flagged)
      claimed: night ballots **234,342**, certified final **292,713**, share **80.06%**
      numerator URL: https://web.archive.org/web/20120607192808/http://www.sccgov.org/elections/results/jun2012/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CEILING (next-day/canvass-mode value; true overnight plateau unarchived), comparable:false. Santa Clara's June 2012 primary predates its Clarity adoption (Clarity electionId 43231 = Nov 2012 general only); the county's legacy sccgov.org GEMS-style live-results page (http://www.sccgov.org/elections/r
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2012-06-05
      controller verdict: REFUTED_AS_PLATEAU (earliest archived capture of the only election-night channel (legacy pre-Clarity sccgov.org page) is already ~23h post-poll-close with precincts at 100% and a once-daily canvass cadence; kept only as a documented ceiling per RUNBOOK 5.2, comparable:false)
      full flag: CEILING (next-day/canvass-mode value; true overnight plateau unarchived), comparable:false. Santa Clara's June 2012 primary predates its Clarity adoption (Clarity electionId 43231 = Nov 2012 general only); the county's legacy sccgov.org GEMS-style live-results page (http://www.sccgov.org/elections/results/jun2012/) was the only election-night channel. Earliest Wayback capture of that URL is 2012-06-07 12:28:08 PM PDT (no June 5-6 capture exists in CDX, narrow or wide window), internal 'Last Updated : 6/6/2012 7:02:03 PM' (~23h post poll-close), Completed Precincts 874 of 874 (100%), county-wide Registration & Turnout block: Vote by Mail 185,455 + Precinct 48,887 = 234,342 (31.03% of 755,117 registered). Subsequent captures (6/7 4:43:58 PM at Wayback ts 20120608222327; 6/8 4:21:51 PM at ts 20120609022555) show a once-daily afternoon-update cadence, confirming the page was already in canvass mode by the first crawl -- same signature this dataset treats as a next-day ceiling elsewhere (Riverside 2024, Placer 2018, this county's own pre-correction 2014 general). Certified final 292,713 ballots (CA SoS Voter Participation Statistics by County, 2012-primary: 55,518 poll + 237,195 VBM = 292,713; 38.76% of 755,117 registered). Ceiling pct = 234,342/292,713 = 80.06% (NOT the plateau -- true election-night share is lower). Pre-epollbook (adopted 2020); ASV never. FREEZE TEST (2026-07-10, retry log santa-clara-2012-06-retry.md): the ceiling classification was re-tested and CONFIRMED-as-a-ceiling; 234,342 is NOT a frozen night state -- the very next capture (20120608222327, internal 6/7 4:43:58 PM) reads 268,370, the next (20120609022555, 6/8 4:21:51 PM) 284,025, growing to the certified 292,713 which then froze July 3 - Dec 8 2012; VBM drove the growth (185,455 -> 237,195, +28%) while precinct barely moved (48,887 -> 55,518), i.e. 'Semi-Final' here is this county's generic in-progress-canvass label, not end-of-night language. A scaling estimate was COMPUTED BUT NOT ADOPTED: applying Santa Clara's own Nov-2012 night-plateau-to-canvass-start ratio (460,329/438,348 = 1.0501) in reverse to 234,342 gives an implied night plateau ~223,152 ballots ~76.24% of 292,713; both bias directions are non-negligible and offsetting (elapsed-time mismatch biases the estimate high; precinct-already-complete mismatch biases it low), so it is a rough central value only, not a bound. MAINTAINER DEFAULT is the 234,342/80.06% ceiling (comparable:false) pending final say; the ~223,152/76.24% scaling estimate is recorded here as the not-adopted alternative. FLAG for manual operator: a June 5-6 capture CDX may have missed (replay aliasing), and/or a San Jose Mercury News election-night quote via NewsBank, could yet upgrade this to a real plateau; neither attempted here.

## 4. Machine-confirmed rows (number is at the URL; plateau read still owed)

- [ ] **colusa-ca 2014-11-04** (plateau check)
      claimed: night ballots **3,628**, certified final **4,422**, share **82.04%**
      numerator URL: https://web.archive.org/web/20141105141649/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Colusa County: 100.0% precincts reporting, Ballots Cast 3,628, Last Report stamp 'Nov 4 10:00 p.m.' (First Report 'Nov 4 9:11 p.m.') at Wayback capture 20141105141649 (2014-11-05 14:16:49 UTC). SINGLE CAPTURE at 2014-11-05 14:16:49 UTC carr
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for colusa-ca 2014-11-04
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **colusa-ca 2016-11-08** (plateau check)
      claimed: night ballots **4,952**, certified final **6,814**, share **72.67%**
      numerator URL: https://web.archive.org/web/20161110185817/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Colusa County: 100.0% precincts reporting, Ballots Cast 4,952, Last Report stamp 'Nov 8 10:25 p.m.' (First Report 'Nov 8 9:10 p.m.') at Wayback capture 20161110185817 (2016-11-10 18:58:17 UTC). SINGLE CAPTURE at 2016-11-10 18:58:17 UTC carrie
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for colusa-ca 2016-11-08
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **colusa-ca 2022-06-07** (plateau check)
      claimed: night ballots **1,693**, certified final **3,593**, share **47.12%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Colusa County: 100.0% precincts reporting, Ballots Cast 1,693, Last Report stamp 'Jun 7 11:09 p.m.' (First Report 'Jun 7 8:51 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 1,693 r
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for colusa-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **colusa-ca 2022-11-08** (plateau check)
      claimed: night ballots **2,958**, certified final **5,617**, share **52.66%**
      numerator URL: https://web.archive.org/web/20221109072903/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Colusa County: 100.0% precincts reporting, Ballots Cast 2,958, Last Report stamp 'Nov 8 11:20 p.m.' (First Report 'Nov 8 9:15 p.m.') at Wayback capture 20221109072903 (2022-11-09 07:29:03 UTC). FROZEN: the identical Ballots Cast figure 2,958 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for colusa-ca 2022-11-08
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **colusa-ca 2024-03-05** (plateau check)
      claimed: night ballots **1,846**, certified final **3,788**, share **48.73%**
      numerator URL: https://web.archive.org/web/20240306063830/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Colusa County: 100.0% precincts reporting, Ballots Cast 1,846, Last Report stamp 'Mar 5 9:14 p.m.' (First Report 'Mar 5 8:52 p.m.') at Wayback capture 20240306063830 (2024-03-06 06:38:30 UTC). FROZEN: the identical Ballots Cast figure 1,846 re
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for colusa-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **colusa-ca 2024-11-05** (plateau check)
      claimed: night ballots **2,868**, certified final **7,122**, share **40.27%**
      numerator URL: https://web.archive.org/web/20241106065418/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Colusa County: 100.0% precincts reporting, Ballots Cast 2,868, Last Report stamp 'Nov 5 8:38 p.m.' (First Report 'Nov 5 8:38 p.m.') at Wayback capture 20241106065418 (2024-11-06 06:54:18 UTC). FROZEN: the identical Ballots Cast figure 2,868 r
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for colusa-ca 2024-11-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **del-norte-ca 2012-06-05** (plateau check)
      claimed: night ballots **4,820**, certified final **5,242**, share **91.95%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Del Norte County: 100.0% precincts reporting, Ballots Cast 4,820, Last Report stamp 'Jun 5 11:07 p.m.' (First Report 'Jun 5 8:30 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). FROZEN: the identical Ballots Cast figure 4
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **del-norte-ca 2014-06-03** (plateau check)
      claimed: night ballots **5,122**, certified final **5,950**, share **86.08%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Del Norte County: 100.0% precincts reporting, Ballots Cast 5,122, Last Report stamp 'Jun 3 10:14 p.m.' (First Report 'Jun 3 8:32 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). FROZEN: the identical Ballots Cast figure 5
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **del-norte-ca 2014-11-04** (plateau check)
      claimed: night ballots **6,539**, certified final **7,332**, share **89.18%**
      numerator URL: https://web.archive.org/web/20211102111036id_/https://425abd7a-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/elect/elections/election-results/november-4-2014-general-election/November%204%2C%202014%20General%20Election%20-%20Release%202.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PLATEAU = Release 2 of 3 in the county's numbered 2014 election-night PDF series (county's OLDER Google-Sites-hosted domain elections.co.del-norte.ca.us, site name 'elect', distinct from the co.del-norte.ca.us/'dnco' site used 2016-2020). Internal report footer timestamp 11/4/2014 10:05 PM, header '
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2014-11-04
      controller verdict: CONFIRMED (last surviving on-night release (provably the last of only 2 pre-Final releases per the county's own dated index page), still labeled Unofficial; next report 3 days later relabeled Final at the exact certified total)

- [ ] **del-norte-ca 2016-06-07** (plateau check)
      claimed: night ballots **5,020**, certified final **6,185**, share **81.16%**
      numerator URL: https://drive.google.com/uc?export=download&id=1Y1Kj4-IqXW5uEgZh6c206EsmNoj9pSEN
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = Release 3 of 5 in the county's numbered 2016 primary election-night PDF series, recovered LIVE (no Wayback needed) from the county's public Google Drive 'Elections Postings (Archive)' folder, child folder 'June 7, 2016 Primary Election Results' (drive.google.com/drive/folders/1nwgviB22IuQI
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2016-06-07
      controller verdict: CONFIRMED (self-titled 'Final Election Night Report / Unofficial Results', last of a numbered on-night release series (numbering does NOT equal plateau position here -- verified via each file's own CreationDate), next report 3 days later retitled 'Friday Report' at a higher count)

- [ ] **del-norte-ca 2016-11-08** (plateau check)
      claimed: night ballots **8,450**, certified final **9,790**, share **86.31%**
      numerator URL: https://web.archive.org/web/20161110185817/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = county's own numbered election-night release series, Release 4 of 6, self-labeled 'Unofficial Results / Election Night Final', internal page-header timestamp 11/8/2016 10:47:49 PM, 18 of 18 precincts (100.00%) reporting. Registered Voters 8,155 of 14,320 (56.95%). Series ran Release 1 (8:0
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2016-11-08
      controller verdict: CONFIRMED (CA SoS county-reporting-status page FENU-equivalent figure, frozen 5 days then jumping to the exact certified final; supersedes the county's own slightly-earlier Release 4 as the last election-night value fed to the state)

- [ ] **del-norte-ca 2018-11-06** (plateau check)
      claimed: night ballots **7,127**, certified final **8,439**, share **84.45%**
      numerator URL: https://web.archive.org/web/20201111052344id_/https://b012f97e-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/dnco/departments/clerk-recorder/elections/election-results/november-6-2018-general-election/November%206%2C%202018%20General%20Election%20Results%20-%20Release%204.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = Release 4 of 5 in the county's own numbered 2018 election-night PDF series, self-titled (exact document header) 'STATEWIDE GENERAL ELECTION / TUESDAY, NOVEMBER 6, 2018 / ELECTION NIGHT SUMMARY REPORT / ELECTION NIGHT FINAL REPORT (UNOFFICIAL RESULTS)', internal timestamp 11/6/2018 9:42:38 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2018-11-06
      controller verdict: CONFIRMED (document explicitly titled 'ELECTION NIGHT FINAL REPORT'; next report 3 days later explicitly retitled to note late VBM additions)

- [ ] **del-norte-ca 2022-06-07** (plateau check)
      claimed: night ballots **4,019**, certified final **5,989**, share **67.11%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Del Norte County: 100.0% precincts reporting, Ballots Cast 4,019, Last Report stamp 'Jun 7 10:25 p.m.' (First Report 'Jun 7 8:35 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 4,0
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **del-norte-ca 2022-11-08** (plateau check)
      claimed: night ballots **6,312**, certified final **8,450**, share **74.7%**
      numerator URL: https://drive.google.com/uc?export=download&id=131PTrk6-v_7MrZiAlLp8BzoQzysS97eu
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = Release 4 ('Report #3' header / '4th Report - 19 Precincts Reporting' subtitle) of 4 same-night numbered reports in the county's live Google Drive election-postings archive (same archive used for the 2024 row; folder 'November 8, 2022 General Election', id 1t5FEPXr-4Ub5a2ABa9ItGgZi06WBmxgd
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2022-11-08
      controller verdict: CONFIRMED (last of 4 same-night numbered reports (strictly increasing timestamps, all election night); next artifact ('Final Unofficial Report' / 5th Report) 6 days later at a much higher count)

- [ ] **del-norte-ca 2024-03-05** (plateau check)
      claimed: night ballots **3,285**, certified final **6,121**, share **53.67%**
      numerator URL: https://web.archive.org/web/20240306063830/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Del Norte County: 100.0% precincts reporting, Ballots Cast 3,285, Last Report stamp 'Mar 5 10:25 p.m.' (First Report 'Mar 5 8:28 p.m.') at Wayback capture 20240306063830 (2024-03-06 06:38:30 UTC). FROZEN: the identical Ballots Cast figure 3,2
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **del-norte-ca 2024-11-05** (plateau check)
      claimed: night ballots **6,719**, certified final **10,676**, share **62.94%**
      numerator URL: https://drive.google.com/uc?export=download&id=1U3HX1aB8Fim-Ca6_qL_EdSPliM8OHpYB
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = Release 3 of 6 in the county's numbered 2024 election-night PDF series, now hosted on a public Google Drive folder linked from the live Elections News page (successor to the pre-2020 Google-Sites attachment scheme; the numbering convention survived the CMS migration). Document explicitly s
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for del-norte-ca 2024-11-05
      controller verdict: CONFIRMED (document explicitly titled 'Election Night Report ... Final Report'; next release 3 days later retitled 'Update' at a much higher count)

- [ ] **fresno-ca 2012-06-05** (plateau check)
      claimed: night ballots **66,323**, certified final **113,975**, share **58.19%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Fresno County: 100.0% precincts reporting, Ballots Cast 66,323, Last Report stamp 'Jun 6 1:45 a.m.' (First Report 'Jun 5 8:09 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). SINGLE CAPTURE at 2012-06-08 22:26:55 UTC carr
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **fresno-ca 2014-06-03** (plateau check)
      claimed: night ballots **79,801**, certified final **107,805**, share **74.02%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Fresno County: 100.0% precincts reporting, Ballots Cast 79,801, Last Report stamp 'Jun 4 1:28 a.m.' (First Report 'Jun 3 8:15 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). SINGLE CAPTURE at 2014-06-06 20:55:10 UTC carr
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **fresno-ca 2014-11-04** (plateau check)
      claimed: night ballots **119,317**, certified final **163,420**, share **73.01%**
      numerator URL: https://web.archive.org/web/20141105141649/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Fresno County: 100.0% precincts reporting, Ballots Cast 119,317, Last Report stamp 'Nov 5 1:38 a.m.' (First Report 'Nov 4 8:00 p.m.') at Wayback capture 20141105141649 (2014-11-05 14:16:49 UTC). FROZEN: the identical Ballots Cast figure 119
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2014-11-04
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **fresno-ca 2016-11-08** (plateau check)
      claimed: night ballots **177,183**, certified final **291,890**, share **60.7%**
      numerator URL: https://web.archive.org/web/20161112171743/http://www2.co.fresno.ca.us/2850/Results/Results20161108.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night PLATEAU = 177,183 ballots ('Registered Voters 437667 - Cards Cast 177183 40.48%', 'Num. Report Precinct 592 - Num. Reporting 592 100.00%'), from Fresno County's official GEMS 'Election Summary Report' headed 'Fresno County Unofficial Final Results ... 11/9/2016 1:42:19 AM' -- the LAST
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2016-11-08
      controller verdict: CONFIRMED (frozen GEMS live page, held past night)

- [ ] **fresno-ca 2022-06-07** (plateau check)
      claimed: night ballots **76,241**, certified final **136,114**, share **56.01%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Fresno County: 100.0% precincts reporting, Ballots Cast 76,241, Last Report stamp 'Jun 7 11:00 p.m.' (First Report 'Jun 7 8:12 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 76,24
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **fresno-ca 2022-11-08** (plateau check)
      claimed: night ballots **126,440**, certified final **221,419**, share **57.1%**
      numerator URL: https://web.archive.org/web/20221109070432/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Fresno County: 100.0% precincts reporting, Ballots Cast 126,440, Last Report stamp 'Nov 8 10:56 p.m.' (First Report 'Nov 8 8:23 p.m.') at Wayback capture 20221109070432 (2022-11-09 07:04:32 UTC). FROZEN: the identical Ballots Cast figure 126,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2022-11-08
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **fresno-ca 2024-03-05** (plateau check)
      claimed: night ballots **82,242**, certified final **156,425**, share **52.58%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Fresno County: 100.0% precincts reporting, Ballots Cast 82,242, Last Report stamp 'Mar 6 12:58 a.m.' (First Report 'Mar 5 8:12 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 82,24
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **fresno-ca 2024-11-05** (plateau check)
      claimed: night ballots **206,372**, certified final **330,932**, share **62.36%**
      numerator URL: https://web.archive.org/web/20241107003627/https://www.fresnocountyca.gov/files/sharedassets/county/v/5/county-clerk-registrar-of-voters/1_election-results-page-sov-ssov/2024/november-5th-general-election/electionsummaryreportrpt_11_5_24_1231.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night PLATEAU = 206,372 ballots ('Voters Cast: 206,372 of 511,349', 40.36% of registered), from Fresno County's OFFICIAL 'Election Summary Report' dated/internally timestamped 11/6/2024 12:30:26 AM with Precincts Reported 478 of 478 (100.00%) -- the LAST election-night update (file election
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for fresno-ca 2024-11-05
      controller verdict: CONFIRMED (official county summary PDF, end of night)

- [ ] **lake-ca 2012-06-05** (plateau check)
      claimed: night ballots **10,427**, certified final **14,274**, share **73.05%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Lake County: 100.0% precincts reporting, Ballots Cast 10,427, Last Report stamp 'Jun 6 1:08 a.m.' (First Report 'Jun 5 9:46 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). FROZEN: the identical Ballots Cast figure 10,427
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **lake-ca 2012-11-06** (plateau check)
      claimed: night ballots **16,622**, certified final **23,685**, share **70.18%**
      numerator URL: https://web.archive.org/web/20121110034513/http://acm.co.lake.ca.us:80/elections/results/result24.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = county's own numbered results-report system (acm.co.lake.ca.us/elections/results/result24.htm, report #24 = the Nov 6 2012 Consolidated General per its index24.htm title block). Internal header: 'Preliminary Election Results as of 11/06/2012 at 11:59:41 PM' (self-described late-night times
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2012-11-06
      controller verdict: CONFIRMED (self-described late-night timestamp + later capture of same URL overwritten to the certified final)

- [ ] **lake-ca 2014-06-03** (plateau check)
      claimed: night ballots **9,703**, certified final **15,548**, share **62.41%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Lake County: 100.0% precincts reporting, Ballots Cast 9,703, Last Report stamp 'Jun 4 12:55 a.m.' (First Report 'Jun 3 8:59 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). FROZEN: the identical Ballots Cast figure 9,703 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **lake-ca 2014-11-04** (plateau check)
      claimed: night ballots **12,593**, certified final **18,061**, share **69.72%**
      numerator URL: https://web.archive.org/web/20141108050347/http://acm.co.lake.ca.us:80/elections/results/result27.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PLATEAU = county's own numbered results-report system (acm.co.lake.ca.us/elections/results/result27.htm, report #27 = Nov 4 2014 General per its index27.htm title block). Internal header: 'Election Results as of 11/05/2014 at 12:41:23 AM' (past-midnight, tail of election night). 'Completed Precincts
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2014-11-04
      controller verdict: CONFIRMED (self-described past-midnight timestamp + byte-identical later capture of same URL (digest match) three weeks after election night)

- [ ] **lake-ca 2016-06-07** (plateau check)
      claimed: night ballots **9,049**, certified final **16,712**, share **54.15%**
      numerator URL: https://web.archive.org/web/20160614032019/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Lake County: 100.0% precincts reporting, Ballots Cast 9,049, Last Report stamp 'Jun 8 2:11 a.m.' (First Report 'Jun 7 9:56 p.m.') at Wayback capture 20160614032019 (2016-06-14 03:20:19 UTC). FROZEN: the identical Ballots Cast figure 9,049 r
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2016-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **lake-ca 2016-11-08** (plateau check)
      claimed: night ballots **13,484**, certified final **25,085**, share **53.75%**
      numerator URL: https://web.archive.org/web/20161112110847/http://publicapps.lakecountyca.gov:80/elections/results/result30.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = county's own numbered results-report system, now hosted on publicapps.lakecountyca.gov (moved from acm.co.lake.ca.us between 2014 and 2016), report #30 = Nov 8 2016 Consolidated General. Internal header: 'Election Results as of 11/09/2016 at 12:49:48 AM', explicitly labeled 'PRELIMINARY RE
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2016-11-08
      controller verdict: CONFIRMED (self-described past-midnight 'PRELIMINARY RESULTS' timestamp + only later capture of same URL (6 weeks on, no intermediate captures) labeled 'FINAL RESULTS' at the certified total)

- [ ] **lake-ca 2018-06-05** (plateau check)
      claimed: night ballots **8,158**, certified final **14,119**, share **57.78%**
      numerator URL: https://web.archive.org/web/20180610025440id_/http://publicapps.lakecountyca.gov:80/elections/results/result35.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Lake County: 100.0% precincts reporting, Ballots Cast 8,158, Last Report stamp 'Jun 6 1:44 a.m.' (First Report 'Jun 5 9:07 p.m.') at Wayback capture 20180619011846 (2018-06-19 01:18:46 UTC). SINGLE CAPTURE at 2018-06-19 01:18:46 UTC carries th
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2018-06-05
      controller verdict: CONFIRMED (county's own numbered results-report system (result35.htm), self-labeled preliminary results at 100% precincts, same-URL overwritten to the exact certified total 5 weeks later (upgraded 2026-07-10 from the SoS status-page single-capture PLAUSIBLE read, retained as historical corroboration))

- [ ] **lake-ca 2018-11-06** (plateau check)
      claimed: night ballots **13,522**, certified final **21,465**, share **63.0%**
      numerator URL: https://web.archive.org/web/20181129033058/http://publicapps.lakecountyca.gov/elections/results/result37.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = county's own numbered results-report system (publicapps.lakecountyca.gov/elections/results/result37.htm, report #37 = Nov 6 2018 Statewide General per its index37.htm title block, confirmed by CDX). Internal header: 'Election Results as of 11/07/2018 at 12:14:30 AM', explicitly labeled 'PR
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2018-11-06
      controller verdict: PLAUSIBLE (self-described past-midnight 'PRELIMINARY RESULTS' timestamp; the only later observation is a single Wayback crawl (not a second independent capture) whose crawl date diverges from the page's own generation timestamp -- suggestive but not one of the section 8 non-circular legs)

- [ ] **lake-ca 2022-06-07** (plateau check)
      claimed: night ballots **4,562**, certified final **13,470**, share **33.87%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Lake County: 100.0% precincts reporting, Ballots Cast 4,562, Last Report stamp 'Jun 8 2:32 a.m.' (First Report 'Jun 7 9:34 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 4,562 recu
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **lake-ca 2022-11-08** (plateau check)
      claimed: night ballots **7,842**, certified final **20,362**, share **38.51%**
      numerator URL: https://web.archive.org/web/20230131164229/https://lakeconews.com/news/74153-registrar-of-voters-office-issues-preliminary-results-for-tuesday-s-general-election-canvass-process-to-begin
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = the LAST election-night preliminary report, per a Lake County News article (archived copy used; live lakeconews.com blocks both curl and WebFetch with HTTP 403) quoting the Registrar of Voters' office directly: 'By 1 a.m. Wednesday, Valadez's office had issued the last preliminary ballot c
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2022-11-08
      controller verdict: CONFIRMED (on-the-record registrar-office quote naming the number as the last preliminary count of election night, plus the number holding unchanged across two Wayback captures of the county's own results page 12+ days apart)

- [ ] **lake-ca 2024-03-05** (plateau check)
      claimed: night ballots **7,181**, certified final **15,626**, share **45.96%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Lake County: 100.0% precincts reporting, Ballots Cast 7,181, Last Report stamp 'Mar 6 2:01 a.m.' (First Report 'Mar 5 9:15 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 7,181 recu
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **lake-ca 2024-11-05** (plateau check)
      claimed: night ballots **7,960**, certified final **27,127**, share **29.34%**
      numerator URL: https://web.archive.org/web/20241210113951/https://lakeconews.com/news/80085-official-canvass-underway-thousands-of-ballots-still-to-be-counted
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = the last election-night preliminary report, per Lake County News ('Official canvass underway; thousands of ballots still to be counted', archived copy used; live lakeconews.com blocks both curl and WebFetch with HTTP 403): 'The Lake County Registrar of Voters Office has issued preliminary 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for lake-ca 2024-11-05
      controller verdict: CONFIRMED (on-the-record news report naming the number as the election-night preliminary count for all precincts, with an independent second-article snippet pinning the report to 4 a.m. the morning after election day; the alternative county-page capture was checked and explicitly rejected as already-canvass-contaminated)

- [ ] **los-angeles-ca 2012-06-05** (plateau check)
      claimed: night ballots **765,552**, certified final **973,274**, share **78.66%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Los Angeles County: 100.0% precincts reporting, Ballots Cast 765,552, Last Report stamp 'Jun 6 4:41 a.m.' (First Report 'Jun 5 8:13 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). SINGLE CAPTURE at 2012-06-08 22:26:55 UT
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **los-angeles-ca 2012-11-06** (plateau check)
      claimed: night ballots **2,368,283**, certified final **3,236,704**, share **73.17%**
      numerator URL: https://www.lavote.gov/Documents/News_Releases/11072012-055616.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau. LA County RR/CC 'Semi-Final Official Election Results' news release (Documents/News_Releases/11072012-055616.pdf, released ~5:56 AM Nov 7 2012): 'On Election Night a total of 2,368,283 ballots were counted' (448,470 vote-by-mail + 1,919,813 precinct; the RR/CC estimated 792
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2012-11-06
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **los-angeles-ca 2014-06-03** (plateau check)
      claimed: night ballots **636,186**, certified final **824,070**, share **77.2%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Los Angeles County: 100.0% precincts reporting, Ballots Cast 636,186, Last Report stamp 'Jun 4 3:07 a.m.' (First Report 'Jun 3 8:06 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). SINGLE CAPTURE at 2014-06-06 20:55:10 UT
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **los-angeles-ca 2014-11-04** (plateau check)
      claimed: night ballots **1,147,248**, certified final **1,518,835**, share **75.53%**
      numerator URL: https://www.lavote.gov/Documents/News_Releases/11052014.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PRIMARY official plateau (verified against the release PDF). LA County RR/CC (Dean Logan) 'Semi-Final Official Results Reported for the Nov. 4, 2014 General Election' (Documents/News_Releases/11052014.pdf, morning of Nov 5 2014): 'A total of 1,147,248 ballots were processed and counted, with 25.25% 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2014-11-04
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **los-angeles-ca 2016-06-07** (plateau check)
      claimed: night ballots **1,438,909**, certified final **2,026,068**, share **71.02%**
      numerator URL: https://www.lavote.gov/Documents/News_Releases/06072016_semi-official-results.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau. LA County RR/CC 'Semi-Final Official Results Reported for the June 7, 2016 Presidential Primary Election' release (Documents/News_Releases/06072016_semi-official-results.pdf, released June 8 2016): 'A total of 1,438,909 ballots were processed and counted, with 29.92% of eli
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2016-06-07
      controller verdict: CONFIRMED (RR/CC semi-final press release plus exact-arithmetic report-series bracket 3 days later)

- [ ] **los-angeles-ca 2016-11-08** (plateau check)
      claimed: night ballots **2,306,321**, certified final **3,544,115**, share **65.07%**
      numerator URL: https://www.lavote.gov/Documents/News_Releases/11082016-semi-official-results.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau (fills the prior null). LA County RR/CC semi-official results release (Documents/News_Releases/11082016-semi-official-results.pdf): announced semi-final official results for the Nov. 8 General Election, 'A total of 2,306,321 ballots were processed and counted, with 45.19% of
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2016-11-08
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **los-angeles-ca 2018-06-05** (plateau check)
      claimed: night ballots **952,633**, certified final **1,490,502**, share **63.91%**
      numerator URL: https://www.lavote.gov/docs/rrcc/news-releases/06052018_semi-official-results.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau. LA County RR/CC 'Semi-Official Results Announced for the Statewide Direct Primary Election' release (docs/rrcc/news-releases/06052018_semi-official-results.pdf, released June 6 2018): 'A total of 952,633 ballots were processed and counted, with 18.53% of eligible registered
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2018-06-05
      controller verdict: CONFIRMED (RR/CC semi-official press release plus exact-arithmetic report-series bracket 3 days later)

- [ ] **los-angeles-ca 2018-11-06** (plateau check)
      claimed: night ballots **1,975,855**, certified final **3,023,417**, share **65.35%**
      numerator URL: https://www.lavote.gov/docs/rrcc/news-releases/11062018_semi-official-results.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau (REPLACES the earlier derived lower-bound 2,038,417). LA County RR/CC semi-official results release (docs/rrcc/news-releases/11062018_semi-official-results.pdf): semi-official results for the Nov. 6 General Election, 'A total of 1,975,855 ballots were processed and counted, 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2018-11-06
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **los-angeles-ca 2022-06-07** (plateau check)
      claimed: night ballots **822,545**, certified final **1,620,593**, share **50.76%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Los Angeles County: 100.0% precincts reporting, Ballots Cast 822,545, Last Report stamp 'Jun 8 2:12 a.m.' (First Report 'Jun 7 8:28 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 8
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **los-angeles-ca 2022-11-08** (plateau check)
      claimed: night ballots **1,318,093**, certified final **2,456,701**, share **53.65%**
      numerator URL: https://www.lavote.gov/docs/rrcc/news-releases/11082022_semi-final-results.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau (verified against the canonical RR/CC release PDF; previously cited via the lacounty.gov blog). LA County RR/CC 'Semi-Final Results Announced for the 2022 General Election' (docs/rrcc/news-releases/11082022_semi-final-results.pdf): 'A total of 1,318,093 ballots were processe
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2022-11-08
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **los-angeles-ca 2024-03-05** (plateau check)
      claimed: night ballots **910,857**, certified final **1,641,715**, share **55.48%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Los Angeles County: 100.0% precincts reporting, Ballots Cast 910,857, Last Report stamp 'Mar 6 2:06 a.m.' (First Report 'Mar 5 8:44 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 9
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **los-angeles-ca 2024-11-05** (plateau check)
      claimed: night ballots **2,615,541**, certified final **3,793,106**, share **68.96%**
      numerator URL: https://content.lavote.gov/docs/rrcc/documents/11-11062024_pr-11052024_semi-final-results.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PRIMARY official plateau (confirms the earlier derivation EXACTLY). LA County RR/CC 'Semi-Final Results Announced for the 2024 General Election' (content.lavote.gov/docs/rrcc/documents/11-11062024_pr-11052024_semi-final-results.pdf, Nov 6 2024): 'A total of 2,615,541 ballots were processed and count
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for los-angeles-ca 2024-11-05
      controller verdict: CONFIRMED (RR/CC semi-final press release states the election-night total)

- [ ] **madera-ca 2012-06-05** (plateau check)
      claimed: night ballots **16,619**, certified final **20,538**, share **80.92%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Madera County: 100.0% precincts reporting, Ballots Cast 16,619, Last Report stamp 'Jun 5 11:20 p.m.' (First Report 'Jun 5 8:27 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). FROZEN: the identical Ballots Cast figure 16,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **madera-ca 2014-06-03** (plateau check)
      claimed: night ballots **15,719**, certified final **19,206**, share **81.84%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Madera County: 100.0% precincts reporting, Ballots Cast 15,719, Last Report stamp 'Jun 3 10:40 p.m.' (First Report 'Jun 3 8:00 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). FROZEN: the identical Ballots Cast figure 15,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **madera-ca 2014-11-04** (plateau check)
      claimed: night ballots **22,031**, certified final **27,370**, share **80.49%**
      numerator URL: https://web.archive.org/web/20141105141649/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Madera County: 100.0% precincts reporting, Ballots Cast 22,031, Last Report stamp 'Nov 4 11:03 p.m.' (First Report 'Nov 4 8:07 p.m.') at Wayback capture 20141105141649 (2014-11-05 14:16:49 UTC). FROZEN: the identical Ballots Cast figure 22,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2014-11-04
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **madera-ca 2016-06-07** (plateau check)
      claimed: night ballots **21,553**, certified final **26,941**, share **80.0%**
      numerator URL: https://web.archive.org/web/20160614032019/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Madera County: 100.0% precincts reporting, Ballots Cast 21,553, Last Report stamp 'Jun 7 11:20 p.m.' (First Report 'Jun 7 8:19 p.m.') at Wayback capture 20160614032019 (2016-06-14 03:20:19 UTC). FROZEN: the identical Ballots Cast figure 21,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2016-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **madera-ca 2016-11-08** (plateau check)
      claimed: night ballots **35,364**, certified final **44,186**, share **80.0%**
      numerator URL: https://web.archive.org/web/20161112115134/http://votemadera.com/results/Election33/HTML/resultsc33.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Numerator 35,364 = the election-night Semi-Final Official Canvass total from votemadera.com's static results page resultsc33.htm/result33.htm, header 'Election Results as of 11/08/2016 at 11:31:17 PM', 102 of 102 precincts completed: Precinct Ballots Cast 12,803 + Absentee Ballots Cast 22,561 = Tota
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2016-11-08
      controller verdict: CONFIRMED (static county results page, frozen)

- [ ] **madera-ca 2018-06-05** (plateau check)
      claimed: night ballots **18,258**, certified final **24,211**, share **75.41%**
      numerator URL: https://web.archive.org/web/20260710214438/https://results.enr.clarityelections.com/CA/Madera/75694/204457/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: UPGRADED (2026-07-10, backfill batch 2): numerator 18,258 = total Ballots Cast (Contests[0].BC) from Madera County's Clarity ENR election-night data version 204457 (results.enr.clarityelections.com/CA/Madera/75694/204457/json/sum.json), Madera's FIRST-EVER Clarity election (id 75694). websiteupdated
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2018-06-05
      controller verdict: CONFIRMED (UPGRADED (2026-07-10): Clarity version bracket, re-derived from CDN, supersedes the prior CA SoS single-capture PLAUSIBLE read)

- [ ] **madera-ca 2018-11-06** (plateau check)
      claimed: night ballots **28,159**, certified final **38,968**, share **72.26%**
      numerator URL: https://web.archive.org/web/20260627203408/https://results.enr.clarityelections.com/CA/Madera/92458/220349/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Numerator 28,159 = total Ballots Cast (Contests[0].BC) from the Madera County Clarity ENR election-night data version 220349 (results.enr.clarityelections.com/CA/Madera/92458/220349/json/sum.json), recovered from the LIVE Clarity CDN (immutable version-pinned data) and freshly archived to Wayback (s
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2018-11-06
      controller verdict: CONFIRMED (clarity version bracket, re-derived from CDN)

- [ ] **madera-ca 2022-06-07** (plateau check)
      claimed: night ballots **13,417**, certified final **24,810**, share **54.08%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Madera County: 100.0% precincts reporting, Ballots Cast 13,417, Last Report stamp 'Jun 7 11:09 p.m.' (First Report 'Jun 7 8:43 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 13,41
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **madera-ca 2022-11-08** (plateau check)
      claimed: night ballots **21,951**, certified final **37,345**, share **58.78%**
      numerator URL: https://web.archive.org/web/20260627203522/https://results.enr.clarityelections.com/CA/Madera/116174/311779/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Numerator 21,951 = total Ballots Cast (Contests[0].BC) from the Madera County Clarity ENR election-night data version 311779 (results.enr.clarityelections.com/CA/Madera/116174/311779/json/sum.json), recovered from the LIVE Clarity CDN (immutable version-pinned data) and freshly archived to Wayback (
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2022-11-08
      controller verdict: CONFIRMED (clarity version bracket, re-derived)

- [ ] **madera-ca 2024-03-05** (plateau check)
      claimed: night ballots **16,048**, certified final **27,609**, share **58.13%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Madera County: 100.0% precincts reporting, Ballots Cast 16,048, Last Report stamp 'Mar 5 10:32 p.m.' (First Report 'Mar 5 8:02 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 16,048
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **madera-ca 2024-11-05** (plateau check)
      claimed: night ballots **37,106**, certified final **55,329**, share **67.1%**
      numerator URL: https://web.archive.org/web/20241108001837/https://results.enr.clarityelections.com/CA/Madera/122832/353191/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Numerator 37,106 = total Ballots Cast (field BC) from the Madera County Clarity ENR election-night data version 353191 (results.enr.clarityelections.com/CA/Madera/122832/353191/json/sum.json), recovered via Wayback (snapshot 20241108001837). The version's electionsettings.json gives websiteupdatedat
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for madera-ca 2024-11-05
      controller verdict: CONFIRMED (clarity version bracket, re-derived)

- [ ] **mendocino-ca 2012-06-05** (plateau check)
      claimed: night ballots **13,485**, certified final **20,116**, share **67.04%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Mendocino County: 100.0% precincts reporting, Ballots Cast 13,485, Last Report stamp 'Jun 6 1:16 a.m.' (First Report 'Jun 5 8:46 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). FROZEN: the identical Ballots Cast figure 1
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **mendocino-ca 2014-06-03** (plateau check)
      claimed: night ballots **8,669**, certified final **16,420**, share **52.8%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Mendocino County: 100.0% precincts reporting, Ballots Cast 8,669, Last Report stamp 'Jun 4 1:29 a.m.' (First Report 'Jun 3 8:47 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). FROZEN: the identical Ballots Cast figure 8,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **mendocino-ca 2016-06-07** (plateau check)
      claimed: night ballots **11,320**, certified final **28,056**, share **40.35%**
      numerator URL: https://web.archive.org/web/20160614032019/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('CCU'-coded row), Mendocino County: 100.0% precincts reporting, Ballots Cast 11,320, Last Report stamp 'Jun 8 4:00 a.m.' (First Report 'Jun 7 9:02 p.m.') at Wayback capture 20160614032019 (2016-06-14 03:20:19 UTC). FROZEN: the identical Ballots Cast figure 11
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2016-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **mendocino-ca 2016-11-08** (plateau check)
      claimed: night ballots **12,032**, certified final **38,730**, share **31.07%**
      numerator URL: https://web.archive.org/web/20161113022000/http://www.co.mendocino.ca.us/acr/current.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = county's own 'ELECTION SUMMARY REPORT ... THIS IS THE FINAL ELECTION NIGHT REPORT' (curl id_ raw fetch of the archived /acr/current.htm 'Current Election Results' page, no gzip; plain HTML; re-verified 2026-07-10, both the FINAL label and 'Cards Cast 12032 23.58%' confirmed present in the 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2016-11-08
      controller verdict: CONFIRMED (county report self-describes + later capture same count)

- [ ] **mendocino-ca 2018-11-06** (plateau check)
      claimed: night ballots **15,819**, certified final **33,966**, share **46.57%**
      numerator URL: https://web.archive.org/web/20181107234314/https://www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = county's own 'Election Night Final Report' (found via the new mendocinocounty.org CMS page's embedded iframe src='//www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl', an OLD-domain CGI script the county kept running post-migration; curl id_ raw fetch, plain HTML, no gzip; re-verified 2026-0
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2018-11-06
      controller verdict: CONFIRMED (county report self-describes + next-captured state is weeks later and materially different)

- [ ] **mendocino-ca 2022-06-07** (plateau check)
      claimed: night ballots **3,864**, certified final **22,248**, share **17.37%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Mendocino County: 100.0% precincts reporting, Ballots Cast 3,864, Last Report stamp 'Jun 8 12:48 a.m.' (First Report 'Jun 7 8:45 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 3,8
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **mendocino-ca 2022-11-08** (plateau check)
      claimed: night ballots **12,597**, certified final **31,008**, share **40.62%**
      numerator URL: https://web.archive.org/web/20221109142729/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Mendocino County: 100.0% precincts reporting, Ballots Cast 12,597, Last Report stamp 'Nov 9 1:13 a.m.' (First Report 'Nov 8 8:49 p.m.') at Wayback capture 20221109142729 (2022-11-09 14:27:29 UTC). FROZEN: the identical Ballots Cast figure 12,5
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2022-11-08
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **mendocino-ca 2024-03-05** (plateau check)
      claimed: night ballots **7,418**, certified final **23,935**, share **30.99%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Mendocino County: 100.0% precincts reporting, Ballots Cast 7,418, Last Report stamp 'Mar 6 12:35 a.m.' (First Report 'Mar 5 8:30 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 7,41
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for mendocino-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **napa-ca 2012-06-05** (plateau check)
      claimed: night ballots **19,147**, certified final **29,305**, share **65.34%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Napa County: 100.0% precincts reporting, Ballots Cast 19,147, Last Report stamp 'Jun 5 11:03 p.m.' (First Report 'Jun 5 8:00 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). FROZEN: the identical Ballots Cast figure 19,14
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **napa-ca 2012-11-06** (plateau check)
      claimed: night ballots **32,715**, certified final **57,672**, share **56.73%**
      numerator URL: https://web.archive.org/web/20121208223758/http://www.countyofnapa.org/ElectionResults/20121106/20101102-1129PM_dtl.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = final-of-night report. County 'Unofficial Election Night Results' detail header reads 'Last Updated: November 6, 2012 11:29 PM (Last of the Night)'. Registration & Turnout block: Vote by Mail Turnout 26,846 + Election Day Turnout 5,869 = Total 32,715 (45.07% of 72,592 reg). Napa released A
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2012-11-06
      controller verdict: CONFIRMED (county report self-describes)

- [ ] **napa-ca 2014-06-03** (plateau check)
      claimed: night ballots **17,431**, certified final **28,179**, share **61.86%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Napa County: 100.0% precincts reporting, Ballots Cast 17,431, Last Report stamp 'Jun 3 11:43 p.m.' (First Report 'Jun 3 7:59 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). FROZEN: the identical Ballots Cast figure 17,43
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **napa-ca 2014-11-04** (plateau check)
      claimed: night ballots **19,515**, certified final **38,766**, share **50.34%**
      numerator URL: https://web.archive.org/web/20141105141649/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: BEST-AVAILABLE (10:30 PM report; the EXACT final-of-night report is permanently unrecoverable from Wayback). Napa's 11/4/2014 election-night reports ran 8:01 PM (20141104-2001) -> 10:30 PM (20141104-2230) -> 10:42 PM final (20141104-2242). RE-VERIFIED: the 10:42 PM final-of-night report's content fr
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2014-11-04
      controller verdict: CONFIRMED (CA SoS county-reporting-status page's Final Election Night Unofficial (FENU) figure, doubly bracket-confirmed (frozen 2 days, then a correctly-identified CCU jump))

- [ ] **napa-ca 2016-06-07** (plateau check)
      claimed: night ballots **20,427**, certified final **43,450**, share **47.01%**
      numerator URL: https://web.archive.org/web/20160614032019/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('CCU'-coded row), Napa County: 100.0% precincts reporting, Ballots Cast 20,427, Last Report stamp 'Jun 8 12:08 a.m.' (First Report 'Jun 7 8:00 p.m.') at Wayback capture 20160614032019 (2016-06-14 03:20:19 UTC). SINGLE CAPTURE at 2016-06-14 03:20:19 UTC carrie
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2016-06-07
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **napa-ca 2016-11-08** (plateau check)
      claimed: night ballots **34,108**, certified final **63,255**, share **53.92%**
      numerator URL: https://web.archive.org/web/20161218225536/http://www.countyofnapa.org/ElectionResults/20161108/20161108-2306.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = final-of-night report. County 'Election Summary Report' PDF 20161108-2306.pdf (filename ts = Nov 8 2016, 23:06 = 11:06 PM) is the LAST election-night report (next archived file is the Nov 16 canvass update 20161116-1635.pdf, then the Dec 5 certified Final). Header: 'Precincts Reported: 167
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2016-11-08
      controller verdict: CONFIRMED (county last-report title)

- [ ] **napa-ca 2018-06-05** (plateau check)
      claimed: night ballots **15,091**, certified final **37,525**, share **40.22%**
      numerator URL: https://www.napacounty.gov/DocumentCenter/View/8722/Final-Unofficial-Election-Night-Report---Primary-Election-06052018-1039pm-PDF
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: ROLLOUT ELECTION: Napa's first VCA / e-pollbook election (county-tech record epollbook.adopted_year=2018, first_election='2018-06'); vs_epollbook classed POST since vote centers/e-pollbooks were live for this entire election, not adopted after it (same convention already used for this county's 2018-
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2018-06-05
      controller verdict: CONFIRMED (rollout election; county's own report-series titling (last report still labeled 'Election Night' vs the 'POST-Election Night' series 3 days later) plus late-night internal timestamp plus a later capture showing the count had moved)

- [ ] **napa-ca 2018-11-06** (plateau check)
      claimed: night ballots **21,774**, certified final **57,132**, share **38.11%**
      numerator URL: https://www.napacounty.gov/DocumentCenter/View/10436/Last-Unofficial-Election-Night-Report-11-06-18-PDF
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 'LAST UNOFFICIAL ELECTION NIGHT REPORT' (napacounty.gov DocumentCenter View/10436, the last of First/Last pair published election night). 'Precincts Reported: 170 of 170 (100.00%)', 'Registered Voters: 21,774 of 78,135 (27.87%)', and per-contest 'Times Cast 21,774'. ('Ballots Cast: 43,611'
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2018-11-06
      controller verdict: CONFIRMED (county titled last-of-night series)

- [ ] **napa-ca 2022-06-07** (plateau check)
      claimed: night ballots **14,658**, certified final **36,285**, share **40.4%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Napa County: 100.0% precincts reporting, Ballots Cast 14,658, Last Report stamp 'Jun 7 11:08 p.m.' (First Report 'Jun 7 8:12 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 14,658 r
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **napa-ca 2022-11-08** (plateau check)
      claimed: night ballots **21,943**, certified final **50,788**, share **43.21%**
      numerator URL: https://www.napacounty.gov/DocumentCenter/View/26985/Last-Unofficial-Election-Night-Report-1046-PM-11822-PDF
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 'Last Unofficial Election Night Report' timestamped 10:46 PM (napacounty.gov DocumentCenter View/26985; the night's reports ran First 8:01 PM -> Second 9:50 PM -> Last 10:46 PM, then the Nov 14 4:19 PM '1st Post Election Night' canvass report View/26995). Header: 'Precincts Reported: 200 o
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2022-11-08
      controller verdict: CONFIRMED (county titled last-of-night series)

- [ ] **napa-ca 2024-03-05** (plateau check)
      claimed: night ballots **15,304**, certified final **37,878**, share **40.4%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Napa County: 100.0% precincts reporting, Ballots Cast 15,304, Last Report stamp 'Mar 5 11:34 p.m.' (First Report 'Mar 5 8:02 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 15,304 r
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **napa-ca 2024-11-05** (plateau check)
      claimed: night ballots **26,160**, certified final **66,634**, share **39.26%**
      numerator URL: https://www.napacounty.gov/DocumentCenter/View/34231/Last-Unofficial-Election-Night-Results-1235AM-11062024-PDF
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 'Last Unofficial Election Night Report' timestamped 12:35 AM Nov 6 (napacounty.gov DocumentCenter View/34231; the night's reports ran First 8:01 PM 22,504 -> Second 9:49 PM -> Third 11:45 PM -> Last 12:35 AM 26,160, monotonic, then the multi-day canvass). Header: 'Precincts Reported: 204 o
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for napa-ca 2024-11-05
      controller verdict: CONFIRMED (county titled last-of-night series)

- [ ] **nevada-ca 2012-06-05** (plateau check)
      claimed: night ballots **21,763**, certified final **31,333**, share **69.46%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Nevada County: 100.0% precincts reporting, Ballots Cast 21,763, Last Report stamp 'Jun 6 12:41 a.m.' (First Report 'Jun 5 9:13 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). SINGLE CAPTURE at 2012-06-08 22:26:55 UTC car
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **nevada-ca 2012-11-06** (plateau check)
      claimed: night ballots **31,275**, certified final **52,173**, share **59.94%**
      numerator URL: https://web.archive.org/web/20121112105530/http://yubanet.com:80/regional/Nevada-County-Election-Tally-Continues---Turnout-Is-Nearly-80-Mail-Ins-Top-16-000.php
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 31,275, the END-OF-ELECTION-NIGHT tabulation. Official Nevada County Elections Office release (Registrar Gregory Diaz / Assistant Registrar Gail Smith quoted), republished verbatim by YubaNet: 'On Tuesday, Election Day, workers in the election office tabulated a total of 31,275 votes by 1 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2012-11-06
      controller verdict: CONFIRMED (county release republished verbatim)

- [ ] **nevada-ca 2014-06-03** (plateau check)
      claimed: night ballots **17,752**, certified final **27,596**, share **64.33%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Nevada County: 100.0% precincts reporting, Ballots Cast 17,752, Last Report stamp 'Jun 4 12:23 a.m.' (First Report 'Jun 3 8:49 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). FROZEN: the identical Ballots Cast figure 17,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **nevada-ca 2014-11-04** (plateau check)
      claimed: night ballots **22,366**, certified final **39,629**, share **56.44%**
      numerator URL: https://web.archive.org/web/20141108075409/http://yubanet.com:80/regional/Many-Nevada-County-races-too-close-to-call.php
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PLATEAU = 22,366, the FINAL election-night cumulative. YubaNet's 'Many Nevada County races too close to call' (Nov 5 2014) republished the county's official final election-night report: 'The final election night tally of votes comes in at 22,366 of 61,706 - a rather low voter turnout of 36.25%' (61,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2014-11-04
      controller verdict: CONFIRMED (morning-after report of the official night tally)

- [ ] **nevada-ca 2016-06-07** (plateau check)
      claimed: night ballots **27,852**, certified final **45,167**, share **61.66%**
      numerator URL: https://web.archive.org/web/20160614032019/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Nevada County: 100.0% precincts reporting, Ballots Cast 27,852, Last Report stamp 'Jun 8 12:08 a.m.' (First Report 'Jun 7 9:38 p.m.') at Wayback capture 20160614032019 (2016-06-14 03:20:19 UTC). SINGLE CAPTURE at 2016-06-14 03:20:19 UTC car
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2016-06-07
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **nevada-ca 2016-11-08** (plateau check)
      claimed: night ballots **34,728**, certified final **56,800**, share **61.14%**
      numerator URL: https://yubanet.com/regional/nevada-county-ballot-measures-fate-depends-on-remaining-absentee-ballots/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 34,728, the LAST election-night update. YubaNet's morning-after article (published Nov 9 2016 10:08 UTC) reporting the county's official cumulative election-night results on countywide Measure A: 'Measure A received 23,060 Yes votes, 68.99% of the 34,728 ballots counted as of tonight ... i
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2016-11-08
      controller verdict: CONFIRMED (morning-after report of the official cumulative)

- [ ] **nevada-ca 2018-06-05** (plateau check)
      claimed: night ballots **16,346**, certified final **38,792**, share **42.14%**
      numerator URL: https://yubanet.com/wp-content/uploads/2018/06/finalelectionnightupdate.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 16,346, the county's own 'Cumulative Report - Unofficial' for the June 5, 2018 primary, internal timestamp 11:06 PM, Precincts Reporting 39 of 39 = 100.00%. Posted by YubaNet's live-blog (yubanet.com/regional/june-2018-primary/) at its 11:23 PM entry captioned 'The final update for electio
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2018-06-05
      controller verdict: CONFIRMED (county's own last-of-night report, self-titled and time-stamped, plus a multi-day posting-schedule gap)

- [ ] **nevada-ca 2018-11-06** (plateau check)
      claimed: night ballots **26,956**, certified final **54,996**, share **49.01%**
      numerator URL: https://yubanet.com/regional/an-estimated-22000-ballots-remain-to-be-counted-in-nevada-county/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 26,956, the END-OF-ELECTION-NIGHT total stated by the county. YubaNet 'An estimated 22,000 ballots remain to be counted in Nevada County' (published Nov 7 2018 morning): 'NEVADA CITY, Calif. November 7, 2018 - At the end of election night, 26,956 ballots have been counted in Nevada County,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2018-11-06
      controller verdict: CONFIRMED (morning-after county statement)

- [ ] **nevada-ca 2022-06-07** (plateau check)
      claimed: night ballots **17,574**, certified final **37,990**, share **46.26%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Nevada County: 100.0% precincts reporting, Ballots Cast 17,574, Last Report stamp 'Jun 7 10:16 p.m.' (First Report 'Jun 7 8:16 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 17,574
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **nevada-ca 2022-11-08** (plateau check)
      claimed: night ballots **28,824**, certified final **51,370**, share **56.11%**
      numerator URL: https://yubanet.com/regional/election-day-is-over-whats-the-holdup-in-results/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 28,824, the end-of-election-night cumulative. YubaNet 'Election Day is over, what's the holdup on results?' (morning after, Nov 9 2022): 'For the November 8th election 74,225 vote by mail ballots were issued ... Last night, 38.83% of those ballots - 28,824 were counted. The first results o
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2022-11-08
      controller verdict: CONFIRMED (morning-after county explainer)

- [ ] **nevada-ca 2024-03-05** (plateau check)
      claimed: night ballots **21,753**, certified final **39,579**, share **54.96%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Nevada County: 100.0% precincts reporting, Ballots Cast 21,753, Last Report stamp 'Mar 6 12:08 a.m.' (First Report 'Mar 5 8:22 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 21,753
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **nevada-ca 2024-11-05** (plateau check)
      claimed: night ballots **15,486**, certified final **63,240**, share **24.49%**
      numerator URL: https://www.nevadacountyca.gov/DocumentCenter/View/55078/Third-Report-Cumulative-Results-11-5-2024-11-24-31-PM
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 15,486, CONFIRMED as the LAST of the three election-night reports. Source: Nevada County Elections' own official 'Third Report - Cumulative Results' PDF (DocumentCenter View/55078), Run Date 11/05/2024, Run Time 11:24 PM, Precincts Reporting 118 of 118 = 100.00%, Ballots Counted = 15,486 (
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for nevada-ca 2024-11-05
      controller verdict: CONFIRMED (county's own last-of-three night report)

- [ ] **orange-ca 2012-06-05** (plateau check)
      claimed: night ballots **315,584**, certified final **426,869**, share **73.93%**
      numerator URL: https://ocvote.gov/fileadmin/live/pri2012/run09/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). OCROV posted sequential 'UNOFFICIAL RESULTS CUMULATIVE TOTALS' runs (Presidential Primary Election, Tuesday June 5, 2012): run01 (Run Date/Time 06/05/2012 07:42:12 pm) = 0 of 1,976 precincts, VBM-only pre-count dump; the cou
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2012-06-05
      controller verdict: CONFIRMED (county report-series time-gap bracket (100% precincts, ~15.7-hour gap to next-day run))

- [ ] **orange-ca 2012-11-06** (plateau check)
      claimed: night ballots **862,544**, certified final **1,133,204**, share **76.12%**
      numerator URL: https://ocvote.gov/fileadmin/live/gen2012/Run09/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). OCROV posted sequential 'Cumulative Totals' runs every ~20-40 min through election night: Run 01 (Run Date/Time 11/06/2012 07:45:25 pm) = 385,929 ballots / 0 of 1,977 precincts = vote-by-mail-only first tranche; the count th
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2012-11-06
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **orange-ca 2014-06-03** (plateau check)
      claimed: night ballots **238,460**, certified final **340,187**, share **70.1%**
      numerator URL: https://ocvote.gov/fileadmin/live/pri2014/run10/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). OCROV posted sequential 'UNOFFICIAL RESULTS CUMULATIVE TOTALS' runs (Statewide Direct Primary Election, Tuesday June 3, 2014): run01 (Run Date/Time 06/03/2014 07:41:17 pm) = 151,033 ballots / 0 of 1,856 precincts = VBM-only 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2014-06-03
      controller verdict: CONFIRMED (county report-series time-gap bracket (100% precincts, ~15.1-hour gap to next-day run))

- [ ] **orange-ca 2014-11-04** (plateau check)
      claimed: night ballots **464,313**, certified final **640,358**, share **72.51%**
      numerator URL: https://ocvote.gov/fileadmin/live/gen2014/Run%2009/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Run 01 (Run Date/Time 11/04/2014 07:54:23 pm) = 250,187 ballots / 0 of 1,863 precincts = vote-by-mail-only first tranche; the count climbed and PLATEAUED at Run 09 (Run Date/Time 11/05/2014 01:55:59 am) = 464,313 ballots wit
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2014-11-04
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **orange-ca 2016-06-07** (plateau check)
      claimed: night ballots **477,064**, certified final **691,802**, share **68.96%**
      numerator URL: https://ocvote.gov/fileadmin/live/pri2016/Run%2010/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). OCROV posted sequential 'UNOFFICIAL RESULTS CUMULATIVE TOTALS' runs (Presidential Primary Election, Tuesday June 7, 2016): run01 (Run Date/Time 06/07/2016 07:49:11 pm) = 254,324 ballots / 0 of 1,597 precincts = VBM-only pre-
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2016-06-07
      controller verdict: CONFIRMED (county report-series time-gap bracket (100% precincts, ~14.75-hour gap to next-day run, exact reconciliation to certified))

- [ ] **orange-ca 2016-11-08** (plateau check)
      claimed: night ballots **825,317**, certified final **1,239,405**, share **66.59%**
      numerator URL: https://ocvote.gov/fileadmin/live/gen2016/Run%2011/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Run 01 (Run Date/Time 11/08/2016 08:03:32 pm) = 430,263 ballots / 0 of 1,668 precincts = vote-by-mail-only first tranche; the count climbed and PLATEAUED at Run 11 (Run Date/Time 11/09/2016 01:55:57 am) = 825,317 ballots wit
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2016-11-08
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **orange-ca 2018-06-05** (plateau check)
      claimed: night ballots **369,267**, certified final **635,224**, share **58.13%**
      numerator URL: https://ocvote.gov/fileadmin/live/pri2018/Run%2009/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). OCROV posted sequential 'UNOFFICIAL RESULTS CUMULATIVE TOTALS' runs (Statewide Direct Primary Election, Tuesday June 5, 2018): run01 (Run Date/Time 06/05/2018 07:57:34 pm) = 191,928 ballots / 0 of 1,561 precincts = VBM-only 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2018-06-05
      controller verdict: CONFIRMED (county report-series time-gap bracket (100% precincts, ~16.0-hour gap to next-day run), cross-checked against the 2018 general share)

- [ ] **orange-ca 2018-11-06** (plateau check)
      claimed: night ballots **650,671**, certified final **1,106,729**, share **58.79%**
      numerator URL: https://ocvote.gov/fileadmin/live/gen2018/Run_11/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Run 01 (Run Date/Time 11/06/2018 07:49:18 pm) = 362,079 ballots / 0 of 1,546 precincts = vote-by-mail-only first tranche; the count climbed and PLATEAUED at Run 11 (Run Date/Time 11/07/2018 01:48:27 am) = 650,671 ballots wit
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2018-11-06
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **orange-ca 2022-06-07** (plateau check)
      claimed: night ballots **325,774**, certified final **636,497**, share **51.18%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Orange County: 100.0% precincts reporting, Ballots Cast 325,774, Last Report stamp 'Jun 7 11:42 p.m.' (First Report 'Jun 7 8:24 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 325,7
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **orange-ca 2022-11-08** (plateau check)
      claimed: night ballots **611,060**, certified final **994,277**, share **61.46%**
      numerator URL: https://ocvote.gov/fileadmin/live/Gen2022/Run_08/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Vote-center era (precincts read 100% from Run 02 on, so the plateau is identified by the election-night/next-day TIME GAP, not precinct %). Run 01 (Run Time 8:00 PM, 11/08/2022) = 442,334 ballots = pre-Election-Day mail firs
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2022-11-08
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **orange-ca 2024-03-05** (plateau check)
      claimed: night ballots **400,430**, certified final **685,038**, share **58.45%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Orange County: 100.0% precincts reporting, Ballots Cast 400,430, Last Report stamp 'Mar 6 12:06 a.m.' (First Report 'Mar 5 8:28 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 400,4
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **orange-ca 2024-11-05** (plateau check)
      claimed: night ballots **1,007,150**, certified final **1,417,397**, share **71.06%**
      numerator URL: https://ocvote.gov/fileadmin/live/GEN2024/Run_09/cumulative.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Vote-center era (precincts read 100% from Run 02 on, so the plateau is identified by the election-night/next-day TIME GAP, not precinct %). Run 01 (Run Time 8:00 PM, 11/05/2024) = 718,019 ballots = pre-Election-Day mail firs
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for orange-ca 2024-11-05
      controller verdict: CONFIRMED (county-archived night report with past-midnight stamp)

- [ ] **placer-ca 2012-06-05** (plateau check)
      claimed: night ballots **62,087**, certified final **89,019**, share **69.75%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Placer County: 100.0% precincts reporting, Ballots Cast 62,087, Last Report stamp 'Jun 6 12:42 a.m.' (First Report 'Jun 5 8:40 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). FROZEN: the identical Ballots Cast figure 62,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **placer-ca 2014-06-03** (plateau check)
      claimed: night ballots **47,986**, certified final **70,016**, share **68.54%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Placer County: 100.0% precincts reporting, Ballots Cast 47,986, Last Report stamp 'Jun 4 2:06 a.m.' (First Report 'Jun 3 9:14 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). FROZEN: the identical Ballots Cast figure 47,9
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **placer-ca 2014-11-04** (plateau check)
      claimed: night ballots **76,411**, certified final **115,547**, share **66.1%**
      numerator URL: https://web.archive.org/web/20141115000402/http://www.placerelections.com/election-night-results.aspx
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/2014-complete-sov.pdf
      look for: PLATEAU = 76,411 'Cards Cast', the registrar's GEMS 'SEMI-OFFICIAL ELECTION SUMMARY / Election Night Final' with all 369 of 369 precincts reporting (38.13% reg turnout). The report carries its OWN embedded data timestamp '11/05/14 00:36:57' (12:36 a.m. PT Nov 5, i.e. ~4.5 hrs after 8pm Nov 4 poll cl
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2014-11-04
      controller verdict: CONFIRMED (GEMS night-final report)

- [ ] **placer-ca 2016-06-07** (plateau check)
      claimed: night ballots **71,358**, certified final **115,266**, share **61.91%**
      numerator URL: https://web.archive.org/web/20160614032019/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Placer County: 100.0% precincts reporting, Ballots Cast 71,358, Last Report stamp 'Jun 8 2:27 a.m.' (First Report 'Jun 7 9:48 p.m.') at Wayback capture 20160614032019 (2016-06-14 03:20:19 UTC). FROZEN: the identical Ballots Cast figure 71,3
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2016-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **placer-ca 2016-11-08** (plateau check)
      claimed: night ballots **109,666**, certified final **190,550**, share **57.55%**
      numerator URL: https://web.archive.org/web/20161113042955/http://www.placerelections.com/election-night-results.aspx
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = 109,666 'Cards Cast', the registrar's GEMS 'PLACER COUNTY SEMI-OFFICIAL ELECTION SUMMARY / November 8, 2016 / FINAL' with all 363 of 363 precincts reporting (48.43% reg turnout). The report carries its OWN embedded data timestamp '11/09/16 00:29:40' (12:29 a.m. PT Nov 9, ~4.5 hrs after 8pm
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2016-11-08
      controller verdict: CONFIRMED (GEMS night report)

- [ ] **placer-ca 2022-06-07** (plateau check)
      claimed: night ballots **39,433**, certified final **128,152**, share **30.77%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Placer County: 100.0% precincts reporting, Ballots Cast 39,433, Last Report stamp 'Jun 8 12:34 a.m.' (First Report 'Jun 7 8:02 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 39,43
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **placer-ca 2022-11-08** (plateau check)
      claimed: night ballots **65,224**, certified final **184,507**, share **35.35%**
      numerator URL: https://web.archive.org/web/20221109142729/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Placer County: 100.0% precincts reporting, Ballots Cast 65,224, Last Report stamp 'Nov 9 1:23 a.m.' (First Report 'Nov 8 8:05 p.m.') at Wayback capture 20221109142729 (2022-11-09 14:27:29 UTC). FROZEN: the identical Ballots Cast figure 65,224
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2022-11-08
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **placer-ca 2024-03-05** (plateau check)
      claimed: night ballots **69,436**, certified final **135,869**, share **51.11%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Placer County: 100.0% precincts reporting, Ballots Cast 69,436, Last Report stamp 'Mar 6 12:04 a.m.' (First Report 'Mar 5 8:02 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 69,436
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **placer-ca 2024-11-05** (plateau check)
      claimed: night ballots **165,535**, certified final **239,402**, share **69.15%**
      numerator URL: https://web.archive.org/web/20241106105347/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Placer County: 100.0% precincts reporting, Ballots Cast 165,535, Last Report stamp 'Nov 6 2:14 a.m.' (First Report 'Nov 5 8:04 p.m.') at Wayback capture 20241106105347 (2024-11-06 10:53:47 UTC). FROZEN: the identical Ballots Cast figure 165,53
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for placer-ca 2024-11-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **riverside-ca 2012-06-05** (plateau check)
      claimed: night ballots **189,087**, certified final **238,152**, share **79.4%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Riverside County: 100.0% precincts reporting, Ballots Cast 189,087, Last Report stamp 'Jun 6 1:42 a.m.' (First Report 'Jun 5 8:11 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). SINGLE CAPTURE at 2012-06-08 22:26:55 UTC 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **riverside-ca 2014-11-04** (plateau check)
      claimed: night ballots **265,771**, certified final **357,764**, share **74.29%**
      numerator URL: https://web.archive.org/web/20141105141649/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Riverside County: 100.0% precincts reporting, Ballots Cast 265,771, Last Report stamp 'Nov 5 2:26 a.m.' (First Report 'Nov 4 8:20 p.m.') at Wayback capture 20141105141649 (2014-11-05 14:16:49 UTC). SINGLE CAPTURE at 2014-11-05 14:16:49 UTC 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2014-11-04
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **riverside-ca 2016-06-07** (plateau check)
      claimed: night ballots **249,970**, certified final **403,828**, share **61.9%**
      numerator URL: https://web.archive.org/web/20160615020639/http://www.voteinfo.net:80/elections/20160607/eresults/Summary_Update8.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: Election-night plateau = 249,970 ballots ('Total Ballots Cast' countywide, Riverside County column) from the official Riverside Sequoia 'Official Semi-Final Results' report Summary_Update8.pdf, Run Date/Time 6/8/16 3:18:26 AM (the last-of-night report; posting cadence ~hourly from 8:02 PM through 3:
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2016-06-07
      controller verdict: CONFIRMED (self-labeled 'Official Semi-Final Results' report, last of a numbered on-night release series, next report 2 days later at a higher count)

- [ ] **riverside-ca 2016-11-08** (plateau check)
      claimed: night ballots **481,315**, certified final **769,193**, share **62.57%**
      numerator URL: https://web.archive.org/web/20161110185817/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Riverside County: 100.0% precincts reporting, Ballots Cast 481,315, Last Report stamp 'Nov 9 5:52 a.m.' (First Report 'Nov 8 8:31 p.m.') at Wayback capture 20161110185817 (2016-11-10 18:58:17 UTC). SINGLE CAPTURE at 2016-11-10 18:58:17 UTC ca
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2016-11-08
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **riverside-ca 2018-06-05** (plateau check)
      claimed: night ballots **193,152**, certified final **346,472**, share **55.75%**
      numerator URL: https://web.archive.org/web/20260710205406/https://docs.voteinfo.net/Elections/20180605/eresults/Summary8.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night plateau = 193,152 ballots ('Total Ballots Cast' countywide, Riverside County column) from the official Riverside Sequoia 'Official Semi-Final Results' report Summary8.pdf, Run Date/Time 6/6/18 6:25:10 AM. Wayback's own crawl of the eresults/ directory only preserved Summary12.pdf (alr
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2018-06-05
      controller verdict: CONFIRMED (self-labeled 'Official Semi-Final Results' report, last of a numbered on-night release series, next report 2 days later at a higher count)

- [ ] **riverside-ca 2022-06-07** (plateau check)
      claimed: night ballots **191,996**, certified final **375,610**, share **51.12%**
      numerator URL: https://web.archive.org/web/20260710205902/https://docs.voteinfo.net/Elections/20220607/docs/ElectionSummaryReportRPT6.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night plateau = 191,996 ballots ('Voters Cast: 191,996 of 1,304,447') from the official Riverside Dominion EMS 'Semi-Official Election Results' report ElectionSummaryReportRPT6.pdf, timestamp 6/8/2022 12:31:41 AM -- the first report to reach 795/795 (100.00%) precincts reported, i.e. electi
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2022-06-07
      controller verdict: CONFIRMED (self-labeled 'Semi-Official Election Results' report, first to reach 100% precincts reported, next report jumps to the following afternoon then settles into daily canvass cadence)

- [ ] **riverside-ca 2022-11-08** (plateau check)
      claimed: night ballots **205,813**, certified final **604,617**, share **34.0%**
      numerator URL: https://web.archive.org/web/20221109110809/https://www.voteinfo.net/Elections/20221108/docs/ElectionSummaryReportRPT_mhtml.htm
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night plateau = 205,813 ballots ('Voters Cast: 205,813 of 1,310,928 (15.70%)'; Governor Times Cast 205,813) from the official Riverside Dominion EMS 'Semi-Official Election Results' report, Last-Modified 11/09/2022 02:04 PST (the ~2 a.m. final election-night report, within the hourly-until-
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2022-11-08
      controller verdict: CONFIRMED (2 AM report held until the canvass)

- [ ] **riverside-ca 2024-03-05** (plateau check)
      claimed: night ballots **213,998**, certified final **409,269**, share **52.29%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Riverside County: 100.0% precincts reporting, Ballots Cast 213,998, Last Report stamp 'Mar 6 3:01 a.m.' (First Report 'Mar 5 8:30 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 213
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **riverside-ca 2024-11-05** (plateau check)
      claimed: night ballots **547,742**, certified final **959,098**, share **57.11%**
      numerator URL: https://web.archive.org/web/20241106133254/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: 611,101 'Ballots Counted' from the earliest Wayback capture of Riverside's livevoterturnout ENR, embedded timestamp 'Updated: 11/6/2024 5:35:21 PM' -- the FIRST daily canvass update (afternoon of the day after the Nov 5 election), NOT the ~3 a.m. election-night plateau. Riverside reports hourly unti
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for riverside-ca 2024-11-05
      controller verdict: CONFIRMED (CA SoS county-reporting-status page's ~5 a.m. overnight plateau, frozen 12+ hours across 3 captures before the next-day canvass bump)

- [ ] **sacramento-ca 2012-11-06** (plateau check)
      claimed: night ballots **328,516**, certified final **522,045**, share **62.93%**
      numerator URL: https://web.archive.org/web/20121109045323/http://www.eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, not the 8 p.m. first tranche). Sacramento County VRE posts a fixed-width Hart 'SUMMARY REPORT' on eresults.saccounty.net. The archived capture embeds the SEMI-OFFICIAL report, Run Date 11/07/12, Run Time 12:49 AM (just after midnight on election night), w
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2012-11-06
      controller verdict: PLAUSIBLE (distinct on-time capture exists but is currently unservable)

- [ ] **sacramento-ca 2014-06-03** (plateau check)
      claimed: night ballots **122,053**, certified final **203,850**, share **59.87%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Sacramento County: 100.0% precincts reporting, Ballots Cast 122,053, Last Report stamp 'Jun 4 12:11 a.m.' (First Report 'Jun 3 8:09 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). SINGLE CAPTURE at 2014-06-06 20:55:10 UT
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **sacramento-ca 2014-11-04** (plateau check)
      claimed: night ballots **195,317**, certified final **330,817**, share **59.04%**
      numerator URL: https://web.archive.org/web/20141106101214/http://www.eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, not the 8 p.m. first tranche). Archived eresults.saccounty.net capture embeds the Unofficial 'SUMMARY REPORT', Run Date 11/05/14, Run Time 12:33 AM (just after midnight on election night), with PRECINCTS COUNTED 1,263 of 1,263 (100%), BALLOTS CAST - TOTAL
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2014-11-04
      controller verdict: CONFIRMED (Hart summary with night run time, held)

- [ ] **sacramento-ca 2016-11-08** (plateau check)
      claimed: night ballots **328,744**, certified final **575,711**, share **57.1%**
      numerator URL: https://web.archive.org/web/20161110185817/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Sacramento County: 100.0% precincts reporting, Ballots Cast 328,744, Last Report stamp 'Nov 9 1:52 a.m.' (First Report 'Nov 8 8:07 p.m.') at Wayback capture 20161110185817 (2016-11-10 18:58:17 UTC). SINGLE CAPTURE at 2016-11-10 18:58:17 UTC c
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2016-11-08
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **sacramento-ca 2018-11-06** (plateau check)
      claimed: night ballots **185,623**, certified final **522,652**, share **35.52%**
      numerator URL: https://web.archive.org/web/20181107234429/https://eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report). First Voter's Choice Act / vote-center + e-pollbook general for Sacramento. The eresults.saccounty.net page now embeds an 'ElectionSummaryReportRPT'; the archived capture embeds the report stamped 11/7/2018 1:50:09 AM with Total Times Cast (ballots) 185,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2018-11-06
      controller verdict: CONFIRMED (night report held ~22 hours)

- [ ] **sacramento-ca 2022-06-07** (plateau check)
      claimed: night ballots **107,601**, certified final **336,014**, share **32.02%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Sacramento County: 100.0% precincts reporting, Ballots Cast 107,601, Last Report stamp 'Jun 8 12:16 a.m.' (First Report 'Jun 7 8:12 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 1
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **sacramento-ca 2022-11-08** (plateau check)
      claimed: night ballots **145,015**, certified final **484,315**, share **29.94%**
      numerator URL: https://web.archive.org/web/20221109091143/https://eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report). The archived eresults.saccounty.net capture embeds the ElectionSummaryReportRPT stamped 11/9/2022 12:00:20 AM (SEMI-FINAL) with Voters Cast 145,015 of 864,814 registered (16.77%). This midnight report is the final election-night report and is verified to
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2022-11-08
      controller verdict: CONFIRMED (county schedule plus midnight report)

- [ ] **sacramento-ca 2024-03-05** (plateau check)
      claimed: night ballots **118,205**, certified final **346,502**, share **34.11%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Sacramento County: 100.0% precincts reporting, Ballots Cast 118,205, Last Report stamp 'Mar 5 11:58 p.m.' (First Report 'Mar 5 8:12 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 1
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **sacramento-ca 2024-11-05** (plateau check)
      claimed: night ballots **311,821**, certified final **668,416**, share **46.65%**
      numerator URL: https://web.archive.org/web/20241106151727/https://eresults.saccounty.net/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report, not the 8:15 p.m. first tranche). The archived eresults.saccounty.net capture (taken 11/6 ~7:17 AM PT, the morning after) embeds the ElectionSummaryReportRPT stamped 11/6/2024 1:56:14 AM (SEMI-FINAL) with Voters Cast 311,821 of 889,465 registered (35.06%)
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for sacramento-ca 2024-11-05
      controller verdict: CONFIRMED (county schedule plus night report)

- [ ] **san-bernardino-ca 2014-11-04** (plateau check)
      claimed: night ballots **231,219**, certified final **293,283**, share **78.84%**
      numerator URL: https://web.archive.org/web/20141105141649/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), San Bernardino County: 100.0% precincts reporting, Ballots Cast 231,219, Last Report stamp 'Nov 5 1:50 a.m.' (First Report 'Nov 4 8:09 p.m.') at Wayback capture 20141105141649 (2014-11-05 14:16:49 UTC). SINGLE CAPTURE at 2014-11-05 14:16:49
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-bernardino-ca 2014-11-04
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **san-bernardino-ca 2016-11-08** (plateau check)
      claimed: night ballots **443,517**, certified final **672,871**, share **65.91%**
      numerator URL: https://web.archive.org/web/20161110185817/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), San Bernardino County: 100.0% precincts reporting, Ballots Cast 443,517, Last Report stamp 'Nov 9 4:56 a.m.' (First Report 'Nov 8 8:22 p.m.') at Wayback capture 20161110185817 (2016-11-10 18:58:17 UTC). SINGLE CAPTURE at 2016-11-10 18:58:17 U
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-bernardino-ca 2016-11-08
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **san-bernardino-ca 2022-06-07** (plateau check)
      claimed: night ballots **119,998**, certified final **257,580**, share **46.59%**
      numerator URL: https://web.archive.org/web/20220608230118/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), San Bernardino County: 100.0% precincts reporting, Ballots Cast 119,998, Last Report stamp 'Jun 8 3:16 a.m.' (First Report 'Jun 7 8:42 p.m.') at Wayback capture 20220608230118 (2022-06-08 23:01:18 UTC). SINGLE CAPTURE at 2022-06-08 23:01:18 U
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-bernardino-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **san-bernardino-ca 2024-03-05** (plateau check)
      claimed: night ballots **150,018**, certified final **305,853**, share **49.05%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), San Bernardino County: 100.0% precincts reporting, Ballots Cast 150,018, Last Report stamp 'Mar 6 1:48 a.m.' (First Report 'Mar 5 8:20 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figu
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-bernardino-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **san-bernardino-ca 2024-11-05** (plateau check)
      claimed: night ballots **434,108**, certified final **771,834**, share **56.24%**
      numerator URL: https://web.archive.org/web/20241106224114/https://elections.sbcounty.gov/elections/2024/1105/results/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night PLATEAU = 434,108 ballots ('Voters Cast: 434,108 of 1,198,556', 36.22% of registered) at Precincts Reported 2,872 of 2,872 (100.00%), from San Bernardino's OFFICIAL Clarity-style results page whose header reads literally 'Final Unofficial Election Night Results' with 'Next Update: Nov
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-bernardino-ca 2024-11-05
      controller verdict: CONFIRMED (county posting schedule brackets the capture)

- [ ] **san-diego-ca 2014-11-04** (plateau check)
      claimed: night ballots **509,214**, certified final **692,434**, share **73.54%**
      numerator URL: https://web.archive.org/web/20141105141649/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), San Diego County: 100.0% precincts reporting, Ballots Cast 509,214, Last Report stamp 'Nov 5 1:14 a.m.' (First Report 'Nov 4 8:03 p.m.') at Wayback capture 20141105141649 (2014-11-05 14:16:49 UTC). SINGLE CAPTURE at 2014-11-05 14:16:49 UTC 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-diego-ca 2014-11-04
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **san-diego-ca 2016-06-07** (plateau check)
      claimed: night ballots **468,340**, certified final **775,930**, share **60.36%**
      numerator URL: https://web.archive.org/web/20160608190823/http://www.sdvote.com/content/rov/electioninfo/election.xml
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric, recovered from the lead flagged in the 2016 GENERAL row's own note ('Wayback captured election.xml only for the June 2016 primary'). Pre-livevoterturnout era GEMS-style XML at sdvote.com/content/rov/electioninfo/election.xml (plain text, curl-fetched, no rendering needed). Only elect
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-diego-ca 2016-06-07
      controller verdict: CONFIRMED (self-describing overnight UNOFFICIAL report timestamp, plus growth in the next available capture 12 days later (the non-circular leg; a single-capture crawl-time-vs-data-time gap is noted but treated as weaker corroboration, not the primary basis))

- [ ] **san-diego-ca 2018-06-05** (plateau check)
      claimed: night ballots **406,501**, certified final **673,640**, share **60.34%**
      numerator URL: https://web.archive.org/web/20180606114855/http://www.livevoterturnout.com/SanDiego/LiveResults/en/Index_3.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric. San Diego's June 2018 primary is livevoterturnout.com/SanDiego/LiveResults/en/Index_3.html (Nov 2018 general = Index_5). Only election-night-window Wayback capture is 20180606114855 (4:48:55am PDT 6/6), which shows internal 'Website Updated: 6/6/2018 04:44:12 AM' and the page's own h
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-diego-ca 2018-06-05
      controller verdict: CONFIRMED (self-describing 'ELECTION NIGHT FINAL' header plus growth in the next capture)

- [ ] **san-diego-ca 2018-11-06** (plateau check)
      claimed: night ballots **536,734**, certified final **1,173,924**, share **45.72%**
      numerator URL: https://web.archive.org/web/20181107120607/https://www.livevoterturnout.com/SanDiego/LiveResults/en/Index_5.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report). San Diego's live ENR page (livevoterturnout.com/SanDiego/LiveResults/en/Index_5.html) carries an internal 'Website Updated' data timestamp. The only election-night-era Wayback capture, taken 11/7/2018 04:06 PST (Wayback ts 20181107120607), renders 'Websi
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-diego-ca 2018-11-06
      controller verdict: CONFIRMED (night stamp, captured the same night)

- [ ] **san-diego-ca 2022-06-07** (plateau check)
      claimed: night ballots **416,748**, certified final **674,608**, share **61.78%**
      numerator URL: https://web.archive.org/web/20220608181901/https://www.livevoterturnout.com/ENR/sandiegocaenr/15/en/Index_15.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric. ROLLOUT-TIMING: this is the FIRST election on SD's ENR/vote-center/e-pollbook platform (ElectionID 15; the Nov 2022 general, already CONFIRMED elsewhere in this file, is ElectionID 16, immediately next); data/research/county-tech/san-diego-ca.json independently confirms both epollboo
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-diego-ca 2022-06-07
      controller verdict: CONFIRMED (night stamp plus next-post schedule, corroborated by the companion XML feed's next report landing exactly on schedule)

- [ ] **san-diego-ca 2022-11-08** (plateau check)
      claimed: night ballots **565,982**, certified final **1,043,490**, share **54.24%**
      numerator URL: https://web.archive.org/web/20221109172128/https://www.livevoterturnout.com/ENR/sandiegocaenr/16/en/Index_16.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric (final election-night report). Vote-center / e-pollbook era; the ENR page shows 'Ballots Cast' with an internal 'Website Updated' data timestamp. Sequence from Wayback captures of Index_16.html: 11/8/2022 8:01:54 PM = 487,957 (first tranche, pre-Election-Day mail + early vote-center);
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-diego-ca 2022-11-08
      controller verdict: CONFIRMED (self-describing final plus next-post schedule)

- [ ] **san-diego-ca 2024-03-05** (plateau check)
      claimed: night ballots **425,572**, certified final **704,068**, share **60.44%**
      numerator URL: https://web.archive.org/web/20240306103630/https://www.livevoterturnout.com/ENR/sandiegocaenr/19/en/Index_19.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU metric, best-evidenced row in this dataset's primary set. ENR page Index_19.html (ElectionID 19, confirmed by its March 6 election-night captures and 'Presidential Primary Election' page title) literally headers itself 'FINAL UNOFFICIAL ELECTION NIGHT RESULTS' with internal 'Website Updated:
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-diego-ca 2024-03-05
      controller verdict: CONFIRMED (self-describing 'FINAL UNOFFICIAL ELECTION NIGHT RESULTS' header, held across three captures spanning 14h, plus the promised next-update landing exactly on schedule)

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

- [ ] **san-mateo-ca 2014-06-03** (plateau check)
      claimed: night ballots **70,651**, certified final **97,447**, share **72.5%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), San Mateo County: 100.0% precincts reporting, Ballots Cast 70,651, Last Report stamp 'Jun 3 11:30 p.m.' (First Report 'Jun 3 8:05 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). SINGLE CAPTURE at 2014-06-06 20:55:10 UTC 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-mateo-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

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

- [ ] **san-mateo-ca 2022-06-07** (plateau check)
      claimed: night ballots **63,362**, certified final **166,405**, share **38.08%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), San Mateo County: 100.0% precincts reporting, Ballots Cast 63,362, Last Report stamp 'Jun 8 1:06 a.m.' (First Report 'Jun 7 8:12 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 63,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-mateo-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **san-mateo-ca 2022-11-08** (plateau check)
      claimed: night ballots **122,135**, certified final **252,233**, share **48.42%**
      numerator URL: https://web.archive.org/web/20221109174232/https://www.livevoterturnout.com/ENR/sanmateocaenr/11/en/VRcqD_Index_11.html
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = Final Election Night Report (UPGRADED from prior null/bounded-proxy). Rendered archived San Mateo livevoterturnout ENR (index 11, file VRcqD_Index_11.html) capture 2022-11-09 17:42 UTC — identical across the 17:42 / 20:21 / 22:23 UTC Nov-9 captures — shows the banner 'SEMI-OFFICIAL RESULTS
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-mateo-ca 2022-11-08
      controller verdict: CONFIRMED (self-describing final plus next-update schedule)

- [ ] **san-mateo-ca 2024-03-05** (plateau check)
      claimed: night ballots **92,359**, certified final **174,122**, share **53.04%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), San Mateo County: 100.0% precincts reporting, Ballots Cast 92,359, Last Report stamp 'Mar 6 2:18 a.m.' (First Report 'Mar 5 8:24 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 92,
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for san-mateo-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

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

- [ ] **santa-clara-ca 2014-11-04** (plateau check)
      claimed: night ballots **235,062**, certified final **404,166**, share **58.16%**
      numerator URL: https://web.archive.org/web/20260710175200/https://results.enr.clarityelections.com/CA/Santa_Clara/54209/147908/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CEILING (next-day all-precincts report; true overnight plateau modestly lower and not archived). The overnight election-night versions of Clarity event 54209 (Web01 layout; lower version folders 143630, 144518, 147xxx) WERE captured by Wayback as summary.html only -- their electionsettings.json/sum.
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2014-11-04
      controller verdict: REFUTED_AND_CORRECTED (clarity live-CDN version walk recovers the true overnight plateau, superseding the documented ceiling)

- [ ] **santa-clara-ca 2016-11-08** (plateau check)
      claimed: night ballots **443,269**, certified final **724,596**, share **61.17%**
      numerator URL: https://web.archive.org/web/20260710174832/https://results.enr.clarityelections.com/CA/Santa_Clara/64404/182800/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
      look for: ELECTION-NIGHT PLATEAU NOT SOURCEABLE. Clarity event 64404 (Web01 layout): the only election-night-period capture is a pre-poll-close placeholder (version 178468, Wayback 20161107003316 = Nov 6 4:33 PM PT, Ballots Cast 0). The Nov 8 election-night data versions were never crawled; the next captures 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2016-11-08
      controller verdict: CONFIRMED (clarity live-CDN version bracket: cadence break in the immediately following version)

- [ ] **santa-clara-ca 2018-11-06** (plateau check)
      claimed: night ballots **304,303**, certified final **625,425**, share **48.66%**
      numerator URL: https://web.archive.org/web/20260710173809/https://results.enr.clarityelections.com/CA/Santa_Clara/92418/220444/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
      look for: ELECTION-NIGHT PLATEAU NOT SOURCEABLE. Clarity event 92418 (Web02 SPA): NO election-night (Nov 6-7 2018) data version was crawled; the earliest readable JSON is version 221262, sum.json GOVERNOR BC = 443,266 at 1,098/1,098 precincts, electionsettings '11/11/2018 4:43:32 PM PST' -- a DEEP CANVASS cou
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2018-11-06
      controller verdict: CONFIRMED (clarity live-CDN version bracket: adjacent official versions in the settings array, 9h22m gap)

- [ ] **santa-clara-ca 2022-06-07** (plateau check)
      claimed: night ballots **181,257**, certified final **357,848**, share **50.65%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Santa Clara County: 100.0% precincts reporting, Ballots Cast 181,257, Last Report stamp 'Jun 7 11:00 p.m.' (First Report 'Jun 7 8:28 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **santa-clara-ca 2022-11-08** (plateau check)
      claimed: night ballots **293,148**, certified final **550,602**, share **53.24%**
      numerator URL: https://web.archive.org/web/20221109173423/https://results.enr.clarityelections.com/CA/Santa_Clara/115971/311769/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = held election-night (overnight) level. Clarity event 115971 SPA: the Nov 8 election-night data JSON was not crawled, but the EARLIEST archived data version, 311769 (Wayback 20221109173423 = Nov 9 9:34 AM PT), is the held overnight plateau -- sum.json top contest GOVERNOR 'BC' (county-wide 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2022-11-08
      controller verdict: CONFIRMED (clarity version bracket, re-derived)

- [ ] **santa-clara-ca 2024-03-05** (plateau check)
      claimed: night ballots **182,413**, certified final **383,110**, share **47.61%**
      numerator URL: https://web.archive.org/web/20240306063830/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Santa Clara County: 100.0% precincts reporting, Ballots Cast 182,413, Last Report stamp 'Mar 5 10:26 p.m.' (First Report 'Mar 5 8:22 p.m.') at Wayback capture 20240306063830 (2024-03-06 06:38:30 UTC). FROZEN: the identical Ballots Cast figure 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **santa-clara-ca 2024-11-05** (plateau check)
      claimed: night ballots **460,325**, certified final **765,495**, share **60.13%**
      numerator URL: https://web.archive.org/web/20260702055736/https://results.enr.clarityelections.com/CA/Santa_Clara/122582/353227/json/sum.json
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: PLATEAU = held election-night (overnight) level. Clarity event 122582 SPA: the only archived data version is 353583 (Wayback 20241107034843 = Nov 6 7:48 PM PT), sum.json top contest PRESIDENT AND VICE PRESIDENT 'BC' (county-wide ballots cast; identical across all county-wide contests = total ballots
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for santa-clara-ca 2024-11-05
      controller verdict: REFUTED_AND_CORRECTED (clarity version walk recovers the true plateau)

- [ ] **tehama-ca 2012-06-05** (plateau check)
      claimed: night ballots **9,993**, certified final **13,968**, share **71.54%**
      numerator URL: https://web.archive.org/web/20120608222655/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('FENU'-coded row), Tehama County: 100.0% precincts reporting, Ballots Cast 9,993, Last Report stamp 'Jun 6 12:06 a.m.' (First Report 'Jun 5 8:07 p.m.') at Wayback capture 20120608222655 (2012-06-08 22:26:55 UTC). SINGLE CAPTURE at 2012-06-08 22:26:55 UTC carr
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for tehama-ca 2012-06-05
      controller verdict: CONFIRMED (CA SoS status-page single-capture-then-jump bracket (RUNBOOK 8))

- [ ] **tehama-ca 2014-06-03** (plateau check)
      claimed: night ballots **8,976**, certified final **13,016**, share **68.96%**
      numerator URL: https://web.archive.org/web/20140606205510/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('CCU'-coded row), Tehama County: 100.0% precincts reporting, Ballots Cast 8,976, Last Report stamp 'Jun 4 1:28 a.m.' (First Report 'Jun 3 8:25 p.m.') at Wayback capture 20140606205510 (2014-06-06 20:55:10 UTC). FROZEN: the identical Ballots Cast figure 8,976 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for tehama-ca 2014-06-03
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **tehama-ca 2014-11-04** (plateau check)
      claimed: night ballots **10,558**, certified final **15,791**, share **66.86%**
      numerator URL: https://web.archive.org/web/20141105141649/http://vote.sos.ca.gov/returns/status/
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('CCU'-coded row), Tehama County: 100.0% precincts reporting, Ballots Cast 10,558, Last Report stamp 'Nov 5 12:26 a.m.' (First Report 'Nov 4 8:26 p.m.') at Wayback capture 20141105141649 (2014-11-05 14:16:49 UTC). FROZEN: the identical Ballots Cast figure 10,5
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for tehama-ca 2014-11-04
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **tehama-ca 2022-06-07** (plateau check)
      claimed: night ballots **7,915**, certified final **14,178**, share **55.83%**
      numerator URL: https://web.archive.org/web/20220608094259/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('SF'-coded row), Tehama County: 100.0% precincts reporting, Ballots Cast 7,915, Last Report stamp 'Jun 7 11:41 p.m.' (First Report 'Jun 7 8:39 p.m.') at Wayback capture 20220608094259 (2022-06-08 09:42:59 UTC). FROZEN: the identical Ballots Cast figure 7,915 
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for tehama-ca 2022-06-07
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **tehama-ca 2022-11-08** (plateau check)
      claimed: night ballots **11,878**, certified final **20,819**, share **57.05%**
      numerator URL: https://web.archive.org/web/20221205014450id_/https://www.co.tehama.ca.us/wp-content/uploads/2022/11/ThirdUnofficialPrecinctReport.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night PLATEAU = 11,878 ballots ('Voters Cast: 11,878 of 37,115 (32.00%)'), from Tehama County's official 'Election Summary Report' internally timestamped 11/8/2022 10:37:39 PM -- the 'Third Unofficial Precinct Report' (the county's public numbering skips 'Second'; verified no Second-named f
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for tehama-ca 2022-11-08
      controller verdict: CONFIRMED (internal generation timestamp (10:37:39 PM) squarely inside the election-night window PLUS the county's own posting schedule brackets it: the next report in the series (Fourth) is dated 40 hours later with nothing interposed)

- [ ] **tehama-ca 2024-03-05** (plateau check)
      claimed: night ballots **7,998**, certified final **15,537**, share **51.48%**
      numerator URL: https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
      look for: CA SoS per-county reporting-status page ('U'-coded row), Tehama County: 100.0% precincts reporting, Ballots Cast 7,998, Last Report stamp 'Mar 5 11:34 p.m.' (First Report 'Mar 5 8:21 p.m.') at Wayback capture 20240306144409 (2024-03-06 14:44:09 UTC). FROZEN: the identical Ballots Cast figure 7,998 r
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for tehama-ca 2024-03-05
      controller verdict: CONFIRMED (CA SoS status-page frozen-capture bracket (RUNBOOK 8))

- [ ] **tehama-ca 2024-11-05** (plateau check)
      claimed: night ballots **13,109**, certified final **26,867**, share **48.79%**
      numerator URL: https://www.tehama.gov/wp-content/uploads/2024/11/3rd-Unoffical-Report.pdf
      denominator URL: https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
      look for: Election-night PLATEAU = 13,109 ballots ('Voters Cast: 13,109 of 37,488 (34.97%)', 'Precincts Reported: 40 of 40 (100.00%)'), from Tehama County's official 'Election Summary Report' internally timestamped 11/6/2024 12:17:11 AM -- the '3rd Unofficial Report', the LAST election-night update (all 40 pr
      your check: is this the LAST report posted on election night (the plateau)? full note: VERIFY.md detail bullet for tehama-ca 2024-11-05
      controller verdict: CONFIRMED (self-describes as end-of-night (3rd of 3 Unofficial Reports, 100.00% precincts, 12:17:11 AM internal timestamp) PLUS the county's own posting schedule brackets it: no 4th/5th/Final-Unofficial file exists anywhere (all guessed URLs 404), and the next file in the series (Final Official Report) is dated 27 days later with Voters Cast exactly equal to the certified final)

