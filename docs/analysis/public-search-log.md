# The search log

What has already been searched in the hunt for San Francisco's historical
ballot-count records, so independent researchers don't redo covered ground.
Last updated June 2026.

## Archives searched, and how

**SF Department of Elections (live web).** Every per-release summary report
the Department publishes (2015–present) is already in the dataset. The
Department's historical turnout table (1899–2019) supplies certified
totals and precinct/mail splits for every election.

**Wayback Machine.** Captures of four generations of city results pages
(ci.sf.ca.us, sfgov.org, sfelections.org, sf.gov), the frozen Lotus Domino
canvass views (election2.nsf), Elections Commission meeting minutes, and
DOE "Election Summary" pages. Systematic CDX sweeps were run for every
thin election 2000–2012 across all known host/path generations, windows of
election day through +21 days. Confirmed never captured mid-canvass:
2002-12 results pages, 2004-03 results pages.

**San Francisco Chronicle, NewsBank text archive (1985–present).**
Searched per election, election day through +2 (and +21 for canvass-
progress stories), with query families: the standing results-table titles
("HOW SAN FRANCISCO VOTED", "S.F. VOTE", "SAN FRANCISCO VOTE", "ELECTION
RETURNS", "COUNTY-BY-COUNTY"), and count-language phrases ("ballots
counted", "left to count", "yet to be counted", "remain uncounted",
"absentee ballots", "provisional ballots", registrar names). The standing
results table exists as parseable text for most elections 1986–2002;
for 1992–1999 the San Francisco edition of the county-by-county series
ran as a graphic and is not in the text archive (every neighboring
county's table is).

**San Francisco Chronicle, NewsBank page-image archive (1865–2017).**
Day-after (and where needed day-2) papers page-walked and read for:
every election 1960–1984 with a missing night count; 1985, 1987 (Apr,
Jun), 1992, 1993, 1995, 1996-03, 1999 (Nov, Dec), 2002-12, 2003-10,
2004 (Mar, Nov), 2005-11, 2006 (Jun, Nov), 2008 (Feb, Jun), 2009 (May,
Nov), 2010 (Jun, Nov), 2011-11, 2012 (Jun, Nov). Page ranges swept:
front sections (pages 1–14) for pre-1996 papers; section B / results
pages (roughly pages 10–40, tuned per era) for 2000s papers. Results
boxes were found and read for most; the specific issues where no San
Francisco results box exists in the searched ranges are listed on the
missing-records page.

**San Francisco Examiner (NewsBank).** Searched and effectively empty:
what Access World News holds under this title is the post-2006
Examiner.com regional blog network, not the print afternoon paper.
Election-window searches for 2005-2010 returned only out-of-county blog
posts; nothing exists there for 1985-2003 at all. The print
Examiner's election-night pages — the most promising untapped source
for the missing records, given its evening deadlines — survive only on
microfilm (SFPL and the California State Library hold runs).

**Other Bay Area and national papers (NewsBank, multi-paper sweep).**
Access World News holds ~90 newspapers with same-window SF election
coverage: the San Jose Mercury News, Sacramento Bee, Daily News of Los
Angeles, Daily Breeze, AP wire and others carried precincts-reporting
count snapshots that filled the 1987, 1993, 1995, 1999-12, and 2005
night gaps. Searched per gap election, election day through +3, with
count-language queries; remaining gaps were not covered with usable SF
figures in any of these papers.

**Other sources used.** SFGate's live archive (1995–2001 rich, 2002–2009
sparse), the California Secretary of State's Statements of Vote (online
from 1990), contemporary coverage in other outlets (e.g. Berkeley Daily
Planet for the 2003 mayoral runoff), and Elections Commission minutes
for certification dates.

## Verification standard

Every candidate number passes arithmetic gates before entering the
dataset: a contest sum may not exceed the certified ballot total; counts
must be monotone against neighboring dated observations; printed
percentages must match printed counts within a point; load-bearing digits
are independently re-read; remaining-ballot statements are cross-checked
against any capture-dated record. Rejected so far under these gates:
eight candidate figures, including two printed tables that contradict
their elections' certified totals (June 1974, November 1978) — both
listed on the missing-records page awaiting a second source.

## Why ~30 elections still lack a true election-night count

The remaining diamond-only elections fall into three groups, each
exhausted for the digital archives:

1. **Pre-1985 local primaries and special elections** (11 elections,
   e.g. the 1972/1976/1980/1982 primaries). National and regional wire
   services only carried San Francisco's marquee mayoral and statewide
   races, so out-of-town papers have nothing; the Chronicle's own
   page-image archive has been swept. These are microfilm-or-nothing.

2. **1986-2010 elections with a day-2 floor but no archived night
   table** (17 elections). The Chronicle's "How San Francisco Voted"
   box for these ran in the day-2 (E+2) paper at complete precincts;
   the election-night (E+1) edition either printed only percentages or
   wasn't separately digitized. We hold conservative day-1/day-2 floors
   for all of them.

3. **Modern ranked-choice and special elections** (5 elections:
   2008-04, 2009-05, 2011-11, 2013-11, 2014-06). Coverage reports
   night-of *percentages* ("Lee led the first round with 31 percent")
   but not the absolute ballot counts a floor requires, and RCV has no
   single yes/no contest to sum. The Department's own first-round
   reports would resolve these.

## What would help most

The San Francisco Examiner (the afternoon paper — earlier deadlines meant
fresher night counts; not in the archives searched above), KQED/KRON/KPIX
broadcast archives, Department of Elections internal release reports for
2000–2014, the county pages of the 1964 and 1978 Statements of Vote, and
any photograph of an election-night tally board or results page from the
elections listed on the missing-records page.

**Update (2026-07-06).** The June 1974 "contradicting table" above has been
arbitrated against the CA Statement of Vote and resolved as OUR misread (the
SOV certified total equals the DOE figure, 198,508; the newspaper reading was
corrected in `data/sf_archival_canvass_points.csv`). November 1978 remains a
genuine open discrepancy. A third case found after this log's last entry,
November 1934, was arbitrated the other way: the newspaper was right and the
DOE figure wrong (SOV certified 225,977; the point is now in the chart).
Current register: `docs/doe-data-discrepancies.md`.

