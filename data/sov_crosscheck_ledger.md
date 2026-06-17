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
