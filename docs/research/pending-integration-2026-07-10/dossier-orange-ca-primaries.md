# Orange County, CA — statewide PRIMARY election-night dossier

Read-only research scout output. Companion to the already-committed
`data/research/election-night/orange-ca.json` (generals only, v3 plateau
correction). This dossier extends the SAME county with its six statewide
PRIMARIES: 2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05 (all pre-epollbook),
2022-06-07, 2024-03-05 (post-epollbook). 2020 excluded (VCA launch election,
per task scope). Adoption: e-pollbook 2020 (March primary), ASV never adopted
(per orange-ca.json header).

**Methodology note (discovered this pass):** ocvote.gov's live CMS still
serves the FULL historical "Run NN cumulative.pdf" series for every primary
back to 2012 — same as it does for the generals already in orange-ca.json —
so no Wayback/CDX detour was needed for any of the 6 numerators; the live
server 200'd every fetch. Folder/file-naming per year (discovered by probing,
not documented anywhere):
- `pri2012/run01`..`run17/cumulative.pdf` (lowercase "run", no space, no
  zero-pad separator; NOTE this differs from gen2012's "RunNN" capitalization)
- `pri2014/run01`..`run17/cumulative.pdf` (lowercase, same as pri2012)
- `pri2016/Run 01`..`Run 23/cumulative.pdf` (capital R + space, URL `Run%20NN`)
- `pri2018/Run 01`..`Run 27/cumulative.pdf` (capital R + space, URL `Run%20NN`)
- `PRI2022/Run_01`..`Run_20/cumulative.pdf` (all-caps folder, underscore)
- `PRI2024/Run_01`..`Run_21/cumulative.pdf` (all-caps folder, underscore)

All fetches required a browser User-Agent header (`curl -A "Mozilla/5.0
...Chrome/120.0 Safari/537.36"`); a bare `curl` (no UA) 403'd on several SoS
CDN PDFs and was not tested against ocvote.gov (used UA throughout for
safety). 2s+ pauses were kept between fetches. No source blocked curl; no
`FLAG for manual operator` needed anywhere in this pass.

Same plateau method as the committed generals: for 2012/2014/2016/2018 the
plateau is identified by ALL precincts reporting (100%) in a late-night run,
immediately followed by a ~15-16 hour gap to the next run (next-day
afternoon, when the multi-day canvass resumes). For 2022/2024 (VCA
vote-center era) precincts read 100% from Run 01 on, so the plateau is
identified purely by the TIME GAP (the last run before a >16-hour jump to a
next-day-afternoon run), exactly as documented for Orange's 2022/2024
generals in orange-ca.json.

---

## Item 1 of 6 — 2012-06-05 Presidential Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf`
  (fetched 2026-07-10 with a Chrome UA; plain curl 403'd, UA curl 200'd.
  NOTE: filename says "voter-reg-stats" but the PDF's own printed header
  reads "VOTER PARTICIPATION STATISTICS BY COUNTY" — a naming quirk on the
  SoS CDN for this one year; content is unambiguously the turnout table used
  for every other year in orange-ca.json.)
- Orange line (pdftotext -layout): `Orange  1,976  1,916,528  1,612,145
  145,474  281,395  426,869  65.92%  26.48%  22.27%` = Precincts 1,976,
  Eligible-to-Register 1,916,528, Registered 1,612,145, Precinct Voters
  145,474, Vote-by-Mail Voters 281,395, **Total Voters 426,869**, %VBM
  65.92%, Turnout/Registered 26.48%, Turnout/Eligible 22.27%.
- **certified_final = 426,869**

### Plateau (numerator)
- Source URL: `https://ocvote.gov/fileadmin/live/pri2012/run09/cumulative.pdf`
  (live ocvote.gov, fetched 2026-07-10, 200 OK with Chrome UA)
- Internal timestamp: `Run Date/Time: 06/05/2012 07:42:12 pm` is run01's
  stamp (that field is static per-PDF template text on early runs; the
  operative distinguishing stamp per run, extracted from each PDF's own
  header, is below). Run09's own internal `Run Date/Time` = **06/06/2012
  01:05:49 am**, "Complete Precincts: 1,976 of 1,976" (100%).
- Full sequence (Run Date/Time | Total Ballots Cast | precincts): run01
  06/05 07:42:12pm = pre-count VBM-only dump (0/1,976 precincts); count
  climbs through run08 (06/06 12:19:43am, 311,618, 1,917/1,976); run09
  (06/06 **01:05:49am**, **315,584** = Precinct 128,320 + VBM 187,264,
  **1,976/1,976 = 100%**) — this is the last night run; then a **~15.7-hour
  gap** to run10 (06/06 04:45:57pm, 331,362) where the multi-day canvass
  resumes, continuing daily (run11 06/07, run12 06/08, ... ) through run17
  (06/15/2012 11:01:30am, 145,474 precinct + 281,395 VBM = 426,869, exactly
  the SoS-certified figure).
- **Plateau evidence (RUNBOOK section 8): CONFIRMED.** Self-describes as
  end-of-night (past-midnight internal stamp 01:05:49 am) PLUS a
  non-circular leg = the county's own posting schedule bracketing the
  report (run09 at 100% precincts, then a ~15.7-hour gap to the next-day
  4:45pm run10, matching the exact pattern already CONFIRMED for Orange's
  2012 general in the committed dataset).
- **election_night_ballots = 315,584**

### Arithmetic
315,584 / 426,869 = **73.93%** (2dp percent; `round(315584/426869*100, 2)`)

### Draft row (section 2 schema)
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": 315584,
  "certified_final": 426869,
  "election_night_pct": 73.93,
  "vs_epollbook": "pre",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": "https://ocvote.gov/fileadmin/live/pri2012/run09/cumulative.pdf",
  "confidence": "primary",
  "note": "PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). OCROV posted sequential 'UNOFFICIAL RESULTS CUMULATIVE TOTALS' runs (Presidential Primary Election, Tuesday June 5, 2012): run01 (Run Date/Time 06/05/2012 07:42:12 pm) = 0 of 1,976 precincts, VBM-only pre-count dump; the count climbed and PLATEAUED at run09 (Run Date/Time 06/06/2012 01:05:49 am) = Total Ballots Cast 315,584 (Precinct Ballots Cast 128,320 + Vote-by-Mail Ballots Cast 187,264) with ALL 1,976 of 1,976 precincts complete. run09 was the LAST election-night run before a ~15.7-hour gap to run10 (06/06/2012 04:45:57 pm = 331,362), where the multi-day canvass resumed (daily runs through run17, 06/15/2012 11:01:30 am, reaching 426,869 = certified). 315,584 / 426,869 certified = 73.93%. Denominator confirmed: run17's own Precinct 145,474 + VBM 281,395 = 426,869 exactly = CA SoS Statement of Vote, Voter Participation Statistics by County (Orange Total Voters 426,869; SoS PDF filename is mislabeled '03-voter-reg-stats-by-county.pdf' but its printed header reads 'VOTER PARTICIPATION STATISTICS BY COUNTY'). Pre-epollbook (OC adopted iPad e-pollbooks + Voter's Choice Act vote centers at the March 2020 primary). ASV never adopted. Snapshot used: ocvote.gov live pri2012/run09/cumulative.pdf (lowercase 'run', distinct from gen2012's 'RunNN' capitalization), internal Run Date/Time 06/06/2012 01:05:49 am."
}
```

### VERIFY.md line
Summary-table row (to append under a new "### Orange County — Primaries"
section, or merged into the existing Orange County table with a Type
column disambiguating primary vs general):
```
| 2012 | presidential-primary | 315,584 | 426,869 | 73.9% | primary | [link](https://ocvote.gov/fileadmin/live/pri2012/run09/cumulative.pdf) |
```
Detail bullet:
```
- **2012 presidential-primary** — night `315,584` / final `426,869` = `73.9%` (primary)
  - numerator: <https://ocvote.gov/fileadmin/live/pri2012/run09/cumulative.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf>
  - look for: run09's own header "Run Date/Time: 06/06/2012 01:05:49 am", "Complete Precincts: 1,976 of 1,976", "Total Ballots Cast 315,584" (Precinct Ballots Cast 128,320 + Vote-by-Mail Ballots Cast 187,264). Confirm run10 (same folder) is dated 06/06/2012 04:45:57 pm = 331,362, the next-day-afternoon canvass jump.
```

### Verdict
**CONFIRMED.** Basis: county-archived night report with past-midnight
internal stamp (01:05:49 am) at 100% precincts, bracketed by the county's
own posting-schedule gap to the next-day run. Evidence:
`pri2012/run09/cumulative.pdf`, Run Date/Time 06/06/2012 01:05:49 am,
315,584 ballots, 1,976/1,976 precincts; next run (run10) dated 06/06/2012
04:45:57 pm = 331,362 (proves the gap). No FLAG needed.

---

## Item 2 of 6 — 2014-06-03 Statewide Direct Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf`
  (misspelling "particpiation" intact, matches the pattern already used for
  Orange's 2014 general in orange-ca.json; fetched 2026-07-10 with Chrome UA)
- Orange line: `Orange  1,856  1,955,899  1,411,232  99,397  240,790  340,187
  70.78%  24.11%  17.39%` = Precincts 1,856, Eligible 1,955,899, Registered
  1,411,232, Precinct Voters 99,397, VBM Voters 240,790, **Total Voters
  340,187**, %VBM 70.78%, Turnout/Reg 24.11%, Turnout/Elig 17.39%.
- **certified_final = 340,187**

### Plateau (numerator)
- Source URL: `https://ocvote.gov/fileadmin/live/pri2014/run10/cumulative.pdf`
- Full sequence (Run Date/Time | Total Ballots Cast | precincts): run01
  06/03/2014 07:41:17pm = 151,033 (0/1,856, VBM pre-count dump); climbs
  through run09 (06/04 12:41:45am, 235,580, 1,822/1,856); run10 (06/04
  **01:35:06am**, **238,460** = Precinct 87,164 + Absentee(VBM) 151,296,
  **1,856/1,856 = 100%**) — last night run; then a **~15.1-hour gap** to
  run11 (06/04 04:41:04pm, 245,809), where the multi-day canvass resumes
  (daily runs through run17, 06/12/2014 05:38:10pm, reaching 340,181,
  Precinct 99,391 + Absentee 240,790 — 6 ballots short of the SoS-certified
  340,187, a late-cure reconciliation gap of the same kind already
  documented for Orange's 2022 general in orange-ca.json; SoS figure used
  as the authoritative denominator).
- **Plateau evidence: CONFIRMED.** Past-midnight internal stamp (01:35:06
  am) + 100% precincts, bracketed by the ~15.1-hour posting-schedule gap to
  the next-day run — same non-circular leg pattern as item 1 and as the
  committed 2014 general row.
- **election_night_ballots = 238,460**

### Arithmetic
238,460 / 340,187 = **70.10%**

### Draft row (section 2 schema)
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": 238460,
  "certified_final": 340187,
  "election_night_pct": 70.1,
  "vs_epollbook": "pre",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://ocvote.gov/fileadmin/live/pri2014/run10/cumulative.pdf",
  "confidence": "primary",
  "note": "PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). OCROV posted sequential 'UNOFFICIAL RESULTS CUMULATIVE TOTALS' runs (Statewide Direct Primary Election, Tuesday June 3, 2014): run01 (Run Date/Time 06/03/2014 07:41:17 pm) = 151,033 ballots / 0 of 1,856 precincts = VBM-only pre-count dump; the count climbed and PLATEAUED at run10 (Run Date/Time 06/04/2014 01:35:06 am) = Total Ballots Cast 238,460 (Precinct Ballots Cast 87,164 + Absentee Ballots Cast 151,296) with ALL 1,856 of 1,856 precincts complete. run10 was the LAST election-night run before a ~15.1-hour gap to run11 (06/04/2014 04:41:04 pm = 245,809), where the multi-day canvass resumed (daily runs through run17, 06/12/2014 05:38:10 pm, reaching 340,181). 238,460 / 340,187 certified = 70.10%. Denominator: CA SoS Voter Participation Statistics by County (Orange Total Voters 340,187 = Precinct 99,397 + VBM 240,790); OCROV's own last live run (run17, 340,181 = Precinct 99,391 + Absentee 240,790) was 6 short of the SoS-certified figure (late-cure reconciliation, same pattern as the 2022 general's 50-ballot gap already documented for this county) -- SoS figure used as the authoritative denominator. Pre-epollbook. ASV never adopted. Snapshot used: ocvote.gov live pri2014/run10/cumulative.pdf (lowercase 'run', same style as pri2012), internal Run Date/Time 06/04/2014 01:35:06 am."
}
```

### VERIFY.md line
```
| 2014 | statewide-primary | 238,460 | 340,187 | 70.1% | primary | [link](https://ocvote.gov/fileadmin/live/pri2014/run10/cumulative.pdf) |
```
```
- **2014 statewide-primary** — night `238,460` / final `340,187` = `70.1%` (primary)
  - numerator: <https://ocvote.gov/fileadmin/live/pri2014/run10/cumulative.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf>
  - look for: run10's header "Run Date/Time: 06/04/2014 01:35:06 am", "Complete Precincts: 1,856 of 1,856", "Total Ballots Cast 238,460" (Precinct Ballots Cast 87,164 + Absentee Ballots Cast 151,296). Confirm run11 (same folder) is dated 06/04/2014 04:41:04 pm = 245,809.
```

### Verdict
**CONFIRMED.** Basis + evidence: same pattern as item 1 —
`pri2014/run10/cumulative.pdf`, Run Date/Time 06/04/2014 01:35:06 am,
238,460 ballots, 1,856/1,856 precincts; next run (run11) dated 06/04/2014
04:41:04 pm = 245,809. No FLAG needed.

---

## Item 3 of 6 — 2016-06-07 Presidential Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf`
  (no `sov/` or `pdf/` subfolder for this year; fetched 2026-07-10 with
  Chrome UA — plain curl also 200'd for this particular URL)
- Orange line: `Orange  1,597  2,000,797  1,395,380  283,619  408,183
  691,802  59.00%  49.58%  34.58%` = Precincts 1,597, Eligible 2,000,797,
  Registered 1,395,380, Precinct Voters 283,619, VBM Voters 408,183,
  **Total Voters 691,802**, %VBM 59.00%, Turnout/Reg 49.58%, Turnout/Elig
  34.58%.
- **certified_final = 691,802**

### Plateau (numerator)
- Source URL: `https://ocvote.gov/fileadmin/live/pri2016/Run%2010/cumulative.pdf`
  (folder uses capital "Run" + a literal space, URL-encoded `%2010`)
- Full sequence (Run Date/Time | Total Ballots Cast | precincts): run01
  06/07/2016 07:49:11pm = 254,324 (0/1,597, VBM pre-count dump); climbs
  through run09 (06/08 01:03:08am, 472,937, 1,592/1,597); Run 10 (06/08
  **02:11:01am**, **477,064**, **1,597/1,597 = 100%**) — last night run;
  then a **~14.75-hour gap** to Run 11 (06/08 04:55:50pm, 492,060), where
  the multi-day canvass resumes (daily/near-daily runs through Run 23,
  06/24/2016 06:36:09pm, reaching 691,802 exactly = the SoS-certified
  figure — this year's OCROV total reconciles to the SoS figure with zero
  gap).
- **Plateau evidence: CONFIRMED.** Past-midnight internal stamp (02:11:01
  am) + 100% precincts, bracketed by the ~14.75-hour posting-schedule gap
  to the next-day run.
- **election_night_ballots = 477,064**

### Arithmetic
477,064 / 691,802 = **68.96%**

### Draft row (section 2 schema)
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 477064,
  "certified_final": 691802,
  "election_night_pct": 68.96,
  "vs_epollbook": "pre",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://ocvote.gov/fileadmin/live/pri2016/Run%2010/cumulative.pdf",
  "confidence": "primary",
  "note": "PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). OCROV posted sequential 'UNOFFICIAL RESULTS CUMULATIVE TOTALS' runs (Presidential Primary Election, Tuesday June 7, 2016): run01 (Run Date/Time 06/07/2016 07:49:11 pm) = 254,324 ballots / 0 of 1,597 precincts = VBM-only pre-count dump; the count climbed and PLATEAUED at Run 10 (Run Date/Time 06/08/2016 02:11:01 am) = Total Ballots Cast 477,064 with ALL 1,597 of 1,597 precincts complete (Run 09 at 01:03:08 am was still 1,592/1,597 = not yet complete). Run 10 was the LAST election-night run before a ~14.75-hour gap to Run 11 (06/08/2016 04:55:50 pm = 492,060), where the multi-day canvass resumed (near-daily runs through Run 23, 06/24/2016 06:36:09 pm, reaching 691,802 = certified, exact match). 477,064 / 691,802 certified = 68.96%. Denominator confirmed: OCROV's own final run (Run 23) = 691,802 exactly = CA SoS Voter Participation Statistics by County (Orange Total Voters 691,802 = Precinct 283,619 + VBM 408,183). Pre-epollbook. ASV never adopted. Snapshot used: ocvote.gov live pri2016/Run 10/cumulative.pdf (capital 'Run' + space, URL-encoded 'Run%2010', matching the gen2016 'Run NN' convention), internal Run Date/Time 06/08/2016 02:11:01 am."
}
```

### VERIFY.md line
```
| 2016 | presidential-primary | 477,064 | 691,802 | 69.0% | primary | [link](https://ocvote.gov/fileadmin/live/pri2016/Run%2010/cumulative.pdf) |
```
```
- **2016 presidential-primary** — night `477,064` / final `691,802` = `69.0%` (primary)
  - numerator: <https://ocvote.gov/fileadmin/live/pri2016/Run%2010/cumulative.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf>
  - look for: Run 10's header "Run Date/Time: 06/08/2016 02:11:01 am", "Complete Precincts: 1,597 of 1,597", "Total Ballots Cast 477,064". Confirm Run 11 (same folder) is dated 06/08/2016 04:55:50 pm = 492,060.
```

### Verdict
**CONFIRMED.** Basis + evidence: `pri2016/Run 10/cumulative.pdf`, Run
Date/Time 06/08/2016 02:11:01 am, 477,064 ballots, 1,597/1,597 precincts
(Run 09 at 1,592/1,597 proves Run 10 is the first-and-last 100% night run);
next run (Run 11) dated 06/08/2016 04:55:50 pm = 492,060. No FLAG needed.

---

## Item 4 of 6 — 2018-06-05 Statewide Direct Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf`
- Orange line: `Orange  1,561  2,022,355  1,482,036  226,848  408,376
  635,224  64.29%  42.86%  31.41%` = Precincts 1,561, Eligible 2,022,355,
  Registered 1,482,036, Precinct Voters 226,848, VBM Voters 408,376,
  **Total Voters 635,224**, %VBM 64.29%, Turnout/Reg 42.86%, Turnout/Elig
  31.41%.
- **certified_final = 635,224**

### Plateau (numerator)
- Source URL: `https://ocvote.gov/fileadmin/live/pri2018/Run%2009/cumulative.pdf`
- Full sequence (Run Date/Time | Total Ballots Cast | precincts): run01
  06/05/2018 07:57:34pm = 191,928 (0/1,561, VBM pre-count dump); climbs
  through Run 08 (06/06 12:25:56am, 368,619, 1,557/1,561); Run 09 (06/06
  **12:55:42am**, **369,267** = Precinct 176,297 + Early 766 + VBM 192,204,
  **1,561/1,561 = 100%**) — last night run; then a **~16.0-hour gap** to
  Run 10 (06/06 04:55:41pm, 383,375), where the multi-day canvass resumes
  (near-daily runs through Run 27, 06/25/2018 04:11:15pm, reaching 635,224
  exactly = the SoS-certified figure).
- **Plateau evidence: CONFIRMED.** Past-midnight internal stamp (12:55:42
  am) + 100% precincts, bracketed by the ~16.0-hour posting-schedule gap to
  the next-day run. This share (58.13%) is essentially identical to the
  ~58.79% already CONFIRMED for Orange's 2018 general in orange-ca.json —
  a strong internal cross-check that this is a genuine same-cycle plateau,
  not a mis-picked tranche.
- **election_night_ballots = 369,267**

### Arithmetic
369,267 / 635,224 = **58.13%**

### Draft row (section 2 schema)
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 369267,
  "certified_final": 635224,
  "election_night_pct": 58.13,
  "vs_epollbook": "pre",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://ocvote.gov/fileadmin/live/pri2018/Run%2009/cumulative.pdf",
  "confidence": "primary",
  "note": "PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). OCROV posted sequential 'UNOFFICIAL RESULTS CUMULATIVE TOTALS' runs (Statewide Direct Primary Election, Tuesday June 5, 2018): run01 (Run Date/Time 06/05/2018 07:57:34 pm) = 191,928 ballots / 0 of 1,561 precincts = VBM-only pre-count dump; the count climbed and PLATEAUED at Run 09 (Run Date/Time 06/06/2018 12:55:42 am) = Total Ballots Cast 369,267 (Precinct Ballots Cast 176,297 + Early Ballots Cast 766 + Vote-by-Mail Ballots Cast 192,204) with ALL 1,561 of 1,561 precincts complete. Run 09 was the LAST election-night run before a ~16.0-hour gap to Run 10 (06/06/2018 04:55:41 pm = 383,375), where the multi-day canvass resumed (near-daily runs through Run 27, 06/25/2018 04:11:15 pm, reaching 635,224 = certified, exact match). 369,267 / 635,224 certified = 58.13% (essentially matches the already-CONFIRMED ~58.79% for Orange's 2018 GENERAL in orange-ca.json -- a strong same-cycle cross-check). Denominator confirmed: OCROV's own final run (Run 27) = 226,848 + 4,215 + 404,161 = 635,224 exactly = CA SoS Voter Participation Statistics by County (Orange Total Voters 635,224 = Precinct 226,848 + VBM 408,376). Pre-epollbook. ASV never adopted. Snapshot used: ocvote.gov live pri2018/Run 09/cumulative.pdf (capital 'Run' + space, URL-encoded 'Run%2009'), internal Run Date/Time 06/06/2018 12:55:42 am."
}
```

### VERIFY.md line
```
| 2018 | statewide-primary | 369,267 | 635,224 | 58.1% | primary | [link](https://ocvote.gov/fileadmin/live/pri2018/Run%2009/cumulative.pdf) |
```
```
- **2018 statewide-primary** — night `369,267` / final `635,224` = `58.1%` (primary)
  - numerator: <https://ocvote.gov/fileadmin/live/pri2018/Run%2009/cumulative.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: Run 09's header "Run Date/Time: 06/06/2018 12:55:42 am", "Complete Precincts: 1,561 of 1,561", Precinct Ballots Cast 176,297 + Early Ballots Cast 766 + Vote-by-Mail Ballots Cast 192,204 = 369,267 (the PDF prints this total on the line ABOVE the "Total Ballots Cast" label, a layout quirk unique to 2018). Confirm Run 10 (same folder) is dated 06/06/2018 04:55:41 pm = 383,375.
```

### Verdict
**CONFIRMED.** Basis + evidence: `pri2018/Run 09/cumulative.pdf`, Run
Date/Time 06/06/2018 12:55:42 am, 369,267 ballots, 1,561/1,561 precincts;
next run (Run 10) dated 06/06/2018 04:55:41 pm = 383,375; independently
corroborated by matching the county's already-CONFIRMED 2018 general share.
No FLAG needed.

---

## Item 5 of 6 — 2022-06-07 Statewide Direct Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf`
- Orange line (VCA county, marked `*`): `Orange*  2,179  2,205,404
  1,809,947  72,455  564,042  636,497  88.62%  35.17%  28.86%` = Precincts
  2,179, Eligible 2,205,404, Registered 1,809,947, Precinct Voters 72,455,
  VBM Voters 564,042, **Total Voters 636,497**, %VBM 88.62%, Turnout/Reg
  35.17%, Turnout/Elig 28.86%. Footnote: `*Voter's Choice Act
  county—precinct voters voted at vote centers.`
- **certified_final = 636,497**

### Plateau (numerator)
- Source URL: `https://ocvote.gov/fileadmin/live/PRI2022/Run_06/cumulative.pdf`
  (all-caps folder `PRI2022`, `Run_NN` with underscore)
- VCA vote-center era: precincts already 2,179/2,179 = 100% from run01, so
  the plateau is identified purely by the TIME GAP (same method as Orange's
  committed 2022/2024 generals), not by precinct completion.
- Full sequence (Run Date | Run Time | Ballots "N of Registered = %"): run01
  06/07/2022 8:00 PM = 253,319 of 1,809,773 = 14.00% (pre-Election-Day mail
  first tranche); run02 9:17 PM = 254,567; run03 9:51 PM = 263,524; run04
  10:17 PM = 264,324; run05 10:49 PM = 298,810; **run06 11:15 PM =
  325,774** (18.00%) — last night run; then a **~17.4-hour gap** to run07
  (06/08/2022 4:38 PM = 348,130), where the multi-day canvass resumes
  (near-daily runs through run20, 06/24/2022 3:58 PM, reaching 636,497
  exactly = the SoS-certified figure).
- **Plateau evidence: CONFIRMED.** Election-night stamp (11:15 PM, same
  calendar day as polls-close) + the county's own posting-schedule gap
  (~17.4 hours to the next-day-afternoon run07) — the same non-circular leg
  already used for Orange's 2022/2024 generals.
- **election_night_ballots = 325,774**

### Arithmetic
325,774 / 636,497 = **51.18%**

### Draft row (section 2 schema)
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 325774,
  "certified_final": 636497,
  "election_night_pct": 51.18,
  "vs_epollbook": "post",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://ocvote.gov/fileadmin/live/PRI2022/Run_06/cumulative.pdf",
  "confidence": "primary",
  "note": "PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Vote-center era (precincts read 100% from run01 on -- 2,179 of 2,179 -- so the plateau is identified by the election-night/next-day TIME GAP, not precinct %, same method as Orange's 2022/2024 generals). run01 (Run Date 06/07/2022, Run Time 8:00 PM) = 253,319 ballots (14.00% of 1,809,773 registered) = pre-Election-Day mail first tranche; the count climbed and PLATEAUED at run06 (Run Date 06/07/2022, Run Time 11:15 PM) = 325,774 ballots (18.00%). run06 was the LAST election-night run before a ~17.4-hour gap to run07 (06/08/2022, 4:38 PM = 348,130), where the multi-day canvass resumed (near-daily runs through run20, 06/24/2022 3:58 PM, reaching 636,497 = certified, exact match). 325,774 / 636,497 certified = 51.18%. Denominator confirmed: OCROV's own final run (run20) = 636,497 exactly = CA SoS Voter Participation Statistics by County (Orange* Total Voters 636,497 = Precinct 72,455 + VBM 564,042; *Voter's Choice Act county, precinct voters voted at vote centers). Post-epollbook (e-pollbooks + Voter's Choice Act vote centers since March 2020; the all-mail VCA model independently front-loads ballots into the pre-Election-Day mail batch, consistent with this share running below the pre-epollbook 2014/2018 statewide primaries -- same confound already flagged for the generals). ASV never adopted. Snapshot used: ocvote.gov live PRI2022/Run_06/cumulative.pdf, internal Run Date 06/07/2022 Run Time 11:15 PM."
}
```

### VERIFY.md line
```
| 2022 | statewide-primary | 325,774 | 636,497 | 51.2% | primary | [link](https://ocvote.gov/fileadmin/live/PRI2022/Run_06/cumulative.pdf) |
```
```
- **2022 statewide-primary** — night `325,774` / final `636,497` = `51.2%` (primary)
  - numerator: <https://ocvote.gov/fileadmin/live/PRI2022/Run_06/cumulative.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: header "Run Date  06/07/2022" / "Run Time  11:15 PM", "Registered Voters  325774 of 1809773 = 18.00%", "Precincts Reporting  2179 of 2179 = 100.00%". Confirm run07 (same folder, Run_07) is dated 06/08/2022 4:38 PM = 348,130.
```

### Verdict
**CONFIRMED.** Basis + evidence: `PRI2022/Run_06/cumulative.pdf`, Run Date
06/07/2022 Run Time 11:15 PM, 325,774 ballots (100% precincts, VCA era);
next run (run07) dated 06/08/2022 4:38 PM = 348,130 (proves the ~17.4-hour
gap). No FLAG needed.

---

## Item 6 of 6 — 2024-03-05 Presidential Primary

### Certified final (denominator)
- SoV URL: `https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf`
- Orange line (VCA county, marked `*`): `Orange*  2,239  2,176,472
  1,818,551  106,283  578,755  685,038  84.49%  37.67%  31.47%` = Precincts
  2,239, Eligible 2,176,472, Registered 1,818,551, Precinct Voters 106,283,
  VBM Voters 578,755, **Total Voters 685,038**, %VBM 84.49%, Turnout/Reg
  37.67%, Turnout/Elig 31.47%. Footnote: `*Voter's Choice Act
  county—precinct voters voted at vote centers.`
- **certified_final = 685,038**

### Plateau (numerator)
- Source URL: `https://ocvote.gov/fileadmin/live/PRI2024/Run_07/cumulative.pdf`
- VCA vote-center era: precincts already 2,239/2,239 = 100% from run01.
- Full sequence (Run Date | Run Time | Ballots "N of Registered = %"): run01
  03/05/2024 8:00 PM = 302,566 of 1,819,334 = 16.63% (pre-Election-Day mail
  first tranche); run02 9:20 PM = 307,356; run03 9:50 PM = 317,065; run04
  10:20 PM = 348,420; run05 10:50 PM = 379,754; run06 11:20 PM = 394,489;
  **run07 11:43 PM = 400,430** (22.01%) — last night run; then a
  **~17.3-hour gap** to run08 (03/06/2024 5:03 PM = 427,131), where the
  multi-day canvass resumes (near-daily runs through run21, 03/22/2024
  3:59 PM, reaching 685,038 exactly = the SoS-certified figure).
- **Plateau evidence: CONFIRMED.** Election-night stamp (11:43 PM) + the
  county's own posting-schedule gap (~17.3 hours to the next-day-afternoon
  run08) — same non-circular leg as item 5 and Orange's committed
  2022/2024 generals.
- **election_night_ballots = 400,430**

### Arithmetic
400,430 / 685,038 = **58.45%**

### Draft row (section 2 schema)
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 400430,
  "certified_final": 685038,
  "election_night_pct": 58.45,
  "vs_epollbook": "post",
  "vs_asv": "n-a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://ocvote.gov/fileadmin/live/PRI2024/Run_07/cumulative.pdf",
  "confidence": "primary",
  "note": "PLATEAU metric (final election-night report, NOT the 8 p.m. first tranche). Vote-center era (precincts read 100% from run01 on -- 2,239 of 2,239 -- so the plateau is identified by the election-night/next-day TIME GAP, not precinct %). run01 (Run Date 03/05/2024, Run Time 8:00 PM) = 302,566 ballots (16.63% of 1,819,334 registered) = pre-Election-Day mail first tranche; the count climbed through the night and the LAST election-night run was run07 (Run Date 03/05/2024, Run Time 11:43 PM) = 400,430 ballots (22.01%), after which a ~17.3-hour gap to run08 (03/06/2024, 5:03 PM = 427,131) marks the multi-day canvass resuming (near-daily runs through run21, 03/22/2024 3:59 PM, reaching 685,038 = certified, exact match). 400,430 / 685,038 certified = 58.45%. Denominator confirmed: OCROV's own final run (run21) = 685,038 exactly = CA SoS Voter Participation Statistics by County (Orange* Total Voters 685,038 = Precinct 106,283 + VBM 578,755; *Voter's Choice Act county, precinct voters voted at vote centers). Post-epollbook (e-pollbooks + Voter's Choice Act vote centers since March 2020). ASV never adopted (OC verifies signatures by hand). Snapshot used: ocvote.gov live PRI2024/Run_07/cumulative.pdf, internal Run Date 03/05/2024 Run Time 11:43 PM."
}
```

### VERIFY.md line
```
| 2024 | presidential-primary | 400,430 | 685,038 | 58.5% | primary | [link](https://ocvote.gov/fileadmin/live/PRI2024/Run_07/cumulative.pdf) |
```
```
- **2024 presidential-primary** — night `400,430` / final `685,038` = `58.5%` (primary)
  - numerator: <https://ocvote.gov/fileadmin/live/PRI2024/Run_07/cumulative.pdf>
  - denominator (SoS SoV): <https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf>
  - look for: header "Run Date  03/05/2024" / "Run Time  11:43 PM", "Registered Voters  400430 of 1819334 = 22.01%", "Precincts Reporting  2239 of 2239 = 100.00%". Confirm run08 (same folder, Run_08) is dated 03/06/2024 5:03 PM = 427,131.
```

### Verdict
**CONFIRMED.** Basis + evidence: `PRI2024/Run_07/cumulative.pdf`, Run Date
03/05/2024 Run Time 11:43 PM, 400,430 ballots (100% precincts, VCA era);
next run (run08) dated 03/06/2024 5:03 PM = 427,131 (proves the ~17.3-hour
gap). No FLAG needed.

---

## Nulls (section 5.1)

None. All 6 primaries yielded a sourced, CONFIRMED plateau via route 2
(the county's own dated report series, section 6.3) on the FIRST route
tried — the live ocvote.gov CMS still serves the complete historical Run
series for every primary 2012-2024, so no press-release search, Wayback
detour, Clarity check, or news search was needed for any row. No
`FLAG for manual operator` was required anywhere in this pass.

## Cross-check: internal consistency with Orange's committed generals

| Year | Type | Election-night % | Adjacent general (same slug year, orange-ca.json) |
|---|---|---:|---:|
| 2012 | pres-primary | 73.93% | 2012 general 76.12% |
| 2014 | statewide-primary | 70.10% | 2014 general 72.51% |
| 2016 | pres-primary | 68.96% | 2016 general 66.59% |
| 2018 | statewide-primary | 58.13% | 2018 general 58.79% |
| 2022 | statewide-primary | 51.18% | 2022 general 61.46% |
| 2024 | pres-primary | 58.45% | 2024 general 71.06% |

All six primary shares sit within a plausible band of their same-year
general (never anywhere near half, which is the classic first-tranche
red flag from RUNBOOK section 1) — strong corroboration that every
numerator here is a genuine plateau. Pattern worth flagging to the
maintainer for the tech-comparison chart, consistent with the CAVEAT
already recorded in orange-ca.json for the generals: the two POST-epollbook
primaries (2022, 2024) both sit noticeably BELOW their pre-epollbook
same-type predecessors (2018 statewide 58.13% -> 2022 statewide 51.18%;
2016 presidential 68.96% -> 2024 presidential 58.45%), the same VCA
all-mail-front-loading effect already documented for the generals, not a
counting-speed regression from e-pollbooks.

## Pipeline status

This dossier is a READ-ONLY research product; nothing in
`data/research/election-night/` was written or edited, and the section 3
pipeline (validator, build_county_night, verify_en_*, pytest, vitest) was
NOT run, since these 6 rows are not yet merged into orange-ca.json. Before
any operator merges these rows: append them to the `elections` array in
`data/research/election-night/orange-ca.json` (surgical edits, not a
whole-file rewrite per section 2's editing rule), add the six VERIFY.md
lines to a "Primaries" subsection under Orange County's existing entry
(or a parallel table -- the existing table has no Type-disambiguating rows
today since it only has generals), add the six plateau_review.json
verdict records above, then run the full section 3 pipeline end to end.
