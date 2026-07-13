# San Diego County: Wayback probe for election-night ballots-counted, 1994-2010 generals

Probe only (not a full recovery pass). Scope: the nine Nov generals 1994-2010. Two
routes per election per the brief: (1) CA SoS election-night site, (2) San Diego
County registrar site. RUNBOOK 6.5/7.1 mechanics used throughout: `id_` raw fetches,
gunzip-if-`1f 8b`, tight-window CDX, `curl -sI` for replay-alias checks. All raw
fetches/CDX JSON saved under `/Users/sbuss/.claude/jobs/8f24b289/tmp/sd/wb/` (not in
the repo). Politeness: ~2s between archive.org requests throughout.

Denominators (certified finals) are NOT sourced in this pass; this is a numerator-only
probe per the mission brief.

---

## 1994-11-08 (general)

**Route 1 (SoS).** No candidate host exists this early. `vote94.ss.ca.gov` has only a
`robots.txt` capture from 2007 (a much later placeholder, not an active 1994 site).
CDX check on the SoS root domain confirms Wayback's *earliest* capture of `ss.ca.gov`
of any kind is `19961227034330` — more than two years after this election.

Query run:
```
http://web.archive.org/cdx/search/cdx?url=vote94.ss.ca.gov&matchType=domain&output=json&limit=10
http://web.archive.org/cdx/search/cdx?url=ss.ca.gov&matchType=domain&output=json&limit=10&from=19940101&to=19970101
```

**Route 2 (county).** `co.san-diego.ca.us` domain sweep for 1994-01-01 to 1996-12-31
(only feasible narrower window checked was 1994-09-01/1995-01-01, which 504'd; the
domain's earliest capture of ANY kind, confirmed via the 1996 sweep below, is
`19961230142113`, over two years post-election).

**Verdict: DEAD END.** Wayback has zero coverage of any relevant host before late
1996. Categorically unrecoverable via Wayback.

---

## 1996-11-05 (general)

**Route 1 (SoS).** `vote96.ss.ca.gov` exists in Wayback, but its earliest capture of
any page is `19961225213858` (Dec 25, 1996) — seven weeks after the election. A
`Vote96/html/stats/turnout.htm` page (captured `19980113020112`, over a year later) was
checked and contains only a *statewide* historical primary-turnout table (1910-1994),
no per-county or per-election general-election data. No `Returns/status.htm`-style
per-county page exists under this host at all (confirmed via a domain-wide
`filter=original:.*(tatus|ounty|urnout).*` sweep — the only hits were
`html/absnt/county.doc` and the turnout page above).

Queries run:
```
http://web.archive.org/cdx/search/cdx?url=vote96.ss.ca.gov&matchType=domain&output=json&limit=20&collapse=urlkey
http://web.archive.org/cdx/search/cdx?url=vote96.ss.ca.gov&matchType=domain&output=json&limit=500&filter=original:.*(tatus|ounty|urnout).*&collapse=urlkey
```
Fetched (raw, `id_`): `http://vote96.ss.ca.gov:80/Vote96/html/stats/turnout.htm` @ 19980113020112.

**Route 2 (county).** `co.san-diego.ca.us` domain sweep for Sep-Dec 1996 shows the
site's earliest-ever captures are Dec 28-30, 1996 (an air-pollution-control-district
subdomain and an `onyx` subdomain holiday page) — nothing election-related, nothing
before late December, i.e. nothing anywhere near Nov 5.

Query run:
```
http://web.archive.org/cdx/search/cdx?url=co.san-diego.ca.us&matchType=domain&output=json&limit=100&from=19960901&to=19970101
```

**Verdict: DEAD END.** No Wayback coverage of either host exists within ~7 weeks of
election night; what little exists post-dates it by months to years and contains no
per-county results.

---

## 1998-11-03 (general)

**Route 1 (SoS).** `vote98.ss.ca.gov/Returns/status.htm` EXISTS and has the expected
FENU-style per-county "County Returns Status" table format (confirmed by content, see
below) — but its earliest Wayback capture is `19990422074557` (Apr 22, 1999), over five
months post-election. That capture's own header reads "As of Jan 22, 1999 at 4:30 pm"
and shows counties' "Latest Report Day-Time" values in the 12-24 (day-of-month) range —
i.e. the frozen page reflects a January 1999 canvass/history state, not election night.
No capture exists between election day and that first crawl.

