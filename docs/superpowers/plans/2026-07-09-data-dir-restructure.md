# `data/` Tiered Restructure Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reorganize `data/` into a tiered layout (headline datasets at top level; `sources/`, `pipeline/`, `provenance/` subdirectories) per the approved spec `docs/superpowers/specs/2026-07-09-data-dir-restructure-design.md`, with all code, tests, and living docs updated.

**Architecture:** Pure file moves (`git mv`, byte-identical) plus mechanical path-constant updates in the `sfcount` package and the generator scripts. Each task moves one tier and updates its consumers in the same commit, so the repo is working at every commit. No schema or value changes anywhere.

**Tech Stack:** Python 3 (`sfcount` package, `scripts/*.py`), pytest, vitest (unaffected but run as a gate), git.

## Global Constraints

- Every moved file is moved with `git mv` and stays byte-identical (no content edits to CSVs/JSON/md being moved).
- Regenerated outputs must be byte-identical to the committed versions, except diffs that are purely moved-path strings.
- `sfcount`'s CLI default `--data-dir data` does not change.
- Dated historical docs are NOT edited: `docs/analysis/*`, `docs/superpowers/plans/*`, `docs/superpowers/specs/*` (except this plan's own spec is already correct), `docs/research/night-recovery-*`.
- No em dashes in any new prose written for docs (use commas, colons, parentheses, or separate sentences).
- Run all commands from the repo root (the worktree root).
- Each task ends with `uv run pytest -q` passing.

---

### Task 1: `pipeline/` tier (sfcount machinery files)

Move `data/manifest.csv`, `data/elections.csv`, `data/parse_failures.csv` to `data/pipeline/` and point `sfcount` + tests at the new location. The consumer-facing `sfcount` outputs (`sf_count_timeline.csv`, `sf_days_to_90.csv`) stay at `data/` top level.

**Files:**
- Move: `data/manifest.csv` → `data/pipeline/manifest.csv`, `data/elections.csv` → `data/pipeline/elections.csv`, `data/parse_failures.csv` → `data/pipeline/parse_failures.csv`
- Modify: `sfcount/inventory.py`, `sfcount/fetch.py`, `sfcount/timeline.py`, `tests/conftest.py`, `tests/test_inventory.py`, `tests/test_timeline.py`

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: `sfcount` stage functions keep their signatures (`stage_inventory(data_dir)`, `stage_fetch(data_dir, raw_dir, eras)`, `stage_parse(data_dir, raw_dir, eras)`); they now read/write machinery files under `data_dir / "pipeline"`. Later tasks rely on `data/pipeline/` existing in git.

- [ ] **Step 1: Move the files**

```bash
mkdir -p data/pipeline
git mv data/manifest.csv data/elections.csv data/parse_failures.csv data/pipeline/
```

- [ ] **Step 2: Update the tests to the new contract (they must fail first)**

In `tests/conftest.py`, the fixture writes machinery files into `data/pipeline/`. Replace lines 12–14 and the two `write_text` targets:

```python
    data, raw = tmp_path / "data", tmp_path / "raw"
    pipeline = data / "pipeline"
    pipeline.mkdir(parents=True)
    raw.mkdir()
```

and

```python
    (pipeline / "elections.csv").write_text(
```

```python
    (pipeline / "manifest.csv").write_text(
```

In `tests/test_inventory.py:47`:

```python
    rows = list(csv.DictReader((tmp_path / "pipeline" / "elections.csv").open()))
```

In `tests/test_timeline.py`, lines 67 and 101:

```python
    with open(data / "pipeline" / "parse_failures.csv", newline="") as f:
```

and lines 111–114:

```python
    manifest = (data / "pipeline" / "manifest.csv").read_text().replace(
        ...  # keep the existing replace() arguments exactly as they are
    (data / "pipeline" / "manifest.csv").write_text(manifest)
```

(`tests/test_fetch.py` needs no change: `save_manifest`/`load_manifest` take explicit paths. `tests/test_derive.py` and `tests/test_cli.py` need no change: `sf_count_timeline.csv` and `sf_days_to_90.csv` stay at the top level.)

- [ ] **Step 3: Run the sfcount tests to verify they fail**

Run: `uv run pytest tests/test_inventory.py tests/test_timeline.py tests/test_cli.py -q`
Expected: FAIL (FileNotFoundError / assertion errors, because `sfcount` still writes to the old paths).

- [ ] **Step 4: Update sfcount**

`sfcount/inventory.py` (`write_inventory`, `load_elections`, `stage_inventory` print):

```python
def write_inventory(seen: dict[dt.date, str], data_dir: Path) -> None:
    (data_dir / "pipeline").mkdir(parents=True, exist_ok=True)
    with open(data_dir / "pipeline" / "elections.csv", "w", newline="") as f:
```

```python
def load_elections(data_dir: Path, eras: tuple[str, ...]) -> list[dict]:
    with open(data_dir / "pipeline" / "elections.csv") as f:
```

```python
    print(f"inventory: {len(seen)} elections -> {data_dir / 'pipeline' / 'elections.csv'}", flush=True)
```

`sfcount/fetch.py` (`stage_fetch`, lines 170 and 176):

```python
    manifest = load_manifest(data_dir / "pipeline" / "manifest.csv")
```

```python
        save_manifest(data_dir / "pipeline" / "manifest.csv", manifest)
```

Also add at the top of `stage_fetch`, right after its signature line:

```python
    (data_dir / "pipeline").mkdir(parents=True, exist_ok=True)
```

`sfcount/timeline.py` (line 40 manifest load; lines 101–107 writers):

```python
    manifest = load_manifest(data_dir / "pipeline" / "manifest.csv")
```

```python
    data_dir.mkdir(parents=True, exist_ok=True)
    with open(data_dir / "sf_count_timeline.csv", "w", newline="") as f:
        ...  # unchanged
    (data_dir / "pipeline").mkdir(parents=True, exist_ok=True)
    with open(data_dir / "pipeline" / "parse_failures.csv", "w", newline="") as f:
```

- [ ] **Step 5: Run the full Python suite to verify it passes**

Run: `uv run pytest -q`
Expected: PASS (same test count as on `main`, zero failures).

- [ ] **Step 6: Commit**

```bash
git add -A
git commit -m "refactor(data): move sfcount machinery files to data/pipeline/"
```

---

### Task 2: `sources/` tier (source-scoped transcriptions)

Move the 13 source-scoped files into `data/sources/` and update every script that reads them. Generated outputs must not change.

**Files:**
- Move (all `git mv` from `data/` to `data/sources/`): `sf_turnout_pre1899.csv`, `sf_turnout_1891_1907.csv`, `sf_turnout_registrar_1899_1916.csv`, `sf_turnout_reused_registration_1917_1945.csv`, `sf_turnout_history_doe_1899_2019.csv`, `sf_turnout_history_1960_2002.csv`, `sf_vbm_share_sos.csv`, `sf_registration_eligible.csv`, `sf_registration_eligible_sov_1974_1998.csv`, `sf_eligible_vap_estimate.csv`, `sf_canvass_minutes_statements.csv`, `sf_vote_by_district_1856_1863.csv`, `sf_june2026_vbm_returns_by_day.csv`
- Modify: `scripts/build_viz_data.py`, `scripts/build_consolidated_export.py`, `scripts/build_elections_master.py`, `scripts/build_franchise_csv.py`, `scripts/fetch_sos_registration.py`, `scripts/recover_sov_registration.py`

**Interfaces:**
- Consumes: nothing from Task 1 (different files).
- Produces: source CSVs live at `data/sources/<name>.csv`. Define and use `SRC = ROOT / "data" / "sources"` in `build_viz_data.py` and `build_consolidated_export.py`, and `SOURCES = DATA / "sources"` in `build_franchise_csv.py`. Task 4's README rewrite documents this layout.

- [ ] **Step 1: Move the files**

```bash
mkdir -p data/sources
git mv data/sf_turnout_pre1899.csv data/sf_turnout_1891_1907.csv \
       data/sf_turnout_registrar_1899_1916.csv \
       data/sf_turnout_reused_registration_1917_1945.csv \
       data/sf_turnout_history_doe_1899_2019.csv \
       data/sf_turnout_history_1960_2002.csv \
       data/sf_vbm_share_sos.csv data/sf_registration_eligible.csv \
       data/sf_registration_eligible_sov_1974_1998.csv \
       data/sf_eligible_vap_estimate.csv data/sf_canvass_minutes_statements.csv \
       data/sf_vote_by_district_1856_1863.csv \
       data/sf_june2026_vbm_returns_by_day.csv \
       data/sources/
```

- [ ] **Step 2: Update `scripts/build_viz_data.py`**

Add one constant next to the existing `ROOT`/`OUT` constants (around line 19–20):

```python
SRC = ROOT / "data" / "sources"
```

Then change every read of a moved file from `ROOT / "data" / "<name>"` to `SRC / "<name>"`. Exact lines (current numbering): 269, 281, 306, 336, 348, 415 (`pre1899 = SRC / "sf_turnout_pre1899.csv"`), 434 (`gap_csv = SRC / "sf_turnout_1891_1907.csv"`), 447, 464 (`registrar_csv = SRC / "sf_turnout_registrar_1899_1916.csv"`), 491 (`reused_csv = SRC / "sf_turnout_reused_registration_1917_1945.csv"`), 523 (`reg_path = SRC / "sf_registration_eligible.csv"`), 540 (`sov_path = SRC / "sf_registration_eligible_sov_1974_1998.csv"`), 567 (`vap_path = SRC / "sf_eligible_vap_estimate.csv"`). Lines 82 (`sf_count_timeline.csv`), 138 (`sf_archival_canvass_points.csv`), and 209 (`newsbank_issue_docrefs.json`) do NOT change in this task. Update the module docstring's `data/*.csv` phrasing to `data/ and data/sources/ CSVs`.

- [ ] **Step 3: Update `scripts/build_consolidated_export.py`**

Add next to `OUT` (line 19):

```python
SRC = ROOT / "data" / "sources"
```

Change: lines 97–98 to `open(SRC / "sf_turnout_reused_registration_1917_1945.csv")`; line 109 to `open(SRC / fn)`; line 152 to `open(SRC / "sf_turnout_history_1960_2002.csv")`; line 160 to `open(SRC / "sf_turnout_history_doe_1899_2019.csv")`; line 164 to `open(SRC / "sf_vbm_share_sos.csv")`. Lines 77 (`elections_master.csv`), 117 (`sf_archival_canvass_points.csv`), and 128 (`sf_count_timeline.csv`) do NOT change.

- [ ] **Step 4: Update `scripts/build_elections_master.py`**

Line 272: `with open(ROOT / "data" / "sources" / fn, newline="") as f:`
Line 277: `with open(ROOT / "data" / "sources" / "sf_turnout_history_doe_1899_2019.csv", newline="") as f:`
Comment lines 115 and 216: change `data/sf_turnout_registrar_1899_1916.csv` to `data/sources/sf_turnout_registrar_1899_1916.csv`.

- [ ] **Step 5: Update `scripts/build_franchise_csv.py`**

Add below `DATA = ROOT / "data"` (line 26):

```python
SOURCES = DATA / "sources"
```

Change lines 66, 73, 83 to open `SOURCES / "sf_turnout_history_doe_1899_2019.csv"`, `SOURCES / "sf_turnout_history_1960_2002.csv"`, `SOURCES / "sf_vbm_share_sos.csv"`. Line 92 (`DATA / "sf_count_timeline.csv"`) and line 28 (`OUT = DATA / "sf_franchise_by_election.csv"`) do NOT change.

- [ ] **Step 6: Update the two fetch/recovery scripts**

`scripts/fetch_sos_registration.py` line 28:

```python
OUT = ROOT / "data" / "sources" / "sf_registration_eligible.csv"
```

and its docstring line 16: `Output: data/sources/sf_registration_eligible.csv ...`.
`scripts/recover_sov_registration.py` docstring line 9: change `data/sf_registration_eligible_sov_1974_1998.csv` to `data/sources/sf_registration_eligible_sov_1974_1998.csv` (grep the file for any other occurrence of the old path and update those too).

- [ ] **Step 7: Regenerate and verify byte-identical outputs**

```bash
python3 scripts/build_viz_data.py
python3 scripts/build_elections_master.py
python3 scripts/build_franchise_csv.py
python3 scripts/build_consolidated_export.py
git status --short
```

Expected: `git status` shows ONLY the renamed CSVs and the six modified scripts. No modified files under `packages/data/`, no modified `data/elections_master.csv`, `data/sf_franchise_by_election.csv`, or `data/exports/sf_elections_consolidated.csv`. If any generated file changed, STOP and diff it: only investigate, do not commit a value change.

- [ ] **Step 8: Run tests, then commit**

Run: `uv run pytest -q` — expected PASS.

```bash
git add -A
git commit -m "refactor(data): move source-scoped transcriptions to data/sources/"
```

---

### Task 3: hoist the consolidated export, delete the dead file, `provenance/` tier

**Files:**
- Move: `data/exports/sf_elections_consolidated.csv` → `data/sf_elections_consolidated.csv`; `data/mirror_manifest.csv`, `data/newsbank_issue_docrefs.json`, `data/pre1892_certified.md`, `data/recovery_ledger_pre1965.md`, `data/sov_crosscheck_ledger.md` → `data/provenance/`
- Delete: `data/sf_night_floor_1964_2026.csv`, the emptied `data/exports/` directory
- Modify: `scripts/build_consolidated_export.py`, `scripts/build_viz_data.py`

**Interfaces:**
- Consumes: `SRC` constants from Task 2 (already committed).
- Produces: the rollup at `data/sf_elections_consolidated.csv` (Task 4 documents it); provenance helpers under `data/provenance/`.

- [ ] **Step 1: Move and delete**

```bash
mkdir -p data/provenance
git mv data/exports/sf_elections_consolidated.csv data/sf_elections_consolidated.csv
git mv data/mirror_manifest.csv data/newsbank_issue_docrefs.json \
       data/pre1892_certified.md data/recovery_ledger_pre1965.md \
       data/sov_crosscheck_ledger.md data/provenance/
git rm data/sf_night_floor_1964_2026.csv
rmdir data/exports 2>/dev/null || true
```

(`sf_night_floor_1964_2026.csv` has zero code consumers, confirmed by repo-wide grep; git history preserves it.)

- [ ] **Step 2: Update the two scripts**

`scripts/build_consolidated_export.py` line 19:

```python
OUT = ROOT / "data" / "sf_elections_consolidated.csv"
```

and its docstring line 2: `"""Build data/sf_elections_consolidated.csv — one row per SF election`. Line 169's `OUT.parent.mkdir(exist_ok=True)` is now a no-op on an existing `data/`; leave it.

`scripts/build_viz_data.py` line 209:

```python
    docref_file = ROOT / "data" / "provenance" / "newsbank_issue_docrefs.json"
```

- [ ] **Step 3: Regenerate and verify**

```bash
python3 scripts/build_consolidated_export.py
python3 scripts/build_viz_data.py
git status --short
```

Expected: only the moves/deletion and the two script edits; `data/sf_elections_consolidated.csv` and `packages/data/*.json` byte-identical (no content diff).

- [ ] **Step 4: Run tests, then commit**

Run: `uv run pytest -q` — expected PASS.

```bash
git add -A
git commit -m "refactor(data): hoist consolidated export, add provenance/, drop dead night-floor CSV"
```

---

### Task 4: docs and skills sweep

**Files:**
- Rewrite: `data/README.md`
- Modify: `README.md`, `packages/data/README.md`, `docs/sources.md`, `docs/missing.md`, `docs/denominator-errors.md`, `docs/archive-recovery-runbook.md`, `docs/research/RUNBOOK.md`, `docs/eligible-denominator-notes.md`, `docs/doe-data-discrepancies.md`, `docs/doe-records-request.md`, `docs/research/registration-law-history-1866-1945.md`, `.claude/skills/ingesting-doe-results/SKILL.md`, `.claude/skills/newsbank-election-recovery/SKILL.md` (each only where it cites a moved path; skip any that turn out to have none)

**Interfaces:**
- Consumes: the final layout from Tasks 1–3.
- Produces: docs that match the new layout; Task 5 greps against them.

- [ ] **Step 1: Rewrite `data/README.md`**

Keep all existing per-file documentation content (column tables, caveats, definitions) but reorganize into the tier structure. Required shape:

1. Title + intro (keep current framing).
2. "Start here" section: `sf_elections_consolidated.csv` (path updated: no more `exports/`).
3. Coverage table: update every path (`sources/sf_turnout_pre1899.csv` etc.); DELETE the `sf_night_floor_1964_2026.csv` row and its per-file section (note its deletion once in the restructure note instead).
4. A short "Layout" section stating the tier rules verbatim from the spec: top level = datasets you open directly; `sources/` = one file per primary source, the inputs and the provenance, never merged; `pipeline/` = sfcount machinery, not for human consumption; `provenance/` = citation ledgers and helper maps. Include one line: "Restructured 2026-07: files previously at the top level moved into these tiers; older dated docs may cite pre-move paths."
5. The existing per-file sections, grouped under tier headings, all internal links/paths updated.
6. Keep the Citing and Reproducing/provenance sections, paths updated (e.g. modern pipeline files now `pipeline/manifest.csv`, `pipeline/elections.csv`).

No em dashes in newly written prose (existing prose being moved verbatim may keep its punctuation).

- [ ] **Step 2: Update the other docs and skills**

For each remaining file in the Files list: `grep -n 'data/' <file>`, and update every reference to a moved path:
- `data/exports/sf_elections_consolidated.csv` → `data/sf_elections_consolidated.csv` (README.md lines 30 and 130)
- `data/sf_turnout_*` / `data/sf_registration_*` / `data/sf_eligible_vap_estimate.csv` / `data/sf_vbm_share_sos.csv` / `data/sf_canvass_minutes_statements.csv` / `data/sf_vote_by_district_1856_1863.csv` / `data/sf_june2026_vbm_returns_by_day.csv` → same name under `data/sources/`
- `data/manifest.csv`, `data/elections.csv`, `data/parse_failures.csv` → same name under `data/pipeline/`
- `data/mirror_manifest.csv`, `data/newsbank_issue_docrefs.json`, `data/pre1892_certified.md`, `data/recovery_ledger_pre1965.md`, `data/sov_crosscheck_ledger.md` → same name under `data/provenance/`
- References to `data/sf_night_floor_1964_2026.csv`: reword to note the file was deleted in the 2026-07 restructure (the chart's `night_floor.json` is computed from the turnout/VBM CSVs).

In `packages/data/README.md`, update the `night_floor.json` row's inputs cell to: `computed live from the turnout/VBM CSVs` (drop the reference to the deleted CSV).

Do NOT touch `docs/analysis/*`, `docs/superpowers/plans/*` (other than this plan), `docs/superpowers/specs/*`, `docs/research/night-recovery-*`.

- [ ] **Step 3: Regenerate docs and verify**

```bash
python3 scripts/gen_docs.py
git status --short
```

Expected: only the intended doc/skill edits (plus any file `gen_docs.py` legitimately rewrites). `gen_docs.py` also re-runs `build_consolidated_export.py`; confirm `data/sf_elections_consolidated.csv` is unchanged.

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "docs: re-tier data/README and update living docs for the data/ restructure"
```

---

### Task 5: final verification

**Files:** none created; fixes only if the sweep finds stragglers.

**Interfaces:**
- Consumes: everything above.
- Produces: a verified, complete restructure.

- [ ] **Step 1: Full test suites**

Run: `uv run pytest -q` — expected PASS.
Run: `pnpm test` (vitest) — expected PASS (charts read `packages/data` via `index.ts`, which this work never touched).

- [ ] **Step 2: Full generator chain, clean diff**

```bash
python3 scripts/build_elections_master.py
python3 scripts/build_viz_data.py
python3 scripts/build_franchise_csv.py
python3 scripts/build_consolidated_export.py
python3 scripts/gen_docs.py
git status --short
```

Expected: empty (every generator reproduces the committed files exactly). Skip `sfcount` network stages (`inventory`/`fetch`); `uv run sfcount parse derive` may be run offline if `raw/` is populated, otherwise the pytest suite already covers the parse/derive path logic via fixtures.

- [ ] **Step 3: Straggler grep**

```bash
grep -rn "data/exports\|data/sf_turnout_\|data/sf_registration_\|data/sf_eligible_vap\|data/sf_vbm_share\|data/sf_canvass_minutes\|data/sf_vote_by_district\|data/sf_june2026\|data/sf_night_floor\|data/manifest.csv\|data/elections.csv\|data/parse_failures\|data/mirror_manifest\|data/newsbank_issue_docrefs\|data/pre1892_certified\|data/recovery_ledger\|data/sov_crosscheck" \
  --include='*.py' --include='*.ts' --include='*.tsx' --include='*.cjs' --include='*.md' \
  . 2>/dev/null | grep -v node_modules \
  | grep -v "docs/analysis/\|docs/superpowers/plans/\|docs/superpowers/specs/\|docs/research/night-recovery-\|data/sources/\|data/pipeline/\|data/provenance/"
```

Expected: zero hits (the trailing filter drops the allowlisted dated docs and the new-path false positives, e.g. `data/sources/sf_turnout_...` contains `data/sources/`, not `data/sf_turnout_`; verify each residual hit by eye and fix any true straggler in living code/docs).

- [ ] **Step 4: Final commit (if the sweep fixed anything)**

```bash
git add -A
git commit -m "docs: fix remaining pre-restructure data/ paths"
```
