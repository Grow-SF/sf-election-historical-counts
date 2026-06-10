# SF Vote-Count Timeline

How long San Francisco takes to count ballots, measured from the Department of
Elections' own per-release results reports, Nov 2015 - present, plus one
archival recovery (Nov 2012).

Reimplementation of `sf-long-count-archive/` (kept as read-only reference):
ingests the structured files SF Elections publishes per release —
`summary.xml` (2019+, Dominion) and `summary.txt` TSV (2008-2018) — instead of
parsing PDFs. Report timestamps come from HTTP `Last-Modified` headers
captured in `data/manifest.csv` (with a folder-date fallback where the server
re-uploaded old files). Counts were reconciled row-for-row against the
PDF-derived archive dataset (`tests/test_reconciliation.py`).

Two corrections over the archive dataset, found by that reconciliation:

- **Presidential primaries 2020-03 and 2024-03** now carry citywide totals.
  The archive's PDF parser had read the first party block (Democratic), so it
  under-reported both. Verified against the DOE results pages:
  2020-03-03 = 305,184 of 503,899 (60.56%); 2024-03-05 = 233,465 (46.61%).
- **Nov 2019 ED/VBM split recovered.** No 2019 summary format publishes it;
  it is summed from the per-precinct statement of the vote
  (`{snap}_psov.xml`, parser tag `era_c_xml+psov`), accepted only when the
  precinct sums reconcile exactly with the summary total. Three snapshots
  (`20191105_2`, `_3`, `20191125`) have no published psov and stay blank.

## Usage

    uv run sfcount all            # full pipeline
    uv run sfcount fetch          # resumable; ~25 min cold

Stages: `inventory` (election list; seeds recently-held elections the sf.gov
index lists only after certification) → `fetch` (probe + download snapshots)
→ `parse` (→ `data/sf_count_timeline.csv`) → `validate` (invariants incl.
certified-final cross-checks; nonzero exit on failure) → `derive`
(→ `data/sf_days_to_90.csv`) → `artifact` (regenerates the data array in
`artifact/sf-long-count.jsx`).

After a new election: add it to `SUPPLEMENTAL_ELECTIONS` in
`sfcount/inventory.py` if the sf.gov index doesn't list it yet, then run
`uv run sfcount all` any time during the canvass; rerun after certification,
add the certified total to `CERTIFIED_FINALS` in `sfcount/validate.py`, and
commit `data/` and the artifact.

## Tests

    uv run pytest                 # offline suite (fixtures are real downloaded files)
    uv run pytest -m network      # live smoke tests against sfelections.org
    uv run pytest -m migration    # reconciliation vs sf-long-count-archive/

## Data boundaries

- Per-release snapshots exist on sfelections.org only from Nov 2015.
- Do not backfill VBM/election-day splits from the eData "returned VBM
  ballots" tool: returned-and-accepted is not the same measure as counted.
- Nov 2012 is recovered from a single Wayback capture (`parser=archival`),
  excluded from days-to-90 derivation.
- The Nov 2015 and Jun 2016 files were re-uploaded by the DOE in Dec 2023,
  so their `Last-Modified` headers are migration artifacts; those rows use
  folder dates (midnight), matching the archive's behavior.
