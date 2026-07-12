// Move ezproxy Chrome windows off-screen so they don't disrupt the user.
// Part of the archive-recovery runbook: docs/archive-recovery-runbook.md
// Prereqs: a browserURL from scripts/research/iso_chrome.sh (headless; see the focus-safe
// launcher docs) with an authenticated SFPL ezproxy profile; puppeteer-core.
// Writes to the gitignored mirror/ tree (licensed content - cited, never republished).

const puppeteer = require('puppeteer-core');
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  for (const page of await browser.pages()) {
    if (page.url().includes('infoweb-newsbank-com.ezproxy')) {
      const ps = await page.target().createCDPSession();
      const {windowId} = await ps.send('Browser.getWindowForTarget');
      await ps.send('Browser.setWindowBounds',{windowId,bounds:{left:3000, top:2000, width:1200, height:900}});
      console.log('parked', page.url().slice(0,80));
    }
  }
  browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
