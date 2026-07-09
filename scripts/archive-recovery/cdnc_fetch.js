// Fetch OCR text (or run a full-text search) against CDNC - the California
// Digital Newspaper Collection, cdnc.ucr.edu - through a REAL Chrome tab over
// CDP. CDNC sits behind a Cloudflare managed challenge that hard-blocks
// curl/WebFetch (see .superpowers/sdd/cdnc-scout-report.md).
//
// IMPORTANT DISCOVERY: puppeteer's normal Page API (page.goto/page.evaluate/
// browser.newPage()) ALSO gets stuck on the Cloudflare challenge forever,
// even in this real, human-driven Chrome. Puppeteer's Page class auto-sends
// the Runtime.enable CDP command on construction, and Cloudflare's managed
// challenge appears to detect that and never clears. The fix, confirmed by
// side-by-side test: drive the tab with a RAW CDPSession instead - only
// Page.enable + Network.enable + DOM.getDocument/getOuterHTML, never
// Runtime.enable/page.evaluate. That passes the challenge in ~5s, same as a
// human tab. Full story: .superpowers/sdd/cdnc-chrome-recipe.md
//
// Usage:
//   node cdnc_fetch.js <ISSUE>                  list the issue's page/article TOC
//   node cdnc_fetch.js <ISSUE> <PAGE_NUMBER>     OCR text of every article on that page
//   node cdnc_fetch.js <ISSUE> <SECTION_OID>     OCR text of one specific section
//   node cdnc_fetch.js <ISSUE> search:<PHRASE>   full-text search scoped to this issue's
//                                                 paper+date, then OCR every hit
// ISSUE = <paper code><YYYYMMDD>, e.g. SFC18961104 (SF Call, 4 Nov 1896) or
// DAC18670217 (Daily Alta California). Paper codes confirmed so far: SFC, DAC
// (see cdnc-scout-report.md for how those were found; the live search form's
// <select name="puq"> has ~540 more CA paper codes if you need another title).
//
// Prereqs: Chrome running with --remote-debugging-port=9222; puppeteer-core
// on NODE_PATH. Prints OCR/search text to stdout AND saves a copy under the
// gitignored mirror/cdnc/<issue>/ tree (provenance: source URL + fetch date).
//
// IMPORTANT: opens its OWN new blank tab and closes it when done. Never
// touches any existing tab - this Chrome profile may hold other live sessions
// (e.g. NewsBank/SFPL ezproxy) that must not be navigated.

const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

const MIRROR_ROOT = path.join(__dirname, '..', '..', 'mirror', 'cdnc');
// Veridian coreData.state constant seen on every link of a bare browse-mode
// page load (English, 20-per-page, text+title-index search defaults). It is
// NOT session- or search-specific - confirmed by reading the page's own
// data-core-data-json blob (see recipe doc). Reusing it verbatim works for
// both the getSectionText AJAX call and the search-form GET.
const STATE = 'e=-------en--20--1--txt-txIN--------';
const CHALLENGE_RE = /Just a moment|Performing security verification|Enable JavaScript and cookies/i;

function usageAndExit() {
  console.error('Usage: node cdnc_fetch.js <ISSUE e.g. SFC18961104> [PAGE_NUMBER|SECTION_OID|search:PHRASE]');
  process.exit(1);
}

function parseIssue(issue) {
  const m = /^([A-Z]+)(\d{4})(\d{2})(\d{2})$/.exec(issue);
  if (!m) throw new Error(`ISSUE must look like SFC18961104, got: ${issue}`);
  const [, paper, y, mo, d] = m;
  return { paper, y, mo, d };
}

function decodeEntities(s) {
  return s
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&amp;/g, '&');
}

// TOC anchor inner-HTML is single-encoded real page HTML.
function stripTagsOnce(s) {
  return decodeEntities(s.replace(/<[^>]+>/g, ' ')).replace(/\s+/g, ' ').trim();
}

// getSectionText's <SectionText> body is XML-escaped HTML (double layer):
// decode once to get real tags, strip them, decode again for entities that
// were inside the article text itself (e.g. &amp; in "Smith &amp; Jones").
function xmlHtmlToText(s) {
  const realHtml = decodeEntities(s);
  const noTags = realHtml.replace(/<[^>]+>/g, '\n');
  return decodeEntities(noTags).replace(/[ \t]+/g, ' ').replace(/\n\s*\n+/g, '\n').trim();
}

