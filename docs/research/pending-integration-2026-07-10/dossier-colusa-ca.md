# Colusa County (colusa-ca) — election-night evidence dossier

Control county for the researching-election-night-share dataset. Probe verdict
(archive-probes-a-m.md): **MARGINAL** — no Clarity (404), no 2016 web trail
under either domain (countyofcolusaca.gov or old countyofcolusa.org), 2018
Wayback coverage is thin (one late-November capture only, nothing
election-night-adjacent). Registrar site is real (200) and a CivicPlus
CivicAlerts module exists but depth/vintage unconfirmed. This dossier extends
that probe into full election-by-election evidence per RUNBOOK.md.

Working notes: appending after each item per process rules (9). Colusa is not
on Clarity (confirmed dead end, skip route 6.4 for all years). Colusa County
Elections Dept has used the same registrar office and (per census note) has
never adopted e-pollbooks or ASV, so vs_epollbook / vs_asv = "n/a" for every
row (control county, no tech transition to bracket).

---
## Item 0 — tech record (data/research/county-tech/colusa-ca.json shape)

Schema reference read: `data/research/county-tech/napa-ca.json` (tech[] entries
of type epollbook/asv/sign-scan-go/vote-center, each with
status/adopted_year/first_election/vendor/evidence_url/confidence/note; plus
a metrics[] array and a top-level notes string). Colusa is a control county
(never adopted any of the four tracked technologies) so metrics[] is thin/null
by definition — there is no "before/after" to measure.

Locating queries run this session (new evidence beyond the census row):
- `curl -s -o colusa_sos_techpdf.pdf "https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf"` then `pdftotext -layout` and `grep -n -i colusa`
- WebSearch: `"Colusa County" elections "electronic poll book" OR "e-pollbook" OR "electronic pollbook"`
- WebSearch: `"Colusa County" elections "signature verification" automated software`

