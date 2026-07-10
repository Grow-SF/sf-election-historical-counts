# Los Angeles County (los-angeles-ca) -- statewide PRIMARY election-night dossier

READ-ONLY research scout output. No repo files were created, edited, or
committed. Nothing was written to `data/research/election-night/cache/`.
All fetches used `curl` (2s pauses between requests) + `pdftotext -layout`.
Local working files (fetched PDFs + extracted text) live in
`/private/tmp/claude-501/-Users-sbuss-workspace-sf-election-count/cbd9561c-405d-4e44-8f38-6a4a9bd48e60/scratchpad/la/`.

Adoption (from `data/research/county-tech/los-angeles-ca.json`): e-pollbook
2020 (first election 2020-03, VSAP/KnowInk), ASV 2020 (first election 2020-11,
estimated). Both dates fall between the 2018-06-05 and 2022-06-07 primaries,
so 2012/2014/2016/2018 = pre, 2022/2024 = post, exactly as in the existing
`los-angeles-ca.json` general-election rows.

Numerator route used for ALL SIX primaries: **route 6.2, the registrar's
morning-after "semi-final/semi-official results" press release** -- LA's
news-room PDF archive (`lavote.gov/Documents/News_Releases/...` for
2012-2016, `lavote.gov/docs/rrcc/news-releases/...` from 2018 on) covers
every primary back to 2012, exactly as the runbook predicted. No Wayback,
no Clarity, no browser needed for this county. **No null rows this pass.**

---

## Item 1 of 6: 2012-06-05 (June 5, 2012 Presidential Primary)

### Denominator (CA SoS SoV)
- URL: `https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf`
  (HTTP 200; 2012 primary uses the `pdf/03-voter-reg-stats-by-county.pdf`
  naming, matching the task brief's note about 2012's convention)
- Column layout: County | Precincts | Eligible to Register | Registered
  Voters | Precinct Voters | VBM Voters | **Total Voters** | %VBM | Turnout%Reg | Turnout%Elig
- LA line (`pdftotext -layout`): `Los Angeles 4,786 5,959,291 4,459,268 541,463 431,811 973,274 44.37% 21.83% 16.33%`
- **Total Voters = 973,274** (541,463 precinct + 431,811 VBM)

### Numerator (plateau)
- Source: `https://www.lavote.gov/Documents/News_Releases/06062012-045350.pdf`
  ("June 5, 2012 Presidential Primary Election Semifinal Results Reported,"
  released June 6, 2012)
- Quote: "A total of **765,552** ballots were counted on Election Night."
  (274,304 VBM + 491,248 precinct ballots cast at 4,786 precincts)
