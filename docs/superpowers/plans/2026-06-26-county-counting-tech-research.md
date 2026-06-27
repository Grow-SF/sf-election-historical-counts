# County Counting-Tech Research Harness — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. Per-jurisdiction research is governed by the `researching-jurisdiction-counting-tech` skill — read it first.

**Goal:** Collect, verify, and integrate election counting-tech adoption (e-pollbooks, ASV, Sign-Scan-Go, vote-center) plus ballot-reporting-speed metrics for ~14 California counties and a few national jurisdictions, into the Long Count dataset and a metric-switchable CountySpeed chart — via a parallel research fan-out that resumes cleanly if agents die.

**Architecture:** A Workflow script fans out one research subagent per jurisdiction (isolated context, parallel, schema-enforced). Each agent follows the `researching-jurisdiction-counting-tech` skill and **writes its own** `data/research/county-tech/<slug>.json`. Resumability is layered: (1) each agent self-skips if its file already exists and validates — so any plain re-run resumes from disk; (2) the Workflow's `resumeFromRunId` caches completed `agent()` calls within a session. The Workflow runtime has NO filesystem access, so persistence and the skip-check live in the *agents*, never in the script. A verification phase adversarially re-checks findings; a merge builds the tidy `county_tech.json`; integration adds a metric selector to the chart and cites every number in `sources.md` through the existing pipeline.

**Tech Stack:** Workflow tool (parallel + schema + resume), the research skill, JSON result files + a Python schema validator, the `build_viz_data.py → gen_docs.py` pipeline, the `long-count` recharts package.

## Global Constraints

- **Record schema = the `researching-jurisdiction-counting-tech` skill's object, verbatim.** Every `value`/`status` carries `source_url` + `confidence`; a missing value is `null` + reason, never a substituted metric/denominator.
- **One metric per series. Never average across metric definitions** (`oneweek_pct` ≠ `electionnight_pct` ≠ `days_to_90`).
- **Result files:** `data/research/county-tech/<slug>.json`, one per jurisdiction, committed (this is hand-curated, source-cited provenance — not deterministically re-fetchable like DOE XML).
- **Never hand-edit derived data** (`packages/data/county_tech.json`, `sources.json`, `docs/sources.md`) — regenerate via the pipeline. (See the `ingesting-doe-results` skill.)
- CA jurisdictions anchor on the one-week spine; national jurisdictions chart on whatever metrics they have, with gaps shaded.
- Workflow concurrency auto-caps at ~10; the ~18-jurisdiction worklist queues the excess.

## File Structure

