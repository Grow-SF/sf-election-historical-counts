// Continuous window parker: connects to a live Chrome over the DevTools
// protocol and moves EVERY window off-screen the instant it appears, so
// NewsBank popups/new tabs cannot flash on-screen or steal focus. Run this
// in the background for the whole duration of a ceremony-session worker.
// Usage: node park_watch.cjs <port>   (default 9230)
const puppeteer = require('puppeteer-core');

const PORT = process.argv[2] || '9230';
const OFF = { left: -32000, top: -32000, width: 1200, height: 900 };

async function parkAll(browser) {
  for (const page of await browser.pages()) {
    try {
      const s = await page.target().createCDPSession();
      const { windowId } = await s.send('Browser.getWindowForTarget');
      await s.send('Browser.setWindowBounds', { windowId, bounds: OFF });
      await s.detach();
    } catch (e) { /* target gone or not a window; ignore */ }
  }
}

(async () => {
  const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:' + PORT, defaultViewport: null });
  await parkAll(browser);
  // Repark whenever a target is created or navigates (covers popups + new tabs).
  browser.on('targetcreated', () => parkAll(browser));
  browser.on('targetchanged', () => parkAll(browser));
  // Belt and suspenders: a low-frequency sweep catches anything the events miss.
  const timer = setInterval(() => parkAll(browser), 400);
  console.log('park_watch active on port ' + PORT + '; parking all windows off-screen continuously');
  process.on('SIGTERM', () => { clearInterval(timer); browser.disconnect(); process.exit(0); });
})().catch(e => { console.error('park_watch ERR', e.message); process.exit(1); });
