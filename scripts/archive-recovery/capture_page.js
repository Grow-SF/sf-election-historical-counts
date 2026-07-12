// Pan-until-bottom image capture of one page as overlapping slices. Usage: node capture_page.js <url> <out.png>
// Part of the archive-recovery runbook: docs/archive-recovery-runbook.md
// Prereqs: a browserURL from scripts/research/iso_chrome.sh (headless; see the focus-safe
// launcher docs) with an authenticated SFPL ezproxy profile; puppeteer-core.
// Writes to the gitignored mirror/ tree (licensed content - cited, never republished).

const puppeteer = require('puppeteer-core');
const fs = require('fs');
const url = process.argv[2], out = process.argv[3];
const MAXSLICES = 14;
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  const cdp = await browser.target().createCDPSession();
  const {targetId} = await cdp.send('Target.createTarget',{url:'about:blank', newWindow:true});
  const page = await (await browser.waitForTarget(t=>t._targetId===targetId)).page();
  const ps = await page.target().createCDPSession();
  const {windowId} = await ps.send('Browser.getWindowForTarget');
  await ps.send('Browser.setWindowBounds',{windowId,bounds:{left:3300, top:2300, width:2400, height:2600}});
  await page.goto(url,{waitUntil:'networkidle2',timeout:90000}).catch(()=>{});
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
  const box = await page.evaluate(()=>{
    const c=[...document.querySelectorAll('canvas')].sort((a,b)=>b.width*b.height-a.width*a.height)[0];
    const r=c.getBoundingClientRect(); return {x:r.x+r.width/2, y:r.y+r.height/2, h:r.height};
  });
  let prev=null, saved=0;
  for (let s=0; s<MAXSLICES; s++) {
    if (s>0) {
      const dy=box.h*0.7;
      await page.mouse.move(box.x, box.y+dy/2); await page.mouse.down();
      await page.mouse.move(box.x, box.y-dy/2, {steps:12}); await page.mouse.up();
      await new Promise(r=>setTimeout(r,2200));
    }
    await stabilize();
    const data=await snap();
    if(!data||data.length<120000){console.log('slice',s,'capture failed');continue;}
    // pan-until-stable: if content stopped changing, we've hit the page bottom
    if (prev && data===prev) { console.log('bottom reached at slice', s-1); break; }
    fs.writeFileSync(out.replace('.png',`_s${s}.png`),Buffer.from(data.split(',')[1],'base64'));
    prev=data; saved++;
    console.log('slice',s,'captured');
  }
  console.log('total slices:', saved);
  await page.close().catch(()=>{});
  browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
