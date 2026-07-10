# County Panel Expansion: Controls, Sample Size, and a Definitive Effect Estimate

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Grow the cross-county election-night dataset from 14 jurisdictions (1 control) to ~19 (6 controls), fill the highest-value pre-adoption gaps, and build a panel estimator that can state the e-pollbook/ASV effect on election-night share with a defensible confidence interval.

**Architecture:** Three thrusts. (1) A CA-58 adoption census (from EAVS + CA SoS records) turns control selection from guesswork into data, and 5 verified never-adopter counties are then researched exactly like the existing adopters via the established runbook. (2) A triage pass re-attacks the existing adopters' missing pre-adoption cells with techniques learned after those rows were first researched. (3) A dependency-free matched-years difference-in-differences estimator with jackknife CIs, placebo tests, mechanism splits (e-pollbook vs ASV), and an MDE/scenario mode quantifies exactly what each new data point buys.

**Tech Stack:** Python 3 stdlib only (no new dependencies), pytest, the existing research pipeline (`scripts/research/*`, `scripts/build_county_night.py`), the `researching-election-night-share` and `researching-jurisdiction-counting-tech` skills.

## Global Constraints

- `docs/research/RUNBOOK.md` is law for all research tasks. When this plan and the runbook disagree, the runbook wins.
- The metric is the election-night PLATEAU share (runbook section 1). Percent units, 2dp max, never a 0.x fraction.
- Denominators come from the CA SoS Statement of Vote only (runbook 6.1). 2020 is excluded everywhere. `comparable: false` conventions per runbook 5.2.
- No public-records requests (CPRA is ruled out for this project). Automated/public sources only: archives, EAVS, SoS, CalVoter, county sites, news.
- After ANY data change, run the full pipeline from runbook section 3; everything must pass before commit.
- Never hand-edit derived files (`packages/data/county_night.json`, `county_tech.json`, `MACHINE_CHECK.md`, `HUMAN_VERIFY.md`).
- Research subagents persist findings to disk after EACH item, batch 1-2 elections per subagent (runbook section 9).
- No em dashes in any prose written (commit messages, notes, docs). Use comma/colon/parens.
- Elections in scope: November generals 2012-2024, excluding 2020.
- Every research finding records its exact locating query, retrieval URL, and in-page location, copy-pasteable; dead ends too.

## Current state (baseline the plan starts from)

Panel coverage (ok = comparable point, ceil = comparable:false ceiling, null = documented dead end or not researched, ---- = no row):

```
county           2012 2014 2016 2018 2022 2024   adoption (epb/asv)
San Francisco      ok   ok   ok   ok   ok   ok   control
Fresno           null null   ok null null   ok   e2020/a2020
Los Angeles        ok   ok   ok   ok   ok   ok   e2020/a2020
Madera           null null   ok   ok   ok   ok   e2018
Napa               ok   ok   ok   ok   ok   ok   e2018
Nevada             ok   ok   ok   ok   ok ceil   e2018/a2022
Orange             ok   ok   ok   ok   ok   ok   e2020
Placer           null   ok   ok ceil null null   e2024
Riverside        null null null null   ok ceil   e2022/a2025
Sacramento         ok   ok null   ok   ok   ok   e2018
San Bernardino   null null null null null   ok   e2020/a2025
San Diego        null null null   ok   ok   ok   e2022/a2024
San Mateo          ok   ok   ok   ok   ok   ok   e2018
Santa Clara        ok ceil null null   ok   ok   e2020
```

Statistical baseline (computed 2026-07-10 from `county_night.json`): 10 adopter counties have usable pre+post points; raw mean effect -8.0 pp (SE 3.3); SF control change -13.5 pp over the same window; crude DiD +5.6 pp (SE 4.5, 95% CI [-3.8, +14.9]). With one control county the control-noise floor alone caps the minimum detectable effect at ~8 pp. The plan attacks: control count (floor drops to ~5-6 pp with 5 controls), per-county point count, and estimator efficiency.

## Why these design choices (the "creative signal" levers, so executors do not undo them)

