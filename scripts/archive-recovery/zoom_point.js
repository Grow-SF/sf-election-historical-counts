// Zoom into a specific point of one page of an image-edition issue and capture.
// Uses double-click (the deep-zoom viewer's native zoom-in) at a fractional point,
// repeated CLICKS times, then captures the canvas (DPR 3). Good for reading a
// returns table's TOTALS row without needing every ward cell.
// Usage: node zoom_point.js <election> <issue> <page> <fx> <fy> <CLICKS> <WIN> [tag]
//   fx,fy = fractional point on the page (0..1) to zoom toward.
// Writes mirror/newsbank/scans/zpt_<EL>_issue<ISSUE>_p<PAGE>_<tag>.png
const puppeteer=require('puppeteer-core');const fs=require('fs');
const DIR='/Users/sbuss/workspace/sf-election-count/mirror/newsbank/scans/';
const EL=process.argv[2],LABEL=process.argv[3],PAGE=+process.argv[4];
const FX=+process.argv[5],FY=+process.argv[6],CLICKS=+(process.argv[7]||3),WIN=+(process.argv[8]||0);
const TAG=process.argv[9]||`${Math.round(FX*100)}_${Math.round(FY*100)}`;
function f(d){const x=new Date(d+'T12:00:00');return `${String(x.getMonth()+1).padStart(2,'0')}/${String(x.getDate()).padStart(2,'0')}/${x.getFullYear()}`;}
(async()=>{
  const browser=await puppeteer.connect({browserURL:'http://127.0.0.1:9222',defaultViewport:null});
  const cdp=await browser.target().createCDPSession();
  const {targetId}=await cdp.send('Target.createTarget',{url:'about:blank',newWindow:true});
  const page=await(await browser.waitForTarget(t=>t._targetId===targetId)).page();
  const ps=await page.target().createCDPSession();const {windowId}=await ps.send('Browser.getWindowForTarget');
  await ps.send('Browser.setWindowBounds',{windowId,bounds:{left:3300+(WIN%5)*340,top:2300+Math.floor(WIN/5)*300,width:2400,height:2600}});
  await page.setViewport({width:2200,height:2400,deviceScaleFactor:3});
  const dr=`${f(LABEL)} - ${f(LABEL)}`;
  const u='https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=alltext&val-base-0='+encodeURIComponent('election')+'&bln-base-1=AND&fld-nav-0=YMD_date&val-nav-0='+encodeURIComponent(dr)+'&sort=YMD_date%3AA';
  await page.goto(u,{waitUntil:'networkidle2',timeout:90000}).catch(()=>{});
  await new Promise(r=>setTimeout(r,3600));
  const id=await page.evaluate(()=>{const a=document.querySelector('a[href*="docref=image"]');const m=a&&a.href.match(/docref=image(?:%2F|\/)([^&"]+)/);return m?decodeURIComponent(m[1]):null;});
  if(!id){console.error('NO ENTRY');process.exit(3);}
  console.log('entry',id.slice(0,40));
  await page.goto('https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=image/'+encodeURIComponent(id),{waitUntil:'networkidle2',timeout:90000}).catch(()=>{});
  await new Promise(r=>setTimeout(r,5000));
  for(let g=0;g<40;g++){const cur=await page.evaluate(()=>{const m=document.body.innerText.match(/Page (\d+) of (\d+)/);return m?{p:+m[1],n:+m[2]}:null;}).catch(()=>null);if(!cur){await new Promise(r=>setTimeout(r,2000));continue;}if(cur.p===PAGE)break;if(PAGE>cur.n){console.log('only',cur.n);process.exit(4);}const step=cur.p<PAGE?cur.p+1:cur.p-1;const ok=await page.evaluate(t=>{const b=[...document.querySelectorAll('button,a')].find(x=>(x.title||x.getAttribute('aria-label'))===('Page '+t));if(!b)return false;b.click();return true;},step).catch(()=>false);if(!ok)break;await new Promise(r=>setTimeout(r,3200));}
  function getbox(){return page.evaluate(()=>{const c=[...document.querySelectorAll('canvas')].sort((a,b)=>b.width*b.height-a.width*a.height)[0];const r=c.getBoundingClientRect();return{x:r.x,y:r.y,w:r.width,h:r.height};}).catch(()=>null);}
  let box=await getbox();if(!box){console.log('no canvas');process.exit(5);}
  // double-click zoom toward the target point, re-reading box each time (it stays same CSS size)
  for(let i=0;i<CLICKS;i++){
    const px=box.x+box.w*FX, py=box.y+box.h*FY;
    await page.mouse.click(px,py,{clickCount:2,delay:60});
    await new Promise(r=>setTimeout(r,1800));
  }
  await new Promise(r=>setTimeout(r,2500));
  const data=await page.evaluate(()=>{const c=[...document.querySelectorAll('canvas')].sort((a,b)=>b.width*b.height-a.width*a.height)[0];return c?c.toDataURL('image/png'):null;}).catch(()=>null);
  if(data&&data.length>100000){const out=`${DIR}zpt_${EL.replace(/-/g,'')}_issue${LABEL.replace(/-/g,'')}_p${PAGE}_${TAG}.png`;fs.writeFileSync(out,Buffer.from(data.split(',')[1],'base64'));console.log('saved',out);}else{console.log('snap failed len',data&&data.length);}
  await page.close().catch(()=>{});browser.disconnect();
})().catch(e=>{console.error('ERR',e.message);process.exit(1)});
