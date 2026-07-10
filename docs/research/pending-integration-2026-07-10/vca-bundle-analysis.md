# VCA vote-center bundle hypothesis: does the current panel identify it?

Pinned inputs (commit `06cf215`, copied read-only into this scratchpad, never touching the live worktree):
- `cn_vca.json` = `packages/data/county_night.json`
- `est_pinned.py` = `scripts/research/estimate_tech_effect.py`
- `census_vca.json` = `data/research/county-tech/ca_adoption_census.json`

All code below imports `est_pinned.py` as a module (`pinned_import/estimate_tech_effect.py`, a straight copy) rather than editing or shadowing the live file the other session is working on. Runner script: `vca_run.py` in this same directory.

## 1. Classification table

19 panel jurisdictions in `cn_vca.json`: 6 nominal controls (San Francisco, Colusa, Del Norte, Lake, Mendocino, Tehama) and 13 treated. Joined against `census_vca.json` (58 CA counties) by slug for `vca_year`/`status`.

**Controls.** All 6 have `census_status = "never"` and `vca_year = null` (clean, as expected). Colusa additionally has zero usable `pct` rows in `county_night.json`, every point is `pct: null`, so it contributes no data to any estimate below despite being nominally a control; effective control n = 5, not 6.

**Treated (one line each).** `epb_year` = e-pollbook adoption year in the panel, `vca_year` = Voter's Choice Act vote-center launch year from the census, usable = years with non-null, `comparable:true` `pct`:

| county | epb_year | asv_year | vca_year | class | usable years |
|---|---|---|---|---|---|
| fresno-ca | 2020 | 2020 | 2020 | VCA-bundled (EPB+ASV both arrived with vote-center launch, Mar 2020 primary) | 2016, 2024 |
| los-angeles-ca | 2020 | 2020 | 2020 | VCA-bundled (VSAP vote centers, Mar 2020) | all 6 |
| madera-ca | 2018 | none | 2018 | VCA-bundled (one of the 5 original 2018 VCA pilots) | 2016,2018,2022,2024 |
| napa-ca | 2018 | none | 2018 | VCA-bundled (2018 pilot) | all 6 |
| nevada-ca | 2018 | 2022 | 2018 | VCA-bundled at EPB, ASV added 4 yrs later (separate later treatment) | 2012,2014,2016,2018,2022 |
| orange-ca | 2020 | none | 2020 | VCA-bundled (Mar 2020) | all 6 |
| placer-ca | 2024 | none | 2024 | VCA-bundled (Mar 2024) | 2014, 2016 only |
| riverside-ca | 2022 | 2025 | 2022 | VCA-bundled at EPB, ASV added 3 yrs later | 2022 only |
| sacramento-ca | 2018 | none | 2018 | VCA-bundled (2018 pilot, largest) | 2012,2014,2018,2022,2024 |
| san-bernardino-ca | 2020 | 2025 | **null** | **standalone-EPB**: traditional precinct polling places, explicitly "NOT a VCA county" per census note; EPB (KNOWiNK) arrived alone in Mar 2020, ASV added separately in 2025 | 2024 only |
| san-diego-ca | 2022 | 2024 | 2022 | VCA-bundled at EPB, ASV added 2 yrs later | 2018,2022,2024 |
| san-mateo-ca | 2018 | none | 2018 | VCA-bundled (2018 pilot) | all 6 |
| santa-clara-ca | 2020 | none | 2020 | VCA-bundled (Mar 2020) | all 6 |

**Key structural finding:** across the full 58-county census file, `epb_year == vca_year` in 28 of 29 counties with a non-null `vca_year`; the one statewide exception is Humboldt (EPB 2016, VCA 2024, not in this panel). Inside the 19-county panel, **12 of 13 treated counties are VCA-bundled by construction**: their `epb_year` field already *is* the vote-center launch year, because whoever populated `county_night.json`'s adoption field used the VCA date as the e-pollbook date for these counties (they didn't have EPBs before the vote-center switch). San Bernardino is the panel's only clean standalone-EPB case (polling-place county, EPB with no vote centers). ASV-only-relevant treatment (ASV arriving detectably later than EPB/VCA) shows up as a secondary event in Nevada, Riverside, San Diego, and San Bernardino.

## 2. Treatment = VCA bundle

Patch: for each treated county, replace the row's `epb_year` field with its `vca_year` before calling the pinned `estimate()`/`jackknife()` (mechanism="epb" so `_adoption_year` reads the patched field); San Bernardino's `epb_year` becomes `None` and it drops out of the treated set per the estimator's own `if a is None: continue` guard, i.e. dropped automatically, not hand-removed.

```
=== BASELINE headline: mechanism=epb (as shipped, unpatched) ===
effect=4.764  se=7.184  n_treated=10  n_controls=5

=== VCA BUNDLE: treatment = vca_year, null-vca treated dropped ===
effect=4.764  se=7.184  n_treated=10  n_controls=5
ci95=(-9.32, 18.84)  mde=20.12
```

