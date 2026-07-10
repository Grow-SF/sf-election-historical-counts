# Mendocino County, CA (slug: mendocino-ca) — CONTROL primaries evidence dossier

Companion to `dossier-mendocino-ca.md` (the Nov generals dossier, already
integrated into `data/research/election-night/mendocino-ca.json`). This
dossier covers the six statewide PRIMARY election nights that bracket the
same control-county window: 2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05,
2022-06-07, 2024-03-05 (types: presidential-primary for 2012/2016/2024,
statewide-primary for 2014/2018/2022, per runbook section 2 schema).

Working files: scratchpad `mendo-primaries/` subdirectory (curl/pdftotext
outputs, NOT repo artifacts). Denominator PDFs also cross-checked against
pre-existing scratchpad root files `sov20{12,14,16,18,22,24}primary.txt`
(left over from other counties' primary dossiers — same statewide PDFs,
re-fetched fresh here for Mendocino's own provenance trail).

Read-only research pass: nothing in this dossier has been written into the
repo. Denominators and numerators below are DRAFT rows for a human/next
pass to fold into `data/research/election-night/mendocino-ca.json`,
`VERIFY.md`, and `plateau_review.json` per RUNBOOK.md section 10.

---

## Denominators (CA SoS SoV "Voter Participation Statistics by County", all primaries)

All fetched fresh this pass, `curl -o <f>.pdf <url>`, `pdftotext -layout`,
`grep -i mendocino`. Column order: Precincts / Eligible to Register /
Registered Voters / Precinct Voters / Vote-By-Mail Voters / **Total
Voters** / %VBM / Turnout-Registered / Turnout-Eligible. Arithmetic
cross-check performed for every row: Precinct+VBM = Total Voters, and
Total/Registered = printed Turnout-Registered%.

| Primary | SoV URL | Mendocino line (as printed) | Total Voters (denominator) |
|---|---|---|---:|
| 2012-06-05 | https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf | `Mendocino 247 62,919 47,546 3,171 16,945 20,116 84.24% 42.31% 31.97%` | 20,116 |
| 2014-06-03 | https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf | `Mendocino 249 64,240 47,400 2,477 13,943 16,420 84.91% 34.64% 25.56%` | 16,420 |
| 2016-06-07 | https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf | `Mendocino 250 63,670 48,935 4,249 23,807 28,056 84.86% 57.33% 44.06%` | 28,056 |
| 2018-06-05 | https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf | `Mendocino 250 64,340 47,487 3,066 19,830 22,896 86.61% 48.22% 35.59%` | 22,896 |
| 2022-06-07 | https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf | `Mendocino 280 67,327 53,555 423 21,825 22,248 98.10% 41.54% 33.04%` | 22,248 |
| 2024-03-05 | https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf | `Mendocino 241 66,335 53,194 324 23,611 23,935 98.65% 45.00% 36.08%` | 23,935 |

Notes on URL anatomy (deviates from the general-election pattern in a couple
of spots, all confirmed live HTTP 200 this pass):
- 2012 primary: no `voter-participation` filename exists; the file is named
  `03-voter-reg-stats-by-county.pdf` but its table header is still literally
  "VOTER PARTICIPATION STATISTICS BY COUNTY" (confirmed by fetching the
  header row). No `sov/` path segment (matches the RUNBOOK 6.1 note that
  2012 drops it).
  Also confirmed a second working 2012 candidate,
  `.../2012-primary/pdf/2012-complete-sov.pdf` (full SOV, same table
  embedded p.~238) — not used since the standalone table PDF above is
  cleaner, but both are live if cross-check is wanted.
- 2014 primary: `03-voter-particpiation-stats-by-county.pdf` — misspelling
  ("particpiation") intact, matches the 2014-general convention exactly.
- 2016/2018/2022/2024: standard pattern, 2016 primary drops the `sov/`
  path segment (like 2012) while 2018/2022/2024 include it.

---

## Item 1 — 2012-06-05 (presidential-primary)

### Denominator
See table above. `certified_final = 20,116`.

### Numerator hunt — EXHAUSTIVE, concluding NULL

Following the same route family that worked for the 2012 GENERAL (which is
also NULL in the existing dataset), tried every candidate page the county
used that era:

1. **`mx2.co.mendocino.ca.us/elections/election_results.php`** (the live
   GEMS results URL, same host the Nov 2012 general used). CDX
   (`from=20120520&to=20120620`) returns exactly 2 captures:
   - `20120521110106` — pre-election; content is actually STALE leftover
     HTML from the county's *prior* election (April 10, 2012 "SPECIAL
     CONSOLIDATED ELECTION," internal timestamp `04/10/12 22:49:49`,
     "Registered Voters 5544 - Cards Cast 1924 34.70%"). Confirms the page
     had not yet been refreshed for June 2012 at crawl time.
   - `20120618211854` (13 days AFTER the primary) — header reads **"FINAL
     OFFICIAL RESULTS"**, body "Registered Voters 47720 - Cards Cast 20116
     42.15%" — `20116` = the SoV certified Total Voters EXACTLY. This is
     the already-certified state, captured too late (identical failure mode
     to the Nov 2012 general's mx2 dead end). No capture exists between
     these two, so the live election-night state was never crawled.
2. **`co.mendocino.ca.us/acr/elections.htm`** (outer nav page). CDX
   (`from=20120501&to=20120701`) shows dense crawling May 15-22 2012 (18
   captures, unrelated to the primary — leftover from April-special
   coverage), then a 27-day GAP from 2012-05-22 17:08 to 2012-06-18 23:35 —
   i.e. **zero captures spanning the entire primary period**, election night
   included. The June 18 capture (13 days post-election) links to
   `http://www.co.mendocino.ca.us/acr/pdf/June_2012_final.pdf` (a
   results PDF, filename literally containing "final") — but CDX for that
   exact PDF URL (`from=20120101&to=20150101`) returns ZERO captures; it
   was linked but never independently crawled by Wayback.
3. **`co.mendocino.ca.us/acr/electionsCurrent.htm`**: single capture
   (2012-06-18), generic nav page, no results content (same pattern as the
   Nov-2012-general dossier's finding for this page).
4. **`co.mendocino.ca.us/acr/pastElections.htm`** (the county's own
   election-history index, which for other years reliably links the
   permanent post-certification results page, e.g. `primary_6-6-2006.htm`
   for the 2006 primary): captures at 2012-06-10 (5 days post-election) and
   2013-05-29 (nearly a year later) and 2014-07-08 (over 2 years later) —
   **NONE of the three list a link for the June 2012 primary at all** (the
   2013/2014 captures list `results20121106.htm` for the Nov 2012 GENERAL,
   but no June 2012 primary entry ever appears in this index, unlike every
   other primary year 2000-2010 which IS indexed). This means there is no
   discoverable permanent-URL naming convention for this specific primary to
   even guess at from the county's own site structure.
5. **Direct guesses at the permanent-URL convention**
   `co.mendocino.ca.us/acr/election_results/results20120605.htm` (the
   pattern used successfully for 2012-11-06 and 2014-11-04): CDX
   (`from=20120601&to=20200101`) returns **zero captures ever**.
6. **News**: Anderson Valley Advertiser "Mendocino County Today: June 7,
   2012" (`https://theava.com/archives/15945`, curl -A `<UA>` fetch, HTTP
   200, found via the AVA June-2012 date-archive listing page
   `theava.com/archives/date/2012/06/06`) is a substantive morning-after
   article discussing the primary's individual races (5th Congressional
   District, 2nd District Supervisor, etc.) by PERCENTAGE only — "Norm
   Solomon only pulled 10%... Dan Roberts, came in at about 11%..." It
   contains **no aggregate ballots-cast, turnout percentage, or "cards
   cast" figure anywhere** (checked systematically: zero hits for
   "turnout", "ballots", "cards cast", "votes cast", "registered voters",
   "percent of registered", "total votes" in the full article text).
   Unusable as a numerator source under RUNBOOK 5.1/5.2 (no document states
   what was actually reported election night).

