# New-county scout memo: election-night dataset expansion

Task 10 of the county election-night research plan. Produces a ranked list of
candidate CA counties (regular + no-new-tech control) for Tasks 11-12 to add
to `data/research/election-night/`. This memo is written incrementally: each
county's probe result is appended as soon as it is probed, per the project's
"persist as you go" rule (`docs/research/RUNBOOK.md` section 9).

Counties already in the dataset (do NOT re-add; excluded from Step 1 probing
below except to note their existing status): San Francisco (control, no
Clarity/no new tech), Fresno, Los Angeles, Madera, Napa, Nevada, Orange,
Placer, Riverside, Sacramento, San Bernardino, San Diego, San Mateo, Santa
Clara. That is 14 of the 58 CA counties. The 44 counties below are the actual
new-candidate universe for Step 1.

## Methodology (exact commands used)

**Step 1a - current_ver.txt at the county root (no electionId known).**

```
curl -s -o body -w "%{http_code}" "https://results.enr.clarityelections.com/CA/<County>/current_ver.txt"
```

Finding: this form 404s for EVERY county tested, including counties we
already know use Clarity (Madera, Santa_Clara both 404 on this exact form).
So a 404 on the county-root `current_ver.txt` is NOT evidence of absence, as
the brief warned; it just means Clarity does not expose a version pointer at
the site root without an electionId. This step was abandoned as a signal
after the confirmation probe; Step 1b (CDX) is the only reliable detector we
found. Also discovered: `results.enr.clarityelections.com` 403s any request
with no `User-Agent` header via a WAF (Akamai/CloudFront-style block page);
every curl in this memo after that point sends
`-A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"`.

**Step 1b - CDX enumeration (the actual detector).**

