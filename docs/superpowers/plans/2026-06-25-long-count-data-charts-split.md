# Long Count — data + charts split Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn `sf-election-count` into a workspace monorepo that ships the data **and** the React charts (defaults styled to match the GrowSF site), delete the standalone `viz/` app, and have the website consume both via a pinned git dependency — eliminating the data/component duplication.

**Architecture:** Three layers. `packages/data` = the JSON the Python pipeline emits (committed) + TS types. `packages/charts` = the React components (extracted from the canonical web copy), styled through a `theme` object + a `charts.css` whose defaults are lifted from the website, plus a Vite dev/preview harness that doubles as the README-screenshot target. The repo root is the npm package `long-count` whose `exports` surface `long-count/data` and `long-count/charts`; the website git-deps it and compiles the chart source via Next `transpilePackages`.

**Tech Stack:** pnpm workspaces, TypeScript, React 18 + recharts (peer deps), Vite (dev/preview harness), Vitest + @testing-library/react (tests), existing Python pipeline (`scripts/build_viz_data.py`), puppeteer-core (`scripts/shoot_charts.js`).

**Source of truth for the components:** the **web** copy at `/Users/sbuss/workspace/web/content/research/2026-06-14-the-long-count/longcount/` (it carries the latest fixes). The `viz/src/components/*` copies are stale duplicates and are discarded, not moved.

**Conventions:** Branch `feat/data-charts-split` in `sf-election-count`; a parallel branch in `web`. Commit after every green step. Run JS commands with pnpm on PATH (`export PATH="/Users/sbuss/.nvm/versions/node/v22.21.1/bin:$PATH"`).

---

## File structure

**`sf-election-count` (becomes the `long-count` package):**

```
package.json                      # CREATE — name "long-count"; exports ./data, ./charts; peerDeps react, recharts
pnpm-workspace.yaml               # CREATE — packages/*
tsconfig.base.json                # CREATE — shared TS config
vitest.config.ts                  # CREATE — jsdom env for component tests
packages/
  data/
    package.json                  # CREATE
    index.ts                      # CREATE — typed re-exports of the JSON
    types.ts                      # CREATE — Election, TurnoutPoint, … (from viz/src/lib/data.ts)
    *.json                        # MOVE   — 8 datasets from viz/src/data/
  charts/
    package.json                  # CREATE
    src/
      index.ts                    # CREATE — public API (LongCount + embeddable wrappers + raw charts)
      theme.tsx                   # CREATE — ChartsTheme, defaultTheme, context, useChartTheme, provider
      charts.css                  # CREATE — .lc-* + scoped chrome classes; defaults from the web styling
      lib/
        categories.ts             # CREATE — KINDS, KIND_DESC, displayKind  (from data.ts)
        filter.ts                 # CREATE — filterElections                (from data.ts)
        format.ts                 # CREATE — formatNumber/Pct/Date, fmt
        fit.ts                    # CREATE — linearFit                       (from data.ts)
        events.ts                 # CREATE — EVENTS, FRANCHISE_EVENTS, yearTicks, yearFrac
        useUrlState.ts            # MOVE   — from web longcount/useUrlState.ts
        context.tsx               # MOVE   — from web longcount/context.tsx (folds theme in)
      components/                 # MOVE+REFACTOR from web longcount/*.tsx
        ui.tsx  NightShareChart.tsx  TurnoutChart.tsx  VbmChart.tsx
        RegistrationChart.tsx  FranchiseFunnelChart.tsx  TrajectoryExplorer.tsx
        FilterBar.tsx  LongCount.tsx
    preview/
      index.html  main.tsx  Gallery.tsx  fonts.css   # CREATE — Vite dev/preview harness
    vite.config.ts                # CREATE
scripts/build_viz_data.py         # MODIFY — OUT path → packages/data/elections.json (+ siblings)
scripts/shoot_charts.js           # MODIFY — SITE_URL default → the harness; titles unchanged
docs/sources.md                   # CREATE — generated from packages/data/sources.json
docs/missing.md                   # CREATE — generated from the ledger + elections_master
viz/                              # DELETE (last)
```

**`web` (the consumer):**

```
package.json                                   # MODIFY — add "long-count" git dep
next.config.{js,ts}                            # MODIFY — transpilePackages: ["long-count"]
app/(...)/globals.css  (or the longcount scope) # MODIFY — map --lc-* → GrowSF tokens (or rely on defaults)
content/research/2026-06-14-the-long-count/index.mdx        # MODIFY — import from long-count/charts; wrap in <LongCount theme>; absorb eras/methods prose
content/research/2026-06-14-the-long-count/longcount/*       # DELETE — components + datasets/
```

---

## Phase 0 — Branch & workspace skeleton

### Task 1: Branch both repos

- [ ] **Step 1: Branch `sf-election-count` off `main`**

```bash
git -C /Users/sbuss/workspace/sf-election-count fetch origin
git -C /Users/sbuss/workspace/sf-election-count checkout -b feat/data-charts-split origin/main
```

- [ ] **Step 2: Move the approved spec onto this branch**

The spec was authored on another branch's working tree. Confirm it is present, then commit it.

