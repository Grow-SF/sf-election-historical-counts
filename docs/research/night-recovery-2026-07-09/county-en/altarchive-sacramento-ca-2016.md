# Task 8: alternate web-archive sweep -- sacramento-ca 2016-11-08

Target URLs (from the row's own dead-end note, Wayback-missed live-results hosts):
- `http://www.eresults.saccounty.net/` (Hart SUMMARY REPORT embed)
- `http://sacresults.e-cers.com/` (live e-cers app homepage)
- `http://sacresults.e-cers.com/resultsVoterTurnout.aspx` (the AJAX turnout total)

## Run 1 (2026-07-09): Library of Congress United States Elections Web Archive

- `curl -A <chrome-UA> --compressed "https://webarchive.loc.gov/all/20161101000000-20161201000000/http://www.eresults.saccounty.net/"` -> HTTP 403, Cloudflare "Just a moment..." managed challenge page (`cf-mitigated: challenge`).
- Repeated against `https://webarchive.loc.gov/all/*/http://www.eresults.saccounty.net/`, the bare homepage `https://webarchive.loc.gov/`, and `https://webarchive.loc.gov/robots.txt` -- all HTTP 403, same Cloudflare JS challenge (`server: cloudflare`, `cf-ray` present, requires WebCrypto to solve, `content-security-policy` locked to `challenges.cloudflare.com`). This is a domain-wide bot wall, not URL-specific; confirmed once here and treated as established for all six Task 8 rows rather than re-run per URL.
- MISS (bot wall, curl-unsolvable; not browser-authorized for this family per the brief).

## Run 1: Common Crawl

- Bracketing crawls per brief: `CC-MAIN-2016-44` (Oct 2016) and `CC-MAIN-2016-50` (Dec 2016).
- `curl "https://index.commoncrawl.org/CC-MAIN-2016-44-index?url=http%3A%2F%2Fwww.eresults.saccounty.net%2F&output=json"` -> HIT: timestamp `20161027104751`, url `https://eresults.saccounty.net/`, offset 827247490 len 5764, file `crawl-data/CC-MAIN-2016-44/segments/1476988721268.95/warc/CC-MAIN-20161020183841-00327-ip-10-171-6-4.ec2.internal.warc.gz`.
- `curl "https://index.commoncrawl.org/CC-MAIN-2016-50-index?url=...&output=json"` -> HIT: timestamp `20161209230435` (=fetched from crawl segment `CC-MAIN-2016-50/.../CC-MAIN-20161202170902-00302...`), offset 845973089 len 9398.
- WARC range-fetched both (`curl -r <offset>-<offset+len-1> https://data.commoncrawl.org/<file> | gunzip`):
  - Oct 27 capture: embedded Hart report `RUN DATE:10/21/16 RUN TIME:10:11 AM`, `PRECINCTS COUNTED (OF 1267) 0`, `BALLOTS CAST - TOTAL 0` -- the pre-election zero/test run, same class as the 20161107220729 Wayback capture already documented.
  - Dec 9 capture: embedded report `RUN DATE:12/05/16 RUN TIME:03:54 PM`, `PRECINCTS COUNTED (OF 1267) 1,267 100.00`, `BALLOTS CAST - TOTAL 575,711` -- this EXACTLY equals the certified final (575,711, CA SoS SOV), i.e. this is the CERTIFIED-FINAL state, not the election-night plateau. Both CC crawls landed outside the Nov 8-9 election-night window (one before, one at certification), same trap the row's note already describes for the two bracketing Wayback captures.
- `sacresults.e-cers.com/` homepage: HIT in both crawls -- Oct 26 (`Precincts Reporting: 0/1267`, `Last Refresh: 10/25/2016 6:26:29 AM`, pre-election) and Dec 2 (`Precincts Reporting: 1267/1267`, `Last Refresh: 11/28/2016 2:34:52 PM` -- a Nov 28 canvass-period state, 20 days post-night).
- `sacresults.e-cers.com/resultsVoterTurnout.aspx`: HIT only in CC-MAIN-2016-50 (`20161202180118`). Fetched: `Last Refresh: 11/28/2016 2:34:52 PM`, Countywide `70.65%`, Voter Turnout 545,963 / Registered Voters 772,777 -- again the Nov 28 canvass state (545,963/575,711 = 94.8% of certified), not election night. No capture of this URL exists in the Oct crawl (the AJAX page apparently 404'd or wasn't linked pre-election).
- No Common Crawl capture of either site in the actual Nov 8-9, 2016 election-night window. MISS for the plateau (real hits found, but both bracketing crawls' timestamps land off-window: one pre-election zero-run, one post-canvass/certified).

## Run 1: Archive-It (CDL California collections)

- `curl --compressed "https://wayback.archive-it.org/all/timemap/link/http://www.eresults.saccounty.net/"` and the `sacresults.e-cers.com/` equivalent -> HTTP 200 body is Archive-It's own "Session Verification" bot-challenge page (client-side SHA-256 proof-of-work requiring WebCrypto, POST to `archive-it.org/_challenge`), not a timemap. Same wall observed on every URL tried across all six rows (see Run 1 notes on the other county files); established once as domain-wide.
- MISS (bot wall, curl-unsolvable; the puzzle is JS-only in practice and not worth solving per "do not fight it").

## Run 1: archive.today

- Debug-port Chrome (127.0.0.1:9222), puppeteer-core connect + reuse `pages()[0]`, `page.goto("https://archive.ph/https://www.eresults.saccounty.net")`, disconnect only (per the brief's ABSOLUTE rules).
- Result: archive.ph served a Cloudflare CAPTCHA wall ("Please complete the security check to access archive.ph"), not a capture list.
- MISS (bot wall). Per instructions, recorded and not fought further.

## Conclusion

All four archive families checked; none surfaces an election-night-window (Nov 8-9, 2016) snapshot of eresults.saccounty.net or sacresults.e-cers.com beyond what NewsBank/Wayback/enumeration passes already found and exhausted. Row stays null/none. See the county JSON's own note for the full existing exhaustion record (press release, eresults, e-cers, NewsBank Sacramento Bee, CivicPlus/Twitter enumeration); this pass adds no new number.
