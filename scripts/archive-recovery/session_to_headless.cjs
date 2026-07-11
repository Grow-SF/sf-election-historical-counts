// Transplant the authenticated ezproxy session from the visible login
// instance into a TRULY headless instance, so all subsequent NewsBank work
// runs with --headless=new (no window exists, so nothing can ever grab
// foreground or steal focus). This is the structural fix: the visible window
// exists only for the one-time human login; work never touches it.
//
// Usage: node session_to_headless.cjs <live_port> <headless_url>
// Prints "OK <headless_url>" on success.
const puppeteer = require('puppeteer-core');

(async () => {
  const livePort = process.argv[2];
  const headlessURL = process.argv[3];

  // 1. Read all cookies from the live (visible) authenticated instance.
  const live = await puppeteer.connect({ browserURL: 'http://127.0.0.1:' + livePort, defaultViewport: null });
  const lp = (await live.pages())[0];
  const ls = await lp.target().createCDPSession();
  const { cookies } = await ls.send('Network.getAllCookies');
  await ls.detach();
  live.disconnect();
  if (!cookies.length) throw new Error('no cookies on live instance; is it logged in?');

  // 2. Inject them into the headless instance.
  const head = await puppeteer.connect({ browserURL: headlessURL, defaultViewport: null });
  const hp = (await head.pages())[0] || (await head.newPage());
  const hs = await hp.target().createCDPSession();
  await hs.send('Network.setCookies', { cookies });
  await hs.detach();
  head.disconnect();

  console.log('OK transplanted ' + cookies.length + ' cookies into ' + headlessURL);
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