async function connectRawSession() {
  const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9222', defaultViewport: null });
  const cdp = await browser.target().createCDPSession();
  const { targetId } = await cdp.send('Target.createTarget', { url: 'about:blank',
    // background:true + reusing the existing window keeps Chrome from
    // stealing macOS keyboard focus on every fetch (operator complaint)
    newWindow: false, background: true });
  const target = await browser.waitForTarget(t => t._targetId === targetId);
  // Do NOT call target.page() - see header comment. Raw session only.
  const session = await target.createCDPSession();
  await session.send('Page.enable');
  await session.send('Network.enable');
  return { browser, session, targetId };
}

async function navGetHtml(session, url, { maxWaitMs = 25000, pollMs = 1500 } = {}) {
  await session.send('Page.navigate', { url });
  const start = Date.now();
  let lastHtml = '';
  while (Date.now() - start < maxWaitMs) {
    await new Promise(r => setTimeout(r, pollMs));
    const doc = await session.send('DOM.getDocument').catch(() => null);
    if (!doc) continue;
    const out = await session.send('DOM.getOuterHTML', { nodeId: doc.root.nodeId }).catch(() => null);
    if (!out) continue;
    lastHtml = out.outerHTML;
    if (!CHALLENGE_RE.test(lastHtml)) return lastHtml;
  }
  throw new Error(`Cloudflare challenge did not clear within ${maxWaitMs}ms for ${url}`);
}

function parseToc(html) {
  const items = [];
  const re = /<a class="sectionlinkwithinviewer logicalsectiontocnodelink" data-section-oid="([^"]+)" data-page-oid="([^"]+)" href="([^"]+)">([\s\S]*?)<\/a>/g;
  let m;
  while ((m = re.exec(html))) {
    const [, sectionOid, pageOid, , inner] = m;
    items.push({ sectionOid, pageOid, title: stripTagsOnce(inner) });
  }
  return items;
}

async function fetchSectionText(session, sectionOid) {
  const url = `https://cdnc.ucr.edu/?a=da&command=getSectionText&d=${encodeURIComponent(sectionOid)}&f=AJAX&${STATE}`;
  const html = await navGetHtml(session, url);
  const m = /<SectionText type="HTML">([\s\S]*?)<\/SectionText>/.exec(html);
  if (!m) {
    if (/<Error>/.test(html)) {
      const em = /<Error>([\s\S]*?)<\/Error>/.exec(html);
      throw new Error(`getSectionText error for ${sectionOid}: ${em ? em[1] : html.slice(0, 300)}`);
    }
    throw new Error(`getSectionText: no <SectionText> found for ${sectionOid}`);
  }
  return { url, text: xmlHtmlToText(m[1]) };
}

