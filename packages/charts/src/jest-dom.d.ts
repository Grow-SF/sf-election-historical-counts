// Pull the @testing-library/jest-dom matcher augmentation (toBeInTheDocument,
// etc.) into the package's type program. The matchers run at test time via the
// repo-root vitest.setup.ts; this side-effect import makes their TYPES visible
// to `tsc -p packages/charts` (whose `include` is only ./src), so the component
// smoke tests type-check.
import "@testing-library/jest-dom/vitest";
