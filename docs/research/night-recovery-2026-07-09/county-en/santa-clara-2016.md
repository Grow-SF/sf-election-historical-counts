# Santa Clara County 2016-11-08: NewsBank recovery attempt (Task 3, step 1)

Existing row (`data/research/election-night/santa-clara-ca.json`, 2016-11-08):
`election_night_ballots: null`, `confidence: "none"`. Certified final (denominator,
CA SoS Voter Participation Statistics by County) = 724,596 ballots (190,379 poll +
534,217 VBM; 82.79% of 875,176 reg, record turnout). Clarity event 64404 numerator
routes are exhausted (only a pre-poll-close placeholder and a Nov 13 deep-canvass
version 183112 at 602,338 / 724,596 = 83.1% survive in Wayback); no county press
release or results PDF exists. Row flags no leads other than local news.

Calibration band (from the brief): adjacent clean points are 67.1% (2012) and the
62.26% next-day ceiling (2014); expect roughly 55-65% for a clean 2016 plateau
(~398k-471k ballots); anything near/above 83.1% (602,338) is canvass-contaminated;
anything near half of SF's 66.1% 2016 share (~33%, ~239k ballots) is the first
tranche.

Task 1 coverage probe (`00-newsbank-coverage.md`) confirmed: source string
`Mercury News, The (San Jose, CA)`, window 2016-11-09 to 2016-11-10, HIT (6)
articles for `alltext="ballots"`. Sample headline already captured: "COUNTING
CONTINUES ON MAIL BALLOTS - ELECTIONS OFFICIALS ESTIMATE 39 PERCENT OF VOTES
REMAIN UNTALLIED IN SANTA CLARA COUNTY" (Nov 9 2016) -- if genuinely about Santa
Clara County and dated to the Nov 9 morning-after edition describing the state as
of election night, "39 percent... remain untallied" implies ~61% counted, which is
within the calibration band and worth chasing first.

Interface: NewsBank Access World News via SFPL ezproxy
(`https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/`), driven via
puppeteer-core against the existing logged-in Chrome tab on debug port 9222
(reused in place, no new tab/window per the browser rules). NewsBank session is
free (Task 2 / Sacramento landed at e833dae before this task started).

## Searches run

(Appended as run.)

### Query: "ballots counted" Santa Clara
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=%22ballots%20counted%22%20Santa%20Clara&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Query: "ballots cast" county
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=%22ballots%20cast%22%20county&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Query: registrar of voters ballots
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=registrar%20of%20voters%20ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 1
- Items:
  - [news/160D491E5982E240] "Go to the document viewer for COUNTING CONTINUES ON MAIL BALLOTS - ELECTIONS OFFICIALS ESTIMATE 39 PERCENT OF VOTES REMAIN UNTALLIED IN SANTA CLARA COUNTY November 10, 2016 Mercury News, The (San Jose, CA) Sharon Noguchi"
  - [news/160D491E5982E240] (KWIC preview removed: licensed content; open the docref)

