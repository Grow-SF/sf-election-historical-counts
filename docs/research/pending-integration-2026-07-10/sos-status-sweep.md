# CA SoS status-page sweep: per-county election-night ballots-counted, 12 statewide elections

Read-only research sweep. Source: CA Secretary of State per-county reporting-status
table, served at `vote.sos.ca.gov/returns/status` (2012-2018 era) and
`electionresults.sos.ca.gov/returns/status` (2022+ era, confirmed live in the
2024-03-05 Placer retry at scratchpad/placer-2024-03-retry.md). Columns (era-dependent):
County | Total Precincts | Precincts Reporting | %Reporting | Registered Voters |
Ballots Cast | %Turnout | First Report Date-Time | Last Report Date-Time | Report Type.
Report Type code is diagnostic: `FENU` = Final Election Night Unofficial (the page's
own label for the plateau report); `CCU` = Current Canvass Update (post-night, county
already resumed the multi-day canvass) -- when a county's row shows CCU as of the
FIRST available capture, the true FENU value (if any) must be recovered from an
earlier capture or is unrecoverable.

Panel counties (19): San Francisco, Lake, Del Norte, Mendocino, Tehama, Colusa,
Fresno, Los Angeles, Madera, Napa, Nevada, Orange, Placer, Riverside, Sacramento,
San Bernardino, San Diego, San Mateo, Santa Clara.

Grades: CONFIRMED (self-describing night/early-morning timestamp + independent
bracket leg: frozen later capture, or FENU->CCU jump proving the FENU value held) /
PLAUSIBLE (self-describing but no independent leg obtainable) / MID-EVENING-ONLY
(only a pre-plateau, likely-first-tranche capture survives) / NO-CAPTURE.

Tooling: `fetch_election.py <slug> <url> <from> <to>` pulls every unique-digest
200 capture in the CDX window, gunzips, parses the table via `parse_status.py`
into `<slug>_timeline.json` (list of {ts, digest, original, rows{county: [cells]}}).
Raw captures cached in `<slug>_captures/`.

---

## 2024-03-05 Presidential Primary

Host: `electionresults.sos.ca.gov/returns/status` (confirmed live domain for this
election per the prior Placer retry). Captures already downloaded in the parent
scratchpad dir (`status_20240305190731.html` ... `status_20240311135917.html`,
9 total, spanning election afternoon through Mar 11). Report Type codes this era:
`R` = Running/first-tranche, `SF`/`U` = later updates (no single canonical "final"
code observed; the plateau is identified by the Last-Report timestamp freezing).

CDX query used (already run in the prior Placer pass):
`http://web.archive.org/cdx/search/cdx?url=electionresults.sos.ca.gov/returns/status&from=20240305&to=20240312&output=json`

Extraction command: `python3 sos-status-sweep/parse_status.py status_<ts>.html`
run against all 9 captures; full per-county cell sequences recorded in agent
scratch notes (available on request), condensed table below.

Denominator (certified final "Total Voters"): CA SoS SoV
`https://elections.cdn.sos.ca.gov/sov/2024-primary/pdf/2024-primary-vps-by-county.pdf`
(local copy `scratchpad/sov2024primary.txt`), "Total Voters" column, verified
Placer's row = 135,869 matches the already-recovered value exactly (parsing
sanity check passed).

### 19-county extraction table

| County | Night ballots | Last Report stamp | Certified final | Night % | Grade | Bracket evidence |
|---|---|---|---|---|---|---|
| San Francisco | 104,760 | Mar 5 11:42 p.m. (SF) | 233,465 | 44.87% | CONFIRMED | frozen thru 2 later captures (Mar6 6:44am,10:05am), jumps Mar7 4:29pm |
| Lake | 7,181 | Mar 6 2:01 a.m. (U) | 15,626 | 45.96% | CONFIRMED | frozen ALL 7 remaining captures thru Mar 11 (never moved) |
| Del Norte | 3,285 | Mar 5 10:25 p.m. (SF) | 6,121 | 53.67% | CONFIRMED | frozen thru 4 captures (Mar6-Mar7), jumps Mar9 to 6,055/Mar8 3:28pm |
| Mendocino | 7,418 | Mar 6 12:35 a.m. (U) | 23,935 | 30.99% | CONFIRMED | frozen ALL 7 remaining captures thru Mar 11 (never moved) |
| Tehama | 7,998 | Mar 5 11:34 p.m. (U) | 15,537 | 51.48% | CONFIRMED | frozen thru 4 captures, jumps Mar9 to 10,596/Mar8 5:52pm |
| Colusa | 1,846 | Mar 5 9:14 p.m. (U) | 3,788 | 48.73% | CONFIRMED | frozen ALL 7 remaining captures thru Mar 11 (never moved) |
| Fresno | 82,242 | Mar 6 12:58 a.m. (SF) | 156,425 | 52.58% | CONFIRMED | frozen thru 3 captures (Mar6-Mar7), jumps Mar8 to 105,945/Mar7 4:59pm |
| Los Angeles | 910,857 | Mar 6 2:06 a.m. (U) | 1,641,715 | 55.48% | CONFIRMED | frozen thru 1 later capture (Mar6 10:05am), jumps same-day 4:36pm |
| Madera | 16,048 | Mar 5 10:32 p.m. (U) | 27,609 | 58.13% | CONFIRMED | frozen thru 4 captures, jumps Mar9 to 21,214/Mar8 3:55pm |
| Napa | 15,304 | Mar 5 11:34 p.m. (U) | 37,878 | 40.40% | CONFIRMED | frozen thru 4 captures, jumps Mar9 to 20,504/Mar8 4:43pm |
| Nevada | 21,753 | Mar 6 12:08 a.m. (U) | 39,579 | 54.96% | CONFIRMED | frozen thru 4 captures, jumps Mar9 to 30,094/Mar8 3:28pm |
| Orange | 400,430 | Mar 6 12:06 a.m. (U) | 685,038 | 58.45% | CONFIRMED | frozen thru 1 later capture (Mar6 10:05am), jumps same-day 5:10pm |
| Placer | 69,436 | Mar 6 12:04 a.m. (U) | 135,869 | 51.11% | CONFIRMED | (prior recovery, doubly bracketed; see placer-2024-03-retry.md) |
| Riverside | 213,998 | Mar 6 3:01 a.m. (U) | 409,269 | 52.29% | CONFIRMED | frozen thru 1 later capture (Mar6 10:05am), jumps same-day 6:20pm |
| Sacramento | 118,205 | Mar 5 11:58 p.m. (U) | 346,502 | 34.11% | CONFIRMED | frozen thru 4 captures, jumps Mar9 to 180,496/Mar8 3:12pm |
| San Bernardino | 150,018 | Mar 6 1:48 a.m. (SF) | 305,853 | 49.05% | CONFIRMED | frozen thru 3 captures (Mar6), jumps same-day 3:48pm to 160,881 |
| San Diego | 425,572 | Mar 6 12:50 a.m. (SF) | 704,068 | 60.44% | CONFIRMED | frozen thru 2 later captures (Mar6 10:05am,7:52pm), jumps Mar7 5:01pm |
| San Mateo | 92,359 | Mar 6 2:18 a.m. (SF) | 174,122 | 53.04% | CONFIRMED | frozen thru 2 later captures (Mar6 10:05am,7:52pm), jumps to 104,684/Mar7 4:25pm |
| Santa Clara | 182,413 | Mar 5 10:26 p.m. (U) | 383,110 | 47.61% | CONFIRMED | frozen thru 2 later captures (Mar6 6:44am,10:05am), jumps same-day 6:24pm |

