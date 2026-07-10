# Santa Clara County 2018-11-06: NewsBank recovery attempt (Task 3, step 2)

Existing row (`data/research/election-night/santa-clara-ca.json`, 2018-11-06):
`election_night_ballots: null`, `confidence: "none"`. Certified final (denominator,
CA SoS Voter Participation Statistics by County) = 625,425 ballots (138,468 poll +
486,957 VBM; 70.61% of 885,764 reg). Clarity event 92418 numerator routes are
exhausted: the earliest archived JSON is version 221262 (captured 2018-11-12),
GOVERNOR BC = 443,266 at 1,098/1,098 precincts, electionsettings '11/11/2018
4:43:32 PM PST' -- a DEEP CANVASS count 5 days post-election, 443,266/625,425 =
70.9%, NOT the plateau. The county's own official Post-Election Report gives only
the certified final, no election-night count. No press release with a ballot
total exists.

Calibration band (from the brief): the row's note establishes 70.9% (443,266) is a
deep-canvass ceiling, well above any legitimate plateau; expect a midterm plateau
in the 50s-60s (roughly 313k-407k ballots), by analogy to Napa 2018 (38.11%, first
VCA year) and San Mateo 2018 (38.49%, also first VCA year) being much lower due to
the Voter's Choice Act shift -- but Santa Clara did NOT adopt VCA/e-pollbooks until
2020, so 2018 should still look like a traditional pre-VCA county, closer to the
2014 62.26% ceiling / 2012 67.1% than to the VCA counties.

Task 1 coverage probe (`00-newsbank-coverage.md`) confirmed: source string
`Mercury News, The (San Jose, CA)`, window 2018-11-07 to 2018-11-08, HIT (7)
articles for `alltext="ballots"`. Sample headline was scrubbed in the coverage
probe (licensed-content cleanup); re-pull it during this pass if a good one turns
up, but do not hunt for it separately.

Interface: NewsBank Access World News via SFPL ezproxy, same session as the 2016
pass (this task's step 2, run immediately after step 1 in the same browser
session).

## Searches run

(Appended as run.)

### Query: "ballots counted" Santa Clara
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=%22ballots%20counted%22%20Santa%20Clara&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Query: "ballots cast" county
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=%22ballots%20cast%22%20county&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Query: registrar of voters ballots
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=registrar%20of%20voters%20ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 1
- Items:
  - [news/16F946169D59A048] "Go to the document viewer for WHY BAY AREA COUNTIES STILL HAVE SO MANY VOTES TO COUNT - AS MORE VOTERS TURN TO MAIL-IN BALLOTS IN CALIFORNIA, RESULTS ARE TAKING LONGER TO COUNT THAN IN PREVIOUS YEARS, ELECTIONS STAFF AND"
  - [news/16F946169D59A048] (KWIC preview removed: licensed content; open the docref)

