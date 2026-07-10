# NewsBank Access World News coverage probe (county election-night papers)

Task 1 of the county election-night research program (2026-07-09). Purpose: a
go/no-go per paper x election-year cell that Tasks 2-7 read before running
their own NewsBank searches, so they skip cells already known to be empty.

## Methodology

- Interface: NewsBank Access World News, SFPL ezproxy
  (`https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/`), driven via
  puppeteer-core against a live logged-in Chrome on debug port 9222 (session
  bring-up done by the controller before this task started; not repeated here).
- **Source identification**: each paper was first looked up in the A-Z Source
  List (`apps/news/source-list?p=WORLDNEWS`, typed into the client-side name
  filter) to get its exact NewsBank source string and confirm it exists at
  all. Every paper below has a "Newspaper / Text" source variant (as opposed
  to Image, Blog, Web-Only, or a modern "Today's Edition" image variant); the
  Text variant is what full-text search covers and is the one recorded and
  used for the coverage query.
- **Coverage query**: one broad advanced search per cell, namely
  `alltext="ballots" AND source=<exact source string> AND YMD_date=<window>`,
  restricted to `Source type = Newspaper` (the AWN facet param
  `t=stp:Newspaper!Newspaper`) to exclude the paper's Blog/Web-Only variants
  which otherwise match on the same source-name substring.
- **Window**: for each needed date `D` (the brief's "day after the election"),
  the search date range is `D` to `D+1` (i.e. day-after through 2-days-after
  the election). This D-to-D+1 superset window was the implementer's choice,
  not something specified by the brief (which lists single day-after dates
  only): querying a 2-day range reduces the risk of a false MISS caused by a
  same-day indexing lag or an off-by-one date-boundary effect in the search
  index.
- **Verdicts**:
  - `HIT (n)` : paper exists as a source, search returns n>0 articles in the
    window; 1-2 promising headlines recorded (no article bodies saved, per
    licensed-content rules).
  - `MISS-empty-window` : paper exists as a source (confirmed in A-Z list)
    but the windowed query returns 0 articles.
  - `MISS-no-source` : paper does not appear in the A-Z source list at all.
    (Not expected to occur here; all 7 papers were confirmed present before
    probing cells : see Source registry below.)
- Auth-wall check: every search checks the page title/text for "Articles and
  Databases" / "Authentication" before recording a result; none fired during
  this run.
- Politeness: ~2-3s between searches (shared NewsBank session).
- Note on cell count: the brief's own table lists 21 paper x window cells (not
  the 16 mentioned in the task summary line); this file follows the brief's
  table verbatim and so covers all 21.

## Source registry (exact NewsBank source strings, Text variant)

