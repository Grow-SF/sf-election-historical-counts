# Did the VCA modernization bundle move county election-night share? (CA, November generals 2012-2024)

Analysis of whether counties that adopted the **VCA modernization bundle**
(vote centers + universal mailed ballots + e-pollbooks, adopted as one
package under California's Voter's Choice Act) posted a larger share of
their certified final count by the end of election night, relative to their
own pre-adoption baselines and to the two never-adopting comparison
counties, San Francisco and San Luis Obispo. The narrower question, whether
e-pollbooks or automated signature verification sped the count on their
own, is not identifiable in this panel; the box below says why.

- Spec: `docs/superpowers/specs/2026-07-09-vca-bundle-model-design.md`
- Script: `scripts/analysis/night_share_bundle_did.py`
- Generated tables: `docs/analysis/generated/` (every number in this
  document comes from those files; the tables below are the generated CSVs
  included verbatim)
- Reproduce:
  `uv run --with numpy python scripts/analysis/night_share_bundle_did.py --draws 10000 --seed 20260709`
  and
  `uv run --with numpy python scripts/analysis/night_share_bundle_did.py --validate --reps 500 --seed 20260709`
  (both are deterministic; rerunning leaves the generated files
  byte-identical)

---

## What this analysis cannot say

> **Explicit refusals, led with on purpose.**
>
> - **The pure e-pollbook effect.** Not estimable: zero within-county
>   contrasts exist (n = 0). The only pure e-pollbook county, San
>   Bernardino, has no usable pre-adoption point.
> - **Any decomposition of the bundle into components.** E-pollbook
>   adoption year equals vote-center adoption year in every county with a
>   within-county contrast: perfect collinearity.
> - **ASV as a population parameter.** Automated signature verification
>   separates from the bundle only in Nevada (2022) and San Diego (2024),
>   one post-ASV point each, both at secondary confidence. Tier 3 of this
>   document gives exact-rank descriptives only.
> - **Sign-Scan-and-Go.** Placer, the only adopter, has no usable
>   post-adoption point.
> - **The 2020 cohort's at-adoption step.** Their adoption November is the
>   excluded COVID election.
> - **Counting speed as a mechanism.** The outcome (election-night share of
>   the certified final) conflates processing speed, ballot-arrival mix,
>   and each county's choice of when to stop posting.

The question "did e-pollbooks and ASV speed up election-night counting" is
**not identifiable** in this panel, for three reasons: (a) e-pollbook
adoption year equals vote-center adoption year in every county with a
within-county contrast; (b) the only pure e-pollbook county (San
Bernardino) has no usable pre-adoption point, so there are zero pure
e-pollbook contrasts; (c) ASV separates from the bundle only in Nevada
(2022) and San Diego (2024), one post-ASV point each, both at secondary
confidence. What can be estimated is the effect of the whole **VCA
modernization bundle**, and that is the treatment named in every table
here.

## Power: read this before any estimate

This design has two never-adopting control counties and sixteen
jurisdictions in total, and its detection floor is high. The randomization
null SD for the headline statistic is 5.67 pp, which puts the minimum
detectable effect at **14.11 pp** (alpha = 0.10, power 0.8) and **15.86
pp** (alpha = 0.05, power 0.8). The simulated power curve from the
validation harness (`validation.json`) agrees: at a true constant effect of
3 pp, power is 0.122 (alpha = 0.10) and 0.058 (alpha = 0.05); at 5 pp,
0.232 and 0.092; at 8 pp, 0.436 and 0.25; even at 12 pp it reaches only
0.704 and 0.50, so the simulated 80 percent power MDE is above 12 pp at
both levels. **This design can detect large operational changes; it cannot
certify small speedups or rule them out.** Any non-rejection below is
reported as uninformative below the printed MDE, never as evidence of no
effect.

## Headline result

**In 2024, counties that had adopted the VCA modernization bundle posted
election-night shares about 10.07 pp higher, relative to their own
pre-adoption baselines, than the two never-adopting counties (vs SF +6.78,
vs SLO +13.37; 90% RI interval [2.00, 19.00]). Under the placebo-calibration
benchmark this pattern would arise in fewer than 0.0663 of random adoption
reassignments, about 1 in every 15 (RI p = 0.0663, Monte Carlo SE 0.0025).
This is an effect of the whole bundle; the data cannot attribute it to
e-pollbooks, vote centers, or signature automation separately.**

What the p-value means (this applies to every p in this document): adoption
was not randomized; the RI p is a placebo-calibration benchmark under
exchangeability of county trajectories, testing the sharp null that
adoption timing moved no county-year outcome. It is evidence against "no
effect plus as-if-random timing", not against "no effect" alone.

Cell composition for theta_2024 (type-matched bases, equal county weights
across the n = 10 contributors; per-cell weights and full per-county
components in `att_matrix.csv`):

- 2018 cohort (n = 4): Madera (base 2016), Napa (2016), Sacramento (2012,
  long-gap flag), San Mateo (2016). Nevada's 2024 point is excluded
  (ballot-printer defect; see the exclusion appendix and robustness row 4).
- 2020 cohort (n = 4): Fresno (2016), Los Angeles (2016), Orange (2016),
  Santa Clara (2012, long-gap flag).
- 2022 cohort (n = 2): San Diego (2012, long-gap flag), Ventura (2016).
  Riverside's 2024 point is excluded (refuted plateau; see appendix).

Design-uncertainty band, equal billing with the p-value: the two
single-control estimates are +6.78 (vs SF alone) and +13.37 (vs SLO alone).
They agree in sign, so the pooled headline stands; had they disagreed, no
pooled estimate would have been reported. Volatility: the leave-one-out
range for theta_2024 is [6.78, 13.37], with the extremes set by dropping
one control or the other; no single county drop flips the sign of any
aggregate (see `aggregates.csv`, column `loo_sign_flip_drops`).

Base-rule co-report (never averaged): under the calendar base rule
theta_2024 is +9.39 (vs SF +6.02, vs SLO +12.77), against +10.07
type-matched. No sign flip, so the headline is not downgraded.

Bounds from re-including the two excluded treated 2024 points travel with
this number: theta_2024 is +6.91 with Nevada 2024 (24.49, printer defect)
restored, +10.04 with Riverside 2024 (63.7, refuted plateau) restored, and
+7.14 with both (robustness row 4). Anyone quoting the +10.07 headline
should quote these bounds with it: the two exclusions sit in treated
post-years, which is a selection channel.

## Secondary family (Holm-corrected as a family of three)

All three secondary statistics are non-rejections and are therefore
uninformative below their printed MDEs; none of them supports any verdict.

| Statistic | Type-matched | vs SF | vs SLO | Calendar | RI p | Holm p | MDE (0.05, 0.8) |
|---|---|---|---|---|---|---|---|
| theta_2022 (n = 12) | +7.20 | +3.95 | +10.45 | +5.66 | 0.3251 | 0.9752 | 18.85 pp |
| theta_step_2018 (n = 5) | -6.62 | -5.38 | -7.85 | -10.30 | 0.3952 | 0.9752 | 20.18 pp |
| theta_step_2022 (n = 3) | +7.44 | +3.76 | +11.13 | +7.44 | 0.4147 | 0.9752 | 24.23 pp |

(Values from `aggregates.csv`; the RI p is the placebo-calibration
benchmark described above.)

