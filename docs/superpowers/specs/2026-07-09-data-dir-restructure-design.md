# `data/` tiered restructure — design

**Date:** 2026-07-09
**Status:** approved (brainstorm)
**Goal:** make `data/` legible: the top level holds only the datasets a consumer
should reach for; source-scoped transcriptions, pipeline machinery, and
provenance apparatus each move one level down. No schema changes; every
source-scoped file survives byte-identical.

## Motivation

`data/` currently has 27 top-level entries: six overlapping turnout series,
two election indexes, pipeline state files, ledgers, manifests, and the
consolidated export hidden in `exports/`. Three pains, confirmed with the
maintainer:

1. **Consumer confusion** — a directory listing gives no signal about what to
   use; the headline rollup is buried in a one-file subdirectory.
2. **Maintenance burden** — the generated-vs-hand-maintained-vs-machinery map
   lives only in prose.
3. **Suspected redundancy** — mostly unfounded: the overlapping turnout series
   each transcribe a distinct primary source and carry distinct adjudications,
   so they stay. Only one file is truly dead (see Deletions).

Constraints established: nothing outside the repo deep-links into `data/`
paths (free to move); `packages/data/` is out of scope for this pass.

## Target layout

```
data/
  README.md                          # rewritten around the tiers
  sf_elections_consolidated.csv      # hoisted from exports/ (generated headline rollup)
  elections_master.csv               # comprehensive index (generated)
  sf_count_timeline.csv              # modern per-release record (sfcount output)
  sf_days_to_90.csv                  # per-election speed summary (sfcount output)
  sf_archival_canvass_points.csv     # historical per-observation record
  sf_franchise_by_election.csv       # per-election franchise join (generated)
  sources/                           # one file per primary source, moved byte-identical
    sf_turnout_pre1899.csv
    sf_turnout_1891_1907.csv
    sf_turnout_registrar_1899_1916.csv
    sf_turnout_reused_registration_1917_1945.csv
    sf_turnout_history_doe_1899_2019.csv
    sf_turnout_history_1960_2002.csv
    sf_vbm_share_sos.csv
    sf_registration_eligible.csv
    sf_registration_eligible_sov_1974_1998.csv
    sf_eligible_vap_estimate.csv
    sf_canvass_minutes_statements.csv
    sf_vote_by_district_1856_1863.csv
    sf_june2026_vbm_returns_by_day.csv
  pipeline/                          # sfcount machinery state
    manifest.csv
    elections.csv
    parse_failures.csv
  provenance/                        # citation/ledger apparatus
    mirror_manifest.csv
    newsbank_issue_docrefs.json
    pre1892_certified.md
    recovery_ledger_pre1965.md
    sov_crosscheck_ledger.md
  research/                          # unchanged
```

Top level: 27 entries → 10.

### Tier rules (for future files)

- **Top level** — datasets a reader opens directly: per-election or
  per-observation, either generated rollups or the two flagship counting
  records.
- **`sources/`** — hand-recovered or fetched transcriptions scoped to one
  primary source each. These are the inputs to the generated tier; they are
  the provenance and are never merged.
- **`pipeline/`** — files the `sfcount` pipeline reads/writes as machinery
  (inventory, fetch manifest, parse-failure log). Not for human consumption.
- **`provenance/`** — citation ledgers, mirror inventory, and citation-helper
  maps.

### Deletions

- `sf_night_floor_1964_2026.csv` — no committed generator, documented in the
  data README as "a record, not a pipeline stage," and not a build input
  (`build_viz_data.py` computes `night_floor.json` independently from the
  turnout/VBM CSVs). Deleted; git history preserves it.
- `data/exports/` — directory removed; its single file hoists to top level.

## Code changes (mechanical path updates)

- **`sfcount`** — keeps `--data-dir data` (default unchanged).
  `inventory.py`, `fetch.py`, and the parse-failure writer in `timeline.py`
  target `data_dir / "pipeline"`; `timeline.py` (count timeline) and
  `derive.py` (days-to-90) keep writing to the top level. `tests/conftest.py`
  and affected tests follow.
- **Generator scripts** — path-constant updates in `build_viz_data.py`,
  `build_consolidated_export.py` (output becomes
  `data/sf_elections_consolidated.csv`), `build_elections_master.py`,
  `build_franchise_csv.py`, `gen_docs.py`, `fetch_sos_registration.py`,
  `recover_sov_registration.py`.
- The deleted night-floor CSV has zero code references (confirmed by a
  repo-wide grep), so its removal requires no code change;
  `build_viz_data.py` already computes `night_floor.json` independently.
- All generated outputs must be byte-identical after regeneration, except
  where a generated file embeds a moved path (verify and accept only
  path-string diffs).

## Docs & skills

- **`data/README.md`** — rewritten around the tiers: headline files first,
  then the sources underneath, pipeline/provenance last. One line notes the
  2026-07 restructure so old paths in dated documents are explainable.
- **Living docs updated** — top-level `README.md`, `docs/sources.md`,
  `docs/missing.md`, `docs/denominator-errors.md`,
  `docs/archive-recovery-runbook.md`, `docs/research/RUNBOOK.md`,
  `docs/eligible-denominator-notes.md`, `docs/doe-data-discrepancies.md`,
  `packages/data/README.md`, and the project skills
  `ingesting-doe-results` and `newsbank-election-recovery`.
- **Dated records left untouched** — `docs/analysis/*`,
  `docs/superpowers/plans/*`, `docs/superpowers/specs/*` (prior to this one),
  and `docs/research/night-recovery-*` are historical logs; their old paths
  stay as written.

## Verification

1. `pytest` and `vitest` pass.
2. Re-run the generator chain — offline-runnable `sfcount` stages,
   `build_elections_master.py`, `build_franchise_csv.py`,
   `build_viz_data.py`, `build_consolidated_export.py`, `gen_docs.py` — and
   confirm regenerated files are unchanged modulo moved-path strings.
3. Repo-wide grep for every old path (e.g. `data/exports/`,
   `data/sf_turnout_`, `data/manifest.csv`) with an allowlist for the dated
   historical docs; zero stragglers elsewhere.

## Out of scope

- `packages/data/` JSON consolidation (behind `index.ts`; cosmetic only).
- Any merging of source-scoped transcriptions (rejected: breaks the
  one-file-per-primary-source provenance model).
- Schema or value changes to any dataset.
