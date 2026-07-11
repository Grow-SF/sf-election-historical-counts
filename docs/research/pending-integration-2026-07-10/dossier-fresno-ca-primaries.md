# Fresno County (fresno-ca) — statewide PRIMARY election-night dossier

Read-only research scout output. Nothing in this file has been written to the
repo. `data/research/election-night/fresno-ca.json` today only carries the six
November GENERALS (2012, 2014, 2016, 2018, 2022, 2024); this dossier covers the
companion six statewide PRIMARIES (2012-06-05, 2014-06-03, 2016-06-07,
2018-06-05, 2022-06-07, 2024-03-05) that bracket the same 2020 e-pollbook/ASV
adoption. Adoption years (from the existing file): `epollbook: 2020, asv:
2020` — so 2012/2014/2016/2018 are pre/pre and 2022/2024 are post/post.

**Good news for the operator:** `scripts/build_county_night.py` ALREADY
supports primary row types (`norm_type()` maps raw `"presidential-primary"` ->
`presidential-primary`, raw `"statewide-primary"` -> `midterm-primary`; see its
module docstring). No code change is needed to merge these rows once a human
reviews them — only the chart-rendering layer currently filters primary points
out (editorial decision already documented in that script, not a blocker for
adding data).

Network note: `web.archive.org` was intermittently refusing connections during
this research session (likely load from several other counties' concurrent
primary research passes sharing this host/scratch dir — see
`dossier-riverside-ca-primaries.md`, `dossier-sacramento-ca-primaries.md`,
`dossier-san-bernardino-ca-primaries.md`, `dossier-san-diego-ca-primaries.md`
alongside this file). Every fetch below was retried with backoff until it
returned HTTP 200; no result here is a false NOT_FOUND from a transient
network failure.

## Summary

| Date | Type | Plateau ballots | Certified final | Share | Confidence | Evidence class |
|---|---|---:|---:|---:|---|---|
| 2012-06-05 | presidential-primary | — | 113,975 | — | none | null (only Official Final canvass survives) |
| 2014-06-03 | statewide-primary | — | 107,805 | — | none | null (only Official Final canvass survives) |
| 2016-06-07 | presidential-primary | — | 169,333 | — | none | null (only Certified Official canvass survives; no no-dash night file archived, unlike Nov 2016) |
| 2018-06-05 | statewide-primary | 112,403 (ceiling) | 136,388 | 82.41% (ceiling, NOT plateau) | secondary | ceiling, comparable=false |
| 2022-06-07 | statewide-primary | — | 136,114 | — | none | null (only Official Final canvass survives) |
| 2024-03-05 | presidential-primary | 143,879 (ceiling) | 156,425 | 91.98% (ceiling, NOT plateau) | secondary | ceiling, comparable=false |

Denominators are SOLID for all six: every SoS SoV "Total Voters" figure is
independently cross-checked against the county's own archived "Cards
Cast"/"Voters Cast" **certified/Official-Final** canvass report, and all six
match EXACTLY (113,975 / 107,805 / 169,333 / 136,388 / 136,114 / 156,425).
Numerators: FOUR of six are genuine election-night dead ends (null per 5.1,
matching the pattern already established for this county's 2012/2014/2018/2022
GENERALS); TWO (2018, 2024) recovered a documented CEILING — a real,
post-election-night ballot count strictly below the plateau — which is more
useful than a bare null but is explicitly NOT the election-night share.
**No true election-night plateau was recovered for any of the six primaries.**
This matches the county's general-election pattern: Fresno's GEMS/Dominion
systems only reliably preserve a frozen election-night snapshot when a
no-dash live file happens to get crawled before it's overwritten (as happened
for the 2016 GENERAL and the 2024 GENERAL); Wayback never crawled an
analogous primary-night snapshot in any of the six years checked.

---

## Denominators (CA SoS Statement of Vote, "Voter Participation Statistics by County")

All fetched and read directly with `pdftotext -layout`; Fresno's row quoted in
full (columns: Precincts / Eligible to Register / Registered Voters / Precinct
Voters / VBM Voters / **Total Voters** / %VBM / Turnout-of-Registered /
Turnout-of-Eligible). `certified_final` = the **Total Voters** column
(precinct + VBM), matching the convention already used in this county's
general-election rows.

