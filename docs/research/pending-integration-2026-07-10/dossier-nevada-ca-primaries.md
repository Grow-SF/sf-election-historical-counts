# Nevada County (nevada-ca) — statewide PRIMARY election-night dossier

Read-only research scout output. Nothing in this file has been written to the
repo. `data/research/election-night/nevada-ca.json` today only carries the six
November GENERALS (2012, 2014, 2016, 2018, 2022, 2024); this dossier covers
the companion six statewide PRIMARIES (2012-06-05, 2014-06-03, 2016-06-07,
2018-06-05, 2022-06-07, 2024-03-05).

Adoption (per `data/research/county-tech/nevada-ca.json`): e-pollbook
`adopted_year: 2018`, `first_election: "2018-06"` (the county's first VCA
election, the June 5 2018 Statewide Direct Primary — CONFIRMED, primary
source: county VCA Overview page + 2017 EAP). ASV `adopted_year: 2022`,
`first_election: ""` (UNCONFIRMED which 2022 election — the tech record
explicitly calls `adopted_year=2022` "a DOCUMENTED LOWER BOUND, not a
confirmed first-election year" and flags "the machine could date back to the
2018 VCA all-mail transition or a later sorter acquisition"). This dossier
investigates the June-vs-November-2022 question directly (see the 2022-06-07
item below) since it determines `vs_asv` for that row and for 2018/2024.

Per RUNBOOK 5.3, YubaNet articles carry `confidence: "primary"` in this
county's existing general-election rows (a maintainer-left-open convention,
not to be "fixed" here) when they republish the county's own official
release verbatim; this dossier follows the same convention for primary rows
sourced the same way, and calls out any row where the YubaNet article is NOT
a verbatim republication (pure news reportage) as `secondary` instead.

## Denominators (CA SoS Statement of Vote, "Voter Participation Statistics by County")

All six already cached in scratch (`sov20{12,14,16,18,22,24}primary.txt`,
fetched by a concurrent county-primary research pass sharing this scratch
dir) and independently re-verified here by grep against Nevada County's row.
`certified_final` = the **Total Voters** column (Precinct + VBM).

| Date | SoV URL | Nevada County row (as printed) | Total Voters |
|---|---|---|---:|
| 2012-06-05 | https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf | `Nevada 74 76,426 60,590 6,408 24,925 31,333 79.55% 51.71% 41.00%` | **31,333** |
| 2014-06-03 | https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf (misspelling intact, per runbook 6.1) | `Nevada 71 76,711 61,711 5,270 22,326 27,596 80.90% 44.72% 35.97%` | **27,596** |
| 2016-06-07 | https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf (no `sov/` sub-segment) | `Nevada 80 77,440 66,149 10,572 34,595 45,167 76.59% 68.28% 58.33%` | **45,167** |
| 2018-06-05 | https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf | `Nevada 39 78,420 68,126 1,761 37,031 38,792 95.46% 56.94% 49.47%` | **38,792** |
| 2022-06-07 | https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf | `Nevada* 78 82,123 75,406 1,932 36,058 37,990 94.91% 50.38% 46.26%` | **37,990** |
| 2024-03-05 | https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf | `Nevada* 108 81,498 74,137 2,740 36,839 39,579 93.08% 53.39% 48.56%` | **39,579** |

(`*` = VCA-county footnote in the SoS table for 2022/2024, consistent with
Nevada being an original VCA county.)

---

## Per-election items

(appended below, one at a time, as numerator research completes)

### 2024-03-05 — presidential-primary

**Certified final:** 39,579 (SoV `Total Voters`, see denominators table). URL:
`https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf`.

**Plateau:** 21,753 ballots, the county's own **Third Report - Cumulative
Results**, run 12:00:06 AM 03/06/2024 (i.e. just past midnight election
night, per RUNBOOK 1's "1am-4am next morning is still election night"
convention — this is even earlier, 12:00 AM). Source:
`https://nevadacountyca.gov/DocumentCenter/View/52637/Cumulative-Results-3-6-2024-12-00-06-AM`
(fetched directly, HTTP 200; header block: "March 5, 2024 Presidential
Primary / Unofficial Results / Registered Voters 21753 of 74201 = 29.32% /
Precincts Reporting 108 of 108 = 100.00% / Run Time 12:00 AM / Run Date
03/06/2024"). NOTE the header mislabels the ballots-counted figure
"Registered Voters" (the RUNBOOK 7.5 Sacramento/Napa 2018 gotcha) — 21,753 is
ballots counted, not registered voters (registered voters = 74,201 per the
same header, matching the SoV's Registered Voters column order of
magnitude).

**Full election-night sequence, all three reports fetched and read directly:**
- First Report: `DocumentCenter/View/52632/...` — Run Time 8:22 PM 03/05/2024,
  19,830 ballots (26.72%). This is the 8pm-ish first tranche, NOT the plateau.
- Second Report: `DocumentCenter/View/52634/Cumulative-Results-3-5-2024-10-11-27-PM`
  — Run Time 10:11 PM 03/05/2024, 20,942 ballots (28.22%).
- Third Report: `DocumentCenter/View/52637/Cumulative-Results-3-6-2024-12-00-06-AM`
  — Run Time 12:00 AM 03/06/2024, **21,753 ballots (29.32%)** = the plateau.
- Each cumulative report is bracketed by a companion "District Results
  Report - March 05, 2024" run within minutes (8:23 PM, 10:18 PM, 12:00 AM
  respectively per each PDF's own header) — the county's report-generation
  cadence itself.

**Corroboration (independent leg, satisfies RUNBOOK section 8 CONFIRMED):**
YubaNet "Voter turnout on par with previous elections" (published 2024-03-06)
states verbatim: "The first results of the night (19,830 ballots) were
vote-by-mail ballots received before the weekend and early voting at the
vote centers... After three reports, 21,753 of 74,201 ballots issued to
Nevada County voters had been tabulated and election night was over." This
matches the county's own PDF numbers exactly (19,830 first tranche, 21,753
after three reports) and explicitly states election night ended after the
third report. YubaNet further confirms the canvass resumed on a Tuesday/
Friday posting cadence starting Thursday March 7 (a >24h gap from the
12:00 AM third report), which is the "county's own posting schedule
bracketing the report" leg per RUNBOOK 8. URL:
`https://yubanet.com/regional/voter-turnout-on-par-with-previous-elections/`.

