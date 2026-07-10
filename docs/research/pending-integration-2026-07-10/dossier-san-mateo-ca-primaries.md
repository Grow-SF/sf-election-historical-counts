# San Mateo County, CA — statewide primaries election-night dossier

Read first: `docs/research/RUNBOOK.md` sections 1, 5, 6, 7, 8; `data/research/election-night/san-mateo-ca.json`;
`data/research/county-tech/san-mateo-ca.json`. This is a READ-ONLY research pass — nothing in the repo was
edited. Everything below is a **draft** for an operator to fold into `data/research/election-night/san-mateo-ca.json`,
`VERIFY.md`, and `plateau_review.json` per the runbook's worked procedure (section 10).

Metric: `election-night % = ballots in the LAST report posted on election night ÷ certified final ballots`.

Tech context (from `data/research/county-tech/san-mateo-ca.json`): e-pollbook **adopted 2018**, `first_election:
"2018-06"` — San Mateo's Board of Supervisors authorized (2017-09-12) the June 5, 2018 primary as the county's
**first VCA election** (vote centers + e-pollbooks together). ASV: never adopted (`status: not-adopted`, human
signature comparison against Vantage Ballot Sorter images). Per the task brief, **2018-06-05 is classified POST**
for `vs_epollbook`: it is not a "pre" baseline year, it IS the rollout election itself, consistent with how the
existing county JSON already classifies 2018-11-06 (Nov general) as `"post"`.

Six primaries: 2012-06-05 (PRE), 2014-06-03 (PRE), 2016-06-07 (PRE), 2018-06-05 (POST/rollout), 2022-06-07 (POST),
2024-03-05 (POST).

---

## ITEM 1 — 2012-06-05 Presidential Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf`
  (filename says "voter-reg-stats" but the PDF's own printed title is "VOTER PARTICIPATION STATISTICS BY COUNTY" —
  confirmed by direct pdftotext read; this is the correct/only 2012-primary participation-stats document linked
  from the SoS's `voter-participation-stats-county` index page).
- San Mateo line (pdftotext -layout): `San Mateo   467   477,460   337,757   33,793   89,537   123,330   72.60%   36.51%   25.83%`
  (columns: Precincts / Eligible / Registered / Precinct Voters / VBM Voters / **Total Voters** / %VBM / %Reg turnout / %Eligible turnout)
- **Certified final = 123,330** (33,793 precinct + 89,537 VBM; arithmetic checks).

### Plateau numerator
- Source: `https://smcacre.gov/media/894/download?attachment` — a live (current, non-Wayback) fetch of a Drupal
  media entity titled "precinct report 5", linked from the current `smcacre.gov/elections/june-5-2012-election-results`
  page under the label "Precinct Report — Preliminary report available after Semi Final results posted at the end
  of the evening on Election Night." (Fetched directly, still resolves live; this is the same document-repository
  pattern already used for the 2012/2014/2016 GENERAL rows already in `san-mateo-ca.json`.)
- Document self-description: title "Precinct Turnout — Total Voters — Unofficial", header
  "COUNTY OF SAN MATEO — 2012-06-05 PRESIDENTIAL PRIMARY ELECTION — June 05, 2012", internal generation timestamp
  **"06/05/2012 11:46 PM"**, "Precincts Reporting 467 of 467 = 100.00%", totals line
  **"Total Number of Voters : 93,604 of 337,702 = 27.72%"**.
- Plateau evidence (RUNBOOK §8 — CONFIRMED): self-describes as end-of-night (past-11pm internal timestamp, 100%
  precincts, "Unofficial") PLUS an independent, non-circular leg — the SAME results page separately links a
  distinct "Results on PDF" document titled **"jun12 final 06 19"** (i.e. the true certified-canvass final, dated
  June 19, 2012, two weeks later). Two separate, differently-dated documents exist in the same document library;
  the precinct report is provably NOT that later final. This satisfies "the report series' next file being days
  later."
- **PLATEAU VERDICT: CONFIRMED.**

### Arithmetic
93,604 / 123,330 = **75.90%**