| paper (brief's name) | exact NewsBank source name | Text coverage dates |
|---|---|---|
| Sacramento Bee | Sacramento Bee, The (CA) | 1984 - Current |
| San Jose Mercury News | Mercury News, The (San Jose, CA) | 1985 - Current |
| Fresno Bee | Fresno Bee, The (CA) | 1986 - Current |
| Madera Tribune | Madera Tribune (CA) | 2002 - Current |
| San Diego Union-Tribune | San Diego Union-Tribune, The (CA) | 1983 - Current |
| Press-Enterprise (Riverside) | Press-Enterprise, The (Riverside, CA) | 1992 - Current |
| San Bernardino Sun | Sun, The (San Bernardino, CA) | 2001 - Current |

All 7 papers exist in the A-Z Source List with a Newspaper/Text variant
whose date range covers every needed window (2012-2022) -> no
`MISS-no-source` verdicts expected; each cell below is still probed
individually to confirm the window itself has hits.

## Per-cell results

(Appended as probed; each row is one search.)


### Sacramento Bee : window 2016-11-09 (search range 11/09/2016 - 11/10/2016)
- Source: `Sacramento Bee, The (CA)`
- Verdict: **HIT (8)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Sacramento%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for Sacramento County sales tax for transit just shy of passing in early returns November 9, 2016 Sacramento Bee, The (CA) Tony Bizjak"

### San Jose Mercury News : window 2016-11-09 (search range 11/09/2016 - 11/10/2016)
- Source: `Mercury News, The (San Jose, CA)`
- Verdict: **HIT (6)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for COUNTING CONTINUES ON MAIL BALLOTS - ELECTIONS OFFICIALS ESTIMATE 39 PERCENT OF VOTES REMAIN UNTALLIED IN SANTA CLARA COUNTY Novem"

### San Jose Mercury News : window 2018-11-07 (search range 11/07/2018 - 11/08/2018)
- Source: `Mercury News, The (San Jose, CA)`
- Verdict: **HIT (7)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Mercury%20News%2C%20The%20(San%20Jose%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Sample headlines:
  - (headline not captured; KWIC body-text snippet removed: licensed content. Re-pull the headline from the Query URL if needed.)

### Fresno Bee : window 2012-11-07 (search range 11/07/2012 - 11/08/2012)
- Source: `Fresno Bee, The (CA)`
- Verdict: **HIT (14)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Fresno%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2012%20-%2011%2F08%2F2012&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for Valley voters turn out in droves - In Tulare County, voting was extended till voters in line were able to cast their ballots. Nove"
  - (a KWIC body-text snippet was removed from this cell: licensed content)

### Fresno Bee : window 2014-11-05 (search range 11/05/2014 - 11/06/2014)
- Source: `Fresno Bee, The (CA)`
- Verdict: **HIT (17)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Fresno%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F05%2F2014%20-%2011%2F06%2F2014&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for Brown wins; voter turnout is low November 5, 2014 Fresno Bee, The (CA) The Fresno Bee Page A1 Lexile: 1410, grade level(s): >12"
  - (a KWIC body-text snippet was removed from this cell: licensed content)

### Fresno Bee : window 2018-11-07 (search range 11/07/2018 - 11/08/2018)
- Source: `Fresno Bee, The (CA)`
- Verdict: **HIT (31)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Fresno%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Sample headlines:
  - (headline not captured; KWIC body-text snippet removed: licensed content. Re-pull the headline from the Query URL if needed.)

### Fresno Bee : window 2022-11-09 (search range 11/09/2022 - 11/10/2022)
- Source: `Fresno Bee, The (CA)`
- Verdict: **HIT (43)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Fresno%20Bee%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2022%20-%2011%2F10%2F2022&sort=YMD_date%3AA
- Sample headlines:
  - (headline not captured; KWIC body-text snippet removed: licensed content. Re-pull the headline from the Query URL if needed.)

### Madera Tribune : window 2012-11-07 (search range 11/07/2012 - 11/08/2012)
- Source: `Madera Tribune (CA)`
- Verdict: **MISS-empty-window**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Madera%20Tribune%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2012%20-%2011%2F08%2F2012&sort=YMD_date%3AA

### Madera Tribune : window 2014-11-05 (search range 11/05/2014 - 11/06/2014)
- Source: `Madera Tribune (CA)`
- Verdict: **HIT (1)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Madera%20Tribune%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F05%2F2014%20-%2011%2F06%2F2014&sort=YMD_date%3AA
- Sample headlines:
  - (headline not captured; KWIC body-text snippet removed: licensed content. Re-pull the headline from the Query URL if needed.)

### San Diego Union-Tribune : window 2012-11-07 (search range 11/07/2012 - 11/08/2012)
- Source: `San Diego Union-Tribune, The (CA)`
- Verdict: **MISS-empty-window**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=San%20Diego%20Union-Tribune%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2012%20-%2011%2F08%2F2012&sort=YMD_date%3AA

### San Diego Union-Tribune : window 2014-11-05 (search range 11/05/2014 - 11/06/2014)
- Source: `San Diego Union-Tribune, The (CA)`
- Verdict: **MISS-empty-window**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=San%20Diego%20Union-Tribune%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F05%2F2014%20-%2011%2F06%2F2014&sort=YMD_date%3AA

### San Diego Union-Tribune : window 2016-11-09 (search range 11/09/2016 - 11/10/2016)
- Source: `San Diego Union-Tribune, The (CA)`
- Verdict: **HIT (27)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=San%20Diego%20Union-Tribune%2C%20The%20(CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Sample headlines:
  - (headline not captured; KWIC body-text snippet removed: licensed content. Re-pull the headline from the Query URL if needed.)

### Press-Enterprise (Riverside) : window 2012-11-07 (search range 11/07/2012 - 11/08/2012)
- Source: `Press-Enterprise, The (Riverside, CA)`
- Verdict: **HIT (15)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Press-Enterprise%2C%20The%20(Riverside%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2012%20-%2011%2F08%2F2012&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for Hemet, SJ races close November 7, 2012 Press-Enterprise, The (Riverside, CA) DARRELL SANTSCHI AND GAIL WESSON STAFF WRITERS DSANTS"

### Press-Enterprise (Riverside) : window 2014-11-05 (search range 11/05/2014 - 11/06/2014)
- Source: `Press-Enterprise, The (Riverside, CA)`
- Verdict: **HIT (11)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Press-Enterprise%2C%20The%20(Riverside%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F05%2F2014%20-%2011%2F06%2F2014&sort=YMD_date%3AA
- Sample headlines:
  - (headline not captured; KWIC body-text snippet removed: licensed content. Re-pull the headline from the Query URL if needed.)

### Press-Enterprise (Riverside) : window 2016-11-09 (search range 11/09/2016 - 11/10/2016)
- Source: `Press-Enterprise, The (Riverside, CA)`
- Verdict: **HIT (13)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Press-Enterprise%2C%20The%20(Riverside%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for Voters face few problems November 9, 2016 Press-Enterprise, The (Riverside, CA) JEFF HORSEMAN Page F_A Lexile: 1240, grade level(s"

### Press-Enterprise (Riverside) : window 2018-11-07 (search range 11/07/2018 - 11/08/2018)
- Source: `Press-Enterprise, The (Riverside, CA)`
- Verdict: **HIT (20)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Press-Enterprise%2C%20The%20(Riverside%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for Riverside County - Voters brave long lines to cast ballots November 7, 2018 Press-Enterprise, The (Riverside, CA) By David Downey "
  - "Go to the document viewer for Riverside County busy at ballot; goat urges students to vote November 7, 2018 Press-Enterprise, The (Riverside, CA) Page 6 Lexile:"

### San Bernardino Sun : window 2012-11-07 (search range 11/07/2012 - 11/08/2012)
- Source: `Sun, The (San Bernardino, CA)`
- Verdict: **HIT (3)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Sun%2C%20The%20(San%20Bernardino%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2012%20-%2011%2F08%2F2012&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for San Bernardino County Registrar to study performance in wake of polling place complaints November 7, 2012 Sun, The (San Bernardino"

### San Bernardino Sun : window 2014-11-05 (search range 11/05/2014 - 11/06/2014)
- Source: `Sun, The (San Bernardino, CA)`
- Verdict: **HIT (7)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Sun%2C%20The%20(San%20Bernardino%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F05%2F2014%20-%2011%2F06%2F2014&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for Redlands City Council - Harrison, Foster, Barich take early lead November 5, 2014 Sun, The (San Bernardino, CA) Sandra Emerson and"

### San Bernardino Sun : window 2016-11-09 (search range 11/09/2016 - 11/10/2016)
- Source: `Sun, The (San Bernardino, CA)`
- Verdict: **HIT (7)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Sun%2C%20The%20(San%20Bernardino%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2016%20-%2011%2F10%2F2016&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for IE voters see some lines but show their pride at the polls November 9, 2016 Sun, The (San Bernardino, CA) From staff reports Page "

### San Bernardino Sun : window 2018-11-07 (search range 11/07/2018 - 11/08/2018)
- Source: `Sun, The (San Bernardino, CA)`
- Verdict: **HIT (13)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Sun%2C%20The%20(San%20Bernardino%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F07%2F2018%20-%2011%2F08%2F2018&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for Voting - Questions and concerns about election integrity November 7, 2018 Sun, The (San Bernardino, CA) Page 14 Lexile: 1210, grad"

### San Bernardino Sun : window 2022-11-09 (search range 11/09/2022 - 11/10/2022)
- Source: `Sun, The (San Bernardino, CA)`
- Verdict: **HIT (33)**
- Query URL: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&t=stp%3ANewspaper!Newspaper&b=results&fld-base-0=alltext&val-base-0=ballots&bln-base-1=AND&fld-base-1=source&val-base-1=Sun%2C%20The%20(San%20Bernardino%2C%20CA)&bln-base-2=AND&fld-base-2=YMD_date&val-base-2=11%2F09%2F2022%20-%2011%2F10%2F2022&sort=YMD_date%3AA
- Sample headlines:
  - "Go to the document viewer for L.A. County Sheriff’s race - Luna takes large early lead with mail-in ballots over Villanueva November 9, 2022 Sun, The (San Berna"
  - (a KWIC body-text snippet was removed from this cell: licensed content)

## Diagnostic follow-up on the 3 MISS-empty-window cells

Zero-result cells are surprising for daily metro papers the day after a
general election, so each was re-tested with looser queries (broader term
`"election"` instead of `"ballots"`, no `Newspaper`-type restriction, no
source restriction at all) before accepting the miss. Findings, in order of
confidence:

- **San Diego Union-Tribune, 2012-11-07 and 2014-11-05: a real archive gap,
  not a query artifact.** With `source=San Diego Union-Tribune, The (CA)` and
  no text term at all: 52,006 articles in all of 2011, only 139 in all of
  2012, **0 in all of 2013**, **0 in all of 2014**, 30,357 in all of 2015,
  28,177 in 2016 H1. So the NewsBank Text archive for this source has a
  genuine ~14-month-to-2-year hole spanning late 2012 through 2014, despite
  the A-Z Source List advertising "1983 - Current" coverage (that date range
  is evidently the outer bound, not a coverage guarantee). This explains both
  misses; it is not worth Tasks 2-7 retrying alternate query terms for these
  two cells against this source. The same-day all-sources control query
  (`election`, no source filter, Nov 7 2012) returned 23,799 hits, confirming
  the archive itself is populated that day, just not for this one source.
  - Query URL (reconstructed), 2011 full year: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=source&val-base-0=San%20Diego%20Union-Tribune%2C%20The%20(CA)&bln-base-1=AND&fld-base-1=YMD_date&val-base-1=01%2F01%2F2011%20-%2012%2F31%2F2011&sort=YMD_date%3AA
  - Query URL (reconstructed), 2012 full year: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=source&val-base-0=San%20Diego%20Union-Tribune%2C%20The%20(CA)&bln-base-1=AND&fld-base-1=YMD_date&val-base-1=01%2F01%2F2012%20-%2012%2F31%2F2012&sort=YMD_date%3AA
  - Query URL (reconstructed), 2013 full year: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=source&val-base-0=San%20Diego%20Union-Tribune%2C%20The%20(CA)&bln-base-1=AND&fld-base-1=YMD_date&val-base-1=01%2F01%2F2013%20-%2012%2F31%2F2013&sort=YMD_date%3AA
  - Query URL (reconstructed), 2014 full year: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=source&val-base-0=San%20Diego%20Union-Tribune%2C%20The%20(CA)&bln-base-1=AND&fld-base-1=YMD_date&val-base-1=01%2F01%2F2014%20-%2012%2F31%2F2014&sort=YMD_date%3AA
  - Query URL (reconstructed), 2015 full year: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=source&val-base-0=San%20Diego%20Union-Tribune%2C%20The%20(CA)&bln-base-1=AND&fld-base-1=YMD_date&val-base-1=01%2F01%2F2015%20-%2012%2F31%2F2015&sort=YMD_date%3AA
  - Query URL (reconstructed), 2016 H1: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=source&val-base-0=San%20Diego%20Union-Tribune%2C%20The%20(CA)&bln-base-1=AND&fld-base-1=YMD_date&val-base-1=01%2F01%2F2016%20-%2006%2F30%2F2016&sort=YMD_date%3AA
  - Query URL (reconstructed), same-day all-sources control (Nov 7 2012, `election`, no source filter): https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=alltext&val-base-0=election&bln-base-1=AND&fld-base-1=YMD_date&val-base-1=11%2F07%2F2012&sort=YMD_date%3AA
- **Madera Tribune, 2012-11-07: also a real archive gap.** `source=Madera
  Tribune (CA)` with no text term returns 0 for all of October 2012, all of
  November 2012, and all of calendar 2012 : despite the A-Z listing's "2002 -
  Current" range. Fresno Bee (which the brief notes also covers Madera) is a
  HIT for this same window, so the Madera election-night story is still
  reachable via Fresno Bee, just not via Madera Tribune's own text.
  - Query URL (reconstructed), October 2012: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=source&val-base-0=Madera%20Tribune%20(CA)&bln-base-1=AND&fld-base-1=YMD_date&val-base-1=10%2F01%2F2012%20-%2010%2F31%2F2012&sort=YMD_date%3AA
  - Query URL (reconstructed), November 2012: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=source&val-base-0=Madera%20Tribune%20(CA)&bln-base-1=AND&fld-base-1=YMD_date&val-base-1=11%2F01%2F2012%20-%2011%2F30%2F2012&sort=YMD_date%3AA
  - Query URL (reconstructed), calendar 2012: https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/results?p=WORLDNEWS&b=results&fld-base-0=source&val-base-0=Madera%20Tribune%20(CA)&bln-base-1=AND&fld-base-1=YMD_date&val-base-1=01%2F01%2F2012%20-%2012%2F31%2F2012&sort=YMD_date%3AA
- Method used to confirm (not saved, no article bodies): `fld-base-0=source`
  + `fld-base-1=YMD_date` only (no text term), swept year-by-year/month-by-
  month for each source, to distinguish "paper had nothing on this exact
  topic that day" from "paper has zero indexed content in this whole window."

## Final summary (paper x year)

`HIT n` = n articles matched `"ballots"` in the window (Newspaper/Text source
only). `MISS-empty` = source exists, 0 articles in-window (confirmed a real
archive gap, see diagnostics above, for the two starred cells). `MISS-no-src`
= paper absent from the A-Z Source List entirely (did not occur).

| paper | 2012-11-07 | 2014-11-05 | 2016-11-09 | 2018-11-07 | 2022-11-09 |
|---|---|---|---|---|---|
| Sacramento Bee | n/a | n/a | HIT 8 | n/a | n/a |
| San Jose Mercury News | n/a | n/a | HIT 6 | HIT 7 | n/a |
| Fresno Bee | HIT 14 | HIT 17 | n/a | HIT 31 | HIT 43 |
| Madera Tribune | MISS-empty* | HIT 1 | n/a | n/a | n/a |
| San Diego Union-Tribune | MISS-empty* | MISS-empty* | HIT 27 | n/a | n/a |
| Press-Enterprise (Riverside) | HIT 15 | HIT 11 | HIT 13 | HIT 20 | n/a |
| San Bernardino Sun | HIT 3 | HIT 7 | HIT 7 | HIT 13 | HIT 33 |

`n/a` = cell not in the brief's table (paper/window not needed). `*` = confirmed
genuine NewsBank archive gap (see diagnostics), not a query-construction
artifact.

**Totals: 21 cells probed, 18 HIT, 3 MISS-empty-window, 0 MISS-no-source.**
All 7 papers exist as NewsBank sources; Tasks 2-7 should skip the 3 starred
cells (Madera Tribune 2012-11-07; San Diego Union-Tribune 2012-11-07 and
2014-11-05) rather than re-querying them, and can lean on Fresno Bee for the
Madera 2012 window per the brief's own note that Fresno Bee also covers
Madera.
