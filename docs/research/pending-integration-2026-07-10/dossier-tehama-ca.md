# Tehama County (tehama-ca) — election-night evidence dossier

Control county for the researching-election-night-share dataset. Probe verdict
(archive-probes-m-y.md): **MARGINAL, thin Wayback** — not on Clarity (genuine
404), live site `co.tehama.ca.us` DNS-unresolvable from this probe environment
(identified historically as `co.tehama.ca.us/dep-elections`), Wayback captures
exist close to but not exactly on election night in both 2016 and 2018 windows
(2016: dep-elections landing 11-03/11-04/11-08 08:19 UTC [pre-results, early
election day]; a dedicated `election_results/Election Result_dtl.htm` page
captured 2016-11-07 22:05 UTC [day BEFORE the election]; 2018: dep-elections
captured 2018-11-07 15:01 and 2018-11-09 15:21 [day-after and 3-days-after]).
Press-release archive unknown (DNS failure blocked the live-site check). This
dossier extends that probe into full election-by-election evidence per
RUNBOOK.md.

Working notes: appending after each item per process rules (9). Tehama is not
on Clarity (confirmed dead end in the probe; route 6.4 skipped for all years
unless new evidence surfaces). Per the county-tech census row (status
"never", confidence "medium"), Tehama has never adopted e-pollbooks or ASV
through 2024, so vs_epollbook / vs_asv = "n/a" for every row (control county,
no tech transition to bracket).

**Contents (items appended out of numeric order; this is the reading map):**
- Item 0 (tech record) -- never-adopter, extends census row
- Item 1 (2012-11-06 presidential) -- **NULL**, weakest year (zero elections-related crawl at all)
- Item 2 (2014-11-04 midterm) -- **NULL**, canvass-complete value found and explicitly rejected as a ceiling
- Item 3 (2016-11-08 presidential) -- **NULL**, report was linked but never crawled by Wayback in time
- Item 4 (2018-11-06 midterm) -- **NULL**, same linked-but-uncrawled pattern as 2016
- Item 5 (2022-11-08 midterm) -- **SOURCED, CONFIRMED**: 11,878 / 20,819 = 57.06%
- Item 6 (2024-11-05 presidential) -- **SOURCED, CONFIRMED**: 13,109 / 26,867 = 48.79%

Overall picture: Tehama's website only became consistently Wayback-recoverable
for election-night detail once it migrated to a WordPress numbered-report
system (co.tehama.ca.us by 2022, tehama.gov by 2024); the older Joomla site
(2012-2018) reused report filenames across elections, so Wayback's crawl
cadence (which rarely hit the exact election-night window) recovered only
pre-election zero-reports or post-election reused-filename content, never
the actual plateau -- a clean methodological finding in its own right, not
just a string of failures.

---

## Item 0: tech record (never-adopter evidence)

Source: `data/research/county-tech/ca_adoption_census.json` (existing row,
read not redone) plus this pass extends the census row's own source list.
Draft record in the `data/research/county-tech/<slug>.json` schema (per the
`napa-ca.json` example: `jurisdiction`, `state`, `tech[]` with
`type`/`status`/`adopted_year`/`first_election`/`vendor`/`evidence_url`/`confidence`/`note`).

```json
{
  "jurisdiction": "Tehama County",
  "state": "CA",
  "tech": [
    {
      "type": "epollbook",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf",
      "confidence": "medium",
      "note": "NOT a VCA county (no vote-center/all-mail model, so no VCA-driven e-pollbook rollout). CA SoS voting-technology-by-county snapshots list Tehama e-pollbook status as 'Do not use' continuously across the May 2022, Sept 2024, and Oct 2025 editions (census row source); EAVS reports 'False' for e-pollbook use in all four editions checked by the census pass. No county document, grand jury report, or news story found describing an electronic roster pilot at any point through 2024. Consistent never-adopter signal."
    },
    {
      "type": "asv",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://krcrtv.com/news/local/tehama-county-clerk-process-of-distinguishing-voter-fraud",
      "confidence": "medium",
      "note": "Positive evidence of manual-only signature verification (not merely absence of evidence). KRCR News 7 feature quotes Tehama County Clerk Jennifer Vise describing a two-person, eyes-on visual comparison process ('We look for slants, loops, certain characteristics of a signature to make sure that it does not match'; 'two people compare the signatures on the ballots to signatures from the past records'); mismatches are referred to the DA's office. No software/scanner/automated matching tool named anywhere in the article. Confidence held at medium (single local-news source, no corroborating official county EAP or grand-jury document; census row already flagged this same gap) -- this pass did not find a second independent source and did not upgrade confidence."
    },
    {
      "type": "sign-scan-go",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://www.sos.ca.gov/voters-choice-act",
      "confidence": "secondary",
      "note": "Tehama is not a Voter's Choice Act county (not on the CA SoS VCA county list), so the AB 626 in-vote-center 'Sign-Scan-and-Go' mail-ballot verify+scan model, which is built on the VCA vote-center infrastructure, does not apply. Absence-of-evidence inference from non-VCA status, consistent with the epollbook finding above."
    },
    {
      "type": "vote-center",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://www.sos.ca.gov/voters-choice-act",
      "confidence": "primary",
      "note": "CA SoS Voter's Choice Act county list does not include Tehama (as of 2024/2025). Tehama continues to run traditional precinct-based polling places plus vote-by-mail rather than the VCA all-mail/vote-center model, consistent with the epollbook not-adopted finding (VCA adoption is the mechanism that drives e-pollbook rollout in most small CA counties)."
    }
  ],
  "metrics": [],
  "notes": "Item 0 of the Tehama election-night dossier (control county, no tech transition to bracket -- both epollbook and ASV are 'never' per the census row, so every election-night row in this dossier uses vs_epollbook/vs_asv = 'n/a'). This pass reused the census row's sources (KRCR ASV feature, SoS voting-tech-by-county 2025 PDF) and added the SoS VCA county-list page as evidence for vote-center/sign-scan-go non-adoption; no new primary source was located for epollbook/ASV beyond what the census already carries. Locating queries reused from census pass: '\"Tehama County\" elections vote by mail signature verification manual staff compare'; 'Tehama County elections office signature verification staff \"compare\" OR \"by eye\" OR \"visually\" scanner'. New query this pass: 'Tehama County California Voter\\'s Choice Act vote center' (confirmed via sos.ca.gov/voters-choice-act county list, Tehama absent)."
}
```