- `data/research/county-tech/worklist.json` — jurisdictions: `{slug, name, state, hints}` (passed to the Workflow via `args`).
- `data/research/county-tech/<slug>.json` — one verified record per jurisdiction (**agent-written**).
- `scripts/research/validate_county_tech.py` — schema validator (gate; also used by agents' self-skip check).
- `scripts/research/county_tech_workflow.js` — the Workflow fan-out script (run via `Workflow({scriptPath})`).
- `scripts/research/merge_county_tech.py` — merge `<slug>.json` files → `packages/data/county_tech.json` (tidy/long).
- `packages/data/county_tech.json` — tidy dataset consumed by the chart.
- `packages/charts/src/components/CountySpeedChart.tsx` — add a metric selector + national jurisdictions.
- `scripts/build_viz_data.py` — emit a `county_tech` provenance record into `sources.json`.

---

### Task 1: Worklist + schema validator

**Files:**
- Create: `data/research/county-tech/worklist.json`
- Create: `scripts/research/validate_county_tech.py`
- Test: `tests/research/test_validate_county_tech.py`

**Produces:** `validate_record(record) -> list[str]` (errors; empty = valid); `WORKLIST` JSON shape `[{slug,name,state,hints}]`.

- [ ] **Step 1: Write `worklist.json`** (the locked scope)

```json
[
  {"slug": "los-angeles-ca",   "name": "Los Angeles County",  "state": "CA", "hints": "e-pollbooks (KNOWiNK 2020); ASV?"},
  {"slug": "orange-ca",        "name": "Orange County",       "state": "CA", "hints": "e-pollbooks (Tenex 2020, VCA); no ASV"},
  {"slug": "san-diego-ca",     "name": "San Diego County",    "state": "CA", "hints": "e-pollbooks"},
  {"slug": "santa-clara-ca",   "name": "Santa Clara County",  "state": "CA", "hints": "e-pollbooks (VCA)"},
  {"slug": "sacramento-ca",    "name": "Sacramento County",   "state": "CA", "hints": "VCA 2018"},
  {"slug": "san-mateo-ca",     "name": "San Mateo County",    "state": "CA", "hints": "VCA pilot 2018"},
  {"slug": "napa-ca",          "name": "Napa County",         "state": "CA", "hints": "VCA pilot 2018"},
  {"slug": "madera-ca",        "name": "Madera County",       "state": "CA", "hints": "VCA pilot 2018"},
  {"slug": "nevada-ca",        "name": "Nevada County",       "state": "CA", "hints": "VCA pilot 2018"},
  {"slug": "fresno-ca",        "name": "Fresno County",       "state": "CA", "hints": "e-pollbooks 2020"},
  {"slug": "san-luis-obispo-ca","name": "San Luis Obispo County","state": "CA","hints": "e-pollbooks 2026"},
  {"slug": "placer-ca",        "name": "Placer County",       "state": "CA", "hints": "Sign-Scan-Go (AB 626)"},
  {"slug": "riverside-ca",     "name": "Riverside County",    "state": "CA", "hints": "ASV"},
  {"slug": "san-bernardino-ca","name": "San Bernardino County","state": "CA","hints": "ASV"},
  {"slug": "san-francisco-ca", "name": "San Francisco",       "state": "CA", "hints": "CONTROL — no e-pollbook, no ASV"},
  {"slug": "pennsylvania-knowink","name": "Pennsylvania (KNOWiNK counties)","state": "PA","hints": "national vignette — e-pollbooks"},
  {"slug": "wisconsin-badgerbooks","name": "Wisconsin (Badger Books)","state": "WI","hints": "national vignette — e-pollbooks"},
  {"slug": "new-york-epb",     "name": "New York (post-2019 e-pollbooks)","state": "NY","hints": "national vignette"}
]
```

- [ ] **Step 2: Write the failing test**

```python
# tests/research/test_validate_county_tech.py
from scripts.research.validate_county_tech import validate_record

GOOD = {
  "jurisdiction": "Orange County", "state": "CA",
  "tech": [{"type": "asv", "status": "not-adopted", "adopted_year": None,
            "evidence_url": "https://laist.com/x", "confidence": "secondary"}],
  "metrics": [{"metric": "oneweek_pct", "year": 2024, "value": 91.8,
               "denominator": "certified final ballots",
               "source_url": "https://calvoter.org/content/ballot-processing",
               "confidence": "primary"}],
  "notes": ""}

def test_accepts_good_record():
    assert validate_record(GOOD) == []

def test_rejects_metric_without_source():
    bad = {**GOOD, "metrics": [{**GOOD["metrics"][0], "value": 91.8, "source_url": ""}]}
    assert any("source_url" in e for e in validate_record(bad))

def test_rejects_value_without_confidence():
    bad = {**GOOD, "metrics": [{"metric": "oneweek_pct", "year": 2024, "value": 91.8,
                                "source_url": "https://x", "confidence": ""}]}
    assert any("confidence" in e for e in validate_record(bad))

def test_non_null_value_must_not_be_confidence_none():
    bad = {**GOOD, "metrics": [{"metric": "oneweek_pct", "year": 2024, "value": 91.8,
                                "source_url": "https://x", "confidence": "none"}]}
    assert any("confidence" in e and "none" in e for e in validate_record(bad))
```

- [ ] **Step 3: Run it, verify it fails** — `uv run pytest tests/research/test_validate_county_tech.py -q` → FAIL (module missing).

- [ ] **Step 4: Implement the validator**

```python
# scripts/research/validate_county_tech.py
"""Schema gate for one jurisdiction's counting-tech research record."""
TECH_TYPES = {"epollbook", "asv", "sign-scan-go", "vote-center"}
METRICS = {"oneweek_pct", "electionnight_pct", "days_to_90", "days_to_cert"}
CONF = {"primary", "secondary", "estimated", "none"}

def validate_record(r: dict) -> list[str]:
    e = []
    for k in ("jurisdiction", "state", "tech", "metrics"):
        if k not in r:
            e.append(f"missing top-level key: {k}")
    for t in r.get("tech", []):
        if t.get("type") not in TECH_TYPES:
            e.append(f"tech.type invalid: {t.get('type')}")
        if t.get("status") not in {"adopted", "not-adopted", "unknown"}:
            e.append(f"tech.status invalid for {t.get('type')}")
        if not t.get("evidence_url"):
            e.append(f"tech {t.get('type')}: missing evidence_url")
        if t.get("confidence") not in CONF:
            e.append(f"tech {t.get('type')}: bad confidence")
        if t.get("status") == "adopted" and not t.get("adopted_year"):
            e.append(f"tech {t.get('type')}: adopted but no adopted_year")
    for m in r.get("metrics", []):
        if m.get("metric") not in METRICS:
            e.append(f"metric invalid: {m.get('metric')}")
        if m.get("confidence") not in CONF:
            e.append(f"metric {m.get('metric')}: bad confidence")
        has_value = m.get("value") is not None
        if has_value and not m.get("source_url"):
            e.append(f"metric {m.get('metric')} {m.get('year')}: value without source_url")
        if has_value and m.get("confidence") == "none":
            e.append(f"metric {m.get('metric')} {m.get('year')}: value with confidence 'none'")
    return e

if __name__ == "__main__":
    import json, sys
    errs = validate_record(json.load(open(sys.argv[1])))
    print("\n".join(errs) or "OK")
    sys.exit(1 if errs else 0)
```

- [ ] **Step 5: Run, verify pass** — `uv run pytest tests/research/test_validate_county_tech.py -q` → PASS.
- [ ] **Step 6: Commit** — `git add data/research/county-tech/worklist.json scripts/research/validate_county_tech.py tests/research/ && git commit -m "research: county-tech worklist + record validator"`

---

### Task 2: The per-jurisdiction research prompt (the resumable unit)

**Files:** Create `scripts/research/prompt.md` (the template the workflow injects per jurisdiction).

**Interfaces:** Consumes a worklist row `{slug,name,state,hints}`. Produces a written, valid `data/research/county-tech/<slug>.json` AND returns the same record (schema-enforced).

- [ ] **Step 1: Write the prompt template** — this is what makes each agent resumable and self-persisting:

```markdown
You are researching ONE jurisdiction for the Long Count county dataset: **{name}** ({state}). Hints: {hints}.

RESUME CHECK FIRST: if `data/research/county-tech/{slug}.json` already exists and
`uv run python scripts/research/validate_county_tech.py data/research/county-tech/{slug}.json`
prints `OK`, then read that file and return its contents UNCHANGED as your final
message. Do not re-research. (This is what makes the run resumable.)

Otherwise: invoke and follow the `researching-jurisdiction-counting-tech` skill
to build the record. Then WRITE it to `data/research/county-tech/{slug}.json`,
run the validator above until it prints `OK`, and return the record as your
final message.
```

- [ ] **Step 2: Commit** — `git add scripts/research/prompt.md && git commit -m "research: per-jurisdiction prompt (resume-check + self-persist)"`

---

### Task 3: The resumable Workflow fan-out script

**Files:** Create `scripts/research/county_tech_workflow.js`

- [ ] **Step 1: Write the script** (run later via `Workflow({scriptPath: "scripts/research/county_tech_workflow.js", args: <worklist>})`):

```javascript
export const meta = {
  name: 'county-tech-research',
  description: 'Fan out one resumable research agent per jurisdiction for the county counting-tech dataset',
  phases: [{ title: 'Research' }],
}

// RECORD schema mirrors validate_county_tech.py — forces structured returns.
const RECORD = {
  type: 'object',
  required: ['jurisdiction', 'state', 'tech', 'metrics'],
  properties: {
    jurisdiction: { type: 'string' }, state: { type: 'string' },
    tech: { type: 'array', items: { type: 'object',
      required: ['type', 'status', 'evidence_url', 'confidence'] } },
    metrics: { type: 'array', items: { type: 'object',
      required: ['metric', 'year', 'value', 'source_url', 'confidence'] } },
    notes: { type: 'string' },
  },
}

const worklist = args // passed in by the caller (read from worklist.json)
const prompt = (j) => `You are researching ONE jurisdiction for the Long Count county dataset: ${j.name} (${j.state}). Hints: ${j.hints}.
RESUME CHECK FIRST: if data/research/county-tech/${j.slug}.json exists and \`uv run python scripts/research/validate_county_tech.py data/research/county-tech/${j.slug}.json\` prints OK, read it and return its contents unchanged — do not re-research.
Otherwise: invoke and follow the researching-jurisdiction-counting-tech skill, WRITE the record to data/research/county-tech/${j.slug}.json, run the validator until it prints OK, and return the record.`

log(`fanning out ${worklist.length} jurisdictions`)
const results = await parallel(
  worklist.map((j) => () =>
    agent(prompt(j), { label: j.slug, phase: 'Research', schema: RECORD })
      .then((rec) => ({ slug: j.slug, ok: !!rec, rec }))
  )
)
const done = results.filter((r) => r && r.ok).map((r) => r.slug)
const failed = worklist.map((j) => j.slug).filter((s) => !done.includes(s))
log(`done: ${done.length}; failed/skipped: ${failed.join(', ') || 'none'}`)
return { done, failed }
```

- [ ] **Step 2: Commit** — `git add scripts/research/county_tech_workflow.js && git commit -m "research: resumable parallel workflow for county-tech fan-out"`

> **Resumability, three ways:** (a) every agent self-skips when its file already validates → a plain re-run resumes from disk; (b) `Workflow({scriptPath, resumeFromRunId})` returns cached results for completed agents after a crash; (c) the per-jurisdiction files are the durable artifact — even if the whole workflow is abandoned, the merge (Task 7) reads whatever files exist. A dead agent leaves its slot empty and is simply re-dispatched next run.

---

### Task 4: Smoke test — one jurisdiction end to end

- [ ] **Step 1:** Run the workflow for a single-row worklist (e.g. `placer-ca`): `Workflow({scriptPath: "scripts/research/county_tech_workflow.js", args: [{slug:"placer-ca",name:"Placer County",state:"CA",hints:"Sign-Scan-Go (AB 626)"}]})`.
- [ ] **Step 2:** Verify the file + schema — `uv run python scripts/research/validate_county_tech.py data/research/county-tech/placer-ca.json` → `OK`, and confirm it has a `sign-scan-go` tech row with `adopted_year` and a real `evidence_url`.
- [ ] **Step 3:** Re-run the same one-row workflow → confirm the agent **self-skips** (returns instantly, no new research). This proves resumability.
- [ ] **Step 4: Commit** the one file — `git add data/research/county-tech/placer-ca.json && git commit -m "research: placer-ca counting-tech record"`

---

### Task 5: Full fan-out

- [ ] **Step 1:** Run the workflow with the full `worklist.json` as `args`.
- [ ] **Step 2:** Validate every file: `for f in data/research/county-tech/*.json; do uv run python scripts/research/validate_county_tech.py "$f" || echo "FAIL $f"; done`.
- [ ] **Step 3:** For any `failed` slug reported by the workflow, re-run (it resumes — only missing ones re-dispatch). Repeat until all validate.
- [ ] **Step 4: Commit** all records — `git add data/research/county-tech/*.json && git commit -m "research: county-tech records for all worklist jurisdictions"`

---

### Task 6: Verification phase (adversarial)

**Goal:** Catch unsourced/over-confident values before they reach the chart.

- [ ] **Step 1:** Run a second workflow: one agent per record, prompt = "Re-open each `value` in `data/research/county-tech/<slug>.json`, fetch its `source_url`, and confirm the number appears there with the stated metric definition. For any that don't check out, set value `null` + confidence `none` + a `note`; downgrade news-only figures to `secondary`. Re-validate and rewrite the file. Return the list of changes." Schema-enforce a `{slug, changes[]}` return.
- [ ] **Step 2:** Surface any `primary`-confidence hand-read figures to the human partner for spot-reading (per the human-verification-loop).
- [ ] **Step 3: Commit** corrections — `git add data/research/county-tech/*.json && git commit -m "research: adversarial verification pass on county-tech records"`

---

### Task 7: Merge → tidy `county_tech.json`

**Files:** Create `scripts/research/merge_county_tech.py`, `tests/research/test_merge_county_tech.py`; output `packages/data/county_tech.json`.

**Produces:** `packages/data/county_tech.json` = `{metrics:[{jurisdiction,state,tech_summary,metric,year,value,confidence,source_url}], adoptions:[{jurisdiction,tech,adopted_year,...}]}` (long/tidy, chart-ready).

- [ ] **Step 1: Failing test** — assert merge of two sample records yields one long `metrics` row per (jurisdiction,metric,year) and an `adoptions` row per adopted tech. (Write the test with two inline records.)
- [ ] **Step 2: Run → fail.**
- [ ] **Step 3: Implement merge** — read every `data/research/county-tech/*.json`, validate each (skip+warn on invalid), flatten into the tidy shape, sort stably, write `packages/data/county_tech.json`. `log` any jurisdiction dropped for invalidity (no silent truncation).
- [ ] **Step 4: Run → pass.**
- [ ] **Step 5: Commit.**

---

### Task 8: Chart — metric selector + national jurisdictions

**Files:** Modify `packages/charts/src/components/CountySpeedChart.tsx`; modify `packages/data/index.ts` (export `COUNTY_TECH`); add `packages/data/types.ts` type; Test: `CountySpeedChart.test.tsx`.

**Interfaces:** Consumes `COUNTY_TECH` (Task 7 shape). Produces the same `CountySpeed`/`CountySpeedChart` exports, now metric-aware.

- [ ] **Step 1:** Export `COUNTY_TECH` from the data package (import `county_tech.json`, add a `CountyTech` type), mirroring the existing `COUNTY_SPEED` wiring.
- [ ] **Step 2:** Add a metric selector to `CountySpeedChart` — local state `metric ∈ {oneweek_pct, electionnight_pct, days_to_90}`, rendered as chips reusing the `FilterBar` chip styling; the bars plot `COUNTY_TECH.metrics` filtered to the chosen metric, grouped by jurisdiction×year; keep the e-pollbook/ASV tick markers; use `noDataGuides`/blank bars where a jurisdiction lacks the metric/year; flip the y-axis framing for `days_to_90` (lower = better, annotate). National jurisdictions render with a state tag.
- [ ] **Step 3:** Update the test to assert the title renders and that switching metric changes the plotted series (jsdom-safe: assert the selector labels render).
- [ ] **Step 4:** `pnpm -C packages/charts build:css` (confirm no stray utilities), `npx vitest run`, screenshot via the :4317 harness + `shoot_county.cjs` and eyeball each metric. **Commit.**

---

### Task 9: Provenance + docs + ship

- [ ] **Step 1:** In `scripts/build_viz_data.py`, emit a `county-tech` provenance record into `sources.json` (one per source, or one summarizing CalVoter + SoS VCA + the registrar sources), exactly as the `county-speed` record was added.
- [ ] **Step 2:** `python3 scripts/build_viz_data.py && python3 scripts/gen_docs.py`; confirm `docs/sources.md` lists the county-tech sources. (Never hand-edit the generated docs.)
- [ ] **Step 3:** `uv run pytest -q && npx vitest run` → green.
- [ ] **Step 4:** Commit `data/research/`, `packages/data/`, `scripts/`, `docs/`; merge to `main`; re-pin the web `long-count` dep to the new SHA + `pnpm install`; update the article's conclusion/table and push to the web research PR.

---

## Self-Review

- **Spec coverage:** worklist (scope) → T1; per-jurisdiction research (skill) → T2/T3/T5; *all three metrics* → enforced by the skill's metric table + `METRICS` in the validator; *national jurisdictions charted* → worklist rows + T8 state tag; *parallel, isolated, resumable* → T3 (parallel + schema + agent self-skip + resumeFromRunId); verification → T6; integration + sourcing → T7/T8/T9.
- **Resumability is real, not aspirational:** durable state is the per-jurisdiction files (agents write them; the Workflow runtime can't); re-runs skip validated files; `resumeFromRunId` covers mid-run crashes.
- **No hand-edited derived data:** county_tech.json/sources.json/docs all regenerate (T7/T9).
- **Open risk:** `days_to_90` will be sparse (few counties publish per-day totals) and absent for most national jurisdictions — shaded as gaps, never back-filled with a substitute metric.
