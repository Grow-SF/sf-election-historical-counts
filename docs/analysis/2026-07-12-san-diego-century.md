# A century of election nights in San Diego

*What the morning-after San Diego Union knew, 1871-1920, recovered scan by
scan from CDNC, and how it reframes the San Francisco story.*

**Date:** 2026-07-12
**Dataset:** [`data/research/san-diego-history/sd_night_history.csv`](../../data/research/san-diego-history/sd_night_history.csv)
**Evidence:** one dossier per election in
[`docs/research/night-recovery-2026-07-11-san-diego/`](../research/night-recovery-2026-07-11-san-diego/)
(transcribed precinct rows, scan paths, verification gates, and a
human-verification ask for every uncertain digit); certified denominators with
page-image provenance in the campaign's
[`denominators.md`](../research/night-recovery-2026-07-11-san-diego/denominators.md).
**Companion:** the SF original,
[`2026-06-13-a-century-of-election-nights.md`](2026-06-13-a-century-of-election-nights.md).

## The metric, and one definitional difference from the SF chart

```
night share = largest single-seat contest sum in the day-after San Diego Union
              / the SAME contest's certified San Diego County total (SoS SoV / Blue Book)
```

The SF century chart divides its contest-sum floor by certified BALLOTS CAST,
which folds top-of-ticket undervote into the denominator. San Diego's record
is computed same-contest on both sides, so its shares run slightly higher by
construction. Comparisons below are era-shape comparisons, not point-for-point
percent comparisons.

## The recovered record

| election | contest | night floor | certified | share | note |
|---|---|---:|---:|---:|---|
| 1871-09 | Governor | 545 | 1,285 | 42.4% | 5/5 precincts, New Town partial |
| 1872-11 | President | 536 | 873 | 61.4% | city + 2 outlying |
| 1875-09 | Governor | 720 | 1,600 | 45.0% | 7 of 8+ precincts |
| 1876-11 | President | 871 | 1,462 | 59.6% | "a little more than half the estimated vote" |
| 1879-09 | Governor | 614 | 1,412 | 43.5% | 8-precinct aggregate |
| 1880-11 | President | 747 | 1,289 | 57.3% | two-ticket basis; 3 a.m., explicitly partial |
| 1882-11 | Governor | 1,103 | not found | (~75%) | certified 1882 denominator not digitized; indicative only |
| 1884-11 | President | 812 | 1,965 | 41.3% | |
| 1886-11 | Governor | 1,031 | 2,826 | 36.5% | |
| 1888-11 | President | 3,288 | 8,194 | 40.1% | boom-era electorate 4x 1884 |
| 1890-11 | Governor | 184 | 7,306 | (2.5%) | definition artifact: paper printed majorities, not raw votes |
| 1892-11 | President | 673 | 7,712 | 8.7% | no city returns printed at all |
| 1894-11 | Governor | 1,761 | 7,124 | 24.7% | includes the page-2 continuation recovered in the mop-up pass |
| 1896-11 | President | 6,315 | 7,762 | 81.4% | 60 of 86 precincts |
| 1898-11 | Governor | 4,589 | 7,117 | 64.5% | LOW transcription confidence (35-column table) |
| 1900-11 | President | 3,672 | 6,931 | 53.0% | city-only total-vote proxy |
| 1902-11 | Governor | 4,202 | 6,459 | 65.1% | |
| 1904-11 | President | 6,300 | 7,241 | 87.0% | near-complete by morning |
| 1906-11 | Governor | 2,016 | 7,800 | 25.8% | 41 precincts, explicitly partial |
| 1908-11 | President | 6,028 | 9,409 | 64.1% | extended floor 6,841 = 72.7% |
| 1910-11 | Governor | 3,741 | 9,479 | 39.5% | 45/95 precincts at 3 a.m. |
| 1912-11 | President | 17,566 | 21,728 | 80.8% | printed grand totals, 114 rows |
| 1916-11 | President | 24,811 | 36,552 | 67.9% | 152/221 precincts |
| 1914-11 | Governor | 3,543 | 34,955 | (10.1%) | remote wire, 20/178 precincts: a wire-coverage artifact |
| 1918-11 | Governor | 4,502 | 25,100 | 17.9% | 63/221 precincts "complete" |
| 1920-11 | President | 8,178 | 31,098 | 26.3% | 73/223 precincts, 5 a.m. EXTRA |
| 1922-11 | Governor | 2,703 | 32,894 | (8.2%) | remote wire, 36/240 precincts: a wire-coverage artifact |
| 1924-11 | President | 23,961 | 46,408 | (51.6%) | remote AP wire, 158/274 precincts: a lower bound, not the night |
| 1926-11 | Governor | 22 | 38,194 | (0.1%) | the LA wire desk carried 2 of 308 precincts: 22 ballots |
| 1928-11 | President | 5,432 | 71,151 | (7.6%) | remote AP wire, 31/310 precincts: a severe lower bound |
| 1930-11 | Governor | 197 | 57,709 | (0.3%) | the LA wire desk carried ONE precinct of 384: 197 ballots |
| 1936-11 | President | 32,370 | 101,854 | (31.8%) | a pre-dawn EXTRA, only 167 precincts at press: a lower bound |
| 1940-11 | President | 114,410 | 128,110 | 89.3% | 550/596 precincts, a 6 a.m. special edition (see below) |

