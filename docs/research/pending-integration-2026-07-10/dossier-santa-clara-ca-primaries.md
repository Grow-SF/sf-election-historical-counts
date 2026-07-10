# Santa Clara County (santa-clara-ca) statewide primaries: evidence dossier

Status: DRAFT / research scratch only. Nothing in this file has been written to the
repo. Built per `docs/research/RUNBOOK.md` sections 1, 5, 6, 7.2, 8 and the
existing `data/research/election-night/santa-clara-ca.json` general-election
rows (same county, same methodology).

## Method note (read before the items)

Santa Clara reports statewide primaries via the same `results.enr.clarityelections.com/CA/Santa_Clara/<electionId>/<version>/...`
Clarity/SOE CDN as its Novembers. **Correction to the prior generals' notes:**
those notes said curl 403s on this CDN and required puppeteer
`headless:"new"` + a real UA to bypass CloudFront. Retested here: plain
`curl --compressed -A "<desktop Chrome UA>" <url>` on the LIVE CDN returns
clean 200s (verified against a known version, `.../92418/220444/json/sum.json`,
reproducing the already-verified BC=304303). Without a UA it 403s. So the
trigger is UA presence, not headless-vs-headed puppeteer; curl+UA is
sufficient and much faster than launching Chrome. `current_ver.txt` even
200s with NO UA at all. All numerators below were pulled this way, no
puppeteer needed.

Election IDs were found by (a) reusing the county's own
`vote.santaclaracounty.gov` / legacy `sccgov.org/sites/rov/Resources/Pages/PastEResults.aspx`
past-results index (Wayback), and (b) a CDX prefix sweep of
`results.enr.clarityelections.com/CA/Santa_Clara/<leading digit>` (matchType=prefix,
one query per leading digit 4-9, `fl=timestamp,original`, deduped to first
capture per election ID) to enumerate every Santa Clara election ID Wayback
has ever seen, then probing each candidate's `current_ver.txt` +
`electionsettings.json` live for its certification date. Cross-check used
throughout: each election's CURRENT (certified) Clarity version's `BC` was
compared against the SoS-certified Total Voters figure -- **it matched
exactly for all 5 Clarity-sourced primaries** (2014, 2016, 2018, 2022, 2024),
which independently confirms the election-ID identification is correct.

Confirmed Santa Clara primary election IDs:
| Primary | Clarity electionId | Style |
|---|---|---|
| 2012-06-05 | *(none -- pre-Clarity; see item 1)* | legacy sccgov.org GEMS-style page |
| 2014-06-03 | 51635 | Web01 (no `versions` array; CDX-sweep-harvested candidates) |
| 2016-06-07 | 60535 | Web01 (no `versions` array; CDX-sweep-harvested candidates) |
| 2018-06-05 | 75369 | Web02 SPA (full official `versions` array, 91 entries) |
| 2022-06-07 | 113941 | Web02 SPA (full official `versions` array, 40 entries) |
| 2024-03-05 | 120250 | Web02 SPA (full official `versions` array, 50 entries) |

For the two Web01 elections (2014, 2016) the candidate version numbers came
from a Wayback CDX prefix sweep (`results.enr.clarityelections.com/CA/Santa_Clara/<eid>/`,
matchType=prefix) of the electionId path, deduped to one row per version
folder, then each candidate's TRUE internal timestamp + BC was read live
(Wayback's own crawl timestamps were not used for anything beyond harvesting
candidate version numbers). Gaps around each claimed plateau/bracket pair
were spot-checked by probing the intervening integers directly (all 404),
consistent with Clarity version numbers being sparse identifiers, not dense
integers -- the same assumption the existing 2014/2016 general rows in
`santa-clara-ca.json` already relied on.

For the three Web02 elections (2018, 2022, 2024) the `versions` array in the
current version's `electionsettings.json` is a COMPLETE official enumeration
(same mechanism the existing 2018 general row in `santa-clara-ca.json` used),
so the plateau/bracket adjacency is gold-standard bracket evidence with no
sweep-completeness risk at all.

