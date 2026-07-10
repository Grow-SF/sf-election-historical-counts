# Gap-fill triage, 2026-07

Triage of the 17 null/ceiling election-night cells listed in Task 5 of the
county panel expansion, per `docs/research/RUNBOOK.md` sections 5, 6, 7, 8.
A read-only scout drafted an initial classification (7 RE-RESEARCH, 16
KEEP-NULL, 1 documentation-hygiene-only); this memo is the verified,
final record after independently re-running or spot-checking every call.
One line per cell below; RECOVERED cells carry the new value + evidence
class, KEEP-NULL cells carry the dead-end reason, quoting or summarizing
the row's note.

Full research narratives (commands run, values found, archived+verified
snapshot URLs) live in the row notes themselves (`data/research/election-night/<slug>.json`)
and in per-cell scratch files under the session scratchpad; this memo is
the index, not the primary evidence trail.

## RECOVERED (4 cells)

- **santa-clara-ca 2016-11-08**: RECOVERED, 443,269 / 724,596 = **61.17%**,
  confidence **primary**, plateau **CONFIRMED**. Route: the live Clarity CDN
  (electionId 64404), not Wayback. curl and puppeteer-with-`headless:true`
  both 403 on this CDN (CloudFront block); puppeteer with `headless:"new"` +
  a real desktop Chrome UA bypasses it. Wayback never crawled the JSON for
  the Nov 8-9 versions, but the live CDN still serves it; candidate version
  numbers were harvested from a wide-window Wayback CDX sweep (which *did*
  crawl the HTML shells) and walked on the live CDN. Plateau = v182800
  (11/9 10:28:40 AM PST), the last of a continuous ~hourly overnight
  sequence; the next version breaks cadence 5h13m later with a
  4x-collapsed increment. Snapshot archived and verified:
  `https://web.archive.org/web/20260710174832/https://results.enr.clarityelections.com/CA/Santa_Clara/64404/182800/json/sum.json`.
- **santa-clara-ca 2018-11-06**: RECOVERED, 304,303 / 625,425 = **48.66%**,
  confidence **primary**, plateau **CONFIRMED**. Same live-CDN route,
  electionId 92418 (Web02 SPA, which does carry a versions array unlike the
  Web01 2016/2014 elections). Plateau = v220444 (11/7 6:37:33 AM PST, all
  1,098 precincts reported); the immediately next official version
  (v220630, 9h22m later) shows only a +1,783 increment. Snapshot archived
  and verified:
  `https://web.archive.org/web/20260710173809/https://results.enr.clarityelections.com/CA/Santa_Clara/92418/220444/json/sum.json`.
- **santa-clara-ca 2014-11-04** (was a documented ceiling, 251,620,
  comparable=false): RECOVERED true plateau, 235,062 / 404,166 = **58.16%**,
  confidence upgraded secondary->**primary**, `comparable=false` REMOVED,
  plateau **CONFIRMED**. Same live-CDN route, electionId 54209 (Web01).
  This is the exact version (147908, 11/5 4:00:59 AM PST) the prior note
  already named as "the true overnight plateau" while treating it as
  unrecoverable; the live CDN still serves it. Pace collapses to +624 in
  the final 63-minute step, then a 13-hour gap to the old ceiling version
  (148095). Snapshot archived and verified:
  `https://web.archive.org/web/20260710175200/https://results.enr.clarityelections.com/CA/Santa_Clara/54209/147908/json/sum.json`.
- **nevada-ca 2024-11-05** (documentation hygiene, not a research gap):
  the row's `flag` field carried a stale caveat ("the true end-of-night
  plateau could not be independently confirmed") that the row's own note
  had already resolved via the county's three dated Cumulative Results
  PDFs (15,486 confirmed as the LAST of three election-night reports).
  Appended a dated CORRECTION sentence to the flag per runbook 2/5.4
  (append-only, did not rewrite history). No numeric value changed; the
  row remains comparable=false (ink-overspray paper-defect exclusion,
  still valid and undisturbed).

## KEEP-NULL after re-research attempt (3 cells)

- **sacramento-ca 2016-11-08**: attempted the scout's proposed bypass
  (curl the Wayback-archived copy of Sacramento Bee articles instead of
  the live-blocked host). CDX-swept ~190 distinct sacbee.com election
  articles from Nov 8-12 2016; checked the dozen earliest-crawled titles
  (all national election coverage or off-topic local pieces, none states a
  Sacramento County ballot total). The registrar's own current "Archived
  Elections" page 301-redirects into the modern homepage (no historical
  index survives the CMS migration). Route exhausted; value remains null.
- **fresno-ca 2018-11-06**: the bypass works technically (both the ABC30
  and GV Wire leads fetch cleanly via their Wayback-archived copies) but
  both turn out to be day-after canvass framings, not election-night
  reports (ABC30 dateModified Nov 7 8:57 PM PST, ~29h post-poll-close,
  "next update Friday 3pm"; GV Wire datePublished Nov 9 5:49 PM PST, 3 days
  post-election). No same-night article with a specific count was found.
  Value remains null.
