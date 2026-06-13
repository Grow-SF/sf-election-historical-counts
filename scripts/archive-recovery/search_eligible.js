// Search NewsBank (AWN/SFPL) for SF "eligible voters" / "voting-age" / citizen
// reporting, to anchor the franchise-denominator (eligible) baseline.
// Part of the archive-recovery runbook: docs/archive-recovery-runbook.md
// Prereqs: Chrome --remote-debugging-port=9222 + active SFPL ezproxy session.
// Prints dated candidate hits (date,title,docref,snippet) for triage; the text
// archive starts ~1985 so pre-1985 needs the image edition. Saves nothing here.
const puppeteer = require('puppeteer-core');
const RANGE = '01/01/1985 - 12/31/2012';
const QUERIES = [
  '"San Francisco" "voting age population"',
  '"San Francisco" "eligible voters"',
  '"San Francisco" "of voting age"',
  '"San Francisco" registrar "eligible to vote"',
];
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  const page = await browser.newPage();
  for (const q of QUERIES) {
    const u='https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results'
      +'&fld-base-0=alltext&val-base-0='+encodeURIComponent(q)
      +'&bln-base-1=AND&fld-base-1=YMD_date&val-base-1='+encodeURIComponent(RANGE)
      +'&sort=YMD_date%3AA';
    await page.goto(u,{waitUntil:'networkidle2',timeout:90000}).catch(()=>{});
    await new Promise(r=>setTimeout(r,3500));
    const walled = await page.evaluate(()=>/Articles and Databases|Authentication/i.test(document.title)).catch(()=>false);
    if (walled) { console.error('AUTH WALL'); process.exit(2); }
    const rows = await page.evaluate(()=>{
      const out=[]; const seen=new Set();
      for (const a of document.querySelectorAll('a[href*="docref=news"]')) {
        const m=a.href.match(/docref=news(?:%2F|\/)([A-F0-9]+)/); if(!m||seen.has(m[1]))continue; seen.add(m[1]);
        const card=a.closest('article,li,div')||a.parentElement;
        const txt=(card?card.innerText:a.innerText).replace(/\s+/g,' ').trim().slice(0,300);
        out.push({id:m[1], txt});
      }
      return out.slice(0,12);
    }).catch(()=>[]);
    console.log('\n===== QUERY:',q,'('+rows.length+' hits) =====');
    for (const r of rows) console.log(r.id, '|', r.txt);
  }
  await page.close(); browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