Metrics array left empty (out of scope for this pass; the deliverable is the
election-night dataset rows in Items 1-6, not the county-tech metrics[]
block). No file written to the repo; this JSON lives only in this dossier
per the read-only mandate.

---

## Item 6: 2024-11-05 presidential-general — SOURCED, CONFIRMED

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2024 general.
URL: `https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf`
County line as printed (pdftotext -layout, row 58): `Tehama  40  46,304  37,488  4,426  22,441  26,867  83.53%  71.67%  58.02%`
(columns: Precincts 40, Eligible-to-Register 46,304, Registered Voters
37,488, Precinct Voters 4,426, Vote-By-Mail Voters 22,441, **Total Voters
26,867**, %VBM 83.53%, Turnout/Registered 71.67%, Turnout/Eligible 58.02%).
Certified final = **26,867**.

**Election-night numerator:** found directly on the live county site
(no Wayback needed) via URL-pattern guessing off a report-series discovered
by web search (a search for `"Tehama County Elections Department" "second
unofficial" 2024` surfaced `https://www.tehama.gov/wp-content/uploads/2024/11/1st-Unoffical-Report.pdf`
in the result list). Probed the full report series on the live tehama.gov
WordPress uploads directory (each fetch 2s apart):
- `.../2024/11/1st-Unoffical-Report.pdf` -> 200, internal header
  `11/5/2024 9:50:38 PM`, "1st Unofficial Report", Precincts Reported 23 of
  40 (57.50%), Voters Cast 11,182 of 37,488 (29.83%). This is the FIRST
  TRANCHE, not the plateau.
- `.../2024/11/2nd-Unoffical-Report.pdf` -> 200, internal header
  `11/5/2024 11:26:29 PM`, "2nd Unofficial Report", Precincts Reported 37 of
  40 (92.50%), Voters Cast 12,823 of 37,488 (34.21%).
- `.../2024/11/3rd-Unoffical-Report.pdf` -> 200, internal header
  `11/6/2024 12:17:11 AM`, "3rd Unofficial Report", **Precincts Reported 40
  of 40 (100.00%)**, **Voters Cast 13,109 of 37,488 (34.97%)**.
- `.../2024/11/4th-Unoffical-Report.pdf`, `5th-...`, `6th-...`,
  `Final-Unoffical-Report.pdf`, `Certified-Results.pdf`,
  `Certified-Report.pdf`, `Final-Report.pdf`, `Semi-Final-Report.pdf`, and
  several `<Nth>-Unofficial-Report-<date>.pdf` date-suffixed variants (the
  suffix pattern used by the 2026-06 primary's later reports, checked as a
  template guess) -> all 404. No report after the 3rd exists on election
  night.
- `.../2024/12/Final-Official-Report.pdf` -> 200, internal header
  `12/3/2024 10:26:46 AM`, "Final Official Report", **Voters Cast 26,867 of
  37,488 (71.67%)** -- exactly the certified final from the SoS SoV. This
  is the CANVASS-COMPLETE report, 27 days after the election, not the
  plateau; it is cited here only as the bracket proof.
- The live "Election Results" page (`https://www.tehama.gov/government/departments/elections/election-results/`)
  no longer links any 2024 files (it now lists only the live 2026-06
  primary's reports), confirming the county's CMS serves only the latest
  election's report list; the 2024 PDFs are still hosted at their original
  URLs (found by direct guess) even though unlinked.

**Plateau identification:** the 3rd Unofficial Report (13,109 ballots,
100.00% of 40 precincts, internal timestamp 12:17:11 AM the morning after
Election Day) is the last election-night report. Evidence it is the
plateau (RUNBOOK 8, CONFIRMED tier): (1) self-describes as end-of-night --
generated 12:17 a.m., all 40/40 precincts at 100%, no higher-numbered
report exists; (2) the report series' next file is the Final Official
Report dated 12/3/2024, a **27-day gap**, with no 4th/5th/Final-Unofficial
file interposed anywhere in that window (all probed and 404) -- the
county's own posting schedule brackets it (no report between night-of and
the canvass-complete Dec 3 file).

**Arithmetic:** 13,109 / 26,867 = **48.79%** (48.792...%, rounds to 48.79).

**Calibration note:** this is markedly LOWER than the runbook's rural-county
expectation of 80-95% and below SF's 51-71% presidential range. Explanation
consistent with Tehama's own data: the county is heavily VBM (83.53% VBM
share in 2024 per the SoV line above), and the 3rd Unofficial Report was
generated only ~4 hours after polls closed (8 p.m. -> 12:17 a.m.) with "all
40 precincts reporting" referring to PRECINCT (in-person) reporting, not
VBM processing -- the Final Official Report's 26,867 includes 22,441 VBM
ballots (83.5% of the final total), most of which (drop-box returns,
late-arriving mail) had not yet been opened/verified by 12:17 a.m. This
matches the pattern seen in Fresno 2024 (VERIFY.md: 62.36% plateau, also
gated by VBM-heavy processing) -- not a red flag, a genuine feature of
VBM-heavy small counties without VCA vote-center same-day processing.

