# Is San Francisco getting slower at counting ballots?

**Short answer: no — and in one specific sense, yes.** The total time to count
is flat-to-slightly-faster across 18 years of elections. What has changed is
*when* the ballots get counted: election night used to deliver ~70% of the
final count; it now delivers 45–57%. The count didn't get slower — it got
back-loaded, because a growing share of ballots are mail ballots that arrive
on or after election day and legally cannot be tallied on night one.

## Data

Two layers, both in this repo:

1. **`data/sf_count_timeline.csv`** — every per-release results report,
   Nov 2015 – present (243 rows, exact release-by-release counts from the
   Department of Elections' own files).
2. **`data/sf_archival_canvass_points.csv`** — 36 mid-canvass observations for
   thirteen elections, Mar 2002 – Nov 2014, recovered from Wayback Machine
   captures of the DOE's live results pages across four site generations
   (sfgov.org/election ES&S report pages, the /site/ CMS, sfelections.org,
   plus one OCR'd press-release PDF for Feb 2008). Sparse by nature: each
   point is a snapshot some crawler happened to take, so pre-2015 crossing
   days are *brackets*, not exact. Certified finals come from the DOE's
   still-live legacy pages, the DOE's own 1960–2002 turnout history
   (`data/sf_turnout_history_1960_2002.csv`), and the CA Secretary of
   State's Statements of Vote.
3. **Recovery limit:** no canvass-progress captures survive for 1995–2001 —
   the Internet Archive's crawler hit the DOE's Lotus Domino results system
   only between elections (all 57 recovered documents carry stale Nov 1998
   stamps), and the Nov/Dec 2003 CMS result pages were never captured
   mid-canvass. Those years are recoverable only from DOE internal records
   (request pending). The DOE's certified result datasets for every election
   Nov 1995 – Nov 2002 were recovered (`mirror/doe-archives/`) along with
   its official turnout history back to 1960.

Raw captures are mirrored (CDN hosting planned; not in git). The committed
`data/mirror_manifest.csv` maps every mirrored file to its source memento URL
and SHA-256, so the mirror is independently verifiable.

## November general elections, 2008–2024

| General | counted by election night | days to 80% | days to 90% | days to 98% |
|---|---|---|---|---|
| 2002 | — | ≤9 | ≤9 | ≤9 (99.8% on day 9) |
| 2004 | **74.9%** | 0–13 | 0–13 | 13–28 |
| 2010 | — | 3–5 | >5 | — |
| 2012 | **71.4%** | **3** | 6–8 | — |
| 2014 | **70.3%** | 2–13 (capture gap) | 2–13 | — |
| 2016 | 66.1% | **7** | 9 | 14 |
| 2018 | 59.3% | 5 | 7 | 10 |
| 2020 | 78.4%* | 2 | 3 | 5 |
| 2022 | 51.0% | 6 | 7 | 9 |
| 2024 | 56.9% | 5 | 6 | 11 |

\* 2020 was the all-mail pandemic election: ballots arrived weeks early and
were pre-processed, so election night covered nearly everything. It is the
exception that proves the mechanism.

Other recovered elections: Mar 2002 primary (certified 150,249); Nov 2005
municipal (80.1% by day 3 and 92.4% by day 7, from the Department's own
press-release series — five dated releases recovered intact); Feb 2008
presidential primary (81.4% of final by day 6 — a slow front even then, at
64.75% turnout); Jun 2010 primary (71.5% by day 2); Nov 2011 municipal (90%
crossed on day 2); Jun 2012 (≥94% by day 2); Nov 2013 (≥95% by day 3);
Jun 2014 (≥96% by day 3). Nov 2002 stands out: 100% of precincts and 99.8%
of the final count reported by day 9, in the punch-card era with absentees
around a third of the vote.

## Findings

1. **Days-to-90% shows no trend, 2008→2026.** Within the exact modern data
   (2015–2026) the regression slope is ~0.00 days/year. The recovered
   2010–2014 brackets (2012 general: 6–8 days; 2011/2013 municipals: 2–3
   days) sit squarely in the modern range (2024 general: 6; 2019 municipal: 3).

2. **The election-night floor (1964–present).** The non-absentee share of
   each certified count bounds the night share from below — precinct ballots
   were reported on election night. The floor was 94% in 1964, ~80% through
   the 1970s–80s, ~65% in the 1990s, ~50% by 2008, and ~10% under universal
   VBM (validated ≤ the actual night share in all 20 cases where both are
   known; `data/sf_night_floor_1964_2026.csv`). Even with zero canvass
   records before 2001, arithmetic alone proves election night once delivered
   nearly the whole count.

3. **The election-night share has fallen hard — this is the real trend.**
   Generals: 74.9% (2004) → ~70–71% (2012, 2014) → 66% (2016) → 59% (2018)
   → 51–57% (2022, 2024). A near-monotone twenty-year decline of ~20 points.
   Driver: VBM share of the vote keeps rising, and California accepts mail
   ballots postmarked by election day for 7 days after; signature
   verification means those simply cannot appear in night-one releases.

4. **The early canvass (to 80%) slowed relative to 2011–2014, but that era
   was the historical fast patch, not the baseline.** Nov 2012 hit 80% on
   day 3; modern generals take 5–7 days. But Feb 2008 took ~6 days to 80%,
   like today. The 2011–2014 period — VBM around half the vote, most of it
   arriving *before* election day — was the sweet spot where mail could be
   pre-processed and election-day volume was small.

5. **The slow tail has not lengthened.** Days from 90% to 98% is stable to
   slightly improving in the modern data. Once late mail is in hand, the DOE
   clears it as fast as it ever has.

6. **Perception check.** Two recent artifacts feed the "it's getting slower"
   feeling: (a) less is known on election night (real, structural, not a
   counting-speed problem); (b) Nov 2025 shows days-to-90 = 13, the worst in
   the dataset — but the count stood at 89.9% on day 6 and the DOE simply
   published no report between day 6 and day 13. Reporting cadence, not
   counting speed.

## Caveats

- Pre-2015 crossings are brackets from sparse captures; treat single-day
  precision claims skeptically.
- The 2014 general has a capture gap between day 2 (78.8%) and day 13.
- Election types differ in size and complexity; this note compares
  like-with-like (generals) where possible.
- The Nov 2012 full curve (7 points, election night through certification)
  is the only pre-2015 election with near-release-level coverage.
- n is small everywhere. The night-share decline is the only trend here that
  would survive a significance test.

*Built 2026-06-09. Recovery provenance: `data/mirror_manifest.csv`;
extraction methods recorded per row in `data/sf_archival_canvass_points.csv`.*