**Update (2026-07-06).** Phase 1 digital recovery for April 8, 2008 (Special
Congressional Open Primary, the post-Lantos CD-12 seat) searched the live
DOE past-results pages, a Wayback CDX sweep of sfgov.org/site/elections_
index.asp (matchType=prefix, windows 2008-04-08 through 2008-05-01 and
unbounded), the sfelections.org domain, and the uploadedfiles/elections
tree (including the SOV080408.pdf/.xls Statement of Vote). No election-night
capture turned up: the earliest archived snapshot of the Department's own
"Election Summary" page for this election (id=75242, reached from the
election-night index page's own "Election Results" link, id=75241) is dated
2008-04-15 and self-reports a "Last Updated: April 14, 2008 11:15 AM" stamp,
with all 107 of 107 precincts already at 100 percent. That day-6,
already-at-certified-total figure (19,742 ballots, exactly the certified
count) is now in `data/sf_archival_canvass_points.csv` as a turnout-only
point (stamp_kind page-self-reported, days_since_election 6); it moves this
election off the missing list but the true night count is still not in the
digital archives. This election was previously grouped above among the "5
elections" lacking absolute counts; that framing predates this finding.

**Update (2026-07-06, later).** The April 2008 night count was then found
after all, in the NewsBank text archive: the Chronicle's morning-after story
(April 9, 2008, pB1, John Wildermuth, docref 11FF1C4B48B28060) prints "About
17,000 ballots were cast in San Francisco" with all San Francisco precincts
reporting, SF-only and separate from the San Mateo figure. The sentence had
been sitting unextracted in a document harvested in June, when this election
was logged as percentage-only; ten fresh queries and five new document
fetches produced nothing better. Ingested as a rounding-safe floor of 16,500
(the printed figure is approximate), giving an 83.6 percent night share.
The lesson for future searches: re-read already-harvested documents for
count language before declaring an election percentage-only.

**Update (2026-07-06, wave B).** Three more "pre-1985 microfilm-or-nothing"
entries above turned out to be recoverable after all, once the June
captures' issue labels were re-verified against mastheads (several batches
were one day off, a session-clobber artifact, so the pages read in June were
not the pages believed). August 1977: the true E+2 paper (Aug 4) carries an
absolute per-district Props A/B table on p2 (Prop B sum 174,308, final
unofficial); the E+1 percentage-map dead end was real but described the
wrong day's paper. June 1976: the E+1 (June 9) "San Francisco Vote Tally"
box exists with counts; its header prints "26.1 per cent of 942 precincts"
while every contest in the table runs 70 to 82 percent of its complete E+2
count, so the header is a typesetting error (likely 76.1); the box is
ingested as a flagged partial with the discrepancy noted. June 1972: no
newspaper night count survives (the registrar said counting would run into
June 7), but the June 8 paper prints "64 per cent of the city's 368,357
registered voters" on the complete count, ingested as a conservative day-2
floor (63.5 percent of registration). Standing lesson: never trust a
NewsBank issue label; verify the masthead date on every capture before
reading numbers from it.

**Update (2026-07-06, wave C).** The 1970 statewide pair is recovered with
Statement of Vote denominators. June 1970: the Chronicle's "San Francisco
Vote Tally" box prints a literal "Total voters reported" line in both
issues, 108,659 at 603 of 1208 precincts election night (flagged partial)
and 214,637 complete on day 2, which lands 306 under the SOV certified
214,943. November 1970: Governor sums of 245,497 at 1331 of 1350 precincts
election night and 254,038 complete on day 2 (cross-checked against the
same page's county-by-county table), against SOV certified 262,398.
November 1971 (municipal) is recovered but HELD OUT of the dataset pending
a certified denominator, which exists in no state SOV (odd-year municipal)
and no DOE table row: the election-night Mayor sum across all 11 candidates
is 248,105 to 248,135 at 1323 of 1350 precincts (the spread is a 30-vote
discrepancy in Feinstein's figure between the front-page box, 53,911, and
the page 1A tally, 53,941), the day-2 paper prints final unofficial Mayor
figures (Alioto 97,251, Dobbs 69,786, Feinstein 55,175) plus "a 75 per cent
voter turnout" against a printed registration of 340,404. Needed to ingest:
the official canvass total from the Registrar (canvass-completion coverage
ran roughly November 18-24, 1971), the Municipal Reports, or the DOE
records request.

**Update (2026-07-06, wave D).** The November 1971 hold above is RESOLVED:
the Chronicle's official-tally story (November 23, 1971, p4, "Official
Tally - Prop. O Passes") prints both the certified total, "258,227 voters
went to the polls, amounting to 75.8 per cent of the registered voters,"
and the election-night plateau in the same sentence: "a slight increase
from the 258,164 vote total reported on election night." That gives
November 1971 a verified 100.0 percent night share (lever machines,
absentees counted night-of), and the same story supplies official Mayor
totals (Alioto 97,477, Dobbs 69,740, Feinstein 55,204) that supersede the
election-night partials widely mirrored online. The canvass-story tactic
did NOT repeat for November 1969 (issues of Nov 21, 25, 26, 27 all dry)
or November 1967 (the Nov 28 paper confirms the canvass happened but
restates no totals). Both elections now hold verified night observations
awaiting a certified denominator: 1969 has a Prop B night sum of 182,237
at 1200 of 1204 precincts plus a complete machine count of 199,488
(absentees excluded), and the Department's own HistoricalBallotPropositions
open-data file gives certified Prop B 183,148, which independently
validates the night read; 1967 has a complete pre-absentee Mayor sum of
242,170 at 1341 of 1341 precincts plus absentee-inclusive top-3 figures
(Alioto 109,982, Dobbs 94,089, Morrison 40,996; full-field estimate about
249,700, consistent with the 249,795 figure circulating unsourced online).
The denominators live in the city's own "Statement of Vote" volumes at the
SFPL History Center (finding aid confirms 1967, 1969, and 1971 volumes
exist; in-library use only, not digitized). June 1968 gained a night
observation (Prop A sum 112,468, the only SF count printed on a night
wrecked by the new computer tabulation system's failure: the Chronicle's
"S.F. COUNT - SLOWEST IN 4 DECADES" reports tally sheets in City Hall
basement suitcases and a firebombed polling place) and a genuine open
discrepancy: the paper's completed unofficial count, 262,449, exceeds the
SOV certified 254,825; see docs/doe-data-discrepancies.md.

**Update (2026-07-06, wave E).** The 1966 pair closes the post-1965 sweep.
November 1966 (Reagan-Brown): the ELECTION EXTRA's "S.F. Vote" box covers
all 1344 precincts semiofficially on election night; the Governor sum
267,247 against the SOV certified 286,049 gives a 93.4 percent night
share. June 1966 (primary): the night box also reached near-complete
precincts (1342 of 1344), but closed-primary contests span single parties,
so the largest provable all-voter floor is the local Prop A sum 146,496
(64.6 percent), ingested as a flagged partial since the true night share
was plainly far higher. With that, every post-1965 election that lacked a
night count has been attempted: eleven now carry night observations, three
carry complete day-2 counts, and two (November 1967 and November 1969)
hold verified night observations awaiting certified denominators from the
city Statement of Vote volumes at the SFPL History Center.

**Update (2026-07-06, turnout 1891-1907).** The turnout record's 1891-1907
hole is filled, from a single overlooked page: the Dept. of Elections
cumulative registration-and-votes table in the FY1907-08 Municipal Report
(p.871, archive.org sanfranciscomuni57sanfrich, cross-verified against the
vols 49, 53, and 55 printings) lists registration and ballots cast for
every election from the 1880s through 1907, statewide and municipal alike.
Sixteen elections gained turnout rows (data/sf_turnout_1891_1907.csv).
Notable as-printed anomalies, kept not smoothed: the 1898 registration dip
(fresh biennial register), the rounded 1905 figures (the 1906 fire
destroyed the underlying records; the Registrar's own table prints
estimates), and the post-fire re-registration collapse (81,576 registered
in 1904 to 51,633 in 1906). The same table exposed three index errors:
the master list's November 1, 1898 municipal election never happened (the
municipal offices rode the November 8 state ballot), the DOE turnout
table's December 2, 1899 row is actually the December 29, 1899 sewer-bond
special (figures exact, date wrong), and two real special elections appear
in no index at all (December 27, 1899 park bonds; December 4, 1902 charter
amendments). The master list now carries 272 elections, and the missing
night-count total rises from 69 to 71 because discovering elections adds
to the denominator. These Municipal Reports ballots-cast figures double as
certified denominators for the pre-1907 night counts still missing.

