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

- Numerator, for the CDNC newspaper-era rows (1871-1928): the largest
  SINGLE-SEAT contest sum (all candidates in that one contest) readable from
  the day-after paper's returns, city + county as reported, with the precinct
  basis recorded. Multi-seat races are never summed. This is a FLOOR of the
  night count. The 1992 and 2004 news-derived rows take the numerator
  differently: certified ballots cast minus the registrar's stated uncounted
  remainder (see `denominators.md`).
- Denominator: the same contest's certified San Diego County total from the CA
  SoS Statement of Vote / CA Blue Book (see `denominators.md`), NOT ballots
  cast, so numerator and denominator share one definition. Exception: the
  news-derived 1992/2004 rows use certified total BALLOTS CAST as the
  denominator (see `denominators.md`, section "Certified county BALLOTS CAST
  (news-derived-floor denominators), 1988-2008"); there too numerator and
  denominator share one definition, but a different one.
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

## The morning/afternoon trap (cost us the 1932 row; read this first)

A "day-after issue" is only a night-count source if the paper was a **morning**
paper. Establish the edition type BEFORE trusting any figure:

- **Morning paper** (the San Diego Union: masthead reads "WEDNESDAY MORNING",
  returns clocked "this morning" / "at 3 o'clock this morning"): the day-after
  issue goes to press around 2-4 a.m. and captures the election-night plateau.
  Valid.
- **Afternoon/evening paper** (the Oceanside Blade-Tribune): the day-after
  issue goes to press around midday, so its returns are clocked "this
  afternoon" and describe a count that has already resumed the multi-day
  canvass, 16-20 hours after polls closed. That is a next-day **CEILING**, not
  a night count (RUNBOOK 5.2). The 1932 dossier initially recorded one as a
  night count and had to be corrected.
- **Weekly**: anything published days later is a canvass figure. Never a night
  count.

So every dossier must record (a) the paper's edition type and (b) the clock
phrase the returns themselves carry. If the figure is afternoon-clocked, record
it as a ceiling with a NULL share, and say so.

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
  against the year selector and Nov 1922 calendar, 2026-07-11), and NewsBank is
  now ruled out too: `newsbank-probe.md` (2026-07-12, run under an authenticated
  SFPL ezproxy session) found no San Diego Union source of any format before
  1970 (image edition `CSD5-EEDT` starts 2018; text source `SDUB` starts 1983),
  so 1914 and 1922 are MICROFILM-ONLY targets. The NewsBank leg itself is done:
  its text-only `SDUB` follow-up (`sdub-text-probe.md`) is what produced the
  1992 and 2004 rows.
- 2008-2024 rows already live in `data/research/election-night/san-diego-ca.json`
  (the cross-county panel), including the 2008 and 2010 rows this campaign
  recovered from the CA SoS status page (`wayback-probe-1994-2010.md`).
- Inside the 1922-2006 window the promoted CSV now carries 1924, 1928 (AP county
  table in a remote paper: `ap-remote-basis` lower bounds), 1992 and 2004
  (San Diego Union-Tribune via NewsBank: `news-derived`), plus 1932 as an
  afternoon-clocked CEILING with a NULL share. The remaining years in that
  window are dark, each probed and documented rather than silently skipped: see
  the dark-years list in `data/research/san-diego-history/README.md`.
- Promoted dataset: `data/research/san-diego-history/sd_night_history.csv`.
