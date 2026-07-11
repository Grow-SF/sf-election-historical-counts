# Madera County, CA -- statewide PRIMARY election-night dossier

READ-ONLY research scratch dossier. Nothing here has been written to the repo.
Built per `docs/research/RUNBOOK.md` (sections 1, 2, 5, 6, 7.2, 8) applied to
Madera's six statewide primaries (2012, 2014, 2016 [pre-VCA]; 2018 [VCA
rollout]; 2022, 2024 [post-VCA]). Cross-checked against the existing
`data/research/election-night/madera-ca.json` (general elections) and
`data/research/county-tech/madera-ca.json` (adoption record) for consistency.

**Adoption record recap** (from `data/research/county-tech/madera-ca.json`):
vote-center/VCA model + e-pollbook-equivalent (DFM EIMS) both `adopted_year:
2018`, `first_election: "2018-06"`. That means **the June 5, 2018 primary
itself is Madera's rollout election** -- not the following November general.
So 2018-06-05 classifies `vs_epollbook: "post"` (same convention the general
row for 2018-11-06 uses despite being the *second* VCA election). ASV never
adopted (`adopted_year: null`) => `vs_asv: "n/a"` on every row below, matching
the existing general-election rows.

**Network note:** web.archive.org connectivity was intermittently flaky during
this session (repeated `connect() failed`, resolved after 5-20s retries); all
numbers below were fetched successfully after retry, and every Clarity
election-night source was freshly archived to Wayback and re-verified from
the archived copy (not just the live CDN) before being cited.

---

## Summary table (VERIFY.md format)

