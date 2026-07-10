# Del Norte County, CA — election-night dossier: statewide PRIMARIES 2012-2024

Control county (`epollbook: null`, `asv: null` in `packages/data/county_tech.json`
/ `data/research/county-tech/del-norte-ca.json`: never-adopter of both
e-pollbooks (three SoS snapshots May 2022/Feb 2024/Oct 2025 all "Do not use")
and ASV (manual/human signature review per on-record 2020 quote), not
Clarity, not VCA/vote-center). This dossier covers the six statewide
primaries (2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05, 2022-06-07,
2024-03-05) as READ-ONLY research to extend
`data/research/election-night/del-norte-ca.json`, which today only carries
the six November generals (2012-2024). Nothing in this file has been written
to the repo; it is a proposed-rows packet for the operator.

Denominators (CA SoS Statement of Vote "Voter Participation Statistics by
County") were re-fetched directly for all 6 primaries. Numerators were
researched via the SAME containers documented in the generals file: the
county's old Google-Sites-hosted numbered election-night PDF release series
(2012-2018, domain-migrated partway through) and, since 2022, the county's
live public Google Drive "Elections Postings (Archive)" folder
(`https://drive.google.com/embeddedfolderview?id=1PJ7b233V3_twHam_vIbbmgze1kpfW5AT#list`,
linked from `https://www.co.del-norte.ca.us/departments/Elections`).
**Finding that changes the general-election playbook:** for primaries, the
live Drive archive turns out to hold folders back to **2016** (not just
2022+), so 2016 and 2018 primary PDFs were fetched live, no Wayback
needed. 2012 and 2014 primaries are NOT in that Drive archive (it starts at
2016) and had to be checked against the old Google-Sites domain the same
way 2012-general was — both came back null, for two different reasons (see
below).

Working files (downloaded PDFs, renders, CDX JSON) are in
`/private/tmp/claude-501/-Users-sbuss-workspace-sf-election-count/cbd9561c-405d-4e44-8f38-6a4a9bd48e60/scratchpad/delnorte/`.
All PDFs in this family are scanned Canon-photocopier output (Creator
`Canon iR-ADV C5240/C5740/4245 PDF`) with **no text layer**
(`pdftotext` returns empty on every file checked); every ballot count below
was read visually from a 150dpi (400dpi for one timestamp disambiguation)
`pdftoppm` render, never OCR.

---

## ITEM 1 of 6 — 2012-06-05 Presidential Primary — NULL

**Certified final (denominator).** CA SoS SoV, "Voter Participation
Statistics by County," 2012 primary:
`https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf`
(re-fetched 2026-07-10, HTTP 200; note this file's own path segment is
`voter-reg-stats`, not `voter-participation-stats` as later years use — a
real naming difference, confirmed via the SoS's own "Statement of Vote"
page for this election, not guessed). Del Norte line (row 13):
`Del Norte    18   18,288   11,815   1,826   3,416   5,242   65.17%   44.37%   28.66%`
— columns are Precincts / Eligible-to-Register / Registered Voters /
Precinct Voters / Vote-By-Mail Voters / **Total Voters** / %VBM / Turnout-of-
Registered / Turnout-of-Eligible. **Total Voters = 5,242.**

**Plateau (numerator): NULL — no election-night report container survives.**
Exhaustive search of the old "elect" Google Site
(`elections.co.del-norte.ca.us`, the domain used for 2012-general and
2014-general/primary):
- The site's nav has exactly one 2012-primary-branded page,
  `/elections/2012-primary-election-viewer` (22 Wayback captures,
  2012-09-17 through 2021-10-18, all HTTP 200). Fetched and inspected the
  earliest capture directly
  (`https://web.archive.org/web/20120917040355id_/http://elections.co.del-norte.ca.us:80/elections/2012-primary-election-viewer`):
  it is NOT a results page — it embeds a USTREAM live-video widget
  ("Live Stream - Ballot Room") and a Google Group forum gadget. No results
  numbers, no PDF attachments, ever. Confirmed identical structure across
  all 22 captures (page persisted as site-nav cruft for 9 years after the
  election, content unchanged).
- There is no `2012-primary-election-results` attachment page analogous to
  the site's own `2012-general-election-results` page (which DOES exist,
  with a numbered Release1-5_FINAL.pdf series, and is the container the
  2012-general NULL row already documents as unreachable-bytes). CDX
  prefix query
  `http://web.archive.org/cdx/search/cdx?url=elections.co.del-norte.ca.us/elections&matchType=prefix&output=json&limit=500`
  (500-row cap, re-run 2026-07-10) returns every page ever crawled under
  `/elections/`; grepped for `primary` and `2012` — the only 2012-primary
  hit is the video-viewer page above. No `june-5-2012...` path exists at
  any capture (`url=elections.co.del-norte.ca.us/elections/june-5-2012&matchType=prefix`
  → `[]`).
- Not in the live Google Drive "Elections Postings (Archive)" folder
  either — that folder's earliest election is 2016 (see preamble).
