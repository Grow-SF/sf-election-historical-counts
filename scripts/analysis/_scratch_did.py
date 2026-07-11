#!/usr/bin/env python
"""VCA modernization bundle vs county election-night share: DiD analysis.

Implements docs/superpowers/specs/2026-07-09-vca-bundle-model-design.md
(sections 2-7) exactly. Single analysis script: panel assembly with hard
startup assertions, Callaway-Sant'Anna-style 2x2 cell means against the
never-treated pair, Fisher randomization inference over adoption labels,
RI test-inversion 90% CI for the headline, BJS imputation cross-check,
quarantined static TWFE exhibit, placebo pre-cells and joint pre-trend
test, the 14-row robustness grid, ASV exact-rank descriptives, and a
--validate synthetic-data harness (scenarios S1-S5 plus a power curve)
whose acceptance criteria are assertions, not prose.

Dependencies: numpy is the ONLY third-party dependency (used for
np.linalg.lstsq on explicitly built dummy matrices and for vectorized RI
loops). Run via:

  uv run --with numpy python scripts/analysis/night_share_bundle_did.py \
      --draws 10000 --seed 20260709
  uv run --with numpy python scripts/analysis/night_share_bundle_did.py \
      --validate --reps 500 --seed 20260709

Determinism: one seed controls every stochastic step via independent child
streams (numpy SeedSequence.spawn). Rerunning either command must leave the
generated files byte-identical. Floats are rounded at emission: 2dp for
estimates, 4dp for probability-type quantities (p-values, Monte Carlo SEs,
rates, power, coverage; 2dp would render the MC SE of p as 0.00, defeating
the spec section 4 requirement that it be reported).

Transparency: every primary number (the seven cells and four aggregates,
both base rules, all three control variants) is computed twice, once with
plain Python arithmetic over lists (the reference implementation a reader
checks by hand against panel.csv) and once inside the numpy engine, and the
two are asserted equal to 1e-9.
"""

import argparse
import json
import math
import os

import numpy as np

# ---------------------------------------------------------------------------
# Constants (spec sections 2-3)
# ---------------------------------------------------------------------------

SEED_DEFAULT = 20260709
YEARS = [2012, 2014, 2016, 2018, 2022, 2024]  # 2020 excluded by design
YTYPE = {2012: "presidential", 2014: "midterm", 2016: "presidential",
         2018: "midterm", 2020: "presidential", 2022: "midterm",
         2024: "presidential"}
COHY = [2018, 2020, 2022, 2024]          # cohort label codes 0..3; 4 = never
NEVER = 4
# Main-analysis controls: parameterized, default the two never-adopters this
# spec's identification rests on (SF + SLO). See CONTROLS_FULL7 below for the
# post-merge 7-control-pool sensitivity check (2026-07-10 merge: origin/main
# contributed five more researched never-adopter counties).
CONTROLS = ["san-francisco-ca", "san-luis-obispo-ca"]
# All 7 no-new-counting-tech controls in the merged county_night.json
# (scripts/build_county_night.py's is_control()). Used ONLY for the row-15
# control-pool-size sensitivity check (robustness_grid); the headline
# identification stays pooled SF+SLO exactly as specified.
CONTROLS_FULL7 = CONTROLS + ["del-norte-ca", "lake-ca", "mendocino-ca",
                             "tehama-ca", "colusa-ca"]

# The 16 jurisdictions this model was designed over (SF + SLO controls + the
# 14 bundle-adoption-labeled counties). The 2026-07-10 merge added primaries
# as a second election type and 5 more never-adopter counties to
# county_night.json; both are out of scope for this generals-only bundle
# model (see load_panel's generals-only filter), so load_panel restricts to
# exactly this set before applying the len(jur) == 16 startup assertion.
CORE_SLUGS = None  # set below, after EXPECTED_COHORTS is defined

EXPECTED_COHORTS = {
    "madera-ca": 2018, "napa-ca": 2018, "nevada-ca": 2018,
    "sacramento-ca": 2018, "san-mateo-ca": 2018,
    "fresno-ca": 2020, "los-angeles-ca": 2020, "orange-ca": 2020,
    "santa-clara-ca": 2020, "san-bernardino-ca": 2020,  # SB label-only
    "riverside-ca": 2022, "san-diego-ca": 2022, "ventura-ca": 2022,
    "placer-ca": 2024,                                   # label-only
}
CORE_SLUGS = set(CONTROLS) | set(EXPECTED_COHORTS)
assert len(CORE_SLUGS) == 16, len(CORE_SLUGS)

# Nevada ASV: adjudicated 2026-07-10 (scratchpad/nevada-tech-adjudication.md,
# see data/research/county-tech/nevada-ca.json's CORRECTION note) at 2016 --
# BEFORE Nevada's own vote-center bundle cohort (2018), not after it as this
# model originally assumed (2022). The bundle cohort year is unaffected
# (vote-center adoption stays 2018); only the ASV year moves. See
# asv_descriptives() for the re-bracketed pre/post-ASV natural-experiment
# test (now 2014->2016, not 2018->2022) and robustness_grid check 9 for the
# ASV-contamination row exclusions this shift implies.
EXPECTED_ASV = {"nevada-ca": 2016, "san-diego-ca": 2024,
                "fresno-ca": 2020, "los-angeles-ca": 2020}
POST_WINDOW_ASV = {"riverside-ca": 2025, "san-bernardino-ca": 2025}

EXPECTED_TIER2 = {
    ("fresno-ca", 2012), ("fresno-ca", 2014), ("fresno-ca", 2018),
    ("napa-ca", 2014),
    ("riverside-ca", 2012), ("riverside-ca", 2014), ("riverside-ca", 2016),
    ("riverside-ca", 2018),
    ("sacramento-ca", 2012),
    ("san-diego-ca", 2012), ("san-diego-ca", 2014),
}

CI_GRID = [i * 0.5 for i in range(-50, 51)]   # -25 .. +25 by 0.5
CI_DRAWS = 2000
LONG_GAP = 8


def repo_root():
    return os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))


# ---------------------------------------------------------------------------
# Rounding / emission helpers
# ---------------------------------------------------------------------------

def r2s(x):
    """Format estimate float at 2dp; normalize -0.00."""
    if x is None:
        return ""
    s = "%.2f" % (float(x),)
    return "0.00" if s == "-0.00" else s


def r4s(x):
    if x is None:
        return ""
    s = "%.4f" % (float(x),)
    return "0.0000" if s == "-0.0000" else s


def r2(x):
    return None if x is None else float(r2s(x))


def r4(x):
    return None if x is None else float(r4s(x))


def sanitize(text, limit=None):
    """Deterministic text for emission; strips em/en dashes per repo rule.

    limit=None keeps the full text (results.json promises the full documented
    exclusion reasons, so they must not be truncated)."""
    t = (text or "").replace("—", ",").replace("–", ",")
    t = " ".join(t.split())
    return t if limit is None else t[:limit]