### Draft row (section 2 schema)
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": 93604,
  "certified_final": 123330,
  "election_night_pct": 75.90,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": "https://smcacre.gov/media/894/download?attachment",
  "confidence": "primary",
  "note": "PLATEAU = Final Election Night Report. Official San Mateo County 'Precinct Turnout — Total Voters — Unofficial' report (Drupal media/894, title 'precinct report 5', linked live from smcacre.gov/elections/june-5-2012-election-results as the 'Preliminary report available after Semi Final results posted at the end of the evening on Election Night') carries embedded report-generation timestamp '06/05/2012 11:46 PM', 'Precincts Reporting 467 of 467 = 100.00%', totals 'Total Number of Voters : 93,604 of 337,702 = 27.72%'. NOT the 8 PM first tranche. The same page separately links a distinct 'Results on PDF' document titled 'jun12 final 06 19' (certified final, June 19 2012, 2 weeks later) -- proves the precinct report is the night-of interim, not the canvass final. Certified final 123,330 (CA SoS Voter Participation Statistics by County: 33,793 precinct + 89,537 VBM; eligible 477,460, registered 337,757). Pct = 93,604/123,330 = 75.90%. Pre-epollbook (adopted 2018); ASV never."
}
```

### VERIFY.md line + detail bullet (draft)
| 2012 | presidential-primary | — | 123,330 | 75.90% | primary | [link](https://smcacre.gov/media/894/download?attachment) |

- **2012 presidential-primary** — night `93,604` / final `123,330` = `75.90%` (primary)
  - numerator: county's own "precinct report" (media/894, "precinct report 5")
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf>
  - look for: "Precinct Turnout — Total Voters — Unofficial", timestamp 06/05/2012 11:46 PM, Precincts Reporting 467 of 467, Total Number of Voters 93,604 of 337,702 = 27.72%.

### plateau_review.json draft entry
```json
{
  "slug": "san-mateo-ca",
  "date": "2012-06-05",
  "verdict": "CONFIRMED",
  "basis": "self-described end-of-night interim report (11:46 PM timestamp, 100% precincts, 'Unofficial') distinct from the county's separately-linked certified-final document dated 2 weeks later",
  "evidence": "media/894 'precinct report 5': 'Total Number of Voters : 93,604 of 337,702 = 27.72%', Precincts Reporting 467 of 467; sibling 'Results on PDF' link titled 'jun12 final 06 19' proves a later, distinct final canvass exists"
}
```

---

## ITEM 2 — 2014-06-03 Statewide Direct Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf`
  (misspelling "particpiation" intact, matches the 2014-general URL convention).
- San Mateo line: `San Mateo   475   488,370   354,994   21,484   75,963   97,447   77.95%   27.45%   19.95%`
- **Certified final = 97,447** (21,484 precinct + 75,963 VBM; arithmetic checks).

### Plateau numerator
- Source: `https://smcacre.gov/media/910/download?attachment` (live fetch), title "precinct report 8", linked
  from the current `smcacre.gov/elections/june-3-2014-election-results` page, same "Preliminary report ... posted
  at the end of the evening on Election Night" label.
- Document self-description: title **"Precinct Turnout — Total Voters — Official"**, header
  "COUNTY OF SAN MATEO — 2014-06-03 STATEWIDE DIRECT PRIMARY ELECTION — June 03, 2014", internal timestamp
  **"06/03/2014 11:24 PM"**, "Precincts Reporting 475 of 475 = 100.00%", totals
  **"Total Number of Voters : 70,651 of 354,994 = 19.90%"**.
- Plateau evidence (§8 — CONFIRMED): past-11pm internal timestamp + 100% precincts, PLUS independent leg: the
  same results page separately links a distinct "Results on PDF" titled **"jun14 final 06 19 2014"** (certified
  final, June 19 2014, 16 days later) — "the report series' next file being days later."
- **PLATEAU VERDICT: CONFIRMED.**

### Arithmetic
70,651 / 97,447 = **72.50%**

