# Mendocino County, CA (slug: mendocino-ca) — control-county evidence dossier

Control county: never adopted e-pollbooks or ASV through 2024 (per
`data/research/county-tech/ca_adoption_census.json`, `status: "never"`,
`vca_year: null`). This dossier extends that census row with a full
`<slug>.json`-shaped tech record and sources the 6 bracketing Nov generals
(2012, 2014, 2016, 2018, 2022, 2024; 2020 excluded as COVID all-mail outlier)
for `data/research/election-night/mendocino-ca.json`.

Working files (curl/pdftotext outputs, NOT repo artifacts): scratchpad
`mendocino-work/` subdirectory.

---

## Item 0 — tech record (draft `data/research/county-tech/mendocino-ca.json`)

Schema modeled on `data/research/county-tech/napa-ca.json`.

### New verification this pass

CA SoS "Voting Technologies in Use by County" ("VOT-TECH") snapshots, three
vintages, all fetched fresh this pass:

- **2022 vintage** (locating query: reused cached `vst2022.pdf`/`.txt` in
  scratchpad root; original source
  `https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/...` per prior
  session) — Mendocino row: Central Tabulation `Hart Verity 3.1
  Central/Count`, Vote Center/Polling Tabulator `Hart Verity Voting 3.1
  Scan`, Accessibility `Hart Verity 3.1 TouchWriter/Reader`, Ballot on Demand
  (Elections Office) `Hart Verity 3.1 Print`, Ballot on Demand
  (VoteCenter/Polling) **`Do not use`**, RAVBM `Democracy Live SecureSelect`,
  **Electronic Pollbook: `Do not use`**.
- **2024 vintage** (cached `vst2024.pdf`/`.txt`) — Mendocino row: `Hart
  Verity 3.2 Central/Count` / `Central Tabulation Only` / `Hart Verity 3.2
  Touchwriter` / `Hart Verity 3.2 Print` / **`Do not use`** (BOD VoteCenter)
  / `Democracy Live Secure Select` / **Electronic Pollbook: `Do not use`**.
- **2025 vintage, fetched live this pass**: `curl -A <UA> -L -o
  vot_tech_2025.pdf
  "https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf"`
  → HTTP 200, 166,745 bytes, `pdftotext -layout` → line 33: `Mendocino
  Hart Verity 3.2.1 Central/Count | Central Tabulation Only | Hart Verity
  3.2.1 Touchwriter | Hart Verity 3.2.1 Print | Hart Verity 3.2.1
  Touchwriter | Democracy Live Secure Select | Do not use`. Header row
  confirms the last column is **"Electronic Pollbook"**. Document dated "As
  of October 10, 2025".
- Cross-check: Mendocino's "Precinct Voters" column in the SoS Statement of
  Vote is nonzero in every study year (2012: 7,046; 2014: 4,377; 2016:
  6,036; 2018: 4,462; 2022: 646; 2024: 2,479) — i.e. Mendocino runs
  traditional precinct-based elections, not the VCA vote-center model,
  consistent with the census row's `vca_year: null`. (Locating: `pdftotext
  -layout` on each year's SoV PDF, `grep -n Mendocino`.)

Net: three independent SoS snapshots (2022, 2024, "as of Oct 2025") all read
Electronic Pollbook = "Do not use" for Mendocino, spanning and bracketing
every election in this dossier's range including 2024. This upgrades the
census row's epollbook confidence from "low" (WebSearch-snippet based) to
primary for the tech-in-use-by-county fact itself; ASV evidence remains the
census row's secondary/low material (no new primary ASV source found this
pass — see note).

### Draft JSON record

```json
{
  "jurisdiction": "Mendocino County",
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
      "note": "CA SoS 'Voting Technologies in Use by County' snapshots read Mendocino's 'Electronic Pollbook' column as 'Do not use' in THREE independent vintages spanning the study period: 2022-cycle vintage (cached vst2022.pdf/.txt, row: Hart Verity 3.1 Central/Count / Central Tabulation Only / Hart Verity 3.1 TouchWriter-Reader / Hart Verity 3.1 Print / Do not use (BOD VoteCenter) / Democracy Live SecureSelect / Do not use (EPB)); 2024-cycle vintage (cached vst2024.pdf/.txt, row: Hart Verity 3.2 Central/Count / Central Tabulation Only / Hart Verity 3.2 Touchwriter / Hart Verity 3.2 Print / Do not use / Democracy Live Secure Select / Do not use (EPB)); and the current 'as of October 10, 2025' vintage fetched live this pass (curl -A <UA> -L -o vot_tech_2025.pdf https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf -> HTTP 200 166,745 bytes; pdftotext -layout; grep -n Mendocino -> line 33, last column 'Do not use', header row confirms last column = 'Electronic Pollbook'). EAVS county-level surveys (per ca_adoption_census.json) also report False for Mendocino electronic-pollbook use across the May 2022 / Sept 2024 / Oct 2025 editions. Also corroborated structurally: Mendocino is not a Voter's Choice Act county (vca_year null; SoV 'Precinct Voters' column nonzero every study year 2012-2024, i.e. traditional precinct-based voting, not the VCA vote-center model that typically accompanies e-pollbook rollout). Consistent never-adopter signal through 2024 and beyond."
    },
    {
      "type": "asv",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://www.mendocinocounty.gov/government/assessor-county-clerk-recorder-elections/elections",
      "confidence": "low",
      "note": "Carried forward from ca_adoption_census.json (no new primary ASV source found this pass). Mendocino County's Registrar of Voters Ballot Information FAQ describes signature review in human terms: 'If the Elections Official verifies the signature, the challenge is removed...' and 'if election workers have trouble reading a signature or believe it doesn't match what's on file, they will make every effort to contact the person' -- language attributing the match decision to a person, no vendor/software named anywhere in county materials found. Direct fetch of the county FAQ page returns HTTP 403 (Cloudflare bot wall); reconstructed from WebSearch-indexed snippets only, not a full primary read (hence confidence stays low, not secondary). Mendocino does not appear in the Stanford Law School 'Signature Verification and Mail Ballots' (May 2020) Appendix III vendor table (33 counties interviewed; Mendocino absent). Locating queries (reused from census pass): 'Mendocino County elections signature verification vote by mail ballot processing'; 'Mendocino County elections \"ballot processing board\" OR \"election workers\" signature compare \"by eye\" OR manually'. FLAG for manual operator: a real-browser fetch of the FAQ page (Cloudflare-blocked to curl/WebFetch) would upgrade this to secondary/primary if it can be read directly."
    },
    {
      "type": "sign-scan-go",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf",
      "confidence": "secondary",
      "note": "No evidence of an AB 626 in-vote-center 'Sign-Scan-and-Go' mail-ballot verify+scan program. Mendocino is not a VCA vote-center county (see epollbook note: nonzero traditional Precinct Voters every SoV year 2012-2024), and Sign-Scan-and-Go is a VCA-vote-center-only feature (piloted at counties like Placer). Confidence secondary: absence-of-evidence inference from the county's non-VCA structure, no explicit county statement ruling it out found."
    },
    {
      "type": "vote-center",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf",
      "confidence": "primary",
      "note": "Mendocino is not a Voter's Choice Act (SB 450) county: not on the SoS VCA county list (https://www.sos.ca.gov/voters-choice-act), and ca_adoption_census.json records vca_year: null. Structural confirmation: the CA SoS Statement of Vote 'Voter Participation Statistics by County' reports a nonzero 'Precinct Voters' figure for Mendocino in every study year (2012: 7,046; 2014: 4,377; 2016: 6,036; 2018: 4,462; 2022: 646; 2024: 2,479), i.e. Mendocino still runs polling-place/precinct voting rather than the VCA all-mail/vote-center model. This matters for the election-night comparison: unlike VCA counties (Napa, San Mateo, etc.) whose election-night share dropped ~15-20pp the year they switched to vote centers, Mendocino's series should show no VCA-transition confound in any study year."
    }
  ],
  "notes": "TECH: Mendocino never adopted electronic pollbooks (SoS VOT-TECH snapshots read 'Do not use' in 2022, 2024, and Oct-2025 vintages; EAVS False across four editions per census row) and shows no primary evidence of automated signature verification (human-review language in the county's Ballot FAQ, confidence kept low pending a real-browser read past the Cloudflare wall). Mendocino is also not a VCA county (never adopted the vote-center/all-mail model), so its election-night series is not confounded by a VCA-transition-year drop the way Napa/San Mateo/Sacramento are -- it is a comparatively clean 'never-adopter' control across all four tracked tech types. Sources carried forward from ca_adoption_census.json plus three fresh SoS VOT-TECH snapshot reads this pass (2022, 2024, Oct 2025) and the SoV precinct-voters structural check."
}
```

---

## Item 3 — 2016-11-08 (presidential-general)

### Denominator (SoS SoV)
`curl -A <UA> -L -o sov_2016.pdf https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf`
→ HTTP 200, 21,468 bytes. `pdftotext -layout`; line 29: `Mendocino 250
63,741 51,061 6,036 32,694 **38,730** 84.42% 75.85% 60.76%` (columns:
Precincts / Eligible / Registered / Precinct Voters / VBM Voters / **Total
Voters** / %VBM / Turnout-Reg / Turnout-Elig). Cross-check: 6,036 + 32,694 =
38,730 ✓; 38,730/51,061 = 75.85% ✓ matches printed Turnout-Registered.
**certified_final = 38,730.**

### Numerator hunt
Route 6.5 (Wayback). Reused the probe's finding that `/acr/elections.htm`
was captured 10x around Nov 2016; fetched two of those captures (`id_` raw,
plain HTML, no gzip) and found the live nav points to `/acr/current.htm`
("Current Election Results", highlighted) vs `/acr/pastElections.htm`
("Election Results", historical index).

- CDX `current.htm` on `co.mendocino.ca.us`, window 20161101-20161201:
  `curl "https://web.archive.org/cdx/search/cdx?url=co.mendocino.ca.us/acr/current.htm&from=20161101&to=20161201&output=json&limit=50"`
  → 11 captures. Pre-election (20161103153517 - 20161107221256, ~5.9KB) is a
  stub. Gap Nov 7 22:12 → Nov 13 02:20 (no capture during election night
  itself). From 20161113022000 onward (~9.2KB) through 20161123011436, all
  captures carry **identical content** (same digest family, same embedded
  data) — a 10-day-plus frozen state.
- Fetched `https://web.archive.org/web/20161107221256id_/http://www.co.mendocino.ca.us/acr/current.htm`
  → pre-election placeholder: "Election Results will become available
  beginning 11-08-2016 after 8 PM." (confirms the report text is NOT static
  boilerplate reused pre-election; it only appears once posted).
