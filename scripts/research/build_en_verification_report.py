#!/usr/bin/env python3
"""Merge cache/*_results.json into two committed reports:

MACHINE_CHECK.md  - status of every machine check (156 rows: 78 denominator
                    + up to 78 numerator, 54 in practice)
HUMAN_VERIFY.md   - the hand-check packet covering EVERY sourced row: machine
                    failures, secondary rows, operator-flagged blocked sources,
                    then all machine-confirmed rows. The machine pass only
                    proves the claimed number appears at the cited URL; whether
                    that report is the election-night PLATEAU is the human's
                    judgment on every row (the original numbers came from
                    research agents, so presence alone is circular).
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
        "Division of labor. The machine pass verified two things only: every",
        "certified final matches the CA SoS Statement of Vote PDF, and every",
        "claimed night count appears at its cited URL (citations intact, nothing",
        "mistyped or fabricated). It CANNOT verify the metric itself: that the",
        "cited report is the LAST report posted on election night (the plateau),",
        "not an earlier tranche or a later canvass update. The claimed numbers",
        "were extracted by research agents, so re-finding them at the same",
        "citation is circular; the plateau judgment is yours on every sourced",
        "row below.",
        "",
        "Your reading wins: any discrepancy, even one ballot, gets corrected in",
        "the county JSON and VERIFY.md (then rerun scripts/build_county_night.py",
        "and scripts/research/build_en_verification_report.py). The full working",
        "note for any row is its detail bullet in VERIFY.md (same directory).",
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
        if b is not None:
            hv.append(
                "      your check: is this the LAST report posted on election"
                " night (the plateau)? full note: VERIFY.md detail bullet for"
                f" {r['slug']} {r['date']}"
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
    listed = {(x["slug"], x["date"]) for x in bad}
    listed |= {(r["slug"], r["date"]) for r in secondary}
    listed |= {(r["slug"], r["date"]) for r in flagged}
    remaining = [
        rows[(x["slug"], x["date"])]
        for x in ok_num
        if (x["slug"], x["date"]) not in listed
    ]
    hv.append(
        "## 4. Machine-confirmed rows (number is at the URL; plateau read still owed)"
    )
    hv.append("")
    for r in remaining:
        entry(r, "plateau check")
    (V4 / "HUMAN_VERIFY.md").write_text("\n".join(hv) + "\n")

    print(f"MACHINE_CHECK.md: {len(results)} checks, {len(bad)} not verified")
    print(
        f"HUMAN_VERIFY.md: {len(bad)} failures + {len(secondary)} secondary "
        f"+ {len(flagged)} flagged + {len(remaining)} awaiting the plateau read"
    )


if __name__ == "__main__":
    main()