| Year | Type | Night | Final | Pct | Confidence | Link |
|---|---|---|---|---|---|---|
| 2012 | presidential-primary | -- | 20,538 | NULL | none | [SoV](https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/2012-complete-sov.pdf) |
| 2014 | statewide-primary | -- | 19,206 | NULL | none | [SoV](https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/2014-complete-sov.pdf) |
| 2016 | presidential-primary | -- | 26,941 | NULL | none | [SoV](https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf) |
| 2018 | statewide-primary | 18,258 | 24,211 | 75.41% | primary | [link](https://web.archive.org/web/20260710214438/https://results.enr.clarityelections.com/CA/Madera/75694/204457/json/sum.json) |
| 2022 | statewide-primary | 13,417 | 24,810 | 54.08% | primary | [link](https://web.archive.org/web/20260710214927/https://results.enr.clarityelections.com/CA/Madera/114136/295158/json/sum.json) |
| 2024 | presidential-primary | 16,048 | 27,609 | 58.13% | primary | [link](https://web.archive.org/web/20260710215117/https://results.enr.clarityelections.com/CA/Madera/120377/331700/json/sum.json) |

---

## ITEM 1 -- 2012-06-05 (Presidential Primary)

**Certified final:** 20,538 ballots cast (Total Voters), CA SoS "Voter
Participation Statistics by County," complete 2012 primary SOV.
URL: `https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/2012-complete-sov.pdf`
(no separate `sov/03-...` extract exists for 2012; this is the full SOV PDF,
p.2 of the "Voter Participation Statistics by County" section, `pdftotext -layout`).
Line: `Madera 54 86,137 52,826 5,654 14,884 20,538 72.47% 38.88% 23.84%`
(precincts 54, eligible-to-register 86,137, registered 52,826, precinct
5,654 + VBM 14,884 = Total Voters 20,538).

**Plateau:** NOT RECOVERABLE. Evidence trail:
- Wayback CDX for `votemadera.com` (domain-wide, Jan-Aug 2012): **zero
  captures of any kind** (`cdx?url=votemadera.com&matchType=domain&from=20120101&to=20120801`
  returns `[]`). The domain was not crawled at all in this window.
- Wayback CDX for `co.madera.ca.us` and `maderacountyca.gov` (same window):
  also zero captures.
- Wayback CDX for `madera-county.com` (the county's 2012-era domain) found
  an `/election_results/` folder with frameset shells captured 2012-06-09
  and 2012-06-10 (4-5 days after election day): `results_frm.html` ->
  frame `frame24.htm`; `resultsc_frm.html` -> frame `resultsc24.htm`
  ("Election 24"). But CDX confirms the frame TARGETS were never crawled:
  `frame24.htm`, `resultsc24.htm`, and `result24.htm` all return `[]`.
  Classic RUNBOOK 7.1 frameset trap: the shell was crawled, the content
  frame was not, and even the June 9-10 captures (had they existed) would
  postdate election night by days.
- No Clarity ENR: confirmed via `results.enr.clarityelections.com/CA/Madera/75694/`
  (Madera's first-ever Clarity election, per the existing general-election
  JSON) is the **June 2018** primary; nothing exists for Madera on Clarity
  in 2012.
- WebSearch for Sierra News Online / Madera Tribune June 2012 primary-night
  coverage: no county-wide ballot total found (searches returned only
  generic "past election results" landing pages and unrelated Clarity SEO
  artifacts from later years indexed under the same "Madera election
  results" query).
- Per RUNBOOK 5.1, recorded null rather than substituting the 4-5-day-later
  frameset (which is unrecoverable anyway) or any other proxy.

**Arithmetic:** n/a (null).

**Draft row (schema per RUNBOOK section 2):**
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 20538,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/2012-complete-sov.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 20,538 ballots cast (Total Voters) from CA SoS 'Voter Participation Statistics by County', complete 2012 primary SOV (Madera: 54 precincts, 86,137 eligible, 52,826 registered, 5,654 precinct + 14,884 VBM = 20,538). Election-night plateau NOT recoverable: Wayback has zero captures of votemadera.com in 2012 (domain-wide CDX empty for Jan-Aug 2012). The county's other 2012-era domain, madera-county.com, has an /election_results/ frameset (results_frm.html -> frame24.htm 'Election 24') captured 2012-06-09/06-10 (4-5 days post-election), but CDX confirms the actual content frames (frame24.htm, resultsc24.htm, result24.htm) were never crawled -- classic frameset trap (RUNBOOK 7.1), and even if recovered would postdate election night. Predates Madera's Clarity ENR (first Clarity election is 75694, June 2018 primary). No news-quoted county-wide ballot total found via WebSearch of Sierra News Online / Madera Tribune archives. No snapshot used. Pre-e-pollbook, pre-ASV (both n/a pre-2018)."
}
```

**VERIFY.md line:** `| 2012 | presidential-primary | -- | 20,538 | NULL | none | [SoV link] |`
**Detail bullet:** "2012 presidential-primary -- night NULL / final 20,538 (none). look for: certified final only; no election-night plateau recoverable (see note)."

**Plateau verdict:** N/A (null row; no plateau_review.json entry needed per RUNBOOK 5.5, which only covers sourced rows).

**FLAG for manual operator:** Optional secondary pass -- try the Wayback UI directly (not curl) on `http://www.madera-county.com/election_results/results_frm.html` circa June 2012; the RUNBOOK notes the Wayback UI sometimes serves frames that curl's CDX enumeration says don't exist. Low expected yield (CDX shows no capture record at all for the frame files, not just a replay-aliasing issue), so not chased further here.

---

## ITEM 2 -- 2014-06-03 (Statewide Primary)

**Certified final:** 19,206 ballots cast (Total Voters), CA SoS "Voter
Participation Statistics by County," complete 2014 primary SOV.
URL: `https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/2014-complete-sov.pdf`
Line: `Madera 76 85,586 52,817 5,197 14,009 19,206 72.94% 36.36% 22.44%`
(precincts 76, eligible 85,586, registered 52,817, precinct 5,197 + VBM
14,009 = Total Voters 19,206).

**Plateau:** NOT RECOVERABLE. Evidence trail:
- Wayback CDX for `votemadera.com` (domain-wide, Jan-Oct 2014, 22 records):
  only homepage/robots.txt/favicon.ico/registrationcheck captures in
  May-Sept 2014 (earliest May 24, then Jul 8, Jul 24, Aug 2, Aug 31, Sep 1,
  Sep 29). **No `/results/` path exists in this window at all.** This
  matches and extends the existing general-election finding in
  `madera-ca.json` (2014-11-04 row): "the /results/ folder is first
  archived as Election28 = Nov 2014" -- i.e. even the NOVEMBER general's
  results folder didn't exist yet as of the June primary; June 2014 predates
  the whole votemadera.com results system.
- Wayback CDX for `madera-county.com/election_results` (prefix match,
  Jan-Oct 2014): **zero captures** -- the frameset system used for the 2012
  primary was gone/unindexed by 2014 (the county's site migration to
  votemadera.com/WordPress apparently left a gap).
- No Clarity ENR (first Clarity election is June 2018, per above).
- WebSearch for Sierra News Online / Madera Tribune June 2014 primary-night
  coverage: no county-wide ballot total found.
- Per RUNBOOK 5.1, recorded null.

**Arithmetic:** n/a (null).

**Draft row:**
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 19206,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/2014-complete-sov.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 19,206 ballots cast (Total Voters) from CA SoS 'Voter Participation Statistics by County', complete 2014 primary SOV (Madera: 76 precincts, 85,586 eligible, 52,817 registered, 5,197 precinct + 14,009 VBM = 19,206). Election-night plateau NOT recoverable: Wayback's votemadera.com CDX for Jan-Oct 2014 (22 records) shows only homepage/robots/favicon/registrationcheck captures -- no /results/ path exists yet in this window, consistent with the existing general-election finding that the /results/ folder is FIRST archived as Election28 = Nov 2014 (i.e. even the following November general's results system postdates this primary). madera-county.com/election_results (the 2012-era frameset host) has zero captures in 2014 -- that system was already retired. Predates Clarity (first Clarity election is 75694, June 2018 primary). No news-quoted county-wide ballot total found via WebSearch. No snapshot used. Pre-e-pollbook, pre-ASV."
}
```

**VERIFY.md line:** `| 2014 | statewide-primary | -- | 19,206 | NULL | none | [SoV link] |`
**Detail bullet:** "2014 statewide-primary -- night NULL / final 19,206 (none). look for: certified final only; no results-system capture exists this early."

**Plateau verdict:** N/A (null row).

**FLAG for manual operator:** None warranted; the evidence trail (domain-wide CDX with zero /results/ hits, corroborated by the general-election row's own finding that the results folder didn't exist until Nov 2014) is about as conclusive a "does not exist" case as this dataset sees.

---

## ITEM 3 -- 2016-06-07 (Presidential Primary)

**Certified final:** 26,941 ballots cast (Total Voters), CA SoS "Voter
Participation Statistics by County," 2016 primary SOV extract.
URL: `https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf`
(NB: unlike 2018-2024, the 2016 primary PDF has no `sov/` path segment before
the filename -- `.../2016-primary/03-...pdf`, confirmed by 403 on the
`sov/03-...` form and 200 on the flat form.)
Line: `Madera 77 87,117 54,017 8,278 18,663 26,941 69.27% 49.88% 30.93%`
(precincts 77, eligible 87,117, registered 54,017, precinct 8,278 + VBM
18,663 = Total Voters 26,941).

**Plateau:** NOT RECOVERABLE. Evidence trail:
- Wayback CDX for `votemadera.com/results` (prefix match, full 2011-2019
  window, collapsed by urlkey): only two Election-ID folders were EVER
  crawled -- **Election28** (Nov 2014 general) and **Election33** (Nov 2016
  general, the source for the existing madera-ca.json 2016-11-08 row). No
  Election29/30/31/32 folder was crawled with usable content.
- Explicitly probed Election29 through Election32 individually via CDX:
  Election29 = zero captures; Election30 = ONE capture, a 404 from a 2019
  crawl (`election30/html/result30.htm`, dead link by then, no content ever
  archived); Election31 = zero captures; Election32 = zero captures. If
  Election32 was in fact the June 2016 primary's ID (plausible given its
  position just before Election33 = Nov 2016), it was never crawled by
  Wayback at any point in its life.
- No Clarity ENR for 2016 (first Clarity election is June 2018).
- WebSearch across Sierra News Online / Madera Tribune for June 2016
  primary-night or semi-final coverage: no county-wide ballot total found.
  One search's AI-generated summary claimed a figure ("24,810 ballots...
  34% turnout") for this election; **verified false by direct WebFetch of
  the cited article** (`maderatribune.com/single-post/results-are-in-it-s-
  official-with-primary-election`), which is actually dated June 25, 2022
  and reports the JUNE 2022 primary's certified total (which does equal
  24,810 -- matches ITEM 5 below). Discarded as a search-summary
  mis-citation, not a real 2016 source.
- Per RUNBOOK 5.1, recorded null.

**Arithmetic:** n/a (null).

**Draft row:**
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 26941,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 26,941 ballots cast (Total Voters) from CA SoS 'Voter Participation Statistics by County', 2016 primary SOV extract (Madera: 77 precincts, 87,117 eligible, 54,017 registered, 8,278 precinct + 18,663 VBM = 26,941). Election-night plateau NOT recoverable: full-lifetime CDX of votemadera.com/results/ (2011-2019, collapsed by urlkey) shows only Election28 (Nov 2014) and Election33 (Nov 2016) folders were ever crawled with content; explicit per-ID probes of Election29-32 found zero usable captures (Election30 has a single 404 from a 2019 crawl, proving the page existed at some point but was already gone and was never archived with content). Predates Clarity (first Clarity election is 75694, June 2018 primary). WebSearch found no genuine news-quoted county-wide ballot total for June 2016; one AI search-summary citation was checked by direct WebFetch and proved to be a mis-dated reference to the June 2022 primary article (discarded, not evidence). No snapshot used. Pre-e-pollbook, pre-ASV. CORRECTION-READY NOTE: if a human operator locates an Election29-32 folder via the live Wayback UI (curl's CDX enumeration can miss replay-aliased captures per RUNBOOK 7.1), this row should be revisited."
}
```

**VERIFY.md line:** `| 2016 | presidential-primary | -- | 26,941 | NULL | none | [SoV link] |`
**Detail bullet:** "2016 presidential-primary -- night NULL / final 26,941 (none). look for: certified final only; no Election-folder capture between Election28 (Nov 2014) and Election33 (Nov 2016) exists for the June primary."

**Plateau verdict:** N/A (null row).

**FLAG for manual operator:** Yes -- lowest-confidence null of the three pre-Clarity primaries, since Election30's single 404 capture proves SOME page existed under that numbering scheme at some point; a human browsing the live Wayback UI directly (not curl CDX) around `votemadera.com/results/Election30/` through `Election32/` in the June-July 2016 window might surface a capture curl's CDX search missed. Not chased further here per the RUNBOOK's "do not burn hours on a bot-wall" guidance and the ~35-min/election budget.

---

## ITEM 4 -- 2018-06-05 (Statewide Primary, VCA ROLLOUT election)

**Certified final:** 24,211 ballots cast (Total Voters), CA SoS "Voter
Participation Statistics by County," 2018 primary SOV.
URL: `https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf`
Line: `Madera 69 89,532 54,848 1,995 22,216 24,211 91.76% 44.14% 27.04%`
(precincts 69, eligible 89,532, registered 54,848, precinct 1,995 + VBM
22,216 = Total Voters 24,211). Confirms the county-tech record's classification:
this is the debut VCA/vote-center election (note the collapse from 76-77
precincts in 2014/2016 to 69 "precincts" here, i.e. vote centers).

**Plateau:** RECOVERED via Clarity ENR (route 6.4), Madera's first-ever
Clarity election, id **75694**.
- Enumerated all 26 published versions via `current_ver.txt` (206422, the
  certified version, dated 6/19/2018) -> `electionsettings.json`
  `versions` array.
- Probed `websiteupdatedat` + `sum.json` `Contests[0].BC` across the
  version range. Progression on election night (6/5/2018):
  v204285 (8:34:16 PM, BC 15,931) -> v204326 (8:51:41 PM, 15,931) ->
  v204373 (9:20:08 PM, 16,500) -> v204435 (10:30:49 PM, 16,760) ->
  v204445 (11:07:22 PM, 17,340) -> v204448 (11:14:15 PM, 17,340) ->
  v204456 (11:57:05 PM, **18,258**) -> **v204457 (6/6/2018 12:03:33 AM
  PDT, BC 18,258)**.
- **Bracket proof (RUNBOOK section 8, gold standard):** the NEXT published
  version, v204551, is dated 6/6/2018 4:45:04 PM PDT -- nearly 17 hours
  later, same afternoon-after -- and STILL shows BC 18,258 (unchanged).
  Only the version after that, v204780 (6/8/2018 2:29:40 PM), shows the
  canvass resuming (BC jumps to 22,247). So 18,258 is confirmed frozen from
  12:03 AM June 6 through the afternoon of June 6, i.e. it is the true
  election-night plateau (the 12:03 AM timestamp falls inside the RUNBOOK's
  explicit "1-4 a.m. next morning still counts as election night" rule).
- Certified version v206422 (6/19/2018) BC = 24,211, exactly matching the
  SoS SoV Total Voters figure -- cross-validates the whole version chain.
- Freshly archived to Wayback (`web.archive.org/save/...`, snapshot
  `20260710214438`) and re-verified by fetching the archived copy directly:
  `Contests[0].BC` = 18258, confirmed.
- Secondary corroboration (non-circular, independent): Sierra News Online,
  "Unofficial Election Results Pending Final Counts" (published June 15,
  2018 -- a different article, about a LATER partial count, not this one)
  reports 43.9% registered-voter participation at that later point, which
  is directionally consistent with continued canvass climbing from the
  18,258/54,848=33.3% overnight figure toward the certified 44.14%; not
  used as the primary evidence (Clarity is), just a sanity check.

**Arithmetic:** 18,258 / 24,211 = 75.4120...% -> **75.41%**.

**Draft row:**
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 18258,
  "certified_final": 24211,
  "election_night_pct": 75.41,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20260710214438/https://results.enr.clarityelections.com/CA/Madera/75694/204457/json/sum.json",
  "confidence": "primary",
  "note": "Numerator 18,258 = total Ballots Cast (Contests[0].BC) from Madera County's Clarity ENR election-night data version 204457 (results.enr.clarityelections.com/CA/Madera/75694/204457/json/sum.json), Madera's FIRST-EVER Clarity election (id 75694). websiteupdatedat = '6/6/2018 12:03:33 AM PDT' -- the last election-night report (progression on 6/5: v204285 8:34PM 15,931 -> v204373 9:20PM 16,500 -> v204445 11:07PM 17,340 -> v204456 11:57PM 18,258 -> v204457 12:03AM 18,258). It is the election-night plateau and HELD STEADY: the next version v204551 ('6/6/2018 4:45:04 PM PDT', same afternoon, ~17hrs later) still shows BC 18,258; only v204780 ('6/8/2018 2:29:40 PM') shows the canvass resuming (22,247). Certified version v206422 ('6/19/2018', BC 24,211) exactly matches the SoS SoV Total Voters. Certified final 24,211 (CA SoS 'Voter Participation Statistics by County'; Madera 69 precincts/vote-centers, 89,532 eligible, 54,848 registered, 1,995 precinct + 22,216 VBM). pct = 18,258/24,211 = 75.41%. Freshly archived to Wayback (snapshot 20260710214438, re-verified BC=18258 from the archived copy). This IS Madera's VCA/e-pollbook ROLLOUT election per county-tech record (adopted_year 2018, first_election '2018-06'), so vs_epollbook = post despite being the same calendar year's first election under the new model."
}
```

**VERIFY.md line:** `| 2018 | statewide-primary | 18,258 | 24,211 | 75.41% | primary | [link](https://web.archive.org/web/20260710214438/https://results.enr.clarityelections.com/CA/Madera/75694/204457/json/sum.json) |`
**Detail bullet:** "2018 statewide-primary -- night 18,258 / final 24,211 = 75.41% (primary). look for: Clarity version 204457, `Contests[0].BC` = 18258, `websiteupdatedat` '6/6/2018 12:03:33 AM PDT', bracket-held through v204551 (6/6 4:45 PM, same BC)."

**Plateau verdict (plateau_review.json style):** `CONFIRMED` -- basis: Clarity version bracket (v204457 late-night timestamp + v204551 same-value ~17hrs later + v204780 jump 2 days after that); self-describes as the live ENR feed; certified version's BC cross-validates against the independently-sourced SoS SoV total.

**render_verified.json entry needed?** No -- this is a direct JSON API fetch (`sum.json`), not a JS-rendered page; no puppeteer rendering was used.

---

## ITEM 5 -- 2022-06-07 (Statewide Primary)

**Certified final:** 24,810 ballots cast (Total Voters), CA SoS "Voter
Participation Statistics by County," 2022 primary SOV.
URL: `https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf`
Line: `Madera* 33 93,606 71,979 1,333 23,477 24,810 94.63% 34.47% 26.50%`
(precincts/vote-centers 33, eligible 93,606, registered 71,979, precinct
1,333 + VBM 23,477 = Total Voters 24,810).

**Plateau:** RECOVERED via Clarity ENR, election id **114136** (identified
by its `current_ver.txt` -> `electionsettings.json` `websiteupdatedat` =
6/22/2022, i.e. shortly after the June 7 primary and well before the Nov
2022 general which is id 116174; Wayback's own CDX only happened to crawl
this election's INDEX page in October 2022, well after the fact, but the
live CDN confirms the id via its certification-date settings).
- 19 published versions (290095 ... 298654). Progression on election night
  (6/7/2022): v295035 (8:11:14 PM, BC 12,121) -> v295150 (10:00:38 PM,
  12,470) -> **v295158 (10:36:58 PM, BC 13,417)**.
- **Bracket proof:** the next version, v295333, is dated 6/8/2022 2:45:05
  PM PDT (next afternoon) and STILL shows BC 13,417 (unchanged, ~16 hours
  later). Only v295603 (6/10/2022 1:43:41 PM, i.e. 2 more days later) shows
  the canvass resuming (BC jumps to 17,214).
- Certified version v298654 (6/22/2022) BC = 24,810, exactly matching the
  SoS SoV Total Voters figure.
- Freshly archived to Wayback (snapshot `20260710214927`), re-verified from
  the archived copy: `Contests[0].BC` = 13417.
- **Independent secondary corroboration (non-circular, strong):** Sierra
  News Online, "Local Primary Election Results" (published June 8, 2022):
  "With 71,961 registered voters in Madera County only 13,417 ballots were
  cast in yesterdays primary for a turnout of 18.64%." This is an
  independently-authored news article (not derived from our research)
  giving the EXACT SAME 13,417 figure the day after the election -- gold
  corroboration for the Clarity-sourced plateau. (Registered-voter figure
  71,961 in the article vs. certified 71,979 in the SoV is the normal
  small drift between an election-night snapshot and the certified roll.)

**Arithmetic:** 13,417 / 24,810 = 54.0790...% -> **54.08%**.

**Draft row:**
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 13417,
  "certified_final": 24810,
  "election_night_pct": 54.08,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20260710214927/https://results.enr.clarityelections.com/CA/Madera/114136/295158/json/sum.json",
  "confidence": "primary",
  "note": "Numerator 13,417 = total Ballots Cast (Contests[0].BC) from Madera County's Clarity ENR election-night data version 295158 (results.enr.clarityelections.com/CA/Madera/114136/295158/json/sum.json). websiteupdatedat = '6/7/2022 10:36:58 PM PDT' -- the last election-night report (progression: v295035 8:11PM 12,121 -> v295150 10:00PM 12,470 -> v295158 10:36PM 13,417). It is the election-night plateau and HELD STEADY: the next version v295333 ('6/8/2022 2:45:05 PM PDT', ~16hrs later) still shows BC 13,417; only v295603 ('6/10/2022 1:43:41 PM', 2 more days later) shows the canvass resuming (17,214). Certified version v298654 ('6/22/2022', BC 24,810) exactly matches the SoS SoV Total Voters. Certified final 24,810 (CA SoS 'Voter Participation Statistics by County'; Madera 33 vote centers, 93,606 eligible, 71,979 registered, 1,333 precinct + 23,477 VBM). pct = 13,417/24,810 = 54.08%. INDEPENDENT CORROBORATION: Sierra News Online 'Local Primary Election Results' (published 6/8/2022, https://sierranewsonline.com/local-primary-election-results/) states verbatim '13,417 ballots were cast in yesterdays primary for a turnout of 18.64%' with 71,961 registered voters cited -- an independently-authored news source giving the identical 13,417 figure the morning after, confirming the Clarity numerator is not a citation artifact. Freshly archived to Wayback (snapshot 20260710214927, re-verified BC=13417). Post-e-pollbook / post-VCA (adopted 2018), post-ASV n/a (never adopted)."
}
```

**VERIFY.md line:** `| 2022 | statewide-primary | 13,417 | 24,810 | 54.08% | primary | [link](https://web.archive.org/web/20260710214927/https://results.enr.clarityelections.com/CA/Madera/114136/295158/json/sum.json) |`
**Detail bullet:** "2022 statewide-primary -- night 13,417 / final 24,810 = 54.08% (primary). look for: Clarity version 295158, `Contests[0].BC` = 13417, `websiteupdatedat` '6/7/2022 10:36:58 PM PDT', bracket-held through v295333 (6/8 2:45 PM, same BC); independently corroborated by Sierra News Online's June 8, 2022 article quoting the identical 13,417."

**Plateau verdict:** `CONFIRMED` -- basis: Clarity version bracket (same as ITEM 4's pattern) PLUS an independent non-circular news corroboration quoting the identical number the morning after election night -- this is stronger evidence than most rows in the existing dataset.

**render_verified.json entry needed?** No (direct JSON API fetch).

---

## ITEM 6 -- 2024-03-05 (Presidential Primary)

**Certified final:** 27,609 ballots cast (Total Voters), CA SoS "Voter
Participation Statistics by County," 2024 primary SOV.
URL: `https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf`
Line: `Madera* 35 94,531 74,723 1,983 25,626 27,609 92.82% 36.95% 29.21%`
(precincts/vote-centers 35, eligible 94,531, registered 74,723, precinct
1,983 + VBM 25,626 = Total Voters 27,609).

**Plateau:** RECOVERED via Clarity ENR, election id **120377** (confirmed by
a Wayback capture of the election's index page dated 2024-03-06, i.e. the
day after the election).
- 20 published versions (330286 ... 334103). Progression on election night
  (3/5/2024): v330900 (11:25:45 AM, BC 0, pre-poll-close) -> v331222
  (7:07:49 PM, BC 0) -> v331436 (8:05:12 PM, BC 14,497) -> v331598 (9:10:51
  PM, 14,614) -> v331637 (9:33:59 PM, 14,920) -> v331675 (9:55:32 PM,
  15,181) -> **v331700 (10:25:53 PM, BC 16,048)**.
- **Bracket proof:** the next version, v332052, is dated 3/8/2024 3:52:11 PM
  PDT -- almost THREE DAYS later -- and shows the canvass resuming (BC
  jumps to 21,214). No intervening Madera version exists between 10:25 PM
  March 5 and the afternoon of March 8, i.e. 16,048 is unambiguously the
  frozen election-night plateau (the county published nothing more until
  the multi-day canvass resumed).
- Certified version v334103 (3/22/2024) BC = 27,609, exactly matching the
  SoS SoV Total Voters figure.
- Freshly archived to Wayback (snapshot `20260710215117`), re-verified from
  the archived copy (gzip-encoded response, decompressed): `Contests[0].BC`
  = 16048.
- **Independent secondary corroboration (non-circular, strong -- exact
  match):** Sierra News Online, "Unofficial Election Results Pending Final
  Counts" (published March 6, 2024, updated March 7): "This includes 16,048
  ballots cast out of 74,256 registered voters," explicitly reported "as of
  10:25 p.m." on election night from all eight voter centers. This
  independently-authored article gives the EXACT SAME ballot count (16,048)
  AND the exact same internal timestamp (10:25 PM) as Clarity version
  331700 -- about as strong a non-circular confirmation as this dataset
  gets.

**Arithmetic:** 16,048 / 27,609 = 58.1259...% -> **58.13%**.

**Draft row:**
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 16048,
  "certified_final": 27609,
  "election_night_pct": 58.13,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20260710215117/https://results.enr.clarityelections.com/CA/Madera/120377/331700/json/sum.json",
  "confidence": "primary",
  "note": "Numerator 16,048 = total Ballots Cast (Contests[0].BC) from Madera County's Clarity ENR election-night data version 331700 (results.enr.clarityelections.com/CA/Madera/120377/331700/json/sum.json). websiteupdatedat = '3/5/2024 10:25:53 PM PST' -- the last election-night report (progression: v331436 8:05PM 14,497 -> v331598 9:10PM 14,614 -> v331675 9:55PM 15,181 -> v331700 10:25PM 16,048). It is the election-night plateau: the NEXT version, v332052, is dated '3/8/2024 3:52:11 PM PDT' -- almost 3 days later -- where BC jumps to 21,214, i.e. the county published nothing between 10:25 PM March 5 and the afternoon of March 8. Certified version v334103 ('3/22/2024', BC 27,609) exactly matches the SoS SoV Total Voters. Certified final 27,609 (CA SoS 'Voter Participation Statistics by County'; Madera 35 vote centers, 94,531 eligible, 74,723 registered, 1,983 precinct + 25,626 VBM). pct = 16,048/27,609 = 58.13%. INDEPENDENT CORROBORATION (exact match): Sierra News Online 'Unofficial Election Results Pending Final Counts' (published 3/6/2024, https://sierranewsonline.com/unofficial-election-results-pending-final-counts/) states 'This includes 16,048 ballots cast out of 74,256 registered voters', explicitly timestamped 'as of 10:25 p.m.' on election night from all eight voter centers -- an independently-authored article matching BOTH the exact ballot count AND the exact internal timestamp of Clarity version 331700. Freshly archived to Wayback (snapshot 20260710215117, re-verified BC=16048 from the gzip-decoded archived copy). Post-e-pollbook / post-VCA, post-ASV n/a (never adopted)."
}
```

**VERIFY.md line:** `| 2024 | presidential-primary | 16,048 | 27,609 | 58.13% | primary | [link](https://web.archive.org/web/20260710215117/https://results.enr.clarityelections.com/CA/Madera/120377/331700/json/sum.json) |`
**Detail bullet:** "2024 presidential-primary -- night 16,048 / final 27,609 = 58.13% (primary). look for: Clarity version 331700, `Contests[0].BC` = 16048, `websiteupdatedat` '3/5/2024 10:25:53 PM PST', next version 3 days later (3/8) jumps to 21,214; independently corroborated by Sierra News Online's March 6, 2024 article quoting the identical 16,048 ballots and the identical 10:25 PM timestamp."

**Plateau verdict:** `CONFIRMED` -- basis: Clarity version bracket (3-day gap to the next version, the cleanest bracket of the three Clarity rows) PLUS an independent non-circular news article matching both the ballot count AND the internal timestamp exactly. Strongest-evidenced row in this dossier.

**render_verified.json entry needed?** No (direct JSON API fetch; the gzip
content-encoding required manual `gunzip` but that is a transport detail,
not a rendering dependency).

---

## Cross-check against the general-election dataset (sanity)

Madera's like-for-like VCA-era pairs from the existing general-election
JSON: 2018 general 72.26%, 2022 general 58.78%, 2024 general 67.1%. The
primaries recovered here run systematically LOWER than their same-year
generals (2018: 75.41% primary vs 72.26% general -- primary actually a bit
HIGHER; 2022: 54.08% vs 58.78% -- primary lower; 2024: 58.13% vs 67.1% --
primary lower). Primaries have much smaller electorates and historically
slower same-day in-person turnout relative to VBM share, so a somewhat lower
or comparable election-night share versus the same year's general is
plausible and not a red flag; the 2018 case (primary slightly ABOVE its own
year's general) is the one soft anomaly worth a human's eye, though it is
well within plausible range and both years are independently
bracket-confirmed via Clarity, so not flagged as an error, just noted.

## Summary of what's unfinished

- **2012-06-05, 2014-06-03, 2016-06-07**: all three left NULL per RUNBOOK
  5.1, each with a full documented search trail (Wayback CDX across both
  known 2010s-era Madera domains, explicit Election-ID probing for 2016,
  Clarity-nonexistence confirmation, and WebSearch/WebFetch of local news
  archives). 2016 carries a soft FLAG for a human operator to try the live
  Wayback UI on Election29-32 (CDX shows Election30 existed as a dead link
  by 2019, so SOME page existed under that scheme; not independently
  confirmed as the June 2016 primary, and no content was ever archived
  either way).
- **2018-06-05, 2022-06-07, 2024-03-05**: all three fully recovered at
  `primary` confidence with bracket-proof plateau evidence (Clarity version
  brackets showing multi-hour-to-multi-day gaps before the canvass
  resumed), and two of the three (2022, 2024) have independent non-circular
  news corroboration matching the Clarity numbers exactly.
- No repo file was created, edited, or committed. This dossier is scratch
  only; a human/maintainer would still need to: (1) decide whether to
  formally extend `data/research/election-night/madera-ca.json`'s schema to
  include primaries (today it holds only generals) or start a new file;
  (2) if extending, run the full pipeline (RUNBOOK section 3) after adding
  rows; (3) resolve the 2016 soft FLAG if desired.
