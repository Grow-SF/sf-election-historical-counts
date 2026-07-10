# Task 8: alternate web-archive sweep -- san-bernardino-ca 2016-11-08

Target URLs (from the row's own dead-end note): the JS-iframe results host
`www.sbcounty.gov/rov/elections/Results/20161108/` -- specifically `default.html` (frameset) and
`content/results.aspx` (the inner iframe data page that Wayback never crawled at an election-night timestamp).

## Run 1 (2026-07-09): Library of Congress United States Elections Web Archive

- Same domain-wide Cloudflare JS-challenge wall confirmed on webarchive.loc.gov (see sacramento-ca-2016 Run 1);
  MISS.

## Run 1: Common Crawl

- Bracketing crawls: `CC-MAIN-2016-44` (Oct 2016), `CC-MAIN-2016-50` (Dec 2016).
- `curl "https://index.commoncrawl.org/CC-MAIN-2016-44-index?url=http%3A%2F%2Fwww.sbcounty.gov%2Frov%2Felections%2FResults%2F20161108%2Fdefault.html&output=json"` -> `{"message": "No Captures found..."}` (404).
- Same 404 for `CC-MAIN-2016-50` on `default.html`.
- Same 404 for both crawls on `content/results.aspx`.
- Tried `matchType=prefix` on `.../Results/20161108/` (whole directory) in `CC-MAIN-2016-44` -> also
  `No Captures found`.
- Conclusion: Common Crawl never crawled this results directory at all in either bracketing crawl. MISS.

## Run 1: Archive-It (CDL California collections)

- `curl --compressed "https://wayback.archive-it.org/all/timemap/link/http://www.sbcounty.gov/rov/elections/Results/20161108/default.html"` -> Archive-It's "Session Verification" SHA-256 proof-of-work bot-challenge
  page, same as every other row. MISS (bot wall, curl-unsolvable).

## Run 1: archive.today

- Debug-port Chrome (127.0.0.1:9222), puppeteer-core connect + reuse `pages()[0]`,
  `page.goto("https://archive.ph/https://www.sbcounty.gov/rov/elections/Results/20161108/default.html")`,
  disconnect only.
- Result: Cloudflare CAPTCHA wall. MISS, recorded and not fought further.

## Conclusion

All four archive families checked; none surfaces an election-night-window capture of San Bernardino's 2016
iframe results host beyond what the row's own note (Wayback: only a Nov 11 frameset default.html + a Nov 18
post-canvass content/results.aspx) and the NewsBank/CivicPlus/Twitter enumeration passes already exhausted.
Row stays null/none.