| Election | SoV URL | Fresno row |
|---|---|---|
| 2012-06-05 | `https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf` | Precincts 484, Eligible 556,382, Registered 390,587, Precinct 38,890, VBM 75,085, **Total 113,975**, %VBM 65.88%, Turnout/Reg 29.18%, Turnout/Elig 20.49% |
| 2014-06-03 | `https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf` (misspelling intact, per runbook 6.1) | Precincts 447, Eligible 569,314, Registered 412,181, Precinct 31,764, VBM 76,041, **Total 107,805**, %VBM 70.54%, Turnout/Reg 26.15%, Turnout/Elig 18.94% |
| 2016-06-07 | `https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf` (NB: no `sov/` sub-segment, unlike 2018/2022/2024) | Precincts 510, Eligible 580,678, Registered 414,976, Precinct 67,266, VBM 102,067, **Total 169,333**, %VBM 60.28%, Turnout/Reg 40.81%, Turnout/Elig 29.16% |
| 2018-06-05 | `https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf` | Precincts 481, Eligible 594,711, Registered 440,617, Precinct 47,937, VBM 88,451, **Total 136,388**, %VBM 64.85%, Turnout/Reg 30.95%, Turnout/Elig 22.93% |
| 2022-06-07 | `https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf` | "Fresno\*" (VCA county footnote), Precincts 328, Eligible 642,055, Registered 498,759, in-person 10,371, VBM 125,743, **Total 136,114**, %VBM 92.38%, Turnout/Reg 27.29%, Turnout/Elig 21.20% |
| 2024-03-05 | `https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf` | "Fresno\*" (VCA county footnote), Precincts 301, Eligible 643,186, Registered 506,668, in-person 16,109, VBM 140,316, **Total 156,425**, %VBM 89.70%, Turnout/Reg 30.87%, Turnout/Elig 24.32% |

URL-pattern gotchas found while locating these (worth adding to runbook 6.1 if
a maintainer wants to generalize it beyond generals): 2012 primary uses
`pdf/03-voter-reg-stats-by-county.pdf` (not "participation"); 2016 primary
drops the `sov/` sub-path segment that 2018/2022/2024 all have; 2014 keeps the
general-election misspelling `particpiation`. All four other guessed
permutations 403'd — do not assume the general-year URL shape transfers to the
matching primary without probing.

Cross-check performed for every year: the county's own GEMS/Dominion
Official-Final "Cards Cast"/"Voters Cast" total (see numerator notes below)
equals the SoV Total Voters figure exactly in all six cases — strong
independent confirmation the denominators are correct.

---

## 2012-06-05 — presidential-primary — NULL

**Certified final:** 113,975 (precinct 38,890 + VBM 75,085; 29.18% of 390,587
registered), source
`https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf`.

**Numerator routes tried (all dead ends):**
- Runbook 6.3 no-dash GEMS live-file convention (`Results20120605.htm`, the
  same pattern that recovered the 2016 GENERAL): CDX
  `https://web.archive.org/cdx/search/cdx?url=www2.co.fresno.ca.us/2850/Results/Results20120605.htm&output=json` →
  `[]`, zero captures. Never crawled.
- Dashed file `Results-2012-06-05.htm`: exactly ONE Wayback capture,
  2012-12-20 00:25:36 UTC (44 days post-election). Fetched via
  `https://web.archive.org/web/20121220040226id_/http://www2.co.fresno.ca.us/2850/Results/Results-2012-06-05.htm`;
  internal GEMS header reads "GEMS ELECTION RESULTS ... Presidential Primary
  Election Summary ... Fresno County **Final Official Report 06/27/12
  13:07:07** Registered Voters 390579 - **Cards Cast 113975** 29.18% Num.
  Report Precinct 484 - Num. Reporting 484 100.00%" — the Official Final
  canvass, Cards Cast = certified total exactly. Not an election-night report.
- `Results-1.pdf` in the same folder (captured 2012-12-20 00:25:36 UTC,
  same day as the htm) — same-day capture strongly implies the same Official
  Final PDF companion; not independently opened given the htm already
  confirms the Official Final content and timestamp.
- CMS page `results-of-june-5-2012-presidential-primary-election`
  (`co.fresno.ca.us/departments/county-clerk-registrar-of-voters/election-information/election-results/`):
  earliest Wayback capture 2018-02-01, 5.7 years post-election — far too late
  to reflect anything but the same stale Official Final; not opened (would
  only reproduce the number already confirmed above).
- News (route 6.6): WebSearch `"Fresno County June 5 2012 primary election
  night ballots counted results"` returned only the SoS/county certified-final
  pages and a Fresnoland 2026 article (unrelated, current-year contamination);
  no distinct election-night ballot count in press coverage.

**Conclusion:** null per runbook 5.1, matching the identical dead end already
documented for this county's 2012 GENERAL (same GEMS system, same absence of
a no-dash frozen night file).

