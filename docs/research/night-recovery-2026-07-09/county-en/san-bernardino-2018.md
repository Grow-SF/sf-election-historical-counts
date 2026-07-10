# San Bernardino 2018-11-06 election-night plateau: NewsBank search log (Task 7)

Registrar: Michael Scarpello (2011-2018 era; Bob Page took over ~2018). Source: found via
Press-Enterprise regional Inland Empire piece (SCNG shared coverage after 2016) while researching
Riverside 2018 -- same article covers both counties.
Existing row: certified_final 546,041; election_night_ballots null.
Calibration: SB precinct-era expect ~55-75%.

## FINDING (2026-07-09, carried over from riverside-2018.md research)

"Elections - Many Inland ballots still not processed or counted" (Nov 8, 2018 Press-Enterprise,
docref news/16F9051D0AED5530, byline Johnny Bender):

"Final unofficial vote counts aren't expected to be released until 6 p.m. today for Riverside
County and 4 p.m. Friday for San Bernardino County."

"In San Bernardino County, elections workers counted about 322,000 ballots overnight Tuesday. On
Wednesday, about 150,816 ballots remained to be counted, along with 8,929 damaged ballots and
43,818 provisional and other ballots that require processing."

"There are 942,474 registered voters in San Bernardino County, so the unofficial turnout estimate
is about 55 percent."

DIRECT statement (not a subtraction derivation): "elections workers counted about 322,000 ballots
overnight Tuesday" -- squarely the election-night plateau. Cross-check: Wednesday's remaining
total (150,816+8,929+43,818 = 203,563) implies a Wednesday-state count of 546,041-203,563=342,478,
somewhat HIGHER than the directly-stated 322,000 overnight-Tuesday figure -- consistent with a
modest amount of same-day Wednesday processing occurring between the overnight count and the
moment this article's "remained to be counted" figures were gathered (SB's own final unofficial
count was not due until 4 p.m. Friday, so some incremental Wednesday work before that is
expected and does not contradict the overnight figure).

PLATEAU = 322,000 (directly stated, "overnight Tuesday").
322,000 / 546,041 = 58.97%. Within the ~55-75% precinct-era calibration band.

LANDED: election_night_ballots 322000, pct 58.97, confidence secondary, comparable true,
plateau_review CONFIRMED (direct overnight-count statement; the Wednesday remaining-ballot count
in the SAME article is a consistent, slightly-later data point, i.e. an internal cross-check, not
a contradiction). Source: news/16F9051D0AED5530.

### Fix pass (2026-07-09, Task 7 review finding 2: reclassify CONFIRMED -> ceiling)

Reclassified from CONFIRMED to REFUTED_AS_PLATEAU / documented ceiling, comparable:false.
The source article schedules San Bernardino's own final unofficial release for 4 p.m. Friday
(movement still pending after election night), unlike Riverside in the same article which had
a same-day "not counting anything today" freeze quote. The only leg used to support 322,000 as
a held plateau was a same-article arithmetic cross-check (turnout-estimate math and the
546,041-minus-remaining=342,478 calculation), which RUNBOOK 8 disallows as circular/non-
independent; that same arithmetic in fact shows a HIGHER state (342,478) already prevailing by
Wednesday than the claimed overnight-Tuesday 322,000. 322,000 is retained only as a documented
plateau CLAIM / ceiling: it may be directionally close to the true election-night count but
cannot be verified against movement evidence the way this county's own 2018/2024 rows or
Riverside's same-day figure can. Also restored the pre-existing (ca18c89) note text to
append-only (it had been condensed when the original RECOVERY text was appended) and added a
round-number caveat for the "about 322,000" figure. plateau_review.json, VERIFY.md (⚠️ cell +
FLAG bullet), county_night.json (comparable:false), and render_verified.json all updated to
match.
