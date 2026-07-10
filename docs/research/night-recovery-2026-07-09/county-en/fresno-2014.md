# Fresno County 2014-11-04 (midterm-general) election-night recovery

Task 6. Certified final: 163,420 ballots (CA SoS SoV). Prior state: null, extensive
GEMS/Wayback dead-end history already in `fresno-ca.json`'s note. Coverage: Fresno
Bee, The (CA) is a HIT for the 2014-11-05/06 window (17 articles matching "ballots")
per `00-newsbank-coverage.md`.

## Searches (NewsBank Access World News, SFPL ezproxy, source = Fresno Bee, The (CA))

- `"ballots counted"` AND source AND 11/05/2014-11/07/2014: 1 hit ("Brown wins;
  voter turnout is low" -- a STATEWIDE controller-race percent, "With 63% of the
  ballots counted, Swearengin was behind Yee 52.2%", not a Fresno County figure).
- `Orth ballots` AND source AND 11/05-11/07/2014: 4 hits, including "Catalano, Soria
  wait for last batch of ballots to be counted" (Nov 6) -- led to opening the
  "Vote update" article below.
- `"votes counted" "Fresno County"` and `"precincts reporting" "Fresno County"` AND
  source AND 11/05-11/07/2014: turned up "Digesting the results" and various local
  race pieces (Zoo tax, judge race, supervisor races), no direct countywide total.
- `"ballots left to count"`, `"Fresno County" ballots counted`,
  `"registrar of voters" Fresno` extensions: surfaced "2014 ELECTION RESULTS"
  (results table, no countywide ballots-cast total, county races only), and
  re-surfaced "Digesting the results" and "Soria takes council race lead."
- Opened and mirrored (gitignored `mirror/newsbank/`):
  - "Brown wins; voter turnout is low" (Nov 5 2014, docref news/1516BFAE2A681058):
    no Fresno County countywide ballot count.
  - "Digesting the results - Shocker..." (Nov 6 2014, docref
    news/15171395564B90B8, John Ellis): **the decisive find.**
  - "Soria takes council race lead - Vote update" (Nov 8 2014, docref
    news/151AB2A3C7094500): the **bracketing** find.
  - "2014 ELECTION RESULTS" (Nov 6 2014, docref news/15171395B2FDF098): full
    results table, county race totals only, no countywide ballots-cast figure.

## The finding

Nov 6 2014 (Thursday), "Digesting the results": "With the Election Day ballot
counting finished, Tacherra holds a slim 736-vote lead over Costa" (in percentage
terms 50.5%-49.5%), and later: "If a third of the approximately 42,600 Fresno
County mail and provisional ballots left to count are from the 16th District..."
-- i.e. approximately 42,600 mail/provisional ballots remained uncounted
countywide once "Election Day ballot counting" was finished.

Nov 8 2014 (Saturday), "Soria takes council race lead - Vote update": "The initial
vote totals -- posted early Wednesday morning after Tuesday's election -- showed
Catalano ahead by 20 votes" (i.e. the first post was Wednesday morning, an
extension of election night's own count) versus "An updated count released at
3 p.m. Friday." Separately: "The Fresno County elections office has plowed through
more than 22,000 absentee and provisional ballots that remained to be counted after
Tuesday night," and (as of that same Friday release) "County Clerk Brandi Orth said
10,300 absentees and 10,100 provisionals from throughout the county remain to be
counted" (20,400).

Cross-check: total remaining after Tuesday night = ~22,000 (processed by Friday) +
20,400 (still remaining as of Friday) = ~42,400, matching the Thursday article's
"approximately 42,600" within rounding. This also confirms no county update was
released between the Wednesday-morning post and Friday 3 p.m. -- otherwise the
Thursday article's figure would predate a since-superseded number, not the
still-current one.

Arithmetic: 163,420 certified minus ~42,600 = 120,820 counted through election
night = 73.93%.

Calibration cross-check: this is above the task's ~50-65% guidance band for 2014,
but San Diego County's own CONFIRMED 2014 row (data/research/election-night/
san-diego-ca.json) lands at 73.54% for the SAME election, a close independent
match. Fresno's own Nov 5 2014 Bee coverage calls this "What may be the lowest
voter turnout for a mid-term general election in state history" -- a smaller,
more front-loaded mail/in-person mix plausibly explains a higher-than-2016/2018
first-report share for this specific low-turnout midterm.

## Verdict

CONFIRMED (plateau_review.json): self-describes as the state once "Election Day
ballot counting" was finished, plus the RUNBOOK-8 non-circular leg (the county's
own posting schedule bracketing the report: nothing released between the
Wednesday-morning post and Friday 3 p.m.).

## Landed

`fresno-ca.json` 2014-11-04 row: election_night_ballots=120820,
election_night_pct=73.93, confidence=secondary, source_url_night=
https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=news/15171395564B90B8
render_verified.json entry added (method newsbank-sfpl-manual). VERIFY.md table +
detail bullet updated. plateau_review.json CONFIRMED entry added.

## Fix pass (2026-07-09, review, Finding 2)

Re-read both mirrored articles (`mirror/newsbank/2014-digesting-the-results.txt`,
`mirror/newsbank/2014-soria-vote-update.txt`) in full against the reviewer's finding
that the Nov 6/Nov 8 two-article bracket is an arithmetic coincidence (~42,600 vs
~22,000+20,400=~42,400 from two independently-approximated figures), not an explicit
county-schedule-bracketing statement like 2012's "first vote-count update since
Tuesday's election" or 2018's "will not announce updated vote totals until Friday
afternoon". Agreed: downgraded verdict CONFIRMED to PLAUSIBLE in `plateau_review.json`
and `fresno-ca.json` (dated append, prior text preserved).

Also confirmed the reviewer's required disclosure: "Digesting the results" states
Merced County's remaining-ballot figure as "officials said late Wednesday," but its
own Fresno County figure ("approximately 42,600 Fresno County mail and provisional
ballots left to count") carries no such attribution -- it may be the reporter's own
approximation rather than a stated official count. Appended to both `fresno-ca.json`
and `VERIFY.md`.

Comparable determination: re-read confirms comparable stays TRUE. The Nov 6 article's
736-vote Costa-Tacherra lead (quoted in the same breath as the 42,600 figure) is
independently identified by the Nov 8 "Soria" article as the state "on election
night" ("Madera's update pushed Republican Tacherra's lead -- 736 on election night --
to 1,775"), and that article separately establishes the Wednesday-morning post held
frozen until Friday's updates across all the county races it covers. So the
Thursday-dated 42,600 figure describes the frozen Tuesday-night/Wednesday-morning
plateau, not a later Thursday-specific state; it targets the plateau directly, same
as the Madera 2014 CEILING precedent would require IF the snapshot had instead been
shown to be a later state (it was not).

Numeric fields (120,820 / 163,420 = 73.93%) unchanged. Only the verdict and note/
VERIFY.md prose changed, via dated appends.