```bash
ls /Users/sbuss/workspace/sf-election-count/docs/superpowers/specs/2026-06-25-long-count-data-charts-split-design.md
git -C /Users/sbuss/workspace/sf-election-count add docs/superpowers/specs/2026-06-25-long-count-data-charts-split-design.md docs/superpowers/plans/2026-06-25-long-count-data-charts-split.md
git -C /Users/sbuss/workspace/sf-election-count commit -m "docs: long-count data+charts split — spec and plan"
```

### Task 2: Workspace skeleton

**Files:** Create `pnpm-workspace.yaml`, `package.json`, `tsconfig.base.json`, `vitest.config.ts`.

- [ ] **Step 1: `pnpm-workspace.yaml`**

```yaml
packages:
  - "packages/*"
  - "packages/charts/preview"
```

- [ ] **Step 2: Root `package.json`** (the published surface; `exports` filled in Phase 5)

```json
{
  "name": "long-count",
  "private": false,
  "version": "0.0.0",
  "type": "module",
  "exports": {
    "./data": "./packages/data/index.ts",
    "./charts": "./packages/charts/src/index.ts",
    "./charts.css": "./packages/charts/src/charts.css"
  },
  "peerDependencies": { "react": ">=18", "react-dom": ">=18", "recharts": ">=3" },
  "devDependencies": {
    "typescript": "^5.5.0",
    "vitest": "^2.0.0",
    "jsdom": "^24.0.0",
    "@testing-library/react": "^16.0.0",
    "@testing-library/jest-dom": "^6.4.0",
    "react": "^18.3.0",
    "react-dom": "^18.3.0",
    "recharts": "^3.8.1"
  }
}
```

- [ ] **Step 3: `tsconfig.base.json`**

```json
{
  "compilerOptions": {
    "target": "ES2020", "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext", "moduleResolution": "Bundler",
    "jsx": "react-jsx", "strict": true, "skipLibCheck": true,
    "resolveJsonModule": true, "esModuleInterop": true, "noEmit": true
  }
}
```

- [ ] **Step 4: `vitest.config.ts`**

```ts
import { defineConfig } from "vitest/config";
export default defineConfig({
  test: { environment: "jsdom", globals: true, setupFiles: ["./vitest.setup.ts"] },
});
```

```ts
// vitest.setup.ts
import "@testing-library/jest-dom/vitest";
```

- [ ] **Step 5: Install + commit**

```bash
export PATH="/Users/sbuss/.nvm/versions/node/v22.21.1/bin:$PATH"
cd /Users/sbuss/workspace/sf-election-count && pnpm install
git add package.json pnpm-workspace.yaml tsconfig.base.json vitest.config.ts vitest.setup.ts pnpm-lock.yaml
git commit -m "chore: pnpm workspace skeleton for the long-count package"
```

---

## Phase 1 — `packages/data`

### Task 3: Stand up the data package

**Files:** Create `packages/data/package.json`, `types.ts`, `index.ts`; move the 8 JSON files; test it loads.

- [ ] **Step 1: Move the datasets**

```bash
cd /Users/sbuss/workspace/sf-election-count
mkdir -p packages/data
git mv viz/src/data/elections.json viz/src/data/turnout_history.json \
       viz/src/data/night_floor.json viz/src/data/vbm_history.json \
       viz/src/data/registration_eligible.json viz/src/data/franchise_funnel.json \
       viz/src/data/sources.json viz/src/data/ledger.json packages/data/
```

- [ ] **Step 2: `packages/data/types.ts`** — copy the exported `type`/`interface` declarations from `viz/src/lib/data.ts` (`Threshold`, `Election`, `VbmPoint`, `FloorPoint`, `TurnoutPoint`, `RegEligPoint`, `FunnelPoint`). Reproduce them verbatim from that file (they are the data shapes; no logic).

- [ ] **Step 3: `packages/data/index.ts`**

```ts
import elections from "./elections.json";
import turnoutHistory from "./turnout_history.json";
import nightFloor from "./night_floor.json";
import vbmHistory from "./vbm_history.json";
import registrationEligible from "./registration_eligible.json";
import franchiseFunnel from "./franchise_funnel.json";
import sources from "./sources.json";
import ledger from "./ledger.json";
import type {
  Election, TurnoutPoint, FloorPoint, VbmPoint, RegEligPoint, FunnelPoint,
} from "./types.js";

export * from "./types.js";
export const ELECTIONS = elections as unknown as Election[];
export const TURNOUT_HISTORY = turnoutHistory as TurnoutPoint[];
export const NIGHT_FLOOR = nightFloor as FloorPoint[];
export const VBM_HISTORY = vbmHistory as VbmPoint[];
export const REGISTRATION_ELIGIBLE = registrationEligible as RegEligPoint[];
export const FRANCHISE_FUNNEL = franchiseFunnel as FunnelPoint[];
export const SOURCES = sources as Record<string, unknown>[];
export const LEDGER = ledger as Record<string, unknown>[];
```

- [ ] **Step 4: `packages/data/package.json`**

```json
{ "name": "@long-count/data", "version": "0.0.0", "type": "module", "main": "./index.ts", "types": "./index.ts" }
```

