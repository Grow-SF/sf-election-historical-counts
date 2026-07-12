// iso_probe.js <browserURL>
//
// Headless session-validity probe. Connects with puppeteer-core to a Chrome
// already running via scripts/research/iso_chrome.sh (headless "new" - no
// window exists, so this script never renders anything visible), loads the
// runbook's known NewsBank docref, and reports whether the SFPL ezproxy
// session is authenticated.
//
// Exit 0: authenticated (article content loaded, no auth-wall text).
// Exit 3: auth wall detected ("Articles and Databases" signature text) -
//         the session needs the login ceremony (iso_chrome.sh login).
// Exit 1: any other failure (missing/bad browserURL, connect/timeout error).
//
// Part of docs/superpowers/plans/2026-07-10-focus-safe-browser.md /
// docs/archive-recovery-runbook.md. Modeled on the port-parameterized copy
// of scripts/archive-recovery/session_probe.js used earlier.
// Note: this repo's root package.json sets "type": "module", so this file
// is loaded as an ES module (import, not require) even with a .js extension.

import puppeteer from 'puppeteer-core';

const DOC_URL =
  'https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=news/0EB4F969E1C867F6';
const AUTH_WALL_SIGNATURE = 'Articles and Databases';

async function main() {
  const browserURL = process.argv[2];
  if (!browserURL) {
    console.error('usage: iso_probe.js <browserURL>');
    process.exit(1);
  }

  const browser = await puppeteer.connect({ browserURL, defaultViewport: null });
  try {
    const page = await browser.newPage();
    await page
      .goto(DOC_URL, { waitUntil: 'networkidle2', timeout: 60000 })
      .catch(() => {});
    await new Promise((r) => setTimeout(r, 2500));
    const text = await page.evaluate(() => document.body.innerText);
    await page.close();

    if (text.includes(AUTH_WALL_SIGNATURE)) {
      console.error('AUTH WALL: session is not authenticated (run the login ceremony)');
      process.exit(3);
    }

    console.log('AUTHENTICATED: session is alive');
    process.exit(0);
  } finally {
    browser.disconnect();
  }
}

main().catch((e) => {
  console.error('ERR', e.message);
  process.exit(1);
});