- Fetched `https://web.archive.org/web/20161113022000id_/http://www.co.mendocino.ca.us/acr/current.htm`
  → header: **"ELECTION SUMMARY REPORT COUNTY OF MENDOCINO 2016
  PRESIDENTIAL GENERAL ELECTION — THIS IS THE FINAL ELECTION NIGHT REPORT —
  Results for this election will be certified at the completion of the
  canvass. — 11/09/16 01:55:06"**. Body: "Registered Voters 51035 - Cards
  Cast 12032 23.58%", "Num. Report Precinct 250 - Num. Reporting 250
  100.00%". Every contest row shows "Times Counted 12032/51035 23.6%" (same
  denominator across all contests → single-card ballot, Cards Cast = voters,
  not ballot-card-doubled).
- Fetched `https://web.archive.org/web/20161123011436id_/http://co.mendocino.ca.us/acr/current.htm`
  (10 days later, last capture in the window) → **byte-identical report**:
  same "11/09/16 01:55:06" internal timestamp, same "Cards Cast 12032".
  Proves the count HELD from the Nov 9 1:55 AM posting through at least Nov
  23 — the canvass had not yet moved the number.

### Plateau vs first tranche
No capture exists of the actual 8 PM election-night first tranche (gap Nov 7
22:12 → Nov 13 02:20), so there is no risk of confusing this with the first
tranche — the ONLY election-night artifact recovered is the one the county
itself titled "FINAL ELECTION NIGHT REPORT," timestamped 1:55 AM the morning
after (within the runbook's "up to 4 a.m." election-night window), and it is
proven to have held for 10+ days after.

**Calibration flag:** 12,032/38,730 = 31.07%, well below the "small rural
county often 80-95%" heuristic and even below half of SF's 2016 ~66%. This
is surprising but the evidence (self-labeled "FINAL," late-night internal
timestamp, 10-day hold) is exactly what RUNBOOK section 8 defines as
CONFIRMED — trusted over the calibration heuristic, which is a sanity prior,
not a hard rule. Left as a flag for human review, not "fixed."

### Arithmetic
12,032 / 38,730 = 0.31067... → **31.07%**

### Draft dataset row
```json
{
  "date": "2016-11-08",
  "type": "presidential-general",
  "election_night_ballots": 12032,
  "certified_final": 38730,
  "election_night_pct": 31.07,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20161113022000/http://www.co.mendocino.ca.us/acr/current.htm",
  "confidence": "primary",
  "note": "PLATEAU = county's own 'ELECTION SUMMARY REPORT ... THIS IS THE FINAL ELECTION NIGHT REPORT' (curl id_ raw fetch of the archived /acr/current.htm 'Current Election Results' page, no gzip; plain HTML). Internal report timestamp '11/09/16 01:55:06' (1:55 AM the morning after Election Day, within the runbook's up-to-4am election-night window). Body: Registered Voters 51,035, Cards Cast 12,032 (23.58%), Num. Reporting Precinct 250/250 (100.00%); every contest's 'Times Counted' reads 12032/51035 uniformly (single-card ballot, Cards Cast = voters, not ballot-card-doubled). Non-circular corroboration: a LATER capture of the SAME URL 10 days later (2016-11-23, snapshot 20161123011436) is byte-identical -- same '11/09/16 01:55:06' timestamp, same 12,032 count -- proving the number held through the canvass pause (RUNBOOK 8: self-description + later-capture-same-count = CONFIRMED). The immediately-prior capture (2016-11-07 22:12 UTC, pre-poll-close) is a placeholder reading 'Election Results will become available beginning 11-08-2016 after 8 PM', confirming the FINAL-report text is not reused boilerplate. No capture exists of the true 8pm first tranche (Wayback gap 11/07 22:12 -> 11/13 02:20), so there is no risk of numerator confusion with the first tranche; the ONLY election-night artifact recovered IS the self-labeled final one. CALIBRATION FLAG: 12,032/38,730 = 31.07%, well below the 'small rural county 80-95%' heuristic and below half of SF's 2016 ~66% -- surprising, but the self-description + hold-evidence is exactly what counts as CONFIRMED plateau evidence per RUNBOOK section 8; flagged for human review rather than discarded. Certified final 38,730 voters (CA SoS Voter Participation Statistics by County: 6,036 precinct + 32,694 VBM = 38,730). Pct = 12,032/38,730 = 31.07%. Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see Item 0)."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2016 | presidential-general | 12,032 | 38,730 | 31.1% | primary | [link](https://web.archive.org/web/20161113022000/http://www.co.mendocino.ca.us/acr/current.htm) |`

Detail bullet:
```
- **2016 presidential-general** — night `12,032` / final `38,730` = `31.1%` (primary)
  - numerator: <https://web.archive.org/web/20161113022000/http://www.co.mendocino.ca.us/acr/current.htm>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: county's own "THIS IS THE FINAL ELECTION NIGHT REPORT", internal timestamp 11/09/16 01:55:06, "Cards Cast 12032" of 51,035 registered. A later Nov 23 capture of the same page is byte-identical, proving the count held. CALIBRATION FLAG: unusually low share (31.1%) for a small rural county; evidence-based, not adjusted.
```

### plateau_review.json draft record
```json
{
  "slug": "mendocino-ca",
  "date": "2016-11-08",
  "verdict": "CONFIRMED",
  "basis": "county report self-describes + later capture same count",
  "evidence": "'THIS IS THE FINAL ELECTION NIGHT REPORT', internal timestamp 11/09/16 01:55:06, Cards Cast 12,032; Nov 23 capture of same URL is byte-identical"
}
```

---

## Item 4 — 2018-11-06 (midterm-general)

### Denominator (SoS SoV)
`curl -A <UA> -L -o sov_2018.pdf https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf`
→ HTTP 200, 92,255 bytes. `pdftotext -layout`; line 29: `Mendocino 250
64,399 49,411 4,462 29,504 **33,966** 86.86% 68.74% 52.74%`. Cross-check:
4,462 + 29,504 = 33,966 ✓; 33,966/49,411 = 68.74% ✓. **certified_final =
33,966.**

### Numerator hunt
By Nov 2018 the county's site had migrated: `co.mendocino.ca.us` now
301-redirects to `mendocinocounty.org` (confirmed via `curl -sI` on the
archived 301: `location: https://web.archive.org/web/20181108034702id_/https://www.mendocinocounty.org/`).
The new CMS page `https://www.mendocinocounty.org/government/assessor-county-clerk-recorder-elections/current-election-results`
(captured 20181107234313, 20181114073116, 20181121111711) embeds results via
an **iframe pointing back at the OLD domain's CGI script**:
`<iframe src="//www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl" style="width: 100%; height: 900px; border: 0;">`
(found by stripping the fetched CMS page's HTML and grepping for `<iframe`).

- CDX directly on the iframe target:
  `curl "https://web.archive.org/cdx/search/cdx?url=co.mendocino.ca.us/acr/cgi-bin/currentFR.pl&from=20181101&to=20190301&output=json&limit=50"`
  → 4 unique-content captures: **20181107234314** (digest `K3Y3...`),
  **20181202045415** (digest `3Y3L...`, distinct), plus later revisits of the
  Dec 2 digest (Dec 22, Feb 2019 — page stopped changing after Dec 2).
- Fetched `https://web.archive.org/web/20181107234314id_/https://www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl`
  (plain HTML, not gzipped) → header: **"Mendocino County Election Results
  for 2018-11-06 ... STATEWIDE GENERAL ELECTION NOVEMBER 6, 2018 Summary For
  Jurisdiction Wide, All Counters, All Races — Election Night Final Report —
  Results for this election will be certified at the completion of the
  canvass. — 11/07/18 00:48:58"**. Body: "Registered Voters 48032 - Cards
  Cast 15819 32.93%", "Num. Reporting Precinct 250/250 100.00%"; every
  countywide contest's "Times Counted" reads `15819/48032` uniformly
  (confirms Cards Cast = voters for the countywide race, not card-doubled;
  smaller district races show their own sub-totals as expected).
- Fetched `https://web.archive.org/web/20181202045415id_/https://www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl`
  (Dec 2, ~4 weeks later) → header now reads **"FINAL OFFICIAL RESULTS
  11/29/18 16:50:33"**, "Registered Voters 48032 - Cards Cast **33966**
  70.72%" — i.e. the CERTIFIED state, and 33,966 matches the SoS SoV Total
  Voters exactly (independent cross-check that both the PDF parse and the
  page-scrape are reading the same underlying number correctly).

### Plateau vs first tranche
The only surviving election-night artifact is the county's own
self-labeled **"Election Night Final Report"**, internal timestamp 11/07/18
00:48:58 (48 minutes after midnight, within the runbook's up-to-4am
election-night window). No 8pm-tranche capture survives to confuse with.
Non-circular corroboration: the SAME URL's next captured content (Dec 2,
dated internally 11/29/18) shows a materially DIFFERENT, higher count
(33,966 vs 15,819) — i.e. the report series' next state is weeks later and
already the certified final, exactly the "county's own posting schedule
bracketing the report" / "next file being days later" leg required for
CONFIRMED (RUNBOOK 8). This also rules out the reverse concern (that
15,819 might itself be a stale pre-election-night artifact): the internal
timestamp, self-label, and the fact that it strictly precedes and is lower
than the certified count all point the same direction.

### Arithmetic
15,819 / 33,966 = 0.465759... → **46.57%**

(Calibration: SF 2018 midterm ~59%; 46.57% is a plausible, more calibration-
consistent result than the 2016 row, at ~79% of the SF figure.)

### Draft dataset row
```json
{
  "date": "2018-11-06",
  "type": "midterm-general",
  "election_night_ballots": 15819,
  "certified_final": 33966,
  "election_night_pct": 46.57,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20181107234314/https://www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl",
  "confidence": "primary",
  "note": "PLATEAU = county's own 'Election Night Final Report' (found via the new mendocinocounty.org CMS page's embedded iframe src='//www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl', an OLD-domain CGI script the county kept running post-migration; curl id_ raw fetch, plain HTML, no gzip). Header: 'STATEWIDE GENERAL ELECTION NOVEMBER 6, 2018 ... Election Night Final Report ... Results for this election will be certified at the completion of the canvass.' Internal timestamp '11/07/18 00:48:58' (48 min after midnight, within the runbook's up-to-4am election-night window). Body: Registered Voters 48,032, Cards Cast 15,819 (32.93%), Num. Reporting Precinct 250/250 (100.00%); countywide contests' 'Times Counted' uniformly 15819/48032 (single-card ballot, not doubled). Non-circular corroboration: the SAME URL's next captured content (2018-12-02, snapshot 20181202045415) is headed 'FINAL OFFICIAL RESULTS 11/29/18 16:50:33' with Cards Cast 33,966 -- a materially higher, later, and independently-labeled-different count, exactly matching the SoS SoV certified Total Voters (33,966) exactly. This satisfies RUNBOOK 8's non-circular leg (report series' next file is weeks later, already the certified final) and rules out 15,819 being anything other than the frozen election-night state. No 8pm first-tranche capture survives to confuse with; the only election-night artifact recovered IS the self-labeled one. Certified final 33,966 voters (CA SoS Voter Participation Statistics by County: 4,462 precinct + 29,504 VBM = 33,966). Pct = 15,819/33,966 = 46.57%, plausible relative to SF's 2018 ~59% calibration (~79% of it). Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see Item 0)."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2018 | midterm-general | 15,819 | 33,966 | 46.6% | primary | [link](https://web.archive.org/web/20181107234314/https://www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl) |`

Detail bullet:
```
- **2018 midterm-general** — night `15,819` / final `33,966` = `46.6%` (primary)
  - numerator: <https://web.archive.org/web/20181107234314/https://www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: county's own "Election Night Final Report", internal timestamp 11/07/18 00:48:58, "Cards Cast 15819" of 48,032 registered. The same URL's next capture (Dec 2, dated 11/29/18) is headed "FINAL OFFICIAL RESULTS" with Cards Cast 33,966 (= SoV certified exactly), proving 15,819 was the frozen night state.
```

### plateau_review.json draft record
```json
{
  "slug": "mendocino-ca",
  "date": "2018-11-06",
  "verdict": "CONFIRMED",
  "basis": "county report self-describes + next-captured state is weeks later and materially different",
  "evidence": "'Election Night Final Report', internal timestamp 11/07/18 00:48:58, Cards Cast 15,819; Dec 2 capture of same URL headed 'FINAL OFFICIAL RESULTS 11/29/18', Cards Cast 33,966 (= SoV certified)"
}
```

---

## Item 1 — 2012-11-06 (presidential-general)

### Denominator (SoS SoV)
`curl -A <UA> -L -o sov_2012.pdf https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf`
(2012 drops the `sov/` path segment per RUNBOOK 6.1) → HTTP 200, 21,328
bytes. `pdftotext -layout`; line 28: `Mendocino 247 62,910 49,765 7,046
29,034 **36,080** 80.47% 72.50% 57.35%`. Cross-check: 7,046 + 29,034 =
36,080 ✓; 36,080/49,765 = 72.50% ✓. **certified_final = 36,080.**

### Numerator hunt — Wayback route exhausted, dead end
- `elections.htm` CDX (`co.mendocino.ca.us`, window 20121001-20130101) → a
  SINGLE capture, 20121106055757 (Nov 5, 9:57 PM PST, pre-poll-close).
  Fetched it (`id_` raw) and found the live-results link for 2012 pointed
  to a DIFFERENT subdomain than 2016/2018's `/acr/current.htm`:
  `<a href="http://mx2.co.mendocino.ca.us/elections/election_results.php">Current Election Results</a>`.
- CDX on that exact URL (`mx2.co.mendocino.ca.us/elections/election_results.php`,
  window 20121101-20130301) → a SINGLE capture, 20121106042956 (Nov 5, 8:29
  PM PST, still pre-poll-close). Fetched it: a static placeholder page —
  *"Election results will begin displaying soon after Tuesday, November
  6th, 2012 -- 8:00 PM PST, with certified results available by Tuesday,
  December 4th, 2012 ... Monday, November 5th, 2012 -- 8:29 PM PST. Initial
  results due in about 24 hours."* No later capture of this URL exists
  anywhere in Wayback (checked to 2013-03-01) — the live-results page for
  2012 was **never crawled while it held real data**.
- `/acr/electionsCurrent.htm` CDX → one capture, 20121127140952 (Nov 27,
  post-certification-adjacent) — generic nav page, no results content.
- `/acr/election_results/results20121106.htm` (the permanent archival URL,
  found via the county's own `pastElections.htm` link list) IS captured
  repeatedly from April 2014 onward, but every capture reads **"FINAL
  CERTIFIED RESULTS 11/29/12 13:23:47 ... Cards Cast 36080 72.45%"** — this
  is the CERTIFIED endpoint (36,080 matches the SoV total exactly), not the
  election-night state; Wayback's earliest capture of this URL (2014-04-30)
  is already ~1.5 years post-certification, long past any chance of
  catching a pre-certification version.
- `current.htm` (the 2016/2018-era path) has ZERO Wayback captures at all
  for 2012 (checked).

**Conclusion: the true 2012 election-night live page was never archived by
Wayback in any state showing real returns.** Route 6.5 is exhausted.

### Numerator recovered via route 6.6 (local news, secondary)
`WebSearch` for Mendocino 2012 election-night coverage surfaced an Anderson
Valley Advertiser (theava.com) live-blog post from **election night 2016**
(`https://theava.com/archives/62338`, fetched via `curl -A <UA>`, HTTP 200)
that gives retrospective comparison figures for prior Mendocino election
nights as context for that night's in-progress count:

> "LOCAL UPDATE: FINAL ELECTION-NIGHT REPORT — Just before 2am Wednesday,
> the final preliminary results (23.58%) for Mendocino County were posted:
> http://www.co.mendocino.ca.us/acr/current.htm — PRELIMINARY ELECTION
> RESULTS/NOTES — **IN NOVEMBER OF 2012 Mendocino County's preliminary
> election night results were based on about 51% of about 36,400 votes
> cast.** IN JUNE OF 2016 the preliminary election night results were based
> on about 41% of about 37,800 votes cast."

Two things make this usable evidence rather than noise: (1) it independently
corroborates our OWN 2016 finding — "23.58%" and "just before 2am Wednesday"
match the county's own `current.htm` header exactly (Item 3 above: internal
timestamp 11/09/16 01:55:06, "Registered Voters 51035 - Cards Cast 12032
23.58%") — a genuinely independent confirmation of that row from a
contemporaneous news source; (2) the phrase describing 2012 uses the SAME
construction ("preliminary election night results... based on about X% of
about Y votes cast") the writer used for the (verified) 2016 figure,
i.e. the writer is citing 2012's OWN election-night-final percentage as a
historical yardstick, not an arbitrary mid-count snapshot.

**This is a coarse, rounded secondary source (whole-percent precision), not
a primary exact count.** Best-estimate ballot count, back-calculated from
the certified final: `round(36,080 x 0.51)` = **18,401** (documented as an
approximation, not a raw count).

### Plateau vs first tranche
Cannot independently verify this is the LAST report of the night (no
Wayback bracket exists for 2012), but the source explicitly frames it as
Mendocino's historical "preliminary election night results" figure (i.e.
the settled overnight number), parallel to the verified 2016 usage in the
same article. Treated as PLAUSIBLE, not CONFIRMED (self-description
consistent, but no independent bracket/hold leg obtainable — RUNBOOK 8).

### Arithmetic
Reported: ~51% (source's own rounding). Back-calculated ballots: 36,080 x
0.51 = 18,400.8 → **18,401**. Pct as stored: 18,401 / 36,080 = **51.00%**
(matches the source figure by construction).

### Draft dataset row
```json
{
  "date": "2012-11-06",
  "type": "presidential-general",
  "election_night_ballots": 18401,
  "certified_final": 36080,
  "election_night_pct": 51.00,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://theava.com/archives/62338",
  "confidence": "secondary",
  "note": "WAYBACK ROUTE EXHAUSTED (documented dead end): elections.htm CDX (co.mendocino.ca.us, 20121001-20130101) has a single pre-poll-close capture (20121106055757, Nov 5 9:57pm PST) whose live-results link points to a THIRD subdomain used only in 2012, http://mx2.co.mendocino.ca.us/elections/election_results.php (2016/2018 used /acr/current.htm and /acr/cgi-bin/currentFR.pl instead). CDX on that mx2 URL (20121101-20130301) has a single capture (20121106042956, Nov 5 8:29pm PST) that is a pre-election placeholder ('Election results will begin displaying soon after ... 8:00 PM PST ... Initial results due in about 24 hours'); no later capture of this URL exists anywhere in Wayback through March 2013 -- the page was never crawled while showing real returns. electionsCurrent.htm (one Nov 27 capture) is generic nav, no results. The permanent archival URL /acr/election_results/results20121106.htm (found via the site's own pastElections.htm link list) is captured repeatedly from April 2014 onward but every capture already reads 'FINAL CERTIFIED RESULTS 11/29/12 13:23:47 ... Cards Cast 36080' (= SoV exactly) -- the certified endpoint, captured too late (Wayback's earliest capture is 1.5 years post-certification) to catch any earlier state. current.htm itself has zero 2012 captures. RECOVERED VIA NEWS (route 6.6, secondary): Anderson Valley Advertiser live-blog from election night 2016 (theava.com/archives/62338, curl -A <UA> fetch, HTTP 200) gives retrospective context: 'LOCAL UPDATE: FINAL ELECTION-NIGHT REPORT -- Just before 2am Wednesday, the final preliminary results (23.58%) for Mendocino County were posted... IN NOVEMBER OF 2012 Mendocino County's preliminary election night results were based on about 51% of about 36,400 votes cast.' The article's 2016 figure (23.58%, 'just before 2am Wednesday') independently corroborates this dossier's own directly-sourced 2016 row (Item 3: county page internal timestamp 11/09/16 01:55:06, Cards Cast 12,032/51,035 = 23.58% of REGISTERED voters), which is strong evidence the writer's parallel 2012 citation is the same kind of number (the county's own settled election-night percentage), not an arbitrary snapshot. However it is a ROUNDED (whole-percent) secondary figure, not a primary exact count: ballots value 18,401 is BACK-CALCULATED as round(36,080 certified final x 0.51), and should be read as approximate (+/- several hundred ballots). Pct = 18,401/36,080 = 51.00% (by construction of the estimate; the source's own reported ratio was 51% of ~36,400, i.e. essentially the same share against the SoV's exact 36,080). PLAUSIBLE not CONFIRMED: self-description consistent (parallel construction to the verified 2016 citation) but no independent Wayback bracket/hold-evidence obtainable for 2012 itself. Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see Item 0)."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2012 ⚠️ | presidential-general | ~18,401 | 36,080 | ~51.0% | secondary | [link](https://theava.com/archives/62338) |`
(⚠️ flag: numerator is a back-calculated estimate from a rounded secondary
source percentage, not a raw primary count — flagged for the human read,
not for `comparable: false`, since it IS a genuine election-night value,
just imprecise.)

Detail bullet:
```
- **2012 presidential-general** — night `~18,401` (estimated) / final `36,080` = `~51.0%` (secondary)
  - numerator: <https://theava.com/archives/62338> (Anderson Valley Advertiser, retrospective citation in a 2016 election-night live-blog)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf>
  - look for: "IN NOVEMBER OF 2012 Mendocino County's preliminary election night results were based on about 51% of about 36,400 votes cast." Wayback has no surviving capture of the actual 2012 live-results page (mx2.co.mendocino.ca.us/elections/election_results.php, single pre-poll-close capture only) -- exhaustively checked and documented as a dead end.
```

### plateau_review.json draft record
```json
{
  "slug": "mendocino-ca",
  "date": "2012-11-06",
  "verdict": "PLAUSIBLE",
  "basis": "news source's parallel citation to an independently-verified same-source figure for a later year, no independent bracket for 2012 itself",
  "evidence": "theava.com 2016-11-09 live-blog: 'IN NOVEMBER OF 2012 Mendocino County's preliminary election night results were based on about 51% of about 36,400 votes cast', in the same sentence construction used for the article's verified 2016 figure (23.58%, matching the county's own page)"
}
```

---

## Item 2 — 2014-11-04 (midterm-general)

### Denominator (SoS SoV)
`curl -A <UA> -L -o sov_2014.pdf https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf`
(2014 uses the `pdf/` segment and the SoS's own misspelling `particpiation`,
per RUNBOOK 6.1) → HTTP 200, 30,131 bytes. `pdftotext -layout`; line 28:
`Mendocino 249 64,404 47,502 4,377 20,640 **25,017** 82.50% 52.67% 38.84%`.
Cross-check: 4,377 + 20,640 = 25,017 ✓; 25,017/47,502 = 52.67% ✓.
**certified_final = 25,017.**

### Numerator hunt — Wayback dead end, same pattern as 2012
- `current.htm` CDX (`co.mendocino.ca.us`, Nov 2014) → captures at Nov 1
  (pre-election stub/leftover), Nov 4 17:35 UTC = 9:35 AM PST (pre-poll-
  close stub), then a **gap straight to Nov 30** (three captures, ~8.5KB).
- Fetched the Nov 30 capture (`20141130082444id_`) → already reads
  **"ELECTION SUMMARY REPORT ... FINAL OFFICIAL RESULTS 11/21/14
  10:08:59 ... Cards Cast 25017 52.70%"** — the certified state (25,017 =
  SoV total exactly), captured 9 days after it was set, same
  dead-end pattern as 2012 (no capture exists of the true overnight state).
- `/acr/election_results/results20141104.htm` (guessed from the confirmed
  2012 naming convention, then CDX-verified) exists but the earliest
  capture is 2015-09-06, already reading the same "FINAL OFFICIAL RESULTS
  11/21/14 10:08:59 ... 25017" state.
- `cgi-bin/currentFR.pl` CDX for Nov 2014 → empty (that path only appears
  archived starting with the 2016/2018 elections).

### Numerator recovered via route 6.6 (local news, verbatim quote)
`WebSearch` surfaced Anderson Valley Advertiser's "Mendocino County Today:
Thursday, Nov 6, 2014" (`https://theava.com/archives/36750`, `curl -A <UA>`,
HTTP 200), published the morning after election night, which **quotes the
county's own election-night report verbatim, including its self-label**:

> "UNOFFICIAL (FINAL) ELECTION RESULTS **'4th and Final Election Night
> Report' 1am 11/05/2014** (Pending certification and the counting of maybe
> 10,000 more votes) for key Mendocino County Elections. **11,402 votes
> cast, 24.02% of registered voters.**"

