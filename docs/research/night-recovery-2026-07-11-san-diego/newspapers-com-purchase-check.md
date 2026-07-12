# Newspapers.com purchase check: does it recover the San Diego Union, 1922-1990?

Status: DONE. **Verdict: DO NOT BUY.** Newspapers.com's own catalog does not contain
*The San Diego Union*, the *San Diego Evening Tribune*, or *The San Diego Union-Tribune*
under any title, alias, or location facet. No subscription tier unlocks a paper that
isn't in the catalog. This supersedes the tier/trial/ToS questions below, which are
answered for completeness but are moot for this specific recovery project.

This probe evaluates a **personal paid Newspapers.com subscription** (the operator's own
money), as distinct from the library-card route already ruled out in
`newspapers-com-probe.md` in this same directory (SFPL does not offer Newspapers.com at
all; California State Library's copy is state-employee/onsite-only).

## Method note

Newspapers.com's `/papers/` browse page is a client-rendered React app; the human-visible
"Filter by paper or location" box and "Location" facet both call clean JSON endpoints
under `/api/title/...`. Once discovered, these were queried directly (curl, with cookies
from an initial page load) rather than driving the browser for every check — faster and
lower-footprint than repeated headless-browser interaction, and the browser
(`127.0.0.1:9222`, background tab, `cdp_fetch.js`/custom puppeteer-core scripts) was used
to discover the endpoints and to capture confirming screenshots. No login was attempted;
everything below is from the logged-out, public side of the site (paper catalog, plan
pricing, free-trial landing page, robots.txt, Ancestry's Terms and Conditions are all
visible without an account).

## Question 1: Does Newspapers.com carry the San Diego Union (or Evening Tribune, or
Union-Tribune), and for which years?

**No. None of the three titles exist anywhere in Newspapers.com's catalog.**

Evidence, in increasing order of rigor:

1. **Keyword search, the exact phrase.** Typing "San Diego Union" into the live filter box
   returns **"Showing 0 papers... We're sorry, there are no matches for your search."**
   Screenshot: `/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/npc_shot_sdu_0results.png`. The
   underlying API call (captured via network log) is
   `https://www.newspapers.com/api/title/query?product-id=1&keyword=San%20Diego%20Union&start=0&count=24&...`
   and returns `{"titles":[],"count":0}` — reproduced directly with curl, saved at
   `/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/api_sdu.json` and `api_sdu2.json`.
2. **Every plausible sub-phrase and variant also returns zero:** `"Diego Union"`,
   `"San Diego Evening"`, `"San Diego Tribune"`, `"San Diego Union-Tribune"` (with and
   without the hyphen) — all `{"titles":[],"count":0}`. Saved:
   `npc_result_unt.json` and inline curl output in this session's transcript.
3. **Broader searches that DO return results, to prove the search mechanism itself
   works and isn't just erroring out:**
   - `"San Diego"` alone -> 10 papers total, "End of results" reached. All 10 are minor
     19th/early-20th-century sheets (*The Daily San Diegan*, *San Diego News*, *The San
     Diego Sun*, *Sud California Deutsche Zeitung*, etc., 1872-1939) — none is the Union,
     Evening Tribune, or Union-Tribune. Saved: `npc_result_sd.json`.
   - `"Union"` alone -> 369 papers nationwide (first page saved,
     `npc_result_union.json`); `"Evening Tribune"` alone -> 34 papers nationwide
     (`npc_result_evetrib.json`). None located in San Diego.
   - **Positive controls** to rule out an API bug: `"Los Angeles Times"` ->
     *The Los Angeles Times*, id 4312, 1881-2026, `extra:true`. `"San Francisco
     Chronicle"` -> *San Francisco Chronicle*, id 835, 1865-2026, `extra:true`.
     `"Sacramento Bee"` -> *The Sacramento Bee*, id 22428, 1857-2026, `extra:true`. All
     three major-metro CA dailies resolve instantly and correctly, confirming the search
     index is not simply broken or missing recent/major titles in general.