1. **Matched-years DiD, not naive pre/post.** Each treated county's change is benchmarked against the mean control change over the SAME calendar years the county itself was observed. This absorbs statewide year shocks (VCA rollout, AB 3184 certification rules, turnout composition) without needing a parametric model.
2. **Mechanism split.** E-pollbooks act on election-day check-in; ASV acts on VBM processing. Several counties adopted them in different years (Nevada e2018/a2022, San Diego e2022/a2024, Riverside e2022/a2025), which separates the two effects within-county. The estimator takes `--mechanism epb|asv|any`.
3. **VCA-but-never-EPB controls.** The biggest confound is the 2018-2020 Voter's Choice Act all-mail shift, collinear with most adoption dates. A control county that went VCA but never adopted e-pollbooks/ASV isolates the VCA effect directly. Task 3's selection rubric requires at least one such county if the census finds any.
4. **Placebo tests.** Assigning fake adoption years to control counties must produce ~0. This is the cheapest credibility check a reviewer can ask for.
5. **Jackknife inference.** Leave-one-county-out over all counties. Honest about small-N, no distributional assumptions, dependency-free.
6. **Scenario mode.** Before spending research effort, the estimator projects the MDE for "+k controls, +m elections per county", so data collection stops when the CI is good enough rather than when the worklist is empty.

