/**
 * Tailwind generator for `charts.css` (Task 9).
 *
 * Precompiles exactly the GrowSF utility classes the Long Count components use
 * into `src/charts.css`, all scoped under `.lc-root` so the standalone package
 * renders identically to the live GrowSF site without shipping Tailwind.
 *
 *  - `important: ".lc-root"` emits every utility as `.lc-root .text-sm { … }`,
 *    scoping + raising specificity so they win inside the provider's root.
 *  - `corePlugins.preflight: false` — never emit Tailwind's global reset; the
 *    chrome in `charts.src.css` hand-writes the bits the utilities depend on.
 *  - `theme.extend.colors` — the GrowSF palette copied verbatim as hardcoded hex
 *    from web/tailwind.config.js so opacity modifiers (`bg-gold/10`,
 *    `text-paper/55`) compute off the hex and match the site exactly.
 *
 * @type {import('tailwindcss').Config}
 */
module.exports = {
  content: ["./src/**/*.{ts,tsx}"],
  important: ".lc-root",
  corePlugins: { preflight: false },
  theme: {
    extend: {
      colors: {
        paper: "#FFFFEB",
        "paper-deep": "#EAF3EC",
        ink: "#16302E",
        night: "#044147",
        "night-soft": "#0B5158",
        rust: "#007784",
        "rust-bright": "#3FB6C9",
        faint: "#5E7167",
        rule: "#CFE3DA",
        "rule-dark": "#14565E",
        gold: "#64D09C",
        slate: "#0A82B2",
        moss: "#1E7B6A",
        plum: "#01384F",
      },
    },
  },
  plugins: [],
};
