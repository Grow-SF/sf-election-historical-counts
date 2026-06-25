/**
 * PostCSS pipeline for the `build:css` step. The Tailwind CLI applies its own
 * Tailwind pass (from `--config ./tailwind.config.cjs`) and then runs the
 * plugins listed here — autoprefixer, for parity with the website's build
 * (e.g. the `-webkit-` prefix on `backdrop-filter` from `backdrop-blur-*`).
 */
module.exports = {
  plugins: {
    autoprefixer: {},
  },
};
