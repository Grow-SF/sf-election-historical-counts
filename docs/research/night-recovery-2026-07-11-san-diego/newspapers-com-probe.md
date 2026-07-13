# Probe: does SFPL provide Newspapers.com access, and can it recover the San Diego Union 1922-1990?

Status: DONE. Verdict: SFPL does not provide Newspapers.com access (no ezproxy entry
exists); this route does not recover the San Diego Union 1922-1990 gap. See RECOMMENDATION
at the bottom.

## Background

- CDNC blocks some 1930s-40s issues behind a "available 23 September 2026 ... available now at newspapers.com" lock screen.
- CDNC does not digitize the San Diego Union after 1922, leaving 1922-1990 mostly dark for this project.
- Hypothesis: SFPL's ezproxy (same one used for NewsBank) also fronts a Newspapers.com subscription (commonly "Library Edition") that could fill this gap.

## Task 1: does SFPL list Newspapers.com in its databases A-Z?

**Answer: NO. SFPL does not offer Newspapers.com (Library Edition or full) in any form, remote or in-branch.**

Method: SFPL's `/databases` page is a Drupal Views listing with an A-Z exposed filter
(`sfpl_az_filter=<letter>`) and a topic filter (`resource_topics_target_id`). Queried:

- `https://sfpl.org/databases?sfpl_az_filter=N` and `&page=1` (all "N" entries, 2 pages x
  10 items): no "Newspapers.com" entry. Present instead: **Newspaper ARCHIVE - United
  States Collection** (newspaperarchive.com, a *different* company/product), **Newspaper
  Source Plus (EBSCO)**, **Newspaper Clipping Files (SFPL)** (in-house vertical file, not
  a digitized-image database).
- `https://sfpl.org/databases?sfpl_az_filter=A&page=1`: **Ancestry Library Edition
  (ProQuest)** is the only Ancestry-family product. Its link (`https://ancestrylibrary.proquest.com`)
  is a bare institutional URL, NOT an `ezproxy.sfpl.org/login?url=...` wrapper like every
  other remote database on the page. This is the standard tell for **Ancestry Library
  Edition's industry-wide licensing restriction: IP-authenticated, in-branch use only, no
  ezproxy/remote access.** Newspapers.com is a sister product under the same Ancestry
  corporate umbrella but is not separately listed at all.
- `https://sfpl.org/databases?resource_topics_target_id=636&items_per_page=50` (topic =
  "History & Genealogy", all 40 items on one page, no further pagination): full list
  reviewed line by line, no Newspapers.com. Full list included ProQuest Historical
  Newspapers titles (see Task-1-alternatives below).
- SFPL site search `https://sfpl.org/search?keys=newspapers.com` silently redirects to the
  BiblioCommons *book catalog* search (`sfpl.bibliocommons.com/?keys=newspapers.com`,
  gated behind a patron login wall) rather than any article-database result — i.e. the
  site's own search treats "newspapers.com" as a title string to look up in the catalog,
  not as a known database name. Confirms there is no LibGuide/database-page reference to
  it either.

Raw HTML saved for the record: `/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/sfpl_db_N.html`,
`sfpl_db_N1.html`, `sfpl_db_A.html`, `sfpl_db_A1.html`, `sfpl_db_genealogy.html`,
`sfpl_sitesearch_npc.html` (job tmp dir, not in repo).

### Alternatives SFPL does offer that touch San Diego / historical newspapers

From the "History & Genealogy" topic listing (40 items, reviewed in full):

| Database | ezproxy URL pattern | Relevance |
|---|---|---|
| Historical Newspapers: U.S. West Collection (ProQuest) | `ezproxy.sfpl.org/login?url=https://www.proquest.com/hnpuswest/fromDatabasesLayer?accountid=35117` | Named for the region SD is in — needs a title-coverage check (Task 1b below) |
| West Regional Historical Newspapers (ProQuest) | `ezproxy.sfpl.org/login?url=https://search.proquest.com/hnpuswest/index?accountid=35117` | Same underlying ProQuest product code (`hnpuswest`) as above, likely a duplicate/legacy catalog entry |
| California Historical Newspapers (NewsBank) | `ezproxy.sfpl.org/login?url=https://infoweb.newsbank.com/apps/news/source-list?p=EANX-NB` | Different NewsBank product code (EANX-NB) than the `WORLDNEWS`/AMNEWS product already used for SF Chronicle recovery — worth a separate title check, but NewsBank's own persistent SD Union gap (post-1922 through ~1970) is already known from prior recovery work |
| Ancestry Library Edition (ProQuest) | none (in-branch only, IP-gated) | Not usable remotely; also does not include Newspapers.com content even in-branch (separate Ancestry product) |