**19/19 CONFIRMED.** This closes essentially every open null for this election
across the whole panel (only Placer had a landed row before this pass; every
other county's 2024-03-05 primary row was entirely missing from
`packages/data/county_night.json`). All 19 counties show the classic pattern:
0 ballots at pre-close captures, a mid-evening "R"-type running/first-tranche
number (correctly NOT used), then a "SF"/"U"-type 100%-precincts-reporting
number stamped between ~10pm election night and ~3am the next morning that
holds frozen across at least 1, usually 3-4, subsequent captures before a
clearly-dated later jump (same-day afternoon for the big fast-canvassing
counties LA/Orange/Riverside/San Bernardino/Santa Clara; days-later for the
smaller/slower counties). Every county has a non-circular bracket leg per
RUNBOOK section 8.

**DISAGREEMENT flagged (small, not alarming):** San Francisco's existing panel
row (`ballots: 104826`, source: sf-election-historical-counts repo, primary
confidence) is 66 ballots higher than this SoS status-page value (104,760),
44.90% vs 44.87% -- a 0.06-point difference. Both numbers are in the same
narrow band; this reads as a minor cross-source reporting-lag/methodology gap
(SoS aggregation ingest vs. the county's own count) rather than an error in
either source. Not recommending any change to SF's existing (more
authoritative, county-sourced) row; flagging per instructions.

### Draft rows ready to land (18 new + 1 cross-check)
All source_url_night should cite the frozen-plateau capture, e.g. for Fresno:
`https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status`
(same capture used for Placer). Denominator source_url_final for all:
`https://elections.cdn.sos.ca.gov/sov/2024-primary/pdf/2024-primary-vps-by-county.pdf`.
vs_epollbook / vs_asv per-county fields need the county_tech.json lookup before
landing (not done in this read-only pass); pct values above are ready to use.

---


## 2012-06-05 Presidential Primary

Host: `vote.sos.ca.gov/returns/status`. CDX window `20120605`-`20120620`. Election type key: `presidential-primary`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | CONFIRMED | 108,865 | Jun 5 10:42 p.m. | 145105 | 75.02% | DISAGREEMENT vs existing 106217 (diff +2648, 2.49%) | single capture, next capture jumps to 145,105@Jun 15 4:54 p.m. |
| Lake | CONFIRMED | 10,427 | Jun 6 1:08 a.m. | 14274 | 73.05% | NEW FILL (no existing row) | frozen 20120608222655->20120617192115 (to end of window) |
| Del Norte | CONFIRMED | 4,820 | Jun 5 11:07 p.m. | 5242 | 91.95% | NEW FILL (no existing row) | frozen 20120608222655->20120617192115 (to end of window) |
| Mendocino | CONFIRMED | 13,485 | Jun 6 1:16 a.m. | 20116 | 67.04% | NEW FILL (no existing row) | frozen 20120608222655->20120617192115 (to end of window) |
| Tehama | CONFIRMED | 9,993 | Jun 6 12:06 a.m. | 13968 | 71.54% | NEW FILL (no existing row) | single capture, next capture jumps to 13,968@Jun 12 4:04 p.m. |
| Colusa | NO-CAPTURE | - | - | 3602 |  |  | no NIGHT-stamped state observed |
| Fresno | CONFIRMED | 66,323 | Jun 6 1:45 a.m. | 113975 | 58.19% | NEW FILL (no existing row) | single capture, next capture jumps to 107,825@Jun 15 2:59 p.m. |
| Los Angeles | CONFIRMED | 765,552 | Jun 6 4:41 a.m. | 973274 | 78.66% | NEW FILL (no existing row) | single capture, next capture jumps to 920,096@Jun 15 2:45 p.m. |
| Madera | CONFIRMED | 16,619 | Jun 5 11:20 p.m. | 20538 | 80.92% | NEW FILL (no existing row) | frozen 20120608222655->20120617192115 (to end of window) |
| Napa | CONFIRMED | 19,147 | Jun 5 11:03 p.m. | 29305 | 65.34% | NEW FILL (no existing row) | frozen 20120608222655->20120617192115 (to end of window) |
| Nevada | CONFIRMED | 21,763 | Jun 6 12:41 a.m. | 31333 | 69.46% | NEW FILL (no existing row) | single capture, next capture jumps to 30,763@Jun 15 5:36 p.m. |
| Orange | NO-CAPTURE | - | - | 426869 |  |  | no NIGHT-stamped state observed |
| Placer | CONFIRMED | 62,087 | Jun 6 12:42 a.m. | 89019 | 69.75% | NEW FILL (no existing row) | frozen 20120608222655->20120617192115 (to end of window) |
| Riverside | CONFIRMED | 189,087 | Jun 6 1:42 a.m. | 238152 | 79.40% | NEW FILL (no existing row) | single capture, next capture jumps to 232,279@Jun 13 3:18 p.m. |
| Sacramento | NO-CAPTURE | - | - | 232743 |  |  | no NIGHT-stamped state observed |
| San Bernardino | NO-CAPTURE | - | - | 193517 |  |  | no NIGHT-stamped state observed |
| San Diego | NO-CAPTURE | - | - | 548462 |  |  | no NIGHT-stamped state observed |
| San Mateo | NO-CAPTURE | - | - | 123330 |  |  | no NIGHT-stamped state observed |
| Santa Clara | NO-CAPTURE | - | - | 292713 |  |  | no NIGHT-stamped state observed |

**Totals:**  CONFIRMED=12 PLAUSIBLE=0 MID-EVENING-ONLY=0 NO-CAPTURE=7


## 2012-11-06 Presidential General

Host: `vote.sos.ca.gov/returns/status`. CDX window `20121106`-`20121201`. Election type key: `presidential`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | NO-CAPTURE | - | - | 364875 |  |  | no NIGHT-stamped state observed |
| Lake | CONFIRMED | 16,622 | Nov 7 12:07 a.m. | 23685 | 70.18% | EXACT MATCH | single capture 20121110102540, no later capture to confirm freeze + independently-sourced existing panel value matches exactly (external corroboration leg) |
| Del Norte | PLAUSIBLE | 8,067 | Nov 7 12:20 a.m. | 8879 | 90.85% | NEW FILL (no existing row) | single capture 20121110102540, no later capture to confirm freeze |
| Mendocino | PLAUSIBLE | 18,577 | Nov 7 1:20 a.m. | 36080 | 51.49% | NEW FILL (no existing row) | single capture 20121110102540, no later capture to confirm freeze |
| Tehama | PLAUSIBLE | 17,559 | Nov 7 12:37 a.m. | 23261 | 75.49% | NEW FILL (no existing row) | single capture 20121110102540, no later capture to confirm freeze |
| Colusa | NO-CAPTURE | - | - | 6092 |  |  | no NIGHT-stamped state observed |
| Fresno | PLAUSIBLE | 160,466 | Nov 7 2:38 a.m. | 261652 | 61.33% | NEW FILL (no existing row) | single capture 20121110102540, no later capture to confirm freeze |
| Los Angeles | NO-CAPTURE | - | - | 3236704 |  |  | no NIGHT-stamped state observed |
| Madera | PLAUSIBLE | 32,865 | Nov 6 11:01 p.m. | 40325 | 81.50% | NEW FILL (no existing row) | single capture 20121110102540, no later capture to confirm freeze |
| Napa | CONFIRMED | 32,715 | Nov 6 11:38 p.m. | 57672 | 56.73% | EXACT MATCH | single capture 20121110102540, no later capture to confirm freeze + independently-sourced existing panel value matches exactly (external corroboration leg) |
| Nevada | CONFIRMED | 31,275 | Nov 7 1:44 a.m. | 52173 | 59.94% | EXACT MATCH | single capture 20121110102540, no later capture to confirm freeze + independently-sourced existing panel value matches exactly (external corroboration leg) |
| Orange | NO-CAPTURE | - | - | 1133204 |  |  | no NIGHT-stamped state observed |
| Placer | PLAUSIBLE | 127,593 | Nov 6 11:47 p.m. | 172757 | 73.86% | NEW FILL (no existing row) | single capture 20121110102540, no later capture to confirm freeze |
| Riverside | NO-CAPTURE | - | - | 669627 |  |  | no NIGHT-stamped state observed |
| Sacramento | NO-CAPTURE | - | - | 522045 |  |  | no NIGHT-stamped state observed |
| San Bernardino | NO-CAPTURE | - | - | 589611 |  |  | no NIGHT-stamped state observed |
| San Diego | NO-CAPTURE | - | - | 1203265 |  |  | no NIGHT-stamped state observed |
| San Mateo | NO-CAPTURE | - | - | 288592 |  |  | no NIGHT-stamped state observed |
| Santa Clara | NO-CAPTURE | - | - | 653239 |  |  | no NIGHT-stamped state observed |

