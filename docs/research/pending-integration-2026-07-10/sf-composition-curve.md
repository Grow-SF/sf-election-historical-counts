# SF composition-curve calibration for the county election-night panel

Read-only analysis scout. All inputs pinned at commit `1cd1f8875a9469d1a194f256131d718f2656d581`
(`git show 1cd1f88:<path>`), copied into `scratchpad/pin/`. Working tree was changing under other
agents during this run; nothing here reads the live tree.

Pinned inputs:
- `pin/sf_count_timeline.csv` (per-release counts, `ballots_vbm` / `ballots_election_day`, `report_datetime`)
- `pin/elections.json` (authoritative `nightPct`, `vbmShare`, `nightPartial`)
- `pin/sf_vbm_share_sos.csv`, `pin/sf_turnout_history_1960_2002.csv`, `pin/sf_turnout_history_doe_1899_2019.csv`, `pin/vbm_history.json` (split back-catalog, used to sanity-check `vbmShare`)

Night cutoff convention (from `scripts/build_consolidated_export.py`): a release counts as an
election-night release if `report_datetime <= E+1 06:00`. The night total is the max
`ballots_counted_total` among qualifying releases; the final is the max over all releases.

Code that produced every number below: `scratchpad/analyze.py` (stdlib only), outputs cached in
`scratchpad/results.json`.

Model being calibrated:

```
night_share = m * S_mail + (1 - m) * S_precinct
  m          = final mail share = final_vbm / final_total
  S_mail     = night_vbm / final_vbm      (fraction of mail ballots counted by night)
  S_precinct = night_eday / final_eday    (fraction of precinct/election-day ballots counted by night)
```

SF is the calibration county because it never adopted e-pollbooks / ASV / vote centers, processes
mail centrally, and publishes a per-release VBM/election-day split. That lets us read `S_mail` and
`S_precinct` straight off the ledger instead of inferring them.

---

## 1. Direct channel measurement (the core)

For every SF election whose night release AND final release both carry the VBM/election-day split
(n = 18, spanning 2015-11 through 2026-06), read `S_mail` and `S_precinct` directly.

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

**Distributions.** `S_mail`: median 0.534, range 0.365 (2020 primary) to 0.789 (2021 recall).
`S_precinct`: median 0.799, range 0.636 (2024 general) to 0.890 (2022 special). Precinct/election-day
ballots are counted roughly 0.80 by night; mail roughly 0.53. The gap `S_precinct - S_mail` is the
whole mechanism: mail is the slower channel, so shifting composition toward mail mechanically lowers
the night share.

**How S_mail moved.** Not monotone, because it is dominated by turnout context, not the calendar.
Two competing forces:
- *Same-day-received VBM grew* (drop-boxes, election-day mail drop-off), which pushes `S_mail` down.
  Visible in the primaries: 2016-06 0.603 -> 2018-06 0.482 -> 2020-03 0.365, and the recent
  presidential-cycle primaries stay low (2024-03 0.405, 2026-06 0.419).
- *The pandemic universal-mail era temporarily raised S_mail.* When SF mailed every registered voter
  a ballot weeks early (2020 general 0.782, 2021 recall 0.789, 2022 specials 0.71-0.78), a large
  share of mail arrived and was processed before polls closed, so `S_mail` spiked. This is an
  era artifact, not a return of fast mail counting.

Net: comparing like with like (November generals) `S_mail` = 0.541 (2016), 0.782 (2020, pandemic),
0.482 (2022), 0.558 (2024). Outside the pandemic year the general-election `S_mail` sits ~0.48-0.56
and has no strong trend; the fall is clearest in the primaries.

