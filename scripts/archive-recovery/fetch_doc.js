// Save one Access World News text document. Usage: node fetch_doc.js <DOCID> <ELECTION>
// Part of the archive-recovery runbook: docs/archive-recovery-runbook.md
// Prereqs: Chrome --remote-debugging-port=9222 + active SFPL ezproxy session; puppeteer-core.
// Writes to the gitignored mirror/ tree (licensed content - cited, never republished).

const puppeteer = require('puppeteer-core');
const fs = require('fs');
const id = process.argv[2], el = process.argv[3];
const DIR='/Users/sbuss/workspace/sf-election-count/mirror/newsbank/';
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  const page=await browser.newPage();
  const url=`https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=news/${id}`;
  await page.goto(url,{waitUntil:'networkidle2',timeout:60000}).catch(()=>{});
  await new Promise(r=>setTimeout(r,2800));
  const doc=await page.evaluate(()=>({title:document.title,text:document.body.innerText}));
  if(/Articles and Databases|Authentication/i.test(doc.title+' '+doc.text.slice(0,2000))){console.error('AUTH WALL');process.exit(2);}
  const fn=`${DIR}docs/${el.replace(/-/g,'')}_${id}.txt`;
  fs.writeFileSync(fn,`DOCID: ${id}\nELECTION: ${el}\nSOURCE: ${url}\nACCESSED: 2026-06-12 via SFPL ezproxy (NewsBank Access World News)\nTITLE: ${doc.title}\n\n${doc.text}`);
  console.log('saved', fn, doc.title);
  await page.close(); browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
