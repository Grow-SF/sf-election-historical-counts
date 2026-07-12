# County election-night research: operator runbook

This is the complete manual for extending and verifying the cross-county
election-night dataset (`data/research/election-night/`). It is written for an
agent that was NOT part of building it. Follow it literally: every convention
here exists because a research pass got it wrong once, and every command is one
that actually ran. When this document and your intuition disagree, this
document wins; when the human's reading of a source disagrees with yours,
the human wins.

Companion skills: `.claude/skills/researching-election-night-share/SKILL.md`
(per-county research procedure) and
`.claude/skills/researching-jurisdiction-counting-tech/SKILL.md` (tech-adoption
records). This runbook is the shared reference they point into.

## 0. Documentation map (which manual for which job)

This runbook covers the CROSS-COUNTY election-night dataset. The project has
a second, older research domain: recovering SAN FRANCISCO's own historical
counts from newspaper archives. Its manuals already exist; do not reinvent
them:

| job | manual |
|---|---|
| County election-night share (this dataset) | this runbook + `researching-election-night-share` skill |
| County tech adoption records | `researching-jurisdiction-counting-tech` skill |
| SF historical recovery from newspaper archives (NewsBank via SFPL ezproxy, scan capture, OCR triage, vision transcription) | `docs/archive-recovery-runbook.md` (master) + `docs/analysis/newsbank-agent-playbook.md` (capture + reader-agent lessons) + `newsbank-election-recovery` skill (one-election procedure) |
| SF current results ingestion (DOE releases, certified totals) | `ingesting-doe-results` skill |
| CA statewide certified turnout (SoS Statement of Vote) | `sov-certified-turnout` skill |

Topic index across the manuals: Wayback mechanics live here (7.1) and in the
archive-recovery runbook's web/Wayback section; puppeteer renderers live
here (section 4) for public pages and in `scripts/archive-recovery/` for
SFPL/NewsBank (a logged-in session on a dedicated profile, reached only
through `scripts/research/iso_chrome.sh` — headless "new" for every worker;
the one visible window is the user-run login ceremony, see
`docs/archive-recovery-runbook.md`); OCR (`tesseract`) belongs ONLY to the SF
scan workflow: it is for locating/triaging results tables in scans, while
model vision does the digit transcription; nothing in the county dataset
needs OCR.

---

## 1. The metric (get this right or nothing else matters)

```
election-night % = ballots in the LAST report posted on election night
                   ÷ certified final ballots
```

- "Last report posted on election night" = the PLATEAU: the cumulative count
  in the county's final update of the continuous election-night count, before
  the county stops and resumes the multi-day canvass. Reports timestamped
  1 a.m. to 4 a.m. the next morning are still "election night" (Santa Clara
  2012 ran to 4:14 a.m.). A county's own labeled "Final Unofficial Election
  Night Results" posting counts even if posted mid-morning (San Bernardino
  2024 posted it at 10 a.m. Wednesday) so long as the canvass had not resumed.
- NOT the 8 p.m. first tranche. That is the classic mistake; it undercounts
  the night roughly 2x (it is just the pre-processed mail dump).
- NOT a next-day or later canvass update. If the only surviving number is
  post-night, see section 5 (ceilings) or record null.
- The denominator is ALWAYS the certified final ballot count from the CA SoS
  Statement of Vote (section 6.1). Never "% of registered voters", never
  "ballots counted to date". A share with the wrong denominator is worse than
  no share.

Calibration checks (use them): San Francisco's authoritative shares are
~71% (2012 presidential), ~66% (2016), ~57% (2024), ~59% (2018 midterm),
~51% (2022 midterm). If your county's number is near HALF the like-for-like
SF figure, you almost certainly grabbed the first tranche. If it is well
ABOVE the county's own adjacent elections, suspect a canvass-contaminated
next-day number.

Confounds to record, never to "fix": presidential vs midterm turnout
(compare like to like); the 2018-2020 Voter's Choice Act all-mail shift
(depresses election-night share independent of any tech); 2020 is a COVID
all-mail outlier and is deliberately excluded from the dataset.

## 2. The data layout