**Data-quality traps hit:**
- *Date-only timestamps (the important one).* The `era_b_tsv` rows for 2015-11 and 2016-06 are
  timestamped `T00:00:00` (date only). A naive `report_datetime <= E+1 06:00` filter lets the
  E+1-dated row (`2015-11-04T00:00:00 <= 2015-11-04T06:00`) slip in as a "night" release, even though
  its VBM count has already jumped from next-day processing. That inflated the night share by
  ~3-4 pp before I caught it. Fix applied in `analyze.py`: a `T00:00:00` row dated after E is
  next-day processing and is excluded. `elections.json` uses the same on-election-day rule, which is
  why my fixed reconstruction matches it (Section 2). Elections with real HH:MM:SS timestamps
  (2016-11 onward) are unaffected: their genuine post-midnight ~00:30 release is correctly election
  night.
- *No provisional residual.* For every one of the 18 elections `night_total == night_vbm + night_eday`
  and `final_total == final_vbm + final_eday` exactly (residual = 0 in both columns of `analyze.py`).
  SF folds provisional/election-day-conditional ballots into the election-day bucket, so there is no
  third channel leaking the identity. This is what makes the reconstruction in Section 2 exact.
- *Blank splits.* 2012-11 has only two archival rows and its night observation (2012-11-11) falls
  outside the E+1 cutoff, so it has no in-window night split and is excluded. 2019-11 has 3 of 13
  rows with blank splits, but its night and final releases both carry splits, so it survives.
- *Definition stability.* The VBM vs election-day definition is stable across the three parser eras
  (`era_b_tsv`, `era_c_xml`); the only discontinuity is the timestamp-precision one above.

---

## 2. Consistency check

Reconstruct `night_share = m*S_mail + (1-m)*S_precinct` and compare to `elections.json` `nightPct`.
Because SF has no provisional residual (Section 1), this is an identity and must match up to the
0.1 rounding baked into `nightPct`.

| date | reconstructed % | nightPct | diff |
|------|----------------:|---------:|-----:|
| 2015-11-03 | 65.13 | 65.1 | +0.03 |
| 2016-06-07 | 70.08 | 70.1 | -0.02 |
| 2016-11-08 | 66.15 | 66.1 | +0.05 |
| 2018-06-05 | 60.84 | 60.8 | +0.04 |
| 2020-03-03 | 47.40 | 47.4 | 0.00 |
| 2020-11-03 | 78.36 | 78.4 | -0.04 |
| 2022-11-08 | 51.02 | 51.0 | +0.02 |
| 2024-11-05 | 56.87 | 56.9 | -0.03 |
| 2026-06-02 | 46.07 | 46.1 | -0.03 |

(Full 18-row table in `results.json`.) Every `|diff| <= 0.05 pp`, i.e. pure rounding. The model is
arithmetically exact for SF; there is no provisional or "other" leakage to explain away. The two
rows that once looked off (2015-11 +4.31, 2016-06 +2.75) were the date-only-timestamp trap, not a
model failure; after the Section-1 fix they collapse to rounding.

---

## 3. Long-run corroboration: regress night_share on m

All SF elections in `elections.json` that carry both `nightPct` and `vbmShare` (n = 27, 1983-2026).
`vbmShare` is the final mail share `m`; only 1983 onward has it, so the pre-1964 night-floor
semantics never enter this regression (those rows have `vbmShare = null`). Simple OLS, stdlib.

Four of the 27 are flagged `nightPartial` (2000-12, 2008-02, 2008-06, and one more): their night
count is a documented floor, so their `night_share` is biased low and is not a true share. I report
with and without them.

| sample | n | slope | intercept | R^2 |
|--------|--:|------:|----------:|----:|
| all (incl. partial floors) | 27 | +0.022 | 0.638 | 0.001 |
| clean (partial floors excluded) | 23 | -0.196 | 0.816 | 0.069 |

- The all-sample slope is essentially zero (R^2 = 0.001): the partial floors, concentrated at
  moderate `m`, flatten it.
- The clean slope is **-0.196**: each +1.0 in mail share drops the night share by ~0.20. Classic OLS
  SE = 0.157; leave-one-election-out jackknife SE = 0.223, 95% CI on the slope
  **(-0.633, +0.241)** -> includes zero. R^2 = 0.069: `m` alone explains little of the
  cross-election variance in night share.

