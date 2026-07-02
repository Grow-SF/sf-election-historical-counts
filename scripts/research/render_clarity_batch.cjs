// Batch-render archived Clarity summary pages; print key turnout lines + the
// embedded "Updated <ts> PST/PT" data timestamp for each. Chrome must bypass the
// system proxy (web.archive.org is refused otherwise).
//   URLS="ts1|orig1 ts2|orig2 ..."  (space-separated; each = waybackts|originalurl)
// Renders https://web.archive.org/web/<ts>/<orig>
const puppeteer = require("puppeteer-core");
const CHROME = process.env.PUPPETEER_EXECUTABLE_PATH ||
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const WANT = /ballots cast|registered voters|voter turnout|updated|precincts (partially|completely|percent)|of \d/i;
(async () => {
  const b = await puppeteer.launch({ executablePath: CHROME, headless: true,
    args: ["--no-sandbox","--disable-setuid-sandbox","--proxy-server=direct://","--proxy-bypass-list=*"] });
  for (const item of process.env.URLS.trim().split(/\s+/)) {
    const [ts, ...rest] = item.split("|");
    const orig = rest.join("|");
    const url = `https://web.archive.org/web/${ts}/${orig}`;
    const p = await b.newPage();
    await p.setDefaultNavigationTimeout(45000);
    let txt = "";
    try {
      await p.goto(url, { waitUntil: "networkidle2", timeout: 45000 });
      await new Promise((r) => setTimeout(r, 4000));
      txt = await p.evaluate(() => (document.body ? document.body.innerText : ""));
    } catch (e) { txt = "NAVERR " + e.message; }
    const lines = txt.split("\n").map(s=>s.trim()).filter(s=>s && WANT.test(s) && s.length<90);
    console.log("### CAP", ts, "VER", orig.replace(/.*Santa_Clara\//,"").replace(/\/en.*/,""));
    console.log(lines.slice(0,12).join("\n") || "  (no turnout lines)");
    console.log("");
    await p.close();
  }
  await b.close();
})().catch((e) => { console.error("ERR", e.message); process.exit(1); });
