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
| 1918-11 | Governor | 4,502 | 25,100 | 17.9% | 63/221 precincts "complete" |
| 1920-11 | President | 8,178 | 31,098 | 26.3% | 73/223 precincts, 5 a.m. EXTRA |

2020s-era rows (45.7%-64.9%) live in the modern cross-county panel
(`data/research/election-night/san-diego-ca.json`), on the plateau/ballots
basis; the 1922-2010 gap is unrecovered (see "Gaps" below).

## The shape: San Diego confirms the SF timing, at half the amplitude

The frontier baseline first: through the 1870s and 80s the morning paper
reliably had 36-61% of the eventual vote, bounded not by counting speed but
by geography (returns rode in from mountain precincts for days). The
certified denominators for that era come from the Tribune Almanac's county
tables rather than a state SOV (none is digitized); they are near-primary and
flagged as such in `denominators.md`.

Three features of the later record line up with San Francisco, one pointedly
does not.

**1. The 1918-1920 collapse is real and shared.** San Diego's two worst
recovered mornings are 1918 (17.9%, 63 of 221 precincts after a night the
paper attributes to a ~55-amendment ballot, rain, war, and the influenza
epidemic) and 1920 (26.3% at the five-o'clock EXTRA, "some of the election
officials were still at it as The Union went to press", 26 amendments). This
is exactly SF's slow window (SF 1918: no city totals printed at all; SF 1922:
27%). Two counties with different sizes, machines, and newspapers slowing at
the same moment points at the statewide mechanism both papers blamed in
print: the Progressive-era long ballot.

**2. But San Diego's 1910s held up where SF's fell apart.** The starkest
contrast in the whole record: 1916, the closest presidential race in
California history. The SF Chronicle that morning confessed "virtually none
of San Francisco's vote" was in hand (~3%). The San Diego Union printed
Hughes 12,629, Wilson 12,182 from 152 of 221 precincts: 67.9% counted. 1912
is the same story (SD 80.8% with printed grand totals at 2 a.m.). A county
counting 25-37k ballots could absorb the long ballot's per-ballot cost in one
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
("the long ballot"), six years earlier, in a county one-tenth the size, on a
night San Diego still managed 64-73%. The dose-response is visible across
the two counties: amendments slowed everyone; scale determined whether
slowed meant "late" or "unknown."

## Gaps and dead ends (documented, not silent)

- **1914 and 1922:** CDNC's San Diego Union digitization has no issues for
  those Novembers (1914 absent entirely). NewsBank was probed and is a dead
  end: its only San Diego Union image edition starts 2018
  ([`newsbank-probe.md`](../research/night-recovery-2026-07-11-san-diego/newsbank-probe.md)).
  Microfilm or another archive is the remaining path.
- **1922-2010:** unrecovered for the same reason. The SDUB text archive
  (1970+) was probed for prose night-count figures for 1984-2008
  ([`sdub-text-probe.md`](../research/night-recovery-2026-07-11-san-diego/sdub-text-probe.md)).
- **Pre-1871:** the San Diego Herald (1851-1860) exists in CDNC but no
  statewide certified denominators are on file; out of scope.
- **1898 and 1900** carry reduced confidence for reasons stated in their
  dossiers (table density; a paper-side arithmetic inconsistency).

## Verification status

Every election has a dossier with per-digit provenance. Adversarial re-read
passes (appendices in each dossier) CONFIRMED the headline digits for 1908,
1912, 1916, 1918, 1920, and 1896 (correcting only the paper's own printed
plurality arithmetic), and left 1898/1900 explicitly unresolved. The
remaining human asks are collected per dossier under "Human-verification
asks" with scan paths and fail criteria; the operator's read wins.
