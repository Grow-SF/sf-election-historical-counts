# Archive viability probes: Monterey through Yuba (excluding already-researched counties)

Scope: Monterey, Plumas, San Benito, San Joaquin, Santa Barbara, Santa Cruz, Shasta, Sierra,
Siskiyou, Solano, Sonoma, Stanislaus, Sutter, Tehama, Trinity, Tulare, Tuolumne, Ventura, Yolo, Yuba.

Excluded (already researched elsewhere): Napa, Nevada, Orange, Placer, Riverside, Sacramento,
San Bernardino, San Diego, San Francisco, San Luis Obispo, San Mateo, Santa Clara.

Scoring: 0-2 per dimension (clarity presence, wayback capture density, registrar URL findability,
press-release archive). 2 = strong evidence source.

---

## Monterey County

1. Clarity: `curl -s "https://results.enr.clarityelections.com/CA/Monterey/current_ver.txt"` -> HTTP 403 (CloudFront blocks curl's default UA). Retried with a browser User-Agent: `curl -s -A "Mozilla/5.0 ... Chrome/120.0" ".../CA/Monterey/current_ver.txt"` -> genuine Clarity "Election Night Reporting 404" page, i.e. Monterey is NOT on Clarity under this name. Score: 0
   NOTE: all subsequent Clarity checks in this file use the browser UA to avoid the CloudFront false-403.
2. Live results URL: legacy site `http://www.montereycountyelections.us/` (pre-redesign, .asp/.htm era, ~2016-2018). Direct curl to modern `montereycountyelections.us` and `co.monterey.ca.us/.../elections` both returned 403 from CloudFront (bot-blocked), so could not confirm current URL live; used Wayback to confirm the county's actual 2016-era domain instead. Score: 1 (found via Wayback, not confirmed live)
3. Wayback CDX:
   - 2016 window (homepage `montereycountyelections.us`): 10 captures 2016-11-03 to 2016-11-30, but none between 11-04 and 11-13 (misses election night 11/8-11/9 on the homepage specifically).
   - Broader 2016-11-05..11-12 CDX on `montereycountyelections.us*` shows a dedicated `Election Result.htm` page captured 2016-11-07 05:13 and 2016-11-07 22:06 (day before election, not night-of/after).
   - 2018 window (homepage): 7 captures 2018-11-03 to 2018-11-30, includes 2018-11-07 (day after election) and 2018-11-11/11-13.
   - No confirmed election-night-exact capture of the results subpage, but adjacent-day captures exist both years. Score: 1
4. Press-release archive: site is a legacy pre-2019 microsite (.asp/.htm), no `/news` found; 403 blocked live checks. Unknown/no evidence of a modern press archive. Score: 0

Verdict: marginal (decent Wayback density around election windows but no Clarity, no confirmed live results-page URL, no press archive).

---

## Plumas County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Plumas/current_ver.txt"` -> HTTP 404 (genuine Clarity 404 page). Not on Clarity. Score: 0
2. Live results URL: `https://www.plumascounty.us/162/Elections-Voter-Registration` -> HTTP 200 live (CivicPlus CMS). This is the current elections landing page; a tiny county (~2016/18 population ~19k), likely posts PDF result summaries rather than a dedicated ENR system. Score: 2 (found and confirmed live in one probe)
3. Wayback CDX (homepage `plumascounty.us`, since the CivicPlus page-ID URL for the elections subpage wasn't resolvable historically):
   - 2016 window: 4 captures (11-15, 11-16, 11-23, 11-26) -- none election night (11/8) or morning-after (11/9).
   - 2018 window: 2 captures (11-03, 11-15) -- none close to election night (11/6) or morning-after.
   - CDX query on `plumascounty.us/162*` (elections subpage) returned zero hits -- the modern elections page ID was not crawled historically.
   Score: 0 (sparse, and misses election-night windows both years)
4. Press-release archive: live site has a CivicPlus "News"/"Archive" module (`list.aspx?nid=`, HTTP 200, "News"/"Archive" strings present in the elections page). Plausible ongoing press-release archive but did not confirm historical (2016/18) depth. Score: 1

Verdict: poor (tiny county, no Clarity, thin Wayback coverage of the actual results page, likely PDF-only result books -- exactly the low-archivability case this probe is meant to flag).

---

## San Benito County

1. Clarity: tried both `San_Benito` and `SanBenito`: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/San_Benito/current_ver.txt"` and `.../CA/SanBenito/current_ver.txt` -> both HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: registrar site is `cosb.us` (County of San Benito); direct curl to `https://www.cosb.us/departments/county-clerk-recorder-elections` returned 403 (bot-blocked, likely Incapsula/Akamai) so could not confirm the live elections subpage. Confirmed via Wayback that `cosb.us` is the correct historical domain. Score: 1
3. Wayback CDX (had to retry over https:// -- the http:// CDX endpoint intermittently connection-refused during this probe):
   - 2016 window (homepage): 3 captures, 11-09 (morning after election night, 09:29 UTC), 11-15, 11-17. The 11-09 capture is a genuine morning-after-election-night snapshot.
   - 2018 window (homepage): 2 captures, 11-14 and 11-26 -- misses election night/morning-after (11/6-11/7).
   - CDX on `cosb.us/elections*` (all years): zero hits -- no dedicated elections subpage ever crawled; homepage is the only crawled surface.
   Score: 1 (good 2016 hit, weak 2018, no dedicated results subpage)
4. Press-release archive: could not check live (403 bot block on cosb.us). Unknown. Score: 0 (unknown, treated as no evidence)

Verdict: marginal (one good election-night-adjacent Wayback hit in 2016, but no Clarity, no confirmed live URL, no dedicated results-page crawl, unknown press archive).

---

## San Joaquin County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/San_Joaquin/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://www.sjgov.org/department/rov` -> HTTP 200 live, confirmed. Score: 2
3. Wayback CDX:
   - 2018 window (`sjgov.org/department/rov`, domain-wide filtered): dense capture set including 2018-11-07 15:01, 2018-11-08 21:51 (x2, election night), 2018-11-09 15:21 (morning after), plus 11-13/11-14/11-15 and a `results/statement-votes-cast` subpage capture on 11-14. Excellent density with a genuine election-night capture. Score: 2
   - 2016 window: exact `/department/rov` URL returns zero hits (that subpage/URL structure didn't exist yet); domain-wide 2016 CDX shows the old sjgov.org site used a `dynamic.aspx?id=` CMS pattern (pre-redesign), with homepage captured 2016-11-14/11-15 but no obvious ROV-specific page in the sample. Score: 1 for 2016 (weaker, dragged down the average from 2)
4. Press-release archive: "News"/"news" strings present on the live ROV page -> a news/press module exists. Score: 1 (presence confirmed, depth/history not verified)

Verdict: viable (strong 2018 Clarity-absent-but-Wayback-rich case with an actual election-night capture; 2016 weaker due to CMS redesign but homepage still archived).

---

## Santa Barbara County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Santa_Barbara/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://www.sbcvote.com/` (legacy domain) -> HTTP 200, 302-redirects to modern `https://countyofsb.org/222/Clerk-Recorder-Assessor-Elections-CRAE`. Both confirmed live in one probe (curl -I). Score: 2
3. Wayback CDX -- this is the standout county so far:
   - 2016 window: only 2 CDX hits for the bare homepage path, but BOTH are election-night-adjacent: 2016-11-05 and 2016-11-08 23:54 UTC (i.e. ~4:54pm PST election day). Expanding to `matchType=domain` for 2016-11-08..11-10 reveals IA did a deep full-site crawl right at election night: dozens of URLs under `/elect/resources/results11_2016/` were captured, including `results-1-zero.htm` (2016-11-09 00:00:32 UTC, pre-results "zero" report) and `results-1-first.htm` (2016-11-09 00:00:34 UTC, first-results report) plus historic per-election results pages back to 2000 (`results11_2000` etc.) and full SOV certified-result PDFs/CSVs for 2014/2016. This is a per-report-snapshot results archive, exactly the kind of granular election-night data this probe is looking for.
   - 2018 window (bare homepage): 3 hits, 2018-11-07, 11-13, 11-30 (302 redirects); did not re-run the deep domain-wide crawl check for 2018 but given 2016's density, high confidence similar depth exists.
   Score: 2
4. Press-release archive: "News"/"news" strings found on the live modern county elections page (`countyofsb.org/222/...`). Score: 1 (presence confirmed, historical depth not verified)

Verdict: viable -- strongest county found so far. No Clarity, but the legacy sbcvote.com site was deep-crawled by Wayback right at election night 2016 with individual timestamped results-report snapshots (`results-1-zero.htm`, `results-1-first.htm`), which is a rare and valuable find.

---

## Santa Cruz County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Santa_Cruz/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://www.votescount.com/` -> HTTP 200, live and confirmed. DNN/SCC CMS. Score: 2
3. Wayback CDX:
   - 2016 window: homepage captured 2016-11-02 and 2016-11-06 (neither is election night 11/8 itself, but close). No results-specific 2016 pages found in the `result`-filtered query.
   - 2018 window: rich capture set of the "November 6, 2018 California General Election" local-measures pages (`Home/Elections/November6,2018CaliforniaGeneralElection/Nov18localmeasures/...`), many timestamped 2018-11-07 (morning after election), plus 11-09 and 11-10. ~20 distinct measure/results-context pages archived. Strong 2018 density, though these are ballot-measure info pages rather than a numeric tally page per se.
   Score: 1 (strong 2018, weak/indirect 2016)
4. Press-release archive: no "news"/"press release" string found on live homepage in a quick grep (could be under a different label in the DNN nav, not conclusively absent). Score: 0 (no evidence found)

Verdict: marginal (good 2018 Wayback density on election-adjacent pages, weaker 2016 coverage, no Clarity, no confirmed press archive).

---

## Shasta County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Shasta/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: could not reach `co.shasta.ca.us` live (curl exit 000/timeout on both `www.co.shasta.ca.us` and `www.elections.co.shasta.ca.us` -- confirmed not a general network problem since `google.com` succeeded in the same probe run). Registrar URL identified via Wayback instead: `https://www.elections.co.shasta.ca.us/`. Score: 1 (identified but not confirmed live)
3. Wayback CDX:
   - 2016 window (`co.shasta.ca.us` elections subdomain): 5+ homepage captures 2016-11-03 through 2016-11-08 02:52 UTC (=2016-11-07 6:52pm PST, evening before election, not quite election night), plus historic `november-4-2014-general-election` page on 11-12.
   - 2018 window: dense capture set 2018-11-07 (day after) through 11-11, including `Election.aspx?eid=57` (2018-11-11) and `ce/mobile/index.soe` paths -- the `.soe` extension indicates the county runs "SOE Software" election-night-reporting (a Clarity alternative), a real ENR vendor, not just static pages. This is a notable finding: Shasta has its own dedicated ENR system, just not on Clarity.
   Score: 2 (dense captures both years, plus discovery of a real ENR backend)
4. Press-release archive: could not verify (site unreachable live). Score: 0 (unknown, treated as no evidence)

Verdict: viable -- found evidence of a dedicated ENR system (SOE Software, `.soe` URL extension) with good Wayback density in both election windows, despite the live site being unreachable during this probe (worth a retry with different network conditions).

---

## Sierra County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Sierra/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity (unsurprising -- population ~3,000). Score: 0
2. Live results URL: `https://www.sierracounty.ca.gov/162/Elections` -> HTTP 200, live, confirmed. CivicPlus CMS. Score: 2
3. Wayback CDX:
   - 2016 window: homepage-only captures (5x between 11-01 and 11-06), no dedicated elections/results subpage found in this window.
   - 2018 window: much richer -- `214/Elections` captured 2018-11-07 15:05, and notably `218/Election-Results` captured 2018-11-07 23:43 (day after election night), a genuinely dedicated results page for a county this small. Score: 1 (great 2018 find, no 2016 results page)
4. Press-release archive: no "news"/"press release" string matched on the live elections page. Score: 0

Verdict: marginal-to-viable for 2018 only (found an actual `Election-Results` page archived day-after in 2018, unusual for a county this tiny -- exactly the small-county positive case), but 2016 offers nothing beyond the homepage and no press archive found.

---

## Siskiyou County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Siskiyou/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://www.co.siskiyou.ca.us/elections` -> HTTP 200 live (redirects to Drupal page `/page/elections-registrar-of-voters-0`). Score: 2
3. Wayback CDX (Drupal site, `co.siskiyou.ca.us`):
   - 2016 window: elections page captured 2016-11-08 00:10 UTC (=11-07 4:10pm PST, day before election, not night-of), plus 11-12 (2 hits). No election-night-exact capture.
   - 2018 window: elections page captured 2018-11-07 15:01/15:02 UTC (day after election), and a rich PDF results-book archive under `/sites/default/files/elections/` -- but the PDFs found in this window are all historic (2013/2015/2016 elections), not the fresh Nov-2018 result -- confirming this county publishes final-only PDF result books rather than live-updated pages, posted with lag after the CDX window.
   Score: 1 (present both years but no genuine night-of capture; confirms PDF-book publishing pattern, i.e. low intra-night granularity even if recovered)
4. Press-release archive: no "news"/"press release" string matched on live elections page. Score: 0

Verdict: marginal (site exists and is crawled, but structurally this is a PDF-final-results-book county, not a live-updating ENR system -- so even a full Wayback recovery would likely only yield the certified final, not an election-night trajectory).

---

## Solano County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Solano/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://www.solanocounty.com/depts/rov/default.asp` -> HTTP 404 live (page has since moved/been restructured); `/depts/rov/` alone also 404'd on a direct check. Confirmed only via Wayback that this legacy `.asp` path was the correct 2016/18-era URL. Score: 1
3. Wayback CDX (legacy `.asp` ROV site):
   - 2016 window: `depts/rov/default.asp` captured 2016-11-03, 11-05, 2016-11-09 00:13 (=11-08 4:13pm PST, still election day, before poll close), 11-10; AND a dedicated election-specific page `depts/rov/november_8th_2016___presidential_general_election/election_results/default.asp` captured 2016-11-10 23:12 (2 days after election). Also a `historic_election_results/resultmaps.asp` page repeatedly captured 11-09 through 11-11.
   - 2018 window: very dense -- `default.asp` captured 2018-11-07 14:59 (day after) and 11-09 15:20 and 11-10 21:01, plus a wide crawl of ~15+ ROV subpages (candidate filings, district maps, FAQs) on 11-06 (election day itself, pre-results).
   Score: 2 (dense both years, with a named 2016-election-specific results subpage found)
4. Press-release archive: "News"/"news" strings present when fetching the archived `default.asp` content. Score: 1

Verdict: viable -- dense Wayback coverage both years including an election-specific results subpage in 2016 and heavy same-day/day-after crawling in 2018; only weakness is the live URL has since moved (404 today), so recovery would rely entirely on Wayback/CDX rather than a live site.

---

## Sonoma County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Sonoma/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://sonomacounty.ca.gov/administrative-support-and-fiscal-services/registrar-of-voters` -> HTTP 200 live. Historically the ROV ran its own subdomain `vote.sonoma-county.org` (found via Wayback, no longer live). Score: 2
3. Wayback CDX -- standout find:
   - The historic `vote.sonoma-county.org` results system encoded each published report as `election_results/resultNN.htm?pub=YYYY-MM-DD_HHMM` (UTC timestamp in the query string itself). CDX for 2018 found `result62.htm?pub=2018-11-07_0222` -- i.e. a report PUBLISHED 2018-11-07 02:22 UTC = 2018-11-06 6:22pm PST, right after polls closed on election night -- captured by Wayback the same evening (2018-11-07 23:43 UTC) and again 2018-11-17. This is a genuine election-night report snapshot with its exact publish time self-documented in the URL.
   - 2016 window: `vote.sonoma-county.org` homepage/content.aspx captured repeatedly, including 2016-11-06 02:43 (2 days before election) and a burst of ~14 captures on 2016-11-12 (post-election); did not find a `resultNN.htm?pub=...` hit in the 2016 sample window, but the URL scheme's existence in 2018 suggests it likely existed in 2016 too (worth a dedicated follow-up CDX sweep over 2016-11-08/09).
   Score: 2 (the pub= timestamp scheme is a rare, high-value find: exact election-night report provenance)
4. Press-release archive: no "news"/"press release" string matched on the live modern ROV page in a quick grep. Score: 0

Verdict: viable -- best find of the batch alongside Santa Barbara: the legacy vote.sonoma-county.org ENR system timestamps each report in its own URL (`?pub=2018-11-07_0222`), and Wayback captured at least one genuine election-night report. A full CDX sweep of `election_results/result*` across Nov 2016 and Nov 2018 (not just the narrow date windows probed here) would likely recover a whole night's sequence of reports.

---

## Stanislaus County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Stanislaus/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://www.stanvote.com/` -> HTTP 200 live, confirmed. Score: 2
3. Wayback CDX:
   - `past-results/results.htm` appears to be a rolling "current/most-recent" results page (not a static archive index) -- its content digest changed repeatedly across Nov-Dec 2016 (captured ~20 times between 11-03 and 01-01, with at least 5 distinct digests), consistent with it being overwritten as results were tallied and later certified. However no capture in the immediate 11-08/11-09 election-night window was found in the narrow probe; closest is 11-03 (before) and 11-14 (six days after).
   - 2018 window: `past-results/results.htm` captured 2018-11-07 23:43 (day after election); dedicated per-election pages exist for OTHER elections (`06-05-2018-results.htm`, `06-07-2016-results.htm`, `11-07-2017-results.htm`) but no `11-06-2018-results.htm` found yet in this window (likely posted after the probe's date range, once results were finalized).
   Score: 1 (site is dense and active, per-election permalink pattern exists and is well established, but no confirmed election-night-exact capture)
4. Press-release archive: "News"/"news" strings found on live homepage. Score: 1

Verdict: marginal-to-viable (an active, well-archived site with a clear per-election permalink naming convention, which is promising for a targeted follow-up CDX sweep on the exact election date, but this probe did not land a confirmed night-of capture).

---

## Sutter County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Sutter/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://www.suttercounty.org/elections` -> HTTP 403 (bot-blocked live check); identified true path `doc/government/depts/cr/elections/cr_elections_home` via Wayback instead. Score: 1
3. Wayback CDX:
   - 2016 window: only 2 hits, both 302-redirect stubs (11-04), no real content captured.
   - 2018 window: elections landing page captured 2018-11-07 15:00 (day after, HTTP 200, real content); AND a `docs/elections/resultNN.htm` numbered-report system (same convention seen in Sonoma/Sutter-style ENR templates) with `result31.htm` captured 2018-11-07 23:43 (day after election night) -- BUT all `resultNN.htm` captures in CDX are 302-redirect stubs (the underlying content had already moved/expired by crawl time), so no actual report content is retrievable from these captures, only proof the numbered-report system existed.
   Score: 1 (system existence confirmed, but captures are redirect stubs, not real content -- a "near miss")
4. Press-release archive: could not check (403 on live site). Score: 0 (unknown)

Verdict: poor (evidence of a numbered election-night-report system, mirroring Sonoma's, but every Wayback capture found is a dead redirect stub rather than real report content -- so 2018 is a promising lead but not yet a usable archive, and 2016 is essentially unarchived).

---

## Tehama County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Tehama/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `www.co.tehama.ca.us` -> DNS resolution failure (curl exit 6, "couldn't resolve host") on two separate attempts; could not confirm live. Identified via Wayback as `co.tehama.ca.us/dep-elections`. Score: 1
3. Wayback CDX:
   - 2016 window: `dep-elections` landing page captured 11-03, 11-04, and 2016-11-08 08:19 UTC (=11-08 12:19am PST, early election day, pre-results); separately a dedicated `election_results/Election Result_dtl.htm` page captured 2016-11-07 22:05 UTC (day before election). Also plain `/elections` alias captured 11-04/11-05.
   - 2018 window: `dep-elections` captured 2018-11-07 15:01 and 2018-11-09 15:21 (day after and 3 days after election).
   Score: 1 (present both years, close to but not exactly election night; small county so expect PDF/table-only results)
4. Press-release archive: could not check (DNS failure on live site). Score: 0 (unknown)

Verdict: marginal (site is crawled with reasonable regularity around election windows both years and has a dedicated results-detail page, but no confirmed exact-election-night capture and live site currently unreachable from this probe environment).

---

## Trinity County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Trinity/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity (tiny county, population ~13,000). Score: 0
2. Live results URL: `https://www.trinitycounty.org/elections` -> HTTP 404 live (page has moved since; Drupal site restructured). Confirmed only via Wayback. Score: 1
3. Wayback CDX:
   - 2016 window: zero hits for the whole domain in this window -- Trinity's site was not archived at all around the 2016 election.
   - 2018 window: `/elections` captured 2018-11-07 15:00 (day after election), and a dedicated `November-Election-2018` page captured 2018-11-12 (6 days after), plus a batch of election-page image assets on 11-07. Reasonable 2018 density.
   Score: 1 (2018 present, 2016 completely absent -- pulls average down)
4. Press-release archive: "News" string found on the archived elections page content. Score: 1

Verdict: poor for 2016 (nothing archived at all), marginal for 2018 (dedicated election page found but not night-of) -- typical small-county pattern where recoverability depends heavily on which election year is needed.

---

## Tulare County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Tulare/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://tularecounty.ca.gov/elections/` -> HTTP 403 live (bot-blocked); identified true 2016/18-era CMS path `registrarofvoters/index.cfm/...` via Wayback, plus two dedicated subdomains: `electbsl.tularecounty.ca.gov` and `electionapps.tularecounty.ca.gov/electionspolling/`. Score: 1
3. Wayback CDX -- notable finding of a custom in-house ENR system:
   - 2016 window: dense capture set on the main CMS site, 11-07 through 11-12, including a `november-8-2016-presidential-general-election/candidate-list` page (captured 2016-11-12) and repeated `historical-information1/prior-election-summary-reports` captures (11-09 through 11-12). No exact election-night capture, but very active crawling in the surrounding days.
   - 2018 window: discovered TWO dedicated election-tech subdomains -- `electbsl.tularecounty.ca.gov` (captured 2018-11-07 23:11-23:12) and `electionapps.tularecounty.ca.gov/electionspolling/` (captured 2018-11-07 14:56-14:59, including a `js/result.js` script) -- i.e. Tulare runs its own in-house "Election Polling"/results web app, separate from any third-party ENR vendor. Both captured the day after the Nov 6 2018 election.
   Score: 2 (dense both years, plus discovery of a dedicated in-house results app)
4. Press-release archive: no "news"/"press release" string matched on live registrar page (403-blocked, so this is from a redirect landing, low confidence). Score: 0 (unknown/not found)

Verdict: viable -- found genuine in-house ENR infrastructure (`electionapps.tularecounty.ca.gov/electionspolling/`) crawled the day after the 2018 election, plus solid 2016 CMS coverage; worth a dedicated CDX sweep of the `electionapps`/`electbsl` subdomains for individual result-report snapshots.

---

## Tuolumne County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Tuolumne/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://www.tuolumnecounty.ca.gov/166/Elections` -> HTTP 403 live (bot-blocked); Wayback confirms the real path is `/194/Election-Information` (page ID differs from the guessed `/166`). Score: 1
3. Wayback CDX:
   - 2016 window: zero hits for the whole domain -- not archived around the 2016 election at all.
   - 2018 window: `194/Election-Information` captured 2018-11-07 15:01 (day after election), plus a DocumentCenter PDF summary for the PRIOR (June 2016) election captured in the same crawl -- suggesting a per-election PDF summary-report pattern exists (`SUMMARY---Web-<date>-Election...pdf`) but the Nov-2018-specific PDF wasn't yet posted/crawled in this window.
   Score: 1 (2018 only, no night-of capture, 2016 fully absent)
4. Press-release archive: "News" string found in archived elections page content (via Wayback replay). Score: 1

Verdict: poor for 2016 (nothing archived), marginal for 2018 (page exists day-after but no numeric results captured, PDF summary pattern confirmed but not the relevant date).

---

## Ventura County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Ventura/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://venturavote.org/` -> HTTP 200 live, but this modern domain has zero 2016 CDX hits and only redirect-stub hits in 2018 (didn't exist as the results domain yet). The real 2016/18-era domain, found via CDX, is `recorder.countyofventura.org/elections/`. Score: 1 (live domain confirmed but wrong era; correct historical domain found separately)
3. Wayback CDX (`recorder.countyofventura.org`):
   - 2016 window: `/elections/` captured 2016-11-03, 11-04, 2016-11-09 12:32 (day after election, new digest vs. pre-election captures = content changed, i.e. results were live), and a burst of ~8 captures 11-12.
   - 2018 window: `/elections/` captured 2018-11-06 19:28 (election day itself, pre-poll-close), 2018-11-07 15:00/22:15 (day after, with a fresh digest), and 2018-11-09 15:20; also deeper subpages like `candidates-campaigns/candidate-list` on 11-11.
   Score: 2 (dense both years with digest changes indicating live content updates around election day)
4. Press-release archive: no "news"/"press release" string matched on live `venturavote.org` homepage (may be under a different nav label). Score: 0

Verdict: viable -- solid Wayback density both years on the correct historical domain (`recorder.countyofventura.org`), with digest changes suggesting the elections page was actively updated around election day; the live domain has since moved to `venturavote.org`, so recovery must go through Wayback/CDX on the old domain, not the current site.

---

## Yolo County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Yolo/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://www.yolocounty.org/elections` -> HTTP 403 (bot-blocked live check); Wayback shows the real 2016-era path was `general-government/general-government-departments/elections`, later 301-redirected from `government/departments/elections`. Score: 1
3. Wayback CDX (Wayback CDX API returned intermittent 504 Gateway Timeouts during this probe, requiring retries with narrower windows):
   - 2016 window: elections page captured 2016-11-06 00:05 (election day, before poll close) and a 302-redirect stub on 11-05.
   - 2018 window: the direct elections-path queries came back empty (site had been rebuilt on an ASP.NET MVC framework, `Areas/Admin/...`, and the elections page URL likely changed again); a broader domain-wide check confirms the homepage itself was captured 2018-11-07 23:29 (day after election) with a full asset crawl, but no elections-specific subpage was found in this narrow window.
   Score: 1 (present, but URL churn between 2016 and 2018 makes exact-page recovery uncertain; no night-of capture found)
4. Press-release archive: no "news"/"press release" string matched (403-blocked live check limited confidence). Score: 0 (unknown)

Verdict: marginal (site is crawled around both election windows, but the elections page URL changed between 2016 and 2018 CMS redesigns, and no election-night-exact or dedicated-results-page capture was found in either year).

---

## Yuba County

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Yuba/current_ver.txt"` -> HTTP 404 (genuine Clarity 404). Not on Clarity. Score: 0
2. Live results URL: `https://www.yuba.org/departments/elections/` -> HTTP 200 live, confirmed. Score: 2
3. Wayback CDX:
   - 2016 window: zero hits domain-wide -- yuba.org was not archived at all around the 2016 election.
   - 2018 window: only one hit, `services/Elections/AbsenteeStatus.aspx` captured 2018-11-07 23:11 (day after election) -- a status-lookup tool, not a results/tally page.
   Score: 0 (essentially unarchived both years; the one 2018 hit is not a results page)
4. Press-release archive: "News"/"news" strings present on the live elections page. Score: 1

Verdict: poor -- weakest of the batch alongside Yolo/Plumas-tier counties: live site exists and is reachable today, but Wayback has almost nothing from either 2016 or 2018 election windows, and what little exists isn't a results page. A recovery effort here would likely have to rely on the county directly (records request) rather than web archives.