### Draft row (section 2 schema)
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 113975,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 113,975 ballots cast (CA SoS SoV, Voter Participation Stats by County: precinct 38,890 + VBM 75,085; 29.18% of 390,587 registered). Pre-adoption (both e-pollbook and ASV adopted 2020), precinct-based. Election-night PLATEAU not sourceable. The runbook 6.3 no-dash GEMS live-file convention that recovered the 2016 GENERAL (Results20120605.htm) has ZERO Wayback captures for this primary. The only archived report in the Results/ folder is the dashed Results-2012-06-05.htm, captured once (2012-12-20, 44 days post-election): internal GEMS header 'Fresno County Final Official Report 06/27/12 13:07:07 ... Cards Cast 113975 29.18%' = certified final exactly, 100% of 484 precincts -- the OFFICIAL FINAL canvass, not an election-night snapshot. The CMS-embedded results page (results-of-june-5-2012-presidential-primary-election) has no capture earlier than 2018-02-01 (5.7 years post-election). No election-night news total found via WebSearch. Null per definition (never substitute a different denominator or report time)."
}
```

### Draft VERIFY.md line
Summary table row: `| 2012 | presidential-primary | — | 113,975 | — | none | — (not sourceable) |`

Detail bullet:
> - **2012 presidential-primary** — night `—` / final `113,975` = `—` (none)
>   - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf>
>   - look for: Certified final 113,975 ballots cast (precinct 38,890 + VBM 75,085). Election-night PLATEAU not sourceable: the no-dash GEMS live-file convention (Results20120605.htm) has zero Wayback captures; the only surviving Results/-folder report (Results-2012-06-05.htm, one capture, 2012-12-20) is headered "Final Official Report 06/27/12", Cards Cast 113,975 = certified final exactly, 44 days post-election.

Plateau verdict: not applicable (no sourced row; null rows carry no
`plateau_review.json` entry per runbook 5.5/8).

---

## 2014-06-03 — statewide-primary — NULL

**Certified final:** 107,805 (precinct 31,764 + VBM 76,041; 26.15% of 412,181
registered), source
`https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf`.

**Numerator routes tried (all dead ends):**
- No-dash `Results20140603.htm`: CDX `[]`, zero captures.
- Dashed `Results-2014-06-03.htm`: ONE capture, 2014-08-25 03:14:01 UTC (83
  days post-election). Fetched via
  `https://web.archive.org/web/20140825031401id_/http://www2.co.fresno.ca.us/2850/Results/Results-2014-06-03.htm`;
  content: "FRESNO COUNTY, CA JUNE 3, 2014 STATEWIDE PRIMARY ELECTION
  **OFFICIAL FINAL SUMMARY REPORT** 06/20/14 15:23:18 ... Registered Voters
  412127 - Cards Cast 107805 26.16% ... Num. Report Precinct 447 - Num.
  Reporting 447 100.00%" — Official Final canvass, exact certified match.
- `Results-2014-06-03.pdf` (same folder, captured 2014-10-21): not opened,
  same-era companion PDF to the confirmed Official Final htm.
- CMS page `results-of-june-3-2014-statewide-direct-primary-election`:
  earliest capture 2018-02-04 (3.7 years post-election), far too late.
- News: WebSearch `"Fresno County June 3 2014 primary election night ballots
  counted turnout"` returned only 2026-primary contamination (ABC30/GV Wire
  articles about the CURRENT June 2026 primary, not 2014) — no usable 2014
  election-night source.

**Conclusion:** null per runbook 5.1, matching this county's 2014 GENERAL
(also GEMS-era, also only-Official-Final-survives).

### Draft row (section 2 schema)
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 107805,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 107,805 ballots cast (CA SoS SoV; precinct 31,764 + VBM 76,041; 26.15% of 412,181 registered). Pre-adoption, precinct-based. Election-night PLATEAU not sourceable. No-dash GEMS convention (Results20140603.htm) has zero Wayback captures. The only archived Results/-folder report, Results-2014-06-03.htm (one capture, 2014-08-25, 83 days post-election), is headered 'OFFICIAL FINAL SUMMARY REPORT 06/20/14 15:23:18', Cards Cast 107,805 = certified final exactly, 100% of 447 precincts. CMS-embedded results page's earliest capture is 2018-02-04 (3.7 years post-election). WebSearch for an election-night news total returned only 2026-primary contamination, no 2014-specific figure. Null per definition."
}
```

### Draft VERIFY.md line
Summary table row: `| 2014 | statewide-primary | — | 107,805 | — | none | — (not sourceable) |`

Detail bullet:
> - **2014 statewide-primary** — night `—` / final `107,805` = `—` (none)
>   - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf>
>   - look for: Certified final 107,805 ballots cast (precinct 31,764 + VBM 76,041). Election-night PLATEAU not sourceable: no no-dash live-file capture exists; the only surviving report (Results-2014-06-03.htm, one capture, 2014-08-25) is headered "OFFICIAL FINAL SUMMARY REPORT 06/20/14", Cards Cast 107,805 = certified final exactly, 83 days post-election.

Plateau verdict: not applicable (null row).

---

## 2016-06-07 — presidential-primary — NULL

**Certified final:** 169,333 (precinct 67,266 + VBM 102,067; 40.81% of
414,976 registered), source
`https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf`.

**Numerator routes tried (all dead ends) — the interesting negative result:**
- No-dash `Results20160607.htm` — **this is the exact filename PATTERN that
  recovered the 2016 GENERAL's election-night plateau** (`Results20161108.htm`,
  frozen at the 11/9/2016 1:42 AM report). Probed directly: CDX
  `url=www2.co.fresno.ca.us/2850/Results/Results20160607.htm` → `[]`, zero
  captures. **Wayback never crawled the primary's no-dash file at all** — the
  general got lucky (crawled before the file was overwritten with the final
  canvass); the primary was not.
- Dashed `Results-2016-06-07.htm`: ONE capture, 2016-07-17 06:34:29 UTC (40
  days post-election). Fetched via
  `https://web.archive.org/web/20160717063429id_/http://www2.co.fresno.ca.us/2850/Results/Results-2016-06-07.htm`;
  content: "Fresno County June 7, 2016 Presidential Primary Election
  **Certified Official Results** 07/01/16 11:45:32 ... Registered Voters
  415217 - Cards Cast 169333 40.78% ... Num. Report Precinct 510 - Num.
  Reporting 510 100.00%" — certified canvass, exact match.
