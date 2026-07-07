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
