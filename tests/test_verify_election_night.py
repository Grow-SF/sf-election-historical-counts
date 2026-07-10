"""Offline tests for the election-night verification helpers."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts/research"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))

from en_common import find_number, norm_pct, strip_html, wayback_raw
from verify_en_numerators import apply_render_override
from build_county_night import is_control


def test_norm_pct_fraction():
    assert norm_pct(0.5673) == 56.73


def test_norm_pct_percent_passthrough():
    assert norm_pct(60.7) == 60.7


def test_norm_pct_none():
    assert norm_pct(None) is None


def test_wayback_raw_inserts_id():
    url = "https://web.archive.org/web/20161112171743/http://x.gov/a.htm"
    assert wayback_raw(url) == (
        "https://web.archive.org/web/20161112171743id_/http://x.gov/a.htm"
    )


def test_wayback_raw_leaves_direct_urls_alone():
    assert wayback_raw("https://smcacre.gov/a.pdf") == "https://smcacre.gov/a.pdf"


def test_find_number_comma_formatted():
    assert find_number("Cards Cast 177,183 40.48%", 177183) is not None


def test_find_number_bare_json():
    assert find_number('"BC":28159,', 28159) is not None


def test_find_number_rejects_embedded_digits():
    assert find_number("run id 1177183x total", 177183) is None


def test_find_number_rejects_longer_comma_number():
    assert find_number("grand total 1,177,183 ballots", 177183) is None


def test_find_number_absent():
    assert find_number("nothing here", 12345) is None


def test_find_number_rejects_leading_group_of_longer_number():
    assert find_number("grand total 177,183,456 ballots", 177183) is None


def test_find_number_accepts_number_followed_by_punctuation_comma():
    assert find_number("Cards Cast 177,183, up from prior", 177183) is not None


def test_strip_html():
    assert strip_html("<td>177,183</td>").strip() == "177,183"


def _res(status="NOT_FOUND", claimed=111637, slug="san-mateo-ca", date="2018-11-06"):
    return {
        "slug": slug, "date": date, "kind": "numerator", "claimed": claimed,
        "url": "https://example.org/results", "artifact": "x.html",
        "status": status, "evidence": None,
    }


def test_apply_render_override_leaves_verified_result_untouched():
    res = _res(status="VERIFIED")
    manifest = {
        ("san-mateo-ca", "2018-11-06", "https://example.org/results"): {
            "evidence": "Total Ballots Cast 111,637",
        },
    }
    out = apply_render_override(res, manifest, "https://example.org/results")
    assert out is res


def test_apply_render_override_skips_on_url_mismatch():
    res = _res()
    manifest = {
        ("san-mateo-ca", "2018-11-06", "https://example.org/other-url"): {
            "evidence": "Total Ballots Cast 111,637",
        },
    }
    out = apply_render_override(res, manifest, "https://example.org/results")
    assert out == res
    assert out["status"] == "NOT_FOUND"


def test_apply_render_override_skips_when_evidence_lacks_claimed_number():
    res = _res(claimed=111637)
    manifest = {
        ("san-mateo-ca", "2018-11-06", "https://example.org/results"): {
            "evidence": "Total Ballots Cast 999,999",
        },
    }
    out = apply_render_override(res, manifest, "https://example.org/results")
    assert out == res
    assert out["status"] == "NOT_FOUND"


def test_is_control_true_when_both_adoption_years_absent():
    assert is_control({"epollbook": None, "asv": None}) is True


def test_is_control_false_when_epollbook_adopted():
    assert is_control({"epollbook": 2018, "asv": None}) is False


def test_is_control_false_when_only_asv_adopted():
    assert is_control({"epollbook": None, "asv": 2022}) is False


def test_is_control_false_when_both_adopted():
    assert is_control({"epollbook": 2020, "asv": 2020}) is False


def test_apply_render_override_applies_when_legitimate():
    res = _res(claimed=111637)
    manifest = {
        ("san-mateo-ca", "2018-11-06", "https://example.org/results"): {
            "evidence": "Total Ballots Cast 111,637",
        },
    }
    out = apply_render_override(res, manifest, "https://example.org/results")
    assert out["status"] == "VERIFIED"
    assert out["evidence"] == "render-verified: Total Ballots Cast 111,637"
