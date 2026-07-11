#!/usr/bin/env python3
"""Offline consistency check of data/research/election-night/.

Row invariants, VERIFY.md table agreement, and SF-control agreement with
packages/data/elections.json. Exits 1 and prints one line per failure.
(county_night.json sync is checked separately via build + git diff -I.)
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import ROOT, EN, load_rows, norm_pct

FAIL = []


def fail(msg):
    FAIL.append(msg)


def check_rows(rows):
    for r in rows:
        key = f"{r['slug']} {r['date']}"
        b = r["election_night_ballots"]
        fin = r["certified_final"]
        p = r["election_night_pct"]
        if not isinstance(fin, int) or fin <= 0:
            fail(f"{key}: bad certified_final {fin!r}")
            continue
        if not (r.get("source_url_final") or "").startswith(
            "https://elections.cdn.sos.ca.gov/"
        ):
            fail(f"{key}: denominator source not CA SoS: {r.get('source_url_final')!r}")
        if b is None:
            if r["confidence"] != "none":
                fail(f"{key}: null numerator but confidence={r['confidence']!r}")
            if p is not None:
                fail(f"{key}: null numerator but pct={p!r}")
            if r.get("source_url_night"):
                fail(f"{key}: null numerator but has source_url_night")
        else:
            if r["confidence"] not in ("primary", "secondary"):
                fail(f"{key}: sourced but confidence={r['confidence']!r}")
            if not r.get("source_url_night"):
                fail(f"{key}: sourced but no source_url_night")
            if not 0 < b < fin:
                fail(f"{key}: ballots {b} not in (0, final {fin})")
            want = round(b / fin * 100, 2)
            got = norm_pct(p)
            if got is None or abs(got - want) > 0.05:
                fail(f"{key}: pct {got} != ballots/final {want}")


def type_bucket(t):
    """'primary' vs 'general', so a county's primary and general rows in the
    SAME calendar year (e.g. Riverside 2016-06 and 2016-11) get distinct
    keys instead of colliding on bare year -- both VERIFY.md's Type column
    and the JSON row's own "type" field are bucketed the same way."""
    return "primary" if "primary" in (t or "").lower() else "general"


def parse_verify_tables(md):
    """(slug, year, type_bucket) -> the VERIFY.md summary-table line, parsed."""
    out = {}
    slug = None
    for line in md.splitlines():
        m = re.match(r"^### (.+?) County", line)
        if m:
            slug = m.group(1).lower().replace(" ", "-") + "-ca"
        elif line.startswith("## San Francisco"):
            slug = "san-francisco-ca"
        if slug and re.match(r"^\| 20\d\d\D*\|", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]

            def num(s):
                s = s.lstrip("≈").replace(",", "").strip()
                return int(s) if s.isdigit() else None

            share = re.search(r"(\d+(?:\.\d+)?)%", cells[4])
            is_county = len(cells) > 6
            link = re.search(r"\((https?://[^)]+)\)", cells[6]) if is_county else None
            year = int(re.search(r"20\d\d", cells[0]).group())
            bucket = type_bucket(cells[1])
            out[(slug, year, bucket)] = {
                "night": num(cells[2]),
                "final": num(cells[3]),
                "share": float(share.group(1)) if share else None,
                "conf": cells[5] if is_county else None,
                "url": link.group(1) if link else None,
            }
    return out


def check_verify_md(rows, tables):
    for r in rows:
        year = int(r["date"][:4])
        bucket = type_bucket(r.get("type"))
        row = tables.get((r["slug"], year, bucket))
        key = f"{r['slug']} {year} ({bucket})"
        if row is None:
            fail(f"{key}: missing from VERIFY.md")
            continue
        if row["night"] != r["election_night_ballots"]:
            fail(f"{key}: VERIFY.md night {row['night']} != json {r['election_night_ballots']}")
        if row["final"] != r["certified_final"]:
            fail(f"{key}: VERIFY.md final {row['final']} != json {r['certified_final']}")
        got = norm_pct(r["election_night_pct"])
        if (row["share"] is None) != (got is None):
            fail(f"{key}: VERIFY.md share {row['share']} vs json {got}")
        elif got is not None and abs(row["share"] - got) > 0.055:
            fail(f"{key}: VERIFY.md share {row['share']} != json {got}")
        if row["conf"] is not None and r["confidence"] != row["conf"]:
            fail(f"{key}: VERIFY.md conf {row['conf']} != json {r['confidence']}")
        if row["url"] and r.get("source_url_night") and row["url"] != r["source_url_night"]:
            fail(f"{key}: VERIFY.md link != json source_url_night")


def check_sf(tables):
    els = json.loads((ROOT / "packages/data/elections.json").read_text())
    for e in els:
        row = tables.get(("san-francisco-ca", e.get("year"), "general"))
        if e.get("kind") != "General" or row is None or e.get("nightPct") is None:
            continue
        if row["final"] != e.get("final"):
            fail(f"SF {e['year']}: VERIFY.md final {row['final']} != elections.json {e.get('final')}")
        if row["share"] is not None and abs(row["share"] - round(e["nightPct"], 1)) > 0.055:
            fail(f"SF {e['year']}: VERIFY.md share {row['share']} != nightPct {e['nightPct']}")


def main():
    rows = load_rows()
    if len(rows) != 192:
        fail(f"expected 192 county rows, got {len(rows)}")
    tables = parse_verify_tables((EN / "VERIFY.md").read_text())
    check_rows(rows)
    check_verify_md(rows, tables)
    check_sf(tables)
    if FAIL:
        print(f"{len(FAIL)} problems:")
        for m in FAIL:
            print(" -", m)
        sys.exit(1)
    sourced = sum(1 for r in rows if r["election_night_ballots"] is not None)
    print(f"OK: {len(rows)} rows ({sourced} sourced), VERIFY.md and elections.json agree")


if __name__ == "__main__":
    main()
