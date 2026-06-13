"""sfcount: SF vote-count timeline pipeline.

Subcommands: inventory | fetch | parse | validate | derive | all
"""
import argparse
from pathlib import Path

from sfcount.derive import stage_derive
from sfcount.fetch import stage_fetch
from sfcount.inventory import stage_inventory
from sfcount.timeline import stage_parse
from sfcount.validate import stage_validate

STAGES = ["inventory", "fetch", "parse", "validate", "derive"]


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="sfcount", description=__doc__)
    p.add_argument("--data-dir", type=Path, default=Path("data"))
    p.add_argument("--raw-dir", type=Path, default=Path("raw"))
    p.add_argument("--eras", default="B,C", help="comma-separated eras (default B,C)")
    sub = p.add_subparsers(dest="cmd", required=True)
    for name in STAGES + ["all"]:
        sub.add_parser(name)
    args = p.parse_args(argv)

    eras = tuple(args.eras.split(","))
    rc = 0
    if args.cmd in ("inventory", "all"):
        stage_inventory(args.data_dir)
    if args.cmd in ("fetch", "all"):
        stage_fetch(args.data_dir, args.raw_dir, eras)
    if args.cmd in ("parse", "all"):
        stage_parse(args.data_dir, args.raw_dir, eras)
    if args.cmd in ("validate", "all"):
        rc = stage_validate(args.data_dir) or rc
    if args.cmd in ("derive", "all"):
        stage_derive(args.data_dir)
    return rc
