# Sacramento County, CA — statewide PRIMARY election-night dossier

Scope: 2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05, 2022-06-07, 2024-03-05.
Methodology: `docs/research/RUNBOOK.md` sections 1, 5-8; `researching-election-night-share` skill.
Metric: election-night % = ballots in the LAST report posted election night / certified final (CA SoS SoV).

## Adoption context (from data/research/county-tech/sacramento-ca.json)

- epollbook: adopted 2018, first_election "2018-06" — i.e. the county-tech record
  ALREADY states the June 5, 2018 statewide primary was the first VCA vote-center +
  e-pollbook election (evidence: county EAP, "The County of Sacramento was the
  largest of five pilot counties to adopt the VCA for the 2018 elections"; first
  VCA election = June 5, 2018 primary). So 2018-06-05 is classed POST for
  vs_epollbook. 2012/2014/2016 primaries are PRE. 2022/2024 primaries are POST.
- ASV: never adopted (vs_asv = "n/a" for all rows).

## Denominators (CA SoS Statement of Vote, Voter Participation Statistics by County)

| date | election | Total Voters (certified final) | source URL |
|---|---|---|---|
| 2012-06-05 | Presidential Primary | 232,743 | https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/2012-complete-sov.pdf (p.238 of pdftotext -layout output, "VOTER PARTICIPATION STATISTICS BY COUNTY" table; no standalone participation-stats PDF exists for 2012 primary, 403s individually, so used the complete SOV PDF) |
| 2014-06-03 | Statewide Direct Primary | 203,850 | https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf (misspelling "particpiation" intact, matches 2014-general convention) |
| 2016-06-07 | Presidential Primary | 340,360 | https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf |
| 2018-06-05 | Statewide Direct Primary | 310,881 | https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf |
| 2022-06-07 | Statewide Direct Primary | 336,014 | https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf |
| 2024-03-05 | Presidential Primary | 346,502 | https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf |

Each "Total Voters" figure = Precinct Voters + Vote-By-Mail Voters column in the SoS table (verified
arithmetic matches printed Total Voters column in every case). Sacramento county line context (Precincts /
Eligible / Registered / Precinct / VBM / Total / %VBM / %Reg-turnout / %Elig-turnout):
- 2012: 1,041 / 941,160 / 653,391 / 71,640 / 161,103 / 232,743 / 69.22% / 35.62% / 24.73%
- 2014: 1,102 / 957,597 / 688,443 / 57,425 / 146,425 / 203,850 / 71.83% / 29.61% / 21.29%
- 2016: 1,172 / 984,952 / 715,975 / 112,023 / 228,337 / 340,360 / 67.09% / 47.54% / 34.56%
- 2018: 573 / 1,009,125 / 741,260 / 18,104 / 292,777 / 310,881 / 94.18% / 41.94% / 30.81%
- 2022: 630 / 1,113,693 / 864,575 / 11,435 / 324,579 / 336,014 / 96.60% / 38.86% / 30.17%
- 2024: 620 / 1,110,422 / 869,219 / 17,774 / 328,728 / 346,502 / 94.87% / 39.86% / 31.20%

---

(Per-primary numerator research appended below, one item at a time.)

---

## ITEM 1 of 6: 2012-06-05 Presidential Primary

**Certified final:** 232,743 (CA SoS SoV, "VOTER PARTICIPATION STATISTICS BY COUNTY" table,
Sacramento line: Precincts 1,041 / Eligible 941,160 / Registered 653,391 / Precinct Voters
71,640 / VBM Voters 161,103 / **Total Voters 232,743** / 69.22% VBM / 35.62% of registered /
24.73% of eligible). Source: https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/2012-complete-sov.pdf
(no standalone "03-voter-participation-stats-by-county.pdf" exists for the 2012 primary — that
exact filename 403s; the county line lives inside the complete SOV PDF's own "Voter Participation
Statistics by County" table, `pdftotext -layout` line 238 of that document).

**Numerator (election-night plateau): NULL.** All three ranked routes exhausted:

1. **Route 1 (registrar semi-final press release):** the modern MediaRoom/Pages/PressReleases.aspx
   archive used for 2016+ general research **did not exist in 2012** — CDX confirms its earliest
   capture anywhere is 2013-08-01 (`https://web.archive.org/web/20130801022828/http://www.elections.saccounty.net/MediaRoom/Pages/PressReleases.aspx`).
   The 2012-era site ran on a different CMS (`elections.saccounty.net/coswcms/groups/public/@wcm/@pub/@pio/...`);
   a domain-wide CDX sweep (`matchType=domain`, 2012-01-01 to 2012-12-31) shows the site was
   crawled only on 2012-01-20, 02-10, 02-13, 02-14, 04-01, 10-08, 10-12, 12-01 — no crawl in the
   May-September window that would catch a June primary press release, and a targeted prefix CDX
   of the `.../documents/pressrelease/` directory across 2012-05-01..2012-12-31 returned zero rows.
2. **Route 2/4 (eresults.saccounty.net dated report / Wayback of live results page):** CDX of the
   exact root URL `http://www.eresults.saccounty.net/` across all of 2012 shows only 4 captures:
   2012-02-13, 2012-03-08, 2012-05-22 (all identical digest `PM23CA26...`, a pre-election
   placeholder/setup page, 2,773-2,930 bytes) and 2012-11-09 (the general-election capture already
   used in the general-election row). **Zero captures exist between 2012-05-22 and 2012-11-09** —
   the crawler simply never visited the site during the June primary window (confirmed both with
   an exact-URL CDX for 2012-06-05..2012-06-15, which returned only two `/robots.txt` hits on
   06-05 and 06-11 and no homepage capture, and a `matchType=prefix` sweep of the whole
   `eresults.saccounty.net` host for 2012-05-01..2012-07-15, same result). The Hart "SUMMARY
   REPORT" system is known to have been live on this exact URL by the November 2012 general (see
   that row's note), so the primary's report almost certainly existed at the time, but no
   Wayback snapshot captured it.
3. **Route 6 (Sacramento Bee via Wayback):** `sacbee.com` homepage was crawled repeatedly
   2012-06-05 through 2012-06-09 (CDX confirms ~20 homepage snapshots), and article-level CDX for
   `sacbee.com/2012/06/05`, `/06/06`, `/06/07`, `/06/08` (prefix match) was pulled and every
   article slug inspected for election/turnout/ballot/vote/poll/county/registrar keywords. Results:
   06/05 = pre-election pieces only ("Field Poll predicting low turnout", Dan Walters column on the
   primary, an opinion piece) with no post-election numbers; 06/06 = "California voters mixed
   about...", "Calif voters OK term limits change", "2 California cities voters embrace..." (all
   statewide/other-city ballot-measure pieces, not a Sacramento County ballots-counted figure);
   06/07 CDX returned zero article rows; 06/08 = "South Sacramento County to get...", "Spending in
   Wisconsin recall election", "Yolo County farm..." (unrelated). No article states a Sacramento
   County ballots-processed/counted total for election night or the following days.

