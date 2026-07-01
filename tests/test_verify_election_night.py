"""Offline tests for the election-night-v4 verification helpers."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts/research"))

from en_common import find_number, norm_pct, strip_html, wayback_raw


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
