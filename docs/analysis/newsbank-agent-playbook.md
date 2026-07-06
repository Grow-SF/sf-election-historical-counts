# NewsBank scan-reading playbook (capture + agent instructions)

Lessons institutionalized 2026-06-12 after the Feb-2008 results-box incident:
a 3-slice pan capture missed the bottom 40% of the page, and the reader agent
"exhaustively" searched slices that never contained the target, then concluded
the box "must be on B1" — wrong page, wasted budget, false negative.

## Capture layer

1. **Pan until bottom, not a fixed slice count.** Page height at capture zoom
   varies wildly (3 slices covered a 1964 broadsheet; Feb 2008 needed 7).
   Capture script must keep panning until the canvas content stops changing
   (bottom hit), then save the slice count in the filename or a manifest.
   Use `scripts/archive-recovery/capture_page.js` (pan-until-bottom; the old
   /tmp/nb_capfull.js and nb_cap1.js prototypes are gone, /tmp is ephemeral),
   or `sweep_section.js` for a page range.
2. **The OSD canvas shows only the viewport.** A "captured page" is only the
   visible band. Never treat a single fit-view capture as the whole page.
3. **Auth hard-stop** in every script: abort on 'Articles and Databases -
   Authentication' rather than saving garbage.

## Reader-agent prompt template — REQUIRED elements

1. **Coverage check first**: "Slices are vertical bands, top to bottom.
   Before searching, confirm the LAST slice shows the page's bottom edge
   (margin/border/page rule). If it does not, STOP and report
   'page bottom not captured' — do NOT conclude the content is absent."
2. **Two distinct null verdicts**: `not-in-scans` (capture incomplete) vs
   `not-on-page` (full page verified, content absent). Never report the
   second when the first is possible.
3. **Masthead first**: report the masthead date exactly as printed before
   extracting anything. NewsBank issue labels are NOT uniformly offset
   (1983 label = masthead+1; 1975-12 label = masthead). Never date an
   observation from the label.
4. **Numeric anchors in the prompt are approximate context only** — never
   use them to decide what a digit "should" be (a misremembered certified
   total once sent an agent reasoning against a correct read). Read the
   pixels; sanity-check arithmetic happens downstream.
5. **Crop recipe** (agents repeatedly fumbled this): crops operate on the
   SLICE file with fractions of THAT slice. For a results column, crop a
   tall band: `crop_helper.py <slice> 0.27 0.0 0.50 1.0 out.png`. Two-step
   zoom: column first, then single-contest rows. Budget ~15 crops/page but
   stop as soon as the target is transcribed.
6. **Persist after every finding** (one CSV row per contest), including
   null rows with the verdict category. A dead agent must cost nothing.
7. **Transcribe digits exactly**; uncertain digits get `?`; "illegible" is
   an acceptable answer, guessing is not.

## Where the 2000s data lives (confirmed Feb 2008)

The Chronicle TEXT archive stops printing vote tables ~2002, but the print
IMAGE edition (available through 2017) runs a results box — e.g. "BAY AREA
ELECTION RESULTS" with a per-county column including San Francisco, each
measure with a "N of M precincts reporting" line — in the FIRST FEW PAGES
OF SECTION B of the day-after paper. Recipe per thin election:
1. Browse the day-after issue in image format (action=browse&format=image).
2. Locate section B pages 1-4 (absolute page index ~18-28 for that era).
3. Full pan-until-bottom capture of each; tesseract-triage for
   "ELECTION RESULTS|precincts reporting".
4. Read the San Francisco column; PCT-validate; largest contest sum =
   conservative night floor; precincts < 100% ⇒ mark night_partial.

Day-after targets: ALL TEN captured and ingested as of 2026-06 (rows in
`data/sf_archival_canvass_points.csv` for the 2002-2012 thin elections);
kept here for provenance. New thin elections follow the same recipe.

## Verification pipeline (unchanged, works)

Haiku/Sonnet transcribe → arithmetic gates vs DOE certified columns
(sum ≤ certified ballots; monotone vs neighboring observations; PCT match
within 1pt) → independent re-read of load-bearing digits → user hand-read
is the authoritative tiebreaker.
