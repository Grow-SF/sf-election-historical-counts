# Control county selection, July 2026

Task 3 of the county-panel expansion (see `.superpowers/sdd/task-3-brief.md`). Picks 5 control
counties for Task 4 to research: San Francisco is the project's existing never-adopter control, and
the design calls for 5 more never-adopter counties to (a) confirm SF's election-night behavior isn't
an SF idiosyncrasy and (b) let matched-years comparisons net out statewide year shocks (a bad-weather
year, a late-breaking statewide race, a printing delay) that would otherwise be mistaken for a
tech effect in the adopter counties.

Consumes `data/research/county-tech/ca_adoption_census.json` (Task 2, committed): of 58 CA counties,
only 6 are `status: "never"` (confidence high/medium/low) and 4 more are `status: "unknown"` with a
census note saying each is "one source away from never." SF itself is excluded as a candidate (it's
the existing control, not a pick).

## Rubric

Per the task brief, score each `never` candidate 0-2 on four archive-viability dimensions (this
decides whether Task 4 can actually recover night-by-night counts, not just certified totals):

1. **Clarity presence** - does/did the county publish results on `results.enr.clarityelections.com`?
2. **Wayback capture density** - how many real (200-status, content-bearing) captures bracket the
   2016 and 2018 general-election nights specifically, not just the domain generally?
3. **Registrar results-URL findability** - is there a confirmed, resolvable results/elections URL
   (live or historical)?
4. **Press-release / media-release archive** - does the county keep a dated press/news archive that
   could corroborate or substitute for a results page?

Then pick 5 by the diversity rubric: >=1 large county (>400k ballots), >=1 small (<100k), >=2
non-VCA, and >=1 VCA-but-never-EPB county if the census found one (the highest-value control in the
design, per the plan's lever 3). Ties broken by archive score.

## The large-county requirement cannot be met, and that's not fixable by better search

The census's full 58-county sweep found **zero** large CA counties (>400k ballots) that never
adopted e-pollbooks or ASV. Every county above roughly 90k population in California has adopted at
least one of the two technologies by 2024. This isn't a gap in the research; it's the actual shape
of the data; California's largest counties adopted VCA vote centers (with e-pollbooks bundled in) or
rolled out standalone ASV between 2018 and 2025, and the handful of holdouts are all small, rural,
mail-heavy counties in the northern part of the state.

**Decision: do not force a large county into the control set.** Selecting the best 5 available
small counties and documenting the gap is more honest than padding the pool with a marginal-adopter
county mislabeled as a control. What this costs and doesn't cost the design:

- **Costs:** the control set can't test whether a large, high-volume county's election-night
  trajectory shifts across matched years the way SF's does. If large adopter counties show a level
  change that's actually a large-county-specific effect (more processing capacity, different
  staffing ratios, urban press cycles) rather than a tech effect, the small-county control panel
  can't distinguish that from a genuine tech effect. Level comparisons between an adopter like LA or
  Orange and a control need to lean more on same-county before/after (already the core of the
  design) than on cross-sectional adopter-vs-control-at-a-point-in-time comparisons.
- **Doesn't cost:** the control panel's primary job in the matched-years design is to net out
  *statewide* year-level shocks common to every county in a given election cycle (weather, a
  marquee statewide race driving turnout, a printing/mailing delay affecting the whole state's VBM
  timeline, a SoS-level rule change). A small-county panel is just as capable of catching a
  statewide shock as a large one would be; the shock hits every county's night-by-night curve
  regardless of county size. So the control's year-shock function is intact even though its
  level-comparison function is weakened for the large-adopter end of the panel.
