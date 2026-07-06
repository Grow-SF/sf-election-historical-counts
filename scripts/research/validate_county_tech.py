"""Schema gate for one jurisdiction's counting-tech research record.

Usage: python3 scripts/research/validate_county_tech.py <record.json>
Prints "OK" and exits 0 if valid; prints errors and exits 1 otherwise.
"""
TECH_TYPES = {"epollbook", "asv", "sign-scan-go", "vote-center"}
METRICS = {"oneweek_pct", "electionnight_pct", "days_to_90", "days_to_cert"}
CONF = {"primary", "secondary", "estimated", "none"}


def validate_record(r: dict) -> list[str]:
    e = []
    for k in ("jurisdiction", "state", "tech", "metrics"):
        if k not in r:
            e.append(f"missing top-level key: {k}")
    for t in r.get("tech", []):
        if t.get("type") not in TECH_TYPES:
            e.append(f"tech.type invalid: {t.get('type')}")
        if t.get("status") not in {"adopted", "not-adopted", "unknown"}:
            e.append(f"tech.status invalid for {t.get('type')}")
        if not t.get("evidence_url"):
            e.append(f"tech {t.get('type')}: missing evidence_url")
        if t.get("confidence") not in CONF:
            e.append(f"tech {t.get('type')}: bad confidence")
        if t.get("status") == "adopted" and not t.get("adopted_year"):
            e.append(f"tech {t.get('type')}: adopted but no adopted_year")
    seen = set()
    for m in r.get("metrics", []):
        key = (m.get("metric"), m.get("year"))
        if key in seen:
            e.append(f"duplicate metric row: {key}")
        seen.add(key)
        if m.get("metric") not in METRICS:
            e.append(f"metric invalid: {m.get('metric')}")
        if m.get("confidence") not in CONF:
            e.append(f"metric {m.get('metric')}: bad confidence")
        has_value = m.get("value") is not None
        if has_value and not m.get("source_url"):
            e.append(f"metric {m.get('metric')} {m.get('year')}: value without source_url")
        if has_value and m.get("confidence") == "none":
            e.append(f"metric {m.get('metric')} {m.get('year')}: value with confidence 'none'")
    return e


if __name__ == "__main__":
    import json
    import sys
    errs = validate_record(json.load(open(sys.argv[1])))
    print("\n".join(errs) or "OK")
    sys.exit(1 if errs else 0)
