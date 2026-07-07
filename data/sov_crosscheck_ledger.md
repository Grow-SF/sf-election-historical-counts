# SOV cross-check ledger (CA Statement of Vote vs DOE)

Source of truth for STATEWIDE elections = CA Secretary of State **Statement of
Vote**, digitized & public on archive.org. See skill `sov-certified-turnout`.
Method: pull SF County certified figure (prefer the SOV's per-county "total
votes cast" turnout line; else the top-contest sum as a floor), via Wikipedia
by-county tables (which cite the exact SOV volume+page) confirmed against the
SOV PDF. NOT applicable to odd-year municipal/special elections.

## Volume map (archive.org)
1908–1922 `statementofvo19081922cali` (1920 also `ldpd_11382167_000`) ·
1924–1930 `statementofvote192430cali` · 1926–1939 `statementofvote192639cali` ·
1932–1939 `statementofvo19321939cali` · 1940–1950 `stateofcaliforn194050cali` ·
1952–1962 `stateofcaliforn195262cali` · 1962–1964 `castatem196264cali` ·
1973–74 `statementofvote197374cali` · 1978–79 `statementofvote197879cali`.

## Discrepancies noticed (under review)
A few figures in DOE's `sf_turnout_history_doe_1899_2019.csv` don't reconcile with
the SOV in the early/mid record — one pattern recurs (1978: the DOE figure matches
the SOV's precinct-only column, appearing to drop absentees). We're not asserting
the table is wrong; these need a closer look. Notes below. See
`docs/doe-data-discrepancies.md` for the friendlier write-up.

## Cross-check results (✓=reconciles · ✗=doesn't reconcile, under review · ⚠=our data fixed)
| Election | SOV SF (contest / turnout) | DOE | verdict | action |
|---|---|---|---|---|
| 1908-11-03 P | President 60,124 (turnout ≥) | 41,137 | ✗ under review (looks low) | certified→60,124; night-share 88.6→**60.6%** |
| 1910-11-08 G | Governor 59,182 | 59,724 | ✓ (turnout≈) | keep 59,724 + SOV cite |
| 1912-11-05 P | President 101,148 | 105,646 | ✓ | keep + SOV cite |
| 1916-11-07 P | President 149,152 | 155,747 | ✓ | keep + SOV cite |
| 1920-11-02 P | President 147,450 | 154,592 | ✓ | keep + SOV cite |
| 1934-11-06 G | Governor 225,977 (turnout≥) | 166,133 | ✗ under review (looks low) | certified→225,977; night 97.7% (done earlier) |
| 1958-11-04 G | turnout 319,179 (Gov 309,969) | (none) | fill | certified→319,179; 100→**99.9%** |
| 1962-11-06 G | Governor 287,463 | (none) | fill | certified→287,463 (done earlier) |
| 1974-06-04 Pr| turnout 198,508 | 198,508 | ✓ DOE | ⚠ our day-2 Prop B 203,381 exceeded turnout → fixed to 198,508 |
| 1978-11-07 G | turnout 238,667 (Gov 225,465) | 217,965 | ✗ under review (looks precinct-only) | certified→238,667; 100→**93.5%** |

## ⚠ Prose impact
- `index.mdx` era-1 says "≈85–89% in 1908 and 1912." **1908 is now ~61%** (was
  computed against DOE's lower 41,137). The 1908 example must be corrected — the
  hand-era "light-ballot fast morning" claim should lean on 1912 (still high) and
  the 1928+ machine era, not 1908. (User edits prose.)

## TODO — remaining statewide cross-checks
Generals: 1914, 1918, 1922, 1924, 1926, 1928, 1930, 1932, 1936, 1938, 1940,
1942, 1946, 1948, 1952, 1956, 1960, 1964. Primaries: 1928, 1930, 1932, 1948,
1950, 1952, 1954, 1956, 1958, 1960, 1962, 1964. (Municipals/specials: N/A.)
Also: modern DOE figures 1968–2014 (lower priority; our exact data matches).

## Batch 2 & 3 results (generals 1914-1960) — all DOE-consistent
| Election | SOV SF contest | SOV total-cast | DOE | verdict |
|---|---|---|---|---|
| 1914-11-03 G | Gov 132,103 | 134,492 | 134,492 | ✓ DOE=SOV turnout |
| 1918-11-05 G | Gov 100,382 | 103,011 | 103,011 | ✓ DOE=SOV turnout |
| 1922-11-07 G | Gov 132,225 | (none) | 134,503 | ✓ |
| 1924-11-04 P | Pres 153,950 | (none) | 159,649 | ✓ |
| 1926-11-02 G | Gov 125,301 | (none) | 130,835 | ✓ |
| 1928-11-06 P | Pres 195,468 | (none) | 199,665 | ✓ |
| 1932-11-08 P | Pres 223,197 | (none) | 227,283 | ✓ |
| 1936-11-03 P | Pres 265,001 | (none) | 269,387 | ✓ |
| 1938-11-08 G | Gov 248,035 | (none) | 257,597 | ✓ |
| 1940-11-05 P | Pres 311,878 | (none) | 315,518 | ✓ |
| 1942-11-03 G | Gov 226,560 | (none) | 230,129 | ✓ |
| 1946-11-05 G | Gov 239,116 | (none) | 270,457 | ✓ (Warren cross-filed) |
| 1948-11-02 P | Pres 350,709 | (none) | 359,134 | ✓ |
| 1952-11-04 P | Pres 374,700 | 365,972 | 365,972 | ⚠ SOV internal anomaly; DOE=SOV turnout |
| 1956-11-06 P | Pres 336,967 | 342,652 | 342,652 | ✓ DOE=SOV turnout |
| 1960-11-08 P | Pres 342,219 | 348,290 | 348,290 | ✓ DOE=SOV turnout |

Generals cross-check complete 1908-1960 (1944 skipped). Discrepancies under review: 1908, 1934, 1978.
Remaining: 1964 general; 1948-1964 primaries.

## Batch 5 (Task 5): 1966-1970 fill (no DOE row exists for these five dates)
`data/sf_turnout_history_doe_1899_2019.csv` has no row at all for 1966-06-07,
1966-11-08, 1968-06-04, 1970-06-02, or 1970-11-03 (a gap in the DOE table, not
a DOE-vs-SOV disagreement), so these are pure "fill" entries: the SOV is the
only certified source. Method note: for all five, the figure recorded is the
SOV's own county **total vote / total ballots cast** summary line (from the
"Registration - Vote - Percentages" / "Vote Percentage" table), not a single
contest's sum (confirmed by internal SOV arithmetic: registration components
sum to the printed registration total; precinct + absentee = the printed
total). Full page-by-page notes: `.superpowers/sdd/task-5-notes/page_readings.md`
(not committed; scratch working notes, screenshots of each SOV page included).

| Election | SF certified total (Total vote/ballots cast) | Registration | SOV volume + page |
|---|---|---|---|
| 1966-06-07 Primary | 226,622 | 355,271 | [californiastate196668cali, p. n11](https://archive.org/details/californiastate196668cali/page/n11) |
| 1966-11-08 General | 286,049 | 372,123 | [californiastate196668cali, p. n47](https://archive.org/details/californiastate196668cali/page/n47) |
| 1968-06-04 Primary | 254,825 | 348,111 | [californiastate196668cali, p. n151](https://archive.org/details/californiastate196668cali/page/n151) |
| 1970-06-02 Primary | 214,943 | 337,127 | [statementofvote197072cali, p. n11](https://archive.org/details/statementofvote197072cali/page/n11) |
| 1970-11-03 General | 262,398 | 372,032 | [statementofvote197072cali, p. n54](https://archive.org/details/statementofvote197072cali/page/n54) |

Cross-checked each general's top contest (Governor) against Wikipedia's
by-county table, which independently cites the same SOV pages: 1966-11-08
Reagan 114,796 + Brown 164,435 + Scattering 341 = 279,572 (< 286,049 total, as
expected: a contest sum is always a floor under the true ballots-cast total);
1970-11-03 Reagan 106,606 + Unruh 140,829 + Romo 3,958 + Shearer 2,625 =
254,018 (< 262,398 total, as expected).

**Source inconsistency flagged (internal to the SOV):** the 1968-06-04
primary's printed "Percentage" column for San Francisco reads 66.34, but
254,825 (Total vote cast) ÷ 348,111 (Total registration) = 73.21%. Every
neighboring county on the same printed page has a percentage that reconciles
exactly against its own printed total/registration (San Diego 71.23%,
Sacramento 73.14%, San Bernardino 69.72%, etc.), and only San Francisco's
percentage cell is off, while its own total-vote and registration cells are
each independently confirmed (registration components sum correctly; precinct
+ absentee sum correctly). This is the same class of anomaly already logged
for 1952-11-04 above ("Source inconsistency (internal to the SOV)"); the
254,825 total-vote-cast figure is used as certified regardless.

## Pre-1908: NO digitized SOV — use California Blue Book / State Roster
The digitized SOV series with SF-county breakdowns effectively starts 1908. For
pre-1908 statewide elections the certified source of truth is the **California
Blue Book / State Roster** (CA Secretary of State), on HathiTrust & archive.org
(e.g. `california-blue-book-1903-sfg`). Wikipedia "19xx ... in California" by-county
tables cite these.

### Pre-1906 certified figures gathered (Blue Book) — night counts pending ezproxy re-login
| Election | SF certified (contest) | Source | Night count |
|---|---|---|---|
| 1904-11-08 Pres | 65,427 (Roosevelt 39,816+Parker 18,027+Debs 7,250+Swallow 334) | Blue Book 1907 pp.419-422 (HathiTrust uiuo.ark:/13960/t8kd5fq60) | BLOCKED (session expired) |
| 1902-11-04 Gov | 60,067 (Pardee 24,106+Lane 33,743+Brower 1,993+Kanouse 164) | Blue Book 1903 p.332 (archive.org california-blue-book-1903-sfg) | 59,040 @320/320 from Nov 6 (2-day); Nov 5 election-night paper had SF BLANK ("only a small % by midnight") → election-night share ~0 (slow hand count) |
| 1900-11-06 Pres | 63,202 (McKinley 35,208+Bryan 25,212+Debs 2,030+Woolley 275+scat 477) | Blue Book 1903 pp.311-314 | BLOCKED |
| 1898-11-08 Gov | 54,372 (Gage 28,218+Maguire 24,632+Harriman 1,388+McComas 134) | Blue Book 1899 p.227 (HathiTrust mdp.39015041451256) | BLOCKED |
| 1896-11-03 Pres | (incomplete — agent stalled on dead session) | — | BLOCKED |

TODO pre-1906 (needs ezproxy re-login for night counts): capture day-after (and 2-day)
Chronicle for 1896,1898,1900,1904 (1902 partly done); then 1886-1894 generals;
municipals 1899/1901/1903/1905. Certified for those via Blue Book.