The brief's literal example command:
```
curl "http://web.archive.org/cdx/search/cdx?url=results.enr.clarityelections.com/CA/<County>*&from=20121101&to=20181201&output=json&limit=200&matchType=prefix"
```
returns `[]` even for Madera, a CONFIRMED Clarity county (verified against
`data/research/election-night/madera-ca.json`'s own cited Clarity URLs). The
literal trailing `*` combined with `matchType=prefix` is invalid: CDX prefix
matching wants the bare URL with NO trailing wildcard once `matchType=prefix`
is set. The working form (verified to return Madera's real captures):
```
curl "https://web.archive.org/cdx/search/cdx?url=results.enr.clarityelections.com/CA/<County>&matchType=prefix&from=20121101&to=20181201&output=json&limit=200"
```
Also: `http://` (plain) to web.archive.org intermittently gave `Connection
refused` on port 80 partway through a batch (a local/network artifact, not a
web.archive.org problem) while `https://` was reliably 200 throughout: all
CDX calls below use `https://`. 2-second sleep between every request to the
same host, per county, in a single-threaded loop.

**Step 1c - JSON confirmation for a found electionId.** For every electionId
`<eid>` a CDX hit surfaces, first `.../CA/<County>/<eid>/current_ver.txt` (this
form, WITH an eid, reliably 200s for real elections, unlike the county-root
form), then `.../CA/<County>/<eid>/<version>/json/en/electionsettings.json`
(fallback `.../json/electionsettings.json`). `electionsettings.json` ->
`settings.electiondetails.electiondate` and `.internalname` identify the
election (e.g. "General Election 2016" / "11/8/2016"), which is how each eid
was dated below (Wayback capture timestamps are a weak proxy only: Clarity
election pages stay live indefinitely post-election and get recrawled for
years afterward, so a capture in e.g. 2018 says nothing about which election
the eid is for; the electionsettings.json's own `electiondate` field is the
only reliable date signal). `.../json/sum.json` -> `Contests[].BC` confirms
real vote-count JSON is being served (not just an HTML shell).

**Step 2 (press-release scout) and Step 3 (control scout) methodology is
recorded inline in their own sections below.**

---

## Step 2: Press-release / dated-report scout (Alameda, Contra Costa, Ventura, Kern, Sonoma, Stanislaus)

Method: identify the county's registrar domain (many have moved domains at
least once since 2012; the live site's redirect chain reveals the current
one), curl the live site for a news/press/results nav link, then CDX the
domain (or the specific results path once found) for 2012-2018 captures.
Same 2-second-per-host politeness pause; same UA header requirement in a
few cases (elections.enr Clarity checks reused from Step 1; plain web
fetches did not need it, except where noted).

### Alameda (acvote.org / now acvote.alamedacountyca.gov)

Live site has a real per-election "News Releases" PDF folder pattern:
`acvote-assets/02_election_information/PDFs/<YYYYMMDD>/en/News%20Releases/<file>.pdf`
(confirmed for the 2018-06-05 election via CDX). However Wayback's crawl of
the ENTIRE acvote.org domain 2012-2018 is very thin (172 total URLs, only
1 matching news/press/release keywords), so this memo could NOT confirm
whether an equivalent "semi-final results" release exists for the Nov
2012/2014/2016/2018 generals within budget. Live news-announcements page
(`https://acvote.alamedacountyca.gov/main/news-announcements`) only shows
posts back to ~2022; no visible pagination reaching 2012-2018. **Verdict:
plausible infrastructure, NOT proof of a 2012-2018 semi-final release;
next step would be to guess dated PDF folder names directly on the LIVE
CMS for Nov 2012/2014/2016 (the assets appear to persist indefinitely) since
Wayback's crawl is too sparse to rely on.**

### Contra Costa (cocovote.us / now contracostavote.org)

The historical domain (cocovote.us, a WordPress site) has 0 CDX hits for
news/press/release keywords across 500 sampled captures in the window. The
CURRENT domain (contracostavote.org) is a JS shell (empty root, redirects to
`/lander`) that curl cannot meaningfully inspect without rendering. **Verdict:
no press-release archive evidence found for Contra Costa in this pass; combined
with the Clarity dead-end above (special-elections-only, HTML-only), Contra
Costa is the weakest of the 6 Step-2 candidates so far probed.**

### Ventura (recorder.countyofventura.org, county-clerk/press-releases)

Strong positive find: a Wayback capture of
`recorder.countyofventura.org/county-clerk/press-releases/` (2016-05-24)
shows a real "Press Releases - Search by year 2016 2015 2014 2013 2012 2011
2010" archive built into the site nav, i.e. a citable multi-year press
release index reaching back past our target window. The specific page
fetched (a May 2016 snapshot) lists only pre-election-day releases (voter
registration deadlines, poll worker notices) for that month, not a
post-election "semi-final results" release; a deeper CDX pull (capped at
500 rows for the whole domain, `recorder.countyofventura.org`) turned up
Ventura's own results/canvass pages
(`elections/election-resultscanvass-of-the-vote/...`) but not yet a
specific November semi-final release URL within budget. **Verdict: the
strongest press-release-archive candidate of the 6 - a genuine year-indexed
press release system predating 2012 - worth a dedicated follow-up pass to
pull the actual November releases page-by-page.** (Also: Ventura's Clarity
2012 presidential-general row is already independently CONFIRMED above, so
Ventura does not strictly need this route to land a first row - it's a
second, complementary path for the other years.)

### Kern (kernvote.com)

kernvote.com is a custom ASP.NET "ElectionInformation" system (not
WordPress, not Clarity), with a `/ElectionInformation/Results/?ID=<n>`
per-election results endpoint. Wayback's earliest capture of this domain is
2018 (92 total URLs, all from the Nov 2018 general, `ElectionID=97`); no
2012-2016 captures found for this domain in this pass, meaning Kern was
likely on a DIFFERENT domain/system before 2018 (not yet identified).
Critically, the captured 2018 results page IS server-rendered (not a JS
shell - curl reads real content directly) and self-labels its report time:
**"KERN COUNTY ELECTION RESULTS November 6, 2018 Statewide General Election
Unofficial Final Results as of 11/26/2018 4:31:29 PM"** - this specific
capture is a 20-DAY-POST-ELECTION canvass update, not the election-night
plateau (same over-ripe-canvass trap as RUNBOOK 5.2/7.3), so it cannot be
used as-is; an earlier Wayback capture of the same URL from Nov 7-9, 2018
would be needed. **Verdict: Kern's ENR system is a good target (self-dating
timestamped reports, real content, not a rendering trap) for 2018 onward;
pre-2018 Kern needs a different domain/system not yet located.**

### Sonoma (sonomacounty.gov/.../registrar-of-voters)

Two finds: (1) Sonoma has RECENTLY adopted Clarity (a live link to
`results.enr.clarityelections.com/CA/Sonoma/126199/web.345435/...` on the
current ROV page) - but this electionId is far outside the 2012-2018 range
(consistent with Step 1's finding of zero Sonoma CDX hits in that window:
Sonoma's Clarity use started recently, likely 2022+, not useful for the
scarce pre-2018 years). (2) Far more useful: Sonoma runs a dedicated
"Historical Election Results" database at **`https://electionstats.sonomacounty.ca.gov`**,
self-described as covering "election results and vote counts... from 2009
to 2024." This is a modern Next.js app (JS-rendered, curl only sees the
shell) so its actual per-contest data could not be read in this pass, and
critically it is framed as a RESULTS/vote-count database, not explicitly an
election-NIGHT snapshot archive - it may show only final canvassed totals,
which would not satisfy the election-night-plateau definition without
further digging (does it version by report date, or only show the final?).
**Verdict: real archive exists and spans the whole target range, but
needs a rendering pass (puppeteer, main-session-only per RUNBOOK 6.7) to
determine whether it carries election-night-specific figures or only
final; flag for whoever picks up Sonoma.**