The at-adoption steps are worded, here and everywhere, as **the total
effect of switching to the vote-center model, dominated at 2018 by the
shift to universal mailed ballots that later reached every county via AB
37**, with the era-split values side by side: **-6.62 type-matched / -10.30
calendar** at the 2018 step, against **+7.44** at the 2022 step. The 2018
cohort switched to all-mail while the controls had not; the 2022 cohort
switched after AB 37 (2021) had put the controls on universal mailed
ballots too. These are two different contrasts and a pooled at-adoption
step across eras is never computed or printed.

Cell composition for theta_2022 (n = 12): Madera (base 2016, fallback
flag), Napa (2014), Nevada (2014), Sacramento (2014), San Mateo (2014),
Fresno (2018), Los Angeles (2018), Orange (2018), Santa Clara (2012,
fallback + long-gap flags), Riverside (2018), San Diego (2018), Ventura
(2018). For theta_step_2018 (n = 5): Madera (2016, fallback), Napa, Nevada,
Sacramento, San Mateo (all 2014). For theta_step_2022 (n = 3): Riverside,
San Diego, Ventura (all 2018).

## Identification map

- ATT(2018, 2018) is identified off SF + SLO and, as a robustness variant,
  off the 8 not-yet-treated comparators (row 6 below).
- Every t = 2024 cell and theta_2024 are identified **only** off SF and San
  Luis Obispo; the two controls carry the entire post-AB 37 identification.
- The 2020 cohort has no at-adoption cell (2020 excluded by design).
- Placer's 2024 cohort has no cells (zero usable post-adoption rows).
- San Bernardino carries a 2020 label in the randomization multiset but
  contributes zero estimation cells (one usable row, 2024, no usable pre).
- Ventura's bundle year is 2022, keyed to its primary-confidence
  vote-center record; the documented EAP-vs-SoS e-pollbook conflict is at
  secondary confidence and cannot move its cohort (robustness note, not a
  sensitivity run).

## Estimator cross-check and the quarantined TWFE exhibit

The BJS-style imputation cross-check (fit alpha_i + gamma_t on the 50
untreated cells, San Bernardino dropped since alpha_SB is unidentified,
impute the 27 non-SB treated post cells) gives theta_2024 = +9.64 vs +10.07
for the cell means (divergence -0.43), theta_2022 = +5.44 (-1.75),
theta_step_2018 = -5.74 (+0.87), and theta_step_2022 = +1.08 (**-6.36,
flagged: above the 3 pp threshold**). The step-2022 divergence is expected
machinery behavior, not a bug: BJS pools all pre-adoption years into
alpha_i, so for the 2022 cohort it averages over Riverside's and San
Diego's volatile tier-2 pre-periods, while the cell mean differences
against 2018 alone. On homogeneous synthetic data the two estimators agree
to machine precision (validation, S1/S2); on real data they answer with
different pre-period weighting, and the divergence concentrated in the
cohort with the noisiest pre-data is discussed here rather than averaged
away.

The static two-way FE model with a single post dummy gives beta = +1.46. It
is printed once, here, as a **known-biased negative exhibit** and never
near the headline: synthetic scenario S3 (`validation.json`) plants a
-10 pp at-adoption dip for the 2018 cohort and +8 pp from 2022 on, and
static TWFE returns -1.58 on average, a -9.58 pp bias against the +8 truth
of the post-2022 era, because already-treated 2018-cohort units serve as
controls for 2022-cohort steps under exactly the dip-then-rebound pattern
this panel exhibits (Goodman-Bacon forbidden comparisons).

## Pre-trend and placebo diagnostics

The 25 placebo pre-cells (calendar base, pooled controls, sign convention
of spec section 3) have mean **+1.04 pp**; the tier-1-only mean is **-0.90
pp** (15 cells). The joint pre-trend RI test on the mean absolute pre-cell
(observed 6.05 pp) gives p = 0.8794: about 88 percent of random adoption
reassignments produce larger pre-period deviations than the observed
labels do. The
pre-specified downgrade rule (joint p < 0.10, or tier-1-only mean above
3 pp in absolute value) is **not triggered**.

The largest pre-cell deviations are Riverside 2014 (+18.18), San Diego 2014
(+18.11), Riverside 2016 (+14.03), and Riverside 2012 (+13.49), all tier-2
secondary data; they are visually flagged in `pretrends.csv` and motivate
robustness rows 3 and 8.

Anticipation check (2018 cohort, movement into the final pre-adoption year
relative to controls, VCA counties ran voter education and mail expansion
before launch): Napa +10.67, Nevada +8.62, Sacramento -0.54, San Mateo
-0.87, mean +4.47. Two counties moved up into event-time -1, which is why
the not-yet-treated variant matters: recomputing ATT(2018, 2018) against
the 8 not-yet-treated comparators (valid under no-anticipation) gives
-1.94 type-matched vs -6.62 against the never-treated pair, and -8.60
calendar vs -10.30 (San Diego is dropped as a comparator where a 2016 base
is needed, since it lacks 2016; details in `sensitivities.csv` row 6). The
divergence is reported, not resolved: it is consistent with either
anticipation in the treated or drift in the two controls.

The placebo-in-time check (row 7: adoption shifted one general earlier,
pre-period only, 6 cells) gives a mean of +0.91 pp, below the 3 pp trigger.

## Inference plan notes

Analytic cluster-robust standard errors are ruled out for this design (16
clusters, a 2-cluster control group, severe imbalance) and no such numbers
appear in this document. The wild cluster bootstrap is **absent by
design**: with the parameter identified off two control clusters it is
known-unreliable (MacKinnon-Webb), it would fail the synthetic coverage
validation this analysis requires of every reported inference procedure,
and it is not transparently hand-checkable.

The Fisher randomization engine permutes the observed adoption-label
multiset {2018 x5, 2020 x5, 2022 x3, 2024 x1, never x2} across the 16
counties, recomputes each statistic under identical rules, and rejects and
redraws degenerate assignments (any required cell empty, or a permuted
control missing a required year, e.g. Placer drawn as a control invalidates
theta_2024). Redraw rates per statistic (share of attempted draws
rejected): theta_2024 0.7676, theta_2022 0.5163, theta_step_2018 0.5097,
theta_step_2022 0.3717, pre-trend joint 0.6217, CI grid mean 0.7669
(`results.json`). The engine was validated before any real number was
read: under the sharp null its rejection rate is 0.0740 at alpha = 0.10
(99 percent band [0.0654, 0.1346]) and 0.0260 at alpha = 0.05 (band
[0.0249, 0.0751]), and the 90 percent test-inversion interval covers a true
constant effect with probability 0.9220 (`validation.json`, S1/S2).

## Robustness matrix (14 pre-specified checks)

The full grid is `sensitivities.csv`, included verbatim in the appendix.
Notable rows, with their pre-specified consequences:

1. **Control triptych.** theta_2024: +10.07 pooled, +6.78 vs SF, +13.37 vs
   SLO. Same sign everywhere, so the pooled headline stands (the
   sign-disagreement kill rule did not fire, for any aggregate).
2. **Base rule.** Type-matched vs calendar moves ATT(2018, 2018) from
   -6.62 to -10.30 (driven by Napa, Nevada and San Mateo taking 2014 vs
   2016 bases); theta_2024 moves only 10.07 to 9.39, no sign flip, no
   downgrade.
3. **Tier-1 only** (drops the 11 tier-2 rows, which cluster in treated
   pre-periods): theta_2024 = +10.30, a move of 0.23 pp, far under the 3 pp
   lead-with-it threshold. ATT(2022, 2022) loses Riverside entirely (its
   whole pre-period is tier 2) and rises to +11.23 on n = 2.