No other candidate route (registrar press release, Clarity/ENR — Mendocino
never used Clarity — or a second news outlet; MendoFever did not yet exist
in 2012) applies. **CONCLUSION: NULL per RUNBOOK 5.1.** This is a genuinely
harder null than the Nov-2012-general case: even the permanent archival
page never surfaces for this specific primary.

### Draft dataset row
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 20116,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "NULL PER RUNBOOK 5.1. WAYBACK ROUTE EXHAUSTED: mx2.co.mendocino.ca.us/elections/election_results.php (the live GEMS URL) has exactly 2 captures in the primary window -- 2012-05-21 (stale content from the PRIOR April 10, 2012 special election, internal timestamp 04/10/12 22:49:49, unrelated to June primary) and 2012-06-18 (13 days post-primary, header 'FINAL OFFICIAL RESULTS', Cards Cast 20,116 = SoV certified total exactly -- the already-certified state, captured too late, same failure mode as the Nov-2012-general dossier row). co.mendocino.ca.us/acr/elections.htm has a 27-day Wayback gap spanning the ENTIRE primary period (2012-05-22 to 2012-06-18); its June 18 capture links to /acr/pdf/June_2012_final.pdf, which was never independently crawled (zero CDX captures ever). /acr/electionsCurrent.htm is generic nav only. /acr/pastElections.htm (the county's own election-history index, which reliably links the permanent results page for every OTHER primary 2000-2010) was checked at 3 dates spanning 2012-06-10 through 2014-07-08 and never once lists a June 2012 primary entry -- no permanent-URL naming convention is even discoverable. Direct guess co.mendocino.ca.us/acr/election_results/results20120605.htm (the pattern that worked for 2012-11-06 and 2014-11-04) has zero captures ever (CDX window 20120601-20200101). NEWS SOURCE CONSIDERED AND REJECTED: Anderson Valley Advertiser 'Mendocino County Today: June 7, 2012' (theava.com/archives/15945, curl -A <UA> fetch, HTTP 200) discusses individual race results by PERCENTAGE ('Norm Solomon only pulled 10%...Dan Roberts, came in at about 11%') with zero aggregate ballots-cast/turnout/cards-cast figure anywhere in the article -- fails RUNBOOK 5.1's bar (no document states what was actually reported election night), and unlike the 2016-11-09 AVA piece used (and then still rejected) for the 2012 GENERAL row, this one does not even offer a retrospective percentage to reject. MendoFever did not yet exist in 2012. Certified final 20,116 voters (CA SoS Voter Participation Statistics by County, 2012 primary: 3,171 precinct + 16,945 VBM = 20,116; https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf, re-fetched fresh 2026-07-10, arithmetic cross-checked: 20,116/47,546 = 42.31% matches printed Turnout-Registered). Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see county-tech record)."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2012 ⚪ | presidential-primary | NULL | 20,116 | NULL | none | — |`

Detail bullet:
```
- **2012 presidential-primary** — night `NULL` / final `20,116` (none)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf>
  - look for: no numerator recovered. mx2.co.mendocino.ca.us's only two
    captures are pre-election-stale and 13-days-post-certified; the outer
    nav page has a 27-day gap over the whole primary; the county's own
    election-history index never lists a June 2012 primary link at all
    (checked 2012/2013/2014 captures); the permanent results20120605.htm
    guess has zero captures ever; the AVA morning-after article states no
    aggregate figure, only per-race percentages.
```

### plateau_review.json record
No entry (null row; matches the established convention that null/`none`
rows carry no plateau_review.json record — see the 2012/2022-general rows
in `dossier-mendocino-ca.md`).

### Verdict
**NULL — none.** Confidence in the null itself is high (multiple
independent routes exhausted, matching or exceeding the rigor of the
already-integrated 2012/2022-general null rows).

---

## Item 2 — 2014-06-03 (statewide-primary)

### Denominator
See table above. `certified_final = 16,420`.

### Numerator hunt

Wayback dead end, identical shape to the 2014 GENERAL and the 2012 primary:
- `/acr/current.htm` CDX (`co.mendocino.ca.us`, `from=20140520&to=20140701`)
  → **zero captures**.
- `co.mendocino.ca.us/current.htm` (no `/acr/` prefix) CDX
  (`from=20140501&to=20140801`) → **zero captures**.
- `/acr/cgi-bin/currentFR.pl` CDX (same window) → **zero captures** (this
  path only starts appearing in Wayback from the 2016/2018 elections on).
- Permanent-URL guesses `/acr/election_results/results20140603.htm` and
  `/acr/election_results/primary_6-3-2014.htm` (the latter matching the
  confirmed `primary_6-6-2006.htm` naming convention for the 2006 primary)
  → both **zero captures ever**.
- `/acr/pastElections.htm` (the county's own election-history index):
  checked 3 captures spanning 2014-07-08 (5 weeks post-primary) through
  2016-02-05 (20 months post-primary) — **never once lists a June 2014
  primary entry** (only `results20141104.htm`, the Nov 2014 GENERAL,
  appears once posted). Same non-indexing pattern as the 2012 primary;
  this county's site apparently never added a permanent link for either of
  these two June primaries.

### Numerator recovered via route 6.1/6.2 (official press release, verbatim
republication, arithmetic derivation)

Anderson Valley Advertiser's "Mendocino County Today: Thursday, June 5,
2014" (`https://theava.com/archives/32161`, found via the AVA June-2014
date-archive listing, `curl -A <UA>`, HTTP 200) republishes, under the
heading **"BALLOTS LEFT TO BE COUNTED JUNE 3, 2014 PRIMARY ELECTION,"**
explicitly attributed `(Assessor-County Clerk-Recorder Press Release)`:

> "Mendocino County Assessor-County Clerk-Recorder Susan M. Ranochak
> announced Wednesday that as with any other election, there are ballots
> left to be processed as part of the official canvass. **Mendocino County
> has 6,721 Vote By Mail ballots to process, and 201 Provisional ballots to
> review and process.**" (plus a district-by-district breakdown of the
> outstanding ballots, summing to the same 6,721 VBM total: 1,339 + 996 +
> 1,536 + 1,161 + 1,689 = 6,721 ✓)

This is the county's own morning-after "ballots remaining" announcement —
the complementary framing of RUNBOOK 6.2's "semi-final results" release
(states what is LEFT rather than what was counted, but is the same
underlying data point). Total outstanding-to-process as of the morning
after = 6,721 + 201 = **6,922**. Since the certified final total (16,420)
is known exactly from the SoV, and this is an EXACT official figure (not a
rounded retrospective estimate — contrast the REJECTED 2012-general AVA
citation, which had no exact document and only rounded whole-percent
language), the election-night count is recoverable by exact subtraction:
**16,420 − 6,922 = 9,498.**