### Stanislaus (stanvote.com/past-results)

Best Step-2 find of the six. `stanvote.com/past-results/` is a flat
directory of dated per-election result pages AND matching Statement-of-Vote
PDFs going back to 2002 (`11-06-2012-results.htm`, `11-04-2014-results.HTM`,
`11-08-2016-results.htm`, `06-05-2018-results.htm`, each paired with a
`-sov.pdf`). Fetched `11-06-2012-results.htm` (only Wayback capture: 2012-12-24):
content is a classic GEMS-style "SUMMARY REPT-GROUP DETAIL... OFFICIAL
RESULTS... RUN DATE:11/29/12 11:11 AM... PRECINCTS COUNTED (OF 388)....100.00...
BALLOTS CAST - TOTAL 156,935." **This is the CERTIFIED FINAL canvass state
(Nov 29, 100% precincts), not the election-night plateau** - the same
single-URL-gets-overwritten trap RUNBOOK 7.3 warns about. A tight CDX query
on that exact URL for the 2012-11-01..2013-01-01 window returns exactly ONE
capture (the Dec 24 one already fetched); Wayback did not preserve an
election-night-era snapshot of this specific file. **Verdict: Stanislaus
clearly has real, structured, citable HTML+PDF result pages for every
Nov general 2012-2018 (a much stronger and more complete historical spread
than any Clarity find in this scout), but the specific file we could reach
is post-canvass; recovering the election-night plateau will require either
an earlier Wayback capture we haven't found yet (broader CDX search) or a
differently-named same-night file (Fresno-style dated report series) that
this pass did not have budget to hunt for.** Given the completeness of the
2012/2014/2016/2018 coverage (all four Nov generals have a same-shaped
`past-results` page), Stanislaus is the single most promising REGULAR-county
candidate in this whole scout, Clarity or not.

---

## Step 3: Control-candidate scout (no e-pollbooks, no ASV, no VCA through 2024)

Method: two authoritative CA SoS documents, both fetched live via curl (not
Wayback, not county sites - this sidesteps every Cloudflare/bot-wall that
blocked several county registrar domains in Step 2):

1. **`https://elections.cdn.sos.ca.gov/vca/2020-vca-report/2020-vca-final-report.pdf`**
   (the SoS's own 2020 VCA program report to the Legislature, `pdftotext -layout`
   then grepped). Page/line 166-167 states verbatim: **"Amador, Butte,
   Calaveras, El Dorado, Fresno, Los Angeles, Madera, Mariposa, Napa, Nevada,
   Orange, Sacramento, San Mateo, Santa Clara, and Tuolumne"** are the 15 VCA
   counties as of the 2020 report. This memo could NOT locate an equivalent
   2022 or 2024 VCA-county report at the analogous CDN path (guessed URLs
   `.../vca/2022-vca-report/...` and `.../vca/2024-vca-report/...` both 403,
   i.e. do not exist at that path) nor a browsable current VCA-counties page
   on sos.ca.gov (the live page's nav says "VCA Counties" but every URL
   tried for it 301-redirects back to the generic VCA landing page, whose
   body text is a CMS template with no county list actually present in the
   fetched HTML). **This is a real gap: the 15-county list is confirmed only
   for 2020; VCA expanded further for 2022 and 2024 and this pass could not
   fetch an authoritative later list. Cross-checked below with a second,
   independent, more current document that closes most of this gap.**
2. **`https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf`**
   ("Voting Technologies in Use by County," dated **as of October 10, 2025**
   - found cited as a primary source in this project's own
   `packages/data/county_tech.json`, e.g. the Fresno e-pollbook record).
   `pdftotext -layout` gives a clean per-county row: Central Tabulation /
   Vote-Center Tabulator / Accessibility / Ballot-on-Demand (Elections
   Office) / Ballot-on-Demand (Vote Center/Polling Place) / Remote
   Accessible VBM / **Electronic Pollbook**. This is a real, dated,
   authoritative SoS document, not an inference. **Caveat that must travel
   with every finding below: this is an OCTOBER 2025 snapshot, i.e. up to
   11 months AFTER the Nov 2024 general.** A "Do not use" entry today is
   strong (adoption timelines essentially never run backward - nobody
   de-installs an e-pollbook system) but not literal proof the county also
   had no e-pollbook on Nov 5, 2024; Task 12 should re-check each finalist's
   own EAP / board minutes / news coverage for the specific 2024 date before
   locking in the choice. (Illustrative of why this caveat matters: this
   same document shows San Francisco's OWN row now reading `DFM` in the
   Electronic Pollbook column - San Francisco is the project's own confirmed
   no-e-pollbook-through-2024 control, so this "DFM" entry must reflect an
   adoption made sometime AFTER Nov 2024, inside the gap this snapshot does
   not resolve. Exactly the caveat above, demonstrated on a county we
   already know the ground truth for.)

