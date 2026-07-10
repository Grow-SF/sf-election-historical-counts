# Robustness readout: Task 7 (tech-effect estimator), pinned snapshot

**Pinned commit:** `d7af5a504d8c54e4d523e0d1fdad36234f248cee` (HEAD of
`.claude/worktrees/cozy-leaping-wreath` at the time this readout started).
Data file pinned to `county_night_pinned.json` via:

```bash
git -C /Users/sbuss/workspace/sf-election-count/.claude/worktrees/cozy-leaping-wreath \
  show HEAD:packages/data/county_night.json > county_night_pinned.json
```

All computation below uses the repo's own estimator
(`scripts/research/estimate_tech_effect.py`) imported, not reimplemented:

```python
import sys; sys.path.insert(0, "/Users/sbuss/workspace/sf-election-count/.claude/worktrees/cozy-leaping-wreath/scripts/research")
from estimate_tech_effect import load_panel, estimate, jackknife, placebo, scenario
panel = load_panel("county_night_pinned.json")
```

The panel has **15 jurisdictions** in the pinned snapshot: 13 treated
California counties and **only 2 controls** (`san-francisco-ca`,
`lake-ca`). Del Norte, Mendocino and Tehama are not present yet (matches
the "pending integrations" note in the memory file). `EXCLUDED_YEARS =
{2020}` in the estimator drops all 2020 points regardless of adoption
status (this removes the Fresno/LA 2020-adoption-year row entirely from
both pre and post sets for those counties).

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
| any | 10.65 | 8.79 | (-6.57, 27.87) | 10 | 2 |
| epb | 10.65 | 8.79 | (-6.57, 27.87) | 10 | 2 |
| asv | 19.11 | 11.53 | (-3.49, 41.72) | 4 | 2 |
| placebo (fake-adopter, controls only) | -7.40 | n/a (single jackknife rep n=1) | n/a | 1 fake-treated | 1 |

**Important finding, not previously flagged:** in this snapshot `any` and
`epb` are **numerically identical in every county and in aggregate**.
That's not a coincidence of rounding — `_adoption_year(mechanism="any")`
takes `min(epb_year, asv_year)`, and in every treated county that
survives the pre/post filter, `epb_year <= asv_year` (or `asv_year` is
`None`). So "any" never actually picks up an ASV-led adoption; it
collapses to "epb" every time. The "any" row in the findings doc is
currently redundant with "epb," not a broader/looser cut of it.

None of the three CIs exclude zero. n_controls=2 throughout (this
drives most of what follows).

Three treated counties are dropped from the `any`/`epb` cut entirely
because they lack either a pre- or a post-adoption observation in the
panel: `placer-ca` (only 2014/2016, both pre-2024 adoption, no post
point yet), `riverside-ca` (only 2022, which is itself the adoption
year — no pre point), `san-bernardino-ca` (only 2024, adopted 2020 — no
pre point).

---

## 2. Leave-one-out sensitivity (aggregate `any` effect, one county dropped at a time)

```python
full = estimate(panel, "any")
for drop in sorted({r["slug"] for r in panel}):
    sub = [r for r in panel if r["slug"] != drop]
    e = estimate(sub, "any")
    print(drop, e["effect"], e["effect"] - full["effect"])
```

Full effect = 10.6537.

| county dropped | effect w/ drop | delta from full |
|---|---|---|
| **san-francisco-ca** (control) | 16.4854 | **+5.8317** |
| **lake-ca** (control) | 4.8220 | **-5.8317** |
| san-diego-ca (treated) | 8.3866 | -2.2671 |
| sacramento-ca (treated) | 12.1586 | +1.5049 |
| san-mateo-ca (treated) | 11.8756 | +1.2219 |
| madera-ca (treated) | 12.2489 | +1.5952 |
| napa-ca (treated) | 11.3019 | +0.6482 |
| nevada-ca (treated) | 11.0216 | +0.3679 |
| fresno-ca (treated) | 9.7858 | -0.8679 |
| los-angeles-ca (treated) | 10.3868 | -0.2669 |
| orange-ca (treated) | 9.6943 | -0.9594 |
| santa-clara-ca (treated) | 9.6770 | -0.9767 |
| placer-ca / riverside-ca / san-bernardino-ca | 10.6537 | 0.0000 (not in the estimated set to begin with) |

**By far the two biggest movers are the two control counties**, and they
move the estimate by exactly equal and opposite amounts (+5.83 / -5.83).
That's mechanical, not a coincidence: with only 2 controls, dropping
either one leaves the *other* as the sole determinant of every treated
county's control-adjustment, so the swing is just "effect computed
against san-francisco-ca alone" (16.49) vs. "effect computed against
lake-ca alone" (4.82) — an 11.7-point range depending on which single
control county you'd trust if you had to pick one. Dropping `lake-ca`
(its 2022/2024 collapse, see Section 5) pulls the aggregate estimate
*down* to 4.82 because losing lake removes the low control-mean that
was making the treated-county deltas look relatively large. Dropping
`san-diego-ca` (the positive outlier, treated) is the biggest mover
among treated counties (-2.27) but is an order of magnitude smaller
than either control swing.

