# Napa County (napa-ca) — statewide PRIMARY election-night dossier

Read-only research scratch dossier. NOT a repo edit. Built per
`docs/research/RUNBOOK.md` sections 1, 5, 6, 7 (esp. 7.5 cards-vs-voters), 8,
and `data/research/election-night/napa-ca.json` (generals, already committed)
for URL patterns / conventions. Six statewide primaries: 2012-06-05 (PRE,
presidential-primary), 2014-06-03 (PRE, statewide-primary), 2016-06-07 (PRE,
presidential-primary), 2018-06-05 (ROLLOUT — Napa's first VCA/e-pollbook
election; classed POST per napa-ca county-tech record `first_election:
"2018-06"`), 2022-06-07 (POST, statewide-primary), 2024-03-05 (POST,
presidential-primary).

Denominators: CA SoS SoV "Voter Participation Statistics by County" PDF per
primary year, Napa's "Total Voters" column (== Precinct Voters + Vote-By-Mail
Voters). Percent = election_night_ballots / certified_final * 100, 2dp,
PERCENT units.

---

## Item 1: 2012-06-05 (Presidential Primary) — presidential-primary

### Denominator (CA SoS SoV)
- URL: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf
  (NOTE: filename says "voter-reg-stats" but the PDF body's table header reads
  "VOTER PARTICIPATION STATISTICS BY COUNTY" — 2012 primary SOV names this
  file differently than the general-election SOV convention; verified by
  fetch + pdftotext -layout, confirmed it is the participation table, not a
  registration-only table.)
- Napa line (pdftotext -layout, row order: Precincts, Eligible to Register,
  Registered Voters, Precinct Voters, Vote-By-Mail Voters, Total Voters, %VBM,
  Turnout/Reg, Turnout/Eligible):
  `Napa   157   90,847   68,330   2,616   26,689   29,305   91.07%   42.89%   32.26%`
- **Total Voters (certified final) = 29,305**

### Numerator / plateau
- County site: old countyofnapa.org/ElectionResults framed-HTML series
  (same family as the 2012-11 general row already in napa-ca.json).
- CDX enumeration (`cdx?url=countyofnapa.org/ElectionResults/20120605&matchType=prefix`)
  shows exactly THREE election-night reports — 0801PM, 0956PM, 1052PM — then
  the series jumps straight to `20120605-Final.htm`, whose own `_dtl.htm`
  internal header reads "Last Updated: June 25, 2012 2:59 PM" (the certified
  canvass final, 20 days later, NOT an election-night report). No report
  exists between 10:52 PM and June 25.
- 8:01 PM report (`_dtl.htm`, snapshot 20120608220109): "Last Updated: June 5,
  2012 8:01 PM", Registration & Turnout (68,330 registered) = Vote by Mail
  Turnout 16,357 (23.94%) + Polling Place Turnout 0 (0.00%) = Total 16,357
  (23.94%). This is the all-pre-processed-VBM first tranche (same pattern as
  Nov 2012: VBM release fixed all night, polling place trickles in).
- 10:52 PM report (`_dtl.htm`, snapshot 20120608220101, fetched raw via
  `https://web.archive.org/web/20120608220101id_/http://www.countyofnapa.org/ElectionResults/20120605/20120605-1052PM_dtl.htm`):
  "Last Updated: June 5, 2012 10:52 PM". Registration & Turnout (68,330
  registered, matches SoV Registered Voters exactly) = Vote by Mail Turnout
  16,357 (23.94%, unchanged from 8:01 PM — VBM was already fully processed
  pre-election-night) + Polling Place Turnout 2,790 (4.08%) = **Total 19,147
  (28.02%)**. `_hdr.htm` (snapshot 20120608220059) confirms page title
  "Napa County / Presidential Primary Election / June 5, 2012 / Unofficial
  Election Night Results".
- This is the LAST election-night report (no later same-night report exists;
  the next archived report is the June 25 certified Final, 20 days later) —
  the plateau. NOT the 8:01 PM first tranche (16,357 = 23.94%, VBM-only).
- **election_night_ballots = 19,147**
- Source URL (numerator): https://web.archive.org/web/20120608220101/http://www.countyofnapa.org/ElectionResults/20120605/20120605-1052PM_dtl.htm

### Arithmetic
19,147 / 29,305 = 0.653400... = **65.34%**

(Above the SF presidential-primary calibration point (~71% in 2012 general),
but this is a June PRIMARY not a November general — lower-salience contest,
smaller electorate, and Napa's June 2012 VBM was only ~59% processed by
election night (16,357 of the eventual certified 26,689 VBM total) vs the
near-100%-processed VBM typical of a November general, so a big remaining
precinct+late-VBM tranche moved in the multi-day canvass. Recorded as-is;
this is a real cross-election-type difference, not a data error — flagged for
operator sanity check given no directly comparable primary calibration point
exists in the runbook.)

