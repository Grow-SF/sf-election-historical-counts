# Placer County 2024-03-05 Presidential Primary — election-night plateau RETRY

Read-only retry scout. Target: election-night PLATEAU ballots-counted figure
(not 8pm first tranche, not canvass/certified). Certified final (denominator):
**135,869** Total Voters (Registered 281,556, 48.26% turnout per CA SoS SoV;
registrar's own certified page: "Registered Voters 281,148 - Cards Cast
135,869 48.33%"). Source:
https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf

Prior pass (dossier-placer-ca-primaries.md item 6) result: NOT FOUND / NULL row.
Leads left: (1) abc10.com CDX 504-timeout, (2) Cloudflare/403-blocked live
registrar pages (retry via puppeteer real-browser UA), (3) new: Gold Country
Media/Auburn Journal, Sacramento Bee live-results (Wayback only), KCRA,
CapRadio, county FB/X, CA SoS EN results archive (vote.sos.ca.gov /
returns.sos.ca.gov).

Budget: ~45 min. Started (session clock, not wall-clock date-aware).

---

## Log

### Route A: abc10.com CDX retry (prior lead #1) — CLOSED, genuinely no captures
Found exact URL via WebSearch: `https://www.abc10.com/article/news/politics/elections/placer-county-election-results-races-2024/103-c7babbde-2d77-4bf0-ae62-2add6baaf4df`
(this is the article ID referenced in the dossier FLAG, `103-c7babbde-...`).
- CDX for exact URL, window `20240301`-`20240401`: empty `[]` (query succeeded,
  not a timeout this time).
- CDX for exact URL, full year `20240101`-`20241231`: timed out once, retried,
  came back `[]` on the narrower window. Wayback genuinely never crawled this
  article. Dead end, not a retry-harder problem.

### Route B: Cloudflare/403-blocked live registrar pages — not re-attempted with
puppeteer (superseded — see Route C which found a non-Cloudflare, better
source first). Flagging as still-untried if Route C is ever disputed.

### Route C: CA SoS electionresults.sos.ca.gov — RECOVERED HERE
WebSearch surfaced the correct modern SoS election-night domain:
`electionresults.sos.ca.gov` (vote.sos.ca.gov, which the task briefing named,
is a DIFFERENT site — general voter-info, Incapsula/503-walled solid in CDX,
zero usable captures; the real per-election EN site is
`electionresults.sos.ca.gov`, confirmed live via
`https://www.sos.ca.gov/elections/prior-elections/statewide-election-results/pres-prim-march-2024`).

CDX domain sweep `electionresults.sos.ca.gov`, `20240301`-`20240401`: ~30
root-page captures across election night. Root page (`/`) is a JS-shell
SPA-ish page but its rendered HTML (curled `id_` raw, gunzipped — 1f8b magic
bytes present, per RUNBOOK 7.1) contains a real nav with a link
`/returns/status` — a per-county reporting-status table page, NOT
JS-rendered (plain server HTML, `<table>` with `<thead>` columns: **County
Name | Election Method | Total Precincts | Precincts Reporting | %
Reporting | Registered Voters | Ballots Cast | % Turnout | First Report
Date-Time | Last Report Date-Time | Report Type**).

CDX for `/returns/status` in the same window returned a dense timeline;
fetched and gunzipped (id_ raw form) the Placer row across the full
sequence:

| capture (UTC) | ≈PST | Ballots Cast | %Reporting | Last Report (as printed) | Report Type |
|---|---|---|---|---|---|
| 20240305190731 | 11:07am Mar 5 (pre-close) | 0 | 0.0% | — | — |
| 20240306024058 | 6:40pm Mar 5 (pre-close) | 0 | 0.0% | — | — |
| 20240306063830 | 10:38pm Mar 5 | 51,885 | 0.0%* | Mar 5 9:54 p.m. | R |
| **20240306144409** | **6:44am Mar 6** | **69,436** | **100.0%** | **Mar 6 12:04 a.m.** | **U** |
| 20240306180549 | 10:05am Mar 6 | 69,436 (same) | 100.0% | Mar 6 12:04 a.m. (same) | U |
| 20240307035236 | 7:52pm Mar 6 | 69,436 (same) | 100.0% | Mar 6 12:04 a.m. (same) | U |
| 20240308155126 | 7:51am Mar 8 | 69,436 (same) | 100.0% | Mar 6 12:04 a.m. (same) | U |
| 20240309194502 | 11:45am Mar 9 | 93,100 (jump) | 100.0% | **Mar 8 4:52 p.m.** (new) | U |
| 20240311135917 | 5:59am Mar 11 | 93,100 (same) | 100.0% | Mar 8 4:52 p.m. (same) | U |

(*%Reporting column at 10:38pm still read 0.0% — that column tracks
precinct-level certification lagging the running ballot count; ballots cast
already showed 51,885 at that point.)

**This is a gold-standard plateau bracket per RUNBOOK 7.2/8:**
- Self-describing: the page's own "Last Report Date-Time" field for Placer
  reads **"Mar 6 12:04 a.m."** — squarely in the 1am-4am "still election
  night" window the runbook allows (here even earlier, just after midnight),
  and "% Reporting" had just hit 100.0% (170/170 precincts), consistent with
  the county's last report of the night.
- Non-circular leg #1: THREE later captures of the same URL (6:44am, 10:05am,
  7:52pm Mar 6, and again 7:51am Mar 8 — spanning 2.5+ days) show the
  identical frozen value (69,436, same "Last Report" timestamp) — proof
  nothing moved during the canvass pause.