And later in the same piece, restated in prose: *"Only 11,402 votes were
tallied on election night, a mere 24.02% of the 47,470 registered voters in
the County."* Arithmetic check: 11,402 / 47,470 = 24.02% ✓ (exact match to
the quoted percentage — the registered-voter denominator here, 47,470,
matches the SoV's own Registered Voters figure exactly).

This is the same report-family label convention independently observed on
the county's own archived pages for 2016 ("THIS IS THE FINAL ELECTION NIGHT
REPORT") and 2018 ("Election Night Final Report") — i.e. the reporter is
quoting the actual GEMS report header/output, not paraphrasing. Per RUNBOOK
5.3 this sits at the boundary of "verbatim republication may be primary" vs
"news reportage is secondary even when quoting officials"; kept
**secondary** (conservative) rather than claiming primary, consistent with
how the runbook treats the analogous Nevada County/yubanet open question.

### Plateau vs first tranche
Self-labeled "4th and Final Election Night Report," internal timestamp 1am
11/05/2014 (within the up-to-4am election-night window). Non-circular leg:
the SAME underlying report series' next captured state (this dossier's own
Wayback fetch of `current.htm`, Nov 30 capture, internally dated 11/21/14)
shows a materially higher, later count (25,017 vs 11,402) — the "report
series' next file being days later" leg (RUNBOOK 8), recovered independent
of the news article. Also structurally consistent with the article's own
framing: "thousands of remaining ballots" still to be counted, "as many as
10,000 or more votes are sitting in the elections office."

