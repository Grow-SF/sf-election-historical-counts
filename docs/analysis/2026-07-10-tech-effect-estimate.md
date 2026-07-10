> **2026-07-10: superseded by [2026-07-10-vca-bundle-tech-effect.md](2026-07-10-vca-bundle-tech-effect.md)** (framing rewrite around the VCA-bundle finding and composition decomposition); the numbers below reflect the pre-primaries panel.

# Does counting technology speed up the election-night count? A first defensible estimate

**Date:** 2026-07-10
**Panel pinned at:** commit `51cdc3f` (`packages/data/county_night.json`)
**Estimator:** `scripts/research/estimate_tech_effect.py` (matched-years difference-in-differences, jackknife inference)

Every number in this document was recomputed by the author against the pinned panel. The exact commands are in Appendix A. Where an earlier robustness readout is cited, its figure is marked as such and the governing figure is the one recomputed here.

## Executive summary

The expanded county panel lets us ask, for the first time with a real control group, whether adopting electronic pollbooks (EPB) or automated signature verification (ASV) raises the share of a county's vote that is counted by election night. The matched-years estimate of the e-pollbook effect is **+4.76 percentage points, with a 95% jackknife confidence interval of (-9.32, +18.84)**. The interval comfortably includes zero.

The single most important number in this document is not that point estimate. It is the placebo. When we assign a fake adoption year to counties that never adopted any counting technology, and enumerate every possible way of splitting the five contributing controls into fake adopters versus fake controls (28 valid splits at fake year 2018, not one arbitrary split), the resulting null distribution spans **-20.72 to +17.29 points**, centered near zero (mean -1.49, sd 11.13), and **20 of the 28 splits (71%) produce spurious "effects" at least as extreme as the real +4.76 headline**. A design whose noise floor routinely matches or exceeds the size of the real treatment effect cannot yet claim to have measured that treatment.

The honest reading is therefore conditional throughout: the data are consistent with a positive e-pollbook effect on the order of a few points, but that signal is **not yet distinguishable from control-assignment noise**. This is a "no-go" on reporting a headline effect, and a "go" on the specific follow-on data collection that would break the tie. The rest of this document establishes exactly why, and what each proposed next step would buy.

## 1. Panel inventory

The campaign grew the cross-county election-night dataset from its starting point of **14 jurisdictions with a single control county** (San Francisco) to **19 jurisdictions with six control counties**, and recovered three pre-adoption cells for Santa Clara (2014, 2016, 2018) that extend a treated county's pre-period.

The nineteen jurisdictions break down as follows.

**Ten treated adopter counties** contribute an identified effect under the e-pollbook / "any" mechanism, because each has at least one comparable election-night point before its adoption year and at least one at or after it: Fresno, Los Angeles, Madera, Napa, Nevada, Orange, Sacramento, San Diego, San Mateo, and Santa Clara.

**Three treated counties are in the panel but not yet identified** under the primary mechanism, because they lack either a pre- or a post-adoption comparable point: Placer (adopted 2024, no post-adoption general yet), Riverside (its only comparable point, 2022, is itself the adoption year), and San Bernardino (adopted 2020, only a 2024 point survives). These three contribute zero to the headline and drop out of every leave-one-out replicate; recovering their missing cells is the highest-value gap-fill remaining, and the November 2026 general supplies Placer's first post-period point mechanically.

**Six control jurisdictions** carry the never-adopter side. Five contribute comparable rows: San Francisco (the pre-existing control, 6 points), Lake (6), Del Norte (5), Mendocino (4), and Tehama (2, in 2022 and 2024 only). The sixth, Colusa, is present and flagged as a control but contributes **zero comparable points**: its entire 2012-2024 series is documented null after the archive routes were exhausted. Colusa is retained in the file for provenance and is correctly excluded from every computation here (`n_controls` resolves to 5, not 6, because the loader drops null rows).

The panel excludes 2020 everywhere (runbook convention: the pandemic all-mail cycle is not comparable), and excludes any point flagged `comparable: false`. Nevada's 2024 point and Riverside's 2024 point are such ceilings and do not enter the comparisons.