- Given the large-county axis is closed off, **the VCA-status mix among the 5 picks is the more
  important remaining diversity axis** (per the brief's own steer). See below: it, too, turned out
  to be unavailable in the current candidate pool, which is itself worth stating plainly rather than
  quietly dropping.

## Attempted flips of the 4 `unknown` counties (none succeeded)

The census left Alpine, Sierra, Siskiyou, and Trinity as `unknown`: each is EPB-clean (consistent
"Do not use" / EAVS-False across all four editions, so no VCA and no e-pollbook) but lacks positive
evidence that ASV was never adopted (the project's rule: `never` requires positive support for
ASV *absence*, not just missing evidence). I spent a time-boxed pass (~10-15 min each) trying to
find that one missing source, since flipping any of these would enlarge the candidate pool.

- **Alpine** (`WebSearch: "Alpine County" California elections vote by mail signature verification
  manual staff`; direct fetch of `alpinecountyca.gov/388/Election`): only the statewide SoS
  boilerplate on signature standards; nothing Alpine-specific on method. No flip.
- **Sierra** (`WebSearch: "Sierra County" California elections signature verification ballot
  software OR manual`; `WebSearch: Sierra County grand jury response elections signature
  verification forensic training`): the 2025-2026 grand jury coverage (Mountain Messenger,
  Sierra Booster) describes jurors watching "signature verification, secure storage, logic and
  accuracy testing, and ballot scanning" and praises staff knowledge, but never states whether the
  verification step itself is machine-assisted or human-only. Same ambiguity the census already
  flagged. No flip.
- **Siskiyou** (`WebSearch: "Siskiyou County" elections signature verification vote by mail staff
  manual grand jury`; `WebSearch: Siskiyou Daily News OR "Mt. Shasta" elections office signature
  verification staff compare ballots`; `WebSearch: "unsigned ballots" OR "signature verification"
  Siskiyou County elections human eyes`; `WebFetch` of `siskiyoucounty.gov/elections/page/vote-mail`):
  one search's summary surfaced the phrase "must be signature verified by human eyes" attributed in
  the answer text to Siskiyou, but cross-checking the actual source set showed that exact phrase
  belongs to **Shasta County's** own `elections.shastacounty.gov/unsigned-ballots-and-signature-
  verification/` page (already correctly captured as Shasta's ASV note in the census), which had
  appeared in the same result set the summarizer was drawing from. A direct `WebFetch` of Siskiyou's
  actual vote-by-mail page confirmed it says nothing about verification method. **This was a
  near-miss caused by search-result cross-contamination, not a real Siskiyou finding; flagging it
  here so a future pass doesn't repeat it.** No flip.
- **Trinity** (`WebSearch: "Trinity County" California elections vote by mail signature verification
  process`; `WebSearch: Trinity Journal elections office signature verification staff compare
  ballots grand jury`): the Dec-2020 grand jury writeup (already in the census) praises Trinity's
  ballot handling and hand-tally redundancy but doesn't touch the signature-comparison method
  specifically. No new source found. No flip.

**Net result: the candidate pool stays at 6 (Colusa, Del Norte, Plumas, Tehama, Lake, Mendocino).**
The census's `unknown` rows for Alpine/Sierra/Siskiyou/Trinity are unchanged; no census edits were
needed, so the validator run below is confirming the existing (untouched) census, not a post-edit
recheck.

## VCA-but-never-EPB: none exist in the current pool

Checked every one of the 6 `never` rows and all 4 `unknown` rows: every single one is explicitly
"NOT a VCA county" per its census note (absent from the SoS VCA Vote Center Usage Summary). There is
currently no VCA-but-never-EPB county anywhere in the 58-county census, adopter or not; California's
VCA-adopting counties bundle an e-pollbook rollout into the same vote-center transition essentially
every time. **The brief's highest-value control type does not exist in this dataset**, so this pick
is dropped rather than forced. All 5 selected controls are non-VCA, traditional-precinct-polling
counties, which trivially satisfies the brief's ">=2 non-VCA" floor but forecloses the VCA-contrast
axis entirely.

## Scored table: all 6 candidates

Probe commands/results are copied verbatim from the two probe evidence files (`archive-probes-a-m.md`,
`archive-probes-m-y.md`), run by two earlier read-only scout passes. Methodology note carried over
from those files: `results.enr.clarityelections.com/CA/<County>/current_ver.txt` 404s at the
county-root level for every CA county (Clarity nests it under a numeric per-election ID); the
adapted probe checks whether `https://results.enr.clarityelections.com/CA/<County>/` (with a
browser User-Agent, since CloudFront 403s bare curl) returns 200 (used Clarity at some point) or a
genuine Clarity 404 page (never did).