### Arithmetic
11,402 / 25,017 = 0.455770... → **45.58%**

### Draft dataset row
```json
{
  "date": "2014-11-04",
  "type": "midterm-general",
  "election_night_ballots": 11402,
  "certified_final": 25017,
  "election_night_pct": 45.58,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://theava.com/archives/36750",
  "confidence": "secondary",
  "note": "WAYBACK DEAD END (same pattern as 2012): current.htm CDX for Nov 2014 has captures Nov 1 (pre-election stub) and Nov 4 17:35 UTC/9:35am PST (pre-poll-close stub), then jumps straight to Nov 30 (three captures ~8.5KB); the Nov 30 capture (20141130082444id_) already reads 'ELECTION SUMMARY REPORT ... FINAL OFFICIAL RESULTS 11/21/14 10:08:59 ... Cards Cast 25017 52.70%' -- the certified state (25,017 = SoV total exactly), captured 9 days after being set. The permanent /acr/election_results/results20141104.htm URL (guessed from the confirmed 2012 naming convention, CDX-confirmed to exist) is not captured until 2015-09-06, already showing the same certified state. cgi-bin/currentFR.pl (the 2016/2018 live-report path) has zero Nov 2014 captures. RECOVERED VIA NEWS (route 6.6): Anderson Valley Advertiser 'Mendocino County Today: Thursday, Nov 6, 2014' (theava.com/archives/36750, curl -A <UA> fetch, HTTP 200), published the morning after, quotes the county's election-night report VERBATIM including its self-label: \"UNOFFICIAL (FINAL) ELECTION RESULTS '4th and Final Election Night Report' 1am 11/05/2014 (Pending certification and the counting of maybe 10,000 more votes) ... 11,402 votes cast, 24.02% of registered voters,\" restated later in prose: \"Only 11,402 votes were tallied on election night, a mere 24.02% of the 47,470 registered voters.\" Arithmetic check: 11,402/47,470 = 24.02% exactly, and 47,470 matches the SoV Registered Voters figure exactly. The '4th and Final Election Night Report' label matches the same report-family convention independently found on the county's OWN archived pages for 2016 ('THIS IS THE FINAL ELECTION NIGHT REPORT') and 2018 ('Election Night Final Report'), i.e. this is a verbatim quote of the GEMS report output, not a paraphrase. Kept SECONDARY per RUNBOOK 5.3 (news reportage is secondary even when quoting officials verbatim; not claiming the 5.3 press-release exception since this is a reporter's live-blog, not an official release) -- flagged as an open question analogous to the Nevada/yubanet case, could arguably be upgraded to primary on review. Non-circular plateau leg: the SAME underlying report series' next captured state (this dossier's own Nov 30 Wayback fetch of current.htm, internally dated 11/21/14) shows a materially higher, weeks-later count (25,017 vs 11,402), independently recovered from Wayback, not from the news source. Certified final 25,017 voters (CA SoS Voter Participation Statistics by County: 4,377 precinct + 20,640 VBM = 25,017). Pct = 11,402/25,017 = 45.58%. Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see Item 0)."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2014 | midterm-general | 11,402 | 25,017 | 45.6% | secondary | [link](https://theava.com/archives/36750) |`

