import csv

from sfcount.archival import ARCHIVAL_ROWS


def test_archival_rows_shape():
    assert len(ARCHIVAL_ROWS) == 2
    for row in ARCHIVAL_ROWS:
        assert row["parser"] == "archival"
        assert row["datetime_source"] == "archival"
        assert row["ballots_vbm"] + row["ballots_election_day"] == row["ballots_counted_total"]
    assert ARCHIVAL_ROWS[1]["ballots_counted_total"] == 364875  # certified final


from sfcount.timeline import stage_parse


def read_timeline(data):
    with open(data / "sf_count_timeline.csv", newline="") as f:
        return list(csv.DictReader(f))


def test_stage_parse_builds_timeline(mini_pipeline):
    data, raw = mini_pipeline
    stage_parse(data, raw, eras=("B", "C"))
    rows = read_timeline(data)
    assert len(rows) == 7  # 5 summary fixtures + 2 archival

    by_key = {(r["election_date"], r["snapshot"]): r for r in rows}
    modern = by_key[("2024-11-05", "20241108")]
    assert modern["ballots_counted_total"] == "289135"
    assert modern["ballots_vbm"] == "251467"
    assert modern["ballots_election_day"] == "37668"
    assert modern["registered_voters"] == "522265"
    assert modern["parser"] == "era_c_xml"
    assert modern["datetime_source"] == "header"
    assert modern["report_datetime"] == "2024-11-08T15:45:18"
    assert modern["source_url"].endswith("/results/20241105/data/20241108/summary.xml")

    night = by_key[("2024-11-05", "20241105_1")]
    assert night["report_seq"] == "1"
    assert modern["report_seq"] == "2"

    # the 2019 summary has no split; it is recovered from the psov precinct sums
    v2019 = by_key[("2019-11-05", "20191108")]
    assert v2019["ballots_counted_total"] == "190504"
    assert v2019["ballots_election_day"] == "45594"
    assert v2019["ballots_vbm"] == "144910"
    assert v2019["parser"] == "era_c_xml+psov"

    primary = by_key[("2016-06-07", "20160610")]
    assert primary["parser"] == "era_b_tsv"
    assert primary["datetime_source"] == "folder"  # no manifest entry
    assert primary["report_datetime"] == "2016-06-10T00:00:00"

    archival = by_key[("2012-11-06", "final")]
    assert archival["parser"] == "archival"
    assert rows[0]["election_date"] == "2012-11-06"  # sorted by election then time


def test_stage_parse_records_failures_not_crashes(mini_pipeline):
    data, raw = mini_pipeline
    bad = raw / "20241105" / "20241109" / "summary.xml"
    bad.parent.mkdir(parents=True)
    bad.write_text("<html>soft 404 that slipped through</html>")
    stage_parse(data, raw, eras=("B", "C"))
    with open(data / "parse_failures.csv", newline="") as f:
        failures = list(csv.DictReader(f))
    assert len(failures) == 1
    assert failures[0]["file"].endswith("20241109/summary.xml")
    assert len(read_timeline(data)) == 7  # bad file excluded, others parsed


def test_stage_parse_2019_without_psov_leaves_split_blank(mini_pipeline):
    data, raw = mini_pipeline
    (raw / "20191105/20191108/20191108_psov.xml").unlink()
    stage_parse(data, raw, eras=("B", "C"))
    v2019 = {(r["election_date"], r["snapshot"]): r
             for r in read_timeline(data)}[("2019-11-05", "20191108")]
    assert v2019["ballots_vbm"] == ""
    assert v2019["parser"] == "era_c_xml"


MISMATCHING_PSOV = """<?xml version="1.0"?><Report xmlns="StatementOfVotesCastRPT">
<Tablix2 Textbox1003="Precinct"><pdGroup_splitByPrecincts>
<cgGroup_splitByPrecincts><cgName cgName="Election Day"><Textbox18 ballots4="1" /></cgName></cgGroup_splitByPrecincts>
<cgGroup_splitByPrecincts><cgName cgName="Vote by Mail"><Textbox18 ballots4="2" /></cgName></cgGroup_splitByPrecincts>
</pdGroup_splitByPrecincts></Tablix2></Report>"""


def test_stage_parse_2019_psov_mismatch_fails_loudly(mini_pipeline):
    # a psov that doesn't reconcile with the summary total must be recorded as
    # a failure and the split left blank - never silently accepted
    data, raw = mini_pipeline
    (raw / "20191105/20191108/20191108_psov.xml").write_text(MISMATCHING_PSOV)
    stage_parse(data, raw, eras=("B", "C"))
    v2019 = {(r["election_date"], r["snapshot"]): r
             for r in read_timeline(data)}[("2019-11-05", "20191108")]
    assert v2019["ballots_vbm"] == ""
    assert v2019["parser"] == "era_c_xml"
    with open(data / "parse_failures.csv", newline="") as f:
        failures = list(csv.DictReader(f))
    assert len(failures) == 1
    assert "psov sum 3 != summary total 190504" in failures[0]["error"]


def test_stage_parse_distrusts_reuploaded_header_timestamps(mini_pipeline):
    # The DOE re-uploaded 2015/2016-era files in Dec 2023; such Last-Modified
    # values are migration artifacts, not report times -> folder-date fallback.
    data, raw = mini_pipeline
    manifest = (data / "manifest.csv").read_text().replace(
        "20161108,20161110,summary.txt,downloaded,2016-11-10T16:01:57",
        "20161108,20161110,summary.txt,downloaded,2023-12-19T17:03:31")
    (data / "manifest.csv").write_text(manifest)
    stage_parse(data, raw, eras=("B", "C"))
    row = {(r["election_date"], r["snapshot"]): r
           for r in read_timeline(data)}[("2016-11-08", "20161110")]
    assert row["datetime_source"] == "folder"
    assert row["report_datetime"] == "2016-11-10T00:00:00"