No candidate for the plateau number survives any route. Per RUNBOOK 5.1, this is `null` with the
searched routes documented above, not a substituted denominator or report time.

### Draft row (data/research/election-night/sacramento-ca.json schema)

```json
{
  "date": "2012-06-05",
  "type": "presidential-primary",
  "election_night_ballots": null,
  "certified_final": 232743,
  "election_night_pct": null,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/2012-complete-sov.pdf",
  "source_url_night": null,
  "confidence": "none",
  "note": "Election-night plateau NOT sourceable for the 2012 presidential primary -- all three numerator routes exhausted. (1) PRESS RELEASE: the MediaRoom/Pages/PressReleases.aspx archive used for later years did not exist yet (earliest Wayback capture of that URL is 2013-08-01); the 2012-era coswcms site was crawled only Jan/Feb/Apr/Oct/Dec 2012, with no capture in the May-Sept window and zero rows in a targeted CDX prefix sweep of its pressrelease document directory for 2012-05-01..2012-12-31. (2) ERESULTS.SACCOUNTY.NET: root-URL CDX for all of 2012 shows only 4 captures -- 2012-02-13/03-08/05-22 (identical-digest pre-election placeholder page) and 2012-11-09 (the general-election capture already used elsewhere in this file); zero captures 2012-05-22 to 2012-11-09, confirmed by both an exact-URL CDX for the primary window (only two /robots.txt hits, no homepage) and a matchType=prefix sweep of the whole host for 2012-05-01..2012-07-15. The Hart SUMMARY REPORT system verified live on this URL by Nov 2012 almost certainly ran the June primary too, but Wayback never crawled it during that window. (3) SACRAMENTO BEE: sacbee.com homepage crawled repeatedly 6/5-6/9/2012; article-level CDX for 2012/06/05 through 2012/06/08 inspected -- pre-election turnout-prediction and opinion pieces (6/5), statewide ballot-measure pieces (6/6), unrelated local pieces (6/8), zero rows (6/7); no article states a Sacramento County ballots-counted total. Denominator = CA SoS Statement of Vote, 2012 Presidential Primary, Voter Participation Statistics by County table (embedded in the complete SOV PDF, no standalone participation-stats PDF exists for this election), Sacramento Total Voters 232,743 (Precinct 71,640 + Vote-By-Mail 161,103; Registered 653,391; Eligible 941,160). Pre-epollbook (adopted June 2018). ASV never adopted."
}
```

### VERIFY.md draft line

Summary table cell: `| 2012-06-05 | NULL | -- | none |` (mirrors the existing 2016-11-08 NULL row style).
Detail bullet: "2012-06-05 presidential primary: election-night ballots NULL (all routes exhausted:
no press-release archive existed yet, zero Wayback captures of eresults.saccounty.net during the
primary window, no Sacramento Bee article states a total). Certified final 232,743 -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2012-primary/pdf/2012-complete-sov.pdf. Look for: any
surviving June 2012 eresults.saccounty.net snapshot or a semi-final press release PDF not indexed
by CDX."

### Plateau verdict

**N/A (null row) — no verdict entry needed** (plateau_review.json only carries verdicts for
sourced rows per RUNBOOK 3/5.5). Confidence: none. Evidence class: null-per-5.1, fully documented
route exhaustion.

---

## ITEM 2 of 6: 2014-06-03 Statewide Direct Primary