### Draft row
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": 70651,
  "certified_final": 97447,
  "election_night_pct": 72.50,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://smcacre.gov/media/910/download?attachment",
  "confidence": "primary",
  "note": "PLATEAU = Final Election Night Report. Official San Mateo County 'Precinct Turnout — Total Voters — Official' report (Drupal media/910, title 'precinct report 8', linked live from smcacre.gov/elections/june-3-2014-election-results) carries embedded timestamp '06/03/2014 11:24 PM', 'Precincts Reporting 475 of 475 = 100.00%', totals 'Total Number of Voters : 70,651 of 354,994 = 19.90%'. NOT the 8 PM first tranche. The same page separately links a distinct 'Results on PDF' titled 'jun14 final 06 19 2014' (certified final, June 19 2014, 16 days later) -- proves the precinct report is the night-of interim. Certified final 97,447 (CA SoS Voter Participation Statistics by County: 21,484 precinct + 75,963 VBM; eligible 488,370, registered 354,994). Pct = 70,651/97,447 = 72.50%. Pre-epollbook (adopted 2018); ASV never."
}
```

### VERIFY.md line + detail bullet
| 2014 | statewide-primary | — | 97,447 | 72.50% | primary | [link](https://smcacre.gov/media/910/download?attachment) |

- **2014 statewide-primary** — night `70,651` / final `97,447` = `72.50%` (primary)
  - numerator: county's own "precinct report" (media/910, "precinct report 8")
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf>
  - look for: "Precinct Turnout — Total Voters — Official", timestamp 06/03/2014 11:24 PM, Precincts Reporting 475 of 475, Total Number of Voters 70,651 of 354,994 = 19.90%.

### plateau_review.json draft entry
```json
{
  "slug": "san-mateo-ca",
  "date": "2014-06-03",
  "verdict": "CONFIRMED",
  "basis": "self-described end-of-night interim report (11:24 PM timestamp, 100% precincts) distinct from the county's separately-linked certified-final document dated 16 days later",
  "evidence": "media/910 'precinct report 8': 'Total Number of Voters : 70,651 of 354,994 = 19.90%', Precincts Reporting 475 of 475; sibling 'Results on PDF' link titled 'jun14 final 06 19 2014' proves a later, distinct final canvass exists"
}
```

---

## ITEM 3 — 2016-06-07 Presidential Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf`
- San Mateo line: `San Mateo   468   501,875   367,155   63,006   127,127   190,133   66.86%   51.79%   37.88%`
- **Certified final = 190,133** (63,006 precinct + 127,127 VBM; arithmetic checks).

### Plateau numerator — NOT SOURCEABLE (null per RUNBOOK §5.1)
Full trail of what was tried, in order:
1. **smcacre.gov current results page** (`/elections/june-7-2016-election-results`, live/current) links a
   "Precinct Report" — but it is Drupal media/1013, titled **"precinct report final"** (not a distinct night
   report like 2012/2014). Fetched live: header "JUNE2016_Precinct Turnout — Total Voters — Official", internal
   timestamp **"07/05/2016 08:58 AM"** (a full month post-election), totals
   "Total Number of Voters : 190,133 of 367,153 = 51.79%" — **this exactly equals the certified final** (190,133).
   Discarded: this is the certified canvass, not the night plateau; the county did not preserve a separate
   election-night interim document for 2016 the way it did for 2012/2014.
2. **Wayback CDX on `smcacre.gov/elections/june-7-2016-election-results`**: only 2024-2025 captures exist (the
   current migrated page); nothing near election day.