Queries run:
```
http://web.archive.org/cdx/search/cdx?url=vote98.ss.ca.gov&matchType=domain&output=json&limit=500&filter=original:.*(tatus|ounty|urnout).*&collapse=urlkey
http://web.archive.org/cdx/search/cdx?url=vote98.ss.ca.gov/Returns/status.htm&output=json&limit=200
```
Fetched (raw, `id_`): `http://vote98.ss.ca.gov:80/Returns/status.htm` @ 19990422074557 —
content confirms "County Returns Status / As of Jan 22, 1999 at 4:30 pm", table columns
Total Precincts / Precincts Rpt'g / %Rpt'g / Reg'd Voters / Ballots Cast / %Turnout /
First Report / Latest Report / Report Type. Not usable as night data.

**Route 2 (county).** `co.san-diego.ca.us` domain sweep, Oct 28 - Nov 15 1998,
election-keyword filter (`vote|elect|rov|regist`): **zero captures**. The county site
has no Wayback presence at all in this window.

Query run:
```
http://web.archive.org/cdx/search/cdx?url=co.san-diego.ca.us&matchType=domain&output=json&limit=200&from=19981028&to=19981115&filter=original:.*(vote|elect|rov|regist).*
```

**Verdict: DEAD END.** The SoS status-page structure existed and would have carried
the right data, but Wayback's first crawl is five-plus months late; the county side has
no presence in-window at all.

---

## 2000-11-07 (general, presidential)

**Route 1 (SoS).** `vote2000.ss.ca.gov/returns/status.htm` (later `/Returns/status.htm`)
EXISTS with full history back to June 2000 (a March 2000 primary snapshot) and forward
to 2007, but the full capture list has a gap from `20000815063633` (Aug 15, 2000)
straight to `20010126093400` (Jan 26, 2001) — **no capture anywhere in Nov/Dec 2000**,
despite this being the highest-profile US election of the era.

Query run:
```
http://web.archive.org/cdx/search/cdx?url=vote2000.ss.ca.gov/returns/status.htm&output=json&limit=200
```

**Route 2 (county).** `co.san-diego.ca.us` domain sweep, Nov 1-20 2000, election filter:
several hits, all static pre/peri-election informational pages under
`cnty/cntydepts/community/voters/election/` — `November7.htm` (captured Nov 9, 2000,
still describing the election as upcoming/logistics: absentee deadlines, weekend voting
hours), `ballot_query.html`, `candidiate.htm`, `polling_query.html`. A
"Reports On-Line" page (`reports/line.htm`, captured Nov 9) links to
`Voter_Turnouts.pdf`, but that PDF's only Wayback capture (`20000823185548`, Aug 23,
2000) predates the election entirely — it is a historical-elections turnout report, not
a live Nov-2000 count. No results/status page of any kind found.

Queries/fetches run:
```
http://web.archive.org/cdx/search/cdx?url=co.san-diego.ca.us&matchType=domain&output=json&limit=200&from=20001101&to=20001120&filter=original:.*(vote|elect|rov|regist).*
http://web.archive.org/cdx/search/cdx?url=co.san-diego.ca.us/cnty/cntydepts/community/voters/Voter_Turnouts.pdf&output=json&limit=100&from=20000101&to=20020101
```
Fetched: `.../election/November7.htm` @ 20001109153300 (pre-election logistics page);
`.../reports/line.htm` @ 20001109184700 (menu page, no inline totals).

**Verdict: DEAD END.** SoS status page has a Nov-2000-shaped hole in its capture
history; county site has only static pre-election pages and a stale (pre-election)
turnout PDF in the window.

---

## 2002-11-05 (statewide general)

**Route 1 (SoS).** `vote2002.ss.ca.gov/Returns/status.htm` has real captures in-window:
`20021111182206` (Nov 11, 2002) shows a page header "County Status As of Nov 10, 2002
at 11:28 pm" with a distinct digest from both the pre-election Oct 13 snapshot and the
eventual frozen final-canvass digest (`VJYNZVHEWL6NNHJQL7YU7NBFBU3UGEDV`, stable from
`20021125181250` through at least 2009). San Diego's row in the Nov 11 capture:
Total Precincts 2,138, 100% reporting, Reg'd Voters 1,411,808, **Ballots Cast 671,611**,
47.5% turnout, First Report "05-8:06pm" (Nov 5, election night), **Latest Report
"08-3:28pm" (Nov 8, 2002)**. That Latest-Report timestamp is three days after election
night — this is a mid-canvass figure, not the night plateau; San Diego's ballots-cast
total almost certainly grew between the true Nov-5/6 overnight count and this Nov-8
reading (absentee/provisional processing continues through the canvass), and no earlier
capture exists to pin the actual overnight number.

