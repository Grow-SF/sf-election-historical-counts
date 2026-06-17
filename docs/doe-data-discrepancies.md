# SF Department of Elections — data discrepancy register

Discrepancies found between the **SF Department of Elections** historical turnout
table (`data/sf_turnout_history_doe_1899_2019.csv`) and the authoritative
**California Secretary of State Statement of Vote (SOV)** — the official certified
canvass, digitized & public on archive.org. Established by the SOV cross-check
(see `data/sov_crosscheck_ledger.md` and skill `sov-certified-turnout`).

**Verdict legend:** `DOE WRONG` · `WE WERE WRONG` · `SOV ANOMALY` (internal SOV
inconsistency) · `POTENTIAL` (flagged, unresolved).
**Our data corrected:** has the value been fixed in *our* dataset.
**DOE notified / DOE corrected:** whether the error has been reported to the SF
DOE and whether *their* published table has been corrected (we cannot edit it).

## Summary

| Election | DOE figure | Authoritative (SOV) | Verdict | Our data corrected | DOE notified | DOE corrected |
|---|---|---|---|---|---|---|
| 1908-11-03 | 41,137 ballots cast | SF **President 60,124** (turnout ≥) | **DOE WRONG** (impossible — a single contest exceeds stated turnout) | ✅ certified→60,124; night-share 88.6→60.6% | ☐ not yet | ☐ no |
| 1934-11-06 | 166,133 ballots cast | SF **Governor 225,977** (turnout ≥) | **DOE WRONG** (Governor alone > DOE turnout) | ✅ certified→225,977; night-share 100→97.7% | ✉️ email drafted | ☐ no |
| 1978-11-07 | 217,965 ballots cast | SF **total cast 238,667** (precinct 217,965 + absentee 20,702) | **DOE WRONG** (DOE = precinct-only; dropped 20,702 absentees) | ✅ certified→238,667; night-share 100→93.5% | ☐ not yet | ☐ no |
| 1974-06-04 | 198,508 ballots cast | SF **total cast 198,508** (= DOE exactly) | **WE WERE WRONG** (our recovered day-2 "Prop B" 203,381 exceeded certified turnout) | ✅ our figure→198,508 | n/a (DOE correct) | n/a |
| 1952-11-04 | 365,972 ballots cast | SF "total vote cast" 365,972 (= DOE) **but** President contest sum 374,700 > that | **SOV ANOMALY** (SOV's own turnout line < its presidential contest sum; DOE matches the SOV turnout line) | ☐ keep DOE 365,972 (consistent w/ SOV turnout line); anomaly noted | n/a | n/a |

## Detail

### 1908-11-03 — DOE WRONG
- **DOE figure / source:** 41,137 ballots cast, 54.51% turnout — `sf_turnout_history_doe_1899_2019.csv` (the DOE's published historical turnout table).
- **Authoritative:** CA SoS *Statement of Vote, Nov 3 1908*, SF County President = **60,124** (Taft 33,184 + Bryan 21,260 + Debs 4,523 + Hisgen 751 + Chafin 406). archive.org `statementofvo19081922cali` p.n5; cross-ref Wikipedia "1908 US presidential election in California."
- **Why it's an error:** the presidential contest alone (60,124) exceeds DOE's stated *total ballots cast* (41,137), which is impossible. True turnout ≥ 60,124 (~80% of 75,467 registered).
- **Resolution:** DOE WRONG. Our `certified_final` corrected 41,137 → 60,124; the recovered 1908 night count (36,450) ÷ 60,124 = **60.6%** (was a phantom 88.6% against the bad denominator). **Prose impact:** the article's "≈89% in 1908" claim was based on the bad denominator — flagged for correction.
- **DOE corrected:** no — should be reported.

### 1934-11-06 — DOE WRONG
- **DOE figure / source:** 166,133 ballots cast, 57.15% — DOE turnout table.
- **Authoritative:** CA SoS *Statement of Vote, Nov 6 1934*, SF County Governor = **225,977** (Merriam 115,047 + Sinclair 87,850 + Haight 21,499). archive.org `statementofvote192639cali` p.n591; cross-ref Wikipedia "1934 California gubernatorial election."
- **Why it's an error:** the Governor contest (225,977) far exceeds DOE's stated total ballots cast (166,133). True turnout ~226k+ (~76% of 290,683 registered) — consistent with the high-turnout 1934 EPIC/Sinclair race.
- **Resolution:** DOE WRONG. `certified_final` corrected 166,133 → 225,977; night-share 100→97.7%.
- **DOE corrected:** no — **email to DOE drafted** (recommends they reconcile to the SOV / their canvass).

### 1978-11-07 — DOE WRONG (precinct-only)
- **DOE figure / source:** 217,965 ballots cast — DOE turnout table.
- **Authoritative:** CA SoS *Statement of Vote, Nov 7 1978*, SF County "Total Votes Cast" = **238,667** (Precinct Vote 217,965 + Absentee Vote 20,702). archive.org `statementofvote197879cali` p.n245.
- **Why it's an error:** DOE's 217,965 is exactly the SOV's **precinct-vote** column — it omits the 20,702 absentee ballots. Certified total turnout = 238,667.
- **Resolution:** DOE WRONG (systematic-looking: precinct-only). `certified_final` corrected 217,965 → 238,667; night-share 100→93.5%. (Worth checking other years for the same precinct-only pattern.)
- **DOE corrected:** no — should be reported.

### 1974-06-04 — WE WERE WRONG
- **DOE figure / source:** 198,508 ballots cast — DOE turnout table.
- **Authoritative:** CA SoS *Statement of Vote, Primary June 4 1974*, SF County Total vote = **198,508** (precinct 185,634 + absentee 12,874). archive.org `statementofvote197374cali` p.n45. **= DOE exactly.**
- **Why it flagged:** *our* recovered day-2 figure (Prop B "Conflicts of Interest" 203,381) exceeded the certified turnout — impossible; a misread / wrong-source city-measure figure on our side.
- **Resolution:** WE WERE WRONG. Our complete-count figure corrected 203,381 → 198,508. DOE was correct.

### 1952-11-04 — SOV ANOMALY (DOE consistent)
- **DOE figure / source:** 365,972 ballots cast — DOE turnout table.
- **Authoritative:** CA SoS *Statement of Vote, Nov 4 1952*: SF "Total Vote Cast" summary = **365,972** (= DOE exactly), **but** the SOV's own presidential-electors detail sums to **374,700** (Eisenhower 198,158 + Stevenson 172,312 + …) — i.e. the contest detail exceeds the SOV's stated turnout line. archive.org `stateofcaliforn195262cali` (turnout n46; President n47–n53).
- **Resolution:** Not a DOE error — DOE matches the SOV's printed turnout line. The inconsistency is internal to the 1952 SOV (summary "total vote cast" compiled differently from the candidate detail, which includes all absentee/armed-forces ballots). Kept DOE 365,972; anomaly documented.

## Verified consistent (cross-checked, no discrepancy)
Generals where DOE turnout is consistent with the SOV (DOE ≥ SOV contest sum, the
normal undervote relationship; for 1914/1918/1956/1960 DOE = the SOV's printed
"total vote cast" line exactly): **1910, 1912, 1914, 1916, 1918, 1920, 1922,
1924, 1926, 1928, 1930*, 1932, 1936, 1938, 1940, 1942, 1946, 1948, 1956, 1960.**
(*1930 via the 1928/1930 cross-checks.) Citations recorded per row in
`sf_archival_canvass_points.csv`.

## Still to cross-check
1964 general; the 1948–1964 statewide primaries; modern DOE figures 1968–2014
(lower priority — our exact per-release data already matches DOE).