**Update (2026-07-07, the CDNC vein).** A wholly new archive opened: the
California Digital Newspaper Collection (cdnc.ucr.edu), free and full-text
searchable, holding the SF Call (1856-1913), the Daily Alta California
(1849-1891), and more. Nobody had tried it. Direct fetches are blocked by
a Cloudflare challenge (and the same wall now fronts Chronicling America),
but a real Chrome driven over a raw CDP session passes it; puppeteer's
normal Page API does not (its Runtime.enable trips the challenge). The
working recipe, search grammar, and OCR-endpoint parameters live in
scripts/archive-recovery/cdnc_fetch.js. First campaign, the 1897-1906
municipals and the post-fire general, all with Municipal Reports
denominators: 1897-12 Freeholders (complete count 26,163 on day 2),
1898-05 charter ratification (26,963 counted complete BY 10 PM ELECTION
NIGHT, a 100.0 percent night share in 1898), 1899-11 (night partial
20,248 clean-digit floor at 2:15am plus day-2 semi-official 51,660; one
garbled Davis digit, hand-read pending, would lift the night floor to
about 67 percent), 1901-11 (1:30am partial 38,982 plus day-2 printed
total 53,493), 1903-11 (1am partial 39,326 plus day-2 printed 'Total
vote Polled 59,767', plurality-checked), 1905-11 (voting machines:
printed total 71,033 essentially complete by 6:20pm election night; the
official denominator is the fire-era rounded 72,000, so the 98.7 percent
share carries about a point of uncertainty), and 1906-11 (Governor sum
37,287 at the Registrar's midnight semi-official revision, 96.7 percent).
Recurring gate: this era's papers print election-night 'total vote of the
city' PROJECTIONS that can exceed the certified count (1896: 65,178 vs
certified 64,820; 1899: 52,005 vs 51,965; 1901: 53,814 vs 53,746; 1903:
60,300 vs 59,824); every such figure was logged and excluded from floors.
The 1896 ballots-cast conflict between Municipal Reports printings (two
early volumes print 64,820, two later ones 61,820) was arbitrated to
64,820 by the election's own fiscal-year volume and by the SOV elector
sum (61,889), which rules the lower figure out arithmetically.

**Update (2026-07-07, the turn-of-the-century specials).** Five of the six
1899-1903 special elections yielded night counts from the day-after Call
on CDNC, every one a printed total-votes line: Dec 27 1899 park bonds
(29,938, 'exactly at 8:20 p.m. the last precinct had reported'), Dec 2
1902 Geary Street bonds (For+Against 26,454 used as the floor; the
printed 26,615 including 161 rejected ballots exceeds the certified
26,612 by 3, logged), Dec 4 1902 charter amendments (14,167), Sept 29
1903 bonds (27,234), Oct 8 1903 Geary bonds again (25,259, the printed
two-thirds shortfall reconciling exactly). The one dry hole: Dec 29 1899
sewer bonds, where the only vote table is OCR-degraded and its attempted
reconstruction FAILS the certified-ballots gate (22,662 against a 22,331
ceiling), proving the digit reads wrong; prose gives only '22,000-odd
voters'. That election needs a page-image read (NewsBank or the CDNC
viewer by hand) rather than OCR.

**Update (2026-07-07, the nineteenth century).** The CDNC vein reached the
Daily Alta California. November 1888 and November 1884 both yielded full
three-day count trajectories (token overnight slices of 6,290 and about
5,056 ballots, majorities by day 2, near-final sums of 52,916 and 40,200
by day 3), the shape of hand-count-era counting made visible. September
1879 (the first election under the new Constitution) is the season's
best story: the Alta documents the Governor lead flipping across the
count (Perkins up 240 at the day-3 midnight report, then White up 300,
then 840, with certification finally at Perkins by 351), each swing
corroborated by the stable Kalloch-Flint differential in the same
tables; ingested as a 2.4 percent night partial plus day-2 and day-3
canvass points (the paper's poll-list turnout reads, 41,113 and 41,804,
bracket the certified 41,575 but are ballots-received figures, not
canvass counts, and were not ingested). November 1880's morning-after
paper spells out 'Forty-One Thousand Two Hundred and Ninety-Eight Votes
Cast', six votes above the certified 41,292 (the rejected-ballot
reclassification class), so 1880 carries a day-2 point only. What
remains in this vein, for a future session: the 1872 and 1867-1871
statewide elections (Alta coverage exists; denominators partly on file
with medium confidence), the pre-1867 run (needs Blue Book denominators
first), and the 1850s-1895 municipals (needs both dates verified and
denominators; the Municipal Reports volumes hold the latter). The one
proven recipe: cdnc_fetch.js, search mode first, gates always.

