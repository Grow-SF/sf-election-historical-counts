# Vote-center counties are weathering the election-night slowdown about 10 points better than everyone else

**Date:** 2026-07-10
**Panel pinned at:** commit `9bff066` (`packages/data/county_night.json`, read via `git show 9bff066:...` so every figure below is reproducible against the committed HEAD, not a working-tree snapshot)
**Estimator:** `scripts/research/estimate_tech_effect.py` (matched-cells difference-in-differences, leave-one-county-out jackknife inference, randomization placebo)
**Composition kernel:** `docs/analysis/2026-07-10-vbm-composition-curve.md` (companion, committed, not superseded)
**Supersedes:** `docs/analysis/2026-07-10-tech-effect-estimate.md`

Every number in this document was recomputed by the author against the pinned panel at HEAD `9bff066`; the exact commands are in Appendix A. Integration of a preserved pending corpus (`docs/research/pending-integration-2026-07-10/`, roughly 46 additional recovered primary cells plus the 87-cell Secretary of State apply-list) continues after this document lands and is expected to refine the decimals below without changing their direction.

## Executive summary

California's election-night counts have been getting slower almost everywhere, for reasons that have nothing to do with counting technology. The shift to mail voting mechanically delays tallies (mail is counted more slowly than in-person ballots in every county measured), statewide postmark-deadline extensions push more ballots past election night, and small-county election offices are strained. The counties that never adopted any counting technology show that raw decay in its purest form: over the study window San Francisco's election-night share fell about 15 points, Del Norte's about 18, Lake's about 30.

Against that baseline, the counties that adopted **Voter's Choice Act vote centers** (with their bundled electronic pollbooks, live check-in, and central mail-processing operations) held up markedly better than their own composition would predict. Comparing every county's actual election-night change to the change its own vote-by-mail shift predicts, at HEAD `9bff066`:

| group | n | mean actual night-share change (pp) | mean composition-expected change (pp) | mean residual (pp) |
|---|---:|---:|---:|---:|
| VCA-bundle adopters | 11 | -8.23 | -4.16 | **-4.07** |
| no-tech controls | 4 | -16.98 | -3.40 | **-13.58** |
| **adopter advantage** | | | | **+9.51** |

Both groups moved voters to mail; the adopters moved *more* mail on average. Both faced the same postmark laws and the same decade. The no-tech counties' election-night counts fell far beyond what their mail shift explains (residual -13.58); the vote-center counties absorbed their larger mail shifts almost completely (residual -4.07). The gap, **+9.51 points**, is the adopters beating their own composition counterfactual relative to the controls. A second, fully independent construction (control-netted matched-cells difference-in-differences, then composition-adjusted) agrees in direction at **+5.8 to +9.1 points** (companion doc, frozen at its own panel). This is the positive finding, and it is robust to how the composition drag is credited.

Two honest limits sit on top of it. First, the formal test still cannot certify the effect against zero: the headline matched-cells difference-in-differences is **+4.83 pp with a 95% jackknife interval of (-6.43, +16.09)**, which includes zero, because California's never-adopter control pool is four small rural counties plus San Francisco and they disagree with each other enough to set a wide noise floor (the randomization placebo, below). Second, this data cannot separate the e-pollbook from the vote-center bundle it arrived in, because 11 of the 13 treated California counties adopted the two in the same year. For the policy question actually on the table, "adopt the vote-center model or not," that second limit does not matter, and this document explains why.

The recommendation: **report the +10-point vote-center advantage as suggestive, not certified**, name the per-county heroes and laggards, and pursue the out-of-state expansion that is now the identification play for a certified causal number.

## 1. The statewide decay is mostly composition, and the rule is era-qualified

