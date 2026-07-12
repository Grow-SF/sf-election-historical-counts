# San Diego County deep-history night-count recovery (2026-07-11)

Reproduces the SF "century of election nights" campaign for San Diego County,
using the San Diego Union (CDNC, paper code `SDDU`, digitized 1871-1922) as the
morning-after source. Companion manuals: `docs/research/RUNBOOK.md` (metric +
process rules), `docs/analysis/2026-06-13-pre1964-night-floor.md` (the SF
method this mirrors), `docs/research/night-recovery-2026-07-09/` (the SF wave
dossiers whose format these files follow).

## Metric

```
night share = ballots counted per the MORNING-AFTER paper (last pre-press count)
              / certified final for San Diego County
```

- Numerator: the largest SINGLE-SEAT contest sum (all candidates in that one
  contest) readable from the day-after San Diego Union's returns, city + county
  as reported, with the precinct basis recorded. Multi-seat races are never
  summed. This is a FLOOR of the night count.
- Denominator: the same contest's certified San Diego County total from the CA
  SoS Statement of Vote / CA Blue Book (see `denominators.md`), NOT ballots
  cast, so numerator and denominator share one definition.
- Gates (reject/flag on failure): masthead date == expected issue date;
  contest sum <= certified contest total; precincts-reported ratio <= 1;
  uncertain digits marked `[?]` and listed for human re-read.

## Source access

- CDNC sits behind Cloudflare: curl/WebFetch are blocked; a raw-CDP Chrome
  session passes (never send Runtime.* before the challenge clears). Chrome is
  already running on 127.0.0.1:9222, launched hidden/off-screen. NO-FOCUS
  RULES: background tabs only (`newWindow:false, background:true`), never
  bringToFront, close your tab when done.
- Tools (paths are absolute):
  - `scripts/archive-recovery/cdnc_fetch.js` - issue TOC / section OCR /
    scoped search (saves OCR under `mirror/cdnc/<issue>/`).
  - `/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/cdnc_shot.js <PAGE_OID> <OUT.png>` -
    full-page viewer screenshot.
  - `/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/cdnc_zoom.js <PAGE_OID> <FX> <FY> <CLICKS> <OUT.png> [PANX PANY]` -
    zoomed legible capture toward a fractional point of the page (3 clicks ~=
    digit-legible). Screenshots go under `mirror/cdnc/screenshots/` (gitignored).
- CDNC rate-limits bursts: pause >=3s between navigations; on an empty TOC
  (0 sections) retry up to 3x with 20s backoff - issues that exist sometimes
  return empty under load.

## Method per election (proven on 1908)

1. TOC the day-after issue (`SDDU<YYYYMMDD+1>`); grep for returns sections
   (e.g. 1908: `.2.47` county table, `.2.51` city article). If returns are
   absent, TOC day+2 for the "complete/official count" and record the day-after
   state as the finding (a slow count is itself a finding).
2. OCR the returns sections (locates numbers; digits are often garbled).
3. Zoom-capture the returns table and vision-read the digits from the
   screenshots, never from OCR alone. Sum ONE single-seat contest across all
   printed precinct rows (city wards + county towns). Cross-check against any
   printed running-total row and against the prose articles.
4. Apply the gates; write the dossier file BEFORE moving to the next election.

## Files

- `denominators.md` - certified SD county contest totals per election (SoV /
  Blue Book provenance).
- `<yyyy-mm-dd>.md` - one dossier per recovered election: sections used, scan
  and OCR paths, transcribed rows, arithmetic, gate results, verdict + share,
  human-verification asks.
- Verdicts use the wave-3 vocabulary: night count / floor / NOT PRINTED /
  gate-flagged.

## Coverage notes

- Scope extended 2026-07-12 to the full digitized run: statewide generals
  1871-1920 (1871/1875/1879 state elections were held in SEPTEMBER; the
  early-1870s paper may be weekly and/or under a different CDNC code, so
  those dossiers document the nearest-after issue used).
- CDNC `SDDU` has no 1914 issues at all and no November 1922 issues (verified
  against the year selector and Nov 1922 calendar, 2026-07-11): 1914 and 1922
  generals are NewsBank/microfilm targets, tracked as a separate leg (needs
  an SFPL ezproxy login; NewsBank's San Diego Union coverage unprobed).
- 2012-2024 rows already live in `data/research/election-night/san-diego-ca.json`
  (the cross-county panel); the 1922-2010 gap is unrecovered.
- Promoted dataset: `data/research/san-diego-history/sd_night_history.csv`.