Five more mid-century figures exist but are **ceilings, not night counts**, so
they carry a null share and stay off the chart entirely: 1932 (76,427), 1934
(71,193), 1942 (51,600), 1944 (118,968) and 1950 (152,068). All come from
routine *evening* editions whose returns are clocked to the afternoon after
election day, when the canvass had already resumed. They bound the night from
above, which is the opposite of what the chart's axis means, so they cannot be
plotted even as dimmed points.

**And a warning about the dots near zero.** The parenthesised shares above,
1914, 1922, 1926, 1928 and 1930, are the weakest class of number in this
project. They come from *remote* papers: a Sacramento or Los Angeles wire desk
printing whatever San Diego copy had reached it overnight. In 1930 that was a
single precinct out of 384. These figures measure the wire's coverage of San
Diego, not San Diego's count, and the county was certainly much further along
than they imply. They are charted as dim lower bounds because they are the only
witness those years have, but no trend should ever be drawn through them.

**1940 is the era's high-water mark, and it nearly got away.** The Escondido
Times-Advocate was an evening paper, which normally disqualifies its day-after
issue (that is exactly how the 1932 row failed). But for this election it ran a
rushed special, and said so in print: "THE TIMES-ADVOCATE scooped the
universe... it issued an election special Wednesday morning... At six o'clock
Wednesday morning the editor's home phone rang... it was all ready to go to
press." A 6 a.m. edition is night-clocked, so the figure stands: 89.3% of the
county's certified presidential vote was counted by daybreak. San Diego's count
had recovered from the 1918-1920 collapse, exactly as San Francisco's had
(SF 1940: 95.3%).

Then the local paper goes dark (below), and the record resumes on a different
denominator, ballots cast rather than a contest sum:

| election | night floor | certified ballots | share | basis |
|---|---:|---:|---:|---|
| 1992-11 | 908,914 | 1,002,914 | 90.6% | news-derived: all 961 city precincts in, only absentees left |
| 2004-11 | 945,035 | 1,145,035 | 82.5% | news-derived: certified minus the registrar's 200,000-ballot remainder |
| 2008-11 | 980,234 | 1,245,947 | 78.7% | SoS election-night status page, last report 6:46 a.m. |
| 2010-11 | 663,326 | 926,363 | 71.6% | SoS election-night status page, last report 2:22 a.m. |

and 2014-2024 (73.5% down to 45.7%, back up to 64.9%) sits in the modern
cross-county panel (`data/research/election-night/san-diego-ca.json`), on that
same ballots-cast basis. 2008 and 2010 were recovered in this campaign and
added to that panel.

**The modern arc, now visible end to end.** 90.6% (1992) → 82.5% (2004) →
78.7% (2008) → 71.6% (2010) → 45.7% (2018) → 64.9% (2024). Mail composition
explains part of the slide, not all of it. The companion composition analysis
([`2026-07-10-vbm-composition-curve.md`](2026-07-10-vbm-composition-curve.md))
exists precisely to separate mechanical composition from real counting speed,
and its kernel puts composition at roughly 1.7 to 3.3 points of night share
per 10 points of mail share. San Diego's mail share rose about 22 points from
2008 (46.0%) to 2018 (68.5%), which accounts for only about 7 of the 33-point
fall; San Diego is in fact that analysis's largest unexplained residual
(residual_net +28.71). And the mail share kept climbing after 2018 (90.0% in
2022, 84.9% in 2024) while the night share recovered, 45.7% to 54.2% to
64.9%, which is why the vote-center/e-pollbook era is doing real work here.

## The shape: San Diego confirms the SF timing, at half the amplitude

The frontier baseline first: through the 1870s and 80s the morning paper
reliably had 36-61% of the eventual vote, bounded not by counting speed but
by geography (returns rode in from mountain precincts for days). The
certified denominators split by year: the pre-1884 elections come from
the Tribune Almanac's near-primary county tables, because no state SOV is
digitized before 1886; 1884 and 1888 come from the near-primary Governmental
Roster of 1889; and 1886 comes from the digitized 1886 SOV itself, a primary
source. 1882 has no certified source at any confidence and is indicative
only. Each year's source and confidence is recorded in `denominators.md`.

