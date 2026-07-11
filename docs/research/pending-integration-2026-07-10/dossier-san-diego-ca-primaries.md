# San Diego County, CA — statewide-PRIMARY election-night dossier

READ-ONLY research scaffold for a future `data/research/election-night/san-diego-ca.json`
addition (primaries). This file is NOT that JSON and is not committed; nothing
in the repo is edited by this pass. Methodology: docs/research/RUNBOOK.md
section 1 (PLATEAU metric, not first tranche), 5 (null/ceiling conventions),
6 (source routes 6.2-6.6), 7 (Wayback gotchas), 8 (plateau evidence standard).

Scope: 2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05 (extend the thin
pre-e-pollbook period; SD adopted e-pollbooks 2022 per
`data/research/election-night/san-diego-ca.json`), 2022-06-07 (adoption-year
primary — rollout timing investigated below), 2024-03-05 (post-adoption,
also post-ASV 2024).

Baseline established by the existing GENERALS row-set (read before this
pass): San Diego's live-results platform history is (a) pre-2018: a JS
viewer of `sdvote.com/content/rov/electioninfo/election.xml`, essentially
unarchived on election night for Nov 2012/2014/2016, EXCEPT the general's
own note flags that Wayback DID capture `election.xml` around the **June
2016 primary** — a lead this dossier chases; (b) 2018-2021:
`livevoterturnout.com/SanDiego/LiveResults/en/Index_N.html`, first archived
election-night-capable page being the **June 2018 primary** per the 2012
general's note ("earliest archived SD results page is the June 2018
primary"); (c) June 2022 primary onward:
`livevoterturnout.com/ENR/sandiegocaenr/N/en/Index_N.html` — the general's
own note states this ENR URL scheme is in use "from the June 2022 primary
on," meaning the June 2022 primary is the FIRST election on the ENR/vote-center
platform, directly relevant to the e-pollbook rollout-timing question below.
No morning-after "semi-final results" press release was ever found for SD in
the generals pass (registrar directs public to the live SDVote.com page
instead of issuing a release); this dossier re-checks that route fresh for
the primary dates per the runbook's guidance that a dead route for Nov
doesn't imply dead for June.

---

## Denominators (CA SoS Statement of Vote, Voter Participation Statistics by County)

All six located directly (curl, `pdftotext -layout`, San Diego row extracted;
arithmetic Precinct + VBM = Total Voters verified for each). Cache:
scratch `sov/*.pdf`.

| date | type | SoV URL | Precinct | VBM | Total Voters (denominator) | Turnout/Reg |
|---|---|---|---:|---:|---:|---:|
| 2012-06-05 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf | 187,942 | 360,520 | 548,462 | 37.43% |
| 2014-06-03 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf | 113,714 | 306,986 | 420,700 | 27.23% |
| 2016-06-07 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf | 285,370 | 490,560 | 775,930 | 50.94% |
| 2018-06-05 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf | 197,501 | 476,139 | 673,640 | 40.02% |
| 2022-06-07 | statewide-primary | https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf | 45,332 | 629,276 | 674,608 | 34.91% |
| 2024-03-05 | presidential-primary | https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf | 53,989 | 650,079 | 704,068 | 36.47% |

Notes on URL anatomy (year-to-year variation confirmed; matches the pattern
found independently for San Bernardino/Riverside primaries in sibling
scratch dossiers — cross-checked, consistent):
- 2012 primary: NO standalone `.../03-voter-participation-stats-by-county.pdf`
  (403). The file that has the "VOTER PARTICIPATION STATISTICS BY COUNTY"
  table is titled (misleadingly) `03-voter-reg-stats-by-county.pdf` — do not
  confuse with the actually-registration-stats `02-voter-reg-stats-by-county.pdf`
  in the same directory. Confirmed by in-PDF header text and columns
  (Precincts / Eligible / Registered / Precinct Voters / VBM Voters / Total
  Voters / %VBM / Turnout-Reg / Turnout-Eligible).
- 2014 keeps the SoS's well-known misspelling "particpiation" in the path.
- 2016 primary lives at the primary-dir ROOT (`/sov/2016-primary/03-...`,
  no `sov/` or `pdf/` subsegment) — different from the 2016 GENERAL
  (`/sov/2016-general/sov/03-...`).
- 2018/2022/2024 all use `/sov/<year>-primary/sov/03-voter-participation-stats-by-county.pdf`
  (same convention as their respective generals). 2022/2024 rows carry a
  "San Diego*" asterisk = standard vote-center footnote, not a data flag.