New finding: the CA SoS "Voting Technologies in Use by County" PDF (As of
October 10, 2025), `https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf`,
column header row confirms 8 columns (County, Central Tabulation System, Vote
Center/Polling Place Tabulator, Accessibility Support, Ballot on Demand
Elections Office, Ballot on Demand VoteCenter/Polling Place, Remote
Accessible Vote by Mail System, Electronic Pollbook). Colusa's row:
`Dominion ICC 5.19 | Central Tabulation Only | Dominion ICX 5.19 |
Dominion MBP 5.19 | Do not use | Dominion ImageCast Remote 5.19 | Do not use`
— last column (Electronic Pollbook) = **"Do not use"**. This is a THIRD SoS
snapshot (alongside the census row's May 2022 and Sept 2024 editions) all
agreeing Colusa never adopted e-pollbooks, extending the never-adopter window
through Oct 2025. Also confirms Colusa runs central-tabulation-only (no
polling-place tabulators) with Dominion equipment (ICC/ICX/MBP/ImageCast
Remote), consistent with a small rural county running vote-by-mail-heavy,
staffed elections.

Draft record (`data/research/county-tech/colusa-ca.json`):

```json
{
  "jurisdiction": "Colusa County",
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
      "note": "CA SoS 'Voting Technologies in Use by County' snapshots list Colusa's Electronic Pollbook column as 'Do not use' continuously across at least three editions: May 2022, Sept 2024 (both cited in ca_adoption_census.json), and Oct 10 2025 (this pass, https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf, grep 'Colusa' on pdftotext -layout output: row reads 'Dominion ICC 5.19 | Central Tabulation Only | Dominion ICX 5.19 | Dominion MBP 5.19 | Do not use | Dominion ImageCast Remote 5.19 | Do not use', last column = Electronic Pollbook). Also: EAVS (federal Election Administration and Voting Survey) reports False for Colusa e-pollbook usage in all four editions per census note. Colusa is not a VCA (Voter's Choice Act) county (vca_year null), so it never adopted the vote-center model that typically drives e-pollbook rollout elsewhere (contrast Napa, adopted 2018 alongside VCA). Confidence primary: official SoS technology-in-use filing, repeated across years."
    },
    {
      "type": "asv",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://www.countyofcolusaca.gov/197/Elections",
      "confidence": "medium",
      "note": "Colusa County's official Elections page states: 'Every single ballot undergoes signature verification by one of our elections staff members. If we have any questions or concerns about your signature, we will call you or mail you a notice to verify.' No automated signature-matching software or vendor is named; described process is staff-only comparison against the voter registration card (carried over verbatim from ca_adoption_census.json's ASV research). This pass (2026-07-09/10) re-searched via WebSearch for \"Colusa County\" elections \"signature verification\" automated software and \"Colusa County\" elections \"electronic poll book\" OR \"e-pollbook\" and found no additional evidence of ASV or e-pollbook adoption anywhere (only the same official page, CivicPlus mirror at ca-colusacounty.civicplus.com/197/Elections, and generic SoS/NCSL background pages). Confidence held at 'medium' per census note (a voter-facing FAQ page, not a technical/procedural filing like an EAP, so cannot fully rule out an unstated machine-assisted first pass) -- schema uses this project's confidence vocabulary (primary/secondary/none); recording as given in the source census row."
    },
    {
      "type": "sign-scan-go",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://www.countyofcolusaca.gov/197/Elections",
      "confidence": "secondary",
      "note": "No AB 626 in-vote-center mail-ballot sign-scan-and-go program found; Colusa is not a Voter's Choice Act county and has no vote centers (per SoS tech PDF: 'Vote Center/Polling Place Tabulator' = Central Tabulation Only, i.e. traditional polling places + central count, not VCA vote centers), so the vote-center-dependent Sign-Scan-and-Go model does not apply. Absence-of-evidence inference, consistent with Napa's pre-VCA baseline pattern."
    },
    {
      "type": "vote-center",
      "status": "not-adopted",
      "adopted_year": null,
      "first_election": "",
      "vendor": "",
      "evidence_url": "https://votingsystems.cdn.sos.ca.gov/oversight/county-vsys/vot-tech-by-counties-2025-1.pdf",
      "confidence": "primary",
      "note": "Colusa is not among CA's Voter's Choice Act counties (census row: vca_year null); Oct 2025 SoS tech PDF lists Colusa's 'Vote Center/Polling Place Tabulator' column as 'Central Tabulation Only' (i.e. traditional precinct polling places, ballots centrally tabulated -- not the VCA vote-center model). This is why Colusa is a clean control: no e-pollbook, no ASV, no vote-center transition across the whole 2012-2024 window, so vs_epollbook / vs_asv can be set 'n/a' for every election row below rather than pre/post."
    }
  ],
  "metrics": [],
  "notes": "CONTROL COUNTY: never adopted e-pollbooks, ASV, sign-scan-go, or the VCA vote-center model through the Oct 2025 SoS snapshot (most recent checked). Confirmed by three independent SoS 'Voting Technologies in Use by County' editions (May 2022, Sept 2024, Oct 2025) all reading 'Do not use' for Electronic Pollbook, plus Colusa's own Elections FAQ page describing staff-only manual signature verification with no automated tooling named. No Clarity usage (results.enr.clarityelections.com/CA/Colusa/ -> 404, confirmed in archive-probes-a-m.md and re-confirmed implicitly by the SoS tech PDF showing Dominion equipment, not a Clarity-affiliated stack). Because there is no adoption event to bracket, every election_night row in the dossier below carries vs_epollbook='n/a', vs_asv='n/a' -- this county's value to the dataset is purely as a no-tech-change baseline against which counties that DID adopt (Napa, Nevada, Fresno, etc.) can be compared."
}
```

---
## Denominators — all six elections (CA SoS Statement of Vote, "Voter Participation Statistics by County")

Fetched and grepped this session; `pdftotext -layout` column headers confirm
"Total Voters" is the 6th data column (Registered Voters / Precinct Voters /
Vote-By-Mail Voters / Total Voters / % VBM / Turnout-Registered / Turnout-Eligible).

| Election | URL | Colusa line (as printed) | Total Voters (certified final) |
|---|---|---|---|
| 2012-11-06 | https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf | `Colusa 18 12,364 7,765 2,692 3,400 6,092 55.81% 78.45% 49.27%` | **6,092** |
| 2014-11-04 | https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf | `Colusa 18 12,296 7,595 1,762 2,660 4,422 60.15% 58.22% 35.96%` | **4,422** |
| 2016-11-08 | https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf | `Colusa 18 12,496 8,638 2,607 4,207 6,814 61.74% 78.88% 54.53%` | **6,814** |
| 2018-11-06 | https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf | `Colusa 18 12,552 8,792 2,580 3,235 5,815 55.63% 66.14% 46.33%` | **5,815** |
| 2022-11-08 | https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf | `Colusa 19 13,214 10,144 1,134 4,483 5,617 79.81% 55.37% 42.51%` | **5,617** |
| 2024-11-05 | https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf | `Colusa 19 13,123 10,626 0** 7,122 7,122 100.00% 67.02% 54.27%` | **7,122** |

Locating commands (repeatable): `curl -s -o sov_<year>.pdf "<url>"; pdftotext -layout sov_<year>.pdf sov_<year>.txt; grep -n -i colusa sov_<year>.txt`

2024 note: Precinct Voters column shows `0**` (double-asterisk footnote, consistent
with the 2024 SoV's noted shift to all-mail/vote-center reporting quirks
elsewhere in the document) — Total Voters 7,122 still reconciles as Precinct(0) + VBM(7,122).

---
## Numerator route summary (applies to all six elections — read this before the per-year items)

Before working year by year, the general shape of Colusa's web footprint became clear
and is recorded once here to avoid repeating it six times:

1. **Clarity (route 6.4): dead end, confirmed.** `results.enr.clarityelections.com/CA/Colusa/`
   -> 404 (probe finding, re-confirmed implicitly: SoS Oct-2025 tech PDF shows Dominion
   equipment, not a Clarity-affiliated ENR stack). Skipped for all years.
2. **Registrar's own results archive (routes 6.2/6.3) exists and is unusually deep** —
   `https://www.countyofcolusaca.gov/679/Past-Election-Results` (formerly
   `www.countyofcolusa.org/index.aspx?NID=679`) lists "By Contest" / "By Precinct" PDF
   result documents back to 1995, including every target year (2012, 2014, 2016, 2018,
   2022, 2024). **But it publishes exactly ONE results document per election, and in
   every case checked its own PDF metadata (CreationDate/ModDate) or embedded report
   date places it 3-4 weeks after election day, at or near the CA 30-day certification
   deadline, not on election night:**
   - 2016 "By Contest" (`/DocumentCenter/View/8620`): PDF CreationDate **Jan 12, 2017**
     (>2 months post-election).
   - 2018 "By Contest" (`/DocumentCenter/View/10616`, and homepage-linked "Official
     Results" `/DocumentCenter/View/10611` which has no independent Wayback capture):
     PDF CreationDate **Nov 28, 2018**, ModDate **Nov 29, 2018** (22-23 days
     post-election; matches the Nov 29, 2018 Wayback capture of the elections
     homepage that links it — the county's crawl-visible page never showed anything
     earlier).
   - 2022 "Summary" (`/DocumentCenter/View/16571`, fetched live from the current site):
     embedded report header timestamp **12/1/2022 4:50:41 PM**, labeled "Official
     Results," and its Voters Cast total (**5,617**) is an EXACT match to the SoS
     certified final (5,617) — i.e. this is the certified canvass, not a night count.
   - 2024 "Election-Night-Results" (`/DocumentCenter/View/18349/Election-Night-Results`,
     fetched live): **THE FILENAME IS A FALSE FRIEND.** The document's own title
     block reads "Colusa County **Final Report**," header timestamp **12/3/2024
     1:03:33 PM** (28 days post-election), and its Voters Cast total (**7,122**) is an
     EXACT match to the SoS certified final (7,122). Colusa's elections-management
     software (Dominion, per the SoS tech PDF) evidently uses a generic filename
     template containing the string "election-night" for its cumulative summary
     report export **regardless of which day of the canvass it represents** — the
     live "Elections" landing page's CURRENT "Official Election Results" link
     (checked 2026-07, most likely the then-upcoming/most-recent election) is
     `/DocumentCenter/View/20340/ElectionSummaryReportRPT-election-night-6226`,
     the same "-election-night-" filename pattern, confirming this is a software
     naming artifact and not a claim about report timing. **This is recorded as a
     gotcha for future researchers** (RUNBOOK.md 7.3/7.5 territory: don't trust a
     results filename's "election night" label without checking the document's own
     internal report date).
   - 2012 "By Contest" (`/DocumentCenter/View/5436`, titled
     "November-6-2012-Official-Results-By-Contest") and 2014 "By Contest"
     (`/DocumentCenter/View/4693`): titles alone ("Official Results") plus their
     position in the same standing single-document-per-election archive pattern
     make them near-certainly the same certified-final pattern; PDF byte-fetch for
     direct metadata confirmation was attempted (see items below) but was
     intermittently blocked by web.archive.org connection failures in this session
     (`curl: (7) Failed to connect to web.archive.org port 443` — recurring,
     unrelated to CDX rate limits, affected only the archive.org host, not the live
     county site) after a partial 1,048,576-byte truncated download on the first
     attempts; not independently re-confirmed by PDF metadata this pass.
3. **No Wayback capture exists during or within days of election night, for any of
   the six years, on either domain** (`countyofcolusa.org`/`www.countyofcolusa.org`,
   `countyofcolusaca.gov`, plus the underlying `ca-colusacounty.civicplus.com`
   CMS host, plus the pre-2012 `co.colusa.ca.us` domain which stops being crawled
   after 2008). Concretely, CDX on `www.countyofcolusa.org/elections` (the one path
   that DOES exist across years) shows a >2-month gap bracketing Nov 8, 2016 (last
   capture before: Oct 20, 2016; first after: Dec 21, 2016) and a >10-month gap
   bracketing Nov 6, 2018 (last before: Jan 31, 2018; first after: Nov 29, 2018,
   i.e. the certified-final capture above). 2012 and 2014 have **zero** captures of
   any elections-labeled path on any domain in Wayback.
4. **Local news (route 6.6):** WebSearch for Colusa Sun-Herald / Appeal-Democrat
   coverage found only a **June 2022 primary** article ("Colusa County releases
   unofficial election results as ballot count continue," appeal-democrat.com,
   published mid-June 2022) — wrong election (primary, not our Nov general target
   years) and its exact ballot figure could not be re-confirmed this pass
   (`WebFetch` returned HTTP 429 on retry). No Sun-Herald/Appeal-Democrat coverage
   surfaced for the actual target Nov-general election nights (2012, 2014, 2016,
   2018, 2022, 2024) despite repeated targeted WebSearch queries per year.

**Conclusion for the whole county:** Colusa never appears to have published a
distinct election-night snapshot anywhere on the open, archived web for any of the
six target elections — only a single, later-uploaded certified-final results
document per election. Per RUNBOOK.md 5.1, every row below is `null` rather than
substituting the certified-final PDF as a fake "night" number (that would just
equal the denominator, which is not permitted and not useful). This makes Colusa a
genuinely well-documented NULL county for the numerator across the whole window,
which is itself a valid, useful control-county deliverable (small non-VCA county,
central-tabulation-only, no distinct night reporting infrastructure at all).

---
## Item 1 — 2012-11-06 (presidential-general)

**Certified final:** 6,092 (CA SoS SoV, `https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf`,
line `Colusa 18 12,364 7,765 2,692 3,400 6,092 55.81% 78.45% 49.27%`).

**Numerator hunt:**
- Route 6.4 (Clarity): skip, confirmed dead (see route summary above).
- Route 6.2/6.3 (registrar release / dated report series): the only surviving
  document is `/DocumentCenter/View/5436`, titled (per its own URL slug recovered
  via CDX) **"November-6-2012-Official-Results-By-Contest"**, and its Wayback
  capture is `https://web.archive.org/web/20220702140759id_/https://www.countyofcolusa.org/DocumentCenter/View/5436/November-6-2012-Official-Results-By-Contest?bidId=`
  (CDX: `curl "https://web.archive.org/cdx/search/cdx?url=countyofcolusa.org/DocumentCenter/View/5436&matchType=prefix&output=json&limit=20"`,
  one row, 2022-07-02, `application/pdf`, 200, length 715116). The "Official
  Results" title (matching the pattern independently confirmed by PDF-internal
  metadata for 2016/2018/2022/2024, all of which turned out to be the certified
  canvass 3-4 weeks post-election, not election night — see route summary) makes
  this near-certainly the certified final too, not a night count. A direct
  byte-fetch to independently confirm the PDF's own CreationDate metadata was
  attempted three times this session (`curl --max-time 45/60`) and failed each
  time with `curl: (7) Failed to connect to web.archive.org port 443` — an
  intermittent connectivity problem specific to web.archive.org in this session
  (the CDX JSON API on the same host succeeded minutes before and after; the live
  `countyofcolusaca.gov` host was unaffected), not a bot-block. This is recorded
  honestly rather than silently dropped; a retry in a future session could recover
  the file and confirm/refute the CreationDate the same way it was confirmed for
  2016/2018/2022/2024.
- Route 6.5 (Wayback of the live results page): **zero captures found for any
  elections-labeled path on any domain in the entire year 2012.** CDX queries run:
  `curl "https://web.archive.org/cdx/search/cdx?url=countyofcolusa.org&matchType=domain&output=json&limit=500&filter=original:.*(?i)(elect|vote|result).*"` (2000-row
  cap hit, earliest elections-labeled hit is 2013-08); `curl "https://web.archive.org/cdx/search/cdx?url=co.colusa.ca.us&matchType=domain&output=json&limit=20"`
  (pre-2012 legacy domain, captures stop 2008, nothing in 2012);
  `curl "https://web.archive.org/cdx/search/cdx?url=ca-colusacounty.civicplus.com&matchType=domain&output=json&limit=200"` (CMS host itself has a 2012-04-15 and
  2013-05-16 homepage capture but no elections subpage). `countyofcolusaca.gov`
  did not exist as a domain in 2012 (post-migration domain).
- Route 6.6 (local news): WebSearch `"Colusa Sun-Herald 2012 election night results
  ballots counted"` returned only the general Colusa Elections page, a 2022
  Colusa Sun-Herald primary-night article (wrong year/election), Ballotpedia's
  measures list, and the modern SoS results portal — nothing dated Nov 2012.

**Result: NULL.** No election-night-specific artifact survives for 2012 by any
route. certified_final is solid (SoV PDF, primary confidence); election-night
value is null per RUNBOOK.md 5.1.

Draft row (`data/research/election-night/colusa-ca.json`):
```json
{
  "date": "2012-11-06",
  "type": "presidential-general",
  "election_night_ballots": null,
  "certified_final": 6092,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "No Clarity (results.enr.clarityelections.com/CA/Colusa/ -> 404). No Wayback capture of any elections-labeled path on countyofcolusa.org, co.colusa.ca.us, or ca-colusacounty.civicplus.com exists anywhere in 2012 (CDX: url=countyofcolusa.org&matchType=domain&filter=original:.*(?i)(elect|vote|result).* limit=2000, earliest hit 2013-08; url=co.colusa.ca.us&matchType=domain, captures stop 2008; url=ca-colusacounty.civicplus.com&matchType=domain, homepage-only captures 2012-04/2013-05, no elections subpage). Colusa's only surviving results artifact for this election is /DocumentCenter/View/5436, titled 'November-6-2012-Official-Results-By-Contest' (Wayback capture 2022-07-02, https://web.archive.org/web/20220702140759id_/https://www.countyofcolusa.org/DocumentCenter/View/5436/November-6-2012-Official-Results-By-Contest?bidId=); its title matches the certified-canvass naming pattern independently confirmed via internal PDF metadata for Colusa's 2016 (CreationDate 2017-01-12), 2018 (CreationDate 2018-11-28), 2022 (report header 2022-12-01, Voters Cast exactly = certified final 5,617), and 2024 (report header 2024-12-03, Voters Cast exactly = certified final 7,122) results documents -- in every year checked, Colusa's registrar publishes exactly ONE results document per election and it is the certified final, 3-4 weeks post-election, never a distinct night snapshot. Byte-level PDF metadata confirmation for the 2012 document specifically was attempted (curl --max-time 45/60 against the web.archive.org id_ replay) but blocked by intermittent web.archive.org connectivity in this research session (curl error 7, connection refused), not a bot-wall; CDX enumeration (which hit the same host) succeeded before and after. No local-news coverage found (WebSearch for Colusa Sun-Herald / Appeal-Democrat 2012 election-night coverage returned nothing dated Nov 2012). Value left null per RUNBOOK.md 5.1 rather than substituting the certified-final PDF as a fake night number."
}
```

**VERIFY.md draft lines:**
Summary table: `| 2012 | presidential-general | — | 6,092 | — | — |`
Detail bullet: `- **2012-11-06** (presidential-general): certified final 6,092 ([SoV PDF](https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf), look for "Colusa" row, Total Voters column). Election-night ballots: **not found** — no Wayback capture of any Colusa elections page exists for 2012 on any domain; the only surviving results document (`/DocumentCenter/View/5436`) is the certified final, by title-pattern and cross-year confirmation, not a night snapshot.`

**Plateau verdict** (`plateau_review.json`): not applicable — no sourced numerator row (null rows do not get a plateau verdict per RUNBOOK.md 5.5, which covers "sourced rows").

---
## Item 2 — 2014-11-04 (midterm-general)

**Certified final:** 4,422 (CA SoS SoV, `https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf`
[note: SoS's own misspelling "particpiation" preserved in the URL], line
`Colusa 18 12,296 7,595 1,762 2,660 4,422 60.15% 58.22% 35.96%`).

**Numerator hunt:**
- Route 6.4 (Clarity): skip, confirmed dead.
- Route 6.2/6.3: only surviving document is `/DocumentCenter/View/4693` ("By
  Contest"), CDX: `curl "https://web.archive.org/cdx/search/cdx?url=countyofcolusa.org/DocumentCenter/View/4693&matchType=prefix&output=json&limit=20"`
  -> one row, 2019-07-20, `application/pdf`, 200, length 647573,
  `https://web.archive.org/web/20190720094634id_/https://www.countyofcolusa.org/DocumentCenter/View/4693`.
  Same reasoning as 2012: this is the standing single-document-per-election
  archive whose every OTHER independently-confirmed year is the certified final
  3-4 weeks out, not a night snapshot; a direct PDF metadata fetch was attempted
  and blocked by the same intermittent web.archive.org connectivity issue this
  session (`curl: (7) Failed to connect`, after one partial download stalled at
  exactly 1,048,576 bytes on an earlier attempt for this same file).
- Route 6.5 (Wayback of the live results page): the elections page
  `www.countyofcolusa.org/elections` has NO capture anywhere near Nov 4, 2014 —
  earliest capture of that path is 2014-08-11 (a 302 redirect, i.e. the page
  didn't even resolve to content yet) and the next is 2016-06-11, an 18-MONTH
  gap spanning the entire 2014 election and canvass. (`curl
  "https://web.archive.org/cdx/search/cdx?url=countyofcolusa.org/elections&matchType=prefix&output=json&limit=200"`.)
  No `countyofcolusaca.gov` (didn't exist yet). `ca-colusacounty.civicplus.com`
  domain-wide CDX shows only CSS/JS asset captures around Nov 2014, no elections
  HTML page.
- Route 6.6 (local news): WebSearch for Colusa Sun-Herald / Appeal-Democrat 2014
  election-night coverage returned nothing dated Nov 2014.

**Result: NULL.**

Draft row:
```json
{
  "date": "2014-11-04",
  "type": "midterm-general",
  "election_night_ballots": null,
  "certified_final": 4422,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "No Clarity. The elections page www.countyofcolusa.org/elections has a >18-month Wayback gap spanning the entire election (last capture before: 2014-08-11 302 redirect / not-yet-live; next: 2016-06-11); CDX: url=countyofcolusa.org/elections&matchType=prefix&limit=200. Only surviving results artifact is /DocumentCenter/View/4693 ('By Contest'), Wayback capture 2019-07-20 (https://web.archive.org/web/20190720094634id_/https://www.countyofcolusa.org/DocumentCenter/View/4693), part of the same standing single-document-per-election results archive whose every independently-confirmed sibling year (2016, 2018, 2022, 2024; see 2012 row note and the route-summary section of the dossier this row was drafted from) turned out via internal PDF metadata to be the certified final 3-4 weeks post-election, not a night snapshot. Direct byte-fetch to confirm 4693's own CreationDate was attempted (curl --max-time 60) and blocked by intermittent web.archive.org connectivity this session (curl error 7; one earlier attempt truncated at exactly 1,048,576 bytes mid-transfer). No local-news coverage found for Nov 2014 election night. Value left null per RUNBOOK.md 5.1."
}
```

**VERIFY.md draft lines:**
Summary table: `| 2014 | midterm-general | — | 4,422 | — | — |`
Detail bullet: `- **2014-11-04** (midterm-general): certified final 4,422 ([SoV PDF](https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf), look for "Colusa" row, Total Voters column). Election-night ballots: **not found** — Wayback has an 18-month gap over the elections page spanning this election; the only surviving results document is the certified final by cross-year pattern.`

**Plateau verdict:** not applicable (null row).

---
## Item 3 — 2016-11-08 (presidential-general)

**Certified final:** 6,814 (CA SoS SoV, `https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf`,
line `Colusa 18 12,496 8,638 2,607 4,207 6,814 61.74% 78.88% 54.53%`).

**Numerator hunt — DEFINITIVELY RESOLVED as the certified canvass, not election night.**
Fetched the only surviving results document, `/DocumentCenter/View/8620`
("November-8-2016-Results-By-Contest"), via its Wayback capture:
`https://web.archive.org/web/20201121161224id_/https://www.countyofcolusa.org/DocumentCenter/View/8620/November-8-2016-Results-By-Contest?bidId=`
(CDX: `curl "https://web.archive.org/cdx/search/cdx?url=countyofcolusa.org/DocumentCenter/View/8620&matchType=prefix&output=json&limit=20"`).
Rendered to PNG with `pdftoppm -png -r 150` (the PDF has no embedded text layer,
`pdffonts` returns zero fonts — image-only report) and read directly:
- **Page 1** is a signed certificate: "**CANVASS AND STATEMENT OF RESULT OF
  ELECTION FOR PRESIDENTIAL GENERAL ELECTION, Tuesday, November 8, 2016**...
  I Rose Gallo-Vasquez hereby certify that pursuant to §15300-15376 of the
  California Elections Code, I canvassed the returns... IN WITNESS WHEREOF, I
  have hereunto set my hand this **30th day of NOVEMBER 2016**." Signed, county
  clerk seal.
- **Page 2**: "SUMMARY REPT-GROUP DETAIL ... OFFICIAL RESULTS - EL45A ...
  **RUN DATE: 11/30/16 04:49 PM** ... BALLOTS CAST - TOTAL: **6,814**" — an
  EXACT match to the SoS certified final.
This is unambiguous: the document is the signed, certified canvass, dated
22 days after election day, not a night snapshot.
- Route 6.5 (Wayback of the live page): confirms the pattern independently —
  `www.countyofcolusa.org/elections` has a 2-month capture gap bracketing
  election night (last before: 2016-10-20; first after: 2016-12-21), so even
  the page that links to results was never crawled during the live count.
- Route 6.6 (local news): WebSearch for Colusa Sun-Herald / Appeal-Democrat
  2016 election-night coverage found nothing dated Nov 2016.

**Result: NULL** (with unusually strong, directly-read evidence for why — this
is a REFUTED-STRENGTH finding, not just an absence).

Draft row:
```json
{
  "date": "2016-11-08",
  "type": "presidential-general",
  "election_night_ballots": null,
  "certified_final": 6814,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "DIRECTLY CONFIRMED not a night number: fetched /DocumentCenter/View/8620 via https://web.archive.org/web/20201121161224id_/https://www.countyofcolusa.org/DocumentCenter/View/8620/November-8-2016-Results-By-Contest?bidId= (image-only PDF, no text layer, rendered with pdftoppm -png -r 150 and read directly). Page 1 is a SIGNED 'CANVASS AND STATEMENT OF RESULT OF ELECTION' certificate dated 'this 30th day of NOVEMBER 2016' by County Clerk/Registrar Rose Gallo-Vasquez. Page 2 header: 'RUN DATE: 11/30/16 04:49 PM ... OFFICIAL RESULTS - EL45A', Ballots Cast - Total: 6,814, exactly equal to the SoS certified final. This is the certified canvass, 22 days post-election, not an election-night report. www.countyofcolusa.org/elections (the page that links to it) has a 2-month Wayback gap bracketing election night (last capture before: 2016-10-20; next: 2016-12-21; CDX: url=countyofcolusa.org/elections&matchType=prefix), consistent with no night-specific page ever being crawled. No Clarity. No local-news coverage of election night found via WebSearch. Value left null per RUNBOOK.md 5.1: the only surviving number is the certified final itself, which cannot stand in as a 'night' figure."
}
```

**VERIFY.md draft lines:**
Summary table: `| 2016 | presidential-general | — | 6,814 | — | — |`
Detail bullet: `- **2016-11-08** (presidential-general): certified final 6,814 ([SoV PDF](https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf)). Election-night ballots: **not found** — the only surviving results document ([Wayback capture of DocumentCenter/View/8620](https://web.archive.org/web/20201121161224id_/https://www.countyofcolusa.org/DocumentCenter/View/8620/November-8-2016-Results-By-Contest?bidId=)) is a SIGNED canvass certificate dated Nov 30, 2016 (22 days post-election), Ballots Cast 6,814 = certified final exactly. Confirmed by direct page image read, not just title-pattern inference.`

**Plateau verdict:** not applicable (null row; the strong negative finding above
would be recorded as informational context if a plateau_review entry format for
"confirmed-null" existed, but per RUNBOOK.md 5.5 plateau verdicts cover sourced
rows only).

---
## Item 4 — 2018-11-06 (midterm-general)

**Certified final:** 5,815 (CA SoS SoV, `https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf`,
line `Colusa 18 12,552 8,792 2,580 3,235 5,815 55.63% 66.14% 46.33%`).

**Numerator hunt — same definitive resolution as 2016.**
Fetched `/DocumentCenter/View/10616` via
`https://web.archive.org/web/20190723050900id_/https://www.countyofcolusa.org/DocumentCenter/View/10616`
(CDX: `curl "https://web.archive.org/cdx/search/cdx?url=countyofcolusa.org/DocumentCenter/View/10616&output=json&limit=50"`).
`pdfinfo` shows CreationDate Nov 28 2018, ModDate Nov 29 2018 (this matches the
Wayback capture of the elections homepage on 2018-11-29 that links to it as
"Official Results"). Rendered pages 1-2 to PNG and read directly:
- Page header: "SUMMARY REPT-GROUP DETAIL ... COLUSA COUNTY, CALIFORNIA ...
  GENERAL ELECTION ... NOVEMBER 6, 2018 ... **OFFICIAL RESULTS** ...
  **RUN DATE: 11/26/18 02:24 PM** ... REPORT-EL45A PAGE 001".
- Page 1 summary block: "BALLOTS CAST - TOTAL: **5,815**" — exact match to the
  SoS certified final.
This is the certified canvass, dated 20 days after election day.
- Route 6.5: `www.countyofcolusa.org/elections` has a >10-month capture gap
  bracketing this election (last before: 2018-01-31; next: 2018-11-29, which
  IS this same certified-final capture, i.e. the FIRST time Wayback saw the
  elections page again after the election was already 3 weeks post-canvass).
- Route 6.6: WebSearch for Colusa Sun-Herald / Appeal-Democrat Nov 2018
  election-night coverage found nothing dated Nov 2018.

**Result: NULL** (directly confirmed, same strength as 2016).

Draft row:
```json
{
  "date": "2018-11-06",
  "type": "midterm-general",
  "election_night_ballots": null,
  "certified_final": 5815,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "DIRECTLY CONFIRMED not a night number: fetched /DocumentCenter/View/10616 via https://web.archive.org/web/20190723050900id_/https://www.countyofcolusa.org/DocumentCenter/View/10616 (image-only PDF, rendered with pdftoppm -png -r 150 and read directly). Header: 'OFFICIAL RESULTS ... RUN DATE: 11/26/18 02:24 PM ... REPORT-EL45A PAGE 001'; Ballots Cast - Total: 5,815, exactly equal to the SoS certified final. pdfinfo also shows CreationDate 2018-11-28 / ModDate 2018-11-29 -- 22-23 days post-election. This document is also what the elections homepage linked as 'Official Results' (/DocumentCenter/View/10611, no independent Wayback capture) in its 2018-11-29 Wayback snapshot -- the FIRST time the elections page was crawled again after a >10-month gap (last before: 2018-01-31; CDX: url=countyofcolusa.org/elections&matchType=prefix), meaning Wayback never saw the page during the live count at all, only after certification was essentially complete. No Clarity. No local-news coverage of election night found via WebSearch. Value left null per RUNBOOK.md 5.1."
}
```

**VERIFY.md draft lines:**
Summary table: `| 2018 | midterm-general | — | 5,815 | — | — |`
Detail bullet: `- **2018-11-06** (midterm-general): certified final 5,815 ([SoV PDF](https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf)). Election-night ballots: **not found** — the only surviving results document ([Wayback capture of DocumentCenter/View/10616](https://web.archive.org/web/20190723050900id_/https://www.countyofcolusa.org/DocumentCenter/View/10616)) is headered "OFFICIAL RESULTS, RUN DATE: 11/26/18", Ballots Cast 5,815 = certified final exactly; confirmed by direct page image read.`

**Plateau verdict:** not applicable (null row).

---
## Item 5 — 2022-11-08 (midterm-general)

**Certified final:** 5,617 (CA SoS SoV, `https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf`,
line `Colusa 19 13,214 10,144 1,134 4,483 5,617 79.81% 55.37% 42.51%`).
(Note: precinct count rose from 18 to 19 vs. earlier elections.)

**Numerator hunt:**
- Route 6.4 (Clarity): skip, confirmed dead.
- Route 6.2/6.3: the CURRENT live registrar site's "Past Election Results"
  archive (`https://www.countyofcolusaca.gov/679/Past-Election-Results`, fetched
  directly, no Wayback needed) lists Nov 8, 2022 as: "Summary: PDF
  (`/DocumentCenter/View/16571`)" and "Provisional Ballot Status: PDF
  (`/DocumentCenter/View/16569`)" — no separate election-night document exists
  in the listing. Fetched `/DocumentCenter/View/16571` directly
  (`curl -L "https://www.countyofcolusaca.gov/DocumentCenter/View/16571"`, live
  site, 689,931 bytes, text-layer PDF this time). `pdfinfo`: CreationDate
  **Dec 2, 2022 12:45:31 PM**, ModDate May 31, 2023 (later admin re-touch,
  irrelevant to the count). `pdftotext -layout` header: "Election Summary
  Report ... General Election ... Colusa ... November 08, 2022 ... **Official
  Results** ... Page 1 of 14 ... **12/1/2022 4:50:41 PM**". Body: "Elector
  Group Total ... Total **5,617** ... Registered Voters 10,147 ... Turnout
  55.36% ... Precincts Reported: 19 of 19 (100.00%) ... Voters Cast: 5,617 of
  10,147 (55.36%)" — EXACT match to the SoS certified final. This is the
  certified canvass, 23 days post-election (report-internal date 12/1/2022),
  not a night snapshot.
- Route 6.5: no need to chase Wayback further given the direct live-site
  confirmation above; the live archive page itself confirms no distinct
  election-night document was ever posted for this election (only "Summary"
  and "Provisional Ballot Status").
- Route 6.6 (local news): the ONE Colusa Sun-Herald / Appeal-Democrat article
  found this session, "Colusa County releases unofficial election results as
  ballot count continue" (`appeal-democrat.com/colusa_sun_herald/...`), is
  dated **mid-June 2022** and covers the June 2022 STATEWIDE DIRECT PRIMARY,
  not this November general — wrong election, not usable. `WebFetch` of the
  article for a possible general re-check returned HTTP 429 on retry (rate
  limited) and was not re-attempted given the date mismatch made it moot
  regardless. No Sun-Herald/Appeal-Democrat coverage of the Nov 2022
  election-night count was found.

**Result: NULL** (directly confirmed via a live, non-Wayback fetch this time —
no connectivity caveat needed for this row).

Draft row:
```json
{
  "date": "2022-11-08",
  "type": "midterm-general",
  "election_night_ballots": null,
  "certified_final": 5617,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "DIRECTLY CONFIRMED not a night number, fetched live (no Wayback needed): https://www.countyofcolusaca.gov/DocumentCenter/View/16571 (curl -L, 689,931 bytes, text PDF). pdfinfo CreationDate 2022-12-02 12:45:31 PM. pdftotext -layout header: 'Election Summary Report ... November 08, 2022 ... Official Results ... Page 1 of 14 ... 12/1/2022 4:50:41 PM'; body 'Total 5,617 ... Registered Voters 10,147 ... Turnout 55.36% ... Precincts Reported: 19 of 19 (100.00%)' -- exact match to the SoS certified final (5,617). This is the certified canvass, 23 days post-election, not election night. The live 'Past Election Results' archive page (https://www.countyofcolusaca.gov/679/Past-Election-Results) lists only 'Summary' and 'Provisional Ballot Status' documents for this election -- no distinct election-night report was ever published. The one Colusa Sun-Herald article found covering an 'unofficial results, ballot count continues' theme (appeal-democrat.com/colusa_sun_herald/colusa-county-releases-unofficial-election-results-as-ballot-count-continue/) is dated mid-June 2022 and covers the June 2022 primary, not this November general -- wrong election, not usable; a WebFetch re-check hit HTTP 429 and was not pursued further given the date mismatch. No Clarity. Value left null per RUNBOOK.md 5.1."
}
```

**VERIFY.md draft lines:**
Summary table: `| 2022 | midterm-general | — | 5,617 | — | — |`
Detail bullet: `- **2022-11-08** (midterm-general): certified final 5,617 ([SoV PDF](https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf)). Election-night ballots: **not found** — the live registrar archive's only document ([DocumentCenter/View/16571](https://www.countyofcolusaca.gov/DocumentCenter/View/16571)) is headered "Official Results ... 12/1/2022 4:50:41 PM", Total 5,617 = certified final exactly.`

**Plateau verdict:** not applicable (null row).

---

## Item 6 — 2024-11-05 (presidential-general)

**Certified final:** 7,122 (CA SoS SoV, `https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf`,
line `Colusa 19 13,123 10,626 0** 7,122 7,122 100.00% 67.02% 54.27%`).

**Numerator hunt — the "false friend" of this whole dossier.**
The current live registrar site's landing "Elections" page
(`https://www.countyofcolusaca.gov/197/Elections`, fetched directly) links
"Official Election Results" -> `/DocumentCenter/View/18349/Election-Night-Results`
for the 2024 general. The FILENAME says "Election-Night-Results." Fetched it
directly (`curl -L "https://www.countyofcolusaca.gov/DocumentCenter/View/18349/Election-Night-Results"`,
live site, 263,768 bytes, image-only PDF, no text layer per `pdffonts`).
`pdfinfo`: CreationDate **Dec 3, 2024 2:11:02 PM**, ModDate Dec 3, 2024
2:37:15 PM — 28 days post-election. Rendered page 1 to PNG
(`pdftoppm -png -r 150 -f 1 -l 1`) and read directly:
- Header: "Page: 1 of 10 ... **12/3/2024 1:03:33 PM** ... **Election Summary
  Report** ... General Election ... Colusa ... November 05, 2024 ... Summary
  for: All Contests, All Districts, All Tabulators, All Counting Groups ...
  **Colusa County Final Report**."
- Body: "Total ... Vote by Mail 7,122 ... 66.87% ... Total 7,122 ... Registered
  Voters 10,651 ... Turnout 66.87% ... Precincts Reported: 19 of 19 (100.00%)
  ... Voters Cast: 7,122 of 10,651 (66.87%)" — EXACT match to the SoS certified
  final.
**The document's own title block reads "Final Report," not "election night,"
despite the URL/filename.** This is confirmed as a naming-convention artifact:
the CURRENT (as of this research, mid-2026) "Official Election Results" link on
the live Elections page for the county's MOST RECENT election is
`/DocumentCenter/View/20340/ElectionSummaryReportRPT-election-night-6226` — the
same "-election-night-" string appears in the generic export filename for
whatever the latest posted report is, regardless of where in the canvass it
falls. Colusa's elections-management software (Dominion, per the CA SoS Oct
2025 "Voting Technologies in Use by County" PDF) evidently uses a fixed
filename template containing "election-night" for its cumulative
`ElectionSummaryReportRPT` export at every stage of the canvass, not only the
first night. **This is the dossier's single most important gotcha finding**
(RUNBOOK.md 7.3/7.5 territory: a report's filename or generic label is not
evidence of when it was generated; only the document's own internal
run-date/report-date proves that).
- Route 6.6 (local news): WebSearch for Appeal-Democrat / Colusa Sun-Herald
  Nov 2024 election-night coverage found nothing dated Nov 2024.

**Result: NULL.**

Draft row:
```json
{
  "date": "2024-11-05",
  "type": "presidential-general",
  "election_night_ballots": null,
  "certified_final": 7122,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "GOTCHA: the registrar's own document is titled/URL-named 'Election-Night-Results' (https://www.countyofcolusaca.gov/DocumentCenter/View/18349/Election-Night-Results, live-fetched, image-only PDF, pdfinfo CreationDate 2024-12-03 2:11 PM) but its OWN internal title block, read directly off the rendered page-1 image, says 'Election Summary Report ... November 05, 2024 ... Colusa County FINAL REPORT', report timestamp 12/3/2024 1:03:33 PM (28 days post-election), Voters Cast 7,122 of 10,651 (66.87%) -- exactly equal to the SoS certified final (7,122). This is the certified canvass, not election night, despite the filename. Confirmed as a systemic naming artifact: the live Elections page's CURRENT 'Official Election Results' link (for the most recent election as of this 2026 research pass) is /DocumentCenter/View/20340/ElectionSummaryReportRPT-election-night-6226, the same '-election-night-' filename fragment, indicating Colusa's Dominion-based elections-management software (per CA SoS Oct-2025 tech PDF) always exports its cumulative ElectionSummaryReportRPT with 'election-night' baked into the filename template regardless of report date. Future researchers: do NOT trust this filename pattern for Colusa; always read the document's own internal 'RUN DATE' / report-title text. No Clarity. No local-news coverage of Nov 2024 election night found via WebSearch. Value left null per RUNBOOK.md 5.1."
}
```

**VERIFY.md draft lines:**
Summary table: `| 2024 ⚠️ | presidential-general | — | 7,122 | — | — |` (flagged only
because a misleadingly-named source was examined and rejected, not because a
comparable=false value is being kept; see 5.2 -- actually per schema this
should NOT carry `comparable:false` since no ballots value is kept at all; the
⚠️ here is documentary, mirroring how other null-but-noteworthy rows would be
flagged for human attention in HUMAN_VERIFY.md, not a schema field)
Detail bullet: `- **2024-11-05** (presidential-general): certified final 7,122 ([SoV PDF](https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf)). Election-night ballots: **not found** — the registrar's document titled/filed as "Election-Night-Results" ([DocumentCenter/View/18349](https://www.countyofcolusaca.gov/DocumentCenter/View/18349/Election-Night-Results)) is, per its own internal title block, the "Colusa County Final Report" dated 12/3/2024, Voters Cast 7,122 = certified final exactly. FILENAME IS MISLEADING — verified by direct page-image read, not the URL text.`

**Plateau verdict:** not applicable (null row); if plateau_review.json supported
a REFUTED-style entry for a candidate source that was examined and rejected
(not merely absent), this row would warrant one: "candidate source
/DocumentCenter/View/18349 examined; REFUTED as election-night despite
filename — internal title block says 'Final Report', date 2024-12-03,
Voters Cast exactly equals certified final."

---
## Session summary / open items for a future pass

- **Item 0 (tech record):** complete. Colusa is a confirmed never-adopter of
  e-pollbooks, ASV, sign-scan-go, and the VCA vote-center model through the Oct
  2025 SoS snapshot (three independent SoS editions + the county's own FAQ page).
- **Items 1-6 (all six target elections):** all six certified finals sourced
  from the SoS SoV PDFs (primary confidence, no ambiguity). All six
  election-night numerators are NULL. Four of the six (2016, 2018, 2022, 2024)
  are DIRECTLY CONFIRMED null (not just absent-evidence): the surviving
  "results" document was fetched and read, and in every case its own internal
  report date/title proves it is the certified canvass 20-28 days
  post-election, with a ballot total exactly equal to the SoS certified final.
  The 2024 document is a notable "gotcha": its filename/URL literally contains
  "Election-Night-Results" but its own title block says "Final Report" — a
  systemic naming-template artifact in Colusa's Dominion-based elections
  software, not evidence of timing. 2012 and 2014 are null by the same
  title-and-pattern inference plus total absence of any Wayback captures near
  election night, but their own PDF byte-level metadata could NOT be
  independently confirmed this session because of intermittent
  `curl: (7) Failed to connect to web.archive.org port 443` connectivity
  failures (the CDX JSON API on the same host worked before and after; the
  live `countyofcolusaca.gov` host was unaffected throughout) — **a follow-up
  session should retry**: `curl --max-time 60 "https://web.archive.org/web/20220702140759id_/https://www.countyofcolusa.org/DocumentCenter/View/5436/November-6-2012-Official-Results-By-Contest?bidId=" -o doc_2012.pdf` and the equivalent for
  `https://web.archive.org/web/20190720094634id_/https://www.countyofcolusa.org/DocumentCenter/View/4693`, then `pdfinfo`/`pdftoppm` + direct image read exactly as done for 2016/2018.
- **Not attempted / could extend a future pass:** (a) a browser-driven
  (Claude-in-Chrome) look at `electionresults.sos.ca.gov` and its predecessor
  SoS statewide live-results site for archived per-county returns during the
  actual election nights (a different site than Colusa's own, run by the
  state; not checked this pass due to time budget; would need its own Wayback
  CDX investigation and is a lower-probability route since it's typically
  contest-level vote totals, not a "ballots cast" county total); (b) a direct
  records request / phone call to the Colusa County Clerk-Recorder-Registrar
  (530-458-0500) asking whether any internal election-night tally sheet or
  press release ever existed outside the web (plausible for a small county
  that counts everything centrally and may have only ever produced one
  report); neither is a `FLAG for manual operator` browser-block situation,
  just unexplored due to the 30-40 min/election budget already being spent on
  the (successful) document-forensics work above.
- No item was left in a "could not finish" state relative to the assignment's
  required deliverables; the only gap is the nice-to-have independent
  byte-confirmation for 2012/2014 noted above.