**Arithmetic:** 21,753 / 39,579 = **54.96%** (21753/39579 = 0.549557...).
Reconciles: 21,753 (election night) + 17,826 (canvass, weekend/Election-Day
drop-off VBM + late signature-verified ballots) = 39,579 certified.

**vs_epollbook:** post (adopted 2018, this is 2024). **vs_asv:** post
(adopted_year 2022 per county-tech record; 2024 postdates 2022 regardless of
the June-vs-November-2022 ambiguity investigated below).

**Draft row (section 2 schema):**
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 21753,
  "certified_final": 39579,
  "election_night_pct": 54.96,
  "vs_epollbook": "post",
  "vs_asv": "post",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://nevadacountyca.gov/DocumentCenter/View/52637/Cumulative-Results-3-6-2024-12-00-06-AM",
  "confidence": "primary",
  "note": "PLATEAU = 21,753, the county's own THIRD/LAST 'Cumulative Results Report' of election night (Run Time 12:00 AM 03/06/2024, 108 of 108 precincts = 100%). Full sequence: First Report 8:22 PM = 19,830 (View/52632); Second Report 10:11 PM = 20,942 (View/52634); Third/LAST Report 12:00 AM = 21,753 (View/52637), header mislabeled 'Registered Voters 21753 of 74201' (RUNBOOK 7.5 mislabel gotcha; 21,753 is ballots counted). Corroborated verbatim by YubaNet 'Voter turnout on par with previous elections' (2024-03-06): 'After three reports, 21,753 of 74,201 ballots issued to Nevada County voters had been tabulated and election night was over.' Canvass resumed on a Tue/Fri posting cadence starting Thu March 7 (county's own posting-schedule gap, RUNBOOK 8 second leg). NOT the 19,830 first tranche. Arithmetic: 21,753/39,579 = 54.96%. Certified final = Total Voters 39,579, CA SoS SoV Voter Participation Statistics by County (VCA-county footnote). Post-e-pollbook (adopted 2018), post-ASV (adopted 2022, and 2024 postdates 2022 under either June/Nov reading)."
}
```

**VERIFY.md draft line:** `| 2024-03-05 | presidential-primary | 21,753 | 39,579 | 54.96% | primary | [First](https://nevadacountyca.gov/DocumentCenter/View/52632/) / [Second](https://nevadacountyca.gov/DocumentCenter/View/52634/) / [Third/LAST](https://nevadacountyca.gov/DocumentCenter/View/52637/Cumulative-Results-3-6-2024-12-00-06-AM) Cumulative Results Report |`

**Plateau verdict: CONFIRMED.** Self-describes as the third of three
election-night reports (past-midnight internal timestamp) AND has an
independent leg (county's own posting-schedule gap to the Thu canvass restart,
corroborated by an independent YubaNet account matching both the first-tranche
and plateau figures exactly).

---

### 2018-06-05 — statewide-primary (VCA/e-pollbook ROLLOUT election)

**Certified final:** 38,792 (SoV `Total Voters`). URL:
`https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf`.

**Plateau:** 16,346 ballots, the county's own **"Cumulative Report -
Unofficial - Official Ballot Statewide Direct Primary Election - June 05,
2018"**, PDF header "Total Number of Voters: 16,346 of 68,023 = 24.03%",
"Precincts Reporting 39 of 39 = 100.00%", internal document timestamp
06/05/2018 11:06 PM. Source: YubaNet's live-blog "Nevada County June 2018
Primary Election - live updates and results"
(`https://yubanet.com/regional/june-2018-primary/`) posted this exact PDF at
its **"June 5, 2018 at 11:23 PM"** entry captioned **"The final update for
election night"**:
`https://yubanet.com/wp-content/uploads/2018/06/finalelectionnightupdate.pdf`.
This is a scanned/image PDF (Canon iR-ADV printer output, no text layer;
`pdfinfo` CreationDate/ModDate = Tue Jun 5 23:11:26 / 23:23:14 2018 PDT,
matching the article's 11:23 PM posting); read directly by rendering page 1
to PNG (150dpi) and transcribing the header/footer by eye — no OCR needed for
the header line. Per-contest cross-check: the Governor race on the same page
shows Cast Votes 16,113 + Over Votes 67 + Under Votes 166 = 16,346, exactly
matching the page-header total — internally consistent.

**Not the first tranche:** the same live-blog's earlier 10:43 PM entry (after
"Election day votes have been added ... with the exception of Truckee and
North San Juan") shows the Sheriff race at 14,975 cast votes, and the 8pm-ish
first VBM-only dump would be lower still (Absentee column alone = 13,522,
constant across all updates that night, i.e. the pre-processed VBM dump).
16,346 is the LAST, 100%-precincts total.

**Corroboration (independent leg):** the morning-after YubaNet article "At
least 14,000 ballots remain to be counted in Nevada County" (2018-06-06)
states the next substantive update would come "probably by late Monday or
maybe Tuesday" — a multi-day gap from the Tuesday-night 11:06/11:23 PM
report, satisfying RUNBOOK 8's "county's own posting schedule bracketing the
report" leg. URL:
`https://yubanet.com/regional/at-least-14000-ballots-remain-to-be-counted-in-nevada-county/`.

**Arithmetic:** 16,346 / 38,792 = **42.14%** (16346/38792 = 0.421376...).
Reconciles: 16,346 (election night) + 22,446 (canvass over the following
weeks) = 38,792 certified.

**vs_epollbook:** post — THIS IS THE ROLLOUT ELECTION. Per
`data/research/county-tech/nevada-ca.json`, e-pollbook `adopted_year: 2018`,
`first_election: "2018-06"` (the county's first VCA election; e-pollbooks
were deployed at all vote centers from day one of VCA, per the county's 2017
Election Administration Plan). No "pre" primary exists for e-pollbook within
this dataset's 2012-2024 window; 2018-06-05 is the earliest "post" row.
**vs_asv:** pre (matches the existing general-election 2018-11-06 row's
convention; no ASV evidence before the documented 2022 lower bound, and the
2017 EAP — which predates this election — does not mention a
signature-verification sorter).

**Draft row (section 2 schema):**
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 16346,
  "certified_final": 38792,
  "election_night_pct": 42.14,
  "vs_epollbook": "post",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://yubanet.com/wp-content/uploads/2018/06/finalelectionnightupdate.pdf",
  "confidence": "primary",
  "note": "PLATEAU = 16,346, the county's own 'Cumulative Report - Unofficial' for the June 5, 2018 primary, internal timestamp 11:06 PM, Precincts Reporting 39 of 39 = 100.00%. Posted by YubaNet's live-blog (yubanet.com/regional/june-2018-primary/) at its 11:23 PM entry captioned 'The final update for election night'. Scanned/image PDF (Canon printer output); read by rendering to PNG and transcribing the header directly (Total Number of Voters: 16,346 of 68,023 = 24.03%). Per-contest cross-check on the same page: Governor race Cast 16,113 + Over 67 + Under 166 = 16,346, internally consistent. NOT the first tranche: the 10:43 PM entry in the same live-blog shows a still-rising Sheriff-race count (14,975 cast) with the Absentee/VBM column frozen at 13,522 across all updates. Morning-after YubaNet ('At least 14,000 ballots remain to be counted in Nevada County', 2018-06-06) confirms the next update was not expected until 'late Monday or maybe Tuesday' -- a multi-day posting-schedule gap (RUNBOOK 8 second leg). Arithmetic: 16,346/38,792 = 42.14%. Certified final = Total Voters 38,792, CA SoS SoV Voter Participation Statistics by County. THIS IS THE E-POLLBOOK ROLLOUT ELECTION (first VCA election, adopted_year 2018, first_election 2018-06 per county-tech record) -- vs_epollbook = post (no pre-adoption primary exists in this dataset's window). Pre-ASV (no signature-verification-sorter evidence before the documented 2022 lower bound; matches the general 2018-11-06 row's pre-ASV classification)."
}
```

**VERIFY.md draft line:** `| 2018-06-05 ⚠️rollout | statewide-primary | 16,346 | 38,792 | 42.14% | primary | [Final election-night PDF](https://yubanet.com/wp-content/uploads/2018/06/finalelectionnightupdate.pdf) via [live-blog](https://yubanet.com/regional/june-2018-primary/) |`
(⚠️ marker here is informational — flags "rollout election," NOT `comparable: false`; this row IS comparable, it is simply the first post-adoption data point.)

**Plateau verdict: CONFIRMED.** Self-describes as "the final update for
election night" with 100% precincts reporting and a document-internal
11:06 PM timestamp, PLUS an independent leg (the multi-day gap to the next
update, stated explicitly in a separate morning-after article) and an
internal-consistency cross-check (per-contest arithmetic sums exactly to the
header total).

---

### 2022-06-07 — statewide-primary (June-vs-November-2022 ASV question)

**MAJOR FLAG BEFORE THE ROW — read this first.** The task brief asks "which
2022 election was ASV's first — the June/November distinction matters for
vs_asv." Researching that question surfaced primary-source evidence that may
supersede the premise entirely: **Nevada County Board of Supervisors File
#SR 16-0825**, adopted 9/27/2016, is a "Resolution approving and authorizing
the Nevada County Clerk-Recorder/Registrar of Voters to execute an agreement
with Election Systems & Software, LLC (ES&S) for the purchase of a **Mail
Ballot Signature Verification Machine (MBV 1000)**" for "not to exceed
$69,969" (trading in the prior "Vote Remote" hardware for a credit not to
exceed $7,500), budgeted to the Clerk-Recorder/Elections FY2016/17 budget.
URL: `https://nevco.legistar.com/LegislationDetail.aspx?GUID=F2AD1997-3E3E-4C30-80F7-21F54318ADDF&ID=2840587`.
ES&S's own marketing material describes its "Mail Ballot Verifier (MBV)"
line as a machine that "fully automates the process of verifying and sorting
mailed ballots" (`https://www.essvote.com/blog/video/video-mail-ballot-verifier/`)
— i.e. algorithmic auto-accept/auto-reject, the same functional description
(auto-accept some signatures, route the rest to human review) that
`data/research/county-tech/nevada-ca.json`'s current ASV record uses to
establish `adopted_year: 2022` from the county's Mail Ballot Processing
Infographic. **If the MBV 1000 purchased in Sept 2016 is the same lineage of
machine (or a predecessor performing the same automated function) still
referenced in the 2022/2023 infographic, Nevada County's true ASV adoption
year could be 2016 or 2017 — six to seven years earlier than the currently
documented 2022 lower bound, and predating EVERY row in both this primaries
dossier and the county's existing general-election dataset except 2012-11
and 2014-11.** This was not independently confirmed within this pass (no
2016/2017 news coverage of the MBV 1000's debut was found, and no
Legistar record was found documenting its replacement/retirement); it needs
the same Legistar-anchored follow-up the existing tech record already calls
for ("Flag for verification: pin the sorter purchase year and vendor via
board agendas / Legistar" — SR 16-0825 appears to be exactly that record).
**FLAG for manual operator: verify whether the MBV 1000 (SR 16-0825, 2016) is
the automated signature-verification system described in the county's Mail
Ballot Processing Infographic, and if so, revise `adopted_year` in
`data/research/county-tech/nevada-ca.json` and `vs_asv` across the entire
county dataset (both this dossier's draft rows and the existing six
general-election rows) accordingly.**

No independent evidence was found this pass to distinguish June vs November
2022 specifically (no news or county document from June 2022 mentions the
signature-verification sorter by name, unlike the county's November 2022
infographic-adjacent materials). **Pending the flag above, this draft row
uses the CURRENT documented record's `adopted_year: 2022` at the calendar-year
grain (consistent with the existing Nov 2022 general row's `vs_asv: "post"`)
— i.e. `"post"` — but this classification should be treated as provisional,
not final,** per the flag.

**Certified final:** 37,990 (SoV `Total Voters`). URL:
`https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf`.

**Plateau:** 17,574 ballots, the county's own **"Cumulative Results Report,"
Run Time 10:11 PM, 06/07/2022**, Polling Places Reporting 17 of 19 = 89.47%.
Source:
`https://nevadacountyca.gov/DocumentCenter/View/44131/Cumulative-Results-6-7-2022-10-11-05-PM`
(fetched directly, HTTP 200; header: "JUNE 7, 2022 STATEWIDE DIRECT PRIMARY
... Registered Voters 17574 of 75368 = 23.32%" — the RUNBOOK 7.5 mislabel
again: 17,574 is ballots counted, not registered voters). No further
DocumentCenter ID between 44132 and 44142 resolves (all 404), confirming no
later election-night report was posted.

**Full election-night sequence:**
- First Report: `DocumentCenter/View/44126/...` — Run Time 8:02 PM, 16,092
  ballots (21.35%), 8 of 19 polling places (42.11%). NOT the plateau.
- Second/LAST Report: `DocumentCenter/View/44131/Cumulative-Results-6-7-2022-10-11-05-PM`
  — Run Time 10:11 PM, **17,574 ballots (23.32%)**, 17 of 19 polling places
  (89.47%) = the plateau. (Only 2 polling places never reported election
  night; this is still the last report actually posted that night, matching
  the metric's definition — "last report posted," not "100% precincts.")

**Corroboration (independent leg):** YubaNet's live-blog "2022 Primary
Election in Nevada County" (`https://yubanet.com/regional/2022-primary-election-in-nevada-county/`)
states, at its "June 7, 2022 at 10:22 PM" entry, "17,574 ballots have been
counted out of 75,368 registered voters" (matching the county PDF exactly),
followed immediately (in publish order) by a "June 7, 2022 at 11:22 PM" entry
reading, verbatim: **"This was the final report for Election night. The
official canvass starts on Thursday, June 9, 2022."** The same live-blog's
next entry is dated **June 10, 2022 at 3:10 PM** and reports "20,222 votes
have now been counted" — a different, higher number three days later,
independently proving 17,574 was frozen through the election-night-to-canvass
gap (RUNBOOK 8's "later capture of the same series showing the count moved"
leg, applied here as "held-then-moved" rather than "held unchanged").

**Arithmetic:** 17,574 / 37,990 = **46.26%** (17574/37990 = 0.462543...).

**vs_epollbook:** post (adopted 2018, well before this election). **vs_asv:**
post, PROVISIONALLY, per the current documented record — see the FLAG above;
this call should be revisited once SR 16-0825 is checked against the
infographic's machine.

**Draft row (section 2 schema):**
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 17574,
  "certified_final": 37990,
  "election_night_pct": 46.26,
  "vs_epollbook": "post",
  "vs_asv": "post",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://nevadacountyca.gov/DocumentCenter/View/44131/Cumulative-Results-6-7-2022-10-11-05-PM",
  "confidence": "primary",
  "note": "PLATEAU = 17,574, the county's own SECOND/LAST 'Cumulative Results Report' of election night (Run Time 10:11 PM 06/07/2022, 17 of 19 polling places = 89.47%; no later DocumentCenter ID resolves). First Report 8:02 PM = 16,092 (View/44126), NOT the plateau. Corroborated verbatim by YubaNet's live-blog: 10:22 PM entry '17,574 ballots have been counted out of 75,368 registered voters', followed by an 11:22 PM entry stating 'This was the final report for Election night. The official canvass starts on Thursday, June 9, 2022.' A June 10 update (3 days later) shows 20,222 -- a different, higher figure proving 17,574 held through the gap. Arithmetic: 17,574/37,990 = 46.26%. Certified final = Total Voters 37,990, CA SoS SoV Voter Participation Statistics by County (VCA-county footnote). Post-e-pollbook (adopted 2018). vs_asv=post is PROVISIONAL, following the current documented adopted_year=2022 at calendar-year grain (no independent June-vs-November evidence found this pass) -- FLAGGED: Nevada County BOS File #SR 16-0825 (adopted 9/27/2016) approved purchase of an ES&S 'Mail Ballot Signature Verification Machine (MBV 1000)', which ES&S's own materials describe as fully automating mail-ballot signature verification and sorting; if this is the machine (or a predecessor of the machine) described in the county's Mail Ballot Processing Infographic that currently anchors adopted_year=2022, the true ASV adoption year could be 2016-2017, which would flip vs_asv to 'post' for this row AND for every other row in the county's dataset back through at least 2016-11 (possibly 2014-11). Needs Legistar-anchored follow-up before this classification is treated as final; see the dossier's dedicated flag section for the full citation."
}
```

**VERIFY.md draft line:** `| 2022-06-07 ⚠️asv-provisional | statewide-primary | 17,574 | 37,990 | 46.26% | primary | [Second/LAST Cumulative Results Report](https://nevadacountyca.gov/DocumentCenter/View/44131/Cumulative-Results-6-7-2022-10-11-05-PM) |`

**Plateau verdict (numerator): CONFIRMED.** Self-describes via the live-blog
as "the final report for Election night" (paired with the county's own PDF,
last of only two reports that night) PLUS an independent leg (a distinctly
different, higher count 3 days later proves the number was frozen through the
gap). **vs_asv classification: UNRESOLVED / FLAGGED**, not a plateau
question — see the flag above.

---

### 2016-06-07 — presidential-primary (SECOND MAJOR FLAG: e-pollbooks in use here, two years before the documented 2018 rollout)

**MAJOR FLAG — read before the row.** Nevada County Clerk-Recorder Gregory J.
Diaz published an official statement on election day itself, "Greg Diaz:
Despite E-Poll book glitch, your vote will be counted"
(`https://yubanet.com/regional/greg-diaz-despite-e-poll-book-glitch-your-vote-will-be-counted/`,
Wayback capture `20160609140926`, article `Published on Jun 7, 2016 -
7:35:42 PM`), stating verbatim: **"At our polling places this morning, some
voters did not appear on our electronic rosters (E-Poll Books) when our poll
workers entered their first and last names in the E-Poll Book... Overall,
less than 9% of voters had any blank field show."** This is unambiguous,
primary-source, same-day evidence that Nevada County was using electronic
poll books at physical polling places in the **June 7, 2016** primary — TWO
YEARS before `data/research/county-tech/nevada-ca.json`'s currently
documented `adopted_year: 2018` / `first_election: "2018-06"` (which ties
e-pollbook adoption exclusively to the VCA vote-center rollout). This
directly contradicts the current record and, if confirmed, would also
require re-examining the existing GENERAL-election dataset's 2016-11-08 row
(currently `vs_epollbook: "pre"`) and possibly 2014. **FLAG for manual
operator: reconcile this June 2016 Diaz statement against the county-tech
e-pollbook record; the pre-VCA/pre-2018 system may have been a
different-but-still-electronic pollbook technology (traditional polling-place
e-pollbooks predate VCA vote-center e-pollbooks nationally), which would mean
`adopted_year: 2018` is really "VCA-model vote-center e-pollbook adoption,"
a narrower category than "any e-pollbook," and the tech record's `type:
"epollbook"` definition may need to be split or re-scoped.**

One partial mitigation: this same finding also HELPS resolve the ASV
question. Nevada County BOS File #SR 16-0825 (the MBV 1000
signature-verification-machine purchase, flagged above under 2022-06-07) was
adopted **9/27/2016** — i.e. AFTER this June 7, 2016 primary. So regardless
of how the e-pollbook flag above is resolved, **this row's `vs_asv: "pre"` is
solid**: the MBV 1000 could not have been in service for an election three
and a half months before its purchase was even approved.

**Certified final:** 45,167 (SoV `Total Voters`). URL:
`https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf`.
Independently cross-checked: the county's own certified "Cumulative Report —
Official" (`https://www.nevadacountyca.gov/DocumentCenter/View/13365/June-2016-Cumulative-Report-PDF`,
Run Date/Time 07/01/2016 08:57 AM, Precincts Reporting 80 of 80 = 100.00%)
states "Total Number of Voters: 45,167 of 66,178 = 68.25%" — matches the SoV
figure exactly.

**Numerator — FLOOR, not a confirmed plateau.** 25,353 ballots, from the
county's own **"Cumulative Report — Unofficial,"** internal Run Date/Time
06/07/2016 10:52 PM, Precincts Reporting 36 of 80 = 45.00%. Source: YubaNet's
live-blog "Live: Nevada County June Election Results"
(`https://yubanet.com/m/nevada-county-06-results/`, Wayback capture
`20160609143131`) linked this PDF at its "June 7, 2016 at 11:16 PM" entry
("36 out of 80 precincts have now reported. Here is the complete pdf file
with the latest results"):
`https://web.archive.org/web/20160625203409id_/http://yubanet.com/m/wp-content/uploads/2016/06/results11pm.pdf`.
**This is NOT the plateau** — the SAME live-blog's next entry, "June 7, 2016
at 11:46 PM," states verbatim: **"Final results for the night. 80 out of 80
precincts have been tabulated."** — a materially later, 100%-precinct report
whose exact countywide ballot total was never independently archived (no
"final" PDF was crawled by Wayback; only per-contest tallies survive in the
blog's own text, e.g. county-wide Measure W: Yes 11,585 + No 15,845 = 27,430
cast votes, up from 24,979 at the 36-of-80 point — a ~9.8% increase,
suggesting (NOT confirming) a true final countywide ballot total in the
high-20-thousands). Per RUNBOOK 5.2, 25,353 is kept as a documented **FLOOR**:
confidence `secondary`, explicitly below the true election-night plateau.

**Arithmetic (floor):** 25,353 / 45,167 = **56.13%** (floor; the true
election-night share is HIGHER than this, plausibly around 60-62% by the
Measure W scaling above, but that scaling is not itself sourced to a
countywide total and is not used as the recorded numerator).

**vs_epollbook:** pre, PROVISIONALLY, per the current documented record
(`adopted_year: 2018`) — see the FLAG above; the Diaz statement is strong
contrary evidence. **vs_asv:** pre (solid; MBV 1000 purchase postdates this
election by 3.5 months).

**Draft row (section 2 schema):**
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 25353,
  "certified_final": 45167,
  "election_night_pct": 56.13,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20160625203409id_/http://yubanet.com/m/wp-content/uploads/2016/06/results11pm.pdf",
  "confidence": "secondary",
  "note": "FLOOR, not plateau = 25,353, the county's own 'Cumulative Report - Unofficial', internal Run Date/Time 06/07/2016 10:52 PM, Precincts Reporting 36 of 80 = 45.00%. Linked by YubaNet's live-blog (yubanet.com/m/nevada-county-06-results/) at its 11:16 PM entry. NOT the plateau: the SAME live-blog's 11:46 PM entry states verbatim 'Final results for the night. 80 out of 80 precincts have been tabulated,' a materially later 100%-precinct report whose exact countywide total was never independently archived (no final PDF crawled by Wayback; only per-contest totals survive in blog text -- county-wide Measure W scaled from 24,979 to 27,430 cast votes, a ~9.8% rise, between the two points). Per RUNBOOK 5.2 kept as a documented FLOOR (secondary confidence, comparable=false) rather than null, since a real election-night report with an exact number does survive, just not the true final one. Arithmetic (floor): 25,353/45,167 = 56.13%; true election-night share is higher. Certified final = Total Voters 45,167, CA SoS SoV, independently cross-checked against the county's own certified 'Cumulative Report - Official' (DocumentCenter/View/13365, Run 07/01/2016, 100% precincts) which states the identical 45,167 figure. vs_epollbook=pre is PROVISIONAL per the current adopted_year=2018 record -- FLAGGED: Nevada County Clerk-Recorder Gregory Diaz's own election-day statement ('Despite E-Poll book glitch, your vote will be counted', published 2016-06-07) describes electronic poll books ('E-Poll Books') in use at Nevada County polling places on THIS election, two years before the documented 2018 VCA rollout; needs reconciliation with the county-tech record (possibly a narrower VCA-vote-center-e-pollbook vs a broader traditional-polling-place-e-pollbook distinction). vs_asv=pre is solid: BOS File SR 16-0825 (MBV 1000 signature verification machine purchase) was adopted 9/27/2016, 3.5 months AFTER this election."
}
```

**VERIFY.md draft line (no ⚠️ marker — per the established Napa-2014-floor
precedent, floors are NOT marked `comparable: false` and get no ⚠️, unlike
ceilings):** `| 2016-06-07 | presidential-primary | 25,353 | 45,167 | 56.13% | secondary | [10:52 PM Cumulative Report - Unofficial](https://web.archive.org/web/20160625203409id_/http://yubanet.com/m/wp-content/uploads/2016/06/results11pm.pdf) via [live-blog](https://yubanet.com/m/nevada-county-06-results/) |`
(the e-pollbook flag above should still be surfaced to the operator
separately, outside the table.)

**Plateau verdict: REFUTED_AS_PLATEAU (kept as documented FLOOR, matching the
Napa 2014 precedent exactly).** The live-blog's own text proves a later,
100%-precinct report existed ("Final results for the night. 80 out of 80
precincts have been tabulated") that is NOT the number recorded here; 25,353
is honestly a floor, not the plateau, per RUNBOOK 5.2's explicit floor/ceiling
provision — `comparable` stays unset (true/omitted), only `confidence:
"secondary"` signals the caveat, exactly as Napa's 2014 row does.

---

### 2014-06-03 — statewide-primary (NULL — no election-night report survives)

**Certified final:** 27,596 (SoV `Total Voters`). URL:
`https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf`.
Independently cross-checked: the county's own certified "Cumulative Report —
Official" (`https://www.nevadacountyca.gov/DocumentCenter/View/13301/June-2014-Official-Summary-Results-PDF`,
Run Date/Time 06/20/2014 02:31 PM, Precincts Reporting 71 of 71 = 100.00%)
states "Total Number of Voters: 27,596 of 61,909 = 44.58%" — matches the SoV
figure exactly.

**Numerator: NOT SOURCEABLE.** Searched and exhausted:
- Nevada County's own live "2013-2016 Historical Election Results" page
  (`https://www.nevadacountyca.gov/3695/2013---2016-Historical-Election-Results`,
  fetched directly with a browser user-agent after a bare `curl` 403'd)
  lists exactly one document for this election: `DocumentCenter/View/13301/
  June-2014-Official-Summary-Results-PDF` — the certified final (above), no
  interim/election-night report.
- Wayback CDX, `yubanet.com` domain-wide, `2014-06-03` to `2014-06-12`: 84
  captures, none an election-results article (all local non-election news;
  the closest hits, e.g. "Election results update for June 9" /
  "Election results update: 6,292 ballots remain to be counted", were
  checked and are CANVASS-period articles from later in June, matching the
  pattern established for this county's other pre-2016 primaries — no
  live-blog format existed yet for this county on YubaNet; that format first
  appears in this dossier's research at the 2016-06-07 primary
  (`yubanet.com/m/nevada-county-06-results/`), i.e. NOT retroactively
  available for 2014.
- No morning-after "semi-final results" press release format existed yet
  either (this predates the format seen from 2018 onward).
Per RUNBOOK 5.1, this row is null: no substituted denominator, no different
report time used.

**vs_epollbook:** pre. **vs_asv:** pre.

**Draft row (section 2 schema):**
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 27596,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Election-night PLATEAU not sourceable. Nevada County's own '2013-2016 Historical Election Results' page lists only the certified final (DocumentCenter/View/13301, Run 06/20/2014, 100% precincts, Total Number of Voters 27,596 of 61,909 = 44.58% -- matches SoV exactly); no interim/election-night report is hosted there. Wayback CDX (yubanet.com, domain-wide, 2014-06-03 to 2014-06-12, 84 captures) contains no election-results article for this primary -- the closest-titled hits ('Election results update for June 9', 'Election results update: 6,292 ballots remain to be counted') are later CANVASS-period articles, not election night. YubaNet's live-blog format for Nevada County elections (yubanet.com/m/<slug>-results/) first appears in this dossier's research at the 2016-06-07 primary; it was not in use for 2014. No morning-after semi-final press release format existed yet either (first seen from 2018 onward). Null per RUNBOOK 5.1: no substituted denominator, no different report time used. Certified final = Total Voters 27,596, CA SoS SoV (misspelling 'particpiation' intact in the URL, per runbook 6.1). Pre-e-pollbook, pre-ASV."
}
```

**VERIFY.md draft line:** `| 2014-06-03 | statewide-primary | — | 27,596 | — | none | — (not sourceable) |`

**Plateau verdict: N/A (null row).** No sourced numerator to verdict.

---

### 2012-06-05 — presidential-primary (NULL — no election-night report survives)

**Certified final:** 31,333 (SoV `Total Voters`). URL:
`https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf`.
Independently cross-checked: the county's own certified "Cumulative Report —
Official" (`https://www.nevadacountyca.gov/DocumentCenter/View/13316/June-2012-Official-Summary-Results-PDF`,
Run Date/Time 06/20/2012 08:39 AM, Precincts Reporting 74 of 74 = 100.00%)
states "Total Number of Voters: 31,333 of 60,638 = 51.67%" — matches the SoV
figure exactly.

**Numerator: NOT SOURCEABLE.** Searched and exhausted:
- Nevada County's own live "2009-2012 Historical Election Results" page
  (`https://nevadacountyca.gov/793/2009---2012-Historical-Election-Results`,
  fetched directly with a browser user-agent after a bare `curl` 403'd)
  lists exactly one document for this election:
  `DocumentCenter/View/13316/June-2012-Official-Summary-Results-PDF` — the
  certified final (above), no interim/election-night report.
- Wayback CDX, `yubanet.com` domain-wide, `2012-06-05` to `2012-06-30`: 229
  captures, none an election-night results article for the June primary; the
  only turnout-adjacent hit found,
  "Voter-Turnout-Inches-Above-50-in-Nevada-County---Updated-Results.php"
  (crawled 2012-06-16), is explicitly dated "June 13, 2012" in its own byline
  and reports a mid-CANVASS interim figure (30,529 ballots, 50.35% turnout,
  captioned "This update is not the final, official tally") — 8 days
  post-election, not election night.
- No YubaNet live-blog format or morning-after semi-final press release
  format existed yet for this county (both are later conventions, first
  seen 2016 and 2018 respectively in this dossier's research).
Per RUNBOOK 5.1, this row is null.

**vs_epollbook:** pre. **vs_asv:** pre.

**Draft row (section 2 schema):**
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 31333,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Election-night PLATEAU not sourceable. Nevada County's own '2009-2012 Historical Election Results' page lists only the certified final (DocumentCenter/View/13316, Run 06/20/2012, 100% precincts, Total Number of Voters 31,333 of 60,638 = 51.67% -- matches SoV exactly); no interim/election-night report is hosted there. Wayback CDX (yubanet.com, domain-wide, 2012-06-05 to 2012-06-30, 229 captures) contains no election-night results article; the only turnout-adjacent hit, 'Voter Turnout Inches Above 50% in Nevada County - Updated Results' (crawled 2012-06-16), is self-dated 'June 13, 2012' in its own byline and explicitly captioned 'This update is not the final, official tally' -- a mid-canvass interim figure (30,529 ballots, 50.35%) 8 days post-election, not election night. No YubaNet live-blog format (first appears 2016) or morning-after semi-final press-release format (first appears 2018) existed yet for this county. Null per RUNBOOK 5.1: no substituted denominator, no different report time used. Certified final = Total Voters 31,333, CA SoS SoV (2012 primary URL uses 'voter-reg-stats-by-county.pdf' not '...participation...', per runbook 6.1-style quirk). Pre-e-pollbook, pre-ASV."
}
```

**VERIFY.md draft line:** `| 2012-06-05 | presidential-primary | — | 31,333 | — | none | — (not sourceable) |`

**Plateau verdict: N/A (null row).** No sourced numerator to verdict.

---

## Consolidated summary

| Date | Type | Plateau ballots | Certified final | Share | Confidence | Evidence class |
|---|---|---:|---:|---:|---|---|
| 2012-06-05 | presidential-primary | — | 31,333 | — | none | null (only certified final survives) |
| 2014-06-03 | statewide-primary | — | 27,596 | — | none | null (only certified final survives) |
| 2016-06-07 | presidential-primary | 25,353 (floor) | 45,167 | 56.13% (floor) | secondary | floor (true final was 80/80 precincts, not archived) |
| 2018-06-05 | statewide-primary | 16,346 | 38,792 | 42.14% | primary | CONFIRMED plateau (rollout election) |
| 2022-06-07 | statewide-primary | 17,574 | 37,990 | 46.26% | primary | CONFIRMED plateau; vs_asv provisional (see flag) |
| 2024-03-05 | presidential-primary | 21,753 | 39,579 | 54.96% | primary | CONFIRMED plateau |

Denominators are SOLID for all six: every SoS SoV "Total Voters" figure was
independently cross-checked against the county's own archived certified
"Cumulative Report — Official" canvass PDF (2012/2014/2016) or is the same
report series used for the numerator (2018/2022/2024), and all six match
exactly. Comparable-primary series (2018/2022/2024, all CONFIRMED
plateaus): election-night share ran 42.14% (2018 rollout) -> 46.26% (2022) ->
54.96% (2024) — a rising trend across the VCA/e-pollbook era, opposite in
direction to the county's GENERAL-election series over the same span (which
DROPPED post-VCA: 61.1% in 2016 -> 49.0% in 2018 -> 56.1% in 2022 -> 24.5%
2024-comparable=false). Primaries in this county are lower-turnout, VBM-heavy
elections where a larger share of ballots typically arrives close to or on
election day itself; the exact mechanism for the primaries' rising trend
(more vote centers over time? faster VBM intake?) was not investigated
further in this pass — flagged as a possible follow-up, not asserted as a
tech effect, per RUNBOOK's confound-recording discipline.

## FLAGS for the operator (in priority order)

1. **[MAJOR] Nevada County BOS File #SR 16-0825 (adopted 9/27/2016):**
   purchase of an ES&S "Mail Ballot Signature Verification Machine (MBV
   1000)," described by ES&S's own materials as fully automating mail-ballot
   signature verification. This directly conflicts with
   `county_tech.json`'s current ASV `adopted_year: 2022` (documented only as
   a lower bound). **Action needed:** confirm via Legistar/board minutes
   whether the MBV 1000 is the machine (or an ancestor of the machine) later
   described in the county's 2022/2023 Mail Ballot Processing Infographic.
   If confirmed, `adopted_year` should move to 2016 or 2017, and `vs_asv`
   should flip to `"post"` for EVERY row in the county's dataset from
   2016-11-08 onward (both the existing six generals and this dossier's six
   primaries), except this dossier's 2016-06-07 row (which predates the
   Sept 2016 purchase and stays solidly `"pre"`).
   Citation: `https://nevco.legistar.com/LegislationDetail.aspx?GUID=F2AD1997-3E3E-4C30-80F7-21F54318ADDF&ID=2840587`.

2. **[MAJOR] Nevada County Clerk-Recorder Gregory Diaz's June 7, 2016
   statement** ("Despite E-Poll book glitch, your vote will be counted")
   describes "electronic rosters (E-Poll Books)" in use at Nevada County
   POLLING PLACES on election day, June 7, 2016 — two years before
   `county_tech.json`'s current e-pollbook `adopted_year: 2018` /
   `first_election: "2018-06"` (which is tied specifically to the VCA
   vote-center rollout). **Action needed:** determine whether this is the
   same "e-pollbook" category the tech record tracks, or a narrower
   traditional-polling-place system that predates and differs from the VCA
   vote-center e-pollbook system; the tracked `type: "epollbook"` schema may
   need a definitional refinement. If the pre-VCA system counts, `vs_epollbook`
   should flip to `"post"` for 2016-06-07, 2016-11-08 (existing general row),
   and possibly 2014.
   Citation: `https://yubanet.com/regional/greg-diaz-despite-e-poll-book-glitch-your-vote-will-be-counted/`
   (Wayback capture `20160609140926`).

3. **[MINOR] 2022-06-07's `vs_asv` classification is provisional**, following
   the current documented adopted_year=2022 at calendar-year grain; no
   independent June-vs-November-2022 evidence was found this pass beyond the
   flag #1 finding above (which, if confirmed, makes the June/November 2022
   question moot — both would already be "post" under a 2016/2017 adoption
   year).

4. **[MINOR] 2016-06-07's numerator is a documented FLOOR (25,353, secondary
   confidence), not a confirmed plateau.** The true election-night final (80
   of 80 precincts, per the live-blog's own text) was never independently
   archived. If the maintainer wants to pursue it further: try
   `https://web.archive.org/save/http://yubanet.com/m/nevada-county-06-results/`-style
   re-crawls are moot (event already passed), but a direct Claude-in-Chrome
   session against the Wayback UI (not curl) occasionally surfaces captures
   CDX/`id_` cannot serve (per RUNBOOK 7.1's replay-aliasing gotcha) — worth
   one try before accepting the floor as final. `FLAG for manual operator`
   if pursued.

5. **[MINOR, for context] 2012-06-05 and 2014-06-03 are genuine nulls,
   consistent with the same pattern already established for this county's
   pre-2016 elections and for other counties' pre-2016 primaries researched
   in parallel this session (e.g. Fresno's primaries dossier, same scratch
   dir).** No further action recommended; the search was exhaustive within
   this pass's tools (county DocumentCenter, Wayback CDX, WebSearch).

## Locating-query provenance (for reproducibility)

- SoS SoV primary PDFs: URL pattern per year established by a concurrent
  county-primary research pass in this same scratch dir (cross-confirmed via
  `grep` across `dossier-*-primaries.md`); Nevada County's row located via
  `grep -n -i nevada sov20{12,14,16,18,22,24}primary.txt`.
- County DocumentCenter numerator PDFs: located via `WebSearch` for
  `nevadacountyca.gov DocumentCenter "Cumulative Results" <date>`, then
  probed sequential DocumentCenter IDs around the found ID with `curl` to
  recover the full First/Second/Third-report sequence (2018, 2022, 2024) or
  confirm no later ID exists (2022's 44132-44142 all 404).
- YubaNet live-blogs/press releases: `WebSearch` for `yubanet <county>
  <date> primary election night ballots`, then `curl`/`WebFetch` the
  specific article; for 2012/2014/2016 (pre-dating easy web search
  indexing), Wayback CDX `matchType=domain` on `yubanet.com` with a
  ~1-3-week window around the election date, filtered client-side for
  election-relevant URL slugs.
- Legistar (BOS File SR 16-0825): `WebSearch` for `nevco.legistar.com Nevada
  County ballot sorter signature verification purchase 2021 2022` (a search
  aimed at 2021/2022 that serendipitously surfaced the 2016 record instead).
- Scanned/image PDFs (2018-06-05's finalelectionnightupdate.pdf): rendered
  to PNG via `pdftoppm -png -r 150` and read directly (vision), not OCR'd.
