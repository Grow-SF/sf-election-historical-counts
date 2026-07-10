<!--
  TARGET PATH (finalizer decides new-file vs. superseding-edit):
    docs/analysis/2026-07-10-vca-bundle-tech-effect.md
    (successor to docs/analysis/2026-07-10-tech-effect-estimate.md; the
     composition-curve companion docs/analysis/2026-07-10-vbm-composition-curve.md
     is cited, not superseded)

  SLOT CONVENTION FOR THE FINALIZER
    Every figure that will move when the mega-integrator's refreshed panel
    lands is written as {{SLOT:short description}} with the current
    provisional value in parentheses immediately after, e.g.
        {{SLOT:any/epb headline effect, pp}} (provisional +3.26)
    Fill each slot from the re-estimated panel; delete the "(provisional ...)"
    parenthetical once filled. Provisional values are reproducible NOW against
    HEAD = b99fdd5 (packages/data/county_night.json, which already carries
    Riverside + San Diego primaries but NOT the full primaries expansion, the
    SoS status-page fills, the human-verification batch, the Nevada
    reclassification, or the --mechanism vca plumbing). They are placeholders,
    not the final word.
-->

# The counting-technology question, reframed: is it e-pollbooks, or the vote-center bundle they came in?

**Date:** 2026-07-10
**Panel:** `packages/data/county_night.json` (to be re-pinned by the finalizer at the post-integration commit; provisional figures reproduced against `b99fdd5`)
**Estimator:** `scripts/research/estimate_tech_effect.py` (cell-matched difference-in-differences, jackknife inference, randomization placebo)
**Supersedes:** `docs/analysis/2026-07-10-tech-effect-estimate.md`
**Companion (not superseded):** `docs/analysis/2026-07-10-vbm-composition-curve.md`

This document is the successor to the first defensible tech-effect estimate. It keeps that document's discipline: every number is recomputed against the pinned panel, the placebo is reported before the point estimate, and the verdict is written conditionally. It incorporates six things learned since that draft was committed: a reframing of what the treatment actually is, a two-channel decomposition that separates counting speed from mail composition, a primaries expansion that roughly doubled the panel, a cell-matched estimator built to hold mixed election types, a reclassification of one county's adoption record, and a corrected placebo methodology credited to the maintainer.

The single most important change is the first one, so it leads.

## Executive summary

The expanded panel still cannot separate a counting-technology speed-up from the noise floor set by its control group, and it now also cannot separate the "e-pollbook effect" from the vote-center bundle the e-pollbooks arrived inside. Both are honest negatives, and both point to the same next step.

The headline matched-cells estimate of the e-pollbook / "any" effect is **{{SLOT:any/epb headline effect, pp}}** (provisional +3.26 pp), with a 95% jackknife confidence interval of **{{SLOT:any/epb 95% jackknife CI}}** (provisional -9.20, +15.73). The interval comfortably includes zero. The randomization placebo, built by promoting subsets of the never-adopter controls to fake adopters and enumerating every valid split, spans **{{SLOT:placebo min}}** to **{{SLOT:placebo max}}** (provisional -20.72 to +17.29) at fake year 2018, centered near zero, and **{{SLOT:placebo n_as_extreme}} of 28 splits ({{SLOT:placebo share_as_extreme}})** (provisional 24 of 28, 86%) produce a spurious "effect" at least as extreme as the real headline. A design whose noise floor routinely matches or exceeds its own treatment estimate has not yet measured that treatment. That conclusion survived the panel roughly doubling.

Layered on top is an identification fact the maintainer's hypothesis surfaced and the adoption census then confirmed: **12 of the 13 treated California counties adopted e-pollbooks in the exact year they became Voter's Choice Act vote-center counties** (`epollbook_year == vca_year` for all twelve; see the treatment-reframing section). In California the "e-pollbook effect" and the "VCA vote-center bundle effect" are therefore observationally identical, not merely correlated. The one standalone e-pollbook adopter that could break the tie, San Bernardino, has no recoverable pre-adoption election-night point left in either generals or primaries, so the panel as constituted cannot decompose the bundle into its components at all.

