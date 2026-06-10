"""Live smoke tests. Run explicitly: uv run pytest -m network"""
import pytest
import requests

from sfcount.parsers import parse_era_b_tsv, parse_era_c_xml

UA = {"User-Agent": "Mozilla/5.0 (research; SF vote-count timeline)"}


@pytest.mark.network
def test_live_era_c_snapshot_parses():
    r = requests.get(
        "https://www.sfelections.org/results/20241105/data/20241108/summary.xml",
        headers=UA, timeout=30)
    assert r.status_code == 200
    rec = parse_era_c_xml(r.content.decode("utf-8-sig"))
    assert rec.ballots_counted_total == 289135
    assert "Last-Modified" in r.headers


@pytest.mark.network
def test_live_era_b_snapshot_parses():
    # The 20161110 summary.txt is windows-1250/latin-1 encoded: byte 0xd1 appears
    # in candidate name "ESPA\xd1A" (ESPAÑA) at position 7965. The Registration &
    # Turnout rows are pure ASCII, so errors="replace" leaves the counts intact.
    r = requests.get(
        "https://www.sfelections.org/results/20161108/data/20161110/summary.txt",
        headers=UA, timeout=30)
    assert r.status_code == 200
    rec = parse_era_b_tsv(r.content.decode("utf-8-sig", errors="replace"))
    assert rec.ballots_counted_total == 283049


@pytest.mark.network
def test_live_2019_psov_reconciles_with_summary():
    from sfcount.parsers import parse_era_c_psov

    r = requests.get(
        "https://www.sfelections.org/results/20191105/data/20191108/20191108_psov.xml",
        headers=UA, timeout=120)  # ~27 MB
    assert r.status_code == 200
    ed, vbm = parse_era_c_psov(r.content.decode("utf-8-sig"))
    assert (ed, vbm) == (45594, 144910)  # sums exactly to the summary total 190504
