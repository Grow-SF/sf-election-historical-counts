// Multi-paper text harvest: per election x date-window x query, collect docrefs and fetch each.
// Part of the archive-recovery runbook: docs/archive-recovery-runbook.md
// Prereqs: a browserURL from scripts/research/iso_chrome.sh (headless; see the focus-safe
// launcher docs) with an authenticated SFPL ezproxy profile; puppeteer-core.
// Writes to the gitignored mirror/ tree (licensed content - cited, never republished).

const puppeteer = require('puppeteer-core');
const fs = require('fs');
const DIR='/Users/sbuss/workspace/sf-election-count/mirror/newsbank/';
const TARGETS=["1985-11-05","1987-04-07","1987-06-02","1993-11-02","1995-11-07","1999-11-02","1999-12-14","2000-11-07","2002-12-10","2003-10-07","2005-11-08","2006-11-07","2010-11-02"];
const QUERIES=['"San Francisco" "precincts reporting"','"San Francisco" "ballots counted"','"San Francisco" mayor returns counted'];
const CAP=12;
function f(d){const x=new Date(d+'T12:00:00');return `${String(x.getMonth()+1).padStart(2,'0')}/${String(x.getDate()).padStart(2,'0')}/${x.getFullYear()}`;}
function plus(d,n){const x=new Date(d+'T12:00:00');x.setDate(x.getDate()+n);return x.toISOString().slice(0,10);}
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  const page = await browser.newPage();
  const have=new Set(fs.readdirSync(DIR+'docs').map(x=>x.split('_')[1]?.replace('.txt','')));
  const found=[];
  for (const el of TARGETS) {
    let per=0;
    for (const q of QUERIES) {
      if (per>=CAP) break;
      const u='https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results'
        +'&fld-base-0=alltext&val-base-0='+encodeURIComponent(q)
        +'&bln-base-1=AND&fld-base-1=YMD_date&val-base-1='+encodeURIComponent(f(el)+' - '+f(plus(el,3)));
      await page.goto(u,{waitUntil:'networkidle2',timeout:90000}).catch(()=>{});
      await new Promise(r=>setTimeout(r,3500));
      const walled = await page.evaluate(()=>/Articles and Databases|Authentication/i.test(document.title)).catch(()=>false);
      if (walled) { console.error('AUTH WALL'); process.exit(2); }
      const res=await page.evaluate(()=>{
        const out=[]; const seen=new Set();
        for (const a of document.querySelectorAll('a[href*="docref=news"]')) {
          const m=a.href.match(/docref=news(?:%2F|\/)([A-F0-9]+)/);
          if(!m||seen.has(m[1])) continue; seen.add(m[1]); out.push(m[1]);
        }
        return out;
      }).catch(()=>[]);
      for (const id of res) {
        if (per>=CAP) break;
        if (!have.has(id) && !found.some(x=>x.id===id)) { found.push({el,id}); per++; }
      }
    }
    console.log(el, 'queued:', per);
  }
  console.log('to harvest:', found.length);
  let n=0;
  for (const r of found) {
    const fn=`${DIR}docs/${r.el.replace(/-/g,'')}_${r.id}.txt`;
    if (fs.existsSync(fn)) continue;
    const url=`https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=news/${r.id}`;
    await page.goto(url,{waitUntil:'networkidle2',timeout:60000}).catch(()=>{});
    await new Promise(rs=>setTimeout(rs,2600));
    const doc=await page.evaluate(()=>({title:document.title,text:document.body.innerText})).catch(()=>({title:'',text:''}));
    if(/Articles and Databases|Authentication/i.test(doc.title)){console.error('AUTH WALL');process.exit(2);}
    if(doc.text.length<600) continue;
    fs.writeFileSync(fn,`DOCID: ${r.id}\nELECTION: ${r.el}\nSOURCE: ${url}\nACCESSED: 2026-06-13 via SFPL ezproxy (NewsBank Access World News, multi-paper)\nTITLE: ${doc.title}\n\n${doc.text}`);
    n++;
  }
  console.log('harvested:',n);
  await page.close(); browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
