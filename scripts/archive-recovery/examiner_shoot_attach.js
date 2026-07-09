// Attach-only screenshotter: finds the tab whose URL contains <match> and saves
// viewport slices while scrolling. NEVER navigates, never creates tabs/windows.
// Drive navigation separately (e.g. via the MCP tab you own), then run this.
// Usage: node examiner_shoot_attach.js <urlSubstring> <outprefix> [slices]
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');
const match = process.argv[2], outprefix = process.argv[3];
const SLICES = parseInt(process.argv[4] || '8', 10);
(async () => {
  const browser = await puppeteer.connect({browserURL: 'http://127.0.0.1:9222', defaultViewport: null});
  const targets = browser.targets().filter(t => t.type() === 'page' && t.url().includes(match));
  if (targets.length !== 1) {
    console.error(`EXPECTED EXACTLY 1 TAB MATCHING "${match}", found ${targets.length}`);
    targets.forEach(t => console.error('  ' + t.url().slice(0, 120)));
    process.exit(3);
  }
  const page = await targets[0].page();
  const robot = await page.evaluate(() => /might be a Robot|hCaptcha|I am human/i.test(document.body.innerText.slice(0, 3000))).catch(() => false);
  if (robot) { console.error('ROBOT CHECK PRESENT - STOPPING'); process.exit(4); }
  fs.mkdirSync(path.dirname(outprefix), {recursive: true});
  let prevY = -1;
  for (let s = 0; s < SLICES; s++) {
    await page.screenshot({path: `${outprefix}_s${s}.png`});
    console.log('slice', s, 'saved');
    const y = await page.evaluate(() => { window.scrollBy(0, Math.round(window.innerHeight * 0.85)); return window.scrollY; });
    await new Promise(r => setTimeout(r, 1500));
    if (y === prevY) { console.log('bottom at slice', s); break; }
    prevY = y;
  }
  browser.disconnect();
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