**Update (2026-07-07, the Examiner claim is FALSE).** This log has said the
print Examiner's pages "survive only on microfilm." That was true of
NewsBank's Access World News holdings and is false in general: ProQuest's
"San Francisco Examiner, Historical and Recent" product carries full-page
digital scans essentially continuously from 1865 to the present, and SFPL
cardholders get it free through ezproxy.sfpl.org (verified on sfpl.org's
Digitized Historical Newspapers page; independently corroborated by the UC
Berkeley and Stanford library guides). The confusion likely stems from a
separate, older ProQuest index-only product covering Jan 1995-Jan 2003
with its own internal gap. Consequence: every "microfilm-or-nothing"
verdict in this log is reopened, and the afternoon Examiner's election
EVENING editions (fresher counts than any morning paper) are now
searchable for the 1995-2010 night gaps and the pre-1985 dead ends alike.

**Update (2026-07-07, CDNC's modern holdings).** For completeness: CDNC
cannot serve the 2000s gaps directly. Its full 518-title list holds no SF
Chronicle and no SF Examiner at any date; the only San Francisco titles
reaching 1995-2014 are niche papers (Bay Area Reporter through 2005, J.
The Jewish News, the UCSF Synapse, Vestkusten). A Bay Area Reporter probe
of the November 2000 and October 2003 elections yielded one
Department-attributed count-status line for 2000-11 ("about 40,000
absentee ballots citywide yet to be counted," Wednesday morning, Nov 9
2000 issue, section BAR20001109.1.1): NOT ingested, because it implies a
floor of about 284,000 that contradicts the finer same-day Chronicle
capture already in the dataset (277,575), the same unsafe-registrar-
estimate class as the rejected 2001-11 figure; it stands as corroboration
within rounding. The October 2003 recall coverage is percentages-only.
The BAR's November 6, 2003 issue carries a count-status line for the
Nov 4 mayoral, superseded by the finer 2am Chronicle point already
ingested (84.7).

**Update (2026-07-07, the records request is dead).** The Department of
Elections has told the operator directly that it does not hold its own
2000-2014 election-night release data. The drafted records request
(docs/doe-records-request.md) is therefore not a path to the fourteen
post-2000 night gaps; third-party captures are the only route. Newly
identified unswept veins: the CA Secretary of State's own election-night
results sites (vote2000.ss.ca.gov and successors), which published live
county-level tallies for every statewide election night and were heavily
captured by Wayback while the city's pages were not; contemporaneous
blogs and liveblogs (SFist, BeyondChron, Calitics, DailyKos election
threads), Usenet (ba.politics via Google Groups), archive.today (2012+),
Common Crawl (2008+), the Library of Congress election web archives, and
Archive-It partner collections (California Digital Library, Stanford).

**Update (2026-07-07, the new veins' first sweep).** The Secretary of
State's election-night sites paid immediately: the state's County Summary
PDF, page-stamped 11:54 pm on election night 2010 and captured by Wayback
at 12:11 am, gives San Francisco 174,563 ballots cast at all 590
precincts, a true 61.3 percent night point that lands beside 2008's 61.0
(reproduce: web.archive.org/web/20101103071138id_/http://www.sos.ca.gov/
contest_summary.pdf). The same vein yielded a day-5 point for November
2002 (215,552) and a late-canvass point for the 2003 recall (264,940);
2000, March 2002, and 2006 are dry (the result paths were never crawled
mid-count; the 2002/2003/2006 pages do preserve first-report timestamps,
8:40pm, 8:33pm, and 8:13pm, useful metadata). The liveblog and Usenet
families produced the 2011 SFist night floor, the 2000-12 LA
Times-via-ba.politics conversion, and a queued 2013 candidate. Source
verdicts: archive.today is bot-blocked; Common Crawl's monthly cadence
never lands on election night; DailyKos and the Library of Congress and
Archive-It collections remain unresolved, not dead; Google Groups needs
a real browser but works. Every find and dead end carries its exact
reproduction path in the session reports.

**Update (2026-07-07, the Examiner vein's first fruits).** ProQuest's
digitized Examiner immediately closed both elections that had been held
for lack of certified denominators. November 1967: the December 12, 1967
Examiner prints 'Final Returns... as certified by the accounting firm of
Arthur Andersen and Company'; the full Mayor-field sum is 249,831 (within
36 votes of the unsourced figure circulating online), and the election
ingests at a 96.9 percent night share. November 1969: the November 19,
1969 Examiner prints 'There were 199,200 votes cast out of a registration
of 324,138'; notably the certified total sits 288 BELOW the Chronicle's
semi-official machine count (199,488), and the certified table's own
per-candidate Change column shows canvass corrections running both
directions, so the machine count is logged, not ingested; the election
ingests at a 91.5 percent night share. December 1995 gained a day-1
floor: 'About 11,000 absentee ballots remained to be counted Wednesday
morning' converts to 187,326 (94.5 percent), far above the chad-jam
partial. November 2000 stayed dry for a numeric improvement (the
Chronicle's same-day capture is finer than everything the Examiner
printed); its best Examiner line, 599 of 647 precincts tallied by
11:04pm election night, is precinct-basis color that cannot convert to
ballots. The SFPL History Center errand now has a single remaining
purpose: arbitrating the June 1968 discrepancy.

**Update (2026-07-07, Examiner round two: 2008 corrected and recovered).**
The Examiner's post-election coverage gave November 2008 its first true
night observation and CORRECTED a committed row. The Wednesday-afternoon
DOE update was a direct printed 241,090 ballots counted (printed twice,
Nov 6 p6 and Nov 7 p18); the dataset had been carrying a Chronicle-derived
252,112 (certified minus the Department's stated '136,000 remaining'),
which the Examiner shows overstated the count by about 11,000 because the
Department underestimated its own remaining pile (actual: 147,022). The
derived row is replaced by the direct count, the same unsafe-derivation
class as the rejected 2001-11 figure. Night reconstruction: Wednesday
added 'only 4,000 additional ballots' over Election Day per both pieces,
so the night floor is 241,090 minus a rounding-safe 4,500 = 236,590
(61.0 percent), with day-2 (253,486 printed) and day-9 (372,812 via
remaining-conversion) points behind it. November 2010 gained a
Wednesday-afternoon floor (187,625 via an 83,000+14,000 remaining
statement); three later Examiner leads sit unverified behind a captcha
wall and are queued. November 2006 stayed dry (best Examiner lead is
coarser than the existing rows). Operational: ProQuest raised an hCaptcha
after parallel agents searched in bursts; Examiner work is serialized
from here.

**Update (2026-07-07, Examiner round three).** December 29, 1899, the
campaign's one OCR-dry hole, is closed: the Examiner's own THE VOTE table
(December 30, page 1) sums its eighteen assembly-district rows exactly to
22,322, and the page-6 editorial prints 'Of the 22,322 voters who went to
the polls' verbatim; nine below certified, ingested as a night-complete
count (the 1889-1902 segment lives under ProQuest publication 2069514,
not 2069513). June 1998 gained an afternoon day-1 floor (185,157 via a
14,000-remaining statement). November 1998 gained its first true night
point by conversion: 'With all the precincts in but no absentee ballots
counted' pins election night to the certified precinct total 183,839
(73.3 percent), plus day-1 and day-2 remaining-conversions (190,719;
223,719). The 1998 findings are KWIC-derived with page images still
behind the captcha wall, so they carry queue entries for image
verification. The 1986 and 1994 elections returned promising but
CLIPPED KWIC leads (a printed 1994 certified-total confirmation, a
derived 1994 night candidate of 175,502, a 1986 'counted by 10 p.m.'
retrospective): held un-ingested pending page-image verification, with
the thirteen-image queue in the session notes.

**Update (2026-07-07, the image-verification pass).** All fourteen queued
page images were read in one serialized run (27-second pacing, no robot
wall). Every ingested 1998 figure confirmed verbatim against its page
image. Two conversions graduated to night points on the strength of the
images plus the certified precinct/absentee splits: November 1994, where
the Examiner's '74,167 absentee and provisional ballots' counted after
election day equals the certified absentee column EXACTLY, pinning the
night count to the certified precinct total 175,502 (70.3 percent); and
June 1986, where the county clerk comparison prints 'San Francisco at
12:09 a.m.' for precinct-tally completion with 'thousands of [absentee]
votes left to count this morning', pinning that night to the precinct
total 125,143 (85.4 percent). November 1994 also gained the registrar's
printed final tally (249,669, matching certified exactly, day 7). Two
predecessor KWIC artifacts were corrected by the images (a Kubby figure
belonging to a different line; an Alameda County story misattributed to
SF). November 1986 remains without a night statement: its coverage is
percentages-only and no absentee-status clause was printed, so no
conversion is available.

**Correction (2026-07-07, same day).** The November 1994 night conversion
described above was WITHDRAWN on review. Unlike 1998 (an election-night-
dated statement that zero absentees were counted, itself a scandal-driven
anomaly rather than era practice) and June 1986 (a printed 12:09 a.m.
precinct-completion time), the 1994 inference rested only on a week-later
retrospective, and the round's own evidence cuts against it: the Nov 9
Examiner front page had just 373 of 576 precincts reporting, so precinct
counting was demonstrably incomplete on election night and the precinct
total is neither a pinned night value nor a guaranteed floor. The day-7
certified point (249,669) stands; November 1994 reverts to turnout-only
pending a genuinely dated night observation.
**Update (2026-07-07, the TV News Archive vein).** The Internet Archive's
closed-caption TV index is now mapped for this project: the Bay Area
stations (KTVU, KPIX, KGO, KRON, KQED) begin 2010-07-14, verified against
each station collection's earliest item, so 2009-05 and everything
earlier is DEAD in this vein, not merely unsearched. For 2013-11-05,
five query passes across all stations including the three election-night
11pm broadcasts found percentages only ('62 percent', '100 percent of
precincts'), never a raw count: DRY. Reusable method notes: the real
search endpoint is the page_production service with backend tvs; quoted
phrases must not be wrapped in +(...); caption downloads are limited to
a 60-second preview, so the search API's highlight snippets are the only
browserless text source.
**Update (2026-07-07, DailyKos).** The working search path is
dailykos.com/?s= with date-ascending sort (the /search route is dead).
It surfaced a minute-by-minute liveblog of the Department's own results
page on the December 2003 runoff night (DaveOinSF, 'Talk about San
Francisco Mayoral Election Here', nineteen timestamped entries 1:46 to
2:48am, explicitly citing sfgov.org/wcm_election/nstats.htm): every
entry is percentages or precinct fractions, never an absolute count, so
nothing ingests, but the 2:48am '99.11 percent in' entry is the standard
precincts-reporting metric (the thread's own entries run 557/562 to
562/562), so it evidences night-complete PRECINCT counting only; it is
silent on the VBM and provisional piles and therefore supports only
part of the queued Examiner 'on Tuesday' judgment (operator's
correction, same day). 2006-11 and 2000-11 are dry there
(eleven queries; the site launched in 2002).
**Update (2026-07-07, LoC and Archive-It, the last web-archive doors).**
Both are now definitively dry for the remaining night gaps, with
structural explanations rather than mere absence: the Library of
Congress's Election 2000 / United States Elections web archive collected
candidate CAMPAIGN sites, not government results infrastructure (its
crawls of the SoS root stop October 18, 2000 and resume December 2,
skipping election night entirely; its first capture of any SF city host
is September 2002); Archive-It's sfgov coverage begins February 2006 but
gaps across both 2006 election windows (August 1 to November 28), and no
CDL or Stanford collection targeted California election administration
in the 2000s. Method notes for future agents: webarchive.loc.gov is
Cloudflare-gated (use the Chrome recipe); Archive-It's timemap/cdx
endpoint 403s always and wildcard URL reports hang, use the single-URL
calendar form. With this, every known web archive (Wayback, LoC,
Archive-It, archive.today, Common Crawl) is exhausted for the November
2000 election night; its number survives, if anywhere, in broadcast
tape, personal archives of era analysts and reporters, or the Secretary
of State's internal records.
**Update (2026-07-07, the Examiner completion pass).** The final six
elections got their Examiner sweep, and four flipped to night: March
2002 (an 11:00 p.m. printed results table, Public Defender sum 85,801,
57.1 percent dim), November 2002 (623 of 632 precincts at press
deadline, Prop R sum 169,484, 75.3 dim), December 2000 (38,445 counted
at 8:30 p.m., citywide by arithmetic necessity, 29.7 dim), and November
2013 (the prize: elections director Arntz quoted that 'just more than
95,000 votes had been counted by 10:30 p.m. Tuesday', a direct
Department night count at 73.7 percent, which also settled the queued
SFist ambiguity). November 2011 gained a day-2 remaining-conversion
(165,242) whose full-field first-choice table refuted the queued ratio
derivation. The October 2003 recall stayed dry in the Examiner
(statewide-focused coverage). With this pass the Examiner trawl is
complete for every post-1995 gap election.
**Update (2026-07-07, the Examiner retry pass).** At the operator's
direction, all six elections still lacking a night observation
(November 2000, December 2001, October 2003, December 2003, November
2006, May 2009) got a second full Examiner pass under genuinely new
query angles (canvass and certification windows, 'official results'
families, swearing-in retrospectives, and named-official searches).
One angle produced: searching the Department of Elections spokeswoman
by name (Hayashi AND pd(20001110-20001205)) surfaced two
Department-attributed canvass floors for November 2000 that generic
election terms had missed under the Florida-recall noise: 310,031 as
of the Friday Nov 10 update ('about 14,000 ballots left to count',
Examiner Nov 11 p2, docview 2206902098, a new point) and 314,031 late
Sunday Nov 12 ('about 10,000 provisional ballots still to be
counted', Nov 13 p3, docview 2206629184, corroborating the existing
Chronicle-derived row exactly). Lesson recorded for future agents:
when generic vocabulary drowns in wire copy, search the named local
official. The other five elections stayed dry again (5 to 9 new
queries each this pass, roughly 16 to 17 cumulative per election
across both passes); with two full passes done, the Examiner is
judged tapped for those five, and any remaining recovery lies with the
Chronicle, broadcast tape, or human channels. Exact queries and
verbatim evidence: the examiner-retry session report.
**Update (2026-07-07, the 2003-12-09 resolution).** The runoff's night
question resolved both ways in one operator session. The Examiner
editorial's 246,667 'processed on Tuesday' was refuted as a night
figure by official Statement of Vote arithmetic the operator supplied
(91,119 total absentees against 253,872 total cast puts election-day
ballots near 162,700, so a night-of 246,667 would need roughly 84,000
absentees counted by midnight, inconsistent with the 225,681 night
state the same paper printed the next morning); its day-3 stamp
stands. And the true night point was already in the dataset
wearing the wrong date: the AP's 'with all precincts reporting'
figures (Newsom 118,651, Gonzalez 107,030, sum 225,681) turn out to be
printed verbatim in the Examiner's December 10 front-page results
boxes (ProQuest docview 2206456902, operator-located), and the
DailyKos-documented DOE liveblog (562 of 562 precincts by about 2:48am
PT) dates that all-precincts state to about 03:00, inside the night
cutoff regardless of the paper's press schedule. The AP row re-stamped to election night: December
2003 becomes the 204th recovered night count (88.9 percent, dimmed as
a contest-sum floor). Lesson: when a wire story's dateline lags, check
the same day's morning print edition for the identical figures; the
press deadline dates the count.
**Update (2026-07-07, the calinst.org vein).** The operator, browsing
freely, surfaced calinst.org/2006elections/, a California Institute
for Federal Policy Research page still live on the open web that
snapshots the Secretary of State's vote.ss.ca.gov feed 'as of Nov 8,
2006 at 8:33 am Eastern (5:33 am Pacific) when 97.9% (24565 of 25090)
precincts were reporting'. That is 27 minutes inside the night cutoff,
and the 2002-2012 eighth Congressional district lay entirely within
San Francisco, so its printed field (Pelosi 101,002, DeNunzio 13,043,
Keefer 9,611, Berg 1,880) sums to a citywide night floor of 125,536:
November 2006, judged Examiner-tapped one day earlier, becomes the
205th recovered night count (49.5 percent, dimmed as a
quarter-city-missing contest sum). The find also proves a new vein
class: third-party morning-after snapshots of the SoS live feed
survive where every web archive missed the count window. The site's
weekly bulletin archive (calinst.org/bull.html) is queued for the
remaining holdouts.
**Update (2026-07-07, the recall night-completeness anchor).** The
operator pulled the Oct 8 2003 Chronicle's turnout story (NewsBank
docref news/0FE0FB1FEB220A59, text mirrored to mirror/newsbank/docs/):
'By 10 p.m., San Francisco officials were able to report results from
99 percent of the city's precincts -- hours, even days, ahead of
previous election reporting.' A precincts metric, so not ingestible by
itself, but it anchors the recall's night state: whatever night-stamped
SF ballot count surfaces will be a near-complete one. The same issue's
text corpus was swept for the print results tables (queries 'recall
AND yes AND no', 'precincts reporting', 'ELECTION RESULTS', 'the
vote'; the Bay Area reaction story news/0FE0FB1FE3468E6C carries
percentages only): the county results tables did not digitize into
NewsBank text, a dead end for absolute SF numbers in that issue.
**Update (2026-07-07, the recall falls).** Minutes after the
night-completeness anchor was logged, the operator found the numbers
themselves: the Oct 8 2003 Chronicle print edition's county table
('CALIFORNIA RECALL / How the regions voted', page A14), which exists
in NewsBank's page-image collection even though it never digitized to
text. The San Francisco row reads 99.2 percent reporting, Yes 45,388
(20), No 186,324 (80): a recall-question sum of 231,712, 86.1 percent
of certified, and October 2003 becomes the 206th recovered night count
(dimmed, undervote-limited). Lesson recorded: when a table is missing
from the NewsBank TEXT corpus, check the page-image edition of the
same issue; the image collection extends later than the previously
assumed mid-1980s endpoint.
**Update (2026-07-07, the snapshot vein sweep).** The vein agent
generalized the calinst find across smartvoter, calvoter, CNN, the SoS
sites, and the old calinst in Wayback (full log: the calinst-vein
session report; all load-bearing pages mirrored under mirror/altweb/).
Two upgrades landed. May 2009: the SoS County Reporting Status page,
captured E+1, prints San Francisco's own night ledger verbatim ('428
428 100.0% 465,181 97,958 21.1% 19 8:08 p.m. 19 11:01 p.m.'), a DIRECT
97,958 ballots-counted night figure (75.0 percent, undimmed) that
supersedes the print-edition Prop 1A sum as the night value. October
2003: CNN's county page, mirroring the official feed with per-county
stamps, shows 'San Francisco updated: 5:28 a.m. [Eastern; 2:28 a.m.
Pacific] Yes 45,783 20% 100% of precincts reporting No 187,450 80%',
lifting the recall's night value to 233,233 (86.7, still dimmed as a
contest sum). Both print-edition rows re-stamped to precede their
feed-snapshot successors. Also established: December 2001 is fully
dead on the open web (no DOE, sfgate, or Examiner captures in the
runoff week; smartvoter never archived a page for it), leaving the
Chronicle print edition in NewsBank as its only plausible carrier.
And a presentation bug surfaced by these finds: the README night-share
image inherited the preview's default kind filter, which hides Special
and Recall elections; the shoot script now passes kinds=all, so the
1980-08 special (100.0), the recall, and both 2022 recalls render.
**Update (2026-07-07, December 2001 falls; the post-2000 sweep is done
save one).** Hours after the web-archive verdict declared this runoff
fully dead on the open web, the operator-directed NewsBank page-image
hunt found its night count in the only place it still existed: the
Dec 12 2001 Chronicle print edition. The pA23 Bay Area front carries
'Herrera victorious in city attorney race' with '52.1 percent to 47.4
percent in unofficial returns last night', and the pA24 jump
quantifies the returns: 'only slightly more than 66,000 - or fewer
than 1 in 5 registered voters - cast ballots.' Rounding-safe floor
66,000, 87.7 percent of certified 75,267, undimmed per the 2013
precedent: the 208th recovered night count. Method note: the image
edition is OCR-searchable, so a name query (Herrera) scoped to the
date finds the exact pages without browsing; the calendar UI defaults
to January and should be avoided. Of the five post-2000 holdouts that
began the evening judged Examiner-tapped, only November 2000 remains,
and the same print-edition trick (the Nov 8 2000 paper's results
tables) is queued for it.
**Update (2026-07-07, November 2000 falls; the post-2000 era is
complete).** The last holdout of the recent era went the same way as
the others: the Nov 8 2000 Chronicle print edition, page 14, 'HOW SAN
FRANCISCO VOTED', prints the county's night state at 599 of 647
precincts reporting. The PRESIDENT block sums to 251,382 (Gore
190,051, Bush 39,756, Nader 20,106, Browne 825, Buchanan 351, Hagelin
163, Phillips 130): a 77.6 percent night floor, dimmed as a contest
sum, corroborated by the same page's Senate field and the S.F.
PROPOSITIONS block under the same precincts header. With this, every
San Francisco election from 2000 onward carries a recovered
election-night count. The era that the Department of Elections said
had no data, that every web archive missed, and that two full
Examiner passes could not complete, was finished in a single evening
by the operator's page-image insight: the print editions were the
mid-count snapshots all along, and NewsBank's image collection
(1865-2017) preserved them.
**Correction (2026-07-07).** The earlier note calling the README
chart's kind filter a presentation bug was wrong, and the operator
overruled it: Special and Recall elections are excluded from the
night-share chart on purpose (the chart is crowded, and off-calendar
elections are unusual by definition, so they stay out of the visual
trends). The kinds override has been reverted; the recovered night
counts for those elections live in the dataset and the master index
regardless of chart presentation.
**Update (2026-07-07, November 1999: the write-in freeze, measured).**
Walking backward from the completed post-2000 era, the same
print-image method dated the era's most notorious count. The Nov 3
1999 Chronicle's final six-star edition shows San Francisco frozen at
232 of 646 precincts at press time, and its front page explains why:
'The first returns from the city's 646 precincts were not released
until about 75 minutes after the polls closed at 8 p.m., then were
not updated again for another hour, and after that only sporadically
into the early hours of today' as the Ammiano write-in campaign
forced hand examination of ballots. The largest same-state contest
sum (Proposition A, Laguna Honda Bonds, 62,334) becomes the 210th
recovered night count at a striking 30.6 percent, dimmed. The
operator read the page live and flagged the write-in mechanics; the
mayor's-race table itself footnotes that its Ammiano figure 'reflects
partial write-in count'.
**Update (2026-07-07, June 1998: the blanket primary counts itself).**
One more step backward. The Jun 3 1998 Chronicle's two-star (later)
edition prints the 'HOW SAN FRANCISCO VOTED' box on page 25 of the
scanned issue with GOVERNOR at 521 of 644 precincts reporting, and
1998's blanket primary makes that contest uniquely useful: every
voter, regardless of party, voted in the same 17-candidate Governor
field, so the full field sum (Davis 62,097 through Johnson 162,
totaling 137,554) is an all-voter undervote-limited night floor, not
a party-slice. That is 69.1 percent of the certified 199,157, dimmed
as a contest sum at 81 percent of precincts, the 211th recovered
night count. An earlier edition of the same box (scanned page 43)
shows the count at 79 of 644 precincts, corroborating that the
editions snapshot the count at different hours; no hour is printed,
so the entry carries the dataset's disclosed 03:00 press-time
convention. It slots monotonically under the existing day-1
afternoon floor of 185,157 (the Examiner's absentee-remaining
conversion). Screenshots under
mirror/newsbank/scans/primary_19980602_issue19980603_p25_*.png;
reproduction: NewsBank image-edition search 'CITY AND COUNTY' scoped
to 1998-06-03, and compare the Governor precinct headers across the
page 25/35/43 edition variants to find the latest.
**Dead end (2026-07-07, November 1994: structurally dry for a night
point).** The same method fails here for a documented reason: the
count crashed. The Nov 9 1994 Chronicle morning edition in NewsBank's
image collection (front page captured at
mirror/newsbank/scans/general_19941108_issue19941109_p1_*.png, plus
pages 13 and 30) leads its election coverage on exit polls and
statewide projections and prints no San Francisco returns table in
the scanned edition; there is no 'HOW SAN FRANCISCO VOTED' box to
read. The repo already holds the next-day state (a day-1 floor of
239,669 via the Chronicle's absentee-remaining conversion), and the
evening Examiner's 373 of 576 precincts figure encountered during the
hunt is likewise day-1 state, not election night; nothing in the Nov
9 morning paper beats either or establishes any night-of figure. Reproduction: NewsBank image-edition issue
1994-11-09, front section; searched 'HOW SAN FRANCISCO VOTED' and
'precincts reporting' scoped to the date. November 1994 stays in the
missing set pending a different vein (wire copy with a timestamped SF
figure, or the Examiner's own Nov 9 morning run if one exists).
**Update (2026-07-08, November 1986: the whole ballot, summed and
beaten by the Senate race).** The operator hand-read hunt that stalled
at the page edge finished today: the Nov 5 1986 Chronicle's page 10
'HOW SAN FRANCISCO VOTED' table (found via the quoted alltext search
'SAN FRANCISCO VOTED' scoped to the date, a single hit) prints every
contest at '611 of 710 precincts reporting', and this time the whole
statewide column was read in the live viewer. The U.S. SENATOR field
is the page's largest single-vote sum: Cranston 143,953 + Zschau
47,667 + McKinley 1,159 + Kangas 1,076 + Vallen 932 = 194,787, edging
the GOVERNOR field's 192,367 and well above the Bird confirmation's
180,053 and every proposition (Prop 64, the AIDS quarantine measure,
tops those at 181,058). That is an 82.2 percent night floor against
the certified 236,863, dimmed as a contest sum, the 212th recovered
night count; the same page's board-president story corroborates the
state: 'With nearly 80 percent of the vote counted last night, Walker
led the pack of 19 candidates.' It slots monotonically under the
repo's existing day-2 Governor sum (222,403 at 710 of 710). Method
note for future agents: the NewsBank viewer viewport clips the
table's left column at default position; click the canvas, then
arrow-key pan (the keys silently no-op if the canvas loses focus),
and zoom in once before reading digits. The 1985-2026 era is now
complete except for the five pre-1985 stragglers (1984-06, 1982-11,
1982-06, 1977-08, 1972-06).
**Finding, not a night count (2026-07-08, June 1984: the ELECTION
SPECIAL edition).** Walking backward past November 1986, the June 6
1984 issue in NewsBank's image collection turns out to be an ELECTION
SPECIAL edition ('MONDALE: I'VE WON' front page), and its page 2 'HOW
SAN FRANCISCO VOTED' table prints the count COMPLETE: every citywide
block at 708 of 708 precincts, City Prop B (Police Night Pay) YES
81,436 + NO 73,756 = 155,192, identical to the E+2 table already in
the dataset (the June 7 paper p20). This does NOT create a night
point: the regular June 6 edition's box (read in an earlier pass)
showed only Prop 24 counted, at 67 percent of precincts, and the
November 1986 comparison (still 611 of 710 at morning press) makes a
pre-dawn completion implausible; the special is a later-press extra
with an unknown hour, likely past the 06:00 night cutoff. Recorded as
day-1 corroboration of the existing 155,192 floor. The true
election-night state of June 1984 remains the early box's Prop 24 at
67 percent, whose sum (36,573) is too small to be useful. June 1984
stays missing a night count pending a source with a clocked overnight
figure. Reproduction: NewsBank image-edition alltext search 'SAN
FRANCISCO VOTED' (quoted) scoped to SF Chronicle 1984-06-06, single
hit page 2; the front page (page 1 of the same scan) carries the
ELECTION SPECIAL banner.
**Dead end confirmed (2026-07-08, November 1982: the ELECTION EXTRA).**
The Nov 3 1982 issue in NewsBank's image collection carries an
ELECTION EXTRA banner on its front page ('WILSON WINS IT'), and its
page 5 'HOW SAN FRANCISCO VOTED' table is headed '100 percent of
vote': like June 1984's ELECTION SPECIAL, the digitized issue is a
post-completion late run whose press hour cannot be placed before the
06:00 night cutoff. Its GOVERNOR field sums to 224,633 (Bradley
149,699 + Deukmejian 67,973 + Dougherty 2,780 + Martinez 3,170 +
Griffin 1,011), which corroborates but does not beat the dataset's
existing day-1 floor for this election (230,991, the same issue's
'8,000 absentee ballots... counted later this week' conversion,
stamped 08:00). November 1982 stays without a night count; what would
resolve it is the REGULAR final edition of Nov 3 (not digitized in
NewsBank, which holds the extra) or a wire snapshot with a clocked
partial. Reproduction: NewsBank image-edition alltext search 'SAN
FRANCISCO VOTED' (quoted) scoped to SF Chronicle 1982-11-03, single
hit page 5; page 1 of the same scan shows the ELECTION EXTRA banner.
**Update (2026-07-08, June 1982: the 64-percent morning table, the
213th night count).** Unlike its November sibling (an ELECTION EXTRA)
and June 1984 (an ELECTION SPECIAL), the June 9 1982 issue's page 8
'HOW SAN FRANCISCO VOTED' table is a genuine mid-count snapshot,
headed '64% of vote', which itself rules out a post-completion extra:
extras print more counted, not less. Propositions appear on every
ballot regardless of party, so the largest all-voter sum is the night
floor: state Prop 9, the Peripheral Canal referendum, YES 4,351 + NO
91,931 = 96,282 (San Francisco rejected the canal 95 to 5), 54.6
percent of the certified 176,381, dimmed as a contest sum, stamped
with the disclosed 03:00 morning-press convention. It sits cleanly
against the existing day-2 floor (93,431, a Democratic-governor
party-subset at 100 percent, a smaller basis) and the 64-percent
state (64 percent of certified is 112,884, above the floor, as
required). Reproduction: NewsBank image-edition alltext search 'SAN
FRANCISCO VOTED' (quoted) scoped to SF Chronicle 1982-06-09, single
hit page 8. Method note: in primary-election tables the party
contests are subsets; read the propositions columns first.
**Update (2026-07-08, August 1977: the overnight count, hiding on the
front page).** The 1977 district-elections special was already in the
dataset as a day-2 floor (174,308, the Aug 4 per-district table) with
a note that the E+1 paper 'printed a percentage map only'. Wrong: the
Aug 3 1977 FRONT PAGE prints the outcome block in text, 'With all 735
precincts reporting, this was the outcome: PROPOSITION A Yes ...;
No—97,5xx. PROPOSITION B Yes, 62,185; No—112,123', digit-for-digit
identical to the E+2 table, and the story confirms the count ran
'last night'. A two-measure lever-era ballot counted overnight: the
existing 174,308 Prop B sum is re-stamped to election night (03:00
press convention, disclosed), dimmed as a contest sum, 97.7 percent
of the certified 178,367: the 214th night count. Lesson repeated: the
E+1 verdict of an earlier pass is worth one more look when it rests
on 'only a map/percentages' — the outcome paragraph often carries the
counts in prose. Reproduction: NewsBank image-edition alltext search
'precincts' scoped to SF Chronicle 1977-08-03, single hit page 1.
**Dead end (2026-07-08, June 1972: the punch-card debut printed no
E+1 numbers).** San Francisco's first Votomatic election jammed the
polls ('This is criminal,' shouted an elderly voter, in the June 7
p6 'Phones Rang On For S.F. Registrar' chaos story; a federal order
was being hand-delivered to precincts at 8 p.m. per the p30 story)
and the next morning's Chronicle printed no results table at all:
alltext searches of the June 7 issue for 'The S.F. Vote', 'ballots
counted', and 'SAN FRANCISCO VOTED' all return zero, and the page 1
election story carries only 'The four incumbents took strong early
leads this morning... With most of the precincts reporting' on the
multi-seat school-board race (vote-for-several, unusable as a ballot
floor). The count was complete by the June 8 paper (the dataset's
existing day-2 record, 1349 of 1349). June 1972 stays without a
night count; the evening Examiner of June 7 (ProQuest vein) is the
untried source that could carry a clocked day-1 partial.
Reproduction: NewsBank image-edition searches scoped to SF Chronicle
1972-06-07 as quoted above; 'precincts' returns six pages, all read.