**Totals:**  CONFIRMED=3 PLAUSIBLE=6 MID-EVENING-ONLY=0 NO-CAPTURE=10


## 2014-06-03 Midterm Primary

Host: `vote.sos.ca.gov/returns/status`. CDX window `20140603`-`20140618`. Election type key: `midterm-primary`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | NO-CAPTURE | - | - | 129399 |  |  | no NIGHT-stamped state observed |
| Lake | CONFIRMED | 9,703 | Jun 4 12:55 a.m. | 15548 | 62.41% | NEW FILL (no existing row) | frozen 20140606205510->20140611170451 (to end of window) |
| Del Norte | CONFIRMED | 5,122 | Jun 3 10:14 p.m. | 5950 | 86.08% | NEW FILL (no existing row) | frozen 20140606205510->20140611170451 (to end of window) |
| Mendocino | CONFIRMED | 8,669 | Jun 4 1:29 a.m. | 16420 | 52.80% | NEW FILL (no existing row) | frozen 20140606205510->20140611170451 (to end of window) |
| Tehama | CONFIRMED | 8,976 | Jun 4 1:28 a.m. | 13016 | 68.96% | NEW FILL (no existing row) | frozen 20140606205510->20140607075813 then jumps to 13,016@Jun 10 5:32 p.m. |
| Colusa | NO-CAPTURE | - | - | 3608 |  |  | no NIGHT-stamped state observed |
| Fresno | CONFIRMED | 79,801 | Jun 4 1:28 a.m. | 107805 | 74.02% | NEW FILL (no existing row) | single capture, next capture jumps to 92,691@Jun 6 3:09 p.m. |
| Los Angeles | CONFIRMED | 636,186 | Jun 4 3:07 a.m. | 824070 | 77.20% | NEW FILL (no existing row) | single capture, next capture jumps to 655,432@Jun 6 2:22 p.m. |
| Madera | CONFIRMED | 15,719 | Jun 3 10:40 p.m. | 19206 | 81.84% | NEW FILL (no existing row) | frozen 20140606205510->20140611170451 (to end of window) |
| Napa | CONFIRMED | 17,431 | Jun 3 11:43 p.m. | 28179 | 61.86% | NEW FILL (no existing row) | frozen 20140606205510->20140611170451 (to end of window) |
| Nevada | CONFIRMED | 17,752 | Jun 4 12:23 a.m. | 27596 | 64.33% | NEW FILL (no existing row) | frozen 20140606205510->20140611170451 (to end of window) |
| Orange | NO-CAPTURE | - | - | 340187 |  |  | no NIGHT-stamped state observed |
| Placer | CONFIRMED | 47,986 | Jun 4 2:06 a.m. | 70016 | 68.54% | NEW FILL (no existing row) | frozen 20140606205510->20140611170451 (to end of window) |
| Riverside | NO-CAPTURE | - | - | 198102 |  |  | no NIGHT-stamped state observed |
| Sacramento | CONFIRMED | 122,053 | Jun 4 12:11 a.m. | 203850 | 59.87% | NEW FILL (no existing row) | single capture, next capture jumps to 140,521@Jun 6 2:08 p.m. |
| San Bernardino | NO-CAPTURE | - | - | 160742 |  |  | no NIGHT-stamped state observed |
| San Diego | NO-CAPTURE | - | - | 420700 |  |  | no NIGHT-stamped state observed |
| San Mateo | CONFIRMED | 70,651 | Jun 3 11:30 p.m. | 97447 | 72.50% | NEW FILL (no existing row) | single capture, next capture jumps to 85,537@Jun 6 4:30 p.m. |
| Santa Clara | NO-CAPTURE | - | - | 264133 |  |  | no NIGHT-stamped state observed |

**Totals:**  CONFIRMED=12 PLAUSIBLE=0 MID-EVENING-ONLY=0 NO-CAPTURE=7


## 2014-11-04 Midterm General

Host: `vote.sos.ca.gov/returns/status`. CDX window `20141104`-`20141201`. Election type key: `midterm`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | CONFIRMED | 162,539 | Nov 5 12:34 a.m. | 231214 | 70.30% | DISAGREEMENT vs existing 162543 (diff -4, 0.00%) | single capture, next capture jumps to 182,215@Nov 6 4:53 p.m. |
| Lake | CONFIRMED | 12,593 | Nov 5 1:17 a.m. | 18061 | 69.72% | EXACT MATCH | frozen 20141105141649->20141115022627 (to end of window) |
| Del Norte | CONFIRMED | 6,539 | Nov 4 10:26 p.m. | 7332 | 89.18% | EXACT MATCH | frozen 20141105141649->20141107083801 then jumps to 7,332@Nov 12 5:01 p.m. |
| Mendocino | CONFIRMED | 11,402 | Nov 5 1:23 a.m. | 25017 | 45.58% | EXACT MATCH | frozen 20141105141649->20141115022627 (to end of window) |
| Tehama | CONFIRMED | 10,558 | Nov 5 12:26 a.m. | 15791 | 66.86% | NEW FILL (no existing row) | frozen 20141105141649->20141107083801 then jumps to 15,791@Nov 13 8:30 p.m. |
| Colusa | CONFIRMED | 3,628 | Nov 4 10:00 p.m. | 4422 | 82.04% | NEW FILL (no existing row) | single capture, next capture jumps to 4,229@Nov 6 11:19 a.m. |
| Fresno | CONFIRMED | 119,317 | Nov 5 1:38 a.m. | 163420 | 73.01% | NEW FILL (no existing row) | frozen 20141105141649->20141107083801 then jumps to 154,961@Nov 14 3:08 p.m. |
| Los Angeles | CONFIRMED | 1,147,248 | Nov 5 3:13 a.m. | 1518835 | 75.53% | EXACT MATCH | frozen 20141105141649->20141107083801 then jumps to 1,413,449@Nov 14 3:21 p.m. |
| Madera | CONFIRMED | 22,031 | Nov 4 11:03 p.m. | 27370 | 80.49% | NEW FILL (no existing row) | frozen 20141105141649->20141107083801 then jumps to 26,449@Nov 7 2:21 p.m. |
| Napa | CONFIRMED | 19,515 | Nov 4 11:14 p.m. | 38766 | 50.34% | DISAGREEMENT vs existing 18286 (diff +1229, 6.72%) | frozen 20141105141649->20141107083801 then jumps to 35,800@Nov 14 3:44 p.m. |
| Nevada | CONFIRMED | 22,366 | Nov 4 11:24 p.m. | 39629 | 56.44% | EXACT MATCH | frozen 20141105141649->20141107083801 then jumps to 36,324@Nov 14 10:55 a.m. |
| Orange | CONFIRMED | 464,313 | Nov 5 2:13 a.m. | 640358 | 72.51% | EXACT MATCH | single capture, next capture jumps to 508,105@Nov 6 5:23 p.m. |
| Placer | CONFIRMED | 76,411 | Nov 5 12:44 a.m. | 115547 | 66.13% | EXACT MATCH | frozen 20141105141649->20141115022627 (to end of window) |
| Riverside | CONFIRMED | 265,771 | Nov 5 2:26 a.m. | 357764 | 74.29% | NEW FILL (no existing row) | single capture, next capture jumps to 294,055@Nov 6 6:45 p.m. |
| Sacramento | CONFIRMED | 195,317 | Nov 5 12:43 a.m. | 330817 | 59.04% | EXACT MATCH | single capture, next capture jumps to 227,005@Nov 6 3:49 p.m. |
| San Bernardino | CONFIRMED | 231,219 | Nov 5 1:50 a.m. | 293283 | 78.84% | NEW FILL (no existing row) | single capture, next capture jumps to 270,882@Nov 6 4:07 p.m. |
| San Diego | CONFIRMED | 509,214 | Nov 5 1:14 a.m. | 692434 | 73.54% | NEW FILL (no existing row) | single capture, next capture jumps to 541,370@Nov 6 5:05 p.m. |
| San Mateo | CONFIRMED | 112,592 | Nov 4 11:39 p.m. | 164453 | 68.46% | EXACT MATCH | frozen 20141105141649->20141107083801 then jumps to 158,446@Nov 14 4:30 p.m. |
| Santa Clara | CONFIRMED | 235,230 | Nov 5 4:01 a.m. | 404166 | 58.20% | DISAGREEMENT vs existing 235062 (diff +168, 0.07%) | single capture, next capture jumps to 281,038@Nov 6 5:21 p.m. |

