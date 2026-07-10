# The vote-by-mail composition curve: how much of the election-night change is just more mail

**Date:** 2026-07-10
**SF panel pinned at:** commit `1cd1f8875a9469d1a194f256131d718f2656d581` (`sf_count_timeline.csv`, `elections.json`, `sf_vbm_share_sos.csv`, `sf_turnout_history_1960_2002.csv`, `sf_turnout_history_doe_1899_2019.csv`, `vbm_history.json`)
**County covariate source:** `data/research/county-vbm/county_vbm_share.csv` (this commit)
**Treated-county DiD effects cited:** `docs/analysis/2026-07-10-tech-effect-estimate.md` at SHA `1cd1f88`
**Code:** `scratchpad/analyze.py` (SF channel measurement, reconstruction check, regression), `scratchpad/apply_real_m.py` (per-county composition adjustment). Both stdlib-only and re-runnable; every number below was recomputed against the pinned inputs by rerunning both scripts, not copied from an earlier draft.

**This document's numbers are pinned, not live.** The underlying county election-night panel is being actively extended (a primaries-integration pass is in flight in a parallel branch at the time of writing). The ten treated-county DiD effects cited here, and therefore the residual figures in Section 4, are frozen at the `1cd1f88` panel. When the panel is re-estimated, a successor findings document will carry the refreshed versions; treat the numbers below as the first defensible calibration, not the final word.

## Why this document exists

The companion panel (`docs/analysis/2026-07-10-tech-effect-estimate.md`) asks whether county adoption of e-pollbooks or automated signature verification raises the share of a county's vote counted by election night. Its headline difference-in-differences estimate is +4.76 percentage points, an interval that comfortably includes zero, and a placebo distribution that swallows the headline. One obvious confound sits underneath that whole design: over the same years counties adopted counting technology, California also moved almost every county toward mail voting (the Voter's Choice Act rollout, then the 2021 universal-vote-by-mail law). If a county's vote-by-mail share rose over its pre/post window, and mail ballots are counted more slowly than in-person ballots everywhere, some or all of an observed drop (or muted rise) in election-night share is mechanical composition, not counting speed. This document builds and applies a composition kernel to separate the two.

San Francisco is the calibration county because it never adopted e-pollbooks, ASV, or vote centers, processes 100% of its mail centrally, and publishes a per-release vote-by-mail / election-day split for every count. That lets the composition mechanism be read directly off the ledger, channel by channel, rather than inferred from a single cross-sectional regression.

## 1. The model

```
night_share = m * S_mail + (1 - m) * S_precinct
  m          = final mail share = final_vbm / final_total
  S_mail     = night_vbm / final_vbm      (fraction of mail ballots counted by night)
  S_precinct = night_eday / final_eday    (fraction of precinct/election-day ballots counted by night)
```

`night_share` decomposes exactly into two channel-completion rates weighted by composition. Any change in `m` moves `night_share` mechanically, holding the channel rates fixed, because `S_mail < S_precinct` for every SF election measured (mail is always the slower channel). Separating that mechanical piece from a genuine change in `S_mail` or `S_precinct` (a real speedup) is the point of the whole exercise.

## 2. SF channel measurement (S_mail / S_precinct)

For every SF election whose night release and final release both carry the vote-by-mail / election-day split (n = 18, spanning 2015-11 through 2026-06), `S_mail` and `S_precinct` are read directly:

| date | election | S_mail | S_precinct | m (final vbm) | night_share |
|------|----------|-------:|-----------:|--------------:|------------:|
| 2015-11-03 | Municipal | 0.524 | 0.858 | 0.619 | 0.651 |
| 2016-06-07 | Presidential Primary | 0.603 | 0.849 | 0.604 | 0.701 |
| 2016-11-08 | General | 0.541 | 0.871 | 0.635 | 0.661 |
| 2018-06-05 | Statewide Primary | 0.482 | 0.839 | 0.646 | 0.608 |
| 2018-11-06 | General | 0.485 | 0.800 | 0.657 | 0.593 |
| 2019-11-05 | Municipal | 0.474 | 0.767 | 0.712 | 0.559 |
| 2020-03-03 | Presidential Primary | 0.365 | 0.675 | 0.649 | 0.474 |
| 2020-11-03 | General (pandemic all-mail) | 0.782 | 0.797 | 0.915 | 0.784 |
| 2021-09-14 | Gubernatorial Recall | 0.789 | 0.762 | 0.915 | 0.787 |
| 2022-02-15 | Special Municipal | 0.712 | 0.889 | 0.934 | 0.724 |
| 2022-04-19 | Special General | 0.782 | 0.890 | 0.953 | 0.787 |
| 2022-06-07 | Statewide Primary | 0.527 | 0.845 | 0.903 | 0.558 |
| 2022-11-08 | General | 0.482 | 0.728 | 0.885 | 0.510 |
| 2024-03-05 | Presidential Primary | 0.405 | 0.772 | 0.880 | 0.449 |
| 2024-11-05 | General | 0.558 | 0.636 | 0.858 | 0.569 |
| 2025-09-16 | Special Recall | 0.759 | 0.869 | 0.946 | 0.765 |
| 2025-11-04 | Statewide Special | 0.655 | 0.750 | 0.904 | 0.664 |
| 2026-06-02 | Statewide Primary | 0.419 | 0.785 | 0.886 | 0.461 |

`S_mail` median 0.534, range 0.365 to 0.789. `S_precinct` median 0.799, range 0.636 to 0.890. Precinct/election-day ballots are counted roughly 0.80 by night; mail roughly 0.53. That gap is the entire mechanism: shifting composition toward mail mechanically lowers the night share, independent of anything a county's elections office does.

**Era channel rates**, the calibration kernel used below:

| era | n | S_mail | S_precinct | S_precinct - S_mail |
|-----|--:|-------:|-----------:|--------------------:|
| pre-2016 | 1 | 0.524 | 0.858 | 0.334 |
| 2016-2020 | 7 | 0.485 | 0.800 | 0.315 |
| 2022+ | 10 | 0.606 | 0.778 | 0.172 |

The gap narrows over time, from about 0.33 to about 0.17, because `S_mail` rose (postmark-deadline extensions plus universal mail moved more ballots into the early-processed pile) while `S_precinct` fell (2024 general S_precinct = 0.636, a growing election-day/provisional verification backlog). The composition kernel is era-specific, not a constant; pre-2016 is a single election and is indicative only.

## 3. The headline, and why it needs an era qualifier

**"For every 10 percentage points of VBM share, the election-night tally share drops by X points."**

Two independent ways to get X, and they disagree in an instructive way:

**(a) Long-run SF regression.** All SF elections carrying both `nightPct` and `vbmShare` (n = 27, 1983-2026), excluding four `nightPartial` floor rows (n = 23 clean), OLS of `night_share` on `m`: slope -0.196, R^2 = 0.069. `X = -10 * slope = **+1.96 pp** per 10 pp of mail share`. Classic OLS SE gives 95% CI (-1.12, +5.04); a leave-one-election-out jackknife, the more honest interval for 23 heterogeneous elections rather than iid draws, gives 95% CI **(-2.41, +6.33)**. The interval includes zero: the regression alone cannot establish that X differs from zero. It is attenuated toward zero because in the SF cross-section `m` and `S_mail` co-move positively (the high-mail elections, 2020 general, 2021 recall, 2022 specials, are exactly the ones where mail arrived early and was processed fast), which partly cancels the mechanical composition penalty.

**(b) Direct channel measurement**, `X = 10 * (S_precinct - S_mail)`, holds the channel rates fixed and varies only `m`, which is the trustworthy estimate; the regression corroborates its sign and central tendency but cannot stand alone.

| era | X (pp per +10 pp mail) |
|-----|----------------------:|
| pre-2016 | +3.34 (n=1, indicative) |
| 2016-2020 | +3.15 |
| 2022+ | +1.72 |
| overall (median) | **+2.65** |

**The honest, era-qualified version:** a single fixed X is not defensible. X drifts from about **+3.1 pp per 10 pp of mail share before 2022** (averaging the pre-2016 and 2016-2020 kernels) to about **+1.7 pp from 2022 on**, a near-halving driven by forces unrelated to any county's counting technology: statewide postmark-deadline extensions (postmark+3 in 2015, postmark+7 in 2020) and the growth of early-returned universal mail both raised `S_mail`, shrinking the `S_precinct - S_mail` gap. The regression's single-number X (+1.96 pp, CI swallowing zero) sits inside the range the direct method spans but cannot arbitrate between eras. Use the 2022+ figure (+1.7 pp) for present-day treated-county work; a pre-2022 kernel on a post-2022 comparison overstates the composition penalty.