**These two runs are numerically identical.** That is not a bug, it is the direct consequence of finding 1: the panel's "epb" mechanism and the "VCA bundle" mechanism already select the same treated counties with the same adoption years, because San Bernardino (the one county where they'd diverge) was *already* excluded from the headline "epb" estimate for an unrelated reason: it has only one usable data point (2024), so it has no pre-adoption years, and the estimator drops it regardless of which adoption-year field is used (see finding under §3). So: **this panel cannot currently distinguish "EPB-driven" from "VCA-bundle-driven" as a matter of estimation**, not because the hypotheses are equivalent, but because the one available discriminating case has no usable pre-period data. The reported effect (+4.76, se 7.18, n=10) should be read as an estimate of the VCA bundle's effect (since that's what 12 of 13 treated counties actually are), not narrowly an EPB effect, but the data as currently populated cannot tell the two apart.

## 3. Bundle vs standalone contrast

- Bundle subset (n=12 nominal, VCA-bundled): fresno, los-angeles, madera, napa, nevada, orange, placer, riverside, sacramento, san-diego, san-mateo, santa-clara. Controls shared with baseline (5 usable controls: del-norte, lake, mendocino, san-francisco, tehama).
- Standalone-EPB subset (n=1 nominal): san-bernardino-ca only.

```
=== BUNDLE subset (n_treated=10 usable of 12 nominal) ===
effect=4.764  se=7.172  ci95=(-9.29, 18.82)  mde=20.08  n_controls=5
placer-ca and riverside-ca drop out: placer has pre-adoption data (2014,2016)
but zero post-adoption data (2022,2024 both null); riverside has one
post-adoption point (2022) but zero pre-adoption data, so neither can form
a pre/post pair, and the estimator silently excludes both.

=== STANDALONE-EPB subset (n_treated=0 of 1 nominal) ===
effect=None  (undefined: no jackknife SE, no CI)
San Bernardino has exactly one usable county_night point in the whole panel
(2024, pct=56.24); every pre-2020 year is null. With zero pre-adoption
years the estimator's per-county-effect guard (`if not pre_years or not
post_years: continue`) drops it. n=0, not "small": literally unidentified.
```

**Honest read: the bundle-vs-standalone contrast is not currently testable.** The bundle side has a real (if wide) estimate; the standalone side has *no* estimate at all, because the panel's only standalone-EPB county lacks any pre-adoption election-night data point. This is not a power problem that a jackknife CI can express, it is a missing-data problem: `county_night.json` needs at least one pre-2020 San Bernardino point (2012 to 2018) before this cell can produce a number of any kind.

## 4. Two-channel decomposition, first pass

**(a) Treated-county night-share change alongside VCA status and VBM share.** No panel treated county's `census_vca.json` note captured a numeric 2024 VBM/mail share; grepped all 58 notes for VBM/mail-share language, and the only hits (Lassen, Modoc, Santa Cruz, Siskiyou, Sutter, Ventura, Yolo) are counties outside this 19-county panel. So there is no ready-made per-county VBM-share covariate to tabulate against the per-county effects in §2/§3 without new collection.

**(b) The algebra of the two-channel identification problem.**

Election-night share `S` (ballots counted by the last night report, divided by the certified final) is a weighted average of two very different processing rates:

```
S = m * S_mail + (1 - m) * S_precinct
```

where `m` = mail (VBM) share of total ballots cast, `S_mail` = fraction of mail ballots resolved by election night (signature-verify, extract, tabulate: the ASV-relevant step), `S_precinct` = fraction of precinct/vote-center ballots resolved by election night (near 100% historically, since those are same-day scanned).

A VCA county's transition changes *both* right-hand terms at once:
1. `m` rises mechanically: VCA counties mail every registered voter a ballot, so the mix shifts toward mail even before any processing-speed change.
2. `S_mail` may rise (ASV/faster signature-verification throughput) or fall (more late-arriving/curable mail ballots now dominate the denominator); direction is genuinely ambiguous a priori.
3. `S_precinct` is largely mechanical and roughly time-invariant, but if vote centers replace precincts, drop-box/vote-center same-day mail deposits shift more ballots into the mail-processing queue right before election night, which can *lower* apparent night-share even with zero technology change.

A single pre/post `pct` number cannot separate "m moved" from "S_mail moved" from "S_precinct moved": the DiD estimate in §2/§3 is a reduced-form estimate of the *net* effect of all three, which is exactly what "test the bundle, not just the pollbooks" means, but it also means a null or noisy result cannot distinguish "the bundle doesn't work" from "the bundle's components pull in offsetting directions." To identify `S_mail` and `m` separately requires, per county-year: (i) total ballots cast, (ii) mail ballots cast, (iii) mail ballots counted by the night-of report, (iv) precinct/vote-center ballots counted by the night-of report. Only (i) and (ii), equivalently `m`, are typically published in a Statement of Vote; (iii) and (iv) require the same night-of canvass report the panel already sources `pct` from, just broken out by ballot type instead of collapsed to one number. Most counties' night-of press releases do not break this out (SF's own do, per `packages/data/vbm_history.json` and `data/sources/sf_vbm_share_sos.csv`, but SF is a control county in this panel, not treated, so that data cannot identify the treated-county channel split without new collection at the treated counties).