The single largest driver of falling election-night shares over 2012-2024 is not any county's counting technology. It is the statewide move toward mail voting, layered on postmark-law changes that push mail past election night. San Francisco is the clean measuring stick for this, because it never adopted e-pollbooks, ASV, or vote centers, processes 100 percent of its mail centrally, and publishes a per-release mail / election-day split for every count. The companion document (`docs/analysis/2026-07-10-vbm-composition-curve.md`, committed) reads the mechanism directly off that ledger through the identity `night_share = m*S_mail + (1-m)*S_precinct`, where `m` is the final mail share. Across 18 SF elections, mail is counted to roughly 0.53 by election night and precinct ballots to roughly 0.80, so shifting composition toward mail lowers the night share by the gap between those two rates.

The calibrated headline, **era-qualified because that gap has narrowed over time**:

> For every 10 percentage points of vote-by-mail share, the election-night tally share drops by about **2.65 points** overall (median), resolving to about **3.1 points before 2022** and about **1.7 points from 2022 on**.

The narrowing (from a roughly 0.33 channel gap in the 2016-2020 era to about 0.17 from 2022) is driven by statewide postmark-deadline extensions and the growth of early-returned universal mail, both unrelated to any county's counting technology. Present-day work should use the 2022+ kernel; a pre-2022 kernel applied to a post-2022 comparison overstates the composition penalty. These are the committed era kernels used throughout this document (0.315 pre-2022, 0.172 from 2022 on, per unit of mail share).

The point of establishing this first is that the raw decline in any county's election-night share is *expected*, and most of it is composition. The interesting quantity is not whether a county's night share fell (nearly all did) but whether it fell more or less than its own mail shift predicts. That residual is the subject of the next section.

## 2. VCA vote-center adopters beat their own composition counterfactual (the required cut)

This is the central positive result, recomputed at HEAD `9bff066` per the method in the ledger (`.superpowers/sdd/progress.md`, "MAINTAINER-PROMPTED counterfactual cut"): for each county, take its own actual election-night change over its pre/post window, subtract the change its own vote-by-mail shift predicts under the era-matched kernel, and compare the residual for the VCA-bundle adopters against the residual for the no-tech controls. Cells are matched to `data/research/county-vbm/county_vbm_share.csv` (228 rows, underscore-slug mapping) by `(county, year, general|primary)`. Treated pre/post windows key on adoption year; controls use a 2020 era-cut (the caveat that follows).

**Per-county residuals (actual minus composition-expected), at HEAD:**

| county | window cut | actual change (pp) | composition-expected (pp) | residual (pp) |
|---|---:|---:|---:|---:|
| San Diego | 2022 | +4.86 | -3.89 | **+8.76** |
| Fresno | 2020 | +1.66 | -4.49 | **+6.15** |
| Orange | 2020 | -2.24 | -3.73 | +1.49 |
| Santa Clara | 2020 | -2.09 | -2.65 | +0.57 |
| Nevada | 2014 | -4.27 | -3.27 | -1.00 |
| Los Angeles | 2020 | -8.48 | -6.68 | -1.79 |
| Riverside | 2022 | -11.42 | -3.04 | -8.38 |
| Madera | 2018 | -13.95 | -4.94 | -9.01 |
| San Mateo | 2018 | -17.58 | -5.57 | -12.00 |
| Napa | 2018 | -13.47 | -1.01 | -12.46 |
| Sacramento | 2018 | -23.61 | -6.58 | -17.03 |
| **adopters (mean, n=11)** | | **-8.23** | **-4.16** | **-4.07** (sd 8.25) |
| Mendocino (control) | 2020 | -4.37 | -1.76 | -2.61 |
| San Francisco (control) | 2020 | -15.48 | -4.39 | -11.09 |
| Del Norte (control) | 2020 | -17.83 | -3.93 | -13.90 |
| Lake (control) | 2020 | -30.24 | -3.52 | -26.72 |
| **controls (mean, n=4)** | | **-16.98** | **-3.40** | **-13.58** (sd 9.99) |
| **adopter advantage** | | | | **+9.51** |

The reading: the no-tech controls' election-night counts collapsed by about 17 points on average while their mail shift alone predicts only about 3, leaving a residual of -13.58 that mail composition cannot explain. The VCA-bundle adopters absorbed their (larger) mail shifts down to a residual of -4.07, close to on-script. The difference, **+9.51 points**, is the vote-center advantage measured against each county's own composition counterfactual rather than against a raw level.

