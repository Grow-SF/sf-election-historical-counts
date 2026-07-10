# Robustness readout: Task 7 (tech-effect estimator), 4-control snapshot

**Pinned commit:** `1ec5652` (Task 4 integrator commit for mendocino-ca, per
`.superpowers/sdd/progress.md`: "Task 4 integrator DONE mendocino-ca (commit
1ec5652)... Estimator: +4.76 se 7.17 n_controls 4"). Data file pinned to
`county_night_4ctrl.json` via:

```bash
git -C /Users/sbuss/workspace/sf-election-count/.claude/worktrees/cozy-leaping-wreath \
  show 1ec5652:packages/data/county_night.json > county_night_4ctrl.json
```

This is the same method the prior (2-control) readout used, just re-pinned
to a later commit. All computation below uses the repo's own estimator
(`scripts/research/estimate_tech_effect.py`) imported, not reimplemented:

```python
import sys; sys.path.insert(0, "/Users/sbuss/workspace/sf-election-count/.claude/worktrees/cozy-leaping-wreath/scripts/research")
from estimate_tech_effect import load_panel, estimate, jackknife, placebo, _by_slug, _adoption_year
panel = load_panel("county_night_4ctrl.json")
```

The panel has **17 jurisdictions**: 13 treated California counties and now
**4 controls** (`san-francisco-ca`, `lake-ca`, `del-norte-ca`,
`mendocino-ca`). Tehama and Colusa are still not integrated (Colusa
contributes 0 night points anyway per progress.md; Tehama integration is
"next" as of this pin). `EXCLUDED_YEARS = {2020}` still drops all 2020
points regardless of adoption status.

---

## 1. Headline table

```python
for mech in ["any", "epb", "asv"]:
    est = estimate(panel, mech)
    jk = jackknife(panel, mech)
    print(mech, jk["effect"], jk["se"], jk["ci95"], est["n_treated"], est["n_controls"])
pb = placebo(panel)
```

| cut | effect (pp) | se | ci95 | n_treated | n_controls |
|---|---|---|---|---|---|
| any | 4.76 | 7.17 | (-9.29, 18.82) | 10 | 4 |
| epb | 4.76 | 7.17 | (-9.29, 18.82) | 10 | 4 |
| asv | 15.71 | 6.92 | (2.14, 29.28) | 4 | 4 |
| placebo (2 fake-adopter controls vs. 2 real controls) | 10.23 | n/a (single jackknife rep n=1) | n/a | 2 fake-treated | 2 |

`any` and `epb` are still **numerically identical, county-for-county** , 
confirmed by a direct dict-equality check on the per-county results, not
just eyeballing the aggregate. The mechanism is unchanged from the 2-control
readout: every treated county in this panel has `epb_year <= asv_year` (or
no `asv_year`), so `min(epb_year, asv_year)` always resolves to the EPB
year. "any" is still redundant with "epb," not a broader cut of it.

The same three treated counties are still dropped from the `any`/`epb` cut
for lacking a pre- or post-adoption point: `placer-ca` (2024 adoption, no
post point yet), `riverside-ca` (2022 adoption is itself the only year, no
pre point), `san-bernardino-ca` (2020 adoption, only a 2024 point, no pre
point). Adding Del Norte and Mendocino did not fill these gaps, they are
treated-county gaps, not control-county gaps, and doubling the control count
was never going to touch them.

**The `asv` CI now excludes zero** (2.14, 29.28), which it did not at 2
controls (-3.49, 41.72). Section 4 explains why this should not be read as
new-found significance, the same mechanism confound from the 2-control
readout is untouched, and the placebo (below) got *worse*, not better.

---

## 2. Leave-one-out sensitivity (aggregate `any` effect, one county dropped at a time)

```python
full = estimate(panel, "any")
for drop in sorted({r["slug"] for r in panel}):
    sub = [r for r in panel if r["slug"] != drop]
    e = estimate(sub, "any")
    print(drop, e["effect"], e["effect"] - full["effect"])
```

