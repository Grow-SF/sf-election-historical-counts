# Turnout-table discrepancies — notes for investigation

While cross-checking the **SF Department of Elections** historical turnout table
(`data/sf_turnout_history_doe_1899_2019.csv`) against the **California Secretary of
State Statement of Vote (SOV)** — the certified canvass we use as our reference,
digitized and public on archive.org — we noticed a few figures that don't reconcile.

We're **not asserting the DOE table is in error.** Any of these could be our own
misreading, a difference in what each source counts, or a transcription slip on
either side. Each item below simply needs a closer look, and where relevant we'd
welcome the Department's input. (Method: see `data/sov_crosscheck_ledger.md` and the
`sov-certified-turnout` skill.)

**Status legend:** `Under review — figures don't reconcile` · `Resolved — our error,
fixed` · `Source inconsistency (internal to the SOV)` · `Open question`.
**Our data:** the value we currently use in *our* dataset — where a figure doesn't
reconcile we adopt the SOV figure, pending confirmation.
**Raised with DOE / DOE updated:** whether we've flagged it to the SF DOE, and
whether *their* published table has since changed (we can't edit it ourselves).

## Summary

| Election | DOE figure | SOV reference | Status | Our data | Raised with DOE | DOE updated |
|---|---|---|---|---|---|---|
| 1908-11-03 | 41,137 | SF President **60,124** | Under review — figures don't reconcile | →60,124; 88.6→60.6% | ☐ | ☐ |
| 1934-11-06 | 166,133 | SF Governor **225,977** | Under review — figures don't reconcile | →225,977; 100→97.7% | ✉️ draft | ☐ |
| 1978-11-07 | 217,965 | SF total cast **238,667** | Under review — looks precinct-only | →238,667; 100→93.5% | ☐ | ☐ |
| 1968-06-04 | (no DOE row) | SOV total cast **254,825**; Chronicle unofficial complete **262,449** | Open question (SOV internal pct anomaly + newspaper conflict) | keep 254,825 | n/a | n/a |
| 1899-12-02 | 70,726 / 22,331 dated Dec 2 | Municipal Reports: **Dec 29, 1899** sewer-bond special, same figures | Under review — date error, figures correct | date fixed to 1899-12-29 | ☐ | ☐ |
| 1974-06-04 | 198,508 | SF total cast **198,508** | Resolved — our error, fixed | our 203,381→198,508 | n/a | n/a |
| 1952-11-04 | 365,972 | turnout 365,972; contest 374,700 | Source inconsistency (internal to the SOV) | keep 365,972 | n/a | n/a |

## Detail

### 1908-11-03 — figures don't reconcile (under review)
- **DOE figure / source:** 41,137 ballots cast (54.51%) — DOE historical turnout table (`sf_turnout_history_doe_1899_2019.csv`).
- **SOV reference:** SF County President = **60,124** (Taft 33,184 + Bryan 21,260 + Debs 4,523 + Hisgen 751 + Chafin 406). Source: [CA SoS *Statement of Vote*, Nov 3 1908 (archive.org)](https://archive.org/details/statementofvo19081922cali/page/n5) · cross-ref [Wikipedia: 1908 U.S. presidential election in California](https://en.wikipedia.org/wiki/1908_United_States_presidential_election_in_California).
- **What we noticed:** the President contest alone (60,124) is larger than the table's total ballots cast (41,137). A single contest can't exceed total turnout, so the table figure looks low — most likely a transcription slip, but worth confirming. (True turnout would be ≥ 60,124, ~80% of 75,467 registered.)
- **How we've handled it:** for our dataset we use the SOV figure — `certified_final` 41,137 → 60,124; recovered night count 36,450 ÷ 60,124 = **60.6%** (rather than a phantom 88.6%). **Prose impact:** the article's "≈89% in 1908" had been computed against the lower denominator — since corrected.
- **Raised with DOE:** not yet — worth raising.

### 1934-11-06 — figures don't reconcile (under review)
- **DOE figure / source:** 166,133 ballots cast (57.15%) — DOE turnout table.
- **SOV reference:** SF County Governor = **225,977** (Merriam 115,047 + Sinclair 87,850 + Haight 21,499). Source: [CA SoS *Statement of Vote*, Nov 6 1934 (archive.org)](https://archive.org/details/statementofvote192639cali/page/n591) · cross-ref [Wikipedia: 1934 California gubernatorial election](https://en.wikipedia.org/wiki/1934_California_gubernatorial_election).
- **What we noticed:** the Governor contest (225,977) is well above the table's total (166,133) — and turnout in the high-interest 1934 EPIC/Sinclair race was very high (~226k, ~76% of 290,683 registered), so the table figure looks low. Worth confirming.
- **How we've handled it:** use the SOV figure — `certified_final` 166,133 → 225,977; night-share 100 → 97.7%.
- **Raised with DOE:** a note to the Department is drafted.

### 1978-11-07 — looks precinct-only (under review)
- **DOE figure / source:** 217,965 ballots cast — DOE turnout table.
- **SOV reference:** SF County "Total Votes Cast" = **238,667** (Precinct 217,965 + Absentee 20,702; Governor sum 225,465). Source: [CA SoS *Statement of Vote*, Nov 7 1978 (archive.org)](https://archive.org/details/statementofvote197879cali/page/n245) · cross-ref [Wikipedia: 1978 California gubernatorial election](https://en.wikipedia.org/wiki/1978_California_gubernatorial_election).
- **What we noticed:** DOE's 217,965 matches the SOV's **precinct-vote** column exactly, which suggests it may not include the 20,702 absentee ballots. (Worth checking other years for the same pattern.)
- **How we've handled it:** use the total-cast figure — `certified_final` 217,965 → 238,667; night-share 100 → 93.5%.
- **Raised with DOE:** not yet — worth raising.

### 1968-06-04 - open question (SOV internal anomaly plus a conflicting newspaper complete count)
- **DOE figure / source:** none; this primary has no row in the DOE historical turnout table.
- **SOV reference:** SF County total vote cast = **254,825** (registration 348,111). Source: CA SoS *Statement of Vote*, Primary June 4 1968, [archive.org page n151](https://archive.org/details/californiastate196668cali/page/n151). The SOV's own printed percentage column for SF (66.34) does not reconcile with its printed total and registration (254,825/348,111 = 73.21%), while every neighboring county's percentage reconciles exactly; see `data/sov_crosscheck_ledger.md` (Batch 5).
- **Newspaper reference:** SF Chronicle, June 7 1968, p30, "S.F. COUNT - SLOWEST IN 4 DECADES": completed unofficial count as of 9:45 p.m. June 6, "**262,449** ballots cast" against 349,078 registered, with 6,437 absentees hand-counted. That figure EXCEEDS the SOV certified total by 7,624.
- **What we noticed:** three mutually inconsistent figures (the SOV pct column implies about 230,937; the SOV total prints 254,825; the paper's unofficial complete count is 262,449). Context: the June 1968 count was a documented operational failure (the Chronicle's "Voting Foul-up In S.F." reports the new computer tabulation system's debacle: 30 machines mishandled, tally sheets found in City Hall basement suitcases, one polling place firebombed), so a downward revision between the June 6 unofficial figure and the official canvass is plausible, but unverified.
- **How we've handled it:** we keep the SOV total (254,825) as `certified_final`, pending resolution; the only night observation ingested (Prop A sum 112,468, flagged night_partial) is below every candidate denominator, so its floor status is safe either way. The city Statement of Vote volume at the SFPL History Center ("Statement of Vote 1906-1979") should settle it.
- **Raised with DOE:** not applicable (no DOE row); worth checking the SFPL volume.

### 1899-12-02 - date error in the DOE table (figures correct)
- **DOE figure / source:** 70,726 registered / 22,331 ballots, dated December 2, 1899 - DOE historical turnout table.
- **Municipal Reports reference:** the Dept. of Elections cumulative registration-and-votes table (SF Municipal Reports FY1907-08, p.871, archive.org sanfranciscomuni57sanfrich; cross-verified against the vols 49/53/55 printings) records a **December 29, 1899** sewer-bond special with exactly these figures. No December 2 election exists in the city record; a companion December 27, 1899 park-bond special (70,681 / 29,972) has no DOE row at all.
- **How we've handled it:** `build_viz_data.py` re-dates the DOE row to 1899-12-29 (DOE_TABLE_DATE_FIXES); the Dec 27 special is added from the Municipal Reports table (`data/sf_turnout_1891_1907.csv`). A second omission found the same way: the December 4, 1902 charter-amendments special (14,271 ballots), also absent from the DOE table.
- **Raised with DOE:** not yet - worth raising along with the omissions.

### 1974-06-04 — our error (fixed)
- **DOE figure / source:** 198,508 ballots cast — DOE turnout table.
- **SOV reference:** SF County total vote = **198,508** (precinct 185,634 + absentee 12,874) — **matches DOE exactly**. Source: [CA SoS *Statement of Vote*, Primary June 4 1974 (archive.org)](https://archive.org/details/statementofvote197374cali/page/n45).
- **What we noticed:** *our* recovered day-2 figure (Prop B 203,381, a city measure) exceeded the certified turnout — a wrong-source/misread on our side. The DOE figure was right.
- **How we've handled it:** corrected our complete-count figure 203,381 → 198,508.

### 1952-11-04 — source inconsistency (internal to the SOV)
- **DOE figure / source:** 365,972 ballots cast — DOE turnout table.
- **SOV reference:** [CA SoS *Statement of Vote*, Nov 4 1952 (archive.org)](https://archive.org/details/stateofcaliforn195262cali/page/n46): SF "Total Vote Cast" = **365,972** (= DOE exactly), **but** the SOV's own presidential detail sums to **374,700** (Eisenhower 198,158 + Stevenson 172,312 + …) — the contest detail exceeds the SOV's own stated turnout line. Cross-ref [Wikipedia: 1952 U.S. presidential election in California](https://en.wikipedia.org/wiki/1952_United_States_presidential_election_in_California).
- **How we've handled it:** this isn't a DOE discrepancy — DOE matches the SOV's printed turnout line; the inconsistency is internal to the 1952 SOV. We kept DOE's 365,972 and noted the anomaly.

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
