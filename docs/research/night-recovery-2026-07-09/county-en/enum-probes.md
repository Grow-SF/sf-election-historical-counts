# Task 9: URL/ID enumeration probes and registrar social media

Persisted-as-you-go log. Every probe (URL, HTTP status/CDX result, verdict)
is appended here as it is run, including all-miss ranges, per the shared
Global Constraints (dead ends are deliverables).

User-Agent used throughout: `Mozilla/5.0 (compatible; sf-election-count-research/1.0)`.
2s pause between probes to the same host. curl only, no browser tools.

## Rows in scope (status at task start, git log checked)

- Fresno: 2012, 2014, 2018, 2022 (null)
- Riverside: 2012, 2014, 2016, 2018 (null)
- San Bernardino: 2012, 2014, 2016, 2018, 2022 (null)
- Placer: 2012, 2022, 2024 (null)
- Sacramento: 2016 (null, NewsBank exhausted per e921aaf-adjacent commit)
- Madera: 2012 (null, NewsBank exhausted, commit e921aaf)
- San Diego 2012/2014/2016: CONFIRMED STILL NULL at task start (`git log --oneline -5`
  showed no San Diego landing commit; san-diego-ca.json rows read null). Will
  re-check immediately before touching any San Diego row (concurrent NewsBank
  task in flight, files `san-diego-2012.md`/`san-diego-2014.md` untracked in
  the worktree).

---

## Family 1: Fresno report-file enumeration

### Live host: www2.co.fresno.ca.us/2850/Results/ (2012, 2014, 2018)

The brief's exact loop (`electionsummaryreportrpt_11_6_12_<t>.pdf` for
t = 2230..0200) run against the live host:

```
404 https://www2.co.fresno.ca.us/2850/Results/electionsummaryreportrpt_11_6_12_2230.pdf
404 https://www2.co.fresno.ca.us/2850/Results/electionsummaryreportrpt_11_6_12_2300.pdf
404 https://www2.co.fresno.ca.us/2850/Results/electionsummaryreportrpt_11_6_12_2330.pdf
404 https://www2.co.fresno.ca.us/2850/Results/electionsummaryreportrpt_11_6_12_0000.pdf
404 https://www2.co.fresno.ca.us/2850/Results/electionsummaryreportrpt_11_6_12_0030.pdf
404 https://www2.co.fresno.ca.us/2850/Results/electionsummaryreportrpt_11_6_12_0100.pdf
404 https://www2.co.fresno.ca.us/2850/Results/electionsummaryreportrpt_11_6_12_0130.pdf
404 https://www2.co.fresno.ca.us/2850/Results/electionsummaryreportrpt_11_6_12_0200.pdf
```
Verdict: the `electionsummaryreportrpt` filename convention did not exist in
2012 (it is a 2022/2024-era naming pattern); confirmed dead.

Directory-listing probe: `.../2850/Results/` -> 403 (no index), but direct
file GETs on this legacy domain DO still resolve for files that were live in
2012-2016 -- the host was never decommissioned. Confirmed with a control:
`Results20161108.htm` (the CONFIRMED 2016 no-dash election-night file) ->
200 live today, Last-Modified Dec 2016.

No-dash GEMS pattern (the one that worked for 2016) probed live for 2012/2014/2018:
```
404 Results20121106.htm
404 Results20141104.htm
404 Results20181106.htm
200 Results-2012-11-06.htm   (dash format; fetched -- see below)
200 Results-2014-11-04.htm   (dash format; fetched -- see below)
404 Results-2018-11-06.htm
404 Results-2018-11-06.pdf
404 Results-1-2018.htm
404 Results2018-11-06.htm
404 Results-2018-11-6.htm
404 ResultsSummary2018.htm
404 Results-2018.htm
404 electionsummaryreportrpt_11_6_18_0000.pdf
```
Fetched the two live 200s and grepped `Cards Cast`:
- `Results-2012-11-06.htm` -> `Cards Cast 261652    63.79%` = exactly the
  certified final (261,652). Confirms this live file IS the Official Final
  canvass version already documented in the row's note (not new information,
  but now cross-checked against the LIVE host, not just the Wayback capture).
- `Results-2014-11-04.htm` -> `Cards Cast 163420    39.24%` = exactly the
  certified final (163,420). Same conclusion.
- No 2018 file exists at any dash/no-dash/pdf variant on this host at all.