Full effect = 4.7635.

| county dropped | effect w/ drop | delta from full | control? |
|---|---|---|---|
| **mendocino-ca** | 9.4523 | **+4.6887** | control |
| **lake-ca** | 0.8562 | **-3.9073** | control |
| san-diego-ca | 2.1591 | -2.6045 | treated |
| madera-ca | 6.3443 | +1.5808 | treated |
| sacramento-ca | 6.2695 | +1.5059 | treated |
| san-mateo-ca | 6.0757 | +1.3122 | treated |
| santa-clara-ca | 3.8089 | -0.9546 | treated |
| orange-ca | 3.8262 | -0.9374 | treated |
| fresno-ca | 3.8347 | -0.9288 | treated |
| del-norte-ca | 4.0016 | -0.7619 | control |
| napa-ca | 5.5020 | +0.7385 | treated |
| nevada-ca | 5.2962 | +0.5327 | treated |
| los-angeles-ca | 4.5187 | -0.2449 | treated |
| san-francisco-ca | 4.7440 | -0.0195 | control |
| placer-ca / riverside-ca / san-bernardino-ca | 4.7635 | 0.0000 | not in the estimated set |

### How much did 4 controls stabilize it?

- **Biggest single-drop swing:** was **+-5.83 pp** at 2 controls (dropping
  either SF or Lake, symmetric because with 2 controls dropping one leaves
  the other as sole control). At 4 controls the biggest swing is
  **mendocino-ca, +4.69 pp**, a **19.6% reduction** in the size of the
  single worst-case control-drop swing (5.83 -> 4.69).
- **Range across control-only drops** (max control-drop effect minus min
  control-drop effect, the spread of "what if you only trusted 3 of the 4
  controls"): was **11.67 pp** at 2 controls (16.49 vs. 4.82, the only two
  possible single-control readings). At 4 controls it is **8.60 pp**
  (9.4523 vs. 0.8562), a **26.3% reduction**.
- **The identity of the biggest mover changed.** At 2 controls, San
  Francisco was the single biggest mover in the whole panel by a wide
  margin (+5.83, more than double the next-largest swing). At 4 controls,
  **San Francisco is now the *smallest* mover in the entire table**
  (-0.02, essentially inert), because SF's leave-one-out effect no longer
  determines the control baseline alone; 3 other controls now anchor it.
  Lake and Mendocino (the two most volatile controls, see Section 5) have
  taken over as the movers, and San Diego (a treated county, -2.60) is now
  the third-largest mover in the panel, closer in size to a "normal" county
  swing than to a control-driven swing.
- **Bottom line on stabilization:** real but partial. The worst-case single
  swing shrank about a fifth and the control-only spread shrank about a
  quarter, and the previously-dominant "SF or Lake, take your pick"
  problem is gone. But the mechanism did not disappear, it moved: now it's
  "Mendocino or Lake, take your pick" (a 8.60-pp spread that is *still
  bigger than the full-panel headline effect itself*, 4.76). Doubling
  n_controls from 2 to 4 shrank but did not solve the core problem
  identified at 2 controls.

---

## 3. Cohort cuts (by treated county's earliest adoption year, `any` mechanism)

```python
groups = _by_slug(panel)
treated_adopt = {slug: _adoption_year(rows, "any")
                 for slug, rows in groups.items() if not rows[0]["control"]}
for name, slugs in cohorts.items():
    sub = [r for r in panel if r["control"] or r["slug"] in slugs]
    print(name, jackknife(sub, "any"), estimate(sub, "any")["n_treated"])
```

