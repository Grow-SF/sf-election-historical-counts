# `data/` — the datasets, documented

This directory is the **source of truth** for the project. Every chart on the
site is built from these files; nothing here is scraped live at view time.

- **CSV files** here are the inputs. Some are produced by the `sfcount` pipeline
  (modern Department of Elections per-release reports); the historical ones are
  hand-recovered from primary sources (newspaper archives, the Department's own
  turnout tables, the California Secretary of State, and the U.S. Census).
- The **JSON the site reads** lives in `viz/src/data/*.json` and is *generated* —
  do not edit it by hand. Rebuild it with:
  ```
  python3 scripts/build_viz_data.py
  ```
- Every recovered value is meant to be **traceable to a cited source** (a
  `source_url`/`source` column, or the row-level citation in the archival file).

**How each file is produced**

| Origin | Files |
|---|---|
| `sfcount` pipeline (modern DOE ingestion) | `manifest.csv`, `elections.csv`, `sf_count_timeline.csv`, `sf_days_to_90.csv` |
| Primary-source recovery (hand-built, cited) | `sf_turnout_history_doe_1899_2019.csv`, `sf_turnout_history_1960_2002.csv`, `sf_vbm_share_sos.csv`, `sf_archival_canvass_points.csv`, `sf_canvass_minutes_statements.csv`, `sf_night_floor_1964_2026.csv` |
| Franchise / eligible-electorate (see [`../docs/eligible-denominator-notes.md`](../docs/eligible-denominator-notes.md)) | `sf_registration_eligible.csv`, `sf_registration_eligible_sov_1974_1998.csv`, `sf_eligible_vap_estimate.csv` |
| Operational / provenance | `mirror_manifest.csv`, `parse_failures.csv`, `newsbank_issue_docrefs.json` |

Recovery methods are documented in
[`../docs/archive-recovery-runbook.md`](../docs/archive-recovery-runbook.md);
known data-quality issues in
[`../docs/denominator-errors.md`](../docs/denominator-errors.md).

---

## Counting & turnout (the core record)

### `sf_count_timeline.csv` — per-release ballot counts (the trajectory)
How the count climbed, release by release, for each modern election. Built by
`sfcount` from the DOE's published `summary.xml`/`summary.txt` files (2015+) plus
Wayback-recovered releases.

| column | meaning |
|---|---|
| `election_date` | election day, `YYYY-MM-DD` |
| `election_name` | official contest name |
| `report_seq` | 1-based order of this release within the election |
| `snapshot` | DOE snapshot id / capture id for this release |
| `report_datetime` | when this release was published (from HTTP `Last-Modified` or capture time) |
| `ballots_counted_total` | cumulative ballots counted as of this release |
| `ballots_vbm` | of which, vote-by-mail (blank if not reported) |
| `ballots_election_day` | of which, in-person/election-day (blank if not reported) |
| `registered_voters` | registered voters for this election |
| `parser` | how the row was obtained (`xml`, `tsv`, `archival`, …) |
| `datetime_source` | provenance of `report_datetime` |
| `source_url` | the release / capture URL |

### `sf_archival_canvass_points.csv` — recovered mid-canvass & night observations (1960–2014)
Historical equivalents of the modern timeline, recovered one observation at a
time from newspaper and web archives. Schema and verification gates are detailed
in the archive-recovery runbook.

| column | meaning |
|---|---|
| `election_date`, `election_name` | the election |
| `observed_at` | timestamp of the observation (`YYYY-MM-DDTHH:MM:SS`) |
| `stamp_kind` | how the time was determined: `capture-time` \| `page-self-reported` \| `minutes-stated` \| `news-derived` |
| `days_since_election` | whole days after election day |
| `ballots_counted_total` | ballots counted as of the observation (a conservative **floor**) |
| `ballots_vbm`, `ballots_election_day` | splits where known (else blank) |
| `registered_voters` | registration for the election (else blank) |
| `certified_final` | the certified final total (the denominator) |
| `pct_of_final` | `ballots_counted_total / certified_final`, percent |
| `source_url` | the row-level citation (archive URL + the exact figure read) |
| `extraction` | `wayback-html` \| `chronicle-subscription` \| `newsbank-sfpl` \| `newsbank-image-scan` \| `web-news` |
| `final_source` | provenance of `certified_final` (and any contradiction flag) |