A note on why five contributing controls behave almost exactly like four: Tehama's two points (2022, 2024) fall inside no treated county's e-pollbook pre/post window in a way that lets Tehama enter that county's control-change term, because the matched-years design requires a control to be observed in at least one pre-year and one post-year of the treated county in question. As a result the "any"/EPB headline at this five-control panel is numerically identical to the prior four-control readout (+4.76). Tehama does move the ASV cut very slightly, through San Diego alone, because San Diego's ASV pre-window (2018, 2022) and post-window (2024) happen to straddle Tehama's two observed years. This is worth stating plainly: the last control we added changed the primary estimate by nothing, which is itself a data point about how quickly the never-adopter pool's marginal value has fallen.

## 2. Headline estimates by mechanism

The estimator takes `--mechanism any|epb|asv`. The results at the pinned panel:

| Mechanism | Effect (pp) | Jackknife SE | 95% CI | MDE (2.8 SE) | n treated | n controls |
|---|---:|---:|---:|---:|---:|---:|
| any | +4.76 | 7.18 | (-9.32, +18.84) | 20.12 | 10 | 5 |
| epb | +4.76 | 7.18 | (-9.32, +18.84) | 20.12 | 10 | 5 |
| asv | +15.58 | 6.64 | (+2.58, +28.59) | 18.58 | 4 | 5 |

Inference is a leave-one-county-out jackknife over all 18 counties that carry data (10 treated plus 5 controls, plus the 3 unidentified treated counties which contribute a null replicate and are dropped), yielding 18 replicates.

Two facts about this table govern how it must be read.

First, **"any" and "epb" are the same number, county for county, not merely in aggregate.** The "any" mechanism resolves each county's adoption year as `min(epb_year, asv_year)`, and in every treated county that survives the pre/post filter the e-pollbook year is the earlier (or the only) one. "Any" therefore never actually picks up an ASV-led transition; it collapses onto the e-pollbook cut every time. The two rows are reported separately only for transparency. There is one effective non-ASV estimate here, +4.76, and it is an e-pollbook estimate.

Second, **the ASV cut's interval excludes zero, but that is not evidence of an ASV effect,** for reasons developed in Section 5. The short version: two of its four identifying counties adopted EPB and ASV in the same year, so their "ASV effect" is arithmetically identical to their EPB effect, and a third spends most of its ASV pre-window already under EPB. The ASV interval is a tight confidence interval around a badly confounded quantity. A narrow interval around the wrong estimand is not more trustworthy than a wide one.

## 3. The placebo, reported prominently

The placebo test is the cheapest and most damning credibility check available, and it is the reason this document's central claim is conditional. The procedure: take the control counties only, promote a subset of them to "fake adopters" at a fake adoption year, and re-run the estimator. Never-adopter counties share the same statewide year shocks as the counties left as controls, so a well-behaved design must return approximately zero.

**This section was corrected on 2026-07-10 (see the note at the end); it now reports the full randomization distribution rather than a single split.** With five contributing controls (Del Norte, Lake, Mendocino, San Francisco, Tehama), there is no single canonical way to divide them into "fake adopters" and "fake controls." `placebo_distribution()` (`scripts/research/estimate_tech_effect.py`) enumerates every nonempty proper subset of the five controls as a candidate fake-adopter split, 30 in total, and re-runs the estimator on each. Two subsets ({Tehama} alone, and the all-four-others subset) produce no identified fake-adopter effect because Tehama has no pre-2018 point, leaving **28 valid splits**.

At a fake adoption year of 2018, those 28 splits produce effects ranging from **-20.72 to +17.29 points**, with mean **-1.49** and standard deviation **11.13**. The distribution is reasonably centered near zero, as a well-behaved design should be, but it is wide: **20 of the 28 splits (71%) produce a spurious "effect" at least as extreme in magnitude as the real +4.76 headline.** The real effect sits well inside this null distribution, not out at a tail the way a genuine, well-identified treatment effect should. The single most spurious split (Del Norte + Lake + San Francisco as fake adopters, at -20.72) is driven by the same idiosyncratic small-county volatility documented in Section 7 (Lake's collapse, Mendocino's single-cycle jump); the point is not any one split's story but that the *spread* across all of them dwarfs the headline.

The distribution is not a one-off artifact of the 2018 fake year. At fake year 2016 it spans -13.14 to +11.95 (mean -0.73, sd 7.49, 16/28 = 57% as extreme as the real effect); at fake year 2022 it spans -19.73 to +19.40 (mean -0.63, sd 13.31, 18/28 = 64% as extreme). Whichever fake year is picked, roughly six in ten (or more) of the possible control splits produce spurious "effects" comparable to or larger than the real +4.76 headline.

