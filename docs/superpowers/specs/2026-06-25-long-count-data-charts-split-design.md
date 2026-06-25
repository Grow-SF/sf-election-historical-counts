# The Long Count — data + charts in the repo, prose in the website

**Status:** Draft for review · **Date:** 2026-06-25

## Goal

Split the Long Count into clean layers so the duplication disappears and the data
repo becomes a first-class, reusable resource:

- **`sf-election-count`** (public data repo) → the data, the Python tooling that
  grows it, the docs (how to use / how to grow), a committed copy of the built
  data, **and** a reusable React charts package.
- **The website** (the GrowSF web repo) → all the prose, importing the data +
  charts straight from the data repo and rendering them around the narrative.

The standalone `viz/` Next app is removed. "Import the repo and render the charts"
becomes literal.

## Background — the duplication today

Data flows `data/*.csv` → `scripts/build_viz_data.py` → `viz/src/data/*.json`, and
that JSON is then **hand-copied** into the web embed's `datasets/`. The chart
components also exist twice — `viz/src/components/*` and an almost-identical
`web/…/longcount/*` — and the `viz/` app carries its own pages (`/`, `/methods`,
`/eras`, `/missing`, `/sources`). Two copies of everything drift, and every data
update is a manual copy. This split removes both copies.

## Decisions (resolved in brainstorming)

| Question | Decision |
|---|---|
| What does the website import? | **Data + chart components** — charts are a reusable package, not buried in the site |
| Where do the charts live? | **Co-located with the data**, as a package inside the data-repo monorepo |
| How does the site consume it? | **Pinned git dependency + Next `transpilePackages`** — no npm publish; the site compiles the chart source |
| `/sources` and `/missing` | **Data-repo docs** (how-to-use / how-to-grow), generated from the same JSON — not website pages |
| Chart styling | **Theme object (context) + prefixed `lc-*` CSS backed by `--lc-*` variables**, shipped with defaults |

## Target architecture

### Data repo → a workspace monorepo (`sf-election-count`)

```
sf-election-count/             # the npm package "long-count" (root package.json + exports)
  packages/
    data/      # built JSON (committed "copy of the data") + index.ts (types + re-exports)
    charts/    # the React chart components; import ../data; react/recharts are peers
  data/        # the source CSVs (unchanged)
  scripts/     # the Python pipeline + recovery tooling (unchanged)
  sfcount/     # Python package (unchanged)
  docs/        # runbooks, analysis, + generated /sources & /missing docs
  package.json # name "long-count"; exports { "./data", "./charts" }; peerDeps react, recharts
  # viz/  ← DELETED
```

- **`packages/data`** — the eight JSON datasets (`elections`, `turnout_history`,
  `night_floor`, `vbm_history`, `registration_eligible`, `franchise_funnel`,
  `sources`, `ledger`), emitted here by `build_viz_data.py` and committed. A small
  `index.ts` re-exports them with the existing TS types (`Election`,
  `TurnoutPoint`, …). This is the "copy of the data" and the typed import surface.
- **`packages/charts`** — the canonical chart components (today's duplicated set:
  `NightShareChart`, `TurnoutChart`, `VbmChart`, `RegistrationChart`,
  `FranchiseFunnelChart`, `TrajectoryExplorer`, `FilterBar`, the `LongCount`
  provider + per-chart embeddable wrappers, and the `ui.tsx` primitives), plus the
  chart-side logic from `data.ts` (`filterElections`, `displayKind`, `KINDS`,
  `EVENTS`, `linearFit`, formatters). Imports `../data`. `react`/`recharts` are
  **peer** deps (the consumer provides them). Also ships a small **dev/preview
  harness** (a lightweight Vite gallery page, or Storybook) that renders each chart
  with the default theme + `packages/data` — this is the charts' development
  environment *and* the target `shoot_charts.js` screenshots for the README (see
  Build, release & images). The "ship default styles" decision is what lets a bare
  harness render faithfully.