- [ ] **Step 5: Write the failing test** — `packages/data/index.test.ts`

```ts
import { test, expect } from "vitest";
import { ELECTIONS, TURNOUT_HISTORY } from "./index.js";

test("data package loads the election record", () => {
  expect(ELECTIONS.length).toBeGreaterThan(150);
  expect(ELECTIONS.find((e) => e.id === "2024-11-05")).toBeTruthy();
});

test("turnout history reaches back to the 19th century", () => {
  expect(TURNOUT_HISTORY.some((p) => p.date.startsWith("1879"))).toBe(true);
});
```

- [ ] **Step 6: Run it — expect PASS** (the data already exists; this guards the move)

```bash
export PATH="/Users/sbuss/.nvm/versions/node/v22.21.1/bin:$PATH"
cd /Users/sbuss/workspace/sf-election-count && pnpm vitest run packages/data
```

Expected: 2 passed.

- [ ] **Step 7: Commit**

```bash
git add packages/data && git commit -m "feat(data): packages/data — typed datasets moved out of viz"
```

### Task 4: Retarget the Python pipeline

**Files:** Modify `scripts/build_viz_data.py`.

- [ ] **Step 1: Change the output root** — in `scripts/build_viz_data.py`, line ~19, replace:

```python
OUT = ROOT / "viz" / "src" / "data" / "elections.json"
```

with:

```python
OUT = ROOT / "packages" / "data" / "elections.json"
```

Then grep the file for any other `viz/src/data` or `viz" / "src" / "data` output paths and repoint them to `packages/data` the same way.

```bash
grep -n "viz.*src.*data" scripts/build_viz_data.py
```

- [ ] **Step 2: Rebuild and confirm the JSON is byte-stable** (no diff = the move + retarget are faithful)

```bash
cd /Users/sbuss/workspace/sf-election-count
uv run python scripts/build_viz_data.py
git status --porcelain packages/data/
```

Expected: clean (or only intended regenerations). If a dataset is emitted by a different script, repoint that one too (grep `scripts/` for `viz/src/data`).

- [ ] **Step 3: Commit**

```bash
git add scripts/build_viz_data.py && git commit -m "build: emit datasets into packages/data"
```

---

## Phase 2 — `packages/charts` foundation (theme + pure logic)

### Task 5: The theme contract

**Files:** Create `packages/charts/src/theme.tsx`, `packages/charts/package.json`.

- [ ] **Step 1: `packages/charts/package.json`**

```json
{
  "name": "@long-count/charts", "version": "0.0.0", "type": "module",
  "main": "./src/index.ts",
  "dependencies": { "@long-count/data": "workspace:*" },
  "peerDependencies": { "react": ">=18", "recharts": ">=3" }
}
```

- [ ] **Step 2: Write the failing test** — `packages/charts/src/theme.test.tsx`

```tsx
import { test, expect } from "vitest";
import { defaultTheme } from "./theme";

test("default theme carries the GrowSF chart colors", () => {
  expect(defaultTheme.colorsByKind.General).toBe("#0A82B2");
  expect(defaultTheme.colorsByKind.Midterm).toBe("#7E5AA8");
  expect(defaultTheme.colorsByKind.Local).toBe("#01384F");
  expect(defaultTheme.gold).toMatch(/^#|^var\(/);
  expect(defaultTheme.formatPct(74.31)).toBe("74.31%");
});
```

- [ ] **Step 3: Run — expect FAIL** (`Cannot find module './theme'`)

```bash
pnpm vitest run packages/charts/src/theme.test.tsx
```

- [ ] **Step 4: Implement `theme.tsx`** — the default values are the website's current ones (so the unconfigured package matches the site).

```tsx
import { createContext, useContext } from "react";

export type ChartsTheme = {
  colorsByKind: Record<string, string>;
  ink: string; paper: string; faint: string; rule: string; gold: string;
  fontMono: string;
  formatNumber: (n: number) => string;
  formatPct: (n: number) => string;
  formatDate: (iso: string) => string;
};

export const defaultTheme: ChartsTheme = {
  colorsByKind: {
    General: "#0A82B2", Midterm: "#7E5AA8", Primary: "#EBAB5A",
    Local: "#01384F", Special: "#1E7B6A", Recall: "#E36246",
  },
  ink: "var(--lc-ink)", paper: "var(--lc-paper)", faint: "var(--lc-faint)",
  rule: "var(--lc-rule)", gold: "var(--lc-gold)", fontMono: "var(--lc-font-mono)",
  formatNumber: (n) => n.toLocaleString("en-US"),
  formatPct: (n) => `${n}%`,
  formatDate: (iso) => iso,
};

const ThemeContext = createContext<ChartsTheme>(defaultTheme);
export const ChartsThemeProvider = ThemeContext.Provider;
export function useChartTheme(): ChartsTheme { return useContext(ThemeContext); }
```

- [ ] **Step 5: Run — expect PASS.** Commit.

```bash
pnpm vitest run packages/charts/src/theme.test.tsx
git add packages/charts && git commit -m "feat(charts): theme contract with web-matching defaults"
```

