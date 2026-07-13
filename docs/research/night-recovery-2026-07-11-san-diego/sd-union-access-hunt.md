# Access hunt: GenealogyBank, SFPL/NewsBank other products, and other institutions for the San Diego Union, 1922-1990

Status: DONE. Follows `newspapers-com-purchase-check.md` (Newspapers.com: zero years, ruled out) and
`newspapers-com-probe.md` (SFPL: no Newspapers.com; SFPL's `WORLDNEWS`/`EANX-NB` NewsBank products
carry no San Diego Union pre-1970(now corrected to 1983) content). This probe evaluates the three
remaining leads that document named: GenealogyBank, other NewsBank products SFPL might license, and
other institutions.

**Bottom line up front: a real, keyword-searchable, full-text-PDF "San Diego Union Historical
(1871-1992)" and "San Diego Evening Tribune Historical (1895-1992)" archive exists at NewsBank
under the Readex product code `EANX`. SFPL does not have it (confirmed by an explicit denial from
NewsBank itself). UC San Diego does, but only for current UCSD affiliates remotely / walk-in guests
on a library computer. GenealogyBank, a NewsBank consumer brand, publishes the identical coverage
range and is the only REMOTE, no-travel route — $79/year with a 7-day free trial.**

## Route 1: GenealogyBank

### Does it hold the titles, and for which years?

**Yes — GenealogyBank's public title catalog (no login) lists all three: San Diego Union, Evening
Tribune, and San Diego Union-Tribune, each with its own title page carrying a coverage-year header.**

Method: `https://www.genealogybank.com/explore/newspapers/all/usa/california/san-diego` is
Cloudflare/CloudFront-protected (plain curl gets a 403; the raw-CDP Chrome session at
`127.0.0.1:9222` loads it fine, 200KB, real content). Its "Newspapers by Title" filter box lists,
among ~13 San Diego titles: `evening-tribune`, `san-diego-union`, `san-diego-union-tribune`, each
linking to its own title page. Saved: `/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/gb_sd_explore.html`.

Each title page's `<h1>` states the vendor's own published coverage range:

| Title | URL | Coverage (verbatim `<h1>`) |
|---|---|---|
| San Diego Union | `https://www.genealogybank.com/explore/newspapers/all/usa/california/san-diego/san-diego-union` | "San Diego Union (San Diego, California) Newspaper Archives (1871 - 1992)" |
| Evening Tribune | `https://www.genealogybank.com/explore/newspapers/all/usa/california/san-diego/evening-tribune` | "Evening Tribune (San Diego, California) Newspaper Archives (1895 - 1992)" |
| San Diego Union-Tribune | `https://www.genealogybank.com/explore/newspapers/all/usa/california/san-diego/san-diego-union-tribune` | "San Diego Union-Tribune (San Diego, California) Newspaper Archives (1992 - 2018)" |

Saved: `gb_sdunion_title.html`, `gb_evetrib_title.html`, `gb_sdunt_title.html` (all in the tmp dir
above). The three ranges tile perfectly at the 1992 merger, which is itself a good internal
consistency check.