**Three caveats travel with this cut, and all three are the same ones the maintainer flagged:**

1. **Only four contributing controls, and Lake dominates.** The control benchmark is a mean over San Francisco, Del Norte, Lake, and Mendocino (Tehama has no pre-2020 point, so it drops under the 2020 cut; Colusa is a documented null). Lake's residual alone is -26.72, roughly twice the group mean; its understaffed-office collapse pulls the control benchmark down and therefore inflates the advantage. This is a control-group artifact, not an adopter effect, and it is large.
2. **The kernel is SF-transferred.** SF's `S_mail` is a central-count rate. A vote-center county's late same-day drop-offs make its true `S_mail` lower and more back-loaded, so the SF kernel understates the composition penalty for exactly the vote-center counties under study, which biases the residual advantage *upward*. The adjusted advantage is if anything generous to the technology.
3. **The 2020 era-cut for controls is a modeling choice.** Controls have no adoption year, so their pre/post split is set at 2020 to bracket the same window the treated post-periods mostly occupy. A different cut moves the control benchmark.

The independent construction agrees in direction. The companion document's composition-adjusted difference-in-differences (control-netted, then netted again for the mechanical mail drag, frozen at its own generals-only panel) lands the adopter residual at **+5.79 pp net to +9.08 pp naive**. Two different constructions (residual-vs-control here, composition-adjusted DiD there) both put the vote-center advantage near +6 to +9 points. That agreement is the strongest positive signal in the dataset.

## 3. The counties behind the average: heroes and laggards

The +9.51-point group average hides a wide spread, and the spread is the story.

**San Diego is the standout hero.** Its election-night share actually *rose* about 5 points while its mail share climbed 23, for a residual of **+8.76** against its own composition counterfactual, the largest in the panel. Its matched-cells difference-in-differences effect is **+20.70 pp**, more than double the next county. It is also the cleanest of the VCA-timing confound (2022 adoption, after the statewide all-mail transition had already run), which is part of why it looks so strong.

**Fresno (+6.15), Orange (+1.49), and Santa Clara (+0.57)** ran on or ahead of script through mail shifts of 15 to 26 points: they moved large volumes of voters to mail and still held their election-night share near what composition predicts.

**Sacramento is the cautionary tale in the other direction.** Its residual is **-17.03**: it adopted vote centers in 2018 and its election-night share still fell 24 points, far more than its mail shift explains. Adopting the vote-center model did not rescue a county with deeper operational problems. Napa (-12.46), San Mateo (-12.00), and Madera (-9.01), the rest of the 2018 cohort, tell the same story more quietly: early adopters at the leading edge of the Voter's Choice Act transition show negative residuals, consistent with the statewide mail shock hitting them before their operations matured.

**Riverside (-8.38)** is a newly identified county (Section 6) whose 2022 rollout election is its only post point so far; its residual is negative and provisional. **Placer**, a late 2024 adopter whose mail share *fell* when vote centers opened yet still reported less on election night, is a genuine contrarian data point; it is not yet identified in the committed panel (its recovered 2024-03 primary sits in the pending corpus) and is worth watching in November 2026.

The heroes-and-laggards split is exactly why the group average, though positive and sizable, cannot yet be certified: the counties disagree by nearly 26 points (San Diego +8.76 to Sacramento -17.03 on the residual, or +20.70 to -8.71 on the raw difference-in-differences).

## 4. How confident to be: suggestive, not yet certified

The honest status is **suggestive, not certified**, and the reason is structural, not a research-effort gap.

**The formal interval includes zero.** The headline matched-cells difference-in-differences (mechanism `any`, which resolves to the e-pollbook cut in every identified county) is **+4.83 pp**, jackknife SE **5.75**, 95% CI **(-6.43, +16.09)**, over 11 identified treated counties and 5 contributing controls (18 jackknife replicates). The interval comfortably includes zero. This is the primary formal statement, and it is a "cannot certify," not a "no effect."

