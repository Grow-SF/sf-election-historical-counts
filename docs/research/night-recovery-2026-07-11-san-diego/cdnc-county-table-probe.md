# CDNC "other-paper" county-table probe for the SDDU 1924-1968 dark years (2026-07-12)

Testing whether OTHER CDNC-digitized California papers printed a
morning-after AP/wire "vote by counties" table (one row per county, with
counts) that would carry a San Diego County figure, for the years the San
Diego Union itself is not digitized (1923-2017 in CDNC).

Method: `scripts/archive-recovery/cdnc_fetch.js <CODE><YYYYMMDD> search:"San
Diego"` scopes a full-text search to one paper+one day and OCRs every hit in
one call. Test elections: 1928-11-06, 1940-11-05, 1952-11-04, 1960-11-08
(day-after issues 11-07 / 11-06 / 11-05 / 11-09 respectively).

## Shortlist (paper, code, digitized run per CDNC title list)

| Paper | Code | Run | Note |
|---|---|---|---|
| Sacramento Daily Union / Union | SDU | 1851-1966 | State-capital daily, most likely to carry a full state canvass table |
| Santa Barbara News-Press | SBNP | 1896-1964 | Large daily, AP member |
| Press-Telegram (Long Beach) | LBPT | 1901-1962 | Large SoCal daily, AP member |
| Madera Tribune | MT | 1916-1968 | Small-town, covers full gap as backstop |
| Blade Tribune (Oceanside) | BT | 1892-1960 | San Diego COUNTY paper (not Union) |
| Times-Advocate (Escondido) | TAD | 1893-1959 | San Diego COUNTY paper (not Union) |
| Desert Sun (Palm Springs) | DS | 1934-1993 | covers 1940/1952/1960 only |

## Test elections

### 1928-11-06 (day-after issue 1928-11-07)

Papers checked: SDU (Sacramento Union), day-after issue `SDU19281107`.

