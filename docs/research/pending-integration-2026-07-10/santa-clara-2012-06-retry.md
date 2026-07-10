# Santa Clara 2012-06-05 primary: retry scout log

Target: upgrade/bound/grade the 234,342-ballot ceiling found at
http://www.sccgov.org/elections/results/jun2012/ (Wayback 20120607192808,
"Unofficial Semi-Final Results", internal stamp 6/6/2012 7:02:03 PM,
874/874 precincts). Certified final 292,713. Ceiling pct 80.06%.
Full context: dossier-santa-clara-ca-primaries.md Item 1 (this scratchpad dir).

Method: runbook 7.3 freeze test -> label semantics cross-check -> scaling fallback.

---

## Step 1: freeze test (runbook 7.3) -- RESULT: FAILED (count moved). CEILING STANDS.

CDX enumeration of `www.sccgov.org/elections/results/jun2012/` (and prefix
sweep of `.../jun2012*`), June-Dec 2012, exact-URL + prefix, no collapse:
27 rows, 19 distinct 200-status captures (dossier's earlier pass only found
4; this pass used a wider window and both exact-URL and prefix queries).
No capture earlier than 20120607192808 exists in CDX (checked June 1 - Dec
31 2012 window and a June-only narrow window); redirect-alias check on the
no-trailing-slash form confirms no hidden earlier timestamp (memento-datetime
matches, no divergent Location). No frameset/inner-frame files found under
the path -- the page is direct HTML with the turnout numbers embedded, not
a frameset shell.

Digests across the 19 captures:
- 20120607192808 = `ML2VSXUKLPFIWHH3OQ4DIR66NALUQ3EA` (the known 234,342 state)
- 20120608222327 = `SWL7AANXNH6D4YFHH3ZBXPUKWKIKJLIQ` (DIFFERENT)
- 20120609022555 = `C4QT7DJMZCIKUH4Y6FCEHNRRNYHADYRQ` (DIFFERENT AGAIN)
- 20120723061342 through 20121208221314 (14 captures) = all
  `OULHMLONY7RIE3U3Z4U2G5OAWKHE3N2S` (identical digest, frozen 4.5+ months)

Fetched and read the three post-234,342 captures directly (raw `id_`,
not gzipped, plain text parse of the county's "Registration & Turnout"
block, VBM + Precinct = total ballots):

| capture (Wayback ts) | internal "Last Updated" | VBM | Precinct | TOTAL | precincts |
|---|---|---|---|---|---|
| 20120607192808 | 6/6/2012 7:02:03 PM | 185,455 | 48,887 | **234,342** | 874/874 |
| 20120608222327 | 6/7/2012 4:43:58 PM | 219,470 | 48,900 | **268,370** | 874/874 |
| 20120609022555 | 6/8/2012 4:21:51 PM | 235,125 | 48,900 | **284,025** | 874/874 |
| 20120723061342 (frozen state, held through 20121208221314) | 07/3/12 03:58 PM | 237,195 | 55,518 | **292,713** | 874/874 |

The frozen state's total (292,713 VBM 237,195 + Precinct 55,518) is an
EXACT match to the SoS certified final (292,713; SoV: 55,518 poll +
237,195 VBM = 292,713). This is the certified/canvass-complete state,
frozen from July 3 (per its own internal stamp) through the last capture
Wayback took, Dec 8 2012.

**Verdict: the freeze test decisively FAILS.** 234,342 is NOT a frozen
night state -- it grew by +34,028 the very next capture (6/7 4:44 PM,
+14.5%), +49,683 total by 6/8 4:22 PM (+21.2%), and continued to the
certified 292,713 (+58,371 total, +24.9%) by canvass close. The "Unofficial
Semi-Final Results" banner text was carried on a page that was still
actively accumulating VBM ballots for weeks after election night (VBM grew
185,455 -> 237,195, +28%, while Precinct grew only 48,887 -> 55,518, +13.6%,
consistent with late-arriving/postmarked VBM being the growth driver, not
precinct recounts). "Semi-Final" here is NOT canonical end-of-night
language the way LA uses it -- it is this county's generic in-progress-canvass
label, used identically on Tuesday-night-equivalent AND Wednesday-evening
AND Thursday-evening pulls.

Per the runbook's own rule ("if the number moved between captures ... your
days-later render is contaminated" -- 7.3, the Placer 2018 precedent): the
ceiling stands. 234,342 remains a valid (monotonic) upper bound on the true
election-night plateau, since it predates all the growth above, but it is
now proven NOT itself close to a stable/final value -- it is a snapshot
mid-canvass, taken ~23 hours after poll close (poll close ~8 PM Tue June 5;
capture stamp 7:02 PM Wed June 6).

## Step 2: label semantics cross-check -- INCONCLUSIVE (no comparable page exists)