Deliberately deferred (documented as follow-ons in Task 7, not built now): out-of-state jurisdictions (breaks VCA collinearity best but needs new denominator playbooks per state), June primaries (doubles the panel but changes the metric's composition), and the canvass-speed alternative outcome (CalVoter week-after data plus Wayback recovery of pre-2022 canvass states).

---

### Task 1: Panel estimator with tests

**Files:**
- Create: `scripts/research/estimate_tech_effect.py`
- Test: `tests/test_estimate_tech_effect.py`

**Interfaces:**
- Consumes: `packages/data/county_night.json` (existing schema: `jurisdictions[]` with `name`, `slug`, `control`, `adoption{epollbook,asv}`, `points[]` with `year`, `type`, `pct`, `comparable`).
- Produces: module functions `load_panel(path) -> list[dict]`, `estimate(panel, mechanism) -> dict`, `jackknife(panel, mechanism) -> dict`, `placebo(panel, fake_year) -> dict`, `scenario(panel, mechanism, n_controls, n_elections) -> float`. CLI: `python3 scripts/research/estimate_tech_effect.py [--mechanism any|epb|asv] [--placebo] [--scenario K M] [--json]`. Task 7 consumes the CLI output.

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_estimate_tech_effect.py
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts" / "research"))
from estimate_tech_effect import (load_panel, estimate, jackknife, placebo,
                                  scenario)


def synth(tmp_path, effect=-10.0, year_drift=-2.0, noise=None):
    """county_night.json-shaped synthetic data. Two treated counties adopt
    e-pollbooks in 2018; two controls never adopt. pct = 60 + county offset
    + year_drift per year-index + effect on treated post rows. noise, if
    given, is a dict {(slug, year): delta} added on top."""
    years = [2012, 2014, 2016, 2018, 2022, 2024]
    juris = []
    for i, (slug, treated) in enumerate(
            [("t1", True), ("t2", True), ("c1", False), ("c2", False)]):
        pts = []
        for k, y in enumerate(years):
            pct = 60.0 + i * 3 + year_drift * k
            if treated and y >= 2018:
                pct += effect
            pct += (noise or {}).get((slug, y), 0.0)
            pts.append({"year": y, "type": "midterm", "pct": round(pct, 2),
                        "comparable": True})
        juris.append({"name": slug, "slug": slug, "control": not treated,
                      "adoption": {"epollbook": 2018 if treated else None,
                                   "asv": None},
                      "points": pts})
    p = tmp_path / "cn.json"
    p.write_text(json.dumps({"jurisdictions": juris}))
    return p


def test_load_panel_excludes_2020_and_noncomparable(tmp_path):
    p = synth(tmp_path)
    data = json.loads(p.read_text())
    data["jurisdictions"][0]["points"].append(
        {"year": 2020, "type": "presidential", "pct": 30.0, "comparable": True})
    data["jurisdictions"][0]["points"].append(
        {"year": 2022, "type": "midterm", "pct": 99.0, "comparable": False})
    p.write_text(json.dumps(data))
    panel = load_panel(p)
    t1_years = sorted(r["year"] for r in panel if r["slug"] == "t1")
    assert 2020 not in t1_years
    assert t1_years.count(2022) == 1  # the comparable one only


def test_estimate_recovers_known_effect_despite_year_drift(tmp_path):
    panel = load_panel(synth(tmp_path, effect=-10.0, year_drift=-2.0))
    res = estimate(panel, mechanism="epb")
    # naive pre/post would report -10 + drift; matched-years DiD must not
    assert abs(res["effect"] - (-10.0)) < 1e-9
    assert res["n_treated"] == 2
    assert res["n_controls"] == 2


def test_jackknife_zero_se_on_noiseless_data(tmp_path):
    panel = load_panel(synth(tmp_path))
    jk = jackknife(panel, mechanism="epb")
    assert jk["se"] < 1e-9
    assert jk["ci95"][0] <= jk["effect"] <= jk["ci95"][1]


def test_placebo_is_zero_on_controls(tmp_path):
    panel = load_panel(synth(tmp_path))
    res = placebo(panel, fake_year=2018)
    assert abs(res["effect"]) < 1e-9


def test_mechanism_filter_uses_matching_adoption_year(tmp_path):
    p = synth(tmp_path)
    data = json.loads(p.read_text())
    # t2 adopts ASV in 2022 as well; asv mechanism must split on 2022 for t2
    data["jurisdictions"][1]["adoption"]["asv"] = 2022
    p.write_text(json.dumps(data))
    panel = load_panel(p)
    res = estimate(panel, mechanism="asv")
    assert res["n_treated"] == 1  # only t2 has an asv adoption year


def test_scenario_mde_decreases_with_more_controls(tmp_path):
    noise = {("c1", 2014): 4.0, ("c2", 2018): -3.0, ("t1", 2016): 2.0,
             ("t2", 2022): -2.5, ("c1", 2024): 1.5}
    panel = load_panel(synth(tmp_path, noise=noise))
    mde_now = scenario(panel, "epb", n_controls=2, n_elections=6)
    mde_more = scenario(panel, "epb", n_controls=8, n_elections=6)
    assert mde_more < mde_now
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_estimate_tech_effect.py -q`
Expected: FAIL with `ModuleNotFoundError: No module named 'estimate_tech_effect'`.

- [ ] **Step 3: Implement the estimator**

```python
# scripts/research/estimate_tech_effect.py
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
        return {"effect": full["effect"], "se": None, "ci95": (None, None)}
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
    out = {"mechanism": args.mechanism, **jackknife(panel, args.mechanism)}
    out["per_county"] = estimate(panel, args.mechanism)["per_county"]
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_estimate_tech_effect.py -q`
Expected: 6 passed.

- [ ] **Step 5: Run against the real panel and sanity-check**

Run: `python3 scripts/research/estimate_tech_effect.py --mechanism any --placebo --scenario 6 6`
Expected: `effect` within 1 pp of +5.6 (the hand-computed crude DiD; the matched-years weighting differs slightly), `n_treated` 10, `n_controls` 1, a finite `se`, and a placebo of `None`/0-treated (only 1 control exists today, so the placebo split has an empty side; that is acceptable until Task 4 lands controls). Paste the output into the commit message body.

- [ ] **Step 6: Commit**

```bash
git add scripts/research/estimate_tech_effect.py tests/test_estimate_tech_effect.py
git commit -m "feat(research): matched-years DiD estimator for the county tech effect"
```

---

### Task 2: CA-58 adoption census

**Files:**
- Create: `data/research/county-tech/ca_adoption_census.json`
- Create: `scripts/research/validate_adoption_census.py`
- Test: `tests/test_adoption_census.py`

**Interfaces:**
- Consumes: nothing from other tasks. Sources: EAVS per-jurisdiction datasets 2016-2024 (eac.gov "EAVS Datasets", the pollbook-technology questions), CA SoS voting-technology / systems-in-use pages, the VCA participating-counties list (sos.ca.gov), CalVoter ballot-processing pages, and the 14 existing `data/research/county-tech/<slug>.json` records.
- Produces: one census row per CA county (58 exactly) with schema below. Task 3 consumes `status == "never"` rows.

Census row schema:

```json
{
  "county": "Kern",
  "slug": "kern-ca",
  "epollbook_year": null,
  "asv_year": null,
  "vca_year": 2022,
  "status": "never",
  "confidence": "high",
  "sources": ["https://..."],
  "note": "EAVS 2016-2024 report no e-pollbooks; SoS systems page lists paper rosters as of 2024. Locating query: ..."
}
```

`status`: `"adopter"` (epollbook_year or asv_year set), `"never"` (confirmed no EPB and no ASV through Nov 2024), `"unknown"` (conflicting or missing evidence). `confidence` applies to the status call. Every row needs at least one source URL and a note with the locating query (reproducible-provenance rule).

- [ ] **Step 1: Write the failing validator test**

```python
# tests/test_adoption_census.py
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
CENSUS = ROOT / "data" / "research" / "county-tech" / "ca_adoption_census.json"
VALIDATOR = ROOT / "scripts" / "research" / "validate_adoption_census.py"


def test_census_exists_and_validator_passes():
    assert CENSUS.exists(), "census file missing"
    r = subprocess.run([sys.executable, str(VALIDATOR)],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr


def test_census_has_58_unique_counties():
    rows = json.loads(CENSUS.read_text())
    assert len(rows) == 58
    assert len({r["slug"] for r in rows}) == 58
```

(The adopter-years cross-check against the researched county-tech records lives in the validator, where failures list one line per mismatch; the test delegates to it via `test_census_exists_and_validator_passes`.)

- [ ] **Step 2: Write the validator**

```python
# scripts/research/validate_adoption_census.py
"""Validate ca_adoption_census.json: 58 CA counties, schema, and agreement
with the researched county-tech records. Exit 1 with one line per failure."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CENSUS = ROOT / "data" / "research" / "county-tech" / "ca_adoption_census.json"
STATUSES = {"adopter", "never", "unknown"}
CONFS = {"high", "medium", "low"}

fails = []
rows = json.loads(CENSUS.read_text())
if len(rows) != 58:
    fails.append(f"expected 58 counties, got {len(rows)}")
slugs = [r["slug"] for r in rows]
if len(set(slugs)) != len(slugs):
    fails.append("duplicate slugs")
for r in rows:
    ctx = r.get("slug", "?")
    for field in ("county", "slug", "status", "confidence", "sources", "note"):
        if not r.get(field):
            fails.append(f"{ctx}: missing {field}")
    if r.get("status") not in STATUSES:
        fails.append(f"{ctx}: bad status {r.get('status')!r}")
    if r.get("confidence") not in CONFS:
        fails.append(f"{ctx}: bad confidence")
    has_year = bool(r.get("epollbook_year") or r.get("asv_year"))
    if r.get("status") == "adopter" and not has_year:
        fails.append(f"{ctx}: adopter without an adoption year")
    if r.get("status") == "never" and has_year:
        fails.append(f"{ctx}: never-adopter with an adoption year")

# cross-check against researched per-county tech records
tech_dir = ROOT / "data" / "research" / "county-tech"
by_slug = {r["slug"]: r for r in rows}
for f in tech_dir.glob("*-ca.json"):
    rec = json.loads(f.read_text())
    slug = rec.get("slug") or f.stem
    if slug in by_slug and by_slug[slug]["status"] == "unknown":
        fails.append(f"{slug}: researched record exists but census says unknown")

for line in fails:
    print(line)
sys.exit(1 if fails else 0)
```

(Adapt the cross-check to the actual per-county tech record schema after reading one, e.g. `data/research/county-tech/napa-ca.json`; the census's adoption years for the 14 researched counties must match the researched records' years, and mismatches are failures listed one per line.)

- [ ] **Step 3: Run the test to verify it fails**

Run: `uv run pytest tests/test_adoption_census.py -q`
Expected: FAIL (census file missing).

- [ ] **Step 4: Research and write the census (subagent work)**

Dispatch research subagents (2-3 in parallel, ~20 counties each, appending to a shared scratch file per runbook section 9). Route order per county: (1) EAVS per-jurisdiction CSV, pollbook question columns, editions 2016/2018/2022/2024 (a county reporting e-pollbooks in an edition brackets its adoption year); (2) CA SoS voting-systems/technology pages; (3) county registrar site + local news for the specific year; (4) the existing 14 researched records take precedence where they exist. ASV evidence is rarer: CalVoter ballot-processing notes, vendor press releases (Runbeck, DFM), county budget documents via plain web search. Where EPB status is clear but ASV is unknown, `status` may still be `"never"` only if ASV absence is positively supported; otherwise `"unknown"` with the EPB finding in the note.

- [ ] **Step 5: Run the validator and tests until they pass**

Run: `python3 scripts/research/validate_adoption_census.py && uv run pytest tests/test_adoption_census.py -q`
Expected: exit 0, 2 passed.

- [ ] **Step 6: Commit**

```bash
git add data/research/county-tech/ca_adoption_census.json \
        scripts/research/validate_adoption_census.py tests/test_adoption_census.py
git commit -m "feat(research): CA-58 e-pollbook/ASV adoption census"
```

---

### Task 3: Select 5 control counties

**Files:**
- Modify: `data/research/county-tech/worklist.json` (append control entries)
- Create: `docs/research/control-selection-2026-07.md`

**Interfaces:**
- Consumes: `ca_adoption_census.json` from Task 2 (`status == "never"`, confidence high/medium).
- Produces: 5 worklist entries shaped like the existing ones plus `"role": "control"`, e.g. `{"slug": "kern-ca", "name": "Kern County", "state": "CA", "role": "control", "hints": "never-adopter per census; non-VCA"}`. Task 4 researches exactly these 5.

- [ ] **Step 1: Score the candidates**

For every census `never` row, probe archive viability (this decides whether night counts are recoverable BEFORE we commit research effort):

```bash
# Clarity presence (best evidence source): county ENR on the Clarity CDN?
curl -s "https://results.enr.clarityelections.com/CA/<County>/current_ver.txt"
# Wayback capture density around two election nights:
curl "http://web.archive.org/cdx/search/cdx?url=<county results url>&from=20161101&to=20161201&output=json&limit=40"
curl "http://web.archive.org/cdx/search/cdx?url=<county results url>&from=20181101&to=20181201&output=json&limit=40"
```

Score each candidate 0-2 on: Clarity presence, Wayback density 2012-2018, registrar press-release archive (runbook 6.2), county size tier, and confound value (VCA-but-never-EPB scores 2). Record every probe command and result in the memo.

- [ ] **Step 2: Pick 5 with the diversity rubric**

Requirements: at least 1 large county (>400k ballots), at least 1 small (<100k), at least 2 non-VCA counties, and at least 1 VCA-but-never-EPB county if the census found any (this is the highest-value control in the design; see plan header lever 3). Break ties by archive score.

- [ ] **Step 3: Write the memo and worklist entries**

`docs/research/control-selection-2026-07.md`: the scored table (all candidates, not just winners), the rubric, the probe evidence per candidate, and one line per rejected near-miss saying why. Append the 5 winners to `worklist.json` with `"role": "control"`.

- [ ] **Step 4: Validate and commit**

Run: `python3 -c "import json; json.load(open('data/research/county-tech/worklist.json'))"` (well-formed), then:

```bash
git add data/research/county-tech/worklist.json docs/research/control-selection-2026-07.md
git commit -m "feat(research): select 5 control counties for the tech-effect panel"
```

---

### Task 4: Research the 5 control counties (repeat this checklist once per county)

**Files (per county `<slug>`):**
- Create: `data/research/county-tech/<slug>.json` (tech record confirming never-adopter status)
- Create: `data/research/election-night/<slug>.json` (night-share rows)
- Modify: `data/research/election-night/VERIFY.md`, `data/research/election-night/plateau_review.json`
- Regenerate: `packages/data/county_night.json`, `county_tech.json`, `MACHINE_CHECK.md`, `HUMAN_VERIFY.md`

**Interfaces:**
- Consumes: the Task 3 worklist entries (`role: "control"`).
- Produces: election-night rows for Nov generals 2012-2024 (skip 2020) per the runbook section 2 schema, with `vs_epollbook: "n/a"` and `vs_asv: "n/a"` on every row (control counties have no adoption), and the jurisdiction appearing in `county_night.json` with `"control": true` alongside San Francisco. Confirm how `build_county_night.py` decides the control flag before writing (read the script; if control status derives from adoption-years-absent, no change is needed; if SF is hard-coded as the only control, extend the script so any jurisdiction with no adoption years and a tech record concluding never-adopter is marked `control: true`, and add a unit test for that rule in `tests/test_verify_election_night.py`'s style).

This is the established two-skill procedure. Execute per county, in this order:

- [ ] **Step 1: Tech record** via the `researching-jurisdiction-counting-tech` skill: confirm the census's never-adopter call with county-level evidence (the census row is a lead, not proof). If the county turns out to be an adopter after all, STOP for this county, update the census row (status/years/note per Task 2 schema), rerun `validate_adoption_census.py`, and report to the controller: Task 3's rubric picks a replacement from the memo's next-ranked candidate.
- [ ] **Step 2: Denominators** for 2012-2024 Nov generals (skip 2020) from the SoS SoV PDFs (runbook 6.1).
- [ ] **Step 3: Night counts** per election via runbook routes 6.2 through 6.6, capturing plateau evidence (runbook section 8) as you go. Batch 1-2 elections per subagent; persist after each (runbook section 9). Null rows per runbook 5.1 where nothing survives; ceilings/floors per 5.2.
- [ ] **Step 4: Write the dataset rows** (runbook section 2 schema, section 10 steps 4-6: county JSON + VERIFY.md section + plateau verdicts).
- [ ] **Step 5: Full pipeline** (runbook section 3), all green:

```bash
python3 scripts/research/validate_election_night.py
python3 scripts/build_county_night.py
python3 scripts/research/verify_en_denominators.py
python3 scripts/research/verify_en_numerators.py
python3 scripts/research/build_en_verification_report.py
uv run pytest tests/test_verify_election_night.py -q
pnpm vitest run
```

- [ ] **Step 6: Re-run the estimator** and record the CI movement in the commit body:

```bash
python3 scripts/research/estimate_tech_effect.py --mechanism any
```

- [ ] **Step 7: Commit** (one commit per county, runbook section 10 step 8 file list), then report to the human per runbook section 10 step 9: which rows are non-CONFIRMED or secondary, with paths + claimed values + fail criteria.

```bash
git add data/research/county-tech/<slug>.json data/research/election-night/<slug>.json \
        data/research/election-night/VERIFY.md data/research/election-night/plateau_review.json \
        packages/data/county_night.json packages/data/county_tech.json \
        data/research/election-night/MACHINE_CHECK.md data/research/election-night/HUMAN_VERIFY.md
git commit -m "feat(research): <County> control county, night shares 2012-2024"
```

---

### Task 5: Gap-fill triage on the existing adopters

**Files:**
- Create: `docs/research/gap-triage-2026-07.md`
- Modify (only where re-research succeeds): the county JSONs, `VERIFY.md`, `plateau_review.json`, regenerated derived files (same set as Task 4).

**Interfaces:**
- Consumes: the 17 null/ceiling cells listed below; the runbook's newest techniques (7.2 full-version-list bracketing, 7.4 render overrides) which postdate some of the original research.
- Produces: recovered rows (same schema/pipeline as Task 4) and a triage memo recording, for every cell, KEEP-NULL (dead end confirmed) or RECOVERED.

The 17 cells, highest value first (pre-adoption cells directly extend treated counties' pre periods):

| county | cells | why it matters |
|---|---|---|
| Riverside | 2012, 2014, 2016, 2018 (all pre-e2022) | currently contributes nothing (0 pre points) |
| San Bernardino | 2012, 2014, 2016, 2018 (all pre-e2020) | currently contributes nothing |
| San Diego | 2012, 2014, 2016 (pre-e2022) | 1 pre point today |
| Santa Clara | 2016, 2018 (pre-e2020) + 2014 ceiling | 1 pre point today |
| Sacramento | 2016 (pre-e2018) | 2 pre points today |
| Fresno | 2012, 2014 (pre), 2018, 2022 | 1 pre + 1 post today |
| Madera | 2012, 2014 (pre-e2018) | 1 pre point today |
| Nevada | 2024 ceiling (post) | ceiling excluded from comparisons |
| Placer | 2012 (pre), 2022 (pre-e2024) | post-2024 period needs the Nov 2026 general (future; note it, do not research it) |

- [ ] **Step 1: Triage every cell from its existing note.** Each null row's note documents what was searched (runbook 5.1). Classify: (a) all routes exhausted including Clarity full-version bracketing and puppeteer rendering: KEEP-NULL, one memo line quoting the note's dead-end evidence; (b) a route was not tried or predates a technique (the Santa Clara 2024 recovery via the 7.2 bracket trick shows old "unrecoverable" calls can fall): RE-RESEARCH.
- [ ] **Step 2: Re-research the RE-RESEARCH subset**, hard-capped at ~30 minutes of agent effort per cell (runbook 6.7: do not burn hours on a bot-wall). Same evidence, schema, and pipeline rules as Task 4 steps 3-5.
- [ ] **Step 3: Write `docs/research/gap-triage-2026-07.md`**: one line per cell (KEEP-NULL with reason, or RECOVERED with the new value and evidence class), so the next person never re-triages from scratch.
- [ ] **Step 4: Full pipeline + estimator delta + commit** (as Task 4 steps 5-7, one commit for the triage memo plus one per county whose rows changed).

---

### Task 6: Placer post-period placeholder check (5 minutes, calendar-gated)

**Files:** none now.

The Nov 2026 general (2026-11-03) is Placer's first post-e-pollbook data point and also adds a post-2024 point for every county. This task exists so the plan's Definition of Done does not silently depend on future data: confirm `docs/research/RUNBOOK.md` needs no change to accommodate 2026 rows (it does not; the year list in section 10 is illustrative), and add one line to `docs/research/gap-triage-2026-07.md`: "Nov 2026 general: collect for all panel counties once certified (SoS SoV publishes ~Dec 2026)." No other action.

---

### Task 7: Run the analysis and write the findings doc

**Files:**
- Create: `docs/analysis/<today's date, YYYY-MM-DD>-tech-effect-estimate.md` (substitute the actual date the doc is written, matching the directory's naming convention)

**Interfaces:**
- Consumes: the final panel (Tasks 4-5 landed), the Task 1 estimator CLI.

- [ ] **Step 1: Run the full estimator battery**

```bash
python3 scripts/research/estimate_tech_effect.py --mechanism any --placebo --json
python3 scripts/research/estimate_tech_effect.py --mechanism epb --json
python3 scripts/research/estimate_tech_effect.py --mechanism asv --json
python3 scripts/research/estimate_tech_effect.py --scenario 6 6 --json
python3 scripts/research/estimate_tech_effect.py --scenario 10 8 --json
```

- [ ] **Step 2: Write the analysis doc** with: the panel inventory (counties, points, controls); the headline estimate + jackknife CI per mechanism; the placebo result (must be reported even if embarrassing); per-county effects table (San Diego's positive outlier discussed, not hidden); the confound discussion (VCA collinearity, what the VCA-never-EPB control shows); the MDE now vs the plan's baseline (~8 pp floor with 1 control); and the decision gate:
  - CI excludes 0 → the measured effect is the finding; propose chart/article updates as follow-on.
  - CI includes 0 and MDE > |point estimate| → recommend the named follow-ons with projected MDE from scenario mode: out-of-state jurisdictions (PA/NY/WI leads in `data/research/county-tech/`), June primaries expansion, canvass-speed alternative outcome (CalVoter 2022+ plus Wayback recovery of earlier canvass states from the existing capture cache).
- [ ] **Step 3: Commit**

```bash
git add docs/analysis/<today's date>-tech-effect-estimate.md
git commit -m "docs: tech-effect estimate from the expanded county panel"
```

---

## Definition of Done

- Estimator committed with 6 passing tests; runs against the live panel.
- Census: 58 rows, validator exit 0, cross-checked against the 14 researched counties.
- 5 control counties fully researched (or explicitly replaced via the Task 4 Step 1 escape hatch), every new row through the full runbook pipeline, human-verification packet regenerated.
- Gap triage memo covers all 17 cells; every RECOVERED row pipeline-clean.
- Analysis doc states the effect, CI, placebo, and the go/no-go on follow-on data collection.
- Nothing in this plan hand-edited a derived file, filed a records request, or used an em dash.
