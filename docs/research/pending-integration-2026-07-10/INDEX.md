# Pending Research Integration Corpus (2026-07-10)

CRITICAL: These are verified-research working documents captured from July 9-10 2026 campaign activity. The authoritative data files live in `data/research/election-night/`. Nothing in this directory should be cited as final data. The `sweep_applylist.json` and `mega-integration-log.md` in this directory are the operational maps for landing the findings documented here into the dataset.

## Index

archive-probes-a-m.md: Web.Archive CDX index results for counties A-M (Waybakc availability scan).  Status: Pending integration into archive-availability reference.

archive-probes-m-y.md: Web.Archive CDX index results for counties M-Y (Wayback availability scan). Status: Pending integration into archive-availability reference.

browser-recovery-sweep.md: Results from hands-on browser recovery attempts using archived web pages; found URLs and partial counts. Status: Pending county-by-county integration.

dossier-colusa-ca.md: Colusa County research including web archive surveys and technology platform identification. Status: Pending integration.

dossier-del-norte-ca.md: Del Norte County general election research. Status: Pending integration.

dossier-del-norte-ca-primaries.md: Del Norte County primary election research. Status: Integrated 2026-07-10 (backfill batch 1): 2012/2014 dossier concluded null where the live dataset already had SoS-sweep values (nothing to land); 2016-06-07 and 2018-06-05 were absent from the live dataset entirely and are now landed as new CONFIRMED/primary rows (2018 carries a FLAG for manual operator re: the ballots-vs-cards mislabel resolution); 2022/2024 already CONFIRMED/primary with matching values, corroborated in place.