**Slope vs direct measurement.** The regression slope should approximate `S_mail - S_precinct`. Direct
measurement gives `S_mail - S_precinct` = 0.534 - 0.799 = **-0.265** (medians). The clean regression
slope **-0.196** is the same sign and the same rough magnitude - reassuring - but it is attenuated
toward zero and far too noisy to pin down. Why attenuated: in the SF cross-section `m` and `S_mail`
**co-move positively** (the high-mail elections - 2020 general, 2021 recall, 2022 specials - are
exactly the ones where mail arrived early and `S_mail` was high). That positive `m`-`S_mail`
correlation partly cancels the mechanical composition penalty, so the naive regression *understates*
it. The direct channel decomposition, which holds `S_mail` and `S_precinct` fixed and varies only
`m`, is the trustworthy estimate; the regression corroborates its sign and central tendency but
cannot stand alone.

---

## 4. Calibration deliverable: channel rates by era

SF-baseline channel rates (medians of the direct measurements), for use as the composition kernel.

| era | n | S_mail | S_precinct | S_precinct - S_mail |
|-----|--:|-------:|-----------:|--------------------:|
| pre-2016 | 1 | 0.524 | 0.858 | 0.334 |
| 2016-2020 | 7 | 0.485 | 0.800 | 0.315 |
| 2022+ | 10 | 0.606 | 0.778 | 0.172 |

(pre-2016 is a single election, 2015-11; treat it as indicative only. Means are close to medians:
2016-2020 S_mail mean 0.533, 2022+ S_mail mean 0.609.)

The `S_precinct - S_mail` gap **narrows over time**: from ~0.33 to ~0.17. Two reasons, both real:
`S_mail` rose in 2022+ (postmark-window extensions + universal mail moved more ballots into the
early-processed pile) and `S_precinct` fell (2024 general = 0.636; growing election-day/provisional
verification backlog). The composition kernel is therefore era-specific, not a constant.

**Composition-expected night-share change for a treated county:**

```
delta_expected = (m_post - m_pre) * (S_mail - S_precinct)
```

using the SF-baseline `(S_mail, S_precinct)` for the relevant era as the channel kernel, and the
treated county's own mail-share shift `(m_pre -> m_post)`. Because `S_mail < S_precinct`,
`delta_expected` is **negative** whenever mail share rises: composition alone *lowers* the
election-night share.

**Worked example, real SF numbers.** SF's own 2016 -> 2022 general-election shift:
`m` went 0.635 -> 0.885 (`Delta m = +0.250`), 2016-2020 kernel `S_mail - S_precinct = -0.315`.

```
delta_expected = 0.250 * (-0.315) = -0.079  ->  -7.9 pp
```

SF's actual night share fell 0.661 -> 0.510, i.e. **-15.1 pp**. Composition explains ~7.9 pp of that;
the remaining ~-7.2 pp is residual (here, SF's mail counting genuinely got slower per-ballot and
`S_precinct` fell too - SF had no speed-up technology to offset it). This is the decomposition the
panel wants to run on treated counties, with the residual read as "processing speedup" only for
counties that actually adopted the technology.

---

## Headline calibration (maintainer's requested form)

**"For every 10 percentage points of VBM share, the election-night tally share drops by X points."**

**(1) X from the long-run SF regression.** Clean OLS slope -0.196 -> `X = -10 * slope = +1.96 pp`
per 10 pp of mail share. 95% CI via leave-one-election-out **jackknife**: slope SE 0.223, so
`X = +1.96 pp, 95% CI (-2.41, +6.33)`. (Classic OLS SE gives a tighter but less honest
`(-1.12, +5.04)`; I report the jackknife as the headline because the sample is 23 heterogeneous
elections, not iid draws.) The interval includes zero: the regression alone cannot establish that
X differs from zero.

