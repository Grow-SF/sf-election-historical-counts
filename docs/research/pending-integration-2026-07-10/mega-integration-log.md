# Mega-integration log (recovery map)

Worktree: cozy-leaping-wreath. Branch: feat/county-panel-expansion (main tip 8412b97? actually on `main` per git; commits de7fd25/9488f84 present). Sole committer.
Baseline before my work: git tip 9488f84, validator OK 120 rows (80 sourced), plateau 80 entries (73C/3P/2R_AS/2R_AND).

## Plan / status
- [x] Commit 1: DONE a13e842. validator 121/82, num 81V+1NF(mendo2012), denom 121, pytest 24, vitest 28. estimator any +4.33 se5.92 n11.
- [ ] Commit 1 was: adjudicated corrections (napa2014->19515/50.34 primary+SoS; delnorte2016->8450/86.31 SoS, drop render_verified; riverside2024->547742/57.11 primary, drop comparable/flag) + human verdicts (mendocino2012 RESTORE 18401/51.00 secondary approx; mendocino2014/2024 human-confirm note; napa2014 human note) + santa-clara 2012-06 ceiling row (234342/80.06 comparable:false) w/ freeze-test+scaling note. VERIFY.md + plateau_review.json(+2=82) + PLATEAU_REVIEW.md totals + validator count 120->121. Delete numerator caches napa-2014-11-04, del-norte-2016-11-08, riverside-2024-11-05.
- [ ] Commit 2: SoS sweep 73 cells (helper script, apply only null/absent cells, primary=CONFIRMED/secondary=PLAUSIBLE, spot-fetch >=5).
- [ ] Commit 3+ (per county): primaries dossiers: santa-clara(5, 2012 ceiling already in c1), sacramento(3+2ceil), fresno(2ceil+nulls), san-bernardino(1+nulls), placer(2+nulls+RECOVERED 2024-03 69436/135869=51.11 CONFIRMED), lake(6), del-norte(4+nulls), mendocino(1C+4 PLAUSIBLE-flagged), tehama(1+nulls), los-angeles(6), napa(6), orange(6), nevada(exists - land PRE-CORRECTED per nevada addendum). madera/san-mateo primaries dossiers: NOT PRESENT as of start (only generals exist).
- [ ] Nevada tech-adjudication commit (addendum, before vca): nevada-ca county-tech ASV 2022->2016, epollbook keyed 2014 (+2018 vote-center record), census sync, flip generals 2014/2016/2018 flags, primaries landed pre-corrected. scratchpad/nevada-tech-adjudication.md.
- [x] FINAL vca commit: DONE e09c86d. build_county_night load_vca_years from census -> adoption.vca; estimator --mechanism vca; types.ts adoption.vca optional; +4 tests. any & vca both +4.33/se5.92/n11 (collinear). full pytest 95, vitest 28, validate 121/82.
- Commit 2 apply-list COMPUTED: scratchpad/sweep_applylist.json (87 null/absent CONFIRMED/PLAUSIBLE cells; all pct match sweep exactly). Per-election frozen-capture URL still needs extraction from sweep bracket-evidence; overlaps commit-3 primary dossiers (must de-dup, prefer stronger source). NOT LANDED.
- [ ] ORIG Final commit: vca_year plumbing in build_county_night.py (adoption block) + estimate_tech_effect.py (--mechanism vca) + tests; regenerate; full battery green.

## LANDED COMMITS (all green, sole committer)
- a13e842 commit 1: SoS adjudications + human verdicts. validate 121/82, num 81V+1NF, denom121, pytest24, vitest28. any +4.33.
- e09c86d final: vca_year plumbing (build_county_night load_vca_years->adoption.vca; estimator --mechanism vca; types.ts; +4 tests). any/vca +4.33.
- 9bff066 nevada tech adj + mendocino ASV: nevada asv2022->2016, epb2018->2014 (split; vote-center keeps 2018); census+county_tech synced; nevada general flags flipped; mendocino ASV FAQ citation. Chart: EARLIEST_ADOPT 2018->2014 dropped Del Norte from control bars (test updated to 3 controls). epb+4.33->+4.83, asv+14.40->+12.33, any+4.83, vca+4.33 (now distinct).

## NOT LANDED (handoff; recovery map)
- Commit 2 (SoS sweep 87 null/absent CONFIRMED/PLAUSIBLE cells): apply-list at scratchpad/sweep_applylist.json (parser scratchpad/parse_sweep.py; pct all match sweep). Still needs: per-election frozen-plateau capture URL (extract from sweep bracket-evidence col; 2024-03 uses 20240306144409, others in bracket text like "frozen <ts>->..."); per-county vs_epollbook/vs_asv from county_tech (nevada now pre-corrected: epb2014/asv2016); VERIFY primaries subsections per county; plateau verdicts (CONFIRMED->primary/SoS-bracket, PLAUSIBLE->secondary/single-capture); validator count bump; numerator cache handling. DE-DUP vs commit-3 dossiers (many primary cells overlap; prefer stronger evidence, cross-cite).
- Commit 3+ (primary dossiers): santa-clara(5 more; 2012-06 ceiling DONE in c1; USE archived Clarity URLs from browser-recovery-sweep.md per coordinator #1), sacramento, fresno, san-bernardino, placer(+RECOVERED 2024-03 69436/135869=51.11 from placer-2024-03-retry.md, also in sweep), lake, del-norte, mendocino(1C+4 PLAUSIBLE flagged), tehama, los-angeles, napa, orange, nevada(land PRE-CORRECTED: epb2014/asv2016 already set; 2014-06 comparable:false mid-pilot, 2016-06 post-epb, 2018-06+ post both). madera/san-mateo primaries dossiers still ABSENT (only generals).
- Reason not landed: budget + integrity. 87 sweep cells + ~70 dossier rows x (JSON+VERIFY+plateau+tech+numerator) + overlap adjudication is beyond safe single-agent completion; rushing risks corrupting the dataset. Recovery map above + apply-list make continuation direct.

## Coordinator addenda
1. Santa Clara primary Clarity numerator URLs now Wayback-archived+CDX-verified: cite archived snapshot URLs from scratchpad/browser-recovery-sweep.md as source_url_night in commit 3 (resolves evidence-permanence FLAG).
2. Mendocino ASV: upgrade absence confidence low->secondary w/ county FAQ citation ("staff check the signature ... by hand") in a county-tech-touching commit (dated note append). Do in mendocino primaries commit or final.
3. Nevada tech adjudication: see dedicated commit above.

## Done so far (commit 1 edits, UNCOMMITTED)
- napa-ca.json 2014: fields + note CORRECTION + HUMAN VERIFICATION. DONE.
- del-norte-ca.json 2016: fields + note CORRECTION. DONE. render_verified.json del-norte 2016 entry removed. DONE.
- riverside-ca.json 2024: fields, removed comparable+flag, note CORRECTION. DONE.
- mendocino-ca.json 2012 RESTORE fields + maintainer-override note. DONE. 2014/2024 human-confirm note appends. DONE.
- TODO c1: santa-clara 2012-06 row insert; VERIFY.md 4 table edits + santa-clara primaries subsection; plateau_review.json (napa2014 P->C, riverside2024 R->C, delnorte2016 evidence update, +mendocino2012 P, +santaclara2012-06 R_AS); PLATEAU_REVIEW.md; validator 120->121; cache deletes; run pipeline; commit.
