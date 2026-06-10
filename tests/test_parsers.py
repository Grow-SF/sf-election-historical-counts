from pathlib import Path

import pytest

from sfcount.parsers import ParseError, TurnoutRecord, parse_era_c_xml

FIXTURES = Path(__file__).parent / "fixtures"


def read(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8-sig")


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