Queries run:
```
http://web.archive.org/cdx/search/cdx?url=vote2002.ss.ca.gov&matchType=domain&output=json&limit=500&filter=original:.*(tatus|ounty|urnout).*&collapse=urlkey
http://web.archive.org/cdx/search/cdx?url=vote2002.ss.ca.gov/Returns/status.htm&output=json&limit=200
```
Fetched (raw, `id_`): `http://vote2002.ss.ca.gov:80/Returns/status.htm` @ 20021111182206.

**Route 2 (county).** `co.san-diego.ca.us` domain sweep, Nov 1-15 2002: the registrar
homepage was crawled daily (Nov 2-15) and links to "Countywide Election Results" ->
`election/results_table.html`, which (per the 2004 finding below, same page, same
digest lineage) is a static per-race MENU page with no inline countywide ballots-cast
figure — it links out to per-race pages, none of which carry a "ballots cast" total.
Also present: a `cgi-bin/Count.cgi?df=elect_20021105.dat` hit (Nov 7, 09:25) — this is
an image/gif-output hit-counter/chart script, not machine-readable text data, and not
pursued further given the SoS-route figure already establishes a (non-night) number.
`election/Nov2002.html` is a static pre-election info page (same digest Oct 2002 -
Dec 2003) — not results.

Queries/fetches run:
```
http://web.archive.org/cdx/search/cdx?url=co.san-diego.ca.us&matchType=domain&output=json&limit=200&from=20021101&to=20021115&filter=original:.*(vote|elect|rov|regist).*
http://web.archive.org/cdx/search/cdx?url=co.san-diego.ca.us/cnty/cntydepts/community/voters/election/Nov2002.html&output=json&limit=50
```
Fetched: `.../voters/` homepage @ 20021106083523 (links to results_table.html and to
vote2002.ss.ca.gov).

**Verdict: DEAD END for plateau grade.** A real, dated county-level figure exists
(671,611 ballots cast) but it is stamped Nov 8, three days into the canvass, not
election night, and per RUNBOOK 1/8 that disqualifies it as the plateau figure. Recorded
here as a non-circular reference point only, not a candidate election-night number.

---

## 2004-11-02 (presidential general)

**Route 1 (SoS).** `vote2004.ss.ca.gov` exists with a rich `/Returns/` tree (per-race
per-county HTML pages for President/US Senate/etc., regenerated multiple times/day
during the election). The one countywide aggregate page, `/Returns/status.htm`
("County Status" — same FENU-style table as later years) has captures on Oct 9 and
Dec 9, 2004 but **none between them** — the entire Oct 9 - Dec 9 span, which fully
brackets election night, is uncaptured for this specific URL. The homepage
(`vote2004.ss.ca.gov/`) has the same gap: last capture before election was Nov 1
("website will be available soon" placeholder), next is Nov 8. The per-candidate
presidential map page (`Returns/pres/mapAN.htm`) WAS captured election night
(`20041104020813` = Nov 3, 2004 18:08 PST) and links to per-county pages
(`Returns/pres/37.htm` = San Diego, county code 37 in SoS alphabetical numbering), but
those give votes-FOR-PRESIDENT only (not "ballots cast", which includes undervotes and
down-ballot-only ballots), and the only captures of `37.htm` are Nov 10 and Dec 5 — both
post-night, non-plateau, and not the right metric even if they were.