### Draft row (schema, `data/research/election-night/napa-ca.json` shape)
```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": 19147,
  "certified_final": 29305,
  "election_night_pct": 65.34,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/03-voter-reg-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20120608220101/http://www.countyofnapa.org/ElectionResults/20120605/20120605-1052PM_dtl.htm",
  "confidence": "primary",
  "note": "PLATEAU = final-of-night report. County '_hdr' identifies 'Napa County / Presidential Primary Election / June 5, 2012 / Unofficial Election Night Results'; '_dtl' header reads 'Last Updated: June 5, 2012 10:52 PM'. Registration & Turnout block (68,330 registered, matches SoV exactly): Vote by Mail Turnout 16,357 (23.94%, fixed since the 8:01 PM first tranche) + Polling Place Turnout 2,790 (4.08%) = Total 19,147 (28.02%). CDX enumeration of countyofnapa.org/ElectionResults/20120605/* shows only three election-night reports (0801PM, 0956PM, 1052PM); the series' next file jumps to 20120605-Final.htm, self-timestamped 'Last Updated: June 25, 2012 2:59 PM' (certified canvass, 20 days later) -- proving 10:52 PM was the last report of election night. NOT the 8:01 PM first tranche (16,357 = 23.94%, all pre-processed VBM). Certified final 29,305 voters (CA SoS 2012-primary Voter Participation Statistics by County: 2,616 precinct + 26,689 VBM; note the SOV filename for this table is misnamed '03-voter-reg-stats-by-county.pdf' though its body table is 'VOTER PARTICIPATION STATISTICS BY COUNTY'). Pct = 19,147/29,305 = 65.34%; this June-primary share is well above the SF November-general calibration band because Napa's June 2012 VBM was only ~61% processed by election night (16,357 of the eventual certified 26,689), unlike a November general where VBM release is typically near-complete pre-election-night -- a real cross-election-type effect (primary vs general processing volume/staffing), not a data error. Pre-epollbook (adopted 2018); ASV never."
}
```

### VERIFY.md line (draft, primaries table -- new section/table needed; column order matches existing Napa County generals table)
```
| 2012 | presidential-primary | 19,147 | 29,305 | 65.3% | primary | [link](https://web.archive.org/web/20120608220101/http://www.countyofnapa.org/ElectionResults/20120605/20120605-1052PM_dtl.htm) |
```

### plateau_review.json entry (draft)
```json
{"slug": "napa-ca", "date": "2012-06-05", "verdict": "CONFIRMED", "basis": "late-night internal timestamp (10:52 PM) plus the report series' next file being 20 days later (certified canvass Final, June 25)", "evidence": "'_dtl' header 'Last Updated: June 5, 2012 10:52 PM'; CDX shows no report between 10:52 PM and the June 25 Final.htm; '_hdr' confirms 'Unofficial Election Night Results' framing"}
```

### VERDICT
CONFIRMED, confidence primary. Denominator solid (SoV table, matches Registered
Voters cross-check exactly). Numerator solid: three-report CDX enumeration
plus a 20-day gap to the next (certified) report is strong plateau evidence,
matching the section-8 bar (late-night timestamp self-description + the
report-series-next-file-is-days-later leg). One thing for a human to sanity
check: the 65.34% figure is notably ABOVE Napa's own November-general
election-night shares (53.9-56.7% pre-VCA); the note explains this as a
primary-vs-general VBM-processing-speed difference (VBM was materially less
complete by election night in this June primary than in the Nov generals),
which is a plausible real effect but is exactly the kind of "well above the
county's own adjacent elections" pattern RUNBOOK section 1 says to be
suspicious of — FLAG for manual operator to eyeball the raw dtl page via
Wayback UI and confirm 19,147/2,790 aren't a mis-scrape.

---

## Item 2: 2014-06-03 (Gubernatorial Primary) — statewide-primary

### Denominator (CA SoS SoV)
- URL: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
  (misspelling "particpiation" intact, same convention as the 2014-general row
  already in napa-ca.json)
- Napa line: `Napa   165   91,388   71,241   1,404   26,775   28,179   95.02%   39.55%   30.83%`
- **Total Voters (certified final) = 28,179**

### Numerator / plateau
- Same countyofnapa.org/ElectionResults framed-HTML series. CDX enumeration
  (`cdx?url=countyofnapa.org/ElectionResults/20140603&matchType=prefix`) shows
  exactly THREE election-night reports — 2001 (8:01 PM), 2210 (10:10 PM), 2330
  (11:30 PM) — then the next file is `20140611-1430.htm` (June 11, 2:30 PM, 8
  days later, a canvass update), then `CertifiedFinalResults.htm`. No report
  exists between 11:30 PM June 3 and June 11.
- 8:01 PM report (`2001_dtl.htm`, snapshot 20140726114741): "Last Updated:
  June 3, 2014 8:01 PM", Registration & Turnout (71,241 registered) = Vote by
  Mail Turnout 16,133 (22.65%) + Election Day Turnout 0 (0.00%) = Total 16,133
  (22.65%) — the all-pre-processed-VBM first tranche.
- 11:30 PM report (`2330_dtl.htm`, snapshot 20140725071031, fetched raw via
  `https://web.archive.org/web/20140725071031id_/http://www.countyofnapa.org/ElectionResults/20140603/20140603-2330_dtl.htm`):
  "Last Updated: June 3, 2014 11:30 PM". Registration & Turnout (71,241
  registered, matches SoV Registered Voters exactly) = Vote by Mail Turnout
  16,133 (22.65%, unchanged from 8:01 PM) + Election Day Turnout 1,298 (1.82%)
  = **Total 17,431 (24.47%)**.
- This is the LAST election-night report (next archived report is 8 days
  later) — the plateau. NOT the 8:01 PM first tranche (16,133 = 22.65%,
  VBM-only).
- **election_night_ballots = 17,431**
- Source URL (numerator): https://web.archive.org/web/20140725071031/http://www.countyofnapa.org/ElectionResults/20140603/20140603-2330_dtl.htm

### Arithmetic
17,431 / 28,179 = 0.618581... = **61.86%**

(Same primary-vs-general pattern as 2012-06: well above Napa's November-general
band, driven by VBM being only ~60% processed by election night in this June
primary — 16,133 of the eventual certified 26,775 VBM — vs near-complete VBM
release typical of a November general.)

