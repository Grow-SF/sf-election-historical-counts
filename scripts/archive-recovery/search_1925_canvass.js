// Find the complete / official canvass returns for the Nov 3 1925 SF municipal
// election (denominator: certified total ballots). Image-edition OCR search.
// Prereqs: Chrome --remote-debugging-port=9222 + active SFPL ezproxy session.
const puppeteer = require('puppeteer-core');
const NAV = '11/3/1925 - 12/15/1925';
const QUERIES = [
  '"official canvass" San Francisco',
  '"complete returns" "819 precincts"',
  '"819 precincts"',
  'Zemansky "total vote"',
  '"complete official" returns election',
];
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  const page = await browser.newPage();
  for (const q of QUERIES) {
    const u='https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results'
      +'&fld-base-0=alltext&val-base-0='+encodeURIComponent(q)
      +'&bln-base-1=AND&fld-nav-0=YMD_date&val-nav-0='+encodeURIComponent(NAV)
      +'&sort=YMD_date%3AA&maxresults=30';
    await page.goto(u,{waitUntil:'networkidle2',timeout:90000}).catch(()=>{});
    await new Promise(r=>setTimeout(r,3500));
    const walled = await page.evaluate(()=>/Articles and Databases|Authentication/i.test(document.title)).catch(()=>false);
    if (walled) { console.error('AUTH WALL'); process.exit(2); }
    const rows = await page.evaluate(()=>{
      const out=[]; const seen=new Set();
      for (const a of document.querySelectorAll('a[href*="docref=image"]')) {
        const m=a.href.match(/docref=image(?:%2F|\/)([^&"]+)/); if(!m)continue;
        const id=decodeURIComponent(m[1]); if(seen.has(id))continue; seen.add(id);
        const card=a.closest('article,li,div')||a.parentElement;
        const txt=(card?card.innerText:a.innerText).replace(/\s+/g,' ').trim().slice(0,260);
        out.push({id, txt});
      }
      return out.slice(0,15);
    }).catch(()=>[]);
    console.log('\n===== QUERY:',q,'('+rows.length+' hits) =====');
    for (const r of rows) console.log(r.id, '|', r.txt);
  }
  await page.close(); browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