**Row draft (per RUNBOOK section 2 schema):**
```json
{
  "date": "2024-11-05",
  "type": "presidential-general",
  "election_night_ballots": 13109,
  "certified_final": 26867,
  "election_night_pct": 48.79,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://www.tehama.gov/wp-content/uploads/2024/11/3rd-Unoffical-Report.pdf",
  "confidence": "primary",
  "note": "Election-night PLATEAU = 13,109 ballots ('Voters Cast: 13,109 of 37,488 (34.97%)', 'Precincts Reported: 40 of 40 (100.00%)'), from Tehama County's official 'Election Summary Report' internally timestamped 11/6/2024 12:17:11 AM -- the '3rd Unofficial Report', the LAST election-night update (all 40 precincts at 100%). Recovered directly from the live tehama.gov WordPress uploads directory (no Wayback needed): .../wp-content/uploads/2024/11/3rd-Unoffical-Report.pdf (sic, county's own filename misspells 'Unofficial'). This is the night's plateau, NOT the 8pm/9:50pm first tranche (1st Unofficial Report, 9:50:38 PM, 11,182 ballots, 57.50% precincts) and NOT the 2nd Unofficial Report (11:26:29 PM, 12,823 ballots, 92.50% precincts): the 3rd is the first (and last) report to reach 100% of precincts. It HELD through the rest of election night and the following weeks: no 4th/5th/Final-Unofficial report exists at any guessed URL (all 404), and the next report found on the county site is the Final Official Report dated 12/3/2024 10:26:46 AM (Voters Cast 26,867 of 37,488, exactly the certified final) -- a 27-day gap with nothing interposed, i.e. the county's own posting schedule brackets the 3rd Unofficial as the last night-of report. Arithmetic: 13,109 / 26,867 = 48.79%. Pre/post tech: n/a, Tehama never adopted e-pollbooks or ASV (control county, county-tech census row status 'never'). PRIMARY (official county Election Summary Report PDF, fetched live, not via Wayback). Calibration: 48.79% reads low vs. the runbook's small-rural-county 80-95% expectation and vs SF's 51-71% presidential range; explained by Tehama's VBM-heavy composition (83.53% VBM of the certified final per the same SoV line) and the report's precinct-centric 100% framing -- 'all precincts reporting' at 12:17 a.m. describes in-person precinct tabulation, not VBM/drop-box processing, most of which (the ~14k-ballot gap to certified) is canvassed over the following month. Not a first-tranche mistake: this IS the last report of the night, verified by the county's own report-numbering scheme and the absence of any later election-night file."
}
```

**VERIFY.md draft (summary row):**
`| 2024 | presidential-general | 13,109 | 26,867 | 48.8% | primary | [link](https://www.tehama.gov/wp-content/uploads/2024/11/3rd-Unoffical-Report.pdf) |`

**VERIFY.md draft (detail bullet):**
- **2024 presidential-general** -- night `13,109` / final `26,867` = `48.79%` (primary)
  - numerator: <https://www.tehama.gov/wp-content/uploads/2024/11/3rd-Unoffical-Report.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "3rd Unofficial Report", header "11/6/2024 12:17:11 AM", "Precincts Reported: 40 of 40 (100.00%)", "Voters Cast: 13,109 of 37,488 (34.97%)".

**plateau_review.json draft:**
```json
{
  "slug": "tehama-ca",
  "date": "2024-11-05",
  "verdict": "CONFIRMED",
  "basis": "self-describes as end-of-night (3rd of 3 Unofficial Reports, 100.00% precincts, 12:17:11 AM internal timestamp) PLUS the county's own posting schedule brackets it: no 4th/5th/Final-Unofficial file exists anywhere (all guessed URLs 404), and the next file in the series (Final Official Report) is dated 27 days later (12/3/2024) with Voters Cast exactly equal to the certified final (26,867).",
  "evidence": ["https://www.tehama.gov/wp-content/uploads/2024/11/3rd-Unoffical-Report.pdf", "https://www.tehama.gov/wp-content/uploads/2024/12/Final-Official-Report.pdf"]
}
```

---

## Item 1: 2012-11-06 presidential-general — NULL (documented dead end)

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2012 general (note: 2012 drops the
`sov/` path segment per RUNBOOK 6.1).
URL: `https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf`
County line as printed (pdftotext -layout, row 57): `Tehama  46  43,306  31,174  8,032  15,229  23,261  65.47%  74.62%  53.71%`
(Precincts 46, Eligible-to-Register 43,306, Registered Voters 31,174,
Precinct Voters 8,032, VBM Voters 15,229, **Total Voters 23,261**, %VBM
65.47%, Turnout/Registered 74.62%, Turnout/Eligible 53.71%). Certified
final = **23,261**.

**Election-night numerator: not sourceable. Every route tried:**
1. *Registrar press release / local news (6.2, 6.6):* WebSearch (multiple
   phrasings) for 2012 election-night coverage from Corning Observer / Red
   Bluff Daily News found nothing 2012-dated; only the recurring 2020
   article and generic county-page results.
2. *County's dated report series / any elections page (6.3, 6.5):* a
   full-domain CDX sweep of co.tehama.ca.us for **2012-10-25 through
   2012-12-15** (widened well past the election to catch any late-crawled
   report) returned only 31 total URLs for the entire domain in that
   7-week window, of which **zero** contain "elect", "result", or
   "unoffic" anywhere in the path -- the domain simply was not crawled for
   any elections content whatsoever around this election (the only 2012
   captures found anywhere on the domain, in an earlier broader sweep, were
   a pre-election "General Election Calendar8-6.pdf" filed under
   `clerk_pdf/November62012/`, crawled 2012-09-05, and a stray 404'd
   personnel PDF -- both irrelevant to results). This is a harder dead end
   than 2016/2018: there isn't even a near-miss linked-but-uncrawled report
   filename to document, because no page discussing results was crawled at
   all in this window.
3. *Election_Result_dtl.htm (the 2014-era frozen page):* does not exist
   yet for 2012 (its earliest capture is 2014-11-04); not applicable.
4. *Clarity (6.4):* skipped per probe (confirmed 404).

**Conclusion:** the weakest-evidenced year in this dossier -- not just a
missed report, but a complete absence of any elections-related crawl in
the entire pre/post-election window. Per RUNBOOK 5.1, documented null.