**Cross-validation (this is the important part):** this is not just marketing copy. UC San Diego
Library's own institutional LibGuide (see Route 3 below) independently states the *identical* two
ranges — "San Diego Union Historical (1871-1992)" and "San Diego Evening Tribune Historical
(1895-1992)," both described as "Full text PDF files of issues of this daily newspaper" — for what
resolves (via its real database link) to a NewsBank/Readex product, `p=EANX`. GenealogyBank's own
Terms of Use names **NewsBank** as the contracting party ("You and NewsBank both consent to the
jurisdiction of such courts..."), and its article-image URLs are served from
`infoweb1.newsbank.com/maximus/cache/...` — NewsBank's own image-hosting infrastructure. So
GenealogyBank is NewsBank's direct-to-consumer storefront for (very likely) the *same* underlying
digitized run that UCSD licenses institutionally as `EANX`. Two independent catalogs (a consumer
site and a university library guide) publishing the same 1871-1992 / 1895-1992 figures for a
NewsBank-sourced archive is real corroboration, not a single unverified claim.

**Rigor caveat, stated plainly:** I could not get a live, query-driven search to actually run
against a specific target date without a paid account. The title page's "Recent Newspaper
Clippings" section (article thumbnails with real dates like `1964-11-09`, `1976-02-27`) looked at
first like search results, but is in fact a "recently clipped by other GenealogyBank users" widget —
changing the `rgfromDate`/`rgtoDate`/`dateType` query parameters in the URL had zero effect on what
rendered (confirmed by grepping the same four `datePublished` dates in both the plain title page and
a parameterized fetch). A scripted attempt to drive the actual "Use a specific date" search form via
headless-browser interaction (check the date-type checkbox, type a date, click Search) failed
silently — the search UI needs live DOM state a direct navigate-and-diff approach doesn't reproduce.
**So the (1871-1992)/(1895-1992) figures are a catalog-level coverage claim** — the same kind of
signal the Newspapers.com check treated as meaningful (its own per-title year ranges), just not
independently confirmed against a specific 1922-1990 issue image the way, e.g., CDNC issues were
verified elsewhere in this campaign. Given the UCSD cross-validation above, this is stronger than a
single un-triangulated number, but it is not the same as having actually seen a page image.

### Pricing / trial

From `https://www.genealogybank.com/static/lp/a/freetrial/` (saved `gb_freetrial.html`):

| Plan | Price | Notes |
|---|---|---|
| Annual | $79/year ($6.58/mo equivalent) | "Save 21%" off reg. $99.90/year; "Most popular plan" |
| Monthly | $19.95/month | Flexible month-to-month |

Both: "Includes 7-day free trial — no charge today," "Cancel anytime by phone or online," phone
866-641-3297. The sign-up flow (`gb_signup.html`) starts with name/email/password account creation;
I did not proceed to a payment step (per task instructions not to sign up), so unlike the
Newspapers.com check, I cannot confirm from this probe alone whether a card must be entered before
the trial starts (industry-standard "free trial" flows usually do; the landing copy's "no charge
today" phrasing implies a card is on file, charged only if not cancelled, same shape as
Newspapers.com's trial — but this specific claim wasn't independently verified here the way
Newspapers.com's trial T&Cs paragraph was).

### Automated-access posture (ToS / robots.txt)

`robots.txt` (`gb_robots.html`): standard Drupal boilerplate, `Crawl-delay: 10`, generic
`Disallow: /doc/` and `/search/`-style query-string paths. **No named AI-crawler blocklist** — unlike
Newspapers.com, which explicitly disallows `ClaudeBot`, `Claude-User`, `GPTBot`, etc. by name. This
is a meaningfully more permissive posture than the site already ruled out.

Terms of Use (`gb_terms.html`, legally NewsBank, Florida jurisdiction) grants "an individual,
non-exclusive, non-transferable, limited license to browse, search, retrieve, view, print and/or
download[] the Content... for your personal non-commercial purposes," with printing/downloading
"further limited to insubstantial portions of the Content." There's also a clause against using
individual licenses to help "any... library, firm, corporation... municipality, county, state...
governmental entity... avoid[ing] the need... from subscribing to any... NewsBank product" — worth
flagging given this is for a civic-data project, though the actual use pattern (one individual paying
personal-tier price to look up ~20 historical dates for a public dataset) matches the product's
intended consumer use rather than an institutional workaround.

## Route 2: SFPL / NewsBank — is there ANY pre-1983 San Diego content under ANY product SFPL licenses?

**No, confirmed exhaustively, with an explicit denial as the decisive proof.**

Re-ran, fresh, the full A-Z Source List for SFPL's `WORLDNEWS` ("Access World News – Historical and
Current") product via `https://ezproxy.sfpl.org/login?url=https://infoweb.newsbank.com/apps/news/source-list?p=WORLDNEWS`
(saved `nb_worldnews_sourcelist.html`, 2.4MB). This list is the **master catalog**, not a
product-narrow slice: it contains 14,656 unique `pubname` codes, and it includes "Alta California," a
title that only otherwise surfaced under the smaller, separately-branded `EANX-NB` product the prior
probe checked (17 sources) — i.e., this master list is a superset that would show any San Diego
content regardless of which specific sub-product it nominally belongs to.

Exhaustively extracted every entry whose locality field is `USA - CA - San Diego`: **22 rows total**,
listed here for the record (this is the positive-control-quality enumeration the task asked for —
compare to the Newspapers.com check's 40-title San Diego County facet):

| Title | pubname | Coverage | Type/Format |
|---|---|---|---|
| San Diego Union-Tribune, The (CA) | `SDUB` | **1983 – Current** | Newspaper, Text |
| San Diego Union-Tribune, The (CA) | `CSD5-EEDT` | 2018 – Current | Newspaper, Image |
| San Diego Union-Tribune, The: Web Edition Articles | `SDUTS` | 2009 – Current | Web-Only |
| San Diego Union-Tribune en Español, The | `ESSDUT` | 2020–2023 | Newspaper, Text |
| San Diego Union-Tribune, The: Video | `UTSDS` | 2017–2025 | Video |
| U-T San Diego: Blogs | `SDUT` | 2004–2014 | Blog |
| (+16 more: campus papers, local broadcast transcripts, web-only outlets — none pre-1983, none a Union/Tribune predecessor) | | | |

**No standalone "San Diego Union (CA)" or "Evening Tribune (CA)" pre-merger title exists anywhere in
this catalog.** Note this **corrects** the earlier README/task-brief figure of "SDUB starts 1970" —
today's fresh pull clearly and unambiguously shows `SDUB` coverage as `1983 - Current`; whether that's
because the earlier probe misread the page or NewsBank's own metadata changed isn't determinable
from here, but 1983 is what the source shows as of this session (worth reconciling in the campaign
README).

Checked every other NewsBank product surfaced on SFPL's own authenticated session home screen
(`https://ezproxy.sfpl.org/login?url=https://infoweb.newsbank.com/apps/news/`, saved `nb_home.html`):
Hot Topics, Heritage Hub, San Francisco Chronicle (CA), San Francisco Community Coverage, California
Historical Newspapers (`EANX-NB`, already known: 17 SF-area 19th-c. sources), East Bay Times / Marin
IJ / Mercury News / Press Democrat / Sacramento Bee / Sunnyvale Sun / USA Today / Vacaville Reporter
collections (all non-SD regional bundles), and "California Newspapers Current and Historical" (a
`state:CA` scoped view whose direct URL isn't independently loadable — it errors "Product is
undefined / Missing or invalid authentication," an artifact of being a client-side "favorite view"
rather than a bookmarkable page; not pursued further since the WORLDNEWS master list above already
serves as the authoritative full-catalog check). **Heritage Hub** (`p=HHUB`, `nb_hhub.html`) is
confirmed to be an obituary/vital-records product ("HeritageHub obituaries, death notices & news
articles," searched by first/last/middle name), not a general newspaper-page archive — not a
plausible route to an election-night vote-count article regardless of date coverage.

**Decisive negative test:** tried to reach the exact product UCSD uses (`EANX`, via NewsBank's
Readex app path) through SFPL's already-whitelisted `infoweb.newsbank.com` ezproxy stanza:

```
https://ezproxy.sfpl.org/login?url=https://infoweb.newsbank.com/apps/readex/publication-browse?p=EANX&t=...
```

Result: **"We're sorry, this account doesn't have access to this product!"** (`nb_eanx_via_sfpl.html`)
— a clean, named, unambiguous denial from NewsBank's own backend, not a silent 404 or a fallback to
different content. (Separately, swapping `p=AMNEWS`, the CSUSM-linked product code, into the
already-working `WORLDNEWS` URL silently returned the *same* `WORLDNEWS` content — SFPL's real
entitlement overrides the parameter rather than leaking access — so the `EANX` test above is the
cleaner, better proof.)

**Verdict: SFPL does not carry pre-1983 San Diego Union or Evening Tribune content under any product
it licenses.** (SDUB's 1983-start does reach the tail of the campaign's window — 1984 and 1988 — but
not the 1922-1982 core, and it's text-only, no page image.)

## Route 3 / Task 4: Other institutions

### UC San Diego (UCSD) — the strongest finding of this probe

UCSD's own LibGuide (`https://ucsd.libguides.com/newspapers/historical`, saved
`ucsd_hist_newspapers.html`) explicitly lists, verbatim:

- **"San Diego Union Historical (1871-1992)"** — "Full text PDF files of issues of this daily
  newspaper"
- **"San Diego Evening Tribune Historical (1895-1992)"** — "Full text PDF files of issues of this
  daily newspaper, which merged with The San Diego Union in 1992"
- "San Diego Union Tribune (1970-present)" — "Full text (but no images)"
- "San Diego Union Tribune (2018-present)" — full text + images

The two "Historical" links (`https://ucsd.libguides.com/sdunionhistorical`,
`.../sdeveningtribune`) resolve (HTTP 302, confirmed with `curl -I`) to:

```
https://go.openathens.net/redirector/ucsd.edu?url=https://infoweb.newsbank.com/apps/readex/publication-browse?p=EANX&t=pubname:136E6A0F0DF56B38!San+Diego+Union&year=1992
https://go.openathens.net/redirector/ucsd.edu?url=https://infoweb.newsbank.com/apps/readex/publication-browse?p=EANX&t=pubname:136E6CB81C5E443C!Evening+Tribune&year=1992
```

i.e., the real underlying database is **NewsBank's Readex product, code `EANX`** — exactly the
product code speculated about in this task's brief — authenticated via OpenAthens/Shibboleth SSO
tied to UCSD's own identity provider (`idp.ucsd.edu`), a completely separate authentication path from
SFPL's ezproxy (confirmed above to be denied this exact product).

**Access policy — remote is affiliates-only, but walk-in guest access exists:**

- "our licenses with publishers only allow remote access for current UC San Diego students, faculty,
  and staff" — **even UCSD alumni are excluded from remote access**
  (`ucsd.libanswers.com/faq/403543`, `/faq/404767`).
- **"Guests are welcome to access most of our electronic resources from a library computer when
  visiting a library building as long as it is for personal or educational use."** No card, no fee,
  just physical presence at Geisel or WongAvery Library.
- One open caveat: "Some electronic resources are further restricted and not available to guests" —
  the FAQ does not name which. **Whether `EANX` specifically is in the guest-accessible set or the
  restricted set was not resolved by this probe** (would need a phone call, email, or an actual
  on-site test) — this is the one loose thread in an otherwise strong finding.

### San Diego State University (SDSU)

SDSU's LibGuide ("Historical Run of San Diego Union Tribune,"
`https://libguides.sdsu.edu/newspapers/SDUT`) documents the same title lineage (San Diego Herald
1851-1860; SD Union Weekly 1868-1872; SD Union 1871-1888 on microform; The Tribune 1981-1992; current
Union-Tribune) plus a NewsBank digital component independently described (web search) as "keyword
searchable... PDF images of the original newspaper copy," bridging index gaps in "1904 and 1930."
**Access: community-borrower/guest database access is explicitly onsite-only** — "Access to most
subscription/licensed electronic databases is available onsite via guest WiFi using your own device...
remote access is not permitted due to licensing restrictions." Same restriction shape as UCSD (guest
WiFi + own device, rather than a library terminal), and thus a viable backup if UCSD's guest
exclusion turns out to cover `EANX`.

### Cal State San Marcos (CSUSM) — the source of the `AMNEWS` product code

CSUSM's "San Diego Union Newspaper Archive" LibGuide redirects (Shibboleth) to
`infoweb.newsbank.com/apps/news/browse-multi?t=favorite:...!San+Diego+Union+Tribune+Historical+and+Current+Collection&p=AMNEWS`
— a **third** packaging of what appears to be the same lineage, under NewsBank's flagship academic
product code `AMNEWS` ("America's News"), also SSO-gated to CSUSM affiliates only. Not pursued
further (CSUSM's guest-access policy wasn't checked — UCSD/SDSU already give two on-site options
closer to San Diego itself).

### California State Library

Re-checked specifically for NewsBank/"America's News" products (the earlier probe in this directory
only checked Newspapers.com there). Via CDP (WebFetch is 403'd on `library.ca.gov`, consistent with
the earlier probe's note): CSL's online-resources page (`cslib_online_resources2.html`) **does** list
NewsBank's "America's News Collection" — Access World News Research Collection, Sacramento Bee
Collection, San Francisco Chronicle Collection, USA Today Collection — but **every single entry is
tagged "For State Employees,"** and **zero entries mention San Diego at all** (a full-text grep for
"San Diego" across the page returned nothing). Ruled out on two independent grounds: wrong audience,
and wrong city, even before the audience question matters.

### Los Angeles Public Library

Checked as a possible free-non-resident-card route, since LAPL's own NewsBank product page states it
"offers a convenient landing page to search all text and image versions dating back to 1871" of the
SD Union lineage. But LAPL's fully-remote, no-visit **"e-card" — the only card type that grants
immediate database access — is restricted to "Los Angeles City Residents only."** A California
resident living outside LA (e.g., in San Francisco) would need to physically visit an LAPL branch
just to get a card, which offers no advantage over visiting UCSD or SDSU directly in San Diego (where
the actual target content lives). Ruled out.

### San Diego Public Library

Not independently re-tested beyond the earlier probe's finding (Tribune microfilm on-site only, Union
holdings unverified). Given the UCSD finding — an on-site, digital, keyword-searchable, full-text-PDF
archive covering the *identical* 1871-1992 span — an in-person SDPL microfilm session is now clearly
inferior to a UCSD guest-computer session (search vs. manual reel-scrubbing), so it wasn't pursued
further. Noted in passing: SDPL's IDEA Lab / Digital Memory Lab and Central Library Special
Collections do offer general reproduction/scanning services (per web search, not independently
tested) — a fallback if `EANX` itself turns out to have gaps that only microfilm can fill.

## Ranked recommendation

1. **Best, free, one open caveat — visit UC San Diego's Geisel Library and use a guest computer** to
   pull NewsBank/Readex `EANX`'s "San Diego Union Historical (1871-1992)" and "San Diego Evening
   Tribune Historical (1895-1992)." This is a real, institutionally-documented, keyword-searchable,
   full-text-PDF archive spanning the entire 1922-1990 target window, for $0, no card, no signup.
   Confirm before or during the visit that `EANX` isn't in UCSD's unnamed "further restricted, not
   available to guests" set (a phone call to the library, or just trying it on arrival, resolves
   this in minutes).
2. **Cheap, remote, no-travel fallback — a personal GenealogyBank subscription**, $79/year
   ($6.58/mo) or $19.95/mo, 7-day free trial. Publishes the identical 1871-1992 / 1895-1992 coverage
   on its own public title pages, cross-validated against UCSD's independent institutional catalog,
   and legally operated by NewsBank itself (not a copycat/unrelated vendor). Its robots.txt carries
   no AI-crawler blocklist (unlike Newspapers.com). Recommend running the free trial *first* and
   manually checking all 20 target dates resolve to real page images before committing to a paid
   year — this probe could not verify that end-to-end without paying.
3. **SDSU** is a second on-site free fallback (same shape as UCSD: guest WiFi + own device rather
   than a library terminal), useful mainly if UCSD's guest restriction excludes `EANX`.
4. **Ruled out:** SFPL and every NewsBank product it licenses (14,656-title master catalog has no
   pre-1983 San Diego content; the exact product UCSD uses, `EANX`, explicitly denied by name to
   SFPL's account); California State Library (state-employee-gated, and carries no San Diego title
   regardless of audience); LAPL's remote e-card (Los Angeles city residents only).

## Evidence index (all under `/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/`, gitignored job tmp dir)

- `gb_sd_explore.html`, `gb_sdunion_title.html`, `gb_evetrib_title.html`, `gb_sdunt_title.html` —
  GenealogyBank catalog/title pages
- `gb_freetrial.html`, `gb_signup.html`, `gb_robots.html`, `gb_terms.html` — pricing/trial/ToS
- `nb_worldnews_sourcelist.html` (2.4MB, 14,656 pubnames) — SFPL's full NewsBank master catalog
- `nb_home.html`, `nb_hhub.html`, `nb_ca_browse.html`/`nb_ca_browse2.html` — SFPL's other NewsBank
  products
- `nb_amnews_via_sfpl.html`, `nb_eanx_via_sfpl.html` — cross-product-code negative tests
- `ucsd_hist_newspapers.html`, `cslib_online_resources2.html` — UCSD and CA State Library catalog
  pages
