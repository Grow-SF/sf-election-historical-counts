import shutil
from pathlib import Path

import pytest

FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture
def mini_pipeline(tmp_path):
    """A raw/ tree built from the source fixtures, plus matching data/ inputs."""
    data, raw = tmp_path / "data", tmp_path / "raw"
    data.mkdir()
    raw.mkdir()
    spec = [
        ("20241105", "20241108", "summary.xml", "era_c_modern.xml"),
        ("20241105", "20241105_1", "summary.xml", "era_c_night.xml"),
        ("20191105", "20191108", "summary.xml", "era_c_2019.xml"),
        ("20191105", "20191108", "20191108_psov.xml", "era_c_2019_psov_turnout.xml"),
        ("20161108", "20161110", "summary.txt", "era_b_general.txt"),
        ("20160607", "20160610", "summary.txt", "era_b_primary.txt"),
    ]
    for e, snap, fname, fixture in spec:
        dest = raw / e / snap / fname
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(FIXTURES / fixture, dest)
    (data / "elections.csv").write_text(
        "election_date,election_name,era\n"
        "2016-06-07,Presidential Primary Election,B\n"
        "2016-11-08,Consolidated General Election,B\n"
        "2019-11-05,Consolidated Municipal Election,C\n"
        "2024-11-05,Consolidated General Election,C\n")
    (data / "manifest.csv").write_text(
        "election,snapshot,filename,status,last_modified\n"
        "20241105,20241105_1,summary.xml,downloaded,2024-11-05T20:41:41\n"
        "20241105,20241108,summary.xml,downloaded,2024-11-08T15:45:18\n"
        "20191105,20191108,summary.xml,downloaded,2019-11-08T15:35:55\n"
        "20161108,20161110,summary.txt,downloaded,2016-11-10T16:01:57\n")
    # 20160607/20160610 has no manifest entry -> exercises folder-date fallback
    return data, raw