**Row draft:**
```json
{
  "date": "2012-11-06",
  "type": "presidential-general",
  "election_night_ballots": null,
  "certified_final": 23261,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 23,261 ballots cast (CA SoS SoV; precinct 8,032 + VBM 15,229; 74.62% of 31,174 registered). Election-night PLATEAU not sourceable. A full-domain Wayback CDX sweep of co.tehama.ca.us for 2012-10-25 through 2012-12-15 (31 total URLs crawled domain-wide in that 7-week window) found zero pages with 'elect'/'result'/'unoffic' in the path -- the county's website was not crawled for any elections-related content around this election at all (the only 2012-adjacent captures anywhere on the domain are a pre-election calendar PDF crawled 2012-09-05 and an unrelated 404). No local news election-night figure found (WebSearch, multiple phrasings). Not on Clarity. This is the weakest-evidenced year in the dossier: not a near-miss (unlike 2016/2018, where a report was linked but never crawled), but a total absence of any elections crawl. Null per RUNBOOK 5.1. vs_epollbook/vs_asv n/a (control county, never adopted)."
}
```

**VERIFY.md draft (summary row):**
`| 2012 | presidential-general | — | 23,261 | — | none | — (not sourceable) |`

**VERIFY.md draft (detail bullet):**
- **2012 presidential-general** -- night `—` / final `23,261` = `—` (none)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf>
  - look for: Certified final 23,261 ballots cast. Election-night PLATEAU not sourceable: no elections-related page on co.tehama.ca.us was crawled by Wayback anywhere in the Oct 25-Dec 15 2012 window (verified by full-domain CDX sweep).

---

## Item 2: 2014-11-04 midterm-general — NULL (documented dead end)

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2014 general (note: 2014 uses the
misspelled path `pdf/03-voter-particpiation-stats-by-county.pdf`, per
RUNBOOK 6.1).
URL: `https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf`
County line as printed (pdftotext -layout, row 57): `Tehama  46  43,727  30,169  4,527  11,264  15,791  71.33%  52.34%  36.11%`
(Precincts 46, Eligible-to-Register 43,727, Registered Voters 30,169,
Precinct Voters 4,527, VBM Voters 11,264, **Total Voters 15,791**, %VBM
71.33%, Turnout/Registered 52.34%, Turnout/Eligible 36.11%). Certified
final = **15,791**.

**Election-night numerator: not sourceable as a plateau (a canvass-complete
value was found and explicitly rejected). Every route tried:**
1. *Dedicated results-detail page (6.3/6.5), the strongest lead in this
   dossier:* `election_results/Election Result_dtl.htm` is THE 2014
   results page (this is the same URL later found frozen through 2021,
   see Items 3-4). Its FULL capture history was pulled and every capture
   fetched:
   - `20141104172500` (Nov 4, 2014, 9:25 AM PST -- Election Day MORNING,
     before poll close): internal stamp "Last Updated: October 17, 2014
     9:42 AM", every contest shows `0 / 46 precincts, 0.00%` -- a
     pre-election zero-report template, not live data.
   - **No capture exists between Nov 4 and Jan 19, 2015** (CDX queried
     tightly for `20141104`-`20141116` and `20141116`-`20150119`; both
     empty except the two endpoints already known) -- Wayback's crawler
     missed the entire election night AND the following 10 weeks of
     canvass.
   - `20150119173119` (Jan 19, 2015, 2.5 months after the election):
     internal stamp **"Last Updated: November 13, 2014 2:36 PM"**,
     `46/46 precincts, 100.00%`, **Total 15,791 (52.33%)** -- this exactly
     equals the CERTIFIED FINAL from the SoS SoV (15,791). This is the
     CANVASS-COMPLETE state as of Nov 13 (9 days post-election), not the
     election-night plateau; the page was then frozen (digest unchanged)
     from this capture through 2021 and was never updated for 2016 or 2018
     (see Items 3-4).
   - **Explicit rejection of this value as a RUNBOOK 5.2 ceiling:** a
     post-night ceiling is normally usable with `comparable: false` when it
     "slightly" overstates the plateau -- but here the Nov 13 value is
     numerically IDENTICAL to the certified final (100.00% match), so
     recording it as `election_night_ballots` would compute a meaningless
     `election_night_pct` of exactly 100.00%, actively misrepresenting the
     row as "the county counted everything on election night," the
     opposite of what a ceiling is supposed to communicate. Judged not
     defensible per RUNBOOK 5.2's "prefer whichever the note can defend";
     null is the honest call here, not a 100% ceiling.
2. *County's numbered report series (6.3):* as documented in Items 3-4,
   the Joomla `images/`-directory Unofficial Report filenames are reused
   across elections; no First/Second/Third/etc. filename specific to
   Nov 2014 was found referenced from any 2014 page capture, and the
   `dep-elections` page's one Nov 4 8:18 PM PST capture (right at poll
   close) carries no results link at all (only site navigation).
3. *Local news (6.6):* WebSearch (multiple phrasings) for 2014
   election-night coverage returned nothing 2014-dated.
4. *Clarity (6.4):* skipped per probe (confirmed 404).

**Conclusion:** the closest this dossier comes to a usable non-plateau
number, but it fails the ceiling test (RUNBOOK 5.2) by being identical to
the final rather than merely close to it. Documented null per RUNBOOK 5.1.