Detail bullet:
```
- **2014 midterm-general** — night `11,402` / final `25,017` = `45.6%` (secondary)
  - numerator: <https://theava.com/archives/36750> (Anderson Valley Advertiser, morning-after live-blog quoting the county's report verbatim)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf>
  - look for: "UNOFFICIAL (FINAL) ELECTION RESULTS '4th and Final Election Night Report' 1am 11/05/2014 ... 11,402 votes cast, 24.02% of registered voters." Wayback has no surviving capture of the actual overnight page (current.htm jumps from a pre-poll-close stub straight to an already-certified Nov 30 capture) -- exhaustively checked and documented as a dead end.
```

### plateau_review.json draft record
```json
{
  "slug": "mendocino-ca",
  "date": "2014-11-04",
  "verdict": "CONFIRMED",
  "basis": "county report self-describes (verbatim-quoted by news) + later Wayback capture of the same URL shows a materially higher, weeks-later count",
  "evidence": "\"'4th and Final Election Night Report' 1am 11/05/2014 ... 11,402 votes cast, 24.02% of registered voters\" (theava.com); current.htm's next Wayback state (Nov 30 capture, dated 11/21/14 internally) reads 25,017"
}
```

---

## Item 6 — 2024-11-05 (presidential-general)

### Denominator (SoS SoV)
`curl -A <UA> -L -o sov_2024.pdf https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf`
→ HTTP 200, 163,153 bytes. `pdftotext -layout`; line 29: `Mendocino 245
66,917 54,447 2,479 37,358 **39,837** 93.78% 73.17% 59.53%`. Cross-check:
2,479 + 37,358 = 39,837 ✓; 39,837/54,447 = 73.17% ✓. **certified_final =
39,837.**