- Local news: web search for Del Norte Triplicate June 2012 primary
  election-night coverage returned no article with a usable ballot count
  (only later, unrelated Triplicate stories from 2022-2024 and general SoS
  turnout summaries surfaced); Triplicate's own site search does not expose
  a June 2012 archive page, and NewsBank/SFPL access was not attempted for
  a non-SF county (out of scope per RUNBOOK 0's domain map).
- Clarity: confirmed elsewhere in this dataset that Del Norte was never on
  Clarity (`results.enr.clarityelections.com/CA/Del_Norte/` 404s).

No substitute denominator or later-canvass number used. Left null per
RUNBOOK 5.1.

**Draft JSON row:**
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 5242,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "NULL PER 5.1: no election-night report container survives. The county's only 2012-primary-branded page on the old 'elect' Google Site, elections.co.del-norte.ca.us/elections/2012-primary-election-viewer (22 Wayback captures 2012-09-17 through 2021-10-18, all HTTP 200), is a live-video/forum embed page (USTREAM 'Live Stream - Ballot Room' + Google Group gadget), never a results/PDF page -- confirmed by direct fetch of the earliest capture. Unlike 2012-general, there is no numbered-release attachment page at all for the primary (CDX prefix query over elections.co.del-norte.ca.us/elections, 500-row cap, re-run 2026-07-10, shows no june-5-2012 or 2012-primary-election-results path ever crawled). Not in the live Google Drive 'Elections Postings (Archive)' folder either (that archive's earliest election is 2016). Del Norte Triplicate searched for June 2012 primary-night coverage; no article with a ballot count found. Clarity not used (confirmed elsewhere: results.enr.clarityelections.com/CA/Del_Norte/ 404s). Certified final 5,242 from SoS SoV 2012-primary Total Voters column (re-fetched 2026-07-10, note this file's own path segment reads 'voter-reg-stats', a genuine naming difference from later years' 'voter-participation-stats', confirmed via the SoS's own election-page link, not guessed)."
}
```

**Draft VERIFY.md line:** `| 2012 | presidential-primary | — | 5,242 | NULL | none | — |`

**Draft plateau_review.json:** not applicable (no sourced row; null rows carry no verdict entry per existing dataset convention — no other del-norte-ca null row has one either).

**Verdict:** NULL, high-confidence null (exhaustive container search, two independent negative findings: video-embed page + absent results page). No operator action needed unless someone wants to try NewsBank/Triplicate paid archive access, which is outside this dataset's normal toolkit.

---

## ITEM 2 of 6 — 2014-06-03 Statewide Primary — NULL (but timing-characterized)

**Certified final (denominator).** CA SoS SoV, 2014 primary:
`https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf`
(misspelling "particpiation" intact, matches the RUNBOOK 6.1 note that 2014
uses this exact misspelled filename; re-fetched 2026-07-10, HTTP 200). Del
Norte line: `Del Norte   18   18,378   12,398   2,288   3,662   5,950   61.55%   47.99%   32.38%`.
**Total Voters = 5,950.**

**Plateau (numerator): NULL — container found, index page recovered, but
the actual PDF bytes were never crawled.** This is the SAME failure mode as
2012-general (documented in the existing JSON), on the SAME old "elect"
Google Site, one election-cycle later.

- The county's dated results index page IS archived and readable:
  `https://web.archive.org/web/20140608033400id_/http://elections.co.del-norte.ca.us:80/elections/june-3-2014-primary-election`
  (earliest of 4 HTML captures, 2014-06-08 through 2014-10-18, all 200).
  It lists exactly 3 attachments — **Final, Release 1, Release 2** — same
  3-release-then-Final pattern as the November 2014 general (which this
  page's sibling `november-4-2014-general-election` index also shows).
- **The page embeds each attachment's Google-Sites upload epoch
  (millisecond `data-val` timestamp), which independently timing-brackets
  the series without needing the PDF bytes:**
  - Release 1: `data-val="1401852329919"` → **2014-06-03 20:25:29 PDT**
    (election night, ~25 min after 8pm poll close — the classic first
    tranche)
  - Release 2: `data-val="1401858489459"` → **2014-06-03 22:08:09 PDT**
    (election night, ~2h08m after poll close)
  - Final: `data-val="1402097498090"` → **2014-06-06 16:31:38 PDT**
    (**3 days later** — exactly the same 3-day Unofficial-to-Final gap
    pattern as the 2014 GENERAL row's Release 2 → Release 3-Final)
  - This upload-timestamp evidence, on its own, would satisfy RUNBOOK 8's
    self-description + next-report-days-later legs for Release 2 IF the
    ballot count inside it could be read. It cannot.
- **The PDF bytes themselves are unrecoverable.** Every attachment link on
  the index page resolves through the same session-scoped signed-redirect
  scheme as 2012/2014-general
  (`425abd7a-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/elect/elections/june-3-2014-primary-election/...`).
  CDX exact-URL query on that content host
  (`https://web.archive.org/cdx/search/cdx?url=425abd7a-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/elect/elections/june-3-2014-primary-election/June%203%2C%20Primary%20Election%20Results%20-%20Final.pdf&matchType=exact&output=json&limit=50`,
  re-run 2026-07-10) returns exactly one row, a `warc/revisit` record
  (statuscode `-`, length 901 bytes — far too small to be a scanned PDF,
  consistent with a redirect/error page, not content). Direct `id_` replay
  of that exact capture (`20220414210026`) serves the Wayback "not
  available" HTML shell, not a PDF (`file` reports "HTML document", 142KB
  of Wayback chrome). A prefix CDX query over the same content-host path
  (`.../june-3-2014-primary-election&matchType=prefix`) returns 7 rows
  total, ALL `text/html` `302` redirect stubs or the one revisit record
  above — never `application/pdf`. Release 1's redirect target was never
  independently crawled at all (0 rows for its content-host URL).
- Not in the live Google Drive archive (starts 2016). Del Norte Triplicate
  searched for June 2014 primary-night coverage; no usable article found.

**Draft JSON row:**
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 5950,
  "election_night_pct": null,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "NULL PER 5.1: container found and timing-characterized, but the PDF bytes were never crawled -- same failure mode as 2012-general, one cycle later, same old 'elect' Google Site. The county's dated index page (https://web.archive.org/web/20140608033400id_/http://elections.co.del-norte.ca.us:80/elections/june-3-2014-primary-election, re-verified 2026-07-10) lists exactly 3 attachments (Final, Release 1, Release 2), matching the same 2014 general's 3-release-then-Final pattern, and embeds each attachment's Google-Sites upload epoch: Release 1 = 2014-06-03 20:25:29 PDT (election night, first tranche), Release 2 = 2014-06-03 22:08:09 PDT (election night), Final = 2014-06-06 16:31:38 PDT (3 days later) -- this upload-timestamp bracket alone would satisfy runbook-8 plateau evidence for Release 2 IF its ballot count were readable, but it is not: every attachment resolves via the session-scoped signed-redirect scheme to 425abd7a-a-03565450-s-sites.googlegroups.com/a/co.del-norte.ca.us/elect/elections/june-3-2014-primary-election/, and an exact-URL CDX query on that content host for Final.pdf (re-run 2026-07-10) returns only one warc/revisit record (901 bytes, not real PDF content; direct id_ replay of it serves the Wayback not-available HTML shell, confirmed by fetching and running `file` on it); a prefix query over the same path returns 7 rows, all text/html 302 stubs or the one revisit record, never application/pdf; Release 1's target was never crawled at any URL variant (0 rows). Not in the live Google Drive archive (that archive's earliest election is 2016, confirmed by listing its root folder). Del Norte Triplicate searched for June 2014 primary-night coverage; no usable article found. No substitute denominator or later-canvass number used. Certified final 5,950 from SoS SoV 2014-primary Total Voters column (misspelled filename 'voter-particpiation' intact, matches the 2014-general row's same-year misspelling; re-fetched 2026-07-10)."
}
```

**Draft VERIFY.md line:** `| 2014 | statewide-primary | — | 5,950 | NULL | none | — |`

**Draft plateau_review.json:** not applicable (null row).

**Verdict:** NULL. Unlike 2012, this one has real timing evidence (upload
epochs) that PROVES a genuine election-night plateau existed and even
brackets it to the minute — it is just unreadable. FLAG for manual operator:
if anyone ever gets a human-browser session that can walk
`docs.google.com/viewer?...srcid=...` (the index page's alternate "View"
links, which route through Google's own doc-viewer rather than the
googlegroups redirect and were NOT tried here) that might recover the
actual page image where curl/CDX cannot; not attempted this pass because it
requires an interactive Google Docs viewer render, which is a
Claude-in-Chrome main-session task, not a parallelizable one.

---

## ITEM 3 of 6 — 2016-06-07 Presidential Primary — CONFIRMED, 5,020 / 6,185 = 81.16%

**Certified final (denominator).** CA SoS SoV, 2016 primary:
`https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf`
(note: no `sov/` or `pdf/` sub-segment for this year, confirmed by
fetching the SoS's own election page and 200-testing the link; re-fetched
2026-07-10). Del Norte line: `Del Norte   18   18,073   13,585   2,184   4,001   6,185   64.69%   45.53%   34.22%`.
**Total Voters = 6,185.**

**Plateau (numerator).** Recovered LIVE from the county's public Google
Drive "Elections Postings (Archive)" folder → child folder "June 7, 2016
Primary Election Results"
(`https://drive.google.com/drive/folders/1nwgviB22IuQIVWjSquSY6Y_6APYvMgnH`),
which holds a clean 5-file numbered release series: Release 1-5, Release 5
explicitly suffixed "(FINAL RESULTS)". **The plateau is Release 3, not
Release 4** — determined by checking every file's actual PDF `CreationDate`
metadata (`pdfinfo`), not by assuming the numbering:
```
Release 1: Tue Jun  7 21:04:28 2016 PDT   (election night)
Release 2: Tue Jun  7 22:01:22 2016 PDT   (election night)
Release 3: Tue Jun  7 23:09:27 2016 PDT   (election night)  <- file CreationDate
Release 4: Fri Jun 10 13:35:57 2016 PDT   (3 days later)
Release 5: Wed Jun 15 17:05:29 2016 PDT   (8 days later, FINAL)
```
Downloaded direct (`https://drive.google.com/uc?export=download&id=<fileId>`,
no auth needed) and rendered Release 3 at 150dpi
(`pdftoppm -png -r 150 -f 1 -l 1 2016p_r3.pdf`); page 1 reads (verbatim):
"Election Summary Report / Closed Primary / County of Del Norte /
June 07, 2016 / Summary for: All Contests, All Districts, All Counting
Groups / **Final Election Night Report** / **Unofficial Results** /
Precincts Reported: 18 of 18 (100.00%) / Registered Voters: 5,020 of 13,525
(37.12%) / **Ballots Cast: 5,020**." Top-right printed page timestamp reads
"6/7/2016 10:07:46 PM" (confirmed at 400dpi crop; this printed
report-generation stamp runs ~62 minutes ahead of the file's own
`CreationDate` metadata of 11:09:27 PM — an unusually large scan/upload lag
for this dataset, but both timestamps are still comfortably within election
night and do not change which release is the plateau). **Ballots Cast is
stated directly and unambiguously; no mislabeling to resolve this year.**

