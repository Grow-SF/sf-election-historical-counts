# SF Department of Elections — data discrepancy register

Discrepancies found between the **SF Department of Elections** historical turnout
table (`data/sf_turnout_history_doe_1899_2019.csv`) and the authoritative
**California Secretary of State Statement of Vote (SOV)** — the official certified
canvass, digitized & public on archive.org. Established by the SOV cross-check
(see `data/sov_crosscheck_ledger.md` and skill `sov-certified-turnout`).

**Verdict legend:** `DOE WRONG` · `WE WERE WRONG` · `SOV ANOMALY` (internal SOV
inconsistency) · `POTENTIAL` (flagged, unresolved).
**Our data corrected:** has the value been fixed in *our* dataset.
**DOE notified / DOE corrected:** whether reported to the SF DOE and whether
*their* published table has been corrected (we cannot edit it).

## Summary

| Election | DOE figure | Authoritative (SOV) | Verdict | Our data | DOE notified | DOE corrected |
|---|---|---|---|---|---|---|
| 1908-11-03 | 41,137 | SF President **60,124** | **DOE WRONG** | ✅ →60,124; 88.6→60.6% | ☐ | ☐ |
| 1934-11-06 | 166,133 | SF Governor **225,977** | **DOE WRONG** | ✅ →225,977; 100→97.7% | ✉️ draft | ☐ |
| 1978-11-07 | 217,965 | SF total cast **238,667** | **DOE WRONG** (precinct-only) | ✅ →238,667; 100→93.5% | ☐ | ☐ |
| 1974-06-04 | 198,508 | SF total cast **198,508** | **WE WERE WRONG** | ✅ our 203,381→198,508 | n/a | n/a |
| 1952-11-04 | 365,972 | turnout 365,972; contest 374,700 | **SOV ANOMALY** | ☐ keep 365,972 | n/a | n/a |

## Detail