One honest asymmetry works against this comparison, and it should widen rather than narrow the reader's skepticism: **the placebo can only be built from the five control counties, so its fake-adopter groups are necessarily small (1 to 4 counties) versus the real estimate's ten treated counties.** A smaller group is noisier by construction (the between-county heterogeneity documented in Section 8 does not average out as much), so this randomization distribution is a *conservative, wide* noise floor, not an apples-to-apples one: it likely overstates the noise on an n=10 estimate. That the real +4.76 still lands inside the bulk of this deliberately-generous-to-the-real-effect distribution, rather than clearly outside it, is correspondingly more damning, not less: even a noise floor built to be wider than the real estimate's own sampling variation swallows the headline.

The conclusion is unavoidable and must be stated first, not buried: **at this panel the measured e-pollbook effect cannot be reliably distinguished from the effect the same estimator produces from counties that were never treated at all.** We cannot yet distinguish the e-pollbook effect from the noise floor set by the control group's composition: San Francisco plus a handful of small rural never-adopter counties. The jackknife confidence interval in Section 2 (-9.32, +18.84), computed over all 18 counties that carry data, remains the primary formal inference; this randomization spread is corroborating evidence, not a replacement for it, and both point the same direction. Every "effect" in this document is written conditionally for that reason.

**CORRECTION (2026-07-10):** an earlier version of this section quoted a single arbitrary-split placebo of +10.23 (promoting every second control county, sorted alphabetically, at fake year 2018) as "the single most important number in this document," and compared the headline against that one draw. That single split was one of 28 valid ways to split the five controls into fake adopters and fake controls; a different split (Del Norte + Lake + San Francisco as fake adopters) gives -14.32, and the full distribution of all 28 splits at fake year 2018 spans -20.72 to +17.29 (mean -1.49, sd 11.13). The section above now reports that full distribution. The inference conclusion is unchanged (most placebo splits are at least as extreme as the real effect, 20 of 28 at fake year 2018; the jackknife CI already included zero), but the earlier presentation understated the true noise floor by quoting one point instead of the distribution it was drawn from. Credit to the maintainer for catching this.

## 4. Per-county effects

The headline is a simple mean over the ten identified treated counties' individual matched-years effects. Those effects are not a tight cluster around +4.76; they range across 37 points.

| County | Adoption (epb / asv) | Matched-years effect (pp) |
|---|---|---:|
| San Diego | 2022 / 2024 | **+28.20** |
| Santa Clara | 2020 / n/a | +13.35 |
| Orange | 2020 / n/a | +13.20 |
| Fresno | 2020 / 2020 | +13.12 |
| Los Angeles | 2020 / 2020 | +6.97 |
| Nevada | 2018 / 2022 | -0.03 |
| Napa | 2018 / n/a | -1.88 |
| San Mateo | 2018 / n/a | -7.05 |
| Sacramento | 2018 / n/a | -8.79 |
| Madera | 2018 / n/a | -9.46 |
| **Mean** | | **+4.76** |