4. **Excluded 2024 points re-included as bounds.** With Nevada 2024
   (24.49, printer defect) re-included theta_2024 **drops to +6.91**; with
   Riverside 2024 (63.7, refuted plateau) re-included it is +10.04; with
   both, +7.14. The exclusions concentrated in treated post-years are a
   selection channel and these bounds travel with the headline.
5. **Leave-one-out.** Ranges above; no single county flips any aggregate's
   sign.
6. **Not-yet-treated comparators** for ATT(2018, 2018): -1.94 type-matched
   / -8.60 calendar (vs -6.62 / -10.30 never-treated).
7. **Placebo-in-time**: +0.91 pp mean, not triggered.
8. **Riverside excluded entirely** (pre-registered endogeneity case: its
   night share collapsed to 46.12 in 2018, years before its 2022 adoption, on
   all-secondary pre-data): theta_2022 +7.86 (n = 11), theta_step_2022
   +11.23 (n = 2), theta_2024 unchanged at +10.07 (Riverside's 2024 point
   was already excluded).
9. **ASV-augmented county-years excluded** (Nevada 2022, San Diego 2024):
   theta_2022 = +5.91 (n = 11), theta_2024 = +8.58 (n = 9). The headline
   direction is not driven by the two bundle+ASV county-years.
10. **Ballot-weighted** (a different estimand, effectively Los Angeles):
    theta_2024 = +15.14. Reported beside the county-weighted primary,
    never substituted.
11. **Logit transform**: all four aggregates keep sign (+0.44, +0.29,
    -0.26, +0.29 in logit units); no bounded-share artifact disqualifies
    the level-based claims.
12. **2020 restored**: a no-op by construction on this dataset, because
    only one usable 2020 row exists at all (San Francisco); no treated
    county has a 2020 outcome or gains a 2020 base year, so every
    aggregate is unchanged. The COVID exclusion cannot be driving
    conclusions when there is nothing to restore.
13. **Estimator dependence**: BJS beside cell means (discussed above; the
    theta_step_2022 divergence of -6.36 is flagged), static TWFE
    quarantined.
14. **Size split (descriptive only, no p-values)**: theta_2024 is +5.99 in
    the five smaller counties (Fresno, Madera, Napa, San Mateo, Ventura)
    and +14.16 in the five larger ones (Los Angeles, Orange, Sacramento,
    San Diego, Santa Clara), split at a median certified final of
    531306.50 ballots. Consistent with vote-center consolidation binding
    differently at Madera vs LA scale, and left as description.

Multiplicity discipline: theta_2024 was the single pre-declared headline;
rows 1-14 are diagnostics and nothing in the grid is promoted after seeing
results.

**Control-side shock sensitivity (validation S4, the design's key
non-identifiability):** a level shock of +s pp to both controls in
2022-2024 with zero treatment effect produces spurious theta_2024 of -s pp,
one for one: simulated shocks of +2, +5 and +8 pp produced spurious
theta_2024 of -2.00, -5.00 and -8.00 (per-pp coefficient -1.00). The design
cannot distinguish a bundle effect from control-side drift of the same
size, and the observed headline of +10.07 pp could in principle be
manufactured by an adverse control-side shock of comparable size specific
to SF and SLO in 2022-2024.

## Tier 3: ASV case studies (descriptive only)

**Inference at conventional levels is impossible by construction in this
tier**; the minimum attainable p-values are 0.1429 (Nevada pool of 7),
0.0833 (San Diego pool of 12), and 0.1667 (2020-cohort 6-assignment
permutation). These are exact-rank placebo positions, not estimates.

- **Nevada (ASV 2022)**: its 2018-to-2022 night-share change of +7.10 pp
  ranks **2nd of 7** against the six no-tech-change counties with both
  years usable (one-sided p = 0.2857).
- **San Diego (ASV 2024)**: its 2022-to-2024 change of +10.65 pp ranks
  **5th of 12** against the eleven no-change counties (one-sided
  p = 0.4167).
- **Within the 2020 cohort**, the bundle+ASV pair (Fresno, Los Angeles)
  vs the bundle-only pair (Orange, Santa Clara): observed difference in
  mean post-adoption deltas is **-4.19 pp**, the ASV pair doing worse; the
  exact 6-assignment permutation gives one-sided p = 1.0000.
- **San Bernardino** (pure e-pollbook, one usable row): its 2024 night
  share of 56.24 places 10th of the 13 counties with usable 2024 points.
  One row, no inference.

Framed as the falsifiable prediction from the spec: if ASV produced large
(above 10 pp) gains, its adopters would lead their cohorts. They do not
(rank 2/7 with a +7.10 change is the closest, and the within-cohort
contrast is negative). The design can rule out large ASV effects and says
nothing about small ones.

## Outcome validity

The outcome is the share of the certified final count posted in the last
report of election night (the plateau), and it is not a pure speed
measure: it conflates processing speed, the ballot-arrival mix, and each
county's choice of when to stop posting. San Luis Obispo's 2024 "final
election-night" report was generated the next day; every non-SF usable
point carries a plateau-review verdict from
`data/research/election-night/plateau_review.json`. Among the 78 usable
rows (counts from `panel.csv`): 68 CONFIRMED, 3 PLAUSIBLE, 1
REFUTED_AND_CORRECTED, and San Francisco's 6 home-dataset rows with no
review record, at primary confidence throughout; every REFUTED_AS_PLATEAU
row was already non-comparable and none enters the panel. Tier 2 (11 rows: secondary confidence or a
PLAUSIBLE verdict, including Sacramento 2012, primary but PLAUSIBLE) is
stress-tested in robustness row 3. Permitted outcome language is used
throughout: bundle counties "posted a larger share of their final count by
the end of election night"; no claim about counting speed is made.

## Limitations

- **Two controls carry everything after AB 37.** Every 2024 cell is
  identified only off SF and SLO. The two controls themselves drifted
  apart by several pp over the window (SF night share moved -14.50 pp from
  2012 to 2024, SLO -23.84 pp), which is exactly why the triptych gets
  equal billing with the p-value.
- **Control-side shocks are indistinguishable from treatment effects**
  (S4 above, one for one).
- **Adoption was selected, not assigned.** Counties chose the bundle and
  chose when; the RI p is a placebo benchmark, not design-based inference.
- **No external validity.** Nothing here generalizes to what would happen
  if San Francisco or San Luis Obispo adopted the bundle: adoption was
  selected, and the comparison is to two specific counties.
- **The headline mixes horizons** (6 years post for the 2018 cohort, 2
  years for the 2022 cohort) and reflects the post-AB 37 regime in which
  controls are also all-mail.
- **Detection floor.** Effects below the headline MDEs of 14.11 pp
  (alpha = 0.10) and 15.86 pp (alpha = 0.05) are not reliably detectable
  (power section above); the secondary statistics are uninformative below
  MDEs of 18.85 to 24.23 pp.
- **The mechanism covariate does not exist in-repo.** A per-county
  VBM-share series would allow a mediator decomposition
  (ballot-mix composition vs the rest); `packages/data/vbm_history.json`
  is SF-only, so that extension is gated on a separate research task and
  this analysis runs without it.

## Exclusion appendix

Every dropped point, with its documented reason (full text in
`results.json`, key `exclusions`; snippets abridged here):

