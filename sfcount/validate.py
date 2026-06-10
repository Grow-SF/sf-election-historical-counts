"""Stage 4: dataset invariants. Nonzero exit on violation so it can gate CI."""
import csv
from pathlib import Path

# Certified turnout from the Department of Elections' final official summaries.
CERTIFIED_FINALS = {
    "2024-11-05": 412231,
    "2016-11-08": 414528,
    "2012-11-06": 364875,
}


def _int(value):
    return int(value) if value not in ("", None) else None


def _sorted(rows):
    return sorted(rows, key=lambda r: (r["election_date"], r["report_datetime"], r["snapshot"]))


def check_monotonic(rows) -> list[str]:
    errs, prev = [], {}
    for r in _sorted(rows):
        k, total = r["election_date"], _int(r["ballots_counted_total"])
        if total is None:
            continue
        if k in prev and total < prev[k]:
            errs.append(f"non-monotonic {k} {r['snapshot']}: {total} < {prev[k]}")
        prev[k] = total
    return errs


def check_split_sum(rows) -> list[str]:
    errs = []
    for r in rows:
        vbm, ed = _int(r["ballots_vbm"]), _int(r["ballots_election_day"])
        if vbm is None or ed is None:
            continue
        total = _int(r["ballots_counted_total"])
        if vbm + ed != total:
            errs.append(f"split mismatch {r['election_date']} {r['snapshot']}: "
                        f"{vbm} + {ed} != {total}")
    return errs


def check_certified(rows) -> list[str]:
    errs, finals = [], {}
    for r in rows:
        total = _int(r["ballots_counted_total"])
        if total is None:
            continue
        k = r["election_date"]
        finals[k] = max(finals.get(k, 0), total)
    for k, certified in CERTIFIED_FINALS.items():
        if k in finals and finals[k] != certified:
            errs.append(f"certified mismatch {k}: max {finals[k]} != certified {certified}")
    return errs


def validate_rows(rows) -> list[str]:
    return check_monotonic(rows) + check_split_sum(rows) + check_certified(rows)


def stage_validate(data_dir: Path) -> int:
    with open(data_dir / "sf_count_timeline.csv", newline="") as f:
        rows = list(csv.DictReader(f))
    errs = validate_rows(rows)
    for e in errs:
        print(f"VALIDATE FAIL: {e}", flush=True)
    print(f"validate: {len(rows)} rows, {len(errs)} errors", flush=True)
    return 1 if errs else 0