- `results-2016-06-07.pdf` — CDX showed a capture dated 2016-04-17 19:20:29
  UTC, i.e. **before** the election (June 7). Fetched it directly to check
  for a mis-dated capture: it is a genuine pre-election placeholder page,
  "Presidential Primary Election Results Coming Soon / June 7, 2016" — no
  data, confirms the capture date is correct and this is simply a
  not-yet-populated file, not a numerator lead.
- CMS page `results-of-june-7-2016-presidential-primary-election`: earliest
  capture 2018-02-04, 1.7 years post-election, far too late.
- News: WebSearch `"Fresno County June 7 2016 presidential primary election
  night ballots counted results Bee"` returned only the certified-final PDF
  and current-2026-primary contamination; no on-night figure.

**Conclusion:** null per runbook 5.1. Worth flagging explicitly: the runbook's
own route-6.3 table cites the Fresno no-dash filename convention as reliable
evidence for one general (2016); this research confirms it is NOT reliable
across the board — it depends entirely on Wayback's crawl timing, and for the
2016 primary specifically the crawler simply never visited that URL before the
county overwrote it.

### Draft row (section 2 schema)
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 169333,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 169,333 ballots cast (CA SoS SoV; precinct 67,266 + VBM 102,067; 40.81% of 414,976 registered). Pre-adoption, precinct-based. Election-night PLATEAU not sourceable. IMPORTANT NEGATIVE RESULT: the exact no-dash GEMS filename convention that recovered THIS COUNTY'S 2016 GENERAL plateau (Results20161108.htm, frozen at 11/9/2016 1:42 AM) has zero Wayback captures for the primary equivalent (Results20160607.htm) -- the general was crawled before being overwritten, the primary never was. The only archived Results/-folder report is the dashed Results-2016-06-07.htm (one capture, 2016-07-17, 40 days post-election), headered 'Certified Official Results 07/01/16 11:45:32', Cards Cast 169,333 = certified final exactly, 100% of 510 precincts. A same-named results-2016-06-07.pdf captured 2016-04-17 (pre-election) was checked directly and is a placeholder page ('Results Coming Soon'), not data. CMS-embedded results page's earliest capture is 2018-02-04. No election-night news total found. Null per definition."
}
```

### Draft VERIFY.md line
Summary table row: `| 2016 | presidential-primary | — | 169,333 | — | none | — (not sourceable) |`

Detail bullet:
> - **2016 presidential-primary** — night `—` / final `169,333` = `—` (none)
>   - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf>
>   - look for: Certified final 169,333 ballots cast (precinct 67,266 + VBM 102,067). Election-night PLATEAU not sourceable: unlike the 2016 GENERAL, the no-dash GEMS live-file convention (Results20160607.htm) was never crawled by Wayback; the only surviving report (Results-2016-06-07.htm, one capture, 2016-07-17) is headered "Certified Official Results 07/01/16", Cards Cast 169,333 = certified final exactly, 40 days post-election.

Plateau verdict: not applicable (null row).

---

## 2018-06-05 — statewide-primary — CEILING (comparable: false)

**Certified final:** 136,388 (precinct 47,937 + VBM 88,451; 30.95% of
440,617 registered), source
`https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf`.

**Numerator (best available, NOT the true plateau):**
CMS page
`co.fresno.ca.us/departments/county-clerk-registrar-of-voters/election-information/election-results/results-for-june-5-2018-statewide-primary-election`
(the analogous page to the one used for the 2018 GENERAL) has 13 Wayback
captures. The EARLIEST is
`https://web.archive.org/web/20180610030903/http://www.co.fresno.ca.us:80/departments/county-clerk-registrar-of-voters/election-information/election-results/results-for-june-5-2018-statewide-primary-election`
(crawl timestamp 2018-06-10; the report's own embedded GEMS internal
timestamp is 06/08/18 14:21:09 — Friday, June 8, 3 days after the Tuesday
election). Content: "Election Summary Report Statewide Primary Election
Summary ... Fresno County June 5, 2018 **Unofficial Final Results 06/08/18
14:21:09** Registered Voters 438782 - **Cards Cast 112403** 25.62% Num.
Report Precinct 481 - Num. Reporting 481 100.00%".

No earlier capture of this URL, nor of any other candidate (no-dash/dashed
Results/ files, `/2850/post/2018June5/` folder — checked, contains only 2
pre-election admin PDFs) exists anywhere. 112,403 is genuinely the
earliest-surviving snapshot.