3. **shapethefuture.org** (San Mateo's pre-2017 registrar domain — the county-tech notes confirm the legacy
   `shapethefuture.org` domain preceded `smcacre.org`/`smcacre.gov`): CDX on
   `shapethefuture.org/elections/results/2016/june` found the landing page `.../june/web/` captured genuinely
   during the election-night window:
   - `2016-06-08 05:25:18 UTC` = June 7, 10:25 PM PDT (election night) — page links a numbered interim report
     `documents/(05)1000/JUN16_1000.pdf` (report "1000").
   - `2016-06-09 09:56:02 UTC` = June 8, 2:56 AM PDT (still within the runbook's 1-4am "election night" window)
     — the SAME landing page now links `documents/(12)semi/JUN16_Semi.pdf` — a **"Semi[-Final]"**-labeled report
     (report #12), which by the registrar's own naming convention IS the plateau document.
   - A later capture, `2016-06-17 10:10:31 UTC` (10 days on), shows the landing page had moved to
     `documents/(14)semi/JUN16_Semi_06-15.pdf` ("Semi" again, but dated June 15) — confirming report #12 was
     superseded by a later canvass update, i.e. the report-series' "next file being days later" leg WOULD be
     satisfiable IF the #12 document's contents were recoverable.
   - **BUT**: neither `documents/(05)1000/JUN16_1000.pdf` nor `documents/(12)semi/JUN16_Semi.pdf` (nor their
     `media_report_*.txt` siblings) was ever crawled by Wayback — direct CDX queries for each exact URL return
     zero captures, and direct `id_` fetch of both returns the Wayback "not in archive" HTML shell, not PDF bytes.
     The documents were LINKED but never independently crawled (classic Wayback linked-but-uncaptured gap).
4. **shapethefuture.org broader domain sweep** for June 2016: no `/tallyroom/`, `/notices/`, or press-release
   page was captured either (confirmed via CDX prefix search).
5. **Local news**: WebSearch surfaced only a San Mateo Daily Journal URL
   (`smdailyjournal.com/.../san-mateo-county-june-primary-election-results/...`) that is a **live, reused URL
   template** — WebFetch confirms its current content is the **2026** June primary, not an archived 2016 page;
   not usable without a dedicated NewsBank/SFPL archive search (out of scope for this pass).
6. Given the county's own live media library retains only the CERTIFIED FINAL for 2016 (unlike 2012/2014, which
   still host a separate night document), and the only surviving proof of a genuine night report is an
   uncrawled PDF link, this row is **null** per RUNBOOK §5.1.

**FLAG for manual operator**: two candidate URLs exist for a human Wayback Machine UI session (not curl/CDX,
which can miss captures per RUNBOOK §7.1 replay-aliasing) to re-check:
`https://web.archive.org/web/2016*/https://www.shapethefuture.org/elections/results/2016/june/documents/(12)semi/JUN16_Semi.pdf`
and its `media_report_Semi.txt` sibling. A NewsBank/SFPL search of the San Mateo Times/Daily Journal for
June 7-8, 2016 is the other live lead.

### Draft row
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 190133,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Election-night PLATEAU not sourceable. The county's live media library's only surviving 'Precinct Report' (media/1013, 'precinct report final') carries internal timestamp 07/05/2016 08:58 AM -- a MONTH post-election -- and its total (190,133) exactly equals the certified final, i.e. it IS the canvass final, not a night report (unlike 2012/2014, which retain distinct night documents). Wayback CDX on the current smcacre.gov results page has no capture before 2024. shapethefuture.org (the pre-2017 registrar domain) DOES show two genuine election-night-window captures of the results landing page -- June 7 10:25 PM PDT linking report '(05)1000', and June 8 2:56 AM PDT linking a 'Semi[-Final]' report '(12)semi' (JUN16_Semi.pdf), later superseded by a June 15 update -- proving a true night report existed and was superseded, but neither PDF (nor its .txt sibling) was ever independently crawled by Wayback (CDX returns zero captures for the exact document URLs); content unrecoverable by machine. No press release or usable archived news quote found (the one Daily Journal URL found is a live template currently showing the 2026 primary, not an archived 2016 page). FLAG for manual operator: retry documents/(12)semi/JUN16_Semi.pdf via the Wayback Machine UI (not curl -- CDX can miss captures per replay-aliasing), and/or a NewsBank/SFPL search of the San Mateo Times/Daily Journal for June 7-8, 2016. Certified final 190,133 (CA SoS Voter Participation Statistics by County: 63,006 precinct + 127,127 VBM; eligible 501,875, registered 367,155). Pre-epollbook (adopted 2018); ASV never. Value left null per RUNBOOK 5.1."
}
```

### VERIFY.md line + detail bullet
| 2016 | presidential-primary | — | 190,133 | — | none | — (not sourceable) |

- **2016 presidential-primary** — night `—` / final `190,133` = `—` (none)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf>
  - look for: Certified final 190,133 ballots cast. Election-night PLATEAU not sourceable: the county's only
    surviving "Precinct Report" (media/1013) is timestamped a month post-election and equals the certified
    final exactly; two genuine night-window shapethefuture.org captures prove a distinct night "Semi" report
    (report #12) existed but its PDF was never crawled by Wayback. FLAG for manual operator (see note).

**No plateau_review.json entry** (null rows carry no verdict per repo convention — confirmed against existing
`colusa-ca` null rows, which have zero `plateau_review.json` records).

---

## ITEM 4 — 2018-06-05 Statewide Direct Primary (San Mateo's first VCA / e-pollbook election)

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf`
- San Mateo line: `San Mateo   477   506,481   388,456   12,637   159,531   172,168   92.66%   44.32%   33.99%`
- **Certified final = 172,168** (12,637 vote-center + 159,531 VBM; arithmetic checks).

### Plateau numerator — NOT SOURCEABLE (null per RUNBOOK §5.1)
Full trail of what was tried:
1. **smcacre.org** (`/post/june-5-2018-election-results`, which 302-redirects to
   `/election-results-archive/june-5-2018-election-results`): the EARLIEST Wayback capture of either URL is
   **2018-11-14** — over five months post-election.
2. Rendered (puppeteer, `render_wayback.cjs`) the Nov 14, 2018 capture. Contrary to the Nov-2018-GENERAL row
   (which uses a JS iframe widget), the June 2018 primary page turned out to be **plain static HTML** (a Drupal
   node body, no iframe/JS widget found via full-page rendering or raw-HTML `<iframe>`/`data-src` search):
   `<h4>Registration and Turnout</h4> ... Total Registered Voters 388,298 ... Total Ballots Cast 172,168 (44.3%)`
   — Voting Center 12,637 and VBM 159,531 **exactly match the certified SoV columns**. This Nov 14 snapshot
   already reflects the CERTIFIED canvass, not an election-night state (the June 2018 canvass would have
   certified around early July 2018, well before this Nov 14 crawl). Discarded.