The recommendation is unchanged in direction and sharper in detail: **do not report a headline counting-technology effect**, and pursue the out-of-state expansion, which is now the identification play for the bundle-versus-component question, not merely a way to add observations. The rest of the document establishes why, and what the primaries bought.

## 1. The treatment, reframed: e-pollbooks or the VCA bundle?

The first draft treated "adopted e-pollbooks (EPB)" as the intervention and differenced it against never-adopters. The maintainer raised the obvious confound in its strongest form: in California, a county did not adopt e-pollbooks in isolation. It adopted them as one component of the Voter's Choice Act conversion to vote centers, which simultaneously changed where people vote, how many mail ballots are processed centrally, when precinct results are consolidated, and which signature-verification workflow runs. If all of those changed on the same day, then whatever moved the election-night share is a property of the whole bundle, and calling it an "e-pollbook effect" is a naming choice, not a measurement.

The adoption census settles the factual question. For every treated county in the panel, `data/research/county-tech/ca_adoption_census.json` records `epollbook_year` and `vca_year` independently. They coincide exactly:

| County | epb year | vca year | asv year | bundle status |
|---|---|---|---|---|
| Fresno | 2020 | 2020 | 2020 | bundled |
| Los Angeles | 2020 | 2020 | 2020 | bundled |
| Madera | 2018 | 2018 | n/a | bundled |
| Napa | 2018 | 2018 | n/a | bundled |
| Nevada | 2018 | 2018 | 2022 (see Section 5) | bundled |
| Orange | 2020 | 2020 | n/a | bundled |
| Sacramento | 2018 | 2018 | n/a | bundled |
| San Diego | 2022 | 2022 | 2024 | bundled |
| San Mateo | 2018 | 2018 | n/a | bundled |
| Santa Clara | 2020 | 2020 | n/a | bundled |
| Placer | 2024 | 2024 | n/a | bundled |
| Riverside | 2022 | 2022 | 2025 | bundled |
| **San Bernardino** | **2020** | **none** | **2025** | **standalone** |

Twelve of the thirteen adopted e-pollbooks in the same year they became VCA vote-center counties. The estimator's e-pollbook cut and a would-be VCA-bundle cut therefore select the identical adoption year, county for county, for those twelve. The `--mechanism vca` cut being added to the estimator (`vca_year`-keyed, plumbing in flight with the mega-integration) will return **{{SLOT:vca-mechanism effect vs epb effect}}** (provisional: byte-identical to the epb cut for all twelve bundled counties, since the keying year is the same). This is not a robustness win; it is a statement that the panel cannot tell the two apart.

San Bernardino is the lone county whose e-pollbook adoption (2020) is not a VCA year (it never converted to vote centers; its `vca_year` is null, and its ASV came separately in 2025). It is the only county in California that could, in principle, isolate a standalone e-pollbook effect from the bundle. It cannot do so here, because its pre-adoption election-night record is exhausted: every pre-2020 general and every pre-2020 primary has been researched to a documented null (`.superpowers/sdd/dossier-san-bernardino-ca-primaries.md`; its single recoverable point, the 2022 primary, is post-adoption). With no pre-period, San Bernardino contributes no identified effect and drops out of every replicate. The standalone-versus-bundle contrast has no support in the California panel and will not acquire any from further California digging.

The consequence for how this document reads: wherever it says "e-pollbook effect," read "VCA vote-center bundle effect, of which e-pollbooks are one inseparable component." The two are the same estimand here. Breaking them apart requires jurisdictions that adopted e-pollbooks without a simultaneous vote-center conversion, which is the central argument for the out-of-state expansion in Section 9.

## 2. Two-channel decomposition: how much of the change is just more mail

A second confound runs underneath the whole design and is separable, at least partially, with SF's own ledger. Over the same years counties adopted the VCA bundle, California moved nearly every county toward mail voting. Mail ballots are counted more slowly than in-person ballots everywhere, so a rise in a county's vote-by-mail (VBM) share mechanically lowers its election-night share, independent of anything its counting technology does. The companion document (`docs/analysis/2026-07-10-vbm-composition-curve.md`, committed) builds and calibrates that separation; this section states its headline and folds its residuals into the reframed panel.