**Why this is a CEILING, not the plateau (contamination check per runbook
7.3):** fetched every later capture of the same URL. By the very next capture,
`https://web.archive.org/web/20180711104507/...` (2018-07-11), the SAME page
shows "**Official Final Results 06/26/18 14:38:06** ... Cards Cast 136388
31.08%" = the certified total exactly (confirmed unchanged across 4 further
captures through 2019-10-15). Since 112,403 (06/08) ≠ 136,388 (06/26 =
certified), the page provably kept tracking the canvass after June 8; 112,403
is at least ~24,000 ballots short of the true final and cannot be the
election-night plateau (Tuesday-to-Friday, 3 days, matches this county's
documented Friday canvass-update cadence — see the 2018 GENERAL note's
ABC30/GV Wire citation of the same weekly rhythm).

**Arithmetic (ceiling, not the election-night share):** 112,403 / 136,388 =
82.41%. This overstates the true (unrecoverable) election-night share.

**Conclusion:** kept as a documented CEILING per runbook 5.2 (`comparable:
false`, `confidence: "secondary"`) — closer and more evidenced than the 2018
GENERAL's flat null (that one's earliest capture was 3 WEEKS out, this one is
3 DAYS out and explicitly self-labeled "Unofficial Final Results"), but it is
NOT election night and must never be read as the plateau.

### Draft row (section 2 schema)
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 112403,
  "certified_final": 136388,
  "election_night_pct": 82.41,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20180610030903/http://www.co.fresno.ca.us/departments/county-clerk-registrar-of-voters/election-information/election-results/results-for-june-5-2018-statewide-primary-election",
  "confidence": "secondary",
  "comparable": false,
  "note": "CEILING, NOT the election-night plateau (comparable=false). Certified final 136,388 ballots cast (CA SoS SoV; precinct 47,937 + VBM 88,451; 30.95% of 440,617 registered). Best-available numerator: the county's CMS-embedded GEMS report at the June-5-2018-primary results page, EARLIEST surviving Wayback capture 2018-06-10 (embedded report internally timestamped 06/08/18 14:21:09, i.e. the Friday 3 days after the Tuesday election -- matches this county's documented Friday canvass-update cadence, not election night), labeled 'Unofficial Final Results', Cards Cast 112,403 (25.62%), 100% of 481 precincts. PROVEN not the plateau: the SAME URL's next capture (2018-07-11) shows 'Official Final Results 06/26/18 14:38:06', Cards Cast 136,388 = certified final exactly (confirmed unchanged through 4 further captures to 2019-10-15) -- the page was still tracking the canvass after 06/08, so 112,403 undercounts the true final by ~24,000 ballots and cannot be the plateau. No earlier capture of this or any candidate URL exists (checked: no-dash/dashed Results/-folder files -- none archived for 2018 at all; /2850/post/2018June5/ folder -- only 2 pre-election admin PDFs). 112,403 / 136,388 = 82.41% (a CEILING on the unarchived true election-night share, which is necessarily lower). Pre-epollbook AND pre-ASV (both adopted 2020). FLAG for manual operator: confirm the 06/08/18 14:21:09 embedded timestamp and the 06/26/18 14:38:06 successor timestamp by opening both Wayback captures directly, since this conclusion rests on reading two internal GEMS report headers, not a machine string match."
}
```

### Draft VERIFY.md line
Summary table row (⚠️ per runbook 5.2 comparable=false convention):
`| 2018 ⚠️ | statewide-primary | 112,403 | 136,388 | 82.41%\* | secondary | [results page, 06/08/18 report](https://web.archive.org/web/20180610030903/http://www.co.fresno.ca.us/departments/county-clerk-registrar-of-voters/election-information/election-results/results-for-june-5-2018-statewide-primary-election) |`

Detail bullet:
> - **2018 statewide-primary** — night `112,403` / final `136,388` = `82.41%` **(CEILING, not the plateau — comparable=false)**
>   - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf>
>   - numerator (ceiling): <https://web.archive.org/web/20180610030903/http://www.co.fresno.ca.us/departments/county-clerk-registrar-of-voters/election-information/election-results/results-for-june-5-2018-statewide-primary-election>
>   - look for: embedded GEMS report "Unofficial Final Results 06/08/18 14:21:09", Cards Cast 112,403. This is 3 days post-election (Friday canvass cadence), NOT election night; the same page's 2018-07-11 capture shows "Official Final Results 06/26/18", Cards Cast 136,388 = certified, proving the number was still climbing on 06/08. Kept only as a documented ceiling.

Draft `plateau_review.json` entry:
```json
{
 "slug": "fresno-ca",
 "date": "2018-06-05",
 "verdict": "REFUTED_AS_PLATEAU",
 "basis": "earliest-surviving capture provably tracked the canvass past its own timestamp",
 "evidence": "cited capture's internal GEMS timestamp is 06/08/18 14:21:09 (3 days post-election, Friday canvass-cadence), 'Unofficial Final Results' at 100% precincts, Cards Cast 112,403; the SAME URL's next available capture (2018-07-11) shows 'Official Final Results 06/26/18 14:38:06', Cards Cast 136,388 = certified exactly -- proves the count kept climbing after 06/08, so 112,403 is not the plateau; no earlier capture of this or any other candidate URL exists; retained as a documented ceiling (comparable=false, secondary)"
}
```

---

## 2022-06-07 — statewide-primary — NULL

**Certified final:** 136,114 (in-person 10,371 + VBM 125,743; 27.29% of
498,759 registered; VCA vote-center county), source
`https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf`.

**Numerator routes tried (all dead ends):**
- CMS page `co.fresno.ca.us/departments/county-clerk-registrar-of-voters/election-races/statewide-direct-primary-election-june-2022`:
  exactly ONE capture, 2022-05-02 (pre-election). Fetched and enumerated its
  links: all point to pre-election voter-guide/candidate-statement PDFs via
  `/home/showpublisheddocument/...` — the identical pattern already documented
  as a dead end for this county's Nov 2022 general (many candidate PDFs, no
  results report). No post-election capture of this page exists.
