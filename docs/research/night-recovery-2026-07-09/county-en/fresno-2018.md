# Fresno County 2018-11-06 (midterm-general) election-night recovery

Task 6. Certified final: 256,972 ballots (CA SoS SoV). Prior state: null, extensive
GEMS/Wayback dead-end history already in `fresno-ca.json`'s note (the county's own
results page's earliest Wayback capture is a 2018-11-28 canvass snapshot at 239,032;
gvwire and the Fresno Bee's own site were curl/WebFetch-blocked, previously flagged
for manual operator follow-up). Coverage: Fresno Bee, The (CA) is a HIT for the
2018-11-07/08 window (31 articles matching "ballots") per `00-newsbank-coverage.md`.
This task's NewsBank access (real logged-in Chrome via puppeteer, SFPL ezproxy) is
exactly the manual-operator route the prior note flagged for.

## Searches (NewsBank Access World News, SFPL ezproxy, source = Fresno Bee, The (CA))

- `"ballots counted"` AND source AND 11/07/2018-11/09/2018: 2 hits, both bare page
  scans (no headline text captured).
- `Orth ballots` AND source AND 11/07-11/09/2018: 7 hits, including "It's all over
  but the counting" (Nov 8) -- **the decisive find** -- and "Election 2018 results"
  turnout piece.
- `"votes counted" "Fresno County"` and `"precincts reporting" "Fresno County"` AND
  source AND 11/07-11/09/2018: surfaced local-race pieces (parks tax, council,
  senate district) and page scans, no additional countywide total.
- `"100,000" ballots Fresno` AND source AND 11/07-11/10/2018: 5 hits, re-surfacing
  "It's all over but the counting" plus the turnout piece and page scans.
- Opened and mirrored (gitignored `mirror/newsbank/`): "It's all over but the
  counting" (Nov 8 2018, docref news/16F940DF80FB53D8, Barbara Anderson).

## The finding

Nov 8 2018 (Thursday), "It's all over but the counting": "Election Day is over, but
there are still 100,000 vote-by-mail and provisional ballots left to count in
Fresno County. Registrar Brandi Orth said Wednesday morning that the process of
counting about 76,000 mail-in ballots had begun... 'We don't anticipate we will get
all of those done this week,' she said. Once the vote-by-mail ballots are counted,
her office will turn to the provisional ballots... 'we have to hand research each
of the 24,000 provisionals'" (76,000+24,000=100,000). Crucially: "Fresno County
will not announce updated vote totals until Friday afternoon, Orth said" -- i.e.
no county release moved the public count between the Wednesday-morning statement
and Friday, so 100,000 outstanding is the frozen post-election-night state.

Arithmetic: 256,972 certified minus 100,000 = 156,972 counted through election
night = 61.09%.

Consistency check against this row's own already-documented 2018-11-21 canvass
snapshot (239,032 of 455,662, 100% of 640 precincts, from the co.fresno.ca.us
results-page embed): 156,972 (night) -> 239,032 (day 15) -> 256,972 (certified) is
a smooth, plausible canvass curve.

Calibration: 61.09% is within the task's ~50-65% expected band for 2018 and close
to Fresno's own 2016 presidential plateau (60.70%) and 2024 (62.36%).

## Verdict

CONFIRMED (plateau_review.json): self-describes as the state Wednesday morning
right after election night (the process of counting the outstanding mail-in
ballots "had begun," i.e. not yet reflected in the public total) plus the
RUNBOOK-8 non-circular leg (the county's own posting schedule bracketing the
report: no update until Friday afternoon).

## Landed

`fresno-ca.json` 2018-11-06 row: election_night_ballots=156972,
election_night_pct=61.09, confidence=secondary, source_url_night=
https://infoweb-newsbank-com.ezproxy.sfpl.org/apps/news/document-view?p=WORLDNEWS&docref=news/16F940DF80FB53D8
render_verified.json entry added (method newsbank-sfpl-manual). VERIFY.md table +
detail bullet updated. plateau_review.json CONFIRMED entry added.