**(2) X implied by the direct channel measurement**, `X = 10 * (S_precinct - S_mail)`:

| era | X (pp per +10 pp mail) |
|-----|----------------------:|
| pre-2016 | +3.34 (n=1, indicative) |
| 2016-2020 | +3.15 |
| 2022+ | +1.72 |
| overall (median) | +2.65 |

**(3) Honesty box.** A single fixed X is **not** defensible. The direct measurement shows X drifting
from ~3.3 pp (pre-2016) to ~3.2 pp (2016-2020) to ~1.7 pp (2022+), a near-halving driven by
forces unrelated to any county's counting technology: statewide postmark-deadline extensions
(postmark+3 in 2015, postmark+7 in 2020) and the growth of early-returned universal mail both raised
`S_mail`, shrinking the `S_precinct - S_mail` gap and therefore X. The regression's single-number X
(+1.96 pp) sits inside the range the direct method spans but has a CI that swallows zero, so it
cannot arbitrate. The only honest statement is era-qualified: **X is about +3 pp per 10 pp of mail
share before 2022 and about +1.7 pp from 2022 on**, and the direction of change (X falling) is the
signal, not any single value. Use the 2022+ figure (+1.7 pp) for present-day treated-county work.

**(4) SF-only caveat.** This is one county's composition curve. SF processes 100% of its mail
centrally at a single facility and has no vote centers, so its `S_mail` reflects central-count mail
throughput. A VCA/vote-center county's late same-day drop-offs (ballots dropped at vote centers on
election day, opened days later) make its `S_mail` lower and more back-loaded than SF's for the same
`m`. Transporting SF's `S_mail` to those counties will therefore *understate* their composition
penalty and *overstate* the residual "speedup" attributed to their technology (Section 5 states the
bias direction per caveat). The calibration is a defensible first-order kernel, not a county-specific
truth.

---

## 5. Honest caveats (bias direction on the residual "speedup" estimate)

The residual is `speedup = observed_night_change - delta_expected`. If we mis-estimate
`delta_expected`, the error flows straight into the speedup.

1. **SF central mail processing may not transfer to VCA vote-center counties.** SF's `S_mail` is a
   central-count rate. Vote-center counties get more election-day/late mail drop-off that is opened
   days later, so their true `S_mail` is *lower* (more back-loaded) than SF's. Using SF's higher
   `S_mail` makes `S_mail - S_precinct` less negative than reality, so `|delta_expected|` is too
   small -> **residual speedup biased upward** (we credit technology for a composition drag we
   under-counted). Direction: **over-states speedup**.

2. **Late-arriving-VBM law changes moved S_mail statewide, for reasons unrelated to county tech.**
   Postmark+3 (2015) and postmark+7 (2020) pushed a larger share of mail past election night into the
   canvass, lowering `S_mail` over time - independent of e-pollbooks or ASV. If a county's pre/post
   windows straddle a law change, part of its `S_mail` shift (and thus `delta_expected`) is
   statewide-legal, not compositional or technological. Using a stale-era SF kernel across a law
   change mis-sizes `delta_expected`; because the laws *lowered* `S_mail` (bigger gap) in the earlier
   post-periods and SF's own 2022+ kernel already absorbs the later law, the sign depends on window
   placement. Direction: **ambiguous, window-dependent** - use the era-matched kernel to neutralize
   it, and never a pre-2015 kernel on a post-2020 comparison.

3. **The m-S_mail co-movement (from Section 3) is SF-specific.** In SF, high-mail elections were also
   early-processed-mail elections. A treated county without that correlation will have a more
   negative effective `S_mail - S_precinct` than SF's medians imply. Direction: SF kernel
   **under-states** the composition penalty -> **over-states speedup**.

