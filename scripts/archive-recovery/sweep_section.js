// Walk a page range of an image-edition issue, full-capturing each. Usage: node sweep_section.js <election> <issue> <p0> <p1>
// Part of the archive-recovery runbook: docs/archive-recovery-runbook.md
// Prereqs: Chrome --remote-debugging-port=9222 + active SFPL ezproxy session; puppeteer-core.
// Writes to the gitignored mirror/ tree (licensed content - cited, never republished).

const puppeteer = require('puppeteer-core');
const fs = require('fs');
const DIR='/Users/sbuss/workspace/sf-election-count/mirror/newsbank/scans/';
const EL = process.argv[2];        // e.g. 2008-06-03
const LABEL = process.argv[3];     // issue date label e.g. 2008-06-04
const P0 = +(process.argv[4]||20), P1 = +(process.argv[5]||26);
const MAXSLICES = 12;
function f(d){const x=new Date(d+'T12:00:00');return `${String(x.getMonth()+1).padStart(2,'0')}/${String(x.getDate()).padStart(2,'0')}/${x.getFullYear()}`;}
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  const cdp = await browser.target().createCDPSession();
  const {targetId} = await cdp.send('Target.createTarget',{url:'about:blank', newWindow:true});
  const page = await (await browser.waitForTarget(t=>t._targetId===targetId)).page();
  const ps = await page.target().createCDPSession();
  const {windowId} = await ps.send('Browser.getWindowForTarget');
  await ps.send('Browser.setWindowBounds',{windowId,bounds:{left:3300, top:2300, width:2400, height:2600}});
  // entry docref via free search
  const u=`https://sfchronicle.newsbank.com/search?text=election&date_from=${encodeURIComponent(f(LABEL))}&date_to=${encodeURIComponent(f(LABEL))}&pub%5B0%5D=142051F45F422A02`;
  await page.goto(u,{waitUntil:'networkidle2',timeout:60000}).catch(()=>{});
  await new Promise(r=>setTimeout(r,3600));
  const id = await page.evaluate(()=>{
    const a=document.querySelector('a[href*="/doc/image/"]');
    const m=a&&a.href.match(/doc\/image\/(v2[^?]+)/);
    return m?decodeURIComponent(m[1]):null;
  });
  if(!id){console.error('NO ENTRY for', LABEL);process.exit(3);}
  console.log('entry ok');
  await page.goto('https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=image/'+encodeURIComponent(id),{waitUntil:'networkidle2',timeout:90000}).catch(()=>{});
  await new Promise(r=>setTimeout(r,5000));
  const walled = await page.evaluate(()=>/Articles and Databases|Authentication/i.test(document.title+' '+document.body.innerText.slice(0,1500))).catch(()=>false);
  if (walled) { console.error('AUTH WALL'); process.exit(2); }
  async function stabilize(){
    let last=-1, stable=0;
    for(let i=0;i<20;i++){
      await new Promise(r=>setTimeout(r,2200));
      const ink=await page.evaluate(()=>{
        const c=[...document.querySelectorAll('canvas')].sort((a,b)=>b.width*b.height-a.width*a.height)[0];
        if(!c||!c.width) return -1;
        const ctx=c.getContext('2d'); const d=ctx.getImageData(0,0,c.width,c.height).data;
        let dark=0; for(let k=0;k<d.length;k+=800) if(d[k]<128) dark++;
        return dark;
      }).catch(()=>-2);
      if(ink>150 && Math.abs(ink-last)<Math.max(15,ink*0.01)){stable++; if(stable>=2) return;} else stable=0;
      last=ink;
    }
  }
  async function snap(){
    return await page.evaluate(()=>{
      const c=[...document.querySelectorAll('canvas')].sort((a,b)=>b.width*b.height-a.width*a.height)[0];
      return c?c.toDataURL('image/png'):null;
    }).catch(()=>null);
  }
  for (let target=P0; target<=P1; target++) {
    // navigate to target page
    let ok=false;
    for (let guard=0; guard<40; guard++) {
      const cur = await page.evaluate(()=>{
        const m=document.body.innerText.match(/Page (\d+) of (\d+)/);
        return m?{p:+m[1],n:+m[2]}:null;
      }).catch(()=>null);
      if (!cur) { await new Promise(r=>setTimeout(r,2000)); continue; }
      if (cur.p===target) { ok=true; break; }
      if (target>cur.n) { console.log('issue has only',cur.n,'pages'); break; }
      const step = cur.p<target ? cur.p+1 : cur.p-1;
      const clicked = await page.evaluate((t)=>{
        const b=[...document.querySelectorAll('button,a')].find(x=>(x.title||x.getAttribute('aria-label'))===('Page '+t));
        if(!b) return false; b.click(); return true;
      }, step).catch(()=>false);
      if(!clicked) break;
      await new Promise(r=>setTimeout(r,3200));
    }
    if(!ok){console.log('could not reach page',target);continue;}
    const box = await page.evaluate(()=>{
      const c=[...document.querySelectorAll('canvas')].sort((a,b)=>b.width*b.height-a.width*a.height)[0];
      const r=c.getBoundingClientRect(); return {x:r.x+r.width/2, y:r.y+r.height/2, h:r.height};
    }).catch(()=>null);
    if(!box){console.log('no canvas page',target);continue;}
    let prev=null, saved=0;
    for (let s=0; s<MAXSLICES; s++) {
      if (s>0) {
        const dy=box.h*0.7;
        await page.mouse.move(box.x, box.y+dy/2); await page.mouse.down();
        await page.mouse.move(box.x, box.y-dy/2, {steps:12}); await page.mouse.up();
        await new Promise(r=>setTimeout(r,2000));
      }
      await stabilize();
      const data=await snap();
      if(!data||data.length<120000) continue;
      if (prev && data===prev) break;
      fs.writeFileSync(`${DIR}sweep_${EL.replace(/-/g,'')}_issue${LABEL.replace(/-/g,'')}_p${target}_s${s}.png`,Buffer.from(data.split(',')[1],'base64'));
      prev=data; saved++;
    }
    console.log('page',target,'slices:',saved);
    // reset to top for next page navigation (pan back up)
    for(let r=0;r<saved;r++){
      await page.mouse.move(box.x, box.y-box.h*0.35); await page.mouse.down();
      await page.mouse.move(box.x, box.y+box.h*0.35, {steps:8}); await page.mouse.up();
      await new Promise(rr=>setTimeout(rr,600));
    }
  }
  console.log('sweep done');
  await page.close().catch(()=>{});
  browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