Read `data/research/election-night/santa-clara-ca.json`'s Nov 2012 general
row. It is sourced ENTIRELY from Clarity electionId 43231 (438,348 night
plateau / 460,329 next-day canvass-start / 653,239 certified), not from any
sccgov.org legacy GEMS page. Checked directly: a legacy
`sccgov.org/elections/results/nov2012/` path DOES exist in CDX (captured
2012-11-02, i.e. pre-election, 200 status) but by 2012-11-09 it 301-redirects
straight to `results.enr.clarityelections.com/CA/Santa_Clara/43231/index.html`
(verified via `curl -sI`, `x-archive-orig-date: Fri, 09 Nov 2012`, Location
header confirmed). So the legacy page family was NEVER populated with Nov
2012 general data -- it was retired in favor of Clarity before election day
-- and there is no case where the SAME page family shows both a "Semi-Final"
label AND a value independently known (via Clarity) to be the true election
night count. No calibration of the label is possible this way. (This also
confirms June 2012 was the LAST election Santa Clara ran on the legacy
system; Nov 2012 was Clarity's debut.)

## Step 3: scaling fallback -- APPLIED (Step 1 failed, per the method's own trigger)

Santa Clara's OWN Nov 2012 general night-plateau-to-next-day-canvass-start
growth (from `santa-clara-ca.json`'s existing sourced row, Clarity event
43231): night plateau ver 110787, "Updated 11/7/2012 4:14:04 AM PST" =
438,348 (996/1000 precincts) -> next-day canvass-start ver 111043, "Updated
11/7/2012 5:14:09 PM PST" = 460,329 (1000/1000 precincts). Ratio =
460,329 / 438,348 = **1.050145** (+5.01%).

Structural fit check: this Nov ratio's two stamps sit 13h (4:14 AM ->
5:14 PM) and ~21h14m after poll close (8 PM Nov 6 -> 5:14 PM Nov 7). June's
234,342 stamp (6/6/2012 7:02:03 PM) sits ~23h02m after poll close (8 PM
June 5 -> 7:02 PM June 6) -- close to the same elapsed-time position as
Nov's canvass-start stamp, which supports treating 234,342 as this
election's structural analogue of the Nov "canvass-start" point (both
Wednesday-evening, ~21-23h post-poll-close), NOT the night plateau itself.
This matches the original ceiling classification.

Applying the ratio in reverse (dividing the canvass-start-analogue value by
the ratio to back out an implied night-plateau) :

```
estimated June night plateau = 234,342 / 1.050145 = 223,152
estimated pct of certified final = 223,152 / 292,713 = 76.24%
```

**Assumptions and bias directions (stated honestly):**
1. Assumes June 2012's own night-to-Wednesday-evening growth curve tracks
   Nov 2012's night-to-Wednesday-evening growth curve (same registrar, same
   year, same VBM-processing regime). Reasonable but not verified for June
   specifically -- no independent June data point exists to test it.
2. Elapsed-time match is close (23h vs 21h) but not exact; June's stamp is
   ~2h further from poll close than Nov's canvass-start stamp, meaning
   slightly MORE growth time had elapsed for the 234,342 reading than for
   Nov's 460,329 reading. If growth continues past the canvass-start-analogue
   point, applying the Nov ratio may UNDER-correct (i.e. the true night
   plateau could be even a bit lower than 223,152) -- biases the estimate
   HIGH.
3. Countervailing bias: at Nov's night plateau, precincts were still short
   (996/1000) and part of the Nov ratio's growth is precinct-completion
   catch-up. June's earliest capture is ALREADY 874/874 (100% precincts),
   so if June's true night plateau also already had 874/874 (plausible for
   a smaller, non-presidential-scale primary), none of the ratio's
   precinct-completion component applies to June, and using the full Nov
   ratio removes too much -- biases the estimate LOW.
   These two effects partially offset; net direction is not confidently
   signable, so the estimate should be treated as a rough central value,
   not a tight bound.
4. Denominator/system difference: Nov 2012 ratio comes from Clarity
   (electronic, precinct-by-precinct granular uploads); June 2012 is the
   legacy GEMS-style batch page (updated by hand/less frequently -- only 3
   distinct states in the first 48 hours). Update cadence differs, so the
   two systems' "elapsed time since poll close" is not perfectly
   equivalent to "elapsed processing effort."

Sanity cross-check (not part of the task's prescribed method, but useful
context): the SAME ratio computed from Santa Clara's OTHER even-year
generals (2014 1.0704, 2018 1.0059-1.0668 depending on which next version
is used, 2022 1.0561, 2024 1.0175) ranges from +0.6% to +7.0%, median ~+5.0%
-- almost identical to the Nov 2012 figure used above (+5.01%), which is
mild independent support that +5% is a reasonable central estimate for this
county's Wednesday-evening-to-night-plateau gap, though the spread shows
real year-to-year variance and this is a primary (smaller electorate),
which may behave differently.

---

## Bottom line

CEILING STANDS (freeze test conclusively failed: digest changed at the very
next capture, and the full trajectory was recovered showing continuous
growth from 234,342 through 268,370, 284,025, to the certified 292,713,
which then froze July 3 - Dec 8 2012). 234,342 / 292,713 = 80.06% remains
the documented ceiling, confidence secondary, comparable:false, exactly as
graded.

SCALING OPTION (secondary/approximation, Mendocino-2012-precedent style):
apply Santa Clara's own Nov 2012 night-to-canvass-start ratio (+5.01%) in
reverse to the 234,342 Wednesday value -> estimated night plateau ~223,152
ballots ~76.24% of 292,713. Assumptions and both bias directions listed
above; net bias is not confidently signable given two offsetting effects
(elapsed-time mismatch pushes the estimate high; precinct-already-complete
mismatch pushes it low). This should be presented to the maintainer as an
explicitly-labeled approximation, not swapped in silently for the
234,342/80.06% ceiling row already drafted.