Three features of the later record line up with San Francisco, one pointedly
does not.

**1. The 1918-1920 collapse is real and shared.** Setting aside the
print-practice floors of 1890/1892 and the remote-wire lower bounds of
1924/1928, 1918 is the worst genuine counting morning in the whole San Diego
record (17.9%, 63 of 221 precincts after a night the paper attributes to a
~55-amendment ballot, rain, war, and the influenza epidemic), and 1920 is
nearly as bad (26.3% at the five-o'clock EXTRA, "some of the election officials
were still at it as The Union went to press", 26 amendments), both far below
the 64-87% the same paper had been printing a decade earlier. This
is exactly SF's slow window (SF 1918: no city totals printed at all; SF 1922:
27%). Two counties with different sizes, machines, and newspapers slowing at
the same moment points at the statewide mechanism both papers blamed in
print: the Progressive-era long ballot.

**2. But San Diego's 1910s held up where SF's fell apart.** The starkest
contrast in the whole record: 1916, the presidential race that hung on
California for days (Wilson took the state by 3,773 votes, 466,289 to Hughes's
462,516). The SF Chronicle that morning confessed "virtually none of San
Francisco's vote" was in hand (~3%). The San Diego Union printed
Hughes 12,629, Wilson 12,182 from 152 of 221 precincts: 67.9% counted. 1912
is the same story (SD 80.8% with printed grand totals at 2 a.m.). A county
counting 22-37k ballots could absorb the long ballot's per-ballot cost in one
night; a county counting 100-155k could not. The long-ballot slowdown was
real everywhere but CATASTROPHIC only at metropolitan scale.