**Row draft:**
```json
{
  "date": "2014-11-04",
  "type": "midterm-general",
  "election_night_ballots": null,
  "certified_final": 15791,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 15,791 ballots cast (CA SoS SoV; precinct 4,527 + VBM 11,264; 52.34% of 30,169 registered). Election-night PLATEAU not sourceable. The county's dedicated 'Election Result_dtl.htm' results page (later found frozen through 2021, see tehama-ca 2016/2018 notes) has only two captures bracketing this election: 2014-11-04 9:25 AM PST (pre-poll-close, internal stamp 'Last Updated: October 17, 2014', all contests 0/46 precincts 0.00%) and 2015-01-19 (2.5 months later, internal stamp 'Last Updated: November 13, 2014 2:36 PM', 46/46 precincts 100.00%, Total 15,791/52.33% -- EXACTLY the certified final). No capture exists in between (CDX-checked tightly, both Nov4-Nov16 and Nov16-Jan19 windows empty). The Nov 13 value was explicitly considered and REJECTED as a RUNBOOK 5.2 ceiling: because it numerically equals the certified final exactly, recording it would produce a fabricated-looking 100.00% election-night share, which misrepresents rather than bounds the true plateau -- not defensible as 'slightly overstates'. No numbered Unofficial Report filename specific to Nov 2014 was found linked from any contemporaneous page capture (the dep-elections page's one poll-close-time capture, Nov 4 8:18 PM PST, carries no results link at all). No local news figure found. Not on Clarity. Null per RUNBOOK 5.1: never substitute a different report time or a value indistinguishable from the final. vs_epollbook/vs_asv n/a (control county, never adopted)."
}
```

**VERIFY.md draft (summary row):**
`| 2014 | midterm-general | — | 15,791 | — | none | — (not sourceable) |`

**VERIFY.md draft (detail bullet):**
- **2014 midterm-general** -- night `—` / final `15,791` = `—` (none)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf>
  - look for: Certified final 15,791 ballots cast. Election-night PLATEAU not sourceable: the only surviving post-poll-close capture of the county's results page (Jan 19, 2015) carries an internal 'Last Updated: November 13, 2014' stamp already equal to the certified final -- rejected as a ceiling because it equals rather than bounds the final (see note).

---

## Item 3: 2016-11-08 presidential-general — NULL (documented dead end)

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2016 general.
URL: `https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf`
County line as printed (pdftotext -layout, row 58): `Tehama  46  43,753  32,555  7,489  17,052  24,541  69.48%  75.38%  56.09%`
(Precincts 46, Eligible-to-Register 43,753, Registered Voters 32,555,
Precinct Voters 7,489, VBM Voters 17,052, **Total Voters 24,541**, %VBM
69.48%, Turnout/Registered 75.38%, Turnout/Eligible 56.09%). Certified
final = **24,541**.

**Election-night numerator: not sourceable. Every route tried:**
1. *Registrar press release / local news (6.2, 6.6):* WebSearch for 2016
   election-night coverage (Corning Observer, Red Bluff Daily News)
   returned no 2016-dated article; the same 2020 article resurfaces every
   time.
2. *County's dated report series (6.3):* the co.tehama.ca.us `/elections`
   page was fetched at every Wayback capture surrounding the election
   (2016-11-04 17:51 UTC, 2016-11-05 04:21/04:22 UTC [i.e. Nov 4, ~8:21 PM
   PST, right after poll close], 2016-11-08 08:19 UTC [Nov 8 12:19 AM PST,
   still PRE-Election-Day -- Nov 8 was the election], 2016-11-13 05:31 UTC
   [Nov 12, 9:31 PM PST, 4 days after]). The page's single "Election
   Summary Report" link target changes over these captures: at Nov 4/5 and
   Nov 8 08:19 it points to `images/images/Elections/November_2016_Zero_Proof_Report.pdf`
   (a pre-election zero report); by Nov 13 it points to
   `images/images/Elections/Fifth_Unofficial_Report.pdf`. **No capture
   exists of this page in the gap between Nov 8 08:19 UTC (pre-poll-close)
   and Nov 13** -- i.e. Wayback never crawled the page while it was linking
   to the actual election-night report (First through however-many
   Unofficial Reports were posted the night of Nov 8-9). Probed CDX
   directly for `images/images/Elections/{First,Second,Third,Fourth,Sixth}_Unofficial_Report.pdf`
   -- all zero captures ever; `Fifth_Unofficial_Report.pdf` (the one link
   we do have) has its earliest capture dated **2018-09-03**, nearly two
   years after the 2016 election -- this is the same reused-Joomla-filename
   problem documented for 2018 (confirmed by the Fifth report's own
   sibling filename recurring with a 2024-06 capture elsewhere): the file
   at this URL had already been overwritten by a later election's Fifth
   report by the time Wayback finally crawled it, so it cannot be cited as
   2016 data even though the link existed on the Nov 13 2016 page.
3. *Dedicated results-detail page:* as documented in Item 4 (2018) above,
   `election_results/Election Result_dtl.htm` is frozen on 2014 data from
   2015-01-19 onward; its 2016-11-07 22:05 UTC capture (flagged by the
   archive probe as "day before the election") is a `warc/revisit` of that
   same frozen 2014 digest, not live 2016 content. Dead end, same finding
   as 2018.
4. *Clarity (6.4):* skipped per probe (confirmed 404).

**Conclusion:** no on-night report survives at any checked route (the
closest miss in this whole dossier: the link existed and was posted, but
Wayback's crawl cadence missed the exact election-night window and only
picked up the reused filename years later showing different content). Per
RUNBOOK 5.1, documented null.

**Row draft:**
```json
{
  "date": "2016-11-08",
  "type": "presidential-general",
  "election_night_ballots": null,
  "certified_final": 24541,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 24,541 ballots cast (CA SoS SoV; precinct 7,489 + VBM 17,052; 75.38% of 32,555 registered). Election-night PLATEAU not sourceable. The co.tehama.ca.us '/elections' page's single 'Election Summary Report' link points to a pre-election Zero Proof Report at every capture through 2016-11-08 08:19 UTC (still pre-Election-Day) and has jumped to a 'Fifth_Unofficial_Report.pdf' link by the next capture, 2016-11-13 -- Wayback never crawled the page during the gap when it would have linked the actual election-night report(s). Direct CDX probes of images/images/Elections/{First,Second,Third,Fourth,Sixth}_Unofficial_Report.pdf found zero captures ever; the one linked filename we do have (Fifth_Unofficial_Report.pdf) was first crawled 2018-09-03, almost two years later, on a Joomla directory confirmed (Item 4 note) to silently overwrite report filenames across elections -- that 2018 capture reflects a later election's Fifth report, not 2016's, and is not citable as 2016 data. The dedicated Election_Result_dtl.htm page is frozen on 2014 data throughout this window (see Item 4). No local news election-night figure found. Not on Clarity. Null per RUNBOOK 5.1. vs_epollbook/vs_asv n/a (control county, never adopted)."
}
```