**San Diego is a positive outlier and must be named as one.** Its +28.20 is more than double the next-largest county effect and roughly six times the panel mean. Its adoption is also the cleanest in the panel of the VCA confound (2022, after the Voter's Choice Act all-mail transition had already run through the other counties), which is exactly why the "2022+ cohort" in Section 6 looks so strong, and exactly why that strength is illusory: the 2022+ cohort is San Diego and nothing else. Dropping San Diego alone pulls the headline from +4.76 down to +2.16, the largest single-county swing among the treated counties (leave-one-out, Appendix B).

**The lower half of the table is the more sobering half.** The entire 2018 e-pollbook cohort (Madera, Napa, Nevada, Sacramento, San Mateo) sits at or below zero. These five counties' election-night share grew *more slowly* than the never-adopter control baseline over their own pre/post windows. That is not what an effective speed-up technology looks like. It is developed as a cohort finding in Section 6, but it is visible here as a fact about individual counties: five of the ten identified adopters have a negative estimated effect, and the positive mean is carried by San Diego plus the four 2020-cohort counties.

**Lake's no-tech collapse belongs in this discussion even though Lake is a control, not a treated county.** Lake's election-night share falls from 63.0% in 2018 to 38.5% in 2022 to 29.3% in 2024, a 34-point decline over two cycles with no counting-technology adoption on record (local reporting attributes it to an understaffed elections office). Lake is the most volatile series in the control group, and because the control baseline is a mean over only five counties, Lake's collapse materially lowers that baseline in the post-period and thereby inflates every treated county's apparent gain. This is not a treated-county effect; it is a control-group artifact, and it is a large one. It is developed quantitatively in Section 7.

## 5. Mechanism: why the ASV cut cannot be read as an ASV effect

The ASV cut returns +15.58 with an interval that excludes zero, and it is tempting to read that as "ASV is the real driver." The panel does not support that reading. The four counties that identify the ASV effect are:

| County | epb year | asv year | ASV pre-window | ASV effect | epb effect (same county) |
|---|---|---|---|---:|---:|
| Fresno | 2020 | 2020 | 2016 | +13.12 | +13.12 (identical) |
| Los Angeles | 2020 | 2020 | 2012-2018 | +6.97 | +6.97 (identical) |
| Nevada | 2018 | 2022 | 2012-2018 | +16.93 | -0.03 |
| San Diego | 2022 | 2024 | 2018, 2022 | +25.30 | +28.20 |

Fresno and Los Angeles adopted e-pollbooks and ASV in the **same year (2020)**. There is no information anywhere in this panel that could separate "the ASV effect" from "the EPB effect" for these two counties: their ASV per-county effect is bit-for-bit identical to their EPB per-county effect. They are pure EPB-plus-ASV bundle effects, not ASV increments over an EPB baseline.

Nevada is the county that most tempts an ASV story, because its ASV effect (+16.93) diverges sharply from its EPB effect (-0.03). But Nevada adopted EPB in 2018 and ASV in 2022, and its ASV "pre" window (2012, 2014, 2016, 2018) is **three-quarters pre-EPB.** The +16.93 is therefore an "EPB-plus-later-ASV versus mostly-nothing" contrast, not "ASV over an established EPB baseline." It cannot carry the ASV-specific interpretation.

San Diego, the one county with a genuine EPB-then-ASV stagger (2022 then 2024), comes closest to a clean ASV increment, but its ASV pre-window is just two points (2018, one of them pre-EPB; 2022, itself the EPB adoption year), and it is the same outlier county already flagged in Section 4.

The honest statement is: **none of the four ASV-identifying counties yields a clean, EPB-isolated ASV estimate,** the ASV headline is a bundle-plus-timing artifact, and its tight interval is a false comfort. What *could* eventually identify the two mechanisms separately is exactly the within-county staggered-adopter structure that Nevada, San Diego, and Riverside (EPB 2022, ASV 2025) begin to provide. With enough post-2024 data points on those staggered counties, and ideally more counties that adopt the two technologies years apart, the estimator's mechanism split becomes meaningful. It is not meaningful yet.

## 6. Cohort cuts and the VCA confound

Splitting the treated counties by adoption cohort is the clearest single diagnostic in this analysis, and it is unflattering.

| Cohort | Members (identified) | Effect (pp) | 95% CI | n treated |
|---|---|---:|---:|---:|
| 2018 adopters | Madera, Napa, Nevada, Sacramento, San Mateo | **-5.44** | (-17.14, +6.25) | 5 |
| 2020 adopters | Fresno, LA, Orange, Santa Clara (San Bernardino dropped) | +11.66 | (-1.90, +25.22) | 4 |
| 2022+ adopters | San Diego (Placer, Riverside dropped) | +28.20 | (+16.92, +39.49) | 1 |

The headline +4.76 is not a stable number hiding inside three consistent cohorts. It is an average over three cohorts that disagree violently, ranging from -5.44 to +28.20.

**The 2018 cohort's near-zero-to-negative effect is the most important cohort finding.** These five counties adopted e-pollbooks in 2018, right at the leading edge of California's Voter's Choice Act transition to universal vote-by-mail. Their post-period is precisely the window in which every California county, treated or not, was absorbing the VCA all-mail shift. The matched-years design differences that statewide shock out through the control group, and once it is differenced out, the 2018 adopters show *no* e-pollbook advantage: their point estimate is negative. Read carefully, the 2018 cohort says that whatever raised election-night shares in 2018-2022 was a statewide phenomenon (VCA, mail processing, certification-rule changes), not the pollbooks, because the never-adopter controls got the same lift.

The 2020 cohort is positive (+11.66) but its interval crosses zero, and it is also VCA-era. The 2022+ cohort's interval is the only one excluding zero, and it must be read for what it literally is: **a single county (San Diego) wearing a cohort label,** because the estimator correctly discards Placer and Riverside for lacking an identifying pre/post point. An n=1 cohort with a tight interval is not a cohort finding.

The synthesis across cohorts is that the cleanest-of-VCA cohort (2022+) looks strongest and the most-VCA-confounded cohort (2018) looks weakest, which is exactly the pattern you would see if a good part of the apparent "tech effect" were really the VCA transition leaking through imperfectly matched controls. That is a hypothesis this panel cannot resolve, because in California adoption timing and VCA timing are collinear by construction. Breaking that collinearity requires jurisdictions that adopted counting technology *without* a simultaneous all-mail transition, which is the central argument for the out-of-state expansion in Section 9.

## 7. Control heterogeneity and the exhausted never-adopter pool

The five contributing control series, year by year:

| Year | San Francisco | Lake | Del Norte | Mendocino | Tehama | spread | mean | sd |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 2012 | 71.4 | 70.2 | n/a | n/a | n/a | 1.2 | 70.8 | 0.9 |
| 2014 | 70.3 | 69.7 | 89.2 | 45.6 | n/a | 43.6 | 68.7 | 17.9 |
| 2016 | 66.1 | 53.8 | 83.3 | 31.1 | n/a | 52.2 | 58.6 | 22.0 |
| 2018 | 59.3 | 63.0 | 84.5 | 46.6 | n/a | 37.9 | 63.3 | 15.7 |
| 2022 | 51.0 | 38.5 | 74.7 | n/a | 57.0 | 36.2 | 55.3 | 15.1 |
| 2024 | 56.9 | 29.3 | 62.9 | 39.2 | 48.8 | 33.6 | 47.4 | 13.5 |

The controls are not a homogeneous bloc. In level they span 30 to 50 points in any given year (Del Norte plateaus in the 60s-to-80s, Mendocino in the 30s-to-40s), and in trend they diverge just as much: Lake collapses from 2018 onward, Mendocino spikes up in 2018, Del Norte declines moderately and steadily. The matched-years design differences each control within itself before averaging, so the relevant quantity is the spread of each control's own pre-to-post delta, not the level spread. Even on that measure, the controls disagree enough that swapping which controls you trust moves the headline by more than the headline's own size (Appendix B: dropping Mendocino moves it +4.69, dropping Lake moves it -3.91, against a headline of 4.76).

This heterogeneity is the mechanical source of the Section 3 placebo. The control group has exactly one large, stable comparator: San Francisco, whose series is the smooth decline in the table above. The other four contributing series are idiosyncratic small counties, and because SF is a single series among five, the small-county noise still dominates the mean control change, which ends up noisy on the same scale as the effect we are trying to measure.

**The uncomfortable structural fact is that California's never-adopter pool is exhausted.** The CA-58 adoption census (`data/research/county-tech/ca_adoption_census.json`) finds exactly **seven counties that never adopted EPB or ASV through November 2024**: Colusa, Del Norte, Lake, Mendocino, Plumas, San Francisco, and Tehama. Six of the seven are already in this panel as controls. The only one left on the table is Plumas, among the smallest and most rural counties in the state, whose recoverable election-night archive is thin and whose marginal contribution would be another idiosyncratic small-county series of the exact kind already driving the placebo. Every larger never-adopter has already been integrated. There is no California control county left to add that would materially stabilize this design. This is not a research-effort problem that more digging solves; it is a census result. The state has run out of clean controls.

## 8. Minimum detectable effect: now, and the floor

The plan's baseline projection was that a single control county caps the minimum detectable effect at roughly an 8-point floor, and that adding controls would drop that floor toward 5-6 points. The realized numbers are worse than that optimistic projection, for an instructive reason.

The realized jackknife MDE at the pinned five-control panel is **20.12 points** (2.8 times the standard error of 7.18). The scenario projector, which models hypothetical panels, gives 17.29 points at (6 controls, 6 elections), 15.94 at (8, 6), and 14.14 at (10, 8). Pushing controls to absurd levels, 100 controls at 10 elections, still only reaches 11.19.

The reason the MDE will not fall to the plan's 5-to-6-point target by adding controls is that **control noise is no longer the binding constraint; between-county heterogeneity among the treated counties is.** The standard deviation of the ten treated counties' individual effects is 12.30 points (that 37-point San-Diego-to-Madera range from Section 4). The MDE has a floor set by that heterogeneity divided by the square root of the number of treated counties: with 10 treated counties, that floor is about **10.9 points even with an infinite number of perfect controls.** No amount of control-side work gets the MDE below roughly 11 points. To detect an effect of the headline's own size (about 5 points) at conventional confidence, the arithmetic requires on the order of 50 treated counties, not 10.

This single fact reframes the entire decision gate. The binding constraint is **the number of treated counties and the spread of their effects, not the number of controls.** The follow-ons that matter are the ones that add treated counties (and ideally ones whose adoption is not VCA-confounded, which also shrinks the heterogeneity by removing a confound), not the ones that add more California controls, of which there are none left anyway.

## 9. Decision gate

The formal gate from the plan: if the confidence interval excludes zero, the measured effect is the finding and we propose chart and article updates; if the interval includes zero and the MDE exceeds the absolute point estimate, we recommend the named follow-on data collection with projected MDEs.

We are unambiguously in the second case. The any/EPB interval (-9.32, +18.84) includes zero; the MDE (20.12) is more than four times the absolute point estimate (4.76); and the placebo randomization distribution (-20.72 to +17.29, 71% of splits at least as extreme as the headline) shows the headline cannot be reliably separated from noise generated by counties that adopted nothing. **The recommendation is: do not report a headline tech effect, and pursue the follow-on data collection below.** They are ranked by what each one fixes, because Section 8 shows the constraints are specific and not interchangeable.

**First priority: out-of-state jurisdictions (Pennsylvania, New York, Wisconsin).** Leads already exist in `data/research/county-tech/` (`pennsylvania-knowink.json`, e-pollbooks from about 2016 in a staggered county-by-county rollout; `new-york-epb.json`, 2019; `wisconsin-badgerbooks.json`, 2018). This is the highest-value follow-on because it fixes **two** binding constraints at once. It breaks the VCA collinearity (Section 6): none of these states ran California's Voter's Choice Act all-mail transition, so a county that adopts e-pollbooks there does so without a simultaneous statewide mail shift, which is the one thing no California county can offer. And it adds treated counties with different adoption timing and, critically, larger and more comparable counties than the small rural never-adopters that make up the rest of California's exhausted control pool (San Francisco, its one large member, is already in the panel), which attacks the between-county-heterogeneity floor from Section 8. The cost is real (each state needs its own denominator and archive playbook), but this is the only follow-on that addresses the design's two deepest problems together. Projected MDE contribution: moving from 10 to roughly 18-20 treated counties would pull the heterogeneity floor from about 10.9 toward 8 points, and removing the VCA confound should shrink the heterogeneity term itself.

**Second priority: a June-primaries expansion.** Adding June primary election-night points roughly doubles the number of observations per county and adds identifying pre/post points for the three currently-unidentified treated counties (Placer, Riverside, San Bernardino). This directly fixes the **n problem**: more points per county tighten each county's own pre/post estimate and bring the three benched counties into the headline. It does not fix the VCA confound or the control heterogeneity, and it changes the metric's composition (primary turnout and mail mix differ from a general), so it ranks below the out-of-state work. Projected MDE contribution: the scenario projector's (10 controls, 8 elections) case, 14.14 points, approximates the primaries-doubled panel, a meaningful improvement over 20.12 but still above the effect size.

**Third priority: a canvass-speed alternative outcome.** Instead of the election-night plateau share, measure the number of days from election day to a fixed completion threshold, using CalVoter's 2022-onward week-after ballot-processing data plus Wayback recovery of earlier canvass states from the existing capture cache. This fixes **outcome directness**: counting speed is what the technology plausibly affects most directly, and a days-to-threshold outcome may carry a cleaner signal than the election-night snapshot, which is sensitive to poll-close timing and reporting-cadence idiosyncrasies. It ranks third because it is a new metric requiring its own validation rather than an extension of the existing one, and because it does not by itself add treated counties.

**What November 2026 adds mechanically, at no research cost.** The November 2026 general is Placer's first post-e-pollbook data point, converting Placer from an unidentified county into an identified one, and it adds a fresh post-2024 point for every county in the panel. It is calendar-gated (the Secretary of State's Statement of Vote publishes around December 2026) and requires no new playbook. It will not resolve the VCA confound or the control-exhaustion problem, but it is the cheapest available increment to n and should be collected for all panel counties as soon as it certifies.