| County | Year | Value | Reason |
|---|---|---|---|
| madera-ca | 2012 | null | no usable night figure (pct null) |
| madera-ca | 2014 | 80.42 | comparable=false; plateau verdict PLAUSIBLE (ceiling, not a confirmed plateau) |
| nevada-ca | 2024 | 24.49 | comparable=false; ballot-printer ink-overspray defect made tens of thousands of VBM ballots unreadable; hand-rescan ran to about Thanksgiving; excluded from tech comparison (re-included as a bound in robustness row 4) |
| placer-ca | 2012 | null | no usable night figure (pct null) |
| placer-ca | 2018 | 63.8 | comparable=false; REFUTED_AS_PLATEAU (GEMS semi-official, not the night plateau) |
| placer-ca | 2022 | null | no usable night figure (pct null) |
| placer-ca | 2024 | null | no usable night figure (pct null) |
| riverside-ca | 2024 | 63.7 | comparable=false; REFUTED_AS_PLATEAU (Nov 6 canvass update; the ~3 AM plateau is unarchived; re-included as a bound in row 4) |
| sacramento-ca | 2016 | null | no usable night figure (pct null) |
| san-bernardino-ca | 2012 | 82.19 | comparable=false; REFUTED_AS_PLATEAU |
| san-bernardino-ca | 2014 | 78.7 | comparable=false; REFUTED_AS_PLATEAU |
| san-bernardino-ca | 2016 | null | no usable night figure (pct null) |
| san-bernardino-ca | 2018 | 58.97 | comparable=false; REFUTED_AS_PLATEAU |
| san-bernardino-ca | 2022 | 47.72 | comparable=false; REFUTED_AS_PLATEAU |
| san-diego-ca | 2016 | 53.96 | comparable=false; REFUTED_AS_PLATEAU |
| san-francisco-ca | 2020 | 78.4 | 2020 excluded by design (COVID election); the only 2020 point in the dataset, see robustness row 12 |
| santa-clara-ca | 2014 | 62.26 | comparable=false; PLAUSIBLE ceiling (next-day all-precincts report) |
| santa-clara-ca | 2016 | 41.91 | comparable=false; PLAUSIBLE; night plateau not sourceable |
| santa-clara-ca | 2018 | 48.61 | comparable=false; PLAUSIBLE; night plateau not sourceable |

Santa Clara 2024 is REFUTED_AND_CORRECTED (value corrected to the true
night plateau and kept in the panel), not an exclusion.

---

## Appendix: generated tables (verbatim)

Treatment in every table: the VCA modernization bundle (vote centers +
universal mailed ballots + e-pollbooks, one package). No table below is an
e-pollbook or ASV effect.

### aggregates.csv (VCA modernization bundle)

```
statistic,rule,n,counties,est_pooled,est_sf_only,est_slo_only,ri_p,ri_p_mc_se,holm_p,redraw_rate,null_sd,mde_alpha10_power80,mde_alpha05_power80,ci90_lo,ci90_hi,loo_min,loo_max,loo_sign_flip_drops
theta_2024,type-matched,10,fresno-ca+los-angeles-ca+madera-ca+napa-ca+orange-ca+sacramento-ca+san-diego-ca+san-mateo-ca+santa-clara-ca+ventura-ca,10.07,6.78,13.37,0.0663,0.0025,,0.7676,5.67,14.11,15.86,2.00,19.00,6.78,13.37,none
theta_2022,type-matched,12,fresno-ca+los-angeles-ca+madera-ca+napa-ca+nevada-ca+orange-ca+riverside-ca+sacramento-ca+san-diego-ca+san-mateo-ca+santa-clara-ca+ventura-ca,7.20,3.95,10.45,0.3251,0.0047,0.9752,0.5163,6.73,16.76,18.85,,,3.95,10.45,none
theta_step_2018,type-matched,5,madera-ca+napa-ca+nevada-ca+sacramento-ca+san-mateo-ca,-6.62,-5.38,-7.85,0.3952,0.0049,0.9752,0.5097,7.21,17.95,20.18,,,-8.84,-3.21,none
theta_step_2022,type-matched,3,riverside-ca+san-diego-ca+ventura-ca,7.44,3.76,11.13,0.4147,0.0049,0.9752,0.3717,8.65,21.55,24.23,,,0.91,11.23,none
theta_2024,calendar,10,fresno-ca+los-angeles-ca+madera-ca+napa-ca+orange-ca+sacramento-ca+san-diego-ca+san-mateo-ca+santa-clara-ca+ventura-ca,9.39,6.02,12.77,,,,,,,,,,,,
theta_2022,calendar,12,fresno-ca+los-angeles-ca+madera-ca+napa-ca+nevada-ca+orange-ca+riverside-ca+sacramento-ca+san-diego-ca+san-mateo-ca+santa-clara-ca+ventura-ca,5.66,2.34,8.99,,,,,,,,,,,,
theta_step_2018,calendar,5,madera-ca+napa-ca+nevada-ca+sacramento-ca+san-mateo-ca,-10.30,-9.24,-11.36,,,,,,,,,,,,
theta_step_2022,calendar,3,riverside-ca+san-diego-ca+ventura-ca,7.44,3.76,11.13,,,,,,,,,,,,
```

### att_matrix.csv (VCA modernization bundle)

