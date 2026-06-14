// Render static PNGs of the site's charts for the README, via headless Chrome.
// Prereqs: the dev server running (`cd viz && npm run dev`, default :3000) and
// puppeteer-core (in viz/node_modules — run with NODE_PATH=viz/node_modules).
// Usage:  NODE_PATH=viz/node_modules node scripts/shoot_charts.js
// Chrome path: set PUPPETEER_EXECUTABLE_PATH, else the macOS default below.
const puppeteer = require("puppeteer-core");

const URL = process.env.SITE_URL || "http://localhost:3000/";
const CHROME =
  process.env.PUPPETEER_EXECUTABLE_PATH ||
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";

// output file -> a substring of the chart's <h3> title to locate its <figure>
const TARGETS = {
  "docs/img/night-share.png": "How much of the vote was counted",
  "docs/img/vote-by-mail.png": "Vote-by-mail share of ballots cast",
  "docs/img/franchise-funnel.png": "Who could vote",
};

(async () => {
  const browser = await puppeteer.launch({
    executablePath: CHROME,
    headless: true,
    args: ["--no-sandbox"],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1180, height: 1500, deviceScaleFactor: 2 });
  await page.goto(URL, { waitUntil: "networkidle2", timeout: 60000 });
  await new Promise((r) => setTimeout(r, 3000)); // let recharts settle
  for (const [file, title] of Object.entries(TARGETS)) {
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
  await browser.close();
})().catch((e) => { console.error("ERR", e.message); process.exit(1); });
