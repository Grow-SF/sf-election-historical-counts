from sfcount.validate import (
    CERTIFIED_FINALS, check_certified, check_monotonic, check_split_sum, validate_rows,
)


def row(edate="2024-11-05", snap="x", total="100", vbm="", ed="", parser="era_c_xml"):
    return {
        "election_date": edate, "snapshot": snap,
        "ballots_counted_total": total, "ballots_vbm": vbm,
        "ballots_election_day": ed, "report_datetime": "2024-11-06T12:00:00",
        "parser": parser,
    }


def test_monotonic_ok_and_violation():
    rows = [row(snap="a", total="100"), row(snap="b", total="100"), row(snap="c", total="150")]
    assert check_monotonic(rows) == []
    rows.append(row(snap="d", total="149"))
    errs = check_monotonic(rows)
    assert len(errs) == 1 and "149" in errs[0]


def test_split_sum():
    assert check_split_sum([row(total="100", vbm="60", ed="40")]) == []
    assert check_split_sum([row(total="100", vbm="", ed="")]) == []  # no split published
    errs = check_split_sum([row(total="100", vbm="60", ed="41")])
    assert len(errs) == 1


def test_certified_finals():
    assert CERTIFIED_FINALS["2024-11-05"] == 412231
    good = [row(total="412231")]
    assert check_certified(good) == []
    bad = [row(total="412230")]
    assert len(check_certified(bad)) == 1
    # elections we have no certified number for are not checked
    assert check_certified([row(edate="2026-06-02", total="5")]) == []


def test_validate_rows_aggregates():
    rows = [row(snap="a", total="100", vbm="60", ed="41")]
    errs = validate_rows(rows)
    assert any("split" in e for e in errs)