3. **Broad CDX sweep of the entire `smcacre.org` domain, June 5-8, 2018** (`matchType=domain`, narrow window):
   only 17 URLs total were crawled in that window, and they are exclusively the `/election-results-archive`
   INDEX page (captured June 6, 2018 10:50 AM PDT) plus its static CSS/JS/image assets. No results-DETAIL page,
   no press release, no news page for this specific election was captured by Wayback in the days surrounding
   the election.
4. **smcacre.gov** (the newer, post-migration domain): no capture of a June 2018 primary results page exists
   before 2025 (same current-migrated-page pattern as the 2016 row).
5. **Local news**: WebSearch turned up a Patch "REAL-TIME RESULTS" page (not independently archived with a
   ballot total) and the same live/reused Daily Journal URL template that currently shows 2026 content (not
   usable as archival evidence of June 2018's figure).
6. Given no distinct election-night artifact survives at any route and the only captured content already
   equals the certified final, this row is **null** per RUNBOOK §5.1.

**FLAG for manual operator**: this is San Mateo's inaugural VCA election and the most editorially important row
in this set (the pre/post e-pollbook pivot); worth a NewsBank/SFPL search of the San Mateo Times/Daily Journal
for June 6, 2018 ("semiofficial results ... as of 9 p.m." pattern was seen live-quoted for other years), and/or
a direct email/records request to smcacre.gov for the original June 5, 2018 semi-final report PDF (the registrar
plausibly still holds it even though it was never migrated to the public site).

### Draft row
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": null,
  "certified_final": 172168,
  "election_night_pct": null,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Election-night PLATEAU not sourceable. This is San Mateo's FIRST VCA/e-pollbook election (Board authorization 2017-09-12; per county-tech.json). smcacre.org's results page for this election (/post/june-5-2018-election-results, redirecting to /election-results-archive/june-5-2018-election-results) has no Wayback capture until 2018-11-14, five+ months post-election; rendered, that Nov 14 capture is PLAIN STATIC HTML (not a JS widget) showing Total Ballots Cast 172,168 (44.3%) with Voting Center 12,637 / VBM 159,531 -- exactly the certified SoV figures -- i.e. it is the certified canvass, not a night snapshot. A domain-wide CDX sweep of smcacre.org for June 5-8 2018 finds only the results-archive INDEX page and its static assets crawled (17 URLs total); no detail page, press release, or news page for this election was captured near the election date. smcacre.gov (newer domain) has no capture before 2025. No usable archived press release or news total found. FLAG for manual operator: this is the pre/post e-pollbook pivot row -- worth a NewsBank/SFPL San Mateo Times/Daily Journal search for June 6, 2018, or a records request to smcacre.gov for the original semi-final PDF. Certified final 172,168 (CA SoS Voter Participation Statistics by County: 12,637 vote-center + 159,531 VBM; eligible 506,481, registered 388,456). Post-epollbook/VCA (adopted 2018, this IS the rollout election); ASV never. Value left null per RUNBOOK 5.1."
}
```

### VERIFY.md line + detail bullet
| 2018 ⚠️ | statewide-primary | — | 172,168 | — | none | — (not sourceable; first VCA election) |

- **2018 statewide-primary** — night `—` / final `172,168` = `—` (none)
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: Certified final 172,168 ballots cast. Election-night PLATEAU not sourceable: earliest capture of
    the results page (Nov 14, 2018) already shows the certified-final figures verbatim; no night-window capture
    of any smcacre.org page for this election survives. FLAG for manual operator — the pre/post e-pollbook pivot
    row (see note).

**No plateau_review.json entry** (null row).

---

## ITEM 5 — 2022-06-07 Statewide Direct Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf`
- San Mateo line: `San Mateo*   277   517,795   433,638   6,750   159,655   166,405   95.94%   38.37%   32.14%`
- **Certified final = 166,405** (6,750 vote-center + 159,655 VBM; arithmetic checks).

### Plateau numerator
- Route: livevoterturnout ENR, index **10** (confirmed via CDX: `livevoterturnout.com/ENR/sanmateocaenr/10/en/Index_10.html`
  is the only sanmateocaenr index active June 7-9, 2022; index 11 is the Nov 2022 general already in the county
  JSON, confirming indices increment chronologically).
