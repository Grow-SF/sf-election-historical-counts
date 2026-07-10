"""Validate ca_adoption_census.json: 58 CA counties, schema, and agreement
with the researched county-tech records. Exit 1 with one line per failure.

Usage: python3 scripts/research/validate_adoption_census.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CENSUS = ROOT / "data" / "research" / "county-tech" / "ca_adoption_census.json"
STATUSES = {"adopter", "never", "unknown"}
CONFS = {"high", "medium", "low"}


def validate(rows: list[dict], tech_dir: Path) -> list[str]:
    fails = []
    if len(rows) != 58:
        fails.append(f"expected 58 counties, got {len(rows)}")
    slugs = [r.get("slug") for r in rows]
    if len(set(slugs)) != len(slugs):
        dupes = {s for s in slugs if slugs.count(s) > 1}
        fails.append(f"duplicate slugs: {sorted(dupes)}")

    for r in rows:
        ctx = r.get("slug") or r.get("county") or "?"
        for field in ("county", "slug", "status", "confidence", "sources", "note"):
            if not r.get(field):
                fails.append(f"{ctx}: missing {field}")
        if r.get("status") not in STATUSES:
            fails.append(f"{ctx}: bad status {r.get('status')!r}")
        if r.get("confidence") not in CONFS:
            fails.append(f"{ctx}: bad confidence {r.get('confidence')!r}")
        if not isinstance(r.get("sources"), list) or not all(
            isinstance(s, str) and s for s in r.get("sources", [])
        ):
            fails.append(f"{ctx}: sources must be a non-empty list of URL strings")

        has_year = bool(r.get("epollbook_year") or r.get("asv_year"))
        if r.get("status") == "adopter" and not has_year:
            fails.append(f"{ctx}: adopter without an adoption year")
        if r.get("status") == "never" and has_year:
            fails.append(f"{ctx}: never-adopter with an adoption year")

        for field in ("epollbook_year", "asv_year", "vca_year"):
            val = r.get(field)
            if val is not None and not isinstance(val, int):
                fails.append(f"{ctx}: {field} must be an int or null, got {val!r}")

    # cross-check against researched per-county tech records (data/research/county-tech/*-ca.json).
    # Those records use a different schema: a `tech` array of
    # {"type": "epollbook"|"asv"|..., "status": "adopted"|"not-adopted"|"unknown",
    #  "adopted_year": int|None}. The census's epollbook_year/asv_year for a
    # county with a researched record must match that record's adopted_year
    # for the corresponding tech type; mismatches are failures.
    by_slug = {r.get("slug"): r for r in rows}
    for f in sorted(tech_dir.glob("*-ca.json")):
        try:
            rec = json.loads(f.read_text())
        except json.JSONDecodeError as exc:
            fails.append(f"{f.name}: unparseable researched record ({exc})")
            continue
        slug = f.stem
        if slug not in by_slug:
            fails.append(f"{slug}: researched record exists but missing from census")
            continue
        census_row = by_slug[slug]

        tech_by_type = {t.get("type"): t for t in rec.get("tech", [])}
        for tech_type, census_field in (("epollbook", "epollbook_year"), ("asv", "asv_year")):
            t = tech_by_type.get(tech_type)
            if t is None:
                continue
            rec_year = t.get("adopted_year") if t.get("status") == "adopted" else None
            census_year = census_row.get(census_field)
            if rec_year != census_year:
                fails.append(
                    f"{slug}: {census_field}={census_year!r} disagrees with "
                    f"researched record's {tech_type} adopted_year={rec_year!r}"
                )

        # a county with a full researched record has real evidence; the
        # census should not punt to "unknown" for it.
        if census_row.get("status") == "unknown":
            fails.append(f"{slug}: researched record exists but census says unknown")

    return fails


if __name__ == "__main__":
    if not CENSUS.exists():
        print(f"census file missing: {CENSUS}")
        sys.exit(1)
    rows = json.loads(CENSUS.read_text())
    tech_dir = ROOT / "data" / "research" / "county-tech"
    fails = validate(rows, tech_dir)
    for line in fails:
        print(line)
    sys.exit(1 if fails else 0)