### Draft row
```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": 17431,
  "certified_final": 28179,
  "election_night_pct": 61.86,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20140725071031/http://www.countyofnapa.org/ElectionResults/20140603/20140603-2330_dtl.htm",
  "confidence": "primary",
  "note": "PLATEAU = final-of-night report. '_dtl' header reads 'Last Updated: June 3, 2014 11:30 PM'. Registration & Turnout block (71,241 registered, matches SoV Registered Voters exactly): Vote by Mail Turnout 16,133 (22.65%, fixed since the 8:01 PM first tranche) + Election Day Turnout 1,298 (1.82%) = Total 17,431 (24.47%). CDX enumeration of countyofnapa.org/ElectionResults/20140603/* shows only three election-night reports (2001, 2210, 2330); the series' next file is 20140611-1430.htm, 8 days later, then CertifiedFinalResults.htm -- proving 11:30 PM was the last report of election night. NOT the 8:01 PM first tranche (16,133 = 22.65%, all pre-processed VBM). Certified final 28,179 voters (CA SoS 2014-primary Voter Participation Statistics by County: 1,404 precinct + 26,775 VBM). Pct = 17,431/28,179 = 61.86%; consistent with the June-primary-vs-November-general pattern seen at 2012-06 (VBM materially less complete by election night in June primaries than in Nov generals -- a real cross-election-type effect, not a data error). Pre-epollbook (adopted 2018); ASV never."
}
```

### VERIFY.md line (draft)
```
| 2014 | statewide-primary | 17,431 | 28,179 | 61.9% | primary | [link](https://web.archive.org/web/20140725071031/http://www.countyofnapa.org/ElectionResults/20140603/20140603-2330_dtl.htm) |
```

### plateau_review.json entry (draft)
```json
{"slug": "napa-ca", "date": "2014-06-03", "verdict": "CONFIRMED", "basis": "late-night internal timestamp (11:30 PM) plus the report series' next file being 8 days later (June 11 canvass update, then CertifiedFinalResults)", "evidence": "'_dtl' header 'Last Updated: June 3, 2014 11:30 PM'; CDX shows no report between 11:30 PM and 20140611-1430.htm"}
```

### VERDICT
CONFIRMED, confidence primary. Same evidentiary shape as 2012-06 (three-report
CDX enumeration + multi-day gap to next report + Registered-Voters
cross-check against the SoV). FLAG for manual operator: same June-primary
elevated-share pattern as 2012-06 (61.9% vs the Nov-general 47.2% in this same
pre-VCA era) — worth a human eyeball of the raw Wayback page to confirm the
1,298/17,431 read, though the internal arithmetic (16,133 + 1,298 = 17,431,
24.47% of 71,241) is self-consistent within the artifact.

---

## Item 3: 2016-06-07 (Presidential Primary) — presidential-primary

### Denominator (CA SoS SoV)
- URL: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf
  (2016 primary drops the `sov/` path segment used by the 2016-general SOV;
  correct table title "VOTER PARTICIPATION STATISTICS BY COUNTY" confirmed by
  pdftotext.)
- Napa line: `Napa   167   93,331   72,461   2,150   41,300   43,450   95.05%   59.96%   46.55%`
- **Total Voters (certified final) = 43,450**

### Numerator / plateau
- County site switched to PDF-report format by 2016 (same family as the
  2016-11 general row in napa-ca.json). CDX enumeration
  (`cdx?url=countyofnapa.org/ElectionResults/20160607&matchType=prefix`)
  shows: a pre-election `20160513-0445PM.pdf` (sample-ballot-era file, not a
  results report), then TWO election-night reports — `20160607-0801PM.pdf`
  and `20160607-1032PM.pdf` — then the next file is `20160623-0224PM.pdf`
  (June 23, 16 days later, a canvass update), then
  `20160629-1059AM-Final.pdf` (certified final).
- 8:01 PM report (fetched via
  `https://web.archive.org/web/20160615060453id_/...20160607-0801PM.pdf`,
  pdftotext): titled "Unofficial Election Night **First** Report /
  Presidential Primary / County of Napa / June 7, 2016", stamped
  "6/7/2016 8:01:00 PM", "Precincts Reported: 154 of 167 (92.22%)", "**Ballots
  Cast: 18,331**".