### Query: precincts reporting Santa Clara County
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=precincts%20reporting%20Santa%20Clara%20County&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: ballots
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 7
- Items:
  - [news/16F8F1C37B289B88] "Go to the document viewer for ‘GOOGLE TAX' AND POT TAX ARE OUT IN FRONT November 7, 2018 Mercury News, The (San Jose, CA) Khalida Sarwari and Kevin Kelly, Staff writers Page 6A Lexile: 1610, grade level(s): >12"
  - [news/16F8F1C37B289B88] (KWIC preview removed: licensed content; open the docref)
  - [news/16F8F1C35E8A9A80] "Go to the document viewer for STRONG SUPPORT FOR BOND TO FIX ROADS, BRIDGES November 7, 2018 Mercury News, The (San Jose, CA) Emily Deruy, ederuy@bayareanewsgroup.com Page 6A Lexile: 1350, grade level(s): >12"
  - [news/16F8F1C35E8A9A80] (KWIC preview removed: licensed content; open the docref)
  - [news/16F946169D59A048] "Go to the document viewer for WHY BAY AREA COUNTIES STILL HAVE SO MANY VOTES TO COUNT - AS MORE VOTERS TURN TO MAIL-IN BALLOTS IN CALIFORNIA, RESULTS ARE TAKING LONGER TO COUNT THAN IN PREVIOUS YEARS, ELECTIONS STAFF AND"
  - [news/16F946169D59A048] (KWIC preview removed: licensed content; open the docref)
  - [news/16F94616A43CA450] "Go to the document viewer for HOW TO SOLVE THE BAY AREA'S HOUSING CRISIS November 8, 2018 Mercury News, The (San Jose, CA) Editorial Board Page 10A Lexile: 1450, grade level(s): >12"
  - [news/16F94616A43CA450] (KWIC preview removed: licensed content; open the docref)
  - [news/16F94616B9AF0760] "Go to the document viewer for HOUSING CRISIS SOLUTION ELUSIVE - TENANTS' RIGHTS ADVOCATES WANT MORATORIUM ON RENT INCREASES November 8, 2018 Mercury News, The (San Jose, CA) Katy Murphy, kmurphy@bayareanewsgroup.com Page"
  - [news/16F94616B9AF0760] (KWIC preview removed: licensed content; open the docref)
  - [news/16F94616B29C0630] "Go to the document viewer for VOTERS WANT TO KEEP DAYLIGHT SAVING TIME - LAWMAKER BEHIND INITIATIVE THINKS IT WILL CLEAR FEDERAL HURDLES November 8, 2018 Mercury News, The (San Jose, CA) John Woolfolk, jwoolfolk@bayarean"
  - [news/16F94616B29C0630] (KWIC preview removed: licensed content; open the docref)

### Extended sweep query: Measure B Santa Clara County
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=Measure%20B%20Santa%20Clara%20County&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: election night results Santa Clara
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=election%20night%20results%20Santa%20Clara&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: semi-official Santa Clara
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=semi-official%20Santa%20Clara&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: countywide votes counted
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=countywide%20votes%20counted&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: results
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=results&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 11
- Items:
  - [news/16F8F1C37B289B88] "Go to the document viewer for ‘GOOGLE TAX' AND POT TAX ARE OUT IN FRONT November 7, 2018 Mercury News, The (San Jose, CA) Khalida Sarwari and Kevin Kelly, Staff writers Page 6A Lexile: 1610, grade level(s): >12"
  - [news/16F8F1C37B289B88] (KWIC preview removed: licensed content; open the docref)
  - [news/16F8F1C38DE34C40] "Go to the document viewer for MORE INSIDE November 7, 2018 Mercury News, The (San Jose, CA) Bay Area News Group Page 1A Lexile: 1540, grade level(s): >12"
  - [news/16F8F1C38DE34C40] (KWIC preview removed: licensed content; open the docref)
  - [news/16F8F1C374384940] "Go to the document viewer for STATE VOTERS SOUNDLY REJECTING PROP. 6 IN BID TO KEEP FUNDS FOR ROADS November 7, 2018 Mercury News, The (San Jose, CA) Erin Baldassari, ebaldassari@bayareanewsgroup.com Page 1A Lexile: 1580"
  - [news/16F8F1C374384940] (KWIC preview removed: licensed content; open the docref)
  - [news/16F8F1C3AB785778] "Go to the document viewer for CALIFORNIA HANDS A SOLID DEFEAT TO PROPOSITION 10; PROPONENTS OUTSPENT 3-1 November 7, 2018 Mercury News, The (San Jose, CA) Katy Murphy, kmurphy@bayareanewsgroup.com Page 1A Lexile: 1560, g"
  - [news/16F8F1C3AB785778] (KWIC preview removed: licensed content; open the docref)
  - [news/16F8F1C309391D50] "Go to the document viewer for DEMS CAPTURE HOUSE; NEWSOM SAILS TO WIN - DEMOCRATS ADD TO THEIR MAJORITY IN STATE, WREST CONTROL OF HOUSE November 7, 2018 Mercury News, The (San Jose, CA) Casey Tolan, ctolan@bayareanewsgr"
  - [news/16F8F1C309391D50] (KWIC preview removed: licensed content; open the docref)
  - [news/16F94616A43CA450] "Go to the document viewer for HOW TO SOLVE THE BAY AREA'S HOUSING CRISIS November 8, 2018 Mercury News, The (San Jose, CA) Editorial Board Page 10A Lexile: 1450, grade level(s): >12"
  - [news/16F94616A43CA450] (KWIC preview removed: licensed content; open the docref)