Queries/fetches run (representative):
```
http://web.archive.org/cdx/search/cdx?url=vote2004.ss.ca.gov&matchType=domain&output=json&limit=50&from=20040901&to=20041231
http://web.archive.org/cdx/search/cdx?url=vote2004.ss.ca.gov&matchType=domain&output=json&limit=200&from=20041101&to=20041106
http://web.archive.org/cdx/search/cdx?url=vote2004.ss.ca.gov&matchType=domain&output=json&limit=2000&from=20040901&to=20041231&collapse=urlkey
http://web.archive.org/cdx/search/cdx?url=vote2004.ss.ca.gov/Returns/status.htm&output=json&limit=100
http://web.archive.org/cdx/search/cdx?url=vote2004.ss.ca.gov/&output=json&limit=100&from=20041102&to=20041110
http://web.archive.org/cdx/search/cdx?url=vote2004.ss.ca.gov/Returns/pres/37.htm&output=json&limit=100&from=20041101&to=20041210
```
Fetched (raw, `id_`, gunzip-checked): `/Returns/status.htm` @ 20041009164159 (shows
March-2004-primary content, frozen/stale, confirming this is not a live Nov page at that
date); `/Returns/pres/mapAN.htm` @ 20041104020813 (Nov 3 18:08 PST, real presidential
per-county leader map, but no ballots-cast data).

**Route 2 (county).** `co.san-diego.ca.us` domain sweep, Sep-Dec 2004, election filter:
the registrar's "results_table.html" (linked from the homepage as "Countywide Election
Results") is a static per-race menu — its digest is UNCHANGED
(`NVN6UIL43HKE3HMQN2GES2OTPF4DWLF7`) from Dec 2002 straight through Jan 2005, i.e. it
never carried live data for this election at all; content is literally a stale index of
race names (including "GOVERNOR", not even on the 2004 ballot) linking to per-race
pages, no inline county totals.

Queries/fetches run:
```
http://web.archive.org/cdx/search/cdx?url=co.san-diego.ca.us&matchType=domain&output=json&limit=300&from=20040901&to=20041231&filter=original:.*(rov|elect|vote|regist).*&collapse=urlkey
http://web.archive.org/cdx/search/cdx?url=co.san-diego.ca.us/cnty/cntydepts/community/voters/election/results_table.html&output=json&limit=100
```
Fetched (raw, `id_`): `results_table.html` @ 20041031080645 — confirmed static menu, no
totals.

**Verdict: DEAD END.** The SoS county-status URL that carries ballots-cast data exists
structurally but has an Oct9-Dec9 capture gap covering the entire election; the only
in-window SoS capture (the presidential leader map) doesn't carry the right metric; the
county's own "results" page is a static stale template.

---

## 2006-11-07 (statewide general)

**Route 1 (SoS).** Correct host is `vote2006.sos.ca.gov` (NOT `.ss.ca.gov` —
`vote2006.ss.ca.gov` has zero Wayback captures at all). `vote2006.sos.ca.gov/Returns/status.htm`
exists but its only captures are `20080608063644` and `20080907144738` — both June/Sept
2008, over a year and a half post-election, with IDENTICAL digest (frozen). Content
confirms it is a "November 7, 2006 General Election" county-status page and San Diego's
row shows Latest Report "11 12:17pm" (Nov 11, 2006) — a mid-canvass reading (like 2002),
not night, and the earliest available capture is 19 months later than even that, so
there is no way to bracket or verify it further; it is simply the frozen end-state of a
page nobody re-crawled until 2008.

Queries/fetches run:
```
http://web.archive.org/cdx/search/cdx?url=vote2006.ss.ca.gov&matchType=domain&output=json&limit=5&collapse=urlkey   [empty]
http://web.archive.org/cdx/search/cdx?url=vote2006.sos.ca.gov&matchType=domain&output=json&limit=5&collapse=urlkey
http://web.archive.org/cdx/search/cdx?url=vote2006.sos.ca.gov&matchType=domain&output=json&limit=500&filter=original:.*(tatus|ounty|urnout).*&collapse=urlkey
http://web.archive.org/cdx/search/cdx?url=vote2006.sos.ca.gov/Returns/status.htm&output=json&limit=100&from=20060801&to=20090101
```
Fetched (raw, `id_`): `/Returns/status.htm` @ 20080608063644 — San Diego row: Total
Precincts 2,211, 100.0%, Reg'd 1,381,835, Ballots Cast 789,676, 57.1%, First Report
"7 8:19pm" (election night), Latest Report "11 12:17pm" (Nov 11, 2006), Report Type F.

