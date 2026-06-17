---
name: newsbank-election-recovery
description: Use when ingesting a historical San Francisco election that is missing from the DOE turnout table (odd-year municipals, primaries, specials) and its election-night vote count must be recovered from the SF Chronicle NewsBank image archive via SFPL ezproxy. One election per run; safe to run many in parallel, one per election.
---

# NewsBank SF-election recovery (one election → structured record)

Recover a single San Francisco election's **election-night count floor** and
**certified/complete total** from the *San Francisco Chronicle* NewsBank image
edition. One run = one election. Many runs are safe in parallel (each opens its
own Chrome window via CDP).

## Prerequisites (already set up by the operator — do NOT touch credentials)
- Chrome is running with `--remote-debugging-port=9222`.
- The SFPL ezproxy NewsBank session is logged in (the human logs in manually;
  never automate or enter credentials).
- Licensed content stays in the **gitignored** `mirror/newsbank/scans/` tree.
  Only figures + citations (docref / scan filename) are ever committed — never
  the page images.

## Environment for every shell command
```
cd /Users/sbuss/workspace/sf-election-count
export PATH="/Users/sbuss/.nvm/versions/node/v22.21.1/bin:$PATH"
export NODE_PATH="$(pwd)/viz/node_modules"
```

## Step 1 — capture the day-after pages
The returns box is almost always on the **front page** of the **day-after**
issue; the complete "total vote of city" may be on the front page (machine era,
~1928+) or only in the **two-days-after** issue (slower hand-count era).

```
node scripts/archive-recovery/sweep_section.js <ELECTION_DATE> <ISSUE_DATE> <P0> <P1> <WIN>
```
- `ELECTION_DATE` e.g. `1927-11-08`; `ISSUE_DATE` = election date + 1 day.
- `P0 P1` = page range, use `1 3` (front pages carry the returns box + totals).
- `WIN` = a distinct integer per parallel run (staggers the window position).
- Output: `mirror/newsbank/scans/sweep_<ELEC>_issue<ISSUE>_p<page>_s<slice>.png`
  (dates with dashes stripped). If it prints `NO ENTRY`, the free-text search
  found no issue for that date — try the alternate spelling or an adjacent date.

If the day-after returns are partial and no complete citywide total appears,
also capture the **two-days-after** issue the same way (`ISSUE_DATE` + 1).

## Step 2 — transcribe the scans (vision, not OCR libraries)
`Read` each captured slice (they render visually; downscale can blur them — if a
number is ambiguous, crop+upscale with `sips` and re-read). Extract, verbatim:
- **Precincts reported**: "X of Y precincts" / "X precincts, complete, out of Y"
  + any timestamp ("at 2 o'clock this morning", "semi-official", edition slug).
- **Every single-seat contest** (Mayor, Sheriff, District Attorney, City
  Attorney, Treasurer, Recorder, Assessor, Auditor, Tax Collector, etc.) with
  each candidate's exact vote. For a single-seat office, **sum ALL its
  candidates** = ballots cast in that contest. The **largest** such sum is the
  election-night **count floor** (numerator). Skip multi-seat races (Supervisors,
  Police Judges) — they aren't a ballot count.
- **Complete "total vote of city" = N** (all precincts) if printed = the
  certified denominator. Note the precinct basis and whether it's
  "semi-official" vs "official canvass".
- Any **registration** figure.

## Step 3 — verification gates (reject if any fails)
- Masthead date on the scan == ISSUE_DATE (you grabbed the right issue).
- Largest contest sum ≤ complete total vote (a contest can't exceed turnout).
- Precincts-reported ratio is sane (numerator/denominator ≤ 1).
- Numbers re-read at high zoom; mark any uncertain digit `[?]` and flag it.

## Step 4 — return a structured record
Return ONLY this (the operator appends it to
`data/sf_archival_canvass_points.csv` and rebuilds):

```
election_date:   YYYY-MM-DD
election_name:   e.g. "General Municipal Election" / "Direct Primary"
observed_at:     ISSUE_DATE T<hh:mm>:00  (use the box's clock time, else T03:00:00)
night_floor:     <largest single-seat contest sum>   (ballots_counted_total)
night_contest:   which office + the candidate sums that produced it
precincts:       "<reported>/<total>"  + status (semi-official / complete)
certified_final: <complete total vote of city>   OR  "DOE" if to be taken from
                 the DOE turnout table   OR  "needs-2day-capture" if not found
certified_src:   issue + page + scan filename for the complete total
night_src:       issue + page + scan filename for the returns box
edition:         masthead edition slug if any
confidence:      high / medium / low  + any [?] digits
```

Do not write to the CSV yourself; just return the record. Keep the scans in
`mirror/newsbank/scans/` (gitignored) for the operator to spot-check.

## Common mistakes
- **Summing a multi-seat race** (Supervisors, Police Judges) as a ballot count —
  voters cast multiple votes, so the sum exceeds turnout. Only single-seat
  offices give a valid floor.
- **Using the winner+runner-up only** when a single-seat race has 3+ candidates —
  sum *all* candidates in that one office; that equals ballots cast in the contest.
- **Trusting a turnout *estimate*** ("Zemansky estimated 125,000–130,000") as the
  certified total. Estimates are not the denominator; find the printed complete
  "total vote of city," or fall back to DOE, or report `needs-2day-capture`.
- **Reading the downscaled `Read` thumbnail** and guessing digits. Crop + upscale
  with `sips` and re-read; mark any unsure digit `[?]`.
- **Grabbing the wrong issue**: always confirm the masthead date == ISSUE_DATE.
- **Reusing another run's `WIN` index** in parallel — windows fully occlude and
  one capture comes back blank. Give every concurrent run a distinct `WIN`.
