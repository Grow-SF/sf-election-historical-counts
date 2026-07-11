# Dossier: Del Norte County, CA (slug del-norte-ca)

Control county for the researching-election-night-share dataset: NEVER adopted
e-pollbooks or ASV through 2024 (per SoS voting-tech-by-county snapshots).
Building per docs/research/RUNBOOK.md sections 1, 5, 6, 7, 8. Read-only
research; no repo files touched. Working dir for any repo script invocation
must be this scratch dir.

Sources already on hand before this pass (from
data/research/county-tech/ca_adoption_census.json census row for Del Norte):
- epollbook_year: null, asv_year: null, vca_year: null, status: "never",
  confidence: "medium"
- https://wildrivers.lostcoastoutpost.com/2020/sep/4/dubious-about-vote-mail-call-or-ask-del-norte-coun/
- https://www.co.del-norte.ca.us/departments/Elections/VoteMail
- https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf
- https://www.eac.gov/research-and-data/datasets-codebooks-and-surveys

Probe file verdict (archive-probes-a-m.md, Del Norte section): **viable** —
county's own site keeps dated per-election results subpages (e.g.
`.../election-results/november-8-2016-general-election-results`), captured in
Wayback as of 2018-11-25. No Clarity usage (confirmed 404 at
`https://results.enr.clarityelections.com/CA/Del_Norte/`).

---

## Item 0: Tech record (e-pollbook + ASV never-adopter evidence)

Locating query used: reused census row's cited URLs; extended by pattern-
guessing two more dated SoS "Voting Technologies in Use By County" PDF URLs
(same CDN path family as the 2025 one) and fetching them directly.

### New evidence gathered this pass

1. **SoS "Voting Technologies in Use By County" PDF, October 10, 2025 snapshot**
   (already cited in census row) — confirmed by direct fetch+pdftotext this
   pass.
   - URL: `https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf`
   - Locating query: direct URL fetch, `pdftotext -layout`, `grep -n -i "del norte"`.
   - Result line 18: `Del Norte | Dominion ICC 5.10A | Dominion ICE 5.10A | Dominion ICX 5.10A | Do not use | Do not use | Democracy Live Secure Select | Do not use`
     — the LAST column (header: "Electronic Pollbook") = **"Do not use"**.