## 4. Identity check: the model is exact for SF

Because SF folds provisional/election-day-conditional ballots into the election-day bucket (no third channel), `night_total == night_vbm + night_eday` and `final_total == final_vbm + final_eday` hold exactly for all 18 elections, so `night_share = m*S_mail + (1-m)*S_precinct` is an identity, not an approximation, and must reconstruct `elections.json`'s `nightPct` up to its 0.1-point rounding.

**18/18 reconstruct.** Rerunning `analyze.py` against the pinned inputs, every one of the 18 elections has `|reconstructed% - nightPct| <= 0.05 pp`: 2015-11-03 (+0.03), 2016-06-07 (-0.02), 2016-11-08 (+0.05), 2018-06-05 (+0.04), 2018-11-06 (+0.01), 2019-11-05 (-0.01), 2020-03-03 (0.00), 2020-11-03 (-0.04), 2021-09-14 (-0.04), 2022-02-15 (-0.00), 2022-04-19 (-0.03), 2022-06-07 (+0.01), 2022-11-08 (+0.02), 2024-03-05 (-0.03), 2024-11-05 (-0.03), 2025-09-16 (+0.02), 2025-11-04 (-0.01), 2026-06-02 (-0.03). Pure rounding, in both directions, with no residual pattern. Two rows that once looked off (2015-11 +4.31, 2016-06 +2.75, in an earlier draft) were a date-only-timestamp bug that let a next-day-processing release slip in as "election night"; after excluding `T00:00:00` rows dated after election day, they collapse to rounding like every other row. There is no provisional or "other" leakage this model has to excuse.

## 5. Applying the kernel to the treated-county panel

`data/research/county-vbm/county_vbm_share.csv` (228 rows, 19 panel counties x 12 statewide elections, 2012-2024 excluding 2020) supplies real per-county mail shares to replace the placeholder used in an earlier draft of this calibration. For each of the ten treated counties identified in the pinned tech-effect estimate, `m_pre` and `m_post` are the mean of the county's real `vbm_share_pct/100` over its actual panel pre/post windows (the same matched-cells windows the DiD estimator uses), and the kernel is the SF era rate matched to the post window's year(s):

```
delta_expected = (m_post - m_pre) * kernel
residual       = DiD - delta_expected
```

| county | DiD (pp) | m_pre | m_post | delta_expected (pp) | residual (pp) |
|--------|---------:|------:|-------:|--------------------:|--------------:|
| san-diego-ca | +28.20 | 0.685 | 0.874 | -3.25 | +31.45 |
| santa-clara-ca | +13.35 | 0.745 | 0.899 | -2.65 | +16.00 |
| orange-ca | +13.20 | 0.587 | 0.803 | -3.73 | +16.93 |
| fresno-ca | +13.12 | 0.548 | 0.809 | -4.49 | +17.61 |
| los-angeles-ca | +6.97 | 0.373 | 0.761 | -6.68 | +13.65 |
| nevada-ca | -0.03 | 0.759 | 0.934 | -4.25 | +4.22 |
| napa-ca | -1.88 | 0.919 | 0.965 | -1.01 | -0.87 |
| san-mateo-ca | -7.05 | 0.644 | 0.898 | -5.57 | -1.48 |
| sacramento-ca | -8.79 | 0.624 | 0.924 | -6.58 | -2.21 |
| madera-ca | -9.46 | 0.656 | 0.881 | -4.94 | -4.52 |
| **mean** | **+4.76** | | | **-4.32** | **+9.08** |

Every treated county's mail share rose over its window (delta m from +0.05 Napa to +0.39 Los Angeles), so composition alone should have *lowered* every night share; netting that out roughly doubles the mean technology-attributable residual, from the raw +4.76 pp DiD headline to a **naive** +9.08 pp.

