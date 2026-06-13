# Extending the election-night floor to 1899

**Phase 0 findings** for the plan
[`2026-06-13-extend-to-1899.md`](../superpowers/plans/2026-06-13-extend-to-1899.md).
Goal: push the night-share floor back from 1960 to 1899.

## The gating fact: absentee voting was negligible before 1964

The floor method (`docs/archive-recovery-runbook.md`, "in-person diamond") is:
in-person ballots are counted on election night, so the non-absentee share of
the certified total bounds the night share from below. For 1964+ the project
computes it from the DOE turnout table's `precinct`/`mail` split. Before 1964
those columns are `n/a`, so the floor was never extended back.

But we don't need the per-election split: **California absentee voting was a
low-single-digit share of the vote throughout this era**, so in-person ≈ total
and the night floor is ~94–98%. Evidence:

| Year | Absentee share of CA vote (statewide) |
|---|---|
| 1962 | **2.63%** (earliest year in the CA SoS series) |
| 1964 | 4.21% |
| 1968 | 4.54% |
| 1972 | 4.72% (general) |
| 1976 | 4.50% |
| 1980 | 6.26% |

- Earliest year the CA Secretary of State publishes absentee usage is **1962,
  at 2.63%** — and absentee stayed **below 7% through 1980**.
- California did not allow **no-excuse** absentee voting until **1978**; before
  that it was excuse-required (travel, illness, military) and witnessed, so the
  pre-1962 share was lower still — there is no reason to think 1899–1960 SF
  exceeded the 2.6% seen in 1962.
- SF cross-check from the project's own data: the **1964** SF non-absentee
  share is **94.4%** (mail 18,478 / 348,290 cast → 5.6% absentee, slightly above
  statewide, as expected for an urban county). Every earlier year had *less*
  absentee, so **94.4% is a safe, conservative flat floor for 1899–1960** — the
  true night share was higher.

Sources:
- CA Secretary of State, *Historical Vote-By-Mail (Absentee) Ballot Use in
  California* — https://www.sos.ca.gov/elections/historical-absentee
- Background on the 1978 no-excuse change and 1962+ series start: TIME, *Voting
  By Mail History*; AEI, *Absentee and Early Voting*.

**Decision.** Pre-1964 elections get a conservative night floor of **94.4%**
(= the 1964 SF non-absentee share; every earlier year had less absentee),
labelled distinctly so it is never confused with a measured precinct split:
`method = in-person floor (absentee ≤ 1964 SF level; era estimate)`. Phase 2
newspaper recovery upgrades sampled years to their actual (higher) night share.

## Implementation discovery

`scripts/build_viz_data.py` computes the floor **live from precinct/absentee
splits** (three sources: `sf_turnout_history_1960_2002.csv`,
`sf_vbm_share_sos.csv`, and the `precinct` column of the DOE 1899–2019 table —
the last filtered to rows where `mail != "n/a"`, i.e. 1964+). The committed
`data/sf_night_floor_1964_2026.csv` is a **derived artifact**, not a build
input. So extending to 1899 means **adding a new floor source** for the
`mail == "n/a"` pre-1964 rows, not editing the turnout table.

## Target elections (denominators already in hand)

All 30 are already in `data/sf_turnout_history_doe_1899_2019.csv` with a
certified `ballots_cast`. 1960 already has a recovered canvass point
(Nixon+Kennedy = 318,462), so **29 are genuinely new**:

1899-12-02, 1902-12-02, 1903-09-29, 1903-10-08, 1908-11-03, 1910-11-01,
1912-11-05, 1914-11-03, 1916-11-07, 1918-11-05, 1920-11-02, 1922-11-07,
1924-11-04, 1926-11-02, 1928-11-06, 1930-11-04, 1932-11-08, 1934-11-06,
1936-11-03, 1938-11-08, 1940-11-05, 1942-11-03, 1944-11-07, 1946-11-05,
1948-11-02, 1950-11-07, 1952-11-04, 1954-11-02, 1956-11-06, (1960-11-08).

## Phase 2 finding (2026-06-13): the hand-count era was ALSO slow