```
rule,cohort,year,row_type,county,base_year,weight,y_t,y_base,ctrl_change,delta_pooled,delta_sf_only,delta_slo_only,flags,n
type-matched,2018,2018,component,madera-ca,2016,0.2000,72.26,80.00,-5.79,-1.94,-0.94,-2.95,fallback,5
type-matched,2018,2018,component,napa-ca,2014,0.2000,38.11,47.17,-9.71,0.65,1.94,-0.64,,5
type-matched,2018,2018,component,nevada-ca,2014,0.2000,49.01,56.44,-9.71,2.28,3.57,0.99,,5
type-matched,2018,2018,component,sacramento-ca,2014,0.2000,35.52,59.04,-9.71,-13.81,-12.52,-15.10,,5
type-matched,2018,2018,component,san-mateo-ca,2014,0.2000,38.49,68.46,-9.71,-20.26,-18.97,-21.55,,5
type-matched,2018,2018,cell_mean,madera-ca+napa-ca+nevada-ca+sacramento-ca+san-mateo-ca,,,,,,-6.62,-5.38,-7.85,,5
type-matched,2018,2022,component,madera-ca,2016,0.2000,58.78,80.00,-17.78,-3.44,-6.12,-0.76,fallback,5
type-matched,2018,2022,component,napa-ca,2014,0.2000,43.21,47.17,-21.70,17.73,15.34,20.13,,5
type-matched,2018,2022,component,nevada-ca,2014,0.2000,56.11,56.44,-21.70,21.37,18.97,23.76,,5
type-matched,2018,2022,component,sacramento-ca,2014,0.2000,29.94,59.04,-21.70,-7.40,-9.80,-5.01,,5
type-matched,2018,2022,component,san-mateo-ca,2014,0.2000,48.42,68.46,-21.70,1.66,-0.74,4.05,,5
type-matched,2018,2022,cell_mean,madera-ca+napa-ca+nevada-ca+sacramento-ca+san-mateo-ca,,,,,,5.98,3.53,8.43,,5
type-matched,2018,2024,component,madera-ca,2016,0.2500,67.10,80.00,-11.90,-1.00,-3.70,1.71,,4
type-matched,2018,2024,component,napa-ca,2016,0.2500,39.26,53.92,-11.90,-2.76,-5.46,-0.05,,4
type-matched,2018,2024,component,sacramento-ca,2012,0.2500,46.65,62.93,-19.17,2.89,-1.78,7.56,long_gap,4
type-matched,2018,2024,component,san-mateo-ca,2016,0.2500,63.28,63.67,-11.90,11.51,8.81,14.22,,4
type-matched,2018,2024,cell_mean,madera-ca+napa-ca+sacramento-ca+san-mateo-ca,,,,,,2.66,-0.53,5.86,,4
type-matched,2020,2022,component,fresno-ca,2018,0.2500,57.10,61.09,-11.98,7.99,4.31,11.68,,4
type-matched,2020,2022,component,los-angeles-ca,2018,0.2500,53.65,65.35,-11.98,0.29,-3.40,3.97,,4
type-matched,2020,2022,component,orange-ca,2018,0.2500,61.46,58.79,-11.98,14.65,10.97,18.34,,4
type-matched,2020,2022,component,santa-clara-ca,2012,0.2500,53.24,67.10,-25.05,11.19,6.54,15.83,fallback;long_gap,4
type-matched,2020,2022,cell_mean,fresno-ca+los-angeles-ca+orange-ca+santa-clara-ca,,,,,,8.53,4.61,12.45,,4
type-matched,2020,2024,component,fresno-ca,2016,0.2500,62.36,60.70,-11.90,13.56,10.86,16.27,,4
type-matched,2020,2024,component,los-angeles-ca,2016,0.2500,68.96,65.07,-11.90,15.79,13.09,18.50,,4
type-matched,2020,2024,component,orange-ca,2016,0.2500,71.06,66.59,-11.90,16.37,13.67,19.08,,4
type-matched,2020,2024,component,santa-clara-ca,2012,0.2500,60.13,67.10,-19.17,12.20,7.53,16.87,long_gap,4
type-matched,2020,2024,cell_mean,fresno-ca+los-angeles-ca+orange-ca+santa-clara-ca,,,,,,14.48,11.29,17.68,,4
type-matched,2022,2022,component,riverside-ca,2018,0.3333,34.00,46.12,-11.98,-0.14,-3.82,3.55,,3
type-matched,2022,2022,component,san-diego-ca,2018,0.3333,54.24,45.72,-11.98,20.50,16.82,24.19,,3
type-matched,2022,2022,component,ventura-ca,2018,0.3333,54.11,64.13,-11.98,1.96,-1.72,5.65,,3
type-matched,2022,2022,cell_mean,riverside-ca+san-diego-ca+ventura-ca,,,,,,7.44,3.76,11.13,,3
type-matched,2022,2024,component,san-diego-ca,2012,0.5000,64.89,60.52,-19.17,23.54,18.87,28.21,long_gap,2
type-matched,2022,2024,component,ventura-ca,2016,0.5000,67.79,71.09,-11.90,8.61,5.90,11.31,,2
type-matched,2022,2024,cell_mean,san-diego-ca+ventura-ca,,,,,,16.07,12.39,19.76,,2
calendar,2018,2018,component,madera-ca,2016,0.2000,72.26,80.00,-5.79,-1.94,-0.94,-2.95,,5
calendar,2018,2018,component,napa-ca,2016,0.2000,38.11,53.92,-5.79,-10.02,-9.01,-11.02,,5
calendar,2018,2018,component,nevada-ca,2016,0.2000,49.01,61.14,-5.79,-6.34,-5.33,-7.34,,5
calendar,2018,2018,component,sacramento-ca,2014,0.2000,35.52,59.04,-9.71,-13.81,-12.52,-15.10,,5
calendar,2018,2018,component,san-mateo-ca,2016,0.2000,38.49,63.67,-5.79,-19.39,-18.38,-20.39,,5
calendar,2018,2018,cell_mean,madera-ca+napa-ca+nevada-ca+sacramento-ca+san-mateo-ca,,,,,,-10.30,-9.24,-11.36,,5
calendar,2018,2022,component,madera-ca,2016,0.2000,58.78,80.00,-17.78,-3.44,-6.12,-0.76,,5
calendar,2018,2022,component,napa-ca,2016,0.2000,43.21,53.92,-17.78,7.07,4.39,9.75,,5
calendar,2018,2022,component,nevada-ca,2016,0.2000,56.11,61.14,-17.78,12.75,10.07,15.43,,5
calendar,2018,2022,component,sacramento-ca,2014,0.2000,29.94,59.04,-21.70,-7.40,-9.80,-5.01,,5
calendar,2018,2022,component,san-mateo-ca,2016,0.2000,48.42,63.67,-17.78,2.53,-0.15,5.21,,5
calendar,2018,2022,cell_mean,madera-ca+napa-ca+nevada-ca+sacramento-ca+san-mateo-ca,,,,,,2.30,-0.32,4.92,,5
calendar,2018,2024,component,madera-ca,2016,0.2500,67.10,80.00,-11.90,-1.00,-3.70,1.71,,4
calendar,2018,2024,component,napa-ca,2016,0.2500,39.26,53.92,-11.90,-2.76,-5.46,-0.05,,4
calendar,2018,2024,component,sacramento-ca,2014,0.2500,46.65,59.04,-15.82,3.43,1.01,5.85,long_gap,4
calendar,2018,2024,component,san-mateo-ca,2016,0.2500,63.28,63.67,-11.90,11.51,8.81,14.22,,4
calendar,2018,2024,cell_mean,madera-ca+napa-ca+sacramento-ca+san-mateo-ca,,,,,,2.80,0.16,5.43,,4
calendar,2020,2022,component,fresno-ca,2018,0.2500,57.10,61.09,-11.98,7.99,4.31,11.68,,4
calendar,2020,2022,component,los-angeles-ca,2018,0.2500,53.65,65.35,-11.98,0.29,-3.40,3.97,,4
calendar,2020,2022,component,orange-ca,2018,0.2500,61.46,58.79,-11.98,14.65,10.97,18.34,,4
calendar,2020,2022,component,santa-clara-ca,2012,0.2500,53.24,67.10,-25.05,11.19,6.54,15.83,long_gap,4
calendar,2020,2022,cell_mean,fresno-ca+los-angeles-ca+orange-ca+santa-clara-ca,,,,,,8.53,4.61,12.45,,4
calendar,2020,2024,component,fresno-ca,2018,0.2500,62.36,61.09,-6.11,7.38,3.67,11.09,,4
calendar,2020,2024,component,los-angeles-ca,2018,0.2500,68.96,65.35,-6.11,9.72,6.01,13.43,,4
calendar,2020,2024,component,orange-ca,2018,0.2500,71.06,58.79,-6.11,18.38,14.67,22.09,,4
calendar,2020,2024,component,santa-clara-ca,2012,0.2500,60.13,67.10,-19.17,12.20,7.53,16.87,long_gap,4
calendar,2020,2024,cell_mean,fresno-ca+los-angeles-ca+orange-ca+santa-clara-ca,,,,,,11.92,7.97,15.87,,4
calendar,2022,2022,component,riverside-ca,2018,0.3333,34.00,46.12,-11.98,-0.14,-3.82,3.55,,3
calendar,2022,2022,component,san-diego-ca,2018,0.3333,54.24,45.72,-11.98,20.50,16.82,24.19,,3
calendar,2022,2022,component,ventura-ca,2018,0.3333,54.11,64.13,-11.98,1.96,-1.72,5.65,,3
calendar,2022,2022,cell_mean,riverside-ca+san-diego-ca+ventura-ca,,,,,,7.44,3.76,11.13,,3
calendar,2022,2024,component,san-diego-ca,2018,0.5000,64.89,45.72,-6.11,25.28,21.57,28.99,,2
calendar,2022,2024,component,ventura-ca,2018,0.5000,67.79,64.13,-6.11,9.77,6.06,13.48,,2
calendar,2022,2024,cell_mean,san-diego-ca+ventura-ca,,,,,,17.53,13.82,21.24,,2
```