---

## 3. Cohort cuts (by treated county's earliest adoption year, `any` mechanism)

```python
groups = _by_slug(panel)
treated_adopt = {slug: _adoption_year(rows, "any")
                 for slug, rows in groups.items() if not rows[0]["control"]}
# 2018 adopters: madera, napa, nevada, sacramento, san-mateo
# 2020 adopters: fresno, los-angeles, orange, san-bernardino, santa-clara
# 2022+ adopters: placer, riverside, san-diego
for name, slugs in cohorts.items():
    sub = [r for r in panel if r["control"] or r["slug"] in slugs]
    print(name, jackknife(sub, "any"), estimate(sub, "any")["n_treated"])
```

| cohort | effect (pp) | se | ci95 | n_treated (identified) | n_controls |
|---|---|---|---|---|---|
| 2018 adopters (VCA-confounded) | **1.05** | 4.02 | (-6.83, 8.92) | 5 (madera, napa, nevada, sacramento, san-mateo) | 2 |
| 2020 adopters (VCA-confounded) | **17.56** | 11.16 | (-4.30, 39.43) | 4 of 5 (san-bernardino dropped, no pre point) | 2 |
| 2022+ adopters (clean of VCA) | **31.06** | 14.53 | (2.58, 59.53) | **1 of 3** (only san-diego-ca; placer/riverside dropped, no pre or post point) | 2 |

This is the most important robustness finding in the whole readout: the
headline "any"/"epb" effect of 10.65 is **not a stable single number
across cohorts** — it ranges from essentially zero (1.05, 2018 cohort)
to 31.06 (2022+ cohort), and the 2022+ "cohort effect" is really a
**single-county effect** (san-diego-ca) dressed up as a cohort estimate,
because the estimator's own filter throws away placer-ca and
riverside-ca for lack of a pre or post observation. The 2022+ row is
the only one of the three whose CI excludes zero, and that's driven
entirely by n=1.

---

## 4. Mechanism disentangling (asv panel)

Treated counties identified under the `asv` mechanism, with both
adoption years:

| county | epb year | asv year | gap | asv "pre" years available | asv "post" years available |
|---|---|---|---|---|---|
| fresno-ca | 2020 | 2020 | 0 | 2016 | 2024 |
| los-angeles-ca | 2020 | 2020 | 0 | 2012,2014,2016,2018 | 2022,2024 |
| nevada-ca | 2018 | 2022 | 4 | 2012,2014,2016,2018 | 2022 |
| san-diego-ca | 2022 | 2024 | 2 | 2018,2022 | 2024 |

Plain statement: **the asv cut is confounded with EPB for half its
counties and only partially separable for the other half.**

- `fresno-ca` and `los-angeles-ca` adopted EPB and ASV in the **same
  year** (2020). Their asv per-county effects (18.46 and 13.06) are
  bit-for-bit identical to their epb per-county effects — there is no
  data in this panel that could distinguish "the EPB effect" from "the
  ASV effect" for these two counties. They are pure EPB+ASV bundle
  effects, not ASV increments.
- `nevada-ca` adopted EPB in 2018 and ASV in 2022. Its asv "pre" window
  (2012-2018) is **mostly pre-EPB** (3 of 4 years), with only the 2018
  point already reflecting EPB. So the asv effect for nevada-ca (20.19)
  is still substantially an EPB-plus-ASV blend, not a clean ASV
  increment over an EPB baseline — contrary to what you'd want for a
  clean increment estimate.
- `san-diego-ca` adopted EPB in 2022 and ASV in 2024. Its asv "pre"
  window is {2018, 2022} — one pre-EPB year and one year that is
  *itself* the EPB adoption year. This is the closest thing in the
  panel to an "ASV increment over an EPB baseline," but it rests on
  only 2 pre-period observations, one of which is transitional.

Bottom line: **none of the four asv-cohort counties gives a clean,
EPB-isolated ASV-only estimate.** The "asv effect" of 19.11 should be
read as "effect of adopting ASV, typically alongside or shortly after
EPB," not as the marginal effect of ASV holding EPB constant.

---

## 5. Control heterogeneity

Only 2 controls exist in this snapshot: `san-francisco-ca`, `lake-ca`.
With n_controls=2, "within-year spread" is just `|sf_pct - lake_pct|`
per year, and there's no averaging-out of idiosyncratic county trends —
whichever way the pair splits determines the entire control-adjustment.

```python
lake = {2012:70.18,2014:69.72,2016:53.75,2018:63.0,2022:38.51,2024:29.34}
sf   = {2012:71.4, 2014:70.3, 2016:66.1, 2018:59.3, 2022:51.0, 2024:56.9}
for y in sorted(lake):
    print(y, sf[y]-lake[y])
```

