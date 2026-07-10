"""Matched-years difference-in-differences estimator for the county
election-night panel.

Effect per treated county c with adoption year a:
    delta_c   = mean(pct, post years) - mean(pct, pre years)
    ctrl_c    = mean over control counties k of
                [mean(pct_k over c's post years) - mean(pct_k over c's pre
                 years)], using only controls observed in at least one year
                of each set
    effect_c  = delta_c - ctrl_c
Aggregate effect = mean over treated counties. Inference = leave-one-county-
out jackknife over ALL counties (treated and control). Placebo = same
computation with controls assigned a fake adoption year and treated counties
excluded. Scenario mode projects the MDE (2.8 * SE) for hypothetical panel
sizes using the observed between-county effect s.d. and the controls'
year-demeaned within-county s.d. (a first-order approximation, documented
here so nobody mistakes it for the real jackknife).

Usage:
  python3 scripts/research/estimate_tech_effect.py
      [--path packages/data/county_night.json]
      [--mechanism any|epb|asv] [--placebo] [--scenario K M] [--json]
"""
import argparse
import json
import math
import statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_PATH = ROOT / "packages" / "data" / "county_night.json"
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
            })
    return rows


def _adoption_year(rows_slug, mechanism):
    r = rows_slug[0]
    if mechanism == "epb":
        return r["epb_year"]
    if mechanism == "asv":
        return r["asv_year"]
    cands = [y for y in (r["epb_year"], r["asv_year"]) if y]
    return min(cands) if cands else None


def _by_slug(panel):
    out = {}
    for r in panel:
        out.setdefault(r["slug"], []).append(r)
    return out


def _control_change(controls, pre_years, post_years):
    changes = []
    for rows in controls.values():
        pre = [r["pct"] for r in rows if r["year"] in pre_years]
        post = [r["pct"] for r in rows if r["year"] in post_years]
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
        ctrl = _control_change(controls, pre_years, post_years)
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


def placebo(panel, fake_year=2018):
    """Controls only: every second control county (sorted by slug) becomes a
    fake adopter at fake_year; the rest stay controls. A working design must
    return ~0 (fake adopters and real controls share the same year shocks)."""
    ctrl = [r for r in panel if r["control"]]
    fake_adopters = set(sorted({r["slug"] for r in ctrl})[::2])
    out = []
    for r in ctrl:
        r2 = dict(r)
        if r2["slug"] in fake_adopters:
            r2["control"] = False
            r2["epb_year"] = fake_year
            r2["asv_year"] = None
        out.append(r2)
    return estimate(out, mechanism="epb")


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
    ap.add_argument("--mechanism", choices=["any", "epb", "asv"],
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
            print(f"{k}: {v}")


if __name__ == "__main__":
    main()