### `sf_turnout_history_doe_1899_2019.csv` — DOE certified turnout (1899–2019)
The Department of Elections' own historical turnout table (recovered from a 2023
web capture). The backbone denominator series.

| column | meaning |
|---|---|
| `election_date` | `YYYY-MM-DD` |
| `registration` | registered voters |
| `ballots_cast` | certified ballots cast |
| `pct_turnout` | turnout as printed (e.g. `31.57%`) |
| `precinct` | in-person/precinct ballots (`n/a` where not split) |
| `mail` | vote-by-mail/absentee ballots (`n/a` where not split) |

### `sf_turnout_history_1960_2002.csv` — turnout with absentee/precinct split (1960–2002)
DOE/SoS turnout history carrying the absentee-vs-precinct breakdown used to
compute the election-night in-person floor.

| column | meaning |
|---|---|
| `date` | election date, `MM/DD/YY` |
| `registration`, `ballots_cast` | registered voters; certified ballots (comma-formatted) |
| `absentee`, `precinct` | absentee (mail) and precinct (in-person) ballots |
| `pct_turnout` | turnout percent |
| `pct_reg_returned_av` | absentee ballots returned as % of registration |
| `pct_turnout_voted_av` | absentee as % of ballots cast |

### `sf_vbm_share_sos.csv` — certified vote-by-mail share (2002–2014)
Certified polling-vs-absentee splits recovered from California Secretary of State
Statements of Vote and DOE SOV spreadsheets, filling the 2002–2014 gap.

| column | meaning |
|---|---|
| `election_date` | `YYYY-MM-DD` |
| `ballots_polling`, `ballots_absentee`, `ballots_total` | in-person, mail, and total certified ballots |
| `vbm_share_pct` | absentee share of the total |
| `source_url` | the SOV / spreadsheet citation |

### `sf_night_floor_1964_2026.csv` — election-night in-person floor
The non-absentee (precinct) share of the certified total. Precinct ballots are
counted on election night, so this is a guaranteed lower bound on the night share
even with no newspaper data.

| column | meaning |
|---|---|
| `election_date` | `YYYY-MM-DD` |
| `night_floor_pct` | precinct ballots ÷ certified total, percent |
| `method` | how computed (e.g. `non-absentee (precinct) share of certified total`) |
| `source` | source series (`doe-turnout-history`, `certified-sov`, …) |

### `sf_canvass_minutes_statements.csv` — Elections Commission minutes
Registrar statements of ballots-remaining read from meeting minutes, turned into
conservative counted-so-far estimates.

| column | meaning |
|---|---|
| `election_date`, `meeting_date`, `days_since_election` | the election and the meeting |
| `statement` | the quoted statement |
| `derived_estimate` | the conservative figure derived from it |
| `source_page` | the minutes citation |

### `sf_days_to_90.csv` — derived summary (generated)
Per-election summary of how long the count took. Produced by `sfcount` (`derive.py`).

| column | meaning |
|---|---|
| `election_date`, `election_name` | the election |
| `final_ballots` | certified total |
| `n_reports` | number of releases observed |
| `date_90pct`, `days_to_90pct` | when 90% of the final was reached, and days after election |
| `pct_on_election_night` | share counted on election night |

---

## Franchise & the eligible electorate

Full provenance, the citizen-vs-VAP distinction, and caveats are in
[`../docs/eligible-denominator-notes.md`](../docs/eligible-denominator-notes.md).
Findings: [`../docs/analysis/2026-06-14-franchise-and-eligible-electorate.md`](../docs/analysis/2026-06-14-franchise-and-eligible-electorate.md).

