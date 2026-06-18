// Probe NewsBank image-edition coverage for a list of issue dates (no capture).
// Usage: node coverage_probe.js 1884-11-05 1880-11-03 1876-11-08 ...
// For each date, runs the ezproxy date-filtered results search and reports
// whether an SF Chronicle image-edition issue (docref=image) exists + its title.
const puppeteer = require('puppeteer-core');
const dates = process.argv.slice(2);
function f(d){const x=new Date(d+'T12:00:00');return `${String(x.getMonth()+1).padStart(2,'0')}/${String(x.getDate()).padStart(2,'0')}/${x.getFullYear()}`;}
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  const cdp = await browser.target().createCDPSession();
  const {targetId} = await cdp.send('Target.createTarget',{url:'about:blank', newWindow:true});
  const page = await (await browser.waitForTarget(t=>t._targetId===targetId)).page();
  for (const d of dates) {
    const dr=`${f(d)} - ${f(d)}`;
    const u='https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results'
      +'&fld-base-0=alltext&val-base-0='+encodeURIComponent('election')
      +'&bln-base-1=AND&fld-nav-0=YMD_date&val-nav-0='+encodeURIComponent(dr)
      +'&sort=YMD_date%3AA';
    await page.goto(u,{waitUntil:'networkidle2',timeout:90000}).catch(()=>{});
    await new Promise(r=>setTimeout(r,3000));
    const info = await page.evaluate(()=>{
      const walled=/Articles and Databases|Authentication|Sign in/i.test(document.title);
      const a=document.querySelector('a[href*="docref=image"]');
      const m=a&&a.href.match(/docref=image(?:%2F|\/)([^&"]+)/);
      const cnt=(document.body.innerText.match(/([\d,]+)\s+result/i)||[])[1]||'?';
      // try to grab the source/title text of the first hit
      const title=a?(a.textContent||'').trim().slice(0,80):'';
      return {walled, has: !!m, id:m?decodeURIComponent(m[1]).slice(0,40):null, cnt, title};
    }).catch(e=>({err:e.message}));
    console.log(d, JSON.stringify(info));
  }
  await page.close().catch(()=>{});
  browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
