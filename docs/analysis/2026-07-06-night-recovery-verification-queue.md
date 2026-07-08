# Night-recovery verification queue (2026-07-06 session)

Load-bearing digits from the July 2026 recovery of the post-1965 missing
night counts, queued for the operator's hand-read. Every value below was
machine-read from a scan, re-read at high zoom, and gate-checked; the
operator's reading wins. Scan paths are relative to the MAIN checkout
(`/Users/sbuss/workspace/sf-election-count/`), all gitignored under
`mirror/newsbank/scans/`.

Threshold column: what the digit gates. If a hand-read moves a value past
its threshold, the row's ingestion decision must be revisited (correct
`data/sf_archival_canvass_points.csv` and rebuild per the
always-use-real-data rule).

## Ingested values (verify these first)

| Election | Claimed value | What it is | Scan | Threshold / gate | Confidence |
|---|---|---|---|---|---|
| 1971-11-02 | 258,164 | election-night total, quoted in canvass story | sweep_19711102_issue19711123_p4_s2.png | must be ≤ certified 258,227 | high |
| 1971-11-02 | 258,227 | official canvass total (certified) | sweep_19711102_issue19711123_p4_s2.png | denominator for both 1971 rows | high |
| 1966-11-08 | 157,821 + 109,426 = 267,247 | Governor sum, 1344/1344 | sweep_19661108_issue19661109_p4_s0.png | ≤ certified 286,049; sets 93.4% night | high |
| 1970-11-03 | 136,028 + 102,571 + 4,044 + 2,854 = 245,497 | Governor sum, 1331/1350 | sweep_19701103_issue19701104_p2_s0.png (zooms zoom_gov_*.png) | ≤ certified 262,398; sets 93.6% night | high |
| 1970-06-02 | 108,659 | printed "Total voters reported", 603/1208 | sweep_19700602_issue19700603_p3_s0.png (crop_19700602_p3s0_tally_flat.png) | ≤ certified 214,943; dimmed partial | high |
| 1970-06-02 | 214,637 | printed "Total voters reported", 1208/1208 | sweep_19700602_issue19700604_p2_s0.png | ≤ certified 214,943 (306 under) | high |
| 1970-11-03 | 140,327 + 106,706 + 4,078 + 2,927 = 254,038 | Governor sum, 1350/1350 (day 2) | sweep_19701103_issue19701105_p10_s0.png/_s1.png | ≤ certified 262,398; cross-checked against same-page county table | high |
| 1974-11-05 | 228,265 | printed turnout line "228,265 out of 369,005" | sweep_19741105_issue19741107_p9_s1.png | ≤ certified 228,586 (321 under) | high |
| 1974-11-05 | 169,752 | Governor sum, 775/1359 (night partial) | sweep_19741105_issue19741106_p5_s1.png | ≤ certified; dimmed | high |
| 1980-08-19 | 140,514 | printed "only 140,514 voters went to the polls", 100% tallied | sweep_19800819_issue19800820_p1_s2.png/_s3.png | ≤ certified 140,551 (37 under); sets 100.0% night | high |
| 1980-06-03 | 37,691 + 93,633 = 131,324 | Prop 9 SF sum, 70% precincts (night partial) | sweep_19800603_issue19800604_p2_s2.png/_s3.png | ≤ certified 206,366; dimmed | high |
| 1980-06-03 | 69,628 + 102,007 = 171,635 | Prop V sum, 100% precincts (day 2) | sweep_19800603_issue19800605_p5_s0.png | ≤ certified 206,366 | high |
| 1976-06-08 | 78,324 + 77,890 = 156,214 | Prop 15 sum, E+1 box (night partial) | tbl_19760608_issue19760609_p1.png | ≤ certified 208,884; dimmed | high |
| 1976-06-08 | header "26.1 per cent of 942 precincts" | box header, judged a TYPESETTING ERROR for ~76.1 (table sums run 70-82% of complete) | crop_1976_pct_header.png | affects the header note only, not the sum | verified crop; judgment documented |
| 1976-06-08 | 95,823 + 95,200 = 191,023 | Prop 15 sum, 942/942 (day 2) | sweep_19760608_issue19760610_p10_s1.png (crop_prop15_1976.png) | ≤ certified; 661 below in-person floor, no floor claimed | high |
| 1977-08-02 | 62,185 + 112,123 = 174,308 | Prop B per-district sum incl. absentee (day 2) | sweep_19770802_issue19770804_p2_s0.png/_s1.png | ≤ certified 178,367; beats floor 161,622 | high |
| 1972-06-06 | "64 per cent of the city's 368,357 registered voters" | turnout prose on complete count; ingested rounding-safe as 233,906 | flip_19720606_issue19720609_p12.png (label off by one; masthead June 8) | 63.5% band floor ≤ certified 234,840 | high |
| 1984-06-05 | 81,436 + 73,756 = 155,192 | Prop B sum, 708/708 (day 2) | final_19840605_issue19840607_p20_s1_cityprop.png | ≤ certified 180,741; beats floor 151,013 | high |
| 2008-04-08 | "About 17,000 ballots were cast in San Francisco" | SF-only night prose, all SF precincts reporting; ingested rounding-safe as 16,500 | NewsBank text doc, docref 11FF1C4B48B28060 (mirror/newsbank/docs/) | ≤ certified 19,742; sets 83.6% night | medium (approximate printed figure) |
| 1968-06-04 | 77,906 + 34,562 = 112,468 | Prop A sum, no precinct basis (night partial, debacle night) | sweep_19680604_issue19680605_p1_s2.png | ≤ certified 254,825; dimmed | medium (no precinct basis) |
| 1966-06-07 | 58,194 + 88,302 = 146,496 | city Prop A sum, 1342/1344 (undervote-limited, dimmed) | sweep_19660607_issue19660608_p3_s0.png/_s2.png | ≤ certified 226,622 | high |