### Extended sweep query: "of precincts" Santa Clara (range 11/07/2018 - 11/09/2018)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=%22of%20precincts%22%20Santa%20Clara&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F09%2F2018&sort=YMD_date%3AA
- Result count: 1
- Items:
  - [news/16FA96F533667668] "Go to the document viewer for TIME TO GET OVER OUR VOTING-BOOTH NOSTALGIA November 9, 2018 Mercury News, The (San Jose, CA) Daniel Borenstein, dborenstein@bayareanewsgroup.com Page 8A Lexile: 1150, grade level(s): 9 10 1"
  - [news/16FA96F533667668] (KWIC preview removed: licensed content; open the docref)

### Extended sweep query: Measure T Measure V votes (range 11/07/2018 - 11/09/2018)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=Measure%20T%20Measure%20V%20votes&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F09%2F2018&sort=YMD_date%3AA
- Result count: 2
- Items:
  - [news/16F8F1C35E8A9A80] "Go to the document viewer for STRONG SUPPORT FOR BOND TO FIX ROADS, BRIDGES November 7, 2018 Mercury News, The (San Jose, CA) Emily Deruy, ederuy@bayareanewsgroup.com Page 6A Lexile: 1350, grade level(s): >12"
  - [news/16F8F1C35E8A9A80] (KWIC preview removed: licensed content; open the docref)
  - [news/16FA96F517D549B0] "Go to the document viewer for BRISBANE VOTERS SAW THE HANDWRITING ON THE BAYLANDS WALL November 9, 2018 Mercury News, The (San Jose, CA) John Horgan, Correspondent Page 8B Lexile: 1160, grade level(s): 10 11-12"
  - [news/16FA96F517D549B0] (KWIC preview removed: licensed content; open the docref)

### Extended sweep query: title:RESULTS (range 11/07/2018 - 11/09/2018)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=title%3ARESULTS&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F09%2F2018&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Title-field sweep: ti="results" (range 11/07/2018 - 11/08/2018)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=ti&val-base-0=results&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Title-field sweep: ti="election results" (range 11/07/2018 - 11/09/2018)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=ti&val-base-0=election%20results&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F09%2F2018&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

## Outcome

Landed as a documented CEILING (RUNBOOK 5.2), comparable:false, confidence
secondary, verdict PLAUSIBLE (plateau_review.json): 304,000 ballots / 625,425
certified = 48.61%, from Sciacca and Geha's Nov 8, 2018 Mercury News article
(docref news/16F946169D59A048), "As of Wednesday afternoon, about 304,000
ballots were counted" (Registrar Shannon Bushey). This tightens the row's
prior known deep-canvass ceiling (443,266 / 70.9%, five days post-election)
to about one day post-election, corroborated by Borenstein's Nov 9 op-ed
(docref news/16FA96F533667668) citing "about 47 percent remaining" as of
Thursday morning. No same-contest ratio floor (as used for the 2016 row) was
recoverable: no Mercury News tabular results page was found for this
election in the Nov 7-9 window. True plateau likely sits in the high-40s to
low-50s, short of the brief's 50s-60s midterm expectation, since the tightest
available number is itself already a post-night ceiling. Committed at
952e430 (data: Santa Clara 2018 election-night plateau ceiling from Mercury
News), corrected for a shared-file leak at 6c71813.
