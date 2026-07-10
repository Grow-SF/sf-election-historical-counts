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