## Not ingested, awaiting operator action

| Election | Value | Status | Scan / source |
|---|---|---|---|
| 1967-11-07 | Mayor 18-candidate night sum 242,170 at 1341/1341 (pre-absentee); absentee-inclusive top 3: 109,982 / 94,089 / 40,996 | held: no certified denominator; SFPL History Center "Statement of Vote 1906-1979" volume has it | sweep_19671107_issue19671108_p1_s3.png, sweep_19671107_issue19671109_p1_s3.png |
| 1969-11-04 | Prop B night sum 95,252 + 86,985 = 182,237 at 1200/1204; complete machine count 199,488 | held: no certified denominator; same SFPL volume; DOE open-data certified Prop B 183,148 already validates the night read | sweep_19691104_issue19691105_p3_s0.png, sweep_19691104_issue19691106_p1_s2.png |
| 1968-06-04 | completed unofficial count 262,449 (exceeds SOV certified 254,825) | open discrepancy, registered in docs/doe-data-discrepancies.md; the SFPL volume should arbitrate | sweep_19680604_issue19680607_p30_s0.png |
| 1971-11-02 | Feinstein night figure 53,941 (p1A tally) vs 53,911 (front-page box) | 30-vote edition discrepancy, moot for ingestion (floor is the prose 258,164) but note for the record | sweep_19711102_issue19711103_p2_s0.png vs _p1_s1.png |

## One operator errand closes the rest

UPDATE 2026-07-07: 1967-11 and 1969-11 are RESOLVED without the library
trip; the ProQuest Examiner printed both certified totals (see the search
log). The 1971-11 rows in the held table above are likewise resolved (the
canvass story supplied everything). The SF History Center's "Statement of
Vote 1906-1979" volumes now serve one purpose: arbitrating the June 1968
three-way discrepancy (SOV 254,825 vs Chronicle unofficial complete
262,449). Also verify the 1967 certified read (Examiner docview
2164093541, full-field Mayor sum 249,831) and the 1969 one (docview
2196968259, total 199,200) if you're in ProQuest anyway.

## Overnight additions (2026-07-07, the CDNC campaign)

CDNC items are text-OCR reads; to hand-verify, open the cited section on
cdnc.ucr.edu (issue code in the citation) and read the page image.

