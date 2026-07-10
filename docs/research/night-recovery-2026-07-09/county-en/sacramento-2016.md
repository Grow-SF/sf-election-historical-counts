# Sacramento County 2016-11-08: NewsBank recovery attempt (Task 2)

Existing row (`data/research/election-night/sacramento-ca.json`, 2016-11-08):
denominator (certified final) = 575,711; Friday 11/11 canvass upper bound =
385,520 (66.96%, NOT the metric); expected plateau band by analogy to the
clean 2012 presidential plateau (62.93%) = roughly 60-63% i.e. ~345k-363k
ballots. All Wayback/press-release/e-cers routes previously exhausted; the
row flags the Sacramento Bee as the most likely recovery source.

Task 1 coverage probe (`00-newsbank-coverage.md`) confirmed: source string
`Sacramento Bee, The (CA)`, window 2016-11-09 to 2016-11-10, HIT (8) articles
for `alltext="ballots"`.

Interface: NewsBank Access World News via SFPL ezproxy
(`https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/`), driven via
puppeteer-core against the existing logged-in Chrome tab on debug port 9222
(reused in place, no new tab/window per the browser rules).

## Searches run

(Appended as run.)

### Query: "ballots counted"
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=%22ballots%20counted%22&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Query: "ballots cast"
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=%22ballots%20cast%22&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 1
- Items:
  - [news/160AF31155E01CE8] "Go to the document viewer for THE BUZZ November 10, 2016 Sacramento Bee, The (CA) Dan Smith, Jim Miller; Staff Writer Page 8A Lexile: 1330, grade level(s): >12"
  - [news/160AF31155E01CE8] (KWIC preview removed: licensed content; open the docref)

### Query: "votes counted" election night
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=%22votes%20counted%22%20election%20night&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Query: LaVine ballots
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=LaVine%20ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 1
- Items:
  - [news/160AF30E34506520] "Go to the document viewer for School measures prevail - except city parcel tax November 10, 2016 Sacramento Bee, The (CA) Loretta Kalb; Staff Writer Page 3A Lexile: 1370, grade level(s): >12"
  - [news/160AF30E34506520] (KWIC preview removed: licensed content; open the docref)

### Query: turnout Sacramento County
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=turnout%20Sacramento%20County&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 2
- Items:
  - [news/160AF3095FA30F60] "Go to the document viewer for HOUSE, 7TH DISTRICT - Bera leads Sheriff Jones in bid to keep House seat November 9, 2016 Sacramento Bee, The (CA) Christopher Cadelago; Staff Writer Page 3A Lexile: 1370, grade level(s): >1"
  - [news/160AF3095FA30F60] (KWIC preview removed: licensed content; open the docref)
  - [news/160AF31155E01CE8] "Go to the document viewer for THE BUZZ November 10, 2016 Sacramento Bee, The (CA) Dan Smith, Jim Miller; Staff Writer Page 8A Lexile: 1330, grade level(s): >12"
  - [news/160AF31155E01CE8] (KWIC preview removed: licensed content; open the docref)

### Query: precincts reporting Sacramento County
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=precincts%20reporting%20Sacramento%20County&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found on results page.

### Extended sweep query: semi-official Sacramento (range 11/09/2016 - 11/17/2016)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=semi-official%20Sacramento&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F17%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found.

### Extended sweep query: unofficial results Sacramento County (range 11/09/2016 - 11/17/2016)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=unofficial%20results%20Sacramento%20County&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F17%2F2016&sort=YMD_date%3AA
- Result count: 0
- No document-view items found.

### Extended sweep query: LaVine (range 11/09/2016 - 11/17/2016)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=LaVine&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F17%2F2016&sort=YMD_date%3AA
- Result count: 1
- Items:
  - [news/160AF30E34506520] "Go to the document viewer for School measures prevail - except city parcel tax November 10, 2016 Sacramento Bee, The (CA) Loretta Kalb; Staff Writer Page 3A Lexile: 1370, grade level(s): >12"
  - [news/160AF30E34506520] (KWIC preview removed: licensed content; open the docref)

### Extended sweep query: registrar ballots counted (range 11/09/2016 - 11/17/2016)
- URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=registrar%20ballots%20counted&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F17%2F2016&sort=YMD_date%3AA
- Result count: 4
- Items:
  - [news/160AF31155E01CE8] "Go to the document viewer for THE BUZZ November 10, 2016 Sacramento Bee, The (CA) Dan Smith, Jim Miller; Staff Writer Page 8A Lexile: 1330, grade level(s): >12"
  - [news/160AF31155E01CE8] (KWIC preview removed: licensed content; open the docref)
  - [news/160AF30D446FD958] "Go to the document viewer for Bera, Jones chipper as House race nail-biter drags on November 10, 2016 Sacramento Bee, The (CA) Alexei Koseff; Staff Writer Page 9A Lexile: 1150, grade level(s): 9 10 11-12"
  - [news/160AF30D446FD958] (KWIC preview removed: licensed content; open the docref)
  - [news/160AF30E34506520] "Go to the document viewer for School measures prevail - except city parcel tax November 10, 2016 Sacramento Bee, The (CA) Loretta Kalb; Staff Writer Page 3A Lexile: 1370, grade level(s): >12"
  - [news/160AF30E34506520] (KWIC preview removed: licensed content; open the docref)
  - [news/160B9E00F42AD3F0] "Go to the document viewer for THE NUMBERS CRUNCH - Sacramento can brag a little about its local elections November 12, 2016 Sacramento Bee, The (CA) Foon Rhee; Staff Writer Page 5B Lexile: 1260, grade level(s): 11-12"
  - [news/160B9E00F42AD3F0] (KWIC preview removed: licensed content; open the docref)