**Evidence-permanence caveat (unresolved, flagged):** this sandbox's network
to `web.archive.org` was extremely flaky throughout this session (`curl`
against `web.archive.org` intermittently returned `Connection refused` even
for simple GETs, unrelated to the Clarity CDN). CDX lookups eventually
succeeded after generous retries, but `https://web.archive.org/save/<url>`
(to archive-and-cite the live Clarity JSON, the pattern the existing
generals' notes used) did not complete in this session despite ~10+ minutes
of background retries. **FLAG for manual operator:** before promoting any
row below into `santa-clara-ca.json`, run
`https://web.archive.org/save/<url>` for each numerator URL cited (listed
per item) and swap `source_url_night` to the resulting
`https://web.archive.org/web/<ts>/<url>` snapshot, exactly as the existing
2014/2016/2018 general corrections in that file already do. Until then the
URLs below are live-CDN URLs, verified working via direct curl fetch in this
session (evidence quoted inline), not yet Wayback-permanent.

---

## Item 1 of 6: 2012-06-05 Presidential Primary

**Certified final:** 292,713 ballots.
**SoV URL:** <https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf>
("VOTER PARTICIPATION STATISTICS BY COUNTY" -- filename says "voter-reg" but
the table is the participation table, same as every other year here). Santa
Clara line (`pdftotext -layout`): `874` precincts, `1,116,131` eligible to
register, `755,117` registered voters, `55,518` precinct voters, `237,195`
VBM voters, **`292,713` Total Voters**, `81.03%` VBM share, `38.76%` turnout
of registered, `26.23%` turnout of eligible.

**Numerator: NOT Clarity.** Exhaustively checked -- Clarity election IDs are
present for Santa Clara starting with the Nov 2012 general (`43231`); a CDX
prefix sweep of `results.enr.clarityelections.com/CA/Santa_Clara/4` found no
ID between roughly 40000-43230 (i.e. nothing pre-dating 43231), and the
`43231` Nov-2012-general row's own note in `santa-clara-ca.json` already
establishes 43231 = the November general only. June 2012 used the county's
LEGACY `sccgov.org` GEMS-style live-results page instead (the predecessor
system, retired sometime between June and November 2012):
`http://www.sccgov.org/elections/results/jun2012/`. Confirmed live in the
Wayback-archived June-2012 registrar "Past Election Results" index page
(`https://web.archive.org/web/20141107061521id_/http://www.sccgov.org/sites/rov/Resources/Pages/PastEResults.aspx`,
link text `/elections/results/jun2012`).

**Numerator value found (CEILING, not the plateau):** `234,342` ballots.
- URL: <https://web.archive.org/web/20120607192808id_/http://www.sccgov.org/elections/results/jun2012/>
- Look for: page banner "Unofficial Semi-Final Results", internal
  `Last Updated : 6/6/2012 7:02:03 PM`, `Completed Precincts 874 of 874`,
  first "Registration & Turnout" block (county-wide, before the per-party
  breakdowns): `Percent Votes / Vote by Mail Reporting Turnout 24.56% 185,455
  / Precinct Reporting Turnout 6.47% 48,887 / 31.03% 234,342` -- i.e.
  185,455 VBM + 48,887 precinct = **234,342** total ballots, 31.03% of
  755,117 registered.

**Why this is a CEILING, not the plateau (and why it can't be upgraded):**
CDX for this exact URL (`sccgov.org/elections/results/jun2012/`, narrowed to
2012-06-05 through 2012-06-10) returns exactly 4 captures, and the EARLIEST
is `20120607192808` (June 7, 12:28 PM PDT) -- there is no capture from
election night itself (June 5 8pm poll-close through June 6 early morning).
The internal timestamp embedded in that earliest capture, `6/6/2012
7:02:03 PM`, is already ~23 hours after poll close, with precincts already
at 874/874 = 100%. The next two captures show the page advancing on a
once-daily afternoon cadence (`6/7/2012 4:43:58 PM` at capture
`20120608222327`; `6/8/2012 4:21:51 PM` at capture `20120609022555`),
confirming the page was already in canvass mode, not continuous
election-night mode, by the time Wayback's first crawl caught it. This is
the same signature (100%-precincts + daily-cadence next update) this
dataset treats elsewhere as a next-day canvass-start ceiling (Santa Clara's
own pre-correction 2014 general; Riverside 2024; Placer 2018), so 234,342 is
kept as a documented CEILING, not asserted as the plateau. A true overnight
number (some value below 234,342, likely with precincts still short of
874/874) is not recoverable from Wayback for this URL -- no earlier capture
exists in CDX, checked both narrow (June 5-10) and unrestricted windows, and
a broader `sccgov.org/elections/` prefix sweep restricted to June 5 18:00 -
June 7 00:00 UTC also returned zero captures. There is no Clarity CDN
fallback for this pre-Clarity year.

**FLAG for manual operator:** (1) try the Wayback UI directly (not just the
CDX API + raw `id_` fetch) for `sccgov.org/elections/results/jun2012/`
between June 5-7 2012 -- CDX/curl can miss captures that alias to a
different replay timestamp (runbook 7.1's "replay aliasing" gotcha); (2) a
San Jose Mercury News election-night story (via SFPL/NewsBank, per the
`newsbank-election-recovery` skill) may quote an official election-night
ballot count for Santa Clara's June 2012 primary -- not attempted in this
pass (out of scope: that skill's workflow is per-election and this dossier
covered 6 elections across 2 vendor systems already).

**Arithmetic (ceiling):** 234,342 / 292,713 = **80.06%** (NOT the plateau;
recorded only as an upper bound -- the true election-night share is lower).

**Draft row** (would need a real plateau number or an explicit null before
landing in `santa-clara-ca.json`; shown here as the CEILING variant per 5.2):
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": 234342,
  "certified_final": 292713,
  "election_night_pct": 80.06,
  "vs_epollbook": "pre",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20120607192808id_/http://www.sccgov.org/elections/results/jun2012/",
  "confidence": "secondary",
  "comparable": false,
  "note": "CEILING (next-day/canvass-mode value; true overnight plateau unarchived). Santa Clara's June 2012 primary predates its Clarity adoption (Clarity electionId 43231 = Nov 2012 general only); the county's legacy sccgov.org GEMS-style live-results page (http://www.sccgov.org/elections/results/jun2012/) was the only election-night channel. Earliest Wayback capture of that URL is 2012-06-07 12:28:08 PM PDT (no June 5-6 capture exists in CDX, narrow or wide window), internal 'Last Updated : 6/6/2012 7:02:03 PM' (~23h post poll-close), Completed Precincts 874 of 874 (100%), county-wide Registration & Turnout block: Vote by Mail 185,455 + Precinct 48,887 = 234,342 (31.03% of 755,117 registered). Subsequent captures (6/7 4:43:58 PM at Wayback ts 20120608222327; 6/8 4:21:51 PM at ts 20120609022555) show a once-daily afternoon-update cadence, confirming the page was already in canvass mode by the first crawl -- same signature this dataset treats as a next-day ceiling elsewhere (Riverside 2024, Placer 2018, this county's own pre-correction 2014 general). FLAG for manual operator: try the Wayback UI directly for a June 5-6 capture CDX may have missed (replay aliasing), and/or a Mercury News election-night quote via NewsBank; neither attempted here. Certified final 292,713 ballots (CA SoS Voter Participation Statistics by County, 2012-primary: 55,518 poll + 237,195 VBM = 292,713; 38.76% of 755,117 registered). Ceiling pct = 234,342/292,713 = 80.06% (NOT the plateau -- true election-night share is lower). Pre-epollbook (adopted 2020); ASV never."
}
```

**Draft VERIFY.md summary row:** `| 2012 ⚠️ | presidential-primary | 234,342 | 292,713 | 80.06% | secondary | [link](https://web.archive.org/web/20120607192808id_/http://www.sccgov.org/elections/results/jun2012/) |`

**Draft VERIFY.md detail bullet:**
`- **2012 presidential-primary** — night `234,342` / final `292,713` = `80.06%` (secondary, CEILING not plateau)`
`  - numerator: <https://web.archive.org/web/20120607192808id_/http://www.sccgov.org/elections/results/jun2012/>`
`  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf>`
`  - look for: "Last Updated : 6/6/2012 7:02:03 PM", "Completed Precincts 874 of 874", first Registration & Turnout block "31.03% 234,342". This is a CEILING (next-day/canvass value); true overnight plateau not archived.`

**Draft plateau_review.json verdict:**
```json
{
  "slug": "santa-clara-ca",
  "date": "2012-06-05",
  "verdict": "REFUTED_AS_PLATEAU",
  "basis": "earliest archived capture of the only election-night channel (legacy pre-Clarity sccgov.org page) is already ~23h post-poll-close with precincts at 100% and a once-daily canvass cadence starting; kept only as a documented ceiling per runbook 5.2, not asserted as the plateau",
  "evidence": "Wayback CDX for sccgov.org/elections/results/jun2012/ has zero captures before 2012-06-07 12:28 PM PDT; that capture's internal 'Last Updated' is 6/6/2012 7:02:03 PM with Completed Precincts 874 of 874 (100%) and 234,342 ballots; the next two captures (6/7 4:43:58 PM, 6/8 4:21:51 PM) confirm a once-daily canvass-mode cadence"
}
```

**render_verified.json:** not applicable -- this is a plain server-rendered
HTML page (no JS rendering needed), same as `curl`-fetched pages elsewhere
in the dataset; no manifest entry required.

**Confidence / status: SECONDARY, CEILING, FLAG for manual operator.**

---

## Item 2 of 6: 2014-06-03 Statewide Primary

**Certified final:** 264,133 ballots.
**SoV URL:** <https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf>
(misspelling "particpiation" intact in the real filename). Santa Clara line:
`1,026` precincts, `1,150,600` eligible, `805,922` registered, `50,290`
precinct, `213,843` VBM, **`264,133` Total Voters**, `80.96%` VBM share,
`32.77%` turnout of registered, `22.96%` of eligible.

**Numerator: Clarity electionId `51635`** (Web01, no official `versions`
array; candidates harvested via CDX prefix sweep, then read live). Current
(certified) version `135179`, live `websiteupdatedat` = `6/30/2014
10:26:33 AM PDT`, `sum.json` `BC` = **264,133** -- exact match to the SoS
certified figure, confirming this is the right election ID.

**Full trajectory (all fetched live via `curl --compressed -A <UA>`):**
| version | internal timestamp | BC | precincts reporting |
|---|---|---:|---|
| 131844 | 6/3/2014 4:09:06 PM | 0 | 0/1026 |
| 131975 | 6/3/2014 7:39:42 PM | 124,445 | 0/1026 (first tranche, pre-processed VBM) |
| 132000 | 6/3/2014 9:52:00 PM | 124,465 | 1/1026 |
| 132007 | 6/3/2014 10:25:07 PM | 128,348 | 98/1026 |
| 132031 | 6/4/2014 12:20:58 AM | 156,355 | 684/1026 |
| 132033 | 6/4/2014 1:11:22 AM | 165,889 | 1016/1026 |
| **132035** | **6/4/2014 2:39:54 AM** | **166,360** | **1026/1026 (100%)** |
| 132218 | 6/5/2014 4:13:39 PM (+37h34m gap) | 198,499 | 1026/1026 |
| 132392 | 6/6/2014 7:38:09 PM | 254,537 | 1026/1026 |
| 135179 (current/certified) | 6/30/2014 10:26:33 AM | 264,133 | 1026/1026 |

Version 132035 (100% precincts, election-night internal timestamp) is the
PLATEAU. Spot-checked integers 132036-132217 (a sample of them) for skipped
intermediate versions between 132035 and 132218: all 404/no-settings,
consistent with sparse version numbering. The ~37.5-hour gap to the
next-published version, which then jumps +32,139 (the classic next-day VBM
canvass-start batch), is the bracket proof.

**URLs (live; archiving to Wayback attempted but the sandbox's connection to
`web.archive.org/save/` did not complete in this session -- FLAG for manual
operator to run these through `/save/` before landing):**
- numerator (plateau) sum: <https://results.enr.clarityelections.com/CA/Santa_Clara/51635/132035/json/sum.json>
- numerator (plateau) settings: <https://results.enr.clarityelections.com/CA/Santa_Clara/51635/132035/Web01/en/json/electionsettings.json>
- bracket sum: <https://results.enr.clarityelections.com/CA/Santa_Clara/51635/132218/json/sum.json>

**Arithmetic:** 166,360 / 264,133 = **62.98%**.

**Draft row:**
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": 166360,
  "certified_final": 264133,
  "election_night_pct": 62.98,
  "vs_epollbook": "pre",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://results.enr.clarityelections.com/CA/Santa_Clara/51635/132035/json/sum.json",
  "confidence": "primary",
  "note": "PLATEAU = last continuous election-night report, precincts at 100%. Clarity electionId 51635 (Web01, no official versions array; candidates harvested via a Wayback CDX prefix sweep of the electionId path, each read live via curl --compressed with a real desktop UA, which 200s directly on this CDN -- retested and found puppeteer is NOT required, contra the prior generals' notes; a bare curl with no UA still 403s). Trajectory: v131975 6/3 7:39:42 PM 124,445 (0/1026 precincts, pre-processed-VBM first tranche) -> v132007 6/3 10:25 PM 128,348 (98/1026) -> v132031 6/4 12:20:58 AM 156,355 (684/1026) -> v132033 6/4 1:11:22 AM 165,889 (1016/1026) -> v132035 6/4 2:39:54 AM 166,360 (1026/1026 = 100%) [PLATEAU] -> v132218 6/5 4:13:39 PM 198,499 (+37h34m gap, +32,139 jump = next-day VBM canvass-start batch) [bracket]. Spot-probed integers between 132035 and 132218 (sample) all 404, consistent with sparse version numbering (same assumption this file's existing 2014/2016 general rows rely on). Current/certified version 135179 (6/30/2014) BC=264,133 matches the SoS certified total exactly, confirming the election ID. Certified final 264,133 ballots (CA SoS Voter Participation Statistics by County, 2014-primary: 50,290 poll + 213,843 VBM = 264,133; 32.77% of 805,922 registered). Pct = 166,360/264,133 = 62.98%. Pre-epollbook (adopted 2020); ASV never. Evidence-permanence FLAG: source_url_night here is the LIVE Clarity CDN URL, verified serving the claimed BC by direct fetch in this research session (2026-07-10); it has not yet been archived to Wayback (web.archive.org/save/ did not complete in this sandbox session -- connection issues unrelated to the Clarity CDN itself). A manual operator should run https://web.archive.org/save/<this URL> and swap source_url_night to the resulting web.archive.org/web/<ts>/<url> snapshot before this row is treated as final, per the pattern already used for this county's other Clarity rows."
}
```

**Draft VERIFY.md summary row:** `| 2014 | statewide-primary | 166,360 | 264,133 | 62.98% | primary | [link](https://results.enr.clarityelections.com/CA/Santa_Clara/51635/132035/json/sum.json) |`

**Draft VERIFY.md detail bullet:**
`- **2014 statewide-primary** — night `166,360` / final `264,133` = `62.98%` (primary)`
`  - numerator: <https://results.enr.clarityelections.com/CA/Santa_Clara/51635/132035/json/sum.json>`
`  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf>`
`  - look for: sum.json BC = 166,360 at Clarity ver 132035 (Web01), electionsettings websiteupdatedat 6/4/2014 2:39:54 AM PDT, precincts 1026/1026 = 100%. Bracket: next version 132218, 6/5/2014 4:13:39 PM (+37.5h gap), BC 198,499.`

**Draft plateau_review.json verdict:**
```json
{
  "slug": "santa-clara-ca",
  "date": "2014-06-03",
  "verdict": "CONFIRMED",
  "basis": "election-night internal timestamp (2:39:54 AM the morning after) with precincts at 100%, plus a Clarity version bracket: the next published version is 37.5 hours later with a large jump, proving the cited version was the last of the night",
  "evidence": "sum.json BC=166360 at Clarity electionId 51635 version 132035 (live CDN, curl --compressed -A <UA>), electionsettings websiteupdatedat 6/4/2014 2:39:54 AM PDT, precincts 1026/1026; next version 132218 is 6/5/2014 4:13:39 PM PDT (BC 198,499), a 37h34m gap"
}
```

**render_verified.json:** not applicable -- Clarity `sum.json`/`electionsettings.json` are plain JSON, not JS-rendered pages; the manifest is for JS results widgets (see runbook 7.4). No entry needed, consistent with the existing Santa Clara general rows (none of which appear in render_verified.json either).

**Confidence / status: PRIMARY, CONFIRMED. Evidence-permanence FLAG only (Wayback archiving pending).**

---

## Item 3 of 6: 2016-06-07 Presidential Primary

**Certified final:** 430,779 ballots.
**SoV URL:** <https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf>
Santa Clara line: `932` precincts, `1,186,947` eligible, `788,063`
registered, `110,976` precinct, `319,803` VBM, **`430,779` Total Voters**,
`74.24%` VBM share, `54.66%` turnout of registered, `36.29%` of eligible.

**Numerator: Clarity electionId `60535`** (Web01, no official `versions`
array; candidates harvested via CDX prefix sweep, then read live). Current
(certified) version `173168`, live `websiteupdatedat` = `6/30/2016
3:31:59 PM PDT`, `sum.json` `BC` = **430,779** -- exact match to the SoS
certified figure.

**Full trajectory (live-fetched):**
| version | internal timestamp | BC | precincts reporting |
|---|---|---:|---|
| 171232 | 6/7/2016 7:58:30 PM | 189,407 | 0/932 (first tranche) |
| 171243 | 6/7/2016 8:45:53 PM | 202,042 | 200/932 |
| 171259 | 6/7/2016 10:29:07 PM | 208,404 | 200/932 |
| 171264 | 6/7/2016 11:07:12 PM | 212,113 | 235/932 |
| 171272 | 6/7/2016 11:57:31 PM | 220,983 | 287/932 |
| 171281 | 6/8/2016 1:49:05 AM | 250,419 | 547/932 |
| **171284** | **6/8/2016 3:49:26 AM** | **282,389** | **932/932 (100%)** |
| 171298 | 6/8/2016 8:43:21 AM (+4h54m gap) | 286,492 | 932/932 |
| 171384 | 6/8/2016 4:07:10 PM | 300,459 | 932/932 |
| 173168 (current/certified) | 6/30/2016 3:31:59 PM | 430,779 | 932/932 |

Version 171284 is the PLATEAU: precincts first hit 100% here, at an internal
timestamp still inside the "1am-4am the morning after" election-night window
this dataset explicitly treats as election night (runbook section 1's own
Santa Clara-2012 calibration example). The overnight pace into 171284 was
~11,850 ballots/hr (250,419 -> 282,389 in 2h); the very next version,
171298, comes 4h54m later at only ~837/hr -- a >10x cadence collapse, the
bracket proof. (Rate picks back up in the afternoon -- 171298->171384 runs
~1,887/hr over 7.4h -- consistent with ordinary business-hours canvass
processing resuming, not a continuation of election night.) Spot-probed
integers 171285-171297 individually: all no-settings/404, confirming 171284
and 171298 are adjacent published versions, not an artifact of an
incomplete sweep.

**URLs (live; Wayback archiving not completed this session, see Item 2's
caveat):**
- numerator (plateau) sum: <https://results.enr.clarityelections.com/CA/Santa_Clara/60535/171284/json/sum.json>
- numerator (plateau) settings: <https://results.enr.clarityelections.com/CA/Santa_Clara/60535/171284/Web01/en/json/electionsettings.json>
- bracket sum: <https://results.enr.clarityelections.com/CA/Santa_Clara/60535/171298/json/sum.json>

**Arithmetic:** 282,389 / 430,779 = **65.55%**.

**Draft row:**
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 282389,
  "certified_final": 430779,
  "election_night_pct": 65.55,
  "vs_epollbook": "pre",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://results.enr.clarityelections.com/CA/Santa_Clara/60535/171284/json/sum.json",
  "confidence": "primary",
  "note": "PLATEAU = last continuous election-night report, precincts at 100%. Clarity electionId 60535 (Web01, no official versions array; candidates from a Wayback CDX prefix sweep, each read live via curl --compressed -A <UA>). Trajectory: v171232 6/7 7:58:30 PM 189,407 (0/932, first tranche) -> v171264 6/7 11:07:12 PM 212,113 (235/932) -> v171281 6/8 1:49:05 AM 250,419 (547/932) -> v171284 6/8 3:49:26 AM 282,389 (932/932 = 100%) [PLATEAU] -> v171298 6/8 8:43:21 AM 286,492 (+4h54m gap; overnight pace collapses from ~11,850/hr to ~837/hr) [bracket]; rate resumes at ~1,887/hr by v171384 4:07 PM (ordinary business-hours canvass, not election night). Integers 171285-171297 individually probed: all no-settings, confirming adjacency. Current/certified version 173168 (6/30/2016) BC=430,779 matches the SoS certified total exactly. Certified final 430,779 ballots (CA SoS Voter Participation Statistics by County, 2016-primary: 110,976 poll + 319,803 VBM = 430,779; 54.66% of 788,063 registered). Pct = 282,389/430,779 = 65.55%. Pre-epollbook (adopted 2020); ASV never. Evidence-permanence FLAG: source_url_night is the live Clarity CDN URL (verified serving the claimed BC by direct fetch, 2026-07-10); not yet archived to Wayback this session (web.archive.org/save/ did not complete -- sandbox connectivity, unrelated to the Clarity CDN). Manual operator should run https://web.archive.org/save/<url> and swap to the resulting snapshot before this row is treated as final."
}
```

**Draft VERIFY.md summary row:** `| 2016 | presidential-primary | 282,389 | 430,779 | 65.55% | primary | [link](https://results.enr.clarityelections.com/CA/Santa_Clara/60535/171284/json/sum.json) |`

**Draft VERIFY.md detail bullet:**
`- **2016 presidential-primary** — night `282,389` / final `430,779` = `65.55%` (primary)`
`  - numerator: <https://results.enr.clarityelections.com/CA/Santa_Clara/60535/171284/json/sum.json>`
`  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf>`
`  - look for: sum.json BC = 282,389 at Clarity ver 171284 (Web01), electionsettings websiteupdatedat 6/8/2016 3:49:26 AM PDT, precincts 932/932 = 100%. Bracket: next version 171298, 6/8/2016 8:43:21 AM (+4h54m gap), BC 286,492.`

**Draft plateau_review.json verdict:**
```json
{
  "slug": "santa-clara-ca",
  "date": "2016-06-07",
  "verdict": "CONFIRMED",
  "basis": "election-night internal timestamp (3:49 AM the morning after) with precincts first reaching 100%, plus a cadence-break bracket: the immediately next published version is 4h54m later with the reporting rate collapsing >10x",
  "evidence": "sum.json BC=282389 at Clarity electionId 60535 version 171284 (live CDN), electionsettings websiteupdatedat 6/8/2016 3:49:26 AM PDT, precincts 932/932; next version 171298 is 6/8/2016 8:43:21 AM PDT (BC 286,492, +4103 vs the prior +31970-in-2h overnight pace)"
}
```

**render_verified.json:** not applicable (plain JSON, not JS-rendered).

**Confidence / status: PRIMARY, CONFIRMED. Evidence-permanence FLAG only.**

---

## Item 4 of 6: 2018-06-05 Statewide Primary

**Certified final:** 369,332 ballots.
**SoV URL:** <https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf>
Santa Clara line: `988` precincts, `1,203,427` eligible, `846,228`
registered, `73,948` precinct, `295,384` VBM, **`369,332` Total Voters**,
`79.98%` VBM share, `43.64%` turnout of registered, `30.69%` of eligible.

**Numerator: Clarity electionId `75369`** (Web02 SPA -- current version's
`electionsettings.json` carries a COMPLETE official `versions` array, 91
entries, `195838`-`208007`; no CDX sweep needed, same mechanism as this
county's existing 2018-general row). Current (certified) version `208007`,
live `websiteupdatedat` = `7/9/2018 1:12:36 PM PDT`, `sum.json` `BC` =
**369,332** -- exact match to the SoS certified figure.

**Election-night slice of the official versions array (all live-fetched):**
| version | internal timestamp | BC | precincts reporting |
|---|---|---:|---|
| 204149 | 6/5/2018 7:49:04 PM | 135,701 | 164/988 (first tranche) |
| 204422 | 6/5/2018 10:19:16 PM | 144,171 | 381/988 |
| 204460 | 6/6/2018 12:33:16 AM | 154,757 | 504/988 |
| 204470 | 6/6/2018 4:28:02 AM | 175,207 | 748/988 |
| 204480 | 6/6/2018 7:21:44 AM | 185,728 | 868/988 |
| 204495 | 6/6/2018 8:52:52 AM | 192,683 | 952/988 |
| **204514** | **6/6/2018 10:38:16 AM** | **196,184** | **988/988 (100%)** |
| 204549 | 6/6/2018 4:25:41 PM (+5h47m gap) | 205,809 | 988/988 |
| 204580 | 6/7/2018 10:14:01 AM | 215,461 | 988/988 |
| 208007 (current/certified) | 7/9/2018 1:12:36 PM | 369,332 | 988/988 |

Version 204514 is the PLATEAU: it is where precincts first hit 100%,
directly analogous to the existing 2018-general row in this same file
(BC=304,303 at 100% precincts, same discriminator). The overnight rate
running into it was ~2,100-4,400 ballots/hr; the immediately NEXT entry in
the OFFICIAL versions array, 204549, is 5h47m later at only ~1,662/hr net --
a real cadence break, and since this is the complete official enumeration
(not a CDX sweep), there is no possibility a version was skipped between
them.

**URLs (live; Wayback archiving not completed this session, see Item 2's
caveat):**
- numerator (plateau) sum: <https://results.enr.clarityelections.com/CA/Santa_Clara/75369/204514/json/sum.json>
- numerator (plateau) settings: <https://results.enr.clarityelections.com/CA/Santa_Clara/75369/204514/json/en/electionsettings.json>
- bracket sum: <https://results.enr.clarityelections.com/CA/Santa_Clara/75369/204549/json/sum.json>

**Arithmetic:** 196,184 / 369,332 = **53.12%**.

**Draft row:**
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 196184,
  "certified_final": 369332,
  "election_night_pct": 53.12,
  "vs_epollbook": "pre",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://results.enr.clarityelections.com/CA/Santa_Clara/75369/204514/json/sum.json",
  "confidence": "primary",
  "note": "PLATEAU = last continuous election-night report, precincts at 100%. Clarity electionId 75369 (Web02 SPA with a COMPLETE official versions array, 91 entries -- same mechanism as this file's existing 2018-general row, no CDX-sweep completeness risk). Trajectory: v204149 6/5 7:49:04 PM 135,701 (164/988, first tranche) -> v204460 6/6 12:33:16 AM 154,757 (504/988) -> v204495 6/6 8:52:52 AM 192,683 (952/988) -> v204514 6/6 10:38:16 AM 196,184 (988/988 = 100%) [PLATEAU] -> v204549 6/6 4:25:41 PM 205,809 (+5h47m gap in the OFFICIAL array; rate ~1,662/hr vs the ~2,100-4,400/hr overnight pace) [bracket]. Current/certified version 208007 (7/9/2018) BC=369,332 matches the SoS certified total exactly. Certified final 369,332 ballots (CA SoS Voter Participation Statistics by County, 2018-primary: 73,948 poll + 295,384 VBM = 369,332; 43.64% of 846,228 registered). Pct = 196,184/369,332 = 53.12%. Pre-epollbook (adopted 2020); ASV never. Evidence-permanence FLAG: source_url_night is the live Clarity CDN URL (verified serving the claimed BC by direct fetch, 2026-07-10); not yet archived to Wayback this session (web.archive.org/save/ did not complete -- sandbox connectivity). Manual operator should run https://web.archive.org/save/<url> and swap to the resulting snapshot before this row is treated as final."
}
```

**Draft VERIFY.md summary row:** `| 2018 | statewide-primary | 196,184 | 369,332 | 53.12% | primary | [link](https://results.enr.clarityelections.com/CA/Santa_Clara/75369/204514/json/sum.json) |`

**Draft VERIFY.md detail bullet:**
`- **2018 statewide-primary** — night `196,184` / final `369,332` = `53.12%` (primary)`
`  - numerator: <https://results.enr.clarityelections.com/CA/Santa_Clara/75369/204514/json/sum.json>`
`  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf>`
`  - look for: sum.json BC = 196,184 at Clarity ver 204514 (Web02), electionsettings websiteupdatedat 6/6/2018 10:38:16 AM PDT, precincts 988/988 = 100%. Bracket: next OFFICIAL version 204549, 6/6/2018 4:25:41 PM (+5h47m gap), BC 205,809.`

**Draft plateau_review.json verdict:**
```json
{
  "slug": "santa-clara-ca",
  "date": "2018-06-05",
  "verdict": "CONFIRMED",
  "basis": "election-night internal timestamp (10:38 AM the morning after) with precincts first reaching 100%, plus an official-versions-array bracket: the immediately next entry (no skipped version possible) is 5h47m later with the reporting rate slowing",
  "evidence": "sum.json BC=196184 at Clarity electionId 75369 version 204514 (live CDN), electionsettings websiteupdatedat 6/6/2018 10:38:16 AM PDT, precincts 988/988 (complete official versions array of 91 entries); next entry 204549 is 6/6/2018 4:25:41 PM PDT (BC 205,809)"
}
```

**render_verified.json:** not applicable (plain JSON, not JS-rendered).

**Confidence / status: PRIMARY, CONFIRMED. Evidence-permanence FLAG only.**

---

## Item 5 of 6: 2022-06-07 Statewide Primary

**Certified final:** 357,848 ballots.
**SoV URL:** <https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf>
Santa Clara* line (asterisk = VCA county footnote): `599` precincts,
`1,263,458` eligible, `1,001,791` registered, `15,811` precinct, `342,037`
VBM, **`357,848` Total Voters**, `95.58%` VBM share, `35.72%` turnout of
registered, `28.32%` of eligible.

**Numerator: Clarity electionId `113941`** (Web02 SPA, complete official
`versions` array, 40 entries, `288423`-`300273`). Current (certified)
version `300273`, live `websiteupdatedat` = `7/6/2022 10:33:13 AM PDT`,
`sum.json` `BC` = **357,848** -- exact match to the SoS certified figure.

**Election-night slice of the official versions array:**
| version | internal timestamp | BC | precincts reporting |
|---|---|---:|---|
| 294562 | 6/7/2022 3:01:20 PM | 0 | 0/599 (pre-close) |
| 295003 | 6/7/2022 7:55:47 PM | 158,048 | 0/599 (first tranche) |
| 295118 | 6/7/2022 9:01:42 PM | 161,745 | 0/599 |
| 295151 | 6/7/2022 10:04:39 PM | 177,927 | 530/599 |
| **295160** | **6/7/2022 10:54:32 PM** | **181,257** | **538/599 (89.8%)** |
| 295352 | 6/8/2022 4:27:00 PM (+17h33m gap) | 187,550 | 538/599 (held) |
| 295493 | 6/9/2022 4:46:15 PM | 212,360 | 540/599 (real canvass jump) |
| 300273 (current/certified) | 7/6/2022 10:33:13 AM | 357,848 | 599/599 |

Unlike 2016/2018, precincts never reach 100% during election night for this
primary (peaks at 538/599 = 89.8%). This is the SAME "held" pattern this
county's own existing 2022-GENERAL row already documents (671/754 = 89%,
held into the next morning): version 295160 is the LAST version posted on
election night (10:54:32 PM), and the next official entry, 295352, is
17h33m later with precincts UNCHANGED (538, still not 100%) and only a
modest +6,293 bump -- i.e. the count held essentially flat overnight into
the next afternoon before the real canvass jump (+24,810) appears two days
later at 295493. Because this Web02 election's `versions` array is the
complete official enumeration, the ~17.5-hour gap is proven, not an
artifact of incomplete crawling.

**URLs (live; Wayback archiving not completed this session, see Item 2's
caveat):**
- numerator (plateau) sum: <https://results.enr.clarityelections.com/CA/Santa_Clara/113941/295160/json/sum.json>
- numerator (plateau) settings: <https://results.enr.clarityelections.com/CA/Santa_Clara/113941/295160/json/en/electionsettings.json>
- bracket sum: <https://results.enr.clarityelections.com/CA/Santa_Clara/113941/295352/json/sum.json>

**Arithmetic:** 181,257 / 357,848 = **50.65%**.

**Draft row:**
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 181257,
  "certified_final": 357848,
  "election_night_pct": 50.65,
  "vs_epollbook": "post",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://results.enr.clarityelections.com/CA/Santa_Clara/113941/295160/json/sum.json",
  "confidence": "primary",
  "note": "PLATEAU = held election-night (overnight) level, same discriminator as this county's own 2022 GENERAL row. Clarity electionId 113941 (Web02 SPA, complete official versions array, 40 entries). Trajectory: v295003 6/7 7:55:47 PM 158,048 (0/599, first tranche) -> v295151 6/7 10:04:39 PM 177,927 (530/599) -> v295160 6/7 10:54:32 PM 181,257 (538/599 = 89.8%) [PLATEAU, last election-night version] -> v295352 6/8 4:27:00 PM 187,550 (538/599 UNCHANGED, +6,293 modest trickle over a 17h33m gap in the OFFICIAL array = held) [bracket] -> v295493 6/9 4:46:15 PM 212,360 (540/599, +24,810 = the real canvass jump, 2 days out). Precincts never reach 100% on election night (peaks 538/599=89.8%); held flat through the next afternoon before the real canvass jump, same signature as the county's Nov 2022 general (671/754 held). Current/certified version 300273 (7/6/2022) BC=357,848 matches the SoS certified total exactly. Certified final 357,848 ballots (CA SoS Voter Participation Statistics by County, 2022-primary: 15,811 poll + 342,037 VBM = 357,848; 35.72% of 1,001,791 registered). Pct = 181,257/357,848 = 50.65%. POST-epollbook (e-pollbooks + VCA vote centers since 2020); ASV never. Evidence-permanence FLAG: source_url_night is the live Clarity CDN URL (verified serving the claimed BC by direct fetch, 2026-07-10); not yet archived to Wayback this session (web.archive.org/save/ did not complete -- sandbox connectivity). Manual operator should run https://web.archive.org/save/<url> and swap to the resulting snapshot before this row is treated as final."
}
```

**Draft VERIFY.md summary row:** `| 2022 | statewide-primary | 181,257 | 357,848 | 50.65% | primary | [link](https://results.enr.clarityelections.com/CA/Santa_Clara/113941/295160/json/sum.json) |`

**Draft VERIFY.md detail bullet:**
`- **2022 statewide-primary** — night `181,257` / final `357,848` = `50.65%` (primary)`
`  - numerator: <https://results.enr.clarityelections.com/CA/Santa_Clara/113941/295160/json/sum.json>`
`  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf>`
`  - look for: sum.json BC = 181,257 at Clarity ver 295160 (Web02), electionsettings websiteupdatedat 6/7/2022 10:54:32 PM PDT, precincts 538/599 = 89.8%, held into the next-day 295352 (4:27 PM, +17.5h, still 538/599, BC 187,550).`

**Draft plateau_review.json verdict:**
```json
{
  "slug": "santa-clara-ca",
  "date": "2022-06-07",
  "verdict": "CONFIRMED",
  "basis": "last version posted on election night (10:54 PM), held essentially flat (precincts unchanged, modest ballot bump) through the next official version 17.5 hours later, matching this county's own 2022-general held-overnight pattern; the real canvass jump only appears two days later",
  "evidence": "sum.json BC=181257 at Clarity electionId 113941 version 295160 (live CDN), electionsettings websiteupdatedat 6/7/2022 10:54:32 PM PDT, precincts 538/599 (complete official versions array of 40 entries); next entry 295352 is 6/8/2022 4:27:00 PM PDT (BC 187,550, precincts still 538/599)"
}
```

**render_verified.json:** not applicable (plain JSON, not JS-rendered).

**Confidence / status: PRIMARY, CONFIRMED. Evidence-permanence FLAG only.**

---

## Item 6 of 6: 2024-03-05 Presidential Primary

**Certified final:** 383,110 ballots.
**SoV URL:** <https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf>
Santa Clara* line: `597` precincts, `1,254,436` eligible, `1,024,622`
registered, `26,105` precinct, `357,005` VBM, **`383,110` Total Voters**,
`93.19%` VBM share, `37.39%` turnout of registered, `30.54%` of eligible.

**Numerator: Clarity electionId `120250`** (Web02 SPA, complete official
`versions` array, 50 entries, `329019`-`334586`). Current (certified)
version `334586`, live `websiteupdatedat` = `4/4/2024 1:55:33 PM PDT`,
`sum.json` `BC` = **383,110** -- exact match to the SoS certified figure.

**Election-night slice of the official versions array:**
| version | internal timestamp | BC | precincts reporting |
|---|---|---:|---|
| 330464 | 2/29/2024 11:58:50 AM | 0 | 0/597 (pre-election) |
| 331452 | 3/5/2024 8:11:58 PM | 149,133 | 0/597 (first tranche) |
| 331551 | 3/5/2024 8:45:43 PM | 152,272 | 0/597 |
| 331624 | 3/5/2024 9:26:47 PM | 165,338 | 597/597 (100%) |
| 331690 | 3/5/2024 10:09:35 PM | 181,819 | 597/597 |
| **331698** | **3/5/2024 10:20:10 PM** | **182,413** | **597/597 (100%)** |
| 331853 | 3/6/2024 5:05:30 PM (+18h45m gap) | 209,664 | 597/597 |
| 331957 | 3/7/2024 4:58:01 PM | 232,035 | 597/597 |
| 334586 (current/certified) | 4/4/2024 1:55:33 PM | 383,110 | 597/597 |

Version 331698 is the LAST version posted on election night itself, at
10:20:10 PM (precincts already at 100% since 331624, 9:26 PM). The
immediately next entry in the OFFICIAL versions array, 331853, is 18h45m
later -- a real gap proven by the complete enumeration, not a sweep
artifact -- with a +27,251 canvass jump. This is an early-ending election
night (last update before 11 PM), matching the same pattern as this
county's 2022 primary (Item 5: last update 10:54 PM) rather than the
overnight-into-early-morning pattern of 2014/2016/2018.

**URLs (live; Wayback archiving not completed this session, see Item 2's
caveat):**
- numerator (plateau) sum: <https://results.enr.clarityelections.com/CA/Santa_Clara/120250/331698/json/sum.json>
- numerator (plateau) settings: <https://results.enr.clarityelections.com/CA/Santa_Clara/120250/331698/json/en/electionsettings.json>
- bracket sum: <https://results.enr.clarityelections.com/CA/Santa_Clara/120250/331853/json/sum.json>

**Arithmetic:** 182,413 / 383,110 = **47.61%**.

**Draft row:**
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 182413,
  "certified_final": 383110,
  "election_night_pct": 47.61,
  "vs_epollbook": "post",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://results.enr.clarityelections.com/CA/Santa_Clara/120250/331698/json/sum.json",
  "confidence": "primary",
  "note": "PLATEAU = last version posted on election night, precincts at 100%. Clarity electionId 120250 (Web02 SPA, complete official versions array, 50 entries). Trajectory: v331452 3/5 8:11:58 PM 149,133 (0/597, first tranche) -> v331624 3/5 9:26:47 PM 165,338 (597/597 = 100%) -> v331698 3/5 10:20:10 PM 182,413 (597/597) [PLATEAU, last election-night version] -> v331853 3/6 5:05:30 PM 209,664 (+18h45m gap in the OFFICIAL array, +27,251 canvass jump) [bracket]. Election night ends early here (last update 10:20 PM, before midnight) -- same pattern as this county's 2022 primary (Item 5, last update 10:54 PM) rather than the overnight-into-early-AM pattern of 2014/2016/2018. Current/certified version 334586 (4/4/2024) BC=383,110 matches the SoS certified total exactly. Certified final 383,110 ballots (CA SoS Voter Participation Statistics by County, 2024-primary: 26,105 poll + 357,005 VBM = 383,110; 37.39% of 1,024,622 registered). Pct = 182,413/383,110 = 47.61%. POST-epollbook (e-pollbooks + VCA vote centers since 2020); ASV never. Evidence-permanence FLAG: source_url_night is the live Clarity CDN URL (verified serving the claimed BC by direct fetch, 2026-07-10); not yet archived to Wayback this session (web.archive.org/save/ did not complete -- sandbox connectivity). Manual operator should run https://web.archive.org/save/<url> and swap to the resulting snapshot before this row is treated as final."
}
```

**Draft VERIFY.md summary row:** `| 2024 | presidential-primary | 182,413 | 383,110 | 47.61% | primary | [link](https://results.enr.clarityelections.com/CA/Santa_Clara/120250/331698/json/sum.json) |`

**Draft VERIFY.md detail bullet:**
`- **2024 presidential-primary** — night `182,413` / final `383,110` = `47.61%` (primary)`
`  - numerator: <https://results.enr.clarityelections.com/CA/Santa_Clara/120250/331698/json/sum.json>`
`  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf>`
`  - look for: sum.json BC = 182,413 at Clarity ver 331698 (Web02), electionsettings websiteupdatedat 3/5/2024 10:20:10 PM PST, precincts 597/597 = 100%. Bracket: next OFFICIAL version 331853, 3/6/2024 5:05:30 PM (+18h45m gap), BC 209,664.`

**Draft plateau_review.json verdict:**
```json
{
  "slug": "santa-clara-ca",
  "date": "2024-03-05",
  "verdict": "CONFIRMED",
  "basis": "last version posted on election night (10:20 PM, precincts at 100%), plus an official-versions-array bracket: the immediately next entry (no skipped version possible) is 18h45m later with a large canvass jump",
  "evidence": "sum.json BC=182413 at Clarity electionId 120250 version 331698 (live CDN), electionsettings websiteupdatedat 3/5/2024 10:20:10 PM PST, precincts 597/597 (complete official versions array of 50 entries); next entry 331853 is 3/6/2024 5:05:30 PM PST (BC 209,664)"
}
```

**render_verified.json:** not applicable (plain JSON, not JS-rendered).

**Confidence / status: PRIMARY, CONFIRMED. Evidence-permanence FLAG only.**

---

## Summary table

| Date | Type | Election-night ballots | Certified final | Pct | Confidence | Evidence class |
|---|---|---:|---:|---:|---|---|
| 2012-06-05 | presidential-primary | 234,342 (CEILING, not plateau) | 292,713 | 80.06% | secondary | none (no bracket; earliest capture already next-day) |
| 2014-06-03 | statewide-primary | 166,360 | 264,133 | 62.98% | primary | bracket (Clarity CDX-sweep, 100% precincts + cadence break) |
| 2016-06-07 | presidential-primary | 282,389 | 430,779 | 65.55% | primary | bracket (Clarity CDX-sweep, 100% precincts + cadence break) |
| 2018-06-05 | statewide-primary | 196,184 | 369,332 | 53.12% | primary | bracket (Clarity official versions array) |
| 2022-06-07 | statewide-primary | 181,257 | 357,848 | 50.65% | primary | bracket (Clarity official versions array, held pattern) |
| 2024-03-05 | presidential-primary | 182,413 | 383,110 | 47.61% | primary | bracket (Clarity official versions array) |

Calibration sanity check (runbook section 1): the like-for-like presidential
primaries (2012, 2016, 2024) show a declining election-night share --
80.06% (ceiling, so directionally consistent with "even higher than a true
plateau would be") -> 65.55% -> 47.61% -- tracking the well-documented VBM
share climb (74.24% -> 93.19% VBM of ballots cast per the SoV tables above)
and, for 2024, post-e-pollbook/VCA-vote-center status. The two
statewide-midterm primaries with pre/post e-pollbook status on either side
of 2020 (2014/2018 pre vs 2022 post) show 62.98% / 53.12% pre and 50.65%
post -- directionally consistent with the county's own November pattern in
`santa-clara-ca.json` (pre-epollbook Novembers running higher than the
post-epollbook 2022/2024 Novembers), though confounded by the same
VBM-share climb and by 2022/2024 being lower-turnout-percentage elections
generally. Not a causal claim -- just noting these numbers are in the
expected range, not a first-tranche artifact (a first-tranche mistake here
would read roughly half these values, e.g. ~90-125K instead of ~165-280K).

## What's unfinished / outstanding for a human or a follow-up pass

1. **Wayback permanence (all 5 Clarity rows, items 2-6).** The live Clarity
   CDN URLs are verified working (direct curl fetch reproduced the claimed
   BC values in this session), but `web.archive.org/save/` did not complete
   for any of the 15 evidence URLs queued -- this sandbox's network to
   `web.archive.org` was flaky throughout (intermittent `Connection
   refused` even on simple CDX GETs, unrelated to the Clarity CDN itself,
   which was reliable). A follow-up pass (or a session with better
   connectivity) should run `https://web.archive.org/save/<url>` for each
   of the 15 URLs listed per item above and swap `source_url_night` to the
   resulting snapshot, matching the pattern already used for this county's
   existing Clarity rows in `santa-clara-ca.json`.
2. **2012-06-05 (item 1) needs a human decision, not just an upgrade
   attempt.** Recorded here as a CEILING (comparable=false, secondary) per
   runbook 5.2 because no true overnight number is archived anywhere found.
   FLAGGED for manual operator to (a) try the Wayback UI directly for a
   June 5-6 2012 capture that the CDX API might be aliasing away from (7.1),
   and (b) consider a NewsBank/SFPL Mercury News pull for an election-night
   quote (the `newsbank-election-recovery` skill's workflow, not attempted
   in this pass -- it is a per-election, browser-driven procedure and this
   dossier already spans 6 elections across 2 vendor systems).
3. **This dossier does not touch the pipeline.** No file in
   `data/research/election-night/` was written or edited; nothing was run
   through `validate_election_night.py` / `build_county_night.py` /
   `verify_en_denominators.py` / `verify_en_numerators.py`. Landing these
   rows requires (a) resolving #1 and #2 above, (b) the surgical JSON edits
   described in runbook section 2 (not whole-file rewrites), (c) the
   matching `VERIFY.md` table rows + detail bullets (drafted above,
   ready to paste), (d) `plateau_review.json` verdict entries (drafted
   above), and (e) a full run of the section-3 pipeline.