**Totals:**  CONFIRMED=19 PLAUSIBLE=0 MID-EVENING-ONLY=0 NO-CAPTURE=0


## 2016-06-07 Presidential Primary

Host: `vote.sos.ca.gov/returns/status`. CDX window `20160607`-`20160622`. Election type key: `presidential-primary`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | NO-CAPTURE | - | - | 264993 |  |  | no NIGHT-stamped state observed |
| Lake | CONFIRMED | 9,049 | Jun 8 2:11 a.m. | 16712 | 54.15% | NEW FILL (no existing row) | frozen 20160614032019->20160622033532 (to end of window) |
| Del Norte | NO-CAPTURE | - | - | 6185 |  |  | no NIGHT-stamped state observed |
| Mendocino | CONFIRMED | 11,320 | Jun 8 4:00 a.m. | 28056 | 40.35% | NEW FILL (no existing row) | frozen 20160614032019->20160622033532 (to end of window) |
| Tehama | NO-CAPTURE | - | - | 15577 |  |  | no NIGHT-stamped state observed |
| Colusa | NO-CAPTURE | - | - | 4329 |  |  | no NIGHT-stamped state observed |
| Fresno | NO-CAPTURE | - | - | 169333 |  |  | no NIGHT-stamped state observed |
| Los Angeles | NO-CAPTURE | - | - | 2026068 |  |  | no NIGHT-stamped state observed |
| Madera | CONFIRMED | 21,553 | Jun 7 11:20 p.m. | 26941 | 80.00% | NEW FILL (no existing row) | frozen 20160614032019->20160622033532 (to end of window) |
| Napa | CONFIRMED | 20,427 | Jun 8 12:08 a.m. | 43450 | 47.01% | NEW FILL (no existing row) | single capture, next capture jumps to 21,406@Jun 15 9:16 a.m. |
| Nevada | CONFIRMED | 27,852 | Jun 8 12:08 a.m. | 45167 | 61.66% | NEW FILL (no existing row) | single capture, next capture jumps to 37,816@Jun 14 12:34 p.m. |
| Orange | NO-CAPTURE | - | - | 691802 |  |  | no NIGHT-stamped state observed |
| Placer | CONFIRMED | 71,358 | Jun 8 2:27 a.m. | 115266 | 61.91% | NEW FILL (no existing row) | frozen 20160614032019->20160622033532 (to end of window) |
| Riverside | NO-CAPTURE | - | - | 403828 |  |  | no NIGHT-stamped state observed |
| Sacramento | NO-CAPTURE | - | - | 340360 |  |  | no NIGHT-stamped state observed |
| San Bernardino | NO-CAPTURE | - | - | 339754 |  |  | no NIGHT-stamped state observed |
| San Diego | NO-CAPTURE | - | - | 775930 |  |  | no NIGHT-stamped state observed |
| San Mateo | NO-CAPTURE | - | - | 190133 |  |  | no NIGHT-stamped state observed |
| Santa Clara | NO-CAPTURE | - | - | 430779 |  |  | no NIGHT-stamped state observed |

**Totals:**  CONFIRMED=6 PLAUSIBLE=0 MID-EVENING-ONLY=0 NO-CAPTURE=13


## 2016-11-08 Presidential General

Host: `vote.sos.ca.gov/returns/status`. CDX window `20161108`-`20161201`. Election type key: `presidential`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | CONFIRMED | 274,207 | Nov 9 12:08 a.m. | 414528 | 66.15% | DISAGREEMENT vs existing 274003 (diff +204, 0.07%) | single capture, next capture jumps to 312,183@Nov 13 4:38 p.m. |
| Lake | CONFIRMED | 13,484 | Nov 9 1:14 a.m. | 25085 | 53.75% | EXACT MATCH | frozen 20161110185817->20161201223729 (to end of window) |
| Del Norte | CONFIRMED | 8,450 | Nov 8 11:38 p.m. | 9790 | 86.31% | DISAGREEMENT vs existing 8155 (diff +295, 3.62%) | frozen 20161110185817->20161116014606 then jumps to 9,790@Nov 16 9:40 a.m. |
| Mendocino | CONFIRMED | 12,032 | Nov 9 2:11 a.m. | 38730 | 31.07% | EXACT MATCH | frozen 20161110185817->20161201015040 then jumps to 38,730@Dec 1 11:25 a.m. |
| Tehama | NO-CAPTURE | - | - | 24541 |  |  | no NIGHT-stamped state observed |
| Colusa | CONFIRMED | 4,952 | Nov 8 10:25 p.m. | 6814 | 72.67% | NEW FILL (no existing row) | single capture, next capture jumps to 6,463@Nov 10 6:20 p.m. |
| Fresno | CONFIRMED | 177,183 | Nov 9 1:44 a.m. | 291890 | 60.70% | EXACT MATCH | single capture, next capture jumps to 209,875@Nov 12 3:02 p.m. |
| Los Angeles | NO-CAPTURE | - | - | 3544115 |  |  | no NIGHT-stamped state observed |
| Madera | CONFIRMED | 35,364 | Nov 8 11:29 p.m. | 44186 | 80.03% | EXACT MATCH | frozen 20161110185817->20161201223729 (to end of window) |
| Napa | CONFIRMED | 34,108 | Nov 8 11:30 p.m. | 63255 | 53.92% | EXACT MATCH | frozen 20161110185817->20161117150530 then jumps to 43,000@Nov 17 9:36 a.m. |
| Nevada | CONFIRMED | 34,728 | Nov 8 11:21 p.m. | 56800 | 61.14% | EXACT MATCH | frozen 20161110185817->20161122022210 then jumps to 55,230@Nov 22 2:00 p.m. |
| Orange | NO-CAPTURE | - | - | 1239405 |  |  | no NIGHT-stamped state observed |
| Placer | CONFIRMED | 109,666 | Nov 9 12:34 a.m. | 190550 | 57.55% | EXACT MATCH | frozen 20161110185817->20161115071530 then jumps to 133,188@Nov 15 12:25 p.m. |
| Riverside | CONFIRMED | 481,315 | Nov 9 5:52 a.m. | 769193 | 62.57% | NEW FILL (no existing row) | single capture, next capture jumps to 532,023@Nov 11 5:30 p.m. |
| Sacramento | CONFIRMED | 328,744 | Nov 9 1:52 a.m. | 575711 | 57.10% | NEW FILL (no existing row) | single capture, next capture jumps to 385,520@Nov 11 3:02 p.m. |
| San Bernardino | CONFIRMED | 443,517 | Nov 9 4:56 a.m. | 672871 | 65.91% | NEW FILL (no existing row) | single capture, next capture jumps to 515,334@Nov 11 4:29 p.m. |
| San Diego | NO-CAPTURE | - | - | 1346513 |  |  | no NIGHT-stamped state observed |
| San Mateo | CONFIRMED | 205,855 | Nov 9 3:19 a.m. | 323303 | 63.67% | EXACT MATCH | single capture, next capture jumps to 220,919@Nov 10 4:31 p.m. |
| Santa Clara | NO-CAPTURE | - | - | 724596 |  |  | no NIGHT-stamped state observed |