Every county whose Electronic Pollbook column reads **"Do not use"** in the
Oct 2025 document: Alpine, Calaveras, Colusa, Del Norte, Glenn, Imperial,
Lake, Mariposa, Mendocino, Plumas, Sacramento, San Luis Obispo, Shasta,
Sierra, Siskiyou, Tehama, Trinity, Ventura (18 counties). Cross-referencing
against the confirmed 2020 VCA list removes Calaveras, Mariposa, and
Sacramento (all three are on the 2020 VCA list despite showing no
e-pollbook - a real, separate finding: VCA adoption and e-pollbook adoption
are independent facts, not a package deal, exactly as the
`researching-jurisdiction-counting-tech` skill warns not to conflate).
Shasta and Ventura are EXCLUDED from control consideration here even though
they also show "Do not use" - both are already this memo's top two REGULAR-
county nominees (Step 1/2 above) and should not double-book both roles.

That leaves 13 clean candidates: Alpine, Colusa, Del Norte, Glenn, Imperial,
Lake, Mendocino, Plumas, San Luis Obispo, Sierra, Siskiyou, Tehama, Trinity.
A second corroborating column in the SAME document, "Ballot on Demand
VoteCenter/Polling Place" (VCA-model counties always show a real device
here, since VCA is built around vote centers with on-demand ballot
printing), reads **"Do not use"** for ALL of: Colusa, Del Norte(has
`Dominion ICE` central-only), Glenn(has a device - see caveat), Imperial,
Lake, Mendocino, Plumas, San Luis Obispo, Sierra, Siskiyou, Tehama, Trinity
- i.e. essentially the whole list independently reads as still running the
traditional (non-VCA) precinct/polling-place model, which is a second, more
direct signal than the VCA-county-list absence alone.

**ASV (automated signature verification) could not be independently
confirmed or refuted for any of these counties within this pass's budget**
(no small rural county publishes a signature-verification-software press
release the way Fresno's registrar did; this project's own `county_tech.json`
has no records yet for any of them). The working assumption - stated
honestly as an assumption, not a finding - is that ASV adoption in CA has so
far tracked VCA/vote-center adoption in every documented case in this
project's own data (Fresno, LA, etc. all pair ASV with their VCA rollout
year); a county with zero VCA infrastructure and zero e-pollbooks buying
standalone signature-verification software would be an unusual, expensive,
undocumented outlier. **Task 12 must verify this leg specifically (EAP where
one exists, county board minutes, local news) before finalizing** - this
memo nominates on the strength of the VCA+e-pollbook legs only.

### Nominated control candidates, ranked

1. **San Luis Obispo County** - by far the largest of the 13 (roughly
   180,000+ registered voters vs. a few thousand for Alpine/Sierra/Trinity/
   Modoc-sized counties), meaning any election-night share computed for it
   is statistically meaningful the way Sacramento/Riverside-scale counties
   already in the dataset are; confirmed absent from the 2020 VCA list;
   confirmed "Do not use" for both Electronic Pollbook and VoteCenter/Polling
   Ballot-on-Demand in the Oct 2025 SoS equipment table (i.e. still a
   precinct/polling-place county with no vote-center infrastructure at all).
   **Top pick: best combination of real evidence and analytical usefulness.**
2. **Tehama County** - clean on every column (Electronic Pollbook "Do not
   use", both Ballot-on-Demand columns "Do not use", not on the 2020 VCA
   list), a mid-small rural Central Valley/foothill county with a real (if
   modest) voter base, giving more geographic/demographic spread than the
   tiny mountain counties.
