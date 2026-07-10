# Human-verification packet v2: primaries-phase judgment calls

This packet supersedes `scratchpad/human-verify-consolidated.md` (v1)
completely. It carries forward every v1 item that is still open, marks the
v1 items the maintainer already resolved (dated, per the ledger
`.superpowers/sdd/progress.md`), and adds the new judgment calls raised by
the primaries-expansion campaign: the 17 county primary dossiers, the
Nevada tech adjudication, the SoS-vs-committed adjudication, and the
browser-recovery sweep's credential-bound list.

Scope note: this does NOT restate ordinary mechanical presence/plateau-read
rows (source URL, does the page say what it claims) unless a judgment call
rides on top of one. Ordinary rows still live in
`data/research/election-night/HUMAN_VERIFY.md` and each county's
`PLATEAU_REVIEW.md` entry.

Ordering: most-consequential-first, where "consequential" means how much a
reversed call would move `docs/analysis/2026-07-10-tech-effect-estimate.md`'s
headline or reclassify a county's pre/post treatment window. Tier A =
headline movers / treatment-window reclassifications. Tier B = value and
classification checks. Tier C = documentation-only / credential-bound /
zero current consequence.

No em dashes used below.

---

## TIER A: headline movers and treatment-window reclassifications

### A1. Nevada County: two tech-adoption dates are proposed to move by 4-6 years, reclassifying 6+ rows across generals and primaries

**Consequence if adopted:** highest in this packet. This is not a value
correction, it is a proposed change to Nevada County's `pre`/`post`
treatment windows for BOTH tracked technologies. If adopted as recommended:
ASV moves from adopted_year 2022 to 2016 (flips 2016-11, 2018-11, and
2018-06 from `pre` to `post`); e-pollbook moves from adopted_year 2018 to
2014, split-record (flips 2014-11, 2016-11, and 2016-06 from `pre` to
`post`, and marks 2014-06 as a non-comparable partial-pilot election rather
than clean `pre`). Nevada is a treated county in the panel; this changes
which of its rows sit in which cohort, which changes both its own
before/after delta and the aggregate `any`/`epb`/`asv` computations. NOT
YET LANDED: `data/research/county-tech/nevada-ca.json` still reads ASV
`adopted_year: 2022` and epollbook `adopted_year: 2018` as of this
writing; the adjudication below is a proposal awaiting maintainer sign-off.

- What to open:
  1. ASV leg: `https://nevco.legistar.com/View.ashx?M=F&ID=4686315&GUID=8629A10C-62AE-48AC-9004-41FA82CB8A51`
     (the executed ES&S Mail Ballot Verifier contract, machine-readable
     PDF, Board-adopted 9/27/2016). Also see the Legistar detail page:
     `https://nevco.legistar.com/LegislationDetail.aspx?GUID=F2AD1997-3E3E-4C30-80F7-21F54318ADDF&ID=2840587`.
  2. Epollbook leg: `https://web.archive.org/web/20150222033106/http://yubanet.com/regional/Trading-in-the-Paper---Nevada-County-s-Electronic-Poll-Book-Journey.php`
     (Clerk-Recorder Gregory Diaz, Feb 2015, on-the-record).
- Claimed / decisive quotes (evidence lives partly in scratch working
  files, quoted here so the packet is self-contained):
  - Contract Exhibit B, equipment list: "1 MBV 1000 Transport ... 1 MBV
    Software with imaging adjustable signature block and barcode scanning
    ... 1 'No Signature' Detection ... 1 Automated Signature Recognition
    Software ... Election setup support and training- 2016 General
    Election $3,150.00." Exhibit A: "Anticipated Initial Term: 10/1/2016
    through 9/31/2017."
  - Diaz, Feb 18 2015: "During the 2014 election cycle, the Nevada County
    Elections Office implemented electronic poll books to replace paper
    rosters in all polling places across the county."
- Two things specifically need the maintainer's judgment, not just a
  document check:
  1. **The ASV live-use caveat.** The contract proves Board approval and
     intended first-use timing (support term starting 10/1/2016, a line
     item contractually named for "2016 General Election"), but no
     independent post-election source (news, canvass report, Grand Jury
     report) confirms the MBV 1000 was actually live and processing
     signatures on Nov 8, 2016. The proposed 2016 revision rests on
     contractual intent, not a confirmed go-live date.
  2. **The 2014-keying modeling choice for epollbook.** The proposal keys
     `vs_epollbook` on 2014 (the traditional precinct roster's full
     deployment) rather than 2018 (the VCA vote-center e-pollbook), on the
     reasoning that keying on 2018 would double-count the VCA/vote-center
     transition under two flags at once (the county-tech schema already
     tracks `vote-center` separately, adopted_year 2018). This is a
     genuine modeling choice about what the `epollbook` variable should
     measure, not a fact-finding question. Full reasoning:
     `scratchpad/nevada-tech-adjudication.md`.
- What counts as a fail: the maintainer reads the contract and disagrees
  that "election-dated support term + named line item" is strong enough
  evidence of 2016 go-live without an independent use-confirmation; or
  disagrees that the epollbook flag should key on the traditional-roster
  date rather than the VCA date.
