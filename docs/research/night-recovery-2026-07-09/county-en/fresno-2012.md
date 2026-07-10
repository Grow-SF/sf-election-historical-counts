# Fresno County 2012-11-06 (presidential-general) election-night recovery

Task 6. Certified final: 261,652 ballots (CA SoS SoV). Prior state: null, extensive
GEMS/Wayback/Task-9-enumeration dead-end history already in `fresno-ca.json`'s note
(no election-night-named report file was ever archived under
www2.co.fresno.ca.us/2850/Results/ for this year). Coverage: Fresno Bee, The (CA) is
a HIT for the 2012-11-07/08 window (14 articles matching "ballots") per
`00-newsbank-coverage.md`.

## Searches (NewsBank Access World News, SFPL ezproxy, source = Fresno Bee, The (CA))

- `"ballots counted"` AND source AND 11/07/2012-11/09/2012: 0 hits.
- `Salazar ballots` AND source AND 11/07/2012-11/09/2012: 0 hits. (Victor Salazar was
  registrar through 2013, but Brandi Orth, already county clerk since 2011, is the
  official quoted throughout the Bee's 2012 coverage; Salazar does not appear.)
- `"votes counted" "Fresno County"` AND source AND 11/07/2012-11/09/2012: 2 hits
  (both the same "Trend looks good for Jim Patterson" Assembly-race piece, precinct
  percentages only, not countywide).
- `"precincts reporting" "Fresno County"` AND source AND 11/07/2012-11/09/2012: 3 hits
  (Patterson piece again + a library-tax piece, no countywide ballot total).
- `"Fresno County" ballots counted` (no quotes) AND source AND 11/07-11/10/2012:
  10 hits, mostly City Council/library-tax/Assembly race pieces, no exact countywide
  total.
- `"left to count" "Fresno County"`, `"remain to be counted" Fresno`,
  `"provisional ballots" "Fresno County"`, `"election night" "Fresno County"` AND
  source AND 11/07-11/10/2012: surfaced the two decisive articles below.
- Opened and mirrored (gitignored `mirror/newsbank/`):
  - "Valley voters turn out in droves" (Nov 7 2012, docref news/142721EBA095B490):
    turnout color only, no ballot count.
  - "Valley ballot-counting continues - In Fresno County alone, 98,000 ballots still
    must be tallied" (Nov 8 2012, docref news/142721EBD5B41378, Pablo Lopez): **the
    decisive find.**
  - "Election throws Valley GOP roots deep" (Nov 10 2012, docref
    news/142872B3AAB99388): the **bracketing** find (Political Notebook item "Vote
    counting continues with little change").

## The finding

Nov 8 2012 (Thursday), Fresno County Clerk Brandi Orth: "So far, about 160,400
ballots have been counted, putting voter turnout at 39.1%." (160,400 / 410,188
registered = 39.10%, matches Orth's stated turnout exactly, confirming the quote is
countywide and not race-specific.) The same article: "election workers will work
double-shifts and Saturdays to count a record 98,000 uncounted ballots" and Orth
"plans to update vote totals every Friday and Wednesday on the county's website."

Nov 10 2012 (Political Notebook, "Vote counting continues with little change"):
"Fresno County on Friday did its **first vote-count update since Tuesday's
election**, and not much has changed... Fresno County counted 19,000 absentee
ballots since election night and has 78,000 still to count."

This second article is the non-circular bracket: it explicitly states that Friday's
release was the FIRST update since election night, i.e. no county release moved
the count between Tuesday night and Thursday's article. So the 160,400 figure
quoted Thursday is the frozen election-night state, not a mid-week update.
Cross-check: 160,400 + 19,000 (added by Friday) + 78,000 (still outstanding after
Friday) = 257,400, close to certified 261,652 (remaining gap = further weeks of
processing to the Dec 4, 2012 certification deadline). Also self-consistent with
Thursday's own "record 98,000 uncounted" framing: 160,400 + 98,000 = 258,400.

Arithmetic: 160,400 / 261,652 = 61.30%. Calibration: within the task's expected
55-70% band for 2012, and below Fresno's own 2016 presidential plateau (60.70%,
comparable magnitude for a like-for-like presidential year).

## Verdict

CONFIRMED (plateau_review.json): self-describes as the through-election-night
state (Orth's own words, county released nothing until Friday) plus the RUNBOOK-8
non-circular leg "the county's own posting schedule bracketing the report"
(explicit "first vote-count update since Tuesday's election").

## Landed

`fresno-ca.json` 2012-11-06 row: election_night_ballots=160400,
election_night_pct=61.3, confidence=secondary, source_url_night=
https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=news/142721EBD5B41378
render_verified.json entry added (method newsbank-sfpl-manual). VERIFY.md table +
detail bullet updated. plateau_review.json CONFIRMED entry added.
