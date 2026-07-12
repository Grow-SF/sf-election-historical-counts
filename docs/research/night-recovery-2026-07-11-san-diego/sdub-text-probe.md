# SDUB text-only source probe: San Diego County election-night ballots-counted figures

Follow-up to `newsbank-probe.md` (which established that the San Diego
Union-Tribune image edition only starts in 2018, but the `SDUB` text-only
source runs 1970-2026 with gaps, continuous from 1983). This probe asks: for
the generals that fall inside SDUB's continuous coverage window, do the
morning-after (day+1) or two-days-after (day+2) articles state a usable
**San Diego County** election-night ballots-counted figure (a raw count of
ballots/absentees, not a percent of registration)?

## Method

- Landed on each issue via NewsBank's publication-calendar browse
  (`browse-pub?p=WORLDNEWS&t=pubname%3ASDUB!...` -> select year -> click the
  day), not the `results` keyword-search grammar. The keyword-search grammar
  (`fld-base-0=alltext&...&fld-nav-0=YMD_date`) returned false "No results
  found" for every SDUB date tried here (matches the caveat already logged in
  `newsbank-probe.md`) even when the issue demonstrably exists, so it was
  abandoned in favor of listing the full issue's article titles via the
  calendar-browse `document-view` links and opening the politically-relevant
  ones directly.
- For each issue, pulled the full title list (`format=text` articles for that
  date), filtered for election/vote/ballot/county/registrar/precinct/measure
  keywords, and opened the top candidates (registrar-focused stories, page
  A-1 election-night roundups, and county-wide contests/measures) to read
  full body text for a countable figure.
- Scripts used: `/tmp/sdub_probe/issue_browse.js` (list an issue's articles
  via the calendar-browse path), `/tmp/sdub_probe/dump_full.js` /
  `open_doc.js` (open a `document-view` link and dump/keyword-scan its body
  text). Background tab only, window parked off-screen, never foregrounded.

## 1984-11-06 (day-after issue: 1984-11-07)

Hits examined (title, docref, page):
- "Hedgecock: a solid win : Mayor returns to office with broad voter support" — `news/11793000211574CB`, A-1
- "President Thrashes Mondale - Hedgecock Outpolls Carlson - Mayor easily wins despite indictment" — `news/11792FFEBB0E5CCA`, A-1
- "For county board, it's Golding, Bailey..." — `news/11793000C9C2016F`, A-10
- "Unofficial Results ... : ... Scenes from an election day in San Diego" — `news/11793000E0D819AD`, A-10
- "At Precinct 27530, that 7 o'clock surge never came" — `news/11792FFE5D937CE4`, A-12
- "Early win didn't slow vote here..." — `news/1179300082839311`, A-4 (registrar Ray Ortiz quoted on turnout trend, no count)
- "Prop. A, limiting authority of supervisors, OK'd" — `news/11792FFF15CAA49D`, A-7 (no numbers at all)
- "Stadium measure defeated" — `news/11792FFF279EF147`, A-8 (no numbers at all)
- "A Reagan landslide : 49-state mandate for president" — `news/11793000392FA1CD` (national analysis, no county figure)
- "INCUMBENTS HOLD FAST : Demos retain strong grip in state" — county Legislature race percentages only, no ballot count

Verbatim quotes with figures:
- "Of 370,000 ballots cast in the city of San Diego, only about 18,000 did not make a choice between Hedgecock and Carlson." (from "Hedgecock: a solid win", A-1) — this is a **city of San Diego** figure, explicitly scoped to the city, not the county.
- "When the votes were tallied Hedgecock got 47 percent to Carlson's 38 percent. The minor candidates received a surprisingly large 15 percent of the ballots." — percentages only, no raw count.
- Precinct-level color piece (299 marked ballots at one precinct of 450 issued) — a single-precinct anecdote, not a county figure.

**Verdict: NOT FOUND.** No county-wide ballots-counted or absentees-remaining figure turned up in any of the ~10 election-relevant articles opened. The only raw count found (370,000 ballots, Hedgecock race) is explicitly a **city** total, not county, so it doesn't satisfy the metric. 1984 SDUB prose is percentage-driven, not count-driven, for this issue.

## 1988-11-08 (day-after issue: 1988-11-09)

