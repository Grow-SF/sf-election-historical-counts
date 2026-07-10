import json
import subprocess
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
