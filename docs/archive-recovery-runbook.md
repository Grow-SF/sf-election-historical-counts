# Archive-recovery runbook

How to recover historical San Francisco election-night and mid-canvass vote
counts from newspaper and web archives — the method, the automation, and the
hard-won lessons. Written so a future maintainer (human or agent) can extend
the dataset without rediscovering everything.

This complements two narrower docs:
- [`newsbank-agent-playbook.md`](analysis/newsbank-agent-playbook.md) — capture
  + reader-agent prompt rules (the failure modes to avoid).
- [`public-search-log.md`](analysis/public-search-log.md) — what has already
  been searched per archive (so you don't redo it). Ships to the site `/methods`.

The narrative record of everything found/rejected is
[`analysis/2026-06-10-archive-recovery-ledger.md`](analysis/2026-06-10-archive-recovery-ledger.md)
(internal working diary — **not** for publication; the curated public version
is `public-search-log.md`).

---

## What we're recovering, and what counts as valid

The project's finding: we learn election outcomes much later than we used to —
not because counting got slower, but because the vote shifted to late-arriving
mail. To show that, we need, for each historical election, the **share of the
final certified vote that was counted by election night** (and the days
after). Every value is a
**conservative floor** — a number the true count cannot be below — derived one
of these ways, in rough order of strength:

1. **Turnout / "ballots cast" prose** — "51.2% of the city's 339,306
   registered voters went to the polls." Best: no undervote gap.
2. **Registrar "remaining" statement** — certified total minus "X ballots
   still to be counted." A real DOE figure beats a reporter's guess.
3. **Top ballot-measure sum** (YES+NO) — every voter can vote on a measure,
   so it floors ballots cast better than a partisan contest.
4. **Top-contest candidate sum** — a single race's votes ≤ ballots cast.
5. **In-person floor (the "diamond")** — certified precinct ballots ÷
   certified total, from the DOE turnout table / SoS. In-person ballots are
   counted election night, so this is a guaranteed night floor even with **no**
   newspaper at all. For high-in-person elections (pre-2002) this is often
   83–93% and already strong — such elections are *not* "missing" night data.

**Verification gates (every candidate number must pass before ingestion):**
- contest sum ≤ certified ballots (see denominator caveat below);
- monotone vs neighboring dated observations (a later count can't be smaller);
- printed percentages match printed counts within ~1 point;
- load-bearing digits re-read independently (a second model pass, or by hand);
- the column header actually says **San Francisco** (neighboring-county columns
  are identical in layout — a San Mateo "District 5" was once misread as SF).

**The denominator lesson (important).** An internal contradiction —  a contest
sum *exceeding* the certified total — usually means the **denominator is
wrong**, not the newspaper. The DOE turnout table undercounts at least two
1970s elections (1974-06, 1978-11): a single contest drew more votes than its
"ballots cast" figure, which is impossible. Re-read the scan AND question the
certified figure before excluding anything. Tracked in
[`denominator-errors.md`](denominator-errors.md).

---

## Where the data lives (which archive for which era)

| Era / type | Best source | How |
|---|---|---|
| 2015–present | DOE per-release reports | the `sfcount` pipeline (see main README) |
| 2000–2014 mid-canvass | Wayback Machine of DOE results pages | CDX sweep (below) |
| 1986–2002 | Chronicle "HOW SAN FRANCISCO VOTED" text tables | NewsBank **text** archive |
| 1960–2017 night/day-after | Chronicle results boxes (image edition) | NewsBank **image** archive (capture + read) |
| any year, marquee races | other papers (Mercury News, Bee, AP wire) | NewsBank **all-publications** search |
| certified denominators | DOE turnout table; CA SoS Statement of Vote | `data/*.csv`; archive.org for old SoV |

Key access facts:
- **NewsBank** is behind the SF Public Library (SFPL) card via ezproxy. The
  *search* index at `sfchronicle.newsbank.com` and the *Access World News*
  interface (`infoweb-newsbank-com.ezproxy.sfpl.org`) return **different**
  result sets over the same archive — always try both; the AWN interface
  surfaced tables the Chronicle portal missed.
- The text archive starts ~1985. The image edition runs 1865–2017.
- The **print SF Examiner is NOT digitized** anywhere (NewsBank's "SF
  Examiner" is the post-2006 Examiner.com blog network). It survives on
  microfilm only — the top non-digital lead.
- NewsBank **issue labels are not a fixed offset** from the masthead date
  (1983 label = masthead+1; 1975-12 and 1995 labels = masthead). **Always
  masthead-verify** the captured page before assigning an observation date.

---

## Prerequisites for the NewsBank scripts

The browser-automation scripts drive a logged-in Chrome over the DevTools
protocol. They require:
1. An SFPL library card and an **active ezproxy session** — the user logs in
   manually (we never automate credential entry).
2. Chrome launched with remote debugging and background throttling disabled:
   ```
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
     --remote-debugging-port=9222 \
     --disable-background-timer-throttling \
     --disable-renderer-backgrounding \
     --disable-backgrounding-occluded-windows
   ```
   (Throttling must be off or off-screen capture windows render blank.)
3. `puppeteer-core` available to Node, and `tesseract` + Python `pillow`.
4. Output goes to the **gitignored** `mirror/newsbank/` tree (licensed
   content — cited, never republished, never to a CDN). Only IDs/citations
   and derived floors enter committed data.

Every script aborts loudly if it hits the SFPL auth wall (text "Articles and
Databases — Authentication") rather than saving login-page garbage. If that
fires, ask the user to re-login, then resume.

`scripts/archive-recovery/` (all reference implementations; paths/URLs are
hardcoded to this project + SFPL — adapt as needed):
- `session_probe.js` — load a known doc; confirm the session is alive.
- `window_login.js` / `window_park.js` — surface the login window top-left;
  park ezproxy windows off-screen so they don't disrupt the user.
- `fetch_doc.js <DOCID> <ELECTION>` — save one Access World News text doc.
- `harvest_text.js` — multi-paper text harvest: per election × date-window ×
  query, collect docrefs, fetch each (the winning vein for marquee races).
- `capture_page.js <url> <out.png>` — pan-until-bottom image capture of one
  page as overlapping vertical slices (handles variable page heights).
- `sweep_section.js <election> <issue> <p0> <p1>` — walk a page range of an
  image-edition issue, full-capturing each (for finding the results box).
- `locate_columns.py <glob> [out]` — find the SF column in slices, emit crops.
- `triage.sh <glob>` — OCR slices, list those that look like a results table.
- `crop_helper.py FILE x0 y0 x1 y1 OUT` — crop+zoom a fractional region,
  capped at 1900px (the API image limit) for a reader to read.

---

## The loop (manual or agent-driven)

```
1. SEARCH    find candidate articles/issues (harvest_text.js, or Wayback CDX,
             or a manual NewsBank search the user pastes you a docref from)
2. CAPTURE   text → fetch_doc.js;  image → sweep_section.js / capture_page.js
3. TRIAGE    triage.sh to find which slices hold a results table (free, local)
4. LOCATE    locate_columns.py to crop the SF column from the right slices
5. READ      a reader agent (or you) transcribes digits from the crops
6. VERIFY    arithmetic gates; re-read load-bearing digits; masthead-date it
7. INGEST    append a row to data/sf_archival_canvass_points.csv (schema below)
8. REBUILD   python3 scripts/build_viz_data.py  → viz/src/data/*.json
9. RECORD    update the ledger; if a contest exceeds certified, add it to
             denominator-errors.md
```

### Automating with agents (what worked)

Reading scanned tables is the expensive step; delegate it and keep your own
context clean.

- **Parallelism.** Independent windows/searches run concurrently. Run 3–4
  harvest/sweep jobs at once (background bash), and dispatch 3–5 reader
  subagents in parallel, each on a disjoint slice set. Don't read scan images
  in the main context — it blows up token cost (images replay every turn).
- **Model tier.** Use a cheap model (Haiku) for first-pass transcription, a
  stronger model (Sonnet) to re-read load-bearing or disputed digits. Vision
  beats `tesseract` on bold table digits; `tesseract` is for *locating* and
  free triage only.
- **Batch size: 1-2 elections per reader agent, not 5.** Image-reading agents
  overflow fast (each crop/Read is heavy and replays every turn); in
  practice they died at ~70-200 tool calls, typically after 2-3 elections,
  even under a crop-only rule. Small batches finish before overflow.
- **Incremental persistence (non-negotiable).** Every reader agent appends to
  a file on disk **after each item**, not just in its final message. Agents die
  mid-run ("prompt too long"); a dead agent must cost nothing. Make it a HARD
  rule with the exact command in the prompt, one file per item so there are
  no append races and salvage is trivial:
  `printf '%s\n' 'ROW' >> /tmp/<job>/<item-id>.psv` after EACH item.
  Salvage a dead agent from its transcript at
  `~/.claude/projects/<proj>/<session>/subagents/agent-<id>.jsonl` (extract
  assistant text + bash `#`-comment narration + grep tool_results for key
  numbers; never cat the whole JSONL, it overflows context).
- **Dead agents leave their crops on disk.** Before re-dispatching, run
  `tesseract` over the crops the dead agent already made: it recovers most
  numbers free and locally, without re-reading images. De-hyphenate OCR text
  (`-\n`) and the top-line contest sums are often readable directly in the
  main context, cheaper than a new reader agent for easy cases.
- **Reader-prompt must-haves** (full list in the playbook): report the
  masthead date first; give two distinct null verdicts — `not-in-scans`
  (capture incomplete) vs `not-on-page` (full page verified, absent) and never
  the second when the page bottom wasn't captured; treat any numeric context
  you give them as approximate (never let them "correct" a digit toward an
  expected value); crop tall column-band first, then row-level zoom.
- **Verify agent claims.** Re-check every agent-claimed number against the
  source before ingesting — agents have invented totals, misattributed
  neighboring counties, and misread leading digits. The arithmetic gates catch
  most; a second independent read catches the rest.

### Searching the live web / Wayback (no login needed)

- Other outlets are free and Google-indexed: Berkeley Daily Planet, BeyondChron,
  FairVote, and SFGate's own archive. A distinctive query (names + numbers)
  works; generic queries drown.
- Wayback CDX for DOE results pages:
  ```
  curl -s 'http://web.archive.org/cdx/search/cdx?url=<PATTERN>&from=YYYYMMDD&to=YYYYMMDD&collapse=urlkey&limit=50&matchType=prefix'
  ```
  Fetch a snapshot's raw bytes with the `if_` suffix:
  `http://web.archive.org/web/<TS>if_/<ORIGINAL_URL>`. Known DOE page families:
  `sfgov.org/site/election(s)_index.asp?id=NNNN`, `sfelections.org/results/<YYYYMMDD>/`,
  the frozen Lotus Domino `election2.nsf` / `eresults.nsf` views. Caveat: the
  1999 Domino DB served stale data even on election night; the Nov-2000 DB was
  wiped when reused for the December runoff. **WebFetch is blocked on
  web.archive.org — use `curl`.**
- Always read the page's own "Last Updated" / "RUN DATE" stamp and date the
  observation by that, not by the capture timestamp (a recurring +1-day error).

---

## Ingestion schema

`data/sf_archival_canvass_points.csv` — one row per observation:

```
election_date,election_name,observed_at,stamp_kind,days_since_election,
ballots_counted_total,ballots_vbm,ballots_election_day,registered_voters,
certified_final,pct_of_final,source_url,extraction,final_source
```

- `stamp_kind`: `capture-time` | `page-self-reported` | `minutes-stated` |
  `news-derived`.
- `extraction`: `wayback-html` | `chronicle-subscription` | `newsbank-sfpl`
  (text) | `newsbank-image-scan` | `web-news`.
- `observed_at` < election day +1 06:00 → counts as a **night** point; later →
  day-N. The build (`scripts/build_viz_data.py`) applies this cut, marks
  partials, and raises any solid floor below its in-person diamond up to the
  diamond (a floor can't render below the diamond).
- `source_url` should carry the docref/citation; the build turns NewsBank
  docrefs into SFPL deep links on the `/sources` page. `final_source`
  documents the certified denominator (and flags it if contradicted).

After editing the CSV: `python3 scripts/build_viz_data.py`, eyeball the chart,
commit `data/` + `viz/src/data/`.

---

## Status & what's left

The night-of record now spans 1908–2026. Remaining gaps are documented on the
site's `/missing` page and fall into three exhausted-for-digital groups:
pre-1985 local races (no wire coverage; image archive swept), 1986–2010
day-2-floor-only elections (no separately archived night table), and modern
ranked-choice/special elections (coverage gives night *percentages* but not
absolute counts). The two remaining non-digital paths: **SFPL/State Library
microfilm** (esp. the print Examiner) and a **DOE public-records request**
(draft in [`doe-records-request.md`](doe-records-request.md)).
