# Archive viability probes: Alameda through Mono (excl. Fresno, Los Angeles, Madera)

Scores are 0-2 per dimension: Clarity presence / Wayback capture density / Registrar results-URL findability / Press-release archive.
Verdict: viable (evidenced, multiple recovery paths) / marginal (one path, gaps) / poor (little to nothing).

Note on methodology: `results.enr.clarityelections.com/CA/<County>/current_ver.txt` 404s at the
county-root level for every CA county (Clarity nests current_ver.txt under a numeric per-election
ID, e.g. `/CA/Butte/115760/current_ver.txt` -> `314320`). Adapted probe: check
`curl -A <browser-UA> -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/<County>/`
(200 = county has used Clarity at some point; 404 = never). CloudFront also 403s a bare curl with no
User-Agent, so a browser UA string is required on every Clarity request. CDX endpoint requires
https (plain http://web.archive.org/cdx/... returned connection errors); all queries below use https.

---

## Alameda

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Alameda/` -> 404 (also tried `/CA/Alameda/current_ver.txt` -> 404 "requested page not found"). No evidence Alameda ever used Clarity ENR.
2. Registrar URL: `curl -s -o /dev/null -w "%{http_code} %{url_effective}" -L https://www.acvote.org` -> 200, redirects to `https://acvote.alamedacountyca.gov/index` (current site). Historical (2016/2018-era) URL was `https://www.acgov.org/rov/`.
3. Wayback density: `curl "https://web.archive.org/cdx/search/cdx?url=acgov.org/rov&matchType=prefix&from=20161101&to=20161201&output=json&limit=10"` -> dense, multiple captures/day including **2016-11-08 13:32:01** (election day itself) and 2016-11-09/11-10 (canvass days). `...from=20181101&to=20181201...` -> dense captures through Nov 2018 including 2018-11-07 (day after election). Both windows show real 200-status HTML captures, not just revisits.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://acvote.alamedacountyca.gov/news` -> 404; no news/press link found via grep of homepage HTML (likely JS-rendered nav, not confirmed within probe budget).
Scores: Clarity 0 / Wayback 2 / Registrar-URL 2 / Press-release 0 (unconfirmed).
Verdict: **viable** — no Clarity, but the old acgov.org/rov URL has dense Wayback coverage bracketing both election nights, including a same-day 2016 capture.

---

## Alpine

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Alpine/` -> 404. No Clarity usage (expected for a ~1,200-registered-voter county — likely PDF-only results).
2. Registrar URL: found via web search (SOS county lookup / county site nav); `curl -o /dev/null -w "%{http_code}" -L "https://www.alpinecountyca.gov/index.aspx?NID=388"` -> 200 (elections page). (`/162/Elections` guess redirected to an unrelated page — wrong numeric ID.)
3. Wayback density: CDX on the exact elections URL for Nov 2016 -> several captures 2016-11-06 through 2016-11-22 (200 status, ~20-21KB pages, election week coverage). Same exact-URL query for Nov 2018 -> empty; broadened to the whole domain for Nov 2018 -> homepage (`/`) captured 2018-11-09 (day after election) but the specific NID=388 elections subpage was not captured that month.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" -L https://www.alpinecountyca.gov/162/News` -> 200 (a news page exists) but depth/vintage unconfirmed within probe budget.
Scores: Clarity 0 / Wayback 1 / Registrar-URL 2 / Press-release 1.
Verdict: **marginal** — homepage and elections page are both archived at least once per election cycle, but coverage is thin and county is small enough that granular precinct data may only ever have existed as a PDF, not a web page Wayback would capture well.

---

## Amador

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Amador/` -> 404. No Clarity usage.
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" -L https://www.amadorgov.org/172/Elections-Voter-Registration` -> 403 to plain curl (Cloudflare/bot-protection block; site itself is real — confirmed via CDX below and SOS listing). Current path is `amadorgov.org/government/elections`.
3. Wayback density: CDX on `amadorgov.org` filtered to elections-related paths for Nov 2016 -> multiple captures (calendar/news pages linking from `backlist=/government/elections`, 2016-11-12 through 2016-11-14). For Nov 2018 -> `amadorgov.org/government/elections` itself captured repeatedly, including **2018-11-07 15:05** (day after election), 200 status, ~26KB.
4. Press-release archive: direct curl to a guessed news path 403'd (Cloudflare), but CDX shows `amadorgov.org/about/county-news` captured repeatedly from 2018-02-21 through at least 2019-10-14 — a real, multi-year general county news archive (not elections-specific, but usable for corroboration).
Scores: Clarity 0 / Wayback 2 / Registrar-URL 1 (site confirmed real but blocks curl directly, needs browser/Wayback access) / Press-release 2.
Verdict: **viable** — Cloudflare blocks live scraping but Wayback has dense coverage of the actual elections page including the day-after-2018 capture, plus a genuine multi-year news archive.

---

## Butte

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Butte/` -> 200 (confirmed Clarity user). Root `current_ver.txt` 404s (expected — nests under election ID); found live numeric election IDs via search (e.g. `/CA/Butte/115760/current_ver.txt` -> `314320`, `/CA/Butte/113944/current_ver.txt` -> `298821`), both recent (2026-cycle) elections, not 2016/2018. CDX on `results.enr.clarityelections.com/CA/Butte` for Nov 2016 and Nov 2018 -> both empty (Clarity's own historical archive doesn't reach back that far, or Wayback never crawled it then).
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://www.buttecounty.net/1509/Voting-Elections` -> 200; also `https://buttevotes.net` -> redirects to `https://buttevotes.ca.gov/` -> 200 (dedicated Clerk-Recorder/elections domain).
3. Wayback density: CDX on `buttecounty.net` filtered to vote/elect paths for Nov 2016 -> empty; Nov 2018 -> a handful of incidental hits (library/news-widget assets, not the elections page itself). CDX on `buttevotes.net` (the elections-specific domain) -> Nov 2016 empty, Nov 2018 -> a few captures including 2018-11-05 and 2018-11-07 (day after election), but thin (5 URLs, mostly robots.txt/favicon, homepage present but shallow).
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://buttevotes.ca.gov/m/newsflash` -> 200; web search independently surfaced `buttevotes.ca.gov/m/newsflash/home/detail/201` ("Unofficial Election Results") confirming an active newsflash/press-release module.
Scores: Clarity 1 (confirmed platform, vintage for 2016/2018 unconfirmed) / Wayback 1 (thin, homepage-level only) / Registrar-URL 2 / Press-release 2.
Verdict: **viable** — best-evidenced source is likely Clarity's own current election-night pages for recent cycles; for 2016/2018 specifically the Wayback trail on buttevotes.net is thin, so the county's own newsflash archive is the stronger secondary path.

---

## Calaveras

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Calaveras/` -> 404. No Clarity usage.
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://elections.calaverasgov.us/` -> 200 (a dedicated `elections.` subdomain, with its own `/Results/Current-Results` path).
3. Wayback density: CDX on `elections.calaverasgov.us` for Nov 2016 -> real results pages captured: `Results.aspx` at **2016-11-11** and **2016-11-12** (200, ~18KB, right after election day), plus `Elections.aspx` on 2016-11-03. For Nov 2018 -> homepage captured 5x through the month (2018-11-07 through 2018-11-30, 200 status each time, day-after-election capture present).
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://elections.calaverasgov.us/News` -> 404 (wrong path guess, not retried within budget).
Scores: Clarity 0 / Wayback 2 / Registrar-URL 2 / Press-release 0 (unconfirmed).
Verdict: **viable** — small county, but the dedicated elections subdomain has a real, dated `Results.aspx` capture from the Friday after the 2016 general.

---

## Colusa

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Colusa/` -> 404. No Clarity usage.
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://www.countyofcolusaca.gov/197/Elections` -> 200 (current site, migrated from old domain `countyofcolusa.org` at some point between 2018 and now).
3. Wayback density: CDX on current domain `countyofcolusaca.gov` for both Nov 2016 and Nov 2018 -> **empty both windows** (domain didn't exist yet, or wasn't crawled). CDX on the old domain `countyofcolusa.org` -> Nov 2016 also empty; Nov 2018 has a real `/elections` page capture (2018-11-29, 200, 18KB) plus incidental site-chrome assets, but nothing dated closer to election night itself and nothing at all for 2016.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.countyofcolusaca.gov/CivicAlerts.aspx` -> 200 (CivicPlus alerts module exists; depth/vintage unconfirmed).
Scores: Clarity 0 / Wayback 1 (2018 only, thin, no election-night-adjacent capture) / Registrar-URL 2 / Press-release 1.
Verdict: **marginal** — no 2016 web trail found at all under either domain; 2018 has only a late-month capture. This is a small county where PDF result books may be the only real record for 2016.

---

## Contra Costa

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Contra_Costa/` -> 200 (confirmed Clarity user, one of the larger CA counties on the platform). Found election ID 64177 via search; `.../64177/current_ver.txt` -> `184353` (a working version number; ID is low enough in Clarity's global numbering to plausibly be an older cycle, vintage not independently confirmed).
2. Registrar URL: two generations found — current `https://www.contracostavote.gov/elections/` (200) plus a **purpose-built historical results database**, `https://pastresults.contracostavote.gov/` (200), whose own marketing copy (per search snippet) claims coverage "from 1997 to 2025." Old 2016/2018-era domain was `cocovote.us`.
3. Wayback density: CDX on `pastresults.contracostavote.gov` for Nov 2016 -> empty (site itself postdates 2016, expected — it's a modern re-hosting of old data, not something Wayback would catch back then). CDX on the actual period domain `cocovote.us` -> dense for both windows: 2016 shows `/current-election/` captured 2016-11-09, 11-19 (200, ~7.7KB) plus demographic/admin pages; 2018 shows `/current-and-past-elections/current-election-results/` captured 2018-11-14 (200, 10.5KB) and per-election subpages (June 2018 primary, March 2018 special).
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" -L https://www.contracostavote.gov/elections/news/` -> 404 (wrong path guess). Not retried within budget, but the pastresults.contracostavote.gov database itself functions as a de facto multi-decade archive.
Scores: Clarity 1 (confirmed, vintage unconfirmed) / Wayback 2 / Registrar-URL 2 / Press-release 1 (pastresults DB counts but not a classic press-release feed).
Verdict: **viable** — best case in this batch: three independent paths (Clarity, dense Wayback on the period domain, and a modern from-scratch historical database claiming 1997-2025 coverage that should be checked directly for the 2016/2018 canvass detail).

---

## Del Norte

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Del_Norte/` -> 404. No Clarity usage (small county).
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://www.co.del-norte.ca.us/departments/elections` -> 200; canonical path is actually `/departments/clerk-recorder/elections` (also 200), plus a legacy subdomain `elections.co.del-norte.ca.us`.
3. Wayback density: strong in both windows. Nov 2016: `elections.co.del-norte.ca.us/` captured 5x (2016-11-02 through 2016-11-21, 200 each); `.../clerk-recorder/elections` captured 2016-11-03 and 2016-11-17. Nov 2018: `.../elections/election-results` captured repeatedly, and — notably — dated per-election subpages exist: `.../election-results/november-8-2016-general-election-results` and `.../june-7-2016-primary-election-results`, both still live and captured as of 2018-11-25, meaning the county keeps a standing results archive by election name rather than overwriting a single "current results" page.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.co.del-norte.ca.us/departments/clerk-recorder/elections/press-releases` -> 200 (path guessed correctly on first try).
Scores: Clarity 0 / Wayback 2 / Registrar-URL 2 / Press-release 2.
Verdict: **viable** — best result in this batch for methodology: the county's own site structure preserves dated per-election results pages, so even a single fresh capture would recover the 2016 numbers; Wayback also already has that exact page indexed.

---

## El Dorado

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/El_Dorado/` -> 404. No Clarity usage.
2. Registrar URL: current site `https://www.eldoradocounty.ca.gov/County-Government/Elections` (curl -> 403, Cloudflare-blocked to bare curl but real per search). Old 2016/2018-era domain `edcgov.us` still resolves and redirects to the new domain.
3. Wayback density: CDX on `edcgov.us` for Nov 2016 -> homepage captured 8x (2016-11-03 through 2016-11-28, all 200); Nov 2018 -> homepage captured repeatedly including **2018-11-05, -07, -09** (200, ~44KB, spans election day through the week after). Filtered search for an elections-specific subpath came up empty both years — homepage-level only in this probe, actual results subpage not independently located.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" -L https://www.eldoradocounty.ca.gov/County-Government/Elections/Election-Results` -> 403 (Cloudflare-blocked; page presumably exists per search results listing it directly).
Scores: Clarity 0 / Wayback 1 (dense homepage captures, no confirmed results subpage) / Registrar-URL 1 (confirmed real, blocks curl) / Press-release 1 (found by search, unconfirmed by curl).
Verdict: **marginal** — site is real and actively archived around both election nights, but this probe only pinned the homepage, not a results page; a follow-up should search Wayback's edcgov.us captures for the actual elections subpath URL before concluding more.

---

## Glenn

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Glenn/` -> 404. No Clarity usage.
2. Registrar URL: current `https://www.countyofglenn.net/government/departments/elections` (curl -> 403, Cloudflare-blocked but real). A legacy `archive.countyofglenn.net/dept/elections/welcome` subdomain was surfaced by search (confirms the county itself preserves an "archive" mirror of the old site) but did not resolve to curl (connection failure, DNS or DOA).
3. Wayback density: CDX on `countyofglenn.net` for Nov 2016 -> homepage captured 5x (2016-11-03 through 2016-11-23, 200 each) but no elections-specific subpage in this window. Nov 2018 -> **strong**: `/dept/elections/welcome` captured 6x (2018-11-07 through 2018-11-30, 200, ~12KB), `/dept/elections/voting-locations` and `/dept/elections/absentee-ballot-status` also captured repeatedly through the same window.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" -L "https://www.countyofglenn.net/resources?f%5B0%5D=department:Elections"` -> 403 (Cloudflare-blocked; a filtered "Elections" resources feed does exist per search).
Scores: Clarity 0 / Wayback 2 (2018 excellent, 2016 homepage-only) / Registrar-URL 1 (real, curl-blocked) / Press-release 1 (exists per search, unconfirmed by curl).
Verdict: **viable** — 2018 has a well-archived elections department page across the whole canvass window; 2016 is thinner (homepage only) but the county's own `archive.countyofglenn.net` mirror is worth a direct follow-up.

---

## Humboldt

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Humboldt/` -> 404. No Clarity usage — Humboldt instead built its own tool (see #2).
2. Registrar URL: `https://humboldtgov.org/890/Elections-Voter-Registration` -> 200. Notably also has a **purpose-built historical results database**, `https://electstats.humboldtgov.org/` -> 200, described by search results as covering "2013 to 2026," directly analogous to Contra Costa's pastresults.contracostavote.gov.
3. Wayback density: excellent in both windows. Nov 2016: `/890/Elections-Voter-Registration` captured repeatedly on **2016-11-12** (multiple same-day snapshots) and again 2016-11-20 and 2016-11-18, all 200/~18.5KB. Nov 2018: same page captured on **2018-11-07** (day after election) and again 2018-11-13, -14, -18, -28, -29 — dense, real 200-status captures throughout the canvass.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://humboldtgov.org/Archive.aspx?AMID=76` -> 200, an "Archive Center - Election Results" page (name found directly via search, confirms a standing results/press archive).
Scores: Clarity 0 / Wayback 2 / Registrar-URL 2 / Press-release 2.
Verdict: **viable** — one of the strongest counties probed so far: dense Wayback coverage of the actual elections page in both windows, plus a dedicated modern historical-results database (ElectStats) and a confirmed press "Archive Center" — three independent, corroborating paths.

---

## Imperial

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Imperial/` -> 404. No Clarity usage.
2. Registrar URL: current `https://elections.imperialcounty.org/` -> 200. 2016/2018-era domain was `co.imperial.ca.us/regvoters` (old ASP-based site).
3. Wayback density: **split result, worth flagging**. Nov 2016 -> real, dated results page: `co.imperial.ca.us/regvoters/index.asp?fileinc=results` captured **2016-11-19**, 200, plus PDF result-report links referenced (revisits) and a full sample-ballot PDF capture. Nov 2018 -> the site had already migrated to a `/elections/` path by then, and **every single capture in the Nov 2018 window returned 404** (old `/regvoters` and even the newer `/elections/` paths both dead-linked that month) — no working results page captured that election cycle in this probe.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://elections.imperialcounty.org/election-data/` -> 200, an "Election Data" page on the current site.
Scores: Clarity 0 / Wayback 1 (2016 good, 2018 a confirmed gap — all captures 404) / Registrar-URL 2 / Press-release 1.
Verdict: **marginal** — 2016 recovery looks solid (a dated results page is directly in Wayback), but 2018 is a real gap: the site was mid-migration and Wayback caught only dead links that month. 2018 Imperial results likely need a different route (PDF, SOS canvass, or a differently-dated CDX window).

---

## Inyo

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Inyo/` -> 404. No Clarity usage.
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://elections.inyocounty.us/` -> 200; has an explicit `/results/` and `/p/election-results.html` path structure.
3. Wayback density: strong. Nov 2016 -> `/p/election-results.html` captured directly on **2016-11-13** and **2016-11-19** (200, ~7.7-7.9KB — a real dated results page). Nov 2018 -> homepage captured repeatedly (2018-11-07 day-after-election, -13 x2), and old PDF result files from even earlier cycles (`ElectionResults-ConsolidatedGeneral_101102.pdf`, `...ConsolidatedPrimary_100608.pdf`) still referenced/redirecting — evidence the county has archived election PDFs by name back to at least 2008.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://elections.inyocounty.us/news/` -> 200.
Scores: Clarity 0 / Wayback 2 / Registrar-URL 2 / Press-release 2.
Verdict: **viable** — a real, dated `election-results.html` page is directly in Wayback for the days after the 2016 general, plus a confirmed news archive and evidence of a long PDF-naming convention for even older cycles.

---

## Kern

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Kern/` -> 404. No Clarity usage.
2. Registrar URL: current site `https://www.kernvote.com/` (curl -> 403, Cloudflare-blocked but real). **The legacy 2016/2018-era site `http://elections.co.kern.ca.us/` is still live today** (200), and its `/ElectionInformation/ElectionResults` link (found by grepping the live homepage) also returns 200 right now — a rare case where the original results portal never went dark.
3. Wayback density: excellent both windows. Nov 2016: `elections.co.kern.ca.us/elections/` captured on **2016-11-07, -08 (election day), -09, -11, -12, -16, -17, -27** — repeated same-week, all 200. Nov 2018: homepage and `/elections/` captured through the month, plus actual election PDF documents preserved and fetchable from the archive (`ContestsNotOnBallot.pdf` 186KB, `Schools.pdf` 172KB, both 200 on 2018-11-10).
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" -L https://www.kernvote.com/elections/other` -> 403 (Cloudflare-blocked; page presumably exists per search listing "Contact & About Elections" under the same section).
Scores: Clarity 0 / Wayback 2 / Registrar-URL 2 (bonus: the live legacy site is a fifth recovery path beyond the four scored dimensions) / Press-release 1 (likely exists, blocked to curl).
Verdict: **viable** — best-evidenced county in this batch: dense Wayback captures bracketing 2016 election day itself, real PDFs recoverable from 2018, and an unusual bonus — the original ASP-era elections.co.kern.ca.us site is still live and serving results pages today.

---

## Kings

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Kings/` -> 404. No Clarity usage.
2. Registrar URL: current `https://www.countyofkingsca.gov/departments/administration/elections` (curl -> 403, Cloudflare-blocked but real per search). 2016/2018-era domain was `countyofkings.com`.
3. Wayback density: Nov 2016 -> real elections department page (`.../assessor-clerk-recorder-elections`) captured 3x (2016-11-15, -11-30, 200, ~19KB) plus a splash-redirect straight to an "election-results" sub-path. Nov 2018 -> mostly 302 splash-redirects resolving to 200 (2018-11-07, -11-13, -11-30) rather than a clean direct capture, plus one 404 on an admin login page — content is there but noisier to extract than 2016.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.countyofkingsca.gov/media` -> 403 (Cloudflare-blocked, not independently confirmed).
Scores: Clarity 0 / Wayback 2 (2016 clean, 2018 present but redirect-heavy) / Registrar-URL 1 (real, curl-blocked) / Press-release 0 (unconfirmed).
Verdict: **marginal** — 2016 has a clean elections-department capture; 2018 recovery will need to follow redirect chains rather than hitting a page directly, and the press-release path is unconfirmed.

---

## Lake

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Lake/` -> 404. No Clarity usage.
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://www.lakecountyca.gov/818/Registrar-of-Voters` -> 200.
3. Wayback density: strong once the right subdomain is found. Nov 2016 -> `publicapps.lakecountyca.gov/elections/results/result30.htm` captured **2016-11-12**, 200, 4.3KB — a genuine dated results page (the main `www.lakecountyca.gov` domain itself didn't show elections-tagged hits in the same window, so results lived on a separate `publicapps` subdomain). Nov 2018 -> very dense: individual ballot-measure PDFs (`Hv2.pdf`, `Iv2.pdf`, `Kv2.pdf`, `Lv2.pdf`, `Mv2.pdf`) and a `Nov2018MediaReleases/Registration+Deadline.pdf` all captured 200 through late November — the county evidently keeps a dedicated per-election media-release folder.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.lakecountyca.gov/916/Resources` -> 200; CDX independently surfaced a `Nov2018MediaReleases/` folder confirming an actual press-release archiving convention, not just a guess.
Scores: Clarity 0 / Wayback 2 / Registrar-URL 2 / Press-release 2.
Verdict: **viable** — the `publicapps` results subdomain plus a confirmed `MediaReleases` folder-per-election convention makes this one of the cleaner recoveries in the batch, though note results.aspx lives on a different subdomain than the main county site, worth remembering for future probes.

---

## Lassen

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Lassen/` -> 404. No Clarity usage.
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" -L https://www.lassencounty.org/dept/county-clerk-recorder/elections` -> 200, but redirects to the bare domain root `https://www.lassencounty.gov/` rather than the elections subpage — site has since migrated `.org` -> `.gov` and the deep link no longer resolves to elections specifically.
3. Wayback density: strong. Nov 2016: `/dept/registrar-voters/elections` captured 2016-11-30 (200, 72KB); `/ElectionResults/` captured 2016-11-12 (200); and a real GEMS (their voting-system vendor) election summary PDF captured **2016-11-24** (23KB, 200) — direct evidence of a machine-generated results report being preserved. Nov 2018: `/dept/county-clerk-recorder/elections` captured 4x (2018-11-07 day-after-election through 2018-11-30, all 200, ~75KB).
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.lassencounty.gov/CivicAlerts.aspx` -> 200 (CivicPlus alerts module present).
Scores: Clarity 0 / Wayback 2 / Registrar-URL 1 (site migrated domains, current deep link 404s/redirects to homepage) / Press-release 1.
Verdict: **viable** — both election-night windows have real archived content including an actual GEMS summary-report PDF from 2016; the live-URL findability score is dinged only because the county has since restructured its site.

---

## Marin

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Marin/` -> 200 (confirmed Clarity user). Election ID 112981 found via search; `.../112981/current_ver.txt` -> `300799` (working version number).
2. Registrar URL: current `https://www.marincounty.gov/departments/elections` (curl -> 403, Cloudflare-blocked but real). **A purpose-built historical database also exists**: `https://pastelections.marincounty.gov/` -> 200, directly analogous to Contra Costa's and Humboldt's equivalents. 2016/2018-era domain was `marincounty.org`.
3. Wayback density: exceptional — the densest of any county probed so far. Nov 2016: `/depts/rv` (Registrar of Voters) captured **15 times** between 2016-11-01 and 2016-11-26, consistently 200, ~15-16KB. Nov 2018: `/depts/rv` (now `/depts/RV`) captured **15+ times** between 2018-11-07 and 2018-11-29, all 200, ~13.5KB.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" -L https://www.marincounty.gov/news-releases/election-night-results-watch-online` -> 403 (Cloudflare-blocked, but the URL itself — an actual dated news-release page about election night — was found directly by search, confirming a real press-release archive exists).
Scores: Clarity 2 (confirmed platform, election ID resolves) / Wayback 2 / Registrar-URL 2 / Press-release 2.
Verdict: **viable** — the strongest county found in this whole run: four independent, corroborating paths (Clarity, a dedicated modern historical-results database, near-daily Wayback captures across both election nights, and a confirmed press-release archive).

---

## Mariposa

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Mariposa/` -> 404. No Clarity usage (small county, ~11,000 registered voters).
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" http://www.mariposacounty.gov/87/Elections` -> 200.
3. Wayback density: thin and one-sided. Nov 2016 on the period domain `mariposacounty.org` -> only incidental image-asset captures (calendar icons, etc.), no elections page and no homepage capture found in this window — a real gap. Nov 2018 -> homepage captured 6x (2018-11-07 day-after-election through 2018-12-01, all 200, ~22KB), but still no elections-specific subpage isolated.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.mariposacounty.org/CivicAlerts.aspx` -> 200 (CivicPlus alerts module present).
Scores: Clarity 0 / Wayback 1 (2018 homepage only, 2016 essentially empty) / Registrar-URL 2 / Press-release 1.
Verdict: **marginal** — 2016 shows almost no web trail for this small county; 2018 has homepage-only coverage. This is a strong candidate for the "PDF-only, low web-archive-ability" bucket this probe exists to flag — a records request or direct PDF hunt may beat Wayback here.

---

## Mendocino

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Mendocino/` -> 404. No Clarity usage.
2. Registrar URL: current `https://www.mendocinocounty.gov/government/assessor-county-clerk-recorder-elections/elections` (curl -> 403, Cloudflare-blocked but real). 2016/2018-era domain was `co.mendocino.ca.us`.
3. Wayback density: strong, and shows a long-running naming convention. Nov 2016: `/acr/elections.htm` captured **10 times** between 2016-11-04 and 2016-11-23 (all 200, ~6.4KB, spanning election day 2016-11-08 itself). Nov 2018: the same path now 301-redirects to the new site, but CDX also surfaced named historical-results pages reaching back to 2008 (`election_results/results20080205.pdf`, `results-20080620.htm`, `results20091118.htm`, `results20100608.htm`, `20101102-general.htm`) and a `pastElections.htm` index — strong evidence the county has archived results by dated filename for over a decade.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" -L https://www.mendocinocounty.gov/government/assessor-county-clerk-recorder-elections/current-election-results` -> 403 (Cloudflare-blocked, not independently confirmed, though a "Past Election Results" page was found directly via search).
Scores: Clarity 0 / Wayback 2 / Registrar-URL 1 (real, curl-blocked) / Press-release 1 (likely exists, unconfirmed by curl).
Verdict: **viable** — 2016 has a direct, dated `elections.htm` capture including election day itself, and the site's own dated-filename convention for results pages (`resultsYYYYMMDD.htm`) going back to 2008 makes this one of the more self-documenting counties in the batch.

---

## Merced

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Merced/` -> 200 (confirmed Clarity user). Election ID 126388 found via search; `.../126388/current_ver.txt` -> `376465` (working version number; ID is high/recent, no independent confirmation this reaches back to 2016/2018).
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://www.countyofmerced.com/3878/Elections` -> 200; also has a dedicated `/3702/Past-Election-Results` page per search.
3. Wayback density: weak. Nov 2016 -> **zero captures at all** for `countyofmerced.com`, filtered or not — a real gap. Nov 2018 -> only incidental calendar-icon image assets, no elections page or even homepage captured.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.countyofmerced.com/CivicAlerts.aspx` -> 200 (CivicPlus alerts module present).
Scores: Clarity 1 (confirmed, vintage unconfirmed) / Wayback 0 (real gap both years on the county's own domain) / Registrar-URL 2 / Press-release 1.
Verdict: **marginal** — despite being a mid-size county with Clarity ENR today, its own website has no Wayback trail at all for 2016 or 2018; Clarity itself (if its historical archive still holds early elections) or the "Past Election Results" page on the current site are the better recovery routes, not Wayback.

---

## Modoc

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Modoc/` -> 404. No Clarity usage.
2. Registrar URL: old domain `co.modoc.ca.us` now redirects to `https://www.countyofmodoc.gov/`, but the deep link `/departments/elections/` 404s post-migration; homepage `curl -o /dev/null -w "%{http_code}" -L https://www.countyofmodoc.gov/` -> 200.
3. Wayback density: split by year but the 2018 side is a standout. Nov 2016 -> only homepage/other-department captures on `co.modoc.ca.us` (2016-11-03 through -28, 200 each), no elections-specific page isolated. Nov 2018 -> **`/departments/elections/2016-elections` captured twice** (2018-11-07 and 2018-11-14, both 200, ~14KB) — the county keeps a standing, dated archive page for the *2016* election that was still live and captured in *2018*, plus the live `/departments/elections` page itself captured 3x that same window.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.countyofmodoc.gov/CivicAlerts.aspx` -> 200.
Scores: Clarity 0 / Wayback 2 (thanks to the retrospective 2016-elections page caught in the 2018 crawl) / Registrar-URL 1 (current site real, old deep link now 404s) / Press-release 1.
Verdict: **viable** — small county, but the site's own "keep a page per past election" convention means the 2016 general is directly recoverable from a single 2018-dated Wayback capture.

---

## Mono

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Mono/` -> 404. No Clarity usage.
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://monocounty.ca.gov/elections` -> 200.
3. Wayback density: excellent 2016, gap in 2018. Nov 2016: `/elections` page captured 2016-11-04 and 2016-11-15 (200, ~8.5KB), **and two actual results PDFs captured 2016-11-17**: `SemiFinalElection.pdf` and `3950_001.pdf` (both ~9.1KB, 200) — direct results documents, not just a landing page. Nov 2018: the same document paths were being served over HTTP->HTTPS migration that month; every capture in the window is a 301 redirect immediately followed by a 404 on the HTTPS target — no working 2018 election document actually recovered from Wayback in this probe.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://monocounty.ca.gov/elections/page/election-updates` -> 200 ("Election Updates" page, confirmed).
Scores: Clarity 0 / Wayback 1 (2016 excellent including real results PDFs, 2018 a confirmed gap — all captures 404/redirect) / Registrar-URL 2 / Press-release 2.
Verdict: **marginal-to-viable** — 2016 is genuinely strong (semi-final results PDF directly archived), but 2018 recovery will need a source other than Wayback (the site was mid-HTTPS-migration and every capture that month dead-ends); worth re-querying CDX with a wider date window in case a working capture exists just outside November.

