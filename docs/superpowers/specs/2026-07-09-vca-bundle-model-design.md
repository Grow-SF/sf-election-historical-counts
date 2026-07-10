All factual disputes are now verified against the repo. Writing the final synthesis spec.

# Specification: Did the VCA modernization bundle move county election-night share? (CA, Nov generals 2012-2024)

Synthesis of three panel proposals, adjudicated against the repo data at `/Users/sbuss/workspace/sf-election-count/.claude/worktrees/bubbly-dazzling-wren`. Every disputed fact below was re-verified directly against `packages/data/county_night.json`, `packages/data/county_tech.json`, and `data/research/election-night/plateau_review.json`; every dry-run number quoted was independently recomputed.

**Adjudicated facts (all three proposals were right to correct the briefing):**
- San Mateo has NO ASV (status `not-adopted`, confidence `primary`). The briefing matrix's "2018*" is wrong.
- The usable panel is exactly **78 points** (comparable=true, pct non-null, year != 2020), not ~70.
- San Bernardino has **one** usable point (2024, primary) and **zero** usable pre-adoption points; the pure e-pollbook effect has zero within-county contrasts, not n=1. Proposal 1 is right; the controller's audit understated this.
- Placer (cohort 2024) has zero usable post-adoption points. Ventura's bundle year is 2022 via its primary-confidence vote-center record; the secondary-confidence e-pollbook conflict cannot move its cohort.
- All REFUTED_AS_PLATEAU rows are already comparable=false; no usable row carries that verdict. Santa Clara 2024 is REFUTED_AND_CORRECTED (value corrected, kept). San Francisco's 6 usable rows have no plateau_review records (home dataset, primary throughout); everyone missed this join gap, handled in Section 2.
- `packages/data/vbm_history.json` is an SF-only series (no county field). The mechanism covariate does not exist in-repo.
- Verified dry-run values (calendar base, pooled controls): ATT(2018,2018) = -10.30, ATT(2022,2022) = +7.44, theta_2022 = +5.66 (n=12), theta_2024 = +9.39 (n=10); vs SF only +6.02, vs SLO only +12.77; type-matched theta_2024 = +10.07, type-matched ATT(2018,2018) = -6.62. Pre-cell mean is **+1.04** under the sign convention in Section 5 (Proposal 1 reported -1.0; the magnitude is right, the sign convention was left undefined; it is pinned below). Nevada rank 2/7 and San Diego rank 5/12 in the ASV placebo pools verified exactly.

---

## 1. Estimands

The question "did e-pollbooks and ASV speed up election-night counting" is **not identifiable** in this panel and the writeup must say so in its first paragraph, for three reasons: (a) e-pollbook adoption year equals vote-center adoption year in every county with a within-county contrast; (b) the only pure e-pollbook county (San Bernardino) has no usable pre-adoption point, so there are zero pure e-pollbook contrasts; (c) ASV separates from the bundle only in Nevada (2022) and San Diego (2024), one post-ASV point each, both at secondary confidence.

The treatment estimated is the **VCA modernization bundle**: vote centers + universal mailed ballots + e-pollbooks, adopted as one package. That name appears in every table header and the doc title.

**Tier 1, primary (one preregistered headline):**
- **theta_2024**, the post-AB 37 presidential differential. Plain language: in November 2024, after AB 37 (2021) put every county including the controls on universal mailed ballots, did bundle counties post a larger share of their final count on election night, relative to their own pre-adoption baselines, than the two never-adopting counties did over the same interval? Notation: theta_2024 = (1/10) * sum over treated i with usable 2024 and a usable pre-adoption base of delta_i(2024), with delta defined in Section 3. This is the cleanest available contrast because the mail-mix confound is roughly equalized across treated and control after 2021.

**Tier 2, secondary (Holm-corrected as a family of three):**
- **theta_2022**: same construction at the 2022 midterm (n=12).
- **theta_step_2018 = ATT(2018,2018)**: the at-adoption step for the 2018 cohort, the only pre-AB 37 at-adoption contrast. This is dominated by the mail-mix composition shift (treated went all-mail while controls had not) and is labeled "total effect of switching to the vote-center model", never a tech-speed effect.
- **theta_step_2022 = ATT(2022,2022)**: the at-adoption step under the post-AB 37 regime (controls also all-mail).
- The pooled at-adoption step across eras is **never computed or printed**. Proposal 1 is right that it averages two different contrasts; Proposal 2's pooled ATT_adopt is rejected.