---

## 2022-06-07 statewide-primary — ROLLOUT-TIMING FINDING (read this first)

`data/research/county-tech/san-diego-ca.json` (already in the repo, independently
researched) states explicitly, for BOTH `epollbook` and `vote-center` tech
records: `"first_election": "2022-06"`, i.e. **"the first election conducted
under it was the June 7, 2022 Gubernatorial Primary"** (Board of Supervisors
approved the VCA vote-center/e-pollbook model 2021-10-19; vendor Tenex
Precinct Central V 6.0.1; source: CA SoS "Voting Technologies Used by
Counties" Nov 5 2024 PDF + San Diego EAP 09/05/2023). So **YES — the June
2022 primary was run on the new e-pollbooks**, not just the following
November general. This is corroborated independently in this pass by the
livevoterturnout ENR platform itself: the June 2022 primary is
`ElectionID 15` on `livevoterturnout.com/ENR/sandiegocaenr/`, and the Nov
2022 general (already CONFIRMED plateau in san-diego-ca.json) is
`ElectionID 16` — i.e. June 2022 is the FIRST election on this ENR/vote-center
platform generation, immediately followed by the Nov 2022 general, with no
election between them. `vs_epollbook` for **both** 2022 rows should be
`"post"`.

### 2022-06-07 numerator (CONFIRMED plateau)

Route: 6.4/6.5, the ENR page + its data feed, via Wayback (no rendering
needed for the corroborating leg — the XML feed is plain-text).

- CDX for `livevoterturnout.com/ENR/sandiegocaenr/15/en/Index_15.html`
  (2022-06-07 to 2022-06-12): only ONE election-night-window capture,
  `20220608181901` (2022-06-08 11:19:01 PDT, i.e. late morning after the
  primary). Rendered via `render_wayback.cjs`-style puppeteer render
  (`WB_URL=https://web.archive.org/web/20220608181901/https://www.livevoterturnout.com/ENR/sandiegocaenr/15/en/Index_15.html`):
  ```
  Website Updated: 6/8/2022 12:39:38 AM
  UNOFFICIAL ELECTION RESULTS
  PROJECTED OUTSTANDING BALLOTS: 250,000
  NEXT POST 6/9/22 BY 5PM
  VOTER TURNOUT 21.5%
  Ballots Cast 416,748
  Vote Center Ballots 44,165
  Mail Ballots 372,583
  Registered Voters 1,933,896
  ```
  The internal "Website Updated" stamp (12:39:38 AM, past-midnight election
  night) IS the plateau data-timestamp; the page's own "NEXT POST 6/9/22 BY
  5PM" text (still showing at the 11:19am capture, hours later, with no
  intervening update) is the county's own posting-schedule bracket per
  RUNBOOK 8.
- Independent corroborating leg: `summary_15.xml` (same ElectionID, the
  underlying plain-XML data feed, no rendering required) was captured 3x by
  Wayback on 2022-06-10 23:08 UTC; all three carry the SAME embedded
  `<GeneratedDate>2022-06-09T16:49:11.541-07:00</GeneratedDate>` and
  `<TotalBallotsCast>475054</TotalBallotsCast>` — i.e. the NEXT report after
  election night is dated 6/9 4:49pm PDT (matching "NEXT POST 6/9/22 BY 5PM"
  exactly) and shows 475,054, a jump from 416,748. This proves 416,748 held
  through the night and the very next update was post-night canvass, per
  RUNBOOK 8's "later capture of a companion data source confirming the next
  report is post-night" leg. CONFIRMED.
- Arithmetic: 416,748 / 674,608 certified = **61.78%** (416748/674608*100 =
  61.7764...).