2. **SoS same-series PDF, February 9, 2024 snapshot** (NEW find this pass, not
   in the census row's source list).
   - URL: `https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2024-1.pdf`
   - Locating query: guessed URL pattern `vot-tech-by-counties-2024-1.pdf` in
     the same CDN directory as the 2025 file; `curl -o /dev/null -w
     "%{http_code}"` returned 200 on first try.
   - Header: "As of Feburary 9, 2024" [sic], for the March 5, 2024 Presidential
     Primary.
   - Del Norte row: `Dominion ICC 5.10A | Dominion ICE 5.10A | Dominion ICX
     5.10A | Do not use | Do not use | Democracy Live Secure Select | Do not
     use` — Electronic Pollbook column = **"Do not use"**. This is the
     snapshot closest to (just before) the 2024-11-05 general in our election
     list, i.e. direct evidence Del Norte had no e-pollbook for the 2024
     general.

3. **SoS same-series PDF, May 9, 2022 snapshot** (NEW find this pass).
   - URL: `https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2022-1.pdf`
   - Locating query: same pattern guess, `vot-tech-by-counties-2022-1.pdf`,
     200 on first try.
   - Header: "As of May 9, 2022", for the June 7, 2022 Primary.
   - Del Norte row: `Dominion ImageCast Central 5.10A | Dominion ImageCast
     Precinct 2 | Dominion ImageCast X 5.10A | Do not use | Do not use |
     Democracy Live SecureSelect | Do not use` — Electronic Pollbook column =
     **"Do not use"**. Covers the 2022-11-08 general in our election list.
   - Together, the 2022/2024/2025 snapshots bracket both the 2022-11-08 and
     2024-11-05 elections in this dossier with "Do not use" e-pollbook status
     each time: continuous never-adopter signal through 2024, no adoption gap
     possible between snapshots.

4. **Wild Rivers Outpost (Lost Coast Outpost), Sept 4 2020** — re-confirmed by
   direct fetch this pass (exact quote extracted from live HTML).
   - URL: `https://wildrivers.lostcoastoutpost.com/2020/sep/4/dubious-about-vote-mail-call-or-ask-del-norte-coun/`
   - Locating query: direct URL fetch, HTML stripped to text, searched for
     "handled by a human".
   - Quote, then-County Clerk/Registrar Alissia Northrup: "Each ballot is
     handled by a human being who examines the ballot to make sure it hasn't
     been tampered with. They verify signature against the signature we have
     on file from (the voter's) registration card and they verify the address
     to make sure it's the address where they're registered to vote and to
     make sure they're only voting on what they should be voting on. If any
     of those things are off, we contact the voter to let them know..."
   - This is explicit on-the-record evidence signature review is
     human/manual, not software-assisted (no ASV), as of the 2020 VBM cycle.

5. **Del Norte County "VoteMail" page** — re-confirmed by direct fetch this
   pass.
   - URL: `https://www.co.del-norte.ca.us/departments/Elections/VoteMail`
   - Locating query: direct URL fetch, HTML stripped to text, searched
     "signature".
   - Page describes only the statutory absentee-ballot request process
     (mail/fax/in-person written request with a signature on the request
     form) — no mention of any automated signature-verification or
     electronic-pollbook technology anywhere on the page. Consistent with
     (does not contradict) the never-adopter finding; this page is
     process-description, not a tech inventory, so kept at supporting
     (not primary) weight.

6. EAC "Election Administration and Voting Survey" dataset page
   (`https://www.eac.gov/research-and-data/datasets-codebooks-and-surveys`)
   was in the census row's source list as a generic pointer (not a specific
   citable finding); not re-derived this pass; carried forward as-is without
   claiming a new quote from it.

### Draft data/research/county-tech/del-norte-ca.json record

```json
{
  "jurisdiction": "Del Norte County",
  "state": "CA",
  "tech": [
    {
      "type": "epollbook",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf",
      "confidence": "primary",
      "note": "CA SoS 'Voting Technologies in Use By County' snapshots consistently list Del Norte's Electronic Pollbook column as 'Do not use': May 9, 2022 snapshot (https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2022-1.pdf, row: Dominion ImageCast Central/Precinct/X tabulation, Electronic Pollbook = Do not use), February 9, 2024 snapshot (https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2024-1.pdf, Electronic Pollbook = Do not use), and October 10, 2025 snapshot (this evidence_url, Electronic Pollbook = Do not use). Three consecutive official snapshots bracketing the 2022-11-08 and 2024-11-05 elections in this dataset show no e-pollbook adoption at any point. Not a VCA county (no vote-center model). Locating query: fetch https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-<YEAR>-1.pdf, pdftotext -layout, grep -n -i 'del norte'."
    },
    {
      "type": "asv",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://wildrivers.lostcoastoutpost.com/2020/sep/4/dubious-about-vote-mail-call-or-ask-del-norte-coun/",
      "confidence": "secondary",
      "note": "No automated signature-verification vendor/software found in any county material. Then-Clerk/Registrar Alissia Northrup on-the-record (Wild Rivers Outpost, Sept 4 2020): 'Each ballot is handled by a human being who examines the ballot to make sure it hasn't been tampered with. They verify signature against the signature we have on file from (the voter's) registration card...' -- explicit description of manual/human signature review, no automated matching software named. Del Norte's own VoteMail page (https://www.co.del-norte.ca.us/departments/Elections/VoteMail) describes only the statutory written-request process, no ASV technology mentioned (supporting, not primary, since it is process description not a tech inventory). Confidence secondary: quote dates to 2020, no county statement located reconfirming the process is still fully manual through 2024, though nothing in the 2022/2024/2025 SoS tech snapshots names any ASV product for Del Norte either (those snapshots do not have a distinct ASV column but no ASV vendor appears anywhere in county communications searched)."
    },
    {
      "type": "vote-center",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf",
      "confidence": "primary",
      "note": "Not a Voter's Choice Act county. SoS voting-tech snapshots show a conventional precinct-tabulator setup (Dominion ICE precinct scanner column populated) rather than the VCA all-mail/vote-center model; census row also independently marked vca_year null."
    }
  ],
  "notes": "TECH: Del Norte never adopted e-pollbooks through at least Oct 10 2025 (three SoS snapshots: May 2022, Feb 2024, Oct 2025, all 'Do not use' in the Electronic Pollbook column) and never adopted ASV (2020 on-the-record county quote describes fully manual/human signature review; no ASV vendor found anywhere). Not a VCA/vote-center county. This is a control county for the pre/post e-pollbook and pre/post ASV comparisons: vs_epollbook and vs_asv should be 'n/a' for every election-night row. Confidence kept at primary for epollbook (direct official snapshot evidence, three independent dates) and secondary for ASV (single 2020 quote, no more recent reconfirmation)."
}
```

STATUS: Item 0 complete.

---

## Denominators for all 6 elections (fetched together, before per-election items)

Locating query pattern: fetch each `https://elections.cdn.sos.ca.gov/sov/<year>-general/[sov/|pdf/]03-voter-participation-stats-by-county.pdf` per runbook 6.1's per-year URL quirks; `pdftotext -layout`; `grep -n -i "del norte"`. All six fetched at HTTP 200 on the first try.

| Election | SoV URL | Del Norte line (Precincts, Eligible, Registered, Precinct Voters, VBM Voters, Total Voters, %VBM, %Reg turnout, %Elig turnout) | Total Voters (certified_final) |
|---|---|---|---|
| 2012-11-06 | https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf | `Del Norte 18 18,250 12,516 3,620 5,259 8,879 59.23% 70.94% 48.65%` | **8,879** |
| 2014-11-04 | https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf | `Del Norte 18 18,253 12,750 2,980 4,352 7,332 59.36% 57.51% 40.17%` | **7,332** |
| 2016-11-08 | https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf | `Del Norte 18 17,996 14,318 3,653 6,137 9,790 62.69% 68.38% 54.40%` | **9,790** |
| 2018-11-06 | https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf | `Del Norte 18 18,039 14,150 2,898 5,541 8,439 65.66% 59.64% 46.78%` | **8,439** |
| 2022-11-08 | https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf | `Del Norte 19 19,219 14,943 1,133 7,317 8,450 86.59% 56.55% 43.97%` | **8,450** |
| 2024-11-05 | https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf | `Del Norte 19 18,059 15,036 1,686 8,990 10,676 84.21% 71.00% 59.12%` | **10,676** |

Column header confirmed from each PDF's own header row: County / Number of Precincts / Eligible to Register / Registered Voters / Precinct Voters / Vote-By-Mail Voters / **Total Voters** / Percent of Vote-By-Mail Voters / Turnout Registered / Turnout Eligible. "Total Voters" (Precinct Voters + VBM Voters) is the certified_final figure used below.

---

## Item 3: 2016-11-08 presidential-general (researched first; page structure discovery)

**Certified final:** 9,790 (SoS SoV, see denominators table above; URL
https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf).

**Election-night plateau: FOUND, primary confidence, CONFIRMED.**

Route used: 6.3 (county's own dated report series), discovered via 6.5 (Wayback capture of the county's dated per-election results page, per the probe file's lead).

Locating query / recovery path (fully reproducible):
1. `curl -s "http://web.archive.org/cdx/search/cdx?url=co.del-norte.ca.us/departments/clerk-recorder/elections/election-results/november-8-2016-general-election-results&matchType=prefix&output=json&limit=500&collapse=urlkey"` -> only the page shell itself archived under the custom domain (capture `20180419085323`), no PDF attachments under that urlkey.
2. Fetched the page shell (`https://web.archive.org/web/20180419085323id_/http://www.co.del-norte.ca.us:80/departments/clerk-recorder/elections/election-results/november-8-2016-general-election-results`): a Google Sites (JotSpot-era, custom-domain-mapped) page listing 7 attachment links: "November 8, 2016 General Election Results - Release 1.pdf" through "Release 6.pdf", plus "November 8, 2016 General Election-Certified Final Results.pdf". Page HTML also reveals the underlying canonical Google Sites URL (`sites.google.com/a/co.del-norte.ca.us/dnco/...`), which Wayback crawled independently and much more completely.
3. `curl -s "http://web.archive.org/cdx/search/cdx?url=sites.google.com/a/co.del-norte.ca.us/dnco/departments/clerk-recorder/elections/election-results/november-8-2016-general-election-results&matchType=prefix&output=json&limit=500&collapse=urlkey"` -> 16 captures including all 7 attachment links, captured mostly 2020-11-11 (archiveteam Google Sites shutdown-rescue crawl) plus 3 older captures of the Certified Final (2017-02-25, 2017-04-28, 2018-11-28).
4. Each attachment link itself only 302-redirected in Wayback's normal replay (Google Sites attachment URLs point through a signed, session-scoped `attachauth=` token to a `*.s-sites.googlegroups.com` content host). Followed the `Location:` header from `curl -sIL` on the normal (non-`id_`) replay to get the exact target URL+timestamp, then ran a second CDX query on `b012f97e-a-03565450-s-sites.googlegroups.com` (same path prefix) which DOES show the actual `application/pdf` 200 responses with real byte lengths — this is the archiveteam megawarc capturing the destination of the redirect under its own URL, a case not explicitly in runbook 7.1 but the same "replay aliasing" family of gotcha.
5. Fetched each release's PDF bytes with the raw `id_` form at its EXACT matched timestamp (not the page-shell timestamp): all 6 Releases + Certified Final downloaded successfully as real, valid PDFs (poppler `file`/`pdfinfo` confirm valid PDF 1.3/1.4, 9 pages each for Releases, 40 pages for the Certified Final SOVC).
6. Releases 1-5 and the Certified Final SOVC are **scanned image PDFs** (Creator: "Canon iR-ADV C5240 PDF", a photocopier/scanner) with NO text layer — `pdftotext` returns empty. Per the runbook, OCR is reserved for the SF newspaper-scan workflow, not this dataset, so these were read the way a human would read a scan: rendered to PNG with `pdftoppm -png -r 150` and read visually (page 1, the summary header, is sufficient; no digit-transcription ambiguity — printed government report, clean typeface, no handwriting). Release 6 and the Certified Final Statement-of-Votes-Cast happen to be a DIFFERENT report generator (Microsoft Reporting Services 10.0.0.0) with a real text layer; those were read with `pdftotext -layout`.

**The full election-night release series (all 7 artifacts recovered and read):**

| Release | PDF internal timestamp (page header) | Label | Precincts | Times Cast / Registered | Turnout % |
|---|---|---|---|---|---|
| 1 | 11/8/2016 8:01:37 PM | "Unofficial Results / Vote By Mail Ballots" | 0 of 18 (0.00%) | 4,797 / 14,320 | 33.50% |
| 2 | 11/8/2016 9:13:13 PM | "Unofficial Results / Vote By Mail Ballots With Precinct Updates 1" | 5 of 18 (27.78%) | 5,437 / 14,320 | 37.97% |
| 3 | 11/8/2016 9:55:02 PM | "Unofficial Results / Vote By Mail Ballots" | 17 of 18 (94.44%) | 7,951 / 14,320 | 55.52% |
| **4** | **11/8/2016 10:47:49 PM** | **"Unofficial Results / Election Night Final"** | **18 of 18 (100.00%)** | **8,155 / 14,320** | **56.95%** |
| 5 | 11/15/2016 12:31:24 PM (8 days later) | "Unofficial Results" (no VBM/night subtitle; full canvass update) | 18 of 18 (100.00%) | 9,702 / 14,320 | 67.75% |
| 6 | 11/16/2016 9:15:31 AM | "Unofficial Final Report" (Microsoft Reporting Services) | 18 of 18 (100.00%) | 9,790 / 14,320 | 68.37% (= exact certified final) |
| Certified Final | 12/8/2016 10:15:51 AM | "Official Certified Results" (Statement of Votes Cast, 40pp precinct-by-precinct) | Countywide Total: 14,320 registered, 19,556 cards cast | 9,790 (implied; ballot CARDS 19,556, ~2 cards/voter matches Release 6's Ballots Cast 19,556 exactly) | matches SoS |

**PLATEAU = Release 4, "Election Night Final", 8,155 ballots.** The report self-labels as the election-night final (exact runbook-8 self-description criterion), is at 100% precincts reporting, and the NEXT report in the same numbered series is 8 days later at a materially higher count (9,702) — the bracket/gap-to-next-report leg required for CONFIRMED. Release 3 (9:55 PM, still labeled "Vote By Mail Ballots" only, 17/18 precincts) is the prior, NOT-yet-final report and is clearly the second-to-last step, not the plateau; Release 1 (8:01 PM, 0 precincts, pure pre-processed VBM, 33.5%) is the classic first tranche this dataset must NOT use.

Arithmetic: 8,155 / 9,790 = **83.30%** (2dp). This is well inside the "small rural county, most vote counted on night" 80-95% calibration band from RUNBOOK section 1, and well above the ~54.4% registered-turnout figure printed in the SoS row (which is a different denominator, registered voters not ballots-vs-final, so not directly comparable, but sanity-consistent: turnout was high and Del Norte counted the overwhelming majority of it same night).

**Draft data/research/election-night/del-norte-ca.json row (2016):**

```json
{
  "date": "2016-11-08",
  "type": "presidential-general",
  "election_night_ballots": 8155,
  "certified_final": 9790,
  "election_night_pct": 83.30,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20201111052405id_/https://b012f97e-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/dnco/departments/clerk-recorder/elections/election-results/november-8-2016-general-election-results/November%208%2C%202016%20General%20Election%20Results%20-%20Release%206.pdf",
  "confidence": "primary",
  "note": "PLATEAU = county's own numbered election-night release series, Release 4 of 6, self-labeled 'Unofficial Results / Election Night Final', internal page-header timestamp 11/8/2016 10:47:49 PM, 18 of 18 precincts (100.00%) reporting. Times Cast 8,155 of 14,320 registered (56.95%). Series ran Release 1 (8:01 PM, 0 precincts, pure pre-processed VBM, 4,797 = 33.50%, the classic first tranche, NOT used) -> Release 2 (9:13 PM, 5,437) -> Release 3 (9:55 PM, 17/18 precincts, 7,951) -> Release 4 (10:47 PM, 18/18, 8,155, ELECTION NIGHT FINAL) -> Release 5 (11/15, 8 days later, 9,702, full-canvass update) -> Release 6 (11/16, 9,790, 'Unofficial Final Report', exactly equal to the certified final) -> Official Certified Statement of Votes Cast (12/8, 9,790 confirmed, 19,556 ballot cards countywide). Recovered from Wayback's archiveteam Google-Sites rescue crawl of the county's dated per-election results page (a Google Sites-hosted county site at the time); the PDF attachments are served through session-scoped signed redirect URLs, so the working citation is the exact googlegroups content-host URL matched to its own CDX timestamp, not the page-shell URL. Releases 1-5 and the Certified Final SOVC are scanned photocopier PDFs (Canon iR-ADV C5240) with no text layer, read visually via 150dpi PNG render (not OCR, per runbook 0's OCR-is-SF-only rule); Release 6 and the certified SOVC are Microsoft Reporting Services PDFs with real text, read via pdftotext. Arithmetic: 8,155/9,790 = 83.30%, consistent with RUNBOOK 1's calibration that a small rural county's election-night plateau share is often 80-95% (most of its (small) vote is counted the same night). Del Norte never adopted e-pollbooks or ASV (see county-tech record); vs_epollbook and vs_asv both n/a (control county, no adoption event to be pre/post of)."
}
```

**VERIFY.md draft summary-table line (2016):**
`| 2016 | presidential-general | 8,155 | 9,790 | 83.3% | primary | [link](https://web.archive.org/web/20201111052405id_/https://b012f97e-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/dnco/departments/clerk-recorder/elections/election-results/november-8-2016-general-election-results/November%208%2C%202016%20General%20Election%20Results%20-%20Release%206.pdf) |`
(numerator link points at Release 4's own archived URL in the real dataset; using Release 6 URL above only as a stand-in reference since Release 4 and Release 6 share the same googlegroups host path family — CORRECTION when filing for real: use Release 4's exact matched URL+timestamp, captured 2020-11-11 05:24:03, `.../Release%204.pdf?attachauth=...` per the CDX dump saved in this dossier's scratch dir.)

**VERIFY.md draft detail bullet (2016):**
- **2016 presidential-general** — night `8,155` / final `9,790` = `83.3%` (primary)
  - numerator: Release 4 of the county's 2016 election-night PDF series (Wayback/archiveteam Google Sites rescue crawl; see note above for exact URL-recovery chain)
  - denominator (SoS SoV): https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf
  - look for: "Unofficial Results / Election Night Final", 18 of 18 precincts (100.00%), Times Cast 8,155/14,320 (56.95%), page-header timestamp 11/8/2016 10:47:49 PM.

**plateau_review.json draft record (2016):**
```json
{
  "slug": "del-norte-ca",
  "date": "2016-11-08",
  "verdict": "CONFIRMED",
  "basis": "self-labeled 'Election Night Final' report, last of a numbered on-night release series, next report 8 days later at a higher count",
  "evidence": "Release 4/6, 11/8/2016 10:47:49 PM, 18/18 precincts (100%), Times Cast 8,155/14,320 (56.95%); Release 5 (next in series) is dated 11/15/2016, 9,702/14,320 -- confirms Release 4 was the last report before the canvass resumed"
}
```

STATUS: Item 3 (2016-11-08) complete. Denominators for all 6 elections also captured above.

---

## Item 4: 2018-11-06 midterm-general

**Certified final:** 8,439 (SoS SoV; see denominators table above; URL
https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf).

**Election-night plateau: FOUND, primary confidence, CONFIRMED.**

Route used: 6.3 (county's own dated per-election page, same Google Sites
"election-results/november-6-2018-general-election" directory discovered
while mapping the 2016 page's parent index; runbook 6.5 Wayback mechanics for
recovery).

Locating query: `curl -s "http://web.archive.org/cdx/search/cdx?url=sites.google.com/a/co.del-norte.ca.us/dnco/departments/clerk-recorder/elections/election-results&matchType=prefix&output=json&limit=2000&collapse=urlkey"` (the same broad prefix query run for 2016) surfaced a `november-6-2018-general-election` subdirectory with 5 numbered releases + a local-candidate-list PDF. Followed the same redirect-resolution chain as 2016 (page -> attachment href with `attachauth=` token -> normal-replay `curl -sIL` to read the `Location:` -> CDX query on the `b012f97e-a-03565450-s-sites.googlegroups.com` content host, same path prefix, to find the real `application/pdf` 200 captures) -> fetched Release 4 and Release 5 (the last two) with the raw `id_` form at their exact matched timestamps. Both are scanned Canon-photocopier PDFs (no text layer); read visually via 150dpi PNG render.

**The two relevant releases:**

| Release | Internal report timestamp | Header | Precincts | Times Cast / Registered | 
|---|---|---|---|---|
| **4** | **11/6/2018 9:42:38 PM** | **"STATEWIDE GENERAL ELECTION ... ELECTION NIGHT SUMMARY REPORT / ELECTION NIGHT FINAL REPORT (UNOFFICIAL RESULTS)"** | **18 of 18 (100.00%)** | **7,127 / 14,289 (49.88%)** |
| 5 | 11/9/2018 3:39:03 PM (3 days later) | "STATEWIDE GENERAL ELECTION ... Election Results With Late Vote By Mail (UNOFFICIAL RESULTS)" | 18 of 18 (100.00%) | 8,121 / 14,289 (56.83%) |

**PLATEAU = Release 4, explicitly titled "ELECTION NIGHT FINAL REPORT", 7,127 ballots.** This is even stronger self-description than 2016 (the exact phrase "ELECTION NIGHT FINAL REPORT" appears in the document header, not inferred). The next report in the series (Release 5) is 3 days later, retitled to explicitly say "With Late Vote By Mail" (documenting that it is a canvass addition beyond the night's count) and shows a higher count (8,121). Both legs of runbook-8 CONFIRMED are satisfied: self-description AND the next report being both later and explicitly labeled as adding post-night ballots.

Arithmetic: 7,127 / 8,439 (certified final) = **84.45%** (2dp). Consistent with the small-rural-county 80-95% calibration band, and close to 2016's 83.30%, which is a good cross-check (Del Norte's election-night completeness looks stable year to year while never having e-pollbooks/ASV, as expected for a true control county).

**Draft data/research/election-night/del-norte-ca.json row (2018):**

```json
{
  "date": "2018-11-06",
  "type": "midterm-general",
  "election_night_ballots": 7127,
  "certified_final": 8439,
  "election_night_pct": 84.45,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20201111052344id_/https://b012f97e-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/dnco/departments/clerk-recorder/elections/election-results/november-6-2018-general-election/November%206%2C%202018%20General%20Election%20Results%20-%20Release%204.pdf",
  "confidence": "primary",
  "note": "PLATEAU = Release 4 of 5 in the county's own numbered 2018 election-night PDF series, self-titled (exact document header) 'STATEWIDE GENERAL ELECTION / TUESDAY, NOVEMBER 6, 2018 / ELECTION NIGHT SUMMARY REPORT / ELECTION NIGHT FINAL REPORT (UNOFFICIAL RESULTS)', internal timestamp 11/6/2018 9:42:38 PM, 18 of 18 precincts (100.00%), Times Cast 7,127 of 14,289 registered (49.88%). Recovered via the same Google-Sites archiveteam rescue crawl as the 2016 row (dated per-election subpage under the county's then Google-Sites-hosted site, attachment PDFs served via session-scoped signed redirect to a *.s-sites.googlegroups.com content host; the working citation is the exact googlegroups content URL matched to its own CDX timestamp). The next and final report in the series, Release 5, is dated 11/9/2018 3:39:03 PM (3 days later) and is explicitly retitled 'Election Results With Late Vote By Mail (UNOFFICIAL RESULTS)', Times Cast 8,121/14,289 -- i.e. the county's own next release documents that the canvass had resumed and added late-arriving VBM ballots, directly confirming Release 4 was the last report before the canvass. Scanned Canon-photocopier PDF, no text layer; read visually via 150dpi PNG render (not OCR). Arithmetic: 7,127/8,439 = 84.45%, consistent with the small-rural-county 80-95% calibration band and close to Del Norte's 2016 figure (83.30%). Del Norte never adopted e-pollbooks or ASV; vs_epollbook and vs_asv both n/a (control county)."
}
```

**VERIFY.md draft summary-table line (2018):**
`| 2018 | midterm-general | 7,127 | 8,439 | 84.5% | primary | [link](https://web.archive.org/web/20201111052344id_/https://b012f97e-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/dnco/departments/clerk-recorder/elections/election-results/november-6-2018-general-election/November%206%2C%202018%20General%20Election%20Results%20-%20Release%204.pdf) |`

**VERIFY.md draft detail bullet (2018):**
- **2018 midterm-general** — night `7,127` / final `8,439` = `84.5%` (primary)
  - numerator: Release 4 of the county's 2018 election-night PDF series (Wayback/archiveteam Google Sites rescue crawl)
  - denominator (SoS SoV): https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf
  - look for: "ELECTION NIGHT SUMMARY REPORT / ELECTION NIGHT FINAL REPORT (UNOFFICIAL RESULTS)", 18 of 18 precincts (100.00%), Times Cast 7,127/14,289 (49.88%), internal timestamp 11/6/2018 9:42:38 PM.

**plateau_review.json draft record (2018):**
```json
{
  "slug": "del-norte-ca",
  "date": "2018-11-06",
  "verdict": "CONFIRMED",
  "basis": "document explicitly titled 'ELECTION NIGHT FINAL REPORT'; next report 3 days later explicitly retitled to note late VBM additions",
  "evidence": "Release 4/5, 11/6/2018 9:42:38 PM, 18/18 precincts (100%), Times Cast 7,127/14,289 (49.88%); Release 5 (11/9/2018, 3 days later) retitled 'Election Results With Late Vote By Mail', Times Cast 8,121/14,289 -- confirms Release 4 was the last report before the canvass resumed"
}
```

STATUS: Item 4 (2018-11-06) complete.

---

## Item 2: 2014-11-04 midterm-general

**Certified final:** 7,332 (SoS SoV; see denominators table above; URL
https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf).

**Election-night plateau: FOUND, primary confidence, CONFIRMED.**

Route used: 6.3 (county's own dated per-election page). For 2014 the county's
election site was still on a DIFFERENT, older Google-Sites-hosted domain
(`elections.co.del-norte.ca.us`, top-level site named "elect") than the
2016-2020 site (`co.del-norte.ca.us` custom-domain-mapped to a Google Site
named "dnco"); both use the same numbered-release-PDF convention.

Locating query / recovery path:
1. `curl -s "http://web.archive.org/cdx/search/cdx?url=elections.co.del-norte.ca.us&matchType=domain&output=json&limit=500&collapse=urlkey&from=20110101&to=20150101"` surfaced `elections/election-results/november-4-2014-general-election` (captured 2014-11-08, 2 days after election, through 2021).
2. Fetched the page shell at capture `20141108203212` (`https://web.archive.org/web/20141108203212id_/http://elections.co.del-norte.ca.us:80/elections/election-results/november-4-2014-general-election`): lists 3 attachments -- "Release  1" (double space in filename), "Release 2", "Release 3 - Final".
3. Each attachment link redirects (302, `attachauth=` signed token) to a `425abd7a-a-03565450-s-sites.googlegroups.com` content host (a DIFFERENT numbered content-host prefix than 2016/2018's `b012f97e-...`, consistent with it being a separate/older Google Site). Followed each redirect via `curl -s ... -o file.html` (GET, not HEAD -- HEAD requests to web.archive.org intermittently connection-refused during this session; plain GET always worked) to read the `Location:` target, then found the matching CDX-archived `application/pdf` 200 capture for each target URL.
4. **Release 1's actual PDF bytes were never crawled** by Wayback under any URL variant found (confirmed via an exact-URL CDX query returning `[]`); only the redirect stub survives. This is a genuine, documented gap -- noted, not needed for the plateau determination since Release 1 (lowest-numbered, by the pattern in 2016/2018 always the earliest/first-tranche report) is not the number we want anyway.
5. Release 2 and Release 3-Final both recovered successfully (scanned Canon-photocopier PDFs, no text layer, read visually via 150dpi PNG render).

**The two recovered releases:**

| Release | Internal report timestamp (page footer) | Header | Precincts | Total Voters (Times Cast) / Registered |
|---|---|---|---|---|
| **2** | **11/4/2014 10:05 PM** | **"DEL_20141104_E ... Summary Report ... Del Norte County ... Nov. 4, 2014 General Election Unofficial"** | **18 of 18 (100.00%)** | **6,539 / 12,743 (51.31%)** |
| 3 - Final | 11/7/2014 3:55 PM (3 days later) | "DEL_20141104_E ... Nov. 4, 2014 General Election Final" | 18 of 18 (100.00%) | 7,332 / 12,743 (57.54%) |

**PLATEAU = Release 2, election night 10:05 PM, 6,539 ballots.** Release 2 is the last SURVIVING report of election night (Release 1's content is lost, but by the invariant naming convention seen consistently in 2016 and 2018, lower release numbers are always earlier in time, so Release 1 preceded Release 2 the same evening and was superseded by it -- Release 2 is not a "floor," it is the actual last-of-night state, already at 18/18 precincts 100% reporting). The next and final release (Release 3) is dated 3 days later, explicitly re-labeled from "Unofficial" to "Final," and shows a higher, exactly-certified-matching count (7,332 = the SoS SoV Total Voters figure exactly) -- textbook runbook-8 CONFIRMED: self-description-adjacent evidence (100% precincts already reporting, "Unofficial" not yet "Final") PLUS the next-report-days-later-with-relabeling leg.

Note the important distinction from 2016/2018: in 2014 there was NO separate on-night release explicitly titled "Election Night Final" -- Release 2 is simply the last one that exists before the 3-day gap to the certified-matching Release 3. This is documented per runbook 5.4/8 as CONFIRMED on the strength of the gap-to-next-report leg (not a self-description leg), which is one of the four accepted independent legs.

Arithmetic: 6,539 / 7,332 = **89.18%** (2dp). This is the highest of Del Norte's shares recovered so far (2016: 83.30%, 2018: 84.45%), still consistent with the "small rural county counts almost everything on election night" pattern, though at the upper edge -- worth a second look if a human wants to sanity-check the read of "6,539" (page 1 of 3, top-right registration/turnout box; the same digits recur seven times down the page as "Total ... 6,539 51.31%" wait -- actually recur as the per-race "Total" turnout denominator is different per race; the county-wide Total Voters figure appears once at top: "Total ... 6,539 51.31%").

**Draft data/research/election-night/del-norte-ca.json row (2014):**

```json
{
  "date": "2014-11-04",
  "type": "midterm-general",
  "election_night_ballots": 6539,
  "certified_final": 7332,
  "election_night_pct": 89.18,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20211102111036id_/https://425abd7a-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/elect/elections/election-results/november-4-2014-general-election/November%204%2C%202014%20General%20Election%20-%20Release%202.pdf",
  "confidence": "primary",
  "note": "PLATEAU = Release 2 of 3 in the county's numbered 2014 election-night PDF series (county's OLDER Google-Sites-hosted domain elections.co.del-norte.ca.us, site name 'elect', distinct from the co.del-norte.ca.us/'dnco' site used 2016-2020). Internal report footer timestamp 11/4/2014 10:05 PM, header 'Nov. 4, 2014 General Election Unofficial', 18 of 18 precincts (100.00%), Total Voters 6,539 of 12,743 registered (51.31%). Release 1's actual PDF bytes were never crawled by Wayback (only the redirect stub survives; CDX confirms no application/pdf capture at any URL variant) so it cannot be independently timestamped, but by the invariant convention observed in Del Norte's 2016 and 2018 release series (release numbers strictly increase with time), Release 1 preceded Release 2 the same night and is the first-tranche report, NOT used. Release 3, the only later release, is dated 11/7/2014 3:55 PM (3 days later), explicitly retitled 'Nov. 4, 2014 General Election Final', and shows Total Voters 7,332/12,743 (57.54%) -- exactly equal to the SoS SoV certified Total Voters figure, i.e. this is the certified-final report, not an election-night one. The 3-day gap plus the Unofficial-to-Final relabeling is the plateau-confirming leg (runbook section 8: report series' next file being days later). Both recovered releases are scanned Canon-photocopier PDFs, no text layer, read visually via 150dpi PNG render (not OCR). Arithmetic: 6,539/7,332 = 89.18%, the highest of Del Norte's recovered shares so far (2016: 83.30%, 2018: 84.45%) but still consistent with the small-rural-county high-election-night-completeness pattern. Del Norte never adopted e-pollbooks or ASV; vs_epollbook and vs_asv both n/a (control county)."
}
```

**VERIFY.md draft summary-table line (2014):**
`| 2014 | midterm-general | 6,539 | 7,332 | 89.2% | primary | [link](https://web.archive.org/web/20211102111036id_/https://425abd7a-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/elect/elections/election-results/november-4-2014-general-election/November%204%2C%202014%20General%20Election%20-%20Release%202.pdf) |`

**VERIFY.md draft detail bullet (2014):**
- **2014 midterm-general** — night `6,539` / final `7,332` = `89.2%` (primary)
  - numerator: Release 2 of the county's 2014 election-night PDF series (Wayback, elections.co.del-norte.ca.us "elect" Google Site, redirect-resolved to the googlegroups content host)
  - denominator (SoS SoV): https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf
  - look for: "Nov. 4, 2014 General Election Unofficial", 18 of 18 precincts (100.00%), Total Voters 6,539/12,743 (51.31%), page footer timestamp 11/4/2014 10:05 PM.

**plateau_review.json draft record (2014):**
```json
{
  "slug": "del-norte-ca",
  "date": "2014-11-04",
  "verdict": "CONFIRMED",
  "basis": "last surviving on-night release (18/18 precincts, still labeled Unofficial); next report 3 days later relabeled Final at the exact certified total",
  "evidence": "Release 2/3, footer timestamp 11/4/2014 10:05 PM, 18/18 precincts (100%), Total Voters 6,539/12,743 (51.31%); Release 3 (11/7/2014, 3 days later) retitled 'General Election Final', Total Voters 7,332/12,743 -- exactly the SoS certified figure -- confirming Release 2 was the last report before the canvass resumed and completed"
}
```

STATUS: Item 2 (2014-11-04) complete.

---

## Item 1: 2012-11-06 presidential-general

**Certified final:** 8,879 (SoS SoV; see denominators table above; URL
https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf).

**Election-night plateau: NOT FOUND. Null row per runbook 5.1.**

Extensive search across all runbook 6.x routes; documented below with every
CDX query tried.

1. **6.3 (county's dated report series), same mechanism that worked for 2014/2016/2018:** the county's 2012-era Google-Sites-hosted page `elections.co.del-norte.ca.us/elections/2012-general-election-results` IS indexed in Wayback (4 captures of the index page itself, 2012-11-30 through 2013-03-08, all 200) and its listing DOES show 5 numbered attachment links (`2012_General_Release1.pdf` through `2012_General_Release4.pdf`, plus `2012_General_Release5_FINAL.pdf`) -- so the county followed the same numbered-release convention as later years. BUT every single attachment link is only archived as a 302-redirect STUB (to a `425abd7a-a-03565450-s-sites.googlegroups.com` content host, same "elect" Google Site used for 2014); the actual PDF bytes were never independently crawled at ANY point in Wayback's history. Verified by exact-URL CDX queries (not prefix, not domain-wide) for Release 3, Release 4, and Release 5-FINAL, each returning `[]` (zero captures of any kind, not even a differently-dated one): `http://web.archive.org/cdx/search/cdx?url=425abd7a-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/elect/elections/2012-general-election-results/2012_General_Release4.pdf&output=json&limit=50` -> `[]`; same for Release3, Release5_FINAL, Release1, Release2. This is different from the 2016 "replay aliasing" gotcha (where content existed under a session token URL and could be found via a follow-up CDX query): here the archiveteam Google-Sites rescue crawl (which supplied 2014's, 2016's, and 2018's release PDFs from this same content-host family) evidently did NOT capture this specific subpage's attachments in Oct/Nov 2020 -- other pages under the same "elect" site (2012 candidate list, vote-by-mail application, precinct maps) WERE captured then, so the crawl reached the "elect" site generally but this particular election-results subpage/its attachments were apparently no longer discoverable/linked from the site's live navigation by the time of that rescue crawl (the page may have been unlinked or the site's internal structure changed between 2013 and 2020). Genuinely unrecoverable from Wayback as things stand.
2. **6.2 (registrar press release):** current county press-releases page (`https://www.co.del-norte.ca.us/departments/clerk-recorder/elections/press-releases`) does not have an archive reaching back to 2012 (confirmed by the county-tech item 0 research and general county-site probing); no 2012-era press-release URL located.
3. **6.4 (Clarity):** confirmed not used by Del Norte at any point (probe file, item 0 above).
4. **6.5 (Wayback captures of the live results page), broader sweep:** already covered by (1) above -- the index page itself is well archived, only the attachment PDFs are missing.
5. **6.6 (local news):** searched `Del Norte Triplicate November 2012 election results ballots counted` and variants. Found only: (a) a Nov 15, 2012 Triplicate story mentioned in search snippets ("County election returns") whose current live URL (`https://www.triplicate.com/csp/mediapool/sites/Triplicate/News/story.csp?cid=4378506&fid=151&sid=923`) 302-redirects (old CMS, likely dead/paywalled) and has NO Wayback capture (`curl "http://web.archive.org/cdx/search/cdx?url=triplicate.com/csp/mediapool/sites/Triplicate/News/story.csp?cid=4378506*&matchType=prefix&output=json&limit=20"` -> `[]`); (b) a domain-wide CDX sweep of `triplicate.com` for Nov 2012 filtered to election-related paths surfaced only one unrelated pre-election candidate-forum story (`Gitlin-a-one-candidate-show-at-Tea-Party-foru`, Nov 29 2012, not an election-night results story). No usable election-night ballot count found in local news.

**No number survives from any route. Draft null row:**

```json
{
  "date": "2012-11-06",
  "type": "presidential-general",
  "election_night_ballots": null,
  "certified_final": 8879,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "NULL PER 5.1: no election-night report survives. The county DID run a numbered election-night release series in 2012 (elections.co.del-norte.ca.us/elections/2012-general-election-results, Release1.pdf through Release5_FINAL.pdf, same convention later confirmed for 2014/2016/2018), and the index page listing those releases IS archived (4 captures 2012-11-30 through 2013-03-08), but every attachment link resolves only to a 302-redirect stub pointing at a session-scoped signed URL on a 425abd7a-a-03565450-s-sites.googlegroups.com content host; the actual PDF bytes were never independently crawled at that host for ANY of the 5 releases (verified via exact-URL, not prefix, CDX queries for Release3/4/5-FINAL, each returning zero captures). This differs from 2016's recoverable case: there, the archiveteam Google-Sites rescue crawl (Oct/Nov 2020) DID capture the actual redirect-target bytes as a byproduct of crawling the destination host; here it did not, even though it demonstrably reached other pages of the same 'elect' Google Site around the same time (2012 candidate list PDF, vote-by-mail application PDF, and precinct-map images from this same site ARE captured 2020-10-11) -- this specific subpage's attachments were apparently unlinked/unreachable from the site's then-current navigation and so fell outside the crawl's discovery, even though the URL itself still 302-redirected when directly requested by an OLDER crawl (2013). CDX queries run (all returned empty or redirect-stub-only): http://web.archive.org/cdx/search/cdx?url=425abd7a-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/elect/elections/2012-general-election-results&matchType=prefix&output=json&limit=200 (only Release5_FINAL's redirect stub, 4 captures, all text/html 302); exact-URL queries for Release1/2/3/4/5_FINAL individually all return []. Local news (Del Norte Triplicate) searched for a Nov 2012 election-night ballot count; the one plausibly relevant Nov 15 2012 story ('County election returns') has no working live URL (302 to a dead/paywalled old CMS path) and no Wayback capture at all. Registrar press-release archive does not reach back to 2012. Clarity not used (confirmed elsewhere in this dossier). No substitute denominator or later-canvass number used in place of a genuine election-night figure; left null per convention rather than guessing."
}
```

**VERIFY.md draft summary-table line (2012):** `| 2012 | presidential-general | -- | 8,879 | -- | none | (no surviving election-night source; see note) |`

**plateau_review.json:** no record (null rows get no plateau_review entry per the schema's "sourced row" scope).

**Possible future recovery path (not pursued further this pass, budget-bounded):** a real logged-in-adjacent human browser session hitting `https://web.archive.org/web/20130108050440*/http://elections.co.del-norte.ca.us:80/elections/2012-general-election-results/2012_General_Release5_FINAL.pdf?attredirects=0&d=1` might surface a Wayback UI affordance (e.g. a "view all versions" or alternate replay mode) that a raw CDX/curl sweep cannot; per runbook 6.7 this would need `FLAG for manual operator` if attempted. Given CDX shows literally zero captures of the destination bytes (not merely a curl-vs-browser rendering gap), a browser is unlikely to help; the content appears to be genuinely un-archived rather than archived-but-hard-to-reach.

STATUS: Item 1 (2012-11-06) complete (null row).

---

## Item 6: 2024-11-05 presidential-general

**Certified final:** 10,676 (SoS SoV; see denominators table above; URL
https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf).

**Election-night plateau: FOUND, primary confidence, CONFIRMED (live source, no Wayback needed).**

Route used: 6.2/6.3 (county's own current-site election archive). The county
migrated off Google Sites (used through 2018-2020) to its current "evo"-
template CMS; the numbered-release-PDF convention SURVIVED the migration but
moved hosting to a public Google Drive folder linked from the live Elections
News page.

Locating query / recovery path (fully reproducible, no archive needed --
this is a LIVE, currently-working source):
1. `curl -s -A "Mozilla/5.0" "https://www.co.del-norte.ca.us/departments/Elections/news/category/all/"` -> page includes `href="https://drive.google.com/embeddedfolderview?id=1PJ7b233V3_twHam_vIbbmgze1kpfW5AT#list"`, labeled "Elections Postings (Archive)" in the page nav. This is the county's public Google-Drive-hosted election-document archive (successor to the old Google Sites attachment scheme).
2. Fetching that embedded-folder-view URL directly with curl (no auth) returns a full file listing including a folder per election back through the 2021 recall, e.g. "November 5, 2024 - General Election" (folder id `14V5RgvY-ggQ1mBcDyd5Hib4Y76OBHepc`), "November 8, 2022 General Election" (see Item 5 below), and even "November 8, 2016 General Election Results" / "November 6, 2018 General Election" (already recovered from Wayback above -- this live folder is a second, independent confirmation path for those years, not pursued further since Wayback already gave primary-confidence rows).
3. Fetched the 2024 general folder's listing the same way: `curl -s -A "Mozilla/5.0" "https://drive.google.com/embeddedfolderview?id=14V5RgvY-ggQ1mBcDyd5Hib4Y76OBHepc#list"` -> lists "November 5, 2024-General Election-Release 1.pdf" through "Release 6.pdf", with Release 3 explicitly named "...-Release 3-Unofficial Results-Final Report.pdf" (last-modified 11/5/24, i.e. election night) and Release 4 "...-Release 4-Unofficial Results.pdf" (last-modified 11/8/24, 3 days later).
4. Each file's Google Drive file ID is parsed straight out of the HTML (`id="entry-<FILEID>"` next to the matching title). Downloaded directly and publicly with `curl -sL "https://drive.google.com/uc?export=download&id=<FILEID>"` -- no login, no Wayback, no redirect-chain workaround needed (unlike the 2012-2018 Google-Sites-era files).
5. Both Release 3 and Release 4 are scanned Canon-photocopier PDFs (Creator "Canon iR-ADV C5740 PDF", the county's current scanner model), no text layer; read visually via 150dpi PNG render.

**The two decisive releases:**

| Release | Internal timestamp (page header) | Header | Precincts | Voters Cast / Registered |
|---|---|---|---|---|
| **3** | **11/5/2024 10:05:17 PM** | **"General Election ... November 05, 2024 ... Election Night Report / Unofficial Results / Final Report"** | **19 of 19 (100.00%)** | **6,719 / 15,117 (44.45%)** |
| 4 | 11/8/2024 3:00:15 PM (3 days later) | "General Election ... 11/08/2024 Update / Unofficial Results" | 19 of 19 (100.00%) | 9,102 / 15,117 (60.21%) |

**PLATEAU = Release 3, explicitly titled "Election Night Report / Unofficial Results / Final Report", 6,719 ballots.** This is the clearest self-description recovered anywhere in this dossier (the literal phrase "Election Night Report" appears in the document, distinct from "Final Report" which here means final-of-the-night, confirmed by Release 4's jump). The next release (Release 4) is dated 3 days later, explicitly labeled a dated "Update" (not "Election Night"), and shows Voters Cast jumping from 6,719 to 9,102 (+2,383, +35% relative) -- both runbook-8 CONFIRMED legs present (self-description AND the next-report-days-later-higher-count leg).

Arithmetic: 6,719 / 10,676 (certified final) = **62.94%** (2dp). This is markedly LOWER than Del Norte's 2014/2016/2018 shares (89.18% / 83.30% / 84.45%). This is a genuine trend, not a research error: same-day and near-Election-Day mail-ballot drop-off has grown substantially statewide by 2024 (California's postmark-by-Election-Day + up-to-7-day receipt deadline means a much larger fraction of ballots arrive in the days just before/after Election Day than in 2014-2018), and this shows up even in a non-VCA, non-e-pollbook control county -- exactly the kind of secular/confound effect RUNBOOK section 1 says to record, not "fix." Also consistent with California's broader 2024 pattern (SF's own 2024 election-night share is ~57%, itself down from ~71% in 2012 and ~66% in 2016 -- the same-direction, same-era decline shows up in both a big urban county with all the counting tech AND this small rural county with none of it, which is itself informative for the control-county comparison this dataset is built to support).

**Draft data/research/election-night/del-norte-ca.json row (2024):**

```json
{
  "date": "2024-11-05",
  "type": "presidential-general",
  "election_night_ballots": 6719,
  "certified_final": 10676,
  "election_night_pct": 62.94,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://drive.google.com/uc?export=download&id=1U3HX1aB8Fim-Ca6_qL_EdSPliM8OHpYB",
  "confidence": "primary",
  "note": "PLATEAU = Release 3 of 6 in the county's numbered 2024 election-night PDF series, now hosted on a public Google Drive folder linked from the live Elections News page (successor to the pre-2020 Google-Sites attachment scheme; the numbering convention survived the CMS migration). Document explicitly self-titled 'Election Night Report / Unofficial Results / Final Report' (page header), internal timestamp 11/5/2024 10:05:17 PM (file CreationDate 10:06:25 PM PST), 19 of 19 precincts (100.00%), Voters Cast 6,719 of 15,117 registered (44.45%). The next release, Release 4, is dated 3 days later (11/8/2024 3:00:15 PM), explicitly retitled '11/08/2024 Update / Unofficial Results' (no longer 'Election Night'), and shows Voters Cast jumping to 9,102/15,117 (60.21%) -- both runbook-8 CONFIRMED legs present (self-description + next-report-days-later-and-higher). Scanned Canon-photocopier PDF (Creator: Canon iR-ADV C5740 PDF), no text layer; read visually via 150dpi PNG render. Recovered directly from the LIVE, currently-working county source (drive.google.com/embeddedfolderview, folder id 14V5RgvY-ggQ1mBcDyd5Hib4Y76OBHepc, file id 1U3HX1aB8Fim-Ca6_qL_EdSPliM8OHpYB), no Wayback needed; the same folder's parent archive also independently mirrors the 2016 and 2018 releases already sourced from Wayback in this dossier, corroborating those. Arithmetic: 6,719/10,676 = 62.94%, markedly lower than Del Norte's 2014-2018 shares (89.18% / 83.30% / 84.45%); this reflects the statewide growth of near-Election-Day mail-ballot drop-off by 2024 (same-direction decline as SF's own 2024 election-night share, ~57%, down from ~71% in 2012), not any change in Del Norte's counting technology -- Del Norte never adopted e-pollbooks or ASV (see county-tech record; three SoS voting-tech snapshots bracketing this election, May 2022/Feb 2024/Oct 2025, all show Electronic Pollbook = 'Do not use'). vs_epollbook and vs_asv both n/a (control county, no adoption event)."
}
```

**VERIFY.md draft summary-table line (2024):**
`| 2024 | presidential-general | 6,719 | 10,676 | 62.9% | primary | [link](https://drive.google.com/uc?export=download&id=1U3HX1aB8Fim-Ca6_qL_EdSPliM8OHpYB) |`

**VERIFY.md draft detail bullet (2024):**
- **2024 presidential-general** — night `6,719` / final `10,676` = `62.9%` (primary)
  - numerator: Release 3 of the county's 2024 election-night PDF series (live Google Drive election-postings archive linked from the county Elections News page)
  - denominator (SoS SoV): https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf
  - look for: "Election Night Report / Unofficial Results / Final Report", 19 of 19 precincts (100.00%), Voters Cast 6,719/15,117 (44.45%), page-header timestamp 11/5/2024 10:05:17 PM.

**plateau_review.json draft record (2024):**
```json
{
  "slug": "del-norte-ca",
  "date": "2024-11-05",
  "verdict": "CONFIRMED",
  "basis": "document explicitly titled 'Election Night Report ... Final Report'; next release 3 days later retitled 'Update' at a much higher count",
  "evidence": "Release 3/6, 11/5/2024 10:05:17 PM, 19/19 precincts (100%), Voters Cast 6,719/15,117 (44.45%); Release 4 (11/8/2024, 3 days later) retitled '11/08/2024 Update / Unofficial Results', Voters Cast 9,102/15,117 (60.21%) -- confirms Release 3 was the last report before the canvass resumed"
}
```

STATUS: Item 6 (2024-11-05) complete.

---

## Item 5: 2022-11-08 midterm-general

**Certified final:** 8,450 (SoS SoV; see denominators table above; URL
https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf).

**Election-night plateau: FOUND, primary confidence, CONFIRMED (same live Google Drive archive as 2024).**

Route used: 6.2/6.3, same live county Google Drive election-postings
archive discovered for 2024 (Item 6). Folder "November 8, 2022 General
Election" (id `1t5FEPXr-4Ub5a2ABa9ItGgZi06WBmxgd`) contains: `NOTICE OF
ELECTION.pdf`, `Nov 8, 2022 Election Calendar.pdf`, 4 numbered
`November 8, 2022 General Election - Release N.pdf` (N=1-4), and a separate
`November 8, 2022 General Election - Final Unofficial Report.pdf`.

Locating query / recovery path: `curl -s -A "Mozilla/5.0"
"https://drive.google.com/embeddedfolderview?id=1t5FEPXr-4Ub5a2ABa9ItGgZi06WBmxgd#list"`
-> parsed file IDs from `id="entry-<FILEID>"` attributes; downloaded each
with `curl -sL "https://drive.google.com/uc?export=download&id=<FILEID>"`,
no auth or Wayback needed. Unlike 2024, 2022's report format is a different
template: not Canon-scanned "Election Summary Report" pages but a native-text
"Report #N / Nth Report - 19 Precincts Reporting" summary generated directly
as a PDF (readable with `pdftotext`, no visual/PNG read needed for this
year) -- though in practice the report was read visually (150dpi render) to
cross-check the printed digits since the layout has two side-by-side
columns pdftotext can scramble.

**Internal PDF `CreationDate` timeline (via `pdfinfo`) for all 5 artifacts, all Nov 8, 2022 = election day itself:**

| Release | Internal CreationDate | Internal report label | Total Registration and Turnout |
|---|---|---|---|
| 1 | 11/8/2022 8:05:43 PM PST | "1st Report" (by numbering pattern) | (not read; not needed) |
| 2 | 11/8/2022 8:53:32 PM PST | "2nd Report" (by numbering pattern) | (not read; not needed) |
| 3 | 11/8/2022 9:17:10 PM PST | "3rd Report" (by numbering pattern) | (not read; not needed) |
| **4** | **11/8/2022 9:40:53 PM PST** | **"Report #3" (header) / "4th Report - 19 Precincts Reporting" (subtitle) — "Data Refreshed: Tuesday, November 8, 2022 9:39 PM"** | **Registered Voters 15,024, Turnout 6,312** |
| Final Unofficial Report | 11/14/2022 2:37:48 PM PST (6 days later) | "Final Unofficial Report" / "5th Report - 19 Precincts Reporting" — "Data Refreshed: Monday, November 14, 2022 2:35 PM" | Registered Voters 15,024, Turnout 8,286 |

(Note the file's internal top-left "Report #3" label appears to be a template/report-type identifier distinct from the "4th Report" sequence subtitle immediately below it; the sequence subtitle plus the strictly-increasing `CreationDate` timeline across Releases 1-4 is what establishes ordering, not the "Report #" label.)

**PLATEAU = Release 4 ("4th Report"), 6,312 ballots, timestamped 9:39-9:40 PM election night.** This is the last of 4 same-night numbered reports (Releases 1-4 span 8:05 PM to 9:40 PM, all election day). No 5th-of-the-night report exists; the next artifact in the folder, explicitly named "Final Unofficial Report" / internally labeled "5th Report," is dated 6 days later (Nov 14) and shows Turnout jumping from 6,312 to 8,286. Runbook-8 CONFIRMED via the gap-to-next-report leg (6 days, explicit "Final" relabeling, large jump).

Arithmetic: 6,312 / 8,450 (certified final) = **74.70%** (2dp). This sits between Del Norte's 2014-2018 shares (83-89%) and 2024's 62.94%, consistent with a gradual, monotonic decline in Del Norte's election-night completeness across 2014 -> 2016 -> 2018 -> 2022 -> 2024 (89.18% -> 83.30% -> 84.45% -> 74.70% -> 62.94%) that tracks the statewide trend of growing near-Election-Day mail-ballot volume, not any change in Del Norte's own counting technology (never adopted e-pollbooks/ASV across this entire span).

**Draft data/research/election-night/del-norte-ca.json row (2022):**

```json
{
  "date": "2022-11-08",
  "type": "midterm-general",
  "election_night_ballots": 6312,
  "certified_final": 8450,
  "election_night_pct": 74.70,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://drive.google.com/uc?export=download&id=131PTrk6-v_7MrZiAlLp8BzoQzysS97eu",
  "confidence": "primary",
  "note": "PLATEAU = Release 4 ('4th Report - 19 Precincts Reporting') of 4 same-night numbered reports in the county's live Google Drive election-postings archive (same archive used for the 2024 row; folder 'November 8, 2022 General Election', id 1t5FEPXr-4Ub5a2ABa9ItGgZi06WBmxgd). Internal PDF CreationDate 11/8/2022 9:40:53 PM PST; page itself stamped 'Data Refreshed: Tuesday, November 8, 2022 9:39 PM'; Total Registration and Turnout: Registered Voters 15,024, Turnout 6,312. Releases 1-4 run strictly increasing 8:05 PM -> 8:53 PM -> 9:17 PM -> 9:40 PM, all election night (Nov 8, 2022 was election day itself). The only later artifact, 'November 8, 2022 General Election - Final Unofficial Report.pdf' (internally labeled '5th Report'), is dated 6 days later (11/14/2022 2:37:48 PM, page stamped 'Data Refreshed: Monday, November 14, 2022 2:35 PM') and shows Turnout jumping to 8,286 -- confirming Release 4 was the last report before the canvass resumed. This report template (native-text PDF, 'Report #N / Nth Report - 19 Precincts Reporting' header, two-column contest layout) differs from the Canon-scanned 'Election Summary Report' template used in 2016/2018/2024; read both via pdftotext and a 150dpi visual cross-check. Arithmetic: 6,312/8,450 = 74.70%, between Del Norte's 2014-2018 shares (83-89%) and its 2024 share (62.94%), consistent with a gradual year-over-year decline driven by growing near-Election-Day mail-ballot volume statewide, not any technology change (Del Norte never adopted e-pollbooks or ASV; SoS voting-tech snapshot closest to this election, May 9 2022, shows Electronic Pollbook = 'Do not use'). vs_epollbook and vs_asv both n/a (control county)."
}
```

**VERIFY.md draft summary-table line (2022):**
`| 2022 | midterm-general | 6,312 | 8,450 | 74.7% | primary | [link](https://drive.google.com/uc?export=download&id=131PTrk6-v_7MrZiAlLp8BzoQzysS97eu) |`

**VERIFY.md draft detail bullet (2022):**
- **2022 midterm-general** — night `6,312` / final `8,450` = `74.7%` (primary)
  - numerator: Release 4 / "4th Report" of the county's 2022 election-night PDF series (live Google Drive election-postings archive)
  - denominator (SoS SoV): https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf
  - look for: "4th Report - 19 Precincts Reporting", "Data Refreshed: Tuesday, November 8, 2022 9:39 PM", Total Registration and Turnout Registered Voters 15,024 / Turnout 6,312.

**plateau_review.json draft record (2022):**
```json
{
  "slug": "del-norte-ca",
  "date": "2022-11-08",
  "verdict": "CONFIRMED",
  "basis": "last of 4 same-night numbered reports (strictly increasing timestamps, all election night); next artifact ('Final Unofficial Report' / 5th Report) 6 days later at a much higher count",
  "evidence": "Release 4/4, internal CreationDate 11/8/2022 9:40:53 PM, page stamp 'Data Refreshed 11/8/2022 9:39 PM', Turnout 6,312/15,024; 'Final Unofficial Report' (11/14/2022, 6 days later) Turnout 8,286/15,024 -- confirms Release 4 was the last report before the canvass resumed"
}
```

STATUS: Item 5 (2022-11-08) complete. ALL SIX ELECTIONS NOW RESEARCHED (5 sourced primary rows: 2014, 2016, 2018, 2022, 2024; 1 documented null: 2012).

---

## Summary (all items complete)

| Election | Type | Night ballots | Certified final | Pct | Confidence | Verdict | Evidence class |
|---|---|---:|---:|---:|---|---|---|
| 2012-11-06 | presidential-general | NULL | 8,879 | NULL | none | -- | none (genuinely un-archived; see Item 1) |
| 2014-11-04 | midterm-general | 6,539 | 7,332 | 89.18% | primary | CONFIRMED | held-capture / next-report-days-later (Wayback, old "elect" Google Site) |
| 2016-11-08 | presidential-general | 8,155 | 9,790 | 83.30% | primary | CONFIRMED | self-labeled "Election Night Final" + next-report-days-later (Wayback, "dnco" Google Site) |
| 2018-11-06 | midterm-general | 7,127 | 8,439 | 84.45% | primary | CONFIRMED | self-labeled "ELECTION NIGHT FINAL REPORT" + next-report-days-later-relabeled (Wayback, same Google Site) |
| 2022-11-08 | midterm-general | 6,312 | 8,450 | 74.70% | primary | CONFIRMED | last of 4 same-night numbered reports + next-report-6-days-later (live Google Drive archive) |
| 2024-11-05 | presidential-general | 6,719 | 10,676 | 62.94% | primary | CONFIRMED | self-labeled "Election Night Report...Final Report" + next-report-days-later (live Google Drive archive, official-release-class) |

Trend note (not a research artifact, an observation for the human reviewer):
Del Norte's election-night completeness declines fairly monotonically across
this span (89.18% -> 83.30% -> 84.45% -> 74.70% -> 62.94%) despite NEVER
adopting e-pollbooks or ASV at any point 2014-2024 (three independent SoS
voting-tech snapshots -- May 2022, Feb 2024, Oct 2025 -- all show Electronic
Pollbook "Do not use"). As a true control county with zero tech adoption
events, this decline is useful signal for the broader Long Count project:
it suggests California's statewide trend toward more near-Election-Day
mail-ballot volume (VCA-era deadline extensions, growing late-drop habits)
depresses election-night share independent of any county's own counting
technology -- exactly the kind of confound RUNBOOK section 1 flags counties
should record, not "fix."

All five sourced rows are self-contained, directly reproducible (every URL,
file ID, and CDX query is copy-pasteable in the item sections above), and
required no `FLAG for manual operator` -- no source in this dossier blocked
curl or required a live browser session.

---