**Certified final:** 203,850 (CA SoS SoV Voter Participation Statistics by County, Sacramento line:
Precincts 1,102 / Eligible 957,597 / Registered 688,443 / Precinct Voters 57,425 / VBM Voters
146,425 / **Total Voters 203,850** / 71.83% VBM / 29.61% of registered / 21.29% of eligible).
Source: https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf
(misspelling "particpiation" intact, same convention as the 2014 general).

**Numerator (election-night plateau): CEILING ONLY, comparable=false.** Route 2/4 (eresults
dated report / Wayback of the live results page) is the only route that surfaces a number at all:
a `matchType=prefix` CDX sweep of the whole `eresults.saccounty.net` host for 2014-05-25..2014-06-15
returns exactly ONE capture in the entire window: `20140610002504` of
`http://www.eresults.saccounty.net:80/`. Fetched via `id_` raw replay (not gzip this time), it
embeds the Hart "SUMMARY REPORT," labeled **SEMIOFFICIAL**, **Run Date: 06/06/14, RUN TIME: 12:44 PM**
-- i.e. 3 days AFTER the election (Tue June 3), not an election-night timestamp -- with PRECINCTS
COUNTED 1,102 of 1,102 (100.00%), REGISTERED VOTERS - TOTAL 688,443, **BALLOTS CAST - TOTAL 140,521**,
VOTER TURNOUT - TOTAL 20.41% (arithmetic checks: 140,521/688,443 = 20.41%, matches). This is a
mid-canvass report, not the true midnight-of-election-night plateau; no earlier (election-night or
next-morning) capture of this URL survives anywhere in Wayback for this election. Because the
report is dated 3 days post-election it necessarily includes some canvass ballots processed after
election night, so 140,521 OVERSTATES the true election-night plateau -- kept as a documented
CEILING per RUNBOOK 5.2, not the metric itself. 140,521 / 203,850 = 68.93%, notably higher than the
clean 2014 GENERAL election-night share (59.04%) for the same county under the same pre-VCA
counting system, consistent with this being a several-days-later, canvass-boosted figure rather
than the night-of number.

Additional routes checked and exhausted:
- **Route 1 (press release):** `elections.saccounty.net/MediaRoom/Pages/PressReleases.aspx` has
  zero Wayback captures in 2014-05-25..2014-06-20 (repeated retries, all empty). A domain-wide CDX
  sweep of `elections.saccounty.net` for the same window turned up two other MediaRoom PDFs
  crawled 2014-06-11 (`Documents/sac_004950.pdf`, `sac_004951.pdf`) but both are unrelated CACEO/CERA
  professional-certification handouts, not election-night releases; and the `MediaRoom/Pages/default.aspx`
  landing page (captured 2014-06-07) is a navigation shell only, no release text or numbers rendered
  in the static HTML.
- **Route 6 (Sacramento Bee):** not exhaustively re-run for 2014 given the 2012 and 2016 precedents
  in this same dossier/dataset both turned up nothing county-specific; not pursued further to stay
  within the per-election time budget. FLAG for manual operator: a human search of sacbee.com's own
  archive or a NewsBank/ProQuest pull for "Sacramento County" + "ballots" the week of June 3-6, 2014
  could still recover the true election-night total that Wayback missed.

### Draft row

```json
{
  "date": "2014-06-03",
  "type": "statewide-primary",
  "election_night_ballots": 140521,
  "certified_final": 203850,
  "election_night_pct": 68.93,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20140610002504/http://www.eresults.saccounty.net:80/",
  "confidence": "secondary",
  "comparable": false,
  "note": "CEILING, not the plateau metric (RUNBOOK 5.2). Only one Wayback capture of eresults.saccounty.net survives anywhere near this election (matchType=prefix CDX sweep of the whole host for 2014-05-25..2014-06-15 returns exactly one row): 20140610002504, embedding the Hart SUMMARY REPORT labeled SEMIOFFICIAL, Run Date 06/06/14, RUN TIME 12:44 PM -- three days AFTER election day (Tue June 3), not an election-night timestamp. PRECINCTS COUNTED 1,102 of 1,102 (100%), BALLOTS CAST - TOTAL 140,521, REGISTERED VOTERS 688,443, VOTER TURNOUT 20.41% (140,521/688,443 checks). No earlier (election-night or next-morning) capture of this URL exists in Wayback for this election, and no morning-after press release survives either (PressReleases.aspx has zero captures 2014-05-25..2014-06-20; two other MediaRoom PDFs crawled 2014-06-11 are unrelated CACEO/CERA training handouts). Because this SEMIOFFICIAL report is dated 3 days post-election it necessarily includes canvass ballots processed after election night, so 140,521 overstates the true election-night plateau -- recorded as a CEILING (comparable: false), not the metric. 140,521 / 203,850 certified = 68.93%, notably above the clean 2014 GENERAL election-night share for this county (59.04%, same pre-VCA counting system), consistent with a several-days-later, canvass-boosted number. Pre-epollbook (adopted June 2018). ASV never adopted. FLAG for manual operator: a NewsBank/library search of Sacramento Bee coverage for June 3-6, 2014 could recover the true election-night total that Wayback did not capture."
}
```

### VERIFY.md draft line