- Non-circular leg #2: the report series' NEXT update is days later (Mar 8
  4:52 p.m., jumping to 93,100) — the classic "next file is days later"
  bracket proof.
Both legs independently satisfy CONFIRMED; this is doubly bracketed.

**RECOVERED VALUE: 69,436 ballots cast** (Placer's own SoS-reported "Ballots
Cast" column, last-report-stamped Mar 6 12:04 a.m. PST — within the plateau,
well after the 8pm first tranche which this same source shows was only
51,885 as of 9:54 p.m.).

vs certified final 135,869 (registrar's own "Cards Cast" / SoS SoV "Total
Voters", per dossier item 6): **69,436 / 135,869 = 51.11%**.

Sanity check vs RUNBOOK 1 calibration (SF ~57% in 2024 general, presidential
years read higher): 51.11% for a presidential PRIMARY (lower-salience,
lower-turnout election type than a general) is plausible — comparable to or
a bit below SF's general-election shares, and well above a "half of the
real number = first-tranche mistake" trap (the true first tranche here, per
the same source, was 51,885/135,869 = 38.2% at 9:54pm, and even that isn't
suspiciously low). Also plausible given the dossier's own flag that
Sign-Scan-and-Go might push this county's post-adoption share HIGHER than
its pre-adoption 62-70% range — 51% is actually LOWER, which is itself a
notable/counterintuitive finding worth flagging to the operator (in-person
Sign-Scan-and-Go ballots count live, but this was a low-in-person-turnout
primary with the VCA all-mail-ballot default likely dominating; 51% sits
below the pre-adoption baseline, suggesting Sign-Scan-and-Go did NOT
outweigh the general VCA/all-mail slowdown for this county, contrary to the
prior scout's hypothesis).

Primary evidence URLs (Wayback, `id_` raw form used for fetch; cite the
rendered form per repo convention):
- `https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status`
  (first capture showing the frozen night-final count, 69,436 / 100.0%
  reporting / Last Report Mar 6 12:04 a.m.)
- Bracket corroboration: `https://web.archive.org/web/20240308155126/https://electionresults.sos.ca.gov/returns/status`
  (still 69,436, 2.5 days later) and
  `https://web.archive.org/web/20240309194502/https://electionresults.sos.ca.gov/returns/status`
  (jumps to 93,100 with a NEW "Last Report: Mar 8 4:52 p.m.", proving the
  69,436/Mar-6-12:04am value was frozen until then).
- First-tranche control (NOT used as the plateau, cited only to show the
  8pm dump vs. plateau distinction): `https://web.archive.org/web/20240306063830/https://electionresults.sos.ca.gov/returns/status`
  (51,885 ballots, Last Report Mar 5 9:54 p.m.).

Raw fetch artifacts saved in this scratch dir for reproducibility:
`status_20240305190731.html` ... `status_20240311135917.html` (gunzipped
from the `id_` raw Wayback replies) and `sos_en_root_093348.html` (the
`electionresults.sos.ca.gov` root page that led to discovering
`/returns/status`).

Confidence class: **CONFIRMED** (self-describing timestamp + double
non-circular bracket, per RUNBOOK section 8). Source type: primary
(official CA SoS election-night reporting page, county-reported, distinct
from and independent of the county's own site — which is exactly the site
the task briefing predicted might hold this: "the CA SoS EN results site
archives per-county snapshots for statewide elections").

### Routes not needed (closed by the Route C recovery)
Not pursued further since Route C fully resolved the target with CONFIRMED
evidence: Gold Country Media/Auburn Journal, Sacramento Bee live-results,
KCRA, CapRadio, county FB/X, returns.sos.ca.gov (checked: CDX empty, this
predecessor domain has no 2024 captures — dead by the time of this
election), puppeteer/Cloudflare retry on placercountyelections.gov's own
live pages.

---

## RESULT

**RECOVERED.** Placer County 2024-03-05 Presidential Primary election-night
plateau: **69,436 ballots cast**, last-report-stamped Mar 6 12:04 a.m. PST,
against certified final 135,869 → **51.11%**. Evidence class: CONFIRMED
(double bracket proof). Source: CA SoS `electionresults.sos.ca.gov
/returns/status` per-county reporting table (Wayback captures, see table
above). This closes the panel's most consequential missing cell — Placer's
only post-e-pollbook/post-VCA/post-Sign-Scan-Go election-night observation.

### Draft row (section 2 schema) — for the operator to land
```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 69436,
  "certified_final": 135869,
  "election_night_pct": 51.11,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20240306144409/https://electionresults.sos.ca.gov/returns/status",
  "confidence": "primary",
  "note": "RECOVERED on retry via a route the prior pass had not tried: the CA SoS's own election-night reporting site electionresults.sos.ca.gov (distinct from the Incapsula-walled vote.sos.ca.gov; distinct from the county's own placercountyelections.gov, which per the prior pass has a one-month Wayback gap over the election-night window). Its /returns/status page is a plain-HTML per-county reporting-status table (County | Election Method | Total/Reporting Precincts | %Reporting | Registered Voters | Ballots Cast | %Turnout | First/Last Report Date-Time | Report Type) -- no JS rendering needed. Wayback captured this page repeatedly through election night and the following days. Placer's row: pre-close captures (11:07am, 6:40pm Mar 5) show 0; 10:38pm Mar 5 shows 51,885 ballots (Last Report 'Mar 5 9:54 p.m.', the 8pm-tranche-equivalent, correctly NOT used); the 6:44am Mar 6 capture shows 69,436 ballots, 170/170 precincts (100.0%) reporting, Last Report 'Mar 6 12:04 a.m.', Report Type 'U' -- this is the plateau. THREE further captures (10:05am and 7:52pm Mar 6, and 7:51am Mar 8 -- spanning 2.5+ days) show the identical frozen 69,436/Mar-6-12:04am state; the NEXT capture (11:45am Mar 9) jumps to 93,100 with a new Last Report stamp 'Mar 8 4:52 p.m.', proving the 69,436 value was genuinely frozen from election night until the next canvass update days later -- a double bracket proof per RUNBOOK 7.2/8 (frozen-later-capture leg AND next-file-is-days-later leg). Denominator = certified Total Voters 135,869 (registrar's own certified page: Cards Cast 135,869 48.33%; CA SoS SoV Total Voters 135,869/Registered 281,556, 48.26%). 69,436/135,869 = 51.11%. Note for interpretation: this is BELOW this county's pre-adoption primary range found elsewhere in this dossier (61.91% in 2016, 69.75% in 2012), which cuts against the hypothesis (flagged by the prior pass) that Sign-Scan-and-Go's live-counted in-person VBM scans would push the post-adoption election-night share higher; for this low-turnout presidential primary the all-mail VCA default appears to dominate instead. abc10.com's 2024-updates article (the prior pass's other lead) was confirmed via a clean (non-timeout) CDX query to have zero Wayback captures ever -- genuinely unrecoverable by that route, not a retry issue."
}
```

### Routes tried and outcomes (for the final report)
1. abc10.com CDX retry -- CLOSED, confirmed zero captures (not a timeout artifact).
2. vote.sos.ca.gov -- CLOSED, Incapsula-walled, all 503s, zero usable content.
3. returns.sos.ca.gov -- CLOSED, zero captures for 2024.
4. electionresults.sos.ca.gov root -- led to discovery of `/returns/status`.
5. electionresults.sos.ca.gov/returns/status -- **RECOVERED** (this is the answer).