## 10. Verification status

The numbers in this document inherit the verification status of the underlying election-night rows, which is tracked in `data/research/election-night/HUMAN_VERIFY.md`. Rows that are non-CONFIRMED, secondary-sourced, or that rested on a plateau judgment call are enumerated there with their claimed values and fail criteria for hand-reading.

Across the expansion, a consolidated judgment-call packet was compiled and **delivered to the maintainer**: seven judgment items spanning the nineteen jurisdictions. That packet was a session-scratch artifact; its durable in-repo trail is `data/research/election-night/HUMAN_VERIFY.md` plus the judgment items called out in the individual task reports (`.superpowers/sdd/task-*-report.md`). The single item whose failure would most move the numbers in this document is **Lake County's ASV classification.** Lake is currently classified as a never-adopter and therefore sits in the control group, and Section 7 shows Lake's no-tech collapse is one of the largest single influences on the control baseline. If Lake were in fact an ASV adopter, it would move from the control side to the treated side, the control baseline would rise in the post-period, and the headline e-pollbook effect would fall further. That one classification is load-bearing for the entire control group, and it is the top item flagged for human confirmation.

---

## Appendix A: Commands

All figures were computed against the panel pinned at commit `51cdc3f`:

```bash
git show 51cdc3f:packages/data/county_night.json > county_night_final.json

# Headline battery (Section 2, 3)
python3 scripts/research/estimate_tech_effect.py --path county_night_final.json --mechanism any --placebo --json
python3 scripts/research/estimate_tech_effect.py --path county_night_final.json --mechanism epb --json
python3 scripts/research/estimate_tech_effect.py --path county_night_final.json --mechanism asv --json

# Scenario / MDE projections (Section 8)
python3 scripts/research/estimate_tech_effect.py --path county_night_final.json --scenario 6 6 --json
python3 scripts/research/estimate_tech_effect.py --path county_night_final.json --scenario 10 8 --json
```

