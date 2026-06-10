# SF Vote-Count Timeline

How long San Francisco takes to count ballots, measured from the Department of
Elections' own per-release summary reports, Nov 2015 – Jun 2026, plus one
archival recovery (Nov 2012).

## Contents

| file | what it is |
|---|---|
| sf-count-timeline-pipeline-plan.md | Design doc: scope, schema, pipeline stages, era taxonomy, risks, locked decisions. Written and reviewed before any code. |
| sfcount.py | The pipeline. Subcommands: `inventory`, `fetch`, `parse`, `derive`. Era-dispatched PDF parsers (Era C Dominion 2019+, two layout variants; Era B 2008–2018 incl. per-party primary blocks). Probe-miss cache makes fetch resumable. Archival rows documented inline. |
| elections.csv | Stage 0 inventory, 47 elections Nov 2000 – Jun 2026, era-tagged. |
| sf_count_timeline.csv | Main output: 242 rows, one per results release. Cumulative total, VBM / election-day split (227 rows; Nov 2019 format publishes none), registered voters, PDF-internal timestamp, source URL, parser tag. |
| sf_days_to_90.csv | Derived: per election, final ballots, % counted by midnight, days to first report ≥ 90% of final. Archival-parser elections excluded. |
| sf-long-count.jsx | "The Long Count" — React/Recharts page. Trajectory overlay with 90% rule, type filters (Primary/General/Special), by-year trend scatters, days-to-90 bars, per-election VBM/ED stacked step-area, 2012 archival marker. Self-contained; data array embedded. |

## Reproduce

    python3 sfcount.py inventory
    python3 sfcount.py fetch B,C     # resumable; ~25 min cold
    python3 sfcount.py parse B,C
    python3 sfcount.py derive

Requires requests, pdfplumber. Raw PDFs land in raw/, outputs in out/.

## Data boundaries

- Per-release snapshots exist on sfelections.org only from Nov 2015
  (pattern: /results/{election}/data/{report_date}/summary.pdf;
  election night: {date}_1 … _4).
- 2008–2014 and pre-2008 require web-archive recovery. web.archive.org content
  was unreachable from the build environment; wayback.archive-it.org worked and
  yielded the Nov 2012 point (89.2% on day 4.85). IA's availability API shows
  more 2012 canvass captures exist — a local Wayback stage would extend this.
- Jun 2026 uncertified at build time; its denominator is the count to date.

## Validation performed

Zero parse failures (242 rows). Monotonicity checked. ED+VBM = total on all
227 split rows. Certified-final cross-checks exact: Nov 2024 = 412,231,
Nov 2016 = 414,528, Nov 2012 = 364,875.

Built 2026-06-09.
