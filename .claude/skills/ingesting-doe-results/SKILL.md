---
name: ingesting-doe-results
description: Use when SF Department of Elections results for an election change — a new per-release summary.xml, an "the <month year> results are now final" message, or a certified Final Summary Report — OR whenever you are about to change an election's ballot total, turnout, count, or trajectory in data/*.csv or packages/data/*.json. Symptoms: a fresh sfelections.org results URL, a certified total to record, a count that looks stale.
---

# Ingesting DOE results

## Overview

The committed `data/*.csv` and `packages/data/*.json` are **derived** from the
real DOE release XMLs by the `sfcount` pipeline. To change an election number,
change the **source** — the real DOE `summary.xml` (fetched into `raw/`) and the
`CERTIFIED_FINALS` constant — then re-run the **whole** pipeline.

Don't hand-edit a derived file (the next `parse` overwrites it). The subtler
trap is a *partial* run that leaves `docs/` and `elections_master.csv` stale
while the rest moves — run every generator below.

## Source vs derived (what you may touch)

| File | Role | Hand-edit? |
|------|------|------------|
| `raw/<el>/<snap>/summary.xml` | real DOE release (gitignored local cache) | no — `sfcount fetch` |
| `data/sf_count_timeline.csv` | committed source of truth | no — `sfcount parse` |
| `data/sf_days_to_90.csv`, other `data/*.csv` | derived | no — `sfcount derive` |
| `data/elections_master.csv` | derived | no — `build_elections_master.py` |
| `packages/data/*.json` | derived, consumed by the charts | no — `build_viz_data.py` |
| `docs/sources.md`, `docs/missing.md` | derived | no — `gen_docs.py` |
| `sfcount/validate.py` → `CERTIFIED_FINALS` | hand-maintained input | **yes** — add the certified total |

## Recipe — run all of it

From the repo root:

1. `uv run sfcount fetch` — pulls real release XMLs into `raw/` (incremental).
   Confirm the new snapshot, e.g. `ls raw/20260602/`.
2. `uv run sfcount parse` — rebuilds `data/sf_count_timeline.csv`. **`git diff`
   it:** expect only the new row(s); if any election *lost* rows, `raw/` was
   incomplete — re-fetch, don't commit a regressed timeline.
3. On certification: add the certified citywide total to `CERTIFIED_FINALS` in
   `sfcount/validate.py` (`"YYYY-MM-DD": total`, comment turnout % + source).
   Certified total = Final Summary Report `ballots3` on the
   `electorGroupId2="Total"` node (= Election Day + Vote-by-Mail `Textbox171`);
   `Textbox32` = registered, `Textbox6` = turnout.
4. `uv run sfcount validate` — must be **0 errors**.
5. `uv run sfcount derive` — regenerate the derived `data/*.csv`.
6. `python3 scripts/build_viz_data.py` — rebake `packages/data/*.json`.
7. `python3 scripts/build_elections_master.py` — rebuild `data/elections_master.csv`.
8. `python3 scripts/gen_docs.py` — rewrite `docs/sources.md` + `docs/missing.md`.
9. `uv run pytest -q && npx vitest run` — both green. (Newly certified an
   election? Repoint any validator test fixture that used that date as its
   "uncertified" example to a synthetic sentinel date.)
10. If the change is visually material, regenerate the README chart images:
    run the preview harness (`pnpm --filter @long-count/preview exec vite`, :4317)
    then `node scripts/shoot_charts.cjs`. (A few-ballot correction is invisible —
    skip it.)
11. Update hardcoded figures in the web article
    `content/research/2026-06-14-the-long-count/index.mdx`; recheck any derived
    sentence (e.g. "X% counted on election night") still rounds the same.
12. Commit `data/`, `packages/data/`, `docs/`, `sfcount/validate.py`; merge to
    `main`; re-pin the web `long-count` dependency to the new `main` SHA +
    `pnpm install`; push to the web research PR. (A docs/master-only follow-up
    needs no web re-pin — the charts read only `packages/data`.)

## Gotchas

- `raw/` is gitignored and often incomplete after a checkout, and `parse`
  rebuilds **every** election from `raw/`, silently dropping any whose files are
  missing — always `fetch` before `parse`.
- Skipping a generator (steps 6–8) leaves its artifact stale: e.g. omitting
  `build_elections_master.py`/`gen_docs.py` left `docs/sources.md`
  ("Certified final") and `elections_master.csv` (`night_pct`) wrong while
  `packages/data` was right.
- `FORCE_FINAL` in `build_viz_data.py` marks an election final before the 32-day
  provisional cutoff (canvass); certification adds it to `CERTIFIED_FINALS` too —
  leaving it in `FORCE_FINAL` is harmless.
- A larger certified final can push a days-to-threshold a day later (65% crossing
  on day 6 not 3) — correct, not a bug.
- DOE publishes on canvass business days, then a final report ~3 weeks out; date
  gaps (404s) are normal, cached as probe-misses.
- Statewide elections: the CA Secretary of State Statement of Vote is the
  ultimate certified source — see the `sov-certified-turnout` skill.