**Tier 3, descriptive only (no estimates, no conventional inference; exact-rank placebo positions with stated minimum attainable p):**
- ASV case studies: Nevada's 2018-to-2022 change (+7.10) ranked against the 6 no-tech-change counties with both years usable (observed rank 2/7, one-sided p = 2/7 = 0.29); San Diego's 2022-to-2024 change (+10.65) ranked against the 11 no-change counties (observed rank 5/12, p = 0.42). Plus the within-2020-cohort contrast Fresno+LA (bundle+ASV) vs Orange+Santa Clara (bundle only), exact 6-assignment permutation, minimum attainable p = 1/6. Framed per Proposal 3's falsifiable prediction: if ASV produced large (>10pp) gains its adopters would lead their cohorts; they do not; the design can rule out large ASV effects and says nothing about small ones.
- San Bernardino's single 2024 point placed against same-year counties, one row, no inference.

**Explicit refusals (led with, not buried):** the pure e-pollbook effect (n=0 contrasts); any bundle decomposition into components (perfect collinearity); ASV as a population parameter; Sign-Scan-and-Go (Placer has no usable post point); the 2020 cohort's at-adoption step (their adoption November is the excluded COVID election); counting speed as a mechanism (night share conflates processing speed, ballot-arrival mix, and each county's choice of when to stop posting).

**Optional extension, gated:** a mechanism decomposition (how much of the effect is ballot-mix composition) runs if and only if a per-county VBM-share covariate file lands with full provenance from the CA SoS Statements of Vote (a separate research task; `vbm_history.json` is SF-only, verified). It is labeled a mediator decomposition, never "the effect controlling for mail". The primary analysis must run and publish without it.

## 2. Panel assembly rules

All in-script from the canonical JSONs; no hand-edited intermediates (repo rule: always use the real data).

**Outcome panel.** From `packages/data/county_night.json` (16 jurisdictions): keep points with `comparable == true` AND `pct != null` AND `year != 2020`. Attach `type` (presidential/midterm), `confidence`, `ballots`, `final`.

**Plateau verdicts.** Join `data/research/election-night/plateau_review.json` by (slug, year parsed from `date`). Rule for missing records: assert that the only usable rows without a verdict are San Francisco's six (home dataset); treat them as verdict-clean. 

**Quality tier.** Tier 1 = confidence `primary` AND verdict in {CONFIRMED, REFUTED_AND_CORRECTED} (or SF no-record). Tier 2 = everything else. On the current data tier 2 comprises exactly 11 usable rows: Fresno 2012/2014/2018, Napa 2014, Riverside 2012/2014/2016/2018, San Diego 2012/2014 (secondary confidence), plus Sacramento 2012 (primary confidence but PLAUSIBLE plateau; all three proposals missed that the tier rule must consult the verdict even for primary rows, else Sacramento 2012 slips through).

**Treatment coding.** From `packages/data/county_tech.json` adoptions: drop the three non-county vignettes (state != CA: NY, PA, WI). Bundle year g(i) = vote-center `adopted_year`; assert epollbook year equals it for every CA county where both are adopted. Cohorts: 2018 = {Madera, Napa, Nevada, Sacramento, San Mateo}; 2020 = {Fresno, Los Angeles, Orange, Santa Clara} plus San Bernardino as a label-only member; 2022 = {Riverside, San Diego, Ventura}; 2024 = {Placer, label-only}; never = {San Francisco, San Luis Obispo}.

**Special handling:**
- **San Bernardino**: vote-center `not-adopted` (primary), epb 2020. It carries the 2020 label in the randomization multiset but contributes zero estimation cells (assert: exactly one usable row, 2024, no usable pre). Its 2024 point appears only in the Tier 3 descriptive row.
- **San Luis Obispo**: epb `adopted_year` 2026 is post-window; assert 2026 > 2024 and keep SLO as a never-treated control.
- **Ventura**: g = 2022 keyed to the primary-confidence vote-center record; assert epb year == vote-center year == 2022 so the documented EAP-vs-SoS epb conflict (secondary) cannot move the cohort. One robustness note, not a sensitivity run.
- **ASV years**: Nevada 2022, San Diego 2024, Fresno 2020, LA 2020 (same-year as bundle, collinear); Riverside 2025 and San Bernardino 2025 are post-window. Assert San Mateo asv status == `not-adopted`.

