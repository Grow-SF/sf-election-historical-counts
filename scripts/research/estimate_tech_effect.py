"""Matched-CELLS difference-in-differences estimator for the county
election-night panel.

A "cell" is a (year, election-type) pair, e.g. (2018, "midterm") or
(2018, "midterm-primary"). Matching on cells rather than bare years matters
once the panel carries primaries alongside generals: a year can hold two
observations of systematically different level (primaries run well below
generals in election-night share), and primary coverage is uneven across
counties (some researched counties have no primary rows at all). Matching
controls to a treated county by calendar year alone would silently blend a
control's primary-year row into a comparison the treated county never had,
biasing the control-adjustment. Matching by (year, type) cell instead means a
control only contributes a cell the treated county actually has.

Effect per treated county c with adoption year a:
    delta_c   = mean(pct, post years) - mean(pct, pre years)   [c's own
                rows, unchanged: still averaged by bare year, not cell --
                this is c's own observed trajectory, not a match]
    pre_cells / post_cells = the (year, type) cells present in c's own rows
                for year < a / year >= a
    ctrl_c    = mean over control counties k of
                [mean(pct_k over cells in post_cells present in k's rows) -
                 mean(pct_k over cells in pre_cells present in k's rows)],
                using only controls with at least one matching cell in each
                of pre_cells and post_cells
    effect_c  = delta_c - ctrl_c
Aggregate effect = mean over treated counties. Inference = leave-one-county-
out jackknife over ALL counties (treated and control). Placebo = the same
computation run over EVERY nonempty proper subset of control counties as a
fake-adopter split (treated counties excluded entirely), reporting the full
distribution of split-level effects rather than one arbitrary split -- an
earlier version quoted a single alphabetical every-second split as if it
were the noise floor, which understated how wide that floor actually is (see
placebo_distribution() and the dated correction in
docs/analysis/2026-07-10-tech-effect-estimate.md Section 3). Scenario mode
projects the MDE (2.8 * SE) for hypothetical panel sizes using the observed
between-county effect s.d. and the controls' year-demeaned within-county
s.d. (a first-order approximation, documented here so nobody mistakes it for
the real jackknife).

Usage:
  python3 scripts/research/estimate_tech_effect.py
      [--path packages/data/county_night.json]
      [--mechanism any|epb|asv|vca] [--placebo] [--scenario K M] [--json]
  (--mechanism vca uses each county's Voter's Choice Act all-mail / vote-
   center adoption year, adoption["vca"], baked from the CA adoption census.)
"""
import argparse
import itertools
import json
import math
import random
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_PATH = ROOT / "packages" / "data" / "county_night.json"
# 2020 is excluded as a COVID all-mail outlier for BOTH elections that year:
# the November general and the March 2020 presidential primary. Neither is
# comparable to a normal election-night count, so both are dropped here
# rather than filtered by type.
EXCLUDED_YEARS = {2020}


def load_panel(path=DEFAULT_PATH):
    data = json.loads(Path(path).read_text())
    rows = []
    for j in data["jurisdictions"]:
        for p in j["points"]:
            if p["year"] in EXCLUDED_YEARS:
                continue
            if not p.get("comparable", True):
                continue
            if p.get("pct") is None:
                continue
            rows.append({
                "slug": j["slug"], "year": p["year"], "type": p["type"],
                "pct": p["pct"], "control": bool(j.get("control")),
                "epb_year": j["adoption"].get("epollbook"),
                "asv_year": j["adoption"].get("asv"),
                "vca_year": j["adoption"].get("vca"),
            })
    return rows


def _adoption_year(rows_slug, mechanism):
    r = rows_slug[0]
    if mechanism == "epb":
        return r["epb_year"]
    if mechanism == "asv":
        return r["asv_year"]
    if mechanism == "vca":
        return r.get("vca_year")
    cands = [y for y in (r["epb_year"], r["asv_year"]) if y]
    return min(cands) if cands else None


def _by_slug(panel):
    out = {}
    for r in panel:
        out.setdefault(r["slug"], []).append(r)
    return out


def _control_change(controls, pre_cells, post_cells):
    """pre_cells/post_cells are sets of (year, type) tuples -- the cells the
    treated county actually has. A control contributes only the subset of
    its own rows whose (year, type) matches one of those cells, so a
    control's row in a year/type the treated county doesn't have never
    leaks into the comparison."""
    changes = []
    for rows in controls.values():
        by_cell = {(r["year"], r["type"]): r["pct"] for r in rows}
        pre = [by_cell[c] for c in pre_cells if c in by_cell]
        post = [by_cell[c] for c in post_cells if c in by_cell]
        if pre and post:
            changes.append(st.mean(post) - st.mean(pre))
    return st.mean(changes) if changes else None


