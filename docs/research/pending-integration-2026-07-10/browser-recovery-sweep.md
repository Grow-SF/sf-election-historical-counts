# Browser recovery sweep — 2026-07-10

Read-only recovery scout. Attacking every "FLAG for manual operator" item
found in scratchpad dossiers + committed data/research/election-night/*.json,
per RUNBOOK plateau semantics. Escalation order: curl -A UA -> repo puppeteer
renderers -> isolated throwaway Chrome -> Wayback/archive.today.

## Target list (built from grep, deduped, classified)

ATTACK NOW (Cloudflare/CloudFront/paywall-lite public sites):
1. fresno-ca.json 2018-11-06 general: gvwire.com, Fresno Bee (McClatchy) — curl 403, WebFetch blocked.
2. sacramento-ca.json 2016-11-08 general: sacbee.com (McClatchy) — curl/WebFetch blocked.
3. dossier-sacramento-ca-primaries 2014-06-03: sacbee.com search.
4. dossier-placer-ca-primaries (3 elections): placercountyelections.gov/past-elections-january-2011-to-november-2014/,
   /election-results/ (Cloudflare); abc10.com "where the vote stands so far" (2018p) and
   "2024 Election Updates" (2024p) (403 + CDX 504).
5. dossier-mendocino-ca (tech record): mendocinocounty.gov FAQ page (403 Cloudflare).
6. dossier-fresno-ca-primaries 2018p: re-open 2 Wayback captures to confirm GEMS header timestamps (archive.org, not walled — sanity check).
7. dossier-fresno-ca-primaries 2024p: fresnoland.org live text verify (not Cloudflare-listed — check).
8. dossier-napa-ca-primaries (2012p, 2014p): Wayback dtl page eyeball to confirm digit reads (archive.org, sanity check).
9. dossier-santa-clara-ca-primaries: web.archive.org/save/ for Clarity JSON numerator URLs; Wayback UI retry for June 2012 5-6 capture.
10. dossier-nevada-ca-primaries: Legistar SR 16-0825 (Nevada County board agenda system) — public gov site.
11. dossier-del-norte-ca-primaries: Google Drive PDF re-read (id=1xrb3b2Kmu...) to confirm digits; docs.google.com/viewer Google Groups doc.

CREDENTIAL-BOUND (list for human, do not attempt):
- sacramento-ca.json 2016-11-08: NewsBank/ProQuest Sacramento Bee archive as fallback.
- dossier-sacramento-ca-primaries 2014-06-03: NewsBank/ProQuest pull.
- dossier-santa-clara-ca-primaries 2012p: San Jose Mercury News via SFPL/NewsBank.

SKIP (not actually browser-block flags, or already resolved):
- dossier-del-norte-ca.md (general): CDX shows zero captures, genuinely unarchived, not a wall.
- dossier-colusa-ca.md: explicitly not a FLAG/browser-block situation.
- dossier-mendocino-ca-primaries.md: FLAGs are analytical-calibration asks (subtraction-derived numerator,
  outlier share, retrospective news citation) for a human sanity check, not blocked URLs.
- dossier-san-bernardino-ca-primaries.md: explicitly no browser needed.
- dossier-riverside-ca-primaries.md: explicitly no FLAG needed.
- dossier-san-diego-ca-primaries.md: FLAG is ASV-adoption-date ambiguity (records research), not a walled URL.

---

## Operational note

Mid-sweep, coordinator flagged that my first headful throwaway Chrome
(port 9223, default window position) was stealing the human's window focus.
Killed it and relaunched per coordinator's spec: `open -gjn -a "Google Chrome"
--args --remote-debugging-port=9223 --user-data-dir=/tmp/throwaway-chrome-hidden
--no-first-run --no-default-browser-check --window-position=-32000,-32000`
(the `-n` flag was required too -- without it `open -gj -a` just re-activated
the user's already-running Chrome instead of spawning a new one). Confirmed
via `ps aux` that only the new off-screen instance has `--remote-debugging-
port=9223`; the user's own long-running Chrome (pid 11427, launched Wed 3pm)
was never touched. All subsequent browser attempts below use this hidden
instance, connected via `puppeteer.connect({browserURL:'http://127.0.0.1:9223'})`.
Killed at the end of the sweep.

## Attempts log
(populated per item below)

### Continuation note (new session)

Resuming per the coordinator's instruction: HEADLESS ONLY this time, no
headful/off-screen Chrome at all (the prior session's off-screen-window
approach is retired). Tooling: `puppeteer-core@25.2.1` (already present in
repo root `node_modules/.pnpm`, symlinked at `node_modules/puppeteer-core`)
`.launch({headless: 'new', executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
args: ['--disable-blink-features=AutomationControlled','--no-sandbox']})`,
real desktop Chrome UA set via `page.setUserAgent(...)`. Script:
`scratchpad/pp_fetch.cjs`. This never creates a visible window (headless mode
has no window at all, on- or off-screen) and does not touch the user's Chrome
process. Also rebuilt the target list from this session's read of the prior
log's Step-1 inventory PLUS cross-checked `scratchpad/sos-status-sweep.md`
and the many `dossier-*-primaries.md` / `cell-*.md` files a concurrent
research effort had populated in this same scratch dir since the prior sweep
was killed — several original targets turned out to already be resolved
(RECOVERED or exhaustively KEEP-NULL/NOT-RECOVERED) by that other work and
are marked SKIPPED-ALREADY-FILLED below rather than re-attempted.

#### Item: Mendocino County ASV FAQ page — RECOVERED (headless bypass)

Original flag (dossier-mendocino-ca.md item 0, ASV note): county's Ballot
Information FAQ page 403s to curl/WebFetch (Cloudflare), confidence stuck at
"low" (WebSearch-snippet only).

1. curl -A `<realUA>` on the URL cited in the dossier's `evidence_url`
   (`mendocinocounty.gov/government/assessor-county-clerk-recorder-elections/elections`)
   → **HTTP 403** (confirms the wall).
2. Headless-"new" puppeteer fetch of that same URL → HTTP 200, but it's the
   general Elections landing page, not the specific FAQ subpage; no
   "signature"/"verifies" content on it (the dossier's evidence_url was
   imprecise, not the actual FAQ document).
3. WebSearch for the exact quoted sentence from the dossier's WebSearch-snippet
   version ("if the Elections Official verifies the signature, the challenge
   is removed") surfaced the REAL source: `https://www.mendocinocounty.gov/Home/Components/News/News/6964/4035?arch=1`
   ("Mendocino County Registrar of Voters Ballot Information 2024 - FAQs").
4. Headless-"new" puppeteer fetch of that URL → **HTTP 200**, full page
   content recovered (118,506 bytes). Extracted the passage directly (more
   context than the WebSearch snippet had):

   > "...the address scanned and the file is uploaded into the elections
   > management system. If a challenge code comes up in the election
   > management system, the ballot is put aside for the elections official to
   > review. **Additionally, Elections Office staff check the signature on
   > each ballot envelope by hand.** If there is a discrepancy in the
   > signature it is challenged in the elections management system and
   > brought to the Elections Official for signature verification. If the
   > Elections Official verifies the signature, the challenge is removed, and
   > the ballot is filed by precinct to be opened and counted. If the
   > signature does not match the Elections Office contacts the voter to
   > re-sign and/or complete a new registration form, as a person's signature
   > may change over time."

   The "by hand" phrase (not present in the WebSearch snippet used for the
   dossier's original "low" confidence note) is direct, unambiguous
   confirmation of human (not automated) signature review, from a primary
   source now directly read past the wall.
5. Attempted `https://web.archive.org/save/<url>` to pin a permanent Wayback
   snapshot: **HTTP 520** (Wayback's save-page-now service errored; CDX
   confirms no snapshot landed — `cdx?url=mendocinocounty.gov/Home/Components/News/News/6964/4035` → `[]`).
   This matches the flaky `web.archive.org` connectivity already documented
   elsewhere in this scratch dir (santa-clara/nevada primary dossiers); not a
   Cloudflare issue, a Wayback-side transient. Live fetch stands as the
   evidence; a re-save attempt later would still be worthwhile.

**RECOVERED.** Upgrade recommendation for `data/research/county-tech/mendocino-ca.json`'s
`asv` tech record: raise `confidence` from `low` to `secondary` (direct
primary-source page read past the Cloudflare wall, still secondary rather
than `primary` per RUNBOOK 5.3 since the FAQ is explanatory prose, not a
technical spec sheet), `evidence_url` corrected to
`https://www.mendocinocounty.gov/Home/Components/News/News/6964/4035?arch=1`
(the dossier's originally-cited URL was the wrong page). Quote for the note:
"Elections Office staff check the signature on each ballot envelope by hand"
— confirms manual/human signature review, no ASV vendor.

#### Item: Placer County Cloudflare-gated live pages (2014-06-03 primary flag) — BYPASSED, CONFIRMS NULL (no new data)

Original flag (dossier-placer-ca-primaries.md item 2, 2014-06-03): the live
`placercountyelections.gov/past-elections-january-2011-to-november-2014/`
and `.../election-results/` pages 403 to curl/WebFetch; dossier used a 2022
Wayback snapshot of the first page instead (linking the same document
directory it had already CDX-enumerated) and left the numerator null.

1. curl -A `<realUA>` on both URLs → **HTTP 403** confirmed on both.
2. Headless-"new" puppeteer fetch of both → **HTTP 200** on both (214,245
   bytes / 119,775 bytes). Bypass succeeded.
3. Grepped the live `past-elections-january-2011-to-november-2014` page for
   every `06032014/` (the June 3, 2014 primary's document folder) link: 24
   files, byte-for-byte the SAME set the dossier's Wayback-CDX enumeration
   already found (pre-election notices/calendars, `06032014_SOV.txt`,
   `06032014_SOV_Totals By District.pdf`, `06032014_Certifications.pdf`, and
   `06032014_Fiinal_Results.pdf` [sic, the county's own typo] — the OFFICIAL
   FINAL canvass PDF already examined by the dossier). **No interim/semi-final/election-night-dated
   report exists in this folder on the LIVE site either** — the live listing
   is not more complete than the 2022 Wayback capture the dossier used.
   `election-results/` (the second URL) carries zero 2014-dated links at all
   (it's the current-cycle results page only).

**Bypass succeeded technically (Cloudflare no longer blocks this route with
headless-"new"), but it changes nothing substantively: this independently
confirms, via a second/live method rather than only the 2022 Wayback
snapshot, that Placer's June 2014 primary document directory genuinely has
no election-night artifact.** The dossier's NULL verdict for 2014-06-03
stands, now with stronger evidence (live-site confirmation, not just one
Wayback capture). No change to the draft row.

#### Item: Placer County 2018-06-05 primary numerator (abc10.com "where the vote stands so far") — STILL-BLOCKED (genuinely unarchived, not a wall)

Original flag (dossier-placer-ca-primaries.md item 4, 2018-06-05): abc10.com
"Placer County Primary Election Results: Where the vote stands so far" 403s
to curl and has zero Wayback captures for the article the dossier had
identified.

1. Headless-"new" bypass of the sibling Cloudflare-gated Placer page **"Past
   Elections May 2016 to November 2018"** (`placercountyelections.gov/past-elections-may-2016-to-november-2018/`,
   not previously checked by name in the dossier) → HTTP 200. Its
   `06052018/` document folder link list is IDENTICAL in character to the
   already-CDX-enumerated one: 30 files, all pre-election notices plus
   **`06052018_Final_Results.pdf`** (a file not in the dossier's prior CDX
   enumeration). Fetched it directly (curl, HTTP 200, 64,625 bytes,
   `pdftotext`): header "PLACER COUNTY OFFICIAL ELECTION SUMMARY JUNE 5, 2018
   **FINAL** Date:07/02/18 Time:09:56:27 ... Cards Cast 109097 48.72%" — the
   CERTIFIED FINAL canvass (109,097 = certified total exactly, dated July 2,
   4 weeks post-election). Not a new lead; confirms (via a document the
   dossier hadn't examined) that only the pre-election batch and the final
   canvass exist in this folder, no interim report.
2. WebSearch for the specific abc10 2018 article surfaced two DIFFERENT
   abc10 article IDs referencing Placer County results, neither the 2018
   primary: `103-856867fa-...` (CDX: captures dated 2024-03-05, i.e. the
   2024 PRIMARY — already independently RECOVERED via the SoS route in
   `placer-2024-03-retry.md`, not needed here) and `103-32f1bf95-...` (CDX:
   one capture dated 2022-11-09, the Nov 2022 GENERAL, out of scope for this
   primaries dossier).
3. No 2018-06-05-dated abc10 article URL was found by WebSearch beyond the
   one already known to the dossier (zero Wayback captures, confirmed
   unchanged).

**STILL-BLOCKED / genuinely unarchived** — this is not a bot-wall problem
(curl 403 was never the real obstacle; headless bypass works fine on this
domain, as shown by the sibling-page and 2024/2022-article successes above)
but a "Wayback never crawled this specific 2018 URL" problem, and the live
2018-era article no longer resolves to retrievable content (abc10 recycles
its CMS article-ID space; no live URL for the exact 2018 headline was
located). No change to the dossier's NULL verdict for this row.

#### Item: Santa Clara County primaries — Wayback permanence for 5 live Clarity numerator URLs — RECOVERED (all 5 archived)

Original flag (dossier-santa-clara-ca-primaries.md, "evidence-permanence
caveat", items 2-6, 2014/2016/2018/2022/2024 primaries): all 5 numerators
were verified live (curl --compressed -A UA, no bot wall on this CDN — the
dossier itself notes UA presence, not headless-vs-headed, is what matters
here) but `web.archive.org/save/` never completed in that session due to
flaky sandbox connectivity to web.archive.org (unrelated to the Clarity CDN
itself, which was reliable).

Not a bot-wall item technically (no Cloudflare/CloudFront block on this
route) but explicitly listed as an ATTACK-class target in the Step-1
inventory ("web.archive.org/save/ for Clarity JSON numerator URLs"), so
attempted here as a mechanical retry with plain `curl -A <UA> https://web.archive.org/save/<url>`
(no puppeteer needed):

| Election | Clarity URL | save/ result | CDX-confirmed snapshot |
|---|---|---|---|
| 2014-06-03 | `.../51635/132035/json/sum.json` | 302 | `20260710205734`, 200, `application/json` |
| 2016-06-07 | `.../60535/171284/json/sum.json` | 302 | `20260710205905`, 200 |
| 2018-06-05 | `.../75369/204514/json/sum.json` | 302 | `20260710210752`, 200 |
| 2022-06-07 | `.../113941/295160/json/sum.json` | 302 | `20260710220033`, 200 |
| 2024-03-05 | `.../120250/331698/json/sum.json` | 429 (rate-limited), retried after 20s → 302 | `20260710220123`, 200 (a pre-existing 2024-03-06 crawl was also already on file) |

All 5 confirmed landed via CDX lookup after the save. Spot-verified one
payload's content: fetched
`https://web.archive.org/web/20260710205734id_/https://results.enr.clarityelections.com/CA/Santa_Clara/51635/132035/json/sum.json`,
gunzipped, parsed JSON — `Contests[0].BC = 166360`, `Contests[0].C =
"GOVERNOR"` — exact match to the dossier's claimed 2014-06-03 plateau value.

**RECOVERED (archival permanence, not new data).** All 5
`source_url_night` values in the dossier's draft rows should be swapped from
the live Clarity CDN URL to the corresponding
`https://web.archive.org/web/<ts>/<url>` snapshot cited above, matching the
pattern used for this county's other Clarity rows already in
`santa-clara-ca.json`. The dossier's numerator VALUES were already correct
(verified live); this closes the sole remaining "evidence-permanence FLAG"
on all 5 CONFIRMED primary rows (2014/2016/2018/2022/2024).

#### Item: Del Norte County 2014-06-03 primary numerator (docs.google.com/viewer alternate route) — STILL-BLOCKED (dead Google service, credential wall not a Cloudflare wall)

Original flag (dossier-del-norte-ca-primaries.md item 2, 2014-06-03): the
PDF bytes behind the county's old Google-Sites-hosted "Release 2" (the
timing-bracketed but unreadable plateau candidate, upload epoch 2014-06-03
22:08:09 PDT) are unrecoverable via the normal `sites.googlegroups.com`
signed-redirect host (CDX returns only tiny `warc/revisit` stubs); the
dossier flagged the index page's alternate `docs.google.com/viewer?a=v&pid=sites&srcid=...`
"View" links as untried, requiring an interactive Google Docs viewer render.

1. Fetched the Wayback-archived June-2014-primary index page directly (plain
   curl, not Cloudflare-walled) and extracted all 3 `docs.google.com/viewer`
   links (one per attachment: Final, Release 1, Release 2).
2. CDX for the Release-2 viewer URL shows a real 200-status capture
   (`20140825122340`, 19,210 bytes, `text/html`) — fetched it directly: it is
   a bare "Google Drive Viewer" JS-app shell with no embedded page-image URLs
   or extractable text (old Google Docs Viewer rendered PDF pages via a
   client-side JS canvas API, not present in the static archived HTML).
3. Headless-"new" puppeteer fetch of the LIVE viewer URL: the page's own JS
   redirects to `accounts.google.com/ServiceLogin?passive=1209600&continue=https://docs.google.com/viewer?...`
   — i.e. the old Google-Sites document-viewer backend for this vintage of
   `srcid` now requires a signed-in Google account and no longer serves
   anonymous/public content at all (the service has been retired/gated since
   2014). This is a genuine authentication wall, not a headless-vs-headed or
   Cloudflare-style block — no UA or bypass technique defeats a real Google
   login redirect.

**STILL-BLOCKED (credential wall, effectively CREDENTIAL-BOUND despite not
being NewsBank/ProQuest)** — reclassifying this specific lead: it cannot be
closed by any ATTACK-class technique (curl, headless-new puppeteer, or
Wayback); it would need an authenticated Google session, which is out of
scope for this sweep. The dossier's timing-bracketed-but-unreadable NULL
verdict for 2014-06-03 stands.

Note on the sibling lead in the same dossier item (2018-06-05, Del Norte's
mislabel-resolution FLAG for a human eyeball of
`https://drive.google.com/uc?export=download&id=1xrb3b2KmuaR0EhVysw--eKyjXANMzy6k`):
NOT re-attempted here — that FLAG is explicitly a "please eyeball my
transcription" human-verification-loop ask (the digits were already read by
the dossier author from a rendered PNG; the ask is for independent human
confirmation, not a blocked source), out of scope for a bot-wall recovery
sweep. Left for the human per the existing FLAG.

---

## Sweep summary (this session)

Scope actually covered: the genuine ATTACK-class (Cloudflare/CloudFront
public-site) walls from the Step-1 inventory, plus the one purely-mechanical
Wayback-permanence item explicitly listed alongside them. Sanity-check items
(re-opening already-read Wayback captures to eyeball digits/timestamps —
Fresno 2018p/2024p, Napa 2012p/2014p, Del Norte 2018p) were left for the
human per the human-verification-loop convention; they were never
bot-walled to begin with.

No headful/visible Chrome was ever launched; all fetches used
`puppeteer-core` + system Chrome with `headless: 'new'` (no window, on- or
off-screen) or plain `curl`. No user-facing process was touched.

#### Item: Sacramento Bee 2014-06-03 primary coverage — STILL-BLOCKED / exhausted (route dead end, not a wall)

Original flag (dossier-sacramento-ca-primaries.md item 2, 2014-06-03,
route 6): sacbee.com not exhaustively re-run for this specific election;
"FLAG for manual operator: a human search of sacbee.com's own archive or a
NewsBank/ProQuest pull... could still recover the true election-night
total."

1. Live `sacbee.com` 403s to curl with a real UA (consistent with the
   already-confirmed cell-sacramento-2016.md finding for the same domain).
2. CDX prefix sweep of `sacbee.com/news/politics-government/election/` for
   the June 3-7, 2014 window (the same section path that worked for the 2016
   general-election KEEP-NULL pass): **zero captures** — Wayback never
   crawled this section during the June 2014 primary week at all (unlike
   2016, which had ~170 crawled URLs in that section for its own election
   week).
3. WebSearch for a Sacramento Bee June 2014 primary ballots/turnout article:
   surfaced only the CA SoS results page, current-cycle county portals, and
   a 2026-dated NewsBreak/SacBee syndication piece (contamination) — no 2014
   article.

**STILL-BLOCKED, exhausted** — this is a "Wayback never crawled it" dead
end, same pattern already independently confirmed for 2012 (item 1 of this
same dossier) and 2016 (cell-sacramento-2016.md). ATTACK-class routes
(curl+UA, headless bypass — moot since there's no captured content to
bypass toward, and no live URL was ever identified either) are exhausted.
The remaining lead is genuinely CREDENTIAL-BOUND (NewsBank/ProQuest
Sacramento Bee archive), as the dossier itself already anticipated. No
change to the dossier's CEILING-only verdict for this row.

#### Item: Nevada County Legistar SR 16-0825 — SKIPPED-ALREADY-FILLED (never actually walled)

Sanity-checked per the original Step-1 inventory item 10. `curl -A <UA>
https://nevco.legistar.com/LegislationDetail.aspx?GUID=F2AD1997-3E3E-4C30-80F7-21F54318ADDF&ID=2840587`
→ **HTTP 200** directly, no wall at all. This was never a browser-block
situation (the dossier author already fetched and quoted it directly); it
was miscategorized as an ATTACK target in the prior log's inventory. No
action needed.