### Plateau vs first tranche
This is not a "first tranche" risk: the press release explicitly frames
6,922 as everything STILL remaining "as part of the official canvass" the
morning after the election, i.e. describes the state at the close of
election-night counting before any canvass-day processing resumed. Non-
circular corroboration: the release itself states "Per State law, we have
28 days to complete the canvass" and promises the certified SoV only "at
that time" — confirming the 6,922 figure is the pre-canvass, election-night
baseline, not a canvass-day update.

### Arithmetic
16,420 − 6,922 = 9,498. 9,498 / 16,420 = 0.578563... → **57.86%**

### Draft dataset row
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": 9498,
  "certified_final": 16420,
  "election_night_pct": 57.86,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://theava.com/archives/32161",
  "confidence": "secondary",
  "note": "WAYBACK DEAD END (same shape as the 2014 general and 2012 primary): /acr/current.htm and root current.htm CDX for the primary window (May-July 2014) both zero captures; /acr/cgi-bin/currentFR.pl zero captures (path not archived until 2016+); permanent-URL guesses results20140603.htm and primary_6-3-2014.htm (matching the confirmed primary_6-6-2006.htm naming convention) both zero captures ever; the county's own /acr/pastElections.htm index, checked at 3 dates spanning 2014-07-08 through 2016-02-05, never once lists a June 2014 primary entry (same non-indexing pattern independently observed for the 2012 primary). RECOVERED VIA OFFICIAL PRESS RELEASE, republished verbatim by news (route 6.1/6.2): Anderson Valley Advertiser 'Mendocino County Today: Thursday, June 5, 2014' (theava.com/archives/32161, curl -A <UA> fetch, HTTP 200), under the heading 'BALLOTS LEFT TO BE COUNTED JUNE 3, 2014 PRIMARY ELECTION,' explicitly tagged '(Assessor-County Clerk-Recorder Press Release)': 'Mendocino County Assessor-County Clerk-Recorder Susan M. Ranochak announced Wednesday that as with any other election, there are ballots left to be processed as part of the official canvass. Mendocino County has 6,721 Vote By Mail ballots to process, and 201 Provisional ballots to review and process,' with a district breakdown (1,339+996+1,536+1,161+1,689=6,721, verified) confirming the VBM figure. Total outstanding = 6,721+201 = 6,922 (exact official figures, not a rounded estimate -- contrast the REJECTED 2012-general AVA citation which had no exact document). Election-night count derived by exact subtraction from the certified final: 16,420 - 6,922 = 9,498. Plateau reasoning: the release explicitly frames 6,922 as everything remaining 'as part of the official canvass' the morning after, i.e. the pre-canvass baseline the county itself measured at the close of election night, not a canvass-day update ('Per State law, we have 28 days to complete the canvass ... The Statement of Vote ... will be available at that time'). Kept SECONDARY (news republication of an official release, not the release itself) for consistency with the sibling 2014-11-04 general row's identical treatment of a verbatim-quoted AVA press item -- same open question the maintainer left unresolved for the Nevada/yubanet case, not fixed silently here either. Pct = 9,498/16,420 = 57.86%. Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see county-tech record). FLAG for manual operator: this row uses a subtraction-derived numerator (certified minus officially-stated outstanding) rather than a directly-quoted counted figure; a human should confirm this construction is acceptable under RUNBOOK 5.1/5.2 before promotion to the live dataset, since it is a new pattern not used elsewhere in the Mendocino dossier."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2014 | statewide-primary | 9,498 | 16,420 | 57.9% | secondary | [link](https://theava.com/archives/32161) |`

Detail bullet:
```
- **2014 statewide-primary** — night `9,498` / final `16,420` = `57.9%` (secondary)
  - numerator: <https://theava.com/archives/32161> ("BALLOTS LEFT TO BE
    COUNTED JUNE 3, 2014 PRIMARY ELECTION" -- Assessor-County Clerk-Recorder
    press release republished verbatim: 6,721 VBM + 201 Provisional = 6,922
    outstanding; 16,420 certified - 6,922 outstanding = 9,498 election-night)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf>
  - look for: "Mendocino County has 6,721 Vote By Mail ballots to process,
    and 201 Provisional ballots to review and process."
```

### plateau_review.json record
```json
{
  "slug": "mendocino-ca",
  "date": "2014-06-03",
  "verdict": "PLAUSIBLE",
  "basis": "Self-describing official press release (morning-after 'ballots left to process' announcement, explicitly attributed to the Assessor-County Clerk-Recorder) gives an exact outstanding figure; election-night count derived by exact subtraction from the SoV certified final. No independent second leg (no Wayback bracket, no later-capture-same-count) obtainable since the county's own results pages were never crawled during this window -- hence PLAUSIBLE not CONFIRMED per RUNBOOK section 8.",
  "evidence": "theava.com/archives/32161: 'Mendocino County has 6,721 Vote By Mail ballots to process, and 201 Provisional ballots to review and process' (Assessor-County Clerk-Recorder Press Release, June 4 2014); 16,420 - 6,922 = 9,498"
}
```

### Verdict
**PLAUSIBLE, secondary, FLAGGED for manual operator review** (subtraction
construction is new to this dossier; a human should confirm it is
acceptable before promotion).

---

## Item 3 — 2016-06-07 (presidential-primary)

### Denominator
See table above. `certified_final = 28,056`.

### Numerator hunt — CONFIRMED primary, same route family as 2016-11-08

CDX `/acr/current.htm` (`co.mendocino.ca.us`, `from=20160525&to=20160701`) →
9 captures: pre-election stubs May 26 - June 2 (6.7-6.7KB, page furniture
only, no results table — confirmed by fetching the June 2 20:08 capture,
which has no "ELECTION SUMMARY" content at all), then **June 11 20:22 UTC**
(8.7KB) and **June 24 07:03** (8.9KB).

- Fetched `https://web.archive.org/web/20160611202253id_/http://www.co.mendocino.ca.us:80/acr/current.htm`
  → header: **"Election Summary Report County of Mendocino PRESIDENTIAL
  PRIMARY ELECTION JUNE 7, 2016 — Final Election Night Report — 06/08/16
  02:24:41 — Registered Voters 46795 - Cards Cast 11320 24.19% — Num.
  Report Precinct 250 - Num. Reporting 250 100.00%"**. Internal timestamp
  2:24 AM the morning after (within the up-to-4am election-night window).
- Fetched the June 24 capture (17 days later, same URL) → **byte-identical
  results header**: same "06/08/16 02:24:41" timestamp, same "Cards Cast
  11320". Proves the count held for 17+ days through the canvass pause —
  RUNBOOK 8's "later capture of the same URL still showing the same count"
  leg, satisfied non-circularly.
- No capture exists of the true 8pm first-tranche state (only pre-election
  stubs through June 2, then straight to June 11), so there is no first-
  tranche confusion risk.

Same pattern exactly as the already-integrated 2016-11-08 general row: the
county's own self-labeled "Final Election Night Report," late-night
internal timestamp, and multi-day hold-evidence. **CONFIRMED** per RUNBOOK
section 8.

### Arithmetic
11,320 / 28,056 = 0.403476... → **40.35%**

### Draft dataset row
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 11320,
  "certified_final": 28056,
  "election_night_pct": 40.35,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20160611202253/http://www.co.mendocino.ca.us:80/acr/current.htm",
  "confidence": "primary",
  "note": "PLATEAU = county's own 'Election Summary Report ... PRESIDENTIAL PRIMARY ELECTION JUNE 7, 2016 ... Final Election Night Report' (curl id_ raw fetch of the archived /acr/current.htm page, plain HTML, no gzip). Internal report timestamp '06/08/16 02:24:41' (2:24 AM the morning after Election Day, within the runbook's up-to-4am election-night window). Body: Registered Voters 46,795, Cards Cast 11,320 (24.19%), Num. Reporting Precinct 250/250 (100.00%). Non-circular corroboration: a LATER capture of the SAME URL 17 days later (2016-06-24, snapshot 20160624070319) is byte-identical -- same '06/08/16 02:24:41' timestamp, same 11,320 count -- proving the number held through the canvass pause (RUNBOOK 8: self-description + later-capture-same-count = CONFIRMED). The immediately-prior capture (2016-06-02 20:08 UTC, pre-poll-close) has no results table at all (page furniture only), confirming the FINAL-report text is not reused boilerplate. No capture of the true 8pm first tranche survives (CDX jumps from June 2 pre-election stubs straight to June 11), so there is no risk of numerator confusion with the first tranche. Same route family and evidence shape as the already-integrated 2016-11-08 general row (same /acr/current.htm URL, same 'Final Election Night Report' label convention). Certified final 28,056 voters (CA SoS Voter Participation Statistics by County, 2016 primary: 4,249 precinct + 23,807 VBM = 28,056; https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf, re-fetched fresh 2026-07-10, arithmetic cross-checked: 28,056/48,935 = 57.33% matches printed Turnout-Registered). Pct = 11,320/28,056 = 40.35%. Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see county-tech record)."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2016 | presidential-primary | 11,320 | 28,056 | 40.3% | primary | [link](https://web.archive.org/web/20160611202253/http://www.co.mendocino.ca.us:80/acr/current.htm) |`

Detail bullet:
```
- **2016 presidential-primary** — night `11,320` / final `28,056` = `40.3%` (primary)
  - numerator: <https://web.archive.org/web/20160611202253/http://www.co.mendocino.ca.us:80/acr/current.htm>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf>
  - look for: "PRESIDENTIAL PRIMARY ELECTION JUNE 7, 2016 ... Final
    Election Night Report ... 06/08/16 02:24:41 ... Cards Cast 11320 24.19%"
```

### plateau_review.json record
```json
{
  "slug": "mendocino-ca",
  "date": "2016-06-07",
  "verdict": "CONFIRMED",
  "basis": "Self-labeled 'Final Election Night Report' with late-night internal timestamp (06/08/16 02:24:41), plus a later capture of the same URL 17 days later showing the identical byte-for-byte count -- both legs of RUNBOOK section 8's CONFIRMED test satisfied non-circularly.",
  "evidence": "web.archive.org/web/20160611202253/.../acr/current.htm: 'Final Election Night Report 06/08/16 02:24:41 ... Cards Cast 11320 24.19%'; web.archive.org/web/20160624070319/.../acr/current.htm: byte-identical, same count 17 days later"
}
```

### Verdict
**CONFIRMED, primary.** Strongest-evidenced row in this dossier so far.

---

## Item 4 — 2018-06-05 (statewide-primary)

### Denominator
See table above. `certified_final = 22,896`.

### Numerator hunt

Wayback dead end on every county-side route:
- `/acr/cgi-bin/currentFR.pl` (the confirmed 2018-GENERAL live-report path,
  both `http://` and `https://` variants) — CDX widened to the FULL 2018
  calendar year → only 3 captures, all Nov 7 / Dec 2 / Dec 22 (the Nov
  general's window); **zero for June 2018**.
- `/acr/current.htm` — one capture June 1 2018, but it is a bare 301
  redirect to the new `mendocinocounty.org` CMS root (confirmed via
  `curl -sI`, `location: https://www.mendocinocounty.org/`); the old page
  had already stopped serving results content by primary night.
- The new CMS page
  `mendocinocounty.org/government/assessor-county-clerk-recorder-elections/current-election-results`
  (the wrapper that embeds the `currentFR.pl` iframe, confirmed working for
  the Nov 2018 general) — CDX shows its EARLIEST capture is 2018-11-07;
  **zero captures for June 2018**, i.e. this page did not exist yet (or was
  not crawled) at primary time.
- Permanent-URL guess `/acr/election_results/results20180605.htm` → zero
  captures.
- Domain-wide CDX probes on `mendocinocounty.org` for an "election" path in
  the June 2018 window 504'd / returned empty on broad queries (per RUNBOOK
  7.1's warning about broad `matchType=domain` queries); no narrower
  specific path found the results.

### Numerator recovered via route 6.6 (local news)

Anderson Valley Advertiser's "Mendocino County Today: Wednesday, June 6,
2018" (`https://theava.com/archives/83237`, found via the AVA June-2018
date-archive listing, `curl -A <UA>`, HTTP 200; live page still serves the
identical text as of this fetch). The post has two timestamped checkpoints
in one rolling entry:

> "WITH OVER A QUARTER of the votes counted, early returns (**late Tuesday
> night**) in closely watched local races have Michelle Hutchins leading
> Bryan Barrett..." [first-tranche checkpoint — NOT used]
>
> "**UPDATE (Wednesday 8:40am)** With **all precincts reporting** and just
> over 40% of the ballots cast (**19,049**) the local trends are holding:
> County Superintendent of Schools Hutchins 4262 (53%) Barrett 3694
> (46%)..." [second checkpoint — the one used]

Arithmetic check on the "just over 40%" framing: 19,049 / 47,487 (SoV
Registered Voters, 2018 primary) = **40.11%** — matches "just over 40%"
exactly, confirming 19,049 is being reported the same way the county's own
GEMS pages phrase it ("Registered Voters N — Cards Cast M X%"), i.e. this
is very likely a direct paraphrase/observation of the county's own Election
Night Final Report (the same report family confirmed for 2016/2018-general
via `currentFR.pl`), just relayed by the reporter rather than captured
directly from the page (which Wayback never crawled).

### Plateau vs first tranche
The article explicitly distinguishes two checkpoints: "late Tuesday night"
(a partial count, "over a quarter of the votes counted" — the FIRST
tranche, correctly NOT used) vs. "UPDATE (Wednesday 8:40am) With all
precincts reporting" (250/250 precincts — a state a small rural county
normally reaches by the end of its own election-night GEMS run, matching
the "100.00%" reporting-precinct marker seen directly on the county's own
pages in every other confirmed Mendocino year). No non-circular second leg
is obtainable (Wayback has zero captures of the underlying county page for
this window), so this stays **PLAUSIBLE**, not CONFIRMED.