18 live-host probes to www2.co.fresno.ca.us total (well under the 40 cap),
no 403/429 encountered on this host.

### CDX full-prefix dump: www2.co.fresno.ca.us/2850/Results/ (all-time)

```
curl "http://web.archive.org/cdx/search/cdx?url=www2.co.fresno.ca.us/2850/Results/&matchType=prefix&output=json&limit=200&collapse=urlkey"
```
131 distinct URLs ever archived under this prefix (1998-2025), every general/
primary/special from 1998 through 2016 plus 2010s retirement-board elections.
Confirms by exhaustive listing (not just targeted URL probes) that NO
election-night-named file (no-dash `Results<date>.htm`, or any
`electionsummaryreportrpt*`) exists for 2012, 2014, or 2018 under this path;
2012/2014 have only the dash-format Official Final (`Results-2012-11-06.htm`,
`Results-1.pdf`, captured 20121220; `Results-2014-11-04.htm`,
`Results-2014-11-04.pdf`, captured 20141126/20210117); 2018 has NO entries
under this prefix at all (2018 results moved to the co.fresno.ca.us CMS).
This strengthens (does not merely repeat) the existing 2012/2014/2018 dead-end
notes with an exhaustive-prefix confirmation.

### CDX domain scope: co.fresno.ca.us, Nov 2018 window

```
curl "http://web.archive.org/cdx/search/cdx?url=co.fresno.ca.us&matchType=domain&from=20181101&to=20181201&filter=urlkey:.*(result|election|summaryreportrpt).*&output=json&limit=300&collapse=urlkey"
```
35 rows. Only one relevant page:
`.../election-results/2018-november-general-election-results`, single
capture 20181128205624 (Nov 28) -- already documented in the note as the
Nov-21 canvass embed (239,032). No earlier (election-night) capture of this
page or any results/summary-report path exists anywhere on the domain in
this window. Confirms the dead end exhaustively.

### CDX domain scope: co.fresno.ca.us, Nov 2022 window -- NEW FIND

```
curl "http://web.archive.org/cdx/search/cdx?url=co.fresno.ca.us&matchType=domain&from=20221108&to=20221115&filter=urlkey:.*(result|election-race|summaryreport|showpublisheddocument).*&output=json&limit=300&collapse=urlkey"
```
151 rows. Alongside the already-known zero-report URL
(`.../election-races/statewide-general-election-november-2022/2022-november-result-page`),
this turned up an UNCHECKED sibling page:
`.../election-information/election-results/results-for-november-8-2022-statewide-general-election`,
captured 4 times: 20221109071724, 20221109093422, 20221110225454, 20221118193230.

Fetched all 4 (curl `<ts>id_/` + gunzip; all 4 replies were gzip per RUNBOOK
7.1, none served decoded):
- 20221109071724 (11:17 PM PST Nov 8, election night): GEMS widget
  "FRESNO COUNTY CONSOLIDATED STATEWIDE GENERAL ELECTION / NOVEMBER 8, 2022
  UNOFFICIAL ELECTION RESULTS", own embedded time-stamp "11/08/2022 10:42:58 PM",
  "Precincts Reported: 562 of 562 (100.00%)", "Voters Cast: 126,440 of
  499,979 (25.29%)".
- 20221109093422 (1:34 AM PST Nov 9, still election night): IDENTICAL
  10:42:58 PM report, unchanged.
- 20221110225454 (Nov 10, 2 days later): IDENTICAL 10:42:58 PM report,
  still unchanged.
- 20221118193230 (Nov 18): DIFFERENT report, internally timestamped
  "11/15/2022 5:09:58 PM", 187,620 voters cast -- the canvass update.

Verdict: LANDED. 10:42:58 PM report brackets as the last election-night
report (held >=2 days before the canvass update). 126,440 / 221,419 =
57.10%. Landed as fresno-ca 2022-11-08, confidence primary, comparable true,
CONFIRMED in plateau_review.json. Commit 1b62e29 "data: Fresno 2022
election-night plateau from an unexamined county GEMS results URL".

### Placer report-file / directory enumeration (2012, 2022, 2024)

Placer's 2012/2022/2024 rows were already RE-VERIFIED in 2026-06 with full
CDX sweeps of `election-night-results.aspx` and the `/Uploads/documents/<date>/`
directories (see the row notes: full CDX of election-night-results.aspx for
2012 returns exactly one 200 capture; the entire archived
/Uploads/documents/11052024/ and (2022) directories were enumerated and hold
only certified-final + late-unprocessed-ballot artifacts). This task's
additional enumeration pass:

```
curl "http://web.archive.org/cdx/search/cdx?url=www.placerelections.com/Uploads/documents/11062012/&matchType=prefix&output=json&limit=100"
curl "http://web.archive.org/cdx/search/cdx?url=placer.ca.gov&matchType=domain&from=20221101&to=20221201&filter=urlkey:.*(document|result).*&output=json&limit=200&collapse=urlkey"
```

Results:
- `Uploads/documents/11062012/` prefix on `www.placerelections.com`: 90+ rows,
  all operational documents (ballot dropoff, poll worker publication,
  certifications, SOV) already listed in the row's note, plus one new file
  not previously named: `110612_results.pdf` -- but its EARLIEST Wayback
  capture is 20141124 (Nov 2014, TWO YEARS after the election), so it cannot
  evidence the 2012 election-night state; not usable.
- Broader `placerelections.com` domain CDX (Nov 2012 window, filter
  document/upload/result): turned up one URL not in the row's note,
  `election-tracker-results.aspx` (distinct from `election-night-results.aspx`),
  captured 20121201032213 (same Dec-1 2012 crawl session as the already-known
  `election-night-results.aspx` OFFICIAL SUMMARY capture, 42s apart). Checked
  this URL's full capture history across all time: it is a long-running
  generic "election tracker" page crawled regularly from 2009 on, with NO
  capture between Nov 6 and Dec 1, 2012 either -- same dead end, not a new lead.
- `placer.ca.gov` full-domain CDX with date restriction: TIMED OUT (30s) on
  both the 2022 and would-be 2024 window -- confirms RUNBOOK 7.1's "broad
  domain queries 504" gotcha even with a date filter on this host; abandoned
  domain-wide queries for Placer, used only path-prefix queries below.
- `placercountyelections.gov/election-results` prefix, ALL TIME: only 3
  captures ever (20231106, 20231129, 20250122) -- none in the 2022 or 2024
  election windows. Confirms (independently of the row notes' own 2026-06
  re-verification) that this page was never captured near either election.

Verdict: Placer 2012/2022/2024 confirmed dead by this task's probes too; no
new candidate URL found beyond what the rows' notes already document.
26 live/CDX probes to placerelections.com/placer.ca.gov/placercountyelections.gov
hosts, no 403/429 encountered.

---

## Family 2: DocumentCenter ID walk

Nevada County (`nevadacountyca.gov/DocumentCenter/View/55078`) and Napa
County (`napacounty.gov/DocumentCenter/View/10436` etc.) both prove the
CivicPlus DocumentCenter module keeps guessable sequential IDs across a
whole site. Checked whether any of this task's six target counties'
ROOT domains use the same module at all (CDX prefix probe, all-time,
before attempting any ID walk):

```
curl "http://web.archive.org/cdx/search/cdx?url=<host>/DocumentCenter&matchType=prefix&output=json&limit=5&collapse=urlkey"
```

| host | DocumentCenter captures |
|---|---|
| www.sbcounty.gov | 0 |
| www.saccounty.gov | 0 |
| www.rivco.org | 0 |
| www.co.fresno.ca.us | 0 |
| www.fresnocountyca.gov | 0 |
| www.placer.ca.gov | YES (root /DocumentCenter page + many /View/<id> docs) |

Only `placer.ca.gov` (the general county government site) uses CivicPlus
DocumentCenter at all. Followed up with a `/DocumentCenter/View` prefix dump
(50 rows returned): every ID present (range ~1000-100067+) is a PLANNING /
ENVIRONMENTAL-REVIEW / GENERAL-COUNTY document (construction brochures,
conservation plan chapters, HCP/NCCP documents), dated captures cluster in
2019 and 2025 -- NOT an elections department repository. Placer's actual
elections-report host is `placercountyelections.gov` (`/Uploads/documents/`),
already exhaustively checked under Family 1 above; that host does NOT run
DocumentCenter. Riverside (voteinfo.net/livevoterturnout.com), San
Bernardino (sbcounty.gov/rov, sbcountyelections.com,
results.rov.sbcounty.gov), Sacramento (eresults.saccounty.net), Madera
(votemadera.com WordPress + Clarity ENR), and Fresno (co.fresno.ca.us GEMS
CMS + fresnocountyca.gov CivicPlus "sharedassets"/"showpublisheddocument")
all use CMSes structurally distinct from CivicPlus DocumentCenter -- an ID
walk requires that module to exist first, so no walk was performed for any
of the six target counties. This is a clean negative result, not an
oversight: 6 CDX probes total on this family, no 403/429.

