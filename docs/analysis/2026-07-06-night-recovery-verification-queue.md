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

The SF History Center (Main Library, 6th floor) holds the city's own
"Statement of Vote" volumes for Nov 7 1967, Nov 4 1969, and Nov 2 1971
(finding aid: sfpl.org, "Statement of Vote 1906-1979"; in-library use).
Certified totals from those volumes unlock the two held elections above
and arbitrate the 1968-06 discrepancy.

## Overnight additions (2026-07-07, the CDNC campaign)

CDNC items are text-OCR reads; to hand-verify, open the cited section on
cdnc.ucr.edu (issue code in the citation) and read the page image.

| Election | Claimed value | What to check | Where | Priority |
|---|---|---|---|---|
| 1899-11-07 | Davis E+1 figure, OCR-garbled, prose implies about 14,676 | one digit string on the 2:15am table; a confirmed read lifts the night floor from 20,248 (39.0) to about 34,900 (67) | SFC18991108 p1 'THE COUNT.' | HIGH (biggest single improvement available) |
| 1906-11-06 | grand total prints 38,802 (headline) vs 38,302 (body line) | which is the true printed total; neither is ingested (Governor sum 37,287 is the floor) | SFC19061107 section 2.10.5 | medium |
| 1899-12-27 | total 29,938 vs component arithmetic 29,958 | a 3/5 digit; both pass the gate; lower ingested | SFC18991228 section 2.5.2 | low |
| 1896-11-03 | ballots corrected 61,820 to 64,820 | spot-check mirror/muni_reports/vol47_n320.jpg (crisp) and the SOV elector pages | evidence saved | medium |
| 1888-11-06 | Curtis (American) day-3 figure illegible, excluded | if readable on the page image, add to the 52,916 sum | DAC18881109 section 2.3 | low |
| 1884-11-04 | third column (528) party identity: Butler vs St. John | affects labeling only, not the 40,200 sum | DAC18841107 section 2.2.3 | low |
| 1902-12-02 | printed 26,615 exceeds certified 26,612 by 3 | consistent with the 161 rejected ballots reclassified at canvass; For+Against 26,454 ingested | SFC19021203 section 2.128 | low |
| 1905-11-07 | promotion question: printed 71,033 vs official rounded 72,000 denominator | if you judge the paper's precise figure the better denominator, the night share becomes 100.0 and the turnout row should change too | report .superpowers/sdd/cdnc-1905-11-report.md | judgment call |
| 1899-12-29 | dry: the only vote table's OCR fails the certified gate | needs a page-image read (CDNC viewer by hand or NewsBank) | SFC18991230 section 2.4.2 | medium |