```
data/research/election-night/            # THE dataset (one dir; old v1-v3 iterations were deleted, git history has them)
  <slug>.json                            # one file per county (fresno-ca.json, ...)
  VERIFY.md                              # human-readable sheet: summary table + detail bullet per row
  MACHINE_CHECK.md                       # generated: presence-check status of every number
  HUMAN_VERIFY.md                        # generated: the hand-check packet for the human
  PLATEAU_REVIEW.md / plateau_review.json# committed plateau verdicts per sourced row
  render_verified.json                   # manifest of rows verified via JS rendering (see 7.4)
  CHANGES_v3_to_v4.md                    # historical provenance record; do not update
  cache/                                 # gitignored fetch cache; safe to delete, scripts refill it
packages/data/county_night.json          # DERIVED; never hand-edit; scripts/build_county_night.py writes it
packages/data/county_tech.json           # tech-adoption records (merge_county_tech.py writes it)
```

County JSON row schema (all fields required unless noted):

```json
{
  "date": "2016-11-08",
  "type": "presidential-general",
  "election_night_ballots": 177183,          // int or null
  "certified_final": 291890,                 // int, from SoS SoV
  "election_night_pct": 60.7,                // PERCENT with 2dp max (60.7 or 60.13); NEVER a 0.x fraction
  "vs_epollbook": "pre",                     // "pre" | "post" | "n/a"
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/...pdf",
  "source_url_night": "https://...",         // null when ballots is null; see 5.1
  "confidence": "primary",                   // "primary" | "secondary" | "none"
  "comparable": false,                       // OPTIONAL; only present when false; see 5.2
  "note": "..."                              // the full evidence trail; see 5.4
}
```

Hard field rules (the validator enforces most of these):
- `election_night_ballots` null => `election_night_pct` null, `confidence`
  "none", `source_url_night` null. `source_url_night` means "the source of
  the number used", never "a source we examined and rejected"; rejected
  sources go in the note as text.
- `election_night_pct` = round(ballots / final * 100, 2). Percent units.
- `confidence`: primary = official registrar release or archived official
  results page or SoS; secondary = local news, or a proxy/floor/ceiling
  value; none = null row.
- Editing these files: make SURGICAL text edits (targeted string
  replacement). The files mix indent styles; a whole-file `json.dump`
  rewrite creates a giant noisy diff. Pattern that works:
  compute the exact old substring (e.g. `"election_night_pct": 61.19`),
  assert it occurs exactly once, replace it. For note appends, take the
  parsed note string, JSON-escape it, find it in the raw text, replace with
  the escaped extended note.

## 3. The pipeline (run after ANY data change, in this order)

```bash
python3 scripts/research/validate_election_night.py     # offline consistency; MUST exit 0
python3 scripts/build_county_night.py                   # regenerates packages/data/county_night.json
python3 scripts/research/verify_en_denominators.py      # presence-check finals vs SoS PDFs (network, cached)
python3 scripts/research/verify_en_numerators.py        # presence-check night counts vs cited URLs (network, cached)
python3 scripts/research/build_en_verification_report.py # regenerates MACHINE_CHECK.md + HUMAN_VERIFY.md
uv run pytest tests/test_verify_election_night.py -q    # 17 tests, offline
pnpm vitest run                                          # chart tests consume county_night.json
```

- The validator cross-checks every row against VERIFY.md's summary tables and
  the SF control section against `packages/data/elections.json`. If you edit
  a county JSON you MUST edit the matching VERIFY.md table line and detail
  bullet, or the validator fails (that is the point).
- `county_night.json` and the two generated MD reports are committed, but you
  never edit them; you regenerate them. To check they are in sync without
  committing a date-only change:
  `python3 scripts/build_county_night.py && git diff -I '"generated"' --exit-code packages/data/county_night.json && git checkout -- packages/data/county_night.json`
- The numerator checker caches fetched artifacts by SLUG-DATE, not by URL.
  If you change a row's `source_url_night`, DELETE
  `data/research/election-night/cache/numerators/<slug>-<date>.*` first or
  the check silently re-reads the old page.
- MACHINE_CHECK/HUMAN_VERIFY must regenerate byte-identically from the same
  cache (`git status` clean after a rerun). If they do not, something is
  nondeterministic; stop and find it.

## 4. Tooling reference (what exists so you do not rebuild it)