dossier-fresno-ca-primaries.md: Fresno County primary election research and archive availability assessment. Status: Integrated 2026-07-10 (backfill batch 2): 2012-06-05 was already landed via the SoS status-page sweep (CONFIRMED/primary, 66,323/113,975=58.19%) at the EXACT figure a separate NewsBank pass independently recovered (Fresno Bee, 2012-06-06, docref news/13F45F3B8CAE5680); cross-cited as strong corroboration (two unrelated routes, identical number). 2014-06-03 already landed (CONFIRMED/primary, 79,801/107,805=74.02%) where the dossier found null; NewsBank checked separately and found no clean count either; one-line note appended, cell unchanged. 2022-06-07 and 2024-03-05 already landed (CONFIRMED/primary) where the dossier found null or a weaker ceiling; nothing to land. 2016-06-07 is null in both the dossier and the live dataset; no row needed. 2018-06-05 was absent from the live dataset and is now landed as a new ceiling/REFUTED_AS_PLATEAU row (112,403/136,388=82.41%, comparable=false; the dossier proves the county's earliest-surviving capture already postdates election night by 3 days and kept climbing after that).

dossier-lake-ca.md: Lake County general election research. Status: Pending integration.

dossier-lake-ca-primaries.md: Lake County primary election research. Status: Integrated 2026-07-10 (backfill batch 1): all 6 primary rows were already landed via the SoS status-page sweep with matching values; 2012/2014/2016/2022/2024 corroborated in place (JSON note append, source/confidence unchanged), 2018 upgraded from the SoS single-capture PLAUSIBLE/secondary read to this dossier's county-report bracket (CONFIRMED/primary).

dossier-los-angeles-ca-primaries.md: Los Angeles County primary election research. Status: Integrated 2026-07-10 (backfill batch 2): 2012-06-05, 2014-06-03, 2022-06-07, 2024-03-05 were already landed via the SoS status-page sweep (CONFIRMED/primary, bracketed) with values matching the dossier exactly; equal evidence class, so cross-cited as corroboration in the JSON note only (no field change). 2016-06-07 and 2018-06-05 were absent from the live dataset entirely and are now landed as new CONFIRMED/primary rows from the dossier's registrar press-release + exact-arithmetic bracket evidence.

dossier-madera-ca-primaries.md: Madera County primary election research. Status: Integrated 2026-07-10 (backfill batch 2): all 6 primary rows were already landed (no new rows). 2012/2014/2016 dossier concluded null where the live dataset already had CONFIRMED/primary SoS-sweep values (nothing to land). 2022/2024 match the dossier exactly (Clarity version bracket, independent Sierra News Online corroboration); equal evidence class, cross-cited as corroboration in the JSON note only. 2018-06-05 UPGRADED from the live PLAUSIBLE/secondary CA SoS single-capture read to the dossier's CONFIRMED/primary Clarity version-bracket evidence (same 18,258 value both routes; prior read retained as history in the JSON note).

dossier-mendocino-ca.md: Mendocino County general election research. Status: Pending integration.

dossier-mendocino-ca-primaries.md: Mendocino County primary election research. Status: Integrated 2026-07-10 (backfill batch 1): 2012 dossier concluded null where the live dataset already had a SoS-sweep value (nothing to land). 2016/2018/2022/2024 already sourced with matching values, corroborated in place (no field changes; 2018 stays PLAUSIBLE/secondary with its calibration flag carried forward, both routes independently agree on the same unusually-high figure). 2014-06-03 is a VALUE DISAGREEMENT the dossier's subtraction-derived 9,498/57.86% (PLAUSIBLE/secondary) does not match the landed 8,669/52.80% (CONFIRMED/primary, SoS sweep); the landed value was NOT touched (stronger evidence class), flagged to the operator in the batch-1 report rather than silently resolved.

dossier-napa-ca-primaries.md: Napa County primary election research. Status: Integrated 2026-07-10 (backfill batch 2): 2012-06-05, 2014-06-03, 2016-06-07, 2022-06-07, and 2024-03-05 were already landed via the SoS status-page sweep (CONFIRMED/primary, bracketed), values matching the dossier exactly; equal evidence class, cross-cited as corroboration in the JSON note only. 2018-06-05 (Napa's VCA/e-pollbook rollout election, classed vs_epollbook=post) was absent from the live dataset entirely and is now landed as a new CONFIRMED/primary row from the county's own report series, with the RUNBOOK 7.5 ballots-cards-vs-times-cast mislabel resolved via the Governor contest cross-check.

dossier-nevada-ca-primaries.md: Nevada County primary election research with technology findings. Status: Integrated 2026-07-10 (backfill batch 2): 2012-06-05, 2014-06-03, 2016-06-07, 2022-06-07, 2024-03-05 were already landed via the SoS status-page sweep (CONFIRMED/primary, bracketed); 2022/2024 match the dossier exactly and are cross-cited as corroboration in the JSON note only; 2012/2014 landed as null in the dossier (nothing to land, live already stronger); 2016 landed as a documented FLOOR (25,353/56.13%) in the dossier, weaker than and below the live CONFIRMED value (27,852/61.66%), left untouched. 2018-06-05 was absent from the live dataset entirely and is now landed as a new CONFIRMED/primary row from the county's own scanned last-of-night report (via YubaNet), with vs_asv corrected from the dossier's draft "pre" to "post" to match this county's corrected ASV adoption year (2016, per the 2026-07-10 Nevada tech adjudication, which independently resolved both of the dossier's own major flags about the county's true e-pollbook/ASV adoption years).

dossier-orange-ca-primaries.md: Orange County primary election research. Status: Integrated 2026-07-10 (backfill batch 2): 2022-06-07 and 2024-03-05 were already landed via the SoS status-page sweep (CONFIRMED/primary, bracketed), values matching the dossier exactly; equal evidence class, cross-cited as corroboration in the JSON note only. 2012-06-05, 2014-06-03, 2016-06-07, and 2018-06-05 were absent from the live dataset entirely and are now landed as new CONFIRMED/primary rows from the county's own ocvote.gov numbered-run report series with time-gap brackets.

dossier-placer-ca-primaries.md: Placer County primary election research. Status: Integrated 2026-07-10 (backfill batch 2): 2012-06-05, 2016-06-07, 2024-03-05 were already landed via the SoS status-page sweep (CONFIRMED/primary), values matching the dossier (2012/2016, via the county's own GEMS report) and the placer-2024-03-retry.md recovery (2024, via the CA SoS's own electionresults.sos.ca.gov/returns/status page, the same route the sweep independently used) exactly; cross-cited as corroboration in the JSON note only. 2014-06-03 and 2022-06-07 already landed (CONFIRMED/primary) where the dossier concluded null; nothing to land. 2018-06-05 is null in both the dossier and the live dataset; no row needed. No new rows this pass -- all six primaries were already present.

dossier-riverside-ca-primaries.md: Riverside County primary election research. Status: Pending integration.

dossier-sacramento-ca-primaries.md: Sacramento County primary election research. Status: Integrated 2026-07-10 (backfill batch 2): 2014-06-03 was already landed via the SoS status-page sweep (CONFIRMED/primary, 122,053); the dossier's own independent finding for this date (140,521, secondary, a documented ceiling) DISAGREES with the landed value, but a NewsBank pass found no clean count either, so per the task's explicit instruction the landed cell is left unchanged with a one-line NewsBank-checked note appended (not silently reconciled). 2022-06-07 and 2024-03-05 already CONFIRMED/primary, values matching the dossier exactly; cross-cited. 2016-06-07 and 2018-06-05 were absent from the live dataset and are now landed as new rows (2016 a documented ceiling/REFUTED_AS_PLATEAU per the dossier's own finding that the count was still moving; 2018 CONFIRMED, Sacramento's VCA/e-pollbook rollout election, exposing a numerator-checker gap fixed via a render_verified.json entry: the count lived in a hidden HTML input's value attribute, stripped by the shared tag-stripping regex). 2012-06-05 was null in the dossier (all three machine routes exhausted) but is now landed as a new PLAUSIBLE/secondary row from a NewsBank recovery (Sacramento Bee, 2012-06-06, docref news/158D11D2DFBCFC18, 150,286/232,743=64.57%); this NewsBank figure could not be independently corroborated against a cached artifact in this repo (the committed newsbank-recovery.md log shows only a NEEDS_LOGIN-blocked run), so it is flagged for a human spot-check.

dossier-san-bernardino-ca-primaries.md: San Bernardino County primary election research. Status: Integrated 2026-07-10 (backfill batch 2): 2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05 are null in both the dossier and the live dataset; no rows needed. 2022-06-07 was already landed via the SoS status-page sweep (CONFIRMED/primary, 119,998/257,580=46.59%), matching the dossier's independently-routed value (the county's own downloadable Election Summary Report) exactly; cross-cited as corroboration in the JSON note only. 2024-03-05 was already landed (CONFIRMED/primary, 150,018/305,853=49.05%) where the dossier concluded null; nothing to land, live already stronger. No new rows this pass.

dossier-san-diego-ca-primaries.md: San Diego County primary election research. Status: Pending integration.

dossier-san-mateo-ca-primaries.md: San Mateo County primary election research. Status: Integrated 2026-07-10 (backfill batch 2): 2014-06-03, 2022-06-07, 2024-03-05 were already landed via the SoS status-page sweep (CONFIRMED/primary), values matching the dossier's independently-routed evidence (county precinct reports / livevoterturnout ENR) exactly; equal evidence class, cross-cited as corroboration in the JSON note only. 2016-06-07 and 2018-06-05 are null in both the dossier and the live dataset (genuinely unrecoverable by machine per the dossier's documented search trail; both carry FLAGs for a human/NewsBank follow-up, not chased further here). 2012-06-05 was absent from the live dataset entirely and is now landed as a new CONFIRMED/primary row from the county's own live precinct-turnout report. Fixed a verify_en_numerators.py false-negative along the way: it classified sources as PDF/HTML purely from the URL, missing a live PDF served without a .pdf suffix; now sniffs the fetched bytes' magic number.

dossier-santa-clara-ca-primaries.md: Santa Clara County primary election research. Status: Pending integration.

dossier-tehama-ca.md: Tehama County general election research. Status: Pending integration.

dossier-tehama-ca-primaries.md: Tehama County primary election research. Status: Integrated 2026-07-10 (backfill batch 1): 2012/2014/2022 dossier concluded null where the live dataset already had SoS-sweep values (nothing to land); 2016-06-07 and 2018-06-05 are null in both the dossier and the live dataset (no row needed, same as this county's existing general-election gaps for those years); 2024-03-05 already CONFIRMED/primary with a matching value, corroborated in place.

findings-rewrite-draft.md: Draft of consolidated research findings across recovery operations. Status: Pending editorial review before integration into public findings.

gap-triage-draft.md: Analysis and triage of remaining data gaps across counties. Status: Pending integration into gap-reference documentation.

human-verify-v2.md: Second pass of human verification results; discrepancies noted and reconciled. Status: Pending integration into verification record.

mega-integration-log.md: Master operational log tracking which recovered data has been integrated into data/research/election-night/ and which remains pending. STATUS: Active tracking document; use this to prioritize remaining work.

nevada-tech-adjudication.md: Technology platform findings for Nevada County adjudicated against county sources. Status: Integrated partially; some findings pending supplemental verification.

newsbank-recovery.md: Results from NewsBank archive recovery (historical newspaper text recovery). Status: Pending integration into news-source timeline.

placer-2018-general-retry.md: Retry recovery for Placer County 2018 general election; previous gaps addressed. Status: Pending integration.

placer-2024-03-retry.md: Retry recovery for Placer County 2024 March primary election; web archive access rescan. Status: Integrated 2026-07-10 (backfill batch 2): the retry's recovered 69,436/135,869=51.11% figure (via electionresults.sos.ca.gov/returns/status) matches the already-landed live row exactly (same route independently found by the SoS status-page sweep); cross-cited as corroboration in the placer-ca.json 2024-03-05 note, alongside the dossier-placer-ca-primaries.md cross-cite for the same row.

prelim-analysis.md: Preliminary statistical analysis of recovered datasets with confidence intervals. Status: Pending integration into analysis section after data validation complete.

prelim-analysis-4ctrl.md: Preliminary analysis limited to 4-county control set with detailed methodology. Status: Pending integration as case-study analysis.

santa-clara-2012-06-retry.md: Retry recovery for Santa Clara County 2012 primary election; focused archive search. Status: Pending integration.

sf-composition-curve.md: San Francisco ballot composition analysis over time. Status: Integrated into SF-specific findings; details pending supplemental review.

sos-disagreements-adjudication.md: Reconciliation of disagreements between recovered data and Secretary of State records. Status: Pending integration into variance-explanation document.

sos-status-sweep.md: Survey of Secretary of State publication status and availability across all elections. Status: Integrated partially; updates pending monthly verification.

sweep_applylist.json: JSON apply-list mapping recovered records to target locations in data/research/election-night/; used to drive batch integration. STATUS: Primary operational artifact; do not edit without logging changes to mega-integration-log.md.

vca-bundle-analysis.md: Voter choice analysis bundle findings (conditional vote sharing patterns). Status: Pending integration into detailed analysis.