### pretrends.csv (VCA modernization bundle)

```
county,cohort,year,base_year,event_time_years,delta_pre,tier1_cell
napa-ca,2018,2012,2016,-6,-4.46,yes
napa-ca,2018,2014,2016,-4,-10.67,no
nevada-ca,2018,2012,2016,-6,-8.47,yes
nevada-ca,2018,2014,2016,-4,-8.62,yes
sacramento-ca,2018,2012,2014,-6,0.54,no
san-mateo-ca,2018,2012,2016,-6,-0.15,yes
san-mateo-ca,2018,2014,2016,-4,0.87,yes
fresno-ca,2020,2012,2018,-8,-12.85,no
fresno-ca,2020,2014,2018,-6,3.13,no
fresno-ca,2020,2016,2018,-4,-6.18,no
los-angeles-ca,2020,2012,2018,-8,-5.24,yes
los-angeles-ca,2020,2014,2018,-6,0.47,yes
los-angeles-ca,2020,2016,2018,-4,-6.07,yes
orange-ca,2020,2012,2018,-8,4.27,yes
orange-ca,2020,2014,2018,-6,4.01,yes
orange-ca,2020,2016,2018,-4,2.01,yes
riverside-ca,2022,2012,2018,-10,13.49,no
riverside-ca,2022,2014,2018,-8,18.18,no
riverside-ca,2022,2016,2018,-6,14.03,no
san-diego-ca,2022,2012,2018,-10,1.74,no
san-diego-ca,2022,2014,2018,-8,18.11,no
ventura-ca,2022,2012,2018,-10,0.57,yes
ventura-ca,2022,2014,2018,-8,1.46,yes
ventura-ca,2022,2016,2018,-6,1.17,yes
placer-ca,2024,2014,2016,-10,4.63,yes
```

### sensitivities.csv (VCA modernization bundle)

```
check,name,variant,statistic,value,n,note
1,control_triptych,pooled,theta_2024,10.07,10,
1,control_triptych,pooled,theta_2022,7.20,12,
1,control_triptych,pooled,theta_step_2018,-6.62,5,
1,control_triptych,pooled,theta_step_2022,7.44,3,
1,control_triptych,sf,theta_2024,6.78,10,
1,control_triptych,sf,theta_2022,3.95,12,
1,control_triptych,sf,theta_step_2018,-5.38,5,
1,control_triptych,sf,theta_step_2022,3.76,3,
1,control_triptych,slo,theta_2024,13.37,10,
1,control_triptych,slo,theta_2022,10.45,12,
1,control_triptych,slo,theta_step_2018,-7.85,5,
1,control_triptych,slo,theta_step_2022,11.13,3,
2,base_rule,type,theta_2024,10.07,10,
2,base_rule,type,theta_2022,7.20,12,
2,base_rule,type,theta_step_2018,-6.62,5,
2,base_rule,type,theta_step_2022,7.44,3,
2,base_rule,calendar,theta_2024,9.39,10,
2,base_rule,calendar,theta_2022,5.66,12,
2,base_rule,calendar,theta_step_2018,-10.30,5,
2,base_rule,calendar,theta_step_2022,7.44,3,
2,base_rule,flip_check,theta_2024_sign_flip,,,False
3,tier1_only,drop_11_tier2_rows,theta_2024,10.30,10,
3,tier1_only,drop_11_tier2_rows,theta_2022,7.46,11,
3,tier1_only,drop_11_tier2_rows,theta_step_2018,-8.75,5,
3,tier1_only,drop_11_tier2_rows,theta_step_2022,11.23,2,
4,excluded_2024_bounds,nevada_2024_included,theta_2024,6.91,11,
4,excluded_2024_bounds,riverside_2024_included,theta_2024,10.04,11,
4,excluded_2024_bounds,both_included,theta_2024,7.14,12,
5,leave_one_out,min,theta_2024,6.78,,drop san-luis-obispo-ca
5,leave_one_out,max,theta_2024,13.37,,drop san-francisco-ca
5,leave_one_out,sign_flips,theta_2024,,,none
5,leave_one_out,min,theta_2022,3.95,,drop san-luis-obispo-ca
5,leave_one_out,max,theta_2022,10.45,,drop san-francisco-ca
5,leave_one_out,sign_flips,theta_2022,,,none
5,leave_one_out,min,theta_step_2018,-8.84,,drop nevada-ca
5,leave_one_out,max,theta_step_2018,-3.21,,drop san-mateo-ca
5,leave_one_out,sign_flips,theta_step_2018,,,none
5,leave_one_out,min,theta_step_2022,0.91,,drop san-diego-ca
5,leave_one_out,max,theta_step_2022,11.23,,drop riverside-ca
5,leave_one_out,sign_flips,theta_step_2022,,,none
6,not_yet_treated_att2018,type,theta_step_2018,-1.94,5,"never-treated version -6.62; comparators dropped: san-diego-ca (for madera-ca, base 2016)"
6,not_yet_treated_att2018,calendar,theta_step_2018,-8.60,5,"never-treated version -10.30; comparators dropped: san-diego-ca (for madera-ca, base 2016); san-diego-ca (for napa-ca, base 2016); san-diego-ca (for nevada-ca, base 2016); san-diego-ca (for san-mateo-ca, base 2016)"
7,placebo_in_time,shift_one_general_earlier,mean_placebo_delta,0.91,6,cells: fresno-ca@2018(base 2014)=-3.13; los-angeles-ca@2018(base 2014)=-0.47; napa-ca@2016(base 2012)=4.46; nevada-ca@2016(base 2012)=8.47; orange-ca@2018(base 2014)=-4.01; san-mateo-ca@2016(base 2012)=0.15
8,riverside_excluded,drop_riverside,theta_2024,10.07,10,
8,riverside_excluded,drop_riverside,theta_2022,7.86,11,
8,riverside_excluded,drop_riverside,theta_step_2018,-6.62,5,
8,riverside_excluded,drop_riverside,theta_step_2022,11.23,2,
9,asv_rows_excluded,drop_nevada2022_sandiego2024,theta_2022,5.91,11,
9,asv_rows_excluded,drop_nevada2022_sandiego2024,theta_2024,8.58,9,
10,ballot_weighted,final_ballots_at_t,theta_2024,15.14,10,
10,ballot_weighted,final_ballots_at_t,theta_2022,6.23,12,
10,ballot_weighted,final_ballots_at_t,theta_step_2018,-13.50,5,
10,ballot_weighted,final_ballots_at_t,theta_step_2022,11.32,3,
11,logit_transform,logit_pct,theta_2024,0.44,10,logit units
11,logit_transform,logit_pct,theta_2022,0.29,12,logit units
11,logit_transform,logit_pct,theta_step_2018,-0.26,5,logit units
11,logit_transform,logit_pct,theta_step_2022,0.29,3,logit units
11,logit_transform,sign_flips,any,,,none
12,restore_2020,include_covid_election,theta_2024,10.07,10,only 1 usable 2020 row exists in the canonical dataset (san-francisco-ca); restoring 2020 adds no treated outcome or base year
12,restore_2020,include_covid_election,theta_2022,7.20,12,only 1 usable 2020 row exists in the canonical dataset (san-francisco-ca); restoring 2020 adds no treated outcome or base year
12,restore_2020,include_covid_election,theta_step_2018,-6.62,5,only 1 usable 2020 row exists in the canonical dataset (san-francisco-ca); restoring 2020 adds no treated outcome or base year
12,restore_2020,include_covid_election,theta_step_2022,7.44,3,only 1 usable 2020 row exists in the canonical dataset (san-francisco-ca); restoring 2020 adds no treated outcome or base year
13,estimator_dependence,bjs_imputation,theta_2024,9.64,,cell-mean 10.07; divergence -0.43
13,estimator_dependence,bjs_imputation,theta_2022,5.44,,cell-mean 7.20; divergence -1.75
13,estimator_dependence,bjs_imputation,theta_step_2018,-5.74,,cell-mean -6.62; divergence 0.87
13,estimator_dependence,bjs_imputation,theta_step_2022,1.08,,cell-mean 7.44; divergence -6.36
13,estimator_dependence,static_twfe_exhibit,beta_post,1.46,,known-biased; quarantined; see validation.json S3
14,size_split,small_counties,theta_2024_descriptive,5.99,5,final<=median(531306.50): fresno-ca+madera-ca+napa-ca+san-mateo-ca+ventura-ca
14,size_split,large_counties,theta_2024_descriptive,14.16,5,final>median: los-angeles-ca+orange-ca+sacramento-ca+san-diego-ca+santa-clara-ca
```