**The randomization placebo shows why.** Take the control counties only, promote a subset to fake adopters at a fake adoption year, and re-run the estimator; never-adopters share the same statewide year shocks, so a working design must return approximately zero. There is no single canonical way to split the controls, so `placebo_distribution()` enumerates every valid split (28 of them at fake year 2018) and reports the whole distribution. At HEAD it spans **-18.41 to +14.86**, mean **-1.52**, sd **9.75**, and **20 of 28 splits (71%)** produce a spurious effect at least as extreme as the real +4.83 headline. A design whose noise floor, built from counties that adopted nothing, routinely matches or exceeds its own treatment estimate has not yet measured that treatment. One asymmetry makes this conservative rather than alarmist: the fake-adopter groups are small (1 to 4 controls) versus the real estimate's 11 treated counties, so this null is a deliberately wide floor. The point estimate still sits inside its bulk.

**Why California cannot certify it.** The never-adopter pool is exhausted as a census result, not a digging gap: exactly seven California counties never adopted e-pollbooks or ASV through 2024 (Colusa, Del Norte, Lake, Mendocino, Plumas, San Francisco, Tehama), six already in the panel, and the seventh (Plumas) is another idiosyncratic small rural series of the kind already driving the placebo. There is no California control left to add that would stabilize the design. The `--placebo` methodology itself was corrected during the campaign, credited to the maintainer: an earlier draft quoted one arbitrary split as "the single most important number in this document"; a different split of the same controls gives the opposite sign, so the full distribution replaced the single draw (`.superpowers/sdd/placebo-fix-report.md`, commit `90ead96`). The conclusion did not change, but the earlier presentation understated the noise floor.

## 5. What this data cannot answer, and why that is fine for the policy question

Whether the e-pollbooks *specifically*, or the signature-verification machines specifically, drive the advantage is unanswerable in California, and that is acceptable for the question actually on the table.

The adoption census (`data/research/county-tech/ca_adoption_census.json`) records `epollbook_year`, `asv_year`, and `vca_year` independently for every treated county. **Eleven of the thirteen adopted e-pollbooks in the exact year they became VCA vote-center counties** (`epb_year == vca_year`), so their e-pollbook cut and their vote-center cut select the identical adoption year, county for county. In the panel the two are observationally identical, not merely correlated. The two exceptions prove the rule rather than breaking it:

| county | epb year | vca year | asv year | status |
|---|---|---|---|---|
| Fresno, Los Angeles | 2020 | 2020 | 2020 / 2020 | bundled |
| Orange, Santa Clara | 2020 | 2020 | n/a | bundled |
| Madera, Napa, Sacramento, San Mateo | 2018 | 2018 | n/a | bundled |
| Riverside | 2022 | 2022 | 2025 | bundled |
| San Diego | 2022 | 2022 | 2024 | bundled |
| Placer | 2024 | 2024 | n/a | bundled |
| **Nevada** | **2014** | **2018** | **2016** | **EPB precedes VCA (see Section 6)** |
| **San Bernardino** | **2020** | **none** | **2025** | **standalone EPB, never did VCA** |

Because the `vca_year` cut and the `epb_year` cut coincide for the 11 bundled counties, the estimator's `--mechanism vca` aggregate (**+4.33 pp**, CI **(-7.27, +15.93)**) differs from its `--mechanism epb` aggregate (**+4.83 pp**) by a small amount that is *entirely* Nevada: Nevada's per-county effect is +6.93 under the 2014 e-pollbook cut but +1.40 under the 2018 vote-center cut. San Bernardino, the one county that adopted e-pollbooks without ever converting to vote centers, is the only California county that could in principle isolate a standalone e-pollbook effect, and it cannot do so here: its entire pre-2020 election-night record is a documented null in both generals and primaries, so it drops out of every replicate. The standalone-versus-bundle contrast has no support in the California panel and will not acquire any from further California digging.