## Note on scope

Fresno 2022-11-08 (the fourth year in this task's brief) was independently landed
by a concurrent task (Task 9, commit 1b62e29, 126,440/221,419 = 57.10%, CONFIRMED)
before this task reached it; per the coordinator's explicit instruction this task
left that row untouched. All four Fresno rows (2012, 2014, 2018, 2022) plus the
already-CONFIRMED 2016/2024 rows are now landed, so Fresno reaches the chart with
a complete six-election series.

## Fix pass (2026-07-09, review, Finding 1)

Reviewer flagged that this row's landed leg rests entirely on ONE article (Nov 8
2018 "It's all over but the counting"), whose only bracketing evidence is Orth's own
forward-looking promise ("Fresno County will not announce updated vote totals until
Friday afternoon") -- never confirmed by a second, later source that the promise was
kept (the pattern the 2012 row uses: a companion Friday-or-later piece).

Ran the requested NewsBank search (Fresno Bee, Nov 9-12 2018 window, real logged-in
Chrome on port 9222, puppeteer-core `connect({browserURL:'http://127.0.0.1:9222'})`
reusing `(await browser.pages())[0]`, 2-3s between searches):

- `"Fresno County" ballots update` 11/09-11/12/2018: 2 hits, including "Election 2018
  - Hurtado increases lead, Janz closes slightly on Nunes" (Nov 11 2018, docref
  news/16FA94EDA82A6CC8) -- **the decisive find**.
- `Orth count Friday` 11/09-11/12/2018: 0 hits.
- `"votes counted" Friday` 11/09-11/12/2018: 0 hits.
- `"100,000 ballots"` 11/09-11/12/2018: 0 hits.
- `"updated vote totals" Friday` 11/09-11/12/2018: 0 hits.
- `Orth "ballots" counted` 11/09-11/12/2018: 0 hits.
- Follow-up sanity checks for an earlier (Wed/Thu) interim update:
  `"Fresno County" "vote count" Thursday` 11/08-11/09/2018: 0 hits.
  `Fresno "vote totals" Wednesday` 11/07-11/09/2018: 3 hits, all the already-known
  Nov 8 "It's all over but the counting" (no distinct interim-update article).

Opened and mirrored (gitignored `mirror/newsbank/2018-hurtado-janz-nunes-friday-
update.txt`): "Election 2018 - Hurtado increases lead, Janz closes slightly on
Nunes" (Nov 11 2018, docref news/16FA94EDA82A6CC8, Rory Appleton): "Several central
San Joaquin Valley counties updated their election results Friday... Fresno County
-- About 23,000 of the 100,000 remaining ballots were counted and included in a
Friday update from the Fresno County Clerk's office. The next update on the
remaining 77,000 votes will come Wednesday at 3 p.m." (100,000-23,000=77,000,
arithmetic checks out).

This is a genuinely separate article (published Nov 11, three days after the
original Nov 8 piece, by a different byline) independently confirming that Orth's
promise was kept: no county release moved the 100,000-outstanding count between
election night and Friday's update, matching the 2012 row's gold-standard
bracketing pattern (two independent articles) rather than resting on a single
article's forward-looking statement alone.

## Verdict (updated)

CONFIRMED stands, now with an independent bracketing leg in addition to the
self-describing Wednesday-morning statement. Numeric fields (156,972 / 256,972 =
61.09%) unchanged.

## Landed (correction)

`fresno-ca.json` 2018-11-06 note: dated append (2026-07-09) adding the Nov 11 2018
docref and quote. `plateau_review.json` evidence/basis updated to cite the new leg
(verdict unchanged, CONFIRMED). `VERIFY.md` detail bullet appended with the same
correction. `render_verified.json` unchanged (source_url_night still the original
Nov 8 docref; the new article is corroborating evidence in the note/plateau_review,
not a new numerator source).