def _per_county_effects(panel, mechanism):
    groups = _by_slug(panel)
    controls = {s: rs for s, rs in groups.items() if rs[0]["control"]}
    effects = {}
    for slug, rows in groups.items():
        if rows[0]["control"]:
            continue
        a = _adoption_year(rows, mechanism)
        if a is None:
            continue
        pre_years = {r["year"] for r in rows if r["year"] < a}
        post_years = {r["year"] for r in rows if r["year"] >= a}
        if not pre_years or not post_years:
            continue
        pre = [r["pct"] for r in rows if r["year"] in pre_years]
        post = [r["pct"] for r in rows if r["year"] in post_years]
        pre_cells = {(r["year"], r["type"]) for r in rows if r["year"] < a}
        post_cells = {(r["year"], r["type"]) for r in rows if r["year"] >= a}
        ctrl = _control_change(controls, pre_cells, post_cells)
        if ctrl is None:
            continue
        effects[slug] = (st.mean(post) - st.mean(pre)) - ctrl
    return effects, len(controls)


def estimate(panel, mechanism="any"):
    effects, n_controls = _per_county_effects(panel, mechanism)
    if not effects:
        return {"effect": None, "n_treated": 0, "n_controls": n_controls,
                "per_county": {}}
    return {"effect": st.mean(effects.values()),
            "n_treated": len(effects), "n_controls": n_controls,
            "per_county": dict(sorted(effects.items()))}


def jackknife(panel, mechanism="any"):
    full = estimate(panel, mechanism)
    slugs = sorted({r["slug"] for r in panel})
    reps = []
    for drop in slugs:
        sub = [r for r in panel if r["slug"] != drop]
        e = estimate(sub, mechanism)["effect"]
        if e is not None:
            reps.append(e)
    n = len(reps)
    if n < 2 or full["effect"] is None:
        return {"effect": full["effect"], "se": None, "ci95": (None, None),
                "mde": None, "n_replicates": n}
    mean_rep = st.mean(reps)
    var = (n - 1) / n * sum((e - mean_rep) ** 2 for e in reps)
    se = math.sqrt(var)
    eff = full["effect"]
    return {"effect": eff, "se": se,
            "ci95": (eff - 1.96 * se, eff + 1.96 * se),
            "mde": 2.8 * se, "n_replicates": n}


# Above this many control counties, enumerating every nonempty proper subset
# (2**n - 2 of them) stops being sane -- cap enumeration and sample instead.
_MAX_ENUM_CONTROLS = 12
_MAX_SAMPLED_SPLITS = 2000


def _fake_adopter_splits(slugs):
    """Every nonempty proper subset of slugs, as sorted tuples. Exhaustive
    for up to _MAX_ENUM_CONTROLS controls (2**12 - 2 = 4094 subsets, still
    fast); above that, deterministically sample up to _MAX_SAMPLED_SPLITS
    distinct subsets instead of enumerating 2**n of them."""
    n = len(slugs)
    if n < 2:
        return []
    if n <= _MAX_ENUM_CONTROLS:
        return [c for k in range(1, n)
                for c in itertools.combinations(slugs, k)]
    rng = random.Random(0)  # deterministic across runs
    seen = set()
    attempts = 0
    while len(seen) < _MAX_SAMPLED_SPLITS and attempts < _MAX_SAMPLED_SPLITS * 20:
        attempts += 1
        k = rng.randint(1, n - 1)
        seen.add(tuple(sorted(rng.sample(slugs, k))))
    return list(seen)