**(c) Where mail/precinct splits already sit in cited artifacts (grep of `county_night.json` notes/source_urls).** Checked every point's `source_url` and note text in `cn_vca.json` for mail/VBM/precinct language:
- `nevada-ca` 2012 `source_url` is a Yubanet article titled "...Turnout Is Nearly 80%, Mail-Ins Top 16,000": an informal textual signal of high mail volume, not a structured split, and not machine-usable.
- `san-mateo-ca` (2012, 2014, 2016) and `tehama-ca` (2022) source URLs point to county "precinct report" / "precinct turnout report" PDFs; these are organized *by precinct*, which is the opposite axis from mail-vs-precinct ballot type, and would need to be re-read to check whether they also tabulate absentee/VBM totals (not confirmed here).
- No other panel county's night-report source in `cn_vca.json` names mail/VBM/absentee in its citation text.
- Searched `docs/research/` in the live repo (read-only) for a doc describing "the VCA-era composition shift" as referenced in the task brief: **not found**. The closest SF-specific artifacts are `packages/data/vbm_history.json` (1964-present VBM share %, SF only) and `data/sources/sf_vbm_share_sos.csv` (polling/absentee/total counts, SF only, sourced from CA SOS Statements of Vote); useful as a *template* for what a treated-county version should look like, but they do not cover any treated county in this panel.

**Bottom line for §4:** the panel as it stands has essentially zero treated-county mail/precinct split data already sitting in cited sources. A future sweep should not expect to mine this from existing citations; it needs a fresh SoV-driven collection pass (see §5).

## 5. Honest bottom line

**Does the panel support, refute, or fail to identify the bundle hypothesis?** It fails to identify it, in a specific and fixable way. The panel's structure happens to make "EPB" and "VCA bundle" the same treatment for 12 of 13 treated counties (finding in §1/§2), so there is no internal contrast between "pollbooks alone" and "the full vote-center bundle" among the well-populated counties: they're the same natural experiment. The one county that could supply that contrast, San Bernardino (standalone EPB, no vote centers), has only a single usable election-night data point in the whole panel and literally cannot produce an estimate (§3). So the current data neither supports nor refutes "it's the centers, not the pollbooks": it simply has no counties positioned to answer that specific question. What it *does* support, with wide uncertainty (se 7.18, CI roughly -9 to +19), is that the VCA bundle as a whole (12 counties, since it's indistinguishable from "epb" here) has a positive but not statistically distinguishable-from-zero point estimate on election-night share, unchanged from the headline EPB number precisely because they are the same estimate.

**Cheapest data to actually identify it**, in priority order:
1. **Fill San Bernardino's missing pre-2020 county_night points** (2012, 2014, 2016, 2018, currently all null). Source: San Bernardino ROV's own historical Statement of Vote / semi-final and certified canvass reports for those four elections (the county's `election-night-source-hunting` style research would find the night-of report vs. certified-final ratio the same way the other 18 counties were populated). This single fix turns the standalone-EPB cell from n=0/undefined into n=1 with an actual (if single-county) effect estimate; cheap because it is exactly the same style of lookup already done for every other panel county, just backfilling one county's gaps.
2. **Recruit 1-2 more standalone-EPB, non-VCA, polling-place counties into the panel as treated observations.** San Bernardino alone will always be n=1. Good statewide candidates (from the same `ca_adoption_census.json`, filtered `status=adopter` and `vca_year=null`) worth checking for panel-quality night-of data: needs a quick scan of the 29 counties. Kern and Kings would be natural candidates to check (large polling-place counties with EPB reported in the SoS voting-tech PDF), not yet verified against `ca_adoption_census.json`, flagging for the next sweep rather than asserting unverified.
3. **For the two-channel decomposition (§4b)**, the specific artifact class needed is the CA SoS **Statement of Vote, "Ballots Cast by Type"** or equivalent county Registrar semi-final/certified canvass summary that breaks total ballots into mail vs. precinct/vote-center for each treated county, for each panel election year (2012, 2014, 2016, 2018, 2022, 2024). These exist as PDFs on each county Registrar's site (the same class of "release N" / "semifinal" / "certified canvass" PDF that `dossier-*.md` files in this scratchpad already retrieved for several counties this session, e.g. the `sov/`, `raw2016/`, `raw2022/` subfolders here); the missing step is re-reading them for the mail/precinct line rather than only the top-line ballots-counted number. Cheapest first targets: San Mateo and Sacramento (2018 pilot counties, `complete: true` in the panel, so their canvass PDFs are already fully cited and just need a second read for the type breakdown).

File: `/private/tmp/claude-501/-Users-sbuss-workspace-sf-election-count/cbd9561c-405d-4e44-8f38-6a4a9bd48e60/scratchpad/vca-bundle-analysis.md`
Runner: `/private/tmp/claude-501/-Users-sbuss-workspace-sf-election-count/cbd9561c-405d-4e44-8f38-6a4a9bd48e60/scratchpad/vca_run.py`