- **Root `package.json`** — package name `long-count`, with an `exports` map:
  `"./data" → packages/data`, `"./charts" → packages/charts`. A consumer that
  git-deps the repo imports `long-count/data` and `long-count/charts`. Modeling the
  repo root as the package (with subpath exports) sidesteps the "git dep can't
  target a sub-folder" problem; the `packages/` layout (a workspace for local dev
  + tests) is internal.

### Website → the consumer (web repo)

- Adds a **pinned git dependency** on `Grow-SF/sf-election-count` and one
  **`transpilePackages: ["long-count"]`** entry so Next compiles the chart source.
- **Deletes** its duplicated `longcount/` components and `datasets/` JSON copies.
  The MDX imports `{ LongCount, NightShare, Turnout, … }` from `long-count/charts`
  and wraps them in prose, exactly as it does today — only the import path changes.
- Holds **all prose**: today's `index.mdx` plus the narrative currently in the
  viz's `/`, `/eras`, and `/methods` pages.

### Data flow

```
data/*.csv  →  scripts/build_viz_data.py  →  packages/data/*.json  (committed)
                                                     │  (pinned git dep)
                                                     ▼
                              website imports long-count/data + long-count/charts
```

One source of truth, zero hand-copied JSON. Recover an election → rebuild →
commit → tag → `npm update long-count` in the site → deploy.

## The charts package: API & styling contract

Charts are a special case: the SVG internals take colors as **values/props**, not
CSS, so the cascade can't reach them. The contract is therefore two layers — a JS
theme for the SVG, prefixed CSS for the HTML chrome — each shipping defaults so the
package renders correctly unconfigured (including in a standalone preview).

**1. Theme (JS, via context, with a baked-in default):**

```ts
type ChartsTheme = {
  colorsByKind: Record<string, string>; // categorical series colors (General, Midterm, …)
  ink: string; paper: string; faint: string; rule: string; gold: string; // semantic
  fontMono: string;
  formatNumber: (n: number) => string;  // formatting hooks
  formatPct: (n: number) => string;
  formatDate: (iso: string) => string;
};
```

The `<LongCount theme={…}>` provider (the *same* wrapper that owns the filter state,
below — one provider carries both) supplies this. **The default theme and the chrome
CSS are lifted straight from the website's current chart styling**, so the
unconfigured package looks exactly like the live GrowSF site. That's the point: the
website renders identically to today (it passes the same values, or just relies on
the matching defaults), and the dev harness + **README images inherit the web look
for free**. Components read colors from the theme and hand them to recharts as
`stroke`/`fill`.

**2. Chrome CSS (prefixed classes backed by variables):**

A shipped `charts.css` defines `.lc-frame`, `.lc-smallcaps`, `.lc-figure`,
`.lc-tooltip`, `.lc-legend`, … with values from `--lc-ink`, `--lc-paper`,
`--lc-font-display`, `--lc-font-mono`, … — and its **defaults replicate the website's
current chart chrome** (frame border, tooltip box, the smallcaps / stat-figure
treatment, spacing). The consumer imports it once and re-themes by setting the
`--lc-*` variables, or overrides the prefixed classes outright for full control.

**Fonts are part of the contract.** `--lc-font-display` / `--lc-font-mono` name the
families the website uses; for the dev harness — and therefore the README
screenshots — to match the live site, the harness must load those same fonts.
Whether the package bundles the font files or the harness pulls them from the same
source the website uses is a sub-decision, likely the latter to avoid redistributing
licensed font files.

**The website then does two trivial things:** wrap the embeds in
`<LongCount theme={growsfPalette}>`, and map `--lc-*` to its existing tokens
in one CSS block (or rely on the defaults). Today's `smallcaps` / `--color-ink`
usage becomes the package's **default**, not a hard dependency.

**Explicitly not** sharing a Tailwind preset / `content` glob: it's less work but
hard-couples the charts to Tailwind and to GrowSF's theme, killing the
import-and-render-anywhere portability this whole split is for.

## Interactivity & URL state

