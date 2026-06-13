// Surface the SFPL login window top-left for the user to sign in.
// Part of the archive-recovery runbook: docs/archive-recovery-runbook.md
// Prereqs: Chrome --remote-debugging-port=9222 + active SFPL ezproxy session; puppeteer-core.
// Writes to the gitignored mirror/ tree (licensed content - cited, never republished).

const puppeteer = require('puppeteer-core');
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  const page = await browser.newPage();
  const ps = await page.target().createCDPSession();
  const {windowId} = await ps.send('Browser.getWindowForTarget');
  await ps.send('Browser.setWindowBounds',{windowId,bounds:{left:80, top:60, width:1100, height:850}});
  // land on a known doc so a successful login shows the article immediately
  await page.goto('https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=news/0EB4F969E1C867F6',{waitUntil:'networkidle2',timeout:60000}).catch(()=>{});
  console.log('login window placed at top-left');
  browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
