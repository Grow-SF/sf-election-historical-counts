#!/usr/bin/env python3
"""Bake packages/data/county_night.json — the cross-county ELECTION-NIGHT share
comparison (last election-night report ÷ certified final). San Francisco plus
six researched window-clean counties (San Luis Obispo, Lake, Del Norte,
Mendocino, Tehama, Colusa) serve as the no-new-counting-tech controls; see
is_control() below for exactly how a county earns that flag.

Sources:
  - data/research/election-night/<slug>.json
    one file per CA county, each election row carrying the verified
    election_night_ballots / certified_final / election_night_pct + source +
    confidence (+ optional comparable/flag). See data/research/.../VERIFY.md.
  - packages/data/elections.json — SF's authoritative nightPct (DOE pipeline),
    used for the control row.

This is the data behind the "Did counting tech speed up election night?" chart.
Re-run after the election-night fan-out updates the per-county JSON.

Type vocabulary (emitted in every jurisdiction's points[].type, and consumed
by scripts/research/estimate_tech_effect.py's (year, type) cell-matching):
  - "presidential" / "midterm" -- November generals (unchanged).
  - "presidential-primary" -- statewide primaries in a presidential year
    (2012-06-05, 2016-06-07, 2024-03-05).
  - "midterm-primary" -- statewide primaries in a midterm year
    (2014-06-03, 2018-06-05, 2022-06-07).
County research JSONs (data/research/election-night/<slug>.json) may carry
raw row types like "presidential-primary" or the generic "statewide-primary";
norm_type() maps "statewide-primary" -> "midterm-primary" and passes the two
explicit primary types through unchanged. Charts currently render generals
only (see packages/charts/src/components/CountyNight*.tsx); primary points
flow into county_night.json but are filtered out at the chart's data-
selection boundary pending an editorial decision on how to display them.
"""
import json
import pathlib
import sys
import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "data/research/election-night"
COUNTY_TECH = ROOT / "data/research/county-tech"
CENSUS = COUNTY_TECH / "ca_adoption_census.json"
OUT = ROOT / "packages/data/county_night.json"
ELECTIONS = ROOT / "packages/data/elections.json"

# election-type normalisation -> "presidential" | "midterm" |
# "presidential-primary" | "midterm-primary". See the module docstring for
# the full vocabulary.
PRES_YEARS = {2012, 2016, 2020, 2024}

# SF statewide primary election dates in scope (see load_sf()): the six
# 2012-2024 statewide primaries whose election-night shares are already
# hand-verified and baked into packages/data/elections.json. An explicit
# date list is self-documenting and keeps this from silently picking up a
# future non-statewide primary (special election, municipal RCV primary,
# etc.) that happens to carry kind "Primary".
SF_PRIMARY_DATES = {
    "2012-06-05", "2014-06-03", "2016-06-07",
    "2018-06-05", "2022-06-07", "2024-03-05",
}


def norm_type(year: int, raw: str) -> str | None:
    r = (raw or "").lower()
    if "special" in r or "recall" in r or "municipal" in r:
        return None
    if r == "statewide-primary":
        return "midterm-primary"
    if r == "presidential-primary":
        return "presidential-primary"
    if r == "midterm-primary":
        return "midterm-primary"
    if "primary" in r:
        # generic/unlabeled primary raw string: derive presidential vs
        # midterm from the year, same rule as generals below.
        return "presidential-primary" if year in PRES_YEARS else "midterm-primary"
    if "pres" in r or year in PRES_YEARS:
        return "presidential"
    return "midterm"