- What happens on failure (or on partial acceptance): edit
  `data/research/county-tech/nevada-ca.json` (`asv` and `epollbook`
  entries, plus `adoption` top-level fields) and
  `data/research/election-night/nevada-ca.json` (`adoption` fields; no row
  values change, only `vs_asv`/`vs_epollbook` tags once those rows exist).
  Then rerun `scripts/build_county_night.py`,
  `scripts/research/verify_en_denominators.py`,
  `scripts/research/verify_en_numerators.py`,
  `scripts/research/build_en_verification_report.py`, and
  `scripts/research/estimate_tech_effect.py`; recompute the headline table
  in `docs/analysis/2026-07-10-tech-effect-estimate.md`.

---

### A2. Napa County 2014-11-04: the landed value was replaced by an SoS figure AFTER the maintainer had already verified the prior value as correct

**Consequence if reversed:** high, and distinct in kind from a normal value
check: this is a case where a maintainer verdict was overtaken by a later
automated process without being re-presented for sign-off. Per the ledger,
the maintainer verified "napa-ca 2014 general CORRECT" on 2026-07-10 (at
that time the landed value was 18,286 ballots / 47.17%, sourced from the
county's own 10:30 PM page). Later the same day, the SoS status-page sweep
found the state's own reporting system showed a later, fuller count for the
same night (19,515 ballots, Last Report "Nov 4 11:14 p.m."), and an
adjudication pass replaced the row with that figure. **The currently landed
value is 19,515 / 50.34%, not the 18,286 / 47.17% the maintainer signed off
on.** Napa is a treated county (2018 VCA adopter) and this row sits in its
PRE window; a ~6.7% swing in one pre-period point moves that county's own
delta and the pooled PRE baseline for its cohort.

- What to open: `data/research/election-night/napa-ca.json` (2014-11-04
  row, currently landed at 19,515/50.34%). Cross-check sources:
  - County's own last web report: `https://web.archive.org/web/20150916061050/http://countyofnapa.org/ElectionResults/20141104/20141104-2230_dtl.htm`
    (reads "Last Updated: November 4, 2014 10:30 PM," Total 18,286, 25.94%).
  - SoS status-page state now used instead:
    `https://web.archive.org/web/20141105141649/http://vote.sos.ca.gov/returns/status/`
    (Napa row: 167/167 100.0%, 19,515, "Last Report: Nov 4 11:14 p.m.",
    frozen through `https://web.archive.org/web/20141107083801/http://vote.sos.ca.gov/returns/status/`
    two days later, before jumping to 35,800 on Nov 14).
- What counts as a fail: the maintainer prefers the county's own
  last-crawled web report (18,286) over the state's later, fuller
  aggregation (19,515) as the "election night" figure, for example on the
  theory that the county's OWN public posting is what the public actually
  saw election night, even if the county kept transmitting data to the
  state afterward.
- What happens on failure: revert `data/research/election-night/napa-ca.json`'s
  2014-11-04 row to `election_night_ballots: 18286`,
  `election_night_pct: 47.17`, restore `source_url_night` to the county
  capture, and record BOTH the original maintainer verification and the
  reversal with dates in the row's note (do not silently drop either). Rerun
  the verify_en_* + build pipeline and recompute the headline. Also
  double-check `packages/data/county_night.json` if this row is mirrored
  there.
- Same-pattern items, lower priority (bundled below in B1) since they were
  never separately maintainer-verified before the SoS replacement:
  del-norte-ca.json 2016-11-08 (8,155 to 8,450) and riverside-ca.json
  2024-11-05 (611,101 ceiling to 547,742 comparable plateau).

---

### A3. Santa Clara 2016-11-08: does a 10:28 AM Wednesday report count as election night? (carried forward from v1, unresolved)

**Consequence if reversed:** high. Santa Clara is a treated county
(2020-adopter cohort) with one of the larger positive per-county effects in
the panel (13.35 pp per the prior analysis). If this row is downgraded to a
non-comparable ceiling, Santa Clara loses one of its best-evidenced
post-adoption points.

- What to open: `data/research/election-night/santa-clara-ca.json`
  (2016-11-08 row, landed at 443,269/724,596 = 61.17%).
  Source: `https://web.archive.org/web/20260710174832/https://results.enr.clarityelections.com/CA/Santa_Clara/64404/182800/json/sum.json`
  (`BC: 443269`) and the settings snapshot
  `https://web.archive.org/web/20260710174839/https://results.enr.clarityelections.com/CA/Santa_Clara/64404/182800/Web01/en/json/electionsettings.json`
  (`websiteupdatedat` "11/9/2016 10:28:40 AM PST").
- The judgment call: this version's internal timestamp is 10:28 AM the
  Wednesday morning after election night, not an overnight hour. It was
  counted as election night because the continuous count had not yet
  broken (the next report, 5h13m later, shows the cadence collapse the
  runbook treats as the plateau marker: overnight pace ~5,700-15,400/hr
  drops to ~1,406/hr), but a human could reasonably read a Wednesday-morning
  report as post-night by clock time alone.
- What counts as a fail: the maintainer reads 10:28 AM Wednesday as
  post-night regardless of the cadence evidence.
- What happens on failure: set `comparable: false` on this row, update its
  note and `PLATEAU_REVIEW.md` verdict, rerun the verify_en_* + build
  pipeline, and recompute Santa Clara's per-county effect and the headline
  in `docs/analysis/2026-07-10-tech-effect-estimate.md`.

---

### A4. Placer County 2024-03-05: a new CONFIRMED recovery closes the panel's only post-adoption primary for this county, and it is a contrarian result

**Consequence if adopted:** high. Placer had zero post-adoption primary
data before this recovery (its only pre-Nov-2026 chance to observe a
post-Sign-Scan-and-Go primary). The new figure is 69,436 / 135,869 =
**51.11%**, which is LOWER than Placer's pre-adoption primary range
(61.91% in 2016-06, 69.75% in 2012-06), the opposite direction from the
scout's own working hypothesis that in-person Sign-Scan-and-Go processing
would push the post-adoption share higher. A surprising result filling a
previously-empty, structurally important cell deserves a sanity check
before it lands and enters the treated-county POST computation. NOT YET
LANDED: no 2024-03-05 row exists yet in
`data/research/election-night/placer-ca.json`.

- What to open: `https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status`
  (CA SoS per-county reporting-status table; Placer row: Ballots Cast
  69,436, 100.0% precincts reporting, "Last Report: Mar 6 12:04 a.m.").
  Bracket proof (value held 2.5 days, then jumped): `https://web.archive.org/web/20240308155126/https://electionresults.sos.ca.gov/returns/status`
  (still 69,436) and `https://web.archive.org/web/20240309194502/https://electionresults.sos.ca.gov/returns/status`
  (jumps to 93,100, "Last Report: Mar 8 4:52 p.m."). First-tranche control
  (not used): `https://web.archive.org/web/20240306063830/https://electionresults.sos.ca.gov/returns/status`
  (51,885 at 9:54 PM Mar 5, the true first tranche, correctly excluded).
- Claimed: election-night ballots 69,436, certified final 135,869, pct
  51.11%, evidence class CONFIRMED (self-describing timestamp + double
  non-circular bracket).
- What counts as a fail: the SoS table's Placer row does not read Ballots
  Cast 69,436 with Last Report "Mar 6 12:04 a.m." at the cited capture, or
  a human judges the falling share should be attributed to something the
  scout did not account for (e.g., a Placer-specific mail-processing
  slowdown unrelated to Sign-Scan-and-Go) before it is presented as a
  finding about the technology's effect.
- What happens on failure: if the value itself is wrong, do not land it and
  keep Placer's 2024-03 row null. If the value is right but the maintainer
  wants the contrarian framing corrected before it lands, add the row with
  an explicit note on the direction (do not silently smooth it toward the
  scout's original hypothesis). Either way, once landed: rerun the
  verify_en_* + build pipeline and recompute the headline and Placer's
  per-county effect.

---

### A5. Mendocino primaries 2018-06-05: an outlier-high 83.20% PLAUSIBLE estimate in a control county

**Consequence if adopted:** high. Mendocino is a control county; a control
row that is structurally unusual pulls on the control baseline used to
compute every treated county's adjustment (this is the same mechanism that
made Lake County's classification the top item in v1). NOT YET LANDED: no
2018-06-05 row exists yet in `data/research/election-night/mendocino-ca.json`.

- What to open: `https://theava.com/archives/83237` (Anderson Valley
  Advertiser, "Mendocino County Today: Wednesday, June 6, 2018," live URL,
  re-verified still showing the same text).
- Claimed / decisive quote: the article distinguishes two checkpoints in
  one rolling post: "late Tuesday night" ("over a quarter of the votes
  counted," the first tranche, correctly NOT used) versus "UPDATE
  (Wednesday 8:40am) With all precincts reporting and just over 40% of the
  ballots cast (19,049) the local trends are holding." Arithmetic:
  19,049 / 47,487 registered = 40.11%, matching "just over 40%" exactly.
  Against the certified final (22,896 voters): 19,049 / 22,896 = **83.20%**.
- What counts as a fail: 83.20% is well above this county's other primary
  years (2014: 57.86%, 2016: 40.35%) and its own 2018 GENERAL (46.57%). The
  scout's structural explanation (2018 primary VBM was 19,830 of 22,896
  certified, i.e. mostly already returned by election day) is plausible but
  unverified by an independent second source; a human should judge whether
  this explanation is sufficient before the row is treated as PLAUSIBLE
  rather than discarded or downgraded.
- What happens on failure: if rejected, record the row null per Runbook 5.1
  rather than landing the estimate (mirrors the Mendocino 2012-general
  precedent, where a rejected estimate is preserved in the note as
  history). If accepted as-is, land the row with `confidence: "secondary"`,
  plateau verdict PLAUSIBLE, and rerun the pipeline; Mendocino's cohort
  membership as a control means this changes every treated 2018-cohort
  county's control-adjustment.

---

### A6. Del Norte's numerator PDFs are image-only scans, read visually, not machine-OCR'd (carried forward from v1, now spans both generals and a pending primary)

**Consequence if reversed:** moderate-high. Del Norte is a control county
contributing the largest number of panel-years of any control (5 generals
already landed, plus up to 6 more primary years pending integration), and
its values sit at the high end of the control range (53.67% to 89.18%),
distinctly different in level from SF/Lake/Mendocino. A single misread
digit would be hard to catch by cross-county plausibility alone because
this county's whole level is already an outlier by design (small rural
county).

- Files: `data/research/election-night/del-norte-ca.json` (5 landed general
  rows: 2014, 2016, 2018, 2022, 2024) plus
  `data/research/election-night/render_verified.json`. Primary rows
  (2016-06, 2018-06, 2022-06, 2024-03) are drafted in
  `scratchpad/dossier-del-norte-ca-primaries.md`, not yet landed, and carry
  the same risk.
- Why this is distinct from an ordinary mechanical check: every one of
  these PDFs is a Canon-photocopier scan with no text layer (`pdftotext`
  returns empty on all of them, independently confirmed). Every claimed
  ballot count was read by an agent visually inspecting a 150dpi-rendered
  PNG, not extracted by text-matching. Per the runbook's
  human-verification-loop rule, the human's reading of the linked PDF
  overrides the agent's on any discrepancy, and this is the one category in
  the whole panel where that rule is load-bearing on nearly every row for
  one county.
- What to open (generals, already landed): the 5 Wayback/Drive URLs already
  cited in `del-norte-ca.json`'s rows (2014, 2016, 2018 via
  `sites.googlegroups.com` Wayback captures; 2022, 2024 via
  `drive.google.com/uc?export=download&id=...` direct downloads). For the
  pending primaries, the Google Drive folders:
  `https://drive.google.com/drive/folders/1nwgviB22IuQIVWjSquSY6Y_6APYvMgnH`
  (2016), `https://drive.google.com/drive/folders/1j_tx1oilfY7jlehwAx8Njwa7WH21-_CQ`
  (2018), and two more cited in the dossier for 2022/2024.