Score legend: 0-2 per dimension (Clarity presence / Wayback density around Nov 2016 & Nov 2018 /
registrar-URL findability / press-release archive). Total = sum of the 4, max 8.

| County | Clarity | Wayback | Registrar-URL | Press-release | Total | Verdict | Census status/confidence | Picked? |
|---|---|---|---|---|---|---|---|---|
| Del Norte | 0 | 2 | 2 | 2 | 6 | viable | never / medium | **Yes** |
| Lake | 0 | 2 | 2 | 2 | 6 | viable | never / low | **Yes** |
| Colusa | 0 | 1 | 2 | 1 | 4 | marginal | never / medium | **Yes** |
| Mendocino | 0 | 2 | 1 | 1 | 4 | viable | never / low | **Yes** |
| Tehama | 0 | 1 | 1 | 0 | 2 | marginal | never / medium | **Yes** |
| Plumas | 0 | 0 | 2 | 1 | 3 | poor | never / medium | No - rejected |

### Why Plumas, not Tehama, is the one rejected near-miss

Tehama's raw dimension sum (2) is actually lower than Plumas's (3), but the probe's categorical
verdict ranks Plumas *below* Tehama ("poor" vs "marginal") because of what the sum obscures: Plumas's
Wayback score is a hard 0 - the CDX sweep found **zero** captures anywhere near election night in
*either* 2016 or 2018 (closest hits are 11-15/11-16/11-23/11-26 in 2016 and 11-03/11-15 in 2018, and
the elections-subpage-specific query came back empty both years). Tehama's Wayback score of 1 means
real, if imperfect, coverage: a `dep-elections` landing page captured 2016-11-08 (election day
itself, pre-results) and 2018-11-07/11-09 (day after and three days after), plus a dedicated
`election_results/Election Result_dtl.htm` page captured the day before the 2016 election. Since the
whole point of this control panel is recovering night-by-night trajectories (not just a certified
final), a county with literally nothing archived near election night in either target year is the
weaker pick even though its summed score edges out Tehama's on paper. The probe's own verdict
("exactly the low-archivability case this probe is meant to flag") makes the same call. Plumas is
therefore the rejected near-miss; the other 5 are the picks.

## Probe evidence per candidate (copied from the scout files)