def placebo_distribution(panel, mechanism="epb", fake_year=2018):
    """Controls only: enumerate EVERY nonempty proper subset of control
    counties (not one arbitrary split) and promote each subset to fake
    adopters at fake_year, with the remaining controls left as controls and
    all real treated counties excluded. A working design must return a
    distribution centered near 0 (fake adopters and real controls share the
    same year shocks); reporting a single split, as an earlier version of
    this function did, understates how wide that null distribution actually
    is.

    NOTE on precision asymmetry: because each split's fake-adopter group is
    drawn from the (small) control pool, it is almost always smaller than
    the real treated group (n_treated counties), so any individual split's
    effect is noisier than the real estimate. That means this distribution's
    spread OVERSTATES the noise on a same-size estimate -- it is a
    conservative (wide) noise floor, not an apples-to-apples one. Read the
    real estimate's jackknife CI as the primary inference; this distribution
    corroborates it.

    Returns a dict: effects (sorted list of per-split aggregate effects),
    n_splits, mean, sd, min, max, real_effect (the actual estimate at
    `mechanism` against the unmodified panel), n_as_extreme (count of
    |placebo effect| >= |real_effect|), share_as_extreme."""
    ctrl = [r for r in panel if r["control"]]
    slugs = sorted({r["slug"] for r in ctrl})
    real_effect = estimate(panel, mechanism)["effect"]
    fake_key = "asv_year" if mechanism == "asv" else "epb_year"
    other_key = "epb_year" if mechanism == "asv" else "asv_year"
    est_mechanism = "asv" if mechanism == "asv" else "epb"

    effects = []
    for split in _fake_adopter_splits(slugs):
        fake_adopters = set(split)
        out = []
        for r in ctrl:
            r2 = dict(r)
            if r2["slug"] in fake_adopters:
                r2["control"] = False
                r2[fake_key] = fake_year
                r2[other_key] = None
            out.append(r2)
        e = estimate(out, mechanism=est_mechanism)["effect"]
        if e is not None:
            effects.append(e)
    effects.sort()

    n_splits = len(effects)
    if n_splits == 0:
        return {"effects": [], "n_splits": 0, "mean": None, "sd": None,
                "min": None, "max": None, "real_effect": real_effect,
                "n_as_extreme": None, "share_as_extreme": None}

    mean = st.mean(effects)
    sd = st.stdev(effects) if n_splits > 1 else 0.0
    if real_effect is None:
        n_as_extreme = None
        share_as_extreme = None
    else:
        n_as_extreme = sum(1 for e in effects if abs(e) >= abs(real_effect))
        share_as_extreme = n_as_extreme / n_splits
    return {"effects": effects, "n_splits": n_splits, "mean": mean,
            "sd": sd, "min": effects[0], "max": effects[-1],
            "real_effect": real_effect, "n_as_extreme": n_as_extreme,
            "share_as_extreme": share_as_extreme}


def placebo(panel, mechanism="epb", fake_year=2018):
    """Thin wrapper kept for existing callers: returns the same distribution
    dict as placebo_distribution(). The old version of this function
    returned a single arbitrary split's point estimate; every caller must
    now read the distribution, not a lone "effect" key."""
    return placebo_distribution(panel, mechanism=mechanism,
                                fake_year=fake_year)


def scenario(panel, mechanism, n_controls, n_elections):
    effects, _ = _per_county_effects(panel, mechanism)
    n_t = max(len(effects), 2)
    s_b = st.stdev(effects.values()) if len(effects) > 1 else 10.0
    ctrl_rows = [r for r in panel if r["control"]]
    year_means = {}
    for r in ctrl_rows:
        year_means.setdefault(r["year"], []).append(r["pct"])
    resid = [r["pct"] - st.mean(year_means[r["year"]]) for r in ctrl_rows]
    s_w = st.stdev(resid) if len(resid) > 1 and st.stdev(resid) > 0 else 5.0
    half = max(n_elections // 2, 1)
    se_ctrl = s_w * math.sqrt(2 / half) / math.sqrt(n_controls)
    se = math.sqrt(s_b ** 2 / n_t + se_ctrl ** 2)
    return 2.8 * se


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default=str(DEFAULT_PATH))
    ap.add_argument("--mechanism", choices=["any", "epb", "asv", "vca"],
                    default="any")
    ap.add_argument("--placebo", action="store_true")
    ap.add_argument("--scenario", nargs=2, type=int, metavar=("K", "M"))
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    panel = load_panel(args.path)
    est = estimate(panel, args.mechanism)
    out = {"mechanism": args.mechanism, **jackknife(panel, args.mechanism)}
    out["n_treated"] = est["n_treated"]
    out["n_controls"] = est["n_controls"]
    out["per_county"] = est["per_county"]
    if args.placebo:
        out["placebo"] = placebo(panel)
    if args.scenario:
        out["scenario_mde"] = scenario(panel, args.mechanism,
                                       args.scenario[0], args.scenario[1])
    if args.json:
        print(json.dumps(out, indent=1))
    else:
        for k, v in out.items():
            if k == "placebo" and v is not None:
                print("placebo:")
                print(f"  n_splits: {v['n_splits']}")
                print(f"  real_effect: {v['real_effect']}")
                print(f"  mean: {v['mean']}")
                print(f"  sd: {v['sd']}")
                print(f"  min: {v['min']}")
                print(f"  max: {v['max']}")
                print(f"  n_as_extreme: {v['n_as_extreme']}")
                print(f"  share_as_extreme: {v['share_as_extreme']}")
            else:
                print(f"{k}: {v}")


if __name__ == "__main__":
    main()