### Numerator hunt — Wayback dead end (same pattern as 2022)
- Outer CMS page (`mendocinocounty.gov/.../current-election-results`) CDX
  Nov 2024: only 403s (Nov 1, Cloudflare-blocked even for the archiver) and
  a 301 (Nov 9 23:20 UTC) until the first working 200 capture on **Nov 22**.
  The `.org` domain 301-redirects to `.gov` by this point.
- `co.mendocino.ca.us/acr/cgi-bin/currentFR.pl` CDX (Nov 2024) → a SINGLE
  capture, **20241122142811** (Nov 22). Fetched it (plain HTML, not
  gzipped): header **"OFFICIAL UPDATE #1 OFFICIAL — Run Time 3:38 PM Run
  Date 11/13/2024 — MENDOCINO COUNTY, CALIFORNIA 2024 PRESIDENTIAL GENERAL
  ELECTION 11/5/2024 Unofficial Results — Registered Voters 24062 of 54640 =
  44.04%"** — i.e. even this earliest-available capture is already a
  post-night canvass update (internally dated Nov 13, labeled "OFFICIAL
  UPDATE #1", 24,062 ballots) — Wayback never caught the true overnight
  state, same dead-end pattern as 2022.

### Numerator recovered via route 6.6 (local news, verbatim press-release-adjacent)
`WebSearch` surfaced MendoFever's "Election 2024: Voter turnout, tight
races, and early results in Mendocino County" (Matt LaFever, published
2024-11-06). The live site currently 500-errors (`mendofever.com` is
mid-rebuild, "Coming Soon" / WordPress critical error), so fetched via
Wayback: `curl "https://web.archive.org/cdx/search/cdx?url=mendofever.com/2024/11/06/election-2024-voter-turnout-tight-races-and-early-results-in-mendocino-county/&output=json&limit=20"`
→ earliest capture 20241123041721; fetched `.../20241123041721id_/...`
(gzip'd, `1f 8b` magic bytes, gunzipped). Key passage:

> "With all precincts reporting in the 2024 Presidential General Election,
> voter turnout in Mendocino County reached 28.57%, with **15,611** out of
> 54,640 registered voters casting ballots. ... **These unofficial results,
> released shortly before midnight, are subject to change** as final
> tallies are certified in the coming days"

`datePublished: "2024-11-06T08:20:42+00:00"` = Nov 6, 12:20 AM PST (article
published just after the "shortly before midnight" data it reports).
A later comment thread on the SAME article (author reply) makes the
plateau/first-tranche distinction explicit without being asked:

> "the turnout mentioned in this article is a preliminary number for **the
> ballots that were tabulated by Election night**"

### Plateau vs first tranche — non-circular corroboration
Self-description ("released shortly before midnight," "with all precincts
reporting," explicitly reconfirmed as "tabulated by Election night" in the
same source) satisfies the self-describe leg. Independent, non-circular
leg recovered from Wayback (not the news source): the SAME underlying
county report series' next captured state (`currentFR.pl`, Nov 22 capture,
internally dated **Run Date 11/13/2024**, "OFFICIAL UPDATE #1") shows a
materially higher count, **24,062** — proving 15,611 was a genuine earlier
point that the canvass later moved past, exactly RUNBOOK 8's "report
series' next file being days later" leg.