| Election | Claimed value | What to check | Where | Priority |
|---|---|---|---|---|
| 1899-11-07 | RESOLVED (operator hand-read of the page image, 2026-07-07): Davis 14,690 and Phelan 19,907 (the OCR had garbled Davis entirely and dropped Phelan's final digit to 19,901). Full Mayor sum 35,055; night floor lifted from 20,248 (39.0) to 35,055 (67.5), the biggest single improvement of the campaign. Page image screenshot saved: mirror/cdnc/SFC18991108/shot_section_2.2.2_thecount.png (captured via the raw-CDP recipe with the tab briefly foregrounded; Veridian's canvas tiles do not paint in a background tab) | SFC18991108 p1 'THE COUNT.' | done |
| 1906-11-06 | RESOLVED (operator hand-read, 2026-07-07): the body line also reads 38,802; the OCR's 38,302 was an artifact and no discrepancy exists. The consistent printed total 38,802 exceeds certified 38,564 by 238, so it remains logged-never-ingested per the above-certified rule and the Governor-sum night floor 37,287 (96.7) stands; the adjacent printed 'Total 51,633' matches certified registration exactly | SFC19061107 section 2.10.5 | done |
| 1899-12-27 | total 29,938 vs component arithmetic 29,958 | a 3/5 digit; both pass the gate; lower ingested | SFC18991228 section 2.5.2 | low |
| 1896-11-03 | RESOLVED (operator hand-read of vol47_n320.jpg, 2026-07-07): the crisp printing reads 64,820, confirming the arbitration (the 61,820 variant was refuted by the SOV elector-sum proof). Operator also noted the vol47 cumulative Registrar table extends back to 1878, a possible denominator source for pre-1891 elections | mirror/muni_reports/vol47_n320.jpg | done |
| 1888-11-06 | RESOLVED (operator hand-read, 2026-07-07): Curtis (American, running for President not Mayor) polled 14; the OCR had also misread Harrison (24,980, not 24,950). Presidential sum corrected to 52,960, and the operator's read of the Mayor column (Pond 20,211 + O'Donnell 15,219 + Story 18,671 = 54,101) supplied a larger same-day floor, so the day-3 row moves 52,916 to 54,101 (95.7 to 97.8) | DAC18881109 section 2.3 | done |
| 1884-11-04 | third column (528) party identity: Butler vs St. John | affects labeling only, not the 40,200 sum | DAC18841107 section 2.2.3 | low |
| 1902-12-02 | printed 26,615 exceeds certified 26,612 by 3 | consistent with the 161 rejected ballots reclassified at canvass; For+Against 26,454 ingested | SFC19021203 section 2.128 | low |
| 1905-11-07 | RESOLVED (operator judgment, 2026-07-07): the printed 'Total vote cast 71,033' is PROMOTED to the denominator over the Municipal Reports rounded fire-era estimate of 72,000 (the operator read the page image; the internal plurality cross-check is exact and 72,000 reads as a rounding of this count). Night share becomes 100.0 by identity; the turnout row now carries 71,033 with the promotion disclosed in both citations | report .superpowers/sdd/cdnc-1905-11-report.md; screenshot mirror/cdnc/SFC19051108/shot_section_2.2.3_schmitz_lead.png | done |
| 1899-12-29 | SUPERSEDED: the CDNC table stayed unreadable but the election was recovered anyway via the ProQuest Examiner (Dec 30 1899 p1 'THE VOTE' table, docview 2132356675, night 22,322 of certified 22,331, ingested at 100.0); screenshots mirror/examiner/1899-12-30/docview_2132356675_p1_s*.png if a spot-check is ever wanted | SFC18991230 section 2.4.2 (dead end, documented) | done |

## Resumable ProQuest queue (1999-11-02, blocked by the returning captcha)

Six KWIC-located Examiner docviews await page-image reads once the robot
wall cools (it now retriggers after a handful of loads even at 27-second
pacing; consider resuming tomorrow, or reading these by hand in ProQuest):
2206373293 (Nov 5 p22, an itemized status box, highest value), 2206796248
(Nov 4 p16, count-completion estimate), 2206420897 and 2206420136 (Nov 3,
registrar spokesperson on the write-in backlog), 2206377576 (Nov 5 p18,
Friday updated numbers), 2206795946 (Nov 4 p30). The 2003-12-09 runoff
was not searched at all before the block: virgin territory for the next
run. Method notes in the session's examiner-1999-2003 report.