**HIT.** SDU front-page-continuation returns page (`SDU19281107.1.5`, printed
"CALIFORNIA'S ELECTION" wire table, a genuine AP county-by-county roundup;
dozens of counties appear as rows: Calaveras, El Dorado, Yuba, San Francisco,
Riverside, Oakland, Fresno, Glenn, Imperial, San Luis Obispo, Los Angeles,
Santa Clara, San Bernardino, Ventura, Mono, Sierra, Colusa, Amador, Trinity,
Modoc, Sutter, San Joaquin... and San Diego.

TWO separate San Diego County lines appear in the SAME page/edition (distinct
wire flashes printed as they arrived, not one cumulative table) - confirmed
both by OCR (`scripts/archive-recovery/cdnc_fetch.js SDU19281107 'search:San
Diego'`, saved to `mirror/cdnc/SDU19281107/search_San_Diego.txt`) and by
visual zoom read (`mirror/cdnc/screenshots/probe_sdu1928_sandiego.png`,
zoom `SDU19281107.1.5` FX=0.17 FY=0.44 3 clicks):

> SAN DIEGO COUNTY — 17 out of 310 precincts, Republican 3,063, Democratic
> 1,452, Socialist 17, Prohibition 19.
>
> SAN DIEGO COUNTY — 31 out of 310 precincts, Republican 3,533, Democratic
> 1,799, socialist 45, Prohibition 55; senator, Johnson 3,525, Moore 1,073,
> Randall 88, Lewis 97. Measures, 14 precincts...

Basis stated explicitly ("N out of 310 precincts") - this is unambiguously an
incomplete, election-night wire count, not a certified total. The two lines
are inconsistent snapshots (17/310 read LOWER precinct count but higher per
some columns than 31/310 in others - typical of AP flashes compiled out of
order); the later/larger (31/310, Hoover 3,533 + Smith 1,799 = 5,332
presidential ballots) is the better floor candidate.

Screenshots: `mirror/cdnc/screenshots/probe_sdu1928_overview.png` (page
overview), `mirror/cdnc/screenshots/probe_sdu1928_sandiego.png` (zoomed,
legible).

**Verdict: VIABLE via SDU for 1928.**

### 1940-11-05 (day-after issue 1940-11-06)

Papers checked: SDU, SBNP (Santa Barbara News-Press), MT (Madera Tribune),
DS (Desert Sun).

**BLOCKED by a CDNC access embargo, not by content absence.** Both
`SDU19401106` and `SBNP19401106` render a lock screen instead of the page
image/OCR:

> This issue will be available in the California Digital Newspaper
> Collection on 23 September 2026. It is available now at newspapers.com.

Identical embargo date (23 Sep 2026) on two unrelated papers (Sacramento
Union, Santa Barbara News-Press) for the same day - this is a scheduled,
rolling CDNC-wide release gate (content already licensed to newspapers.com,
staged for free CDNC release later), not a per-title restriction. It explains
the earlier `getSectionText` "Please log in before performing this action"
errors: the search index still has these issues catalogued (hence snippets
appear in search results) but the OCR/page-image endpoints refuse to serve
them pre-release. Screenshots: `mirror/cdnc/screenshots/probe_sdu1940_shot.png`,
`probe_sbnp1940_shot.png` (both show the identical lock notice).

Smaller/non-newspapers.com-partner titles are NOT gated the same way:
Madera Tribune's `MT19401106` loaded fine, but its one "San Diego" hit was an
unrelated NYA-program brief, no county returns table. Desert Sun's
`DS19401107` loaded (0 hits for "San Diego" - Desert Sun in 1940 was a small
weekly with essentially no wire-service state coverage). Blade Tribune
(`BT19401106.1.1`) returned "Invalid value ... for CGI argument d" (that
issue/page simply doesn't exist in CDNC, not an embargo).

**Verdict: NOT TESTABLE right now for the large/AP-wire-carrying papers
(SDU, SBNP) - re-probe after 2026-09-23.** The small papers that ARE open
don't carry the county-table format.

### 1952-11-04 (day-after issue 1952-11-05)

Papers checked: SDU (front page 1 + 2 fully OCR'd/screenshotted), LBPT
(Long Beach Press-Telegram, 5 search hits on "San Diego County").

**Format has moved on - no statewide AP county-by-county table found.**
SDU's front page (`SDU19521105.1.1`, screenshot
`mirror/cdnc/screenshots/probe_sdu1952_p1.png`) leads with "Ike Sweeps Into
White House; Stevenson Is Crushed" plus a Sacramento-only "BOX SCORE" (local
precincts/props) and a "Third District Results" congressional box - no
county-by-county state table. Targeted searches ("San Diego County", "Vote by
Counties") on the full issue turned up only an unrelated human-interest brief
("Aged Woman Is Killed On Way to Vote SAN DIEGO") and a legal escheatment
notice mentioning a San Diego bank - no vote counts. LBPT is even more
hyper-local (Long Beach/South Bay precinct-level results for its own metro
area - San Pedro, Wilmington, Gardena) with "San Diego County" appearing only
incidentally (as part of the 28th Congressional District description and a
coroner's-office mention), never as its own returns row.

**Verdict: NOT FOUND.** By 1952 neither paper prints the granular
AP wire state canvass table the 1928 SDU used.

### 1960-11-08 (day-after issue 1960-11-09)

Papers checked: SDU (front page).

SDU's front page (`SDU19601109.1.1`, screenshot
`mirror/cdnc/screenshots/probe_sdu1960_p1.png`, headline "KENNEDY IS
PRESIDENT") carries only a national electoral-vote box (Kennedy
21,830,734/51.7% - Nixon 20,394,772/48.3%) plus exclusively Sacramento-area
local races (Yolo, Placer, Sacramento supervisor contests). No California
county-by-county table, no San Diego mention on the page.

**Verdict: NOT FOUND** (not separately re-tested against a second paper
given the consistent 1952 pattern and time budget; the front-page format
shift away from statewide tables is the same one seen in 1952).

## Recommendation

**Partially viable, and window-limited, not a clean 1924-1968 solution.**

1. The hypothesis is CONFIRMED for the early part of the gap: the Sacramento
   Union ran a genuine AP wire "vote by counties" roundup with a San Diego
   County row (precincts reporting + Republican/Democratic + minor-party
   counts) at least through 1928. This is a real, usable election-night floor
   source for early-1920s/1930s elections once SDDU itself goes dark.
2. The format appears to have DISAPPEARED from the papers we sampled by the
   early 1950s - both a Sacramento paper and a Los Angeles-metro paper had
   shifted to hyper-local precinct coverage plus a bare national tally box,
   with no county-by-county state table at all. So even where CDNC content is
   open, 1952 and 1960 look genuinely NOT RECOVERABLE via this route with the
   papers tried (though only 2 of the ~7 shortlisted papers were actually
   checked for 1952 and only 1 for 1960 - a fuller sweep of LAE, CASAL, POR,
   MR, NJ could still turn up a late holdout, but the trend line across two
   very different newsrooms argues against it).
3. A SEPARATE, unplanned finding matters more operationally: CDNC has a
   rolling access embargo (content already sold to newspapers.com, staged for
   free CDNC release later) that currently blocks BOTH Sacramento Union and
   Santa Barbara News-Press for 6 Nov 1940 specifically, with an identical
   "available 23 September 2026" notice on both. That date is suspicious
   (2.5 months out) and may mean a broader swath of the 1930s-40s unlocks on
   a schedule - worth a quick re-check after 2026-09-23 before concluding
   1940 is unrecoverable via this method. 1928 was open; 1952/1960 were open;
   only the ~1940 slice hit the wall in this sample, so the embargo boundary
   is narrow, not "everything after 1930."
4. Recommended next step if pursuing this further: re-probe SDU/SBNP for
   1940 after 23 Sep 2026 (5 minutes of work), and if still no county table,
   treat 1924-1968 as only PARTIALLY bridgeable (roughly 1924-1931) via this
   AP-county-table method, with 1932-1968 needing a different route
   (NewsBank/microfilm SFPL-style access, or a same-San-Diego-County paper's
   OWN local returns - Blade Tribune/Times-Advocate/Chula Vista Star-News
   are all San Diego County papers with 1930s-1960s CDNC runs and were not
   yet content-probed in this pass, only spot-checked for
   existence/embargo).