All in `scripts/research/` unless noted. All share `en_common.py`:
`EN` (dataset dir), `CACHE`, `norm_pct`, `wayback_raw` (inserts `id_`),
`find_number(text, n)` (comma-aware presence check that refuses matches
embedded in longer numbers), `strip_html`, `pdf_text`, `fetch(url, dest)`
(curl with disk cache, 2s politeness pause, retries, delete-on-failure),
`load_rows()` (all county rows flattened, skips non-county JSONs like
render_verified.json).

| script | what it does |
|---|---|
| `validate_election_night.py` | offline invariants + VERIFY.md agreement + SF control check; exit 1 with one line per failure |
| `verify_en_denominators.py` | every certified_final vs the 6 SoS "Voter Participation Statistics by County" PDFs; county-line match |
| `verify_en_numerators.py` | every sourced night count vs its cited URL; gunzips Wayback raw replies; applies render_verified.json overrides (url + evidence-contains-claimed guarded) |
| `build_en_verification_report.py` | merges cache results + plateau_review.json into MACHINE_CHECK.md + HUMAN_VERIFY.md |
| `extract_plateau_evidence.py` | compact digest of every cached artifact: opening text, timestamps, plateau-vocabulary lines; the fast way to eyeball 54 sources |
| `fetch_clarity_versions.py` | Clarity CDN version brackets around each cited version (see 7.2) |
| `render_wayback.cjs` | puppeteer render of a JS Wayback page: `WB_URL="https://web.archive.org/web/<ts>/<orig>" node scripts/research/render_wayback.cjs` |
| `render_clarity_batch.cjs` | batch puppeteer render of Clarity pages |
| `iso_chrome.sh <headless\|login\|stop\|status>` | the ONLY sanctioned Chrome launcher (focus-safe: headless "new" only, no window, cannot steal focus); `login` is the one visible ceremony, gated behind a human-set `ISO_CHROME_LOGIN_ACK=yes` latch an agent cannot set itself; see `docs/superpowers/plans/2026-07-10-focus-safe-browser.md` |
| `iso_probe.js <browserURL>` | headless session-validity probe against an `iso_chrome.sh headless` profile; exit 0 authenticated, exit 3 auth wall |
| `validate_county_tech.py`, `merge_county_tech.py` | county-tech record validation + merge into county_tech.json |
| `validate_adoption_census.py` | validates `ca_adoption_census.json` (58-county schema + agreement with the researched county-tech records); exit 1 with one line per failure |
| `estimate_tech_effect.py` | matched-years difference-in-differences estimator over `county_night.json` (headline effect, placebo, jackknife inference, scenario/MDE projections) |
| `data/research/county-tech/ca_adoption_census.json` | not a script: the 58-CA-county adoption census (`status`: adopter/never/unknown, with sources/confidence per county) that `validate_adoption_census.py` checks and that Task 3's control-county selection (`docs/research/control-selection-2026-07.md`) was picked from |
| `scripts/build_county_night.py` | bakes county_night.json from the dataset + SF control from elections.json |

**The control-flag rule.** A jurisdiction is marked `control: true` in
`county_night.json` only when BOTH adoption years (`epollbook`, `asv`) are
null AND its `data/research/county-tech/<slug>.json` record independently
concludes never-adoption for both tracked technologies (status
`not-adopted`, or the schema fallback of no recorded adoption event, for
each). Null adoption years alone are never sufficient: an unresearched
county has null years too, and treating that silently as a control would
smuggle an unverified county into the comparison set. See `is_control()` in
`scripts/build_county_night.py` for the implementation.

pdftotext and jq are installed. `WebFetch` is BLOCKED for web.archive.org;
`curl` and puppeteer are not.

## 5. Dataset conventions for hard cases

### 5.1 Null per definition
If no on-night report survives anywhere (Wayback, county archive, press
release, news quote), the row is `ballots: null, pct: null, confidence:
"none", source_url_night: null`, and the note explains exactly what was
searched and why each candidate failed (list the CDX queries and captures
examined). Never substitute a different report time or denominator.

### 5.2 Ceilings, floors, comparable=false
- A value from a report posted ON election night that is slightly BEFORE the
  true final (e.g. the 10:30 p.m. report when the 10:42 p.m. final is
  unarchived) may be kept as a documented FLOOR: confidence `secondary`,
  note says "floor". (Example: Napa 2014.)