The Section 3 randomization distributions (the `--placebo` flag now reports the full distribution over every valid control split, not one arbitrary split; `placebo()` is a thin wrapper around `placebo_distribution()`), leave-one-out (Appendix B), cohort cuts (Section 6), control heterogeneity (Section 7), and the between-county-heterogeneity floor (Section 8) were computed by importing the estimator's own functions (`load_panel`, `estimate`, `jackknife`, `placebo_distribution`, `scenario`, `_per_county_effects`, `_by_slug`, `_adoption_year`) against `county_night_final.json`, not by reimplementing any of the estimation logic.

## Appendix B: Leave-one-out sensitivity (any mechanism)

Full "any" effect = +4.7635. Effect with each county dropped, sorted by absolute swing:

| County dropped | Effect with drop | Delta from full | Role |
|---|---:|---:|---|
| Mendocino | +9.45 | +4.69 | control |
| Lake | +0.86 | -3.91 | control |
| San Diego | +2.16 | -2.60 | treated |
| Madera | +6.34 | +1.58 | treated |
| Sacramento | +6.27 | +1.51 | treated |
| San Mateo | +6.08 | +1.31 | treated |
| Santa Clara | +3.81 | -0.95 | treated |
| Orange | +3.83 | -0.94 | treated |
| Fresno | +3.83 | -0.93 | treated |
| Del Norte | +4.00 | -0.76 | control |
| Napa | +5.50 | +0.74 | treated |
| Nevada | +5.30 | +0.53 | treated |
| Los Angeles | +4.52 | -0.24 | treated |
| San Francisco | +4.74 | -0.02 | control |
| Placer / Riverside / San Bernardino / Tehama | +4.76 | 0.00 | not in estimated set |

The two largest movers are control counties (Mendocino +4.69, Lake -3.91), and both swings exceed the headline's own magnitude. San Francisco, the pre-existing control, is now nearly inert (-0.02): the four added controls have absorbed the load it used to carry alone. The largest treated-county mover is the San Diego outlier (-2.60). This is the numerical signature of a design still governed by which small control counties it happens to contain.