Filter/selection state (`kinds`, year range, day range, trajectory selection)
currently lives in `useUrlState` + a React context (web) / props (viz). The whole
assembly moves into `packages/charts`: the `<LongCount>` provider owns the state and
the embeddable wrappers read it — the website embeds them around prose exactly as
now. URL-sync (read/write `window.location`) stays, but behind a prop
(`urlSync={false}` default-on for the site) so a non-URL consumer isn't forced into
it.

## Prose & docs migration

- **Prose** (`/` Story intro, `/eras` analysis, `/methods`) → the website. Most is
  already in `index.mdx`; the gap is the eras/methods narrative unique to the viz —
  audit and fold in.
- **`/sources`** → a data-repo doc generated from `sources.json` (every number +
  citation). The website may link to it; it is not a website page.
- **`/missing`** → a data-repo doc generated from the recovery ledger +
  `elections_master` `recovered=no` rows (the README "help wanted" section already
  seeds this).
- `sources.json` and `ledger.json` move into `packages/data` (they are data).

## What gets deleted / collapsed

- `viz/` (the whole Next app) — removed.
- `web/…/longcount/*` chart components + `datasets/` — removed; replaced by imports
  from `long-count/charts` + `long-count/data`.
- The duplicate-drift problem disappears: one set of components, one set of JSON.

## Build, release & images

- `build_viz_data.py` retargets its output from `viz/src/data/` to `packages/data/`
  (one `OUT` path change).
- **README chart images:** `viz/` is gone, so the screenshot target becomes the
  charts package's own **dev/preview harness** (defined under `packages/charts`
  above). `shoot_charts.js` barely changes — it points `SITE_URL` at the harness
  instead of the old viz app and locates each chart's `<figure>` by its `<h3>` title
  exactly as today. README-image generation stays **self-contained in the data
  repo** (no dependency on the deployed website) — and because the package's defaults
  *are* the website's styling (theme, chrome CSS, and the fonts the harness loads),
  those screenshots **look like the live site**. Harness choice: a lightweight Vite
  gallery is the default; Storybook if a fuller component workshop is wanted.
- The site bumps the git-dep ref deliberately to pick up new data (reproducible
  builds; data lands when chosen).

## Risks & open questions

- **Styling refactor surface** — every chart touches colors/classes; the theme +
  CSS migration is the bulk of the work. Mitigate by making today's values the
  defaults, so the move is behavior-preserving.
- **Prose completeness** — confirm nothing unique is lost from `/eras` / `/methods`
  when `viz/` is deleted.
- **Charts dev harness** — new surface to build (a Vite gallery or Storybook), but
  the charts need a development environment regardless, and it doubles as the README
  screenshot target (above) — so it earns its keep rather than being pure overhead.
- **Standalone viz URL** — if the viz was publicly deployed, add redirects to the
  web article. (Confirm whether it ever was.)
- **TrajectoryExplorer** — currently perf-hidden in the web embed; carry that hidden
  status into the package.
- **Whole-repo git-dep clone** — the site pulls the entire repo (Python/docs) as the
  dependency. Harmless (`mirror/` is gitignored, so licensed scans stay out), noted.

## Non-goals

- No npm publishing (single consumer).
- No change to the CSV schema or the Python recovery pipeline.
- No chart redesign — this is relocation + a theming seam, behavior-preserving.

## Rough sequencing (full plan to follow via writing-plans)

1. Stand up `packages/data` (move JSON, retarget the Python `OUT`, add types/index).
2. Extract `packages/charts` from the canonical (web) components; add the theme
   context + `charts.css`, defaulting to today's values (behavior-preserving).
3. Wire the workspace + root `exports`; stand up the dev/preview harness (Vite
   gallery / Storybook) so the charts render with the default theme + `packages/data`.
4. Point the website at the git dep + `transpilePackages`; swap its imports; delete
   `longcount/` + `datasets/`.
5. Migrate the eras/methods prose into the website; generate `/sources` + `/missing`
   docs in the data repo.
6. Retarget `shoot_charts.js` at the dev/preview harness; regenerate the README
   images; delete `viz/`.
7. Verify parity (charts byte-identical or visually identical), then cut over.
