# packages/data

The committed JSON datasets the charts consume. **Every file here except one
is GENERATED; never hand-edit a generated file** (fix the inputs, rerun the
generator, commit both). Types live in `types.ts`; `index.ts` is the public
entry (`sources.json` and `ledger.json` are typed inline there, not in
`types.ts`).

| file | generator | inputs |
|---|---|---|
| `elections.json` | `scripts/build_viz_data.py` | `data/*.csv` |
| `turnout_history.json` | `scripts/build_viz_data.py` | `data/*.csv` |
| `night_floor.json` | `scripts/build_viz_data.py` | computed live from the turnout/VBM CSVs (NOT from `data/sf_night_floor_1964_2026.csv`) |
| `vbm_history.json` | `scripts/build_viz_data.py` | `data/*.csv` |
| `registration_eligible.json` | `scripts/build_viz_data.py` | `data/*.csv` |
| `franchise_funnel.json` | `scripts/build_viz_data.py` | `data/*.csv` |
| `sources.json` | `scripts/build_viz_data.py` | the other series |
| `ledger.json` | `scripts/build_viz_data.py` | `docs/analysis/public-search-log.md` |
| `county_night.json` | `scripts/build_county_night.py` | `data/research/election-night/*.json` + `elections.json` |
| `county_tech.json` | `scripts/research/merge_county_tech.py` | `data/research/county-tech/*.json` |
| `county_speed.json` | **none: hand-authored** | California Voter Foundation "Ballot Processing" (see `docs/sources.md`) |

Sync convention: after changing any input, rerun the generator and commit the
regenerated JSON in the same commit. `county_night.json` has an explicit
in-sync check (`git diff -I '"generated"'` after a rebuild); the full recipe
for SF data changes is the `ingesting-doe-results` skill, and for the county
research dataset it is `docs/research/RUNBOOK.md` section 3.
