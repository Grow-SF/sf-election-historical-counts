"""Stage 0: the canonical election list, scraped from sf.gov/results."""
import csv
import datetime as dt
import re
from pathlib import Path

ERA_C_START = dt.date(2019, 1, 1)  # Dominion era
ERA_B_START = dt.date(2008, 1, 1)
EARLIEST = dt.date(2000, 11, 1)

MONTHS = {m: i + 1 for i, m in enumerate(
    "January February March April May June July August September October November December".split())}

# The page embeds election names in JSON ("<" escapes) as well as HTML.
ELECTION_RE = re.compile(
    r"(January|February|March|April|May|June|July|August|September|October|November|December)"
    r"\s+(\d{1,2}),\s+(\d{4})[, ]*([^\\<]{0,70}?Election[^\\<]{0,30}?)(?:\\u003c|<)")

# Elections already underway on sfelections.org but not yet listed on the
# sf.gov past-results page (it adds elections only after certification).
# Page listings override these once they appear.
SUPPLEMENTAL_ELECTIONS = {
    dt.date(2026, 6, 2): "Consolidated Statewide Direct Primary Election",
}


def era_for(date: dt.date) -> str:
    if date >= ERA_C_START:
        return "C"
    if date >= ERA_B_START:
        return "B"
    return "A"


def extract_elections(html: str) -> dict[dt.date, str]:
    seen: dict[dt.date, str] = dict(SUPPLEMENTAL_ELECTIONS)
    for month, day, year, name in ELECTION_RE.findall(html):
        date = dt.date(int(year), MONTHS[month], int(day))
        name = re.sub(r"\s+", " ", name).strip(" ,").removesuffix(" Results")
        if date >= EARLIEST:
            seen[date] = name
    return seen


def write_inventory(seen: dict[dt.date, str], data_dir: Path) -> None:
    data_dir.mkdir(parents=True, exist_ok=True)
    with open(data_dir / "elections.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["election_date", "election_name", "era"])
        for date in sorted(seen):
            w.writerow([date.isoformat(), seen[date], era_for(date)])


def load_elections(data_dir: Path, eras: tuple[str, ...]) -> list[dict]:
    with open(data_dir / "elections.csv") as f:
        return [row for row in csv.DictReader(f) if row["era"] in eras]


def stage_inventory(data_dir: Path) -> None:
    import requests

    r = requests.get(
        "https://www.sf.gov/results", timeout=30,
        headers={"User-Agent": "Mozilla/5.0 (research; SF vote-count timeline)"})
    r.raise_for_status()
    seen = extract_elections(r.text)
    write_inventory(seen, data_dir)
    print(f"inventory: {len(seen)} elections -> {data_dir / 'elections.csv'}", flush=True)