### Task 6: `displayKind` + categories (TDD — pure logic, currently untested)

**Files:** Create `packages/charts/src/lib/categories.ts` + `.test.ts`.

- [ ] **Step 1: Failing test** — `packages/charts/src/lib/categories.test.ts`

```ts
import { test, expect } from "vitest";
import { displayKind, KINDS } from "./categories";

test("presidential vs midterm general split by year parity", () => {
  expect(displayKind("General", 1960)).toBe("General");
  expect(displayKind("General", 1962)).toBe("Midterm");
});
test("Municipal renders as Local", () => {
  expect(displayKind("Municipal", 1971)).toBe("Local");
});
test("other kinds pass through", () => {
  expect(displayKind("Primary", 1968)).toBe("Primary");
});
test("KINDS lists the six display categories in order", () => {
  expect([...KINDS]).toEqual(["General","Midterm","Primary","Local","Special","Recall"]);
});
```

- [ ] **Step 2: Run — expect FAIL.**

- [ ] **Step 3: Implement `categories.ts`** (lifted from the current `data.ts`)

```ts
export const KINDS = ["General","Midterm","Primary","Local","Special","Recall"] as const;

export function displayKind(kind: string, year: number): string {
  if (kind === "Municipal") return "Local";
  return kind === "General" && year % 4 !== 0 ? "Midterm" : kind;
}

export const KIND_DESC: Record<string, string> = {
  General: "Presidential general election — the November ballot held every fourth year.",
  Midterm: "Midterm general election — the November ballot in the even years between presidential elections.",
  Primary: "Primary election — usually June, narrowing the field before the November general.",
  Local: "Local election — mayor, supervisors, and city measures, usually in odd years.",
  Special: "Special election — called off the regular calendar for a single measure, recall, or vacancy.",
  Recall: "Recall election — a vote on whether to remove an elected official before their term ends.",
};
```

- [ ] **Step 4: Run — expect PASS. Commit.**

```bash
pnpm vitest run packages/charts/src/lib/categories.test.ts
git add packages/charts/src/lib/categories.ts packages/charts/src/lib/categories.test.ts
git commit -m "feat(charts): categories + displayKind (now under test)"
```

### Task 7: `filterElections` (TDD)

**Files:** Create `packages/charts/src/lib/filter.ts` + `.test.ts`.

- [ ] **Step 1: Failing test**

```ts
import { test, expect } from "vitest";
import { filterElections } from "./filter";
const E = (id: string, kind: string, year: number) =>
  ({ id, kind, year } as any);

test("filters by display category and year window", () => {
  const all = [E("1962-11-06","General",1962), E("1960-11-08","General",1960), E("1971-11-02","Municipal",1971)];
  const got = filterElections(all, { kinds: new Set(["Midterm"]), from: 1900, to: 2000 });
  expect(got.map((e) => e.id)).toEqual(["1962-11-06"]);
});
```

- [ ] **Step 2: Run — expect FAIL.**

- [ ] **Step 3: Implement `filter.ts`** (note: takes `elections` as an argument now, since the data is imported by the caller)

```ts
import { displayKind } from "./categories";
export type Filters = { kinds: Set<string>; from: number; to: number };
export function filterElections<T extends { kind: string; year: number }>(
  elections: T[], f: Filters,
): T[] {
  return elections.filter(
    (e) => f.kinds.has(displayKind(e.kind, e.year)) && e.year >= f.from && e.year <= f.to,
  );
}
```

- [ ] **Step 4: Run — expect PASS. Commit** (`git add … && git commit -m "feat(charts): filterElections under test"`).

### Task 8: formatters + `linearFit` + events helpers

**Files:** Create `lib/format.ts` (+test), `lib/fit.ts` (+test), `lib/events.ts`.

- [ ] **Step 1: `lib/format.test.ts` (failing)**

```ts
import { test, expect } from "vitest";
import { fmt } from "./format";
test("fmt groups thousands", () => { expect(fmt(271439)).toBe("271,439"); });
```

- [ ] **Step 2: `lib/format.ts`**

```ts
export const fmt = (n: number) => n.toLocaleString("en-US");
export const formatNumber = fmt;
export const formatPct = (n: number) => `${n}%`;
export const formatDate = (iso: string) => iso;
```

- [ ] **Step 3: `lib/fit.test.ts` (failing)** — a known-slope line:

```ts
import { test, expect } from "vitest";
import { linearFit } from "./fit";
test("recovers a perfect linear slope", () => {
  const fit = linearFit([[0,0],[1,2],[2,4]]);
  expect(fit?.slope).toBeCloseTo(2); expect(fit?.r2).toBeCloseTo(1);
});
```

- [ ] **Step 4: `lib/fit.ts`** — copy the `linearFit` body verbatim from the current `data.ts` (lines defining `linearFit` and the `Fit` type).

- [ ] **Step 5: `lib/events.ts`** — copy `EVENTS`, `FRANCHISE_EVENTS`, `yearTicks`, `yearFrac` verbatim from the current `data.ts`.

- [ ] **Step 6: Run all `lib` tests — expect PASS. Commit.**