def is_control(slug: str, adoption: dict, points: list[dict],
               tech_dir: pathlib.Path = COUNTY_TECH) -> bool:
    """A county is a second CONTROL (alongside SF) only when BOTH conditions
    hold, for both tracked technologies (epollbook, asv):

    1. WINDOW-CLEAN: it had not adopted the tech at or before the last
       election year this dataset observes for it. Never-adoption qualifies,
       and so does an adoption dated strictly AFTER the county's observed
       window (e.g. San Luis Obispo's 2026 e-pollbook debut, outside the
       2012-2024 panel): the panel years are untreated either way.
    2. RESEARCHED: its data/research/county-tech/<slug>.json record exists
       and independently supports that conclusion (status "not-adopted" --
       or, as a schema fallback, no recorded adoption event -- or an
       adopted_year after the observed window). Null adoption years alone
       are NOT enough: a future county whose years are null merely because
       it is UNRESEARCHED must not silently become a control.

    See docs/research/RUNBOOK.md section 4 (the control-flag rule paragraph;
    window-aware refinement recorded 2026-07-10). A county with NO points
    can't be evaluated and is conservatively not marked control."""
    if not points:
        return False
    max_point_year = max(p["year"] for p in points)
    if any(y is not None and y <= max_point_year
           for y in (adoption.get("epollbook"), adoption.get("asv"))):
        return False
    tech_fp = tech_dir / f"{slug}.json"
    if not tech_fp.exists():
        print(
            f"WARNING: {slug} has window-clean epollbook/asv adoption years "
            f"but no county-tech record at {tech_fp}; treating as NOT a "
            f"control (unresearched, not a confirmed never-adopter)",
            file=sys.stderr,
        )
        return False
    tech = json.loads(tech_fp.read_text())
    entries = {t.get("type"): t for t in tech.get("tech", [])}
    for kind in ("epollbook", "asv"):
        entry = entries.get(kind)
        if entry is None:
            continue  # schema fallback: no adoption event recorded for this type
        ay = entry.get("adopted_year")
        if entry.get("status") == "adopted" or ay is not None:
            if ay is None or ay <= max_point_year:
                return False
    return True


def load_vca_years(census_path: pathlib.Path = CENSUS) -> dict:
    """slug -> Voter's Choice Act (all-mail / vote-center) adoption year, read
    from the CA adoption census (ca_adoption_census.json's vca_year field).
    The census's vca_year agrees with each county-tech record's vote-center
    entry adopted_year for every panel county (checked 2026-07-10); the census
    is used as the single keyed source. Absent/None where the county never
    adopted VCA."""
    if not census_path.exists():
        return {}
    rows = json.loads(census_path.read_text())
    return {r["slug"]: r.get("vca_year") for r in rows if r.get("slug")}


def load_counties() -> list[dict]:
    vca = load_vca_years()
    out = []
    for fp in sorted(EN.glob("*.json")):
        d = json.loads(fp.read_text())
        if not isinstance(d, dict):
            continue  # skip non-county manifests, e.g. render_verified.json
        adopt = d.get("adoption", {}) or {}
        points = []
        for e in d.get("elections", []):
            yr = int(e["date"][:4])
            t = norm_type(yr, e.get("type", ""))
            if t is None:
                continue
            pct = e.get("election_night_pct")
            if pct is not None and pct <= 1.5:  # a few rows stored as fractions
                pct = round(pct * 100, 2)
            points.append({
                "year": yr,
                "type": t,
                "pct": pct,
                "ballots": e.get("election_night_ballots"),
                "final": e.get("certified_final"),
                "confidence": e.get("confidence"),
                "comparable": e.get("comparable", True) is not False,
                "source_url": e.get("source_url_night"),
            })
        out.append({
            "name": d.get("jurisdiction", fp.stem).replace(" County", ""),
            "slug": fp.stem,
            "control": is_control(fp.stem, adopt, points),
            # complete = every Nov-general row has a sourced election-night
            # count. Primaries are the charts' secondary (dimmed, dashed)
            # series and deliberately do NOT gate completeness: a county with
            # a fully sourced general trajectory keeps its timeline panel
            # even while primary cells are still being researched.
            "complete": bool(gen_points := [p for p in points
                                            if p["type"] in ("presidential", "midterm")])
                        and all(p["ballots"] is not None for p in gen_points),
            "adoption": {"epollbook": adopt.get("epollbook"), "asv": adopt.get("asv"),
                         "vca": vca.get(fp.stem)},
            "points": points,
        })
    return out