**VERIFY.md draft (summary row):**
`| 2016 | presidential-general | — | 24,541 | — | none | — (not sourceable) |`

**VERIFY.md draft (detail bullet):**
- **2016 presidential-general** -- night `—` / final `24,541` = `—` (none)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: Certified final 24,541 ballots cast. Election-night PLATEAU not sourceable: the county elections page's report link is a pre-election zero report through the last pre-Nov-13 capture, and the only later-linked report filename (Fifth_Unofficial_Report.pdf) was first crawled in Sept 2018 showing different (later-election) content due to Joomla filename reuse.

---

## Item 4: 2018-11-06 midterm-general — NULL (documented dead end)

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2018 general.
URL: `https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf`
County line as printed (pdftotext -layout, row 58): `Tehama  46  43,847  33,286  5,583  15,564  21,147  73.60%  63.53%  48.23%`
(Precincts 46, Eligible-to-Register 43,847, Registered Voters 33,286,
Precinct Voters 5,583, VBM Voters 15,564, **Total Voters 21,147**, %VBM
73.60%, Turnout/Registered 63.53%, Turnout/Eligible 48.23%). Certified
final = **21,147**.

**Election-night numerator: not sourceable. Every route tried:**
1. *Registrar press release (6.2):* WebSearch for the exact press-release
   phrasing that DID work for 2020/2022/2024 ("Tehama County Elections
   Department issued its second unofficial..."), targeted at 2018 and at
   Red Bluff Daily News / Corning Observer 2018 coverage generally --
   returned no 2018-dated article; every hit resolved to the 2020 article
   already found (`appeal-democrat.com/corning_observer/tehama-county-unofficial-election-results/article_806ab74a-1e67-11eb-bc52-33b1155ccf2e.html`,
   confirmed datePublished 2020-11-04, not reusable).
2. *County's dated report series (6.3):* the site was still Joomla-era
   co.tehama.ca.us in Nov 2018 (confirmed via a 2018-11-13 Wayback capture
   of `co.tehama.ca.us/elections`). That page's raw HTML DOES link a
   dated report: `<a href="/images/Third_Unofficial_report.pdf">
   November 6, 2018 Election Results</a>` -- but CDX shows Wayback never
   crawled that PDF at the time; the only capture of that exact URL is
   `20251206112906` (Dec 2025), seven years later and long after this same
   filename would have been silently overwritten by subsequent elections'
   reports (the Joomla `images/` directory reuses filenames across
   elections rather than dating them, confirmed by the analogous
   `Fifth_Unofficial_report.pdf` also showing only a 2024-06 capture, i.e.
   June 2024 primary content). Guessed sibling filenames
   `First_Unofficial_report.pdf`, `Second_Unofficial_report.pdf`,
   `Fourth_Unofficial_report.pdf`, `Final_Unofficial_report.pdf` all have
   ZERO CDX captures ever. The only other 2018-era "results" PDF found,
   `images/images/Elections/Final_Official_Report.pdf`, has a capture
   dated **2018-09-03** (before the Nov 6 election) with a "revisit"
   (unchanged digest) in Feb 2019 -- i.e. this filename is a stale leftover
   from the June 2018 primary, never updated for the November general.
3. *Dedicated results-detail page:* `election_results/Election
   Result_dtl.htm` (found in the archive-probes for 2016/2018 windows) was
   independently re-checked across its FULL capture history (CDX, no date
   filter): the digest `HGC6WFCVJWKP2475SDIH4XXDVXDDEFPF` is IDENTICAL from
   2015-01-19 through 2021-06-20 (including the 2016-11-07 and 2018-11-28
   captures the archive probe flagged as "close to election night" --
   both are `warc/revisit`s of that same frozen digest). Fetched and
   read two of these captures directly (2014-11-04 zero-report, and
   2015-01-19 which carries an internal "Last Updated: November 13, 2014
   2:36 PM" stamp with Total 15,791 -- exactly the 2014 CERTIFIED final).
   Conclusion: this page was frozen showing **2014** results from Jan 2015
   onward and was never updated for the 2016 or 2018 elections; the probe's
   read of the 2016/2018 captures as "day-before-election" content was a
   false lead corrected by this pass.
4. *Wayback of the live results page generally (6.5):* the `dep-elections`
   landing page (captures 2018-11-07 15:01 UTC, 2018-11-09 15:21 UTC,
   2018-11-13 19:44 UTC, 2018-11-30 00:09 UTC) was fetched and de-tagged at
   all four timestamps; none embed ballot counts directly, only links to
   PDFs (enumerated above). No JS-rendered ENR widget exists on this
   Joomla-era site (unlike 2022+), so `render_wayback.cjs` has nothing to
   render here.
5. *Local news (6.6):* WebSearch for Red Bluff Daily News / Corning
   Observer 2018-dated election-night coverage returned no results
   (searches surfaced only 2020/2022/2024/2026 articles; a KRCR "Early
   voter turnout numbers disappoint in Shasta, Tehama Counties" story
   surfaced but is a pre-election VBM-return-rate story, not an
   election-night ballot count).
6. *Clarity (6.4):* skipped per probe (confirmed 404, not on Clarity).

**Conclusion:** no on-night report survives at any checked route. Per
RUNBOOK 5.1, this is a documented null, not a substituted denominator or a
different report time.

**Row draft (per RUNBOOK section 2 schema):**
```json
{
  "date": "2018-11-06",
  "type": "midterm-general",
  "election_night_ballots": null,
  "certified_final": 21147,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Certified final 21,147 ballots cast (CA SoS SoV; precinct 5,583 + VBM 15,564; 63.53% of 33,286 registered). Election-night PLATEAU not sourceable despite substantial effort. The Nov 6, 2018 co.tehama.ca.us 'elections' page (Wayback capture 2018-11-13) links a dated report, '/images/Third_Unofficial_report.pdf' ('November 6, 2018 Election Results'), but Wayback never crawled that PDF at the time -- its only capture is dated 2025-12-06, seven years later, on a Joomla-era 'images/' directory confirmed (via the sibling Fifth_Unofficial_report.pdf, captured only 2024-06) to silently overwrite the same filename across elections, so that 2025 capture would show a much later election's content, not 2018's, and cannot be cited. Guessed sibling filenames (First/Second/Fourth/Final_Unofficial_report.pdf) have zero CDX captures ever. The dedicated 'Election Result_dtl.htm' results page (flagged by the archive probe as plausible for 2016/2018) was re-examined across its full capture history and found to be FROZEN on 2014 election data from 2015-01-19 through 2021-06-20 (digest HGC6WFCVJWKP2475SDIH4XXDVXDDEFPF unchanged for 6+ years, including the 2016-11-07 and 2018-11-28 captures the probe flagged) -- corrects the probe's read of those captures as live pre/post-election content. images/images/Elections/Final_Official_Report.pdf is a stale leftover from the June 2018 primary (captured 2018-09-03, before the November election, revisit-unchanged into 2019). No registrar press release found for Nov 2018 (WebSearch for the exact phrasing that worked for 2020/2022/2024 surfaced nothing dated 2018). No local news election-night figure found (Red Bluff Daily News, Corning Observer). Not on Clarity (probe-confirmed 404). Null per RUNBOOK 5.1: never substitute a different report time or denominator. vs_epollbook/vs_asv n/a (control county, never adopted)."
}
```

**VERIFY.md draft (summary row):**
`| 2018 | midterm-general | — | 21,147 | — | none | — (not sourceable) |`

**VERIFY.md draft (detail bullet):**
- **2018 midterm-general** -- night `—` / final `21,147` = `—` (none)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: Certified final 21,147 ballots cast. Election-night PLATEAU not sourceable: the linked `/images/Third_Unofficial_report.pdf` on the county's Nov 2018 elections page was never crawled by Wayback at the time (only a 2025-12-06 capture exists, on a filename confirmed reused/overwritten across later elections); the "Election Result_dtl.htm" results page is frozen on 2014 data throughout the 2016-2021 window. No press release or local news figure found.

(No plateau_review.json entry: RUNBOOK 5.5 requires a verdict only for
*sourced* rows; this is a null row.)

---

## Item 5: 2022-11-08 midterm-general — SOURCED, CONFIRMED

**Certified final (denominator):** CA SoS Statement of Vote, Voter
Participation Statistics by County, 2022 general.
URL: `https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf`
County line as printed (pdftotext -layout, row 59): `Tehama  40  46,966  37,131  3,258  17,561  20,819  84.35%  56.07%  44.33%`
(Precincts 40, Eligible-to-Register 46,966, Registered Voters 37,131,
Precinct Voters 3,258, VBM Voters 17,561, **Total Voters 20,819**, %VBM
84.35%, Turnout/Registered 56.07%, Turnout/Eligible 44.33%). Certified
final = **20,819**. Cross-check: the county's own `Final-Summary-Report.pdf`
(see below) independently states "Total Registration and Turnout 37,115 /
20,819" -- the 20,819 figure matches exactly.

**Election-night numerator:** the co.tehama.ca.us domain (2022-era site,
already migrated to the same WordPress theme later reused at tehama.gov) is
DNS-dead today (confirmed: all direct curl attempts to co.tehama.ca.us
return connection failure, matching the probe's finding), so every 2022
source below is a Wayback recovery, not a live fetch. Route: found the
`election-results` page's Wayback capture, gunzipped the raw `id_` reply
(bytes started `1f 8b`, per RUNBOOK 7.1), and read its PDF link list.
- Page capture `20221109070542` (2022-11-09 07:05:42 UTC = Nov 8, 2022
  11:05:42 PM PST, i.e. still election night): only link present is
  `.../wp-content/uploads/2022/11/FirstUnofficialVoteByMailReport.pdf`.
- Page capture `20221123010654` (Nov 23, well into canvass): now lists the
  FULL report series: `FirstUnofficialVoteByMailReport.pdf`,
  `ThirdUnofficialPrecinctReport.pdf`, `Fourth-Unofficial-Precinct-Report.pdf`,
  `FifthUnofficialReport.pdf`, `SixthUnofficialReport.pdf`,
  `SeventhUnofficialReport.pdf`, `Eighth-Unofficial-Report.pdf`,
  `Final-Summary-Report.pdf`. No "Second" report link appears at any
  capture of this page (checked both listing captures and several filename
  variants directly against CDX -- `SecondUnofficialVoteByMailReport.pdf`,
  `SecondUnofficialPrecinctReport.pdf`, `Second-Unofficial-...` -- all
  return zero CDX hits); the county's own public numbering skips straight
  from First to Third.
- Fetched every report via `web.archive.org/web/<ts>id_/<url>` (gunzip
  where needed) and read the internal `Election Summary Report` header
  timestamp + `Voters Cast` line:
  - **First Unofficial Vote By Mail Report**: internal header `11/8/2022
    8:02:41 PM`. Voters Cast 8,882 of 37,115 (23.93%). FIRST TRANCHE
    (VBM-only, generated right at poll close), not the plateau.
  - **Third Unofficial Precinct Report**: internal header `11/8/2022
    10:37:39 PM`. **Voters Cast 11,878 of 37,115 (32.00%)**. Still election
    night (10:37 PM).
  - **Fourth Unofficial Precinct Report**: internal header `11/10/2022
    3:02:05 PM` -- Thursday afternoon, TWO DAYS after the election.
    Precincts Reported 40 of 40 (100.00%), Voters Cast 14,317 of 37,115
    (38.57%). This is a canvass update, NOT election night.
  - Fifth (`11/14/2022 4:35:33 PM`), Sixth (`11/16/2022 1:50:42 PM`),
    Seventh (`11/17/2022 4:14:40 PM`), Eighth (`11/23/2022 2:37:40 PM`):
    all clearly post-night canvass batches, dates confirm progression
    through the 30-day certification window.
  - **Final Summary Report** (no page-1 internal date stamp, 4-page
    condensed format): "Total Registration and Turnout 37,115 / 20,819" --
    the certified total, matching the SoS SoV exactly.

**Plateau identification:** the **Third Unofficial Precinct Report**
(11,878 ballots, internal timestamp 10:37:39 PM election night) is the
last report generated ON election night. Evidence (RUNBOOK 8, CONFIRMED
tier): (1) self-describes via internal generation timestamp squarely inside
the election-night window (10:37 PM, before the "1-4 a.m. next morning"
cutoff the runbook allows); (2) the report series' NEXT file (Fourth) is
generated 11/10/2022 3:02:05 PM -- a **40-hour gap** spanning the whole of
election night, the next morning, and into a second business day, with no
report interposed -- the county's own posting schedule brackets the Third
report as the last one of election night.

**Arithmetic:** 11,878 / 20,819 = **57.06%** (57.0584...%, rounds to 57.06).

**Calibration note:** 57.06% is a plausible plateau, comparable to SF's own
midterm shares (59.3% in 2018, 51.0% in 2022) rather than the runbook's
"80-95%" small-rural-county expectation -- consistent with the same
VBM-heavy explanation noted for the 2024 row (84.35% VBM share this year
per the SoV line above): a report generated less than 3 hours after poll
close, even at "precinct" 100%-of-40-precincts-eventually framing, still
has most VBM/drop-box ballots unopened. (Note: the Third report itself does
NOT state 100% precincts reporting -- that milestone is first stated on the
Fourth report, Nov 10 -- so 11,878 likely undercounts even in-person
precinct tabulation slightly in addition to VBM backlog; still the LAST
number posted on election night per the file-timestamp evidence, which is
what the metric definition requires.)

**Row draft (per RUNBOOK section 2 schema):**
```json
{
  "date": "2022-11-08",
  "type": "midterm-general",
  "election_night_ballots": 11878,
  "certified_final": 20819,
  "election_night_pct": 57.06,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20221205014450id_/https://www.co.tehama.ca.us/wp-content/uploads/2022/11/ThirdUnofficialPrecinctReport.pdf",
  "confidence": "primary",
  "note": "Election-night PLATEAU = 11,878 ballots ('Voters Cast: 11,878 of 37,115 (32.00%)'), from Tehama County's official 'Election Summary Report' internally timestamped 11/8/2022 10:37:39 PM -- the 'Third Unofficial Precinct Report' (the county's public numbering skips 'Second'; verified no Second-named file exists via CDX on several filename guesses). Recovered from Wayback (co.tehama.ca.us is DNS-dead live; fetched via web.archive.org/web/<ts>id_/<url>, gunzipped -- raw id_ replies were gzip-encoded, bytes 1f8b, per RUNBOOK 7.1) since the live domain no longer resolves. This is the night's plateau, NOT the 8:02:41 PM First Unofficial Vote By Mail Report (8,882 ballots, VBM-only first tranche) and NOT the Fourth Unofficial Precinct Report (14,317 ballots, internally timestamped 11/10/2022 3:02:05 PM, Thursday afternoon, 2 days post-election -- a canvass update). It HELD through election night and beyond: the report series' next file (Fourth) is dated 40 hours later with nothing interposed, i.e. the county's own posting schedule brackets the Third report as the last one of election night. Arithmetic: 11,878 / 20,819 = 57.06% (certified final confirmed independently by the county's own Final-Summary-Report.pdf: 'Total Registration and Turnout 37,115 / 20,819', matching the SoS SoV exactly). Pre/post tech: n/a, Tehama never adopted e-pollbooks or ASV (control county). PRIMARY (official county Election Summary Report PDF via Wayback). Calibration: 57.06% sits closer to SF's own midterm shares (59.3% 2018, 51.0% 2022) than the runbook's 80-95% small-rural-county expectation; explained by Tehama's heavy VBM share (84.35% VBM of the certified final) and the report's own admission it had not yet reached 100% of precincts (unlike Fourth, which explicitly states 40/40 100.00%) -- consistent with, not contradicting, the same pattern seen in the 2024 row."
}
```

**VERIFY.md draft (summary row):**
`| 2022 | midterm-general | 11,878 | 20,819 | 57.1% | primary | [link](https://web.archive.org/web/20221205014450id_/https://www.co.tehama.ca.us/wp-content/uploads/2022/11/ThirdUnofficialPrecinctReport.pdf) |`

**VERIFY.md draft (detail bullet):**
- **2022 midterm-general** -- night `11,878` / final `20,819` = `57.06%` (primary)
  - numerator: <https://web.archive.org/web/20221205014450id_/https://www.co.tehama.ca.us/wp-content/uploads/2022/11/ThirdUnofficialPrecinctReport.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "Third Unofficial Precinct Report", header "11/8/2022 10:37:39 PM", "Voters Cast: 11,878 of 37,115 (32.00%)".

**plateau_review.json draft:**
```json
{
  "slug": "tehama-ca",
  "date": "2022-11-08",
  "verdict": "CONFIRMED",
  "basis": "internal generation timestamp (10:37:39 PM) is squarely inside the election-night window PLUS the report series' next file (Fourth Unofficial Precinct Report) is dated 40 hours later (11/10/2022 3:02:05 PM) with nothing interposed -- the county's own posting schedule brackets the Third report as the last one of election night.",
  "evidence": ["https://web.archive.org/web/20221205014450id_/https://www.co.tehama.ca.us/wp-content/uploads/2022/11/ThirdUnofficialPrecinctReport.pdf", "https://web.archive.org/web/20221205013240id_/https://www.co.tehama.ca.us/wp-content/uploads/2022/11/Fourth-Unofficial-Precinct-Report.pdf"]
}
```

---