Rendered Release 4 (150dpi) as the bracket leg: page reads "Election
Summary Report / ... / June 07, 2016 / **Friday Report** / Unofficial
Results / Precincts Reported: 18 of 18 (100.00%) / Registered Voters: 6,178
of 13,525 (45.68%) / Ballots Cast: 6,178", printed timestamp "6/10/2016
10:09:09 AM" — 3 days later, retitled away from "Election Night," count up
1,158 ballots. This is the bracket-proof leg per RUNBOOK 8.

**Arithmetic:** 5,020 / 6,185 = **81.16%**.

**Draft JSON row:**
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 5020,
  "certified_final": 6185,
  "election_night_pct": 81.16,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://drive.google.com/uc?export=download&id=1Y1Kj4-IqXW5uEgZh6c206EsmNoj9pSEN",
  "confidence": "primary",
  "note": "PLATEAU = Release 3 of 5 in the county's numbered 2016 primary election-night PDF series, recovered LIVE (no Wayback needed) from the county's public Google Drive 'Elections Postings (Archive)' folder, child folder 'June 7, 2016 Primary Election Results' (drive.google.com/drive/folders/1nwgviB22IuQIVWjSquSY6Y_6APYvMgnH). Plateau determined by checking every release's actual PDF CreationDate (pdfinfo), NOT the release number: Release 1 9:04:28 PM, Release 2 10:01:22 PM, Release 3 11:09:27 PM (all election night 6/7/2016), Release 4 CreationDate Fri Jun 10 1:35:57 PM (3 days later), Release 5 CreationDate Wed Jun 15 5:05:29 PM (8 days later, filename-suffixed FINAL RESULTS) -- i.e. Release 4 is already post-night, unlike the general-election years where Release 4 was the plateau; the release NUMBER alone is not a safe proxy for plateau position and must be checked per file. Self-titled (exact document header) 'Final Election Night Report / Unofficial Results', printed page timestamp 6/7/2016 10:07:46 PM (confirmed at 400dpi crop; runs ~62 min behind the file's own CreationDate metadata, an unusually large scan/upload lag for this dataset but still same-night), 18 of 18 precincts (100.00%), Registered Voters 5,020 of 13,525 (37.12%), Ballots Cast 5,020 (stated directly and unambiguously, no ballot-card mislabeling this file). Bracket leg: Release 4, rendered, self-retitled 'Friday Report' (dropping 'Election Night'), printed timestamp 6/10/2016 10:09:09 AM (3 days later), Ballots Cast 6,178 -- confirms Release 3 was the last report before the canvass resumed. Scanned Canon-photocopier PDF (Creator Canon iR-ADV C5240 PDF), no text layer (pdftotext empty, confirmed 2026-07-10); read visually via 150dpi pdftoppm render (200dpi/400dpi crop used only to disambiguate the printed timestamp digits). Arithmetic: 5,020/6,185 = 81.16%, the highest of Del Norte's primary shares recovered this pass, consistent with the runbook's small-rural-county 80-95% calibration band seen across this county's general-election rows (83-89% for 2014-2018). Del Norte never adopted e-pollbooks or ASV (control county); vs_epollbook and vs_asv both n/a."
}
```

**Draft VERIFY.md line:** `| 2016 | presidential-primary | 5,020 | 6,185 | 81.2% | primary | [link](https://drive.google.com/uc?export=download&id=1Y1Kj4-IqXW5uEgZh6c206EsmNoj9pSEN) |`

**Draft plateau_review.json:**
```json
{
  "slug": "del-norte-ca",
  "date": "2016-06-07",
  "verdict": "CONFIRMED",
  "basis": "self-labeled 'Final Election Night Report / Unofficial Results', last of a numbered on-night release series (numbering does NOT equal plateau position here -- verified via each file's own CreationDate), next report 3 days later retitled 'Friday Report' at a higher count",
  "evidence": "Release 3/5, file CreationDate 6/7/2016 11:09:27 PM PDT / printed page stamp 10:07:46 PM, 18/18 precincts (100%), Ballots Cast 5,020/13,525 (37.12%); Release 4 (next in series, NOT the plateau despite the numbering) is CreationDate 6/10/2016 (3 days later), Ballots Cast 6,178 -- confirms Release 3 was the last report before the canvass resumed. Release 5 (6/15, 8 days later) explicitly filename-suffixed FINAL RESULTS."
}
```

**Verdict / evidence class:** CONFIRMED (self-description + bracket leg,
both directly render-verified, no proxy needed). No FLAG.

---

## ITEM 4 of 6 — 2018-06-05 Statewide Primary — CONFIRMED, 4,637 / 5,472 = 84.74%

**Certified final (denominator).** CA SoS SoV, 2018 primary:
`https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf`
(re-fetched 2026-07-10, HTTP 200). Del Norte line: `Del Norte   18   17,889   14,141   1,796   3,676   5,472   67.18%   38.70%   30.59%`.
**Total Voters = 5,472.**

**Plateau (numerator).** Recovered LIVE from the same Drive archive, child
folder "June 5, 2018 Primary Election"
(`https://drive.google.com/drive/folders/1j_tx1oilfY7jlehwAx8Njwa7WH21-_CQ`;
NOTE — there is a second, differently-ID'd sibling folder in the archive
root also named close to "June 5, 2018 Statewide Direct Primary Election"
that holds only filing/candidate-list documents, no releases; the release
series is in the FIRST folder only, and its filenames are the disambiguator
if this is ever re-checked). 6-file release series, Release 6 suffixed
"Final Uncertified"; PDF `CreationDate` metadata:
```
Release 1: Tue Jun  5 20:01:24 2018 PDT   (election night)
Release 2: Tue Jun  5 21:07:40 2018 PDT   (election night)
Release 3: Tue Jun  5 21:28:06 2018 PDT   (election night)
Release 4: Tue Jun  5 21:46:30 2018 PDT   (election night)  <- plateau
Release 5: Thu Jun  7 11:01:30 2018 PDT   (2 days later)
Release 6: Thu Jun 14 16:56:20 2018 PDT   (9 days later, Final Uncertified)
```
Rendered Release 4 at 150dpi: front page reads "Summary for: All Contests,
All Districts, All Tabulators, All Counting Groups / STATEWIDE GUB PRIMARY
ELECTION / TUESDAY, JUNE 5, 2018 / TOTAL RESULT SUMMARY REPORT
(UNOFFICIAL)", printed timestamp "6/5/2018 9:42:38 PM" (election night).
Front page prints "Precincts Reported: 18 of 18 (100.00%) / **Registered
Voters: 4,637 of 14,151 (32.77%)** / Ballots Cast: 9,284." **This is
RUNBOOK 7.5's known Del Norte mislabeling pattern** (already documented for
this county's own 2016-general row): "Registered Voters" on the front page
is actually TURNOUT, and the raw "Ballots Cast" figure is the ballot-CARD
count (~2 cards/voter for a many-contest statewide primary), not the voter
count. Disambiguated exactly as RUNBOOK 7.5 prescribes — checked the
per-contest "Times Cast" row: the GOVERNOR contest (page 2) prints "Times
Cast ... Total 4,637 / 14,151 32.77%", an EXACT match to the front page's
"Registered Voters" field and its own printed percentage. **4,637 is the
correct people-count (voters), not 9,284 (cards).**

Bracket leg: rendered Release 5 (2 days later), front page retitled
"COUNTYWIDE RESULT SUMMARY REPORT / **1st Update (6/7/2018)** /
(UNOFFICIAL)", printed timestamp "6/7/2018 10:58:12 AM", "Registered
Voters: 5,347 of 14,151 (37.79%) / Ballots Cast: 10,707" — count up (5,347
vs 4,637), title changed from a plain election-night summary label to an
explicit dated "Update," 2 days later.