- A value from a POST-night report (next-day canvass state) may be kept ONLY
  as a documented CEILING with `"comparable": false`, confidence `secondary`,
  and a note saying it overstates the plateau. (Examples: Riverside 2024,
  Santa Clara 2014, Placer 2018.) `comparable: false` excludes the point
  from pre/post comparisons in the charts. In VERIFY.md, mark the row's
  year cell `| 2018 ⚠️ |`.
- When in doubt between ceiling-with-flag and null, prefer whichever the
  note can defend; both are honest, silence is not.

### 5.3 Confidence legend
News reportage is `secondary` even when it quotes officials. A county press
release republished VERBATIM by a news site may be `primary` (say so in the
note). Known open question: nevada-ca 2016/2018/2022 cite yubanet articles
but carry `primary`; the maintainer has deliberately left that call open. Do
not "fix" it silently.

### 5.4 Notes are the evidence trail
Every note states: the exact report used (its internal timestamp and
precincts-reporting), why it is the plateau (which later report or capture
proves it held / what the next report was), the first-tranche number it is
NOT, the arithmetic (numerator / denominator = pct), the pre/post tech
status, and the snapshot or version identifiers used. Corrections APPEND a
dated sentence ("CORRECTION (YYYY-MM-DD): ...") rather than rewriting
history. If a source needs a human browser, include the exact string
`FLAG for manual operator` in the note; the packet generator keys on it.

### 5.5 Plateau verdicts
`plateau_review.json` carries a verdict per sourced row: CONFIRMED /
PLAUSIBLE / REFUTED_AS_PLATEAU / REFUTED_AND_CORRECTED, with basis and
evidence. If you add or change a row, add/update its verdict record (and
regenerate the reports). A machine presence-check is NOT plateau evidence;
see section 8 for what counts.

## 6. Source playbooks, in the order to try them

### 6.1 Denominator: CA SoS Statement of Vote (always, first, non-negotiable)
`https://elections.cdn.sos.ca.gov/sov/<year>-general/sov/03-voter-participation-stats-by-county.pdf`
(2012 drops the `sov/` segment; 2014 uses `pdf/03-voter-particpiation-stats-by-county.pdf`,
misspelling intact). `pdftotext -layout`, find the county's line, take
"Total Voters". For odd-year municipals there is no statewide SoV; see the
`sov-certified-turnout` skill for what is and is not allowed.

### 6.2 Numerator route 1: the registrar's morning-after press release
Search `<registrar site>/news` or `/press-releases` for "semi-final" /
"semi-official results". The sentence "A total of N ballots were processed
and counted" IS the plateau, stated officially, no rendering needed. LA
County has this for every election back to 2012. One news-room page covers
all years; check it before anything else.

### 6.3 Numerator route 2: the county's dated report series
Counties post timestamped election-night reports; take the LAST one dated
election night:
- Napa: DocumentCenter PDFs literally titled "Last Unofficial Election Night
  Report".
- Fresno: `electionsummaryreportrpt_<M_D_YY>_<HHMM>.pdf` (the ~12:30 a.m. one).
- Nevada Co.: "First/Second/Third Report - Cumulative Results" PDFs; last = plateau.
- San Diego / San Mateo (recent): livevoterturnout ENR pages whose header
  says "FINAL UNOFFICIAL ELECTION NIGHT RESULTS / Final Election Night
  Report" plus the next-post schedule.
- Sacramento: eresults.saccounty.net inline Hart "SUMMARY REPORT" with
  `Run Date`/`RUN TIME` header.
- Orange: ocvote.gov archived "UNOFFICIAL RESULTS" cumulative, stamp ~1-2 a.m.
A live county CMS usually serves only the LATEST version; historical
versions come from Wayback (6.5) or Clarity (6.4).

### 6.4 Numerator route 3: Clarity ENR (the best-evidenced source there is)
See section 7.2. Immutable version-pinned JSON; you can usually recover the
exact last-of-night report AND prove it was last.

### 6.5 Numerator route 4: Wayback captures of the live results page
See section 7.1 for mechanics. Pick the LAST election-night capture; a
capture 1-4 days later that still shows the night state is a BONUS (proves
the plateau held); a capture whose embedded data moved is a warning.