**3. The 1890s dip is a newspaper-practice artifact worth keeping.** 1890
(2.5%) and 1892 (8.7%) are floors of what the PAPER printed, not of what was
counted: in 1890 the Union reported most precincts as majorities ("Markham by
40") rather than raw votes, and in 1892 it printed no city returns at all.
The 1894 mop-up (which found the returns' continuation on page 2 and more
than doubled the floor to 24.7%) shows how much of this era's apparent
slowness is print-space, not counting speed. SF's early record has the same
property; both charts should carry these years as floors, visually distinct.

**4. Same century, same three meanings of "we don't know yet."** In the
1870s-80s San Diego the morning paper carried a few hundred votes from a
handful of precincts because returns traveled by stage and telegraph from
mountain precincts ("it may be a couple of days before all the back country
precincts have sent their returns in," 1920, but true of every year before
it). In 1918-1920 the clerks were still counting a bedsheet ballot at
daybreak. And in the modern panel the ballots are in the mail. Transport,
then counting, then arrival: the symptom recurs, the mechanism rotates.

## The 1908 quote that ties the two counties together

The Union, morning of 1908-11-04, on its own incomplete returns:

> "Almost all night was consumed in some of the precincts counting ballots,
> the constitutional amendments making the work of tallying votes many times
> harder than it otherwise would have been. Were it not for the amendments
> the returns would have been absolutely complete not much later than
> midnight."

This is the same complaint the SF Chronicle printed by name in 1914 and 1918
("the long ballot"), six years earlier, in a county a quarter the size, on a
night San Diego still managed 64-73%. The dose-response is visible across
the two counties: amendments slowed everyone; scale determined whether
slowed meant "late" or "unknown."

## Gaps and dead ends (each probed, none silent)

The San Diego Union itself is digitized only to 1922, so the middle of the
century had to be attacked sideways. Six routes were tried; four paid, a fifth
paid only a ceiling. The best of them, the one that recovered 1940, is also the
least obvious: hunt for *special editions*.

- **Remote AP county tables (paid, partly).** Other CDNC papers printed an AP
  "vote by counties" table the morning after, with a San Diego row. That
  recovered 1924 and 1928, but as *remote-wire* floors: a distant paper's
  press time catches far fewer precincts than the local paper's own
  compilation (1928 caught 31 of 310), so both are dimmed lower bounds, useful
  for the record and useless for trend. **1926 has no candidate table; 1930 is
  CDNC embargo-locked** ("available 23 September 2026"), 1934 and 1936 have no
  county-level numerator in any reachable paper, and by 1952 the format had
  vanished from the sampled papers
  ([`cdnc-county-table-probe.md`](../research/night-recovery-2026-07-11-san-diego/cdnc-county-table-probe.md)).
- **A county paper's election SPECIAL (paid, and it is the best point we have).**
  San Diego County's own dailies are in CDNC, and the Escondido Times-Advocate
  printed a full county presidential table for **1940**. It was an evening
  paper, which should have disqualified it, except that for this election it
  rushed out a 6 a.m. special and bragged about it in print. That makes the
  figure night-clocked: 114,410 ballots, 550 of 596 precincts, **89.3%**. The
  same trick found **1936**, whose "EXTRA EXTRA / ROOSEVELT WINS" special went
  out free to subscribers before dawn, though it went to press so early (167
  precincts) that it is only a lower bound. The lesson generalizes: an evening
  paper is not categorically useless, it is useless *except* when a big election
  pushed it to print a morning special. So the mid-century hunt is a hunt for
  specials, and it is worth continuing: three of the four years probed this way
  produced something, and the fourth (1944) produced a ceiling
  ([`sd-local-papers-probe.md`](../research/night-recovery-2026-07-11-san-diego/sd-local-papers-probe.md)).
- **The same route, and the trap inside it.** The Oceanside
  Blade-Tribune (also a county paper) printed a full county
  compilation for **1932**: 76,427 ballots with 339 of 384 precincts in, which
  would have been the best-covered point of the era at 89.8%. It is not a night
  count. The Blade-Tribune was an **afternoon** paper, so its day-after edition
  went to press around midday and its returns are clocked "this afternoon",
  sixteen to twenty hours after polls closed, with the canvass already resumed.
  The figure is therefore recorded as a **ceiling** (share NULL,
  `comparable: false`) and excluded from the chart, and the dossier carries a
  dated correction. The general rule, now written into the campaign README: a
  day-after issue is a night source only if the paper was a *morning* paper.
  This is why the San Diego Union (masthead "WEDNESDAY MORNING", returns
  clocked "this morning") underpins the whole pre-1922 record and a county
  weekly could not.
- **NewsBank image edition (dead).** Its San Diego Union image edition starts
  in **2018**, so it cannot touch 1914, 1922, or the mid-century
  ([`newsbank-probe.md`](../research/night-recovery-2026-07-11-san-diego/newsbank-probe.md)).
- **NewsBank text archive (paid, twice).** The text run is empty across most
  of 1970-1986, and most morning-after quotes bound only *one* ballot category
  ("50,000 provisionals remain"), which says nothing about uncounted mail and
  yields no sound floor. Only **1992** and **2004** carry statements that bound
  the entire remainder, so only they became floors; 1988, 1996, 2000 and 2008
  each got a dossier explaining precisely why they did not
  ([`sdub-text-probe.md`](../research/night-recovery-2026-07-11-san-diego/sdub-text-probe.md)).
- **Wayback (paid, twice).** The Secretary of State's election-night
  county-status pages yield plateau-grade counts for **2008** and **2010**,
  both bracketed by later captures showing the count growing. For 1994-2006 the
  crawls fall in gaps that swallow election night itself
  ([`wayback-probe-1994-2010.md`](../research/night-recovery-2026-07-11-san-diego/wayback-probe-1994-2010.md)).

Still dark as a *night* count, after all six routes: **1938**, **1946**,
**1948**, **1952-1990**, and **1994-2002 plus 2006**. Five further years
(**1932, 1934, 1942, 1944, 1950**) yield only afternoon-clocked ceilings, and
five more (**1914, 1922, 1926, 1928, 1930**) yield only remote-wire artifacts.
The San Diego Union, the one paper that would settle all of them properly, is
simply not digitized after 1922: a direct test confirms CDNC returns "no such
issue" for its post-1922 dates, rather than the embargo lock screen it shows for
other papers, so there is no release date to wait for. Newspapers.com, the obvious
commercial fallback, turns out not to carry the San Diego Union at all: zero
years, confirmed against their catalog and cross-checked with working controls
(see
[`newspapers-com-purchase-check.md`](../research/night-recovery-2026-07-11-san-diego/newspapers-com-purchase-check.md)).
The untested leads that remain are GenealogyBank, which may hold the title, and
San Diego Public Library's in-branch microfilm.

- **Pre-1871:** the San Diego Herald (1851-1860) is in CDNC but no statewide
  certified denominators are on file; out of scope.
- **1898 and 1900** carry reduced confidence for reasons stated in their
  dossiers: 1898 for table density, 1900 for an unresolved
  internal-consistency failure in the city-totals row.

## Verification status

Every election has a dossier with per-digit provenance. Adversarial re-read
passes (appendices in each dossier) CONFIRMED the headline digits for 1896,
1908, 1912, 1918, and 1920 (correcting only the paper's own printed plurality
arithmetic), and left 1898/1900 explicitly unresolved. 1916 has had no
adversarial re-read: its floor rests on a single printed pair (Hughes 12,629,
Wilson 12,182) with no precinct table to cross-check it against, so those
digits remain an open priority human ask (the only internal corroboration is
the paper's own rounded "about 450" plurality, against the 447 the pair
implies). The remaining human asks are collected per dossier under
"Human-verification asks" with scan paths and fail criteria; the operator's
read wins.