Summary table cell: `| 2014-06-03 ⚠️ | 140,521 | 68.93% | secondary |` (ceiling flag, mirrors Riverside
2024 / Santa Clara 2014 / Placer 2018 style in the existing VERIFY.md).
Detail bullet: "2014-06-03 statewide primary: CEILING ONLY (comparable=false) -- eresults.saccounty.net
SEMIOFFICIAL report dated Run Date 06/06/14 12:44 PM (3 days post-election, the only surviving
capture in the window), Ballots Cast 140,521 of 203,850 certified = 68.93%. True election-night
plateau not recovered; treat as an upper bound. Certified final -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2014-primary/pdf/03-voter-particpiation-stats-by-county.pdf.
Look for: any Sacramento Bee or press-release mention of a June 3-4, 2014 ballots-counted total."

### Plateau verdict (plateau_review.json)

**REFUTED_AS_PLATEAU** (kept as documented ceiling per 5.2, not a plateau claim). Basis: the
report explicitly self-identifies as SEMIOFFICIAL with an internal Run Date 3 days after the
election, i.e. it fails the "late-night internal timestamp" self-description test in RUNBOOK
section 8 outright -- it was never asserted as CONFIRMED/PLAUSIBLE plateau evidence in the first
place, so this is filed as a ceiling data point, not a refuted plateau claim.

---

## ITEM 3 of 6: 2016-06-07 Presidential Primary

**Certified final:** 340,360 (CA SoS SoV Voter Participation Statistics by County, Sacramento line:
Precincts 1,172 / Eligible 984,952 / Registered 715,975 / Precinct Voters 112,023 / VBM Voters
228,337 / **Total Voters 340,360** / 67.09% VBM / 47.54% of registered / 34.56% of eligible).
Source: https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf

**Numerator (election-night plateau): CEILING ONLY, comparable=false, and CONFIRMED still moving
(not the plateau).** The domain moved from `www.eresults.saccounty.net` (http) to
`eresults.saccounty.net` (https, no www) right around this election (CDX shows the http root as an
unchanging pre-election placeholder digest through 2016-06-03, then a 302 redirect, then nothing
further on that host except one more stale revisit on 2016-06-20). The https root has exactly TWO
real content captures near the election: `20160611133801` and `20160620220131`. Both embed the Hart
"SUMMARY REPORT," both labeled **SEMI-OFFICIAL**:
- `20160611133801` -> internal **RUN DATE: 06/10/16, RUN TIME: 02:31 PM** (3 days post-election) --
  PRECINCTS COUNTED 1,172 of 1,172 (100%), REGISTERED VOTERS 715,993, **BALLOTS CAST - TOTAL 230,234**,
  VOTER TURNOUT 32.16% (230,234/715,993 checks).
- `20160620220131` -> internal **RUN DATE: 06/17/16, RUN TIME: 01:53 PM** (10 days post-election) --
  same precincts, **BALLOTS CAST - TOTAL 297,409** (up from 230,234).