| cohort | effect (pp) | se | ci95 | n_treated (identified) | n_controls | 2-control effect (for comparison) |
|---|---|---|---|---|---|---|
| 2018 adopters (VCA-confounded) | **-5.44** | 5.93 | (-17.07, 6.18) | 5 (madera, napa, nevada, sacramento, san-mateo) | 4 | +1.05 |
| 2020 adopters (VCA-confounded) | **11.66** | 6.88 | (-1.82, 25.14) | 4 of 5 (san-bernardino dropped, no pre point) | 4 | +17.56 |
| 2022+ adopters (clean of VCA) | **28.20** | 5.68 | (17.08, 39.33) | **1 of 3** (only san-diego-ca; placer/riverside still dropped, no pre or post point) | 4 | +31.06 |

The cohort-membership rosters are unchanged from the 2-control readout
(same treated counties, same adoption years, same identification gaps for
placer/riverside/san-bernardino), only the control side of each estimate
changed. What that control-side change did to each cohort:

- **The 2018 cohort flipped sign**: +1.05 (2 controls) -> **-5.44** (4
  controls). This is the single biggest qualitative change in this readout.
  The 2018 cohort is entirely VCA-confounded counties (Madera, Napa,
  Nevada, Sacramento, San Mateo); its effect is not "essentially zero"
  anymore, it is now *negative*, i.e., these five counties' election-night
  share grew *more slowly* than the 4-control baseline over their
  pre/post windows. Still statistically indistinguishable from zero (CI
  crosses zero, and comfortably), but the point estimate moved 6.5 points
  and crossed sign.
- **The 2020 cohort shrank**: 17.56 -> 11.66, roughly a third smaller, and
  its CI now crosses zero more comfortably in the negative direction
  (-1.82 vs. -4.30 before, actually a modestly *tighter* lower bound, SE
  fell from 11.16 to 6.88).
- **The 2022+ cohort is still a single county** (san-diego-ca) wearing a
  cohort label, unchanged from the 2-control readout's central caveat.
  Its point estimate fell somewhat (31.06 -> 28.20) but its CI still
  excludes zero (17.08, 39.33), this remains an n=1 result, not
  evidence of a real "2022+ adopter cohort effect."

**Conclusion for this section: the headline instability across cohorts
persists at 4 controls and, if anything, got more dramatic**, the 2018
cohort didn't just stay near zero, it crossed from positive to negative.
This is the opposite of what you'd hope "more controls" would do to a
robustness readout; it's evidence the panel's remaining instability isn't
purely a small-n-controls artifact, since adding 2 more controls changed a
sign, not just tightened a CI around the same number.

---

## 4. Mechanism disentangling (asv panel)

Treated counties identified under the `asv` mechanism (unchanged roster
from the 2-control readout, this is a treated-side identification issue,
untouched by adding controls):

| county | epb year | asv year | asv "pre" years | asv "post" years | asv effect (4 ctrl) | epb effect, same county (4 ctrl) |
|---|---|---|---|---|---|---|
| fresno-ca | 2020 | 2020 | 2016 | 2024 | 13.12 | 13.12 (identical) |
| los-angeles-ca | 2020 | 2020 | 2012,2014,2016,2018 | 2022,2024 | 6.97 | 6.97 (identical) |
| nevada-ca | 2018 | 2022 | 2012,2014,2016,2018 | 2022 | 16.93 | -0.03 |
| san-diego-ca | 2022 | 2024 | 2018,2022 | 2024 | 25.83 | 28.20 |

Same structural confound as before: `fresno-ca` and `los-angeles-ca`
adopted EPB and ASV in the identical year, so their asv effects are still
bit-for-bit identical to their epb effects (still zero information to
separate the two mechanisms for these two counties). `nevada-ca`'s asv
"pre" window is still mostly pre-EPB (3 of 4 years). `san-diego-ca`'s asv
"pre" window is still {2018, 2022}, one pre-EPB year and one transitional
year.

What changed numerically: nevada-ca's asv effect moved from 20.19 (2
controls) to 16.93 (4 controls), and interestingly now diverges sharply
from its own epb effect (-0.03), a bigger epb/asv gap for this one county
than existed before, though this reflects the new control baseline, not
new treated-county data.

