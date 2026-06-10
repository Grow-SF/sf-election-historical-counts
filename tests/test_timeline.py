from sfcount.archival import ARCHIVAL_ROWS


def test_archival_rows_shape():
    assert len(ARCHIVAL_ROWS) == 2
    for row in ARCHIVAL_ROWS:
        assert row["parser"] == "archival"
        assert row["datetime_source"] == "archival"
        assert row["ballots_vbm"] + row["ballots_election_day"] == row["ballots_counted_total"]
    assert ARCHIVAL_ROWS[1]["ballots_counted_total"] == 364875  # certified final