### Query: precincts reporting Santa Clara County
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=precincts%20reporting%20Santa%20Clara%20County&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: ballots
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 6
- Items:
  - [news/1608FF6CA843D4B0] "Go to the document viewer for RO KHANNA DEFEATS MIKE HONDA - RO KHANNA OUSTS INCUMBENT MIKE HONDA FOR 17TH CONGRESSIONAL DISTRICT SEAT. November 9, 2016 Mercury News, The (San Jose, CA) Eric Kurhi, ekurhi@bayareanewsgrou"
  - [news/1608FF6CA843D4B0] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491E5982E240] "Go to the document viewer for COUNTING CONTINUES ON MAIL BALLOTS - ELECTIONS OFFICIALS ESTIMATE 39 PERCENT OF VOTES REMAIN UNTALLIED IN SANTA CLARA COUNTY November 10, 2016 Mercury News, The (San Jose, CA) Sharon Noguchi"
  - [news/160D491E5982E240] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491EE056F9F8] "Go to the document viewer for DISTRICT 8 RACE FLIPS IN FAVOR OF ARENAS - HOPEFUL EMERGES 11 VOTES AHEAD OF OPPONENT NGUYEN November 10, 2016 Mercury News, The (San Jose, CA) Ramona Giwargis, rgiwargis@bayareanewsgroup.co"
  - [news/160D491EE056F9F8] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491ED9FA1DB0] "Go to the document viewer for KALRA LEADS RIVAL IN RACE FOR 27TH ASSEMBLY - IF COUNCILMAN HOLDS ADVANTAGE, HE'LL MAKE HISTORY IN LEGISLATURE November 10, 2016 Mercury News, The (San Jose, CA) Ramona Giwargis, rgiwargis@b"
  - [news/160D491ED9FA1DB0] (KWIC preview removed: licensed content; open the docref)
  - [news/16095334ABD1D5A0] "Go to the document viewer for CALIFORNIA, MUCH OF U.S. WORLDS APART November 10, 2016 Mercury News, The (San Jose, CA) Mercury News Editorial Board Page 14A Lexile: 1190, grade level(s): 10 11-12"
  - [news/16095334ABD1D5A0] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491DDE2B0D90] "Go to the document viewer for EXECUTION MEASURE FACES CHALLENGES - NO FUNDING INCLUDED FOR ATTORNEYS, JUDGES TO SPEED UP APPEALS November 10, 2016 Mercury News, The (San Jose, CA) Tracey Kaplan, tkaplan@bayareanewsgroup."
  - [news/160D491DDE2B0D90] (KWIC preview removed: licensed content; open the docref)

### Extended sweep query: Measure A Santa Clara County
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=Measure%20A%20Santa%20Clara%20County&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 6
- Items:
  - [news/1608FF6CE26E2DB0] "Go to the document viewer for TRANSIT SALES TAX MEASURE LEADING - MEASURE B WOULD GENERATE REVENUE FOR IMPROVEMENTS November 9, 2016 Mercury News, The (San Jose, CA) Tatiana Sanchez, tsanchez@bayareanewsgroup.com Page 6S"
  - [news/1608FF6CE26E2DB0] (KWIC preview removed: licensed content; open the docref)
  - [news/1608FF6D81BADB18] "Go to the document viewer for RESULTS November 9, 2016 Mercury News, The (San Jose, CA) Bay Area News Group Page 8S"
  - [news/1608FF6D81BADB18] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491E5982E240] "Go to the document viewer for COUNTING CONTINUES ON MAIL BALLOTS - ELECTIONS OFFICIALS ESTIMATE 39 PERCENT OF VOTES REMAIN UNTALLIED IN SANTA CLARA COUNTY November 10, 2016 Mercury News, The (San Jose, CA) Sharon Noguchi"
  - [news/160D491E5982E240] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491E473EFEE8] "Go to the document viewer for BAY AREA BIG BACKER OF POT PROPOSITION November 10, 2016 Mercury News, The (San Jose, CA) Lisa M. Krieger, lkrieger@bayareanewsgroup.com Page 12A Lexile: 1120, grade level(s): 9 10 11-12"
  - [news/160D491E473EFEE8] (KWIC preview removed: licensed content; open the docref)
  - [news/16095334ABD1D5A0] "Go to the document viewer for CALIFORNIA, MUCH OF U.S. WORLDS APART November 10, 2016 Mercury News, The (San Jose, CA) Mercury News Editorial Board Page 14A Lexile: 1190, grade level(s): 10 11-12"
  - [news/16095334ABD1D5A0] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491E407C9688] "Go to the document viewer for ELECTION 2016 RESULTS November 10, 2016 Mercury News, The (San Jose, CA) Bay Area News Group Page 13A"
  - [news/160D491E407C9688] (KWIC preview removed: licensed content; open the docref)