**Bottom line, unchanged in substance:** none of the four asv-cohort
counties gives a clean, EPB-isolated ASV-only estimate. The asv headline
moved from 19.11 to 15.71 and its CI now excludes zero, but the underlying
identification problem (2 of 4 counties are pure EPB+ASV bundles, a third
is mostly pre-EPB in its own "pre" window) is completely unaffected by
control-count. A tighter, sign-flipped CI riding on the same confounded
identification is not more trustworthy than a wide one was.

---

## 5. Control heterogeneity, year-by-year (now 4 series)

```python
controls = ['san-francisco-ca','lake-ca','del-norte-ca','mendocino-ca']
```

| year | san-francisco-ca | lake-ca | del-norte-ca | mendocino-ca | spread (max-min) | mean | stdev |
|---|---|---|---|---|---|---|---|
| 2012 | 71.40 | 70.18 | -- | -- | 1.22 | 70.79 | 0.86 |
| 2014 | 70.30 | 69.72 | 89.18 | 45.58 | 43.60 | 68.69 | 17.87 |
| 2016 | 66.10 | 53.75 | 83.30 | 31.07 | 52.23 | 58.55 | 21.97 |
| 2018 | 59.30 | 63.00 | 84.45 | 46.57 | 37.88 | 63.33 | 15.74 |
| 2022 | 51.00 | 38.51 | 74.70 | -- (null) | 36.19 | 54.74 | 18.38 |
| 2024 | 56.90 | 29.34 | 62.94 | 39.19 | 33.60 | 47.09 | 15.54 |

Del Norte and Mendocino are **very different kinds of counties from SF and
Lake in raw level** (Del Norte plateaus in the 60s-80s%, Mendocino in the
30s-40s%, reflecting real differences in rural VBM adoption timing and
processing capacity, not noise), the level spread (33-52 points per year)
is large but is not itself the relevant DiD heterogeneity measure, since the
estimator differences pre/post *within* each control county before
averaging across controls. The relevant measure is the spread of each
control's own **pre-to-post delta**, which is what feeds `_control_change`.

Year-over-year deltas per control:

```
san-francisco-ca: 2014 -1.10, 2016 -4.20, 2018 -6.80, 2022 -8.30, 2024 +5.90
lake-ca:          2014 -0.46, 2016 -15.97, 2018 +9.25, 2022 -24.49, 2024 -9.17
del-norte-ca:     2016 -5.88, 2018 +1.15, 2022 -9.75, 2024 -11.76
mendocino-ca:     2016 -14.51, 2018 +15.50, 2024 -7.38
```

Pairwise divergence (mean and sd of the year-matched difference between
every pair of controls, all 6 pairs):

| pair | mean diff | sd diff |
|---|---|---|
| sf vs lake | 8.42 | 11.48 |
| sf vs del-norte | -18.19 | 7.55 |
| sf vs mendocino | 22.55 | 9.67 |
| lake vs del-norte | -28.05 | 7.36 |
| lake vs mendocino | 13.35 | 15.82 |
| del-norte vs mendocino | 39.37 | 11.96 |

Two things stand out:

1. **Lake remains the most volatile control** (largest single yoy swings:
   -24.49 in 2022, -15.97 in 2016), its documented no-tech collapse from
   2018 onward is unchanged by adding Del Norte/Mendocino and continues to
   drive a disproportionate share of every pairwise sd involving it
   (lake-vs-mendocino sd 15.82 is the largest of the 6 pairs).
2. **Adding two more controls added heterogeneity in absolute level, not
   necessarily in trend.** Del Norte is the most stable of the four in
   yoy terms (max swing -11.76) but sits at a level 15-35 points above the
   other three; Mendocino swung +15.50 in a single cycle (2018), the
   second-largest single-year swing of any control after Lake's 2022 drop.

### Placebo, traced