**First newspaper cross-check overturns the Phase-1 premise.** The morning-after
SF Chronicle for the 1916 presidential general (Wed 1916-11-08, 3 A.M. edition;
scans `mirror/newsbank/scans/sweep_19161107_issue19161108_p2_s0.png` and
`_s1.png`) shows the count was far from complete on election night:

- Turnout was essentially full ("160,000 VOTE IN S.F. NEW RECORD; 100,000
  Ballots in Boxes at 1 P.M." vs. certified 155,747 cast) — but that is ballots
  *cast*, not *counted*.
- President: "He was ahead by 1400 votes, with **virtually none of San
  Francisco's** nor Los Angeles' vote at hand."
- Statewide only **1,264 of 5,917 precincts** reporting; "COUNTING IS SLOW."
- SF ballot measures: "partial returns from **300 precincts**" (of ~600–700;
  SF had ~1,286 by 1960), with tiny printed sums.

**Implication.** The "in-person diamond" floor is valid for *total ballots cast*
but NOT for *what was known the morning after* in the hand-count era: counting
paper ballots by hand was itself slow. So a pre-1964 night floor cannot be
assumed ~94–100% — it must be **measured per election** from the morning-after
returns, exactly as Phase 2 does. This is a richer story than the plan assumed:
the modern slowdown is mail; the early slowdown was manual counting. Same
symptom (you don't know on election night), two different mechanisms, with the
machine/punch-card era (≈1960s–1990s) as the fast interlude between them.

Caveat: 1916 was the closest presidential race in CA history (Wilson won the
state — and the presidency — by ~3,800 votes), so national desks may have held
returns; the captured edition also reads as a very early (3 A.M.) run.

**Second check — 1932 (FDR landslide) — was the OPPOSITE: complete by morning.**
The Wed 1932-11-09 Chronicle (masthead-confirmed; scans
`sweep_19321108_issue19321109_p1_s2.png`, `_p4_s0.png`) prints:
- "For presidential electors, the **complete** San Francisco vote was Roosevelt
  134,801; Hoover 66,111" → SF president sum **200,912**.
- U.S. Senator "**final** vote" Tubbs 112,263 / McAdoo 61,043 / Shuler 14,253;
  the statewide county table's SF row matches and shows SF at **1,050 precincts**.
- Certified cast (DOE) = 227,283 → president sum = **88.4%** floor; "complete"
  implies the true night share was ~100% (the 88.4% is just president undervote).
  *(Load-bearing digits to be re-read on the image before ingestion.)*

**Reframing.** Pre-1964 night-of completeness was **not flat** — it varied, and
the variation IS the signal. 1932 was counted overnight (~complete); 1916 was
not. Whether 1916 was slow from the close race, hand-counting load, or just an
early captured edition is the open question. Either way the conclusion stands:
**each pre-1964 election needs its night-of share measured from the paper**
(Phase 2), not assumed. The narrative gains a third act: a slow hand-count era,
a fast machine/punch-card interlude (1960s–90s, the ~94% diamonds), then the
modern mail-driven slowdown.

## 1916 edition question — RESOLVED: the slow night was real

Captured the day-2 paper (Thu 1916-11-09; scans `sweep_19161107_issue19161109_*`)
and compared edition press-times:
- Both the 1916 Nov-8 and the 1932 Nov-9 captures are early **~2–3 A.M. first
  editions** (1916 stamps "2 A. M."/"3 A. M."; 1932 stamps "3 o'clock this
  morning") — directly comparable night snapshots.
- At that same hour: **1916 SF ≈ 300 of 684 precincts** (partial; president
  "virtually none at hand"), vs **1932 SF complete** (200,912 president).
- 1916 day-2 (Nov 9, ~1 A.M. Thu) shows SF at **676 of 684 precincts**, amendment
  No. 2 ≈ 148,576 (≈95% of certified 155,747) — the count genuinely spanned >24h.

**Verdict:** 1916's incompleteness is structural, not an early-edition artifact.
Pre-1964 night-of completeness genuinely varied. Likely drivers of the
1916-vs-1932 gap: 1916 was the closest CA presidential race ever (decided the
presidency; contested/careful count) and/or **mechanical voting machines**, which
SF/CA adopted in the 1920s–30s and which report precinct totals instantly. The
latter is worth confirming — if machines drove it, the "fast interlude" began
decades earlier than the 1960s, sharpening the three-act story.

## FINAL RESULTS (2026-06-13): 22 elections recovered, 1908–1956

Recovered SF election-night (morning-after) vote shares from NewsBank image
scans, ingested to `sf_archival_canvass_points.csv` (pct = largest verified
SF contest sum ÷ DOE certified ballots cast):

| Year | Night share | Year | Night share | Year | Night share |
|---|---|---|---|---|---|
| 1908 | 88.6% | 1924 | 35.6% | 1942 | 96.5% |
| 1910 | 17.8% | 1926 | 70.9% | 1946 | 87.2% |
| 1912 | 85.0% | 1928 | 90.8% | 1948 | 95.7% |
| 1914 | 4.2% | 1930 | 91.6% | 1950 | 96.5% |
| **1916** | **3.0%** | 1932 | 88.4% | 1952 | 99.0% |
| 1920 | 66.2% | 1936 | 90.1% | 1954 | 88.7% |
| 1922 | 26.5% | 1938 | 94.3% | 1956 | 93.6% |
|  |  | 1940 | 95.3% |  |  |

**There IS a real slow era — it's the 1910s–1920s, not a generic "hand-count
era."** (My intermediate notes flip-flopped: 1916 alone suggested a slow start;
the 1930s–50s landslides then suggested a flat-fast baseline; the focused
re-read of 1910–1924 settled it.) The shape is **four phases**:

1. **Fast 1900s–early 1910s** — 1908 (89%), 1912 (85%): most of the vote known
   by morning.
2. **Slow 1910s–1920s** — 1910 (18%), 1914 (4%), 1916 (3%), 1920 (66%), 1922
   (27%), 1924 (36%), 1926 (71%): a decade-plus of *partial* mornings. Papers
   repeatedly cite "unusually slow," "unprecedented slowness," long
   Progressive-era ballots (many propositions + judicial races to hand-count),
   and close top-of-ticket races. 1918 was the extreme: the first precinct
   didn't reach the Registrar until after midnight and **no SF totals were
   published at all** (→ `/missing`).
3. **Fast again, 1928–1990s** — 1928 onward sits at ~88–99% known overnight
   (the machine/punch-card era the project already documented from 1964).
4. **Modern mail-driven collapse, post-2000** — down to ~10–50%.

So the long baseline is **not** flat: it dips hard in the 1910s–20s, recovers,
then collapses again in the 2000s for an entirely different reason (mail, not
counting speed). The "you don't know on election night" symptom recurs across a
century with *three* distinct causes — long hand-counted ballots (1910s), then
neither (fast mid-century), then late mail (today). Pushing the record to 1908
is what makes this visible.

### Gaps (not ingested — for `/missing` / follow-up)
- **No night figure recoverable from captured pages:** 1899-12-02, 1903-09-29,
  1903-10-08 (swept pages 1–5 held literary/sports sections; results on
  uncaptured pages — need a wider re-sweep), 1944-11-07 (Election-Extra carried
  no SF returns; CA was 908/14,841 precincts at press), **1918-11-05** (count so
  slow no SF totals were published election night — itself a finding).
- **No NewsBank issue found:** 1902-12-03 (entry-search missed it even after
  retry — likely an archive gap).
- **Low confidence:** 1914 (4.2%) — OCR heavily garbled, digits may be
  truncated; ingested as a conservative floor (true value ≥ 4.2%).
- **Denominator error:** 1934-11-06 — complete Governor race (220,894) exceeds
  DOE ballots-cast (166,133); excluded from the chart, logged in
  `denominator-errors.md`.

Notes carried into later phases:
- **Gaps**: no 1904/1906 rows — the **1906 earthquake** destroyed records.
  Odd municipal years are largely absent pre-1960.
- **1911 women's suffrage**: ballots cast nearly double 1910→1912
  (59,724 → 105,646); a real structural feature, not an error.
- `1910-11-01` has `registration = n/a` but a `ballots_cast` of 59,724, so its
  floor is still computable.
