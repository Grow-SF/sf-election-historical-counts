"""Rows recovered from web-archive captures of the live results pages.

Archive-It memento of sfelections.org/results/20121106/, captured 2012-11-12
02:00 UTC, page self-reports "Last Updated: November 11, 2012 16:28:21".
Sparse by nature; parser tag "archival" excludes them from days-to-90
derivation. Certified finals from the live final pages.
"""
ARCHIVAL_ROWS = [
    dict(election_date="2012-11-06", election_name="Consolidated General Election",
         snapshot="wb20121112020016", report_datetime="2012-11-11T16:28:21",
         ballots_counted_total=325298, ballots_vbm=174755,
         ballots_election_day=150543, registered_voters=502841,
         parser="archival", datetime_source="archival",
         source_url="https://wayback.archive-it.org/all/20121112020016/http://sfelections.org/results/20121106/"),
    dict(election_date="2012-11-06", election_name="Consolidated General Election",
         snapshot="final", report_datetime="2012-12-04T16:00:00",
         ballots_counted_total=364875, ballots_vbm=193196,
         ballots_election_day=171679, registered_voters=502841,
         parser="archival", datetime_source="archival",
         source_url="https://www.sfelections.org/results/20121106/"),
]