**Route 2 (county).** Domain sweeps of both `co.san-diego.ca.us` and `sdcounty.ca.gov`
(the county's newer domain by 2006) for Nov 1-15 2006, election-keyword filtered: only
two hits on `co.san-diego.ca.us` (both 404s on a PDF search-anchor URL); the
`sdcounty.ca.gov` sweep returns dozens of unrelated county-department hits (HR, public
defender, library, OES) plus `rov/Eng/Edistrict_query.asp`,
`rov/Eng/Epolling_query.asp` (district/polling-place lookup TOOLS, not a results page) —
no results or status page captured anywhere in the window.

Queries run:
```
http://web.archive.org/cdx/search/cdx?url=co.san-diego.ca.us&matchType=domain&output=json&limit=200&from=20061101&to=20061115&filter=original:.*(vote|elect|rov|regist).*
http://web.archive.org/cdx/search/cdx?url=sdcounty.ca.gov&matchType=domain&output=json&limit=200&from=20061101&to=20061115
```

**Verdict: DEAD END.** SoS status page exists and would carry the data, but is
uncaptured until 19 months post-election (frozen at a mid-canvass, non-night state even
then); county route has no results page in-window at all.

---

## 2008-11-04 (presidential general) — RECOVERABLE

**Route 1 (SoS).** `vote.sos.ca.gov/Returns/status.htm` was captured
`20081106063312` (2008-11-06 06:33:12 UTC = **Nov 5, 2008, 22:33 PST**). Page header:
"County Reporting Status ... 100.0% (25,423 of 25,423) precincts partially or fully
reporting as of Nov. 5, 2008, at 10:05 p.m." San Diego's row:

> San Diego 2,328 2,328 100.0% 1,488,157 **980,234** 65.9% First Report "4 8:01 p.m."
> (Nov 4, 8:01pm) Latest Report **"5 6:46 a.m."** (Nov 5, 6:46am) Report Type **FENU**

I.e. San Diego's own last update that election night was 6:46 a.m. the morning after
polls closed (10.75 hours post-close) with **980,234 ballots cast**, 65.9% turnout of
1,488,157 registered.

**Plateau bracket (RUNBOOK 8):** the next capture, `20081108032433` (Nov 8, 2008,
03:24 UTC; page header "as of Nov. 7, 2008, at 7:06 p.m."), shows San Diego's row grown
to **1,051,756** ballots cast (70.7%), Latest Report now "7 5:04 p.m." (Nov 7), Report
Type changed to **CCU** (county canvass update). The FENU->CCU transition plus the
number moving upward between the two captures is a clean non-circular bracket: 980,234
was San Diego's last FENU (election-night) figure before the canvass moved past it.

Queries/fetches run:
```
http://web.archive.org/cdx/search/cdx?url=vote2008.sos.ca.gov&matchType=domain&output=json&limit=500&filter=original:.*(tatus|ounty|urnout).*&collapse=urlkey   [only a stray 2011 capture]
http://web.archive.org/cdx/search/cdx?url=vote.sos.ca.gov&matchType=domain&output=json&limit=200&filter=original:.*(tatus|ounty|urnout).*&from=20080901&to=20090101
```
Fetched (raw, `id_`): `http://vote.sos.ca.gov/Returns/status.htm` @ 20081106063312 (the
figure) and @ 20081108032433 (the bracket).

**Verdict: RECOVERABLE.** Figure: **San Diego 980,234 ballots cast**, last report Nov 5,
2008 6:46 a.m., 65.9% of 1,488,157 registered. Source:
`https://web.archive.org/web/20081106063312/http://vote.sos.ca.gov/Returns/status.htm`.
Bracketed by `https://web.archive.org/web/20081108032433/http://vote.sos.ca.gov:80/Returns/status.htm`
(1,051,756, CCU). Route 2 (county) not pursued — SoS route already fully solved this row.

---

## 2010-11-02 (midterm general) — RECOVERABLE

**Route 1 (SoS).** `vote.sos.ca.gov/returns/status/` was captured `20101105215804`
(2010-11-05 21:58:04 UTC = Nov 5, 13:58 PST). San Diego's row:

> San Diego 2,050 2,050 100% 1,442,161 **663,326** 46% First Report "Nov 2 8:02 p.m."
> Latest Report **"Nov 3 2:22 a.m."** Report Type **FENU**

San Diego's own last update was 2:22 a.m. the morning after election day (6.3 hours
post-close), **663,326 ballots cast**, 46% of 1,442,161 registered.