### `sf_registration_eligible.csv` — registered vs eligible, CA SoS (2000–2026)
San Francisco county rows from the Secretary of State's Reports of Registration.
Recreate with `python3 scripts/fetch_sos_registration.py`.

| column | meaning |
|---|---|
| `report_date` | the report's "as of" date, `YYYY-MM-DD` |
| `election_context` | which election the report precedes (or "odd-year") |
| `eligible` | SoS eligible-adult-citizen estimate (DOF/Census-derived) |
| `registered` | registered voters |
| `pct_registered_of_eligible` | `registered / eligible`, percent |
| `source_url` | the `county.pdf` on the SoS CDN |

### `sf_registration_eligible_sov_1974_1998.csv` — recovered from printed SOVs (1974–1998)
SF rows recovered from the printed Statement of Vote "Voter Participation by
County" tables on archive.org. **Pending hand-verification.** Recreate the crops
with `python3 scripts/recover_sov_registration.py <archive_id>=<label>`.

| column | meaning |
|---|---|
| `report_date` | election/report date, `YYYY-MM-DD` |
| `election_context` | election label |
| `eligible`, `registered` | eligible-citizen estimate; registered voters |
| `pct_registered_of_eligible` | percent |
| `votes_cast` | ballots cast (cross-check; blank where n/a) |
| `confidence` | `high` \| `medium` \| `low` (low = anomalous in the source, e.g. 1994–96 deadwood) |
| `source_archive_id` | archive.org item id (or `newsbank-<docref>`) |
| `source_leaf` | page/leaf within the scanned volume |
| `source_url` | link to the source |

### `sf_eligible_vap_estimate.csv` — census voting-age & eligible-citizen population (1900–2020)
San Francisco County from the decennial census via **IPUMS NHGIS**
(`scripts/nhgis_extract*.json` reproduce the pulls). A leading comment block in
the file restates the basis and the required NHGIS citation.

| column | meaning |
|---|---|
| `year` | census year |
| `total_population` | total county population (decennial census) |
| `voting_age_pop` | voting-age population (21+ before 1971, 18+ after) |
| `vap_age_basis` | `21+` or `18+` |
| `vap_sex_basis` | `male-only` (1900/1910, pre–women's suffrage) or `both` |
| `vap_kind` | always `nhgis-census` (real count) |
| `citizen_eligible` | eligible (citizen) voting-age count (blank 1980+, where the SoS publishes it) |
| `citizen_kind` | `nhgis-census` (direct) \| `nhgis-approx` \| `nhgis-partial` \| `interp` \| `see-sos` |

---

## Pipeline / provenance helpers

### `elections.csv` — election index
`election_date`, `election_name`, and an `era` label, used to drive the modern pipeline.

### `manifest.csv` — DOE per-release download manifest
One row per fetched DOE release: `election`, `snapshot`, `filename`, `status`,
`last_modified` (the HTTP timestamp that dates each release).

### `mirror_manifest.csv` — licensed-content manifest (paths only)
Inventory of the **gitignored** `mirror/` tree (NewsBank/Chronicle scans, DOE
spreadsheets — cited, never republished): `path`, `source`, `sha256`, `bytes`.
The bytes themselves are not in the repository.

### `parse_failures.csv` — parser error log
`file`, `error` — DOE files the parser could not read (empty when clean).

### `newsbank_issue_docrefs.json` — citation lookup
Maps NewsBank issue dates to document references so the build can turn archival
citations into SFPL deep links on the site's `/sources` page.

---

## Citing this data

See [`../CITATION.cff`](../CITATION.cff) and the "How to cite" section of the
[top-level README](../README.md). Data derived from IPUMS NHGIS and from
licensed newspaper archives carries its own citation requirements noted above.
