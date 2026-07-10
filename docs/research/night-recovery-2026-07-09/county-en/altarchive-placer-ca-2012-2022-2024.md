# Task 8: alternate web-archive sweep -- placer-ca 2012-11-06, 2022-11-08, 2024-11-05

Target URLs (from each row's own dead-end note):
- 2012: `www.placerelections.com/election-night-results.aspx` (GEMS live-results page).
- 2022 and 2024: `placercountyelections.gov/election-results/` (the in-place-updated GEMS/Dominion summary
  page, formerly `placerelections.com/election-night-results/`).

## Run 1 (2026-07-09): Library of Congress United States Elections Web Archive

- Same domain-wide Cloudflare JS-challenge wall confirmed on webarchive.loc.gov (see sacramento-ca-2016 Run 1);
  MISS for all three rows.

## Run 1: Common Crawl

### 2012 (`www.placerelections.com/election-night-results.aspx`)
- Crawls checked: `CC-MAIN-2012` (2012-01-27..2012-06-05, entirely pre-election so structurally moot),
  `CC-MAIN-2013-20` (2013-05-18..06-20), `CC-MAIN-2013-48` (2013-12-04..12-22, request errored with a
  connection-reset after several retries; not recovered, treated as inconclusive/no-hit for that one crawl).
- `CC-MAIN-2013-20` HIT: timestamp `20130521145158`, offset 663417691 len 10580, file
  `crawl-data/CC-MAIN-2013-20/segments/1368700107557/warc/CC-MAIN-20130516102827-00038-...warc.gz`. WARC
  range-fetched and read: the embedded report header is `PLACER COUNTY OFFICIAL ELECTION SUMMARY / January 8,
  2013 / FINAL`, `Registered Voters 88120 - Cards Cast 22644 25.70%`, `81` precincts. This is a DIFFERENT,
  much smaller Placer election (a Jan 8, 2013 special/local ballot, 81 precincts vs. the Nov 2012 general's
  ~350 precincts and 172,757 certified) -- the live page had simply been overwritten for the next election by
  the time this crawl ran. Not usable; confirms the URL is in-place-overwritten and CC's one hit lands on the
  wrong contest entirely.
- No capture of the actual Nov 6, 2012 general on this URL in any crawl checked. MISS.

### 2022 and 2024 (`placercountyelections.gov/election-results/`)
- Crawls checked: `CC-MAIN-2022-40`, `CC-MAIN-2022-49` (2022 bracket); `CC-MAIN-2024-42`, `CC-MAIN-2024-46`,
  `CC-MAIN-2024-51` (2024 bracket), both with and without trailing slash.
- Every query returned `{"message": "No Captures found for: https://www.placercountyelections.gov/election-results[/]"}` (404). Common Crawl never crawled this URL in any of the five crawls tried. MISS for both rows.

## Run 1: Archive-It (CDL California collections)

- `curl --compressed "https://wayback.archive-it.org/all/timemap/link/<url>"` for both
  `www.placerelections.com/election-night-results.aspx` and `www.placercountyelections.gov/election-results/`
  -> Archive-It's "Session Verification" SHA-256 proof-of-work bot-challenge page, same as every other row.
  MISS (bot wall, curl-unsolvable) for all three rows.

## Run 1: archive.today

- Debug-port Chrome (127.0.0.1:9222), puppeteer-core connect + reuse `pages()[0]`, disconnect only, tested:
  - `https://archive.ph/https://www.placerelections.com/election-night-results.aspx` (2012)
  - `https://archive.ph/https://www.placercountyelections.gov/election-results/` (2022 and 2024, same URL)
- Both returned the Cloudflare CAPTCHA wall. MISS for all three rows, recorded and not fought further.

## Conclusion

All four archive families checked for all three Placer rows. No election-night-window capture surfaces beyond
what each row's own note already exhausted (2012: GEMS page overwritten pre-Dec-1; 2022/2024: the VCA-era
results page was never crawled during the relevant canvass windows by Wayback, and Common Crawl/Archive-It/LoC/
archive.today add nothing new -- the one Common Crawl hit found lands on an unrelated Jan 2013 special
election, not the Nov 2012 general). All three rows stay null/none.