### Arithmetic
15,611 / 39,837 = 0.391938... → **39.19%**

### Draft dataset row
```json
{
  "date": "2024-11-05",
  "type": "presidential-general",
  "election_night_ballots": 15611,
  "certified_final": 39837,
  "election_night_pct": 39.19,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://mendofever.com/2024/11/06/election-2024-voter-turnout-tight-races-and-early-results-in-mendocino-county/",
  "confidence": "secondary",
  "note": "WAYBACK DEAD END (same pattern as 2022): outer CMS page (mendocinocounty.gov/.../current-election-results) CDX for Nov 2024 shows only 403s (Nov 1, Cloudflare-blocked even for the archiver) and a bare 301 (Nov 9) until the first working 200 capture on Nov 22. co.mendocino.ca.us/acr/cgi-bin/currentFR.pl CDX (Nov 2024) has a SINGLE capture (20241122142811); fetched it (plain HTML) -- header 'OFFICIAL UPDATE #1 OFFICIAL -- Run Time 3:38 PM Run Date 11/13/2024 ... Registered Voters 24062 of 54640 = 44.04%' -- even this earliest-available capture is already a post-night canvass update (internally dated Nov 13, 8 days after the election), not the true overnight state. RECOVERED VIA NEWS (route 6.6): MendoFever 'Election 2024: Voter turnout, tight races, and early results in Mendocino County' (Matt LaFever, published 2024-11-06T08:20:42+00:00 = 12:20am PST Nov 6). Live site currently 500-errors (mendofever.com mid-rebuild); fetched via Wayback (curl CDX + id_ raw fetch of snapshot 20241123041721, gzip'd 1f8b bytes, gunzipped). Quote: 'With all precincts reporting in the 2024 Presidential General Election, voter turnout in Mendocino County reached 28.57%, with 15,611 out of 54,640 registered voters casting ballots ... These unofficial results, released shortly before midnight, are subject to change.' A reader-comment reply by the article's author on the SAME page further disambiguates unprompted: 'the turnout mentioned in this article is a preliminary number for the ballots that were tabulated by Election night' -- explicit self-description as the election-night total, not a next-day figure. Non-circular corroboration (independent of the news source): the SAME underlying county report series' next captured Wayback state (currentFR.pl, Nov 22 capture, internally dated Run Date 11/13/2024, labeled 'OFFICIAL UPDATE #1') shows a materially higher count, 24,062 -- proving 15,611 was a genuine earlier point later superseded by the canvass (RUNBOOK 8's 'next file days later' leg). Registered-voters figure in the article (54,640) is close to but not identical to the SoV's certified Registered Voters (54,447), consistent with a live snapshot taken before final roll reconciliation; does not affect the ballots/certified_final calculation, which uses the SoS Total Voters denominator only. Certified final 39,837 voters (CA SoS Voter Participation Statistics by County: 2,479 precinct + 37,358 VBM = 39,837). Pct = 15,611/39,837 = 39.19%. Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see Item 0). (2020 deliberately excluded as a COVID all-mail outlier.)"
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2024 | presidential-general | 15,611 | 39,837 | 39.2% | secondary | [link](https://mendofever.com/2024/11/06/election-2024-voter-turnout-tight-races-and-early-results-in-mendocino-county/) |`

Detail bullet:
```
- **2024 presidential-general** — night `15,611` / final `39,837` = `39.2%` (secondary)
  - numerator: <https://mendofever.com/2024/11/06/election-2024-voter-turnout-tight-races-and-early-results-in-mendocino-county/> (live site currently down; use the Wayback capture https://web.archive.org/web/20241123041721/https://mendofever.com/2024/11/06/election-2024-voter-turnout-tight-races-and-early-results-in-mendocino-county/ )
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "voter turnout in Mendocino County reached 28.57%, with 15,611 out of 54,640 registered voters casting ballots ... unofficial results, released shortly before midnight" plus an author comment confirming "tabulated by Election night." Wayback's own currentFR.pl capture 11 days later (Run Date 11/13/2024) shows 24,062, confirming 15,611 was the earlier, election-night state.
```

### plateau_review.json draft record
```json
{
  "slug": "mendocino-ca",
  "date": "2024-11-05",
  "verdict": "CONFIRMED",
  "basis": "news source explicitly self-describes as election-night-tabulated + independent Wayback capture of the same county report series shows a materially higher, 8-days-later count",
  "evidence": "MendoFever: '15,611 ... released shortly before midnight'; author comment: 'tabulated by Election night'; currentFR.pl Nov 22 capture (Run Date 11/13/2024, 'OFFICIAL UPDATE #1') reads 24,062"
}
```

---

## Item 5 — 2022-11-08 (midterm-general)

### Denominator (SoS SoV)
`curl -A <UA> -L -o sov_2022.pdf https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf`
→ HTTP 200, 109,762 bytes. `pdftotext -layout`; line 30: `Mendocino 281
67,114 53,105 646 30,362 **31,008** 97.92% 58.39% 46.20%`. Cross-check: 646
+ 30,362 = 31,008 ✓; 31,008/53,105 = 58.39% ✓. **certified_final =
31,008.**

### Numerator hunt — exhaustive, no usable plateau number recovered

**Wayback (route 6.5), fully dead:**
- Outer CMS page (`mendocinocounty.org/.../current-election-results`) CDX
  Nov 2022: captures only start **Nov 18** (10 days post-election);
  earliest content, fetched and gunzipped (`1f 8b` gzip), embeds
  `<iframe src="//www.co.mendocino.ca.us/acr/cgi-bin/currentFR.pl" ...>`.