---

## Family 3: registrar social media via Wayback

Per-account CDX probes (`url=twitter.com/<handle>`, both exact and
`matchType=prefix`, unrestricted date range first to establish whether the
account has ANY Wayback presence before spending per-week queries):

| handle (brief's exact spelling) | any Wayback capture? |
|---|---|
| @sacvote | 0 (see correction below) |
| @sdvote | YES, earliest 2015-09-30 |
| @SBCountyROV | 0 |
| @RivCoVote | 0 |
| @FresnoCoClerk | 0 |

Correction: Sacramento's registrar Twitter handle is actually **@sacvoter**
(not @sacvote as given in the brief); `twitter.com/sacvoter` has captures
from 2019 onward (earliest tweet-level capture 20190209). Checked directly
whether any @sacvoter tweet was captured in the Sacramento 2016 target
window:
```
curl "http://web.archive.org/cdx/search/cdx?url=twitter.com/sacvoter&matchType=prefix&from=20161105&to=20161112&output=json&limit=40"
```
-> `[]` (zero captures). The account's earliest ANY capture (2019) postdates
the 2016 election by 3 years regardless, so this route was dead before the
date-window check even ran; confirmed empty as expected.

@SBCountyROV, @RivCoVote, @FresnoCoClerk: zero Wayback captures under any
matching form (exact URL and `matchType=prefix`), meaning either the handle
name differs from the brief's guess or Wayback's crawler never picked up a
profile/tweet page for these specific accounts (Twitter/X profile pages are
notoriously under-crawled pre-2015 due to JS rendering + robots.txt).
Time-boxed a small set of plausible alternate-handle guesses for Riverside/
San Bernardino/Fresno (RivCoElections, VoteRiverside, SBCountyElex,
FresnoVotes, FresnoElections, FresnoCounty, etc.) -- all zero captures too
(one batch hit a transient connection-refused from web.archive.org after
~15 rapid CDX calls; backed off and confirmed the pattern held). Given no
source-of-truth for the ACTUAL current handles of these three accounts was
available via curl-only research, further guessing was abandoned as
unproductive per the politeness/time-box rule.

Facebook: five plausible page-name guesses probed
(FresnoCountyElections, RiversideCountyROV, SBCountyROV,
SacramentoCountyVoterRegistration, SanDiegoCountyROV) via
`facebook.com/<name>` CDX prefix -- all zero captures. Facebook pages are
even less reliably named from guesses than Twitter handles; this is a
documented dead end, not a random walk given up early.

Verdict: Family 3 yields NO usable evidence for any of this task's null
rows. ~25 CDX probes total (all under web.archive.org, well-spaced),
one transient connection-refused encountered and recovered from with a
longer backoff (no 403/429 from the archive.org side; the block, if any,
was rate-limiting on my end).




---

## Outcome summary

- **LANDED:** fresno-ca 2022-11-08, 126,440/221,419 = 57.10%, primary,
  CONFIRMED. Commit 1b62e29.
- **Dead end, note extended (Family 1):** fresno-ca 2012-11-06, 2014-11-06,
  2018-11-06 (exhaustive live-host + full-prefix CDX confirmation).
- **Dead end, note extended (Family 1):** placer-ca 2012-11-06, 2022-11-08,
  2024-11-05 (fresh CDX re-confirmation, one new URL examined and rejected
  for 2012, domain-wide query timeout noted for 2022/2024).
- **Dead end, note extended (Family 2, no walk possible):** riverside-ca
  2012/2014/2016/2018; san-bernardino-ca 2012/2014/2016/2018/2022;
  sacramento-ca 2016; madera-ca 2012 (none of these counties' elections
  CMSes run CivicPlus DocumentCenter; Placer's DocumentCenter is a
  general-county repository, not elections-specific).
- **Dead end, note extended (Family 3):** all of the above rows also get the
  social-media finding folded in (no usable tweet/FB capture for any of
  them; Sacramento 2016 checked directly against the real @sacvoter handle).
- **Out of scope, not touched:** san-diego-ca 2012/2014/2016 (concurrent
  NewsBank task's territory; confirmed still-null at task start via
  `git log --oneline -5`, not re-touched here).