- `election_night_pct`: 61.78. `confidence`: primary. `vs_epollbook`: post
  (per finding above). `vs_asv`: pre (SD's ASV first-use year is 2024).
- `source_url_night`:
  `https://web.archive.org/web/20220608181901/https://www.livevoterturnout.com/ENR/sandiegocaenr/15/en/Index_15.html`
- Draft row (type `statewide-primary`):
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 416748,
  "certified_final": 674608,
  "election_night_pct": 61.78,
  "vs_epollbook": "post",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20220608181901/https://www.livevoterturnout.com/ENR/sandiegocaenr/15/en/Index_15.html",
  "confidence": "primary",
  "note": "PLATEAU metric. ROLLOUT-TIMING: this is the FIRST election on SD's ENR/vote-center/e-pollbook platform (ElectionID 15; Nov 2022 general = ElectionID 16, immediately next); data/research/county-tech/san-diego-ca.json independently confirms both epollbook and vote-center adopted_year 2022 first_election '2022-06' = this primary. So vs_epollbook=post for THIS row too, not just Nov 2022. Index_15.html (Wayback 20220608181901, PDT 11:19am 6/8) shows internal 'Website Updated: 6/8/2022 12:39:38 AM' (post-midnight election-night update) with Ballots Cast 416,748 and 'NEXT POST 6/9/22 BY 5PM' still posted hours later with no intervening update = county's own posting-schedule bracket. Corroborating leg: summary_15.xml (plain XML feed, 3 Wayback captures 2022-06-10) all show GeneratedDate 2022-06-09T16:49:11-07:00 / TotalBallotsCast 475,054 = the very next (post-night, 6/9 5pm) report, confirming 416,748 held through the night. 416,748/674,608 certified = 61.78%. CONFIRMED plateau. vs_asv=pre (ASV first-use year 2024)."
}
```

---

## 2024-03-05 presidential-primary (CONFIRMED plateau, best-evidenced row in this dossier)

ElectionID on the same ENR platform: `sandiegocaenr/19` (ElectionID 18,
captured 2024-02-01, is a different/earlier item, not this primary; 19 is
confirmed by its March 6 election-night captures and "Presidential Primary
Election" page title). No plain-text/XML data feed was captured for
ElectionID 19 (unlike 2022's `summary_15.xml`), so this relies entirely on
puppeteer-rendered Wayback captures of `Index_19.html` — but the sequence is
unusually rich and self-labeling:

| Wayback ts (UTC) | local (PST) | internal "Website Updated" | header | Ballots Counted |
|---|---|---|---|---|
| 20240306080941 | 3/6 12:09am | 3/5/2024 11:38:36 PM | "UNOFFICIAL ELECTION RESULTS" | 420,618 |
| 20240306103630 | 3/6 2:36am | 3/6/2024 12:46:42 AM | **"FINAL UNOFFICIAL ELECTION NIGHT RESULTS"**, "NEXT UPDATE: MAR. 7" | **425,572** |
| 20240306145646 | 3/6 6:56am | 3/6/2024 12:46:42 AM (same) | same header/schedule | 425,572 (held) |
| 20240306223911 | 3/6 2:39pm | 3/6/2024 12:46:42 AM (same) | same header/schedule | 425,572 (held, +14h) |
| 20240308170624 | 3/8 9:06am | 3/7/2024 4:48:18 PM | "NEXT UPDATE: MAR. 8" (canvass resumed) | 492,333 |

The 2:36am capture is the plateau: the page itself carries the literal
header **"FINAL UNOFFICIAL ELECTION NIGHT RESULTS"** (the runbook's own
calibration phrase, RUNBOOK.md section 1) plus an explicit
"NEXT UPDATE: MAR. 7" schedule note, and the SAME internal timestamp/count
(425,572) is still showing 14 hours later at 2:39pm on 3/6 with no
intervening update — then the 3/8 capture shows the canvass resumed exactly
per that promised schedule (Website Updated 3/7 4:48:18 PM, Ballots Counted
jumped to 492,333). Self-description (leg 1) + held-across-later-captures
(leg 2) + county's own posting schedule (leg 3, redundant with leg 2) all
present. CONFIRMED, no ambiguity.

- Arithmetic: 425,572 / 704,068 certified = **60.44%**
  (425572/704068*100 = 60.4448...).
- `vs_epollbook`: post (2022 adoption, well before this election).
- `vs_asv`: **AMBIGUOUS, FLAG for manual operator.** SD's ASV `adopted_year`
  is 2024 per `data/research/county-tech/san-diego-ca.json`, but that
  record's own note says: "Could not pin first election to March 2024
  primary vs Nov 2024 general from primary sources." The existing
  `san-diego-ca.json` general row for 2024-11-05 marks `vs_asv: "post"`
  without qualification. Applying the coarse annual rule (adopted_year 2024
  => any 2024 election is "post") this row would ALSO be `"post"`, but that
  is not independently confirmed for the March date specifically — it may
  actually be the FIRST asv election, or ASV may not yet have rolled out.
  Recommend the operator either (a) accept "post" per the coarse annual
  rule for consistency with the Nov 2024 general row, or (b) research SD's
  ASV go-live date more precisely (board minutes / RFP timeline) before
  finalizing. This dossier defaults to "post" below to match the existing
  Nov-2024-row convention but flags the caveat in the note.
- `source_url_night`:
  `https://web.archive.org/web/20240306103630/https://www.livevoterturnout.com/ENR/sandiegocaenr/19/en/Index_19.html`