**CALIBRATION FLAG:** 19,049/22,896 = 83.20% is unusually HIGH relative to
the rest of this dossier (2014 primary 57.86%, 2016 primary 40.35%, 2018
GENERAL 46.57%) and RUNBOOK section 1 explicitly warns that a number "well
ABOVE the county's own adjacent elections" should raise suspicion of a
canvass-contaminated next-day number. Weighed against that: the source text
itself distinguishes the true first tranche ("late Tuesday night," expressly
NOT what is used) from the "all precincts reporting" checkpoint used here,
and 100%-precincts-reporting is a marker that arrives ON election night for
this county in every other confirmed row (2016/2018 general). The high
share is plausible on its own terms too: 2018 primary had far more VBM
voters already returned by election day (19,830 of 22,896 certified, per
the SoV) than late/canvass-only ballots, unlike November generals which see
heavier late/provisional volume. Left as a flag for human review, not
"fixed," per the same policy the general dossier applied to the 2016
row's unusually LOW figure.

### Arithmetic
19,049 / 22,896 = 0.831982... → **83.20%**

### Draft dataset row
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 19049,
  "certified_final": 22896,
  "election_night_pct": 83.20,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://theava.com/archives/83237",
  "confidence": "secondary",
  "note": "WAYBACK DEAD END on every county-side route: /acr/cgi-bin/currentFR.pl (the confirmed 2018-GENERAL live-report path, both http/https) has zero June-2018 captures (only Nov7/Dec2/Dec22, the general's window, checked with the CDX window widened to the full 2018 calendar year); /acr/current.htm's one June-2018 capture is a bare 301 to the new mendocinocounty.org CMS root, no results content; the new CMS wrapper page mendocinocounty.org/government/assessor-county-clerk-recorder-elections/current-election-results (confirmed working for the Nov 2018 general) has its earliest capture on 2018-11-07, zero for June; permanent-URL guess results20180605.htm has zero captures. RECOVERED VIA NEWS (route 6.6): Anderson Valley Advertiser 'Mendocino County Today: Wednesday, June 6, 2018' (theava.com/archives/83237, curl -A <UA> fetch, HTTP 200, live page re-verified 2026-07-10 to still show the same text) distinguishes two checkpoints in one rolling post: 'late Tuesday night' ('over a quarter of the votes counted' -- explicitly the FIRST tranche, NOT used) vs. 'UPDATE (Wednesday 8:40am) With all precincts reporting and just over 40% of the ballots cast (19,049) the local trends are holding.' Arithmetic check: 19,049/47,487 (SoV Registered Voters) = 40.11%, matching the article's 'just over 40%' framing exactly and matching the county's own GEMS report phrasing convention ('Registered Voters N - Cards Cast M X%') seen directly on the confirmed 2016/2018-general rows. 'All precincts reporting' (250/250) is the same completion marker that arrives ON election night in every other confirmed Mendocino row. No non-circular second leg obtainable (no Wayback capture of the underlying county page survives for this window), so PLAUSIBLE not CONFIRMED. CALIBRATION FLAG: 19,049/22,896 = 83.20% is well ABOVE this dossier's other primary years (2014: 57.86%, 2016: 40.35%) and the 2018 GENERAL itself (46.57%); RUNBOOK section 1 flags unusually-high numbers as a canvass-contamination risk, but the source explicitly distinguishes the true first tranche (correctly excluded) from the all-precincts-reporting checkpoint used, and the high share is structurally plausible (2018 primary VBM was mostly already returned by election day: 19,830 of 22,896 certified). Flagged for human review, not altered, per the same policy applied to the 2016-general row's unusually LOW figure. Certified final 22,896 voters (CA SoS Voter Participation Statistics by County, 2018 primary: 3,066 precinct + 19,830 VBM = 22,896; https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf, re-fetched fresh 2026-07-10, arithmetic cross-checked: 22,896/47,487 = 48.22% matches printed Turnout-Registered). Pct = 19,049/22,896 = 83.20%. Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see county-tech record). FLAG for manual operator: unusually high share for a primary; a human read of the AVA source (and any surviving local coverage) is warranted before promotion."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2018 ⚠️ | statewide-primary | 19,049 | 22,896 | 83.2% | secondary | [link](https://theava.com/archives/83237) |`
(⚠️ flag per RUNBOOK 5.2 convention for a calibration-flagged value, even
though this is not a `comparable: false` ceiling case — recommend the human
reviewer decide whether the flag belongs in VERIFY.md's ⚠️ column or just
in the note; included here for visibility.)

Detail bullet:
```
- **2018 statewide-primary** — night `19,049` / final `22,896` = `83.2%` (secondary)
  - numerator: <https://theava.com/archives/83237> ("UPDATE (Wednesday
    8:40am) With all precincts reporting and just over 40% of the ballots
    cast (19,049) the local trends are holding")
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "all precincts reporting ... 19,049"; CALIBRATION FLAG --
    unusually high vs. this dossier's other primaries, human review wanted.
```

### plateau_review.json record
```json
{
  "slug": "mendocino-ca",
  "date": "2018-06-05",
  "verdict": "PLAUSIBLE",
  "basis": "News source explicitly distinguishes the first tranche (excluded) from an 'all precincts reporting' checkpoint matching this county's own completion marker on every other confirmed row; arithmetic against SoV Registered Voters matches the article's stated percentage exactly. No independent second leg obtainable (no surviving Wayback capture of the underlying county page). Calibration flag: share is unusually high vs. sibling rows -- PLAUSIBLE not CONFIRMED, human review recommended before promotion.",
  "evidence": "theava.com/archives/83237: 'UPDATE (Wednesday 8:40am) With all precincts reporting and just over 40% of the ballots cast (19,049) the local trends are holding'; 19,049/47,487 = 40.11% matches stated percentage"
}
```

### Verdict
**PLAUSIBLE, secondary, FLAGGED for manual operator review** (both for the
subtraction-free but still news-sourced numerator, and specifically for the
unusually high calibration figure).

---

## Item 5 — 2022-06-07 (statewide-primary)

### Denominator
See table above. `certified_final = 22,248` (423 precinct + 21,825 VBM).
Note the structural shift vs earlier years: VBM is now 98.1% of all ballots
(precinct-day in-person is a tiny 1.9% remainder) — by 2022 California's
universal-VBM law (mailing a ballot to every active registered voter) was
in full effect, unlike 2012-2018 when VBM required an opt-in request.

### Numerator hunt — county-side dead end (same shape as the 2022 GENERAL)
- `/acr/cgi-bin/currentFR.pl` CDX widened to the full 2022 calendar year →
  captures at Feb 18 (pre-election placeholder) and Apr 29 (revisit, same
  placeholder), then a gap straight to **Jul 5, 2022** (28 days
  post-election). Fetched it: header **"FINAL OFFICIAL RESULTS - WEBSITE —
  Election Day — Run Time 9:41 AM Run Date 06/28/2022 — ... Registered
  Voters 22248 of 52602 = 42.29%"** — 22,248 = the SoV certified total
  EXACTLY, the already-certified state, captured too late (same dead-end
  pattern as every other Mendocino year on this path).
- The CMS wrapper page (`mendocinocounty.org/government/.../current-
  election-results`) has a single June 2022 capture, June 29 (22 days
  post-election) — only the embedded iframe tag, no renderable numbers
  (curl cannot execute the iframe's JS/frame load), and by then already
  past the primary window anyway.

### Numerator recovered via route 6.6 (local news, two independent outlets
corroborating each other)

**MendoFever** "[UPDATE: Unofficial Winners] Election Night Mendocino: Stay
Tuned With Us This Evening as the Votes Come In"
(`https://mendofever.com/2022/06/07/election-night-mendocino-stay-tuned-with-us-this-evening-as-the-votes-come-in/`
— live site currently serves a "Coming Soon" placeholder, site mid-rebuild;
recovered via Wayback CDX + `id_` raw fetch, gzip'd, gunzipped). The article
is a rolling live-blog with three checkpoints:
- 8:06 p.m.: "the first round of numbers coming in ... with 3,461 of 52,602
  (6.58%) registered voters' ballots being counted" — **first tranche, NOT
  used.**
- "UPDATE 10:47 p.m.: The Mendocino County Election website has released
  its 2nd report for the night, published at 10:15 p.m., and 3,597 of
  52,602 registered voters making 6.84% of eligible ballots counted" —
  still an intermediate tranche, NOT used.
- "**UPDATE 6:00 a.m.**: And there you have it folks, **as of 12:32 a.m.**,
  we have our unofficial elected winners of the significant races in our
  local elections... **these numbers at this point with all precincts
  reporting** generally indicate the winners." — the completion marker
  (280/280 precincts, matching this county's own "100.00%" reporting
  convention seen directly on every other confirmed Mendocino year) is
  reached here, but this final update states only per-race winner tallies,
  not an aggregate ballots-cast figure. A linked image/PDF captioned
  "Current-Election-Results-_-Mendocino-County-CA" (evidently a screenshot
  of the county's live results page at 12:32 a.m., which would have shown
  the aggregate "Registered Voters N of 52,602 = X%" line directly) is
  unrecoverable: live URL 500s (site rebuild) and it has zero Wayback
  captures ever.

**The Mendocino Voice** "Mendocino County election officials still
processing ballots in primary election" (`https://mendovoice.com/2022/06/mendocino-county-election-officials-still-processing-ballots-in-primary-election/`,
dateline UKIAH 6/14/22, `curl -A <UA>` live fetch, HTTP 200) states directly:

> "**Unofficial election results showed 3,864 registered voters' ballots
> were counted as of early morning Wednesday, June 8, the day following the
> election.**" ... "which reported a nearly 7.5% initial turnout on
> Wednesday, June 8" ... "There are 52,602 registered voters in the
> county."

Arithmetic check: 3,864/52,602 = 7.35%, matching the article's own "nearly
7.5%" framing. This is a directly-stated official figure (attributed
throughout the piece to county clerk Katrina Bartolomie), not a derived or
rounded retrospective guess — contrast the REJECTED 2012-general AVA
citation, which had no exact document behind it. Non-circular corroboration:
MendoFever's own INDEPENDENTLY-recovered live-blog sequence (3,461 at
8:06pm -> 3,597 at 10:15pm) is monotonically consistent with 3,864 being the
next data point reached by "early morning Wednesday," and MendoFever's own
"12:32 a.m., all precincts reporting" completion marker independently
brackets the same window this MendoVoice figure describes.