### Extended sweep query: Kalra Nguyen votes
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=Kalra%20Nguyen%20votes&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 5
- Items:
  - [news/1608FF6D81BADB18] "Go to the document viewer for RESULTS November 9, 2016 Mercury News, The (San Jose, CA) Bay Area News Group Page 8S"
  - [news/1608FF6D81BADB18] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491ED9FA1DB0] "Go to the document viewer for KALRA LEADS RIVAL IN RACE FOR 27TH ASSEMBLY - IF COUNCILMAN HOLDS ADVANTAGE, HE'LL MAKE HISTORY IN LEGISLATURE November 10, 2016 Mercury News, The (San Jose, CA) Ramona Giwargis, rgiwargis@b"
  - [news/160D491ED9FA1DB0] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491EE056F9F8] "Go to the document viewer for DISTRICT 8 RACE FLIPS IN FAVOR OF ARENAS - HOPEFUL EMERGES 11 VOTES AHEAD OF OPPONENT NGUYEN November 10, 2016 Mercury News, The (San Jose, CA) Ramona Giwargis, rgiwargis@bayareanewsgroup.co"
  - [news/160D491EE056F9F8] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491E5982E240] "Go to the document viewer for COUNTING CONTINUES ON MAIL BALLOTS - ELECTIONS OFFICIALS ESTIMATE 39 PERCENT OF VOTES REMAIN UNTALLIED IN SANTA CLARA COUNTY November 10, 2016 Mercury News, The (San Jose, CA) Sharon Noguchi"
  - [news/160D491E5982E240] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491E407C9688] "Go to the document viewer for ELECTION 2016 RESULTS November 10, 2016 Mercury News, The (San Jose, CA) Bay Area News Group Page 13A"
  - [news/160D491E407C9688] (KWIC preview removed: licensed content; open the docref)

### Extended sweep query: election night results Santa Clara
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=election%20night%20results%20Santa%20Clara&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 2
- Items:
  - [news/1608FF6D4BD57310] "Go to the document viewer for JIMENEZ, DAVIS, NGUYEN LEAD - TWO BUSINESS-BACKED, ONE LABOR-BACKED CANDIDATE IN FRONT AT CITY HALL November 9, 2016 Mercury News, The (San Jose, CA) Ramona Giwargis, rgiwargis@bayareanewsgr"
  - [news/1608FF6D4BD57310] (KWIC preview removed: licensed content; open the docref)
  - [news/160D491E164D6190] "Go to the document viewer for A SHELLSHOCKED BAY AREA REACTS November 10, 2016 Mercury News, The (San Jose, CA) Katy Murphy, Thomas Peele and Tatiana Sanchez, Staff Page 1A Lexile: 1260, grade level(s): 11-12"
  - [news/160D491E164D6190] (KWIC preview removed: licensed content; open the docref)

### Extended sweep query: semi-official Santa Clara
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=semi-official%20Santa%20Clara&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: countywide votes counted
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=countywide%20votes%20counted&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: Bushey ballots (range 11/08/2016 - 11/12/2016)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=Bushey%20ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F08%2F2016%20-%2011%2F12%2F2016&sort=YMD_date%3AA
- Result count: 1
- Items:
  - [news/160D491E5982E240] "Go to the document viewer for COUNTING CONTINUES ON MAIL BALLOTS - ELECTIONS OFFICIALS ESTIMATE 39 PERCENT OF VOTES REMAIN UNTALLIED IN SANTA CLARA COUNTY November 10, 2016 Mercury News, The (San Jose, CA) Sharon Noguchi"
  - [news/160D491E5982E240] (KWIC preview removed: licensed content; open the docref)

### Extended sweep query: "ballots have been counted" (range 11/08/2016 - 11/12/2016)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=%22ballots%20have%20been%20counted%22&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F08%2F2016%20-%2011%2F12%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: "final tally" Santa Clara (range 11/08/2016 - 11/12/2016)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=%22final%20tally%22%20Santa%20Clara&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F08%2F2016%20-%2011%2F12%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: overnight count Santa Clara (range 11/08/2016 - 11/12/2016)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=overnight%20count%20Santa%20Clara&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F08%2F2016%20-%2011%2F12%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

## Outcome

Landed as a documented FLOOR (RUNBOOK 5.2), confidence secondary, verdict
PLAUSIBLE (plateau_review.json): 303,678 ballots / 724,596 certified = 41.91%,
from the Nov 9, 2016 Mercury News "RESULTS" page (docref news/1608FF6D81BADB18,
Measure A + Measure B same-contest ratio at 41% of precincts). The
"COUNTING CONTINUES ON MAIL BALLOTS" article (docref news/160D491E5982E240)
supplies corroborating (not adopted) context: officials' rough post-night
estimate of ~61% counted "as of Wednesday afternoon". True plateau likely
sits in the brief's 55-65% calibration band, between these two points, but
is not more precisely recoverable from this paper. Committed at f9fc42a
(data: Santa Clara 2016 election-night plateau floor from Mercury News).