### 1908-11-03 — DOE WRONG
- **DOE figure / source:** 41,137 ballots cast (54.51%) — DOE historical turnout table (`sf_turnout_history_doe_1899_2019.csv`).
- **Authoritative:** SF County President = **60,124** (Taft 33,184 + Bryan 21,260 + Debs 4,523 + Hisgen 751 + Chafin 406). Source: [CA SoS *Statement of Vote*, Nov 3 1908 (archive.org)](https://archive.org/details/statementofvo19081922cali/page/n5) · cross-ref [Wikipedia: 1908 U.S. presidential election in California](https://en.wikipedia.org/wiki/1908_United_States_presidential_election_in_California).
- **Why an error:** the President contest alone (60,124) exceeds DOE's stated total ballots cast (41,137) — impossible. True turnout ≥ 60,124 (~80% of 75,467 registered).
- **Resolution:** DOE WRONG. `certified_final` 41,137 → 60,124; recovered night count 36,450 ÷ 60,124 = **60.6%** (was a phantom 88.6%). **Prose impact:** the article's "≈89% in 1908" was computed against the bad denominator — flagged for correction.
- **DOE corrected:** no — should be reported.

### 1934-11-06 — DOE WRONG
- **DOE figure / source:** 166,133 ballots cast (57.15%) — DOE turnout table.
- **Authoritative:** SF County Governor = **225,977** (Merriam 115,047 + Sinclair 87,850 + Haight 21,499). Source: [CA SoS *Statement of Vote*, Nov 6 1934 (archive.org)](https://archive.org/details/statementofvote192639cali/page/n591) · cross-ref [Wikipedia: 1934 California gubernatorial election](https://en.wikipedia.org/wiki/1934_California_gubernatorial_election).
- **Why an error:** Governor contest (225,977) far exceeds DOE's total (166,133). True turnout ~226k+ (~76% of 290,683) — consistent with the high-turnout 1934 EPIC/Sinclair race.
- **Resolution:** DOE WRONG. `certified_final` 166,133 → 225,977; night-share 100 → 97.7%.
- **DOE corrected:** no — **email to DOE drafted**.

### 1978-11-07 — DOE WRONG (precinct-only)
- **DOE figure / source:** 217,965 ballots cast — DOE turnout table.
- **Authoritative:** SF County "Total Votes Cast" = **238,667** (Precinct 217,965 + Absentee 20,702; Governor sum 225,465). Source: [CA SoS *Statement of Vote*, Nov 7 1978 (archive.org)](https://archive.org/details/statementofvote197879cali/page/n245) · cross-ref [Wikipedia: 1978 California gubernatorial election](https://en.wikipedia.org/wiki/1978_California_gubernatorial_election).
- **Why an error:** DOE's 217,965 is exactly the SOV's **precinct-vote** column — it omits the 20,702 absentees. (Worth checking other years for this precinct-only pattern.)
- **Resolution:** DOE WRONG. `certified_final` 217,965 → 238,667; night-share 100 → 93.5%.
- **DOE corrected:** no — should be reported.

### 1974-06-04 — WE WERE WRONG
- **DOE figure / source:** 198,508 ballots cast — DOE turnout table.
- **Authoritative:** SF County Total vote = **198,508** (precinct 185,634 + absentee 12,874) — **= DOE exactly**. Source: [CA SoS *Statement of Vote*, Primary June 4 1974 (archive.org)](https://archive.org/details/statementofvote197374cali/page/n45).
- **Why flagged:** *our* recovered day-2 figure (Prop B 203,381, a city measure) exceeded the certified turnout — impossible; a wrong-source/misread on our side.
- **Resolution:** WE WERE WRONG. Our complete-count figure 203,381 → 198,508. DOE was correct.

### 1952-11-04 — SOV ANOMALY (DOE consistent)
- **DOE figure / source:** 365,972 ballots cast — DOE turnout table.
- **Authoritative:** [CA SoS *Statement of Vote*, Nov 4 1952 (archive.org)](https://archive.org/details/stateofcaliforn195262cali/page/n46): SF "Total Vote Cast" = **365,972** (= DOE exactly), **but** the SOV's own presidential detail sums to **374,700** (Eisenhower 198,158 + Stevenson 172,312 + …) — contest detail exceeds the SOV's stated turnout line. Cross-ref [Wikipedia: 1952 U.S. presidential election in California](https://en.wikipedia.org/wiki/1952_United_States_presidential_election_in_California).
- **Resolution:** Not a DOE error — DOE matches the SOV's printed turnout line; the inconsistency is internal to the 1952 SOV. Kept DOE 365,972; anomaly documented.

## Verified consistent (cross-checked, no discrepancy)
Generals where DOE turnout is consistent with the SOV (DOE ≥ SOV contest sum; for
**1914, 1918, 1956, 1960** DOE = the SOV's printed "total vote cast" line exactly).
All cite the [CA Statement of Vote series on archive.org](https://archive.org/search?query=title%3A%28statement+of+vote%29+California) with the per-row volume + page recorded in `sf_archival_canvass_points.csv`:

| Election | SOV figure | DOE | SOV source |
|---|---|---|---|
| 1910-11-08 G | Gov 59,182 | 59,724 | [archive.org 1908-22](https://archive.org/details/statementofvo19081922cali) |
| 1912-11-05 P | Pres 101,148 | 105,646 | [archive.org n35](https://archive.org/details/statementofvo19081922cali/page/n35) |
| 1914-11-03 G | Gov 132,103 / cast 134,492 | 134,492 | [archive.org n71](https://archive.org/details/statementofvo19081922cali/page/n71) |
| 1916-11-07 P | Pres 149,152 | 155,747 | [archive.org 1908-22](https://archive.org/details/statementofvo19081922cali) |
| 1918-11-05 G | Gov 100,382 / cast 103,011 | 103,011 | [archive.org 1908-22](https://archive.org/details/statementofvo19081922cali) |
| 1920-11-02 P | Pres 147,450 | 154,592 | [archive.org n313](https://archive.org/details/statementofvo19081922cali/page/n313) |
| 1922-11-07 G | Gov 132,225 | 134,503 | [archive.org p12](https://archive.org/details/statementofvo19081922cali/page/12) |
| 1924-11-04 P | Pres 153,950 | 159,649 | [archive.org n99](https://archive.org/details/statementofvote192430cali/page/n99) |
| 1926-11-02 G | Gov 125,301 | 130,835 | [archive.org n205](https://archive.org/details/statementofvote192430cali/page/n205) |
| 1928-11-06 P | Pres 195,468 | 199,665 | [archive.org n235](https://archive.org/details/statementofvote192639cali/page/n235) |
| 1932-11-08 P | Pres 223,197 | 227,283 | [archive.org n523](https://archive.org/details/statementofvote192639cali/page/n523) |
| 1936-11-03 P | Pres 265,001 | 269,387 | [archive.org n739](https://archive.org/details/statementofvote192639cali/page/n739) |
| 1938-11-08 G | Gov 248,035 | 257,597 | [archive.org n849](https://archive.org/details/statementofvote192639cali/page/n849) |
| 1940-11-05 P | Pres 311,878 | 315,518 | [archive.org n109](https://archive.org/details/stateofcaliforn194050cali/page/n109) |
| 1942-11-03 G | Gov 226,560 | 230,129 | [archive.org n193](https://archive.org/details/stateofcaliforn194050cali/page/n193) |
| 1946-11-05 G | Gov 239,116 | 270,457 | [archive.org n338](https://archive.org/details/stateofcaliforn194050cali/page/n338) |
| 1948-11-02 P | Pres 350,709 | 359,134 | [archive.org 1940-50](https://archive.org/details/stateofcaliforn194050cali) |
| 1956-11-06 P | Pres 336,967 / cast 342,652 | 342,652 | [archive.org n189](https://archive.org/details/stateofcaliforn195262cali/page/n189) |
| 1960-11-08 P | Pres 342,219 / cast 348,290 | 348,290 | [archive.org n327](https://archive.org/details/stateofcaliforn195262cali/page/n327) |
| 1964-11-03 P | Pres 323,908 | 331,612 | [archive.org 1962-64](https://archive.org/details/castatem196264cali) |

Primaries 1948–1960 certified turnout pulled from the SOV (see `sf_archival_canvass_points.csv`).

## Still to cross-check
1962/1928/1930/1932 primaries; modern DOE figures 1968–2014 (lower priority — our
exact per-release data already matches DOE). Pre-1906 elections: see open question.