### Plateau vs first tranche
"As of early morning Wednesday, June 8" (the morning after) is later than
both of MendoFever's tracked election-night tranches (8:06pm, 10:15pm) and
aligns with MendoFever's own "12:32 a.m., all precincts reporting"
completion state — i.e. this is the LAST report before the extended VBM
canvass window opens (the same article explains ballots postmarked by
Election Day and received through June 14 still had to be processed,
and processing continued for a full week afterward), not a next-day canvass
update itself.

**CALIBRATION NOTE (structural, not a red flag):** 3,864/22,248 = 17.37% is
far below every other row in this dossier. This is explained by a genuine
structural shift, not a sourcing error: by 2022 California mailed ballots
to every active registered voter (no opt-in required) and extended the
acceptance window to ballots postmarked by Election Day and received up to
7 days later (per this same MendoVoice article: "must accept and process
all mail-in ballots that are postmarked by Election Day and received by
Tuesday, June 14"). With VBM now 98.1% of all certified ballots (21,825 of
22,248) and a week-long trailing return window, most VBM ballots physically
had not yet arrived by election night, structurally depressing the
election-night share independent of any counting-technology confound (this
is exactly the "2018-2020 Voter's Choice Act mail shift" confound RUNBOOK
section 1 instructs recording, never "fixing").