The identity is `night_share = m*S_mail + (1-m)*S_precinct`, where `m` is the final mail share, `S_mail` is the fraction of mail counted by night, and `S_precinct` the fraction of precinct ballots counted by night. San Francisco is the calibration county (no vote centers, no e-pollbooks, no ASV, 100% central mail count, and a published per-release mail/election-day split), so the two channel rates are read directly off its ledger rather than inferred. Across 18 SF elections, `S_mail` runs about 0.53 and `S_precinct` about 0.80: precinct ballots are counted faster every time, and shifting composition toward mail lowers the night share by the gap between them.

The calibrated headline, era-qualified because the gap has narrowed over time: **for every 10 points of VBM share, the election-night tally drops about {{SLOT:composition X overall, pp per 10pp mail}}** (provisional 2.65 pp), resolving to **{{SLOT:composition X pre-2022}}** (provisional ~3.1 pp) before 2022 and **{{SLOT:composition X 2022+}}** (provisional ~1.7 pp) from 2022 on. The narrowing is driven by statewide postmark-deadline extensions and the growth of early-returned universal mail, both unrelated to any county's counting technology; use the 2022+ kernel for present-day work.

Applying the era-matched kernel to the treated counties' real mail shares (`data/research/county-vbm/county_vbm_share.csv`, 228 rows) nets the mechanical composition drag out of each county's DiD. Every treated county's mail share rose over its window, so composition alone should have lowered every night share; excusing that roughly doubles the apparent technology-attributable residual. On the generals-only panel the mean raw DiD of +4.76 became a composition-adjusted **{{SLOT:composition-adjusted headline, net}}** (provisional +5.79 pp control-netted) to **{{SLOT:composition-adjusted headline, naive}}** (provisional +9.08 pp naive, which double-counts the statewide mail shift already differenced out through the controls). The net figure is the defensible one; the naive figure must never be quoted without its double-counting caveat.

These residuals are pinned to the +4.76 generals-only panel and **will refresh with the primaries re-estimate**; treat every composition figure above as a slot. Two things do not change with the refresh. First, three of the four caveats in the companion document push the residual "speed-up" estimate upward (SF's central-count `S_mail` is higher and less back-loaded than a vote-center county's, so the SF kernel understates the true composition penalty for exactly the vote-center counties under study), meaning the adjusted headline is if anything generous to the technology. Second, and decisively: the composition adjustment changes the *size* of the claim, not whether it clears the design's own noise floor. The placebo distribution (Section 6) still exceeds even the net-adjusted headline, and the 37-point county-level spread is untouched by a near-uniform composition shift.

## 3. Panel inventory after the primaries expansion

The first draft's panel was generals-only: nineteen jurisdictions, six control counties (five contributing), ten identified treated counties, and three benched treated counties (Placer, Riverside, San Bernardino) that lacked an identifying pre/post point.

The expansion added June/March statewide primaries as a second election type per county. Primaries dates in scope: 2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05, 2022-06-07, 2024-03-05 (the March 2020 presidential primary is excluded alongside the November 2020 general as COVID-adjacent all-mail outliers). This brought **{{SLOT:count of new county primary cells recovered}}** (provisional ~60 new county primary cells across 17 dossiers) plus San Francisco's six own-data primary points, and it changed the identified set:

- **Riverside becomes identified.** Its generals gave no pre-adoption sourced point; its 2016 and 2018 primaries (pre-adoption) plus its 2022 primary (its VCA rollout election) supply the missing pre/post cells. Its per-county effect enters negative (**{{SLOT:riverside per-county effect}}**, provisional -4.22 pp), pulling the aggregate down.
- **Placer becomes identified** once its recovered 2024-03 primary point lands (69,436 / 135,869 = 51.11%, recovered from the CA Secretary of State election-night status page via Wayback). Contrarian: its post-adoption share (~51) sits below its pre-adoption primary range (62-70) despite a *falling* mail share after its 2024 vote-center switch pulled voters back in person. (Placer's primaries are integrated by the mega-integrator, not yet in HEAD; its identified status is **{{SLOT:placer identified yes/no + per-county effect}}**, provisional: identified after integration.)
- **San Bernardino stays benched.** Pre-period exhausted in both generals and primaries (Section 1).
- **San Diego's outlier is tempered.** Its primary series is flat through adoption (~60-62% at all four primaries), which drags its formerly extreme generals-based per-county effect down from +28.20 toward **{{SLOT:san-diego per-county effect}}** (provisional +20.70 pp at HEAD).

Identified treated counties after full integration: **{{SLOT:n identified treated counties}}** (provisional 11 at HEAD with Riverside; ~12 once Placer's primaries land). Contributing controls remain the same five (San Francisco, Lake, Del Norte, Mendocino, Tehama; Colusa is retained as a documented-null control and contributes zero comparable points). The California never-adopter pool is a census result, not a research-effort gap: exactly seven counties never adopted EPB or ASV through 2024 (Colusa, Del Norte, Lake, Mendocino, Plumas, San Francisco, Tehama), six already in the panel, and the seventh (Plumas) is another small idiosyncratic rural series of the exact kind already driving the placebo. There is no California control left to add that would stabilize the design.

### The Secretary of State status-page vein

The primaries expansion surfaced a new systematic evidence source worth naming, because it did double duty. The CA Secretary of State election-night status page (`electionresults.sos.ca.gov/returns/status`, recoverable via Wayback) publishes a per-county night-count table for every statewide election. A sweep across all 12 panel elections x 19 counties graded **{{SLOT:SoS sweep cells graded}}** (provisional 228) cells: it produced **{{SLOT:SoS brand-new fills}}** (provisional 73) brand-new fills for cells individual county scouts had nulled, and, as an independent cross-check, it re-derived **{{SLOT:SoS cross-checks validating existing values}}** (provisional ~49) already-committed values from a second source and **corrected {{SLOT:SoS corrections count}}** (provisional 3) of them (Napa 2014-11 to 50.34%, Del Norte 2016-11 to 86.31%, Riverside 2024-11 to 57.11% and thereby comparable). An independent source that reproduces roughly fifty committed numbers and corrects three is the strongest provenance check this dataset has received.

## 4. The cell-matched estimator

Adding a second election type broke a hidden assumption in the original estimator and required a real fix before any county primary rows could land. `_control_change` decided which of a control county's rows to average into its pre/post change by bare calendar year. Once a single year can hold two elections of different type (a general and a primary), matching on year alone blends unrelated levels: a control's primary row in a year the treated county never held a primary would contaminate that control's pre-period average, even though primaries run structurally lower than generals.

The fix keys matching on `(year, type)` cells. `_per_county_effects` builds the treated county's own `pre_cells` and `post_cells` as `(year, type)` tuples; a control contributes only the cells the treated county actually has, and only if it has at least one matching pre cell and one matching post cell. The treated county's own pre/post average is unchanged; only the control-matching side moved to cells. This matters specifically because primary and general turnout, mail mix, and reporting cadence differ, so comparing a treated county's general to a control's primary (or vice versa) is not a valid counterfactual.

The change was built test-first. A synthetic panel with uneven primary coverage recovered the injected effect exactly under cell-matching but returned a biased -12.125 (against an injected -10.0) under the old year-only matching, confirming the bug was real and the fix removes it (`.superpowers/sdd/primaries-plumbing-report.md`). As a guardrail, regenerating SF's six primary points left the headline byte-identical (+4.763520833...) before any treated county carried primaries, exactly as cell-matching predicts (SF's new primary cells are only ever consumed as a control contribution, and no treated county had a matching primary cell yet).

## 5. Nevada's reclassification, and why the adjudication layer exists

Nevada County is the case study for why the census carries an explicit adjudication layer rather than trusting a single first-pass tech record. Its primaries scout turned up two documents that contradict the committed record: a Board of Supervisors file (SR 16-0825, dated 9/27/2016) recording an ES&S MBV-1000 purchase with signature-recognition software, and a County Clerk statement describing e-pollbooks in use at the June 2016 cycle, two years before the documented 2018 adoption.

The adjudication (`.superpowers/sdd/progress.md`, 2026-07-10) resolved both: **ASV revised to 2016** (signed contract plus a 2016-General setup line, with a live-use caveat carried because a signed contract is procurement, not proof of election-day use), and the **e-pollbook record split-keyed to 2014** (the Clerk's countywide-EPB-in-2014 statement), with the 2018 vote-center record retained as the VCA conversion. The committed census at HEAD still shows Nevada as EPB 2018 / ASV 2022; the mega-integrator lands the correction as **EPB 2014 / ASV 2016**. This reclassification moves Nevada's treatment windows and its cohort membership: **{{SLOT:Nevada cohort + per-county effect after reclassification}}** (provisional, pre-reclassification at HEAD: Nevada per-county effect -0.03 pp, currently grouped in the 2018 cohort; post-reclassification it shifts earlier). Two judgment calls in that adjudication are flagged for the maintainer: the 2014-keying modeling choice, and the ASV-live-use caveat.

The general point: a first-pass tech record extracted by a research agent is a hypothesis, not a fact, and the census plus adjudication layer exists precisely so that a load-bearing classification (an adoption year that decides which cohort a county sits in, or whether a county is treated or control at all) can be revised against primary-source documents without silently corrupting the panel.

## 6. Inference: jackknife primary, randomization placebo corroborating

The formal inference is a leave-one-county-out jackknife over the counties that carry data, yielding the confidence interval quoted in the executive summary: **{{SLOT:any/epb 95% jackknife CI}}** (provisional -9.20, +15.73), which includes zero. This is the primary formal statement.

The placebo corroborates it. The procedure takes the control counties only, promotes a subset to "fake adopters" at a fake adoption year, and re-runs the estimator; never-adopters share the same statewide year shocks as the controls left behind, so a well-behaved design must return approximately zero. There is no single canonical way to split five controls into fake adopters and fake controls, so `placebo_distribution()` enumerates every nonempty proper subset (30 total; 2 invalid because Tehama has no pre-2018 point, leaving **28 valid splits**) and reports the whole distribution.

At fake year 2018 the 28 splits span **{{SLOT:placebo min}}** to **{{SLOT:placebo max}}** (provisional -20.72 to +17.29), mean **{{SLOT:placebo mean}}** (provisional -1.49), sd **{{SLOT:placebo sd}}** (provisional 11.13), and **{{SLOT:placebo n_as_extreme}} of 28 ({{SLOT:placebo share_as_extreme}})** (provisional 24 of 28, 86%) are at least as extreme as the real headline. The distribution is centered near zero, as it should be, but wide enough that the real effect sits inside its bulk rather than out at a tail. One asymmetry makes this more damning, not less: the fake-adopter groups are necessarily small (1 to 4 controls) versus the real estimate's ten-plus treated counties, so this null is a deliberately wide, conservative noise floor, and the headline still fails to clear it.

**The placebo-methodology correction is credited to the maintainer.** An earlier draft quoted a single arbitrary split (+10.23, every-second control alphabetically at fake year 2018) as "the single most important number in this document" and compared the headline head-to-head against that one draw. The maintainer caught that this was one of 28 valid splits, not a stable noise-floor estimate; a different split of the same controls gives -14.32. `placebo_distribution()` and a dated correction note replaced the single draw with the full distribution (`.superpowers/sdd/placebo-fix-report.md`, commit `90ead96`). The inference conclusion was unchanged, but the earlier presentation understated the noise floor by quoting one point instead of the distribution it was drawn from.

For transparency, the ASV cut returns **{{SLOT:asv effect and CI}}** (provisional +13.91 pp, CI +2.73 to +25.09, n_treated 4) with an interval excluding zero. That is not evidence of an ASV effect. Two of its four identifying counties adopted EPB and ASV in the same year (Fresno, LA), so their "ASV effect" is arithmetically identical to their EPB effect; a third (Nevada) spends most of its ASV pre-window pre-EPB; and after the reclassification in Section 5 the ASV timing shifts again. A tight interval around a badly confounded estimand is a false comfort, not a finding.

## 7. Minimum detectable effect and the binding constraint

The realized jackknife MDE at the current panel is **{{SLOT:realized MDE, pp}}** (provisional 17.80 pp), still several times the absolute point estimate. The primaries expansion improved it (more points per county tighten each county's own pre/post estimate) but did not fix the underlying constraint, and the reason is worth stating because it re-ranks the follow-ons.

Control noise is no longer binding; between-county heterogeneity among the treated counties is. The standard deviation of the treated counties' individual effects is **{{SLOT:treated-effect sd, pp}}** (provisional ~12 pp, the 37-point San-Diego-to-Madera range). The MDE has a floor of roughly that heterogeneity divided by the square root of the number of treated counties, which is about **{{SLOT:heterogeneity floor, pp}}** (provisional ~11 pp) even with infinite perfect controls. No amount of California control-side work gets below it, and there are no California controls left to add anyway. Detecting an effect of the composition-adjusted headline's own size at conventional confidence requires on the order of 50 treated counties, not the {{SLOT:n identified treated counties}} (provisional ~12) in hand. The binding constraint is the number of treated counties and the spread of their effects, so the follow-ons that matter are the ones that add treated counties, ideally counties whose adoption is not VCA-bundled, which shrinks the heterogeneity by removing a confound.

## 8. Verification status

The numbers inherit the verification status of the underlying election-night rows, tracked in `data/research/election-night/HUMAN_VERIFY.md`, whose plateau judgments are the maintainer's to make (the machine pass can confirm a number appears at its cited URL and that finals match the SoS Statement of Vote, but cannot confirm that a cited report is the *last* one posted on election night). The human-verification loop was load-bearing this campaign; the maintainer's verdicts, incorporated into the panel, were:

- **Lake ASV = not adopted** (confirmed 2026-07-10). Lake's control status stands. This was the single most consequential open item, because Lake's no-tech election-night collapse (63.0% in 2018 to 38.5% in 2022 to 29.3% in 2024) is one of the largest single influences on the control baseline; had Lake been an ASV adopter it would have moved to the treated side and lowered the headline further. A dated human-confirmed annotation was recorded in the Lake county-tech record.
- **Mendocino 2012 general: override to restore as an approximation** (18,401 / 36,080 = 51.00%, secondary, with a dated maintainer-override sentence and the plateau verdict set to PLAUSIBLE-approximation). This adds a Mendocino pre-point and shifts the estimate slightly; the refreshed headline reflects it.
- **Three confirmations:** Mendocino 2014 general (11,402 / 25,017), Mendocino 2024 general (15,611 / 39,837), Napa 2014 general, each hand-read and confirmed correct.
- **Santa Clara 2012-06 primary: ceiling default.** In deadline mode the maintainer set this to the ceiling-plus-scaling-note default (the 234,342 "Semi-Final" Wednesday state treated as a ceiling rather than a plateau) rather than upgrading it to a sourced point.

Two plateau rows were refuted as plateaus during review and correctly excluded (Placer 2018-11 and Riverside 2024-11 both tracked the canvass, not election night). The outstanding judgment items the maintainer may still want to weigh: San Diego's 2024-03 `vs_asv` classification (March-primary versus November-general first ASV election is genuinely ambiguous), the Nevada 2014-keying and ASV-live-use caveats from Section 5, and the small set of secondary-confidence rows enumerated in HUMAN_VERIFY.md.

## 9. Decision gate and re-ranked follow-ons

The gate: if the interval excludes zero, report the effect; if it includes zero and the MDE exceeds the absolute point estimate, recommend the follow-on that breaks the tie. We are unambiguously in the second case. The interval **{{SLOT:any/epb 95% jackknife CI}}** (provisional -9.20, +15.73) includes zero; the MDE **{{SLOT:realized MDE, pp}}** (provisional 17.80) is several times the point estimate; the placebo swallows the headline; and the composition adjustment moves the size of the claim without clearing the noise floor. **Do not report a headline counting-technology effect.** The follow-ons, re-ranked given what the primaries already bought:

**First, and now the identification play: out-of-state jurisdictions** (Pennsylvania, New York, Wisconsin; leads in `data/research/county-tech/`). The primaries expansion did *not* break the VCA collinearity, because 12 of 13 California adopters are bundled by construction (Section 1) and no California county adopted e-pollbooks without a simultaneous vote-center conversion (San Bernardino, the one standalone adopter, has no recoverable pre-period). Out-of-state counties adopted e-pollbooks without California's VCA all-mail vote-center transition, so they are the only way to separate a standalone e-pollbook effect from the bundle effect, and they add larger, more comparable treated counties that attack the between-county-heterogeneity floor from Section 7. This is the one follow-on that addresses both of the design's deepest problems. (The California in-state shortcut, verifying Kern/Kings as candidate non-VCA e-pollbook counties, was dropped in deadline mode and remains a cheap thing to revisit before committing to out-of-state archive work.)

**Second: November 2026, mechanically and at no research cost.** The November 2026 general adds a fresh post-2024 point for every county in the panel and a second post-adoption point for the newly-identified Placer and Riverside. It is calendar-gated (SoS Statement of Vote publishes around December 2026) and requires no new playbook. It will not resolve the bundle confound or the control exhaustion, but it is the cheapest available increment to n and should be collected for all panel counties as soon as it certifies.

**Third: a canvass-speed alternative outcome** (days-to-threshold rather than the election-night plateau share), which may carry a cleaner signal than a snapshot sensitive to poll-close timing. It ranks third because it is a new metric needing its own validation and does not by itself add treated counties.

**Credential-bound items for the human** (browser-armed recovery could not clear these; they need NewsBank/SFPL ezproxy credentials): the Sacramento Bee 2014-06 primary and the Sacramento 2016-11 and Fresno 2018-11 election-night plateaus, all McClatchy/NewsBank-walled. These are the remaining recoverable gaps that automated routes exhausted.

---

## Appendix A: Reproducing the provisional figures

All provisional figures were computed against HEAD `b99fdd5` (`packages/data/county_night.json`). The finalizer should re-pin to the post-integration commit and refill every slot from that panel.

```bash
# Headline + placebo (Sections 1, 6)
python3 scripts/research/estimate_tech_effect.py --mechanism any --placebo --json
python3 scripts/research/estimate_tech_effect.py --mechanism epb --json
python3 scripts/research/estimate_tech_effect.py --mechanism asv --json
# VCA-bundle cut (once vca_year plumbing + --mechanism vca land)
python3 scripts/research/estimate_tech_effect.py --mechanism vca --json
# Composition residuals (Section 2): companion doc's analyze.py / apply_real_m.py
```

Provisional readouts at HEAD `b99fdd5`: any/epb effect +3.26, se 6.36, CI (-9.20, +15.73), MDE 17.80, n_treated 11, n_controls 5; placebo (fake 2018) n=28, mean -1.49, sd 11.13, min -20.72, max +17.29, 24/28 as extreme; asv +13.91, CI (+2.73, +25.09), n_treated 4. Per-county at HEAD: San Diego +20.70, Santa Clara +13.35, Orange +13.20, Fresno +13.12, LA +6.97, Nevada -0.03, Napa -1.88, Riverside -4.22, San Mateo -7.05, Sacramento -8.79, Madera -9.46. These reflect Riverside + San Diego primaries only; the full primaries expansion, SoS fills, human-verify batch, and Nevada reclassification will move all of them.

## Appendix B: Slot index

Headline: any/epb effect, any/epb 95% CI, vca-mechanism effect vs epb, asv effect and CI.
Panel: count of new county primary cells, n identified treated counties, Riverside per-county effect, Placer identified + effect, San Diego per-county effect, SoS sweep cells graded / brand-new fills / cross-checks / corrections.
Placebo: min, max, mean, sd, n_as_extreme, share_as_extreme.
Composition: X overall / pre-2022 / 2022+, composition-adjusted headline net / naive.
MDE: realized MDE, treated-effect sd, heterogeneity floor.
Nevada: cohort + per-county effect after reclassification.