- Internal timestamp: dated June 6, 2012 (morning after the June 5 election)
- **Plateau evidence (section 8, CONFIRMED):** self-description ("counted on
  Election Night") PLUS the report-series bracket: the same-day companion
  release "Ballots to be Processed for June 5, 2012 Primary Election"
  (`06062012-031844.pdf`) estimates 162,108 ballots remaining right after
  "the semi-final Election Night tally"; the actual next update, a MEDIA
  ADVISORY "First Ballot Counting Update" (`06082012-050049.pdf`, dated
  **June 8, 2012, 3 days later**), states "Of the 176,287 remaining ballots,
  59,243 total ballots were processed today" -- proving 765,552 held frozen
  from election night through June 8. NOT the 8pm first tranche: the same-day
  "Los Angeles County Polls Close" media advisory (`06052012-090443.pdf`)
  reported only 239,769 returned VBM ballots at poll closing.
- Arithmetic: 765,552 / 973,274 = **78.66%**

### Draft row (schema, section 2)
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": 765552,
  "certified_final": 973274,
  "election_night_pct": 78.66,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": "https://www.lavote.gov/Documents/News_Releases/06062012-045350.pdf",
  "confidence": "primary",
  "note": "PRIMARY official plateau. LA County RR/CC 'June 5, 2012 Presidential Primary Election Semifinal Results Reported' news release (Documents/News_Releases/06062012-045350.pdf, released June 6 2012): 'A total of 765,552 ballots were counted on Election Night' (274,304 VBM + 491,248 precinct ballots at 4,786 precincts). Distinct from the 8pm first tranche: the same-day 'Polls Close' media advisory (06052012-090443.pdf) reported only 239,769 returned VBM ballots at poll closing. A same-morning companion release ('Ballots to be Processed', 06062012-031844.pdf) estimated 162,108 ballots remaining after the semi-final tally, and the first post-night update (06082012-050049.pdf MEDIA ADVISORY, June 8, 3 days later) processed 59,243 more of a then-176,287 remaining, confirming the 765,552 figure held frozen from election night through June 8. Certified final 'Total Voters' 973,274, CA SoS SoV 2012 primary voter-participation-by-county PDF. 765,552/973,274 = 78.66%. Pre-e-pollbook, pre-ASV (both adopted 2020)."
}
```

### VERIFY.md line (draft, to add to Los Angeles County table)
```
| 2012 | presidential-primary | 765,552 | 973,274 | 78.7% | primary | [link](https://www.lavote.gov/Documents/News_Releases/06062012-045350.pdf) |
```
Detail bullet:
```
- **2012 presidential-primary** -- night `765,552` / final `973,274` = `78.7%` (primary)
  - numerator: <https://www.lavote.gov/Documents/News_Releases/06062012-045350.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf>
  - look for: "A total of 765,552 ballots were counted on Election Night."
```

### plateau_review.json verdict (draft)
```json
{
  "slug": "los-angeles-ca",
  "date": "2012-06-05",
  "verdict": "CONFIRMED",
  "basis": "RR/CC semi-final press release self-describes as Election Night total; report-series bracket (next update 3 days later) confirms it held",
  "evidence": "'A total of 765,552 ballots were counted on Election Night'; June 8 first update processed 59,243 of a then-176,287 remaining, i.e. still building on the frozen 765,552 base"
}
```

**VERDICT: CONFIRMED.**

---

## Item 2 of 6: 2014-06-03 (June 3, 2014 Statewide Direct Primary)

### Denominator (CA SoS SoV)
- URL: `https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf`
  (HTTP 200; misspelling "particpiation" intact, matching the 2014 general's
  known convention)
- LA line: `Los Angeles 4,870 6,076,302 4,857,424 423,376 400,694 824,070 48.62% 16.97% 13.56%`
- **Total Voters = 824,070** (423,376 precinct + 400,694 VBM)

### Numerator (plateau)
- Source: `https://www.lavote.gov/Documents/News_Releases/06042014-044011.pdf`
  ("Ballots Left to be Counted for the June 3, 2014 Statewide Direct Primary
  Election," dated June 4, 2014)
- Quote: "On Election Night, a total of **636,186** ballots were counted."
  (The same-morning "Semi-Final Official Results Reported" release,
  `06042014-031226.pdf`, restates the identical figure: "A total of 636,186
  ballots were processed and counted, with 13.19% of eligible registered
  voters casting ballots.")
- Internal timestamp: June 4, 2014 (morning after the June 3 election)
- **Plateau evidence (CONFIRMED):** explicit self-description ("counted on
  Election Night") PLUS bracket: the actual next report, "First Ballot
  Counting Update" (`06062014-025032.pdf`, dated **June 6, 2014, 2 days
  later**), states "The update includes 19,246 ballots processed since
  Election Night" (636,186+19,246=655,432 -- consistent), and adds "the
  second ballot counting update is on Tuesday, June 10." NOT the 8pm first
  tranche: the same-day "Polls Close and First Election Night Ballot Count"
  release (`06032014-082850.pdf`) reported only 256,813 returned VBM
  ballots at poll closing.
- Arithmetic: 636,186 / 824,070 = **77.20%**

### Draft row (schema, section 2)
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": 636186,
  "certified_final": 824070,
  "election_night_pct": 77.2,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://www.lavote.gov/Documents/News_Releases/06042014-044011.pdf",
  "confidence": "primary",
  "note": "PRIMARY official plateau. LA County RR/CC 'Ballots Left to be Counted for the June 3, 2014 Statewide Direct Primary Election' release (Documents/News_Releases/06042014-044011.pdf, June 4 2014): 'On Election Night, a total of 636,186 ballots were counted.' The same-morning 'Semi-Final Official Results' release (06042014-031226.pdf) restates the identical figure: 'A total of 636,186 ballots were processed and counted, with 13.19% of eligible registered voters casting ballots.' Distinct from the 8pm first tranche: the same-day 'Polls Close and First Election Night Ballot Count' release (06032014-082850.pdf) reported only 256,813 returned VBM ballots at poll closing. The first post-night update (06062014-025032.pdf, June 6, 2 days later) added 19,246 ballots 'processed since Election Night' -> 655,432, confirming 636,186 was frozen from election night to June 6. Certified final 'Total Voters' 824,070, CA SoS SoV 2014 primary voter-participation-by-county PDF (misspelled 'particpiation' path, same convention as the 2014 general). 636,186/824,070 = 77.20%. Pre-e-pollbook, pre-ASV."
}
```

### VERIFY.md line (draft)
```
| 2014 | statewide-primary | 636,186 | 824,070 | 77.2% | primary | [link](https://www.lavote.gov/Documents/News_Releases/06042014-044011.pdf) |
```
Detail bullet:
```
- **2014 statewide-primary** -- night `636,186` / final `824,070` = `77.2%` (primary)
  - numerator: <https://www.lavote.gov/Documents/News_Releases/06042014-044011.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf>
  - look for: "On Election Night, a total of 636,186 ballots were counted."
```

### plateau_review.json verdict (draft)
```json
{
  "slug": "los-angeles-ca",
  "date": "2014-06-03",
  "verdict": "CONFIRMED",
  "basis": "RR/CC release explicitly labels the figure as the Election Night total; next report (2 days later) confirms",
  "evidence": "'On Election Night, a total of 636,186 ballots were counted'; June 6 first update added 19,246 'processed since Election Night' -> 655,432"
}
```

**VERDICT: CONFIRMED.**

---

## Item 3 of 6: 2016-06-07 (June 7, 2016 Presidential Primary)

### Denominator (CA SoS SoV)
- URL: `https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf`
  (HTTP 200; note 2016-primary drops the `sov/` and `pdf/` sub-segments
  present in other years -- confirmed by direct fetch after two 403s on the
  general-pattern URL variants)
- LA line: `Los Angeles 4,698 6,199,606 4,909,904 1,303,989 722,079 2,026,068 35.64% 41.26% 32.68%`
- **Total Voters = 2,026,068** (1,303,989 precinct + 722,079 VBM)

### Numerator (plateau)
- Source: `https://www.lavote.gov/Documents/News_Releases/06072016_semi-official-results.pdf`
  ("Semi-Final Official Results Reported for the June 7, 2016 Presidential
  Primary Election," dated June 8, 2016)
- Quote: "A total of **1,438,909** ballots were processed and counted, with
  29.92% of eligible registered voters casting ballots."
- Internal timestamp: June 8, 2016
- **Plateau evidence (CONFIRMED) -- the strongest bracket of the six:** NOT
  the 8pm first tranche -- the same-day "L.A. County Polls Close and First
  Election Night Ballot Count" release (`06072016_polls-close-first-vbm-count.pdf`)
  reported only 387,237 returned VBM ballots (of 1,891,963 issued) at poll
  closing. The actual next report, "First Election Results Update"
  (`06072016_first-canvass-update.pdf`, dated **June 10, 2016, 3 days
  later**), states verbatim: "The update includes 66,869 ballots processed
  since Election Night. The total election results count is now at
  1,505,778" -- and 1,438,909 + 66,869 = 1,505,778 **exactly**, an
  arithmetic-exact bracket proof that 1,438,909 was the frozen election-night
  total.
- Arithmetic: 1,438,909 / 2,026,068 = **71.02%**

### Draft row (schema, section 2)
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 1438909,
  "certified_final": 2026068,
  "election_night_pct": 71.02,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://www.lavote.gov/Documents/News_Releases/06072016_semi-official-results.pdf",
  "confidence": "primary",
  "note": "PRIMARY official plateau. LA County RR/CC 'Semi-Final Official Results Reported for the June 7, 2016 Presidential Primary Election' release (Documents/News_Releases/06072016_semi-official-results.pdf, released June 8 2016): 'A total of 1,438,909 ballots were processed and counted, with 29.92% of eligible registered voters casting ballots.' Distinct from the 8pm first tranche: the same-day 'L.A. County Polls Close and First Election Night Ballot Count' release (06072016_polls-close-first-vbm-count.pdf) reported only 387,237 returned VBM ballots (of 1,891,963 issued) at poll closing. The next report, 'First Election Results Update' (06072016_first-canvass-update.pdf, dated June 10, 3 days later) states: 'The update includes 66,869 ballots processed since Election Night. The total election results count is now at 1,505,778' (1,438,909+66,869=1,505,778 exactly), confirming 1,438,909 held frozen from election night through June 10. Certified final 'Total Voters' 2,026,068, CA SoS SoV 2016 primary voter-participation-by-county PDF. 1,438,909/2,026,068 = 71.02%. Pre-e-pollbook, pre-ASV."
}
```

### VERIFY.md line (draft)
```
| 2016 | presidential-primary | 1,438,909 | 2,026,068 | 71.0% | primary | [link](https://www.lavote.gov/Documents/News_Releases/06072016_semi-official-results.pdf) |
```
Detail bullet:
```
- **2016 presidential-primary** -- night `1,438,909` / final `2,026,068` = `71.0%` (primary)
  - numerator: <https://www.lavote.gov/Documents/News_Releases/06072016_semi-official-results.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf>
  - look for: "A total of 1,438,909 ballots were processed and counted, with 29.92% of eligible registered voters casting ballots."
```

### plateau_review.json verdict (draft)
```json
{
  "slug": "los-angeles-ca",
  "date": "2016-06-07",
  "verdict": "CONFIRMED",
  "basis": "RR/CC semi-final press release plus exact-arithmetic report-series bracket 3 days later",
  "evidence": "'A total of 1,438,909 ballots were processed and counted'; June 10 update: '66,869 ballots processed since Election Night...total...now at 1,505,778' (1,438,909+66,869=1,505,778 exactly)"
}
```

**VERDICT: CONFIRMED (gold-standard bracket).**

---

## Item 4 of 6: 2018-06-05 (June 5, 2018 Statewide Direct Primary)

### Denominator (CA SoS SoV)
- URL: `https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf`
  (HTTP 200)
- LA line: `Los Angeles 4,357 6,216,686 5,149,461 825,427 665,075 1,490,502 44.62% 28.94% 23.98%`
- **Total Voters = 1,490,502** (825,427 precinct + 665,075 VBM)

### Numerator (plateau)
- Source: `https://www.lavote.gov/docs/rrcc/news-releases/06052018_semi-official-results.pdf`
  ("Semi-Official Results Announced for the Statewide Direct Primary
  Election," dated June 6, 2018)
- Quote: "A total of **952,633** ballots were processed and counted, with
  18.53% of eligible registered voters casting ballots."
- Internal timestamp: June 6, 2018
- **Plateau evidence (CONFIRMED):** same title/timing convention as the
  already-accepted 2018 general row (distinct from the county's separate
  election-day "polls open/polls closed" release series). Bracket: the
  actual next report, "First Election Results Update"
  (`06052018_first-canvass-update.pdf`, dated **June 8, 2018, 3 days
  later**), states: "The update includes 83,267 ballots processed since
  Election Night. The total election results count is now 1,035,900" --
  952,633 + 83,267 = 1,035,900 **exactly**.
- Arithmetic: 952,633 / 1,490,502 = **63.91%**

### Draft row (schema, section 2)
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 952633,
  "certified_final": 1490502,
  "election_night_pct": 63.91,
  "vs_epollbook": "pre",
  "vs_asv": "pre",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://www.lavote.gov/docs/rrcc/news-releases/06052018_semi-official-results.pdf",
  "confidence": "primary",
  "note": "PRIMARY official plateau. LA County RR/CC 'Semi-Official Results Announced for the Statewide Direct Primary Election' release (docs/rrcc/news-releases/06052018_semi-official-results.pdf, released June 6 2018): 'A total of 952,633 ballots were processed and counted, with 18.53% of eligible registered voters casting ballots.' Same naming/timing convention as the accepted 2018 general row (title distinct from the county's separate election-day 'polls open/polls closed' release series). The next report, 'First Election Results Update' (06052018_first-canvass-update.pdf, dated June 8, 3 days later) states: 'The update includes 83,267 ballots processed since Election Night. The total election results count is now 1,035,900' (952,633+83,267=1,035,900 exactly), confirming 952,633 held frozen from election night through June 8. Certified final 'Total Voters' 1,490,502, CA SoS SoV 2018 primary voter-participation-by-county PDF. 952,633/1,490,502 = 63.91%. Pre-e-pollbook, pre-ASV (last pre-2020 primary)."
}
```

### VERIFY.md line (draft)
```
| 2018 | statewide-primary | 952,633 | 1,490,502 | 63.9% | primary | [link](https://www.lavote.gov/docs/rrcc/news-releases/06052018_semi-official-results.pdf) |
```
Detail bullet:
```
- **2018 statewide-primary** -- night `952,633` / final `1,490,502` = `63.9%` (primary)
  - numerator: <https://www.lavote.gov/docs/rrcc/news-releases/06052018_semi-official-results.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "A total of 952,633 ballots were processed and counted, with 18.53% of eligible registered voters casting ballots."
```

### plateau_review.json verdict (draft)
```json
{
  "slug": "los-angeles-ca",
  "date": "2018-06-05",
  "verdict": "CONFIRMED",
  "basis": "RR/CC semi-official press release plus exact-arithmetic report-series bracket 3 days later",
  "evidence": "'A total of 952,633 ballots were processed and counted'; June 8 update: '83,267 ballots processed since Election Night...total...now 1,035,900' (952,633+83,267=1,035,900 exactly)"
}
```

**VERDICT: CONFIRMED.**

---

## Item 5 of 6: 2022-06-07 (June 7, 2022 Primary)

### Denominator (CA SoS SoV)
- URL: `https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf`
  (HTTP 200)
- LA line (LA carries a `*` VCA footnote marker, same as its 2022/2024
  general rows): `Los Angeles* 3,293 6,677,886 5,615,370 248,821 1,371,772 1,620,593 84.65% 28.86% 24.27%`
- **Total Voters = 1,620,593** (248,821 precinct/vote-center + 1,371,772 VBM)

### Numerator (plateau)
- Source: `https://www.lavote.gov/docs/rrcc/news-releases/06072022_semi-final-results.pdf`
  ("Semi-Final Results Announced for the June Primary Election," dated
  June 8, 2022)
- Quote: "A total of **822,545** ballots were processed and counted, with
  14.45% of registered voters casting ballots."
- Internal timestamp: June 8, 2022
- **Plateau evidence (CONFIRMED):** bracket -- the actual next report,
  "First Post-Election Ballot Count Update"
  (`06072022_first-post-election-update.pdf`, dated **June 10, 2022, 3 days
  later**), states: "The update includes 169,338 ballots processed since
  Election Night. The total election results count is now 991,883" --
  822,545 + 169,338 = 991,883 **exactly**.
- Arithmetic: 822,545 / 1,620,593 = **50.76%**

### Draft row (schema, section 2)
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 822545,
  "certified_final": 1620593,
  "election_night_pct": 50.76,
  "vs_epollbook": "post",
  "vs_asv": "post",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://www.lavote.gov/docs/rrcc/news-releases/06072022_semi-final-results.pdf",
  "confidence": "primary",
  "note": "PRIMARY official plateau. LA County RR/CC 'Semi-Final Results Announced for the June Primary Election' release (docs/rrcc/news-releases/06072022_semi-final-results.pdf, released June 8 2022): 'A total of 822,545 ballots were processed and counted, with 14.45% of registered voters casting ballots.' The next report, 'First Post-Election Ballot Count Update' (06072022_first-post-election-update.pdf, dated June 10, 3 days later) states: 'The update includes 169,338 ballots processed since Election Night. The total election results count is now 991,883' (822,545+169,338=991,883 exactly), confirming 822,545 held frozen from election night through June 10. Certified final 'Total Voters' 1,620,593, CA SoS SoV 2022 primary voter-participation-by-county PDF. 822,545/1,620,593 = 50.76%. Post-e-pollbook, post-ASV (both 2020); first primary under the all-mail VCA model (confound, same as the 2022 general)."
}
```

### VERIFY.md line (draft)
```
| 2022 | statewide-primary | 822,545 | 1,620,593 | 50.8% | primary | [link](https://www.lavote.gov/docs/rrcc/news-releases/06072022_semi-final-results.pdf) |
```
Detail bullet:
```
- **2022 statewide-primary** -- night `822,545` / final `1,620,593` = `50.8%` (primary)
  - numerator: <https://www.lavote.gov/docs/rrcc/news-releases/06072022_semi-final-results.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "A total of 822,545 ballots were processed and counted, with 14.45% of registered voters casting ballots."
```

### plateau_review.json verdict (draft)
```json
{
  "slug": "los-angeles-ca",
  "date": "2022-06-07",
  "verdict": "CONFIRMED",
  "basis": "RR/CC semi-final press release plus exact-arithmetic report-series bracket 3 days later",
  "evidence": "'A total of 822,545 ballots were processed and counted'; June 10 update: '169,338 ballots processed since Election Night...total...now 991,883' (822,545+169,338=991,883 exactly)"
}
```

**VERDICT: CONFIRMED.**

---

## Item 6 of 6: 2024-03-05 (March 5, 2024 Presidential Primary)

### Denominator (CA SoS SoV)
- URL: `https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf`
  (HTTP 200)
- LA line: `Los Angeles* 2,391 6,556,074 5,654,222 321,826 1,319,889 1,641,715 80.40% 29.04% 25.04%`
- **Total Voters = 1,641,715** (321,826 precinct/vote-center + 1,319,889 VBM)

### Numerator (plateau)
- Source: `https://www.lavote.gov/docs/rrcc/news-releases/03062024_PR-13-03052024-Semi-Final-Results.pdf`
  ("Semi-Final Results Announced for the 2024 Presidential Primary
  Election," dated March 6, 2024). NOTE: LA's own news-room page currently
  links this file under a `stage.lavote.gov` staging host, which is
  unreachable; the identical filename resolves cleanly (HTTP 200) on the
  public `www.lavote.gov` host used here -- record this quirk in the note
  so a future re-check does not follow the dead staging link.
- Quote: "A total of **910,857** ballots were processed and counted, with
  16.03% of registered voters casting ballots."
- Internal timestamp: March 6, 2024
- **Plateau evidence (CONFIRMED):** bracket -- the actual next report,
  "First Post-Election Night Ballot Count Update"
  (`03062024_PR-11-03052024_First-Post-Election-Update.pdf`, also dated
  **March 6, 2024, 1 day after** the March 5 election -- a shorter gap than
  the other five years but still after and distinct from the semi-final
  release), states: "The update includes 105,717 ballots processed since
  Election Night. The total election results count is now 1,016,574" --
  910,857 + 105,717 = 1,016,574 **exactly**.
- Arithmetic: 910,857 / 1,641,715 = **55.48%**

### Draft row (schema, section 2)
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 910857,
  "certified_final": 1641715,
  "election_night_pct": 55.48,
  "vs_epollbook": "post",
  "vs_asv": "post",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://www.lavote.gov/docs/rrcc/news-releases/03062024_PR-13-03052024-Semi-Final-Results.pdf",
  "confidence": "primary",
  "note": "PRIMARY official plateau. LA County RR/CC 'Semi-Final Results Announced for the 2024 Presidential Primary Election' release (docs/rrcc/news-releases/03062024_PR-13-03052024-Semi-Final-Results.pdf, released March 6 2024): 'A total of 910,857 ballots were processed and counted, with 16.03% of registered voters casting ballots.' The next report, 'First Post-Election Night Ballot Count Update' (docs/rrcc/news-releases/03062024_PR-11-03052024_First-Post-Election-Update.pdf, also dated March 6, 1 day after the March 5 election) states: 'The update includes 105,717 ballots processed since Election Night. The total election results count is now 1,016,574' (910,857+105,717=1,016,574 exactly), confirming 910,857 was the frozen election-night figure the canvass then built on. NOTE: this county page links a 'stage.lavote.gov' staging URL for these two releases; the identical filenames resolve on the public www.lavote.gov host (used here, HTTP 200) -- flag for anyone re-checking not to follow the dead staging link. Certified final 'Total Voters' 1,641,715, CA SoS SoV 2024 primary voter-participation-by-county PDF. 910,857/1,641,715 = 55.48%. Post-e-pollbook, post-ASV (both 2020); all-mail VCA confound (same as the 2024 general)."
}
```

### VERIFY.md line (draft)
```
| 2024 | presidential-primary | 910,857 | 1,641,715 | 55.5% | primary | [link](https://www.lavote.gov/docs/rrcc/news-releases/03062024_PR-13-03052024-Semi-Final-Results.pdf) |
```
Detail bullet:
```
- **2024 presidential-primary** -- night `910,857` / final `1,641,715` = `55.5%` (primary)
  - numerator: <https://www.lavote.gov/docs/rrcc/news-releases/03062024_PR-13-03052024-Semi-Final-Results.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: "A total of 910,857 ballots were processed and counted, with 16.03% of registered voters casting ballots." (FLAG: news-room page's own link uses a dead stage.lavote.gov host; use www.lavote.gov instead.)
```

### plateau_review.json verdict (draft)
```json
{
  "slug": "los-angeles-ca",
  "date": "2024-03-05",
  "verdict": "CONFIRMED",
  "basis": "RR/CC semi-final press release plus exact-arithmetic report-series bracket 1 day later",
  "evidence": "'A total of 910,857 ballots were processed and counted'; March 6 First Post-Election Night update: '105,717 ballots processed since Election Night...total...now 1,016,574' (910,857+105,717=1,016,574 exactly)"
}
```

**VERDICT: CONFIRMED.**

---

## Summary table (all 6, ready to merge)

| Year | Type | Night ballots | Certified final | Share | e-pollbook | ASV | Conf. |
|---|---|---:|---:|---:|---|---|---|
| 2012-06-05 | presidential-primary | 765,552 | 973,274 | 78.66% | pre | pre | primary |
| 2014-06-03 | statewide-primary | 636,186 | 824,070 | 77.20% | pre | pre | primary |
| 2016-06-07 | presidential-primary | 1,438,909 | 2,026,068 | 71.02% | pre | pre | primary |
| 2018-06-05 | statewide-primary | 952,633 | 1,490,502 | 63.91% | pre | pre | primary |
| 2022-06-07 | statewide-primary | 822,545 | 1,620,593 | 50.76% | post | post | primary |
| 2024-03-05 | presidential-primary | 910,857 | 1,641,715 | 55.48% | post | post | primary |

Pattern: the election-night share falls steadily 2012->2022 (78.66% ->
50.76%) largely tracking the VCA/all-mail shift (VBM share of the
certified final rises from 44% in 2012 to ~85% by 2022), then partially
recovers in 2024 (55.48%) despite being fully post-e-pollbook/post-ASV --
consistent with the runbook's caution that the 2018-2020 VCA shift is a
confound that suppresses the metric independent of tech, and that the
metric should not be read as "tech made counting slower." No pre/post
tech-adoption causal read is asserted here; that synthesis is left to the
estimator script, not this scouting pass.

**Null rows: none.** All six primaries resolved via route 6.2 (registrar
morning-after press release) on the first attempt; routes 6.3-6.6 were not
needed.

**Nothing flagged for manual/browser operator work.** All sources were
`curl`-reachable; the only wrinkle was LA's own news-room page linking a
dead `stage.lavote.gov` URL for the 2024 releases, resolved by using the
public `www.lavote.gov` host instead (noted in the 2024 row's note text
above for anyone re-checking).

**Not done (explicitly out of scope for this READ-ONLY scouting pass):**
no repo file was edited. To land this, an operator must: (1) surgically
insert the six draft rows into `data/research/election-night/los-angeles-ca.json`'s
`elections` array (or a new primaries array/section, per current schema
conventions -- check whether primaries share the county JSON's top-level
`elections` list with generals or need their own field); (2) add the
summary-table rows + detail bullets to `VERIFY.md`'s Los Angeles County
section; (3) append the six verdict objects to `plateau_review.json`;
(4) run the full pipeline (RUNBOOK.md section 3): validator ->
`build_county_night.py` -> `verify_en_denominators.py` ->
`verify_en_numerators.py` -> `build_en_verification_report.py` -> pytest ->
vitest.