def load_sf(elections_path: pathlib.Path = ELECTIONS) -> dict:
    els = json.loads(elections_path.read_text())
    pts = []
    for e in els:
        kind = e.get("kind")
        yr = e.get("year")
        if kind == "General":
            if not (2012 <= yr <= 2024) or not e["id"].endswith(("11-06", "11-04", "11-08", "11-03", "11-05")):
                continue
            etype = "presidential" if yr in PRES_YEARS else "midterm"
        elif kind == "Primary":
            if e["id"] not in SF_PRIMARY_DATES:
                continue
            etype = "presidential-primary" if yr in PRES_YEARS else "midterm-primary"
        else:
            continue
        np = e.get("nightPct")
        fin = e.get("final")
        if np is None:
            continue
        pt = {
            "year": yr,
            "type": etype,
            "pct": round(np, 2),
            "ballots": round(np / 100 * fin) if fin else None,
            "final": fin,
            "confidence": "primary",
            "comparable": True,
            "source_url": "https://github.com/Grow-SF/sf-election-historical-counts/blob/main/docs/sources.md",
        }
        # Mirror elections.json's own nightPartial semantics (an optional
        # flag, present/true only when the night figure is a press-deadline
        # partial rather than a full report -- e.g. 2012's primary, a
        # newspaper-scan floor at 49% precincts reporting statewide).
        if e.get("nightPartial"):
            pt["nightPartial"] = True
        pts.append(pt)
    return {
        "name": "San Francisco",
        "slug": "san-francisco-ca",
        "control": True,
        "complete": True,
        # SF is the never-adopter control on every mechanism, including VCA
        # (San Francisco is not a Voter's Choice Act county); vca is None by
        # construction, consistent with its census row (san-francisco-ca
        # vca_year null).
        "adoption": {"epollbook": None, "asv": None, "vca": None},
        "points": sorted(pts, key=lambda p: p["year"]),
    }


def main() -> None:
    jurisdictions = [load_sf()] + load_counties()
    payload = {
        "metric": "election-night share = ballots in the last election-night report / certified-final ballots",
        "note": (
            "San Francisco plus six researched window-clean counties (San Luis "
            "Obispo, Lake, Del Norte, Mendocino, Tehama, Colusa) are the "
            "no-new-tech controls; San Luis Obispo's first e-pollbook election "
            "(June 2026) postdates the panel window, and Colusa "
            "carries documented nulls (no surviving election-night report for any "
            "year) rather than sourced points. 2020 (presidential) is a COVID "
            "all-mail outlier; rows flagged comparable=false (e.g. Nevada 2024, a "
            "ballot-printer-defect outlier) are excluded from pre/post comparisons. "
            "The 2018-2020 statewide Voter's Choice Act all-mail shift is a confound "
            "independent of e-pollbooks/ASV."
        ),
        "source": "data/research/election-night/ (per-county, verified) + SF DOE pipeline (packages/data/elections.json)",
        "generated": datetime.date.today().isoformat(),
        "jurisdictions": jurisdictions,
    }
    OUT.write_text(json.dumps(payload, indent=2) + "\n")
    nj = len(jurisdictions)
    pts = [p for j in jurisdictions for p in j["points"]]
    ngen = sum(1 for p in pts if p["type"] in ("presidential", "midterm"))
    nprim = sum(1 for p in pts if p["type"].endswith("-primary"))
    sourced = sum(1 for p in pts if p["pct"] is not None)
    print(f"wrote {OUT.relative_to(ROOT)}: {nj} jurisdictions, {ngen} general rows, "
          f"{nprim} primary rows, {sourced} with a night share")
    print(f"  (county source: {EN.relative_to(ROOT)})")


if __name__ == "__main__":
    main()