### Arithmetic
3,864 / 22,248 = 0.173706... → **17.37%**

### Draft dataset row
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 3864,
  "certified_final": 22248,
  "election_night_pct": 17.37,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://mendovoice.com/2022/06/mendocino-county-election-officials-still-processing-ballots-in-primary-election/",
  "confidence": "secondary",
  "note": "WAYBACK DEAD END (same shape as the 2022 general): /acr/cgi-bin/currentFR.pl CDX widened to the full 2022 calendar year has only a pre-election placeholder (Feb18/Apr29 revisit) then jumps straight to Jul 5 2022 (28 days post-election), already reading 'FINAL OFFICIAL RESULTS - WEBSITE ... Run Date 06/28/2022 ... Registered Voters 22248 of 52602 = 42.29%' -- the certified state (22,248 = SoV total exactly), captured too late. The CMS wrapper page has one June capture (June 29, past the primary window) with only the unrendered iframe tag. RECOVERED VIA TWO INDEPENDENT NEWS SOURCES corroborating each other: (1) MendoFever's live-blog 'Election Night Mendocino: Stay Tuned...' (mendofever.com/2022/06/07/election-night-mendocino-stay-tuned-with-us-this-evening-as-the-votes-come-in/, live site 'Coming Soon'-placeholder mid-rebuild, recovered via Wayback CDX id_ raw fetch, gzip'd/gunzipped) shows three checkpoints: 8:06pm 3,461/52,602=6.58% (first tranche, NOT used), 'UPDATE 10:47pm: ... 2nd report ... published at 10:15pm ... 3,597 of 52,602 ... 6.84%' (still intermediate, NOT used), and 'UPDATE 6:00am: ... as of 12:32am, we have our unofficial elected winners ... with all precincts reporting' (the completion marker, 280/280, matching this county's own convention -- but this final update states only per-race winners, no aggregate figure; a linked screenshot/PDF of the county results page at 12:32am is unrecoverable, live 500s and zero Wayback captures). (2) The Mendocino Voice 'Mendocino County election officials still processing ballots in primary election' (mendovoice.com/2022/06/mendocino-county-election-officials-still-processing-ballots-in-primary-election/, dateline UKIAH 6/14/22, curl -A <UA> live fetch HTTP 200) states directly, attributed to county clerk Katrina Bartolomie: 'Unofficial election results showed 3,864 registered voters' ballots were counted as of early morning Wednesday, June 8, the day following the election' ... 'a nearly 7.5% initial turnout' (3,864/52,602=7.35%, matches). Non-circular corroboration: MendoFever's independently-recovered monotonic sequence (3,461 -> 3,597) is consistent with 3,864 as the next data point by 'early morning Wednesday,' and MendoFever's own '12:32am, all precincts reporting' completion marker independently brackets the same window. CALIBRATION NOTE (structural, not a sourcing flag): 3,864/22,248=17.37% is far below this dossier's other rows because by 2022 CA mailed ballots to every active registered voter (VBM now 98.1% of certified total: 21,825 of 22,248) with a 7-day-postmark trailing return window (ballots 'postmarked by Election Day and received by Tuesday, June 14' per this same article) -- most VBM ballots had not yet physically arrived by election night, a structural VCA/universal-mail confound (RUNBOOK section 1), not a sourcing error. Certified final 22,248 voters (CA SoS Voter Participation Statistics by County, 2022 primary: 423 precinct + 21,825 VBM = 22,248; https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf, re-fetched fresh 2026-07-10, arithmetic cross-checked: 22,248/53,555 = 41.54% matches printed Turnout-Registered). Pct = 3,864/22,248 = 17.37%. Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see county-tech record). FLAG for manual operator: numerator is a retrospective news citation of an official figure (not a directly-captured document); a human read of the two source articles is recommended before promotion."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2022 | statewide-primary | 3,864 | 22,248 | 17.4% | secondary | [link](https://mendovoice.com/2022/06/mendocino-county-election-officials-still-processing-ballots-in-primary-election/) |`

Detail bullet:
```
- **2022 statewide-primary** — night `3,864` / final `22,248` = `17.4%` (secondary)
  - numerator: <https://mendovoice.com/2022/06/mendocino-county-election-officials-still-processing-ballots-in-primary-election/>
    ("Unofficial election results showed 3,864 registered voters' ballots
    were counted as of early morning Wednesday, June 8"), corroborated by
    <https://mendofever.com/2022/06/07/election-night-mendocino-stay-tuned-with-us-this-evening-as-the-votes-come-in/>
    (8:06pm 3,461 -> 10:15pm 3,597 -> 12:32am "all precincts reporting")
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "3,864 registered voters' ballots were counted as of early
    morning Wednesday, June 8"; STRUCTURAL NOTE -- universal VBM + 7-day
    postmark window depresses this share vs. pre-2022 rows, not a sourcing
    defect.
```

### plateau_review.json record
```json
{
  "slug": "mendocino-ca",
  "date": "2022-06-07",
  "verdict": "PLAUSIBLE",
  "basis": "Directly-stated official figure (attributed to the county clerk) describing the morning-after state, independently corroborated by a second outlet's real-time live-blog showing a consistent monotonic sequence and the same 'all precincts reporting' completion marker used across every other confirmed Mendocino row. No document-level capture obtainable (both the county's own page and the linked screenshot/PDF are unrecoverable), so PLAUSIBLE not CONFIRMED.",
  "evidence": "mendovoice.com/.../still-processing-ballots-in-primary-election/: '3,864 registered voters' ballots were counted as of early morning Wednesday, June 8'; mendofever.com/.../election-night-mendocino-stay-tuned/: 8:06pm 3,461 -> 10:15pm 3,597 -> 12:32am all precincts reporting"
}
```

### Verdict
**PLAUSIBLE, secondary, FLAGGED for manual operator review.**

---

## Status summary

All 6 primaries researched to exhaustion on the county-side (Wayback)
routes; 5 of 6 recovered a numerator via local news (secondary confidence,
4 PLAUSIBLE + 1 CONFIRMED), 1 of 6 (2012) is a documented NULL.

| Primary | Type | Ballots | Certified final | Pct | Confidence | Verdict |
|---|---|---:|---:|---:|---|---|
| 2012-06-05 | presidential-primary | NULL | 20,116 | NULL | none | (no record) |
| 2014-06-03 | statewide-primary | 9,498 | 16,420 | 57.86% | secondary | PLAUSIBLE |
| 2016-06-07 | presidential-primary | 11,320 | 28,056 | 40.35% | primary | CONFIRMED |
| 2018-06-05 | statewide-primary | 19,049 | 22,896 | 83.20% | secondary | PLAUSIBLE |
| 2022-06-07 | statewide-primary | 3,864 | 22,248 | 17.37% | secondary | PLAUSIBLE |
| 2024-03-05 | presidential-primary | 7,418 | 23,935 | 30.99% | secondary | PLAUSIBLE |

Notable pattern, consistent with the generals dossier: Mendocino's own
election-night infrastructure is almost never crawled by Wayback DURING
the actual election-night window across every single primary studied
(2012/2014's `current.htm`/`election_results.php`, 2018/2022/2024's
`cgi-bin/currentFR.pl`) — the crawler reliably catches only pre-election
placeholders and post-canvass "FINAL OFFICIAL RESULTS"/"ELECTION RESULTS
UPDATE" states weeks later, whose ballot counts already equal or approach
the certified final. **2016 is the sole exception** (and the sole `primary`
confidence row): its `/acr/current.htm` page happened to be crawled 4 days
post-primary while still showing the frozen "Final Election Night Report,"
and crawled AGAIN 17 days later still unchanged — the same evidentiary
shape that made the 2016 GENERAL row the strongest in the companion
dossier. Every other primary year required a news-sourced numerator
(Anderson Valley Advertiser for 2014/2018; MendoFever + The Mendocino
Voice, cross-corroborating each other, for 2022/2024), and one (2012) has
no usable news numerator at all despite an unusually thorough search (the
county's own `pastElections.htm` index never lists either the 2012 or
2014 June primary, a gap not seen anywhere in the generals dossier).

Two rows carry unresolved analytical flags for the human reviewer beyond
the routine "news-sourced, FLAG for manual operator" status shared by
2014/2018/2022/2024:
- **2018 (83.20%)** is a genuine outlier vs. every other row in both
  dossiers and needs a human read of the source before promotion.
- **2022 (17.37%)** and, to a lesser extent, **2024 (30.99%)** are
  structurally low for a coherent, documented reason (universal VBM +
  7-day postmark trailing window starting 2022) rather than a sourcing
  defect — this is itself a useful finding for the cross-county comparison
  (a VCA/universal-mail confound distinct from any e-pollbook/ASV effect,
  and Mendocino is NOT a VCA county per the tech record, so this confound
  applies dataset-wide to every CA county's 2022+ primaries, not just
  Mendocino).
- **2014 (57.86%)** uses a new construction (subtraction from an official
  "ballots remaining" release) not used elsewhere in either Mendocino
  dossier; flagged so a human can confirm it fits RUNBOOK 5.1/5.2 before
  promotion.

Nothing required a real-browser (Claude-in-Chrome) fetch beyond what curl +
pdftotext + gzip handling + Wayback CDX reached this pass; the two
county-side infrastructure pages that returned Cloudflare/bot-wall-style
failures elsewhere in this project were not encountered here (Mendocino's
own old-domain CGI pages and Wayback both fetch cleanly via curl). (presidential-primary)

### Denominator
See table above. `certified_final = 23,935` (324 precinct + 23,611 VBM).

### Numerator hunt — county-side dead end (same shape as 2022 and the 2024 GENERAL)
- `/acr/cgi-bin/currentFR.pl` CDX (Feb-Apr 2024) → March 3 09:35 UTC (2
  days pre-election, 4.4KB placeholder), then straight to **March 22**
  (10.3KB) and March 29 (7.9KB), both weeks post-election. Fetched the
  March 22 capture: header **"ELECTION RESULTS UPDATE WEB 3 21 2024
  Official — Run Time 3:31 PM Run Date 03/21/2024 ... Registered Voters
  22615 of 52602 = 42.99% — Precincts Reporting 241 of 241 = 100.00%"** —
  explicitly labeled a canvass "Update" (not an election-night report),
  dated 16 days post-election, ballot count already at 22,615 (not yet the
  final 23,935, but far past any election-night state). Unusable.
- The new CMS wrapper page
  (`mendocinocounty.gov/government/assessor-county-clerk-recorder-elections/current-election-results`)
  DOES have a capture at 2024-03-06 09:21 UTC (**01:21 AM PST**, i.e. within
  the up-to-4am election-night window!) — fetched it, but it contains only
  the unrendered `<iframe src="//www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl">`
  tag; Wayback's crawler did not separately capture the iframe's own
  cross-origin target at that timestamp (the iframe URL's own CDX has no
  capture between March 3 and March 22), so the number itself is
  unrecoverable even though the WRAPPER page was crawled at the right
  moment. Genuinely a near-miss.

### Numerator recovered via route 6.6 (local news, two outlets, monotonic
corroboration)

