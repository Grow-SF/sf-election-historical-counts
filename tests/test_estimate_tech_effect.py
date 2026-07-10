import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts" / "research"))
from estimate_tech_effect import (load_panel, estimate, jackknife, placebo,
                                  scenario)


def synth(tmp_path, effect=-10.0, year_drift=-2.0, noise=None,
          primary_shift=None, primary_coverage=None):
    """county_night.json-shaped synthetic data. Two treated counties adopt
    e-pollbooks in 2018; two controls never adopt. pct = 60 + county offset
    + year_drift per year-index + effect on treated post rows. noise, if
    given, is a dict {(slug, year): delta} added on top.

    primary_shift/primary_coverage add a SECOND (year, type) cell in some
    years: when primary_shift is given, primary_coverage (dict slug -> set of
    years) lists which (slug, year) pairs also get a "primary"-typed row,
    valued at that year's general-row pct minus primary_shift (primaries run
    below generals). Coverage is deliberately uneven across counties -- this
    is what a real primary-election panel looks like once SF starts
    contributing primary points but researched counties mostly don't (yet).
    Every existing caller that omits these two args gets exactly the old
    single-type-per-year data, unchanged."""
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
            if primary_shift is not None and y in (primary_coverage or {}).get(slug, ()):
                pts.append({"year": y, "type": "primary",
                            "pct": round(pct - primary_shift, 2),
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


def test_estimate_recovers_effect_with_type_shifted_uneven_primary_coverage(tmp_path):
    """Cell-matching test: t1 is a treated county with NO primary rows at
    all. Both matched controls (c1, c2) carry general rows every year; c1
    ALSO carries a primary row (shifted 15 points below its general row) in
    2016, one of t1's pre years. c2 has no primary rows.

    Pure year-matching (the old _control_change) would fold c1's 2016
    primary row into c1's pre-period average for that year (year 2016 is in
    the pre-year set regardless of type), pulling the control-side change
    down and mis-recovering the effect. Hand-verified by reasoning through
    both code paths (see report): year-only matching yields effect_t1 =
    -12.125 for this panel; a temporary run of the pre-cell-matching
    _control_change against this exact synthetic panel was used to confirm
    that number before this test was written. Cell-matching must instead use
    only the (year, type) cells t1 actually has (general-only, since t1 has
    no primary rows) when averaging each control's pre/post change, which
    excludes c1's 2016 primary row and recovers the injected effect (-10.0)
    exactly."""
    panel = load_panel(synth(
        tmp_path, effect=-10.0, year_drift=-2.0, primary_shift=15.0,
        primary_coverage={"t2": {2016, 2022}, "c1": {2016}}))
    res = estimate(panel, mechanism="epb")
    assert res["n_treated"] == 2
    assert res["n_controls"] == 2
    # t1 has no primary rows at all -- every matched control cell is general-
    # only, so cell-matching must recover the injected effect exactly.
    assert abs(res["per_county"]["t1"] - (-10.0)) < 1e-9
    # t2 has primaries in a pre year (2016) and a post year (2022), neither
    # of which is fully mirrored by both controls (c1 only has 2016, c2 has
    # none) -- the estimator must still compute a finite, sane result for it
    # rather than crashing on the uneven intersection.
    assert res["per_county"]["t2"] is not None
    assert -30.0 < res["per_county"]["t2"] < 0.0


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


def test_cli_json_reports_counts(tmp_path):
    p = synth(tmp_path)
    r = subprocess.run(
        [sys.executable,
         str(Path(__file__).parent.parent / "scripts" / "research" /
             "estimate_tech_effect.py"),
         "--path", str(p), "--mechanism", "epb", "--json"],
        capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    out = json.loads(r.stdout)
    assert out["n_treated"] == 2
    assert out["n_controls"] == 2
    assert "mde" in out and "n_replicates" in out
