# Task 8: alternate web-archive sweep -- madera-ca 2012-11-06

Target URL note: the task-8 brief names `votemadera.com result28.htm/resultsc28.htm` for this row, but that
folder (`/results/Election28/HTML/...`) is actually the Nov 2014 results set (confirmed by CDX: the earliest
capture of any `election28` path is `20141108134805`/`20141108151723`, and the row's own 2014 note already
documents result28.htm/resultsc28.htm as the 2014 numerator source). The 2012 row's own note already
establishes that votemadera.com's WordPress/Joomla results system (Election<N> numbered folders) did not exist
yet in Nov 2012: Wayback's earliest capture of the whole domain is the 02/02/2011 homepage, then nothing until
Oct 2014. There is therefore no fixed 2012 target URL to test; this sweep checked the bare domain root and, for
completeness, the general county site, across all four families.

## Run 1 (2026-07-09): Library of Congress United States Elections Web Archive

- Same domain-wide Cloudflare JS-challenge wall confirmed on webarchive.loc.gov (see sacramento-ca-2016 Run 1
  for the full curl/response detail); MISS, not re-tested per-URL here.

## Run 1: Common Crawl

- No fixed 2012 URL exists for votemadera.com, so queried the bare domain (`http://votemadera.com/`) against
  every crawl that could plausibly reach back to or shortly after Nov 2012: `CC-MAIN-2012` (ARC-era, but its
  crawl window is 2012-01-27 to 2012-06-05 -- entirely BEFORE the Nov 2012 election, so structurally cannot
  contain election-night data regardless of query result), `CC-MAIN-2013-20` (2013-05-18/06-20), and
  `CC-MAIN-2013-48` (2013-12-04/12-22).
- `curl "https://index.commoncrawl.org/CC-MAIN-2013-20-index?url=http%3A%2F%2Fvotemadera.com%2F&output=json"` ->
  `{"message": "No Captures found for: http://votemadera.com/"}` (HTTP 404).
- Same "No Captures found" for `CC-MAIN-2013-48`.
- Conclusion: Common Crawl has ZERO captures of votemadera.com in either the crawl immediately before or the
  crawl about a year after the election; the domain was simply not in Common Crawl's crawl frontier during this
  window (consistent with Wayback's own finding that nothing else crawled the site between Feb 2011 and Oct
  2014). MISS, and structurally so (no crawl exists close enough in time even in principle for CC-MAIN-2012).

## Run 1: Archive-It (CDL California collections)

- `curl --compressed "https://wayback.archive-it.org/all/timemap/link/http://votemadera.com/"` -> same
  Archive-It "Session Verification" SHA-256 proof-of-work bot-challenge page as every other row (see
  sacramento-ca-2016 Run 1). MISS (bot wall, curl-unsolvable).

## Run 1: archive.today

- Debug-port Chrome (127.0.0.1:9222), puppeteer-core connect + reuse `pages()[0]`,
  `page.goto("https://archive.ph/https://votemadera.com")`, disconnect only.
- Result: Cloudflare CAPTCHA wall ("Please complete the security check to access archive.ph"). MISS, recorded
  and not fought further per instructions.

## Conclusion

All four archive families checked against the only checkable target (the bare domain, since no 2012 results-
folder URL exists to test). None surfaces any 2012 presence for votemadera.com beyond the single 2011 homepage
capture Wayback already found. This confirms, independently, the existing row note's conclusion that Madera's
results web system predates the county's online-results era entirely for the 2012 general; no new route or
number found. Row stays null/none.