- Four captures were rendered (puppeteer, `render_wayback.cjs`) to trace the progression:
  - `2022-06-08 03:11:13 UTC` = June 7, 8:11 PM PDT: Ballots Cast **56,881**, Vote Center Ballots **0** — the 8pm
    first tranche (pre-processed VBM dump only). NOT used.
  - `2022-06-08 15:46:25 UTC` = June 8, 8:46 AM PDT: Ballots Cast **63,362** = VBM 56,881 + Vote Center 6,481.
    Page banner: **"SEMI-OFFICIAL RESULTS - FINAL ELECTION NIGHT REPORT - NEXT UPDATE ON THURSDAY, JUNE 9 AT 4:30
    P.M."**, embedded **"Website Updated: 6/8/2022 1:02:23 AM"** (about 5 hours after poll close).
  - `2022-06-09 15:15:48 UTC` and `2022-06-09 23:07:54 UTC` (both 1-2 days later): identical figures, **63,362**
    unchanged, same "FINAL ELECTION NIGHT REPORT" banner still showing.
- Source URL cited: `https://web.archive.org/web/20220608154625/https://www.livevoterturnout.com/ENR/sanmateocaenr/10/en/Index_10.html`
- Plateau evidence (§8 — CONFIRMED): self-describes "FINAL ELECTION NIGHT REPORT" with a late-night internal
  timestamp (1:02 AM) PLUS independent leg: **held identical across two later captures** 1-2 days on, before the
  scheduled June 9 canvass update ("a later capture of the same URL still showing the same count").
- **PLATEAU VERDICT: CONFIRMED.**

### Arithmetic
63,362 / 166,405 = **38.08%**

### Draft row
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 63362,
  "certified_final": 166405,
  "election_night_pct": 38.08,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20220608154625/https://www.livevoterturnout.com/ENR/sanmateocaenr/10/en/Index_10.html",
  "confidence": "primary",
  "note": "PLATEAU = Final Election Night Report. Rendered archived San Mateo livevoterturnout ENR (index 10) capture 2022-06-08 15:46 UTC (June 8 8:46 AM PDT) shows banner 'SEMI-OFFICIAL RESULTS - FINAL ELECTION NIGHT REPORT - NEXT UPDATE ON THURSDAY, JUNE 9 AT 4:30 P.M.', embedded 'Website Updated: 6/8/2022 1:02:23 AM' (~5 hours after 8pm June 7 poll close), VOTER TURNOUT Ballots Cast 63,362 = Vote by Mail 56,881 + Vote Center 6,481 (Registered Voters 433,539). Figure held IDENTICAL across the two subsequent Nov-9 -- correction, June-9 -- captures (2022-06-09 15:15 UTC and 23:07 UTC), 1-2 days later, before the scheduled canvass update. NOT the 8:11 PM June 7 first tranche (56,881, Vote Center = 0, captured separately at 2022-06-08 03:11 UTC). Certified final 166,405 (CA SoS Voter Participation Statistics by County: 6,750 vote-center + 159,655 VBM; eligible 517,795, registered 433,638). Pct = 63,362/166,405 = 38.08%. Post-VCA/e-pollbook (adopted 2018); ASV never."
}
```

### VERIFY.md line + detail bullet
| 2022 | statewide-primary | 63,362 | 166,405 | 38.08% | primary | [link](https://web.archive.org/web/20220608154625/https://www.livevoterturnout.com/ENR/sanmateocaenr/10/en/Index_10.html) |

- **2022 statewide-primary** — night `63,362` / final `166,405` = `38.08%` (primary)
  - numerator: livevoterturnout ENR index 10, Wayback capture 2022-06-08 15:46 UTC
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "SEMI-OFFICIAL RESULTS - FINAL ELECTION NIGHT REPORT", "Website Updated: 6/8/2022 1:02:23 AM",
    Ballots Cast 63,362.

### plateau_review.json draft entry
```json
{
  "slug": "san-mateo-ca",
  "date": "2022-06-07",
  "verdict": "CONFIRMED",
  "basis": "self-described 'FINAL ELECTION NIGHT REPORT' (1:02 AM internal update) held identical across two later captures 1-2 days on, before the scheduled canvass update",
  "evidence": "livevoterturnout ENR index 10, capture 20220608154625: banner 'SEMI-OFFICIAL RESULTS - FINAL ELECTION NIGHT REPORT - NEXT UPDATE ON THURSDAY, JUNE 9', 'Website Updated: 6/8/2022 1:02:23 AM', Ballots Cast 63,362; captures 20220609151548 and 20220609230754 show the identical 63,362 figure unchanged"
}
```

---

## ITEM 6 — 2024-03-05 Presidential Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf`
- San Mateo line: `San Mateo*   266   510,675   435,483   10,882   163,240   174,122   93.75%   39.98%   34.10%`
- **Certified final = 174,122** (10,882 vote-center + 163,240 VBM; arithmetic checks).

