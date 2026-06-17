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

## DOE error pattern found
DOE's `sf_turnout_history_doe_1899_2019.csv` has real errors in the early/mid
record — at least one looks systematic (1978: DOE = precinct-only, dropped
absentees). Cross-check verdicts below.

## Cross-check results (✓=DOE ok, ✗=DOE wrong, ⚠=our data fixed)
| Election | SOV SF (contest / turnout) | DOE | verdict | action |
|---|---|---|---|---|
| 1908-11-03 P | President 60,124 (turnout ≥) | 41,137 | ✗ DOE too low | certified→60,124; night-share 88.6→**60.6%** |
| 1910-11-08 G | Governor 59,182 | 59,724 | ✓ (turnout≈) | keep 59,724 + SOV cite |
| 1912-11-05 P | President 101,148 | 105,646 | ✓ | keep + SOV cite |
| 1916-11-07 P | President 149,152 | 155,747 | ✓ | keep + SOV cite |
| 1920-11-02 P | President 147,450 | 154,592 | ✓ | keep + SOV cite |
| 1934-11-06 G | Governor 225,977 (turnout≥) | 166,133 | ✗ DOE too low | certified→225,977; night 97.7% (done earlier) |
| 1958-11-04 G | turnout 319,179 (Gov 309,969) | (none) | fill | certified→319,179; 100→**99.9%** |
| 1962-11-06 G | Governor 287,463 | (none) | fill | certified→287,463 (done earlier) |
| 1974-06-04 Pr| turnout 198,508 | 198,508 | ✓ DOE | ⚠ our day-2 Prop B 203,381 exceeded turnout → fixed to 198,508 |
| 1978-11-07 G | turnout 238,667 (Gov 225,465) | 217,965 | ✗ DOE precinct-only | certified→238,667; 100→**93.5%** |

## ⚠ Prose impact
- `index.mdx` era-1 says "≈85–89% in 1908 and 1912." **1908 is now ~61%** (was
  computed against DOE's bad 41,137). The 1908 example must be corrected — the
  hand-era "light-ballot fast morning" claim should lean on 1912 (still high) and
  the 1928+ machine era, not 1908. (User edits prose.)

## TODO — remaining statewide cross-checks
Generals: 1914, 1918, 1922, 1924, 1926, 1928, 1930, 1932, 1936, 1938, 1940,
1942, 1946, 1948, 1952, 1956, 1960, 1964. Primaries: 1928, 1930, 1932, 1948,
1950, 1952, 1954, 1956, 1958, 1960, 1962, 1964. (Municipals/specials: N/A.)
Also: modern DOE figures 1968–2014 (lower priority; our exact data matches).

## Batch 2 & 3 results (generals 1914-1960) — ALL DOE-consistent
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

Generals cross-check COMPLETE 1908-1960 (1944 skipped). DOE errors: 1908, 1934, 1978.
Remaining: 1964 general; 1948-1964 primaries.

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
