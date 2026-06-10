"""Stage 3: walk raw/, dispatch era parsers, assemble sf_count_timeline.csv."""
import csv
import datetime as dt
from dataclasses import replace
from pathlib import Path

from sfcount.archival import ARCHIVAL_ROWS
from sfcount.fetch import BASE, load_manifest
from sfcount.inventory import load_elections
from sfcount.parsers import (
    ParseError, parse_era_b_tsv, parse_era_c_psov, parse_era_c_xml,
)

PARSERS = {"C": ("era_c_xml", parse_era_c_xml), "B": ("era_b_tsv", parse_era_b_tsv)}
TIMELINE_COLS = [
    "election_date", "election_name", "report_seq", "snapshot",
    "report_datetime", "ballots_counted_total", "ballots_vbm",
    "ballots_election_day", "registered_voters", "parser",
    "datetime_source", "source_url",
]


def stage_parse(data_dir: Path, raw_dir: Path, eras: tuple[str, ...]) -> None:
    elections = {
        el["election_date"].replace("-", ""): el
        for el in load_elections(data_dir, eras)
    }
    manifest = load_manifest(data_dir / "manifest.csv")
    rows, failures = [], []

    for path in sorted(raw_dir.glob("*/*/summary.*")):
        e, snap = path.parts[-3], path.parts[-2]
        el = elections.get(e)
        if el is None:
            continue
        parser_name, parse = PARSERS[el["era"]]
        try:
            rec = parse(path.read_text(encoding="utf-8-sig", errors="replace"))
        except ParseError as ex:
            failures.append({"file": str(path), "error": str(ex)})
            continue
        # The Nov 2019 summary publishes no ED/VBM split; recover it from the
        # per-precinct statement of the vote, but only when the precinct sums
        # reconcile exactly with the summary's total.
        psov_path = path.parent / f"{snap}_psov.xml"
        if rec.ballots_vbm is None and el["era"] == "C" and psov_path.exists():
            try:
                ed, vbm = parse_era_c_psov(
                    psov_path.read_text(encoding="utf-8-sig", errors="replace"))
            except ParseError as ex:
                failures.append({"file": str(psov_path), "error": str(ex)})
            else:
                if ed + vbm == rec.ballots_counted_total:
                    rec = replace(rec, ballots_election_day=ed, ballots_vbm=vbm)
                    parser_name = "era_c_xml+psov"
                else:
                    failures.append({
                        "file": str(psov_path),
                        "error": f"psov sum {ed + vbm} != summary total "
                                 f"{rec.ballots_counted_total}; split left blank"})
        mrow = manifest.get((e, snap), {})
        if mrow.get("last_modified"):
            rdt, dt_src = mrow["last_modified"], "header"
        else:
            rdt = dt.datetime.strptime(snap.split("_")[0], "%Y%m%d").isoformat()
            dt_src = "folder"
        rows.append({
            "election_date": el["election_date"],
            "election_name": el["election_name"],
            "snapshot": snap,
            "report_datetime": rdt,
            "ballots_counted_total": rec.ballots_counted_total,
            "ballots_vbm": rec.ballots_vbm,
            "ballots_election_day": rec.ballots_election_day,
            "registered_voters": rec.registered_voters,
            "parser": parser_name,
            "datetime_source": dt_src,
            "source_url": f"{BASE}/{e}/data/{snap}/{path.name}",
        })

    rows.extend(dict(r) for r in ARCHIVAL_ROWS)
    rows.sort(key=lambda r: (r["election_date"], r["report_datetime"], r["snapshot"]))
    seq, last_e = 0, None
    for r in rows:
        seq = seq + 1 if r["election_date"] == last_e else 1
        r["report_seq"], last_e = seq, r["election_date"]

    data_dir.mkdir(parents=True, exist_ok=True)
    with open(data_dir / "sf_count_timeline.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=TIMELINE_COLS)
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if v is None else v) for k, v in r.items()})
    with open(data_dir / "parse_failures.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "error"])
        w.writeheader()
        w.writerows(failures)
    print(f"parse: {len(rows)} rows, {len(failures)} failures", flush=True)