```python
pb = placebo(panel)
# fake_adopters = sorted({'del-norte-ca','lake-ca','mendocino-ca','san-francisco-ca'})[::2]
#              = ['del-norte-ca', 'mendocino-ca']   (indices 0, 2 of the sorted slug list)
# real controls remaining = lake-ca, san-francisco-ca
```

del-norte-ca (fake 2018 adopter): pre(2014,16)=86.24 -> post(2018,22,24)=74.03, delta=-12.21
mendocino-ca (fake 2018 adopter): pre(2014,16)=38.325 -> post(2018,24; 2022 null)=42.88, delta=+4.555
real-control change (mean of lake, sf, computed separately per fake county's own pre/post window):
  for del-norte's window: lake delta=-18.118, sf delta=-12.467, mean=-15.29 -> effect = -12.21-(-15.29) = **+3.08**
  for mendocino's window: lake delta=-15.565, sf delta=-10.10, mean=-12.83 -> effect = 4.555-(-12.83) = **+17.39**
aggregate placebo = mean(3.08, 17.39) = **10.23**

**This is the most important "what changed" finding in the whole readout.**
The placebo did not shrink toward zero, which is what a working design
should do as n_controls grows. It got **larger in magnitude and flipped
sign**: -7.40 (2 controls) -> **+10.23** (4 controls). Tracing why: the new
placebo's two "fake adopters" are Del Norte and Mendocino, and Del Norte's
own pre/post delta (-12.21) is *smaller in magnitude* than the two real
controls' average delta (-15.29) it's being compared against, producing a
small positive spurious effect (+3.08), but Mendocino's delta (+4.555, an
actual *increase*, driven by its 2018 yoy jump of +15.50) is being compared
against a real-control average that's still declining (-12.83), producing a
large positive spurious effect (+17.39) that has nothing to do with tech
adoption (Mendocino never adopted either mechanism). The aggregate placebo
is dragged up by Mendocino's idiosyncratic 2018 spike the same way the
2-control placebo was dragged down by Lake's 2022/2024 collapse, this is
the same underlying phenomenon (a "never-adopter" control county having a
large tech-unrelated swing in some year) recurring with a different
county in the driver's seat.

In magnitude, +10.23 is now **larger than the `any`/`epb` headline itself**
(4.76) and about two-thirds of the `asv` headline (15.71), i.e. the
placebo-implied noise floor is now *bigger relative to the headline* than
it was at 2 controls (where -7.40 was about 70% of the any/epb headline
and 39% of the asv headline). Doubling the controls made this specific
diagnostic look worse, not better.

---

## 6. What changed vs. the 2-control readout

| metric | 2 controls | 4 controls | direction |
|---|---|---|---|
| any/epb headline effect | 10.65 | 4.76 | fell by more than half |
| any/epb 95% CI | (-6.57, 27.87) | (-9.29, 18.82) | still crosses zero, shifted down |
| asv headline effect | 19.11 | 15.71 | fell, modestly |
| asv 95% CI | (-3.49, 41.72) | **(2.14, 29.28)** | **now excludes zero** |
| placebo effect | -7.40 | **+10.23** | **grew in magnitude, flipped sign** |
| biggest single control-drop LOO swing | +-5.83 | +4.69 | shrank ~20% |
| control-drop LOO range | 11.67 | 8.60 | shrank ~26% |
| SF's own LOO swing | +5.83 (largest in panel) | -0.02 (smallest in panel) | SF is no longer load-bearing |
| 2018-cohort effect | +1.05 | **-5.44** | crossed sign |
| 2020-cohort effect | +17.56 | 11.66 | fell ~1/3 |
| 2022+-cohort effect (n=1, san-diego only) | 31.06 | 28.20 | fell modestly, still n=1 |

