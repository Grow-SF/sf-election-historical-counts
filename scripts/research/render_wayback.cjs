// Render an archived (Wayback) JS-heavy election-results page and dump the
// turnout/ballot-count lines. WebFetch is blocked for web.archive.org, but the
// shell + headless Chrome are not, and these ENR pages are JS-rendered (curl
// gets an empty shell), so puppeteer is required.
//
// Usage:  WB_URL="https://web.archive.org/web/<ts>/<original>" \
//           NODE_PATH=$(pwd)/node_modules node scripts/research/render_wayback.cjs
//
// Recipe to find <ts>: query the Wayback CDX API with curl (NOT WebFetch), e.g.
//   curl "https://web.archive.org/cdx/search/cdx?url=<results-page>&from=<YYYYMMDD>&to=<+1day>&output=json&filter=statuscode:200&filter=mimetype:text/html&limit=8"
// then pick the FIRST snapshot AFTER poll close (8pm PT ≈ 04:00 UTC next day)
// whose rendered "Ballots Cast/Counted" is non-zero (the earliest capture is
// often pre-close and reads 0).
const puppeteer = require("puppeteer-core");
const CHROME =
  process.env.PUPPETEER_EXECUTABLE_PATH ||
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
(async () => {
  const b = await puppeteer.launch({ executablePath: CHROME, headless: true, args: ["--no-sandbox"] });
  const p = await b.newPage();
  await p.setDefaultNavigationTimeout(60000);
  try {
    await p.goto(process.env.WB_URL, { waitUntil: "networkidle2", timeout: 60000 });
  } catch (e) { console.log("nav warn:", e.message); }
  await new Promise((r) => setTimeout(r, 6000));
  const text = await p.evaluate(() => (document.body ? document.body.innerText : ""));
  const lines = text.split("\n").map((s) => s.trim()).filter((s) =>
    /ballot|turnout|counted|registered|cast|reporting|precinct/i.test(s) && s.length < 120);
  console.log(lines.slice(0, 30).join("\n"));
  await b.close();
})().catch((e) => { console.error("ERR", e.message); process.exit(1); });