- **fresno-ca 2012-11-06**: tried the press-release/news routes not
  previously checked for this year. The live current county results page
  links zero PDFs; a wider CDX sweep of co.fresno.ca.us/2850/ beyond the
  already-dead Results/ subfolder finds only the poll-place locator tool
  (confirmed by reading two of its pages directly), not a results report.
  WebSearch surfaced no news article with a figure. Value remains null.

## KEEP-NULL, routes confirmed exhausted (17 cells)

Spot-checked directly against each row's JSON note (not just the scout's
summary); all quoted dead-end evidence matches the underlying files
verbatim. No re-research attempted (no untried route existed per runbook
6.1-6.7 and 7.2's Clarity/puppeteer techniques).

- **riverside-ca 2012, 2014, 2016, 2018**: non-Clarity Sequoia "eresults"
  system (voteinfo.net); zero Wayback captures near election night in any
  of the four years (CDX confirmed empty or post-canvass only), and the
  registrar's own press-release archive holds no morning-after
  "semi-official results" release in any year. 7.2's Clarity techniques do
  not apply to a non-Clarity vendor; nothing archived to render via 7.4.
- **san-bernardino-ca 2012, 2014, 2016, 2018**: non-Clarity JS-iframe
  results.aspx system; every year's earliest Wayback capture of the
  results iframe is POST-CANVASS (Nov 7 2014, Nov 18 2016, Nov 12 2018) or
  nonexistent (2012), and the registrar issued no election-night
  press release across all four years. Same "not a Clarity county, nothing
  archived to render" logic as Riverside.
- **san-diego-ca 2012, 2014, 2016**: San Diego did not adopt
  livevoterturnout.com (its Clarity-adjacent ENR) until 2018; pre-2018 the
  live page was a JS viewer over an XML feed (sdvote.com/.../election.xml)
  that Wayback never captured on election night in any of the three years,
  and the registrar's own news page has no Wayback presence before 2019.
  Press-release route independently checked and empty for all three years.
- **fresno-ca 2014-11-04**: official-page CDX dead end (only the Nov 20
  canvass HTM and Nov 26 Official Final PDF are archived; nothing near
  election night) AND the news route was checked (unlike 2012) with no
  election-night total found. Both routes exhausted, unlike 2012/2018 where
  only one route had been tried before this pass.
- **fresno-ca 2022-11-08**: the live results page only ever embedded the
  Dominion ZERO REPORT in both its archived captures; the JS/ENR widget
  that carried the real numbers was never crawled, so nothing exists for
  7.4 puppeteer to render. News (Fresnoland, ABC30) gave only
  wrong-denominator or day-after framings. Hundreds of archived county PDFs
  from that week were enumerated; none is an election-night results
  report.
- **madera-ca 2012-11-06**: predates Madera's Clarity ENR entirely (first
  Clarity election is June 2018) and predates its WordPress results
  system (earliest votemadera.com results-folder capture is Nov 2014). No
  results page, canvass PDF, or news total exists for this year at all.
- **madera-ca 2014-11-04**: the only archived votemadera.com result state
  (Nov 7/18 2014 captures) is explicitly labeled the FIRST CANVASS UPDATE
  (Friday 11/7 afternoon), not the election-night semifinal; CDX confirms
  zero captures before that timestamp. No 2014 Clarity electionId existed
  yet (Madera's first Clarity is 2018), so the live-CDN technique that
  recovered the Santa Clara cells above does not apply here.
- **placer-ca 2012-11-06**: a full CDX sweep of the entire Nov 2012 window
  returns exactly one capture (the Dec 1 2012 Official Election Summary,
  172,757) -- already examined and correctly rejected as post-canvass. Not
  a Clarity county in 2012 (GEMS); nothing else was archived to render.
- **placer-ca 2022-11-08**: a thorough 2026-06 re-verification pass covered
  the results page (no capture until Nov 18, past the plateau), the
  registrar home page (landing-page only), the abc10 live article (JS
  widget never archived), and the full election-week document directory
  (certified-final and late-unprocessed-ballot reports only, no
  election-night report). Not a Clarity county in 2022 either.

## Forward note: Placer post-2024 (not a research gap)

Per the task brief, Placer's post-e2024-adoption period in the county-tech
comparison needs a Nov-2026-general election-night row, which does not yet
exist because that election has not happened as of this triage (2026-07).
This is a scheduling gap, not a research gap: nothing to re-research today;
revisit after the Nov 2026 general is certified.

## Net effect on the panel

- New pre-adoption points added: Santa Clara 2016, 2018 (both pre-e2020),
  and Santa Clara 2014 upgraded from a non-comparable ceiling to a
  comparable plateau point. Riverside, San Bernardino, and San Diego's
  pre-adoption periods remain contributing 0 points (all four/three/three
  candidate cells in each county are genuinely unrecoverable, not
  under-researched).
- No cells flipped from RECOVERED back to null; no comparable=false flags
  added or removed except Santa Clara 2014 (removed) and the nevada-ca 2024
  flag-text hygiene edit (no comparable-status change).