## Judgment items from the alt-web hunt (2026-07-07)

| Election | Item | Question | Where |
|---|---|---|---|
| 2011-11-08 | RESOLVED: the ratio derivation is refuted; the Examiner's day-2 full-field first-choice table (154,942, docview 2069597521) is below the ratio-implied night range, so the liveblog percentages were mis-based; the dim top-3 night floor stands | settled 2026-07-07 |
| 2013-11-05 | RESOLVED: the Examiner's direct night count ('just more than 95,000 counted by 10:30 p.m.', docview 2069644090) confirms the SFist figure was the counted state and supersedes it; night point 73.7 ingested | settled 2026-07-07 |
| 2000-12-12 | LAT-via-Usenet 8,000-remaining conversion (ingested, 93.8) | optional: confirm the sentence against the LA Times archive directly | groups.google.com/g/ba.politics/c/Y8S4VZY1-Ng |
| 2000-12-12 | RESOLVED (operator hand-read, 2026-07-07): the operator opened docview 2206415258 (page A6 of the Dec 13 Examiner) and read the sentence in context: 'By 8:30 p.m., when election officials released the first absentee ballot results, it was clear that District 6 winner Chris Daly had trounced rival Chris Dittenhafer. With 38,445 ballots counted, Daly had won 76 percent to Dittenhafer's 23 percent.' The 38,445 is the citywide first absentee release (the 76/23 is the D6 split within it); a D6-only reading is also arithmetically impossible (nine runoff districts averaged about 14,400 certified ballots). The same page's 'Supervisors' runoff race: 86 percent reporting' sidebar independently confirms exactly nine districts ran runoffs (2 and 9 absent). Row stands as ingested (29.7, night_partial). Full-page screenshot saved: mirror/examiner/2000-12-12/dv2206415258_dec13_pA6_fullpage.png. Note for future capture agents: the docview's page image lazy-loads and the viewport can open mid-page; the earlier 'wrong page' scare was the bottom half of the same A6 | ProQuest docview 2206415258 |
| 2003-12-09 | RESOLVED both ways (operator, 2026-07-07). (a) The 246,667 night reading is REFUTED by official Statement of Vote arithmetic the operator supplied: 91,119 total absentee ballots and 253,872 total cast mean e-day was about 162,700, so a night-of 246,667 would require roughly 84,000 of the 91,119 absentees counted by Tuesday night, inconsistent with the night state the same paper printed the next morning (mayor-race sum 225,681) and with the days of counting that followed (234,627 Wednesday afternoon, 247,890 Friday); the day-3 stamp on that row stands. (b) The TRUE night point was hiding in plain sight: the operator located the Examiner's Dec 10 morning front page (docview 2206456902), whose results boxes print Newsom 118,651 / Gonzalez 107,030 (sum 225,681), identical to the AP 'with all precincts reporting' figures we had conservatively stamped Dec-11 08:00. The DailyKos-documented DOE liveblog (562/562 precincts by about 2:48am PT) dates the all-precincts state to about 03:00, inside the E+1 06:00 night window regardless of the paper's press schedule, so the AP row is re-stamped to 2003-12-10T03:00 and 2003-12-09 becomes a night count: 88.9 percent, night_partial (contest-sum floor). Screenshots mirror/examiner/2003-12/dv2206456902_dec10_s*.png and dv2206312937_dec12_p11_s*.png | ProQuest docviews 2206456902, 2206312937 |

## Resumable ProQuest queue #2: EXECUTED (2026-07-07, fast attended pass)

All five elections in this queue were swept the same day (see the
examiner-runoffs session report, 'fast attended pass'): 2003-12-09
ingested (day-1 race total 234,627 and the day-3 editorial 246,667, with
its night reading in the judgment table above); 2002-12-10 ingested
(night-partial 15,022 from the results-board photograph plus day-1
33,308); 2014-06-03 ingested (night 90,262 plus day-6 106,171);
2001-12-11 dry beyond the existing 70,244 floor (a near-ceiling
percentage derivation was logged, not ingested); 2009-05-19 dry (wire
coverage only). Do not re-run these searches; the exact queries and
their outcomes are in the session report.
