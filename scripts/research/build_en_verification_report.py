#!/usr/bin/env python3
"""Merge cache/*_results.json into two committed reports:

MACHINE_CHECK.md  - status of every machine check (156 rows: 78 denominator
                    + up to 78 numerator, 54 in practice)
HUMAN_VERIFY.md   - the hand-check packet: machine failures, secondary rows,
                    operator-flagged blocked sources, and a spot-check sample.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import CACHE, V4, load_rows, norm_pct


def load_results():
    res = []
    for name in ("denominator_results.json", "numerator_results.json"):
        p = CACHE / name
        if not p.exists():
            sys.exit(f"missing {p}; run the verify_en_* scripts first")
        res.extend(json.loads(p.read_text()))
    return res


def main():
    results = load_results()
    rows = {(r["slug"], r["date"]): r for r in load_rows()}
    bad = [x for x in results if x["status"] != "VERIFIED"]
    ok_num = sorted(
        (x for x in results if x["status"] == "VERIFIED" and x["kind"] == "numerator"),
        key=lambda x: (x["slug"], x["date"]),
    )
    sample = ok_num[::10]
    secondary = [r for r in rows.values() if r["confidence"] == "secondary"]
    flagged = [
        r for r in rows.values() if "FLAG for manual operator" in (r.get("note") or "")
    ]

    mc = [
        "# Machine check of election-night-v4 sources",
        "",
        "Presence checks of each claimed number against its cited URL.",
        "Denominators are checked against the canonical per-year SoS",
        "'Voter Participation Statistics by County' PDF even where a row cites",
        "the complete-SOV PDF (same statistic). Fetched artifacts live in",
        "`data/research/election-night-v4/cache/` (gitignored; rerun the",
        "verify_en_* scripts to regenerate).",
        "",
        "| County | Date | Check | Claimed | Status | Evidence (context around match) |",
        "|---|---|---|---:|---|---|",
    ]
    for x in sorted(results, key=lambda x: (x["slug"], x["date"], x["kind"])):
        ev = (x["evidence"] or "")[:120].replace("|", "\\|")
        mc.append(
            f"| {x['slug']} | {x['date']} | {x['kind']} | {x['claimed']:,} "
            f"| {x['status']} | {ev} |"
        )
    (V4 / "MACHINE_CHECK.md").write_text("\n".join(mc) + "\n")

    hv = [
        "# Hand-verification packet (election-night-v4)",
        "",
        "Open each URL and compare against the claimed value. Your reading wins:",
        "any discrepancy, even one ballot, gets corrected in the county JSON and",
        "VERIFY.md (then rerun scripts/build_county_night.py).",
        "",
    ]

    def entry(r, reason, extra=None):
        b = r["election_night_ballots"]
        claimed = f"night ballots **{b:,}**" if b is not None else "night ballots **null (recover if possible)**"
        share = norm_pct(r["election_night_pct"])
        hv.extend(
            [
                f"- [ ] **{r['slug']} {r['date']}** ({reason})",
                f"      claimed: {claimed}, certified final **{r['certified_final']:,}**"
                + (f", share **{share}%**" if share is not None else ""),
                f"      numerator URL: {r.get('source_url_night') or '(none)'}",
                f"      denominator URL: {r.get('source_url_final')}",
                f"      look for: {(r.get('note') or '')[:300]}",
            ]
        )
        if extra:
            hv.append(f"      {extra}")
        hv.append("")

    hv.append("## 1. Machine check could not verify these (open and eyeball)")
    hv.append("")
    for x in bad:
        entry(rows[(x["slug"], x["date"])], f"{x['kind']} {x['status']}")
    hv.append("## 2. Secondary-confidence rows (weakest sourcing, read closely)")
    hv.append("")
    for r in secondary:
        entry(r, "secondary confidence")
    hv.append("## 3. Blocked-source recoveries (need a real browser)")
    hv.append("")
    for r in flagged:
        entry(r, "operator-flagged", f"full flag: {r['note']}")
    hv.append("## 4. Spot-check sample of machine-verified rows (trust but verify)")
    hv.append("")
    for x in sample:
        entry(rows[(x["slug"], x["date"])], "spot-check")
    (V4 / "HUMAN_VERIFY.md").write_text("\n".join(hv) + "\n")

    print(f"MACHINE_CHECK.md: {len(results)} checks, {len(bad)} not verified")
    print(
        f"HUMAN_VERIFY.md: {len(bad)} failures + {len(secondary)} secondary "
        f"+ {len(flagged)} flagged + {len(sample)} spot-checks"
    )


if __name__ == "__main__":
    main()