**MendoFever** "It's Election Night in Mendocino County—Live Updates and
Preliminary Results"
(`https://mendofever.com/2024/03/05/its-election-night-in-mendocino-county-election-live-updates-and-preliminary-results/`,
recovered via Wayback CDX + `id_` raw fetch, gzip'd/gunzipped, snapshot
2024-03-13) has exactly ONE checkpoint and is never updated further ("Stay
tuned throughout the night for updates... We will post all updates below"
is followed by nothing else in the page): **"As of 8:09 p.m., 7,094
registered voters' ballots have been tallied and 62.66% of the county's
precincts have reported their results."** This is explicitly a partial,
mid-evening count (62.66% precincts, not 100%) — the classic FIRST TRANCHE,
correctly NOT used on its own.

**The Mendocino Voice** "Mendocino County and California primary election
results updated" (`https://mendovoice.com/2024/03/did-you-vote-yet-mendocino-county-and-california-primary-election-ends-today-with-results-beginning-tonight/`,
`curl -A <UA>` live fetch, HTTP 200) carries a later, more complete
checkpoint appended to the same rolling article:

> "**UPDATE 3/6/24 9:30 a.m.**: Mendocino County's election results **were
> updated after midnight on election night**, and the current results
> include **a total of 7,418 ballots**, just over 14% of the county's
> 52,602 registered voters. This update includes a few hundred votes from
> ballots cast in person yesterday, and has not changed which candidates
> are currently ahead in the county's tally."