### asv_descriptives.csv (VCA modernization bundle)

```
test,row_type,unit,value,rank,n_pool,exact_one_sided_p,min_attainable_p,note
nevada_asv_2018_to_2022,pool_change,san-mateo-ca,9.93,,,,,
nevada_asv_2018_to_2022,pool_change,nevada-ca,7.10,2,7,0.2857,0.1429,ASV adopter
nevada_asv_2018_to_2022,pool_change,napa-ca,5.10,,,,,
nevada_asv_2018_to_2022,pool_change,sacramento-ca,-5.58,,,,,
nevada_asv_2018_to_2022,pool_change,san-francisco-ca,-8.30,,,,,
nevada_asv_2018_to_2022,pool_change,madera-ca,-13.48,,,,,
nevada_asv_2018_to_2022,pool_change,san-luis-obispo-ca,-15.67,,,,,
san_diego_asv_2022_to_2024,pool_change,sacramento-ca,16.71,,,,,
san_diego_asv_2022_to_2024,pool_change,los-angeles-ca,15.31,,,,,
san_diego_asv_2022_to_2024,pool_change,san-mateo-ca,14.86,,,,,
san_diego_asv_2022_to_2024,pool_change,ventura-ca,13.68,,,,,
san_diego_asv_2022_to_2024,pool_change,san-diego-ca,10.65,5,12,0.4167,0.0833,ASV adopter
san_diego_asv_2022_to_2024,pool_change,orange-ca,9.60,,,,,
san_diego_asv_2022_to_2024,pool_change,madera-ca,8.32,,,,,
san_diego_asv_2022_to_2024,pool_change,santa-clara-ca,6.89,,,,,
san_diego_asv_2022_to_2024,pool_change,san-francisco-ca,5.90,,,,,
san_diego_asv_2022_to_2024,pool_change,san-luis-obispo-ca,5.85,,,,,
san_diego_asv_2022_to_2024,pool_change,fresno-ca,5.26,,,,,
san_diego_asv_2022_to_2024,pool_change,napa-ca,-3.95,,,,,
cohort2020_asv_contrast,mean_post_delta,fresno-ca,10.78,,,,,bundle+ASV
cohort2020_asv_contrast,mean_post_delta,los-angeles-ca,8.04,,,,,bundle+ASV
cohort2020_asv_contrast,mean_post_delta,orange-ca,15.51,,,,,bundle only
cohort2020_asv_contrast,mean_post_delta,santa-clara-ca,11.69,,,,,bundle only
cohort2020_asv_contrast,observed_diff,fresno+los-angeles minus orange+santa-clara,-4.19,,6,1.0000,0.1667,exact 6-assignment permutation
san_bernardino_2024_placement,night_share_2024,orange-ca,71.06,,,,,
san_bernardino_2024_placement,night_share_2024,los-angeles-ca,68.96,,,,,
san_bernardino_2024_placement,night_share_2024,ventura-ca,67.79,,,,,
san_bernardino_2024_placement,night_share_2024,madera-ca,67.10,,,,,
san_bernardino_2024_placement,night_share_2024,san-diego-ca,64.89,,,,,
san_bernardino_2024_placement,night_share_2024,san-mateo-ca,63.28,,,,,
san_bernardino_2024_placement,night_share_2024,fresno-ca,62.36,,,,,
san_bernardino_2024_placement,night_share_2024,santa-clara-ca,60.13,,,,,
san_bernardino_2024_placement,night_share_2024,san-francisco-ca,56.90,,,,,
san_bernardino_2024_placement,night_share_2024,san-bernardino-ca,56.24,10,13,,,"pure e-pollbook county; descriptive only, no inference"
san_bernardino_2024_placement,night_share_2024,san-luis-obispo-ca,53.80,,,,,
san_bernardino_2024_placement,night_share_2024,sacramento-ca,46.65,,,,,
san_bernardino_2024_placement,night_share_2024,napa-ca,39.26,,,,,
```

### panel.csv (VCA modernization bundle)

The `asv_year` column is the county's ASV adoption year exactly as
recorded in `packages/data/county_tech.json`, so a hand-verifier sees the
same value in both places. The 2025 adoptions (Riverside, San Bernardino)
are post-window and enter no estimate; only ASV years through 2024
(Nevada 2022, San Diego 2024, Fresno 2020, Los Angeles 2020) are used in
the analysis.

