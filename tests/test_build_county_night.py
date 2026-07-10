import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from build_county_night import load_sf, norm_type, SF_PRIMARY_DATES, load_vca_years


# ---- norm_type: type vocabulary -------------------------------------------

def test_norm_type_generals_unchanged():
    assert norm_type(2012, "presidential-general") == "presidential"
    assert norm_type(2014, "midterm-general") == "midterm"
    assert norm_type(2016, "General") == "presidential"  # year-driven
    assert norm_type(2018, "General") == "midterm"


def test_norm_type_excludes_special_recall_municipal():
    assert norm_type(2022, "Special") is None
    assert norm_type(2021, "Recall") is None
    assert norm_type(2019, "Municipal") is None


def test_norm_type_maps_statewide_primary_alias_to_midterm_primary():
    # county research JSONs use "statewide-primary" as a generic label; it
    # must normalize to "midterm-primary" regardless of year.
    assert norm_type(2018, "statewide-primary") == "midterm-primary"
    assert norm_type(2012, "statewide-primary") == "midterm-primary"


def test_norm_type_passes_through_explicit_primary_types():
    assert norm_type(2016, "presidential-primary") == "presidential-primary"
    assert norm_type(2022, "midterm-primary") == "midterm-primary"


def test_norm_type_generic_primary_string_derives_from_year():
    # a bare "primary" raw string (no presidential/midterm/statewide prefix)
    # falls back to the same year-driven rule as generals.
    assert norm_type(2012, "Primary") == "presidential-primary"
    assert norm_type(2014, "Primary") == "midterm-primary"


# ---- load_sf: SF primary points --------------------------------------------

def _fake_elections():
    def general(id_, year, night_pct, final, night_partial=None):
        e = {"id": id_, "kind": "General", "year": year, "nightPct": night_pct,
             "final": final}
        if night_partial is not None:
            e["nightPartial"] = night_partial
        return e

    def primary(id_, year, night_pct, final, night_partial=None):
        e = {"id": id_, "kind": "Primary", "year": year, "nightPct": night_pct,
             "final": final}
        if night_partial is not None:
            e["nightPartial"] = night_partial
        return e

    return [
        general("2012-11-06", 2012, 71.4, 200000, night_partial=False),
        primary("2012-06-05", 2012, 73.2, 145105, night_partial=True),
        primary("2014-06-03", 2014, 69.8, 129399, night_partial=False),
        primary("2016-06-07", 2016, 70.1, 264993),
        primary("2018-06-05", 2018, 60.8, 253583),
        primary("2022-06-07", 2022, 55.8, 229229),
        primary("2024-03-05", 2024, 44.9, 233465),
        # a non-statewide primary date that must NOT be emitted -- only the
        # six explicit statewide primary dates are in scope.
        primary("2022-02-15", 2022, 72.4, 50000),
        # the March 2020 primary must not sneak in either (not one of the six).
        primary("2020-03-03", 2020, 47.4, 305184),
    ]


def test_load_sf_emits_six_statewide_primary_points_with_normalized_types(tmp_path):
    fp = tmp_path / "elections.json"
    fp.write_text(json.dumps(_fake_elections()))
    sf = load_sf(fp)
    primaries = {p["year"]: p for p in sf["points"] if p["type"].endswith("-primary")}
    assert set(primaries) == {2012, 2014, 2016, 2018, 2022, 2024}
    assert primaries[2012]["type"] == "presidential-primary"
    assert primaries[2016]["type"] == "presidential-primary"
    assert primaries[2024]["type"] == "presidential-primary"
    assert primaries[2014]["type"] == "midterm-primary"
    assert primaries[2018]["type"] == "midterm-primary"
    assert primaries[2022]["type"] == "midterm-primary"
    assert primaries[2012]["pct"] == 73.2
    assert primaries[2024]["pct"] == 44.9


def test_load_sf_excludes_non_statewide_primary_dates(tmp_path):
    fp = tmp_path / "elections.json"
    fp.write_text(json.dumps(_fake_elections()))
    sf = load_sf(fp)
    covered_years = {p["year"] for p in sf["points"] if p["type"].endswith("-primary")}
    # 2022-02-15 (a non-statewide special/primary date) must not have produced
    # a second 2022 primary point beyond the legitimate 2022-06-07 one, and
    # 2020-03-03 (not one of the six) must not appear at all.
    assert len([p for p in sf["points"] if p["year"] == 2022 and p["type"] == "midterm-primary"]) == 1
    assert covered_years == {int(d[:4]) for d in SF_PRIMARY_DATES}


def test_load_sf_propagates_night_partial_honestly(tmp_path):
    fp = tmp_path / "elections.json"
    fp.write_text(json.dumps(_fake_elections()))
    sf = load_sf(fp)
    by_key = {(p["year"], p["type"]): p for p in sf["points"]}
    # 2012 primary is a newspaper-derived floor, flagged nightPartial=true
    # upstream in elections.json -- must be propagated, not silently dropped.
    assert by_key[(2012, "presidential-primary")].get("nightPartial") is True
    # 2014 primary's upstream nightPartial is explicitly false -- must not be
    # marked partial.
    assert by_key[(2014, "midterm-primary")].get("nightPartial") is not True
    # generals still carry the same semantics (mirrored, not special-cased).
    assert by_key[(2012, "presidential")].get("nightPartial") is not True


def test_load_sf_general_points_still_present_and_unaffected(tmp_path):
    fp = tmp_path / "elections.json"
    fp.write_text(json.dumps(_fake_elections()))
    sf = load_sf(fp)
    generals = [p for p in sf["points"] if p["type"] in ("presidential", "midterm")]
    assert len(generals) == 1
    assert generals[0]["year"] == 2012
    assert generals[0]["pct"] == 71.4


# ---- vca_year plumbing -----------------------------------------------------

def test_load_vca_years_maps_slug_to_year(tmp_path):
    census = tmp_path / "census.json"
    census.write_text(json.dumps([
        {"slug": "napa-ca", "vca_year": 2018},
        {"slug": "riverside-ca", "vca_year": 2022},
        {"slug": "mendocino-ca", "vca_year": None},  # never adopted
        {"vca_year": 2020},  # no slug -> ignored
    ]))
    m = load_vca_years(census)
    assert m["napa-ca"] == 2018
    assert m["riverside-ca"] == 2022
    assert m["mendocino-ca"] is None
    assert len(m) == 3  # the slug-less row is dropped


def test_load_vca_years_missing_census_returns_empty(tmp_path):
    assert load_vca_years(tmp_path / "does-not-exist.json") == {}


def test_load_sf_adoption_includes_vca_none(tmp_path):
    fp = tmp_path / "elections.json"
    fp.write_text(json.dumps(_fake_elections()))
    sf = load_sf(fp)
    # SF is the never-adopter control on every mechanism, VCA included.
    assert sf["adoption"]["vca"] is None
    assert set(sf["adoption"]) == {"epollbook", "asv", "vca"}