4. **Turnout-context confounding.** `S_mail` swings with turnout magnitude (pandemic universal-mail
   spike to 0.79; high-turnout presidential drop to ~0.48). Matching a treated county's high-turnout
   general to SF's pandemic-era kernel would badly overstate `S_mail`. Direction: depends on match;
   mitigate by matching election type and turnout regime, not just year.

Two of four caveats push the residual speedup **upward**, so the SF-calibrated composition
decomposition most likely **over-credits** counting technology. That matters directly for the
companion panel, whose e-pollbook headline (+4.76 pp) is already smaller than its own placebo
(+10.23 pp): a composition kernel that over-states speedup would make a weak technology effect look
stronger than it is. Lean conservative.

---

## 6. Application stub (SUPERSEDED by Section 7 - kept for the record)

> **Superseded 2026-07-10.** The SoS sweep has since completed; Section 7 below redoes this with
> real per-county mail shares from `county_vbm_share_draft.csv`. The San Diego example here used a
> placeholder `m` and is retained only to show the original wiring.

The parallel sweep file `scratchpad/county_vbm_share_draft.csv` does **not exist yet** at run time
(the `vbm-sweep/` directory holds only source PDFs/TXTs, no compiled per-county `m` series). So no
real treated-county `delta_expected` can be computed. The machinery is ready; below is the wiring
plus one fully-labeled *illustrative* example so the arithmetic is verifiable the moment `m` lands.

Pinned per-county DiD effects (from committed `docs/analysis/2026-07-10-tech-effect-estimate.md`
at SHA 1cd1f88; these are the panel's matched-years, jackknife-inference effects):
- Headline e-pollbook effect: **+4.76 pp** (95% CI -9.32, +18.84); placebo +10.23 pp (larger than
  the headline - the panel itself reads the effect as "not yet distinguishable from noise").
- Per county: **San Diego +28.20**, Fresno +13.12, Sacramento **-8.79**; 2018 cohort -5.44,
  2020 cohort +11.66, 2022+ cohort (San Diego alone) +28.20.

Residual decomposition to run per county once `m` arrives:

```
delta_expected = (m_post - m_pre) * (S_mail - S_precinct)   # SF era kernel, use 2022+: -0.172
residual_speedup = DiD_effect - delta_expected
```

**Illustrative only (hypothetical m, NOT real - flagged):** San Diego, 2018 -> 2022, DiD +28.20 pp.
*Suppose* its mail share rose `m: 0.55 -> 0.80` (`Delta m = +0.25`, placeholder pending the sweep).
Using the 2022+ SF kernel `S_mail - S_precinct = -0.172`:

```
delta_expected   = 0.25 * (-0.172) = -0.043  ->  -4.3 pp   (composition alone lowers night share)
residual_speedup = +28.20 - (-4.3) = +32.5 pp
```

Reading (preliminary): composition would have *dragged* San Diego's night share down ~4 pp, so the
observed +28 pp rise implies ~+32 pp of processing speedup - larger than the raw DiD, because the
county was simultaneously getting more mail (which should have slowed it). But: San Diego is the
panel's flagged positive outlier and the entire 2022+ "cohort," `m` here is a placeholder, and the
SF kernel over-states speedup for vote-center counties (Caveat 1). Every number in this section is
preliminary and must be re-run against real `county_vbm_share_draft.csv` rows with an era- and
type-matched kernel.

---

## 7. Application with real per-county mail shares (redo of Section 6)

The parallel SoS sweep completed: `scratchpad/county_vbm_share_draft.csv` (228 rows, 12 elections
x 19 counties, certified SoS voter-participation splits). All numbers below computed by
`scratchpad/apply_real_m.py`, cached in `scratchpad/apply_real_m.json`. Still preliminary: the DiD
effects themselves are pinned from `docs/analysis/2026-07-10-tech-effect-estimate.md` @ 1cd1f88,
whose own headline is smaller than its placebo.

Method, per identified treated county (all 10 from the pinned per-county DiD table):
- Pre/post windows = the county's actual panel cells: general-election years with a comparable,
  non-null night point, 2020 excluded, split at the e-pollbook adoption year (post inclusive),
  exactly as the estimator's matched-cells design defines them (from pinned `county_night.json`).
- `m_pre`, `m_post` = means of the county's real SoS `vbm_share_pct/100` over those general years.
- Kernel = SF `S_mail - S_precinct`, era-matched per post year and averaged over the post window:
  -0.315 (2016-2020 kernel) for post years before 2022, -0.172 (2022+ kernel) for 2022 on. Counties
  whose post window is all 2022+ get -0.172; the 2018 adopters (post = 2018, 2022, 2024) get the
  mix -0.220 (Nevada, post = 2018, 2022: -0.243). A strict binary era assignment instead of the mix
  moves no residual by more than 1.4 pp and the aggregate by 0.3 pp.
- `delta_expected = (m_post - m_pre) * kernel`; `residual = DiD - delta_expected` (the coordinator's
  requested form).

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

(Window details: San Diego pre = {2018}, post = {2022, 2024}; the 2020 adopters pre = {2012-2018},
post = {2022, 2024} (Fresno pre = {2016}, post = {2024} only); the 2018 adopters pre = {2012-2016},
post = {2018, 2022, 2024} (Sacramento pre = {2012, 2014}, Madera pre = {2016}; Nevada post =
{2018, 2022}, its 2024 point is a flagged ceiling). No sweep row was missing for any window year.)

**Aggregate.** Mean raw DiD = **+4.76 pp**; mean composition-expected change = **-4.32 pp**; mean
residual = **+9.08 pp**. Every treated county's mail share rose (delta m from +0.05 Napa to +0.39
LA), so composition alone should have *lowered* every night share; netting that out nearly doubles
the technology-attributable residual.