**The double-counting caveat.** That +9.08 pp naive figure over-corrects. The DiD estimator already nets out the five control counties, and the controls' mail shares rose too (control-matched mean delta m = 0.13 to 0.20 per window, from the same sweep: the VCA/universal-mail shift was statewide, not confined to the treated counties). Subtracting a treated county's *full* composition drag from a control-netted DiD therefore counts the statewide part of the mail-share shift twice: once implicitly, inside the DiD's control-differencing, and once explicitly, in `delta_expected`. The cleaner form nets the composition shift itself against the control group first, `delta_expected_net = (dm_treated - dm_control) * kernel`, which gives a mean net `delta_expected_net` of only **-1.03 pp** and a mean net residual of **+5.79 pp** (e.g. San Diego residual_net +28.71, Los Angeles +10.24, Madera -7.45; full per-county values in `scratchpad/apply_real_m.json`). **The honest range for the composition-adjusted headline is +5.8 to +9.1 pp**, depending on whether the control group's own composition shift is credited to the DiD (giving the lower, net figure) or to the kernel (giving the higher, naive figure). The net figure, +5.79 pp, is the more defensible one; +9.08 pp should not be quoted without the double-counting caveat attached.

**Does the adjustment change the verdict?** It roughly doubles the point estimate in level (raw +4.76 vs. net-adjusted +5.79 vs. naive-adjusted +9.08) and sharpens the story qualitatively: the 2018 e-pollbook cohort's puzzling negative effects (Napa, San Mateo, Sacramento, Madera) become *more* negative once their composition drag is excused, meaning they adopted the technology and still fell behind even after accounting for the extra mail they had to process. The 2020/2022 cohort's positive effects grow. But the adjustment cannot rescue the design's underlying identification problem: the companion document's placebo distribution (spanning -20.72 to +17.29 pp, 71% of splits at least as extreme as the +4.76 raw headline) still exceeds even the net-adjusted headline, and the county-level spread (a 37-point range from San Diego +28.20 to Madera -9.46) is untouched by a near-uniform composition shift. Composition adjustment changes the size of the claim, not whether the claim clears the design's own noise floor.

## 6. Caveats

1. **SF-only kernel: central-count mail may not transfer to vote-center counties.** SF's `S_mail` is a central-count rate: it has no vote centers, so all its mail is processed at one facility on a predictable schedule. A Voter's Choice Act county's late same-day drop-offs (ballots left at a vote center on election day, transported and opened days later) make its true `S_mail` lower and more back-loaded than SF's for the same `m`. Using SF's higher `S_mail` makes `S_mail - S_precinct` less negative than reality, so `|delta_expected|` is understated, which biases the residual "speedup" **upward** for vote-center counties: some of what this calibration credits to technology may actually be an uncorrected composition penalty.

2. **Postmark-law drift moved S_mail statewide, for reasons unrelated to county tech.** Postmark+3 (2015) and postmark+7 (2020) pushed a larger share of mail past election night into the canvass, lowering `S_mail` over time, independent of e-pollbooks or ASV adoption in any given county. If a treated county's pre/post window straddles one of these law changes, part of its `m` shift (and thus `delta_expected`) is a statewide legal artifact, not composition or technology. This calibration uses the era-matched kernel (2016-2020 vs. 2022+) specifically to neutralize this; a pre-2015 kernel should never be used on a post-2020 comparison.

3. **Vote-center transferability more generally: the m-S_mail co-movement in Section 3 is SF-specific.** In SF, high-mail elections were also early-processed-mail elections, which partly cancels the mechanical composition penalty in the regression. A treated county without that correlation, particularly a vote-center county where late drop-off is common, will have a more negative effective `S_mail - S_precinct` than SF's medians imply. The SF kernel therefore likely **understates** the true composition penalty for those counties, again biasing the residual "speedup" upward.

4. **Turnout-context confounding.** `S_mail` swings with turnout magnitude in SF (pandemic universal-mail spike to 0.79; high-turnout presidential-primary drop to about 0.48 or lower). Matching a treated county's high-turnout general-election window to SF's pandemic-era kernel, rather than an era- and type-matched one, would badly overstate `S_mail` and understate the composition penalty. Mitigated here by using era-matched kernels, not by matching election type or turnout regime directly; a finer match remains future work.

Three of four caveats push the residual "speedup" estimate **upward**. Combined with the companion panel's own finding that its e-pollbook headline (+4.76 pp raw) sits well inside its placebo noise distribution (28 valid fake-adopter splits ranging -20.72 to +17.29 pp, 71% of them at least as extreme as the real headline), a composition kernel that likely over-states speedup would make an already-weak technology effect look stronger than the data support. This calibration should be read conservatively, and any headline drawn from it (+5.79 to +9.08 pp) should carry the SF-only-kernel caveat every time it is quoted.