| year | lake-ca pct | sf-ca pct | sf - lake | election type |
|---|---|---|---|---|
| 2012 | 70.18 | 71.40 | +1.22 | presidential |
| 2014 | 69.72 | 70.30 | +0.58 | midterm |
| 2016 | 53.75 | 66.10 | +12.35 | presidential |
| 2018 | 63.00 | 59.30 | -3.70 | midterm |
| 2022 | 38.51 | 51.00 | +12.49 | midterm |
| 2024 | 29.34 | 56.90 | +27.56 | presidential |

Mean divergence = 8.42 pp, stdev of divergence = 11.48 pp — i.e. the gap
between the two controls is itself larger, on average, than the
headline treatment effect (10.65), and its spread (sd 11.48) is
comparable to the headline effect's own jackknife SE (8.79).

Year-over-year, lake-ca and sf-ca move in visibly different regimes:

```
lake yoy: 2014 -0.46, 2016 -15.97, 2018 +9.25, 2022 -24.49, 2024 -9.17
sf   yoy: 2014 -1.10, 2016 -4.20,  2018 -6.80, 2022 -8.30,  2024 +5.90
```

Lake-ca is in continuous decline from 2018 onward (63.0 -> 38.51 ->
29.34, a 34-point collapse over two cycles with **no tech adoption on
record** — this is the "no-tech collapse" flagged in the job
instructions) while san-francisco-ca partially recovers in 2024 (51.0
-> 56.9). This is exactly what Section 2's leave-one-out numbers
quantify directly: using lake-ca alone as the control drags the control
baseline down and inflates every treated county's apparent gain,
producing the 16.49 aggregate; using san-francisco-ca alone as the
control (a much flatter, later-recovering trend) produces only 4.82.
The true 2-control average (10.65) is a **near-exact midpoint** of those
two single-control estimates (mean of 16.49 and 4.82 is 10.65, matching
because dropping one control is a linear operation on a 2-element mean),
which is itself evidence that this design has no ability to distinguish
"true treatment effect" from "which one of two idiosyncratic control
counties you leaned on."

This heterogeneity is also *why the placebo is nonzero* (-7.40, not the
"~0" a working design should return). Tracing the placebo computation:
it makes `lake-ca` a fake 2018 adopter (sorted-slug indexing picks index
0 of `['lake-ca','san-francisco-ca']`), leaving `san-francisco-ca` as
the sole real control.

```
lake  pre(2012,14,16)=64.55 -> post(2018,22,24)=43.62   delta = -20.93
sf    pre(2012,14,16)=69.27 -> post(2018,22,24)=55.73   delta(ctrl) = -13.53
placebo effect = -20.93 - (-13.53) = -7.40   [matches placebo() output]
```

Lake-ca's decline (delta -20.93) is simply steeper than san-francisco's
decline (delta -13.53) over the *same* pre/post windows, with zero tech
adoption involved on either side. That gap (7.4 pp) is baseline
county-level heterogeneity misattributed to "treatment" whenever one of
these two counties stands in for "the control" against the other. It is
close in magnitude to the 2018-cohort headline effect (1.05, small) but
is a substantial fraction of the "any"/epb headline (10.65, ~70% of it)
and of the asv headline (19.11, ~39% of it) — i.e. plausibly a sizeable
share of the headline numbers could be this kind of control-pair noise
rather than a tech effect, though the placebo's own sign (negative) means
it is not simply additive/subtractive with the headline sign in an
obvious way; it's evidence of scale, not a bias-correction to subtract.

---

## 6. Honest bottom line

The data currently support a positive, but statistically insignificant
(all CIs cross zero) and mechanism-confounded association between
counting-tech adoption and a larger share of the vote being counted by
election night; they do not support a specific point estimate, a
clean EPB-vs-ASV decomposition, or a claim of causal identification.
The single biggest threat to the "any"/"epb" headline (10.65) is that
it is built on only 2 control counties whose own divergence (mean 8.4
pp, sd 11.5 pp) is comparable in size to the effect itself, and the
placebo check confirms this: a fully fake, no-tech "adoption" produces
a nonzero -7.4 pp effect purely from lake-ca's tech-unrelated 2022/2024
collapse. The single biggest threat to the "asv" headline (19.11) is
that two of its four identifying counties (fresno-ca, los-angeles-ca)
adopted EPB and ASV in the identical year, so "asv effect" is
indistinguishable from "epb+asv bundle effect" for half the panel, and
a third (nevada-ca) is still mostly pre-EPB in its own asv "pre"
window. The cohort cut is the clearest single result in this readout:
the 2018-adopter cohort (which carries the VCA confound most directly)
is statistically and substantively near zero (1.05), while the
2022+-adopter cohort is really a one-county (san-diego-ca) result
wearing a cohort label. Adding Del Norte, Mendocino and Tehama would
most plausibly change the picture by (a) enlarging n_controls beyond 2,
which should shrink the placebo toward zero and tighten every CI, and
(b) potentially filling in pre/post observations for placer-ca and
riverside-ca if their full election-night series get pinned down,
which would turn the 2022+ cohort into an actual 3-county cohort
instead of an n=1 stand-in. Until both of those land, I would not sign
off on 10.65, 19.11, or 31.06 as reportable point estimates in the
findings doc without heavy caveats attached to each.