def write_text(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def jdump(obj):
    """JSON with sorted keys; numpy bools/ints converted.

    Enforces the emission precision policy with a pre-emission recursive
    walk: every float (including np.float64, a float subclass, which
    json.dumps would otherwise serialize natively without invoking the
    default= hook) must round-trip through '%.4f', i.e. it must already
    have passed through r2()/r4(). An unrounded or non-finite float raises
    instead of emitting silently."""
    def walk(o, path):
        if isinstance(o, float):
            if not (math.isfinite(o) and float("%.4f" % o) == o):
                raise TypeError("unrounded float reached emission at %s: %r"
                                % (path, o))
        elif isinstance(o, dict):
            for k, v in o.items():
                walk(v, "%s.%s" % (path, k))
        elif isinstance(o, (list, tuple)):
            for i, v in enumerate(o):
                walk(v, "%s[%d]" % (path, i))
    walk(obj, "$")

    def conv(o):
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        raise TypeError("non-serializable value of type %s reached emission: "
                        "%r" % (type(o).__name__, o))
    return json.dumps(obj, indent=1, sort_keys=True, default=conv)


def write_csv(path, header, rows):
    lines = [",".join(header)]
    for row in rows:
        cells = []
        for v in row:
            s = "" if v is None else str(v)
            if "," in s or '"' in s:
                s = '"' + s.replace('"', '""') + '"'
            cells.append(s)
        lines.append(",".join(cells))
    write_text(path, "\n".join(lines) + "\n")


# ---------------------------------------------------------------------------
# Section 2: panel assembly with startup assertions
# ---------------------------------------------------------------------------

def _slug_from_jurisdiction(name):
    n = name.lower().replace(" county", "").strip().replace(" ", "-")
    return n + "-ca"


def load_panel(root):
    """Load canonical JSONs, apply spec section 2 rules, fail loudly."""
    night = json.load(open(os.path.join(root, "packages/data/county_night.json")))
    tech = json.load(open(os.path.join(root, "packages/data/county_tech.json")))
    plateau = json.load(open(os.path.join(
        root, "data/research/election-night/plateau_review.json")))

    # Restrict to the 16 core jurisdictions (SF+SLO controls + the 14 labeled
    # bundle-adoption counties) this model was designed over. The 2026-07-10
    # merge added 5 more never-adopter counties (Del Norte, Lake, Mendocino,
    # Tehama, Colusa) to county_night.json for the county-tech Long Count
    # comparison; they enter THIS model only via CONTROLS_FULL7's dedicated
    # sensitivity row (robustness_grid check 15), not the core panel.
    jur_all = night["jurisdictions"]
    jur = [j for j in jur_all if j["slug"] in CORE_SLUGS]
    assert len(jur) == 16, "expected 16 core jurisdictions, got %d" % len(jur)
    slugs = sorted(j["slug"] for j in jur)
    names = {j["slug"]: j["name"] for j in jur}

    # --- treatment coding from county_tech.json ---
    adopt = [a for a in tech["adoptions"] if a["state"] == "CA"]
    dropped_vignettes = sorted(set(a["state"] for a in tech["adoptions"]
                                   if a["state"] != "CA"))
    assert dropped_vignettes == ["NY", "PA", "WI"], dropped_vignettes
    by = {}
    for a in adopt:
        by[(_slug_from_jurisdiction(a["jurisdiction"]), a["tech"])] = a

    cohorts = {}
    asv_year = {}       # in-window (<= 2024): enters the analysis
    asv_year_all = {}   # every adopted year, incl. post-window (panel.csv)
    for s in slugs:
        vc = by[(s, "vote-center")]
        epb = by[(s, "epollbook")]
        asv = by[(s, "asv")]
        if vc["status"] == "adopted":
            g = vc["adopted_year"]
            if s == "nevada-ca":
                # Nevada tech adjudication (2026-07-10,
                # scratchpad/nevada-tech-adjudication.md): epollbook is keyed
                # to 2014 (a genuinely earlier, different-generation
                # traditional precinct-roster deployment), deliberately
                # decoupled from the 2018 VCA vote-center switch that the
                # vote-center entry (and this county's bundle cohort) tracks.
                assert epb["status"] == "adopted" and epb["adopted_year"] == 2014, (
                    "Nevada epollbook year changed from the adjudicated 2014")
                assert g == 2018, "Nevada vote-center/bundle year changed from 2018"
            elif epb["status"] == "adopted":
                assert epb["adopted_year"] == g, (
                    "epollbook year != vote-center year for %s" % s)
            cohorts[s] = g
        elif s == "san-bernardino-ca":
            # vote-center not-adopted (primary), epb 2020: label-only member.
            assert epb["status"] == "adopted" and epb["adopted_year"] == 2020
            cohorts[s] = 2020
        elif s == "san-luis-obispo-ca":
            assert epb["status"] == "adopted" and epb["adopted_year"] == 2026
            assert epb["adopted_year"] > 2024, "SLO epb year not post-window"
        else:
            assert s == "san-francisco-ca", (
                "unexpected non-adopter without special handling: %s" % s)
        if asv["status"] == "adopted":
            asv_year_all[s] = asv["adopted_year"]
            if asv["adopted_year"] <= 2024:
                asv_year[s] = asv["adopted_year"]
    assert cohorts == EXPECTED_COHORTS, ("cohort map changed:", cohorts)
    assert asv_year == EXPECTED_ASV, ("in-window ASV map changed:", asv_year)
    assert asv_year_all == {**EXPECTED_ASV, **POST_WINDOW_ASV}, (
        "full ASV map changed:", asv_year_all)
    for s, y in POST_WINDOW_ASV.items():
        a = by[(s, "asv")]
        assert a["status"] == "adopted" and a["adopted_year"] == y, s
    assert by[("san-mateo-ca", "asv")]["status"] == "not-adopted", (
        "San Mateo ASV status changed")
    assert by[("ventura-ca", "epollbook")]["adopted_year"] == 2022
    assert by[("ventura-ca", "vote-center")]["adopted_year"] == 2022

    # --- plateau verdict join ---
    verdicts = {}
    for r in plateau:
        verdicts[(r["slug"], int(r["date"][:4]))] = r["verdict"]

    # --- outcome panel ---
    rows = []
    exclusions = []
    usable_years = {s: [] for s in slugs}
    for j in jur:
        s = j["slug"]
        for p in j["points"]:
            # generals-only: the 2026-07-10 merge added primary-election
            # points ("presidential-primary" / "midterm-primary") to
            # county_night.json; this model is specified over November
            # generals only (spec section 2), so primary points are silently
            # out of scope here, not counted as exclusions.
            if p["type"] not in ("presidential", "midterm"):
                continue
            usable = bool(p.get("comparable")) and p.get("pct") is not None \
                and p["year"] != 2020
            if not usable:
                if p["year"] == 2020 and p.get("comparable") and \
                        p.get("pct") is not None:
                    reason = "2020 excluded by design (COVID election)"
                elif p.get("pct") is None:
                    reason = "no usable night figure (pct null)"
                else:
                    v = verdicts.get((s, p["year"]))
                    reason = "comparable=false"
                    if v:
                        reason += "; plateau verdict " + v
                    fl = _research_flag(root, s, p["year"])
                    if fl:
                        # full text, untruncated: results.json is the
                        # documented home of the complete exclusion reasons
                        reason += "; " + sanitize(fl)
                exclusions.append({
                    "county": s, "year": p["year"], "pct": p.get("pct"),
                    "reason": reason})
                continue
            v = verdicts.get((s, p["year"]))
            if v is None:
                assert s == "san-francisco-ca", (
                    "usable row without plateau record: %s %d" % (s, p["year"]))
            assert v != "REFUTED_AS_PLATEAU", (
                "usable row carries REFUTED_AS_PLATEAU: %s %d" % (s, p["year"]))
            tier1 = p["confidence"] == "primary" and (
                v is None or v in ("CONFIRMED", "REFUTED_AND_CORRECTED"))
            rows.append({
                "county": s, "year": p["year"], "type": p["type"],
                "pct": p["pct"], "ballots": p.get("ballots"),
                "final": p.get("final"), "confidence": p["confidence"],
                "verdict": v if v is not None else "NONE_SF_HOME_DATASET",
                "tier": 1 if tier1 else 2,
            })
            usable_years[s].append(p["year"])

    print("DIAG len(rows)=", len(rows))
    tier2 = {(r["county"], r["year"]) for r in rows if r["tier"] == 2}
    print("DIAG tier2=", sorted(tier2))
    print("DIAG placer=", sorted(usable_years["placer-ca"]))
    print("DIAG sb=", sorted(usable_years["san-bernardino-ca"]))
    ex_map = {(e["county"], e["year"]): e for e in exclusions}
    nv = ex_map.get(("nevada-ca", 2024))
    rv = ex_map.get(("riverside-ca", 2024))
    print("DIAG nv=", nv)
    print("DIAG rv=", rv)
    for c in CONTROLS:
        print("DIAG control", c, sorted(usable_years[c]))
    n_untreated = sum(1 for r in rows if cohorts.get(r["county"], 9999) > r["year"])
    treated_post = [(r["county"], r["year"]) for r in rows
                    if r["county"] in cohorts and r["year"] >= cohorts[r["county"]]]
    print("DIAG n_untreated=", n_untreated)
    n_sb_post = sum(1 for c, y in treated_post if c == "san-bernardino-ca")
    print("DIAG n_sb_post=", n_sb_post, "treated_post total=", len(treated_post))

    Y = {(r["county"], r["year"]): r["pct"] for r in rows}
    FIN = {(r["county"], r["year"]): r["final"] for r in rows}
    return {
        "rows": rows, "slugs": slugs, "names": names, "Y": Y, "FIN": FIN,
        "cohorts": cohorts, "asv_year": asv_year,
        "asv_year_all": asv_year_all, "verdicts": verdicts,
        "exclusions": exclusions,
        "usable_years": {s: sorted(v) for s, v in usable_years.items()},
    }


_research_cache = {}


def _research_flag(root, slug, year):
    """Documented exclusion reason from the per-county research JSON.

    Only called for a general-election exclusion (this model is
    generals-only; see load_panel's filter), so the matching row must itself
    be a general, not a same-year primary. The 2026-07-10 merge added primary
    rows to every county file, so a bare "date starts with year" match is no
    longer unique within a year (e.g. Nevada 2024 has both a March primary
    and a November general row) -- excluding "primary" typed rows keeps this
    pinned to the general."""
    if slug not in _research_cache:
        path = os.path.join(root, "data/research/election-night", slug + ".json")
        try:
            _research_cache[slug] = json.load(open(path))
        except OSError:
            _research_cache[slug] = None
    d = _research_cache[slug]
    if not d:
        return None
    for e in d.get("elections", []):
        if e.get("date", "").startswith(str(year)) and \
                "primary" not in (e.get("type") or "").lower():
            return e.get("flag") or e.get("note")
    return None


# ---------------------------------------------------------------------------
# Base-period rules (spec section 3) - shared python utility
# ---------------------------------------------------------------------------

def base_year_py(usable, t, g, rule):
    """Return (base_year or None, fallback_flag). rule in {'type','calendar'}."""
    pre = [y for y in usable if y < g]
    if not pre:
        return None, False
    if rule == "calendar":
        return max(pre), False
    tm = [y for y in pre if YTYPE[y] == YTYPE[t]]
    if tm:
        return max(tm), False
    return max(pre), True


# ---------------------------------------------------------------------------
# Engine: numpy arrays + precomputed base / pre-cell tables
# ---------------------------------------------------------------------------

class Engine(object):
    def __init__(self, Ydict, slugs, years, cohorts, controls, FINdict=None):
        self.slugs = list(slugs)
        self.years = list(years)
        self.cohorts = dict(cohorts)
        self.controls = list(controls)
        self.idx = {s: i for i, s in enumerate(self.slugs)}
        NC, T = len(self.slugs), len(self.years)
        self.NC, self.T = NC, T
        self.Y = np.full((NC, T), np.nan)
        self.FIN = np.full((NC, T), np.nan)
        for (s, y), v in Ydict.items():
            if s in self.idx and y in self.years:
                self.Y[self.idx[s], self.years.index(y)] = v
        if FINdict:
            for (s, y), v in FINdict.items():
                if s in self.idx and y in self.years and v is not None:
                    self.FIN[self.idx[s], self.years.index(y)] = v
        self.usable = ~np.isnan(self.Y)
        self.year_arr = np.array(self.years)
        self.cohy_arr = np.array(COHY)
        # observed labels
        self.obs_lab = np.full(NC, NEVER, dtype=np.int8)
        for s, g in self.cohorts.items():
            if s in self.idx:
                self.obs_lab[self.idx[s]] = COHY.index(g)
        self.ctrl_obs = np.array([self.idx[c] for c in self.controls])
        # base tables: BASE[rule][g_code, i, t] -> base t-index or -1
        self.BASE = {}
        self.FB = {}
        for rule in ("type", "calendar"):
            B = np.full((4, NC, T), -1, dtype=np.int64)
            F = np.zeros((4, NC, T), dtype=bool)
            for gc, g in enumerate(COHY):
                for i, s in enumerate(self.slugs):
                    uy = [self.years[k] for k in range(T) if self.usable[i, k]]
                    for ti, t in enumerate(self.years):
                        b, fb = base_year_py(uy, t, g, rule)
                        if b is not None:
                            B[gc, i, ti] = self.years.index(b)
                            F[gc, i, ti] = fb
            self.BASE[rule] = B
            self.FB[rule] = F
        # pre-cell tables (calendar b0 per spec section 5)
        maxk = 0
        pre_lists = {}
        for gc, g in enumerate(COHY):
            for i, s in enumerate(self.slugs):
                uy = [self.years[k] for k in range(T) if self.usable[i, k]]
                pre = [y for y in uy if y < g]
                if pre:
                    b0 = max(pre)
                    cells = [self.years.index(y) for y in pre if y != b0]
                    pre_lists[(gc, i)] = (self.years.index(b0), cells)
                    maxk = max(maxk, len(cells))
                else:
                    pre_lists[(gc, i)] = (-1, [])
        self.PREK = max(maxk, 1)
        self.PRE_B0 = np.full((4, NC), -1, dtype=np.int64)
        self.PRE_T = np.full((4, NC, self.PREK), -1, dtype=np.int64)
        for (gc, i), (b0, cells) in pre_lists.items():
            self.PRE_B0[gc, i] = b0
            for k, c in enumerate(cells):
                self.PRE_T[gc, i, k] = c
        # multiset for permutations = observed label multiset
        self.multiset = np.sort(self.obs_lab).astype(np.int8)


# ---------------------------------------------------------------------------
# Batch statistics for the RI engine (numpy).  labs: (B, NC) int8.
# Returns (values (B,), valid (B,)).
# ---------------------------------------------------------------------------

def _ctrl_indices(labs):
    # positions of the two NEVER labels per row, ascending (stable argsort)
    return np.argsort(labs != NEVER, axis=1, kind="stable")[:, :2]


def batch_theta(eng, labs, t_idx, rule, Y=None, restrict_g=None):
    Y = eng.Y if Y is None else Y
    B = labs.shape[0]
    ar = np.arange(eng.NC)
    labs_cl = np.minimum(labs, 3).astype(np.int64)
    ty = eng.years[t_idx]
    Bidx = eng.BASE[rule][labs_cl, ar[None, :], t_idx]              # (B,NC)
    treated = labs < NEVER
    g_ok = treated & (eng.cohy_arr[labs_cl] <= ty)
    if restrict_g is not None:
        g_ok = g_ok & (labs == COHY.index(restrict_g))
    contrib = g_ok & eng.usable[:, t_idx][None, :] & (Bidx >= 0)
    cidx = _ctrl_indices(labs)                                       # (B,2)
    Bc = np.clip(Bidx, 0, eng.T - 1)
    Yct = Y[cidx, t_idx]                                             # (B,2)
    Ycb = Y[cidx[:, :, None], Bc[:, None, :]]                        # (B,2,NC)
    ctrl_change = (Yct[:, :, None] - Ycb).mean(axis=1)               # (B,NC)
    Yi_t = Y[:, t_idx][None, :]
    Yi_b = Y[ar[None, :], Bc]
    delta = (Yi_t - Yi_b) - ctrl_change
    any_contrib = contrib.any(axis=1)
    bad_ct = np.isnan(Yct).any(axis=1) & any_contrib
    bad_cb = (contrib & np.isnan(Ycb).any(axis=1)).any(axis=1)
    valid = any_contrib & ~bad_ct & ~bad_cb
    dz = np.where(contrib, np.nan_to_num(delta, nan=0.0), 0.0)
    vals = dz.sum(axis=1) / np.maximum(contrib.sum(axis=1), 1)
    vals = np.where(valid, vals, np.nan)
    return vals, valid


def batch_att(eng, labs, g, t_idx, rule, Y=None):
    return batch_theta(eng, labs, t_idx, rule, Y=Y, restrict_g=g)


def batch_pretrend(eng, labs, Y=None):
    Y = eng.Y if Y is None else Y
    ar = np.arange(eng.NC)
    labs_cl = np.minimum(labs, 3).astype(np.int64)
    treated = labs < NEVER
    b0 = eng.PRE_B0[labs_cl, ar[None, :]]                            # (B,NC)
    cells = eng.PRE_T[labs_cl, ar[None, :]]                          # (B,NC,K)
    mask = (cells >= 0) & treated[:, :, None] & (b0 >= 0)[:, :, None]
    cidx = _ctrl_indices(labs)
    b0c = np.clip(b0, 0, eng.T - 1)
    cc = np.clip(cells, 0, eng.T - 1)
    Yi_t = Y[ar[None, :, None], cc]                                  # (B,NC,K)
    Yi_b = Y[ar[None, :], b0c][:, :, None]
    Yct = Y[cidx[:, :, None, None], cc[:, None, :, :]]               # (B,2,NC,K)
    Ycb = Y[cidx[:, :, None], b0c[:, None, :]][:, :, :, None]        # (B,2,NC,1)
    ctrl_change = (Yct - Ycb).mean(axis=1)                           # (B,NC,K)
    d = (Yi_t - Yi_b) - ctrl_change
    any_cell = mask.any(axis=(1, 2))
    bad = (mask & (np.isnan(Yct).any(axis=1) | np.isnan(Ycb).any(axis=1))).any(
        axis=(1, 2))
    valid = any_cell & ~bad
    az = np.where(mask, np.abs(np.nan_to_num(d, nan=0.0)), 0.0)
    vals = az.sum(axis=(1, 2)) / np.maximum(mask.sum(axis=(1, 2)), 1)
    vals = np.where(valid, vals, np.nan)
    return vals, valid


STAT_FNS = {
    "theta_2024": lambda eng, labs, Y=None: batch_theta(
        eng, labs, eng.years.index(2024), "type", Y=Y),
    "theta_2022": lambda eng, labs, Y=None: batch_theta(
        eng, labs, eng.years.index(2022), "type", Y=Y),
    "theta_step_2018": lambda eng, labs, Y=None: batch_att(
        eng, labs, 2018, eng.years.index(2018), "type", Y=Y),
    "theta_step_2022": lambda eng, labs, Y=None: batch_att(
        eng, labs, 2022, eng.years.index(2022), "type", Y=Y),
    "pretrend": lambda eng, labs, Y=None: batch_pretrend(eng, labs, Y=Y),
}


def observed_stat(eng, stat, Y=None):
    v, ok = STAT_FNS[stat](eng, eng.obs_lab[None, :], Y=Y)
    assert bool(ok[0]), "observed labels invalid for %s" % stat
    return float(v[0])


def ri_run(eng, stat, n_valid, rng, Y=None, batch=2048):
    """Multiset permutation RI: reject-redraw until n_valid valid draws.

    Returns (perm values array (n_valid,), attempts) where attempts counts
    permutations generated up to and including the n_valid-th valid one.
    """
    fn = STAT_FNS[stat]
    vals = []
    attempts = 0
    got = 0
    while got < n_valid:
        keys = rng.random((batch, eng.NC))
        perm = np.argsort(keys, axis=1)
        labs = eng.multiset[perm]
        v, ok = fn(eng, labs, Y=Y)
        oki = np.flatnonzero(ok)
        need = n_valid - got
        if len(oki) >= need:
            take = oki[:need]
            attempts += int(take[-1]) + 1
            vals.append(v[take])
            got += need
        else:
            attempts += batch
            vals.append(v[oki])
            got += len(oki)
    return np.concatenate(vals)[:n_valid], attempts


def ri_pvalue(perm_vals, obs):
    n = len(perm_vals)
    p = (1.0 + float(np.sum(np.abs(perm_vals) >= abs(obs)))) / (1.0 + n)
    mc_se = math.sqrt(p * (1.0 - p) / n)
    return p, mc_se


def holm(pvals):
    """Holm step-down adjusted p-values for a dict name->p."""
    items = sorted(pvals.items(), key=lambda kv: (kv[1], kv[0]))
    m = len(items)
    adj = {}
    running = 0.0
    for k, (name, p) in enumerate(items):
        val = min(1.0, (m - k) * p)
        running = max(running, val)
        adj[name] = running
    return adj


# ---------------------------------------------------------------------------
# Observed-label estimation (generic over engines; used for the real panel
# and every robustness variant).  Plain loops, readable, deterministic.
# ---------------------------------------------------------------------------

def estimates(eng, rule, ctrl_slugs, Y=None, weight=None):
    """Cells and aggregates on the engine's observed cohort map.

    weight: None (equal) or 'ballots' (certified final at the target year).
    Returns dict with 'cells' {(g,t): [component dicts]} and 'aggs'.
    """
    Y = eng.Y if Y is None else Y
    cidx = [eng.idx[c] for c in ctrl_slugs]
    cells = {}
    for s in sorted(eng.cohorts):
        if s not in eng.idx:
            continue
        g = eng.cohorts[s]
        i = eng.idx[s]
        gc = COHY.index(g)
        for ti, t in enumerate(eng.years):
            if t < g or not eng.usable[i, ti]:
                continue
            b_ti = eng.BASE[rule][gc, i, ti]
            if b_ti < 0:
                continue
            if not all(eng.usable[c, ti] and eng.usable[c, b_ti] for c in cidx):
                continue
            cch = sum(Y[c, ti] - Y[c, b_ti] for c in cidx) / float(len(cidx))
            delta = (Y[i, ti] - Y[i, b_ti]) - cch
            w = 1.0
            if weight == "ballots":
                w = float(eng.FIN[i, ti])
                assert np.isfinite(w) and w > 0
            cells.setdefault((g, t), []).append({
                "county": s, "base_year": eng.years[b_ti],
                "y_t": float(Y[i, ti]), "y_base": float(Y[i, b_ti]),
                "ctrl_change": cch, "delta": delta, "weight": w,
                "fallback": bool(eng.FB[rule][gc, i, ti]),
                "long_gap": (t - eng.years[b_ti]) > LONG_GAP,
            })

    def wmean(comps):
        tw = sum(c["weight"] for c in comps)
        return sum(c["delta"] * c["weight"] for c in comps) / tw

    aggs = {}
    for t in (2022, 2024):
        comps = [c for (g, tt), v in cells.items() if tt == t for c in v]
        if comps:
            aggs["theta_%d" % t] = {
                "value": wmean(comps), "n": len(comps),
                "counties": sorted(c["county"] for c in comps)}
    for g in (2018, 2020, 2022):
        comps = cells.get((g, g))
        if comps:
            aggs["theta_step_%d" % g] = {
                "value": wmean(comps), "n": len(comps),
                "counties": sorted(c["county"] for c in comps)}
    return {"cells": cells, "aggs": aggs}


# ---------------------------------------------------------------------------
# Plain-Python reference implementation (no numpy): the hand-check path.
# ---------------------------------------------------------------------------

def plain_estimates(panel, rule, ctrl_slugs):
    Y = panel["Y"]
    uy = panel["usable_years"]
    cells = {}
    for s in sorted(panel["cohorts"]):
        g = panel["cohorts"][s]
        for t in YEARS:
            if t < g or (s, t) not in Y:
                continue
            b, fb = base_year_py(uy[s], t, g, rule)
            if b is None:
                continue
            if not all((c, t) in Y and (c, b) in Y for c in ctrl_slugs):
                continue
            cch = sum(Y[(c, t)] - Y[(c, b)] for c in ctrl_slugs) / float(
                len(ctrl_slugs))
            delta = (Y[(s, t)] - Y[(s, b)]) - cch
            cells.setdefault((g, t), []).append((s, b, delta))
    aggs = {}
    for t in (2022, 2024):
        d = [x[2] for (g, tt), v in cells.items() if tt == t for x in v]
        if d:
            aggs["theta_%d" % t] = sum(d) / len(d)
    for g in (2018, 2022):
        d = [x[2] for x in cells.get((g, g), [])]
        if d:
            aggs["theta_step_%d" % g] = sum(d) / len(d)
    return cells, aggs


def plain_theta_for_labels(panel, label_map, t, rule):
    """Plain-python mirror of batch_theta for one label assignment.

    label_map: slug -> cohort year or 'never'. Returns (value, valid).
    """
    Y = panel["Y"]
    uy = panel["usable_years"]
    ctrls = sorted(s for s, g in label_map.items() if g == "never")
    deltas = []
    for s, g in sorted(label_map.items()):
        if g == "never" or g > t or (s, t) not in Y:
            continue
        b, _ = base_year_py(uy[s], t, g, rule)
        if b is None:
            continue
        if not all((c, t) in Y and (c, b) in Y for c in ctrls):
            return None, False
        cch = sum(Y[(c, t)] - Y[(c, b)] for c in ctrls) / 2.0
        deltas.append((Y[(s, t)] - Y[(s, b)]) - cch)
    if not deltas:
        return None, False
    return sum(deltas) / len(deltas), True


def plain_pretrend_for_labels(panel, label_map):
    Y = panel["Y"]
    uy = panel["usable_years"]
    ctrls = sorted(s for s, g in label_map.items() if g == "never")
    cells = []
    for s, g in sorted(label_map.items()):
        if g == "never":
            continue
        pre = [y for y in uy[s] if y < g]
        if not pre:
            continue
        b0 = max(pre)
        for t in pre:
            if t == b0:
                continue
            if not all((c, t) in Y and (c, b0) in Y for c in ctrls):
                return None, False
            cch = sum(Y[(c, t)] - Y[(c, b0)] for c in ctrls) / 2.0
            cells.append(abs((Y[(s, t)] - Y[(s, b0)]) - cch))
    if not cells:
        return None, False
    return sum(cells) / len(cells), True


def dual_computation_check(panel, eng, seed):
    """Spec section 9: plain-python reference vs numpy engine to 1e-9.

    seed: the run's --seed; per the one-seed policy every stochastic step,
    including this cross-check's 50 random label assignments, derives from
    it via an independent SeedSequence child stream."""
    variants = [("pooled", CONTROLS), ("sf", CONTROLS[:1]), ("slo", CONTROLS[1:])]
    for rule in ("type", "calendar"):
        for _vn, ctrls in variants:
            pcells, paggs = plain_estimates(panel, rule, ctrls)
            e = estimates(eng, rule, ctrls)
            pk = sorted(pcells)
            ek = sorted(e["cells"])
            assert pk == ek, (rule, _vn, pk, ek)
            for key in pk:
                pv = sorted(pcells[key])
                ev = sorted((c["county"], c["base_year"], c["delta"])
                            for c in e["cells"][key])
                for (ps, pb, pd), (es_, eb, ed) in zip(pv, ev):
                    assert ps == es_ and pb == eb and abs(pd - ed) < 1e-9, (
                        rule, _vn, key, ps, pd, ed)
            for name, val in paggs.items():
                assert abs(val - e["aggs"][name]["value"]) < 1e-9, (
                    rule, _vn, name)
    # cross-check numpy batch statistics against plain python on the observed
    # labels and on 50 random label assignments (validates the RI engine).
    rng = np.random.default_rng(np.random.SeedSequence(seed).spawn(64)[63])
    for k in range(51):
        if k == 0:
            labs = eng.obs_lab.copy()
        else:
            labs = eng.multiset[rng.permutation(eng.NC)]
        lm = {}
        for i, s in enumerate(eng.slugs):
            lm[s] = "never" if labs[i] == NEVER else COHY[labs[i]]
        for stat, t in (("theta_2024", 2024), ("theta_2022", 2022)):
            v, ok = STAT_FNS[stat](eng, labs[None, :])
            pv, pok = plain_theta_for_labels(panel, lm, t, "type")
            assert bool(ok[0]) == pok, (stat, k)
            if pok:
                assert abs(float(v[0]) - pv) < 1e-9, (stat, k)
        v, ok = STAT_FNS["pretrend"](eng, labs[None, :])
        pv, pok = plain_pretrend_for_labels(panel, lm)
        assert bool(ok[0]) == pok, ("pretrend", k)
        if pok:
            assert abs(float(v[0]) - pv) < 1e-9, ("pretrend", k)


# ---------------------------------------------------------------------------
# BJS imputation cross-check and static TWFE exhibit (numpy lstsq)
# ---------------------------------------------------------------------------

def bjs_fit(eng, Y=None):
    """Fit Y_it = alpha_i + gamma_t on untreated usable cells.

    Returns (alpha dict slug->float, gamma dict year->float, sigma_dof, n, k).
    Counties with zero untreated cells are dropped (alpha unidentified).
    """
    Y = eng.Y if Y is None else Y
    cells = []
    for i, s in enumerate(eng.slugs):
        g = eng.cohorts.get(s, 10 ** 9)
        for ti, t in enumerate(eng.years):
            if eng.usable[i, ti] and t < g:
                cells.append((i, ti))
    counties = sorted({i for i, _ in cells})
    cpos = {i: k for k, i in enumerate(counties)}
    ncol = len(counties) + (eng.T - 1)
    X = np.zeros((len(cells), ncol))
    yv = np.zeros(len(cells))
    for r, (i, ti) in enumerate(cells):
        X[r, cpos[i]] = 1.0
        if ti > 0:
            X[r, len(counties) + ti - 1] = 1.0
        yv[r] = Y[i, ti]
    beta, _res, _rk, _sv = np.linalg.lstsq(X, yv, rcond=None)
    resid = yv - X.dot(beta)
    dof = len(cells) - ncol
    sigma = math.sqrt(float(resid.dot(resid)) / dof) if dof > 0 else float("nan")
    alpha = {eng.slugs[i]: float(beta[cpos[i]]) for i in counties}
    gamma = {eng.years[0]: 0.0}
    for ti in range(1, eng.T):
        gamma[eng.years[ti]] = float(beta[len(counties) + ti - 1])
    return alpha, gamma, sigma, len(cells), ncol


def bjs_aggregates(eng, Y=None):
    """Impute counterfactuals for treated post cells; aggregate gaps.

    Returns (aggs, sigma, gamma, n_untreated, n_imputed)."""
    Y = eng.Y if Y is None else Y
    alpha, gamma, sigma, n, k = bjs_fit(eng, Y=Y)
    gaps = {}
    for i, s in enumerate(eng.slugs):
        g = eng.cohorts.get(s)
        if g is None or s not in alpha:
            continue
        for ti, t in enumerate(eng.years):
            if eng.usable[i, ti] and t >= g:
                gaps[(s, t)] = float(Y[i, ti]) - alpha[s] - gamma[t]
    aggs = {}
    for t in (2022, 2024):
        d = [v for (s, tt), v in gaps.items() if tt == t]
        if d:
            aggs["theta_%d" % t] = sum(d) / len(d)
    for g in (2018, 2022):
        d = [v for (s, tt), v in gaps.items()
             if tt == g and eng.cohorts.get(s) == g]
        if d:
            aggs["theta_step_%d" % g] = sum(d) / len(d)
    return aggs, sigma, gamma, n, len(gaps)


def twfe_static(eng, Y=None):
    """Static two-way FE with a single post dummy. Known-biased exhibit."""
    Y = eng.Y if Y is None else Y
    rows = [(i, ti) for i in range(eng.NC) for ti in range(eng.T)
            if eng.usable[i, ti]]
    ncol = eng.NC + (eng.T - 1) + 1
    X = np.zeros((len(rows), ncol))
    yv = np.zeros(len(rows))
    for r, (i, ti) in enumerate(rows):
        X[r, i] = 1.0
        if ti > 0:
            X[r, eng.NC + ti - 1] = 1.0
        g = eng.cohorts.get(eng.slugs[i], 10 ** 9)
        if eng.years[ti] >= g:
            X[r, -1] = 1.0
        yv[r] = Y[i, ti]
    beta, _res, _rk, _sv = np.linalg.lstsq(X, yv, rcond=None)
    return float(beta[-1])


# ---------------------------------------------------------------------------
# Section 5: placebo pre-cells, anticipation, not-yet-treated variant
# ---------------------------------------------------------------------------

def precells_observed(panel):
    """The 25 placebo pre-cells (calendar b0, pooled controls, section 3 sign)."""
    Y = panel["Y"]
    uy = panel["usable_years"]
    tier = {(r["county"], r["year"]): r["tier"] for r in panel["rows"]}
    out = []
    for s in sorted(panel["cohorts"]):
        g = panel["cohorts"][s]
        pre = [y for y in uy[s] if y < g]
        if not pre:
            continue
        b0 = max(pre)
        for t in pre:
            if t == b0:
                continue
            cch = sum(Y[(c, t)] - Y[(c, b0)] for c in CONTROLS) / 2.0
            d = (Y[(s, t)] - Y[(s, b0)]) - cch
            t1 = tier[(s, t)] == 1 and tier[(s, b0)] == 1
            out.append({"county": s, "cohort": g, "year": t, "base_year": b0,
                        "event_time": t - g, "delta_pre": d, "tier1_cell": t1})
    return out


def anticipation_2018(panel):
    """Event-time -1 vs -2 movement for the 2018 cohort (relative to controls)."""
    Y = panel["Y"]
    uy = panel["usable_years"]
    rows = []
    for s in sorted(panel["cohorts"]):
        if panel["cohorts"][s] != 2018:
            continue
        pre = [y for y in uy[s] if y < 2018]
        if len(pre) < 2:
            continue
        b0 = max(pre)
        prev = max(y for y in pre if y < b0)
        cch = sum(Y[(c, b0)] - Y[(c, prev)] for c in CONTROLS) / 2.0
        rows.append({"county": s, "minus1": b0, "minus2": prev,
                     "move": (Y[(s, b0)] - Y[(s, prev)]) - cch})
    mean = sum(r["move"] for r in rows) / len(rows)
    return {"counties": rows, "mean": mean, "n": len(rows)}


def nyt_att_2018(panel, rule):
    """ATT(2018,2018) against the 8 not-yet-treated comparators.

    Comparators missing a needed year are dropped for that county's delta
    (San Diego lacks 2016) and recorded.
    """
    Y = panel["Y"]
    uy = panel["usable_years"]
    comparators = ["san-francisco-ca", "san-luis-obispo-ca", "fresno-ca",
                   "los-angeles-ca", "orange-ca", "riverside-ca",
                   "san-diego-ca", "ventura-ca"]
    deltas = []
    dropped = []
    for s in sorted(panel["cohorts"]):
        if panel["cohorts"][s] != 2018 or (s, 2018) not in Y:
            continue
        b, _fb = base_year_py(uy[s], 2018, 2018, rule)
        if b is None:
            continue
        avail = [c for c in comparators if (c, 2018) in Y and (c, b) in Y]
        for c in comparators:
            if c not in avail:
                dropped.append("%s (for %s, base %d)" % (c, s, b))
        cch = sum(Y[(c, 2018)] - Y[(c, b)] for c in avail) / float(len(avail))
        deltas.append((Y[(s, 2018)] - Y[(s, b)]) - cch)
    return sum(deltas) / len(deltas), len(deltas), sorted(set(dropped))


def placebo_in_time(panel, rule):
    """Row 7: adoption shifted one general earlier, pre-period only."""
    Y = panel["Y"]
    uy = panel["usable_years"]
    shift = {2018: 2016, 2020: 2018, 2022: 2020, 2024: 2022}
    cells = []
    for s in sorted(panel["cohorts"]):
        g = panel["cohorts"][s]
        gs = shift[g]
        for t in YEARS:
            if not (gs <= t < g) or (s, t) not in Y:
                continue
            b, _fb = base_year_py(uy[s], t, gs, rule)
            if b is None:
                continue
            cch = sum(Y[(c, t)] - Y[(c, b)] for c in CONTROLS) / 2.0
            cells.append({"county": s, "year": t, "base_year": b,
                          "delta": (Y[(s, t)] - Y[(s, b)]) - cch})
    mean = sum(c["delta"] for c in cells) / len(cells)
    return {"cells": cells, "mean": mean, "n": len(cells)}


# ---------------------------------------------------------------------------
# Tier 3: ASV exact-rank descriptives (spec section 1 tier 3)
# ---------------------------------------------------------------------------

def asv_descriptives(panel, main_est):
    Y = panel["Y"]
    out = {}
    # Nevada 2018 -> 2022 vs the 6 counties with no tech change in (2018, 2022]
    pool_nev = ["san-francisco-ca", "san-luis-obispo-ca", "madera-ca",
                "napa-ca", "sacramento-ca", "san-mateo-ca"]
    nev = Y[("nevada-ca", 2022)] - Y[("nevada-ca", 2018)]
    ch = sorted([(Y[(c, 2022)] - Y[(c, 2018)], c) for c in pool_nev] +
                [(nev, "nevada-ca")], key=lambda x: (-x[0], x[1]))
    # conservative exact-rank convention: rank = #{change >= observed},
    # so an exact tie counts against the ASV county instead of being
    # broken by slug order.
    rank_nev = 1 + sum(1 for v, c in ch if c != "nevada-ca" and v >= nev)
    out["nevada_2018_2022"] = {
        "change": nev, "pool": ch, "rank": rank_nev, "n": len(ch),
        "one_sided_p": rank_nev / float(len(ch)),
        "min_attainable_p": 1.0 / len(ch)}
    # San Diego 2022 -> 2024 vs the 11 counties with no tech change in (2022, 2024]
    pool_sd = pool_nev + ["fresno-ca", "los-angeles-ca", "orange-ca",
                          "santa-clara-ca", "ventura-ca"]
    sd = Y[("san-diego-ca", 2024)] - Y[("san-diego-ca", 2022)]
    ch2 = sorted([(Y[(c, 2024)] - Y[(c, 2022)], c) for c in pool_sd] +
                 [(sd, "san-diego-ca")], key=lambda x: (-x[0], x[1]))
    rank_sd = 1 + sum(1 for v, c in ch2 if c != "san-diego-ca" and v >= sd)
    out["san_diego_2022_2024"] = {
        "change": sd, "pool": ch2, "rank": rank_sd, "n": len(ch2),
        "one_sided_p": rank_sd / float(len(ch2)),
        "min_attainable_p": 1.0 / len(ch2)}
    # 2020-cohort contrast: Fresno+LA (bundle+ASV) vs Orange+Santa Clara
    # (bundle only), exact 6-assignment permutation on mean post delta.
    quad = ["fresno-ca", "los-angeles-ca", "orange-ca", "santa-clara-ca"]
    mean_post = {}
    for s in quad:
        ds = [c["delta"] for key in ((2020, 2022), (2020, 2024))
              for c in main_est["cells"].get(key, []) if c["county"] == s]
        mean_post[s] = sum(ds) / len(ds)
    obs_diff = (mean_post["fresno-ca"] + mean_post["los-angeles-ca"]) / 2.0 - \
               (mean_post["orange-ca"] + mean_post["santa-clara-ca"]) / 2.0
    import itertools
    diffs = []
    for pair in itertools.combinations(sorted(quad), 2):
        a = sum(mean_post[s] for s in pair) / 2.0
        b = sum(mean_post[s] for s in quad if s not in pair) / 2.0
        diffs.append((a - b, pair))
    p_geq = sum(1 for d, _ in diffs if d >= obs_diff - 1e-12) / 6.0
    out["cohort2020_asv_contrast"] = {
        "mean_post_delta": mean_post, "obs_diff": obs_diff,
        "assignments": [(d, "+".join(p)) for d, p in
                        sorted(diffs, key=lambda x: (-x[0], x[1]))],
        "one_sided_p": p_geq, "min_attainable_p": 1.0 / 6.0}
    # San Bernardino single 2024 point vs same-year counties (no inference).
    sb = Y[("san-bernardino-ca", 2024)]
    peers = sorted([(Y[(s, 2024)], s) for s in panel["usable_years"]
                    if (s, 2024) in Y], key=lambda x: (-x[0], x[1]))
    rank_sb = 1 + sum(1 for v, s in peers
                      if s != "san-bernardino-ca" and v >= sb)
    out["san_bernardino_2024"] = {"pct": sb, "peers": peers,
                                  "rank": rank_sb, "n": len(peers)}
    return out


# ---------------------------------------------------------------------------
# Robustness grid (spec section 6, rows 1-14)
# ---------------------------------------------------------------------------

AGG_NAMES = ["theta_2024", "theta_2022", "theta_step_2018", "theta_step_2022"]


def agg_map(est):
    return {k: (est["aggs"][k]["value"], est["aggs"][k]["n"])
            for k in AGG_NAMES if k in est["aggs"]}


def loo_ranges(main_cells_by_variant):
    """Leave-one-county-out ranges over every aggregate (type rule).

    main_cells_by_variant: {'pooled': est, 'sf': est, 'slo': est}.
    Dropping a control = the other single-control estimate; dropping a treated
    contributing county = recompute the pooled aggregate without its deltas.
    """
    out = {}
    pooled = main_cells_by_variant["pooled"]
    for name in AGG_NAMES:
        if name not in pooled["aggs"]:
            continue
        base_val = pooled["aggs"][name]["value"]
        if name.startswith("theta_step"):
            g = int(name.split("_")[-1])
            keys = [(g, g)]
        else:
            t = int(name.split("_")[-1])
            keys = [(g, tt) for (g, tt) in pooled["cells"] if tt == t]
        comps = [c for k in keys for c in pooled["cells"].get(k, [])]
        vals = []
        for s in sorted({c["county"] for c in comps}):
            rest = [c["delta"] for c in comps if c["county"] != s]
            if rest:
                vals.append((sum(rest) / len(rest), "drop " + s))
        vals.append((main_cells_by_variant["slo"]["aggs"][name]["value"],
                     "drop san-francisco-ca"))
        vals.append((main_cells_by_variant["sf"]["aggs"][name]["value"],
                     "drop san-luis-obispo-ca"))
        flips = sorted(lab for v, lab in vals
                       if v == 0 or (v > 0) != (base_val > 0))
        out[name] = {"min": min(v for v, _ in vals),
                     "max": max(v for v, _ in vals),
                     "min_label": min(vals)[1], "max_label": max(vals)[1],
                     "sign_flips": flips}
    return out


def build_variant_engine(panel, drop_rows=(), add_rows=(), drop_county=None,
                         transform=None, years=None, include_2020=False,
                         root=None):
    """Build an Engine for a robustness variant from modified real data."""
    Y = dict(panel["Y"])
    FIN = dict(panel["FIN"])
    for k in drop_rows:
        Y.pop(k, None)
    for (s, y), v in add_rows:
        Y[(s, y)] = v
    if include_2020:
        night = json.load(open(os.path.join(root, "packages/data/county_night.json")))
        for j in night["jurisdictions"]:
            for p in j["points"]:
                if p["year"] == 2020 and p.get("comparable") and \
                        p.get("pct") is not None:
                    Y[(j["slug"], 2020)] = p["pct"]
                    FIN[(j["slug"], 2020)] = p.get("final")
    slugs = [s for s in panel["slugs"] if s != drop_county]
    cohorts = {s: g for s, g in panel["cohorts"].items() if s != drop_county}
    if transform == "logit":
        Y = {k: math.log((v / 100.0) / (1.0 - v / 100.0)) for k, v in Y.items()}
    yrs = years if years is not None else YEARS
    return Engine(Y, slugs, yrs, cohorts, CONTROLS, FINdict=FIN)


def robustness_grid(panel, eng, est_by, root):
    """Rows 1-14. Returns (rows for sensitivities.csv, machine dict)."""
    rows = []
    detail = {}
    tm_pooled = est_by[("type", "pooled")]

    def add(check, name, variant, statistic, value, n, note=""):
        rows.append([check, name, variant, statistic,
                     r2s(value) if value is not None else "", n or "", note])

    # 1 control triptych
    for variant in ("pooled", "sf", "slo"):
        e = est_by[("type", variant)]
        for a in AGG_NAMES:
            add(1, "control_triptych", variant, a,
                e["aggs"][a]["value"], e["aggs"][a]["n"])
    sf24 = est_by[("type", "sf")]["aggs"]["theta_2024"]["value"]
    slo24 = est_by[("type", "slo")]["aggs"]["theta_2024"]["value"]
    detail["sign_disagreement"] = (sf24 > 0) != (slo24 > 0)

    # 2 base rule
    for rule in ("type", "calendar"):
        e = est_by[(rule, "pooled")]
        for a in AGG_NAMES:
            add(2, "base_rule", rule, a, e["aggs"][a]["value"],
                e["aggs"][a]["n"])
    t24_type = tm_pooled["aggs"]["theta_2024"]["value"]
    t24_cal = est_by[("calendar", "pooled")]["aggs"]["theta_2024"]["value"]
    detail["base_rule_flip"] = (t24_type > 0) != (t24_cal > 0)
    add(2, "base_rule", "flip_check", "theta_2024_sign_flip",
        None, "", str(detail["base_rule_flip"]))

    # 3 tier-1 only
    t2_keys = sorted(EXPECTED_TIER2)
    eng_t1 = build_variant_engine(panel, drop_rows=t2_keys)
    e = estimates(eng_t1, "type", CONTROLS)
    for a in AGG_NAMES:
        if a in e["aggs"]:
            add(3, "tier1_only", "drop_11_tier2_rows", a,
                e["aggs"][a]["value"], e["aggs"][a]["n"])
        else:
            add(3, "tier1_only", "drop_11_tier2_rows", a, None, 0, "cell empty")
    detail["tier1_theta_2024"] = e["aggs"]["theta_2024"]["value"]
    detail["tier1_move"] = abs(detail["tier1_theta_2024"] - t24_type)

    # 4 bounds: re-include comparable=false treated-post exclusions
    b_variants = [("nevada_2024_included", [(("nevada-ca", 2024), 24.49)]),
                  ("riverside_2024_included", [(("riverside-ca", 2024), 63.7)]),
                  ("both_included", [(("nevada-ca", 2024), 24.49),
                                     (("riverside-ca", 2024), 63.7)])]
    for vn, adds in b_variants:
        ev = estimates(build_variant_engine(panel, add_rows=adds), "type",
                       CONTROLS)
        add(4, "excluded_2024_bounds", vn, "theta_2024",
            ev["aggs"]["theta_2024"]["value"], ev["aggs"]["theta_2024"]["n"])
        detail.setdefault("bounds", {})[vn] = ev["aggs"]["theta_2024"]["value"]
    assert detail["bounds"]["nevada_2024_included"] < t24_type, (
        "theta_2024 did not drop when Nevada 2024 is included")

    # 5 leave-one-out
    loo = loo_ranges({"pooled": est_by[("type", "pooled")],
                      "sf": est_by[("type", "sf")],
                      "slo": est_by[("type", "slo")]})
    for a in AGG_NAMES:
        add(5, "leave_one_out", "min", a, loo[a]["min"], "",
            loo[a]["min_label"])
        add(5, "leave_one_out", "max", a, loo[a]["max"], "",
            loo[a]["max_label"])
        add(5, "leave_one_out", "sign_flips", a, None, "",
            ";".join(loo[a]["sign_flips"]) or "none")
    detail["loo"] = loo

    # 6 not-yet-treated comparators for ATT(2018,2018)
    for rule in ("type", "calendar"):
        v, n, dropped = nyt_att_2018(panel, rule)
        never_v = est_by[(rule, "pooled")]["aggs"]["theta_step_2018"]["value"]
        add(6, "not_yet_treated_att2018", rule, "theta_step_2018", v, n,
            "never-treated version %s; comparators dropped: %s" % (
                r2s(never_v), "; ".join(dropped) or "none"))
        detail.setdefault("nyt", {})[rule] = {"value": v,
                                              "never_version": never_v,
                                              "dropped": dropped}

    # 7 placebo-in-time
    pit = placebo_in_time(panel, "type")
    add(7, "placebo_in_time", "shift_one_general_earlier", "mean_placebo_delta",
        pit["mean"], pit["n"],
        "cells: " + "; ".join("%s@%d(base %d)=%s" % (
            c["county"], c["year"], c["base_year"], r2s(c["delta"]))
            for c in pit["cells"]))
    detail["placebo_in_time"] = pit
    detail["placebo_time_trigger"] = abs(pit["mean"]) > 3.0

    # 8 Riverside excluded entirely
    e = estimates(build_variant_engine(panel, drop_county="riverside-ca"),
                  "type", CONTROLS)
    for a in AGG_NAMES:
        add(8, "riverside_excluded", "drop_riverside", a,
            e["aggs"][a]["value"], e["aggs"][a]["n"])
    detail["no_riverside"] = agg_map(e)

    # 9 ASV-augmented county-years excluded (Nevada 2022, San Diego 2024)
    e = estimates(build_variant_engine(
        panel, drop_rows=[("nevada-ca", 2022), ("san-diego-ca", 2024)]),
        "type", CONTROLS)
    add(9, "asv_rows_excluded", "drop_nevada2022_sandiego2024", "theta_2022",
        e["aggs"]["theta_2022"]["value"], e["aggs"]["theta_2022"]["n"])
    add(9, "asv_rows_excluded", "drop_nevada2022_sandiego2024", "theta_2024",
        e["aggs"]["theta_2024"]["value"], e["aggs"]["theta_2024"]["n"])
    detail["asv_excluded"] = agg_map(e)

    # 10 ballot-weighted (different estimand, reported beside, never substituted)
    e = estimates(eng, "type", CONTROLS, weight="ballots")
    for a in AGG_NAMES:
        add(10, "ballot_weighted", "final_ballots_at_t", a,
            e["aggs"][a]["value"], e["aggs"][a]["n"])
    detail["ballot_weighted"] = agg_map(e)

    # 11 logit transform
    e = estimates(build_variant_engine(panel, transform="logit"), "type",
                  CONTROLS)
    flips = []
    for a in AGG_NAMES:
        lv = e["aggs"][a]["value"]
        pv = tm_pooled["aggs"][a]["value"]
        if (lv > 0) != (pv > 0):
            flips.append(a)
        add(11, "logit_transform", "logit_pct", a, lv, e["aggs"][a]["n"],
            "logit units")
    add(11, "logit_transform", "sign_flips", "any", None, "",
        ";".join(flips) or "none")
    detail["logit_sign_flips"] = flips

    # 12 2020 restored (single appendix line)
    yrs7 = [2012, 2014, 2016, 2018, 2020, 2022, 2024]
    eng20 = build_variant_engine(panel, years=yrs7, include_2020=True,
                                 root=root)
    n2020 = int(eng20.usable[:, yrs7.index(2020)].sum())
    who2020 = "+".join(eng20.slugs[i] for i in
                       np.flatnonzero(eng20.usable[:, yrs7.index(2020)]))
    note20 = ("only %d usable 2020 row exists in the canonical dataset (%s); "
              "restoring 2020 adds no treated outcome or base year" % (
                  n2020, who2020))
    e = estimates(eng20, "type", CONTROLS)
    for a in AGG_NAMES:
        if a in e["aggs"]:
            add(12, "restore_2020", "include_covid_election", a,
                e["aggs"][a]["value"], e["aggs"][a]["n"], note20)
    att2020 = e["aggs"].get("theta_step_2020")
    if att2020:
        add(12, "restore_2020", "include_covid_election", "att_2020_2020",
            att2020["value"], att2020["n"],
            "at-adoption cell for the 2020 cohort; COVID election")
    detail["with_2020"] = {k: (v["value"], v["n"]) for k, v in e["aggs"].items()}

    # 13 BJS + TWFE beside the cell means
    bjs_aggs, sigma, gamma, n_unt, k_unt = bjs_aggregates(eng)
    div_flags = []
    for a in AGG_NAMES:
        cm = tm_pooled["aggs"][a]["value"]
        bv = bjs_aggs[a]
        if abs(bv - cm) > 3.0:
            div_flags.append(a)
        add(13, "estimator_dependence", "bjs_imputation", a, bv, "",
            "cell-mean %s; divergence %s" % (r2s(cm), r2s(bv - cm)))
    beta = twfe_static(eng)
    add(13, "estimator_dependence", "static_twfe_exhibit", "beta_post", beta,
        "", "known-biased; quarantined; see validation.json S3")
    detail["bjs"] = bjs_aggs
    detail["bjs_divergence_flags"] = div_flags
    detail["twfe_beta"] = beta

    # 14 size split (descriptive only)
    comps24 = [c for (g, t), v in tm_pooled["cells"].items() if t == 2024
               for c in v]
    finals = sorted((float(eng.FIN[eng.idx[c["county"]],
                                   eng.years.index(2024)]), c["county"])
                    for c in comps24)
    med = (finals[len(finals) // 2 - 1][0] + finals[len(finals) // 2][0]) / 2.0
    small = [s for f, s in finals if f <= med]
    large = [s for f, s in finals if f > med]
    sm = [c["delta"] for c in comps24 if c["county"] in small]
    lg = [c["delta"] for c in comps24 if c["county"] in large]
    add(14, "size_split", "small_counties", "theta_2024_descriptive",
        sum(sm) / len(sm), len(sm), "final<=median(%s): %s" % (
            r2s(med), "+".join(sorted(small))))
    add(14, "size_split", "large_counties", "theta_2024_descriptive",
        sum(lg) / len(lg), len(lg), "final>median: %s" % "+".join(sorted(large)))
    detail["size_split"] = {"median_final": med, "small": sorted(small),
                            "large": sorted(large),
                            "small_mean": sum(sm) / len(sm),
                            "large_mean": sum(lg) / len(lg)}
    return rows, detail


# ---------------------------------------------------------------------------
# Section 7: synthetic-data validation harness (--validate)
# ---------------------------------------------------------------------------

def treated_post_mask(eng):
    m = np.zeros((eng.NC, eng.T), dtype=bool)
    for i, s in enumerate(eng.slugs):
        g = eng.cohorts.get(s)
        if g is None:
            continue
        for ti, t in enumerate(eng.years):
            if eng.usable[i, ti] and t >= g:
                m[i, ti] = True
    return m


def sim_skeleton(eng, gamma):
    gvec = np.array([gamma[t] for t in eng.years])
    return gvec


def sim_panel(eng, gvec, alpha, eps, tau_mat):
    Y = alpha[:, None] + gvec[None, :] + tau_mat + eps
    Y = np.where(eng.usable, Y, np.nan)
    return Y


def scenario_estimates(eng, Y):
    """Seven observed-label cells + four aggregates (type rule, pooled)."""
    obs = eng.obs_lab[None, :]
    out = {}
    for (g, t) in [(2018, 2018), (2018, 2022), (2018, 2024), (2020, 2022),
                   (2020, 2024), (2022, 2022), (2022, 2024)]:
        v, ok = batch_att(eng, obs, g, eng.years.index(t), "type", Y=Y)
        assert bool(ok[0])
        out["att_%d_%d" % (g, t)] = float(v[0])
    for stat in AGG_NAMES:
        out[stat] = observed_stat(eng, stat, Y=Y)
    return out


def ri_p_for_Y(eng, Y, rng, n_valid, stat="theta_2024"):
    obs = observed_stat(eng, stat, Y=Y)
    perm, _att = ri_run(eng, stat, n_valid, rng, Y=Y, batch=640)
    p, _ = ri_pvalue(perm, obs)
    return p


def run_validation(panel, eng, reps, seed, draws_per_rep=500):
    """Scenarios S1-S5 plus the power curve. HARD assertions throughout.

    Bias and estimator-agreement acceptance checks are evaluated on
    antithetic noise pairs: every estimator here is linear in the noise, so
    the pair mean equals the exact expectation and the check is a
    deterministic bug check rather than a coin flip at 500 reps. Raw
    (non-antithetic) rep means are reported alongside.
    """
    results = {"reps": reps, "draws_per_rep": draws_per_rep, "seed": seed}
    checks = []

    def check(name, ok, detail=""):
        checks.append({"name": name, "pass": bool(ok), "detail": detail})
        assert ok, "VALIDATION FAILED: %s %s" % (name, detail)

    # calibration off the real untreated cells
    _alpha, gamma, sigma, n_unt, k_unt = bjs_fit(eng)
    gvec = sim_skeleton(eng, gamma)
    results["calibration"] = {
        "sigma_untreated_twfe_rmse": r2(sigma),
        "n_untreated_cells": n_unt, "n_params": k_unt,
        "gamma": {str(t): r2(gamma[t]) for t in eng.years},
        "county_effect_mean": 60.0, "county_effect_sd": 8.0,
        "note": "year shocks and sigma calibrated to the real untreated "
                "two-way FE fit; missingness mask and cohort labels are the "
                "real ones",
    }

    tp = treated_post_mask(eng)
    ss = np.random.SeedSequence(seed).spawn(8)
    # streams: 0 s1, 1 s2, 2 s3, 3 s4, 4 s5, 5 power, 6 spare, 7 label-check

    def draw_panel(rng, tau_mat):
        alpha = 60.0 + 8.0 * rng.standard_normal(eng.NC)
        eps = sigma * rng.standard_normal((eng.NC, eng.T))
        Yp = sim_panel(eng, gvec, alpha, eps, tau_mat)
        Ym = sim_panel(eng, gvec, alpha, -eps, tau_mat)
        return Yp, Ym

    def tau_const(tau):
        return np.where(tp, tau, 0.0)

    cell_names = ["att_2018_2018", "att_2018_2022", "att_2018_2024",
                  "att_2020_2022", "att_2020_2024", "att_2022_2022",
                  "att_2022_2024"]

    # ---------------- S1: sharp null ----------------
    anti = {k: [] for k in cell_names + AGG_NAMES}
    raw = {k: [] for k in AGG_NAMES}
    rej10 = 0
    rej05 = 0
    rep_ss = ss[0].spawn(reps)
    for r in range(reps):
        r_rngs = rep_ss[r].spawn(2)
        prng = np.random.default_rng(r_rngs[0])
        Yp, Ym = draw_panel(prng, tau_const(0.0))
        ep = scenario_estimates(eng, Yp)
        em = scenario_estimates(eng, Ym)
        for k in anti:
            anti[k].append(0.5 * (ep[k] + em[k]))
        for k in AGG_NAMES:
            raw[k].append(ep[k])
        p = ri_p_for_Y(eng, Yp, np.random.default_rng(r_rngs[1]),
                       draws_per_rep)
        rej10 += p <= 0.10
        rej05 += p <= 0.05
    bias_cells = {k: float(np.mean(anti[k])) for k in cell_names}
    bias_aggs = {k: float(np.mean(anti[k])) for k in AGG_NAMES}
    band10 = [0.10 - 2.576 * math.sqrt(0.09 / reps),
              0.10 + 2.576 * math.sqrt(0.09 / reps)]
    band05 = [0.05 - 2.576 * math.sqrt(0.0475 / reps),
              0.05 + 2.576 * math.sqrt(0.0475 / reps)]
    rr10 = rej10 / float(reps)
    rr05 = rej05 / float(reps)
    check("s1_cells_unbiased", max(abs(v) for v in bias_cells.values()) < 0.5,
          str({k: r2(v) for k, v in bias_cells.items()}))
    check("s1_aggs_unbiased", max(abs(v) for v in bias_aggs.values()) < 0.5,
          str({k: r2(v) for k, v in bias_aggs.items()}))
    check("s1_size_alpha10", band10[0] <= rr10 <= band10[1],
          "rate %.4f band [%.4f, %.4f]" % (rr10, band10[0], band10[1]))
    check("s1_size_alpha05", band05[0] <= rr05 <= band05[1],
          "rate %.4f band [%.4f, %.4f]" % (rr05, band05[0], band05[1]))
    # estimator agreement on the exact expectation (noiseless panel)
    Y0 = sim_panel(eng, gvec, np.full(eng.NC, 60.0), np.zeros((eng.NC, eng.T)),
                   tau_const(0.0))
    cm0 = scenario_estimates(eng, Y0)
    bj0, _s, _g, _n, _k = bjs_aggregates(eng, Y=Y0)
    agree0 = {k: abs(cm0[k] - bj0[k]) for k in AGG_NAMES}
    check("s1_bjs_cellmean_agreement", max(agree0.values()) < 0.1,
          str({k: r4(v) for k, v in agree0.items()}))
    results["s1"] = {
        "bias_cells_antithetic": {k: r2(v) for k, v in bias_cells.items()},
        "bias_aggs_antithetic": {k: r2(v) for k, v in bias_aggs.items()},
        "bias_aggs_raw": {k: r2(float(np.mean(raw[k]))) for k in AGG_NAMES},
        "rejection_rate_alpha10": r4(rr10), "band_alpha10": [r4(band10[0]), r4(band10[1])],
        "rejection_rate_alpha05": r4(rr05), "band_alpha05": [r4(band05[0]), r4(band05[1])],
        "bjs_agreement_noiseless_max_abs": r4(max(agree0.values())),
    }

    # ---------------- S2: constant effect tau = +8 ----------------
    anti = {k: [] for k in AGG_NAMES}
    cover = 0
    rep_ss = ss[1].spawn(reps)
    for r in range(reps):
        r_rngs = rep_ss[r].spawn(2)
        prng = np.random.default_rng(r_rngs[0])
        Yp, Ym = draw_panel(prng, tau_const(8.0))
        ep = scenario_estimates(eng, Yp)
        em = scenario_estimates(eng, Ym)
        for k in AGG_NAMES:
            anti[k].append(0.5 * (ep[k] + em[k]))
        # CI coverage at the true tau: is tau=8 inside the 90% inversion set,
        # i.e. p(tau=8) > 0.10 on the tau-adjusted panel?
        Yadj = Yp.copy()
        Yadj[tp] -= 8.0
        p = ri_p_for_Y(eng, Yadj, np.random.default_rng(r_rngs[1]),
                       draws_per_rep)
        cover += p > 0.10
    bias = {k: float(np.mean(anti[k])) - 8.0 for k in AGG_NAMES}
    coverage = cover / float(reps)
    check("s2_aggs_unbiased", max(abs(v) for v in bias.values()) < 0.5,
          str({k: r2(v) for k, v in bias.items()}))
    check("s2_ci_coverage", 0.85 <= coverage <= 0.95,
          "coverage %.4f" % coverage)
    Y8 = sim_panel(eng, gvec, np.full(eng.NC, 60.0), np.zeros((eng.NC, eng.T)),
                   tau_const(8.0))
    cm8 = scenario_estimates(eng, Y8)
    bj8, _s, _g, _n, _k = bjs_aggregates(eng, Y=Y8)
    agree8 = {k: abs(cm8[k] - bj8[k]) for k in AGG_NAMES}
    check("s2_bjs_cellmean_agreement", max(agree8.values()) < 0.1,
          str({k: r4(v) for k, v in agree8.items()}))
    results["s2"] = {
        "bias_aggs_antithetic": {k: r2(v) for k, v in bias.items()},
        "ci90_coverage": r4(coverage), "coverage_band": [0.85, 0.95],
        "bjs_agreement_noiseless_max_abs": r4(max(agree8.values())),
    }

    # ---------------- S3: dynamic sign flip ----------------
    tau3 = np.zeros((eng.NC, eng.T))
    for i, s in enumerate(eng.slugs):
        g = eng.cohorts.get(s)
        if g is None:
            continue
        for ti, t in enumerate(eng.years):
            if not tp[i, ti]:
                continue
            tau3[i, ti] = 8.0 if t >= 2022 else (-10.0 if t == g else 0.0)
    anti = {k: [] for k in AGG_NAMES}
    twfe_vals = []
    rep_ss = ss[2].spawn(reps)
    for r in range(reps):
        prng = np.random.default_rng(rep_ss[r])
        Yp, Ym = draw_panel(prng, tau3)
        ep = scenario_estimates(eng, Yp)
        em = scenario_estimates(eng, Ym)
        for k in AGG_NAMES:
            anti[k].append(0.5 * (ep[k] + em[k]))
        twfe_vals.append(0.5 * (twfe_static(eng, Y=Yp) + twfe_static(eng, Y=Ym)))
    truths = {"theta_2024": 8.0, "theta_2022": 8.0,
              "theta_step_2018": -10.0, "theta_step_2022": 8.0}
    errs = {k: float(np.mean(anti[k])) - truths[k] for k in AGG_NAMES}
    twfe_mean = float(np.mean(twfe_vals))
    check("s3_era_split_recovery", max(abs(v) for v in errs.values()) < 0.5,
          str({k: r2(v) for k, v in errs.items()}))
    twfe_bias = twfe_mean - 8.0
    check("s3_twfe_material_bias", abs(twfe_bias) > 1.0,
          "twfe %.2f vs +8 truth (post-2022 era)" % twfe_mean)
    results["s3"] = {
        "estimates_antithetic": {k: r2(float(np.mean(anti[k])))
                                 for k in AGG_NAMES},
        "truths": truths, "twfe_static_mean": r2(twfe_mean),
        "twfe_bias_vs_post2022_truth": r2(twfe_bias),
    }

    # ---------------- S4: control-side shock ----------------
    s4 = {}
    shocks = (2.0, 5.0, 8.0)
    s4_ss = ss[3].spawn(len(shocks))
    cpos = [eng.idx[c] for c in CONTROLS]
    tlate = [eng.years.index(2022), eng.years.index(2024)]
    for sk, shock in enumerate(shocks):
        rep_ss = s4_ss[sk].spawn(reps)
        vals = []
        for r in range(reps):
            prng = np.random.default_rng(rep_ss[r])
            Yp, Ym = draw_panel(prng, tau_const(0.0))
            for Yv in (Yp, Ym):
                for c in cpos:
                    for ti in tlate:
                        Yv[c, ti] += shock
            vals.append(0.5 * (observed_stat(eng, "theta_2024", Y=Yp) +
                               observed_stat(eng, "theta_2024", Y=Ym)))
        sp = float(np.mean(vals))
        check("s4_shock_%g" % shock, abs(sp + shock) < 0.5,
              "spurious theta_2024 %.2f for control shock +%g" % (sp, shock))
        s4[str(int(shock))] = r2(sp)
    results["s4"] = {
        "spurious_theta_2024_by_shock": s4,
        # signed: spurious theta_2024 per pp of control-side shock
        # (spurious = -s for shock +s, so the coefficient is -1)
        "per_pp_coefficient": r2(float(np.mean(
            [float(s4[k]) / float(k) for k in s4]))),
        "note": "a level shock of +s pp to both controls in 2022-2024 with "
                "zero treatment effect produces spurious theta_2024 of -s pp, "
                "one for one; the design cannot distinguish a bundle effect "
                "from control-side drift",
    }

    # ---------------- S5: heterogeneous effects ----------------
    devs = {k: [] for k in AGG_NAMES}
    cell_devs = {k: [] for k in cell_names}
    tm_pool = estimates(eng, "type", CONTROLS)
    contributing = {}
    for a in AGG_NAMES:
        contributing[a] = tm_pool["aggs"][a]["counties"]
    cell_members = {"att_%d_%d" % (g, t): sorted(
        c["county"] for c in tm_pool["cells"][(g, t)])
        for (g, t) in tm_pool["cells"]}
    rep_ss = ss[4].spawn(reps)
    for r in range(reps):
        r_rngs = rep_ss[r].spawn(2)
        trng = np.random.default_rng(r_rngs[0])
        tau_i = 8.0 + 3.0 * trng.standard_normal(eng.NC)
        tau_mat = np.where(tp, tau_i[:, None], 0.0)
        prng = np.random.default_rng(r_rngs[1])
        Yp, Ym = draw_panel(prng, tau_mat)
        ep = scenario_estimates(eng, Yp)
        em = scenario_estimates(eng, Ym)
        for a in AGG_NAMES:
            tbar = float(np.mean([tau_i[eng.idx[s]] for s in contributing[a]]))
            devs[a].append(0.5 * (ep[a] + em[a]) - tbar)
        for cn in cell_names:
            tbar = float(np.mean([tau_i[eng.idx[s]] for s in cell_members[cn]]))
            cell_devs[cn].append(0.5 * (ep[cn] + em[cn]) - tbar)
    agg_dev = {k: float(np.mean(devs[k])) for k in AGG_NAMES}
    cell_dev = {k: float(np.mean(cell_devs[k])) for k in cell_names}
    check("s5_aggs_unbiased_for_county_mean",
          max(abs(v) for v in agg_dev.values()) < 0.5,
          str({k: r2(v) for k, v in agg_dev.items()}))
    check("s5_cohort_atts_unbiased_for_cohort_means",
          max(abs(v) for v in cell_dev.values()) < 0.5,
          str({k: r2(v) for k, v in cell_dev.items()}))
    results["s5"] = {
        "agg_minus_county_mean_estimand": {k: r2(v) for k, v in agg_dev.items()},
        "cell_minus_cohort_mean": {k: r2(v) for k, v in cell_dev.items()},
    }

    # ---------------- power curve ----------------
    power = {}
    taus = [3.0, 5.0, 8.0, 12.0]
    pw_ss = ss[5].spawn(len(taus))
    for tix, tau in enumerate(taus):
        rep_ss = pw_ss[tix].spawn(reps)
        hits10 = 0
        hits05 = 0
        for r in range(reps):
            r_rngs = rep_ss[r].spawn(2)
            prng = np.random.default_rng(r_rngs[0])
            Yp, _Ym = draw_panel(prng, tau_const(tau))
            p = ri_p_for_Y(eng, Yp, np.random.default_rng(r_rngs[1]),
                           draws_per_rep)
            hits10 += p <= 0.10
            hits05 += p <= 0.05
        power[str(int(tau))] = {"alpha10": r4(hits10 / float(reps)),
                                "alpha05": r4(hits05 / float(reps))}

    def mde80(alpha_key):
        pts = [(t, float(power[str(int(t))][alpha_key])) for t in taus]
        for (t0, p0), (t1, p1) in zip(pts, pts[1:]):
            if p0 < 0.8 <= p1:
                return r2(t0 + (t1 - t0) * (0.8 - p0) / (p1 - p0))
        if pts[0][1] >= 0.8:
            return "<%g" % taus[0]
        return ">%g" % taus[-1]

    results["power_curve"] = {
        "tau_grid": taus, "power": power,
        "mde_power80_alpha10_interpolated": mde80("alpha10"),
        "mde_power80_alpha05_interpolated": mde80("alpha05"),
    }

    results["assertions"] = checks
    results["all_pass"] = all(c["pass"] for c in checks)
    return results


# ---------------------------------------------------------------------------
# Real-data run: inference + emission
# ---------------------------------------------------------------------------

def real_run(panel, eng, draws, seed, outdir, root):
    ss = np.random.SeedSequence(seed).spawn(8)
    # streams: 0 theta_2024, 1 theta_2022, 2 step_2018, 3 step_2022,
    #          4 pretrend, 5 ci (spawned per grid point), 6-7 reserved

    est_by = {}
    for rule in ("type", "calendar"):
        for vn, ctrls in (("pooled", CONTROLS), ("sf", CONTROLS[:1]),
                          ("slo", CONTROLS[1:])):
            est_by[(rule, vn)] = estimates(eng, rule, ctrls)

    # assert the RI batch machinery reproduces the observed aggregates
    # (the plain-python dual computation ran in main before this)
    for stat in AGG_NAMES:
        assert abs(observed_stat(eng, stat) -
                   est_by[("type", "pooled")]["aggs"][stat]["value"]) < 1e-9

    # structural assertions on the cells (spec section 3)
    tm = est_by[("type", "pooled")]
    got = {k: len(v) for k, v in tm["cells"].items()}
    print("DIAG cells=", got)
    print("DIAG theta_2024 n=", tm["aggs"]["theta_2024"]["n"], tm["aggs"]["theta_2024"]["counties"])
    print("DIAG theta_2022 n=", tm["aggs"]["theta_2022"]["n"], tm["aggs"]["theta_2022"]["counties"])

    # ------------- RI inference -------------
    stats_order = ["theta_2024", "theta_2022", "theta_step_2018",
                   "theta_step_2022", "pretrend"]
    ri = {}
    for k, stat in enumerate(stats_order):
        rng = np.random.default_rng(ss[k])
        if stat == "pretrend":
            obs = observed_stat(eng, "pretrend")
        else:
            obs = est_by[("type", "pooled")]["aggs"][stat]["value"]
        perm, attempts = ri_run(eng, stat, draws, rng)
        p, mc_se = ri_pvalue(perm, obs)
        ri[stat] = {"obs": obs, "p": p, "mc_se": mc_se,
                    "null_sd": float(np.std(perm, ddof=1)),
                    "redraw_rate": 1.0 - draws / float(attempts),
                    "n_valid": draws, "attempts": attempts}
    family = {s: ri[s]["p"] for s in ("theta_2022", "theta_step_2018",
                                      "theta_step_2022")}
    holm_adj = holm(family)

    # ------------- 90% RI CI by test inversion (headline only) -------------
    tp = treated_post_mask(eng)
    ci_ss = ss[5].spawn(len(CI_GRID))
    kept = []
    ci_attempts = 0
    for gi, tau in enumerate(CI_GRID):
        Yadj = eng.Y.copy()
        Yadj[tp] -= tau
        obs_t = observed_stat(eng, "theta_2024", Y=Yadj)
        rng = np.random.default_rng(ci_ss[gi])
        perm, att = ri_run(eng, "theta_2024", CI_DRAWS, rng, Y=Yadj)
        ci_attempts += att
        p, _ = ri_pvalue(perm, obs_t)
        if p > 0.10:
            kept.append(tau)
    assert kept, "90% CI empty on the grid"
    ci_lo, ci_hi = min(kept), max(kept)
    # a bound at the grid edge means the true interval extends beyond the
    # grid; reporting the edge as a genuine bound would silently truncate
    # the CI, so fail loudly and widen CI_GRID instead.
    assert ci_lo > CI_GRID[0] and ci_hi < CI_GRID[-1], (
        "90%% CI [%g, %g] reaches the tau grid edge [%g, %g]; interval "
        "open at the edge, widen CI_GRID" % (ci_lo, ci_hi, CI_GRID[0],
                                             CI_GRID[-1]))
    contiguous = len(kept) == int(round((ci_hi - ci_lo) / 0.5)) + 1
    ci_redraw = 1.0 - (CI_DRAWS * len(CI_GRID)) / float(ci_attempts)

    # ------------- MDEs from the RI null SD -------------
    mde = {}
    for stat in AGG_NAMES:
        sd = ri[stat]["null_sd"]
        mde[stat] = {"alpha10_power80": 2.49 * sd,
                     "alpha05_power80": 2.80 * sd}

    # ------------- pre-trends -------------
    pre = precells_observed(panel)
    print("DIAG n_precells=", len(pre))
    # the RI joint statistic must equal the hand-computable cell mean
    assert abs(ri["pretrend"]["obs"] -
               sum(abs(c["delta_pre"]) for c in pre) / len(pre)) < 1e-9
    pre_mean = sum(c["delta_pre"] for c in pre) / len(pre)
    t1cells = [c for c in pre if c["tier1_cell"]]
    pre_mean_t1 = sum(c["delta_pre"] for c in t1cells) / len(t1cells)
    antic = anticipation_2018(panel)
    pretrend_trigger = (ri["pretrend"]["p"] < 0.10) or (abs(pre_mean_t1) > 3.0)

    # ------------- BJS + TWFE -------------
    bjs_aggs, bjs_sigma, bjs_gamma, n_unt, n_imputed = bjs_aggregates(eng)
    print("DIAG n_unt=", n_unt, "n_imputed=", n_imputed)
    twfe_beta = twfe_static(eng)

    # ------------- robustness grid -------------
    sens_rows, rdetail = robustness_grid(panel, eng, est_by, root)

    # ------------- ASV descriptives -------------
    asv = asv_descriptives(panel, tm)
    print("DIAG asv keys=", list(asv.keys()))
    for k in asv:
        if "rank" in asv[k]:
            print("DIAG asv", k, "rank=", asv[k]["rank"], "n=", asv[k]["n"])

    # ------------- LOO -------------
    loo = rdetail["loo"]

    # ------------- headline pattern selection (spec section 8) -------------
    t24 = tm["aggs"]["theta_2024"]["value"]
    sf24 = est_by[("type", "sf")]["aggs"]["theta_2024"]["value"]
    slo24 = est_by[("type", "slo")]["aggs"]["theta_2024"]["value"]
    p24 = ri["theta_2024"]["p"]
    downgrade = {
        "pretrend_rule": pretrend_trigger,
        "base_rule_sign_flip": rdetail["base_rule_flip"],
        "placebo_in_time": rdetail["placebo_time_trigger"],
    }
    if (sf24 > 0) != (slo24 > 0):
        pattern = "C"
    elif any(downgrade.values()) or t24 <= 0:
        pattern = "D"
    elif p24 <= 0.10:
        pattern = "A"
    else:
        pattern = "B"
    headline = {
        "pattern": pattern,
        "statistic": "theta_2024 (type-matched bases, pooled SF+SLO controls)",
        "X_pooled": r2(t24), "a_vs_sf": r2(sf24), "b_vs_slo": r2(slo24),
        "ri_p": r4(p24), "k_one_in": int(round(1.0 / p24)),
        "ci90": [r2(ci_lo), r2(ci_hi)],
        "mde_alpha05_power80": r2(mde["theta_2024"]["alpha05_power80"]),
        "mde_alpha10_power80": r2(mde["theta_2024"]["alpha10_power80"]),
        "downgrade_triggers": downgrade,
        "single_control_sign_disagreement": (sf24 > 0) != (slo24 > 0),
    }

    # ---------------------------------------------------------------
    # Emission
    # ---------------------------------------------------------------
    os.makedirs(outdir, exist_ok=True)

    # panel.csv
    uy = panel["usable_years"]
    prow = []
    for r in sorted(panel["rows"], key=lambda x: (x["county"], x["year"])):
        s, t = r["county"], r["year"]
        g = panel["cohorts"].get(s)
        bt = bc = ""
        flags = []
        if g is not None and t >= g:
            b1, fb = base_year_py(uy[s], t, g, "type")
            b2, _ = base_year_py(uy[s], t, g, "calendar")
            bt = b1 if b1 is not None else ""
            bc = b2 if b2 is not None else ""
            if fb:
                flags.append("fallback_type")
            if b1 is not None and t - b1 > LONG_GAP:
                flags.append("long_gap_type")
            if b2 is not None and t - b2 > LONG_GAP:
                flags.append("long_gap_calendar")
        prow.append([s, t, r["type"], r2s(r["pct"]), r["ballots"], r["final"],
                     r["confidence"], r["verdict"], r["tier"],
                     g if g is not None else "never",
                     # full adoption year from county_tech.json, so a
                     # hand-verifier sees the same value there; post-window
                     # years (Riverside/San Bernardino 2025) enter no
                     # estimate (EXPECTED_ASV is the in-window map).
                     panel["asv_year_all"].get(s, ""), bt, bc,
                     ";".join(flags)])
    write_csv(os.path.join(outdir, "panel.csv"),
              ["county", "year", "type", "pct", "ballots", "final",
               "confidence", "verdict", "tier", "cohort", "asv_year",
               "base_type_matched", "base_calendar", "flags"], prow)

    # att_matrix.csv
    arow = []
    for rule, rn in (("type", "type-matched"), ("calendar", "calendar")):
        e = est_by[(rule, "pooled")]
        e_sf = est_by[(rule, "sf")]
        e_slo = est_by[(rule, "slo")]
        for (g, t) in sorted(e["cells"]):
            comps = sorted(e["cells"][(g, t)], key=lambda c: c["county"])
            sfd = {c["county"]: c["delta"] for c in e_sf["cells"][(g, t)]}
            slod = {c["county"]: c["delta"] for c in e_slo["cells"][(g, t)]}
            n = len(comps)
            for c in comps:
                fl = []
                if c["fallback"]:
                    fl.append("fallback")
                if c["long_gap"]:
                    fl.append("long_gap")
                arow.append([rn, g, t, "component", c["county"],
                             c["base_year"], r4s(1.0 / n), r2s(c["y_t"]),
                             r2s(c["y_base"]), r2s(c["ctrl_change"]),
                             r2s(c["delta"]), r2s(sfd[c["county"]]),
                             r2s(slod[c["county"]]), ";".join(fl), n])
            arow.append([rn, g, t, "cell_mean",
                         "+".join(c["county"] for c in comps), "", "",
                         "", "", "",
                         r2s(sum(c["delta"] for c in comps) / n),
                         r2s(sum(sfd.values()) / n),
                         r2s(sum(slod.values()) / n), "", n])
    write_csv(os.path.join(outdir, "att_matrix.csv"),
              ["rule", "cohort", "year", "row_type", "county", "base_year",
               "weight", "y_t", "y_base", "ctrl_change", "delta_pooled",
               "delta_sf_only", "delta_slo_only", "flags", "n"], arow)

    # aggregates.csv
    grow = []
    for rule, rn in (("type", "type-matched"), ("calendar", "calendar")):
        e = est_by[(rule, "pooled")]
        for stat in AGG_NAMES:
            a = e["aggs"][stat]
            sfv = est_by[(rule, "sf")]["aggs"][stat]["value"]
            slov = est_by[(rule, "slo")]["aggs"][stat]["value"]
            if rule == "type":
                rp = ri[stat]
                hp = holm_adj.get(stat)
                lo = loo[stat]
                grow.append([stat, rn, a["n"], "+".join(a["counties"]),
                             r2s(a["value"]), r2s(sfv), r2s(slov),
                             r4s(rp["p"]), r4s(rp["mc_se"]),
                             r4s(hp) if hp is not None else "",
                             r4s(rp["redraw_rate"]), r2s(rp["null_sd"]),
                             r2s(2.49 * rp["null_sd"]),
                             r2s(2.80 * rp["null_sd"]),
                             r2s(ci_lo) if stat == "theta_2024" else "",
                             r2s(ci_hi) if stat == "theta_2024" else "",
                             r2s(lo["min"]), r2s(lo["max"]),
                             ";".join(lo["sign_flips"]) or "none"])
            else:
                grow.append([stat, rn, a["n"], "+".join(a["counties"]),
                             r2s(a["value"]), r2s(sfv), r2s(slov),
                             "", "", "", "", "", "", "", "", "", "", "", ""])
    write_csv(os.path.join(outdir, "aggregates.csv"),
              ["statistic", "rule", "n", "counties", "est_pooled", "est_sf_only",
               "est_slo_only", "ri_p", "ri_p_mc_se", "holm_p", "redraw_rate",
               "null_sd", "mde_alpha10_power80", "mde_alpha05_power80",
               "ci90_lo", "ci90_hi", "loo_min", "loo_max",
               "loo_sign_flip_drops"], grow)

    # pretrends.csv
    prw = [[c["county"], c["cohort"], c["year"], c["base_year"],
            c["event_time"], r2s(c["delta_pre"]),
            "yes" if c["tier1_cell"] else "no"]
           for c in sorted(pre, key=lambda c: (c["cohort"], c["county"],
                                               c["year"]))]
    write_csv(os.path.join(outdir, "pretrends.csv"),
              ["county", "cohort", "year", "base_year", "event_time_years",
               "delta_pre", "tier1_cell"], prw)

    # sensitivities.csv
    write_csv(os.path.join(outdir, "sensitivities.csv"),
              ["check", "name", "variant", "statistic", "value", "n", "note"],
              sens_rows)

    # asv_descriptives.csv
    asrow = []
    for val, c in asv["nevada_2018_2022"]["pool"]:
        is_t = c == "nevada-ca"
        asrow.append(["nevada_asv_2018_to_2022", "pool_change", c, r2s(val),
                      asv["nevada_2018_2022"]["rank"] if is_t else "",
                      asv["nevada_2018_2022"]["n"] if is_t else "",
                      r4s(asv["nevada_2018_2022"]["one_sided_p"]) if is_t else "",
                      r4s(asv["nevada_2018_2022"]["min_attainable_p"]) if is_t else "",
                      "ASV adopter" if is_t else ""])
    for val, c in asv["san_diego_2022_2024"]["pool"]:
        is_t = c == "san-diego-ca"
        asrow.append(["san_diego_asv_2022_to_2024", "pool_change", c, r2s(val),
                      asv["san_diego_2022_2024"]["rank"] if is_t else "",
                      asv["san_diego_2022_2024"]["n"] if is_t else "",
                      r4s(asv["san_diego_2022_2024"]["one_sided_p"]) if is_t else "",
                      r4s(asv["san_diego_2022_2024"]["min_attainable_p"]) if is_t else "",
                      "ASV adopter" if is_t else ""])
    for s in sorted(asv["cohort2020_asv_contrast"]["mean_post_delta"]):
        asrow.append(["cohort2020_asv_contrast", "mean_post_delta", s,
                      r2s(asv["cohort2020_asv_contrast"]["mean_post_delta"][s]),
                      "", "", "", "",
                      "bundle+ASV" if s in ("fresno-ca", "los-angeles-ca")
                      else "bundle only"])
    cc = asv["cohort2020_asv_contrast"]
    asrow.append(["cohort2020_asv_contrast", "observed_diff",
                  "fresno+los-angeles minus orange+santa-clara",
                  r2s(cc["obs_diff"]), "", 6, r4s(cc["one_sided_p"]),
                  r4s(cc["min_attainable_p"]),
                  "exact 6-assignment permutation"])
    for val, s in asv["san_bernardino_2024"]["peers"]:
        is_t = s == "san-bernardino-ca"
        asrow.append(["san_bernardino_2024_placement", "night_share_2024", s,
                      r2s(val),
                      asv["san_bernardino_2024"]["rank"] if is_t else "",
                      asv["san_bernardino_2024"]["n"] if is_t else "", "", "",
                      "pure e-pollbook county; descriptive only, no inference"
                      if is_t else ""])
    write_csv(os.path.join(outdir, "asv_descriptives.csv"),
              ["test", "row_type", "unit", "value", "rank", "n_pool",
               "exact_one_sided_p", "min_attainable_p", "note"], asrow)

    # results.json
    cells_out = {}
    for rule in ("type", "calendar"):
        e = est_by[(rule, "pooled")]
        for (g, t), comps in sorted(e["cells"].items()):
            key = "%s|g%d|t%d" % (rule, g, t)
            cells_out[key] = {
                "counties": [c["county"] for c in
                             sorted(comps, key=lambda c: c["county"])],
                "bases": {c["county"]: c["base_year"] for c in comps},
                "deltas": {c["county"]: r2(c["delta"]) for c in comps},
                "mean": r2(sum(c["delta"] for c in comps) / len(comps)),
                "n": len(comps),
            }
    results = {
        "meta": {
            "script": "scripts/analysis/night_share_bundle_did.py",
            "spec": "docs/superpowers/specs/2026-07-09-vca-bundle-model-design.md",
            "seed": seed, "draws": draws, "ci_draws_per_grid_point": CI_DRAWS,
            "ci_grid": [-25.0, 25.0, 0.5], "panel_rows": len(panel["rows"]),
            "treatment": "VCA modernization bundle (vote centers + universal "
                         "mailed ballots + e-pollbooks, adopted as one package)",
        },
        "panel_summary": {
            "n_usable": len(panel["rows"]),
            "n_tier2": sum(1 for r in panel["rows"] if r["tier"] == 2),
            "cohorts": {s: panel["cohorts"][s] for s in sorted(panel["cohorts"])},
            "never_treated_controls": CONTROLS,
            "asv_years_in_window": panel["asv_year"],
        },
        "cells": cells_out,
        "aggregates": {
            stat: {rule: {
                "pooled": r2(est_by[(rule, "pooled")]["aggs"][stat]["value"]),
                "sf_only": r2(est_by[(rule, "sf")]["aggs"][stat]["value"]),
                "slo_only": r2(est_by[(rule, "slo")]["aggs"][stat]["value"]),
                "n": est_by[(rule, "pooled")]["aggs"][stat]["n"],
                "counties": est_by[(rule, "pooled")]["aggs"][stat]["counties"],
            } for rule in ("type", "calendar")} for stat in AGG_NAMES},
        "inference": {
            "meaning_of_p": "adoption was not randomized; the RI p is a "
                            "placebo-calibration benchmark under exchangeability "
                            "of county trajectories, testing the sharp null that "
                            "adoption timing moved no county-year outcome. It is "
                            "evidence against 'no effect plus as-if-random "
                            "timing', not against 'no effect' alone.",
            "headline": {
                "statistic": "theta_2024", "rule": "type-matched",
                "obs": r2(ri["theta_2024"]["obs"]),
                "ri_p": r4(ri["theta_2024"]["p"]),
                "mc_se": r4(ri["theta_2024"]["mc_se"]),
                "redraw_rate": r4(ri["theta_2024"]["redraw_rate"]),
                "null_sd": r2(ri["theta_2024"]["null_sd"]),
                "ci90": {"lo": r2(ci_lo), "hi": r2(ci_hi),
                         "contiguous": contiguous,
                         "draws_per_point": CI_DRAWS,
                         "redraw_rate_mean": r4(ci_redraw)},
                "mde": {k: r2(v) for k, v in mde["theta_2024"].items()},
            },
            "secondary_family_holm": {
                s: {"obs": r2(ri[s]["obs"]), "ri_p": r4(ri[s]["p"]),
                    "holm_p": r4(holm_adj[s]),
                    "mc_se": r4(ri[s]["mc_se"]),
                    "redraw_rate": r4(ri[s]["redraw_rate"]),
                    "null_sd": r2(ri[s]["null_sd"]),
                    "mde": {k: r2(v) for k, v in mde[s].items()}}
                for s in ("theta_2022", "theta_step_2018", "theta_step_2022")},
            "pretrend_joint": {
                "obs_mean_abs": r2(ri["pretrend"]["obs"]),
                "ri_p": r4(ri["pretrend"]["p"]),
                "mc_se": r4(ri["pretrend"]["mc_se"]),
                "redraw_rate": r4(ri["pretrend"]["redraw_rate"])},
        },
        "pretrends": {
            "n_cells": len(pre),
            "mean_all": r2(pre_mean),
            "mean_tier1_only": r2(pre_mean_t1),
            "n_tier1_cells": len(t1cells),
            "largest_abs": [
                {"county": c["county"], "year": c["year"],
                 "delta_pre": r2(c["delta_pre"]),
                 "tier1": c["tier1_cell"]}
                for c in sorted(pre, key=lambda c: -abs(c["delta_pre"]))[:4]],
            "anticipation_2018_cohort": {
                "mean_move_into_final_pre_year": r2(antic["mean"]),
                "n": antic["n"],
                "counties": {r["county"]: r2(r["move"])
                             for r in antic["counties"]}},
            "interpretation_rule_triggered": pretrend_trigger,
        },
        "bjs_imputation": {
            "aggregates": {k: r2(v) for k, v in bjs_aggs.items()},
            "cell_mean_comparison": {k: r2(bjs_aggs[k] -
                                           tm["aggs"][k]["value"])
                                     for k in AGG_NAMES},
            "divergence_flags_gt3pp": rdetail["bjs_divergence_flags"],
            "n_untreated_cells": n_unt,
            "n_imputed_cells": n_imputed,
            "sigma_untreated_rmse": r2(bjs_sigma),
            "san_bernardino_dropped": True,
        },
        "twfe_static_exhibit": {
            "beta_post": r2(twfe_beta),
            "label": "known-biased (Goodman-Bacon forbidden comparisons); "
                     "quarantined; see validation.json S3 for the bias "
                     "quantified on this exact panel",
        },
        "identification_map": {
            "att_2018_2018": "identified off SF+SLO; robustness variant off "
                             "the 8 not-yet-treated comparators",
            "t2024_cells_and_theta_2024": "identified ONLY off SF and SLO; "
                                          "the two controls carry the entire "
                                          "post-AB 37 identification",
            "cohort_2020": "no at-adoption cell (2020 excluded)",
            "cohort_2024_placer": "no cells (zero usable post rows)",
        },
        "asv_descriptives": {
            "nevada_2018_2022": {
                "change": r2(asv["nevada_2018_2022"]["change"]),
                "rank": asv["nevada_2018_2022"]["rank"],
                "n": asv["nevada_2018_2022"]["n"],
                "one_sided_p": r4(asv["nevada_2018_2022"]["one_sided_p"]),
                "min_attainable_p": r4(asv["nevada_2018_2022"]["min_attainable_p"])},
            "san_diego_2022_2024": {
                "change": r2(asv["san_diego_2022_2024"]["change"]),
                "rank": asv["san_diego_2022_2024"]["rank"],
                "n": asv["san_diego_2022_2024"]["n"],
                "one_sided_p": r4(asv["san_diego_2022_2024"]["one_sided_p"]),
                "min_attainable_p": r4(asv["san_diego_2022_2024"]["min_attainable_p"])},
            "cohort2020_contrast": {
                "obs_diff": r2(cc["obs_diff"]),
                "one_sided_p": r4(cc["one_sided_p"]),
                "min_attainable_p": r4(cc["min_attainable_p"])},
            "san_bernardino_2024": {
                "pct": r2(asv["san_bernardino_2024"]["pct"]),
                "rank": asv["san_bernardino_2024"]["rank"],
                "n": asv["san_bernardino_2024"]["n"]},
        },
        "robustness_detail": {
            "sign_disagreement_sf_slo": rdetail["sign_disagreement"],
            "base_rule_flip": rdetail["base_rule_flip"],
            "tier1_theta_2024": r2(rdetail["tier1_theta_2024"]),
            "tier1_move_pp": r2(rdetail["tier1_move"]),
            "bounds_theta_2024": {k: r2(v) for k, v in
                                  rdetail["bounds"].items()},
            "placebo_in_time_mean": r2(rdetail["placebo_in_time"]["mean"]),
            "placebo_in_time_n": rdetail["placebo_in_time"]["n"],
            "placebo_in_time_trigger": rdetail["placebo_time_trigger"],
            "loo": {k: {"min": r2(v["min"]), "max": r2(v["max"]),
                        "min_label": v["min_label"],
                        "max_label": v["max_label"],
                        "sign_flips": v["sign_flips"]}
                    for k, v in loo.items()},
            "nyt_att2018": {rk: {"value": r2(v["value"]),
                                 "never_version": r2(v["never_version"]),
                                 "dropped": v["dropped"]}
                            for rk, v in rdetail["nyt"].items()},
            "size_split": {"median_final": r2(rdetail["size_split"]["median_final"]),
                           "small": rdetail["size_split"]["small"],
                           "large": rdetail["size_split"]["large"],
                           "small_mean": r2(rdetail["size_split"]["small_mean"]),
                           "large_mean": r2(rdetail["size_split"]["large_mean"])},
            "sf_slo_drift_2012_2024": {
                "sf": r2(panel["Y"][("san-francisco-ca", 2024)] -
                         panel["Y"][("san-francisco-ca", 2012)]),
                "slo": r2(panel["Y"][("san-luis-obispo-ca", 2024)] -
                          panel["Y"][("san-luis-obispo-ca", 2012)])},
        },
        "exclusions": sorted(panel["exclusions"],
                             key=lambda e: (e["county"], e["year"])),
        "headline": headline,
    }
    write_text(os.path.join(outdir, "results.json"), jdump(results) + "\n")
    return results


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--draws", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=SEED_DEFAULT)
    ap.add_argument("--validate", action="store_true")
    ap.add_argument("--reps", type=int, default=500)
    ap.add_argument("--outdir", default=None)
    args = ap.parse_args()

    root = repo_root()
    outdir = args.outdir or os.path.join(root, "docs/analysis/generated")
    panel = load_panel(root)
    eng = Engine(panel["Y"], panel["slugs"], YEARS, panel["cohorts"],
                 CONTROLS, FINdict=panel["FIN"])
    for c in CONTROLS:
        assert eng.usable[eng.idx[c]].all()
    dual_computation_check(panel, eng, args.seed)
    print("panel: %d usable rows; dual computation (plain python vs numpy) "
          "agrees to 1e-9" % len(panel["rows"]))

    if args.validate:
        res = run_validation(panel, eng, args.reps, args.seed)
        os.makedirs(outdir, exist_ok=True)
        write_text(os.path.join(outdir, "validation.json"), jdump(res) + "\n")
        print("validation: ALL %d ASSERTIONS PASS" % len(res["assertions"]))
        for c in res["assertions"]:
            print("  PASS %s %s" % (c["name"], c["detail"][:100]))
        return

    res = real_run(panel, eng, args.draws, args.seed, outdir, root)
    h = res["headline"]
    print("theta_2024 (type-matched, pooled) = %s pp; vs SF %s; vs SLO %s" % (
        h["X_pooled"], h["a_vs_sf"], h["b_vs_slo"]))
    print("RI p = %s; 90%% CI [%s, %s]; MDE(0.05, 80%%) = %s pp" % (
        h["ri_p"], h["ci90"][0], h["ci90"][1], h["mde_alpha05_power80"]))
    print("wording pattern: %s" % h["pattern"])


if __name__ == "__main__":
    main()