### Plateau numerator
- Route: livevoterturnout ENR, index **14** (confirmed via CDX: `livevoterturnout.com/ENR/sanmateocaenr/14/en/h4CJj_Index_14.html`
  is the only sanmateocaenr index active in the March 4-9, 2024 window; index 16 is the Nov 2024 general already
  in the county JSON, consistent with chronological index growth).
- Three captures rendered:
  - `2024-03-04 19:43:39 UTC` = March 4, 11:43 AM PST — the day BEFORE the election (poll close was March 5,
    8pm PST = March 6, 04:00 UTC); this capture pre-dates poll close and is not a results state. NOT used.
  - `2024-03-07 07:00:14 UTC` = March 6, 11:00 PM PST (the Wednesday after election day): rendered page shows
    banner **"SEMI-OFFICIAL RESULTS - FINAL ELECTION NIGHT REPORT - NEXT UPDATE ON THURSDAY, MARCH 7 BEFORE 4:30
    P.M."**, embedded **"Website Updated: 3/6/2024 4:21:07 PM"** (Wednesday afternoon; the canvass had explicitly
    not yet resumed per the "next update Thursday" banner — this matches RUNBOOK §1's precedent that a labeled
    "Final ... Election Night" report posted mid-day-after still counts, e.g. San Bernardino 2024 at 10 a.m.
    Wednesday). VOTER TURNOUT: **Ballots Counted 92,359** = Vote by Mail 81,991 + Vote Center 10,368 (Registered
    Voters 435,482, 21.2%).
  - `2024-03-09 07:34:00 UTC` = March 8, 11:34 PM PST (2 days later): the page has moved on — banner now reads
    **"SEMI-OFFICIAL RESULTS - MARCH 7, 2024 REPORT - NEXT UPDATE ON MONDAY, MARCH 11"**, "Website Updated:
    3/7/2024 4:20:36 PM", Ballots Counted **104,684** — a distinct, dated, HIGHER canvass update superseding the
    "FINAL ELECTION NIGHT REPORT" state.
- Source URL cited: `https://web.archive.org/web/20240307070014/https://www.livevoterturnout.com/ENR/sanmateocaenr/14/en/h4CJj_Index_14.html`
- Plateau evidence (§8 — CONFIRMED): self-describes "FINAL ELECTION NIGHT REPORT" PLUS independent leg: **the
  report series' next file is a distinctly-dated, higher-count report one day later** ("MARCH 7, 2024 REPORT",
  104,684), proving 92,359 was the frozen night figure superseded by the first canvass update.
- **PLATEAU VERDICT: CONFIRMED.**

### Arithmetic
92,359 / 174,122 = **53.04%**

