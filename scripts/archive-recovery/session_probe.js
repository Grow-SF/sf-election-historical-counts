// Load a known NewsBank doc to confirm the SFPL ezproxy session is alive.
// Part of the archive-recovery runbook: docs/archive-recovery-runbook.md
// Prereqs: a browserURL from scripts/research/iso_chrome.sh (headless; see the focus-safe
// launcher docs) with an authenticated SFPL ezproxy profile; puppeteer-core.
// Writes to the gitignored mirror/ tree (licensed content - cited, never republished).

const puppeteer = require('puppeteer-core');
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  const page = await browser.newPage();
  await page.goto('https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=news/0EB4F969E1C867F6',{waitUntil:'networkidle2',timeout:60000}).catch(()=>{});
  await new Promise(r=>setTimeout(r,2500));
  const t = await page.evaluate(()=>({title:document.title, snip:document.body.innerText.slice(0,300)}));
  console.log('TITLE:', t.title);
  console.log('SNIP:', t.snip.replace(/\n+/g,' | ').slice(0,200));
  await page.close();
  browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