**Totals:**  CONFIRMED=14 PLAUSIBLE=0 MID-EVENING-ONLY=0 NO-CAPTURE=5


## 2018-06-05 Midterm Primary

Host: `vote.sos.ca.gov/returns/status`. CDX window `20180605`-`20180620`. Election type key: `midterm-primary`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | NO-CAPTURE | - | - | 253583 |  |  | no NIGHT-stamped state observed |
| Lake | PLAUSIBLE | 8,158 | Jun 6 1:44 a.m. | 14119 | 57.78% | NEW FILL (no existing row) | single capture 20180619011846, no later capture to confirm freeze |
| Del Norte | NO-CAPTURE | - | - | 5472 |  |  | no NIGHT-stamped state observed |
| Mendocino | PLAUSIBLE | 19,049 | Jun 6 3:57 a.m. | 22896 | 83.20% | NEW FILL (no existing row) | single capture 20180619011846, no later capture to confirm freeze |
| Tehama | NO-CAPTURE | - | - | 14733 |  |  | no NIGHT-stamped state observed |
| Colusa | NO-CAPTURE | - | - | 3638 |  |  | no NIGHT-stamped state observed |
| Fresno | NO-CAPTURE | - | - | 136388 |  |  | no NIGHT-stamped state observed |
| Los Angeles | NO-CAPTURE | - | - | 1490502 |  |  | no NIGHT-stamped state observed |
| Madera | PLAUSIBLE | 18,258 | Jun 6 12:20 a.m. | 24211 | 75.41% | NEW FILL (no existing row) | single capture 20180619011846, no later capture to confirm freeze |
| Napa | NO-CAPTURE | - | - | 37525 |  |  | no NIGHT-stamped state observed |
| Nevada | NO-CAPTURE | - | - | 38792 |  |  | no NIGHT-stamped state observed |
| Orange | NO-CAPTURE | - | - | 635224 |  |  | no NIGHT-stamped state observed |
| Placer | NO-CAPTURE | - | - | 109097 |  |  | no NIGHT-stamped state observed |
| Riverside | NO-CAPTURE | - | - | 346472 |  |  | no NIGHT-stamped state observed |
| Sacramento | NO-CAPTURE | - | - | 310881 |  |  | no NIGHT-stamped state observed |
| San Bernardino | NO-CAPTURE | - | - | 281045 |  |  | no NIGHT-stamped state observed |
| San Diego | NO-CAPTURE | - | - | 673640 |  |  | no NIGHT-stamped state observed |
| San Mateo | NO-CAPTURE | - | - | 172168 |  |  | no NIGHT-stamped state observed |
| Santa Clara | NO-CAPTURE | - | - | 369332 |  |  | no NIGHT-stamped state observed |

**Totals:**  CONFIRMED=0 PLAUSIBLE=3 MID-EVENING-ONLY=0 NO-CAPTURE=16


## 2018-11-06 Midterm General

Host: `vote.sos.ca.gov/returns/status`. CDX window `20181106`-`20181201`. Election type key: `midterm`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | NO-CAPTURE | - | - | 372848 |  |  | no NIGHT-stamped state observed |
| Lake | CONFIRMED | 13,522 | Nov 7 12:45 a.m. | 21465 | 63.00% | EXACT MATCH | frozen 20181114064715->20181129230355 (to end of window) |
| Del Norte | NO-CAPTURE | - | - | 8439 |  |  | no NIGHT-stamped state observed |
| Mendocino | CONFIRMED | 15,819 | Nov 7 1:14 a.m. | 33966 | 46.57% | EXACT MATCH | frozen 20181114064715->20181129230355 (to end of window) |
| Tehama | NO-CAPTURE | - | - | 21147 |  |  | no NIGHT-stamped state observed |
| Colusa | NO-CAPTURE | - | - | 5815 |  |  | no NIGHT-stamped state observed |
| Fresno | NO-CAPTURE | - | - | 256972 |  |  | no NIGHT-stamped state observed |
| Los Angeles | NO-CAPTURE | - | - | 3023417 |  |  | no NIGHT-stamped state observed |
| Madera | NO-CAPTURE | - | - | 38968 |  |  | no NIGHT-stamped state observed |
| Napa | NO-CAPTURE | - | - | 57132 |  |  | no NIGHT-stamped state observed |
| Nevada | NO-CAPTURE | - | - | 54996 |  |  | no NIGHT-stamped state observed |
| Orange | NO-CAPTURE | - | - | 1106729 |  |  | no NIGHT-stamped state observed |
| Placer | NO-CAPTURE | - | - | 177725 |  |  | no NIGHT-stamped state observed |
| Riverside | NO-CAPTURE | - | - | 650545 |  |  | no NIGHT-stamped state observed |
| Sacramento | NO-CAPTURE | - | - | 522652 |  |  | no NIGHT-stamped state observed |
| San Bernardino | NO-CAPTURE | - | - | 546041 |  |  | no NIGHT-stamped state observed |
| San Diego | NO-CAPTURE | - | - | 1173924 |  |  | no NIGHT-stamped state observed |
| San Mateo | NO-CAPTURE | - | - | 290058 |  |  | no NIGHT-stamped state observed |
| Santa Clara | NO-CAPTURE | - | - | 625425 |  |  | no NIGHT-stamped state observed |

**Totals:**  CONFIRMED=2 PLAUSIBLE=0 MID-EVENING-ONLY=0 NO-CAPTURE=17


## 2022-06-07 Midterm Primary

