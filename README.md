# The Long Count

**How long San Francisco takes to know who won — a century-plus of it.**

It takes far longer to learn the outcome of a San Francisco election than it
used to. Not because the count itself got slower — the back-end pace of
processing a ballot is about what it always was — but because of what changed
around it: vote-by-mail grew from a sliver of the vote in the 1960s to nine in
ten today, and those ballots arrive late and need signature checks before they
can be counted. So election night went from telling us almost everything to
telling us barely half, and the result that once was clear by midnight now can
take days or weeks. This project measures that shift from primary sources —
the Department of Elections' own results releases plus a deep recovery of
historical counts from newspaper and web archives — and tells the story in an
interactive site.

Live data spans **1908–2026**: 97 elections with an election-night count
(including 22 pre-1964 counts recovered from the hand-count era, back to 1908),
~169 recovered mid-canvass observations, and 241 modern per-release reports,
every number traceable to a cited source. The long view reveals four eras, not
one — fast (1908–12), slow (1914–26, when hand-counting long Progressive-era
ballots was the bottleneck), fast again (1928–1990s), and the modern
mail-driven slide — see
[`docs/analysis/2026-06-13-a-century-of-election-nights.md`](docs/analysis/2026-06-13-a-century-of-election-nights.md).

---

## Repository map

| Path | What it is |
|---|---|
| `sfcount/` | Python pipeline: ingests DOE per-release reports (2015–present) |
| `data/` | All committed datasets (CSV) — the source of truth |
| `viz/` | Next.js story site, "The Long Count" (builds from `data/`) |
| `scripts/` | `build_viz_data.py` (data → viz JSON) + `archive-recovery/` tooling |
| `docs/` | Methodology, runbook, search log, the records-request draft |
| `mirror/` | **gitignored** — licensed NewsBank/Chronicle source content (cited, never republished) |
| `sf-long-count-archive/` | read-only predecessor (PDF-parsing); kept for reconciliation |

## Key datasets (`data/`)

- `sf_count_timeline.csv` — modern per-release counts (the `sfcount` output).
- `sf_archival_canvass_points.csv` — recovered historical observations
  (1960–2014); schema and method in the runbook.
- `sf_turnout_history_doe_1899_2019.csv` — DOE certified turnout (the
  denominators). Known data-quality issues tracked in
  `docs/denominator-errors.md`.
- `sf_vbm_share_sos.csv`, `sf_turnout_history_1960_2002.csv` — mail-share and
  precinct/absentee splits from the CA Secretary of State and DOE.

## The modern pipeline (`sfcount`)

Ingests the structured files SF Elections publishes per release —
`summary.xml` (2019+) and `summary.txt` TSV (2008–2018) — rather than parsing
PDFs. Timestamps come from HTTP `Last-Modified` headers (`data/manifest.csv`).

    uv run sfcount all        # inventory → fetch → parse → validate → derive
    uv run sfcount fetch      # resumable; ~25 min cold
    uv run pytest             # offline suite (real downloaded fixtures)

After a new election: add it to `SUPPLEMENTAL_ELECTIONS` in
`sfcount/inventory.py` if sf.gov doesn't list it yet; run `uv run sfcount all`
during the canvass; after certification add the certified total to
`CERTIFIED_FINALS` in `sfcount/validate.py` and commit `data/`.

## The visualization (`viz/`)

A Next.js story site built entirely from the committed datasets: the
election-night-share trend (with a 2002 structural break, the permanent
vote-by-mail list), an any-margin "days until the winner is beyond doubt"
explorer, the 1964–2026 mail-ballot share, and a per-canvass trajectory
explorer. Filters are URL-encoded for sharing. Routes: `/` (story),
`/sources` (every number, linked to its archive), `/missing` (open research
list + how to contribute), `/methods` (the public search log).

    python3 scripts/build_viz_data.py   # rebake viz JSON after the pipeline runs
    cd viz && npm install && npm run dev

## Archive recovery (the historical data)

Most of the 1960–2014 record was recovered by hand-and-agent from newspaper
and web archives. If you want to extend it, **start with
[`docs/archive-recovery-runbook.md`](docs/archive-recovery-runbook.md)** — the
full method: which archive holds which era, the browser-automation and
agent workflow, the verification gates, and the lessons (including why an
apparent "contradiction" is usually a bad denominator, not a misread).

Supporting docs:
- `docs/analysis/newsbank-agent-playbook.md` — capture + reader-agent rules.
- `docs/analysis/public-search-log.md` — what's already been searched (so you
  don't redo it); also served at the site's `/methods`.
- `docs/denominator-errors.md` — DOE turnout figures contradicted by the
  count, for manual verification.
- `docs/doe-records-request.md` — drafted public-records request for the
  remaining gaps.

Reusable tooling lives in `scripts/archive-recovery/` (browser capture, text
harvest, OCR triage, column location). These drive a logged-in Chrome over an
SFPL library session; prerequisites are in the runbook.

The Chronicle fetch/scan scripts (`scripts/fetch_*.py`, `scripts/scan_*.py`,
`scripts/sweep_*.py`, `scripts/extract_sf_ballot.py`) write to and read from the
gitignored `mirror/chronicle-sfgate/` by default, resolved relative to the repo.
Set `SF_MIRROR_DIR` to point them at a mirror kept elsewhere:

    SF_MIRROR_DIR=/path/to/mirror python3 scripts/fetch_chronicle.py

## Contributing data

The `/missing` page lists the elections still lacking an election-night count
and what would resolve each. Newspaper photos, microfilm scans, or DOE release
reports are welcome at **steven@growsf.org** — every submission is verified
against certified totals and cited on the sources page.

## Provenance & licensing

Every published number traces to a primary source on the `/sources` page.
Newspaper archive content (NewsBank, Chronicle) is **cited, not republished**:
it lives only in the gitignored `mirror/` tree and never ships to the site or a
CDN. Public-record sources (DOE releases, Wayback captures, Secretary of State
statements) are mirrored and linked freely.

## Data boundaries (don't trip on these)

- Per-release snapshots exist on sfelections.org only from Nov 2015; earlier
  counts are archival recoveries (floors, marked as such).
- Don't backfill VBM/election-day splits from the eData "returned VBM ballots"
  tool — returned-and-accepted ≠ counted.
- The DOE turnout table undercounts at least two 1970s elections (a single
  contest exceeds its "ballots cast"); see `docs/denominator-errors.md`.
- NewsBank issue labels are not a fixed offset from the masthead — always
  masthead-verify a scanned page's date before dating an observation.