- Draft row (type `presidential-primary`):
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 425572,
  "certified_final": 704068,
  "election_night_pct": 60.44,
  "vs_epollbook": "post",
  "vs_asv": "post",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20240306103630/https://www.livevoterturnout.com/ENR/sandiegocaenr/19/en/Index_19.html",
  "confidence": "primary",
  "note": "PLATEAU metric, best-evidenced row in this dossier. ENR page Index_19.html (ElectionID 19) literally headers itself 'FINAL UNOFFICIAL ELECTION NIGHT RESULTS' with internal 'Website Updated: 3/6/2024 12:46:42 AM' and 'NEXT UPDATE: MAR. 7' at the Wayback 20240306103630 capture (2:36am PST 3/6), Ballots Counted 425,572. That exact count+timestamp HELD across two later same-day captures (20240306145646 6:56am, 20240306223911 2:39pm, +14h) with no intervening update, then the 20240308170624 capture (3/8) shows Website Updated 3/7/2024 4:48:18 PM / Ballots Counted 492,333 -- the canvass resumed exactly on the promised MAR.7 schedule. Triple-legged CONFIRMED (self-description + held-across-captures + county posting-schedule bracket, all independently satisfied). 425,572/704,068 certified = 60.44%. vs_epollbook=post (2022 adoption). vs_asv=post per the coarse adopted_year=2024 rule and to match the existing 2024-11-05 general row's convention, BUT FLAG for manual operator: data/research/county-tech/san-diego-ca.json explicitly could not pin ASV's first election to March vs Nov 2024; this row's vs_asv should be reconsidered if a more precise ASV go-live date is later found."
}
```

---

## 2018-06-05 statewide-primary (CONFIRMED plateau)

Pre-vote-center/pre-e-pollbook era; platform `livevoterturnout.com/SanDiego/LiveResults/en/Index_N.html`
(same as the Nov 2018 general, which used Index_5). This June 2018 primary is
`Index_3` (confirmed by page content: "Statewide Direct Primary Election" /
turnout numbers; there is no Index_4 capture between this and the Nov 2018
general's Index_5, consistent with SD's index counter incrementing per
election). CDX for Index_3.html finds exactly ONE capture inside the
election-night window (2018-06-05 18:00 to 2018-06-06 12:00 PDT):
`20180606114855` (2018-06-06 04:48:55 AM PDT).

Rendered (puppeteer via `render_wayback.cjs`-style script):
```
Website Updated: 6/6/2018 04:44:12 AM
UNOFFICIAL RESULTS - ELECTION NIGHT FINAL (ESTIMATED OUTSTANDING BALLOTS 220,000)
Ballots Cast 406,501
```
The page's own header literally says **"ELECTION NIGHT FINAL"** (self-
description, leg 1). The next available capture, `20180608031615`
(2018-06-07 8:16pm PDT, ~37.5h later), shows a DIFFERENT internal timestamp
("Website Updated: 6/7/2018 05:15:43 PM") and a higher Ballots Cast
(427,779) — proving the 406,501/04:44am figure was superseded only by a
post-night canvass update, not still-accumulating same-night activity (leg
2, "a later capture of the same report series showing growth"). CONFIRMED.

- Arithmetic: 406,501 / 673,640 certified = **60.34%**
  (406501/673640*100 = 60.34399...).
- `vs_epollbook`: pre (2022 adoption). `vs_asv`: pre (2024 adoption).
- `source_url_night`:
  `https://web.archive.org/web/20180606114855/http://www.livevoterturnout.com/SanDiego/LiveResults/en/Index_3.html`