- What counts as a fail: any digit in the visually-read ballot count or
  precinct count differs from what a human reads directly off the same PDF
  page.
- What happens on failure: correct the specific row's ballots/pct,
  correct `render_verified.json`'s entry, rerun the verify_en_* + build
  pipeline, and recompute the relevant per-county and aggregate numbers.

---

## TIER B: value and classification checks

### B1. Two more SoS-replacement values the maintainer may want to eyeball (del-norte-ca 2016-11, riverside-ca 2024-11)

**Consequence if reversed:** moderate for each; both are already landed and
neither was separately maintainer-verified before the swap (unlike Napa,
item A2), so this is a lower-priority version of the same check.

- **del-norte-ca.json, 2016-11-08.** Landed value 8,450 / 9,790 = 86.31%
  (was 8,155 / 83.30%, the county's own scanned Release 4 PDF). What to
  open: `https://web.archive.org/web/20161110185817/http://vote.sos.ca.gov/returns/status/`
  (Del Norte row: 18/18 100.0%, 14,318, 8,450, "Last Report: Nov 8 11:38
  p.m.," frozen 5 days before jumping to 9,790 on Nov 16, which matches the
  certified final and the county's own Nov 16 Release 6 exactly). What
  counts as a fail: the maintainer judges the county's own "Election Night
  Final" self-declaration at 10:47:49 PM (8,155) should outrank a
  51-minutes-later state fed by the same county's backend pipeline.
- **riverside-ca.json, 2024-11-05.** Landed value 547,742 / 959,098 =
  57.11%, `comparable: true` (was 611,101, flagged `comparable: false` as
  a next-day ceiling). What to open: `https://web.archive.org/web/20241106133254/https://electionresults.sos.ca.gov/returns/status`
  (547,742 frozen across 3 captures, ~6:32 AM to ~5:18 PM Nov 6, then the
  next capture jumps to the exact 611,101 figure the row used to cite).
  This is the cleanest of the three SoS-replacement cases: the two sources
  are adjacent points on the same timeline, not competing claims. What
  counts as a fail: none expected here; included for completeness since the
  row's classification changed from excluded to included in the comparable
  set.
- What happens on failure (either): revert the specific row's value/URL,
  update the note to document both states, rerun the verify_en_* + build
  pipeline, recompute the headline.

---

### B2. San Diego 2024-03-05: vs_asv is tagged "post" but the underlying tech record admits it cannot pin March vs November 2024

**Consequence if reversed:** moderate. San Diego is a treated county; this
only affects one row's ASV tag, not the ballot count itself (already
landed, CONFIRMED, triple-legged plateau evidence).

- What to open: `data/research/election-night/san-diego-ca.json`
  (2024-03-05 row, landed) and `data/research/county-tech/san-diego-ca.json`
  (the `asv` entry).
- Claimed / decisive quote (already in the landed row's note):
  "data/research/county-tech/san-diego-ca.json's ASV record (adopted_year
  2024, confidence secondary) states VERBATIM: 'Could not pin first
  election to March 2024 primary vs Nov 2024 general from primary
  sources.' Recorded here as vs_asv='post' per the coarse adopted_year=2024
  rule ... but the ambiguity is UNRESOLVED."
- What counts as a fail: the maintainer finds (or decides there is no way
  to find) a precise ASV go-live date; if it turns out ASV went live only
  for the November 2024 general, this row's `vs_asv` should read `pre`
  instead of `post`.
- What happens on failure: flip `vs_asv` to `pre` (or leave `post` if
  confirmed correct) in `data/research/election-night/san-diego-ca.json`'s
  2024-03-05 row, update the note to remove the unresolved-ambiguity
  language, rerun the verify_en_* + build pipeline, recompute San Diego's
  per-county effect.

---

### B3. Del Norte primaries 2018-06-05: a ~2x mislabel disambiguation (4,637 people vs. 9,284 ballot cards) needs an eyeball

**Consequence if reversed:** moderate. If the wrong figure were used this
would be a 2x error in one control-county primary row. NOT YET LANDED.

- What to open: `https://drive.google.com/drive/folders/1j_tx1oilfY7jlehwAx8Njwa7WH21-_CQ`
  (Release 4 of 6, the county's own numbered election-night PDF series).
- Claimed / decisive quote: Release 4's front page reads "Registered
  Voters: 4,637 of 14,151 (32.77%) / Ballots Cast: 9,284." This is Del
  Norte's known Runbook-7.5 mislabel pattern (already documented for this
  county's own 2016-general row): "Registered Voters" on the front page is
  actually turnout, and "Ballots Cast" is the ballot-CARD count (roughly 2
  cards per voter for a many-contest statewide primary). Disambiguated via
  the per-contest GOVERNOR "Times Cast" row on page 2, which reads
  "Total 4,637 / 14,151 32.77%," an exact match to the front page's
  Registered Voters field. **4,637 is the people-count used as the
  numerator; 9,284 is not.**
- What counts as a fail: a human reading the same PDF page disagrees that
  4,637 (not 9,284) is the correct people-count, or finds the per-contest
  cross-check does not match as claimed.
- What happens on failure: correct the row before it lands in
  `data/research/election-night/del-norte-ca.json`; if already landed by
  the time this is checked, correct the value and rerun the pipeline.

---

### B4. Napa primaries: two above-band spot checks plus one editorial POST classification call

**Consequence if reversed:** moderate. Napa is a treated county; all 6
primary rows are drafted CONFIRMED but not yet landed.

- **2012-06-05 (65.34%) and 2014-06-03 (61.86%) run above Napa's own
  November-general band** (pre-era generals run roughly 54-57%). The
  scout's explanation: June-primary VBM was only ~61% processed by election
  night in 2012 (16,357 of the eventual certified 26,689), unlike a
  November general where VBM release is typically near-complete by
  election night; this is a real cross-election-type effect, not a data
  error, per the scout. What to open:
  `https://web.archive.org/web/20120608220101/http://www.countyofnapa.org/ElectionResults/20120605/20120605-1052PM_dtl.htm`
  (claimed Total 19,147 / 28.02%) and
  `https://web.archive.org/web/20140725071031/http://www.countyofnapa.org/ElectionResults/20140603/20140603-2330_dtl.htm`
  (claimed Total 17,431 / 24.47%).
- **2018-06-05 classification.** The dossier classes this rollout election
  itself as `vs_epollbook: "post"` (Napa's own `first_election: "2018-06"`
  in the county-tech record), following the same convention already used
  for the county's November series (2018-11 is POST). This means the PRE
  sample for Napa's primaries is only 2012/2014/2016, with no gap year
  before the first POST primary. This is an editorial convention call, not
  a fact question; flagged by the scout explicitly for maintainer sign-off
  before landing.
- What counts as a fail: the maintainer wants the rollout election itself
  classed `pre` instead (matching a "the rollout election is a mixed
  transition state, exclude or hold as pre" convention some datasets use),
  or the two above-band spot checks reveal a transcription error rather
  than a structural VBM-timing effect.
- What happens on failure: adjust the relevant row(s) in
  `data/research/election-night/napa-ca.json` before or after landing,
  rerun the pipeline, recompute the headline (a 2018-06 reclassification
  would move Napa's own pre/post split and the pooled 2018-cohort primary
  numbers).

---

### B5. Mendocino primaries: three more PLAUSIBLE rows (2014-06 subtraction-derived, 2022-06 and 2024-03 news-sourced), all pending integration

**Consequence if reversed:** moderate each; same control-baseline mechanism
as item A5, lower priority since these three are not calibration-flagged as
outliers the way 2018-06 is.

- **2014-06-03 (57.86%): subtraction-derived numerator.** What to open:
  `https://theava.com/archives/32161` (AVA, official Assessor-Clerk-Recorder
  press release republished verbatim). Claimed: "Mendocino County has 6,721
  Vote By Mail ballots to process, and 201 Provisional ballots to review and
  process" (6,922 total outstanding, exact official figures). Numerator
  derived by subtraction from certified final: 16,420 - 6,922 = 9,498;
  9,498 / 16,420 = 57.86%. What counts as a fail: the maintainer judges a
  subtraction-derived numerator (certified minus officially-stated
  outstanding) is not an acceptable construction under Runbook 5.1/5.2,
  since it is a new pattern not used elsewhere in this county's dossier.
- **2022-06-07 (17.37%): two-source news corroboration, no document
  capture.** What to open:
  `https://mendovoice.com/2022/06/mendocino-county-election-officials-still-processing-ballots-in-primary-election/`
  (live URL). Claimed, attributed to county clerk Katrina Bartolomie:
  "Unofficial election results showed 3,864 registered voters' ballots were
  counted as of early morning Wednesday, June 8." 3,864 / 22,248 = 17.37%.
  Structurally low because by 2022 VBM was 98.1% of the certified total and
  most ballots had not yet arrived by election night (a VCA/universal-mail
  confound, not a sourcing error, per the scout). What counts as a fail:
  the maintainer wants independent document-level confirmation before
  accepting a news-cited official quote as the numerator.
- **2024-03-05 (30.99%): two-source news corroboration.** What to open:
  `https://mendovoice.com/2024/03/did-you-vote-yet-mendocino-county-and-california-primary-election-ends-today-with-results-beginning-tonight/`
  (live URL). Claimed: "the current results include a total of 7,418
  ballots, just over 14% of the county's 52,602 registered voters," framed
  as the state reached "after midnight on election night." 7,418 / 23,935 =
  30.99%. What counts as a fail: same as above, no document-level capture
  exists to fall back on.
- What happens on failure (any of the three): record the specific row null
  instead of landing the estimate, or land with the caveat more strongly
  worded in the note; rerun the pipeline once landed either way.

---

### B6. Lake 2018 PLAUSIBLE downgrade and Lake 2024's uncorroborated companion citation (carried forward from v1, unresolved)

**Consequence if reversed:** moderate. Lake is a control county (its
control status itself was CONFIRMED by the maintainer on 2026-07-10, see
Resolved section); this item is about the reliability of two of its
individual year values, not its control classification.

- **2018 row.** File: `data/research/election-night/lake-ca.json` (2018
  row, already downgraded from CONFIRMED to PLAUSIBLE on integration
  review) and `data/research/election-night/PLATEAU_REVIEW.md`. Claimed:
  13,522 / 21,465 = 63.00%. What to open:
  `https://web.archive.org/web/20181129033058/http://publicapps.lakecountyca.gov/elections/results/result37.htm`
  (this URL's only-ever Wayback capture, confirmed no second capture exists
  anywhere). The judgment call: this verdict is held at PLAUSIBLE, not
  CONFIRMED, because the "held unchanged" argument compares the page's own
  embedded timestamp to its own single crawl date, not two independent
  Wayback observations over time (unlike this county's 2012/2014/2016
  rows, each with two genuine captures).
- **2024 row companion-citation gap.** Same file, 2024 row. Claimed: 7,960
  / 27,127 = 29.34%, primary source machine-verified. The judgment call:
  this row's confirmation also leans on a second supporting article,
  `lakeconews.com/news/80080`, which has no surviving Wayback capture and
  is cited only via a WebSearch-indexed snippet, never a full page read.
  What to open (to try to resolve, not a guaranteed fix):
  `https://lakeconews.com/news/80080` live, or search Wayback CDX for any
  surviving capture.
- What counts as a fail: a second capture of the 2018 URL surfaces with a
  different total, or `news/80080` is located and contradicts the "issued
  by 4 a.m. Wednesday" timing framing the 2024 row's corroboration relies
  on.
- What happens on failure: correct the row and its `PLATEAU_REVIEW.md`
  entry, rerun the pipeline, recompute Lake's control-side contribution and
  the headline.

---

### B7. Sacramento and Fresno primary ceilings: four cells recorded as documented ceilings, `comparable: false`

**Consequence if reversed:** low for the headline (ceilings are excluded
from the comparable set by design), moderate for completeness: these are
the same category as the already-resolved Placer-2018/Santa-Clara-2012-06
precedent (item C, Resolved section), so the default treatment is already
established, but each is a distinct county-year worth a quick eyeball
before landing since none is yet in the repo.

- **sacramento-ca, 2014-06-03**: 140,521 / 203,850 = 68.93% (ceiling; the
  only surviving capture is 3 days post-election, "SEMIOFFICIAL," Run Date
  06/06/14). What to open:
  `https://web.archive.org/web/20140610002504/http://eresults.saccounty.net/`
  (or the specific report path cited in the dossier).
- **sacramento-ca, 2016-06-07**: 230,234 / 340,360 = 67.64% (ceiling,
  proven still-moving: the next surviving capture, 10 days post-election,
  shows 297,409, a 29% jump). What to open:
  `https://web.archive.org/web/20160611133801/http://eresults.saccounty.net/`.
- **fresno-ca, 2018-06-05**: 112,403 / 136,388 = 82.41% (ceiling; earliest
  surviving capture is 3 days post-election, "Unofficial Final Results,"
  internally timestamped 06/08/18). What to open:
  `https://web.archive.org/web/20180610030903/http://www.co.fresno.ca.us/departments/county-clerk-registrar-of-voters/election-information/election-results/results-for-june-5-2018-statewide-primary-election`.
- **fresno-ca, 2024-03-05**: 143,879 / 156,425 = 91.98% (a loose ceiling,
  sourced from a live-edited news page's current text, "Updated March 12,
  2024," 7 days post-election). What to open:
  `https://fresnoland.org/2024/03/05/fresno-county-live-election-results-march-2024-primary/`
  (live URL; note the article was edited in place after publication, so the
  text you see now is the same text the scout cited).
- What counts as a fail: any of the four pages does not show the cited
  figure, or a human finds an earlier capture/report the scout missed that
  would upgrade a ceiling to a true plateau.
- What happens on failure: if a true plateau is found, replace the ceiling
  row with it and set `comparable: true`. If not, land as documented
  ceilings (no pipeline-breaking change; ceilings are excluded from
  comparable computations by construction).

---

## TIER C: documentation-only, credential-bound, or zero current consequence

### C1. LA County: `stage.lavote.gov` is a dead staging host, do not follow it

**Consequence:** none numerically, this is a practical note for whoever
next re-verifies LA's primary rows (not yet landed).

- What to open: `https://www.lavote.gov/docs/rrcc/news-releases/03062024_PR-13-03052024-Semi-Final-Results.pdf`
  (the working public host; the same filename on `stage.lavote.gov`, which
  LA's own news-room page links to, returns a dead staging URL).
- Claimed: "A total of 910,857 ballots were processed and counted, with
  16.03% of registered voters casting ballots" (March 6, 2024 release);
  confirmed against the "First Post-Election Night Ballot Count Update"
  release the next day, which states the canvass added exactly 105,717
  ballots on top of 910,857 to reach 1,016,574.
- What counts as a fail: `www.lavote.gov` also 404s on this filename (try
  the CMS's current news-release index instead).
- What happens on failure: none pipeline-side; just note the working host
  in the row when it lands.

---

### C2. Credential-bound: 3 items need the maintainer's SFPL/NewsBank login

**Consequence:** low to moderate. Two are optional upgrades to existing
ceiling/null rows; one (santa-clara-ca 2012-06) already has a landed
maintainer-approved default, so its NewsBank lead is now genuinely
optional, not blocking anything.

1. **sacramento-ca.json, 2016-11-08 general.** Currently landed as null
   (`election_night_ballots: null`). All non-credential routes exhausted
   (sacbee.com live 403s; Wayback CDX for the section path returns zero
   captures for the relevant window). Lead: a NewsBank/ProQuest pull of
   Sacramento Bee coverage for Nov 8-9, 2016 could recover a plateau.
2. **Sacramento primaries, 2014-06-03** (`scratchpad/dossier-sacramento-ca-primaries.md`
   item 2). Currently a documented ceiling per item B7. Same NewsBank
   route, same county, different election. Wayback never crawled the
   relevant section for this week at all (confirmed by CDX prefix sweep).
3. **Santa Clara primaries, 2012-06-05** (San Jose Mercury News via
   SFPL/NewsBank). This lead is now LOW priority: the row already has a
   maintainer-approved landed default (the 234,342/80.06% ceiling,
   freeze-tested and confirmed not a frozen state; see Resolved section
   item C below). A NewsBank recovery could only upgrade this from a
   ceiling to a true plateau, it would not correct an error.
- What to open: none of these can be opened without the maintainer's own
  SFPL ezproxy session; use the `newsbank-election-recovery` skill's
  isolated-Chrome recipe when ready.
- What happens on success: land a new value in the relevant row (sacramento
  2016-11 goes from null to a real figure; the two ceilings could upgrade
  to true plateaus), then rerun the pipeline.

---

### C3. Imperial County's ASV-adopter call (carried forward from v1, still zero current consequence)

**Consequence:** none for the current panel or the headline. Imperial is
not in `county_night_4ctrl.json`'s 17-jurisdiction panel at all. This item
matters only for a future control-pool or treated-pool expansion.

- File: `data/research/county-tech/ca_adoption_census.json`, the
  imperial-ca row (`asv`, `status: "adopted"`, `adopted_year: 2024`,
  `confidence: "medium"`), unchanged since v1.
- Claimed: a single ivpressonline.com quote attributed to the Registrar:
  "The machines not only count but help verify signatures of the mail-in
  voters." Direct fetch was bot-blocked (429 rate-limited on repeated
  tries); this rests on search-indexed text only.
- What to open: `https://www.ivpressonline.com/featured/registrar-of-voters-gives-november-election-overview-for-imperial-county/article_539a5084-7798-11ef-8d2c-5bb6a2acbdbc.html`
  (retry with a real browser to bypass the rate limit).
- What counts as a fail: a human reads the quote as loose reporter phrasing
  for a ballot-imaging sorter rather than an actual signature-comparison
  step.
- What happens on failure: update the census row's `status` to
  `not-adopted`, drop `adopted_year`; no pipeline rerun needed now, note it
  for whoever next runs a control-selection pass.

---

## Resolved (v1 items closed by maintainer verdict or by inspection; v2 supersedes these)

All dated 2026-07-10 per `.superpowers/sdd/progress.md` unless noted.

- **Lake County ASV "never adopted" call (v1 item 1).** RESOLVED. Maintainer
  reviewed the CalVoter evidence and confirmed Lake did not adopt ASV;
  control classification stands. Landed:
  `data/research/county-tech/lake-ca.json`'s `asv` entry now carries the
  dated confirmation in its note.
- **Mendocino 2012 null-vs-estimate call (v1 item 2).** RESOLVED, RESTORED
  AS APPROXIMATION. Maintainer overrode the earlier integration-review null
  and restored 18,401 / 36,080 = 51.00% as a labeled secondary/PLAUSIBLE
  approximation. Landed in `data/research/election-night/mendocino-ca.json`'s
  2012-11-06 row, with both the original null rationale and the maintainer
  override preserved in the note.
- **Mendocino 2014 and 2024 generals.** RESOLVED, hand-confirmed. Landed
  values 11,402/25,017 (2014) and 15,611/39,837 (2024), both carry a dated
  "HUMAN VERIFICATION (maintainer, 2026-07-10)" line in their notes.
- **Placer 2018-11-06: is the cited artifact a true election-night state or
  a later report?** RESOLVED. A dedicated retry scout
  (`scratchpad/placer-2018-general-retry.md`) confirmed the maintainer's
  concern was worth chasing but found no earlier capture exists anywhere:
  the maintainer's lead (`.../11062018_Results.pdf`) resolves to the
  certified-final canvass PDF, and the true in-place-overwritten live page's
  earliest ever Wayback capture is already Nov 13 (7 days post-election),
  identical to the value already landed. The `comparable: false` ceiling
  (113,380/177,725 = 63.8%) stands as the best obtainable; no better source
  exists.
- **Santa Clara 2012-06-05: freeze-test the "Semi-Final" state.** RESOLVED,
  CEILING DEFAULT APPLIED. A dedicated retry (`scratchpad/santa-clara-2012-06-retry.md`)
  ran the runbook's freeze test and it decisively FAILED (the 234,342 figure
  grew by 14.5% in the very next capture and kept climbing to the certified
  final). Per DEADLINE MODE (user directive, 2026-07-10: "SC 2012-06
  defaults to ceiling+scaling-note"), the ceiling stands as the landed
  default. Landed in `data/research/election-night/santa-clara-ca.json`'s
  2012-06-05 row, note explicitly reads "MAINTAINER DEFAULT is the
  234,342/80.06% ceiling (comparable:false) pending final say."
- **Napa 2014 general "CORRECT" verdict.** SUPERSEDED, not simply resolved.
  See Tier A2 above: the maintainer's verification predates a later SoS-
  driven value replacement that changed the landed number under that
  verdict. Reopened as item A2, ranked at the top of this packet.
- **Nevada 2024 flag text edit (v1 item 6).** RESOLVED by inspection.
  Landed `data/research/election-night/nevada-ca.json`'s 2024-11-05 `flag`
  field retired only the first-vs-last-report ambiguity caveat (now marked
  "This caveat is STALE... resolved") and left the ink-overspray
  `comparable: false` exclusion rationale untouched, exactly as claimed.
- **Santa Clara primaries: Wayback evidence-permanence gap for 5 Clarity
  numerator URLs.** RESOLVED (archival only, no data change). The browser
  recovery sweep successfully ran `web.archive.org/save/` on all 5 URLs
  (2014/2016/2018/2022/2024 primaries) and CDX-confirmed each snapshot;
  one payload was spot-verified byte-for-byte against the dossier's claimed
  value. This closes the permanence flag; the values themselves were
  already correct. Still pending: these 5 rows are not yet landed in
  `data/research/election-night/santa-clara-ca.json` (only 2012-06-05 is
  landed so far), so when they do land, use the archived snapshot URLs, not
  the live Clarity CDN URLs.

---

## Summary table

| # | Item | Tier | Landed? | Consequence |
|---|---|---|---|---|
| A1 | Nevada tech-adjudication (ASV 2016, EPB split 2014) | A | No | Highest: treatment-window reclassification |
| A2 | Napa 2014-11 supersedes a verified value | A | Yes (superseding) | High: process integrity + PRE-window value |
| A3 | Santa Clara 2016-11 10:28am Wed plateau (carried from v1) | A | Yes | High: large per-county effect |
| A4 | Placer 2024-03 new recovery, contrarian direction | A | No | High: fills only post-adoption primary cell |
| A5 | Mendocino 2018-06 primary outlier (83.20%) | A | No | High: control-baseline row |
| A6 | Del Norte image-PDF visual reads (carried from v1 + primaries) | A | Partial | Moderate-high: 5+ control rows |
| B1 | Del Norte 2016-11 + Riverside 2024-11 SoS replacements | B | Yes | Moderate |
| B2 | San Diego 2024-03 vs_asv ambiguity | B | Yes | Moderate |
| B3 | Del Norte 2018-06 primary mislabel (2x risk) | B | No | Moderate |
| B4 | Napa primaries: above-band + 2018-06 POST call | B | No | Moderate |
| B5 | Mendocino primaries: 3 more PLAUSIBLE rows | B | No | Moderate |
| B6 | Lake 2018 PLAUSIBLE + 2024 companion gap (carried from v1) | B | Yes | Moderate |
| B7 | Sacramento/Fresno primary ceilings (4 cells) | B | No | Low-moderate |
| C1 | LA stage.lavote.gov dead host | C | No | None (documentation) |
| C2 | Credential-bound NewsBank/SFPL items (3) | C | Mixed | Low-moderate |
| C3 | Imperial ASV call (carried from v1) | C | N/A | None currently |

16 open items (23 underlying rows/cells when Del Norte's PDFs, Napa's 3
sub-items, Mendocino's 3 primary rows, and the 3 credential-bound items are
counted individually), plus 8 resolved v1 items closing out this packet's
predecessor.
