// Render static PNGs of the site's charts for the README, via headless Chrome.
// Prereqs: the charts preview harness running (`pnpm --filter @long-count/preview exec vite`, :4317) and
// puppeteer-core (a root devDependency — `pnpm install` makes it resolvable from the repo root).
// Usage:  node scripts/shoot_charts.cjs
// Chrome path: set PUPPETEER_EXECUTABLE_PATH, else the macOS default below.
const fs = require("fs");
const path = require("path");
const puppeteer = require("puppeteer-core");

const URL = process.env.SITE_URL || "http://localhost:4317/";
const CHROME =
  process.env.PUPPETEER_EXECUTABLE_PATH ||
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

// Coverage-fitted year ranges. The preview's default range (1902 to the latest
// election) crops charts whose data starts earlier (turnout begins 1879) and
// triggers the no-data edge shading on charts whose data spans less (the
// franchise funnel covers 1908-2024), which reads as blank slabs in a static
// image. Fit those charts' URL state to their own data coverage.
const dataFile = (f) =>
  JSON.parse(
    fs.readFileSync(path.join(__dirname, "..", "packages", "data", f), "utf8"),
  );
const span = (rows, year) => {
  const ys = rows.map(year);
  return [Math.min(...ys), Math.max(...ys)];
};
const TURNOUT_RANGE = span(dataFile("turnout_history.json"), (r) => +r.date.slice(0, 4));
const FUNNEL_RANGE = span(dataFile("franchise_funnel.json"), (r) => r.year);

// output file -> { title: substring of the chart's <h3> to locate its <figure>,
//                  range: optional [from, to] applied via the site's URL state }
const TARGETS = {
  "docs/img/night-share.png": { title: "How much of the vote was counted" },
  "docs/img/turnout.png": { title: "Turnout of registered voters", range: TURNOUT_RANGE },
  "docs/img/vote-by-mail.png": { title: "Vote-by-mail share of ballots cast" },
  "docs/img/franchise-funnel.png": { title: "Who could vote", range: FUNNEL_RANGE },
};

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ["--no-sandbox"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1180, height: 1500, deviceScaleFactor: 2 });

  // group targets by URL (the year range is shared page state, so each
  // distinct range needs its own page load)
  const byUrl = new Map();
  for (const [file, { title, range }] of Object.entries(TARGETS)) {
    const url = range
      ? `${URL}${URL.includes("?") ? "&" : "?"}from=${range[0]}&to=${range[1]}`
      : URL;
    if (!byUrl.has(url)) byUrl.set(url, []);
    byUrl.get(url).push([file, title]);
  }

  for (const [url, targets] of byUrl) {
    await page.goto(url, { waitUntil: "networkidle2", timeout: 60000 });
    await new Promise((r) => setTimeout(r, 3000)); // let recharts settle
    for (const [file, title] of targets) {
      const h = await page.evaluateHandle((t) => {
        const fig = [...document.querySelectorAll("figure")].find((f) =>
          f.querySelector("h3")?.textContent.includes(t),
        );
        if (fig) fig.scrollIntoView({ block: "center" });
        return fig || null;
      }, title);
      const el = h.asElement();
      if (!el) { console.log("NOT FOUND:", title); continue; }
      await new Promise((r) => setTimeout(r, 600));
      await el.screenshot({ path: file });
      console.log("saved", file);
    }
  }
  await browser.close();
})().catch((e) => { console.error("ERR", e.message); process.exit(1); });