- Draft row (type `statewide-primary`):
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 406501,
  "certified_final": 673640,
  "election_night_pct": 60.34,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20180606114855/http://www.livevoterturnout.com/SanDiego/LiveResults/en/Index_3.html",
  "confidence": "primary",
  "note": "PLATEAU metric. San Diego's June 2018 primary is livevoterturnout.com/SanDiego/LiveResults/en/Index_3.html (Nov 2018 general = Index_5). Only election-night-window Wayback capture is 20180606114855 (4:48:55am PDT 6/6), which shows internal 'Website Updated: 6/6/2018 04:44:12 AM' and the page's own header 'UNOFFICIAL RESULTS - ELECTION NIGHT FINAL', Ballots Cast 406,501. The next capture (20180608031615, 6/7 8:16pm PDT, ~37.5h later) shows a different internal timestamp (6/7/2018 5:15:43 PM) and a higher count (427,779), confirming 406,501 was the pre-canvass election-night figure, superseded only by a later canvass update. CONFIRMED (self-description + later-capture-growth legs). 406,501/673,640 certified = 60.34%. Pre-epollbook (2022) and pre-ASV (2024)."
}
```

---

## 2016-06-07 presidential-primary (CONFIRMED plateau — the lead flagged by the 2016 general's own note)

The existing `san-diego-ca.json` note for the 2016 GENERAL explicitly flags:
"Wayback captured election.xml only for the June 2016 primary." This chases
that lead. Pre-livevoterturnout era: SD served a GEMS-style detailed-results
XML at `sdvote.com/content/rov/electioninfo/election.xml` (JS viewer
consumed it; the XML itself is plain-text and curl-fetchable with no
rendering needed).

CDX for `election.xml`, June 2016: exactly ONE capture inside the
election-night-adjacent window, `20160608190823` (archived 2016-06-08 12:08:23
PM PDT); the next captures are 12+ days later (6/20, 6/24, 6/29 — all
different digests, i.e. content kept changing = ongoing canvass). Fetched
directly via curl (`.../web/20160608190823id_/http://www.sdvote.com/content/rov/electioninfo/election.xml`,
plain XML, no puppeteer needed):

```xml
<ELECTION date="06-08-16" time="03:21:51" ... title2="PRESIDENTIAL PRIMARY ELECTION"
   title3="Tuesday, June 7, 2016" etype="UNOFFICIAL" ToBeCnt="285000" ...>
<SUMMARY reported="1726" total="1726">
...
<CONTEST title="UNITED STATES SENATOR" tcounted="468340" tblank="47700" reporting="1726" numprec="1726" pctrpt="100.0" ...>
```

- The internal report timestamp is `06-08-16 03:21:51` — i.e. 3:21:51 AM the
  morning after the June 7 election, the same overnight-report pattern seen
  in every other SD row in this dataset (12:39am 2022, 12:46am 2024, 4:44am
  2018-primary, 4:48am 2018-general). `etype="UNOFFICIAL"`.
- The archived capture was taken at 12:08pm PDT the SAME day (6/8) yet still
  serves the 3:21:51am-generated data verbatim — i.e. the live page itself
  had not updated in the ~9 hours between the overnight report and the
  midday capture, consistent with a paused/plateaued count (leg: page
  frozen across an intraday span).
- `UNITED STATES SENATOR` is CA's nonpartisan top-two blanket-primary
  contest — every registered voter votes on it regardless of party, making
  its `tcounted` the best available proxy for total countywide ballots
  counted at that time (the presidential races are party-restricted and
  undercount DTS/cross-party voters). `tcounted="468340"` recurs identically
  across ~15 other universal contests in the same file (Prop 50, judicial
  races, etc.), confirming it is a genuine snapshot-wide ballot total, not a
  per-contest artifact.