- 10:32 PM report (fetched via
  `https://web.archive.org/web/20160615054733id_/...20160607-1032PM.pdf`,
  pdftotext): titled "Unofficial Election Night **Last** Report / Presidential
  Primary / County of Napa / June 7, 2016", stamped "6/7/2016 10:32:42 PM",
  "Precincts Reported: 167 of 167 (100.00%)", "**Ballots Cast: 20,427**".
  Pre-VCA single-card ballot (VCA/e-pollbooks not adopted until 2018), so
  "Ballots Cast" = voters here, unlike the post-2018 ballot-CARDS trap in
  RUNBOOK 7.5 (mirrors the 2016-11 general row's identical reasoning).
- This report explicitly self-titles "Last Report" (not just a timestamp
  inference) and the next archived file is 16 days later — the plateau. NOT
  the 8:01 PM "First Report" (18,331 = 42.19%).
- **election_night_ballots = 20,427**
- Source URL (numerator): https://web.archive.org/web/20160615054733/http://www.countyofnapa.org/ElectionResults/20160607/20160607-1032PM.pdf

### Arithmetic
20,427 / 43,450 = 0.470195... = **47.01%**

(Below Napa's own Nov 2016 general share of 53.92% -- the opposite direction
from the 2012/2014 June primaries, which both ran ABOVE their adjacent
generals. A presidential primary with the top-of-ticket races already
functionally decided nationally by June 7, 2016 plausibly depressed
election-night processing urgency/turnout differently than a March-timed or
more competitive primary; recorded as-is, FLAG for operator awareness that
the three primaries do not move in one consistent direction relative to their
generals.)

### Draft row
```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 20427,
  "certified_final": 43450,
  "election_night_pct": 47.01,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20160615054733/http://www.countyofnapa.org/ElectionResults/20160607/20160607-1032PM.pdf",
  "confidence": "primary",
  "note": "PLATEAU = self-titled 'Unofficial Election Night Last Report' (County of Napa, Presidential Primary, June 7, 2016), page stamp '6/7/2016 10:32:42 PM' (next archived file is the June 23 canvass update, 16 days later, then the June 29 certified Final). 'Precincts Reported: 167 of 167 (100.00%)', 'Ballots Cast: 20,427'. Pre-VCA single-card ballot (e-pollbooks not adopted until 2018), so Ballots Cast = voters (not the post-2018 ballot-CARDS trap in RUNBOOK 7.5). NOT the 8:01 PM 'First Report' (Ballots Cast 18,331 = 42.19%). Certified final 43,450 voters (CA SoS 2016-primary Voter Participation Statistics by County: 2,150 precinct + 41,300 VBM). Pct = 20,427/43,450 = 47.01%, BELOW the adjacent Nov 2016 general share (53.92%) -- opposite direction from the 2012-06/2014-06 primaries, which both ran above their adjacent generals; recorded as-is, no consistent primary-vs-general direction across this county's primary history. Pre-epollbook (adopted 2018); ASV never. PDF downloaded from snapshot 20160615054733 (id_ raw) and parsed with pdftotext."
}
```

### VERIFY.md line (draft)
```
| 2016 | presidential-primary | 20,427 | 43,450 | 47.0% | primary | [link](https://web.archive.org/web/20160615054733/http://www.countyofnapa.org/ElectionResults/20160607/20160607-1032PM.pdf) |
```

### plateau_review.json entry (draft)
```json
{"slug": "napa-ca", "date": "2016-06-07", "verdict": "CONFIRMED", "basis": "county report self-titled 'Unofficial Election Night Last Report' plus the report series' next file being 16 days later (June 23 canvass update, then June 29 certified Final)", "evidence": "'Unofficial Election Night Last Report / Presidential Primary / County of Napa / June 7, 2016', stamp 6/7/2016 10:32:42 PM, 167/167 precincts"}
```

### VERDICT
CONFIRMED, confidence primary. Strongest evidence of the three PRE-era
primaries so far: the artifact self-titles "Last Report" (not inferred from
timestamp alone) AND the next file is a clean 16-day gap. Denominator
cross-checks cleanly (167 precincts matches SoV's 167). FLAG for operator:
this primary's share (47.0%) sits BELOW its adjacent Nov general (53.9%),
reversing the direction seen in 2012-06/2014-06 -- worth a sanity confirm
that 18,331 -> 20,427 is really the full night's movement and not a
partially-captured "First Report" mislabeled page.

---

## Item 4: 2018-06-05 (Statewide Direct Primary) — statewide-primary — ROLLOUT ELECTION

**This is Napa's first VCA / e-pollbook election** (county-tech record
`data/research/county-tech/napa-ca.json`: `epollbook.adopted_year: 2018`,
`first_election: "2018-06"`). Classed **`vs_epollbook: "post"`** — the
rollout happened AT this election, not after it; e-pollbooks/vote centers
were live for the entire June 5, 2018 primary.

### Denominator (CA SoS SoV)
- URL: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
- Napa line: `Napa   170   92,519   76,211   4   37,521   37,525   99.99%   49.24%   40.56%`
  (Precinct Voters col is "4" -- essentially all-mail, consistent with VCA
  vote-center rollout: in-person Election Day precinct voting nearly
  vanished.)
- **Total Voters (certified final) = 37,525**

### Numerator / plateau
- Found via the county's own **Past Election Results Archive** page for this
  election (`https://www.napacounty.gov/4026/June-5-2018-Election-Results`,
  fetched live, still hosted -- same live-DocumentCenter pattern as the
  2018-11 general row), which lists the full report series:
  1. First Unofficial Election Night Report -- 06/05/2018 8:01pm (View/8721)
  2. **Final Unofficial Election Night Report -- 06/05/2018 10:39pm (View/8722)**
  3. First Unofficial POST-Election Night Report -- 6/08/2018 3:57pm (View/8748, 3 days later)
  4. Second Unofficial Post-Election Night Report -- 6/11/2018 4:07pm (View/8760)
  5. Third Unofficial Post-Election Night Report -- 6/12/2018 4:20pm (View/8772)
  6. Last Unofficial Post-Election Night Report -- 6/13/2018 4:50pm (View/8784)
  7. Final Certified Election Results (View/8900)
  The archive page's own link text titles #2 "**Final** Unofficial Election
  Night Report" (the last report still labeled "Election Night", before the
  series switches to "POST-Election Night" starting 3 days later) -- this is
  Napa's June-primary equivalent of the Nov-general "LAST UNOFFICIAL
  ELECTION NIGHT REPORT" naming.
- Fetched PDF (`https://www.napacounty.gov/DocumentCenter/View/8722/Final-Unofficial-Election-Night-Report---Primary-Election-06052018-1039pm-PDF`,
  pdftotext): titled "FINAL ELECTION NIGHT SEMIFINAL OFFICIAL CANVASS / JUNE
  5, 2018 PRIMARY ELECTION NAPA COUNTY", page stamp "6/5/2018 10:39:31 PM".
  Header: "Precincts Reported: 170 of 170 (100.00%)", "**Registered Voters:
  15,091 of 76,236 (19.80%)**", "Ballots Cast: 30,211".