**Plateau bracket:** the next capture, `20101110011312` (Nov 10, 2010), shows San
Diego's row grown to **825,597** (57.2%), Latest Report now "Nov 8 5:04 p.m.", Report
Type **CCU**. Same clean FENU->CCU, number-moved-up bracket as 2008.

Queries/fetches run:
```
http://web.archive.org/cdx/search/cdx?url=vote2010.sos.ca.gov&matchType=domain&output=json&limit=500&filter=original:.*(tatus|ounty|urnout).*&collapse=urlkey   [empty; host doesn't exist under this name]
http://web.archive.org/cdx/search/cdx?url=vote.sos.ca.gov&matchType=domain&output=json&limit=200&filter=original:.*(tatus|ounty|urnout).*&from=20101001&to=20101201
```
Fetched (raw, `id_`): `http://vote.sos.ca.gov/returns/status/` @ 20101105215804 (the
figure) and @ 20101110011312 (the bracket).

**Verdict: RECOVERABLE.** Figure: **San Diego 663,326 ballots cast**, last report Nov 3,
2010 2:22 a.m., 46% of 1,442,161 registered. Source:
`https://web.archive.org/web/20101105215804/http://vote.sos.ca.gov/returns/status/`.
Bracketed by `https://web.archive.org/web/20101110011312/http://vote.sos.ca.gov/returns/status/`
(825,597, CCU). Route 2 (county) not pursued — SoS route already fully solved this row.

---

## Summary table

| Election | Verdict | Election-night figure (San Diego ballots cast) | Source capture |
|---|---|---|---|
| 1994-11-08 | DEAD END | — | no Wayback coverage exists this early |
| 1996-11-05 | DEAD END | — | earliest Wayback captures are ~7 wks post-election |
| 1998-11-03 | DEAD END | — | status page exists, first crawled 5+ mo late |
| 2000-11-07 | DEAD END | — | status page has a Nov/Dec-2000-shaped capture gap |
| 2002-11-05 | DEAD END | (671,611 @ Nov 8, non-night, for reference only) | 20021111182206 |
| 2004-11-02 | DEAD END | — | status page has an Oct9-Dec9 capture gap |
| 2006-11-07 | DEAD END | (789,676 @ Nov 11, non-night, for reference only) | 20080608063644 |
| 2008-11-04 | **RECOVERABLE** | **980,234** (65.9%, Nov 5 6:46am, FENU) | `web.archive.org/web/20081106063312/http://vote.sos.ca.gov/Returns/status.htm` |
| 2010-11-02 | **RECOVERABLE** | **663,326** (46%, Nov 3 2:22am, FENU) | `web.archive.org/web/20101105215804/http://vote.sos.ca.gov/returns/status/` |

## Recommendation for a recovery pass

- **2008 and 2010 are ready to promote directly** into
  `data/research/election-night/san-diego-ca.json` following the exact evidentiary
  pattern already used for the 2014 row (same host family, same FENU/CCU bracket
  mechanic, same `vote.sos.ca.gov` per-county status table). Denominators (certified
  finals) still need sourcing from the SoS SoV PDFs per RUNBOOK 6.1 before the rows are
  complete; this probe did not touch denominators.
- **1994-2006 are genuine dead ends via Wayback**, not "needs more digging" — the
  binding constraint for 1994-2000 is that Wayback simply has no or near-no coverage of
  the relevant hosts that early; for 2002-2006 the SoS status-page URL structure is
  confirmed to have existed and carried the right per-county metric, but the specific
  captures that survived either fall 3-19 days after election night (2002, 2006) or land
  in a multi-week gap that swallows election night entirely (2000, 2004). No amount of
  rendering or human-eyes-on-Wayback-UI will fix a capture that was never taken — this
  is a "the crawl didn't happen" problem, not a "the crawl is hard to read" problem, so
  none of these six are marked PARTIAL/needs-render.
- **Non-Wayback options not explored here** (out of scope for this probe but worth a
  future pass if these rows are wanted): (a) NewsBank/San Diego Union-Tribune
  morning-after coverage for a "N ballots counted as of election night" quote — SF's
  newsbank-election-recovery playbook has a rough analog, though UT-San Diego's own
  archive/paywall situation would need separate scoping; (b) CA State Archives or SoS
  physical/PDF Statement-of-Vote records occasionally include an "election night
  reported" column distinct from certified final, worth a targeted check for 2002/2006
  specifically since those two already have a real (if non-night) archived figure to
  cross-check against.