Checked `hnpuswest` (ProQuest "Historical Newspapers: U.S. West Collection") and
`EANX-NB` (NewsBank "California Historical Newspapers") — see Task 1b below.

### Task 1b: do SFPL's two alternative historical-newspaper products cover the San Diego Union?

**NewsBank "California Historical Newspapers" (product code `EANX-NB`) — NO.** Followed
`https://ezproxy.sfpl.org/login?url=https://infoweb.newsbank.com/apps/news/source-list?p=EANX-NB`
via the CDP fetcher (session was still authenticated from the earlier NewsBank recovery
work). The A-Z Source List returns exactly **17 sources, all San Francisco/Oakland-area
19th-century papers**: Alta California (1850-1861), American Sentinel, California Farmer
and Journal of Useful Sciences, California Star, Daily Commercial News, Daily Globe, Daily
Placer Times and Transcript, Evening Post, Mercantile Gazette and Prices Current, Oakland
Daily Transcript, Prices Current and Shipping List, San Francisco Abend Post, San
Francisco Bulletin, **San Francisco Chronicle (1865-2017)**, San Francisco Evening
Journal, plus 2 more of the same type. No San Diego title of any kind. Saved:
`/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/eanxnb_sourcelist.html`.

**ProQuest "Historical Newspapers: U.S. West Collection" (`hnpuswest`) — NO, confirmed by
in-database title search.** Logged into the ezproxy session fresh (see re-auth note
below), landed on the authenticated ProQuest UI banner reading "Access provided by SAN
FRANCISCO PUBLIC LIBRARY" (screenshot:
`/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/hnpuswest_after_login.png`). Used the
product's own "Publications" title-search box (`#pubSearchTerm`) to search **"San
Diego" (In title) → "Your search for San Diego found 0 publications."** (screenshot:
`/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/hnpuswest_sandiego_search.png`). Sanity-checked
the search mechanism with a **"Los Angeles" control query** (also 0 — see control-test
note below for why that's expected, not a broken search).

**Re-auth note:** the SFPL ezproxy session for the ProQuest/EBSCO/Gale side had in fact
dropped by the time of this probe (redirected to the "Articles and Databases -
Authentication" barcode/PIN form). Re-authenticated using the operator-provided SFPL card
credentials per this task's authorization; credentials were read from environment
variables at call time and never written to any file. One early re-login attempt hung
indefinitely (`Runtime.callFunctionOn timed out`) because the background tab's JS main
thread was frozen by Chrome's background-tab throttling; fixed by adding
`Emulation.setFocusEmulationEnabled` + `Page.setWebLifecycleState: active` to the tab
before typing/clicking (same trick already used in `cdp_fetch.js`/`cdnc_shot.js` for
CDNC, just not carried over to this new login script). Working script saved at
`/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/ezproxy_nav.js` for reuse.

**Control test:** the "0 publications" result for "San Diego" could in principle mean the
title-search box itself was broken. Ruled that out two ways: (a) resetting to the full,
unfiltered list (`hnpuswest_fulllist.html`) shows this product actually contains only
**94 titles total**, and they are small/mid regional papers under a Gannett Media Corp
umbrella deal — Tulare Advance-Register, Salinas Californian, St. George (UT) Spectrum,
Redding Courier-Free Press, Reno Nevada State Journal, an 1865-1889 San Francisco *Daily
Examiner*, etc. — not the major-metro titles (no LA Times, no SD Union/Union-Tribune;
those are separately-licensed ProQuest products, and SFPL only carries LA Times, NYT, and
SF Chronicle/Examiner separately). (b) A same-mechanism "Los Angeles" title search also
returned 0 (screenshot `hnpuswest_la_search2.png`), consistent with (a) rather than a
search bug. So `hnpuswest`'s name ("U.S. West Collection") is misleading — it is a
regional-paper bundle, not a big-metro collection, and San Diego is absent by design, not
by a query error.

## Other libraries checked for Newspapers.com or equivalent (per operator's fallback instruction)

- **California State Library** (`https://www.library.ca.gov/services/online-resources/`,
  fetched directly — WebFetch got a 403/WAF block, so used the CDP browser instead):
  DOES list two Newspapers.com products —
  **"Newspapers.com California Collection"** (860+ CA newspapers, 1848-2020) and
  **"Newspapers.com UC Riverside collection"** (500+ CA papers, the same underlying CDNC
  partnership) — but **both are tagged "For State Employees"**, and the UC Riverside one
  is additionally marked **"On-Site Access Only."** Neither is available to the general
  public remotely, so this is not usable for our purposes (we are not CA state employees,
  and even that population can't get the UC Riverside collection off-site). Separately,
  the state library's CDNC access note repeats the same "3-year embargo when accessing
  offsite" language we already know from CDNC itself — no new route around it.
  Source page saved at `/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/cslib_online_resources.html`.
  (Note: an AI web-search summary along the way asserted CSL's Newspapers.com had a
  "3-year embargo offsite" with no state-employee restriction; that claim did not match
  the actual page text and was discarded as a hallucination — the real page text is quoted
  above.)

- **San Diego Public Library eLibrary** (`https://www.sandiego.gov/public-library/elibrary`):
  No Newspapers.com. Does carry **San Diego Union-Tribune (NewsBank)** remotely, but
  explicitly scoped to **"Current and back issues (starting January 1, 2019)"** — no help
  for the 1922-1990 gap. Also offers LA Times (ProQuest, 1985-present), NYT Historical
  (1851-2014, doesn't cover SD), and Gale Newsstand/ProQuest Global Newsstream (current
  papers only). Microfilm of the San Diego *Tribune* (the afternoon paper, a different
  masthead from the *Union*) is available but **in-branch only** at the Central Library.

- **San Diego County Library / other SD-area library systems** (via UCSD LibGuide
  `https://ucsd.libguides.com/newspapers/area-public-libraries`): same pattern — SD
  Union-Tribune via NewsBank remote access (current-era only), PressReader (current
  issues only). No Newspapers.com listed at San Diego Public Library, San Diego County
  Library, Carlsbad, Chula Vista, Coronado, or Escondido public libraries.

**Conclusion: no public library card (SFPL, San Diego-area, or California State Library)
grants remote Newspapers.com access that would reach 1922-1990 San Diego Union issues.**
The only "Newspapers.com" access path in this whole survey (CSL's) is state-employee-gated
and/or onsite-only in Sacramento.

## Tasks 2-4: not applicable

**Task 1 came back negative: SFPL does not offer Newspapers.com in any form** (no ezproxy
entry exists at all — see Task 1 above), so there is no authenticated Newspapers.com
session to screenshot, no coverage to test against the 8 target dates, and no edition/page
to verify. Tasks 2, 3, and 4 are void for that reason; no `mirror/newspapers/` screenshot
was produced (directory created but left empty — nothing licensed to mirror).

## Access limits / friction hit along the way

- SFPL's ezproxy session for ProQuest/Gale/EBSCO-side products had silently expired since
  the last NewsBank recovery session; needed a fresh barcode/PIN re-login (see re-auth
  note above). NewsBank's own `WORLDNEWS` session was still live without re-login.
- `library.ca.gov` returns HTTP 403 to the sandboxed WebFetch tool (looks like a bot/WAF
  block on that fetcher's UA/IP) but loads fine through the real Chrome instance at
  `127.0.0.1:9222` — worth remembering for future CA State Library lookups.
- A generic AI web-search summary (not the page itself) asserted a fact about CSL's
  Newspapers.com access (no state-employee gate, offsite-with-embargo) that turned out to
  be wrong once the actual page text was pulled — a reminder to verify AI search summaries
  against the source HTML before recording them as findings, which is what this probe did.
- No rate-limiting, CAPTCHA, or download-cap issues were hit on SFPL's ezproxy, NewsBank,
  or ProQuest in this session — the friction here was entirely "the content isn't there,"
  not "the content is gated behind a usage limit."

## RECOMMENDATION

**This route cannot recover the San Diego Union 1922-1990 gap.** SFPL does not subscribe
to Newspapers.com in any form (confirmed by exhaustive A-Z and topic-filtered review of
its full database list, plus its own site search). The two SFPL products that could
plausibly have substituted — ProQuest "Historical Newspapers: U.S. West Collection" and
NewsBank "California Historical Newspapers" — were checked directly with in-database title
searches/source lists and neither carries any San Diego title at all (the ProQuest one
turned out to be a 94-title Gannett-regional-paper bundle with no major-metro titles; the
NewsBank one is a 17-title 19th-century Bay Area bundle). Checking further afield: the
California State Library does subscribe to Newspapers.com, but it's gated to state
employees and, for the deeper CDNC-partnership collection, onsite-only in Sacramento —
neither is obtainable by an ordinary SFPL patron or by the operator remotely. San Diego's
own library systems (SDPL, SD County, and neighboring city libraries) don't carry
Newspapers.com either and only offer the San Diego Union-Tribune via NewsBank from
2019-present.

**What would actually be needed to fill 1922-1990:** since no card-based remote-access
route exists, recovery has to go around Newspapers.com entirely. Two paths worth
prioritizing next: (1) check whether San Diego Public Library's **in-branch microfilm**
of the *San Diego Union* (not just the *Tribune*, which they confirmed on-site) covers the
gap years — this would require either an in-person visit/proxy or a scan-on-demand
request, not a remote probe; (2) revisit **CDNC's own embargo mechanics** — the lock
screens seen so far cite a specific unlock date (23 September 2026) per issue, which
implies CDNC/UCR is rolling embargoed 1930s-40s content free over time; worth checking
whether CDNC has *any* SD Union coverage past 1922 already digitized-but-embargoed (as
opposed to never-digitized), since an embargo expiring in September is a much shorter wait
than sourcing a new subscription. Newspapers.com itself (a personal paid subscription, not
a library card) remains the only outside-library route confirmed to hold the title for
this period, per the original background brief — but that's a paid-access decision for the
operator, not something an SFPL/library-card probe can unlock.


## Follow-up test (2026-07-12): is the post-1922 San Diego Union merely EMBARGOED in CDNC?

The probe above suggested checking whether CDNC holds post-1922 San Diego Union
content in the "embargoed but already digitized" state (the state that produces
the "available on 23 September 2026" lock screen), which would unlock for free
on a schedule rather than needing a subscription. It does not.

Direct test, fetching each issue's viewer and classifying the response:

| issue | result |
|---|---|
| `SDDU19241105` (San Diego Union, day after the 1924 general) | **NOT PRESENT** ("Oops!" page, no viewer) |
| `SDDU19301105` (San Diego Union, day after the 1930 general) | **NOT PRESENT** |
| `SDDU19401106` (San Diego Union, day after the 1940 general) | **NOT PRESENT** |
| `SDU19301105` (SACRAMENTO Union, same date) | **EMBARGOED**, lock screen states it unlocks 23 September 2026 (content exists) |

So the two states are cleanly distinguishable, and the San Diego Union is in the
first one: CDNC's `SDDU` digitization simply **ends in 1922**. There is no
hidden post-1922 Union content waiting on an embargo clock. The embargo affects
only other papers (the Sacramento Union, the Santa Barbara News-Press), where it
gates an AP county table, i.e. a remote-wire lower bound, not the Union's own
count.

**Consequences for the campaign:**

1. The 1922-1990 gap cannot be closed from CDNC using the San Diego Union. Full
   stop.
2. The only free route left inside CDNC is the one that produced 1936 and 1940:
   hunting San Diego County's *other* papers for election SPECIALS (an evening
   paper's overnight extra is night-clocked and valid; its routine day-after
   edition is not).
3. **A personal Newspapers.com subscription is the only confirmed route to the
   San Diego Union itself for 1922-1990.** That paper is a MORNING daily, so its
   day-after issues are exactly the night-clocked source this campaign is built
   on, and it would likely fill the gap properly rather than with lower bounds.
   This is an operator purchase decision, not something a library card unlocks
   (see the access findings above).
4. Re-running `SDU19301105` (and the other embargoed 1930s-40s issues) after
   **23 September 2026** is worth doing, but note what it buys: a remote AP wire
   snapshot, which this campaign records as a dimmed lower bound, not a clean
   night count.

## CORRECTION (2026-07-12): Newspapers.com does NOT carry the San Diego Union

The section above concluded that "a personal Newspapers.com subscription is the
only confirmed route" to the San Diego Union for 1922-1990. **That was wrong, and
it is withdrawn.** It was an inference from CDNC's embargo lock screen ("It is
available now at newspapers.com"), which refers to the paper that is actually
embargoed there (the SACRAMENTO Union), not to the San Diego Union. The
inference was never tested.

It has now been tested (see `newspapers-com-purchase-check.md` for the full
evidence). Newspapers.com's catalog contains **zero years** of The San Diego
Union, the San Diego Evening Tribune, or The San Diego Union-Tribune. Confirmed
four ways: exact and sub-phrase keyword searches return `count:0`; an exhaustive
enumeration of the 40 titles in their San Diego County location facet includes
none of the three; direct paper-URL guesses 404. Positive controls (LA Times, SF
Chronicle, Sacramento Bee) resolve normally, so the search API is not broken.

**Consequence: do not buy a Newspapers.com subscription for this project.** No
tier unlocks a title that is not in the catalog.

Remaining untested leads for the San Diego Union after 1922:
1. **GenealogyBank** (a NewsBank consumer product; NewsBank is the same vendor
   whose SDUB text archive already gave us 1992 and 2004). Web search suggests
   it may hold both San Diego titles. Untested. This is the next thing to probe.
2. **San Diego Public Library in-branch microfilm** of the Union. Confirmed to
   hold Tribune microfilm; the Union's holdings were not verified. Would need an
   in-person visit or a scan-on-demand request.
3. The **ProQuest San Diego Union-Tribune historical file**, if one exists under
   an institutional subscription somewhere reachable.
