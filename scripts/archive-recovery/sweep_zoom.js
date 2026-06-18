// High-resolution capture of ONE page of an image-edition issue: bumps device
// pixel ratio AND zooms the deep-zoom viewer in, then captures a grid of tiles
// so dense ward/precinct tables become legible (fit-to-page capture is too low-res).
// Usage: node sweep_zoom.js <election> <issue> <page> <ZOOM> <WIN>
//   ZOOM = number of wheel-in notches (try 4-8). Higher = more tiles, sharper.
// Writes mirror/newsbank/scans/zoom_<EL>_issue<ISSUE>_p<PAGE>_r<row>_c<col>.png
const puppeteer = require('puppeteer-core');
const fs = require('fs');
const DIR='/Users/sbuss/workspace/sf-election-count/mirror/newsbank/scans/';
const EL=process.argv[2], LABEL=process.argv[3], PAGE=+process.argv[4];
const ZOOM=+(process.argv[5]||5), WIN=+(process.argv[6]||0);
function f(d){const x=new Date(d+'T12:00:00');return `${String(x.getMonth()+1).padStart(2,'0')}/${String(x.getDate()).padStart(2,'0')}/${x.getFullYear()}`;}
(async () => {
  const browser = await puppeteer.connect({browserURL:'http://127.0.0.1:9222', defaultViewport:null});
  const cdp = await browser.target().createCDPSession();
  const {targetId} = await cdp.send('Target.createTarget',{url:'about:blank', newWindow:true});
  const page = await (await browser.waitForTarget(t=>t._targetId===targetId)).page();
  const ps = await page.target().createCDPSession();
  const {windowId} = await ps.send('Browser.getWindowForTarget');
  await ps.send('Browser.setWindowBounds',{windowId,bounds:{left:3300+(WIN%5)*340, top:2300+Math.floor(WIN/5)*300, width:2400, height:2600}});
  // 3x device pixel ratio => 3x canvas pixels for the same page.
  await page.setViewport({width:2200, height:2400, deviceScaleFactor:3});
  const dr=`${f(LABEL)} - ${f(LABEL)}`;
  const u='https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results'
    +'&fld-base-0=alltext&val-base-0='+encodeURIComponent('election')
    +'&bln-base-1=AND&fld-nav-0=YMD_date&val-nav-0='+encodeURIComponent(dr)+'&sort=YMD_date%3AA';
  await page.goto(u,{waitUntil:'networkidle2',timeout:90000}).catch(()=>{});
  await new Promise(r=>setTimeout(r,3600));
  const id = await page.evaluate(()=>{const a=document.querySelector('a[href*="docref=image"]');const m=a&&a.href.match(/docref=image(?:%2F|\/)([^&"]+)/);return m?decodeURIComponent(m[1]):null;});
  if(!id){console.error('NO ENTRY for',LABEL);process.exit(3);}
  console.log('entry ok',id.slice(0,40));
  await page.goto('https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=image/'+encodeURIComponent(id),{waitUntil:'networkidle2',timeout:90000}).catch(()=>{});
  await new Promise(r=>setTimeout(r,5000));
  // navigate to target page
  for(let guard=0; guard<40; guard++){
    const cur=await page.evaluate(()=>{const m=document.body.innerText.match(/Page (\d+) of (\d+)/);return m?{p:+m[1],n:+m[2]}:null;}).catch(()=>null);
    if(!cur){await new Promise(r=>setTimeout(r,2000));continue;}
    if(cur.p===PAGE)break;
    if(PAGE>cur.n){console.log('only',cur.n,'pages');process.exit(4);}
    const step=cur.p<PAGE?cur.p+1:cur.p-1;
    const ok=await page.evaluate((t)=>{const b=[...document.querySelectorAll('button,a')].find(x=>(x.title||x.getAttribute('aria-label'))===('Page '+t));if(!b)return false;b.click();return true;},step).catch(()=>false);
    if(!ok)break; await new Promise(r=>setTimeout(r,3200));
  }
  const box=await page.evaluate(()=>{const c=[...document.querySelectorAll('canvas')].sort((a,b)=>b.width*b.height-a.width*a.height)[0];const r=c.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2,w:r.width,h:r.height};}).catch(()=>null);
  if(!box){console.log('no canvas');process.exit(5);}
  // zoom in ZOOM notches via the OpenSeadragon zoom-in BUTTON (wheel/dblclick are
  // ignored by this viewer; the button engages true deep-zoom = higher-res tiles).
  for(let z=0;z<ZOOM;z++){
    const ok=await page.evaluate(()=>{const b=document.querySelector('#openseadragon__zoom-toolbar--button--zoom-in')||[...document.querySelectorAll('button')].find(x=>x.title==='Zoom in');if(!b)return false;b.click();return true;}).catch(()=>false);
    if(!ok){console.log('no zoom-in button');break;}
    await new Promise(r=>setTimeout(r,700));
  }
  await new Promise(r=>setTimeout(r,2500));
  async function snap(){return await page.evaluate(()=>{const c=[...document.querySelectorAll('canvas')].sort((a,b)=>b.width*b.height-a.width*a.height)[0];return c?c.toDataURL('image/png'):null;}).catch(()=>null);}
  async function stabilize(){let last=-1,st=0;for(let i=0;i<12;i++){await new Promise(r=>setTimeout(r,1500));const ink=await page.evaluate(()=>{const c=[...document.querySelectorAll('canvas')].sort((a,b)=>b.width*b.height-a.width*a.height)[0];if(!c||!c.width)return -1;const d=c.getContext('2d').getImageData(0,0,c.width,c.height).data;let dk=0;for(let k=0;k<d.length;k+=800)if(d[k]<128)dk++;return dk;}).catch(()=>-2);if(ink>100&&Math.abs(ink-last)<Math.max(15,ink*0.01)){st++;if(st>=2)return;}else st=0;last=ink;}}
  // grid pan: GRID x GRID cells. After zoom the page is ~ZOOM-scaled; sample a grid.
  const GRID=Math.max(3, Math.ceil(ZOOM/1.5));
  // first pan to top-left corner: drag down-right repeatedly
  for(let i=0;i<GRID;i++){ await page.mouse.move(box.x,box.y);await page.mouse.down();await page.mouse.move(box.x+box.w*0.42,box.y+box.h*0.42,{steps:10});await page.mouse.up();await new Promise(r=>setTimeout(r,500)); }
  let saved=0;
  for(let r=0;r<GRID;r++){
    for(let c=0;c<GRID;c++){
      await stabilize();
      const data=await snap();
      if(data&&data.length>120000){fs.writeFileSync(`${DIR}zoom_${EL.replace(/-/g,'')}_issue${LABEL.replace(/-/g,'')}_p${PAGE}_r${r}_c${c}.png`,Buffer.from(data.split(',')[1],'base64'));saved++;}
      // pan left (move content right) to next column
      if(c<GRID-1){await page.mouse.move(box.x,box.y);await page.mouse.down();await page.mouse.move(box.x-box.w*0.75,box.y,{steps:10});await page.mouse.up();await new Promise(rr=>setTimeout(rr,500));}
    }
    // carriage return: pan all the way right, then down one row
    for(let k=0;k<GRID-1;k++){await page.mouse.move(box.x,box.y);await page.mouse.down();await page.mouse.move(box.x+box.w*0.75,box.y,{steps:8});await page.mouse.up();await new Promise(rr=>setTimeout(rr,350));}
    if(r<GRID-1){await page.mouse.move(box.x,box.y);await page.mouse.down();await page.mouse.move(box.x,box.y-box.h*0.75,{steps:10});await page.mouse.up();await new Promise(rr=>setTimeout(rr,500));}
  }
  console.log('zoom page',PAGE,'grid',GRID+'x'+GRID,'saved',saved);
  await page.close().catch(()=>{});
  browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
