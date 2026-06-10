from pathlib import Path

import pytest

from sfcount.parsers import ParseError, TurnoutRecord, parse_era_b_tsv, parse_era_c_xml

FIXTURES = Path(__file__).parent / "fixtures"


def read(name: str) -> str:
    path = FIXTURES / name
    # Era B summary.txt files were exported as Windows-1252/Latin-1;
    # Era C XML files are UTF-8 (possibly with BOM). Try UTF-8 first.
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="latin-1")


def test_era_c_modern():
    rec = parse_era_c_xml(read("era_c_modern.xml"))
    assert rec == TurnoutRecord(
        ballots_counted_total=289135,
        registered_voters=522265,
        ballots_vbm=251467,
        ballots_election_day=37668,
    )


def test_era_c_election_night():
    rec = parse_era_c_xml(read("era_c_night.xml"))
    assert rec.ballots_counted_total == 197108
    assert rec.registered_voters == 522265
    assert rec.ballots_vbm == 197108
    assert rec.ballots_election_day == 0  # zero, not None


def test_era_c_2019_variant_has_no_split():
    rec = parse_era_c_xml(read("era_c_2019.xml"))
    assert rec.ballots_counted_total == 190504
    assert rec.registered_voters == 495050
    assert rec.ballots_vbm is None
    assert rec.ballots_election_day is None


def test_era_c_rejects_non_xml():
    with pytest.raises(ParseError):
        parse_era_c_xml("<html>404 not found</html>")
    with pytest.raises(ParseError):
        parse_era_c_xml("not xml at all")


def test_era_c_rejects_xml_without_turnout():
    with pytest.raises(ParseError):
        parse_era_c_xml("<?xml version='1.0'?><Report></Report>")


def test_era_c_rejects_turnout_block_with_missing_attributes():
    # a truncated/corrupt download must raise ParseError, never TypeError
    broken = '<Report><electorGroupId2 electorGroupId2="Total" ballots3="5" /></Report>'
    with pytest.raises(ParseError):
        parse_era_c_xml(broken)  # Textbox32 missing


def test_era_b_general():
    rec = parse_era_b_tsv(read("era_b_general.txt"))
    assert rec == TurnoutRecord(
        ballots_counted_total=283049,
        registered_voters=513573,
        ballots_vbm=151149,
        ballots_election_day=131900,
    )


def test_era_b_primary_uses_citywide_block_not_party_blocks():
    rec = parse_era_b_tsv(read("era_b_primary.txt"))
    assert rec == TurnoutRecord(
        ballots_counted_total=225014,
        registered_voters=468238,
        ballots_vbm=135794,
        ballots_election_day=89220,
    )


def test_era_b_rejects_non_tsv():
    with pytest.raises(ParseError):
        parse_era_b_tsv("<html>404</html>")
    with pytest.raises(ParseError):
        parse_era_b_tsv("")


def test_era_b_rejects_tsv_without_turnout_rows():
    header = "CONTEST_ID\tTOTAL\tCONTEST_FULL_NAME\tCANDIDATE_FULL_NAME\tCONTEST_TOTAL\n"
    with pytest.raises(ParseError):
        parse_era_b_tsv(header + "1\t5\tMayor\tALICE\t10\n")


def test_era_b_rejects_truncated_row():
    header = "CONTEST_ID\tTOTAL\tCONTEST_FULL_NAME\tCANDIDATE_FULL_NAME\tCONTEST_TOTAL\n"
    # CONTEST_TOTAL absent on the ED row - DictReader yields None
    truncated = header + "1\t131900\tRegistration & Turnout\tElection Day Reporting Turnout"
    with pytest.raises(ParseError):
        parse_era_b_tsv(truncated)


def test_era_b_rejects_header_missing_required_columns():
    with pytest.raises(ParseError):
        parse_era_b_tsv("CONTEST_FULL_NAME\tCANDIDATE_FULL_NAME\nx\ty\n")