The two captures prove the count was STILL CLIMBING between June 10 and June 17 (230,234 ->
297,409, a 29% increase), i.e. neither is frozen/plateaued and neither is anywhere near
election-night. This directly matches the registrar's own posting schedule recovered from the
`MediaRoom/Pages/PressReleases.aspx` archive (one capture, 2016-06-17): a series of "Presidential
Primary Election Update" bulletins titled "Ballot Count Update(s) to be Released on Friday, June 10"
(posted June 9) and "...Wednesday, June 15 and Friday, June 17" (posted June 14) -- i.e. by 2016 the
county had moved to a scheduled Wed/Fri POST-election canvass-update cadence rather than a live
election-night feed, and Wayback never captured anything from the June 7 night or June 8-9 morning.
Exactly as with the 2016 GENERAL row already in this dataset (also null, also "no Nov 8-evening/
Nov 9-morning capture... only a Friday canvass figure"), the 2016 primary numerator is not
recoverable as a true plateau. The earliest available post-night number, 230,234 (June 10 report),
is kept as a documented CEILING (closest to the election but still 3 days out and PROVEN not-frozen
by the later 297,409 capture) -- 230,234 / 340,360 = 67.64%.

Press releases themselves (route 1) never state a ballot number, only the release schedule (same
pattern as every other year checked in this dataset for Sacramento); route 6 (Sacramento Bee) not
separately re-run for this item given the 2012/2014 precedents in this same dossier and the fact
that a same-source, better-dated (June 10) official number already exists as the best available
ceiling.

### Draft row

```json
{
  "date": "2016-06-07",
  "type": "presidential-primary",
  "election_night_ballots": 230234,
  "certified_final": 340360,
  "election_night_pct": 67.64,
  "vs_epollbook": "pre",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20160611133801/https://eresults.saccounty.net/",
  "confidence": "secondary",
  "comparable": false,
  "note": "CEILING, not the plateau metric (RUNBOOK 5.2), and PROVEN still-moving. The eresults.saccounty.net root migrated to https around election day; only two real-content Wayback captures survive near this election, both labeled SEMI-OFFICIAL: 20160611133801 embeds RUN DATE 06/10/16 RUN TIME 02:31 PM (3 days post-election), BALLOTS CAST - TOTAL 230,234 of 715,993 registered (32.16% turnout, checks); 20160620220131 embeds RUN DATE 06/17/16 RUN TIME 01:53 PM (10 days post-election), BALLOTS CAST - TOTAL 297,409 -- a 29% increase over the prior capture, proving the count was still climbing and neither report is a frozen plateau. No election-night (June 7 evening) or next-morning (June 8-9) capture exists anywhere in Wayback for this URL. The registrar's own MediaRoom/Pages/PressReleases.aspx archive (captured 2016-06-17) corroborates: bulletins titled 'Presidential Primary Election Update - Ballot Count Update(s) to be Released on Friday, June 10' (posted June 9) and '...Wednesday, June 15 and Friday, June 17' (posted June 14) show the county was on a scheduled post-election canvass-update cadence, not a live election-night feed, by 2016 -- consistent with the already-null 2016 GENERAL row in this same file (also no Nov 8/9 capture, only a Friday canvass figure). Press releases never state a ballot number, only the release schedule. Recorded 230,234 (the earliest, closest-to-election available official figure) as a documented CEILING (comparable: false): 230,234 / 340,360 certified = 67.64%. Pre-epollbook (adopted June 2018). ASV never adopted."
}
```

### VERIFY.md draft line

Summary table cell: `| 2016-06-07 ⚠️ | 230,234 | 67.64% | secondary |`
Detail bullet: "2016-06-07 presidential primary: CEILING ONLY (comparable=false) -- earliest
surviving eresults.saccounty.net SEMI-OFFICIAL report, Run Date 06/10/16 (3 days post-election),
Ballots Cast 230,234 of 340,360 certified = 67.64%; a later June 17 capture shows 297,409, proving
the count was still climbing and this is not a plateau. No election-night capture survives. Certified
final -- SoS SoV https://elections.cdn.sos.ca.gov/sov/2016-primary/03-voter-participation-stats-by-county.pdf.
Look for: any June 7-9, 2016 capture of eresults.saccounty.net or a numbered semi-final press release."

### Plateau verdict (plateau_review.json)

**REFUTED_AS_PLATEAU.** Basis: independent leg present and DISPROVES plateau status outright -- a
second, later capture of the same URL (20160620220131, Run Date 06/17/16) shows the count moved
from 230,234 to 297,409, which is exactly the "later capture... shows the number moved" warning
sign in RUNBOOK 6.5/8 (the opposite of the "still shows the identical count" CONFIRMED pattern).
Kept as a documented ceiling only, not a plateau claim.

---

## ITEM 4 of 6: 2018-06-05 Statewide Direct Primary -- THE VCA/E-POLLBOOK ROLLOUT ELECTION

**ROLLOUT-TIMING FINDING (answers the task's explicit question):** `data/research/county-tech/sacramento-ca.json`
already resolves this: the `vote-center` and `epollbook` tech records both give
`"adopted_year": 2018, "first_election": "2018-06"`, evidenced by the county's own Election
Administration Plan: "The County of Sacramento was the largest of five pilot counties to adopt the
VCA for the 2018 elections... First VCA election = June 5, 2018 statewide primary." **The June 5,
2018 primary itself was the rollout election** -- Sacramento switched to VCA vote centers +
networked e-pollbook check-in (DFM Associates EIMS) for this exact primary, not starting with the
November 2018 general. This row is therefore classed **POST** for `vs_epollbook` (the earliest
POST-adoption row in the whole primaries series), matching the task's framing.

**Certified final:** 310,881 (CA SoS SoV Voter Participation Statistics by County, Sacramento line:
Precincts 573 / Eligible 1,009,125 / Registered 741,260 / Precinct Voters 18,104 / VBM Voters
292,777 / **Total Voters 310,881** / 94.18% VBM / 41.94% of registered / 30.81% of eligible).
Source: https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf
(cross-checked: the certified-state capture of eresults.saccounty.net from 2018-07-09, see below,
independently shows "Registered Voters: 310,881 of 740,537" i.e. the same 310,881 figure, exact
match).

**Numerator (election-night plateau): CONFIRMED via a clean held-flat-then-jumped bracket on the
`sacresults.e-cers.com` VCA-era results app** (this is the app that replaced/supplemented the old
Hart eresults.saccounty.net page for the VCA rollout -- eresults.saccounty.net itself has NO
captures at all between the pre-election Jun 3-4 subresource crawls and a single Jul 9 "FINAL"
capture, so it is not usable here). CDX of `sacresults.e-cers.com` (matchType=domain,
2018-05-20..2018-08-01) surfaces three `Default.aspx` captures in the days after the election:

- `20180607104634` (crawled Thu Jun 7, 10:46 AM) -- page title "Unofficial 2018 Primary Election
  June 5, 2018", Precincts Reported 100.0%, Voter Turnout displayed 16.83%, and critically the raw
  page HTML has a hidden field `id="hidVoterTurnout" value="124609"` -- the actual ballots-cast
  count baked directly into the page (not an AJAX-only value, unlike the 2016 general's version of
  this same app). The page also states "**Results Last Updated 6/6/2018 2:25:56 PM**" -- i.e. the
  Wednesday afternoon after the Tuesday election, with no canvass yet resumed (matches RUNBOOK
  section 1's allowance for a same/next-day-morning report so long as it is the continuous
  election-night count, e.g. the San Bernardino 2024 10 a.m.-Wednesday precedent).
- `20180609235727` (crawled Sat Jun 9) -- `hidVoterTurnout` now **154,435**, a materially higher
  number: proves a NEW report was posted between Jun 7 and Jun 9 (the canvass had resumed and moved
  past the Jun 6 figure).
- `20180708170109` (crawled Jul 8) -- `hidVoterTurnout` = **310,881**, exactly the certified final
  (confirms the app's field is the right one to trust, and that this is simply the fully-certified
  end state).

The bracket: 124,609 (stamped "Last Updated 6/6/2018 2:25:56 PM") is the number BEFORE any later,
higher report existed (the Jun 9 capture proves the next report was materially different, i.e. the
Jun 6 figure was NOT a live-updating counter that just happened to be crawled mid-tick -- it was a
static, held report that got superseded days later). This is the RUNBOOK section 8 gold-standard
combination: a self-describing "Results Last Updated" timestamp for a specific report PLUS a later
capture proving that exact report was superseded by a different, higher count. 124,609 / 310,881 =
40.08%.

### Draft row

```json
{
  "date": "2018-06-05",
  "type": "statewide-primary",
  "election_night_ballots": 124609,
  "certified_final": 310881,
  "election_night_pct": 40.08,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20180607104634/http://sacresults.e-cers.com/default.aspx",
  "confidence": "primary",
  "note": "PLATEAU metric, held-flat-then-jumped bracket (RUNBOOK 8). This is the VCA/e-pollbook ROLLOUT election: county-tech record (data/research/county-tech/sacramento-ca.json) gives vote-center + epollbook adopted_year 2018, first_election '2018-06' -- the June 5, 2018 primary was the FIRST VCA/e-pollbook election, so this row is POST, the earliest post-adoption point in the primaries series. eresults.saccounty.net has no captures for this election (only pre-election subresource crawls Jun 3-4 and a single certified-FINAL capture Jul 9); the numerator instead comes from the sacresults.e-cers.com VCA-era results app. Capture 20180607104634 (crawled Thu Jun 7 10:46 AM) is titled 'Unofficial 2018 Primary Election June 5, 2018', 100.0% precincts reported, and carries a hidden field id=hidVoterTurnout value=124609 (the actual ballots-cast count embedded in the static page, not AJAX-only) plus 'Results Last Updated 6/6/2018 2:25:56 PM' (Wednesday afternoon after the Tuesday election, canvass not yet resumed). A later capture (20180609235727, Sat Jun 9) shows hidVoterTurnout=154,435, a materially higher number, proving a new report superseded the Jun 6 figure between Jun 7 and Jun 9 -- i.e. 124,609 was a genuine held report, not a live-ticking counter caught mid-update. A third capture (20180708170109, Jul 8) shows hidVoterTurnout=310,881, exactly the certified final, confirming the field is trustworthy. 124,609 / 310,881 certified = 40.08% (consistent in magnitude with the November 2018 general's post-adoption election-night share of 35.52% for the same county). Denominator = CA SoS Voter Participation Statistics by County, Sacramento Total Voters 310,881 (Precinct 18,104 + VBM 292,777); independently cross-checked against the eresults.saccounty.net Jul 9 FINAL capture, which shows the identical 310,881 (mislabeled 'Registered Voters: 310,881 of 740,537', the same mislabel pattern documented for 2018 in RUNBOOK 7.5). ASV never adopted."
}
```

### VERIFY.md draft line

Summary table cell: `| 2018-06-05 | 124,609 | 40.08% | primary |`
Detail bullet: "2018-06-05 statewide primary (THE VCA/e-pollbook rollout election -- first_election
2018-06 per county-tech record): sacresults.e-cers.com Default.aspx, hidden field hidVoterTurnout,
124,609 as of 'Results Last Updated 6/6/2018 2:25:56 PM', held flat through the Jun 7 10:46 AM
crawl, then superseded by 154,435 in a Jun 9 capture (bracket proof). 124,609 / 310,881 certified =
40.08%. Certified final -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2018-primary/sov/03-voter-participation-stats-by-county.pdf.
Look for: the hidVoterTurnout hidden-field value in the cited Wayback capture's raw HTML."

### Plateau verdict (plateau_review.json)

**CONFIRMED.** Basis: self-describing "Results Last Updated 6/6/2018 2:25:56 PM" timestamp for a
same/next-day, pre-canvass-resumption report (RUNBOOK section 1's allowed window) PLUS the
independent, non-circular leg required by section 8 -- a later capture of the same URL (Jun 9)
shows the value moved to a materially different, higher number, proving the Jun 6 report was a
real, held state that was later superseded rather than a stale rendering artifact. A third capture
(Jul 8) independently validates the field by matching the certified final exactly.

---

## ITEM 5 of 6: 2022-06-07 Statewide Direct Primary

**Certified final:** 336,014 (CA SoS SoV Voter Participation Statistics by County, Sacramento line:
Precincts 630 / Eligible 1,113,693 / Registered 864,575 / Precinct Voters 11,435 / VBM Voters
324,579 / **Total Voters 336,014** / 96.60% VBM / 38.86% of registered / 30.17% of eligible).
Source: https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf

**Numerator (election-night plateau): CONFIRMED, clean report-series bracket.** CDX of
`eresults.saccounty.net` (matchType=prefix, 2022-06-01..2022-06-15) shows exactly two homepage
captures, both on Jun 8 -- `20220608172305` (10:23 AM PT) and `20220608211304` (2:13 PM PT) -- with
the IDENTICAL digest (`HMCR4P2QCTHUFJUUH4TJRKDXN2FAH4NA`), i.e. the page held flat across that
~4-hour span. Fetched via `id_` raw replay, it embeds the modern "ElectionSummaryReportRPT" with an
internal page-generation stamp **6/8/2022 12:08:32 AM** (just after midnight the night of the
election, the classic Sacramento election-night pattern seen in every general-election row in this
dataset) and the label **"Sacramento County 2022 June Primary Election June 7, 2022 SEMI-FINAL
Voters Cast: 107,601 of 864,181 (12.45%)"** (107,601/864,181 = 12.45%, checks). The next CDX-visible
capture of this URL is `20220622225426`, 14 DAYS later, with a materially different digest --
satisfying RUNBOOK section 8's "report series' next file being days later" corroborating leg
outright (the classic bracket: same content held same-day, then a much-later capture proves it was
eventually superseded, i.e. it was a genuine frozen report, not a stuck cache). 107,601 / 336,014 =
32.02%.

### Draft row

```json
{
  "date": "2022-06-07",
  "type": "statewide-primary",
  "election_night_ballots": 107601,
  "certified_final": 336014,
  "election_night_pct": 32.02,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20220608172305/https://eresults.saccounty.net/",
  "confidence": "primary",
  "note": "PLATEAU metric (final election-night report, not the 8 p.m. first tranche). eresults.saccounty.net CDX (matchType=prefix, 2022-06-01..2022-06-15) shows two homepage captures, both Jun 8 (10:23 AM and 2:13 PM PT), identical digest -- held flat across that span. The embedded ElectionSummaryReportRPT carries internal page-generation stamp 6/8/2022 12:08:32 AM (just after midnight election night) and label 'Sacramento County 2022 June Primary Election June 7, 2022 SEMI-FINAL Voters Cast: 107,601 of 864,181 (12.45%)' (107,601/864,181 = 12.45%, checks). The next CDX-visible capture of this URL is 14 days later (20220622225426) with a different digest, satisfying the report-series-next-file-days-later plateau leg (RUNBOOK 8): the Jun 8 SEMI-FINAL report was a genuine frozen state, later superseded by the canvass. 107,601 / 336,014 certified = 32.02%. Denominator = CA SoS Voter Participation Statistics by County, Sacramento Total Voters 336,014 (Precinct 11,435 + VBM 324,579). Post-epollbook (VCA vote centers + e-pollbooks since June 2018). ASV never adopted."
}
```

### VERIFY.md draft line

Summary table cell: `| 2022-06-07 | 107,601 | 32.02% | primary |`
Detail bullet: "2022-06-07 statewide primary: eresults.saccounty.net ElectionSummaryReportRPT,
internal stamp 6/8/2022 12:08:32 AM, SEMI-FINAL, Voters Cast 107,601 of 864,181 registered (12.45%),
held flat across two same-day captures then superseded 14 days later. 107,601 / 336,014 certified =
32.02%. Certified final -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2022-primary/sov/03-voter-participation-stats-by-county.pdf.
Look for: 'SEMI-FINAL Voters Cast: 107,601 of 864,181' text in the cited Wayback capture."

### Plateau verdict (plateau_review.json)

**CONFIRMED.** Basis: self-describes as SEMI-FINAL with a just-after-midnight internal generation
timestamp (6/8/2022 12:08:32 AM) PLUS the report-series-next-file-days-later leg (next capture of
the same URL is 14 days later with different content).

---

## ITEM 6 of 6: 2024-03-05 Presidential Primary

**Certified final:** 346,502 (CA SoS SoV Voter Participation Statistics by County, Sacramento line:
Precincts 620 / Eligible 1,110,422 / Registered 869,219 / Precinct Voters 17,774 / VBM Voters
328,728 / **Total Voters 346,502** / 94.87% VBM / 39.86% of registered / 31.20% of eligible).
Source: https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf

**Numerator (election-night plateau): CONFIRMED, the cleanest bracket of all six primaries.** CDX
of `eresults.saccounty.net` (matchType=prefix, 2024-03-05..2024-03-20) shows the homepage first
captured with real content at `20240306092544` (March 6, 1:25 AM PT -- i.e. the small hours right
after election night), digest `LNB7YLSDZG3U3P5NXBYPV4SEGJRSWVBU`. The SAME digest then recurs across
SIX further crawl timestamps through `20240308002038` (March 7 ~4:20 PM PT) -- i.e. it is proven
held flat for roughly 3 days straight -- before a NEW digest (`KJ3DJIHOSJV2NEJAYIHKNQM6DVNAKPD5`)
appears at `20240308234421` (March 8, 3:44 PM PT), which is exactly the canvass-resumption jump
pattern already established for the 2024 GENERAL row in this dataset. Fetched via `id_` raw replay,
the March 6 capture embeds the ElectionSummaryReportRPT with internal page-generation stamp
**3/5/2024 11:47:42 PM** (before midnight election night itself) and the label **"Sacramento County
2024 Presidential Primary Election March 5, 2024 SEMI-FINAL Voters Cast: 118,205 of 868,750
(13.61%)"** (118,205/868,750 = 13.61%, checks). 118,205 / 346,502 = 34.11%.

### Draft row

```json
{
  "date": "2024-03-05",
  "type": "presidential-primary",
  "election_night_ballots": 118205,
  "certified_final": 346502,
  "election_night_pct": 34.11,
  "vs_epollbook": "post",
  "vs_asv": "n/a",
  "source_url_final": "https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf",
  "source_url_night": "https://web.archive.org/web/20240306092544/https://eresults.saccounty.net/",
  "confidence": "primary",
  "note": "PLATEAU metric (final election-night report, not the 8 p.m. first tranche). eresults.saccounty.net CDX (matchType=prefix, 2024-03-05..2024-03-20) shows the homepage first captured with real content at 20240306092544 (March 6, 1:25 AM PT); the identical digest then recurs across six further crawl timestamps through 20240308002038 (~4:20 PM PT March 7), i.e. the report is proven held flat for roughly 3 days, before a new digest appears at 20240308234421 (March 8, 3:44 PM PT) -- the canvass-resumption jump, matching the same pattern already documented for the 2024 GENERAL row in this file. The embedded ElectionSummaryReportRPT carries internal page-generation stamp 3/5/2024 11:47:42 PM (before midnight election night) and label 'Sacramento County 2024 Presidential Primary Election March 5, 2024 SEMI-FINAL Voters Cast: 118,205 of 868,750 (13.61%)' (118,205/868,750 = 13.61%, checks). 118,205 / 346,502 certified = 34.11%. Denominator = CA SoS Voter Participation Statistics by County, Sacramento Total Voters 346,502 (Precinct 17,774 + VBM 328,728). Post-epollbook (VCA vote centers + e-pollbooks since June 2018). ASV never adopted."
}
```

### VERIFY.md draft line

Summary table cell: `| 2024-03-05 | 118,205 | 34.11% | primary |`
Detail bullet: "2024-03-05 presidential primary: eresults.saccounty.net ElectionSummaryReportRPT,
internal stamp 3/5/2024 11:47:42 PM, SEMI-FINAL, Voters Cast 118,205 of 868,750 registered (13.61%),
held flat across seven captures spanning ~3 days before the canvass-resumption jump on March 8.
118,205 / 346,502 certified = 34.11%. Certified final -- SoS SoV
https://elections.cdn.sos.ca.gov/sov/2024-primary/sov/03-voter-participation-stats-by-county.pdf.
Look for: 'SEMI-FINAL Voters Cast: 118,205 of 868,750' text in the cited Wayback capture."

### Plateau verdict (plateau_review.json)

**CONFIRMED.** Basis: self-describes as SEMI-FINAL with a before-midnight internal generation
timestamp (3/5/2024 11:47:42 PM) PLUS the strongest available corroborating leg -- the identical
digest recurs across seven separate crawls spanning three days, then a later capture shows a
different digest (the canvass-resumption jump), exactly matching the section 8 "later capture...
still showing the same count" + "next file is days later" legs simultaneously.

---

## Summary table (draft, for VERIFY.md)

| date | type | election-night ballots | certified final | pct | vs_epollbook | confidence | evidence class |
|---|---|---:|---:|---:|---|---|---|
| 2012-06-05 | presidential-primary | NULL | 232,743 | NULL | pre | none | null-per-5.1 (all routes exhausted) |
| 2014-06-03 | statewide-primary | 140,521 | 203,850 | 68.93% ⚠️ | pre | secondary | ceiling (comparable=false) |
| 2016-06-07 | presidential-primary | 230,234 | 340,360 | 67.64% ⚠️ | pre | secondary | ceiling (comparable=false), proven still-moving |
| 2018-06-05 | statewide-primary | 124,609 | 310,881 | 40.08% | post (ROLLOUT election) | primary | CONFIRMED, held-flat-then-jumped bracket |
| 2022-06-07 | statewide-primary | 107,601 | 336,014 | 32.02% | post | primary | CONFIRMED, report-series-days-later bracket |
| 2024-03-05 | presidential-primary | 118,205 | 346,502 | 34.11% | post | primary | CONFIRMED, 3-day held-flat + canvass-jump bracket |

Like-for-like presidential-primary comparison: 2016 pre (ceiling only) 67.64% vs 2024 post 34.11% --
same caveat as the generals in this dataset: the drop coincides with the 2018 VCA all-mail switch
(simultaneous with e-pollbook adoption), so it is not a clean single-variable test of e-pollbooks
alone. Like-for-like statewide-midterm-style primary comparison: 2014 pre (ceiling only) 68.93% vs
2018 post (the rollout year itself) 40.08% vs 2022 post 32.02% -- same direction and similar
magnitude to the collapse already documented for the November generals (59.04% pre -> 35.52%/29.94%
post). The two PRE rows (2014, 2016) are both ceilings/upper-bounds, not confirmed plateaus, so the
"pre" side of this comparison is weaker evidence than the "post" side (2018/2022/2024 are all
CONFIRMED plateaus); the true pre-adoption primary share may be somewhat LOWER than the recorded
ceilings, which if anything would make the measured pre/post collapse even less certain to be a
real, larger gap than shown (or could narrow it) -- flagged for the human's judgment, not resolved
by this pass.