```
county,year,type,pct,ballots,final,confidence,verdict,tier,cohort,asv_year,base_type_matched,base_calendar,flags
fresno-ca,2012,presidential,61.30,160400,261652,secondary,CONFIRMED,2,2020,2020,,,
fresno-ca,2014,midterm,73.93,120820,163420,secondary,PLAUSIBLE,2,2020,2020,,,
fresno-ca,2016,presidential,60.70,177183,291890,primary,CONFIRMED,1,2020,2020,,,
fresno-ca,2018,midterm,61.09,156972,256972,secondary,CONFIRMED,2,2020,2020,,,
fresno-ca,2022,midterm,57.10,126440,221419,primary,CONFIRMED,1,2020,2020,2018,2018,
fresno-ca,2024,presidential,62.36,206372,330932,primary,CONFIRMED,1,2020,2020,2016,2018,
los-angeles-ca,2012,presidential,73.17,2368283,3236704,primary,CONFIRMED,1,2020,2020,,,
los-angeles-ca,2014,midterm,75.53,1147248,1518835,primary,CONFIRMED,1,2020,2020,,,
los-angeles-ca,2016,presidential,65.07,2306321,3544115,primary,CONFIRMED,1,2020,2020,,,
los-angeles-ca,2018,midterm,65.35,1975855,3023417,primary,CONFIRMED,1,2020,2020,,,
los-angeles-ca,2022,midterm,53.65,1318093,2456701,primary,CONFIRMED,1,2020,2020,2018,2018,
los-angeles-ca,2024,presidential,68.96,2615541,3793106,primary,CONFIRMED,1,2020,2020,2016,2018,
madera-ca,2016,presidential,80.00,35364,44186,primary,CONFIRMED,1,2018,,,,
madera-ca,2018,midterm,72.26,28159,38968,primary,CONFIRMED,1,2018,,2016,2016,fallback_type
madera-ca,2022,midterm,58.78,21951,37345,primary,CONFIRMED,1,2018,,2016,2016,fallback_type
madera-ca,2024,presidential,67.10,37106,55329,primary,CONFIRMED,1,2018,,2016,2016,
napa-ca,2012,presidential,56.73,32715,57672,primary,CONFIRMED,1,2018,,,,
napa-ca,2014,midterm,47.17,18286,38766,secondary,PLAUSIBLE,2,2018,,,,
napa-ca,2016,presidential,53.92,34108,63255,primary,CONFIRMED,1,2018,,,,
napa-ca,2018,midterm,38.11,21774,57132,primary,CONFIRMED,1,2018,,2014,2016,
napa-ca,2022,midterm,43.21,21943,50788,primary,CONFIRMED,1,2018,,2014,2016,
napa-ca,2024,presidential,39.26,26160,66634,primary,CONFIRMED,1,2018,,2016,2016,
nevada-ca,2012,presidential,59.94,31275,52173,primary,CONFIRMED,1,2018,2022,,,
nevada-ca,2014,midterm,56.44,22366,39629,primary,CONFIRMED,1,2018,2022,,,
nevada-ca,2016,presidential,61.14,34728,56800,primary,CONFIRMED,1,2018,2022,,,
nevada-ca,2018,midterm,49.01,26956,54996,primary,CONFIRMED,1,2018,2022,2014,2016,
nevada-ca,2022,midterm,56.11,28824,51370,primary,CONFIRMED,1,2018,2022,2014,2016,
orange-ca,2012,presidential,76.12,862544,1133204,primary,CONFIRMED,1,2020,,,,
orange-ca,2014,midterm,72.51,464313,640358,primary,CONFIRMED,1,2020,,,,
orange-ca,2016,presidential,66.59,825317,1239405,primary,CONFIRMED,1,2020,,,,
orange-ca,2018,midterm,58.79,650671,1106729,primary,CONFIRMED,1,2020,,,,
orange-ca,2022,midterm,61.46,611060,994277,primary,CONFIRMED,1,2020,,2018,2018,
orange-ca,2024,presidential,71.06,1007150,1417397,primary,CONFIRMED,1,2020,,2016,2018,
placer-ca,2014,midterm,66.10,76411,115547,primary,CONFIRMED,1,2024,,,,
placer-ca,2016,presidential,57.55,109666,190550,primary,CONFIRMED,1,2024,,,,
riverside-ca,2012,presidential,72.67,486627,669627,secondary,CONFIRMED,2,2022,2025,,,
riverside-ca,2014,midterm,74.01,264764,357764,secondary,CONFIRMED,2,2022,2025,,,
riverside-ca,2016,presidential,65.94,507193,769193,secondary,CONFIRMED,2,2022,2025,,,
riverside-ca,2018,midterm,46.12,300000,650545,secondary,CONFIRMED,2,2022,2025,,,
riverside-ca,2022,midterm,34.00,205813,604617,primary,CONFIRMED,1,2022,2025,2018,2018,
sacramento-ca,2012,presidential,62.93,328516,522045,primary,PLAUSIBLE,2,2018,,,,
sacramento-ca,2014,midterm,59.04,195317,330817,primary,CONFIRMED,1,2018,,,,
sacramento-ca,2018,midterm,35.52,185623,522652,primary,CONFIRMED,1,2018,,2014,2014,
sacramento-ca,2022,midterm,29.94,145015,484315,primary,CONFIRMED,1,2018,,2014,2014,
sacramento-ca,2024,presidential,46.65,311821,668416,primary,CONFIRMED,1,2018,,2012,2014,long_gap_type;long_gap_calendar
san-bernardino-ca,2024,presidential,56.24,434108,771834,primary,CONFIRMED,1,2020,2025,,,
san-diego-ca,2012,presidential,60.52,728265,1203265,secondary,CONFIRMED,2,2022,2024,,,
san-diego-ca,2014,midterm,73.54,509214,692434,secondary,CONFIRMED,2,2022,2024,,,
san-diego-ca,2018,midterm,45.72,536734,1173924,primary,CONFIRMED,1,2022,2024,,,
san-diego-ca,2022,midterm,54.24,565982,1043490,primary,CONFIRMED,1,2022,2024,2018,2018,
san-diego-ca,2024,presidential,64.89,975373,1503018,primary,CONFIRMED,1,2022,2024,2012,2018,long_gap_type
san-francisco-ca,2012,presidential,71.40,260521,364875,primary,NONE_SF_HOME_DATASET,1,never,,,,
san-francisco-ca,2014,midterm,70.30,162543,231214,primary,NONE_SF_HOME_DATASET,1,never,,,,
san-francisco-ca,2016,presidential,66.10,274003,414528,primary,NONE_SF_HOME_DATASET,1,never,,,,
san-francisco-ca,2018,midterm,59.30,221099,372848,primary,NONE_SF_HOME_DATASET,1,never,,,,
san-francisco-ca,2022,midterm,51.00,158136,310071,primary,NONE_SF_HOME_DATASET,1,never,,,,
san-francisco-ca,2024,presidential,56.90,234559,412231,primary,NONE_SF_HOME_DATASET,1,never,,,,
san-luis-obispo-ca,2012,presidential,77.64,98458,126818,primary,CONFIRMED,1,never,,,,
san-luis-obispo-ca,2014,midterm,72.04,63180,87705,primary,CONFIRMED,1,never,,,,
san-luis-obispo-ca,2016,presidential,68.41,95560,139685,primary,CONFIRMED,1,never,,,,
san-luis-obispo-ca,2018,midterm,63.62,81663,128353,primary,CONFIRMED,1,never,,,,
san-luis-obispo-ca,2022,midterm,47.95,58096,121156,primary,CONFIRMED,1,never,,,,
san-luis-obispo-ca,2024,presidential,53.80,82548,153432,primary,CONFIRMED,1,never,,,,
san-mateo-ca,2012,presidential,70.79,204287,288592,primary,CONFIRMED,1,2018,,,,
san-mateo-ca,2014,midterm,68.46,112592,164453,primary,CONFIRMED,1,2018,,,,
san-mateo-ca,2016,presidential,63.67,205855,323303,primary,CONFIRMED,1,2018,,,,
san-mateo-ca,2018,midterm,38.49,111637,290058,primary,CONFIRMED,1,2018,,2014,2016,
san-mateo-ca,2022,midterm,48.42,122135,252233,primary,CONFIRMED,1,2018,,2014,2016,
san-mateo-ca,2024,presidential,63.28,213421,337241,primary,CONFIRMED,1,2018,,2016,2016,
santa-clara-ca,2012,presidential,67.10,438348,653239,primary,CONFIRMED,1,2020,,,,
santa-clara-ca,2022,midterm,53.24,293148,550602,primary,CONFIRMED,1,2020,,2012,2012,fallback_type;long_gap_type;long_gap_calendar
santa-clara-ca,2024,presidential,60.13,460325,765495,primary,REFUTED_AND_CORRECTED,1,2020,,2012,2012,long_gap_type;long_gap_calendar
ventura-ca,2012,presidential,77.76,256927,330419,primary,CONFIRMED,1,2022,,,,
ventura-ca,2014,midterm,75.30,153442,203783,primary,CONFIRMED,1,2022,,,,
ventura-ca,2016,presidential,71.09,258250,363285,primary,CONFIRMED,1,2022,,,,
ventura-ca,2018,midterm,64.13,201298,313871,primary,CONFIRMED,1,2022,,,,
ventura-ca,2022,midterm,54.11,153682,284013,primary,CONFIRMED,1,2022,,2018,2018,
ventura-ca,2024,presidential,67.79,267226,394197,primary,CONFIRMED,1,2022,,2016,2018,
```