**Startup assertions (fail loudly if data changes):** 78 usable rows; the cohort map above; San Mateo no ASV; Placer zero usable post rows; SB exactly one usable row with no pre; no usable row REFUTED_AS_PLATEAU; SLO epb year > 2024; only SF rows lack plateau records; Nevada 2024 (24.49) and Riverside 2024 (63.7) are comparable=false with documented reasons.

**Emitted for hand-verification** (per the repo's human-verification loop): `docs/analysis/generated/panel.csv` with county, year, type, pct, ballots, final, confidence, verdict, tier, cohort, asv_year, base years under both base rules, and a flag column for fallback or long-gap (>8 years) bases.

## 3. Primary estimator

Callaway-Sant'Anna logic reduced to explicit 2x2 differences of means against the never-treated pair. No regression is needed for any primary number; every cell is a difference of at most six raw pcts, printed with its components.

**Notation.** Y_i(t) = night share (pp) for county i in November general t, t in {2012, 2014, 2016, 2018, 2022, 2024}; T_i = i's usable years; g(i) = bundle cohort; C = {SF, SLO}.

**Base period (primary rule: type-matched).** b(i,t) = max{t' in T_i : t' < g(i) and type(t') == type(t)}; if empty, fall back to max{t' in T_i : t' < g(i)} and flag the row. Adjudication: Proposals 2 and 3 make type-matching primary, Proposal 1 makes it co-primary; majority wins, and the substantive reason is that presidential/midterm swings are the largest single mover of the outcome and are plausibly county-heterogeneous, so differencing within election type removes a first-order contaminant at near-zero cost. The calendar rule (last usable pre of any type) is a mandatory co-reported variant; where the two disagree materially (verified: at-adoption 2018 step is -6.62 type-matched vs -10.30 calendar, driven by Napa/Nevada/San Mateo 2014 vs 2016 bases) both are shown side by side and never averaged.

**Per-county contrast (sign convention: positive = treated county improved relative to controls):**

```
delta_i(t) = [Y_i(t) - Y_i(b(i,t))] - (1/2) * sum_{c in C} [Y_c(t) - Y_c(b(i,t))]
```

**Group-time cells:** ATT(g,t) = mean of delta_i(t) over {i : g(i)=g, t in T_i, b(i,t) exists}, for t >= g. Exactly seven cells exist (verified): (2018,2018) n=5; (2018,2022) n=5; (2018,2024) n=4 (Nevada 2024 excluded, printer defect); (2020,2022) n=4; (2020,2024) n=4; (2022,2022) n=3; (2022,2024) n=2 (Riverside 2024 excluded). Every cell is reported with its county list, base years, and per-county deltas.

**Aggregates (equal county weights, weights printed):** theta_2024 = mean of delta_i(2024) over all contributing treated i (n=10); theta_2022 likewise (n=12); theta_step_2018 = ATT(2018,2018); theta_step_2022 = ATT(2022,2022).

**Identification map (printed in the doc):** ATT(2018,2018) is identified off SF+SLO and, as a robustness variant, off the 8 not-yet-treated comparators. Every t=2024 cell and theta_2024 are identified **only** off SF and SLO; the two controls carry the entire post-AB 37 identification. The 2020 cohort has no at-adoption cell (2020 excluded); Placer's cohort has no cells.

**Cross-check estimator (one, not three):** BJS-style imputation. Fit Y_it = alpha_i + gamma_t by OLS on the 50 untreated usable cells (never-treated all years plus treated pre-adoption years; San Bernardino must be dropped since it has zero untreated cells, so alpha_SB is unidentified; assert this), impute counterfactuals for the 27 non-SB treated post cells, aggregate gaps at the same horizons. Adjudication: Proposal 1's Sun-Abraham saturated OLS is dropped as redundant (with full saturation and never/not-yet-treated identification it re-derives the CS cells with more code); Proposal 2's BJS is kept because it is the simplest genuinely different machinery (pools all pre years instead of one base). Correction to Proposal 2: BJS and the cell means are different estimators and will NOT agree "to within rounding" on real data; they must agree to <0.1pp only on homogeneous synthetic data (Section 7). On real data they are reported side by side; divergence above ~3pp on any aggregate is flagged and discussed, not averaged.

**Negative exhibit:** static two-way FE with a single post dummy, estimated once, labeled known-biased (Goodman-Bacon forbidden comparisons: already-treated 2018-cohort units serving as controls for 2022-cohort steps under the observed dip-then-rebound). Synthetic scenario S3 quantifies its bias on this exact panel. It never appears near the headline. No mixed/hierarchical models (unverifiable distributional assumptions at n=16).

## 4. Inference plan

Analytic cluster-robust SEs are ruled out (16 clusters, 2-cluster control group, severe imbalance): footnote only, no numbers. Wild cluster bootstrap is **cut entirely**, overruling Proposals 1 and 3 (secondary/experimental) in favor of Proposal 2's rejection: with the parameter identified off 2 control clusters, WCB is known-unreliable (MacKinnon-Webb), it would fail the synthetic coverage validation this spec requires of every reported inference procedure, and it is not transparently hand-checkable. One sentence in the doc records why it is absent.

**Primary: Fisher randomization inference (RI) over adoption labels.**
- Scheme: hold each county's outcome series, missingness pattern, and quality flags fixed as county attributes. Permute the observed label multiset {2018 x5, 2020 x5, 2022 x3, 2024 x1, never x2} uniformly across the 16 counties. Recompute the statistic with identical rules (type-matched bases, fallbacks, cell means; the permuted never-labels define the control pair).
- Degenerate draws (any required cell empty, or a permuted control missing a required year, e.g. Placer drawn as control invalidates theta_2024): reject and redraw until 10,000 valid draws per statistic, all from one seeded stream; log and report the redraw rate per statistic (dry-run estimate ~22% for theta_2024).
- Two-sided p = (1 + #{|T_perm| >= |T_obs|}) / (1 + 10,000), with the Monte Carlo SE of p reported (Proposal 2's addition, kept). 10,000 draws suffices (MC SE < 0.005 for p near 0.2); Proposal 2's 100,000 is unnecessary.
- Statistics tested: theta_2024 (headline, standalone); the secondary family {theta_2022, theta_step_2018, theta_step_2022} with Holm correction within the family; and the joint pre-trend statistic (Section 5). Everything else in the paper carries no p-value.
- **What a p-value means here (printed beside every p):** adoption was not randomized; the RI p is a placebo-calibration benchmark under exchangeability of county trajectories, testing the sharp null that adoption timing moved no county-year outcome. It is evidence against "no effect plus as-if-random timing", not against "no effect" alone.

**90% RI confidence interval by test inversion (headline only).** For tau on a grid from -25 to +25 by 0.5: subtract tau from every observed-treated county's post-adoption usable outcomes (observed labels, before permuting), rerun the RI test at 2,000 valid draws per grid point, report {tau : p(tau) > 0.10} as the 90% interval for a constant additive effect. Coverage is validated in Section 7 before this is trusted.

**Design-uncertainty band, equal billing with the p-value (Proposal 2's key demand, adopted):** every aggregate is reported vs SF only, vs SLO only, and pooled. The SF-SLO 2012-2024 drift is 9.3pp (verified: SF -14.50, SLO -23.84), so control choice alone moves long-horizon contrasts by several pp. Verified current values for theta_2024: +6.02 (SF), +12.77 (SLO), +9.39 (pooled). If the two single-control estimates disagree in sign, no pooled headline is reported, full stop.

**Volatility statement:** leave-one-county-out range (each treated county and each control dropped in turn) on every aggregate.

**Power, stated before any estimate:** the script computes the RI null SD for each statistic and reports MDE at alpha = 0.10 and at (alpha = 0.05, power 0.8, MDE ~ 2.8 x null SD), plus the simulated power curve from Section 7. Expected MDE is roughly 10-13pp. Mandatory plain-language sentence: this design can detect large operational changes; it cannot certify small speedups or rule them out.

**Tier 3 inference:** exact rank p-values only (granularity 1/7, 1/12, 1/6), under a banner stating that inference at conventional levels is impossible by construction.

## 5. Event-study / pre-trend diagnostics

- **Placebo pre-cells:** for each treated i and each usable t < g(i) with t != b0(i) (b0 = calendar base, last usable pre), compute delta_i^pre(t) = [Y_i(t) - Y_i(b0)] - control change over the same interval. Under parallel trends these are zero in expectation. Verified: 25 cells exist, mean +1.04pp under the Section 3 sign convention (the spec pins this convention because Proposal 1 reported the same magnitude with opposite sign), with the largest deviations in Riverside (+18.2, +14.0, +13.5) and San Diego (+18.1) pre-cells, all tier-2 secondary data. The full panel is plotted/tabulated by cohort and event time, with tier-2 cells visually flagged.
- **Joint pre-trend RI test:** statistic = mean |delta^pre| across the 25 cells, tested with the same permutation engine.
- **Anticipation check:** event-time -1 vs -2 cells for the 2018 cohort specifically (VCA counties ran voter education and mail expansion before launch).
- **Not-yet-treated variant:** ATT(2018,2018) recomputed with the 8-county not-yet-treated comparator set (SF, SLO, Fresno, LA, Orange, Riverside, San Diego, Ventura); valid under no-anticipation; divergence from the never-treated version is reported.
- **Interpretation rule, pre-specified:** if the joint pre-trend p < 0.10, or the tier-1-only pre-cell mean exceeds 3pp in absolute value, the headline is downgraded to descriptive wording (template D in Section 8) regardless of its own p-value.

## 6. Robustness matrix

Each row: what is rerun, why, and the pre-specified consequence if it moves.

| # | Check | Why it matters | What changes the conclusion |
|---|---|---|---|
| 1 | Control triptych (SF only / SLO only / pooled), every aggregate | Two controls carry all post-AB 37 identification; 9.3pp relative drift | Sign disagreement kills the pooled headline (template C) |
| 2 | Calendar-base variant beside type-matched | Base rule moves ATT(2018,2018) from -6.6 to -10.3 | Reported side by side; if theta_2024 sign flips across rules, downgrade to descriptive |
| 3 | Tier-1-only (drops the 11 tier-2 rows) | Tier-2 rows cluster in treated pre-periods (Riverside's entire pre, San Diego 2012/2014); correlated measurement error can manufacture steps | 2022-cohort cells losing Riverside are re-shown; if theta_2024 moves > 3pp or flips sign, lead with it |
| 4 | Re-include comparable=false treated-post exclusions (Nevada 2024 = 24.49 printer defect; Riverside 2024 = 63.7 refuted plateau) as bounds | Exclusions concentrated in treated post-years are a selection channel | Bounds printed with the headline; the doc must show theta_2024 drops when Nevada is included |
| 5 | Leave-one-county-out ranges | 16 clusters; LA size, San Mateo and Sacramento large steps, Riverside endogeneity | Any single county flipping an aggregate's sign is named in the results section |
| 6 | Not-yet-treated comparators for ATT(2018,2018) | Grows the control set from 2 to 8 for the one cell that allows it | Divergence from never-treated version reported |
| 7 | Placebo-in-time (adoption shifted one general earlier, pre-period only) | Trend selection without cross-county exchangeability assumptions | Nonzero placebo mean (>3pp) triggers the endogeneity paragraph and downgrades wording |
| 8 | Riverside excluded entirely | Pre-registered endogeneity case: night share collapsed to 46.1 in 2018, 3.5 years pre-adoption, on all-secondary pre data | 2022-cohort cells and theta aggregates re-shown |
| 9 | ASV-augmented rows flagged/excluded (Nevada 2022, San Diego 2024) | theta aggregates mix bundle-only and bundle+ASV county-years; missed by all three proposals as a sensitivity | Variant reported; material movement noted in the ASV section |
| 10 | Ballot-weighted aggregates | Different estimand (per-ballot, effectively LA) | Reported beside county-weighted primary, never substituted |
| 11 | Logit transform of pct/100 | Bounded-share/ceiling artifacts | Sign flip anywhere is disqualifying for level-based claims |
| 12 | 2020 restored (single appendix line) | Shows the COVID exclusion is not driving conclusions | Expected to blow up; documented |
| 13 | BJS imputation and static TWFE beside the cell means | Estimator dependence; staggered-bias exhibit | BJS divergence > 3pp on an aggregate is flagged and discussed |
| 14 | Size split (median certified-final ballots), descriptive only | Vote-center consolidation plausibly binds differently at Madera vs LA scale | No p-values; forking-paths door closed by the descriptive label |

Multiplicity discipline: theta_2024 is the single pre-declared headline; rows 1-14 are labeled diagnostic; nothing in the matrix can be promoted to a headline after results are seen.

## 7. Synthetic-data validation plan

A `--validate` mode runs before any real-data number is written. All scenarios simulate on the **exact observed skeleton**: 16 counties, the real usable-year missingness mask, real cohort labels, year-shock vector calibrated to the real gamma_t, county effects SD ~8 around 60, iid noise sigma ~4.6-5.5 (set to the two-way-FE RMSE of the real untreated cells). 500-1,000 reps per scenario, seeded. Committed output file so a referee reruns both with one command. Acceptance criteria are assertions, not prose:

- **S1, sharp null (tau = 0):** all seven cells and all four aggregates unbiased (|mean| < 0.5pp); RI rejection rate at alpha = 0.10 within the binomial 99% band around 0.10; ditto alpha = 0.05. Validates the permutation engine and the redraw rule.
- **S2, constant effect (tau = +8 on all post cells):** aggregate bias < 0.5pp; 90% RI test-inversion CI coverage in [0.85, 0.95]. Validates the CI machinery before it is trusted on real data.
- **S3, dynamic sign flip (tau = -10 at adoption pre-AB 37, +8 from 2022 on, calibrated to the observed pattern):** era-split estimands recover both numbers within 0.5pp; the static TWFE exhibit shows material bias (recorded and cited in the doc as the reason TWFE is quarantined).
- **S4, control-side shock (level shock to SF/SLO only in 2022-2024, zero treatment effect):** quantifies exactly how many pp of spurious theta_2024 one control-side shock of size s produces (expected: one-for-one in s). This number feeds the limitations section verbatim; it is the design's key non-identifiability.
- **S5, heterogeneous effects (tau_i ~ N(tau, 3)):** cohort ATTs unbiased for cohort means; equal-weight aggregates unbiased for the county-mean estimand.
- **Power curve:** tau in {3, 5, 8, 12}; empirical power at alpha = 0.10 and 0.05; the 80%-power MDE goes in the doc's power paragraph.
- **Estimator agreement:** cell-mean ATTs vs BJS imputation agree to < 0.1pp under S1/S2 (homogeneous DGPs). This, not real-data agreement, is the bug check.

## 8. Interpretation guardrails

**Claims that must never appear:**
- "E-pollbooks sped up counting" or any sentence placing "e-pollbook" or "ASV" adjacent to a point estimate without "bundle" or "descriptive". The treatment is the "VCA modernization bundle" in the title and every table.
- "Counted faster". Permitted outcome language: "posted a larger share of its final count by the end of election night". The outcome conflates speed, ballot-arrival mix, and when a county stops posting (SLO's 2024 final election-night report was generated the next day; plateau_review verdicts are cited in an outcome-validity paragraph).
- "No effect". A non-rejection is reported as "uninformative below [MDE] pp", with the MDE printed.
- Significance stars, anywhere.
- A pooled at-adoption step across eras.
- Any at-adoption claim for the 2020 cohort.
- Generalization to SF or SLO adopting the bundle (selected adoption, two specific comparators, no external validity).

**Mandatory furniture:** a "what this analysis cannot say" box first (the Section 1 refusals verbatim); the power paragraph before any estimate; cell composition (county list, base years, flags) under every aggregate; the exclusion appendix listing every dropped point with its documented reason.

**Headline wording templates** (fill numeric slots from the script output; current verified values shown for orientation):

- **Pattern A** (pooled positive, both single-control estimates positive, RI p <= 0.10): "In [year], counties that had adopted the VCA modernization bundle posted election-night shares about [X]pp higher, relative to their own pre-adoption baselines, than the two never-adopting counties (vs SF +[a], vs SLO +[b]; 90% RI interval [l, u]). Under the placebo-calibration benchmark this pattern would arise in fewer than [p] of random adoption reassignments. This is an effect of the whole bundle; the data cannot attribute it to e-pollbooks, vote centers, or signature automation separately."
- **Pattern B** (pooled positive, controls agree, p > 0.10; this is the current data: +9.4pp pooled, +6.0 vs SF, +12.8 vs SLO, p expected near 0.2): "Bundle counties posted election-night shares about [X]pp above their pre-adoption baselines relative to both control counties in [year] (vs SF +[a], vs SLO +[b]). The direction is consistent with the bundle helping, but a difference this size arises in roughly [1/p rounded] of every [k] placebo reassignments of adoption labels, and effects smaller than [MDE]pp are undetectable with two control counties. The honest summary is an interval, [l, u], not a verdict."
- **Pattern C** (single-control estimates disagree in sign): "The answer depends entirely on which of the two never-adopting counties is the comparator (vs SF [a], vs SLO [b]), so no pooled estimate is interpretable. The design cannot distinguish a bundle effect from idiosyncratic drift in one control county."
- **Pattern D** (pooled near zero or negative, or pre-trend rule from Section 5 triggered): "The data show no detectable improvement in election-night share attributable to the bundle; given the design's minimum detectable effect of [MDE]pp, this is uninformative about effects smaller than [MDE]pp in either direction."
- **At-adoption step, all patterns:** always worded as "the total effect of switching to the vote-center model, dominated at 2018 by the shift to universal mailed ballots that later reached every county via AB 37", with the era-split values ([-6.6 type-matched / -10.3 calendar] and [+7.4]) side by side.

## 9. Implementation plan

**Files:**
- `scripts/analysis/night_share_bundle_did.py`: the single analysis script (estimation, inference, robustness, and `--validate` synthetic harness in one file, ~600 lines).
- `docs/analysis/2026-07-09-vca-bundle-night-share.md`: the written deliverable, following the repo's dated-doc convention. No em dashes.
- `docs/analysis/generated/`: script-emitted, committed artifacts: `panel.csv` (hand-verification table), `att_matrix.csv` (7 cells with per-county components), `aggregates.csv` (estimates, RI p, MC SE, 90% RI CI, SF/SLO/pooled triptych, LOO ranges), `pretrends.csv`, `sensitivities.csv` (one row per Section 6 check), `asv_descriptives.csv`, `validation.json` (Section 7 results), `results.json` (everything, machine-readable).

**Runner and dependencies:** `uv run --with numpy python scripts/analysis/night_share_bundle_did.py --draws 10000 --seed 20260709` and `... --validate --reps 500 --seed 20260709`. numpy is the only third-party dependency, documented in the script docstring and the doc header; it is used for `np.linalg.lstsq` (BJS/TWFE dummy matrices, built explicitly) and vectorized RI loops. Adjudication vs Proposal 2's pure-stdlib Gaussian elimination: rejected; hand-rolled linear algebra is more code to verify, not less, and the environment explicitly permits documented `uv run --with numpy`. Transparency requirement kept in a stronger form: every primary number (cells, aggregates) is computed twice, once with plain Python means over lists and once inside the numpy engine, and asserted equal to 1e-9; the plain-Python path is the reference implementation a reader checks by hand against `panel.csv`.

**Script structure (pure functions, RI reuses estimation unchanged):** `load_panel()` (Section 2 filters, joins, assertions), `assign_cohorts()`, `base_year(i, t, rule)`, `delta(i, t, controls, rule)`, `att_cells()`, `aggregates()`, `placebo_precells()`, `ri_engine(stat_fn, draws, seed)` (multiset permutation, reject-redraw-log), `ri_ci(grid, draws_per_point)`, `bjs_imputation()`, `twfe_static_exhibit()`, `asv_rank_tests()` (Nevada 7-pool, San Diego 12-pool, 2020-cohort 6-way), `robustness_grid()`, `validate()` (S1-S5 + power curve), `emit_outputs()`.

**Determinism policy:** one seed (20260709) controls every stochastic step via independent child streams per statistic (numpy `SeedSequence.spawn`); rerunning the command must leave `git status` clean (byte-identical generated files); floats rounded to 2dp at emission. The doc's numeric tables are the generated CSVs included verbatim, so no number in prose can drift from the script (repo norm: no hand-edited derived data).

**Order of work:** (1) `load_panel` + assertions + `panel.csv`, hand-checked against the JSONs; (2) `--validate` passes all Section 7 acceptance criteria; (3) real-data run; (4) doc written from generated tables; (5) PR with script, generated outputs, and doc together.