# packages/charts (`long-count/charts`)

The reusable React chart components. The GrowSF web repo consumes this
package as a PINNED GIT DEPENDENCY of this repository, shipping RAW `.tsx`
source (no build step). That is why the constraints below exist; break them
and this repo's tests stay green while the downstream Next.js build breaks.

## Portability constraints (non-negotiable)

- **Imports of the data package are RELATIVE** (`../../../data/index`), never
  `long-count/data` or `@long-count/data`. The package-name alias exists only
  in this repo's root `vitest.config.ts` for tests; the downstream bundler
  does not recreate workspace aliases from a git dependency. Do not "clean
  up" the triple-relative imports.
- **Every component file starts with `"use client";`** (they use hooks and
  recharts). Omitting it breaks the Next.js App Router consumer at build
  time, not here.
- **Extensionless local imports** (`./types`, not `./types.js`): Turbopack
  and webpack do not remap `.js` to `.ts` the way tsc/Vite do.

## Commands (all from the REPO ROOT)

```bash
pnpm install                                   # once per checkout
pnpm vitest run                                # the test suite (no "test" script alias exists)
pnpm --filter @long-count/preview exec vite    # preview harness on :4317
pnpm --filter @long-count/charts build:css     # regenerate src/charts.css
node scripts/shoot_charts.cjs                  # README chart PNGs (harness must be running)
```

## charts.css convention

`src/charts.css` is GENERATED from `src/charts.src.css` by `build:css`
(Tailwind utilities precompiled under `.lc-root`; the package ships no
Tailwind). After touching component classNames, rerun `build:css`: either
the output is byte-identical (nothing to do) or the diff is real and gets
committed. A class name used by a component but missing from `charts.css`
renders unstyled downstream with no error here.

## Styling scope

`.lc-root` is applied per chart island (and FilterBar), NOT around consumer
content: wrapping arbitrary children in `.lc-root` cascades the package's
serif/reset styles onto the consuming article (this was a real regression).