**Why this is fine.** The policy choice a county faces is "adopt the vote-center model, with its bundled pollbooks and central mail processing, or not." It is not "buy pollbooks a la carte." The bundle is the treatment because the bundle is the decision. Reporting a vote-center-bundle advantage is therefore the *more* useful claim for the article, not a diluted one. The a-la-carte decomposition matters only for a mechanistic paper, and answering it requires jurisdictions that adopted e-pollbooks without a simultaneous vote-center conversion, which is the argument for the out-of-state expansion in Section 10.

## 6. Methods and provenance behind the refreshed panel

Four things changed the panel since the superseded document, and each is load-bearing for a number above.

**The estimator became cell-matched.** Adding primaries as a second election type broke a hidden assumption: matching a control's contribution to a treated county by bare calendar year would blend a control's primary row into a comparison the treated county never had, because primaries run structurally below generals. The fix keys matching on `(year, type)` cells; a control contributes only the cells the treated county actually has, and only if it has at least one matching pre cell and one matching post cell (`_per_county_effects` in `scripts/research/estimate_tech_effect.py`). The change was built test-first: a synthetic panel recovered the injected effect exactly under cell-matching and returned a biased value under the old year-only matching (`.superpowers/sdd/primaries-plumbing-report.md`).

**The primaries expansion.** June and March statewide primaries entered as a second election type (2012, 2014, 2016, 2018, 2022, 2024-03; the March 2020 presidential primary is excluded alongside the November 2020 general as COVID all-mail outliers). At HEAD the committed panel carries **14 primary cells** (San Francisco's 6 own-data points plus 8 treated-county cells: Riverside 3, San Diego 4, Santa Clara 1). This is what made **Riverside identified** (its 2016 and 2018 primaries supply pre-adoption cells its generals lacked; per-county effect **-0.53 pp**) and tempered San Diego's formerly extreme generals-only effect down to **+20.70 pp**. The remaining recovered primary cells (roughly 46 across the wave-3 dossiers) are preserved in `docs/research/pending-integration-2026-07-10/` and integrate after this document.

**Nevada's reclassification.** Nevada is the case study for why the census carries an adjudication layer. Its primaries scout surfaced a signed 2016 ES&S MBV-1000 contract with signature-recognition software and a County Clerk statement describing countywide e-pollbooks in the 2014 cycle, both predating the previously committed 2018 record. The adjudication (`.superpowers/sdd/progress.md`) revised **ASV to 2016** (with a live-use caveat, since a signed contract is procurement, not proof of election-day use) and **split-keyed the e-pollbook record to 2014**, retaining 2018 as the vote-center conversion. This is committed at HEAD `9bff066`. The effect on the numbers: Nevada now carries an EPB-before-VCA stagger, which is the sole source of the epb-versus-vca aggregate gap in Section 5, and its per-county effect reads +6.93 (epb, 2014 cut), +1.40 (vca, 2018 cut), or +9.00 (asv, 2016 cut) depending on the mechanism. Two judgment calls are flagged for the maintainer: the 2014-keying modeling choice and the ASV live-use caveat.

**The Secretary of State status-page vein.** The primaries sweep surfaced a systematic source: the CA Secretary of State election-night status page (recoverable via Wayback) publishes a per-county night-count table for every statewide election. A sweep graded **228 cells**, produced **73 brand-new fills** for cells individual county scouts had nulled, independently **cross-checked 49** already-committed values from a second source, and **corrected 3** of them (Napa 2014-11 to 50.34 percent, Del Norte 2016-11 to 86.31 percent, Riverside 2024-11 to 57.11 percent and thereby comparable). An independent source that reproduces roughly fifty committed numbers and corrects three is the strongest provenance check this dataset has received. The bulk of the 73 fills is in the pending apply-list, integrating after this document.

## 7. The binding constraint is the number of treated counties

The realized jackknife MDE at the current panel is **16.09 pp** (mechanism `any`, 2.8 times the SE), still several times the point estimate. The primaries expansion improved it (from about 20 at the generals-only panel) but did not fix the underlying constraint, and the reason re-ranks the follow-ons.

Control noise is no longer binding; between-county heterogeneity among the treated counties is. The standard deviation of the 11 treated counties' individual effects is **10.24 pp** (the roughly 29-point range from San Diego +20.70 to Madera -8.71). The MDE has a floor of about 2.8 times that heterogeneity divided by the square root of the treated count, roughly **8.6 pp**, even with infinite perfect controls. The scenario projector confirms controls cannot get below it: (6 controls, 6 elections) gives 15.14, (10, 8) gives 12.01, (20, 8) gives 10.47, and even (100, 10) reaches only 8.96. Detecting an effect of the composition-adjusted headline's own size at conventional confidence requires on the order of tens of treated counties, not the 11 in hand. The follow-ons that matter are the ones that add treated counties, ideally counties whose adoption is not VCA-bundled, which also shrinks the heterogeneity by removing the confound.

## 8. Verification status

The numbers inherit the verification status of the underlying election-night rows, tracked in `data/research/election-night/HUMAN_VERIFY.md`, whose plateau judgments are the maintainer's to make (the machine pass can confirm a number appears at its cited URL and that finals match the Statement of Vote, but cannot confirm a cited report is the *last* one posted on election night). The maintainer's incorporated verdicts this campaign:

- **Lake ASV = not adopted** (confirmed 2026-07-10). Lake's control status stands. This was the single most consequential open item: Lake's no-tech collapse (residual -26.72 in Section 2) is one of the largest single influences on the control baseline, and had Lake been a treated ASV adopter it would have lowered the adopter advantage further.
- **Mendocino 2012 general restored as a labeled approximation** (51.00 percent, secondary, plateau verdict PLAUSIBLE-approximation), adding a control pre-point.
- **Three hand-read confirmations:** Mendocino 2014 general, Mendocino 2024 general, Napa 2014 general.
- **Santa Clara 2012-06 primary:** ceiling-plus-scaling-note default in deadline mode rather than an upgraded sourced point.

Two plateau rows were refuted as plateaus during review and correctly excluded (Placer 2018-11 and Riverside 2024-11 both tracked the canvass, not election night). Outstanding judgment items the maintainer may still weigh: San Diego's 2024-03 ASV classification, the Nevada 2014-keying and ASV-live-use caveats, and the secondary-confidence rows enumerated in HUMAN_VERIFY.md.

## 9. Decision gate and follow-ons

The gate: if the interval excludes zero, report the effect; if it includes zero and the MDE exceeds the point estimate, recommend the follow-on that breaks the tie. We are in the second case. The `any`/epb interval (-6.43, +16.09) includes zero, the MDE (16.09) is several times the point estimate, and the placebo swallows the headline. **Do not report a certified headline counting-technology effect.** Do report the +10-point vote-center advantage as the best-supported reading, with its caveats. The follow-ons, re-ranked:

**First, and now the identification play: out-of-state jurisdictions** (Pennsylvania, New York, Wisconsin; leads in `data/research/county-tech/`). The primaries expansion did not break the VCA collinearity, because 11 of 13 California adopters are bundled by construction and the one standalone adopter (San Bernardino) has no recoverable pre-period. Out-of-state counties adopted e-pollbooks without California's all-mail vote-center transition, so they are the only way to separate a standalone e-pollbook effect from the bundle, and they add larger, more comparable treated counties that attack the heterogeneity floor from Section 7. This is the one follow-on that addresses both of the design's deepest problems. (The cheap in-state check, verifying Kern and Kings as candidate non-VCA e-pollbook counties, was dropped in deadline mode and is worth revisiting before committing to out-of-state archive work.)

**Second: November 2026, mechanically and at no research cost.** It adds a fresh post-2024 point for every panel county and a second post-adoption point for the newly identified Riverside and (once its primaries land) Placer. Calendar-gated to the Statement of Vote around December 2026; no new playbook. It will not resolve the bundle confound or the control exhaustion, but it is the cheapest increment to n.

**Third: a canvass-speed alternative outcome** (days-to-threshold rather than the election-night plateau share), which may carry a cleaner signal than a snapshot sensitive to poll-close timing. It ranks third because it is a new metric needing its own validation and does not by itself add treated counties.

**Credential-bound items for the human** (browser-armed recovery reached them but they sit behind NewsBank / SFPL ezproxy): the Sacramento Bee 2014-06 primary and the Sacramento 2016-11 and Fresno 2018-11 election-night plateaus, all McClatchy/NewsBank-walled. These are the remaining recoverable gaps the automated routes exhausted.

---

## Appendix A: Reproducing every figure

All figures were computed against the committed HEAD panel, isolated from the working tree so a concurrent data commit cannot perturb them:

```bash
git rev-parse HEAD          # 9bff066680f087bd72fadfd7d20d2c05b5780731
git show 9bff066:packages/data/county_night.json > county_night_HEAD.json

# Headline battery + placebo (Sections 4, 5)
python3 scripts/research/estimate_tech_effect.py --path county_night_HEAD.json --mechanism any --placebo --json
python3 scripts/research/estimate_tech_effect.py --path county_night_HEAD.json --mechanism epb --json
python3 scripts/research/estimate_tech_effect.py --path county_night_HEAD.json --mechanism asv --json
python3 scripts/research/estimate_tech_effect.py --path county_night_HEAD.json --mechanism vca --json

# Scenario / MDE projections (Section 7)
python3 scripts/research/estimate_tech_effect.py --path county_night_HEAD.json --mechanism any --scenario 6 6 --json
python3 scripts/research/estimate_tech_effect.py --path county_night_HEAD.json --mechanism any --scenario 10 8 --json
python3 scripts/research/estimate_tech_effect.py --path county_night_HEAD.json --mechanism any --scenario 100 10 --json

# Counterfactual residual cut, treated vs control (Section 2)
#   own actual change vs composition-expected change, era kernels 0.315/0.172,
#   cells matched to data/research/county-vbm/county_vbm_share.csv
#   (script: scratchpad/counterfactual_cut.py; method per progress.md ledger)
```

**Readouts at HEAD `9bff066`:**

- **any / epb:** effect +4.83, SE 5.75, CI (-6.43, +16.09), MDE 16.09, n_treated 11, n_controls 5.
- **vca:** effect +4.33, SE 5.92, CI (-7.27, +15.93); differs from epb solely through Nevada (per-county +1.40 at the 2018 vote-center cut vs +6.93 at the 2014 e-pollbook cut).
- **asv:** effect +12.33, SE 5.38, CI (+1.79, +22.87), n_treated 4. A tight interval around a confounded estimand (two of its four counties adopted EPB and ASV the same year, a third spends most of its ASV pre-window pre-EPB, and the Nevada timing shifted with the reclassification); not evidence of a standalone ASV effect.
- **placebo (any, fake 2018):** 28 valid splits, mean -1.52, sd 9.75, min -18.41, max +14.86; 20 of 28 (71%) at least as extreme as the +4.83 headline.
- **per-county (any):** San Diego +20.70, Santa Clara +14.23, Orange +14.07, Fresno +13.87, Los Angeles +7.84, Nevada +6.93, Riverside -0.53, Napa -1.51, San Mateo -5.61, Sacramento -8.11, Madera -8.71. Treated-effect sd 10.24, range 29.41.
- **counterfactual cut:** adopters (n=11) mean residual -4.07 (sd 8.25); controls (n=4) mean residual -13.58 (sd 9.99); advantage +9.51. Companion composition-adjusted DiD (frozen panel) agrees at +5.79 net to +9.08 naive.

## Appendix B: what will move with the pending integration

Integration of `docs/research/pending-integration-2026-07-10/` (roughly 46 further primary cells, the 87-cell Secretary of State apply-list, and any wave-3 stragglers) continues after this document. It is expected to refine decimals, not direction: the counterfactual advantage, the placebo swallowing the headline, and the between-county heterogeneity floor are all robust to the panel roughly doubling once already, and the pending remainder is smaller than that. A successor note will re-pin these figures at the post-integration commit if any headline moves by more than its rounding.