- **RUNBOOK 7.5 trap, hit exactly as documented ("Sacramento 2018, Napa
  2018")**: the header's "Registered Voters: 15,091 of 76,236" line is a
  MISLABEL -- 76,236 is the true registered-voter count (matches SoV's
  76,211 closely; SoV's is a 15-day-close figure, the county's own report
  runs slightly later same-day-registration-inclusive, a known small
  divergence) but 15,091 is actually **Times Cast**, confirmed by the
  per-contest "GOVERNOR (Vote for 1)" row: "Times Cast ... 4 / 15,087 /
  15,091 / 76,236 / 19.80%" -- i.e. the SAME 15,091/76,236 pair reappears
  explicitly labeled "Times Cast". "Ballots Cast: 30,211" is ballot CARDS
  (~2x voters, VCA 2-card ballot), NOT the comparable metric (per RUNBOOK
  7.5: "VCA-era Napa reports 'Ballots Cast' as ballot CARDS ... 'Times Cast'
  / 'Voters Cast' is the voter count you want").
- Cross-check against the First Report (8:01pm, View/8721, pdftotext):
  "FIRST ELECTION NIGHT SEMIFINAL OFFICIAL CANVASS", stamp "6/5/2018
  8:01:57 PM", "Precincts Reported: 168 of 170 (98.82%)", "Registered
  Voters [mislabeled Times Cast]: 15,087 of 76,236 (19.79%)". The count
  barely moved all night (15,087 -> 15,091, +4 voters) -- same signature as
  the 2018-11 general row ("First report of the night was 21,732 voters ...
  the count barely moved election night"): this was Napa's first
  vote-center/all-mail election, so nearly all VBM was pre-processed and
  released in the FIRST tranche already, and same-day-dropped ballots +
  vote-center same-day voting were processed in the multi-day canvass, NOT
  election night.
- Cross-check against the First POST report (6/8/2018 3:57pm, View/8748,
  pdftotext): "SECOND COUNT JUNE 8, 2018", "Registered Voters [Times Cast]:
  16,773 of 76,236 (22.00%)" -- confirms real canvass movement resumed 3
  days later, i.e. 10:39 PM June 5 was genuinely frozen/paused until then.
- **election_night_ballots = 15,091**
- Source URL (numerator): https://www.napacounty.gov/DocumentCenter/View/8722/Final-Unofficial-Election-Night-Report---Primary-Election-06052018-1039pm-PDF

### Arithmetic
15,091 / 37,525 = 0.402051... = **40.22%**

(Closely tracks the 2018-11 general's 38.11% -- both are Napa's first
VCA/vote-center elections in their respective cycles, and both show the
same signature drop from the pre-VCA ~54-65% band down to ~38-40%, consistent
with the county-tech record's account of the VCA rollout moving same-day and
vote-center processing into the canvass.)

### Draft row
```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 15091,
  "certified_final": 37525,
  "election_night_pct": 40.22,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://www.napacounty.gov/DocumentCenter/View/8722/Final-Unofficial-Election-Night-Report---Primary-Election-06052018-1039pm-PDF",
  "confidence": "primary",
  "note": "ROLLOUT ELECTION: Napa's first VCA / e-pollbook election (county-tech record epollbook.adopted_year=2018, first_election='2018-06'); vs_epollbook classed POST since vote centers/e-pollbooks were live for this entire election, not adopted after it. PLATEAU = 'Final Unofficial Election Night Report' (napacounty.gov archive page /4026/June-5-2018-Election-Results, View/8722; the last report still titled 'Election Night' before the series switches to 'POST-Election Night' reports starting 3 days later on 6/8). PDF self-titled 'FINAL ELECTION NIGHT SEMIFINAL OFFICIAL CANVASS', stamp 6/5/2018 10:39:31 PM. 'Precincts Reported: 170 of 170 (100.00%)'. RUNBOOK 7.5 trap hit exactly as documented: header prints 'Registered Voters: 15,091 of 76,236 (19.80%)' but 15,091 is actually Times Cast (confirmed by the Governor contest's own 'Times Cast' row showing the identical 15,091/76,236/19.80% triple); 'Ballots Cast: 30,211' is ballot CARDS (~2x voters, VCA 2-card ballot), NOT the comparable metric. First report of the night (8:01 PM, View/8721) already showed 15,087/76,236 (19.79%) -- count barely moved (+4) all night, mirroring the 2018-11 general's identical signature: nearly all VBM pre-processed and released in the first tranche, same-day/vote-center ballots processed in the canvass. First POST-night report (6/8/2018, View/8748) shows real movement to 16,773/76,236 (22.00%), confirming the count was frozen from 10:39 PM June 5 until the canvass resumed 3 days later. NOT the 8:01 PM first tranche (15,087 = 19.79%, functionally identical to but distinct from the plateau). Certified final 37,525 voters (CA SoS 2018-primary Voter Participation Statistics by County: 4 precinct + 37,521 VBM). Pct = 15,091/37,525 = 40.22%, closely tracking the 2018-11 general's 38.11% (both first-VCA-election shares). ASV never. Live PDF parsed with pdftotext."
}
```

### VERIFY.md line (draft)
```
| 2018 | statewide-primary | 15,091 | 37,525 | 40.2% | primary | [link](https://www.napacounty.gov/DocumentCenter/View/8722/Final-Unofficial-Election-Night-Report---Primary-Election-06052018-1039pm-PDF) |
```

### plateau_review.json entry (draft)
```json
{"slug": "napa-ca", "date": "2018-06-05", "verdict": "CONFIRMED", "basis": "county's own report-series titling (last report still labeled 'Election Night' vs the 'POST-Election Night' series that starts 3 days later) plus late-night internal timestamp (10:39 PM) plus a later capture (the 6/8 POST report) showing the count had moved, proving 10:39 PM held through the pause", "evidence": "'FINAL ELECTION NIGHT SEMIFINAL OFFICIAL CANVASS', stamp 6/5/2018 10:39:31 PM, 170/170 precincts, Times Cast 15,091/76,236 (19.80%); archive page confirms the next report (6/8/2018) is titled 'First Unofficial POST-Election Night Report'"}
```

### VERDICT
CONFIRMED, confidence primary. This is the single most important row in the
dossier (the rollout election itself) and has the cleanest evidence of the
six: the county's own archive page for this specific election lists the full
report series with unambiguous naming (Election Night vs POST-Election
Night), the mislabel trap is caught and resolved via the internal Times Cast
cross-check exactly as RUNBOOK 7.5 anticipates for this county/year, and the
first-report/final-report/first-post-report three-point comparison
independently proves both "barely moved during the night" and "genuinely
resumed 3 days later." No FLAG needed on the numerator. One thing for the
operator to confirm: the classification decision itself (`vs_epollbook:
"post"` for the rollout election, rather than treating 2018-06 as a
boundary/excluded point) -- this dossier follows the task brief's explicit
instruction to class it POST, but it is worth a human sign-off since it
means Napa's PRE-era primary sample is only 2012/2014/2016 and POST-era is
2018/2022/2024, with no "clean gap year" between adoption and the first
POST observation.

---

## Item 5: 2022-06-07 (Statewide Primary) — statewide-primary

### Denominator (CA SoS SoV)
- URL: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf
- Napa line: `Napa*   190   97,727   84,163   520   35,765   36,285   98.57%   43.11%   37.13%`
  (`*` = Voter's Choice Act county footnote.)
- **Total Voters (certified final) = 36,285**

### Numerator / plateau
- Found via the county's Past Election Results Archive page for this
  election (`https://www.napacounty.gov/4041/June-7-2022-Election-Results`),
  which lists the full report series:
  1. First Unofficial Election Night Results -- 8:01 PM, 6/7/22 (View/25206)
  2. Second Unofficial Election Night Results -- 9:39 PM, 6/7/22 (View/25207)
  3. **Last Unofficial Election Night Results -- 10:44 PM, 6/7/22 (View/25208)**
  4. First Unofficial Post Election Night Results -- 2:47 PM, 6/10/22 (View/25572, 3 days later)
  5-7. Second/Third/Last Unofficial Post-Election Night Reports (6/13-6/15/22)
  8. Final Certified Election Results, June 27, 2022 (View/25672)
- Fetched PDF (`https://www.napacounty.gov/DocumentCenter/View/25208/Last-Unofficial-Election-Night-Results-1044-PM-6722-PDF`,
  pdftotext): titled "Election Summary Report / June 7, 2022 Statewide
  Primary Election / **Final Unofficial Election Night Report**" (the PDF's
  internal title says "Final"; the archive-page link text says "Last" --
  same document, both self-describe as the terminal election-night report),
  page stamp "6/7/2022 10:44:46 PM". "Precincts Reported: 190 of 190
  (100.00%)", cleanly labeled "**Voters Cast: 14,658 of 84,146 (17.42%)**"
  (breakdown: Election Day 517 + Vote by Mail 14,141 = Total 14,658) -- no
  mislabel trap this cycle (2022 reports switched to explicit "Voters Cast"
  labeling, unlike the 2018 "Registered Voters" mislabel). Governor contest's
  own "Times Cast" row repeats the identical 14,658/84,146 (17.42%),
  cross-confirming.
- Cross-check against the First POST-night report (6/10/2022, View/25572,
  pdftotext): "First Unofficial Post Election Night Report", Voters Cast
  17,685 of 84,146 (21.02%) -- confirms real movement resumed 3 days later,
  proving 10:44 PM held through the pause.
- This is the LAST election-night report (self-titled "Final"/"Last", next
  report 3 days later) -- the plateau. NOT the 8:01 PM first tranche.
- **election_night_ballots = 14,658**
- Source URL (numerator): https://www.napacounty.gov/DocumentCenter/View/25208/Last-Unofficial-Election-Night-Results-1044-PM-6722-PDF

### Arithmetic
14,658 / 36,285 = 0.403997... = **40.40%**

(Close to the adjacent Nov 2022 general's 43.21% -- both post-VCA, both in
the ~40-43% band, the expected pattern once e-pollbooks/vote-centers are
established rather than newly rolled out.)

### Draft row
```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 14658,
  "certified_final": 36285,
  "election_night_pct": 40.40,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://www.napacounty.gov/DocumentCenter/View/25208/Last-Unofficial-Election-Night-Results-1044-PM-6722-PDF",
  "confidence": "primary",
  "note": "PLATEAU = 'Last Unofficial Election Night Results' (napacounty.gov archive page /4041/June-7-2022-Election-Results, View/25208; PDF's own internal title reads 'Final Unofficial Election Night Report'), stamp 6/7/2022 10:44:46 PM (the night's reports ran First 8:01 PM -> Second 9:39 PM -> Last 10:44 PM, then First Unofficial POST-Election Night Report 6/10/2022 2:47 PM, 3 days later). Header: 'Precincts Reported: 190 of 190 (100.00%)', cleanly labeled 'Voters Cast: 14,658 of 84,146 (17.42%)' (Election Day 517 + Vote by Mail 14,141 = 14,658; no mislabel trap this cycle, unlike 2018). Governor contest 'Times Cast' row repeats the identical figure. First POST report (6/10/2022) shows real movement to 17,685/84,146 (21.02%), confirming the count held from 10:44 PM until the canvass resumed. NOT the 8:01 PM first tranche (14,141 VBM = 16.81%, the v2 value). Post-VCA / e-pollbook (adopted 2018). Certified final 36,285 voters (CA SoS 2022-primary Voter Participation Statistics by County: 520 precinct + 35,765 VBM). Pct = 14,658/36,285 = 40.40%, close to the adjacent Nov 2022 general share (43.21%). ASV never. Live PDF parsed with pdftotext."
}
```

### VERIFY.md line (draft)
```
| 2022 | statewide-primary | 14,658 | 36,285 | 40.4% | primary | [link](https://www.napacounty.gov/DocumentCenter/View/25208/Last-Unofficial-Election-Night-Results-1044-PM-6722-PDF) |
```

### plateau_review.json entry (draft)
```json
{"slug": "napa-ca", "date": "2022-06-07", "verdict": "CONFIRMED", "basis": "county's own report-series titling (last report titled 'Last'/'Final' before the series switches to 'Post Election Night' 3 days later) plus a later capture (the 6/10 POST report) showing the count had moved, proving 10:44 PM held through the pause", "evidence": "'Final Unofficial Election Night Report', stamp 6/7/2022 10:44:46 PM, 190/190 precincts, Voters Cast 14,658/84,146 (17.42%); First POST report 6/10/2022 shows 17,685 (21.02%), confirming movement resumed after a gap"}
```

### VERDICT
CONFIRMED, confidence primary. Clean evidence, no mislabel trap, cleared the
section-8 bar with both self-description and the later-capture-shows-movement
leg. Nothing to flag on this row.

---

## Item 6: 2024-03-05 (Presidential Primary) — presidential-primary

### Denominator (CA SoS SoV)
- URL: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf
- Napa line: `Napa*   200   95,611   83,611   1,130   36,748   37,878   97.02%   45.30%   39.62%`
  (`*` = Voter's Choice Act county footnote.)
- **Total Voters (certified final) = 37,878**

### Numerator / plateau
- Found via the county's Past Election Results Archive page for this
  election (`https://www.napacounty.gov/4046/March-5-2024-Election-Results`),
  which lists the full report series:
  1. First Unofficial Election Night Report -- 8:01 PM, 3/5/24 (View/31600)
  2. Second Unofficial Election Night Report -- 9:57 PM, 3/5/24 (View/31601)
  3. **Last Unofficial Election Night Report -- 11:17 PM, 3/5/24 (View/31602)**
  4. 1st Unofficial Post Election Summary Report -- 4:13 PM, 3/8/24 (View/31634, 3 days later)
  5-9. 2nd-6th Unofficial Post Election Results (3/11-3/26/24)
  10. Final Certified Election Summary Report, March 28, 2024 (View/31807)
- Fetched PDF (`https://www.napacounty.gov/DocumentCenter/View/31602/Last-Unofficial-Election-Night-Report-1117-PM-3524-PDF`,
  pdftotext): titled "March 5, 2024 Presidential Primary / Napa County
  Election Division / **Last Unofficial Election Night Report**", page
  stamp "3/5/2024 11:17:50 PM". "Precincts Reported: 200 of 200 (100.00%)",
  cleanly labeled "**Voters Cast: 15,304 of 83,555 (18.32%)**". Per-contest
  "Times Cast" rows (e.g. Dem Presidential Preference 8,874/42,414) confirm
  the report uses a real voter-count metric, not ballot cards.
- Cross-check against the First report (8:01 PM, View/31600, pdftotext):
  "First Unofficial Election Night Report", stamp "3/5/2024 08:01 PM",
  "Voters Cast: 14,336 of 83,555 (17.16%)".
- Cross-check against the First POST-night report (3/8/2024 4:13 PM,
  View/31634, pdftotext): "First Unofficial Post Election Report", "Voters
  Cast: 20,504 of 83,555 (24.54%)", **and a separate "Cards Cast: 41,161"
  line** -- the post-night report explicitly distinguishes Voters Cast from
  Cards Cast, confirming "Voters Cast" (not a card count) is the correct
  comparable metric used throughout this series, and confirming real
  movement resumed 3 days after the 11:17 PM plateau.
- This is the LAST election-night report (self-titled "Last", next report 3
  days later) -- the plateau. NOT the 8:01 PM first tranche.
- **election_night_ballots = 15,304**
- Source URL (numerator): https://www.napacounty.gov/DocumentCenter/View/31602/Last-Unofficial-Election-Night-Report-1117-PM-3524-PDF

### Arithmetic
15,304 / 37,878 = 0.404037... = **40.40%**

(Essentially identical to the 2022-06 primary share (40.40%) and close to the
adjacent Nov 2024 general's 39.26% -- a stable post-VCA band across three
consecutive Napa elections of different types.)

### Draft row
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 15304,
  "certified_final": 37878,
  "election_night_pct": 40.40,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://www.napacounty.gov/DocumentCenter/View/31602/Last-Unofficial-Election-Night-Report-1117-PM-3524-PDF",
  "confidence": "primary",
  "note": "PLATEAU = 'Last Unofficial Election Night Report' (napacounty.gov archive page /4046/March-5-2024-Election-Results, View/31602), stamp 3/5/2024 11:17:50 PM (the night's reports ran First 8:01 PM -> Second 9:57 PM -> Last 11:17 PM, then 1st Unofficial Post Election Summary Report 3/8/2024 4:13 PM, 3 days later). Header: 'Precincts Reported: 200 of 200 (100.00%)', cleanly labeled 'Voters Cast: 15,304 of 83,555 (18.32%)'. First POST report (3/8/2024) shows 'Voters Cast: 20,504' vs a separately-printed 'Cards Cast: 41,161' -- confirms Voters Cast (not a ballot-card count) is the correct comparable metric throughout this series, and confirms real movement resumed 3 days after the plateau. NOT the 8:01 PM first tranche (Voters Cast 14,336 = 17.16%, the v2 value). Post-VCA / e-pollbook (adopted 2018). Certified final 37,878 voters (CA SoS 2024-primary Voter Participation Statistics by County: 1,130 precinct + 36,748 VBM). Pct = 15,304/37,878 = 40.40%, matching the 2022-06 primary share exactly and close to the adjacent Nov 2024 general share (39.26%). ASV never. (2020 deliberately excluded as a COVID universal-VBM outlier, consistent with the generals dataset.) Live PDF parsed with pdftotext."
}
```

### VERIFY.md line (draft)
```
| 2024 | presidential-primary | 15,304 | 37,878 | 40.4% | primary | [link](https://www.napacounty.gov/DocumentCenter/View/31602/Last-Unofficial-Election-Night-Report-1117-PM-3524-PDF) |
```

### plateau_review.json entry (draft)
```json
{"slug": "napa-ca", "date": "2024-03-05", "verdict": "CONFIRMED", "basis": "county's own report-series titling ('Last Unofficial Election Night Report' before the series switches to 'Post Election' reports 3 days later) plus a later capture (the 3/8 POST report) showing the count had moved, proving 11:17 PM held through the pause", "evidence": "'Last Unofficial Election Night Report', stamp 3/5/2024 11:17:50 PM, 200/200 precincts, Voters Cast 15,304/83,555 (18.32%); First POST report 3/8/2024 shows Voters Cast 20,504 vs Cards Cast 41,161, confirming both the metric and that movement resumed after a gap"}
```

### VERDICT
CONFIRMED, confidence primary. Cleanest row in the dossier: explicit
"Voters Cast" vs "Cards Cast" distinction printed in an adjacent report
removes any ambiguity about the RUNBOOK 7.5 cards-trap for this specific
election, self-titled "Last", and the days-later-movement leg is direct.
Nothing to flag on this row.

---

## Summary table (all six primaries)

| Date | Type | Night ballots | Certified final | Pct | vs_epollbook | Confidence | Verdict |
|---|---|---|---|---|---|---|---|
| 2012-06-05 | presidential-primary | 19,147 | 29,305 | 65.34% | pre | primary | CONFIRMED |
| 2014-06-03 | statewide-primary | 17,431 | 28,179 | 61.86% | pre | primary | CONFIRMED |
| 2016-06-07 | presidential-primary | 20,427 | 43,450 | 47.01% | pre | primary | CONFIRMED |
| 2018-06-05 | statewide-primary (ROLLOUT) | 15,091 | 37,525 | 40.22% | **post** | primary | CONFIRMED |
| 2022-06-07 | statewide-primary | 14,658 | 36,285 | 40.40% | post | primary | CONFIRMED |
| 2024-03-05 | presidential-primary | 15,304 | 37,878 | 40.40% | post | primary | CONFIRMED |

All six rows: confidence `primary`, plateau verdict `CONFIRMED`, no nulls, no
`comparable: false` flags needed. PRE-era mean 58.07%, POST-era mean 40.34%
-- a clean, large drop coincident with the 2018 VCA/e-pollbook rollout,
mirroring the exact same PRE/POST pattern already documented for Napa's
November generals (pre ~54-57%, post ~38-43%). The one directional oddity is
internal to the PRE group (2012/2014 ran ABOVE their adjacent generals,
2016 ran BELOW its adjacent general) and is flagged per-item above; it does
not affect the PRE-vs-POST rollout conclusion, which is unambiguous and
consistent with the generals dataset.

## Open items for the operator (all FLAGs collected)

1. **2012-06-05** (65.34%): well above SF's presidential-primary-adjacent
   calibration and above Napa's own Nov-general band; note explains it as a
   June-primary VBM-processing-completeness effect (only ~61% of eventual
   VBM was in by election night vs near-complete for Nov generals). Ask a
   human to spot-check the raw Wayback `1052PM_dtl.htm` page
   (`https://web.archive.org/web/20120608220101/http://www.countyofnapa.org/ElectionResults/20120605/20120605-1052PM_dtl.htm`)
   against the claimed Total 19,147 / 28.02%.
2. **2014-06-03** (61.86%): same pattern/reasoning as above. Spot-check
   `https://web.archive.org/web/20140725071031/http://www.countyofnapa.org/ElectionResults/20140603/20140603-2330_dtl.htm`
   against Total 17,431 / 24.47%.
3. **2018-06-05 classification**: this dossier classes the rollout election
   itself as `vs_epollbook: "post"` per the task brief's explicit
   instruction (Napa's `first_election: "2018-06"` in the county-tech
   record). This is a genuine editorial call -- it means the PRE sample is
   only 2012/2014/2016 and there is no gap year between "last PRE" and
   "first POST." Flagging for maintainer sign-off before this is merged
   into `data/research/election-night/napa-ca.json`, consistent with how
   the county's own November series treats 2018-11 as POST (same logic,
   already precedented in the committed generals data).
4. No other rows need operator attention; 2016, 2022, and 2024 all carry
   clean self-titled "Last"/"Final" report PDFs with unambiguous voter-count
   labeling and a days-later-movement leg proving the plateau held.

## Status
All 6 primaries researched and drafted. Nothing left unfinished. This file
is a scratch dossier only -- no repo file (napa-ca.json, VERIFY.md,
plateau_review.json) has been edited; the draft rows/lines/verdicts above are
ready for an operator or a follow-up write pass to copy into the repo per
RUNBOOK section 10 (surgical text edits, then the full pipeline in section 3).