4. **The decisive check: a location-facet enumeration, not a keyword search.** The site's
   own "Location" filter resolves "San Diego" to the county record `San Diego County,
   California` (via `/api/title/location/search?prefix=San%20Diego`), and querying
   `/api/title/query?product-id=1&county=San%20Diego&state=California&country=United%20States%20of%20America&count=50`
   returns **every title Newspapers.com has ever catalogued for San Diego County: exactly
   40, and the API's own `count` field confirms 40 is the complete total** (max page size
   is 50, so no pagination was needed). Full list saved at
   `/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/loc_query_p1.json`; titles are Bay Cities
   Press, Bay Cities' Advertiser, The Chula Vista Star, Chula Vista Star-News, Citizen,
   Coast Dispatch, The Daily San Diegan, Daily Times-Advocate, Del Mar Citizen, El Cajon
   Star, El Cajon Valley News, The Fallbrook/Bonsall Enterprise, The Granite Journal,
   Imperial Beach Reminder, Imperial Beach Star-News, The La Costan, Life News, National
   City Star-News, North County Blade-Citizen, North County Times, Once-A-Week, Otay
   Press, Ramona Sentinel, The Record, The San Diego County Star, San Diego News, The San
   Diego Sun, San Dieguito High School, Semi-Tropic Culturist and Advertiser, The
   Star-News, The Star-News National City and Chula Vista, Sud California Deutsche
   Zeitung, The Sun, This Week, The Times-Advocate, Weekly Free Press, The Weekly San
   Diegan, The Weekly San Diegan-Sun, The Weekly Sun, Weekly Times-Advocate. **The city's
   flagship daily is not among them**, nor is any paper with "Union" or "Tribune" (other
   than the unrelated *Otay Press* etc.) in its name. This list cross-validates exactly
   against the keyword search: the subset of these 40 whose title literally contains "San
   Diego" is precisely the same 10 papers the keyword search found.
5. **Direct URL guesses** at plausible slugs (`/paper/the-san-diego-union/1/`,
   `/paper/san-diego-union-tribune/1/`, `/paper/san-diego-evening-tribune/1/`, etc.) all
   return **HTTP 404** — consistent with, though not independently conclusive of (wrong
   numeric ID would also 404), the catalog absence already established above.

**Coverage years: N/A for all three titles — not zero years of a partial run, but zero
presence in the catalog at all.** This is a materially different (and worse) finding than
"covered but gapped": there is no Newspapers.com paper page for the San Diego Union, the
Evening Tribune, or the Union-Tribune to check a date range against.

Note: a Newspapers.com sister product under the same Ancestry corporate umbrella,
**GenealogyBank**, surfaced in general web search as apparently holding a "San Diego
Union Archive Search" and an "Evening Tribune Archive Search"
(`genealogybank.com/explore/newspapers/all/usa/california/san-diego/...`). That is a
**different product with a different subscription**, not evaluated here — it wasn't the
question asked, and it deserves its own from-scratch purchase check (own pricing, own
ToS, own coverage-years verification) before any money moves toward it.

## Question 2: Which subscription tier?

**Moot — there is no tier that grants access to a title that isn't in the catalog.**

