#!/usr/bin/env python3
"""Bake packages/data/county_night.json — the cross-county ELECTION-NIGHT share
comparison (last election-night report ÷ certified final), with San Francisco
(no new counting tech) as the control.

Sources:
  - data/research/election-night/<slug>.json
    one file per CA county, each election row carrying the verified
    election_night_ballots / certified_final / election_night_pct + source +
    confidence (+ optional comparable/flag). See data/research/.../VERIFY.md.
  - packages/data/elections.json — SF's authoritative nightPct (DOE pipeline),
    used for the control row.

This is the data behind the "Did counting tech speed up election night?" chart.
Re-run after the election-night fan-out updates the per-county JSON.
"""
import json
import pathlib
import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
EN = ROOT / "data/research/election-night"
OUT = ROOT / "packages/data/county_night.json"
ELECTIONS = ROOT / "packages/data/elections.json"

# election-type normalisation -> "presidential" | "midterm" (Nov generals only)
PRES_YEARS = {2012, 2016, 2020, 2024}


def norm_type(year: int, raw: str) -> str | None:
    r = (raw or "").lower()
    if "primary" in r or "special" in r or "recall" in r or "municipal" in r:
        return None
    if "pres" in r or year in PRES_YEARS:
        return "presidential"
    return "midterm"


def is_control(adopt: dict, points: list[dict]) -> bool:
    """A jurisdiction is a no-new-tech control if none of its tracked tech
    (epollbook/asv) was adopted at or before the last election year this
    dataset observes for it. Data-driven: derived from the same `adoption`
    dict + per-election years the builder already reads, no hardcoded
    jurisdiction names. A county with NO points can't be evaluated this way
    and is conservatively not marked control."""
    if not points:
        return False
    adopt_years = [y for y in (adopt.get("epollbook"), adopt.get("asv")) if y]
    if not adopt_years:
        return True
    max_point_year = max(p["year"] for p in points)
    return min(adopt_years) > max_point_year


def load_counties() -> list[dict]:
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
            "control": is_control(adopt, points),
            # complete = every Nov-general row has a sourced election-night count
            "complete": bool(points) and all(p["ballots"] is not None for p in points),
            "adoption": {"epollbook": adopt.get("epollbook"), "asv": adopt.get("asv")},
            "points": points,
        })
    return out


def load_sf() -> dict:
    els = json.loads(ELECTIONS.read_text())
    pts = []
    for e in els:
        if e.get("kind") != "General":
            continue
        yr = e.get("year")
        if not (2012 <= yr <= 2024) or not e["id"].endswith(("11-06", "11-04", "11-08", "11-03", "11-05")):
            continue
        np = e.get("nightPct")
        fin = e.get("final")
        if np is None:
            continue
        pts.append({
            "year": yr,
            "type": "presidential" if yr in PRES_YEARS else "midterm",
            "pct": round(np, 2),
            "ballots": round(np / 100 * fin) if fin else None,
            "final": fin,
            "confidence": "primary",
            "comparable": True,
            "source_url": "https://github.com/Grow-SF/sf-election-historical-counts/blob/main/docs/sources.md",
        })
    return {
        "name": "San Francisco",
        "slug": "san-francisco-ca",
        "control": True,
        "complete": True,
        "adoption": {"epollbook": None, "asv": None},
        "points": sorted(pts, key=lambda p: p["year"]),
    }


def main() -> None:
    jurisdictions = [load_sf()] + load_counties()
    payload = {
        "metric": "election-night share = ballots in the last election-night report / certified-final ballots",
        "note": (
            "San Francisco is the no-new-tech control. 2020 (presidential) is a COVID "
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
    npts = sum(len(j["points"]) for j in jurisdictions)
    sourced = sum(1 for j in jurisdictions for p in j["points"] if p["pct"] is not None)
    print(f"wrote {OUT.relative_to(ROOT)}: {nj} jurisdictions, {npts} general-election rows, {sourced} with a night share")
    print(f"  (county source: {EN.relative_to(ROOT)})")


if __name__ == "__main__":
    main()