```bash
pnpm vitest run packages/charts/src/lib
git add packages/charts/src/lib && git commit -m "feat(charts): format, fit, events helpers (tested)"
```

### Task 9: `charts.css` — chrome styling whose defaults match the website

**Files:** Create `packages/charts/src/charts.css`.

- [ ] **Step 1: Extract the chart chrome styles.** Open the website's CSS (`web/.../app` globals + the `.longcount` scope) and copy the rules that style the charts: the `--color-*` variables, the `smallcaps`, `stat-figure`, `rangepair`, and `ChartFrame` framing. Re-author them under an `.lc-root` scope and behind `--lc-*` variables with the **current GrowSF values as the fallbacks**, e.g.:

```css
.lc-root {
  --lc-ink: #1a1a1a; --lc-paper: #faf7f0; --lc-faint: #8a8378;
  --lc-rule: #e5ded0; --lc-gold: #c8a24a;
  --lc-font-mono: ui-monospace, "SFMono-Regular", monospace;
  --lc-font-display: Georgia, "Times New Roman", serif;
  color: var(--lc-ink); font-family: var(--lc-font-display);
}
.lc-root .smallcaps { text-transform: uppercase; letter-spacing: .08em; font-size: .75rem; }
.lc-root .stat-figure { font-family: var(--lc-font-mono); font-variant-numeric: tabular-nums; }
/* …frame, tooltip, legend rules copied from the web styling, all reading --lc-* … */
```

> Replace the placeholder hex/font values above with the **exact** values read out of the website's `:root`/`.longcount` CSS so the default IS the site. Scoping under `.lc-root` (the class the `<LongCount>` provider renders) prevents collision with the consumer's global `smallcaps`/`stat-figure`.

- [ ] **Step 2: Commit** (`git add packages/charts/src/charts.css && git commit -m "feat(charts): charts.css — web-matching chrome defaults under .lc-root"`).

---

## Phase 3 — `packages/charts` components

### Task 10: Move shared client modules

**Files:** `git mv` from web → `packages/charts/src/lib/`.

- [ ] **Step 1: Move `useUrlState` and `context`** from the web copy (the canonical one) into the package.

```bash
cp /Users/sbuss/workspace/web/content/research/2026-06-14-the-long-count/longcount/useUrlState.ts \
   packages/charts/src/lib/useUrlState.ts
cp /Users/sbuss/workspace/web/content/research/2026-06-14-the-long-count/longcount/context.tsx \
   packages/charts/src/lib/context.tsx
```

- [ ] **Step 2: Repoint their imports** — in both files, change `from "./data"` to the new split modules (`./categories`, `./filter`, `../theme`, `@long-count/data`). `context.tsx` must also carry `theme` on its value (so one provider supplies state + theme). Update `LongCountValue` to add `theme: ChartsTheme` and have `useUrlState`'s `KINDS`/`YEAR_*` come from `./categories` + `@long-count/data`.

- [ ] **Step 3: Commit** (`git add packages/charts/src/lib && git commit -m "feat(charts): move url-state + context into the package"`).

### Task 11: The component theme-refactor — rules + worked example

Every chart component currently pulls colors/classes from the web's `data.ts`/CSS. Move each into `packages/charts/src/components/` and apply these **transformation rules** uniformly:

| In the component… | becomes… |
|---|---|
| `import { … } from "./data"` | split: data from `@long-count/data`, logic from `../lib/*`, colors from `useChartTheme()` |
| `KIND_COLOR[k]` | `theme.colorsByKind[k]` (add `const theme = useChartTheme()` at the top of the component) |
| `KIND_DESC` | import from `../lib/categories` |
| `var(--color-ink/paper/faint/rule/gold)` literals passed to recharts | `theme.ink` / `theme.paper` / `theme.faint` / `theme.rule` / `theme.gold` |
| `var(--font-mono)` | `theme.fontMono` |
| `fmt(...)` | `theme.formatNumber(...)` (or keep `fmt` import for non-render uses) |
| the outer wrapper `className` | ensure it sits inside the `.lc-root` the provider renders (no change needed inside `ChartFrame`) |
| class names `smallcaps`, `stat-figure`, etc. | **unchanged** — `charts.css` defines them scoped under `.lc-root` |

- [ ] **Step 1: Move `ui.tsx`** (`ChartFrame`, `PointTooltip`, `eventLines`, `useGraceHover`, `DualRange`, `Section`, `FitBadge`) and apply the rules. `eventLines` takes `stroke` from `theme.gold`; `ChartFrame` is unchanged except it should not hard-code colors.

- [ ] **Step 2: Smoke test for `ui.tsx`** — `packages/charts/src/components/ui.test.tsx`

```tsx
import { test, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { ChartFrame } from "./ui";
test("ChartFrame renders its title", () => {
  render(<ChartFrame title="Turnout of registered voters">x</ChartFrame>);
  expect(screen.getByText("Turnout of registered voters")).toBeInTheDocument();
});
```

Run: `pnpm vitest run packages/charts/src/components/ui.test.tsx` → PASS. Commit.

- [ ] **Step 3: Worked example — `TurnoutChart.tsx`.** Move it, then apply the rules. The diff is mechanical; the key edits:

```tsx
// top of the component body:
const theme = useChartTheme();
// SERIES build + render: KIND_COLOR[k] → theme.colorsByKind[k]
// <Tooltip> label color: style={{ color: theme.colorsByKind[p.kind] }}
// import { TURNOUT_HISTORY } from "@long-count/data";
// import { KINDS, displayKind } from "../lib/categories";
// import { ChartFrame, eventLines } from "./ui";
```

- [ ] **Step 4: Smoke test — `TurnoutChart`** renders a known legend label:

```tsx
import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import TurnoutChart from "./TurnoutChart";
test("turnout chart shows the Midterm series in its legend", () => {
  render(<TurnoutChart from={1900} to={2026} kinds={new Set(["General","Midterm"])} />);
  expect(screen.getByText("Midterm")).toBeInTheDocument();
});
```

Run → PASS. Commit.

- [ ] **Step 5: Apply the same rules to the remaining components, one commit each, each with a smoke test asserting a known string renders.** For each, the table above is the complete recipe; the per-component specifics are:

  - **`NightShareChart.tsx`** — uses `KIND_COLOR[displayKind(...)]` for dots/tooltip, `var(--color-gold)` rings, `eventLines`. Smoke: renders "How much of the vote was counted on election night".
  - **`VbmChart.tsx`** — single series + `eventLines`. Smoke: renders "Vote-by-mail share of ballots cast".
  - **`RegistrationChart.tsx`** — `EVENTS` + `FRANCHISE_EVENTS` lines, single line series. Smoke: renders "Registration among eligible citizens".
  - **`FranchiseFunnelChart.tsx`** — band colors are local `BANDS` (keep as-is or fold into theme later — out of scope), `EVENTS`+`FRANCHISE_EVENTS`. Smoke: renders "Who could vote".
  - **`TrajectoryExplorer.tsx`** — custom SVG; colors from `theme`. (Currently perf-hidden in the embed; keep it exported but unused.) Smoke: renders without throwing.
  - **`FilterBar.tsx`** — chips colored by `theme.colorsByKind[k]`, `KIND_DESC` tooltips. Smoke: renders the six chip labels.

  Run `pnpm vitest run packages/charts/src/components` after each; all green.

### Task 12: The `LongCount` provider + public API

**Files:** Move `LongCount.tsx`; create `packages/charts/src/index.ts`.

- [ ] **Step 1: Move `LongCount.tsx`** and fold the theme into the provider: it accepts `theme?: ChartsTheme` (default `defaultTheme`), renders `<div className="lc-root">` wrapping `<ChartsThemeProvider value={theme}><LongCountProvider value={{state, update, elections, theme}}>…`. Keep the embeddable wrappers (`NightShare`, `Vbm`, `Turnout`, `Registration`, `FranchiseFunnel`, `Trajectory`, `CountingMethods`).

- [ ] **Step 2: `packages/charts/src/index.ts`**

```ts
import "./charts.css";
export { LongCount, NightShare, Vbm, Turnout, Registration, FranchiseFunnel, Trajectory, CountingMethods } from "./components/LongCount";
export { defaultTheme } from "./theme";
export type { ChartsTheme } from "./theme";
export { default as NightShareChart } from "./components/NightShareChart";
export { default as TurnoutChart } from "./components/TurnoutChart";
// …re-export the remaining raw charts for standalone use…
```

- [ ] **Step 3: Typecheck the package — expect clean.**

```bash
cd /Users/sbuss/workspace/sf-election-count && pnpm exec tsc -p packages/charts --noEmit
```

- [ ] **Step 4: Run the full chart test suite — all green. Commit.**

```bash
pnpm vitest run packages/charts
git add packages/charts && git commit -m "feat(charts): LongCount provider + public API"
```

---

## Phase 4 — Dev/preview harness + README images

### Task 13: Vite preview harness

**Files:** Create `packages/charts/preview/{index.html,main.tsx,Gallery.tsx,fonts.css}`, `packages/charts/vite.config.ts`.

- [ ] **Step 1: `vite.config.ts`** (React plugin; resolves `@long-count/*` via the workspace).

```ts
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
export default defineConfig({ plugins: [react()], server: { port: 4317 } });
```

