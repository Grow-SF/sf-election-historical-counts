"""Pure parsers for SF Elections per-release summary files.

Era C (2019-present): Dominion ElectionSummaryReportRPT XML.
Era B (2008-2018):    "summary.txt" TSV, one row per contest/candidate.
"""
import csv
import io
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass


class ParseError(ValueError):
    """The file is not a recognizable summary report."""


def _int_attr(element, name: str) -> int:
    value = element.get(name)
    if value is None:
        raise ParseError(f"turnout block missing attribute {name!r}")
    return int(value)


def _int_field(row: dict, key: str) -> int:
    value = row[key]
    if value is None:
        raise ParseError(f"Era B row missing field {key!r}")
    try:
        return int(value)
    except ValueError as ex:
        raise ParseError(f"Era B field {key!r} is not an integer: {value!r}") from ex


@dataclass(frozen=True)
class TurnoutRecord:
    ballots_counted_total: int
    registered_voters: int
    ballots_vbm: int | None
    ballots_election_day: int | None


def parse_era_c_xml(text: str) -> TurnoutRecord:
    try:
        root = ET.fromstring(text.lstrip("\ufeff"))
    except ET.ParseError as ex:
        raise ParseError(f"not XML: {ex}") from ex

    # Modern variant: RegistrationAndTurnout block. ballots3/Textbox171 count
    # voters; ballots1/ballots2 count CARDS - never use those.
    for eg in root.findall(".//{*}electorGroupId2"):
        if eg.get("electorGroupId2") != "Total":
            continue
        groups = {
            d.get("countingGroup1"): _int_attr(d, "Textbox171")
            for d in eg.findall(".//{*}Details1")
        }
        return TurnoutRecord(
            ballots_counted_total=_int_attr(eg, "ballots3"),
            registered_voters=_int_attr(eg, "Textbox32"),
            ballots_vbm=groups.get("Vote by Mail"),
            ballots_election_day=groups.get("Election Day"),
        )

    # 2019 variant: only a "Registered Voters: N of M" headline. Its
    # cgId2/ballotsTextBox ED-VBM figures are per-contest (they don't sum to
    # the report total), so the split stays None.
    for det in root.findall(".//{*}Details2"):
        m = re.match(r"Registered Voters:\s*(\d+)\s+of\s+(\d+)", det.get("reported3", ""))
        if m:
            return TurnoutRecord(
                ballots_counted_total=int(m[1]),
                registered_voters=int(m[2]),
                ballots_vbm=None,
                ballots_election_day=None,
            )

    raise ParseError("no turnout block found in Era C XML")


def parse_era_b_tsv(text: str) -> TurnoutRecord:
    reader = csv.DictReader(io.StringIO(text.lstrip("\ufeff")), delimiter="\t")
    required = {"CONTEST_FULL_NAME", "CANDIDATE_FULL_NAME", "TOTAL", "CONTEST_TOTAL"}
    if reader.fieldnames is None or not required.issubset(reader.fieldnames):
        raise ParseError("not an Era B summary TSV")

    ed = vbm = registered = None
    for row in reader:
        # Exact match: primaries add per-party contests like
        # "Democratic Registration & Turnout" - only the citywide block counts.
        if row["CONTEST_FULL_NAME"] != "Registration & Turnout":
            continue
        if row["CANDIDATE_FULL_NAME"] == "Election Day Reporting Turnout":
            ed = _int_field(row, "TOTAL")
            registered = _int_field(row, "CONTEST_TOTAL")
        elif row["CANDIDATE_FULL_NAME"] == "VBM Reporting Turnout":
            vbm = _int_field(row, "TOTAL")

    if ed is None or vbm is None or registered is None:
        raise ParseError("citywide turnout rows not found in Era B TSV")
    return TurnoutRecord(
        ballots_counted_total=ed + vbm,
        registered_voters=registered,
        ballots_vbm=vbm,
        ballots_election_day=ed,
    )