**A double-counting warning on that headline.** The DiD effects already net out the five control
counties, and the controls' mail shares rose too (control-matched mean delta m = +0.13 to +0.20 per
window, from the same sweep file: the VCA/mail shift was statewide). Subtracting the treated
county's *full* composition drag from a control-netted DiD therefore counts the statewide part of
the shift twice. The cleaner form nets compositions first:
`delta_expected_net = (dm_treated - dm_control) * kernel`, giving a mean `delta_expected_net` of
only **-1.03 pp** and a mean net residual of **+5.79 pp** (per-county values in
`apply_real_m.json`; e.g. San Diego +28.71, LA +10.24, Madera -7.45). The honest range for the
composition-adjusted headline is therefore **+5.8 to +9.1 pp**, depending on whether the control
group's own composition shift is credited to the DiD or to the kernel.

**Does composition adjustment move the headline materially?** Yes in level, no in verdict. It
roughly doubles the point estimate (+4.76 raw -> +9.08 gross-adjusted, +5.79 net-adjusted) and it
tightens the story qualitatively: the 2018 cohort's puzzling negative effects become *more* negative
(they adopted e-pollbooks and still fell behind even after excusing their composition drag), while
the 2020/2022 cohorts' positives grow. But the adjustment is a near-uniform ~+3-4 pp shift (gross)
across counties, so it cannot rescue the design's identification problem: the placebo (+10.23 pp)
still exceeds even the adjusted headline, the county-level spread (37 pp raw) is untouched, and the
SF central-count kernel over-states the residual for vote-center counties (Caveat 1). Preliminary
throughout; re-run when the panel's DiD is re-estimated.

---

## Files

- This report: `scratchpad/sf-composition-curve.md`
- Analysis code (stdlib, re-runnable): `scratchpad/analyze.py`, `scratchpad/apply_real_m.py`
- Cached numeric results: `scratchpad/results.json`, `scratchpad/apply_real_m.json`
- Sweep input (real per-county m): `scratchpad/county_vbm_share_draft.csv`
- Pinned inputs (SHA 1cd1f88): `scratchpad/pin/` (now also `county_night.json`,
  `estimate_tech_effect.py`)