Arithmetic check: 7,418 / 52,602 = 14.10%, matching "just over 14%" exactly.
Non-circular corroboration: this is a modest, consistent increase over
MendoFever's independently-recovered 8:09pm checkpoint (7,094 -> 7,418, +324
ballots — "a few hundred votes from ballots cast in person" matches exactly
what the county would still be tallying between 8:09pm and after midnight),
and the article explicitly frames the 7,418 figure as the state reached
**"after midnight on election night"** — i.e. the plateau, not a
subsequent canvass-day figure (the same article separately warns "it will
still be a while before the winners are declared, since the county will
continue to check and count votes over the next several weeks," clearly
distinguishing the election-night state it just reported from the
multi-week canvass that follows).

### Plateau vs first tranche
MendoFever's 8:09pm/62.66%-precincts figure is explicitly excluded as the
first tranche. The MendoVoice 7,418 figure is the LAST reported county
update before the multi-week canvass, self-described as occurring "after
midnight on election night." No non-circular SECOND leg (Wayback bracket,
later-capture-same-count) is obtainable since the underlying county page
itself was never captured with rendered content in this window — kept
PLAUSIBLE, not CONFIRMED.

### Arithmetic
7,418 / 23,935 = 0.309963... → **30.99%**

### Draft dataset row
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 7418,
  "certified_final": 23935,
  "election_night_pct": 30.99,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://mendovoice.com/2024/03/did-you-vote-yet-mendocino-county-and-california-primary-election-ends-today-with-results-beginning-tonight/",
  "confidence": "secondary",
  "note": "WAYBACK DEAD END (same shape as 2022 and the 2024 general): /acr/cgi-bin/currentFR.pl CDX (Feb-Apr 2024) has a pre-election placeholder (Mar 3) then jumps to Mar 22/29, both explicitly labeled 'ELECTION RESULTS UPDATE' (canvass), Mar 22 reading 'Run Date 03/21/2024 ... Registered Voters 22615 of 52602 = 42.99% ... Precincts Reporting 241/241 = 100.00%' -- a post-night canvass state, 16 days late, not yet even the certified 23,935. The new CMS wrapper page has a capture at 2024-03-06 01:21 AM PST (within the up-to-4am window!) but it only contains the unrendered iframe tag pointing to the cross-origin currentFR.pl, which Wayback's crawler did not separately capture at that moment (near miss). RECOVERED VIA TWO NEWS SOURCES, monotonically corroborating: (1) MendoFever's live-blog (mendofever.com/2024/03/05/its-election-night-in-mendocino-county-election-live-updates-and-preliminary-results/, Wayback id_ raw fetch, gzip'd/gunzipped) has one checkpoint, explicitly partial: 'As of 8:09 p.m., 7,094 registered voters' ballots have been tallied and 62.66% of the county's precincts have reported their results' -- the classic first tranche, NOT used on its own. (2) The Mendocino Voice (mendovoice.com/2024/03/did-you-vote-yet-mendocino-county-and-california-primary-election-ends-today-with-results-beginning-tonight/, curl -A <UA> live fetch HTTP 200) carries a later checkpoint on the same rolling article: 'UPDATE 3/6/24 9:30 a.m.: Mendocino County's election results were updated after midnight on election night, and the current results include a total of 7,418 ballots, just over 14% of the county's 52,602 registered voters. This update includes a few hundred votes from ballots cast in person yesterday...' Arithmetic: 7,418/52,602 = 14.10%, matches 'just over 14%' exactly. Non-circular corroboration: a modest, consistent increase over MendoFever's independently-recovered 7,094 (+324, 'a few hundred votes from ballots cast in person' matches exactly), and the article explicitly frames 7,418 as the state reached 'after midnight on election night,' separately warning the canvass would continue 'over the next several weeks' -- distinguishing the election-night state from the later canvass. No non-circular second leg (no Wayback capture of the rendered county page survives), so PLAUSIBLE not CONFIRMED. Certified final 23,935 voters (CA SoS Voter Participation Statistics by County, 2024 primary: 324 precinct + 23,611 VBM = 23,935; https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf, re-fetched fresh 2026-07-10, arithmetic cross-checked: 23,935/53,194 = 45.00% matches printed Turnout-Registered). Pct = 7,418/23,935 = 30.99%. Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see county-tech record). FLAG for manual operator: numerator is news-sourced (two outlets, monotonically consistent) rather than a directly-captured document; a human read is recommended before promotion, same as the other secondary rows in this dossier."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2024 | presidential-primary | 7,418 | 23,935 | 31.0% | secondary | [link](https://mendovoice.com/2024/03/did-you-vote-yet-mendocino-county-and-california-primary-election-ends-today-with-results-beginning-tonight/) |`

Detail bullet:
```
- **2024 presidential-primary** — night `7,418` / final `23,935` = `31.0%` (secondary)
  - numerator: <https://mendovoice.com/2024/03/did-you-vote-yet-mendocino-county-and-california-primary-election-ends-today-with-results-beginning-tonight/>
    ("UPDATE 3/6/24 9:30 a.m.: ... updated after midnight on election
    night ... a total of 7,418 ballots, just over 14% of the county's
    52,602 registered voters"), corroborated by
    <https://mendofever.com/2024/03/05/its-election-night-in-mendocino-county-election-live-updates-and-preliminary-results/>
    (8:09pm checkpoint: 7,094 ballots, 62.66% precincts -- the excluded first tranche)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "updated after midnight on election night ... a total of
    7,418 ballots, just over 14%"
```

### plateau_review.json record
```json
{
  "slug": "mendocino-ca",
  "date": "2024-03-05",
  "verdict": "PLAUSIBLE",
  "basis": "News source explicitly frames the figure as the state reached 'after midnight on election night,' distinguished from the multi-week canvass that follows; independently corroborated by a monotonic increase over a second outlet's earlier same-night checkpoint. No document-level capture obtainable (a near-miss Wayback capture of the CMS wrapper exists at the right timestamp but the cross-origin iframe content was not separately crawled), so PLAUSIBLE not CONFIRMED.",
  "evidence": "mendovoice.com/.../did-you-vote-yet-.../: 'UPDATE 3/6/24 9:30 a.m.: ... updated after midnight on election night ... a total of 7,418 ballots, just over 14%'; mendofever.com/.../its-election-night-.../: 'As of 8:09 p.m., 7,094 registered voters' ballots have been tallied'"
}
```

### Verdict
**PLAUSIBLE, secondary, FLAGGED for manual operator review.**

---