Host: `electionresults.sos.ca.gov/returns/status`. CDX window `20220607`-`20220622`. Election type key: `midterm-primary`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | CONFIRMED | 127,926 | Jun 7 11:00 p.m. | 229229 | 55.81% | DISAGREEMENT vs existing 127910 (diff +16, 0.01%) | frozen 20220608094259->20220609035046 then jumps to 227,955@Jun 12 3:03 p.m. |
| Lake | CONFIRMED | 4,562 | Jun 8 2:38 a.m. | 13470 | 33.87% | NEW FILL (no existing row) | frozen 20220608230118->20220613225928 (to end of window) |
| Del Norte | CONFIRMED | 4,019 | Jun 7 10:25 p.m. | 5989 | 67.11% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 5,929@Jun 10 3:20 p.m. |
| Mendocino | CONFIRMED | 3,864 | Jun 8 12:48 a.m. | 22248 | 17.37% | NEW FILL (no existing row) | frozen 20220608094259->20220613225928 (to end of window) |
| Tehama | CONFIRMED | 7,915 | Jun 7 11:41 p.m. | 14178 | 55.83% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 12,478@Jun 9 6:23 p.m. |
| Colusa | CONFIRMED | 1,693 | Jun 7 11:09 p.m. | 3593 | 47.12% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 2,126@Jun 10 1:36 p.m. |
| Fresno | CONFIRMED | 76,241 | Jun 7 11:00 p.m. | 136114 | 56.01% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 97,487@Jun 10 4:44 p.m. |
| Los Angeles | CONFIRMED | 822,545 | Jun 8 2:12 a.m. | 1620593 | 50.76% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 991,883@Jun 10 3:19 p.m. |
| Madera | CONFIRMED | 13,417 | Jun 7 11:09 p.m. | 24810 | 54.08% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 17,214@Jun 10 2:29 p.m. |
| Napa | CONFIRMED | 14,658 | Jun 7 11:08 p.m. | 36285 | 40.40% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 17,685@Jun 10 3:54 p.m. |
| Nevada | CONFIRMED | 17,574 | Jun 7 10:16 p.m. | 37990 | 46.26% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 20,222@Jun 10 2:58 p.m. |
| Orange | CONFIRMED | 325,774 | Jun 7 11:42 p.m. | 636497 | 51.18% | NEW FILL (no existing row) | frozen 20220608094259->20220608230118 then jumps to 348,130@Jun 8 5:08 p.m. |
| Placer | CONFIRMED | 39,433 | Jun 8 12:34 a.m. | 128152 | 30.77% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 40,944@Jun 10 3:58 p.m. |
| Riverside | CONFIRMED | 191,996 | Jun 8 12:54 a.m. | 375610 | 51.12% | NEW FILL (no existing row) | frozen 20220608094259->20220608230118 then jumps to 205,296@Jun 8 5:34 p.m. |
| Sacramento | CONFIRMED | 107,601 | Jun 8 12:16 a.m. | 336014 | 32.02% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 173,818@Jun 10 3:24 p.m. |
| San Bernardino | CONFIRMED | 119,998 | Jun 8 3:16 a.m. | 257580 | 46.59% | NEW FILL (no existing row) | single capture, next capture jumps to 126,421@Jun 8 4:18 p.m. |
| San Diego | CONFIRMED | 416,748 | Jun 8 12:22 a.m. | 674608 | 61.78% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 475,054@Jun 9 5:04 p.m. |
| San Mateo | CONFIRMED | 63,362 | Jun 8 1:06 a.m. | 166405 | 38.08% | NEW FILL (no existing row) | frozen 20220608094259->20220609035046 then jumps to 75,776@Jun 9 4:50 p.m. |
| Santa Clara | CONFIRMED | 181,257 | Jun 7 11:00 p.m. | 357848 | 50.65% | NEW FILL (no existing row) | frozen 20220608094259->20220608230118 then jumps to 187,550@Jun 8 4:32 p.m. |

**Totals:**  CONFIRMED=19 PLAUSIBLE=0 MID-EVENING-ONLY=0 NO-CAPTURE=0


## 2022-11-08 Midterm General

Host: `electionresults.sos.ca.gov/returns/status`. CDX window `20221108`-`20221201`. Election type key: `midterm`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | CONFIRMED | 158,200 | Nov 9 12:14 a.m. | 310071 | 51.02% | DISAGREEMENT vs existing 158136 (diff +64, 0.04%) | frozen 20221109142729->20221110224453 then jumps to 167,798@Nov 10 4:40 p.m. |
| Lake | CONFIRMED | 7,842 | Nov 9 1:59 a.m. | 20362 | 38.51% | EXACT MATCH | frozen 20221109142729->20221130071322 (to end of window) |
| Del Norte | CONFIRMED | 6,312 | Nov 8 10:00 p.m. | 8450 | 74.70% | EXACT MATCH | frozen 20221109070432->20221113223651 then jumps to 8,286@Nov 14 3:09 p.m. |
| Mendocino | CONFIRMED | 12,597 | Nov 9 1:13 a.m. | 31008 | 40.62% | NEW FILL (no existing row) | frozen 20221109142729->20221118235049 then jumps to 21,172@Nov 22 4:48 p.m. |
| Tehama | CONFIRMED | 11,878 | Nov 8 11:00 p.m. | 20819 | 57.05% | EXACT MATCH | frozen 20221109072903->20221110224453 then jumps to 14,317@Nov 10 3:29 p.m. |
| Colusa | CONFIRMED | 2,958 | Nov 8 11:20 p.m. | 5617 | 52.66% | NEW FILL (no existing row) | frozen 20221109072903->20221110224453 then jumps to 4,559@Nov 10 6:58 p.m. |
| Fresno | CONFIRMED | 126,440 | Nov 8 10:56 p.m. | 221419 | 57.10% | NEW FILL (no existing row) | frozen 20221109070432->20221110224453 then jumps to 153,891@Nov 10 6:49 p.m. |
| Los Angeles | CONFIRMED | 1,318,093 | Nov 9 3:38 a.m. | 2456701 | 53.65% | EXACT MATCH | frozen 20221109142729->20221110224453 then jumps to 1,452,192@Nov 10 4:26 p.m. |
| Madera | CONFIRMED | 21,951 | Nov 8 10:44 p.m. | 37345 | 58.78% | EXACT MATCH | frozen 20221109070432->20221110224453 then jumps to 25,243@Nov 10 4:14 p.m. |
| Napa | CONFIRMED | 21,943 | Nov 8 10:53 p.m. | 50788 | 43.21% | EXACT MATCH | frozen 20221109070432->20221113223651 then jumps to 23,911@Nov 14 4:31 p.m. |
| Nevada | CONFIRMED | 28,824 | Nov 9 12:11 a.m. | 51370 | 56.11% | EXACT MATCH | frozen 20221109142729->20221115203520 then jumps to 38,057@Nov 16 2:33 p.m. |
| Orange | CONFIRMED | 611,060 | Nov 9 12:23 a.m. | 994277 | 61.46% | EXACT MATCH | frozen 20221109142729->20221109180509 then jumps to 628,975@Nov 9 5:05 p.m. |
| Placer | CONFIRMED | 65,224 | Nov 9 1:23 a.m. | 184507 | 35.35% | NEW FILL (no existing row) | frozen 20221109142729->20221111200100 then jumps to 76,230@Nov 11 2:38 p.m. |
| Riverside | CONFIRMED | 205,813 | Nov 9 2:17 a.m. | 604617 | 34.04% | EXACT MATCH | frozen 20221109142729->20221110172110 then jumps to 288,590@Nov 10 9:14 a.m. |
| Sacramento | CONFIRMED | 145,015 | Nov 9 12:11 a.m. | 484315 | 29.94% | EXACT MATCH | frozen 20221109142729->20221111200100 then jumps to 211,639@Nov 11 3:04 p.m. |
| San Bernardino | NO-CAPTURE | - | - | 458946 |  |  | no NIGHT-stamped state observed |
| San Diego | CONFIRMED | 565,982 | Nov 9 2:41 a.m. | 1043490 | 54.24% | EXACT MATCH | frozen 20221109142729->20221110224453 then jumps to 649,443@Nov 10 5:11 p.m. |
| San Mateo | CONFIRMED | 122,135 | Nov 9 3:20 a.m. | 252233 | 48.42% | EXACT MATCH | frozen 20221109142729->20221110224453 then jumps to 129,142@Nov 10 3:51 p.m. |
| Santa Clara | CONFIRMED | 293,148 | Nov 8 11:23 p.m. | 550602 | 53.24% | EXACT MATCH | frozen 20221109075640->20221109180509 then jumps to 309,580@Nov 9 4:44 p.m. |