### 6.6 Numerator route 5: local news
Morning-after articles ("At the end of election night, N ballots have been
counted") are usable at `secondary`. Distinguish quotes of the first
tranche from end-of-night statements.

### 6.7 When a source blocks curl
Some hosts 403 curl and WebFetch both (McClatchy papers, gvwire). Options,
in order: the puppeteer renderers (they present a real Chrome); a headless
Chrome via `scripts/research/iso_chrome.sh headless` (still no window, still
cannot steal focus); else put `FLAG for manual operator` in the note and
move on. Do not burn hours on a bot-wall. Browser escalation ends at
headless `iso_chrome.sh` — never fall back to a subagent driving a visible
browser (Claude-in-Chrome or otherwise); that is unscheduled and can steal
the user's focus.

## 7. The gotcha catalog (every one of these bit us)

### 7.1 Wayback
- Raw fetch form: insert `id_` after the 14-digit timestamp:
  `https://web.archive.org/web/<ts>id_/<original-url>`. Without `id_` you get
  the toolbar-wrapped rewrite.
- **Gzip bytes:** the raw `id_` replay serves the ORIGINAL bytes, which for
  many crawls are `content-encoding: gzip` that curl does NOT auto-decode.
  If a fetched file starts with bytes `1f 8b`, gunzip it before reading.
  (This alone caused 5 false NOT_FOUNDs in the first machine pass.)
- **CDX is how you enumerate captures:**
  `curl "http://web.archive.org/cdx/search/cdx?url=<exact-url>&from=YYYYMMDD&to=YYYYMMDD&output=json&limit=40"`.
  Use exact URLs and tight windows; broad domain queries 504. Add
  `matchType=domain` only for small hosts. The digest column tells you when
  two captures differ WITHOUT fetching them.
- **Replay aliasing:** a capture listed 200 in CDX can still be unservable:
  every replay form (`id_`, `if_`, plain, with/without `:80`) may 302 to a
  DIFFERENT timestamp. Check with `curl -sI` and look at `Location:`. This
  is how a "Nov 9 capture" fetched by machine turned out to contain a Nov 30
  report (Sacramento 2012). If CDX shows a distinct digest+length at the
  right time, the content existed; record it as machine-unverifiable and
  flag for a human browser attempt (the Wayback UI sometimes serves what
  curl cannot).
- **Framesets and JS shells:** old GEMS pages are framesets whose inner
  frames were often never crawled; modern ENR pages are JS shells whose
  numbers only exist after rendering. curl the shell to learn the
  structure, then render with `render_wayback.cjs`, or find the underlying
  data URL (Clarity sum.json, livevoterturnout data) and fetch THAT.
- **Archive your own evidence:** for a live version-pinned URL you relied
  on, request `https://web.archive.org/save/<url>` (a 302 response still
  saves) and cite the resulting snapshot. Verify the snapshot serves the
  number before citing it.

### 7.2 Clarity ENR (results.enr.clarityelections.com)
- URL anatomy: `/<ST>/<County>/<electionId>/<version>/json/sum.json`.
  Versions are immutable; the CDN still serves every version ever published.
- `sum.json` field `BC` (top-level, or `Contests[0].BC`) = countywide
  ballots cast. Sanity-check: the CERTIFIED version's BC equals the SoS
  certified total exactly.
- `electionsettings.json` (try `/json/en/electionsettings.json` then
  `/json/electionsettings.json`) carries `websiteupdatedat` (that version's
  publish time) and a `versions` array.
- **THE TRAP:** a version-pinned settings file lists only versions UP TO
  ITSELF. To enumerate the full history, first get the current version:
  `curl .../<eid>/current_ver.txt`, then read the CURRENT version's
  settings. Some versions' settings 404; a neighbor version's settings
  usually works (any later version's list covers the gap you care about).
- **The bracket proof (gold standard plateau evidence):** cited version
  stamped election night + the NEXT version in the full list stamped
  post-night (or same value later) proves the cited version was the last
  report of the night. Conversely this proof can REFUTE a row: Santa Clara
  2024's cited 4:46-p.m.-next-day version was exposed this way, and the true
  12:16 a.m. version (BC 460,325) recovered from the same CDN.
- Pre-~2016 "Web01"-era Clarity has HTML-only versions with no JSON; those
  overnight versions are usually unrecoverable (Santa Clara 2014).

### 7.3 GEMS / static report pages
- The header timestamp is the report GENERATION time, not the data time. A
  past-midnight stamp (12:29 a.m.) is genuine night data. A days-later stamp
  is NOT evidence of a frozen count: check a LATER capture of the same URL;
  if the number moved between captures, the page tracks the canvass and your
  days-later render is contaminated (this refuted Placer 2018: its Nov 9
  render was assumed frozen until the Nov 21 capture showed 162,802).
- A frozen live-results file that a later capture still shows unchanged IS
  good plateau evidence (Fresno 2016, Madera 2016).

### 7.4 JS-rendered sources and the override manifest
When a number is only visible after rendering (JS results widgets), verify it
by puppeteer, then record it in
`data/research/election-night/render_verified.json`:
`{slug, date, url, evidence, method}`. The numerator checker applies the
override only when slug+date+url match AND the evidence string contains the
claimed number, so a stale manifest cannot mask a later correction. Without
a manifest entry, the next machine pass flips your row back to NOT_FOUND.

### 7.5 County-page quirks
- Some county pages MISLABEL ballots-cast as "Registered Voters: N of M"
  (Sacramento 2018, Napa 2018). The per-contest "Times Cast" rows on the
  same page disambiguate. Check the arithmetic: N/M should equal the printed
  turnout percent.
- VCA-era Napa reports "Ballots Cast" as ballot CARDS (~2 per voter);
  "Times Cast" / "Voters Cast" is the voter count you want.

## 8. What counts as plateau evidence (for plateau_review.json)

CONFIRMED needs the artifact to self-describe as end-of-night (late-night
internal timestamp, or a last-of-night / semi-final title) PLUS one
non-circular leg:
- a Clarity version bracket (7.2), or
- a later capture of the same URL still showing the same count, or
- the county's own posting schedule bracketing the report, or
- the report series' next file being days later, or
- an official release stating the number as the election-night total.

PLAUSIBLE = self-description consistent but no independent leg obtainable.
REFUTED = evidence of first-tranche or post-night state (act per 5.2).
Re-finding the claimed number at the claimed URL is NOT evidence of
anything except citation integrity: the numbers originated from research
agents, so presence alone is circular.

## 9. Process rules (from hard experience)

- **Persist as you go.** Subagents die mid-task ("prompt too long", stalls).
  Every research subagent must append findings to a named file after EACH
  item (one file per item is safest), not accumulate them for a final
  message. Batch 1-2 elections per subagent, not 5.
- **Verify agents' claims against artifacts,** not their summaries. Reviewers
  in this project re-run commands and open cached files; reports have
  overstated brief permissions and missed embedded-number false positives.
- **The human verification loop:** the deliverable of any research pass is a
  packet the human can act on: URL + claimed value + what counts as a fail,
  one entry per row. `HUMAN_VERIFY.md` is generated in exactly that shape;
  keep it that way. The human's reading overrides any model's.
- **Always use real data.** Never hand-edit derived files (county_night.json,
  data/*.csv). Fix inputs, rerun generators. For SF data specifically, see
  the `ingesting-doe-results` skill.
- **No em dashes** in any prose you write (commit messages, notes, docs).
  Use comma/colon/parens.

## 10. Worked procedure: adding a new county end to end

1. Read `packages/data/county_tech.json` for (or research, via the
   county-tech skill) the adoption years; pick the Nov generals bracketing
   them (2012-2024, skip 2020).
2. Denominators for all rows from the SoS SoV PDFs (6.1).
3. For each election, walk routes 6.2 -> 6.6; capture the plateau number,
   its report timestamp, and the held/next-report evidence while you are
   there (you need it for 8).
4. Write `data/research/election-night/<slug>.json` per the section 2 schema
   (percent units!), with full notes per 5.4.
5. Add the county's section to VERIFY.md: summary table (same column format
   as existing sections, ⚠️ on comparable=false years) + one detail bullet
   per row (numerator URL, denominator URL, "look for" text).
6. Add plateau verdicts for the new rows to `plateau_review.json`.
7. Run the FULL pipeline from section 3; everything must pass.
8. Commit the county JSON + VERIFY.md + plateau_review.json + regenerated
   county_night.json/MACHINE_CHECK.md/HUMAN_VERIFY.md together.
9. Tell the human which rows landed non-CONFIRMED or secondary and what you
   want their eyes on (paths + claimed values + fail criteria).

Definition of done: validator exit 0; machine checks VERIFIED for every new
sourced row (or documented why not); a plateau verdict per new row; VERIFY.md
readable by a human with zero context; no derived file hand-edited.
