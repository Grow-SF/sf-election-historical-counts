// Legible high-zoom capture of ONE page: engages OpenSeadragon deep-zoom by
// CLICKING the zoom-in button AT ITS COORDINATES (synthetic .click() and wheel are
// ignored by this viewer), then drag-pans a grid and saves real page screenshots
// (canvas.toDataURL does NOT reflect OSD zoom; page.screenshot does).
// Usage: node zoom_grid.js <election> <issue> <page> <ZCLICKS> <GRID> <WIN>
// Writes mirror/newsbank/scans/zg_<EL>_issue<ISSUE>_p<PAGE>_r<r>_c<c>.png
const puppeteer=require("puppeteer-core");const fs=require("fs");
const DIR="/Users/sbuss/workspace/sf-election-count/mirror/newsbank/scans/";
const EL=process.argv[2],LABEL=process.argv[3],PAGE=+process.argv[4];
const ZCLICKS=+(process.argv[5]||6),GRID=+(process.argv[6]||4),WIN=+(process.argv[7]||0);
function f(d){const x=new Date(d+"T12:00:00");return String(x.getMonth()+1).padStart(2,"0")+"/"+String(x.getDate()).padStart(2,"0")+"/"+x.getFullYear();}
(async()=>{
  const b=await puppeteer.connect({browserURL:"http://127.0.0.1:9222",defaultViewport:null});
  const sess=await b.target().createCDPSession();
  const {targetId}=await sess.send("Target.createTarget",{url:"about:blank",newWindow:true});
  const page=await(await b.waitForTarget(t=>t._targetId===targetId)).page();
  const ps=await page.target().createCDPSession();const {windowId}=await ps.send("Browser.getWindowForTarget");
  await ps.send("Browser.setWindowBounds",{windowId,bounds:{left:3300+(WIN%5)*340,top:2300+Math.floor(WIN/5)*300,width:2400,height:2600}});
  await page.setViewport({width:2200,height:2400,deviceScaleFactor:3});
  const dr=f(LABEL)+" - "+f(LABEL);
  const u="https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=alltext&val-base-0=election&bln-base-1=AND&fld-nav-0=YMD_date&val-nav-0="+encodeURIComponent(dr)+"&sort=YMD_date%3AA";
  await page.goto(u,{waitUntil:"networkidle2",timeout:90000}).catch(()=>{});await new Promise(r=>setTimeout(r,3300));
  const id=await page.evaluate(()=>{const a=document.querySelector('a[href*="docref=image"]');const m=a&&a.href.match(/docref=image(?:%2F|\/)([^&"]+)/);return m?decodeURIComponent(m[1]):null;});
  if(!id){console.error("NO ENTRY",LABEL);process.exit(3);}
  console.log("entry",id.slice(0,40));
  await page.goto("https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=image/"+encodeURIComponent(id),{waitUntil:"networkidle2",timeout:90000}).catch(()=>{});await new Promise(r=>setTimeout(r,5000));
  for(let g=0;g<40;g++){const c=await page.evaluate(()=>{const m=document.body.innerText.match(/Page (\d+) of (\d+)/);return m?{p:+m[1],n:+m[2]}:null;}).catch(()=>null);if(!c){await new Promise(r=>setTimeout(r,2000));continue;}if(c.p===PAGE)break;if(PAGE>c.n){console.log("only",c.n,"pages");process.exit(4);}const step=c.p<PAGE?c.p+1:c.p-1;const ok=await page.evaluate(t=>{const x=[...document.querySelectorAll("button,a")].find(e=>(e.title||e.getAttribute("aria-label"))===("Page "+t));if(!x)return false;x.click();return true;},step).catch(()=>false);if(!ok)break;await new Promise(r=>setTimeout(r,3200));}
  const canv=await page.evaluate(()=>{const c=[...document.querySelectorAll("canvas")].sort((a,b)=>b.width*b.height-a.width*a.height)[0];const r=c.getBoundingClientRect();return {x:r.x,y:r.y,w:r.width,h:r.height};}).catch(()=>null);
  if(!canv){console.log("no canvas");process.exit(5);}
  const cx=canv.x+canv.w/2, cy=canv.y+canv.h/2;
  const zb=await page.evaluate(()=>{const x=document.querySelector("#openseadragon__zoom-toolbar--button--zoom-in")||[...document.querySelectorAll("button")].find(e=>e.title==="Zoom in");if(!x)return null;const r=x.getBoundingClientRect();return {x:r.x+r.width/2,y:r.y+r.height/2};});
  if(!zb){console.log("no zoom button");process.exit(6);}
  for(let z=0;z<ZCLICKS;z++){await page.mouse.click(zb.x,zb.y);await new Promise(r=>setTimeout(r,750));}
  await new Promise(r=>setTimeout(r,2200));
  // clip to canvas region for screenshots (CSS px; deviceScaleFactor handles DPI)
  const clip={x:canv.x,y:canv.y,width:canv.w,height:canv.h};
  async function settle(){await new Promise(r=>setTimeout(r,1400));}
  async function dragTo(dx,dy){await page.mouse.move(cx,cy);await page.mouse.down();await page.mouse.move(cx+dx,cy+dy,{steps:12});await page.mouse.up();await new Promise(r=>setTimeout(r,500));}
  // go to top-left: push content down-right
  for(let i=0;i<GRID+1;i++){await dragTo(canv.w*0.45,canv.h*0.45);}
  let saved=0;
  for(let r=0;r<GRID;r++){
    for(let c=0;c<GRID;c++){
      await settle();
      await page.screenshot({path:`${DIR}zg_${EL.replace(/-/g,"")}_issue${LABEL.replace(/-/g,"")}_p${PAGE}_r${r}_c${c}.png`,clip});
      saved++;
      if(c<GRID-1) await dragTo(-canv.w*0.78,0); // pan content left -> reveal right
    }
    for(let k=0;k<GRID-1;k++){await dragTo(canv.w*0.78,0);} // carriage return
    if(r<GRID-1) await dragTo(0,-canv.h*0.78); // next row down
  }
  console.log("zoom-grid page",PAGE,GRID+"x"+GRID,"saved",saved);
  await page.close().catch(()=>{});b.disconnect();
})().catch(e=>{console.error("ERR",e.message);process.exit(1);});