Net read: adding Del Norte and Mendocino **did** partially solve the
specific "SF-or-Lake, take your pick" problem that dominated the 2-control
readout's Section 2 and Section 5, SF's leave-one-out influence collapsed
to near-zero, and the worst-case control-drop swing and range both
shrank meaningfully. But it did **not** solve the design's core problem,
and by two measures (placebo magnitude, 2018-cohort sign flip) it made the
readout's honesty checks look *less* reassuring, not more. The headline
`any`/`epb` number more than halved (10.65 -> 4.76) purely from adding two
more never-adopter counties whose own pre/post trends (Del Norte declining
moderately, Mendocino swinging up in 2018) happened to shift the control
baseline, which is itself direct evidence that this design remains
sensitive to *which* handful of small rural counties you happen to have
recovered data for, not just *how many*.

---

## 7. Honest bottom line

**What the data now supports:** a positive but small, still statistically
insignificant (CI crosses zero) association between EPB/"any" adoption and
a larger night-of share of the vote being counted, roughly half the size of
what the 2-control readout suggested (4.76 vs. 10.65 pp). The `asv` cut's
CI now excludes zero (2.14, 29.28), but this should not be read as
newly-credible evidence: it rests on the same 4-county, half-confounded
identification set as before (2 of 4 counties are pure EPB+ASV bundles),
and the placebo check, which should be the first thing you consult before
trusting a tightened CI, got *worse* in exactly this snapshot, not better.
Given a placebo of +10.23 (bigger than the any/epb headline and comparable
to a third of the asv headline), no CI produced by this design should be
taken as excluding zero in a load-bearing way yet.

**What changed for the better:** the previous readout's single biggest
mechanical weakness, an aggregate estimate that was, almost by
construction, a coin-flip between "trust SF" (16.49) or "trust Lake"
(4.82), is gone. San Francisco's leave-one-out influence fell from the
largest in the panel to the smallest. The worst-case control-drop swing and
range both meaningfully narrowed (roughly 20% and 26% respectively).

**Biggest remaining threats, in order:**

1. **The placebo is worse, not better.** +10.23 pp of spurious effect from
   two never-adopter counties with a fake 2018 "adoption" is larger in
   magnitude than the real any/epb headline. Until the placebo is small
   relative to the headline, none of the point estimates in Section 1
   should be reported without this caveat attached.
2. **Del Norte and Mendocino are individually as influential as SF and
   Lake were.** Adding controls did not average out idiosyncrasy, it just
   redistributed which 1-of-4 counties dominates the leave-one-out swing
   (Mendocino, +4.69) and which drags it the other way (Lake, -3.91). A
   4-control panel where one drop still swings the headline by ~4.7 points
   against a headline of 4.76 points is not yet a stable design.
3. **The cohort instability got more dramatic, not less.** The 2018 cohort
   (VCA-confounded, 5 counties) crossed from a near-zero positive estimate
   to a moderately-sized negative one purely from the control-side change.
   A robustness check that flips sign on a large sub-cohort when you add
   two controls is evidence the underlying design, not just the control
   count, needs more work.
4. **The mechanism confound (EPB vs. ASV) is completely untouched.** It's
   a treated-side identification problem (which counties adopted EPB and
   ASV in the same vs. different years), and no number of additional
   control counties can fix it. Two of the four asv-identified counties
   are still indistinguishable EPB+ASV bundles.
5. **Treated-county gaps are also untouched.** placer-ca, riverside-ca,
   and san-bernardino-ca remain unidentified under `any`/`epb` for lack of
   a pre- or post-adoption observation; the 2022+ cohort remains an n=1
   (san-diego-ca) result dressed as a 3-county cohort.

Adding Tehama (next in the integration queue per `progress.md`) would grow
n_controls to 5 but contributes only 2 election-night points (2022, 2024)
per the dossier notes, so it is unlikely to materially change any of the
above on its own; Colusa contributes 0 night points and would only grow
n_controls nominally, without adding any pre/post information. Neither
remaining integration looks likely, by itself, to resolve threats 1-4
above; those need either materially more controls with less individual
influence, or a design change (e.g., a matched-pair or regression-based
approach that down-weights any single county's idiosyncratic swing) rather
than sheer control-count growth.