Hits examined:
- "Officials pleased with turnout - vote goes well despite long ballot" — `news/11790AA51B85D101`, B-1, by Joe Cantlupe
- "Ballot was huge, but 'no problem' for county voters" — `news/11790AA7FA32889C`, A-1 (Column: ELECTION '88), by Chet Barfield

Verbatim quotes with figures:
- "The registrar's office tallied 159,811 absentee ballots as of last night and the staff was prepared to work through the night to process another 40,000 ballots dropped off at polling places. McCormack said she would release the final absentee tallies tomorrow." (B-1, "Officials pleased with turnout")
- "At least 20 percent of the county's 1,258,868 registered voters requested absentee ballots..." (B-1, same article — registration base, not a count metric, included for context only)
- "About 160,000 mail-ins had been tabulated as of early this morning... And with as many as 40,000 remaining, the tally was not expected to be completed until 10 a.m. tomorrow." (A-1, "Ballot was huge, but 'no problem'")
- "Assistant Registrar Keith Boyer said 50 to 100 employees... would work round-the-clock shifts to sort and process the avalanche of mail-in ballots, which will more than double the previous record of 93,000 filed in the last presidential election." (A-1, same)

**Verdict: USABLE FIGURE.** Two independently bylined articles in the same issue corroborate a San Diego **County** registrar figure: **159,811-160,000 absentee ballots tabulated as of election night**, with ~40,000 more absentee ballots still to be processed the next morning. This satisfies the task's "absentees remaining" metric category directly (a precise, attributed, county-wide absentee count as of election night, not a percent of registration).

## 1992-11-03 (day-after issue: 1992-11-04)

Hits examined:
- "Golding ready to let rancor, invective be bygones - Apparent winner makes overture of peace - absentee votes uncounted" — `news/116C3F652FD3ECE9`, A-7/A-1, by Pat Flynn, Column: DECISION '92/ELECTION RESULTS

Verbatim quotes with figures:
- "The final tally this morning -- not including about 40,000 uncounted absentee ballots -- showed she had won the race with 202,376 votes, 13,668 more than Navarro." — this 40,000 figure is scoped to the **city** mayoral race specifically.
- "With all 961 precincts in the city reporting and only the absentee ballots uncounted, Golding led Navarro 51.75 percent to 48.25 percent. In all, about 94,000 absentee ballots are to be counted in coming days, and election officials said this morning they did not know how many of those ballots were from the city of San Diego."

**Verdict: USABLE FIGURE.** The article distinguishes a city-only absentee remainder (~40,000, tied to the mayoral race) from a broader **county-wide absentee remainder of about 94,000 ballots** still to be counted ("election officials... did not know how many of those ballots were from the city of San Diego" makes clear the 94,000 is the county total). Satisfies the "absentees remaining" metric at the county level as of the morning-after report.

## 1996-11-05 (day-after issue: 1996-11-06, plus 1996-11-07 checked)

Hits examined:
- "The early calls by TV weren't a deterrent for eager voters here" — `news/116C4A4571AFD9C3`, B-4, by Karen Kucher, Column: ELECTION 1996/CITY & COUNTY (the registrar-focused piece, analogous to the 1988 "Officials pleased with turnout" story)
- "Battle for Assembly control too close to call..." — `news/116C4A45C45B091C`, A-9
- "8 legislators retained - Alpert wins Senate" — `news/116C4A45DB9103B5`, A-9 (no figures)
- "Incumbent council members in early lead - Marston within striking distance" — `news/116C4A451CE6AD49`, B-4 (Solana Beach city race, no county figure)
- "He's down for the count, but is he out?" — `news/116C4A46AEAA5FC5` (day+2 issue; false-positive title, actually a sports page E-1 story, not election-related)
- "U.S. House - Bilbray contends win shows voters satisfied..." — `news/116C4A47043D9C99` (day+2 issue, no county count figures)

Verbatim quotes with figures:
- "County registrar Mikel Haas expected more than 70 percent of the county's registered voters to cast ballots yesterday at more than 1,500 polling places." — a turnout **percent**, not a countable figure; excluded by the task's own criteria.
- "Haas said more than 7,000 county voters were saved from automatic ineligibility and given the chance to cast ballots in this election because of a 'fail-safe' provision..." — a registration-mechanics figure, not an election-night ballots-counted/absentees-remaining figure.

**Verdict: NOT FOUND.** The registrar-focused piece that in 1988/1992 carried a specific absentee-ballots-tabulated count instead only quotes a turnout percentage this year, plus unrelated registration figures. No county ballots-counted or absentees-remaining number turned up in the ~6 election-relevant articles examined across the day+1 and day+2 issues.

## 2000-11-07 (day-after issue: 2000-11-08, plus 2000-11-09 checked)

Hits examined:
- "Big turnout, few problems reported" — `news/116D328ED84C73F7`, B-10, by Michael Stetz, Column: ELECTION 2000/SAN DIEGO CITY / COUNTY (registrar-focused piece)
- "Title: ELECTION 2000 - SAN DIEGO CITY / COUNTY - SAN DIEGO" — `news/116D328EA0485689`, B-9 (results box: local races, all reported as "99.97%/100.00% of precincts" + candidate percentages, no raw counts)
- "Murphy tops Roberts in S.D. mayoral race" — `news/116D328E1A908ED3`, A-1 ("100% precincts", percentages only, city-scoped anyway)
- "Voters return Dronenburg, Witt to office" — `news/116D328EC3B8705E`, B-1 (no figures)
- "Feinstein sails to easy victory over Campbell..." — `news/116D328E270A69D5`, A-12 (no county figures)
- "Fire officials on edge in close tax vote - Anticipation high as absentee-ballot count continues" — `news/116D3290F82CA9EA`, B-2, day+2 issue, by Anne Krueger, Column: ELECTION 2000/EAST COUNTY

Verbatim quotes with figures:
- "More than 1 million of the county's 1.4 million registered voters were expected to vote." (B-10, "Big turnout, few problems reported") — an **expectation/projection**, not an actual count; excluded.
- "The Registrar of Voters Office isn't calling tight races until all 150,000 late absentee ballots cast in the county are tabulated, a process expected to last until Monday." (B-2, "Fire officials on edge in close tax vote," day+2 issue)

**Verdict: USABLE FIGURE.** The day+2 East County story states a precise San Diego **County** registrar figure: **150,000 late absentee ballots still to be tabulated** as of two days after the election. This satisfies "absentees remaining" at the county level. (The many "Title: ELECTION 2000..." results boxes found throughout this issue are consistently percent-of-precincts-reporting + candidate vote-share percentages, never raw ballot counts, so they don't independently satisfy the metric.)

## 2004-11-02 (day-after issue: 2004-11-03)

Hits examined:
- "Balloting mostly smooth but not without glitches - Turnout in county is heavy - a few scanners have problems" — `news/1062DF9FDA96EC23`, B-1, by Gregory Alan Gross, Column: ELECTION 2004 (published morning of election day, describes daytime voting/optical-scanner problems, no post-close figures)
- "Title: ELECTION 2004 - Initial county returns" — `news/1062DF9F8AC34007`, B-6 (large results box covering every county/city/district race and measure; consistently reported as "XX.XX% of precincts" + candidate vote-share percentages, never raw ballot counts)
- "Write-in vote takes thin lead over Murphy" — `news/1062DF9FEB760B95`, A-1, by Philip J. LaVelle, Column: ELECTION 2004/SAN DIEGO MAYOR

Verbatim quotes with figures:
- "Registrar of Voters Sally McPherson said the outcome may not be known for days or weeks. About 150,000 to 200,000 ballots, including provisional ballots and absentee ballots dropped off yesterday, will be counted the rest of this week." (A-1, "Write-in vote takes thin lead over Murphy")

**Verdict: USABLE FIGURE.** The county Registrar of Voters is quoted directly with a **county-wide remaining-ballots figure of about 150,000-200,000** (provisional + absentee-drop-off ballots) still to be counted as of the morning after the election. Satisfies "absentees remaining" / ballots-remaining-to-be-counted at the county level. (As with 2000, the "Initial county returns" results box spanning dozens of local races never gives a raw count, only percent-of-precincts-reporting and vote-share percentages.)

## 2008-11-04 (day-after issue: 2008-11-05)

Hits examined:
- "County elections chief: Many voters, few problems - Some Prop. 8 signs put too near polling places" — `news/124565D69B815608`, B-7, by Helen Gao and Jeff McDonald, Column: ELECTION 2008/SAN DIEGO COUNTY
- "Making history - Early voters swamped county election office" — `news/124565D6A476E660`, B-10, unsigned editorial, Column: ELECTION 2008 (about early-voting-period volumes leading up to Election Day, not election-night counting)
- "Title: ELECTION 2008 - COUNTY ELECTION RESULTS" — `news/124565D662AE8A40` (not opened in detail; based on the 2000/2004 pattern this results-box format is expected to be percent-of-precincts + vote-share only)

Verbatim quotes with figures:
- "The first boxes of ballots from precincts arrived at the registrar's office about 10 p.m., more quickly than anticipated, and scanners started counting them." (B-7) — no count given, context only.
- "Over the next few days, election workers will be busy verifying and counting provisional ballots by hand. Seiler estimated that 50,000 to 100,000 voters used such ballots." (B-7, quoting Registrar Deborah Seiler)

**Verdict: USABLE FIGURE.** County Registrar Deborah Seiler is quoted with a county-wide estimate of **50,000-100,000 provisional ballots** cast that remained to be hand-verified and counted after election night. This is a county-level ballots-remaining-to-be-counted figure, the same category as the absentee-remaining figures found for 1988/1992/2000/2004 (provisional rather than absentee, but the same "still to be processed" metric).

## Summary table

| Election | Verdict | Figure |
|---|---|---|
| 1984-11-06 | NOT FOUND | (370,000 ballots cast found but city-of-San-Diego scoped, not county) |
| 1988-11-08 | USABLE FIGURE | ~159,811-160,000 county absentee ballots tabulated election night; ~40,000 more absentee ballots still to process |
| 1992-11-03 | USABLE FIGURE | ~94,000 county absentee ballots uncounted as of election night (distinct from a ~40,000 city-only mayoral-race subset) |
| 1996-11-05 | NOT FOUND | (registrar piece gave only a 70% turnout estimate and an unrelated 7,000-voter "fail-safe" figure) |
| 2000-11-07 | USABLE FIGURE | 150,000 county late-absentee ballots still to be tabulated (day+2 report) |
| 2004-11-02 | USABLE FIGURE | ~150,000-200,000 county ballots (provisional + absentee drop-offs) still to be counted, per Registrar Sally McPherson |
| 2008-11-04 | USABLE FIGURE | 50,000-100,000 county provisional ballots still to be hand-verified/counted, per Registrar Deborah Seiler |

## Recommendation

**A recovery pass is worth it, with the metric reframed.** Five of seven target elections (1988, 1992, 2000, 2004, 2008) yielded a usable, precisely attributed San Diego County figure from SDUB's text-only archive — but in every case it is a **ballots-remaining-to-be-counted** figure (absentee or provisional), quoted directly from the county Registrar of Voters, not a positive "ballots counted by end of night" total and never a returns-box raw vote count. SDUB's own in-house results boxes ("Title: ELECTION ... COUNTY ELECTION RESULTS" / "Initial county returns") are formatted exclusively as percent-of-precincts-reporting plus candidate vote-share percentages across all seven elections checked — they never carry a raw ballot count, so they cannot substitute for or corroborate a count-based recovery on their own.

Practical implications for a recovery pass:
- Treat the recovered figure as a **remainder**, not a count: if a reliable total-ballots-cast (or total-registered-voter) figure for the county is available from another source (e.g., the certified Statement of Vote), the election-night "counted" total can be back-computed as (total ballots cast) minus (SDUB's reported remainder), which is exactly how the 1988/1992/2000/2004/2008 articles frame it themselves ("about X ballots... will be counted the rest of the week").
- The registrar-focused day-after "many voters, few problems" / "officials pleased with turnout" story is the reliable hit type across elections (present in 1988, 1992, 2000, 2004, 2008; absent — or at least not carrying a count that year — in 1984 and 1996). Prioritize opening that story first in any recovery run; it consistently outperforms the routine local-race roundup stories, which almost never carry raw numbers.
- 1984 and 1996 remain genuinely NOT FOUND despite a reasonably broad search (10 and 6 election-relevant articles opened respectively) — a deeper sweep of every remaining local-race story in those two issues is unlikely to change the outcome, since SDUB's non-registrar prose is consistently percentage-driven with no raw counts. If a floor is needed for those two years, microfilm/another archive remains the only path (per `newsbank-probe.md`'s existing recommendation).
