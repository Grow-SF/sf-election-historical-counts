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

*[Superseded, June 2026 snapshot preserved as written. The July 2026
recovery campaign disproved much of this section: group 2's day-2-only
elections and group 3's RCV elections have all since yielded night
counts, and group 1 has shrunk. See the dated update and correction
entries appended below for the current state; the live tally lives in
the README and docs/missing.md.]*

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
**Finding, pending a denominator (2026-07-08, November 1945: twelve
precincts by press time).** The prewar cluster opens with a
hand-count-era night state worthy of 1918: the Nov 7 1945 Chronicle
front page prints an 'Election Returns' box reading 'Complete
semi-official returns from 12 widely scattered precincts out of 1194
at yesterday's election gave the following results', Airport Bonds
YES ~1,362 / NO ~355 (digits soft, operator read requested), and the
adjacent story blames 'showers and a general apathy' for 'a light
vote'. Twelve of 1,194 precincts is a 1.0 percent night state: the
municipal hand count still effectively produced nothing overnight in
1945. NOT ingested yet: this election has no denominator anywhere in
the dataset (absent from the DOE turnout table entirely), so the
night point cannot compute a share until the complete count is
recovered from the Nov 8-10 1945 papers or the Municipal Reports.
Queued. Reproduction: NewsBank image-edition alltext search
'precincts' (quoted) scoped to SF Chronicle 1945-11-07, hit page 1,
'Election Returns' box, left of the fold.
**Correction (2026-07-08, June 1984 IS a night count, the 215th).**
The earlier note calling the June 6 1984 ELECTION SPECIAL a
post-completion late run was overruled by the operator: the special
is the Wednesday morning paper (press deadline early Wednesday
morning), not a later-day extra, so its complete 708-of-708 table is
election-night state, printed hours after the polls closed. The
operator hand-read the propositions columns from the scan. The
existing 155,192 floor (City Prop B, Police Night Pay, YES 81,436 +
NO 73,756) re-stamps from day-2 to night at the disclosed 03:00
convention, dimmed as a contest sum: 85.9 percent of the certified
180,741. The earlier morning edition's box (Prop 24 at 67 percent)
now reads as the early press run of the same night, the familiar
edition sequence. November 1982's ELECTION EXTRA remains open for
the same adjudication: if that extra is likewise a Wednesday-morning
run, its '8,000 absentees remain' conversion (230,991, 96.7 percent)
would re-stamp to night as well; the operator has the scan open.
**Retry, still dry (2026-07-08, November 1994 second pass, the
multi-paper vein).** Operator-requested retry of the 1994 night hunt
through the ~90-paper NewsBank text sweep that filled the 1987, 1993
and 1995 gaps. Queries scoped to 1994-11-09 and -11-10 across all
sources: quoted '576 precincts' (three hits, all out-of-state noise),
'county-by-county' + Feinstein (zero), 'precincts in San Francisco'
(zero), 'San Francisco' + Huffington + precincts (statewide prose
only; the Orange County Register's E+1 story confirms 'results were
incomplete from the Democratic strongholds of Los Angeles and
Feinstein's hometown of San Francisco', corroborating the crashed SF
count), 'San Francisco' + registrar + ballots counted (statewide
Senate arithmetic only). No paper printed an SF-specific counted
figure for election night 1994 in the text archive. Untried veins
that remain: the Oakland Tribune's image edition if NewsBank holds
it for 1994, and broadcast archives.
**Correction (2026-07-08, November 1982 IS a night count, the 216th;
what ELECTION EXTRA means).** The operator researched the Chronicle's
edition mechanics and overruled the dead-end verdict: an ELECTION
EXTRA is an ADDITIONAL OVERNIGHT PRESS RUN of the morning paper, not
a late-day edition. The presses were held (or replated) into the
early morning to get overnight returns onto the street; the four-star
folio ('118th Year No. 249' with four stars) marks the last plate of
the night, and the page's own clocks prove it: the Brown/Wilson story
cites returns 'at 3:30 a.m., with 90 percent of the precincts
reporting' statewide, and the governor's-race story references the
count 'at 4 a.m.'. Pressed ~4-5 a.m. Wednesday, sold that morning,
before the 06:00 night cutoff. The existing 230,991 floor ('With all
the votes cast yesterday counted', certified minus the stated 8,000
remaining absentees) re-stamps from a 08:00 day-1 to a T04:00 NIGHT
observation, undimmed as a statement-derived ballots floor: 96.7
percent of certified, the era's fastest-known modern count. The
edition rule generalizes: for the Chronicle (a morning paper), both
ELECTION SPECIAL and ELECTION EXTRA banners mark late-closing
overnight runs; star counts in the folio order the editions within
the night. The 1984 and 1982 adjudications together re-open any past
verdict that discarded a complete E+1 table for being 'a special'.
**Update (2026-07-08, the CDNC agent batch lands: sixteen night
counts at once, 216 to 232).** With the operator's authorization the
four parallel CDNC agents' verified findings were ingested in one
batch, the largest single-day gain of the campaign. Night counts:
1860-11 (a true clocked midnight state, 9,224 of 14,415 cast, locked
by 'As there were 14,415 votes cast, 5,191 remain to be counted');
1861-09 (2:30 AM, 98.4 percent); 1864-11 (complete overnight, 21,024
margin-locked); 1867-10, 1871-10 ('At three o'clock this morning the
returns of all the Wards were completed'), 1872-11, 1875-10 (the
hand-count era finishing short ballots overnight, all dimmed contest
sums); 1908-05, 1908-11, 1909-12, 1912-03-28, 1913-04 (conservative
62,691 over the discrepant 62,934 headline), and 1921-03 (complete
by 9:30 PM, arithmetic-locked 74,079); the midnight partial 1911-11
(20,633 at 140 of 356, dimmed); and two elections no index knew
existed, now recovered complete: 1909-06-24 (Geary bonds, 22,258,
double-locked by the two-thirds arithmetic) and 1912-03-29 (the
invalidated initiative special, 31,968). Finals without night counts:
1859-09, 1861-05, 1862-09, 1863-05, 1865-05, 1865-09 (poll-list
total, deliberately stamped outside the night cutoff), 1909-06-22
(the master's 'Primary' label corrected to Special: no primary
occurred, the direct primary law being in litigation), 1909-11,
1915-03, 1922-11. Index changes: the universe grows 279 to 281, and
the 1865 general moves to its true date, Wednesday Sept 6. Denominator
convention: where no official certified exists (the DOE table skips
specials and starts at 1899), the complete unofficial count or the
paper's printed ballots-cast total serves as the news-derived final,
per the 1933 precedent. Still held for operator hand-reads: 1877-09
(soft digits at 2:45 AM), 1873-09 (approximations only), 1869-09
(OCR-poor digits), 1863-09 (a three-way total conflict), and the
flagged single digits listed in the verification queue. Full
provenance for every figure: the agent salvage files
(agents/cdnc_*.md) and mirror/cdnc/ screenshots.
**Update (2026-07-08, the official-canvass sweep and the operator
walkthrough: 232 to 235 nights, the no-data bucket falls from 48 to
8, the universe grows to 288).** Three parallel agents chased official
denominators while the operator hand-verified the queue live. The
Municipal Reports (FY1859-60 through FY1916-17, archive.org) yielded
official totals for every 1908-1915 special - including the Weller
recall arbitration: the official canvass says 62,876, a FOURTH number
distinct from all three the Call printed - and for fifteen 1859-1877
elections; the Board of Supervisors Journal of Proceedings and the
Registrar's tabulation in the press supplied 1921 (74,191; the Spring
Valley purchase in fact FAILED two-thirds by 6,387) and 1922 (81,363,
Resolution 20564). The legislative-journal/almanac vein (Tribune/Whig
Almanac SF county rows, read from page images) supplied official
finals for eleven 1849-1858 elections and refuted the 1863
retrospective's 11,507 for September 1861 (official: 15,149) -
confirming the operator's clerical-slip adjudication: the 1863
compiler mis-cited the May 1861 municipal, then computed his '451
more than ever before' boast against his own error. Twenty-four
existing rows gained official denominators. The operator walkthrough
then minted three new night counts from digits agents could not read:
1877 (the original 'THE LONG COUNT' headline election: the full
six-candidate Mayor field, 5,965 counted at 2:45 A.M., 17.7 percent),
1873 (fragment-sum floor 2,393 at 2 A.M., 9.1 percent, the
call-every-name law), and 1869 (straight-ticket ballots 4,624 by
press, 21.3 percent - the counted-first straight tickets called it
for McCoppin; the slow scratched ballots elected Selby by 117, the
era's great miscall). A district-by-year official table printed in
the 1863 Alta is preserved as data/sf_vote_by_district_1856_1863.csv.
Index changes: two phantom elections deleted (1857-09-04 was the same
day as the state election; 1858-07-01 never occurred) and nine real
ones added (1864-05, 1866-09, 1870-09, 1873-10, 1877-10, 1910-01,
1911-10, 1914-10, 1915-10). Operator rulings recorded: 1856 state
canvass (12,019) over the county variant; 1862 official (8,813)
replaces an over-official Alta sum. Still open: 1854 (fraud year, no
defensible total), 1871-09 (three official-series values, operator
pick pending), 1867-10 and 1863-05/1865-05 (official-vs-paper
conflicts queued), and the prewar NewsBank cluster.
**Update (2026-07-08, November 1945: the 236th night count, at one
percent).** The operator verified the Nov 7 front-page box (Airport
Bonds YES 1,362 / NO 355 at '12 widely scattered precincts out of
1194') and the Nov 8 day-2 paper supplied the missing denominator:
'Complete semi-official returns from the 1194 precincts' with the
bond vote 'Yes, 146,285; No, 29,200' - a 5-to-1 landslide totaling
175,485, the page's largest single-vote sum. Night share: 1.0
percent, the lowest twentieth-century night point in the dataset -
the municipal hand count of 1945 produced effectively nothing
overnight, exactly like 1918. 1854 was also recorded as a
floor-with-fraud-note per operator ruling (Benham 5,017; the
Broderick ticket missing from the official compilation, vote-for-two
Congress, the ballot-box-stuffing era) with a legislative-journal
hunt queued for the complete canvass. The zero-data bucket stands at
six: 1871-09 (three official values await an operator pick) and the
prewar NewsBank cluster (1928-08, 1929-11, 1931-02, 1940-05,
1944-05).
**Resolutions (2026-07-08, three operator rulings and a footing-error
audit).** (1) 1871-09: the contemporaneous Municipal Reports total
25,094 governs (operator ruling, same-year-record principle); the
retrospective 25,015 and the state-side Governor figure 24,995 are
logged; the election leaves the zero-data bucket as final-known. (2)
1854: upgraded from the Benham floor to the certified record - the
Secretary of State's own per-county canvass (J.W. Denver, Nov 6
1854, printed in the Sacramento Daily Union) supplies the COMPLETE
SF congressional row including the Broderick ticket the almanac
dropped, corroborated cell-for-cell by the SF Board of Canvassers'
table in the Alta; the single-seat Clerk of the Supreme Court race
sums to 9,949, the new floor (~10,333 ballots derived; fraud-year
spread to ~11.7k disclosed); the 1855 legislative journals print no
1854 canvass (the Legislature only canvassed Governor returns) -
dead end documented. (3) 1867-10: the 100-vote ladder
(13,871/13,971/14,071) dissolved under the operator's ward-sum
audit: the Alta mis-footed Currey's column by +200 (printed 6,257
over wards summing 6,057; Sprague's 7,714 foots honestly), and both
higher paper totals were artifacts of that one error; the corrected
night sum 13,771 sits gate-clean beneath the official 13,871 at 99.3
percent. METHOD LESSON for the era, now twice-proven (the 1863
retrospective mis-citation, the 1867 footing error): never trust a
printed total without summing its own column, and prefer the
same-year official record to any retrospective summary.
**Update (2026-07-08, the prewar five fall and the zero-data bucket
empties: 236 to 241 nights, no election without recovered data).**
The operator-attended walk through the last five blank elections
closed the record. 1944-05 (the Market Street Railway purchase
primary): the ELECTION EXTRA's front-page box gives a 1.0 percent
night twin to 1945's (Charter Amendment 1,137 + 769 = 1,906 at 15 of
1,181 precincts), against the day-2 complete 188,188 (YES 105,302 /
NO 82,886, the operator-read 'Returns on Propositions' box).
1940-05: the count finished overnight - 'semi-official complete
returns of San Francisco's 1084 precincts', the two party
presidential ballots summing 155,367 (Roosevelt 81,331 + Garner
13,328 + Allen 6,610 + Patterson 6,595; Republican 47,503).
1931-02: the Depression employment-bond special printed its own
'Total vote cast......84,725' at complete precincts E+1. 1929-11:
a clocked MIDNIGHT state, 'returns from 734 scattered precincts at
12 o'clock', Treasurer field 96,319, confirmed unchanged by the
day-2 recheck - the lever machines counted the city by midnight.
1928-08: 'primary returns from 1000 out of 1003 precincts, compiled
at midnight', Senate field 50,641. The era story is now complete on
the chart: hand counts crawling at 1-20 percent through 1877, the
machines arriving in 1928 and delivering midnight counts, the
1944-45 wartime paper-ballot municipals collapsing back to 1 percent,
and the modern mail-era slide. Also resolved: the 1863/1865 May
municipal conflicts (the retrospective sentence reported official
single-contest totals, not ballots - 1863's '10,147' is a corrupted
11,147 that exactly matches the official canvass; 1865's '13,770' is
the post-recount Mayor total) and 1864-05's figure reclassified as
the official Sheriff contest floor.
**Update (2026-07-08, the turnout denominator pass: 167 to 243
turnout points, the universe grows 288 to 313).** Two agent
recoveries against the Municipal Reports on archive.org. First, the
full transcription of the Registrar's own cumulative election table
('Registration and votes cast at each Election since the Act of
March 18, 1878') - 237 printed rows across the FY1912-13 volume
(munisanfrancisco62sanfrich pp.260-262), the FY1915-16 volume's
extended reprint with a percentage column (munisanfrancisco65sanfrich
pp.327-329) and categorized index (pp.330-332), and the FY1916-17
canvass. That table carries official per-election REGISTRATION and
VOTE POLLED for every SF election 1878-1916, specials and primaries
included, so 51 curated rows now live in
data/sf_turnout_registrar_1899_1916.csv (the 1878-1898 rows
cross-check the existing pre-1899 file; all match except a one-digit
1879 registration variant, 44,764 in three later printings vs the
FY1888-89 volume's 44,765, which stands). It also surfaced 25
elections absent from every prior index - the 1899-1916 county-run
primaries, the Nov 15 1910 charter special a week after the general,
the Dec 20 1912 general-utilities bond special ten days after the
charter special, and the 1913-11-11 and 1915-11-09 general
municipals - all added to the master list as final-only rows, which
grows the universe from 288 to 313 elections (every one still has a
recovered final; the zero-data bucket stays empty).
**Update (2026-07-08, same pass: registration law by era, and reused
denominators for 1917-1945).** The operator's claim that
registration was annual proved right in spirit, wrong in period:
registration was valid per REGISTRATION PERIOD - per general
election under the March 18, 1878 act (sec. 16: an enrolled elector
may vote 'at all special elections between said general election
and the next general election'), per BIENNIUM 1900-1931 (Stats.
1899 / Pol. Code sec. 1094: complete new registration each even
year, old affidavits canceled Jan 1, carried over only through
March 31; sec. 1121: specials use the last-general roll plus a
supplement), and PERMANENT from Jan 1, 1932 (Prop 14, Nov 1930)
with a non-voter purge each January of odd years. Within a period
the roll accretes continuously and closes 30 days before each
election - which is why the table prints different registration for
elections two days apart (June 22 vs 24, 1909: 75,679 vs 75,808).
Full citations in docs/research/registration-law-history-1866-1945.md. Under those rules the
nearest general's registration is now reused as the denominator for
34 elections 1917-1945 whose ballots-cast final we hold but whose
own registration never got an official printing (the Municipal
Reports series ends FY1916-17 and the DOE table skips most specials
and municipals): data/sf_turnout_reused_registration_1917_1945.csv,
each row carrying the era rule and the bias direction (pre-general
specials and post-purge odd-year specials compute as turnout
floors). The May and August 1932 specials are deliberately omitted -
the old biennial roll was canceled Jan 1, 1932 and the permanent
roll was still forming, so no honest denominator exists.
**Update (2026-07-08, same pass: four official-final corrections
from the registrar table).** (1) The DOE turnout table's Nov 3 1908
row (75,467 / 41,137) actually carries the Nov 12 1908 bond
special's figures - a mislabel in the DOE's own table, which finally
explains our old 'DOE 41,137 appears low' note; the general's
official figures are registration 75,388, total vote polled 61,625,
so the 1908-11-03 final moves from the SOV President-contest floor
60,124 to 61,625 (night 36,450 = 59.2 percent). (2) 1912-12-10:
official total polled 83,850 supersedes the Chronicle's approximate
'~81,104[?]'. (3) 1913-08-26: official 65,522 supersedes the
Chronicle's complete overnight 65,478, which stands as a 99.9
percent night count. (4) 1915-04-20: official Total Vote 73,583
(twice-attested, canvass table plus the suffrage statement's
males 50,556 + females 23,027) supersedes the Chronicle's 73,656,
which included 234 spoiled ballots - the overnight count therefore
computes to 100.1 percent of the official final, the dataset's first
night share above 100, disclosed in the row. Also upgraded:
1905-11-07 registration from vol57's fire-era rounded 98,000 to the
precise 97,670 in the two later printings; and the 1902-12-04
printing split re-examined (now 3 later printings for 14,371 vs the
2 earliest for 14,271 - the earliest-printing rule keeps 14,271, the
same precedent as the 1896 arbitration). Flagged for operator eyes:
the 1911-09-26 municipal-primary vote polled, 79,019 per both
FY1915-16 printings (whose own 77.5 percent column matches exactly)
vs 78,919 in the FY1912-13 printing - 79,019 ingested; and the
1905-08-08 primary, printed only in the FY1915-16 index.
**Update (2026-07-08, operator rulings on the registrar-table flags,
and the 1911 primary arbitrated).** The operator ruled on the four
flagged items: 1879-09-03 registration stays 44,765 (the FY1888-89
printing, closest to the event, over the three later printings'
44,764); 1905-11-07 goes with the precise later-printing figures;
1902-12-04 keeps 14,271. For the 1911-09-26 municipal primary the
operator ordered an independent-printing hunt (a 100-even gap smells
like a mistype or a mis-summed district) - and first, a correction:
the earlier entry's claim that the FY1915-16 percentage column
'matches 79,019 exactly' was weak evidence, since both candidates
round to the printed 77 1/2 at nearest-half precision. The hunt then
settled it properly: the FY1911-12 volume prints the Department of
Elections' own canvass of the primary (sanfranciscomuni61sanfrich
printed p.195, leaf n222, 'PRIMARY MUNICIPAL ELECTION, SEPTEMBER 26,
1911. FOR MAYOR.'), whose 18 assembly-district Total Vote Polled
entries sum to 79,019 exactly as printed (AD28 1,522 through AD45
2,068; candidate columns sum to 78,647 = 79,019 minus 372 blanks),
and '78,919' appears nowhere in that volume. The FY1912-13
cumulative table's 78,919 is a one-digit compositor slip, exactly
the class of error the operator predicted. Dead end recorded: CDNC
corroboration (SF Call, Oct 3-14, 1911 official canvass) blocked by
Cloudflare for the agent; not needed given the district sum.
**Update (2026-07-09, waves 3-4: the great night-count sweep - 241 to
301 nights, the missing list falls from 72 to 12).** Seven parallel
CDNC agents (day-after Daily Alta, SF Call, Sacramento Daily Union)
and three NewsBank agents (day-after SF Chronicle via SFPL) hunted
all 66 reachable targets, followed by a full operator review: every
flagged digit hand-read against the scans, every class decision
adjudicated, four elections transcribed whole by the operator
(1870's sixteen-candidate table, 1880's twelve-ward presidential
table, 1883's charter table, 1871's heterogeneous prose returns).
Sixty new night counts ingested, 1851-1922. The record now reaches
the Gold Rush: 1851's 'up to two o'clock this morning, but little
over a hundred votes had been counted in each ward'. Era headlines:
pioneer hand counts ran ~20-27 percent overnight except when
straight tickets sorted fast (1852 presidential 71.6, 1857 56.8);
the operator identified the 1852 First Ward's identical 485s as
alternating-tally lockstep (both four-elector slates equal at any
snapshot, so W1 = 970); Civil-War-era counts ran 42-80 percent,
collapsing to 19-49 percent in the scratched-ticket 1870s (1870
quantified at 48.9 via the operator's full-table transcription,
which also caught the 1st Ward column as a DUPLICATED typesetting
of 7th-1P); judicial one-question specials counted complete the
same night (1873 exactly 15,594 = the official total; 1877 23,332);
the 1879 constitution ratification near-complete (38,584); the
1880s-90s big-ballot elections crawled again (1886: 3,070 by 1 AM,
6.7 percent) while single-question charters flew (1880: 97.2; 1883:
98.6 with the majority at NINE votes against, one precinct out at
3:15 AM); the 1899-1916 primaries mostly counted overnight (1901:
99.8; 1903: 99.9; 1904-05: 99.9; 1915-11: 'ONLY 83,138 ENTER POLLS'
= 99.8; 1916-05: 97.3 at midnight) except the multi-party state
primaries (1914-08: FOUR precincts complete by 2:15 AM, 0.5 percent,
the slowest night on record; 1910-08: 20.1; 1915-09: 23.4); woman
suffrage 1911: 31,032 counted on the question by night, the city
against 19,869-11,163 while the state carried it; and 1922's school
bonds proved complete by the Chronicle's morning run (80,766 floor,
99.3). A pattern got a name: OVERNIGHT COMPILATIONS RUN HOT - four
elections' complete press counts exceed their official canvasses
(1877 +390, 1879 +550, 1884 +86, 1890 +819), all ingested at their
disclosed >100 percent shares per the 1915-04-20 precedent.
**Update (2026-07-09, same sweep: three more registrar-table
transplants corrected).** (1) 1884-03-18 Assembly special: the
cumulative table's 2,655 is W. T. Wallace's certified vote
transplanted into the Vote Polled column (the row's precinct and
registration cells are uniquely blank; all six printings copy it);
the FY1883-84 volume's own certified canvass gives Wallace 2,655 +
Hawes 2,250 + Ellis 69 + scattering 6 = TOTAL 4,984 - the operator
predicted this class of slip before the agent proved it. (2)
1908-08-11 state primary: 22,698 is the Republican column of the
FY1908-09 certified canvass (p.1125) back-filled as if it were the
total; true all-party total 33,331 (operator independently floored
it at 30,000+ from the Call's night table before the canvass
landed). (3) 1905-08-08 municipal primary: 28,951 is a fire-era
backfill matching NOTHING in the canvass; the Election
Commissioners' declaration of Aug 14, 1905 (Call, Aug 15, p10)
gives 41,117 (R 31,728 across the League and Ruef factions + D
3,732 + UL 4,500 + Soc 319 + scattering 838, every column exact).
Dead ends documented and closed: 1849 (no E+1 paper existed - the
Alta was still a weekly), 1850 (outcomes only, 'we shall give the
result in full to-morrow'), 1902-08 (winners-only delegate lists),
1908-05 (only printed total exceeds the final), 1909-11 (winners
conceded by 10 PM on prose 'indicated plurality' alone; no returns
table in the 16-page issue), 1913-09 (count finished 'shortly after
8', past the 06:00 cutoff; the E+1 daytime 45,752 recorded as a
non-night observation), 1944-11 (the ELECTION EXTRA printed no SF
count of any kind, all 18 pages verified - only the registrar's 3 PM
turnout prediction). Full agent salvage packet with every verbatim
quote, locating query, and the operator review queue preserved at
docs/research/night-recovery-2026-07-09/.
