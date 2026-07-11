"""Merge the per-jurisdiction county-tech research records into the tidy
packages/data/county_tech.json consumed by the CountySpeed chart.

Long/tidy: one row per (jurisdiction, metric, year) and per (jurisdiction, tech).
Every source_url / evidence_url is preserved. Invalid records are skipped LOUDLY
(never silently dropped)."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
SRC = ROOT / "data" / "research" / "county-tech"
OUT = ROOT / "packages" / "data" / "county_tech.json"
sys.path.insert(0, str(ROOT / "scripts" / "research"))
from validate_county_tech import validate_record  # noqa: E402


def main():
    metrics, adoptions, skipped = [], [], []
    for f in sorted(SRC.glob("*.json")):
        if f.name in ("worklist.json", "ca_adoption_census.json"):
            # worklist and the CA-58 adoption census have their own formats,
            # not the per-jurisdiction tech-record schema
            continue
        r = json.loads(f.read_text())
        errs = validate_record(r)
        if errs:
            skipped.append((f.name, errs))
            continue
        j, st = r["jurisdiction"], r["state"]
        for t in r["tech"]:
            adoptions.append({
                "jurisdiction": j, "state": st, "tech": t["type"],
                "status": t["status"], "adopted_year": t.get("adopted_year"),
                "first_election": t.get("first_election"), "vendor": t.get("vendor"),
                "evidence_url": t["evidence_url"], "confidence": t["confidence"],
                "note": t.get("note", ""),
            })
        for m in r["metrics"]:
            metrics.append({
                "jurisdiction": j, "state": st, "metric": m["metric"], "year": m["year"],
                "value": m["value"], "denominator": m.get("denominator"),
                "source_url": m.get("source_url"), "confidence": m["confidence"],
                "note": m.get("note", ""),
            })
    metrics.sort(key=lambda x: (x["metric"], x["jurisdiction"], x["year"]))
    adoptions.sort(key=lambda x: (x["jurisdiction"], x["tech"]))
    OUT.write_text(json.dumps({"metrics": metrics, "adoptions": adoptions}, indent=1))
    print(f"{len(metrics)} metric rows, {len(adoptions)} adoption rows -> {OUT.name}")
    for name, errs in skipped:
        print(f"  SKIPPED (invalid) {name}: {errs}")


if __name__ == "__main__":
    main()