**Arithmetic:** 4,637 / 5,472 = **84.74%**.

**Draft JSON row:**
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 4637,
  "certified_final": 5472,
  "election_night_pct": 84.74,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://drive.google.com/uc?export=download&id=1xrb3b2KmuaR0EhVysw--eKyjXANMzy6k",
  "confidence": "primary",
  "note": "PLATEAU = Release 4 of 6 in the county's numbered 2018 primary election-night PDF series, recovered LIVE from the county's public Google Drive 'Elections Postings (Archive)' folder, child folder 'June 5, 2018 Primary Election' (drive.google.com/drive/folders/1j_tx1oilfY7jlehwAx8Njwa7WH21-_CQ; a second sibling folder in the archive root with a near-identical name holds only filing/candidate documents, not releases -- disambiguated by filename). PDF CreationDate metadata for the full series: Release 1 8:01:24 PM, Release 2 9:07:40 PM, Release 3 9:28:06 PM, Release 4 9:46:30 PM (all election night 6/5/2018), Release 5 CreationDate Thu Jun 7 11:01:30 AM (2 days later), Release 6 CreationDate Thu Jun 14 4:56:20 PM (9 days later, filename-suffixed 'Final Uncertified'). Release 4 front page reads 'TOTAL RESULT SUMMARY REPORT (UNOFFICIAL)', printed timestamp 6/5/2018 9:42:38 PM, 18/18 precincts (100%). RUNBOOK 7.5 mislabel pattern confirmed present (same as this county's own 2016-general row): front page prints 'Registered Voters: 4,637 of 14,151 (32.77%)' and a separate 'Ballots Cast: 9,284' -- the 9,284 figure is ballot CARDS (~2x, many-contest statewide primary), not voters; disambiguated via the per-contest Times Cast row (GOVERNOR contest, page 2: 'Times Cast ... Total 4,637/14,151 32.77%', an exact match to the front-page 'Registered Voters' field and its own printed percentage) -- 4,637 is the correct people-count and is used here, 9,284 is not. Bracket leg: Release 5, rendered, retitled 'COUNTYWIDE RESULT SUMMARY REPORT / 1st Update (6/7/2018) / (UNOFFICIAL)', printed timestamp 6/7/2018 10:58:12 AM (2 days later), 'Registered Voters' field up to 5,347/14,151 -- confirms Release 4 was the last report before the canvass resumed. Scanned Canon-photocopier PDF (Creator Canon iR-ADV C5240 PDF), no text layer (pdftotext empty, confirmed 2026-07-10); read visually via 150dpi pdftoppm render. Arithmetic: 4,637/5,472 = 84.74%, close to this county's 2016-general (83.30%) and 2018-general (84.45%) shares, consistent with the small-rural-county 80-95% calibration band. Del Norte never adopted e-pollbooks or ASV (control county); vs_epollbook and vs_asv both n/a."
}
```

**Draft VERIFY.md line:** `| 2018 | statewide-primary | 4,637 | 5,472 | 84.7% | primary | [link](https://drive.google.com/uc?export=download&id=1xrb3b2KmuaR0EhVysw--eKyjXANMzy6k) |`

**Draft plateau_review.json:**
```json
{
  "slug": "del-norte-ca",
  "date": "2018-06-05",
  "verdict": "CONFIRMED",
  "basis": "late-night internal timestamp (self-description leg), last of a numbered on-night release series before a 2-days-later report explicitly relabeled 'Update' at a higher count (bracket leg); front-page ballot figure disambiguated per the runbook's known Del Norte registered-voters/times-cast mislabel using the per-contest Times Cast cross-check",
  "evidence": "Release 4/6, CreationDate 6/5/2018 9:46:30 PM PDT / printed page stamp 9:42:38 PM, 18/18 precincts (100%); front page 'Registered Voters: 4,637/14,151 (32.77%)' cross-checked against GOVERNOR contest Times Cast 4,637/14,151 (32.77%) -- exact match confirms 4,637 (not the front page's separately printed 'Ballots Cast: 9,284', which is ballot cards) is the true turnout figure. Release 5 (6/7, 2 days later) retitled '1st Update (6/7/2018)', Registered-Voters field up to 5,347/14,151 -- confirms Release 4 was the last report before the canvass resumed."
}
```

**Verdict / evidence class:** CONFIRMED, but flag the mislabel resolution
for a human sanity check since it changes the headline number by ~2x if
misread. **FLAG for manual operator**: please re-open
`https://drive.google.com/uc?export=download&id=1xrb3b2KmuaR0EhVysw--eKyjXANMzy6k`
and confirm page 1's "Registered Voters: 4,637 of 14,151 (32.77%)" line and
page 2's Governor-contest "Times Cast ... 4,637 / 14,151 32.77%" line both
read as transcribed above; if either digit differs the pct changes
materially.

---

## ITEM 5 of 6 — 2022-06-07 Statewide Primary — CONFIRMED, 4,019 / 5,989 = 67.11%

**Certified final (denominator).** CA SoS SoV, 2022 primary:
`https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf`
(re-fetched 2026-07-10, HTTP 200). Del Norte line: `Del Norte   19   19,262   15,256   712   5,277   5,989   88.11%   39.26%   31.09%`.
**Total Voters = 5,989.**

**Plateau (numerator).** Recovered LIVE from the same Drive archive, child
folder "June 7, 2022 Statewide Direct Primary Election"
(`https://drive.google.com/drive/folders/1PpwW41_22SVlWDGeZ2JqrgIKc9FusGDu`).
4 numbered releases plus a separately-filed "Final Official Results.pdf"
(same folder-organization convention as the 2022-GENERAL row already in the
dataset, which used the same folder ID). PDF `CreationDate` metadata:
```
Release 1: Tue Jun  7 20:07:34 2022 PDT   (election night)
Release 2: Tue Jun  7 21:07:33 2022 PDT   (election night)
Release 3: Tue Jun  7 22:06:43 2022 PDT   (election night)  <- plateau
Release 4: Fri Jun 10 15:03:59 2022 PDT   (3 days later)
Final:     Tue Jul  5 10:13:31 2022 PDT   (28 days later, certified)
```
Rendered Release 3 at 150dpi: page 1 reads (verbatim, note the template
mislabels the election TYPE — see caveat below) "Election Summary Report /
**General Election** / Del Norte / June 07, 2022 / Summary for: All
Contests, All Districts, All Tabulators, All Counting Groups / **Final
Report - Unoffficial Results** [sic, double-f typo in the county's own
template] / 19 of 19 Precincts Reporting / **Election Night Totals** /
Precincts Reported: 19 of 19 (100.00%) / **Voters Cast: 4,019 of 15,317
(26.24%)**." **Caveat:** the report's own header template prints "General
Election" even though June 7, 2022 was unambiguously the statewide
primary (no general election occurred that date; this is the same PDF
software template quirk, not a wrong-file mixup — confirmed by the date,
by "19 of 19 Precincts" matching this county's 2022 precinct count
elsewhere in the dataset, and by the file living inside the
"June 7, 2022 Statewide Direct Primary Election" Drive folder alongside the
other 3 same-night releases). "Voters Cast" is printed directly and
unambiguously this year — no mislabel-disambiguation needed.

Bracket leg: rendered Release 4 (3 days later): page 1 reads "Election
Update - Unoffficial Results / 19 of 19 Precincts Reporting / **06/10/2022**",
printed timestamp "6/10/2022 2:54:46 PM", "Voters Cast: 5,929 of 15,317
(38.71%)" — retitled from "Final Report...Election Night Totals" to
"Election Update," count up 1,910 voters, 3 days later.

**Arithmetic:** 4,019 / 5,989 = **67.11%**.

**Draft JSON row:**
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 4019,
  "certified_final": 5989,
  "election_night_pct": 67.11,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://drive.google.com/uc?export=download&id=1bbTlt98fwmF02gJkIgni_JgMBMQvwS9L",
  "confidence": "primary",
  "note": "PLATEAU = Release 3 of 4 same-night numbered reports in the county's live Google Drive election-postings archive, folder 'June 7, 2022 Statewide Direct Primary Election' (drive.google.com/drive/folders/1PpwW41_22SVlWDGeZ2JqrgIKc9FusGDu; same folder-organization convention as this county's own 2022-general row). PDF CreationDate metadata: Release 1 8:07:34 PM, Release 2 9:07:33 PM, Release 3 10:06:43 PM (all election night 6/7/2022), Release 4 CreationDate Fri Jun 10 3:03:59 PM (3 days later), a separately-filed 'Final Official Results.pdf' CreationDate Tue Jul 5 10:13:31 AM (28 days later, certified). Release 3 self-titled (exact document header) 'Final Report - Unoffficial Results [sic, county's own double-f typo] / 19 of 19 Precincts Reporting / Election Night Totals', printed timestamp 6/7/2022 9:58:12 PM, Voters Cast 4,019 of 15,317 (26.24%) -- stated directly, no mislabel this year. CAVEAT: the report's own header template prints 'General Election' even though this is the statewide primary (no general occurred 6/7/2022); confirmed as a template quirk not a wrong file via the date, the matching 19-precinct count, and the file's location inside the primary-named Drive folder alongside the other 3 same-night releases. Bracket leg: Release 4, rendered, retitled 'Election Update - Unoffficial Results / 19 of 19 Precincts Reporting / 06/10/2022', printed timestamp 6/10/2022 2:54:46 PM (3 days later), Voters Cast 5,929/15,317 -- confirms Release 3 was the last report before the canvass resumed. Scanned Canon-photocopier PDF (Creator Canon iR-ADV C5740 PDF, matching this county's 2022-general and 2024 scanner model), no text layer (pdftotext empty, confirmed 2026-07-10); read visually via 150dpi pdftoppm render. Arithmetic: 4,019/5,989 = 67.11%, noticeably lower than this county's 2016/2018 primary shares (81.16%/84.74%) recovered this pass, consistent with the same statewide near-Election-Day mail-ballot growth pattern already documented for this county's 2022-general row (74.70%, also down from 83-89% in 2014-2018) -- not a technology change (Del Norte never adopted e-pollbooks or ASV). vs_epollbook and vs_asv both n/a (control county)."
}
```

**Draft VERIFY.md line:** `| 2022 | statewide-primary | 4,019 | 5,989 | 67.1% | primary | [link](https://drive.google.com/uc?export=download&id=1bbTlt98fwmF02gJkIgni_JgMBMQvwS9L) |`

**Draft plateau_review.json:**
```json
{
  "slug": "del-norte-ca",
  "date": "2022-06-07",
  "verdict": "CONFIRMED",
  "basis": "document explicitly titled 'Final Report - Unoffficial Results ... Election Night Totals'; next report 3 days later explicitly retitled 'Election Update' at a higher count",
  "evidence": "Release 3/4, printed timestamp 6/7/2022 9:58:12 PM, 19/19 precincts (100%), Voters Cast 4,019/15,317 (26.24%); Release 4 (6/10/2022, 3 days later) retitled 'Election Update - Unoffficial Results', Voters Cast 5,929/15,317 -- confirms Release 3 was the last report before the canvass resumed. Report header template mislabels election type 'General Election' (confirmed template quirk, not wrong file, per date/precinct-count/folder-location cross-checks)."
}
```

**Verdict / evidence class:** CONFIRMED (both legs directly render-verified).
No FLAG.

---

## ITEM 6 of 6 — 2024-03-05 Presidential Primary — CONFIRMED, 3,285 / 6,121 = 53.67%

**Certified final (denominator).** CA SoS SoV, 2024 primary:
`https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf`
(re-fetched 2026-07-10, HTTP 200). Del Norte line: `Del Norte   19   18,870   14,717   818   5,303   6,121   86.64%   41.59%   32.44%`.
**Total Voters = 6,121.**

**Plateau (numerator).** Recovered LIVE from the same Drive archive, child
folder "March 5, 2024 Primary Election"
(`https://drive.google.com/drive/folders/15GORlqWIpDXSGiK0ShEo4VPnBXoIACqk`;
sibling to this county's already-dataset 2024-general folder). 5 numbered
releases plus a separately-filed "March 5, 2024 SOV.pdf" (county's own
certified statement, not used here — CA-SoS SoV used instead per RUNBOOK
6.1). PDF `CreationDate` metadata:
```
Release 1: Tue Mar  5 20:02:35 2024 PST   (election night)
Release 2: Tue Mar  5 21:17:45 2024 PST   (election night)
Release 3: Tue Mar  5 21:51:11 2024 PST   (election night)  <- plateau
Release 4: Fri Mar  8 15:24:59 2024 PST   (3 days later)
Release 5: Fri Mar 15 15:22:34 2024 PDT   (10 days later)
```
Rendered Release 3 at 150dpi: page 1 reads "Election Summary Report /
Closed Primary / Del Norte County / March 05, 2024 / **Presidential
Primary Election** / 19 Precincts Reporting / **Unofficial Results** /
Precincts Reported: 19 of 19 (100.00%) / **Voters Cast: 3,285 of 14,743
(22.28%)**," printed timestamp "3/5/2024 9:48:44 PM." Stated directly and
unambiguously — no mislabel. (This release's title is plainer than the
"Election Night Final"-style headers seen elsewhere; the self-description
leg here rests on the late-night internal timestamp, per RUNBOOK 8's
"late-night internal timestamp" alternative to a self-labeled title.)

Bracket leg: rendered Release 4 (3 days later): page 1 retitled
"Unofficial Results - **Friday Report**," printed timestamp "3/8/2024
3:05:29 PM," "Voters Cast: 6,055 of 14,743 (41.07%)" — count up 2,770
voters, 3 days later, "Friday Report" label replacing the plain
election-night phrasing.

**Arithmetic:** 3,285 / 6,121 = **53.67%**.

**Draft JSON row:**
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 3285,
  "certified_final": 6121,
  "election_night_pct": 53.67,
  "vs_epollbook": "n/a",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://drive.google.com/uc?export=download&id=1RaZaZq6m6Wy2vpSYmj3txRh6--X5GThS",
  "confidence": "primary",
  "note": "PLATEAU = Release 3 of 5 in the county's numbered 2024 primary election-night PDF series, recovered LIVE from the county's public Google Drive 'Elections Postings (Archive)' folder, child folder 'March 5, 2024 Primary Election' (drive.google.com/drive/folders/15GORlqWIpDXSGiK0ShEo4VPnBXoIACqk; sibling to this county's already-dataset 2024-general folder). PDF CreationDate metadata: Release 1 8:02:35 PM, Release 2 9:17:45 PM, Release 3 9:51:11 PM (all election night 3/5/2024), Release 4 CreationDate Fri Mar 8 3:24:59 PM (3 days later), Release 5 CreationDate Fri Mar 15 3:22:34 PM (10 days later); a separately-filed 'March 5, 2024 SOV.pdf' (county's own certified statement) exists in the same folder but is not used -- the CA SoS SoV is the denominator per runbook 6.1. Release 3 self-titled 'Presidential Primary Election / 19 Precincts Reporting / Unofficial Results', printed timestamp 3/5/2024 9:48:44 PM (the late-night internal timestamp is the self-description leg here per runbook 8's alternative to an explicit 'Final'/'Election Night' title -- this release's header is plainer than some other years'), 19/19 precincts (100%), Voters Cast 3,285 of 14,743 (22.28%) -- stated directly, no mislabel. Bracket leg: Release 4, rendered, retitled 'Unofficial Results - Friday Report', printed timestamp 3/8/2024 3:05:29 PM (3 days later), Voters Cast 6,055/14,743 (41.07%) -- confirms Release 3 was the last report before the canvass resumed. Scanned Canon-photocopier PDF (Creator Canon iR-ADV C5740 PDF), no text layer (pdftotext empty, confirmed 2026-07-10); read visually via 150dpi pdftoppm render. Arithmetic: 3,285/6,121 = 53.67%, the lowest of Del Norte's primary shares recovered this pass and markedly below the 2022 primary (67.11%), mirroring this county's own 2024-general share (62.94%, its lowest general-election share) and the same statewide near-Election-Day mail-ballot growth trend documented there -- not a technology change (Del Norte never adopted e-pollbooks or ASV). vs_epollbook and vs_asv both n/a (control county, no adoption event)."
}
```

**Draft VERIFY.md line:** `| 2024 | presidential-primary | 3,285 | 6,121 | 53.7% | primary | [link](https://drive.google.com/uc?export=download&id=1RaZaZq6m6Wy2vpSYmj3txRh6--X5GThS) |`

**Draft plateau_review.json:**
```json
{
  "slug": "del-norte-ca",
  "date": "2024-03-05",
  "verdict": "CONFIRMED",
  "basis": "late-night internal timestamp (self-description leg, plainer title than other years but still explicitly the night's Unofficial Results); next report 3 days later retitled 'Friday Report' at a much higher count (bracket leg)",
  "evidence": "Release 3/5, printed timestamp 3/5/2024 9:48:44 PM, 19/19 precincts (100%), Voters Cast 3,285/14,743 (22.28%); Release 4 (3/8/2024, 3 days later) retitled 'Unofficial Results - Friday Report', Voters Cast 6,055/14,743 (41.07%) -- confirms Release 3 was the last report before the canvass resumed."
}
```

**Verdict / evidence class:** CONFIRMED (self-description via late-night
timestamp + bracket leg, both directly render-verified). No FLAG.

---

## Summary table (draft, for VERIFY.md)

| Year | Type | Election-night | Certified | % | Confidence | Numerator source |
|---|---|---|---|---|---|---|
| 2012 | presidential-primary | — | 5,242 | NULL | none | — |
| 2014 | statewide-primary | — | 5,950 | NULL | none | — |
| 2016 | presidential-primary | 5,020 | 6,185 | 81.2% | primary | [Drive link](https://drive.google.com/uc?export=download&id=1Y1Kj4-IqXW5uEgZh6c206EsmNoj9pSEN) |
| 2018 | statewide-primary | 4,637 | 5,472 | 84.7% | primary | [Drive link](https://drive.google.com/uc?export=download&id=1xrb3b2KmuaR0EhVysw--eKyjXANMzy6k) |
| 2022 | statewide-primary | 4,019 | 5,989 | 67.1% | primary | [Drive link](https://drive.google.com/uc?export=download&id=1bbTlt98fwmF02gJkIgni_JgMBMQvwS9L) |
| 2024 | presidential-primary | 3,285 | 6,121 | 53.7% | primary | [Drive link](https://drive.google.com/uc?export=download&id=1RaZaZq6m6Wy2vpSYmj3txRh6--X5GThS) |

Pattern check against the existing general-election rows in
`del-norte-ca.json` (2014: 89.18%, 2016: 83.30%, 2018: 84.45%, 2022:
74.70%, 2024: 62.94%): the primaries track the SAME declining-over-time
trend and land close to their same-year generals except 2022 (primary
67.11% noticeably below that year's general 74.70% — worth an operator
eyeball, though nothing found here contradicts it; smaller electorate
primaries can be noisier). 2024 primary (53.67%) is the closest of all six
primary/general pairs (general 62.94%), both this county's lowest shares,
consistent with a single secular mail-ballot-timing trend rather than a
primary-specific effect.

## Outstanding / unfinished

- 2012 and 2014 primaries are null; 2014's is a "real plateau exists but is
  unreadable" null (timing bracket recovered, bytes are not) — flagged
  above for an optional interactive Google-Docs-viewer attempt, not
  required.
- 2018 primary's 4,637-vs-9,284 mislabel resolution is flagged for a human
  eyeball since it is a ~2x swing if misread (same pattern already present,
  and already human-flagged in spirit, for this county's 2016-general row).
- None of this has been written into `data/research/election-night/`,
  `VERIFY.md`, `plateau_review.json`, or run through the pipeline
  (`scripts/research/validate_election_night.py` etc.) — this task was
  explicitly read-only research. All draft JSON rows above are ready to
  paste in verbatim if an operator decides to commit them; running the full
  RUNBOOK section 3 pipeline afterward is still required before commit.
- All downloaded PDFs, PNG renders, and CDX JSON responses backing every
  claim above are preserved in
  `/private/tmp/claude-501/-Users-sbuss-workspace-sf-election-count/cbd9561c-405d-4e44-8f38-6a4a9bd48e60/scratchpad/delnorte/`
  for re-verification.