### Draft row
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 92359,
  "certified_final": 174122,
  "election_night_pct": 53.04,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20240307070014/https://www.livevoterturnout.com/ENR/sanmateocaenr/14/en/h4CJj_Index_14.html",
  "confidence": "primary",
  "note": "PLATEAU = Final Election Night Report. Rendered archived San Mateo livevoterturnout ENR (index 14) capture 2024-03-07 07:00 UTC (March 6 11:00 PM PST) carries banner 'SEMI-OFFICIAL RESULTS - FINAL ELECTION NIGHT REPORT - NEXT UPDATE ON THURSDAY, MARCH 7 BEFORE 4:30 P.M.', embedded 'Website Updated: 3/6/2024 4:21:07 PM' (Wednesday afternoon, canvass explicitly not yet resumed; consistent with RUNBOOK 1's San Bernardino-2024 precedent for a mid-day-after 'Final Election Night' posting): VOTER TURNOUT Ballots Counted 92,359 = Vote by Mail 81,991 + Vote Center 10,368 (Registered Voters 435,482, 21.2%). The next capture (2024-03-09 07:34 UTC) shows the page moved to a distinctly-dated 'MARCH 7, 2024 REPORT' with Ballots Counted 104,684 -- a higher canvass-day update superseding the night figure, confirming 92,359 held through election night. NOT the March 4 pre-election capture (page not yet live). Certified final 174,122 (CA SoS Voter Participation Statistics by County: 10,882 vote-center + 163,240 VBM; eligible 510,675, registered 435,483). Pct = 92,359/174,122 = 53.04%. Post-VCA/e-pollbook (adopted 2018); ASV never. (2020 not applicable to this primary series.)"
}
```

### VERIFY.md line + detail bullet
| 2024 | presidential-primary | 92,359 | 174,122 | 53.04% | primary | [link](https://web.archive.org/web/20240307070014/https://www.livevoterturnout.com/ENR/sanmateocaenr/14/en/h4CJj_Index_14.html) |

- **2024 presidential-primary** — night `92,359` / final `174,122` = `53.04%` (primary)
  - numerator: livevoterturnout ENR index 14, Wayback capture 2024-03-07 07:00 UTC
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "SEMI-OFFICIAL RESULTS - FINAL ELECTION NIGHT REPORT", "Website Updated: 3/6/2024 4:21:07 PM",
    Ballots Counted 92,359.

### plateau_review.json draft entry
```json
{
  "slug": "san-mateo-ca",
  "date": "2024-03-05",
  "verdict": "CONFIRMED",
  "basis": "self-described 'FINAL ELECTION NIGHT REPORT' (Wednesday-afternoon internal update, canvass not yet resumed) superseded one day later by a distinctly-dated, higher-count 'MARCH 7, 2024 REPORT'",
  "evidence": "livevoterturnout ENR index 14, capture 20240307070014: banner 'SEMI-OFFICIAL RESULTS - FINAL ELECTION NIGHT REPORT - NEXT UPDATE ON THURSDAY, MARCH 7', 'Website Updated: 3/6/2024 4:21:07 PM', Ballots Counted 92,359; capture 20240309073400 shows banner 'MARCH 7, 2024 REPORT', 'Website Updated: 3/7/2024 4:20:36 PM', Ballots Counted 104,684 (higher, distinctly dated, supersedes)"
}
```

---

## Summary table (all six primaries)

| Date | Type | Election-night ballots | Certified final | Share | Confidence | vs_epollbook | Plateau verdict |
|---|---|---:|---:|---:|---|---|---|
| 2012-06-05 | presidential-primary | 93,604 | 123,330 | **75.90%** | primary | pre | CONFIRMED |
| 2014-06-03 | statewide-primary | 70,651 | 97,447 | **72.50%** | primary | pre | CONFIRMED |
| 2016-06-07 | presidential-primary | — | 190,133 | — (null) | none | pre | n/a (null row) |
| 2018-06-05 | statewide-primary | — | 172,168 | — (null) | none | **post** (rollout) | n/a (null row), FLAGGED |
| 2022-06-07 | statewide-primary | 63,362 | 166,405 | **38.08%** | primary | post | CONFIRMED |
| 2024-03-05 | presidential-primary | 92,359 | 174,122 | **53.04%** | primary | post | CONFIRMED |

Reading the trend: the two PRE-VCA primaries (2012, 2014) show a very high election-night share (~73-76%,
comparable to San Mateo's own PRE-VCA generals, 63-71%) because election-day precinct ballots dominated and were
counted that night. The two sourced POST-VCA primaries (2022: 38.08%, 2024: 53.04%) are markedly lower — the
same pattern already documented for San Mateo's Nov 2018/2022/2024 generals (the VCA all-mail/vote-center shift
depresses the night share independent of any e-pollbook effect specifically; this is a confound to record, not
"fix," per RUNBOOK §1). 2016 and 2018 are unfortunately the two most editorially interesting rows (the last
pre-VCA presidential primary, and the VCA-rollout primary itself) and both are genuinely unsourceable by machine
research in this pass; both are FLAGGED for a human/NewsBank follow-up.

## Outstanding / unfinished
- 2016-06-07 and 2018-06-05 numerators are null; both have a specific FLAG for manual operator (Wayback UI
  retry for 2016's uncrawled `(12)semi` PDF; NewsBank/SFPL search or a smcacre.gov records request for 2018).
- None of this was written into the actual repo files (`data/research/election-night/san-mateo-ca.json`,
  `VERIFY.md`, `plateau_review.json`) — this dossier is the draft for an operator/agent with write permission to
  fold in per RUNBOOK §10, then run the full pipeline (RUNBOOK §3).
- The `metrics` block in `data/research/county-tech/san-mateo-ca.json` currently has `electionnight_pct` rows
  only for 2022/2024 GENERAL, both null; this dossier's 2022/2024 PRIMARY figures (38.08%, 53.04%) are a
  separate, new data point (primaries were previously entirely absent from both election-night and county-tech
  files) and were not cross-written into that file either.