### Del Norte (picked)

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Del_Norte/` -> 404. No Clarity usage (small county).
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://www.co.del-norte.ca.us/departments/elections` -> 200; canonical path is actually `/departments/clerk-recorder/elections` (also 200), plus a legacy subdomain `elections.co.del-norte.ca.us`.
3. Wayback density: strong in both windows. Nov 2016: `elections.co.del-norte.ca.us/` captured 5x (2016-11-02 through 2016-11-21, 200 each); `.../clerk-recorder/elections` captured 2016-11-03 and 2016-11-17. Nov 2018: `.../elections/election-results` captured repeatedly, and — notably — dated per-election subpages exist: `.../election-results/november-8-2016-general-election-results` and `.../june-7-2016-primary-election-results`, both still live and captured as of 2018-11-25, meaning the county keeps a standing results archive by election name rather than overwriting a single "current results" page.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.co.del-norte.ca.us/departments/clerk-recorder/elections/press-releases` -> 200 (path guessed correctly on first try).

Verdict: **viable** — best result in this batch for methodology: the county's own site structure preserves dated per-election results pages, so even a single fresh capture would recover the 2016 numbers; Wayback also already has that exact page indexed.

### Lake (picked)

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Lake/` -> 404. No Clarity usage.
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://www.lakecountyca.gov/818/Registrar-of-Voters` -> 200.
3. Wayback density: strong once the right subdomain is found. Nov 2016 -> `publicapps.lakecountyca.gov/elections/results/result30.htm` captured **2016-11-12**, 200, 4.3KB — a genuine dated results page (the main `www.lakecountyca.gov` domain itself didn't show elections-tagged hits in the same window, so results lived on a separate `publicapps` subdomain). Nov 2018 -> very dense: individual ballot-measure PDFs (`Hv2.pdf`, `Iv2.pdf`, `Kv2.pdf`, `Lv2.pdf`, `Mv2.pdf`) and a `Nov2018MediaReleases/Registration+Deadline.pdf` all captured 200 through late November — the county evidently keeps a dedicated per-election media-release folder.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.lakecountyca.gov/916/Resources` -> 200; CDX independently surfaced a `Nov2018MediaReleases/` folder confirming an actual press-release archiving convention, not just a guess.

Verdict: **viable** — the `publicapps` results subdomain plus a confirmed `MediaReleases` folder-per-election convention makes this one of the cleaner recoveries in the batch, though note results.aspx lives on a different subdomain than the main county site, worth remembering for future probes.

### Colusa (picked)

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Colusa/` -> 404. No Clarity usage.
2. Registrar URL: `curl -o /dev/null -w "%{http_code}" https://www.countyofcolusaca.gov/197/Elections` -> 200 (current site, migrated from old domain `countyofcolusa.org` at some point between 2018 and now).
3. Wayback density: CDX on current domain `countyofcolusaca.gov` for both Nov 2016 and Nov 2018 -> **empty both windows** (domain didn't exist yet, or wasn't crawled). CDX on the old domain `countyofcolusa.org` -> Nov 2016 also empty; Nov 2018 has a real `/elections` page capture (2018-11-29, 200, 18KB) plus incidental site-chrome assets, but nothing dated closer to election night itself and nothing at all for 2016.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" https://www.countyofcolusaca.gov/CivicAlerts.aspx` -> 200 (CivicPlus alerts module exists; depth/vintage unconfirmed).

Verdict: **marginal** — no 2016 web trail found at all under either domain; 2018 has only a late-month capture. This is a small county where PDF result books may be the only real record for 2016.

### Mendocino (picked)

1. Clarity: `curl -A UA -o /dev/null -w "%{http_code}" https://results.enr.clarityelections.com/CA/Mendocino/` -> 404. No Clarity usage.
2. Registrar URL: current `https://www.mendocinocounty.gov/government/assessor-county-clerk-recorder-elections/elections` (curl -> 403, Cloudflare-blocked but real). 2016/2018-era domain was `co.mendocino.ca.us`.
3. Wayback density: strong, and shows a long-running naming convention. Nov 2016: `/acr/elections.htm` captured **10 times** between 2016-11-04 and 2016-11-23 (all 200, ~6.4KB, spanning election day 2016-11-08 itself). Nov 2018: the same path now 301-redirects to the new site, but CDX also surfaced named historical-results pages reaching back to 2008 (`election_results/results20080205.pdf`, `results-20080620.htm`, `results20091118.htm`, `results20100608.htm`, `20101102-general.htm`) and a `pastElections.htm` index — strong evidence the county has archived results by dated filename for over a decade.
4. Press-release archive: `curl -o /dev/null -w "%{http_code}" -L https://www.mendocinocounty.gov/government/assessor-county-clerk-recorder-elections/current-election-results` -> 403 (Cloudflare-blocked, not independently confirmed, though a "Past Election Results" page was found directly via search).

Verdict: **viable** — 2016 has a direct, dated `elections.htm` capture including election day itself, and the site's own dated-filename convention for results pages (`resultsYYYYMMDD.htm`) going back to 2008 makes this one of the more self-documenting counties in the batch.

### Tehama (picked)

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Tehama/current_ver.txt"` -> HTTP 404 (genuine Clarity 404 page). Not on Clarity. Score: 0
2. Live results URL: `www.co.tehama.ca.us` -> DNS resolution failure (curl exit 6, "couldn't resolve host") on two separate attempts; could not confirm live. Identified via Wayback as `co.tehama.ca.us/dep-elections`. Score: 1
3. Wayback density: 2016 window: `dep-elections` landing page captured 11-03, 11-04, and 2016-11-08 08:19 UTC (=11-08 12:19am PST, early election day, pre-results); separately a dedicated `election_results/Election Result_dtl.htm` page captured 2016-11-07 22:05 UTC (day before election). Also plain `/elections` alias captured 11-04/11-05. 2018 window: `dep-elections` captured 2018-11-07 15:01 and 2018-11-09 15:21 (day after and 3 days after election). Score: 1
4. Press-release archive: could not check (DNS failure on live site). Score: 0 (unknown)

Verdict: **marginal** — site is crawled with reasonable regularity around election windows both years and has a dedicated results-detail page, but no confirmed exact-election-night capture and live site currently unreachable from this probe environment.

### Plumas (rejected near-miss)

1. Clarity: `curl -s -A "Mozilla/5.0..." "https://results.enr.clarityelections.com/CA/Plumas/current_ver.txt"` -> HTTP 404 (genuine Clarity 404 page). Not on Clarity. Score: 0
2. Live results URL: `https://www.plumascounty.us/162/Elections-Voter-Registration` -> HTTP 200 live (CivicPlus CMS). Score: 2 (found and confirmed live in one probe)
3. Wayback CDX: 2016 window: 4 captures (11-15, 11-16, 11-23, 11-26) -- none election night (11/8) or morning-after (11/9). 2018 window: 2 captures (11-03, 11-15) -- none close to election night (11/6) or morning-after. CDX query on `plumascounty.us/162*` (elections subpage) returned zero hits. Score: 0 (sparse, and misses election-night windows both years)
4. Press-release archive: live site has a CivicPlus "News"/"Archive" module (`list.aspx?nid=`, HTTP 200), plausible but historical depth unconfirmed. Score: 1

Verdict: **poor** (tiny county, no Clarity, thin Wayback coverage of the actual results page, likely PDF-only result books -- exactly the low-archivability case this probe is meant to flag). Rejected in favor of Tehama; see rationale above.

## Rejected `unknown` candidates (not promoted to the pool)

| County | Census status/confidence | Why not promoted |
|---|---|---|
| Alpine | unknown / low | EPB-clean but no ASV-absence source found in either the original census research or this pass's follow-up search; only statewide SoS boilerplate on file. |
| Sierra | unknown / low | 2025-2026 grand jury report watched "signature verification" happen but never states whether the match itself is machine-assisted or human-only; genuinely ambiguous, not just under-searched. |
| Siskiyou | unknown / low | No county-specific verification-method statement found in county pages, local news, or grand jury archive. A promising "human eyes" search snippet turned out to be a misattributed quote actually belonging to Shasta County (see flip-attempt section above) — a real near-miss, not a Siskiyou finding. |
| Trinity | unknown / low | County's own elections page and the one available grand jury writeup (Dec 2020) praise ballot handling generally but don't describe the signature-comparison method specifically. |

## The 5 picks

| Pick | Slug | Verdict | Confidence | Population (2020 census) |
|---|---|---|---|---|
| Del Norte County | `del-norte-ca` | viable | medium | 27,009 |
| Lake County | `lake-ca` | viable | low | 67,764 |
| Colusa County | `colusa-ca` | marginal | medium | 21,839 |
| Mendocino County | `mendocino-ca` | viable | low | 89,175 |
| Tehama County | `tehama-ca` | marginal | medium | 65,829 |

All 5 satisfy the brief's "small" bucket (<100k ballots is trivially true for counties this size;
even Mendocino, the largest, has a population under 90k so ballots cast tops out in the low
tens-of-thousands). All 5 are non-VCA, traditional-precinct-polling counties (satisfies ">=2
non-VCA" many times over). No large county and no VCA-but-never-EPB county exist in the current
58-county census; both gaps are documented above rather than papered over.

## Validation

```
$ python3 -c "import json; json.load(open('data/research/county-tech/worklist.json'))"
(no output = well-formed JSON)

$ python3 scripts/research/validate_adoption_census.py
(no output, exit 0 = census unchanged and still green)
```

No census edits were made (no `unknown` rows flipped), so the census validator run above is
confirming the pre-existing committed census, not re-validating a change.
