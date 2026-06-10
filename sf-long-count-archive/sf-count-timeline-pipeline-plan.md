# SF Vote-Count Timeline Pipeline — Plan

**Goal:** One CSV containing every preliminary results release for every San Francisco election from November 2000 to present, with cumulative ballots counted per release, so we can compute and visualize days-to-90%-counted across 25 years.

**Status:** Plan for review. No code yet.

---

## 1. What reconnaissance already confirmed

Probed live before writing this plan:

- `https://www.sfelections.org/results/{ELECTION_YYYYMMDD}/data/{REPORT_YYYYMMDD}/summary.pdf` returns **200** for both 2024 (`20241105/data/20241110/`) and 2016 (`20161108/data/20161109/`, `20161110/`, `20161122/`). The per-release snapshot structure is consistent across at least 2016–2024.
- Directory listing on `/data/` is **403** — we cannot enumerate snapshot folders; we must generate candidate report dates and probe.
- `/results/20001107/` is **403** even with a browser user agent. The sf.gov "November 7, 2000 Final Election Results" page exists and claims per-day reports, so pre-~2008 data likely lives at different paths (sf.gov, old sfgov.org structures, or Wayback Machine).
- Modern summary PDFs (Dominion era, ~2019+) contain an explicit turnout block: `Election Day N / Vote by Mail N / Total N / Registered Voters N / Turnout %` plus a report timestamp. This is the parse target.
- Older summaries (2016 era, DFM/ES&S era) are "Unofficial Summary Report N" with a different layout; turnout appears as `Registration & Turnout` rows. Era-specific parsers needed.

## 2. Scope

- **Elections:** All SF elections Nov 2000 → June 2026. Source of the canonical list: sfelections.org past results index (the eData site lists elections back to 2012; the sf.gov Results page lists back to 1995). Expect ~50 elections including runoffs, specials, and recalls.
- **Per election:** every results release (election-night releases #1–4 plus daily/periodic releases through certification, typically 10–17 reports).
- **Out of scope for the pipeline:** RCV rounds, contest-level results, precinct data. Turnout block only.

## 3. Output schema

`sf_count_timeline.csv`, one row per (election, release):

| column | type | notes |
|---|---|---|
| election_date | date | e.g. 2024-11-05 |
| election_name | str | e.g. "Consolidated General" |
| report_seq | int | order of release within election |
| report_datetime | datetime | from PDF timestamp where available, else folder date |
| ballots_counted_total | int | cumulative |
| ballots_vbm | int | nullable; where the report breaks it out |
| ballots_election_day | int | nullable |
| registered_voters | int | |
| source_url | str | provenance |
| parser | str | which era-parser produced the row |

Derived columns (computed in a second step, not stored in the raw CSV): `final_ballots` (max per election, cross-checked against certified turnout), `pct_of_final`, `days_since_election`, `days_to_90pct` per election.

## 4. Pipeline stages

**Stage 0 — Election inventory.** Scrape the sf.gov past-results index and the sfelections eData election list; merge into `elections.csv` (date, name). Manual review of this file before proceeding — it's small and errors here poison everything downstream.

**Stage 1 — Snapshot discovery.** For each election, probe `/results/{date}/data/{candidate}/summary.pdf` for candidate report dates: election day through election day + 35 days. Also probe election-night variants (`{date}_1` … `{date}_4` or similar — pattern unconfirmed, needs one manual check against a known election). HEAD requests, rate-limited (1 req/sec, polite User-Agent), results cached to disk so reruns are free.

**Stage 2 — Download.** GET every discovered summary.pdf into `raw/{election}/{report_date}/summary.pdf`. Never re-download an existing file. Expected volume: ~50 elections × ~15 reports ≈ 750 PDFs, small files.

**Stage 3 — Parse.** Era-dispatched parsers:
- **Era C (~2019–present, Dominion):** text-extract the turnout block (`Voters Cast` table). pdfplumber.
- **Era B (~2008–2018, "Unofficial Summary Report"):** parse `Registration & Turnout` rows. Layout shifts within this era; expect 2–3 sub-variants.
- **Era A (2000–~2007):** unknown format, possibly HTML pages or PDFs only reachable via Wayback Machine. Defer: build A last, after B/C prove the schema. If election-era snapshots weren't archived per-day, days-to-90% may be unrecoverable for some early elections — the report can say so honestly rather than interpolate.

Every parse failure is logged with the source file, never silently skipped.

**Stage 4 — Validate.**
- Cumulative counts must be monotonic non-decreasing within an election; flag violations (they can legitimately occur if a report restates totals — investigate, don't auto-drop).
- Final release total must be within 0.5% of certified turnout (cross-reference the Historical Voter Turnout dataset on sf.gov, which goes back to 1899). Mismatch → flag for manual review.
- Spot-check 3 elections by hand against press releases (e.g. Nov 2024: 412,231 final; 364,959 by Nov 10 = 88.5%... note: my earlier in-chat claim that Nov 10 crossed 90% was wrong — 364,959/412,231 = 88.5%; the crossing is Nov 11–12. The pipeline exists precisely to stop this kind of eyeballing).

**Stage 5 — Derive & export.** Compute pct_of_final and days_to_90pct per election; export `sf_count_timeline.csv` + `sf_days_to_90.csv` (one row per election) for the dashboard/report.

## 5. Known risks and open questions

1. ~~Election-night snapshot folder naming~~ — **resolved by probing.** Election-night releases live at `{election}/data/{election_date}_N/summary.pdf`, N = 1–4, confirmed in both 2016 and 2024 (`_5` 404s in both). Stage 1 probes `{d}` and `{d}_1` … `{d}_6` for every candidate date; extra probes are cheap and cached.
2. **Pre-2008 availability** — `/results/20001107/` 403s. Fallback order: alternate sf.gov paths → SFPL archive → Wayback Machine captures of sfgov.org/elections. Risk that per-day granularity simply doesn't survive for 2000–2006; the historical section may need to lean on contemporaneous Chronicle/Examiner reporting for those years.
3. **Runoff elections (Dec 2000–2003)** — small turnout, fast counts; include them but expect to segment them out of the main visualization.
4. **Report timestamps vs. folder dates** — folder date is the release date; PDF-internal timestamp is authoritative when present. Use PDF timestamp, fall back to folder date.
5. **"Ballots counted" definition drift** — older reports may report precincts-reporting rather than ballots; the parser must extract ballots, and where only card counts exist, divide by cards-per-ballot only if that's documented for the election (do not guess).

## 6. Build order

1. Stage 0 inventory (small, manually verifiable)
2. Stage 1+2 for 2019–present (Era C) only
3. Era C parser + validation; confirm Nov 2024 and June 2026 against press releases
4. Extend Stages 1–3 to Era B (2008–2018)
5. Era A investigation (separate spike — feasibility before code)
6. Derivations + export

Each step produces inspectable intermediate artifacts before the next begins.

---

**Decisions (locked):**
- Probe window: election day through election day + 35 days.
- Election-night intra-day releases (8:45pm, 9:45pm, etc.) are separate rows, sequenced by report_seq and report_datetime.
- Capture every release through certification — the dataset does not stop at the 90% crossing. The 90% crossing is a derived statistic only (first release at/above 90% of final), computed in Stage 5; the raw CSV is complete.