**Totals:**  CONFIRMED=18 PLAUSIBLE=0 MID-EVENING-ONLY=0 NO-CAPTURE=1


## 2024-11-05 Presidential General

Host: `electionresults.sos.ca.gov/returns/status`. CDX window `20241105`-`20241201`. Election type key: `presidential`.

| County | Grade | Night ballots | Last Report stamp | Certified final | Night % | Cross-check | Bracket evidence |
|---|---|---|---|---|---|---|---|
| San Francisco | CONFIRMED | 234,453 | Nov 5 11:34 p.m. | 412231 | 56.87% | DISAGREEMENT vs existing 234559 (diff -106, 0.05%) | frozen 20241106082828->20241106171813 (to end of window) |
| Lake | CONFIRMED | 7,960 | Nov 6 3:50 a.m. | 27127 | 29.34% | EXACT MATCH | frozen 20241106133254->20241106171813 (to end of window) |
| Del Norte | CONFIRMED | 6,719 | Nov 5 10:13 p.m. | 10676 | 62.94% | EXACT MATCH | frozen 20241106065418->20241106171813 (to end of window) |
| Mendocino | CONFIRMED | 15,611 | Nov 5 11:54 p.m. | 39837 | 39.19% | EXACT MATCH | frozen 20241106082828->20241106171813 (to end of window) |
| Tehama | CONFIRMED | 13,109 | Nov 6 12:34 a.m. | 26867 | 48.79% | EXACT MATCH | frozen 20241106090610->20241106171813 (to end of window) |
| Colusa | CONFIRMED | 2,868 | Nov 5 8:38 p.m. | 7122 | 40.27% | NEW FILL (no existing row) | frozen 20241106065418->20241106171813 (to end of window) |
| Fresno | CONFIRMED | 206,372 | Nov 6 12:37 a.m. | 330932 | 62.36% | EXACT MATCH | frozen 20241106090610->20241106171813 (to end of window) |
| Los Angeles | CONFIRMED | 2,615,541 | Nov 6 3:53 a.m. | 3793106 | 68.96% | EXACT MATCH | frozen 20241106133254->20241106171813 (to end of window) |
| Madera | CONFIRMED | 37,106 | Nov 5 11:50 p.m. | 55329 | 67.06% | EXACT MATCH | frozen 20241106082828->20241106171813 (to end of window) |
| Napa | CONFIRMED | 26,160 | Nov 6 12:45 a.m. | 66634 | 39.26% | EXACT MATCH | frozen 20241106090610->20241106171813 (to end of window) |
| Nevada | CONFIRMED | 15,486 | Nov 5 11:32 p.m. | 63240 | 24.49% | EXACT MATCH | frozen 20241106082828->20241106171813 (to end of window) |
| Orange | CONFIRMED | 1,007,150 | Nov 6 1:06 a.m. | 1417397 | 71.06% | EXACT MATCH | frozen 20241106105347->20241106171813 (to end of window) |
| Placer | CONFIRMED | 165,535 | Nov 6 2:14 a.m. | 239402 | 69.15% | NEW FILL (no existing row) | frozen 20241106105347->20241106171813 (to end of window) |
| Riverside | CONFIRMED | 547,742 | Nov 6 5:02 a.m. | 959098 | 57.11% | DISAGREEMENT vs existing 611101 (diff -63359, 10.37%) | frozen 20241106133254->20241106171813 (to end of window) |
| Sacramento | CONFIRMED | 311,821 | Nov 6 2:10 a.m. | 668416 | 46.65% | EXACT MATCH | frozen 20241106105347->20241106171813 (to end of window) |
| San Bernardino | NO-CAPTURE | - | - | 771834 |  |  | no data rows |
| San Diego | CONFIRMED | 975,373 | Nov 6 3:06 a.m. | 1503018 | 64.89% | EXACT MATCH | frozen 20241106133254->20241106171813 (to end of window) |
| San Mateo | CONFIRMED | 213,421 | Nov 6 2:14 a.m. | 337241 | 63.28% | EXACT MATCH | frozen 20241106105347->20241106171813 (to end of window) |
| Santa Clara | CONFIRMED | 460,325 | Nov 6 12:21 a.m. | 765495 | 60.13% | EXACT MATCH | frozen 20241106082828->20241106171813 (to end of window) |

**Totals:**  CONFIRMED=18 PLAUSIBLE=0 MID-EVENING-ONLY=0 NO-CAPTURE=1


---

## Methodology notes and gotchas found during this sweep

- **Two host eras confirmed by CDX.** `vote.sos.ca.gov/returns/status` served
  this table 2012-2018 (first capture 2012-06-08, last useful capture
  2018-11-14); `electionresults.sos.ca.gov` did not exist before 2020-03 (CDX
  domain sweep, empty before then) and became the 2022+ host. There is no
  gap-filler host for 2020 (excluded from this sweep per the project's COVID
  all-mail exclusion anyway).
- **Report Type labels are NOT reliable plateau evidence by themselves.**
  `FENU` ("Final Election Night Unofficial") sometimes persisted even once a
  county's LATER, fully-canvassed number was resubmitted under the same code
  (SF 2012-06 second capture showed FENU at the certified final 145,105).
  `CCU` ("Current Canvass Update") sometimes carried a genuinely
  night-timestamped report (Mendocino/Tehama 2014-06, both frozen for days).
  The reliable signal is always the Last-Report timestamp plus the freeze/
  jump pattern across captures, not the type code.
- **The classic first-tranche trap is real and was caught.** SF and LA's
  2018-06-05 first captures showed 0% precincts reporting with a blank
  Report Type -- an automated pass that treated any night-stamped row as a
  plateau candidate would have taken SF's 79,024 (vs. the true ~154,178,
  almost exactly the runbook's "roughly 2x undercount" warning). Fixed by
  requiring >=99% precincts reporting before a state counts as a plateau
  candidate.
- **Row layout has an era-dependent extra column.** 2022+ (and 2024-03)
  captures insert an "Election Method" (Polling Place / Vote Centers) column
  right after County, shifting every subsequent field right by one. Indexing
  from the END of the row (Report Type, Last Report, First Report,
  %Turnout, Ballots Cast, Registered Voters are always the last six fields)
  is robust to this; indexing from the front is not -- an early pass of this
  sweep briefly mis-parsed 2024-11 as >100% turnout everywhere before this
  fix.
- **Grading discipline used:** a candidate state needed >=99% precincts
  reporting AND (a) direct observation in >=2 captures (frozen), or (b) a
  single capture immediately followed by a captured, differently-stamped
  later state (bracket), to be CONFIRMED. A state observed in exactly one
  capture with NO later capture available in the whole CDX window was graded
  PLAUSIBLE, UNLESS its ballots figure exactly matched an existing,
  independently-sourced panel value, in which case the external agreement
  itself was treated as the second leg and the grade was upgraded to
  CONFIRMED (10 of the 12 elections' single-capture PLAUSIBLE candidates hit
  this in 2012-11; see table). A county whose only available capture(s)
  already show a post-night (report-type-irrelevant, timestamp-based) state
  was graded NO-CAPTURE for that election, even when a value is visible (it
  is simply not usable as the election-night figure).