- Dominion filename-convention folder (live-site-confirmed path)
  `fresnocountyca.gov/.../1_election-results-page-sov-ssov/2022/june-primary/`:
  CDX-enumerated in full; only ONE `electionsummaryreportrpt`-pattern file was
  ever crawled: `66298-final_electionsummaryreportrpt_07072022.pdf`
  (captured 2023-09-07, but internally dated 7/7/2022 9:25:05 AM — 30 days
  post-election). Opened directly: "FRESNO COUNTY STATEWIDE DIRECT PRIMARY
  ELECTION JUNE 7, 2022 **FINAL OFFICIAL RESULTS** ... Precincts Reported: 328
  of 328 (100.00%) Voters Cast: **136,114** of 498,698 (27.29%)" — exact
  certified match. No election-night-dated file (e.g. an
  `electionsummaryreportrpt_6_7_22_HHMM.pdf` analogous to the Nov 2024
  general's `electionsummaryreportrpt_11_5_24_1231.pdf`) was ever archived.
- News: WebSearch `"Fresno County" June 7 2022 primary election night ballots
  counted ABC30 GV Wire` returned only the county's own results page and
  ABC30/GV Wire articles that, on inspection, are about the CURRENT (2026)
  June primary — dated 2026-06-10, not 2022 — no usable 2022-specific article
  surfaced.

**Conclusion:** null per runbook 5.1, matching this county's 2022 GENERAL
(same VCA-vote-center era, same "only the zero report / final report get
archived" pattern; post-epollbook, post-ASV, both adopted 2020).

### Draft row (section 2 schema)
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 136114,
  "election_night_pct": null,
  "vs_epollbook": "post",
  "vs_asv": "post",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 136,114 ballots cast (CA SoS SoV; in-person 10,371 + VBM 125,743; 27.29% of 498,759 registered; VCA vote-center county). Post-adoption (e-pollbooks + ASV, both 2020). Election-night PLATEAU not sourceable. The live CMS results page (election-races/statewide-direct-primary-election-june-2022) has only ONE Wayback capture, 2022-05-02 (pre-election), linking only candidate/voter-guide PDFs -- the same pattern already documented for this county's Nov 2022 general. The Dominion electionsummaryreportrpt-pattern folder (fresnocountyca.gov .../2022/june-primary/) was fully enumerated: the only such file ever crawled is 66298-final_electionsummaryreportrpt_07072022.pdf, internally dated 7/7/2022 9:25:05 AM (30 days post-election), 'FINAL OFFICIAL RESULTS ... Voters Cast: 136,114 of 498,698 (27.29%)' = certified exactly. No election-night-dated report file was ever archived. WebSearch for a same-night news figure returned only current-2026-primary contamination (dated articles were 2026-06-10, not 2022). Null per definition."
}
```

### Draft VERIFY.md line
Summary table row: `| 2022 | statewide-primary | — | 136,114 | — | none | — (not sourceable) |`

Detail bullet:
> - **2022 statewide-primary** — night `—` / final `136,114` = `—` (none)
>   - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf>
>   - look for: Certified final 136,114 ballots cast (in-person 10,371 + VBM 125,743). Election-night PLATEAU not sourceable: the live results page's only capture is pre-election; the only electionsummaryreportrpt file ever archived is the FINAL OFFICIAL RESULTS dated 7/7/2022, Voters Cast 136,114 = certified final exactly, 30 days post-election.

Plateau verdict: not applicable (null row).

---

## 2024-03-05 — presidential-primary — CEILING (comparable: false)

**Certified final:** 156,425 (in-person 16,109 + VBM 140,316; 30.87% of
506,668 registered; VCA vote-center county), source
`https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf`.

**GOTCHA found and avoided:** the county's CMS asset folder that holds this
election's files (`fresnocountyca.gov/.../1_election-results-page-sov-ssov/2024/`)
ALSO holds `statementofvotescastrpt_03262024.xlsx` /
`_03282024.pdf` / `_03292024.pdf` / `supplementalstatementofvotescastrpt_03292024.*`.
These look, by filename, like they could be this primary's late-March canvass
reports. **They are not.** Opened `statementofvotescastrpt_03282024.pdf`
directly: its header reads "FRESNO COUNTY **CONGRESSIONAL DISTRICT 20 SPECIAL
PRIMARY ELECTION MARCH 19, 2024** STATEMENT OF VOTES" — a completely different,
concurrent March 2024 election (the CD-20 special primary), sharing the same
top-level `2024/` asset folder. Do not reuse those files for this row; the
actual March 5 presidential primary's results live in a SEPARATE CMS folder,
`1_election-pages/2024_03-march-primary/`.

**Numerator (best available, NOT the true plateau):**
That correct folder was CDX-enumerated in full (100+ files: almost entirely
pre-election voter-guide/candidate/measure PDFs). Only TWO
`electionsummaryreportrpt`-pattern files were ever crawled:
`02212024_zero_report_electionsummaryreportrpt_zerorpt.pdf` (pre-election zero
report, Feb 21) and `electionsummaryreportrpt_03292024.pdf` (captured
2024-05-13, internally dated 3/29/2024 4:06:52 PM — 24 days post-election).
Opened the latter directly: "FRESNO COUNTY CONSOLIDATED PRESIDENTIAL PRIMARY
ELECTION MARCH 5, 2024 **OFFICIAL RESULTS** ... Precincts Reported: 301 of 301
(100.00%) Voters Cast: **156,425** of 507,259 (30.84%)" — exact certified
match (the 507,259-vs-506,668-registered discrepancy is a late roll update,
immaterial to Voters Cast). No election-night-dated report (analogous to the
Nov 2024 general's `electionsummaryreportrpt_11_5_24_1231.pdf`) exists in this
folder.

News (route 6.6) gave the closest available figure. Fresnoland's live-blog
`fresnoland.org/2024/03/05/fresno-county-live-election-results-march-2024-primary/`
was, per its own URL and dateline, originally published election night — but
its ONLY Wayback capture during election week
(`https://web.archive.org/web/20240305234705/...`) is timestamped 2024-03-05
23:47 UTC = 15:47 PST, **before** polls even closed (8 PM PST / 04:00 UTC
3/6), so it shows no real count. The page was subsequently edited in place
(WordPress live-blog pattern, matches this outlet's known behavior); its
current/only-surviving text carries the byline "March 5, 2024 Updated March
12, 2024" and states: "One week after election day, local election officials
have counted **143,879 ballots** — chalking up a 28% voter turnout in Fresno
County for the 2024 presidential primary election." A related Fresnoland
article, `fresnoland.org/2024/03/08/march-primary-turnout-creeps-upward-...`
(published 2024-03-08, 3 days post-election, "Friday morning"), gives only a
percentage ("just under 21% ... turnout ... as of Friday morning" — no raw
ballot count, so not directly usable) and quotes Registrar James Kus
describing an ongoing count with ~40,000 mail ballots + 500 provisionals
still to add at that point, consistent with the total climbing from ~21% on
3/8 to 28% (143,879) by 3/12 to the certified 30.84% (156,425) by 3/29.

**Why this is a CEILING, not the plateau:** March 12 is one week (7 days)
post-election, not election night; the true election-night count is
necessarily lower. No Wayback capture, county document, or news account gives
an election-night-specific (March 5 evening / March 6 early-morning) total.

**Arithmetic (ceiling, not the election-night share):** 143,879 / 156,425 =
91.98%. This is a fairly loose ceiling (7 days of canvassing already folded
in) and materially overstates whatever the true election-night share was.

**Conclusion:** kept as a documented CEILING per runbook 5.2 (`comparable:
false`, `confidence: "secondary"`, sourced to a news outlet quoting the
registrar's office, not a verbatim county press release, so secondary rather
than primary per runbook 5.3).

### Draft row (section 2 schema)
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 143879,
  "certified_final": 156425,
  "election_night_pct": 91.98,
  "vs_epollbook": "post",
  "vs_asv": "post",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://fresnoland.org/2024/03/05/fresno-county-live-election-results-march-2024-primary/",
  "confidence": "secondary",
  "comparable": false,
  "note": "CEILING, NOT the election-night plateau (comparable=false). Certified final 156,425 ballots cast (CA SoS SoV; in-person 16,109 + VBM 140,316; 30.87% of 506,668 registered; VCA vote-center county). GOTCHA avoided: the CMS asset folder .../1_election-results-page-sov-ssov/2024/ also holds statementofvotescastrpt_0326/0328/0329-2024 files that LOOK like this election's late canvass but are actually for a different, concurrent election (opened statementofvotescastrpt_03282024.pdf directly: header is 'CONGRESSIONAL DISTRICT 20 SPECIAL PRIMARY ELECTION MARCH 19, 2024'), not reused here. The correct folder (1_election-pages/2024_03-march-primary/) was fully CDX-enumerated: the only electionsummaryreportrpt files are the pre-election zero report and electionsummaryreportrpt_03292024.pdf (3/29/2024 4:06:52 PM, 24 days post-election), 'OFFICIAL RESULTS ... Voters Cast: 156,425 of 507,259' = certified exactly -- no election-night-dated report survives. Best available numerator: Fresnoland's live-results post (originally published election night per its URL/dateline, but its only election-week Wayback capture, 2024-03-05 23:47 UTC = 15:47 PST, is BEFORE poll close and shows no count; the page was later edited in place) carries byline 'Updated March 12, 2024' and states 'One week after election day, local election officials have counted 143,879 ballots -- chalking up a 28% voter turnout.' A companion Fresnoland article (2024-03-08, 3 days out) gives only a percentage (~21%) with no raw count and quotes Registrar James Kus describing an ongoing count of ~40,000 remaining mail ballots at that point, consistent with the climb from 21% (3/8) to 28%/143,879 (3/12) to 30.84%/156,425 certified (3/29). 143,879 is 7 days post-election, not election night; kept only as a documented ceiling. 143,879 / 156,425 = 91.98% (a loose ceiling, NOT the election-night share). Post-epollbook AND post-ASV (both adopted 2020). FLAG for manual operator: this numerator was recovered by reading a live-edited news page's CURRENT text plus a related article, not a frozen archival snapshot with the number in place at capture time; verify the 143,879/March-12 attribution directly on fresnoland.org before treating it as settled."
}
```

### Draft VERIFY.md line
Summary table row (⚠️ per runbook 5.2 comparable=false convention):
`| 2024 ⚠️ | presidential-primary | 143,879 | 156,425 | 91.98%\* | secondary | [Fresnoland, "one week after election day"](https://fresnoland.org/2024/03/05/fresno-county-live-election-results-march-2024-primary/) |`

Detail bullet:
> - **2024 presidential-primary** — night `143,879` / final `156,425` = `91.98%` **(CEILING, not the plateau — comparable=false)**
>   - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf>
>   - numerator (ceiling, secondary/news): <https://fresnoland.org/2024/03/05/fresno-county-live-election-results-march-2024-primary/>
>   - look for: "One week after election day, local election officials have counted 143,879 ballots — chalking up a 28% voter turnout" (byline "Updated March 12, 2024"). This is 7 days post-election, NOT election night; the county's own electionsummaryreportrpt_03292024.pdf (24 days out) already equals the certified 156,425, confirming the count kept climbing after March 12. Kept only as a documented ceiling. NOTE: do not confuse with statementofvotescastrpt_0326/28/29-2024 in the sibling CMS folder — those are the March 19, 2024 CD-20 special primary, a different election.

Draft `plateau_review.json` entry:
```json
{
 "slug": "fresno-ca",
 "date": "2024-03-05",
 "verdict": "REFUTED_AS_PLATEAU",
 "basis": "cited figure is an explicit one-week-post-election canvass update, not election night",
 "evidence": "Fresnoland's live-results post's only election-week Wayback capture (2024-03-05 23:47 UTC = 15:47 PST) predates poll close and shows no count; the page was edited in place and its surviving text ('Updated March 12, 2024') states 'One week after election day, local election officials have counted 143,879 ballots'; the county's own electionsummaryreportrpt_03292024.pdf (24 days post-election) already equals the certified 156,425, confirming the count kept climbing after March 12; no county report or news account gives an election-night (March 5-6) total; retained as a documented ceiling (comparable=false, secondary)"
}
```

---

## Operator flags (read before merging)

1. **No true election-night plateau recovered for any of the six primaries.**
   Two (2018, 2024) are ceilings; four (2012, 2014, 2016, 2022) are flat
   nulls. This is a genuinely negative result worth keeping — it shows
   Fresno's primary-night reporting infrastructure did not preserve a
   crawlable snapshot in any of six tries across 12 years and two vendor
   systems (GEMS through 2018, Dominion from 2022), unlike its two GENERALS
   (2016, 2024) that got lucky with crawl timing.
2. **FLAG for manual operator** (both explicitly marked in the notes above):
   2018's ceiling rests on reading two GEMS report headers inside archived
   HTML (06/08/18 vs 06/26/18); 2024's ceiling rests on a live-edited news
   page's current text plus a companion article, not a frozen snapshot with
   the number in place at capture time. Both are asks for a human to open the
   cited URLs and eyeball-confirm per the human-verification-loop convention.
3. **CD-20 special-primary decoy** (documented in detail under 2024-03-05):
   worth a one-line addition to runbook 7.5 (county-page quirks) if a
   maintainer wants to warn future researchers — Fresno's CMS asset folders
   are shared across concurrent elections in the same month, and a
   filename/date match alone is not proof of which election a file belongs
   to; always open the PDF and read its own header.
4. `scripts/build_county_night.py` already supports the primary type
   vocabulary end-to-end (`presidential-primary` / raw `"statewide-primary"`
   normalized to `midterm-primary`); no code change needed to merge these
   rows, only the usual pipeline run (validator, denominators/numerators
   presence-check, report regen, pytest, vitest) plus a human VERIFY.md
   read-through, per RUNBOOK.md section 10.
5. Pipeline commands were NOT run against the real repo files in this pass
   (this was a read-only scouting task, scratch-only output). The operator
   should run the full RUNBOOK.md section 3 sequence after applying these
   draft rows for real.