function parseSearchResults(html) {
  const results = [];
  const re = /href="\/\?a=d&amp;d=([^&"]+)&amp;srpos=(\d+)&amp;e=([^"]*)"[\s\S]{0,20}?>([\s\S]*?)<\/a>/g;
  // The result title link is the first <a> inside each vlistentry; grab a
  // generous window after each match for the snippet text too.
  const blockRe = /<div class="vlistentry searchresult">([\s\S]*?)<\/div>\s*<\/div>\s*<\/div>/g;
  let bm;
  while ((bm = blockRe.exec(html))) {
    const block = bm[1];
    const hrefM = /href="\/\?a=d&amp;d=([^&"]+)&amp;srpos=(\d+)&amp;e=([^"]*)"/.exec(block);
    if (!hrefM) continue;
    const text = stripTagsOnce(block);
    results.push({ sectionOid: hrefM[1], srpos: hrefM[2], snippet: text });
  }
  return results;
}

function mirrorDir(issue) {
  const dir = path.join(MIRROR_ROOT, issue);
  fs.mkdirSync(dir, { recursive: true });
  return dir;
}

function provenance(sourceUrl) {
  return `SOURCE: ${sourceUrl}\nACCESSED: ${new Date().toISOString().slice(0, 10)} via real Chrome CDP (Cloudflare-challenge bypass; see scripts/archive-recovery/cdnc_fetch.js header)\n\n`;
}

async function main() {
  const issueArg = process.argv[2];
  const secondArg = process.argv[3];
  if (!issueArg) usageAndExit();
  const { paper, y, mo, d } = parseIssue(issueArg);
  const dir = mirrorDir(issueArg);

  const { browser, session, targetId } = await connectRawSession();
  try {
    if (!secondArg) {
      // TOC mode
      const issueUrl = `https://cdnc.ucr.edu/?a=d&d=${issueArg}`;
      const html = await navGetHtml(session, issueUrl);
      const toc = parseToc(html);
      fs.writeFileSync(path.join(dir, 'toc.json'), JSON.stringify({ issue: issueArg, sourceUrl: issueUrl, items: toc }, null, 2));
      console.log(`# TOC for ${issueArg} (${toc.length} sections) - ${issueUrl}`);
      for (const it of toc) {
        const pageNum = it.pageOid.split('.').pop();
        console.log(`p${pageNum}\t${it.sectionOid}\t${it.title}`);
      }
      console.log(`\n[saved ${path.join(dir, 'toc.json')}]`);
      return;
    }

    if (/^search:/.test(secondArg)) {
      const phrase = secondArg.slice('search:'.length);
      const params = new URLSearchParams({
        a: 'q', hs: '1', r: '1', results: '1',
        txq: phrase, txf: 'txIN', ssnip: 'txt',
        puq: paper,
        dafdq: d, dafmq: mo, dafyq: y,
        datdq: d, datmq: mo, datyq: y,
      });
      const searchUrl = `https://cdnc.ucr.edu/?${params.toString()}&${STATE}`;
      const html = await navGetHtml(session, searchUrl);
      const results = parseSearchResults(html);
      console.log(`# Search "${phrase}" in ${paper} on ${y}-${mo}-${d}: ${results.length} hit(s) - ${searchUrl}`);
      const outLines = [`SEARCH: ${phrase}`, `SCOPE: ${paper} ${y}-${mo}-${d}`, provenance(searchUrl)];
      for (const r of results) {
        console.log(`\n## ${r.sectionOid} (srpos ${r.srpos})\n${r.snippet}`);
        outLines.push(`## ${r.sectionOid} (srpos ${r.srpos})\n${r.snippet}\n`);
        try {
          const { text } = await fetchSectionText(session, r.sectionOid);
          console.log(`\n--- OCR text ---\n${text}\n`);
          outLines.push(`--- OCR text ---\n${text}\n`);
        } catch (e) {
          console.error(`  (could not fetch OCR for ${r.sectionOid}: ${e.message})`);
        }
      }
      const slug = phrase.replace(/[^a-z0-9]+/gi, '_').slice(0, 50);
      const outFile = path.join(dir, `search_${slug}.txt`);
      fs.writeFileSync(outFile, outLines.join('\n'));
      console.log(`\n[saved ${outFile}]`);
      return;
    }

    if (/^\d+$/.test(secondArg)) {
      // Page-number mode: fetch TOC first to find sections on that page.
      const issueUrl = `https://cdnc.ucr.edu/?a=d&d=${issueArg}`;
      const html = await navGetHtml(session, issueUrl);
      const toc = parseToc(html);
      const pageOid = `${issueArg}.1.${secondArg}`;
      const sections = toc.filter(it => it.pageOid === pageOid);
      if (sections.length === 0) throw new Error(`No sections found with page-oid ${pageOid}; run TOC mode first to see valid page numbers`);
      const parts = [`ISSUE: ${issueArg}  PAGE: ${secondArg}`, provenance(issueUrl)];
      for (const sec of sections) {
        console.log(`\n## ${sec.sectionOid}: ${sec.title}`);
        parts.push(`## ${sec.sectionOid}: ${sec.title}`);
        try {
          const { text } = await fetchSectionText(session, sec.sectionOid);
          console.log(text);
          parts.push(text + '\n');
        } catch (e) {
          console.error(`  (skip ${sec.sectionOid}: ${e.message})`);
        }
      }
      const outFile = path.join(dir, `page_${secondArg}.txt`);
      fs.writeFileSync(outFile, parts.join('\n'));
      console.log(`\n[saved ${outFile}]`);
      return;
    }

    // Otherwise: treat secondArg as an explicit section OID.
    const sectionOid = secondArg;
    const { url, text } = await fetchSectionText(session, sectionOid);
    console.log(text);
    const outFile = path.join(dir, `section_${sectionOid.replace(/[^a-zA-Z0-9._-]/g, '_')}.txt`);
    fs.writeFileSync(outFile, `SECTION: ${sectionOid}\n${provenance(url)}${text}\n`);
    console.log(`\n[saved ${outFile}]`);
  } finally {
    await session.send('Target.closeTarget', { targetId }).catch(() => {});
    browser.disconnect();
  }
}

main().catch(e => { console.error('ERR', e.message); process.exit(1); });