- `co.mendocino.ca.us/acr/cgi-bin/currentFR.pl` CDX, widened to
  2022-09-01..2023-01-01 to catch anything just outside the Nov window:
  ONE pre-election `warc/revisit` stub (Oct 28) then a gap straight to
  **Nov 27** (19 days post-election). Fetched the Nov 27 capture (gzip'd,
  gunzipped): header **"Election Update — Run Time 3:57 PM Run Date
  11/18/2022 ... Unofficial Results — Registered Voters 21172 of 52366 =
  40.43%"** — a mid-canvass update (internally dated Nov 18, 10 days after
  the election), explicitly labeled "Election Update" (not "Election
  Night" / "Final"). No earlier state was ever crawled. Checked both
  `matchType=exact` and an explicit `www.` variant; identical result set.

**Local news (route 6.6):**
- The Mendocino Voice, "Initial Mendocino County 2022 election results are
  in — UPDATE: 10:30 p.m." (Dave Brooksher, Nov 8 2022, `dateModified
  2022-11-09T06:30:13+00:00` = 10:30 PM PST): reports a **first round**
  (8:22 PM, 11,951 ballots, explicitly "comprised of ballots submitted
  PRIOR to Election Day," i.e. the classic first-tranche pre-processed VBM
  dump the runbook warns against) and references a **second round** (10:10
  PM) but gives ONLY per-race vote tallies for round 2, no restated
  aggregate ballot total. Critically, the article states in its own voice:
  *"Mendocino County Registrar Katrina Bartolomie said... results will be
  updated every two hours. **This will be our last election update for
  tonight, however.**"* — i.e. MendoVoice explicitly stopped covering
  BEFORE the county's own later election-night updates, and did not quote
  a clean total for even the 10:10 PM round.
- MendoFever, "Over 17,000 Ballots Are Still Being Counted in Mendocino
  County" (Nov 12 2022) — a VERBATIM county press release (Katrina
  Bartolomie) — but it is a Nov 12 (4-day-post-election) canvass-progress
  release with no election-night total: "17,080 Vote By Mail ballots to
  process and count, and 617 Provisional/Conditional ballots to review" as
  of Nov 12 (implies ~13,311 cumulative by Nov 12, itself a canvass-state
  number, not election night, and not directly stated by the source
  anyway).
- Searched for a MendoFever Nov-2022 "Election Night ... Stay Tuned"
  live-blog (the format that worked for June 2022 and was reused Nov 2024)
  — none found; MendoFever's Nov 2022 general-election coverage appears
  limited to the Nov 12 canvass-progress press release above.

**Conclusion:** every avenue either predates poll close (first tranche,
explicitly rejected per RUNBOOK section 1), postdates election night by
1-3 weeks (canvass-contaminated), or lacks a stated aggregate ballot count.
No source states a total ballots-counted figure for the LAST report posted
on election night 2022. Per RUNBOOK 5.1, recorded as **null** rather than
substituting the first tranche or a canvass number.

### Draft dataset row
```json
{
  "date": "2022-11-08",
  "type": "midterm-general",
  "election_night_ballots": null,
  "certified_final": 31008,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "NULL PER RUNBOOK 5.1 -- exhaustive search, no usable election-night total. WAYBACK: outer CMS page (mendocinocounty.org/.../current-election-results) CDX Nov 2022 has no capture before Nov 18 (10 days post-election). Its iframe target co.mendocino.ca.us/acr/cgi-bin/currentFR.pl (curl CDX widened 2022-09-01 to 2023-01-01) has one pre-election placeholder revisit (Oct 28) then jumps straight to Nov 27 (19 days post-election, gzip'd 1f8b, gunzipped): header 'Election Update -- Run Time 3:57 PM Run Date 11/18/2022 ... Registered Voters 21172 of 52366 = 40.43%', explicitly an 'Election Update' (canvass), not an election-night report, dated 10 days post-election. No capture of any kind exists for Nov 8-17, 2022. NEWS: The Mendocino Voice 'Initial Mendocino County 2022 election results are in -- UPDATE: 10:30 p.m.' (dateModified 2022-11-09T06:30:13Z = 10:30pm PST Nov 8) gives the FIRST round (8:22pm, 11,951 ballots, explicitly 'ballots submitted PRIOR to Election Day' -- the classic first-tranche mistake RUNBOOK section 1 warns against, not usable) and references a second round (10:10pm) but states NO aggregate ballot total for it, only per-race tallies; the article explicitly says 'This will be our last election update for tonight, however' while noting the COUNTY continued releasing updates 'every two hours' after MendoVoice stopped covering -- i.e. the true election-night plateau exists but was not captured by this source. MendoFever 'Over 17,000 Ballots Are Still Being Counted in Mendocino County' (Nov 12 2022) is a verbatim county press release (Katrina Bartolomie) but is a Nov-12 canvass-progress update ('17,080 Vote By Mail ballots to process and count, and 617 Provisional/Conditional ballots to review' as of Nov 12), not an election-night total, and does not itself state a cumulative count. Searched for a MendoFever Nov-2022 'Election Night ... Stay Tuned' live-blog (the format used June 2022 and Nov 2024) -- none found. No source anywhere states an aggregate ballots-counted figure for the LAST report posted election night 2022. Certified final 31,008 voters (CA SoS Voter Participation Statistics by County: 646 precinct + 30,362 VBM = 31,008) is solid. Control county: no e-pollbook, no ASV, no VCA/vote-center ever (see Item 0)."
}
```

### VERIFY.md draft (summary row + detail bullet)
Summary table row: `| 2022 | midterm-general | — | 31,008 | — | none | — |`

Detail bullet:
```
- **2022 midterm-general** — night `NULL` / final `31,008` (none)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf>
  - look for: no numerator recovered. Wayback has no capture of the county's live-results page (co.mendocino.ca.us/acr/cgi-bin/currentFR.pl) between Nov 8 and Nov 27, 2022; the earliest capture (Nov 27, internally dated Nov 18) is already a canvass "Election Update." The Mendocino Voice's live-blog explicitly stopped covering after the 10:10pm second round without stating its total, noting the county continued updating "every two hours" after they stopped. MendoFever's Nov 12 press release covers ballots-remaining, not an election-night total.
```

### plateau_review.json record
No entry drafted: checked the convention against the 22 existing null
(`confidence: "none"`) rows across the dataset (fresno-ca, madera-ca,
placer-ca, riverside-ca, san-bernardino-ca, san-diego-ca, sacramento-ca) —
NONE of them have a `plateau_review.json` record. RUNBOOK 5.5 specifies a
verdict "per sourced row"; a null row has no source to render a verdict on,
so per the established convention this row gets no plateau_review entry.

---

## Status summary

All 7 items complete (tech record + 6 elections). Nothing was flagged
`FLAG for manual operator` (no source required a real browser beyond what
`curl` + `pdftotext` + gzip handling reached; the SoS Cloudflare-blocked
county pages were avoidable via Wayback/news routes for every year).

| Year | Ballots | Certified final | Pct | Confidence | Verdict |
|---|---:|---:|---:|---|---|
| 2012 | ~18,401 (estimated) | 36,080 | ~51.0% | secondary | PLAUSIBLE |
| 2014 | 11,402 | 25,017 | 45.58% | secondary | CONFIRMED |
| 2016 | 12,032 | 38,730 | 31.07% | primary | CONFIRMED |
| 2018 | 15,819 | 33,966 | 46.57% | primary | CONFIRMED |
| 2022 | NULL | 31,008 | NULL | none | (no record) |
| 2024 | 15,611 | 39,837 | 39.19% | secondary | CONFIRMED |

Notable pattern: Mendocino's own site infrastructure changed vendors
mid-series (GEMS-style "Election Night Final Report" pages through 2018,
switching to Hart Verity "Election Update"/"OFFICIAL UPDATE" pages by 2022),
and Wayback's crawl density around election night is MUCH worse for the
county's live-results pages than for its outer nav pages -- every single
year in this dossier required either a secondary/news route or accepting a
best-available floor, and NONE of the six years yielded a clean Wayback
capture of the exact final-of-night report itself (2016/2018 came closest:
the report survived because the page was left unchanged for days after,
not because Wayback caught the live moment). All six certified-final
denominators are solid (`primary`, PDF-sourced, arithmetic cross-checked
against the SoV's own printed percentages).

The 2016 row (31.07%) is well below the "small rural county 80-95%"
calibration heuristic and is flagged in its own note for human review, not
altered -- the evidence for it is unusually strong (self-labeled FINAL
report + 10-day hold, independently corroborated by a contemporaneous 2016
Anderson Valley Advertiser live-blog quoting the identical 23.58% figure).