- Growth leg: the next available capture (`20160620034049`, internal date
  `06-16-16 16:10:26`) shows `ToBeCnt` dropped to 83,000 and US SENATOR
  `tcounted` risen to 689,612 — i.e. the count grew substantially between
  the 6/8 election-night snapshot and the 6/16 canvass update, confirming
  468,340 was NOT yet the settled/certified total (RUNBOOK 8's "later
  capture of the same report series showing growth" leg). CONFIRMED.
- Sanity check against the certified final: 468,340 counted + 285,000
  ToBeCnt (the page's own outstanding-ballot estimate) = 753,340, within
  ~3% of the certified final 775,930 — a plausible relationship for an
  election-night projection.
- Arithmetic: 468,340 / 775,930 certified = **60.36%**
  (468340/775930*100 = 60.3585...).
- `vs_epollbook`: pre (2022 adoption). `vs_asv`: pre (2024 adoption).
- `source_url_night`:
  `https://web.archive.org/web/20160608190823/http://www.sdvote.com/content/rov/electioninfo/election.xml`
- Draft row (type `presidential-primary`):
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 468340,
  "certified_final": 775930,
  "election_night_pct": 60.36,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20160608190823/http://www.sdvote.com/content/rov/electioninfo/election.xml",
  "confidence": "primary",
  "note": "PLATEAU metric, recovered from the lead flagged in the 2016 GENERAL row's own note ('Wayback captured election.xml only for the June 2016 primary'). Pre-livevoterturnout era GEMS-style XML at sdvote.com/content/rov/electioninfo/election.xml (plain text, curl-fetched, no rendering needed). Only election-night-adjacent Wayback capture is 20160608190823 (archived 6/8/2016 12:08pm PDT), whose internal ELECTION header reads date=06-08-16 time=03:21:51 etype=UNOFFICIAL ToBeCnt=285000 -- a 3:21am overnight report, matching the overnight-report pattern of every other SD row in this dataset. UNITED STATES SENATOR (CA's nonpartisan top-two blanket-primary contest, open to all voters regardless of party) shows tcounted=468340, a figure that recurs identically across ~15 other universal contests in the same file, confirming it is a genuine countywide ballot snapshot. Two corroborating legs: (a) the capture (12:08pm) is ~9h after the internal report time (3:21am) yet shows the SAME data, i.e. the live page had not updated in that intraday span (plateau evidence); (b) the next available capture (20160620034049, internal date 06-16-16 16:10:26) shows ToBeCnt fallen to 83,000 and US SENATOR tcounted risen to 689,612 -- i.e. the count grew substantially by the next capture, proving 468,340 was the pre-canvass election-night figure, not the settled total. CONFIRMED. Sanity check: 468,340 + ToBeCnt 285,000 = 753,340, within ~3% of the certified final 775,930. 468,340/775,930 certified = 60.36%. Pre-epollbook (2022) and pre-ASV (2024)."
}
```

---

## 2012-06-05 presidential-primary and 2014-06-03 statewide-primary — NULL (numerator not sourceable)

Both primaries checked fresh against every route in RUNBOOK.md 6.2-6.6,
specifically for the June dates (not assuming the generals' dead ends carry
over):

- **election.xml feed** (the route that worked for 2016): CDX
  `sdvote.com/content/rov/electioninfo/election.xml` for the full window
  2010-01-01 to 2016-01-01 returns ZERO captures. The feed simply was not
  archived by Wayback until 2016. Dead end for both years.
- **sdvote.com domain sweep**, tight windows around each primary
  (2012-06-04 to 06-08; 2014-06-02 to 06-06): 2012 shows only `robots.txt`
  captured (2012-06-05); essentially nothing else crawled. 2014 shows a
  handful of PRE-election static pages/PDFs (voter-registration forms,
  candidate list PDF `0614candlist.pdf` captured 2014-06-06 — a candidate
  roster, not results) under the legacy `voters/Eng/...` URL structure (a
  different, older site layout than the `content/rov/...` structure used
  from ~2016 on) — no live-results page, no ballots-counted figure, in
  either window.
- **County News Center** (`countynewscenter.com`, the registrar's press
  outlet, launched ~2014 per the 2014-general row's note): CDX for
  2014-06-01 to 06-15 finds exactly one page,
  "election-tuesday-do-you-know-where-vote" (2014-06-05, a pre-election
  "where to vote" reminder), NOT a results announcement. For 2012, County
  News Center did not exist yet (per the 2012-general row's note). No
  morning-after "semi-final results" release found for either year.
- **Registrar's own news page** (`sdvote.com/content/rov/en/elections/news.html`):
  per the existing generals' notes, archived only from 2019 onward — the
  same constraint applies to these primary dates.
- No local-news numeric ballots-counted figure was found for either
  election-night window in the sources already checked for the generals
  (Times of San Diego, KPBS archives referenced in the existing JSON gave no
  precise totals for these years either); a fresh targeted news search was
  not run beyond the County News Center check above given the exhausted
  official-source routes, consistent with runbook 5.1's null-with-documented-search
  standard.

Per RUNBOOK 5.1, both rows are `null`/`null`/confidence `"none"`/
`source_url_night: null` rather than substituting a different report time or
denominator.

Draft rows:
```json
[
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 548462,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final (denominator) SOLID: CA SoS SoV Voter Participation Statistics by County (filename literally '03-voter-reg-stats-by-county.pdf' despite containing the participation table -- do not confuse with the true registration-stats '02-...' file in the same dir), San Diego Total Voters 548,462 (Precinct 187,942 + VBM 360,520). Election-night NUMERATOR not sourceable, checked fresh for the June date (not just inherited from the Nov-2012 general's dead end): (1) the sdvote.com/content/rov/electioninfo/election.xml feed that recovered the 2016 primary's plateau has ZERO Wayback captures anywhere 2010-2016 -- not archived until 2016; (2) a sdvote.com domain sweep for 2012-06-04 to 06-08 shows only robots.txt captured, no results page; (3) County News Center did not exist yet in 2012 (per the 2012-general row); (4) the registrar's own news page is archived only from 2019 on. No morning-after 'semi-final results' release or precise news figure found. Left null per RUNBOOK 5.1 rather than substitute a different report-time or denominator. Pre-epollbook (2022) and pre-ASV (2024)."
},
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 420700,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final (denominator) SOLID: CA SoS SoV Voter Participation Statistics by County, San Diego Total Voters 420,700 (Precinct 113,714 + VBM 306,986). Election-night NUMERATOR not sourceable, checked fresh for the June date: (1) the sdvote.com/content/rov/electioninfo/election.xml feed (the route that recovered 2016) has ZERO Wayback captures anywhere 2010-2016; (2) a sdvote.com domain sweep for 2014-06-02 to 06-06 shows only PRE-election static pages/PDFs (voter-reg forms, a candidate-list PDF captured 6/6) under the legacy voters/Eng/... URL structure, no live-results page or ballots-counted figure; (3) County News Center (existed by 2014) shows exactly one election-adjacent page in the window, a pre-election 'where to vote' reminder (2014-06-05), not a results release; (4) the registrar's own news page is archived only from 2019 on. No morning-after 'semi-final results' release or precise news figure found. Left null per RUNBOOK 5.1 rather than substitute a different report-time or denominator. Pre-epollbook (2022) and pre-ASV (2024)."
}
]
```

---

## Draft VERIFY.md addition (San Diego primaries table + detail bullets)

Matches the existing San Diego section's format (`data/research/election-night/VERIFY.md`
lines 627-663) so it can be appended directly under that county's existing
generals section if/when the JSON rows are committed.

```markdown
| Year | Type | Night ballots | Certified final | Share | Conf. | Numerator source (open & check) |
|---|---|---:|---:|---:|---|---|
| 2012p | presidential-primary | — | 548,462 | — | none | — (not sourceable) |
| 2014p | statewide-primary | — | 420,700 | — | none | — (not sourceable) |
| 2016p | presidential-primary | 468,340 | 775,930 | 60.4% | primary | [link](https://web.archive.org/web/20160608190823/http://www.sdvote.com/content/rov/electioninfo/election.xml) |
| 2018p | statewide-primary | 406,501 | 673,640 | 60.3% | primary | [link](https://web.archive.org/web/20180606114855/http://www.livevoterturnout.com/SanDiego/LiveResults/en/Index_3.html) |
| 2022p | statewide-primary | 416,748 | 674,608 | 61.8% | primary | [link](https://web.archive.org/web/20220608181901/https://www.livevoterturnout.com/ENR/sandiegocaenr/15/en/Index_15.html) |
| 2024p | presidential-primary | 425,572 | 704,068 | 60.4% | primary | [link](https://web.archive.org/web/20240306103630/https://www.livevoterturnout.com/ENR/sandiegocaenr/19/en/Index_19.html) |
```

Detail bullets (one per row, "look for" text = the row's `note` field
verbatim, truncated here for readability — use the full note from the JSON
draft above when committing):

- **2012p presidential-primary** — night `—` / final `548,462` = `—` (none)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf>
  - look for: election.xml feed has zero Wayback captures 2010-2016; sdvote.com domain sweep 2012-06-04/08 shows only robots.txt; County News Center did not exist yet in 2012; registrar's news page archived only from 2019. No release/news figure found. Null per RUNBOOK 5.1.
- **2014p statewide-primary** — night `—` / final `420,700` = `—` (none)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf>
  - look for: election.xml feed has zero Wayback captures 2010-2016; sdvote.com domain sweep 2014-06-02/06 shows only pre-election static pages (legacy voters/Eng/... structure); County News Center shows only a pre-election "where to vote" page, not a results release. Null per RUNBOOK 5.1.
- **2016p presidential-primary** — night `468,340` / final `775,930` = `60.4%` (primary)
  - numerator: <https://web.archive.org/web/20160608190823/http://www.sdvote.com/content/rov/electioninfo/election.xml>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf>
  - look for: GEMS-style XML, internal header `date="06-08-16" time="03:21:51" etype="UNOFFICIAL" ToBeCnt="285000"`; UNITED STATES SENATOR contest (nonpartisan blanket-primary, universal turnout proxy) `tcounted="468340"`, recurring identically across ~15 universal contests. Next capture (6/16 internal date) shows growth to 689,612 / ToBeCnt 83,000, confirming 468,340 was election night, not final.
- **2018p statewide-primary** — night `406,501` / final `673,640` = `60.3%` (primary)
  - numerator: <https://web.archive.org/web/20180606114855/http://www.livevoterturnout.com/SanDiego/LiveResults/en/Index_3.html>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: page header "UNOFFICIAL RESULTS - ELECTION NIGHT FINAL", internal "Website Updated: 6/6/2018 04:44:12 AM", Ballots Cast 406,501. Next capture (6/7 5:15pm, ~37.5h later) shows a higher count (427,779), confirming 406,501 was the election-night figure.
- **2022p statewide-primary** — night `416,748` / final `674,608` = `61.8%` (primary)
  - numerator: <https://web.archive.org/web/20220608181901/https://www.livevoterturnout.com/ENR/sandiegocaenr/15/en/Index_15.html>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: internal "Website Updated: 6/8/2022 12:39:38 AM", Ballots Cast 416,748, "NEXT POST 6/9/22 BY 5PM" still showing hours later with no update. Companion summary_15.xml (plain XML, 3 captures) shows the next report, GeneratedDate 2022-06-09T16:49:11-07:00, TotalBallotsCast 475,054, confirming 416,748 held through the night. ROLLOUT-TIMING: this is the FIRST election on SD's ENR/vote-center/e-pollbook platform per data/research/county-tech/san-diego-ca.json ("first_election": "2022-06") — vs_epollbook = post for this row.
- **2024p presidential-primary** — night `425,572` / final `704,068` = `60.4%` (primary)
  - numerator: <https://web.archive.org/web/20240306103630/https://www.livevoterturnout.com/ENR/sandiegocaenr/19/en/Index_19.html>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: page literally headers itself "FINAL UNOFFICIAL ELECTION NIGHT RESULTS", internal "Website Updated: 3/6/2024 12:46:42 AM", "NEXT UPDATE: MAR. 7", Ballots Counted 425,572; held across two more same-day captures (+14h); 3/8 capture confirms the promised Mar-7 canvass update landed at 492,333. FLAG for manual operator: vs_asv is ambiguous (county-tech record could not pin ASV's first election to March vs Nov 2024); defaulted to "post" to match the existing Nov-2024-general row's convention.

</details>
```

---

## Draft plateau_review.json entries

Matches the existing `data/research/election-night/plateau_review.json`
schema (list of `{slug, date, verdict, basis, evidence}` objects; existing
san-diego-ca entries for 2018/2022/2024-11 shown above as the format
reference).

```json
[
  {
    "slug": "san-diego-ca",
    "date": "2016-06-07",
    "verdict": "CONFIRMED",
    "basis": "self-describing night stamp (UNOFFICIAL, 03:21:51 AM internal time) plus growth in the next available capture",
    "evidence": "election.xml internal date=06-08-16 time=03:21:51 etype=UNOFFICIAL ToBeCnt=285000; US SENATOR tcounted=468340 (recurs across ~15 universal contests); captured 12:08pm PDT same day with no intervening update; next capture (internal date 06-16-16) shows tcounted risen to 689,612"
  },
  {
    "slug": "san-diego-ca",
    "date": "2018-06-05",
    "verdict": "CONFIRMED",
    "basis": "self-describing final header plus growth in the next capture",
    "evidence": "'UNOFFICIAL RESULTS - ELECTION NIGHT FINAL', stamp 6/6/2018 04:44:12 AM, Ballots Cast 406,501; next capture (6/7 5:15:43 PM) shows 427,779"
  },
  {
    "slug": "san-diego-ca",
    "date": "2022-06-07",
    "verdict": "CONFIRMED",
    "basis": "night stamp plus next-post schedule, corroborated by the companion XML feed's next report",
    "evidence": "stamp 6/8/2022 12:39:38 AM, Ballots Cast 416,748, 'NEXT POST 6/9/22 BY 5PM' still showing hours later; summary_15.xml next report GeneratedDate 2022-06-09T16:49:11-07:00 = 475,054"
  },
  {
    "slug": "san-diego-ca",
    "date": "2024-03-05",
    "verdict": "CONFIRMED",
    "basis": "self-describing final header, held across three captures spanning 14h, plus the promised next-update landing exactly on schedule",
    "evidence": "'FINAL UNOFFICIAL ELECTION NIGHT RESULTS ... NEXT UPDATE: MAR. 7', stamp 3/6/2024 12:46:42 AM, Ballots Counted 425,572 held 20240306103630/145646/223911; 3/8 capture shows stamp 3/7/2024 4:48:18 PM, 492,333"
  }
]
```

(2012-06-05 and 2014-06-03 have no sourced numerator, so no plateau_review
entry is drafted for them per the runbook's "verdict per SOURCED row" rule.)