- [ ] **Step 2: `preview/fonts.css`** — `@font-face` (or a `<link>` in `index.html`) loading the **same fonts the website uses**, from the same source the site loads them (Google Fonts / the web's font files). This is what makes screenshots match; do not rely on system fallbacks.

- [ ] **Step 3: `preview/Gallery.tsx`** — render each chart inside one `<LongCount>` so the default theme + `.lc-root` apply, mirroring the website layout width.

```tsx
import { LongCount, NightShare, Vbm, Turnout, Registration, FranchiseFunnel } from "../src";
export default function Gallery() {
  return (
    <LongCount>
      <div style={{ maxWidth: 960, margin: "0 auto" }}>
        <NightShare /><Vbm /><Turnout /><Registration /><FranchiseFunnel />
      </div>
    </LongCount>
  );
}
```

- [ ] **Step 4: `preview/main.tsx` + `index.html`** — standard Vite React entry; `index.html` links `fonts.css`.

- [ ] **Step 5: Run it and eyeball parity with the live site.**

```bash
cd /Users/sbuss/workspace/sf-election-count && pnpm --filter ./packages/charts/preview exec vite
```

Open `http://localhost:4317`. Confirm the charts look like the GrowSF site (colors, fonts, frame, tooltips). Fix any `--lc-*`/font gaps in `charts.css`/`fonts.css` until they match. Commit.

```bash
git add packages/charts/preview packages/charts/vite.config.ts
git commit -m "feat(charts): vite dev/preview harness rendering the default-themed charts"
```

### Task 14: Retarget the screenshot script + regenerate README images

**Files:** Modify `scripts/shoot_charts.js`.

- [ ] **Step 1: Point the shoot script at the harness** — in `scripts/shoot_charts.js`, change the default URL (line ~8):

```js
const URL = process.env.SITE_URL || "http://localhost:4317/";
```

The `TARGETS` map keys on `<h3>` titles and is unchanged. (Confirm the harness renders each chart's `<h3>` — `ChartFrame` does.)

- [ ] **Step 2: Regenerate the four images against the running harness.**

```bash
cd /Users/sbuss/workspace/sf-election-count
pnpm --filter ./packages/charts/preview exec vite &   # serve the harness
export PATH="/Users/sbuss/.nvm/versions/node/v22.21.1/bin:$PATH"
NODE_PATH=viz/node_modules SITE_URL=http://localhost:4317/ node scripts/shoot_charts.js
```

> `puppeteer-core` currently resolves from `viz/node_modules`. Before deleting `viz/` (Task 20), move puppeteer-core into the root devDeps and drop `NODE_PATH`.

- [ ] **Step 3: Visually verify** the regenerated `docs/img/{turnout,night-share,vote-by-mail,franchise-funnel}.png` match the prior committed versions (same look as the live site). Commit if they are faithful.

```bash
git add docs/img scripts/shoot_charts.js
git commit -m "build: shoot README charts from the package preview harness"
```

---

## Phase 5 — Root exports & local consumption check

### Task 15: Verify the package resolves as `long-count/data` + `long-count/charts`

**Files:** confirm root `package.json` `exports` (Task 2 Step 2).

- [ ] **Step 1: Local resolution smoke test** — `packages/_resolve.test.ts` at repo root importing through the public subpaths:

```ts
import { test, expect } from "vitest";
test("public subpaths resolve", async () => {
  const data = await import("long-count/data");
  const charts = await import("long-count/charts");
  expect(Array.isArray((data as any).ELECTIONS)).toBe(true);
  expect(typeof (charts as any).LongCount).toBe("function");
});
```

Add a tsconfig/vitest path alias `"long-count/*": ["./packages/*"]` mirroring the `exports` map so the test resolves locally.

- [ ] **Step 2: Run — expect PASS. Commit.**

```bash
pnpm vitest run packages/_resolve.test.ts
git add . && git commit -m "test: long-count/data + long-count/charts resolve via exports"
```

---

## Phase 6 — Website cutover (web repo)

### Task 16: Add the dependency + transpile

**Files:** Modify `web/package.json`, `web/next.config.*`.

- [ ] **Step 1: Branch web.**

```bash
git -C /Users/sbuss/workspace/web checkout -b feat/long-count-import origin/main 2>/dev/null || git -C /Users/sbuss/workspace/web checkout -b feat/long-count-import
```

- [ ] **Step 2: Add the git dependency** to `web/package.json` (pin to the `sf-election-count` branch commit for now; switch to a tag once merged):

```json
"long-count": "github:Grow-SF/sf-election-count#feat/data-charts-split"
```

- [ ] **Step 3: Add transpile** to `next.config`:

```js
transpilePackages: ["long-count"],
```

- [ ] **Step 4: Install.**

```bash
export PATH="/Users/sbuss/.nvm/versions/node/v22.21.1/bin:$PATH"
cd /Users/sbuss/workspace/web && pnpm install
```

Commit.

### Task 17: Swap the imports + theme provider

**Files:** Modify `content/research/2026-06-14-the-long-count/index.mdx` and the web CSS.

- [ ] **Step 1: Replace the MDX import** — change

```mdx
import LongCount, { NightShare, Vbm, Turnout, … } from "./longcount/LongCount";
```

to

```mdx
import { LongCount, NightShare, Vbm, Turnout, Registration, FranchiseFunnel, Trajectory, CountingMethods } from "long-count/charts";
```

- [ ] **Step 2: Pass the GrowSF theme + map the vars.** Either pass `<LongCount theme={growsfPalette}>` (build `growsfPalette` from the site's tokens) **or** add one CSS block mapping `--lc-*` to the existing GrowSF tokens under `.lc-root`:

```css
.lc-root { --lc-ink: var(--color-ink); --lc-paper: var(--color-paper);
  --lc-faint: var(--color-faint); --lc-rule: var(--color-rule);
  --lc-gold: var(--color-gold); --lc-font-mono: var(--font-mono);
  --lc-font-display: var(--font-display); }
```

(The defaults already match, so this is belt-and-suspenders / future-proofing.)

- [ ] **Step 3: Build the web page and confirm it renders.**

```bash
cd /Users/sbuss/workspace/web && pnpm build 2>&1 | tail -20
```

Expected: the research route builds; charts present. Commit.

### Task 18: Delete the web duplication + verify parity

**Files:** Delete `content/research/2026-06-14-the-long-count/longcount/`.

- [ ] **Step 1: Visual parity check first** — with `pnpm dev`, screenshot the charts on the research page; compare against the pre-cutover look (they must be identical, since the package was extracted from these very components).

- [ ] **Step 2: Delete the old components + datasets.**

```bash
cd /Users/sbuss/workspace/web
git rm -r content/research/2026-06-14-the-long-count/longcount
```

- [ ] **Step 3: Rebuild — expect clean** (no dangling imports). Fix any stragglers (e.g., `index.mdx` still importing from `./longcount`).

```bash
pnpm build 2>&1 | tail -20
```

- [ ] **Step 4: Commit.**

```bash
git add -A content/research/2026-06-14-the-long-count
git commit -m "the-long-count: consume charts from long-count package; drop duplicated longcount/"
```

---

## Phase 7 — Prose & docs migration

### Task 19: Migrate prose; generate sources/missing docs

- [ ] **Step 1: Audit the viz prose for anything not already in `index.mdx`.**

```bash
grep -rn "" /Users/sbuss/workspace/sf-election-count/viz/src/app/eras/page.tsx \
            /Users/sbuss/workspace/sf-election-count/viz/src/app/methods/page.tsx | wc -l
```

Read `viz/src/app/{eras,methods}/page.tsx` and diff their narrative against `web/.../index.mdx`. Fold any unique paragraphs into the web essay (new sections or prose). Commit on the web branch.

- [ ] **Step 2: Generate `docs/sources.md`** in the data repo from `packages/data/sources.json` — a script `scripts/gen_docs.py` (or extend an existing one) that writes a markdown table of every election → citation. Run it; commit `docs/sources.md` + the generator.

- [ ] **Step 3: Generate `docs/missing.md`** from `packages/data/ledger.json` + `data/elections_master.csv` `recovered=no` rows (the README "help wanted" section is the template). Run it; commit `docs/missing.md` + the generator.

- [ ] **Step 4: Link them** from `README.md` (replace the dead `/sources` `/missing` site links with the new docs).

---

## Phase 8 — Delete viz + final verification

### Task 20: Delete the standalone app

- [ ] **Step 1: Move `puppeteer-core` to root devDeps** (it lived in `viz/node_modules`); drop `NODE_PATH=viz/node_modules` from any docs/commands.

```bash
cd /Users/sbuss/workspace/sf-election-count && pnpm add -D -w puppeteer-core
```

- [ ] **Step 2: Confirm nothing outside `viz/` references it.**

```bash
grep -rn "viz/" --include="*.py" --include="*.js" --include="*.ts" --include="*.json" \
  scripts/ packages/ README.md | grep -v node_modules
```

Expected: no references (the build pipeline now writes `packages/data`; the shoot script targets the harness).

- [ ] **Step 3: Delete it.**

```bash
git rm -r viz
git commit -m "chore: remove standalone viz app — charts now ship from packages/charts"
```

### Task 21: Final verification (both repos)

- [ ] **Step 1: Data repo green.**

```bash
cd /Users/sbuss/workspace/sf-election-count
pnpm vitest run && pnpm exec tsc -p packages/charts --noEmit
uv run python scripts/build_viz_data.py && git status --porcelain packages/data   # clean
```

- [ ] **Step 2: README images regenerate from the harness** (Task 14 commands) and match the live look.

- [ ] **Step 3: Web repo green.** `cd /Users/sbuss/workspace/web && pnpm build`. Visual: research page charts identical to pre-migration.

- [ ] **Step 4: Open PRs.** One in `sf-election-count` (the split), one in `web` (the cutover; its `long-count` dep pins the sf-election-count merge commit once that PR lands).

---

## Self-review

- **Spec coverage:** data package (T3–4) ✓; charts co-located (T5–12) ✓; git-dep + transpile (T16) ✓; theme/CSS contract with web-matching defaults (T5, T9, T17) ✓; fonts in the harness (T13) ✓; dev/preview harness + README images self-contained (T13–14) ✓; `/sources` `/missing` → docs (T19) ✓; prose → website (T19) ✓; delete duplication + viz (T18, T20) ✓; data flow CSV→Python→packages/data→git-dep (T4, T16) ✓.
- **Open risk carried into execution:** the FranchiseFunnel `BANDS` colors are left local (noted in T11) rather than themed — acceptable, behavior-preserving; theme them later if reuse needs it.
- **Type consistency:** `ChartsTheme`, `defaultTheme`, `useChartTheme`, `displayKind`, `filterElections(elections, filters)` signatures are defined once (T5–7) and used consistently downstream.
- **Placeholder note:** Task 9 and Task 17 deliberately say "read the exact values out of the website CSS" rather than inventing hex codes — that is an instruction to copy real values, not a TODO; the engineer must open the web CSS and transcribe them.