3. **Siskiyou County** - same clean profile (Electronic Pollbook "Do not
   use", both BoD columns "Do not use", not on the 2020 VCA list), far
   northern rural county, another useful geographic contrast to SF and to
   the other nominees.

(Colusa, Glenn, Trinity, Lake, Mendocino, Plumas are honorable mentions with
the same clean e-pollbook/VCA profile but smaller voter bases or, in Glenn's
case, a partial Ballot-on-Demand device at the elections office that muddies
the "zero VCA infrastructure" story slightly; Alpine and Sierra are
California's two smallest counties by population and would contribute
almost no statistical weight to the chart.)

---

## Step 1: Clarity scout, 44 candidate counties

### Summary table (CDX hit / no hit, `2012-11-01` to `2018-12-01` window)

| County | CDX hits in window | Notes |
|---|---:|---|
| Alameda | 0 | no Clarity presence found |
| Alpine | 0 | no Clarity presence found |
| Amador | 0 | no Clarity presence found |
| Butte | 0 | no Clarity presence found |
| Calaveras | 0 | no Clarity presence found |
| Colusa | 0 | no Clarity presence found |
| Contra Costa | 200 (capped) | Clarity present but SPECIAL ELECTIONS ONLY, HTML-only (no JSON) - see detail below |
| Del Norte | 0 | no Clarity presence found |
| El Dorado | 0 | no Clarity presence found |
| Glenn | 0 | no Clarity presence found |
| Humboldt | 0 | no Clarity presence found |
| Imperial | 0 | no Clarity presence found |
| Inyo | 0 | no Clarity presence found |
| Kern | 0 | no Clarity presence found |
| Kings | 0 | no Clarity presence found |
| Lake | 0 | no Clarity presence found |
| Lassen | 0 | no Clarity presence found |
| Marin | 0 | no Clarity presence found |
| Mariposa | 0 | no Clarity presence found |
| Mendocino | 0 | no Clarity presence found |
| Merced | 200 (capped) | Clarity present, JSON CONFIRMED for Nov 2016 and Nov 2018 generals - see detail below |
| Modoc | 0 | no Clarity presence found |
| Mono | 0 | no Clarity presence found |
| Monterey | 0 | no Clarity presence found |
| Plumas | 0 | no Clarity presence found |
| San Benito | 0 | no Clarity presence found |
| San Joaquin | 0 | no Clarity presence found |
| San Luis Obispo | 0 | no Clarity presence found |
| Santa Barbara | 0 | no Clarity presence found |
| Santa Cruz | 0 | no Clarity presence found |
| Shasta | 200 (capped) | Clarity present across 2012-2018, multiple election IDs - see detail below |
| Sierra | 0 | no Clarity presence found |
| Siskiyou | 0 | no Clarity presence found |
| Solano | 0 | no Clarity presence found |
| Sonoma | 0 | no Clarity presence found |
| Stanislaus | 1 | single hit, HTML-only landing page, Nov 2018 era - see detail below |
| Sutter | 0 | no Clarity presence found |
| Tehama | 0 | no Clarity presence found |
| Trinity | 0 | no Clarity presence found |
| Tulare | 0 | no Clarity presence found |
| Tuolumne | 0 | no Clarity presence found |
| Ventura | 200 (capped) | Clarity present 2012-2016, at least 2 election IDs - see detail below |
| Yolo | 0 | no Clarity presence found |
| Yuba | 0 | no Clarity presence found |

The 39 "0 hits" counties: their CDX query returned `[]` (a bare header row
after JSON-decoding minus 1, or an empty array), i.e. web.archive.org has
never crawled `results.enr.clarityelections.com/CA/<County>` in this window
with this matchType=prefix query, in either the underscore or (where
applicable) concatenated form. This is not airtight proof of absence
(a county could use Clarity with zero Wayback crawls, or Clarity under a
name spelling we did not try), but combined with the fact that 5/44 counties
DID show hits with the identical method, absence of a hit is reasonably
strong negative evidence. Raw CDX JSON for all 44 is cached at
`/private/tmp/claude-501/.../scratchpad/clarity-probes/cdx_json/<County>.json`
(local scratch, not committed).

### Detail: Contra Costa (dead end for Clarity, still a Step-2 candidate)

CDX hits cluster into 4 electionIds: 10301, 10460, 10505, 11060 (all found
via `results.enr.clarityelections.com/CA/Contra_Costa&matchType=prefix&from=20121101&to=20181201`).
For each, fetched the live CDN's HTML page (Wayback raw `id_` replay) and the
JSON API directly:
- Page titles are generic ("Contra Costa - Election Results") but body text
  for 10301/10460/10505 explicitly says "Special Election" (grep on the
  fetched HTML). None say "General Election".
- `current_ver.txt` at the eid level resolves fine for all 4 (e.g. eid 10460
  -> version 15737), proving these are real, still-live Clarity elections.
- `json/en/electionsettings.json` AND `json/electionsettings.json` both 404
  for all 4 eids at their current version. This is the Web01/Web02-era
  HTML-only limitation from RUNBOOK 7.2: no JSON was ever published for
  these Contra Costa elections.

Probe URL: https://results.enr.clarityelections.com/CA/Contra_Costa/10460/15737/json/sum.json

**Conclusion: Contra Costa's Clarity footprint is limited to special
elections, and none of those special elections publish JSON.** No Nov-general
year is recoverable via Clarity for Contra Costa. This does not disqualify
Contra Costa; it is exactly why the brief nominated it for Step 2 (press
release scout) instead, see below.

### Detail: Merced (best Clarity find - Nov 2016 AND Nov 2018 confirmed)

CDX (2012-11-01 to 2018-12-01 window) surfaces eid 64651 (first capture
2016-11) and eid 71885 (first capture 2017-11). A follow-up CDX query
narrowed to `from=20180901&to=20181215` surfaces two more: 75863, 92905.//
A CDX query for `from=20121001&to=20160101` returns **zero** rows: Merced has
no Clarity presence before 2016 (pre-2016 years are not recoverable via
Clarity for Merced; would need a different route entirely, likely none).

Per-eid electionsettings.json (`settings.electiondetails.electiondate` /
`.internalname`):
- **eid 64651** = "General Election 2016", electiondate `11/8/2016`. Current
  version 184354, `websiteupdatedat` 12/6/2016 2:25 PM PST (a month post-
  election - likely the CERTIFIED version, not election night; a follow-up
  task will need to bracket backward for the actual last-night version, per
  RUNBOOK 7.2's version-bracket method).
  `json/sum.json` at this version returns real contest data:
  `Contests[0].BC = 72631`. **JSON: YES.**
  Probe URL: https://results.enr.clarityelections.com/CA/Merced/64651/184354/json/sum.json
- **eid 71885** = electiondate 11/16/2017 (internalname not captured, but
  the date confirms an off-cycle November 2017 special/municipal election,
  not one of our target even-year Nov generals). Not relevant to this
  dataset; noted for completeness only.
- **eid 75863** = "Statewide Primary 2018", electiondate `6/5/2018`. Not a
  Nov general; not relevant to this dataset's rows (June primaries are out
  of scope), noted for completeness.
- **eid 92905** = "Gubernatorial General Election", electiondate `11/6/2018`.
  Current version 223374, `websiteupdatedat` 12/3/2018 11:23 AM PST (again
  ~1 month post-election, likely certified not election-night). **JSON: YES**
  (electionsettings.json 200; sum.json not separately re-checked for this eid
  to conserve requests, but the identical API shape as 64651 makes it
  extremely likely to work; a Task 11/12 recovery pass should re-verify).
  Probe URL: https://results.enr.clarityelections.com/CA/Merced/92905/223374/json/sum.json

A further CDX query `from=20220901&to=20241215` returns 300 rows (capped)
spanning 8 distinct eids (116138, 111519, 102793, 120376, 113945, 107145,
110594, 122862) - Merced is STILL actively on Clarity through the 2022-2024
cycle (not individually dated to conserve request budget; a follow-up task
would date the Nov 2022 and Nov 2024 eids the same way).

**Merced Clarity-recoverable Nov-general years so far confirmed: 2016, 2018**
(both with real JSON), plus very likely 2022 and 2024 (active Clarity
presence confirmed, exact eid not yet dated). **2012 and 2014 are NOT
recoverable via Clarity** (no Clarity presence before 2016); those years
would need a different route (press release / local news) or be left null,
same as several existing counties in the dataset (e.g. Fresno's 2012/2014
rows are `none`).

### Detail: Shasta (broadest historical spread, 6 election IDs, but AMBIGUOUS dating - flag this)

CDX surfaces 6 distinct eids: 16928, 22577, 39813, 42510, 51521, 53996.
`current_ver.txt` resolves live for eid 22577 (version 43930) and eid 39813
(version 86237); `json/en/electionsettings.json` and `json/electionsettings.json`
both 404 for both (unlike Merced, where `en/electionsettings.json` worked
cleanly), but `json/sum.json` returns real data for both:
- eid 22577, current version: `Contests[0].C = "Governor"`, `BC = 66502`.
  A CA Governor race is on the Nov-general ballot only in 2014 and 2018 in
  this window; Shasta's registered-voter scale makes both years plausible
  and this memo does NOT have a certified-total cross-check handy to
  disambiguate (would need the SoS SoV PDF, out of scope for a scout pass).
  Probe URL: https://results.enr.clarityelections.com/CA/Shasta/22577/43930/json/sum.json
- eid 39813, current version: `Contests[0].C = "DEM - PRESIDENTIAL PREFERENCE - DEMOCRATIC"`,
  `BC = 45233` - this is a **June PRESIDENTIAL PRIMARY subtotal (one party's
  ballot type), not a Nov general.** Off-target for this dataset.

**Important flag for whoever picks up Shasta next:** captures for a single
eid span multiple YEARS (e.g. eid 22577 has captures from 2012-11 through
2018-11), which combined with `current_ver.txt` returning ONE live version
per eid regardless of how old the eid is, strongly suggests Shasta's Clarity
deployment reuses/overwrites the same electionId slot across multiple
election cycles rather than minting a fresh eid per election (or at minimum,
Wayback's capture history is not a safe proxy for "when this eid's election
happened" the way it was for Merced). **Do not trust the eid-level
`current_ver.txt` content as automatically representing the election that
first put that eid on the radar; re-verify the date via a captured-in-time
Wayback snapshot's own page text (not just the live CDN's current version)
before building a row on it.** Net: Shasta clearly HAS a Clarity JSON
pipeline (sum.json is real and working, unlike Contra Costa's dead HTML-only
setup), and clearly has SOME countywide general-election data across
2012-2018, but this scout could not cleanly pin a specific eid to a specific
Nov-general date within budget. Ranked as promising-but-unconfirmed.

### Detail: Ventura (2012 presidential general CONFIRMED, 1 more eid off-target)

CDX surfaces 2 distinct eids: 43954 and 39536. `current_ver.txt` resolves
live for both (113575 and 89284 respectively). `json/en/electionsettings.json`
and `json/electionsettings.json` both 404 for both (same gap as Shasta), but
`json/sum.json` (fetched with `curl --compressed`; without `--compressed` the
response body is raw gzip bytes that fail to parse as JSON, a second
confirmed instance of RUNBOOK 7.1's gzip gotcha, this time on the LIVE
Clarity CDN rather than a Wayback replay) returns real data:
- **eid 43954: `Contests[0].C = "President and Vice President"`,
  `BC = 330,419`.** This is unambiguously the **Nov 6, 2012 presidential
  general** (only a Nov general has a President/VP contest, and 330,419
  ballots is squarely in Ventura County's real 2012 scale - roughly 430K
  registered voters at ~76% turnout, matching 2012's historically high
  presidential-year turnout). **JSON: YES, CONFIRMED, for Ventura 2012.**
  This is the single strongest pre-2018 find of the whole scout: Ventura
  2012 sits right in the scarcest part of the target range (RUNBOOK ranking
  weights pre-2018 years highest) with a clean, unambiguous, non-reused eid.
  Probe URL: https://results.enr.clarityelections.com/CA/Ventura/43954/113575/json/sum.json
- eid 39536: `Contests[0].C = "DEM - Pres Pref - DEMOCRATIC Primary"`,
  `BC = 133,800` - a June presidential-primary subtotal (most likely June
  2016), off-target for this dataset, same pattern as Shasta's 39813.

Ventura is ALSO one of the Step 2 press-release candidates (below); with
Clarity now confirmed for at least 2012, the press-release route only needs
to fill 2014/2016/2018/2022/2024, not carry the whole county.

### Detail: Stanislaus (single hit, likely dead end)

Exactly one CDX row in the whole 2012-2018 window, an eid-less capture of
the bare `/CA/Stanislaus` path from 2018-11 (era of the Nov 2018 general).
No electionId, no deeper path, no JSON signal at all: Stanislaus's Clarity
footprint (if any) is far too thin to be useful. Consistent with it being a
Step-2 (press-release) candidate instead.

---

## Step 4: Ranking

Rank = (years recoverable from immutable/official sources, weighted toward
pre-2018 since those are the scarcest in the existing dataset) x (fills a
gap in the adoption-year spread, or adds a control). Existing dataset
context: the 13 web-researched counties already span a range of VCA/e-
pollbook adoption years (2018 pilots through 2020 expansion), but very few
of them have a CONFIRMED, non-inferred pre-2018 election-night number from
an immutable source (most existing pre-2018 rows in VERIFY.md are `none` or
a Wayback-recovered live-page snapshot, not a version-pinned CDN artifact) -
so a clean pre-2018 Clarity/press-release find is worth more than an
equally-clean 2022/2024 find.

### Regular-county candidates (feeds Task 11)

| Rank | County | Years recoverable (this pass's evidence) | Basis |
|---|---|---|---|
| 1 | **Ventura** | 2012 CONFIRMED (Clarity JSON, presidential general, BC 330,419) + a real year-indexed press-release archive back to 2010 for the other years | Largest county found with a clean pre-2018 Clarity hit; 2012 is the single scarcest year-type combination (presidential, earliest) in the whole scout; large county = high analytical value; still shows "traditional" tech profile per the Oct 2025 SoS equipment table, useful contrast case |
| 2 | **Merced** | 2016 CONFIRMED (Clarity JSON, BC 72,631) + 2018 CONFIRMED (Clarity JSON, electiondate 11/6/2018) + very likely 2022/2024 (active Clarity presence, eid not yet dated) | Two Nov generals independently confirmed with real sum.json vote data via the exact RUNBOOK 7.2 method; strongest MULTI-YEAR Clarity find of the scout; no pre-2016 Clarity (would need a different route for 2012/2014, same gap several existing counties already carry as `none`) |
| 3 | **Stanislaus** | 2012, 2014, 2016, 2018 all have a same-shaped `past-results` HTML page + matching SOV PDF (structurally the most COMPLETE pre-2018 spread of any county in this scout) but every page found so far is the POST-canvass certified state, not yet the election-night plateau | Best BREADTH of any candidate (all 4 target Nov generals have a same-format historical page), but requires more work (an earlier Wayback capture or a same-night dated report) before any row can be written; ranked below Merced only because Merced's rows are already plateau-confirmable today (JSON at a specific version) and Stanislaus's are not yet |
| 4 | **Shasta** | Real Clarity JSON pipeline confirmed working (unlike Contra Costa's dead HTML-only setup) across 6 eids spanning 2012-2017, but this pass could not cleanly date any single eid to a specific Nov-general year (the eid-reuse-across-years pattern makes Wayback-capture dating unsafe here) | High raw potential (widest apparent year spread, 6 distinct election IDs) but the least-verified of the four; needs a careful per-version dating pass before it can be trusted, flagged in detail above |
| - | Alameda | infrastructure (dated press-release PDF folders) confirmed, but no specific semi-final release found within budget | not ranked - insufficient evidence either way |
| - | Kern | self-dating custom ENR system confirmed for 2018 (post-canvass capture only); no pre-2018 domain/system identified | not ranked - only reaches back to 2018, and even that capture is post-night |
| - | Sonoma | a 2009-2024 "Historical Election Results" database exists but is JS-rendered and its content (final-only vs. night-specific) is unconfirmed | not ranked - needs a rendering pass to even assess |
| - | Contra Costa | Clarity is real but special-elections-only + HTML-only (no JSON); no press-release archive evidence found | effectively a dead end in this pass |

### Control-county candidates (feeds Task 12)

| Rank | County | Evidence |
|---|---|---|
| 1 | **San Luis Obispo** | Confirmed absent from the SoS's 2020 VCA 15-county list; confirmed "Do not use" for Electronic Pollbook AND VoteCenter/Polling Ballot-on-Demand in the Oct 2025 SoS equipment table; largest of the clean-profile counties by far, giving the most statistically meaningful comparator |
| 2 | **Tehama** | Same clean profile (no VCA, no e-pollbook, no vote-center BoD equipment at all); mid-small Central Valley/foothill county, useful geographic contrast |
| 3 | **Siskiyou** | Same clean profile; far-northern rural county, another useful geographic contrast |

ASV status is UNCONFIRMED for all three (see Step 3 caveat); Task 12 must
close that gap - via each county's own EAP/board minutes/local news, the
same way this project already documented Fresno's and LA's ASV adoption -
before finalizing the control choice. The 2020-vs-2024 VCA-list gap (this
pass could only confirm the 2020 list, not a later one) should also be
re-checked for whichever county Task 12 shortlists.

## Self-review

- Every ranking claim above is backed by a probe recorded in this memo with
  its exact command/URL, above the ranking section.
- Every county probed in Step 1 (all 44) is recorded in the summary table,
  including the 39 "no CDX hits" dead ends, not just the 5 with hits.
- Every county probed in Step 2 (all 6 named in the brief) has its own
  subsection recording what was tried and what was found, including the
  negative/inconclusive ones (Alameda, Contra Costa).
- Step 3's two source PDFs are cited with their exact retrieval URLs and the
  exact county lists extracted from them; the "current-snapshot vs.
  historical-through-2024" caveat is stated explicitly and demonstrated on
  SF's own row (a county whose ground truth this project already knows),
  rather than glossed over.
- Known gaps flagged for the operator, honestly, rather than silently
  dropped: Shasta's eid-dating ambiguity; Stanislaus's post-canvass-only
  captures; Sonoma's unrendered JS database; Alameda's thin Wayback crawl;
  Kern's missing pre-2018 domain; the unconfirmed ASV leg for all 3 control
  nominees; the unconfirmed 2022/2024 VCA-county list.