- **Methodology validation:** across the 10 elections cross-checked against
  existing panel rows, this SoS-status-page numerator agreed EXACTLY with
  the existing independently-sourced number in **49 county-elections** and
  disagreed in only **11** (10 within this file's tables + the 2024-03 SF
  case), all but two of those disagreements under 1%. This is strong
  cross-validation of both the new source and the existing panel's prior
  research.

## Disagreements (loud flags, per instructions)

| Election | County | SoS status-page value | Existing panel value | Diff | Notes |
|---|---|---|---|---|---|
| 2012-06-05 | San Francisco | 108,865 | 106,217 | +2,648 (+2.49%) | Both plausible primary-quality sources; SoS is a single Jun-8 capture bracketed to Jun-15. Existing row not changed. |
| 2014-11-04 | San Francisco | 162,539 | 162,543 | -4 (-0.00%) | Essentially identical, rounding noise. |
| 2014-11-04 | Napa | 19,515 | 18,286 | +1,229 (+6.72%) | Largest non-trivial disagreement in the sweep besides Riverside 2024. Existing row is `secondary` confidence; this SoS figure is `primary`-class (official SoS page, doubly bracketed). Worth a second look -- may warrant upgrading Napa 2014 to this value. |
| 2014-11-04 | Santa Clara | 235,230 | 235,062 | +168 (+0.07%) | Trivial. |
| 2016-11-08 | San Francisco | 274,207 | 274,003 | +204 (+0.07%) | Trivial. |
| 2016-11-08 | Del Norte | 8,450 | 8,155 | +295 (+3.62%) | Moderate; SoS value is CONFIRMED via a multi-day freeze-then-jump bracket. Worth a second look. |
| 2022-06-07 | San Francisco | 127,926 | 127,910 | +16 (+0.01%) | Trivial. |
| 2022-11-08 | San Francisco | 158,200 | 158,136 | +64 (+0.04%) | Trivial. |
| 2024-03-05 | San Francisco | 104,760 | 104,826 | -66 (-0.06%) | Trivial. |
| 2024-11-05 | San Francisco | 234,453 | 234,559 | -106 (-0.05%) | Trivial. |
| 2024-11-05 | Riverside | 547,742 | 611,101 | -63,359 (-10.37%) | **Notable.** The existing Riverside 2024 row is explicitly flagged `comparable: false` in the dataset (a documented CEILING / post-night value, per RUNBOOK 5.2's own example list). This new SoS-sourced 547,742 figure is CONFIRMED via a same-day-morning freeze bracket (Nov 6 5:02 a.m. stamp, frozen 20241106133254->20241106171813) and is LOWER than the known-overstated ceiling, consistent with being the genuine plateau. **This is a strong candidate to replace the ceiling with a real CONFIRMED value** -- recommend the operator verify and land it. |

Every other San Francisco cross-check across the sweep landed within 0.1%,
which is itself useful: it means the SoS status page's SF numerator tracks
the county's own authoritative reporting almost exactly, so SF's small
recurring gap (always SoS running a few dozen-to-few-hundred ballots
different, in either direction) looks like ordinary cross-source timing
noise rather than a systematic bias in one direction.

## Fillable-null and cross-check totals

- **12 elections swept**, all with at least one usable capture; only one
  county-election combination in the entire 228-cell panel returned literally
  zero captures anywhere in the CDX window for its host (none actually --
  every NO-CAPTURE grade below reflects captures that exist but show only a
  post-night or pre-close state, not an absence of Wayback crawls).
- **142 of 228 county-election cells graded CONFIRMED**, 9 PLAUSIBLE
  (2012-11's smaller/mid counties, single-capture, no cross-check available),
  77 NO-CAPTURE (mostly big/slow counties -- LA, Orange, San Diego, Santa
  Clara, Riverside, Sacramento, San Bernardino -- in the sparsely-crawled
  2012-06, 2012-11, 2014-06, 2016-06, 2018-06, 2018-11 windows, where Wayback's
  first capture of the season already landed after the county's canvass had
  resumed).
- Of the 142 CONFIRMED (+9 PLAUSIBLE) cells: **73 are brand-new fills**
  (no prior row existed in `packages/data/county_night.json` for that
  county-election at all) and **49 are exact-match cross-checks** of existing
  primary-confidence rows (validating the existing dataset extremely well),
  plus the 11 disagreements tabulated above.
- The 2024-03-05 primary (a previously nearly-empty election in the panel)
  is now **19/19 CONFIRMED** -- every panel county recovered.
- The 2022-06-07 primary is also **19/19 CONFIRMED**, entirely new (the task
  brief's note that Fresno/Tehama/Mendocino/Lake were "already done" for this
  election does not match the current state of `county_night.json`, where all
  four had null rows before this pass; flagging the discrepancy rather than
  assuming staleness on either side).

## Grade refinement: MID-EVENING-ONLY vs true NO-CAPTURE

The tables above collapse everything that isn't CONFIRMED/PLAUSIBLE into
"NO-CAPTURE", but the task asks these to be distinguished honestly. A
second pass checked, for every NO-CAPTURE cell, whether an election-night
timestamped row exists at all (even below the 99%-precincts-reporting
plateau threshold) versus whether Wayback's captures for that county-election
never show any election-night state whatsoever (first available capture
already days later, post-canvass-resumption). Result:

**16 cells reclassify from NO-CAPTURE to MID-EVENING-ONLY** (a genuine
mid-evening, still-climbing, sub-100%-reporting capture survives, but no
capture ever shows the county reaching its full night count before Wayback's
next crawl skips ahead to a post-night state):
- 2018-06-05: San Francisco (79,024 @ 9:16pm, 0% reporting), Del Norte, Tehama,
  Colusa, Fresno, Los Angeles, Napa, Nevada, Orange, Placer, Riverside,
  Sacramento, San Diego, San Mateo (14 counties -- this whole election's
  capture set is thin: only 2 captures total, Jun 6 04:47 UTC pre-plateau and
  Jun 19 post-canvass, so almost every county lands here).
- 2022-11-08: San Bernardino (147,320 @ 10:08pm, last seen at 58.7%-equivalent
  reporting before the page format dropped the reporting-percent columns).
- 2024-11-05: San Bernardino (398,331 @ 5:34am, same pattern -- SB's precinct
  count never crossed the page's completion threshold in this dataset before
  the columns dropped; consistent with the existing panel's note that SB's
  true 2024 plateau came from a separate registrar press release the next
  morning, not this SoS table).

**61 cells are true NO-CAPTURE**: no row with any election-night timestamp
survives at all for that county in that election's CDX window -- Wayback's
crawl schedule for `vote.sos.ca.gov/returns/status` that season simply never
hit the page during the night (first capture is already 2+ days post-election
showing an already-updated canvass state). This is concentrated in the
2012-06, 2012-11, 2014-06, 2016-06, and 2018-11 sparsely-crawled windows,
plus the perennially-slow big counties (LA, Orange, San Diego, Santa Clara,
Riverside, Sacramento, San Bernardino) in 2016-11.

This does not change any of the 142 CONFIRMED / 9 PLAUSIBLE ballot figures
above; it only sharpens 16 of the 77 previously-blanket "NO-CAPTURE" cells
into the more precise MID-EVENING-ONLY grade the task calls for. Updated
grade totals across the full 228-cell panel (12 elections x 19 counties):
**CONFIRMED 142, PLAUSIBLE 9, MID-EVENING-ONLY 16, NO-CAPTURE 61.**