For context (since the operator's ~$20-25/~$45-50 estimate is now a year or more stale),
current (2026) Newspapers.com pricing, captured from the live plans page
(`https://www.newspapers.com/plans/?iid=624`, screenshot
`/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/npc_pricing_page.png`, Basic-tile variant
`npc_basic_price.png`):

| Plan | Price | Coverage |
|---|---|---|
| **Basic** | $7.95/mo, or $44.95/6 mo | 318 million+ pages, 27,000+ papers, back to 1618. **Explicitly excludes papers still under copyright — "typically 1931 and newer."** |
| **Publisher Extra** | $19.90/mo, or $74.90/6 mo | All 1 billion+ pages, 31,000+ papers, back to 1618. Includes the post-1931 (still-copyrighted) content Basic lacks. |

Even if the San Diego Union *were* in the catalog, this 1931 cutoff would have been
decisive on its own: 17 of the 20 target election dates (everything from 1934-11-07
onward) fall after it, so **Publisher Extra, not Basic, would have been required for the
large majority of this campaign's target years regardless of any per-title Publisher
Extra flag.** (The three major CA dailies checked as positive controls above — LA Times,
SF Chronicle, Sacramento Bee — are all individually flagged `extra:true` on top of that,
i.e. major metros tend to sit behind Publisher Extra by title as well as by date; had the
San Diego Union been present, betting on the same pattern would have been reasonable, but
it isn't a numbered confirmation since there's no record to check the flag on.)

## Question 3: Is there a free trial, and what are its limits?

**Yes — 7 days, but moot for this project since there's nothing on the platform to
trial against.** From the trial landing page
(`https://www.newspapers.com/free-trial/?iid=3826`, screenshot
`/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/npc_trial_page.png`):

> "\* One free trial per user. Free trial requires registration with a valid credit or
> debit card. You will be charged the full amount of your chosen subscription price on
> expiry of the free trial, unless you cancel at least 2 days before the end of your
> free trial by visiting the Account Details section or by contacting us. Subscriptions
> auto-renew at the end of your subscription period and your payment method will be
> debited the then applicable rate. To avoid auto-renewing cancel at least 2 days before
> your renewal date."

Card required up front, auto-charges at day 7 unless cancelled with 2+ days' buffer. The
trial-vs-tier question (does the 7-day trial include Publisher Extra) wasn't resolved
because it never mattered once Question 1 came back negative — the sign-up flow wasn't
walked further than the plan-selection screen to avoid entering payment info for a
title-absent product.

## Question 4: Automated-access reality check (ToS / robots.txt)

**robots.txt** (`https://www.newspapers.com/robots.txt`, saved
`/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/npc_robots.txt`): generic `User-agent: *` is
`Allow: /` with a Cloudflare "Content-Signal" header of
`search=yes, ai-train=no, use=reference` — i.e. indexing is fine, AI training is not.
Separately, and more pointedly, the file **explicitly, by name, disallows a long list of
AI/LLM crawlers and assistants**, including `ClaudeBot`, `Claude-User`, `Claude-Web`,
`Claude-SearchBot`, `Anthropic-ai`, `GPTBot`, `ChatGPT-User`, `OAI-SearchBot`,
`PerplexityBot`, `Google-Extended`, and about 40 others (`Disallow: /` for each). This is
about crawler identification (User-Agent string), not about a real Chrome browser driven
by an agent — the browser used in this probe identifies as ordinary Chrome/Mozilla, not
as any of the named bots — but it is a clear signal of the operator's posture toward
AI-associated automated access to this specific site, worth weighing heavily given the
project's nature.

**Terms and Conditions** (Newspapers.com's terms redirect to Ancestry's master ToS,
`https://www.ancestry.com/c/legal/termsandconditions`, saved
`/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/npc_terms.html` /
`npc_terms.txt`). Section 1.3 ("Use of the Services") states, among the "you agree"
list:

> "Not to access, acquire, copy, or monitor any portion of the Services by any manual,
> automated, or programmatic method that exceeds the intended standard human use of the
> Services; or to use any data or content from the Services to train, develop, or
> fine-tune any machine learning model, algorithm, or artificial intelligence system[.]"

Two distinct prohibitions in one clause: (a) automated/programmatic access that
**exceeds** "standard human use," and (b) using site content to train/fine-tune an AI
model (not our use case — the goal is human transcription of election counts into a
dataset, not model training). Also present, elsewhere in Section 1.3: content may be
downloaded only "in connection with your family or your professional family history
research or where expressly permitted" — the intended use case is framed around
genealogy, not the kind of civic/historical-count research this project does; that's not
squarely a violation but it isn't squarely covered either.

**Honest assessment for the proposed access pattern (real logged-in Chrome, human-paced,
one page at a time, ~30-60 issues, saved to a gitignored local mirror):** technically,
this is very likely to *work* — the site's Cloudflare protection did not challenge either
plain curl requests (once a session cookie existed) or puppeteer-driven browser
navigation during this probe; there's no indication of an aggressive bot wall on the
public/catalog side, and a human-paced session would likely fare at least as well.
Whether it's *within terms* is genuinely ambiguous: clause (a) turns on whether an
automated method "exceeds... standard human use," which a slow, one-tab, human-supervised
session arguably would not exceed in rate or volume, but the clause names "automated...
method" itself as the flagged category, not just its speed — a strict reading could call
any bot-driven session a violation independent of pacing. This is a judgment call the
operator should make deliberately, not something this probe can resolve for them. Since
it is moot for this specific paper (Question 1), it wasn't tested against a live
gated-image viewer, so the deep-zoom viewer's own bot-friendliness (a separate technical
question from Cloudflare's front door) remains unverified.

## Question 5: The 20 target dates

**0 of 20 confirmed present — not because any individual date is missing from an
existing run, but because there is no San Diego Union browse calendar on Newspapers.com
to check dates against at all** (see Question 1). Listed for the record; every row is
N/A for the same reason:

| Election date | San Diego Union issue on Newspapers.com? |
|---|---|
| 1922-11-08 | N/A — title not in catalog |
| 1926-11-03 | N/A — title not in catalog |
| 1930-11-05 | N/A — title not in catalog |
| 1934-11-07 | N/A — title not in catalog |
| 1938-11-09 | N/A — title not in catalog |
| 1942-11-04 | N/A — title not in catalog |
| 1944-11-08 | N/A — title not in catalog |
| 1946-11-06 | N/A — title not in catalog |
| 1948-11-03 | N/A — title not in catalog |
| 1950-11-08 | N/A — title not in catalog |
| 1952-11-05 | N/A — title not in catalog |
| 1956-11-07 | N/A — title not in catalog |
| 1960-11-09 | N/A — title not in catalog |
| 1964-11-04 | N/A — title not in catalog |
| 1968-11-06 | N/A — title not in catalog |
| 1972-11-08 | N/A — title not in catalog |
| 1976-11-03 | N/A — title not in catalog |
| 1980-11-05 | N/A — title not in catalog |
| 1984-11-07 | N/A — title not in catalog |
| 1988-11-09 | N/A — title not in catalog |

## RECOMMENDATION

**Do not buy a Newspapers.com subscription for this purpose. It cannot recover the San
Diego Union, 1922-1990 — the title (and its successors, the Evening Tribune and the
Union-Tribune) is not in Newspapers.com's catalog at all**, confirmed four independent
ways (exact-phrase keyword search, sub-phrase/variant keyword searches, an exhaustive
40-title San Diego County location-facet enumeration with a self-reported complete count,
and direct URL probes), cross-validated against three major-CA-daily positive controls
(LA Times, SF Chronicle, Sacramento Bee) that prove the search mechanism itself works
correctly for comparable titles. No tier — Basic or Publisher Extra — changes this, and
no free trial would surface content that isn't there.

Do not bother trialing it "just to check" either: the catalog-level `count:0` /
40-title-enumeration evidence above is definitive without needing a logged-in session,
and starting the 7-day trial would require a card on file with an auto-charge risk for a
product this project has no use for.

**What this changes about the campaign:** the earlier probe in this same directory
(`newspapers-com-probe.md`) had already ruled out every library-card route and concluded
"a personal Newspapers.com subscription is the only confirmed route to the San Diego
Union itself for 1922-1990." That conclusion was based on the *hypothesis* that
Newspapers.com carries the title (reasonable, since CDNC's own lock screens reference
newspapers.com by name for *other* papers) — this probe tested that hypothesis directly
and it fails. **As of this check, there is no known remote/digital route to the San Diego
Union for 1922-1990 at all.** Two threads are still open and worth prioritizing next
ahead of any further spend: (1) GenealogyBank, a separate Ancestry-family product that
surfaced in web search as apparently holding both a "San Diego Union" and an "Evening
Tribune" archive — untested here, deserves its own from-scratch coverage/tier/ToS check
before any purchase; (2) San Diego Public Library's in-branch microfilm of the *Union*
(not just the *Tribune*, which was already confirmed on-site-only in the earlier probe),
which would need an in-person visit or a scan-on-demand request rather than a remote
probe.
