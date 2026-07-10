# Nevada County CA tech adjudication — 2016 BOS purchase + Diaz e-pollbook statement

Task: adjudicate two contradicting pieces of evidence vs the committed record at
`data/research/county-tech/nevada-ca.json` (epollbook adopted_year=2018 via VCA,
asv adopted_year=2022). Source dossier:
`scratchpad/dossier-nevada-ca-primaries.md` "FLAGS for the operator" (lines 577-656).
READ-ONLY pass -- no repo writes made. Repo checked out at
`/Users/sbuss/workspace/sf-election-count/.claude/worktrees/cozy-leaping-wreath`.

Committed record as of start:
- epollbook: adopted_year 2018, first_election 2018-06, vendor "Provista ViBE"
  (current SoS listing), confidence primary. Tied to first VCA election.
- asv: adopted_year 2022, first_election "", vendor unknown, confidence
  secondary, documented LOWER BOUND from a Mail Ballot Processing Infographic
  archived by 2023-06-05.
- `ca_adoption_census.json` Nevada row is NOT independent corroboration --
  explicitly "taken verbatim" from nevada-ca.json (same precedence source).
  No raw EAVS file found in-repo (`find ... -iname "*eavs*"` = empty); EAVS
  cross-check not pursued further given the strength of primary-source
  contract/press evidence found directly (see below) and the 60-min cap.

Panel files with vs_epollbook/vs_asv rows for this county:
- `data/research/election-night/nevada-ca.json` (6 committed Nov-general rows,
  2012/2014/2016/2018/2022/2024)
- `scratchpad/dossier-nevada-ca-primaries.md` (6 DRAFT primary rows, not yet
  committed to the repo: 2012-06-05, 2014-06-03, 2016-06-07, 2018-06-05,
  2022-06-07, 2024-03-05)

---

## FLAG 1: BOS File SR 16-0825 (ES&S MBV 1000 purchase, adopted 9/27/2016)

Locating query: direct fetch of
`https://nevco.legistar.com/LegislationDetail.aspx?GUID=F2AD1997-3E3E-4C30-80F7-21F54318ADDF&ID=2840587`
(the dossier's citation), then followed the page's own attachment links
(`View.ashx?M=F&ID=...`) to the Board Letter and the executed ES&S Agreement
PDF. WebFetch could not OCR the Board Letter (scanned/image PDF, no text
layer -- `pdftotext -layout` returned 0 lines); the Agreement PDF (also
initially returned as binary/encoded by WebFetch) WAS machine-text and was
pulled to disk and read with `pdftotext -layout` at
`scratchpad/agreement-16-0825.pdf` / `scratchpad/agreement.txt`.

**Legistar page itself confirms:**
- Title: "Resolution approving purchase of a Mail Ballot Signature
  Verification Machine from Election Systems & Software, LLC" -- adopted
  (Board action) September 27, 2016.
- "Not to exceed $69,969" (contract net was $57,085 after trade-in credit;
  see Exhibit A below -- Legistar's ceiling figure vs. the executed price
  differ slightly, immaterial to the dating question).
- Trade-in reference: Legistar's search-engine summary paraphrased the
  trade-in as the "Vote Remote" system, but the EXECUTED AGREEMENT'S Exhibit
  A instead itemizes "Trade in of 1 AVES Scanner ($7,500.00)" -- i.e. the
  county already owned SOME kind of automated envelope-handling scanner
  ("AVES") pre-2016. Not pursued further (out of scope / low yield within
  the time cap): AVES's own capabilities (sorting only vs. any signature
  check) were not established, so this does NOT by itself push ASV earlier
  than 2016.

**The executed Agreement (`ES&S / Mail Ballot Verifier, Processing and
Services Agreement`, `scratchpad/agreement.txt`) is the decisive primary
document.** Quoted verbatim, Exhibit B (Equipment/Software/Fees):

> Mail Ballot Verifier System Includes the Following:
> 1  MBV 1000 Transport ... Included
> 1  High Capacity Envelope Feeder ... Included
> ...
> 1  MBV Software with imaging adjustable signature block and barcode scanning ... Included
> 1  "No Signature" Detection ... Included
> 1  Automated Signature Recognition Software ... Included
> 1  DIMS Interface ... Included
> ...
> Election setup support and training- 2016 General Election    $3,150.00

This is not a generic/unscoped training line item -- it is contractually
NAMED for the November 8, 2016 General Election. Exhibit A additionally
states:

> Anticipated Initial Term: 10/1/2016 through 9/31/2017

i.e. the hardware/software maintenance-and-support term itself begins
October 1, 2016, five weeks before the Nov 8 General -- consistent with an
intended go-live for that election, not a purchase left in a box. Estimated
delivery date in Exhibit A is left open ("To Be Agreed To By The Parties"),
which is the one piece of residual uncertainty: the contract shows clear
INTENT to deploy for Nov 2016, but delivery timing was not hard-locked at
signing.

**PURCHASE vs. PRODUCTION USE:** I did not find independent post-election
confirmation (news article, county canvass report, Grand Jury report) that
the MBV 1000 was actually live and processing signatures on Nov 8, 2016.
Targeted searches for this (`"Nevada County" signature verification machine
2016 news`, Grand Jury 2017-2018 report) did not surface it -- the 2017-2018
Grand Jury report exists but its elections section was not reachable in the
search excerpt within the time budget. So the verdict below rests on a
signed, election-dated contractual deliverable (strong contemporaneous
evidence of intended first-use timing) rather than a post-hoc use
confirmation. This is a materially stronger basis than a bare purchase
order, but flag it as the one open loose end if the operator wants to push
further (FOIA/records request for the county's Nov 2016 canvass materials,
or a fuller read of the Grand Jury PDF).

The existing note's claim that "the 2017 Election Administration Plan does
not mention a signature-verification sorter" is real but weak counter-
evidence: the 2017 EAP is scoped to the NEW 2018 VCA vote-center rollout
(precinct consolidation, vote-center logistics) and would not necessarily
re-describe legacy central-office mail-ballot processing equipment already
in continuous use since late 2016.

### Verdict: ASV -- REVISE-TO-2016

Basis: a Board-adopted (9/27/2016), executed ES&S contract for a machine
whose own equipment list includes "Automated Signature Recognition
Software" and "'No Signature' Detection," with a paid line item explicitly
named "Election setup support and training- 2016 General Election" and a
support term starting 10/1/2016 -- all pointing to intended first
production use at the Nov 8, 2016 General Election. Confidence: primary
(signed contract), but not a fully independently-confirmed go-live date
(see loose end above); recommend the operator record this the same way the
existing 2022 asv note recorded its lower bound -- as a documented, strong
first-use year, with the caveat flagged in the note text.

**Row consequences if REVISE-TO-2016 is applied** (adopted_year 2016,
first_election "2016-11"):

Committed general rows (`data/research/election-night/nevada-ca.json`):
| date | old vs_asv | new vs_asv |
|---|---|---|
| 2012-11-06 | pre | pre (unchanged) |
| 2014-11-04 | pre | pre (unchanged) |
| 2016-11-08 | pre | **post (FLIP)** -- this becomes the first-ASV general |
| 2018-11-06 | pre | **post (FLIP)** |
| 2022-11-08 | post | post (unchanged; reasoning changes from "anchor row" to "already post") |
| 2024-11-05 | post (excluded, comparable:false) | post (unchanged; still excluded for the ink-overspray reason) |

Draft primary rows (`scratchpad/dossier-nevada-ca-primaries.md`, not yet
committed):
| date | old vs_asv | new vs_asv |
|---|---|---|
| 2012-06-05 | pre | pre (unchanged, null row) |
| 2014-06-03 | pre | pre (unchanged, null row) |
| 2016-06-07 | pre | pre (unchanged -- predates the 9/27/2016 adoption by 3.5 months, dossier's own flag #3 already anticipated this) |
| 2018-06-05 | pre | **post (FLIP)** |
| 2022-06-07 | post (provisional) | post (unchanged, now CONFIRMED rather than provisional) |
| 2024-03-05 | post | post (unchanged) |

Net: 3 rows flip pre->post (2016-11-08 general, 2018-11-06 general,
2018-06-05 primary); the 2022-06-07 primary's previously-provisional "post"
becomes solid; top-level `adoption.asv` in both `county-tech/nevada-ca.json`
and `election-night/nevada-ca.json` should move from 2022 to 2016.

---

## FLAG 2: Clerk-Recorder Gregory Diaz's June 7, 2016 "E-Poll Books" statement

The dossier's cited URL 404'd both live and via a direct Wayback guess (the
capture is filed under a DIFFERENT, `.php`-suffixed, mixed-case URL than the
dossier's citation). Located the real capture via the CDX API directly
(`http://web.archive.org/cdx/search/cdx?url=yubanet.com&matchType=domain&filter=urlkey:.*poll-book.*&output=json`),
which returned:
`com,yubanet)/regional/greg-diaz-despite-e-poll-book-glitch-your-vote-will-be-counted.php`
at timestamp `20160609140926`, original
`http://yubanet.com/regional/Greg-Diaz-Despite-E-Poll-book-glitch-your-vote-will-be-counted.php`.
`WebFetch` refuses `web.archive.org` in this environment; pulled the raw
capture with `curl` (`.../web/20160609140926if_/...`) to
`scratchpad/diaz-glitch-raw.html`, stripped tags, saved to
`scratchpad/diaz-glitch-text.txt`.

**Full article text confirms, quoted verbatim** (published Jun 7, 2016
7:35:42 PM, by Gregory J. Diaz, Nevada County Clerk-Recorder):

> At our polling places this morning, some voters did not appear on our
> electronic rosters (E-Poll Books) when our poll workers entered their
> first and last names in the E-Poll Book.

This is squarely a TRADITIONAL POLLING-PLACE system (June 2016 predates
Nevada's 2018 VCA vote-center switch by two years) -- an in-precinct
electronic check-in roster, not the vote-center e-pollbook the committed
record dates to 2018.

**Backdating the traditional system.** Two more Diaz-authored primary
sources, found via WebSearch and pulled the same way (CDX -> `curl` on the
Wayback raw endpoint):

1. The Union (Nevada City), July 28, 2014, Diaz op-ed on the June 3, 2014
   primary pilot: 25 e-poll-book units from two competing vendors (10
   "Every One Counts," 15 ES&S) tested at 23 polling locations (2 of which
   ran both brands side by side) -- explicitly a PILOT, not full coverage.
   Diaz: pilot "was a success," e-poll books "will be a valuable addition
   to the elections process in Nevada County."
2. YubaNet, Feb 18, 2015, Diaz-authored "'Trading in the Paper' - Nevada
   County's Electronic Poll Book Journey"
   (`scratchpad/epb-journey-text.txt`, pulled via CDX timestamp
   `20150222033106`), quoted verbatim:

   > During the 2014 election cycle, the Nevada County Elections Office
   > implemented electronic poll books to replace paper rosters in all
   > polling places across the county.

   This is Diaz's own on-the-record statement of FULL COUNTYWIDE deployment
   during the 2014 cycle (i.e. by the Nov 4, 2014 General, per a KNCO
   Feb 19, 2015 companion piece's timeline: "2013: Diaz observes the
   devices in Humboldt County" -> "June 2014: pilot" -> "November 2014:
   full countywide deployment").

So: traditional in-precinct e-poll books were PILOTED June 2014 (partial,
23 locations, 2-vendor bake-off) and FULLY DEPLOYED countywide by the Nov 4,
2014 General -- continuing in live use through the June 7, 2016 primary (per
the glitch statement) and presumably through Nov 8, 2016, before the county
retired traditional precincts entirely for the 2018 VCA vote-center model.

**Is this the "same" e-pollbook the schema tracks, or a different system?**
Genuinely different technical generation and operational model:
- 2014-2017 system: precinct-bound roster check-in (two vendors piloted;
  full vendor for the Nov 2014-2016 rollout not independently confirmed in
  this pass), used at dozens of single-precinct polling places.
- 2018-present system: VCA vote-center e-pollbook (currently "Provista
  ViBE" per the Oct 2025 SoS snapshot), required to synchronize ballot-
  issued status in REAL TIME ACROSS all vote centers countywide (since VCA
  voters may vote at any vote center) -- a materially different technical
  requirement from a single-precinct roster, and tied to the vote-center
  model that is ALREADY separately tracked in `nevada-ca.json` as its own
  `type: "vote-center"` entry (adopted_year 2018).

### Verdict: EPOLLBOOK -- SPLIT-RECORD

Keep two distinct `epollbook` entries:
1. Traditional polling-place EPB: adopted_year **2014** (first_election
   "2014-06" for the pilot / "2014-11" for full countywide deployment --
   recommend dating adopted_year to the full-deployment election, 2014-11,
   since that's the first election where EPB coverage was
   near-universal-not-partial), vendor pilot brands "Every One Counts" and
   "ES&S" (2014 pilot; which vendor(s) carried through to full deployment
   and into 2016 not independently confirmed this pass), confidence
   primary (Diaz's own contemporaneous statements).
2. VCA vote-center EPB (existing entry, unchanged): adopted_year 2018,
   vendor currently "Provista ViBE" per SoS, tied to the vote-center-model
   switch.

**Which should the analysis key on, and why:** the county-tech schema
tracks `epollbook` as a standalone variable separate from `vote-center`
(which is already its own tracked type in this file). Keying the
`epollbook`-specific flag on 2018 would double-count the VCA vote-center
transition under two different tech flags at once (epollbook AND
vote-center both flipping in the same election), which would confound any
analysis trying to isolate an e-pollbook-specific effect from a
vote-center-model effect. **Recommend keying `vs_epollbook` on 2014** (the
county's true first adoption of the tracked technology category -- an
electronic check-in roster replacing paper), leaving the separate
`vote-center` flag (already dated 2018) to carry the VCA-specific effect.
The 2018 vendor/technical-model transition is real and worth preserving in
the note text (SPLIT-RECORD, not a silent overwrite), but should not be the
flag-flip anchor.

**Row consequences if SPLIT-RECORD / key-on-2014 is applied:**

Committed general rows (`data/research/election-night/nevada-ca.json`):
| date | old vs_epollbook | new vs_epollbook |
|---|---|---|
| 2012-11-06 | pre | pre (unchanged -- EPB didn't exist yet in the county) |
| 2014-11-04 | pre | **post (FLIP)** -- this is the full-countywide-deployment election itself |
| 2016-11-08 | pre | **post (FLIP)** |
| 2018-11-06 | post | post (unchanged; now correctly reasoned as "2nd-gen VCA EPB, but EPB category itself has been post since 2014") |
| 2022-11-08 | post | post (unchanged) |
| 2024-11-05 | post (excluded) | post (unchanged) |

Draft primary rows (`scratchpad/dossier-nevada-ca-primaries.md`):
| date | old vs_epollbook | new vs_epollbook |
|---|---|---|
| 2012-06-05 | pre | pre (unchanged, null row) |
| 2014-06-03 | pre | **AMBIGUOUS -- this IS the pilot election itself** (23 of the county's polling locations, not "all"). Recommend NOT flipping to a clean post; instead mark `comparable: false` with a note "partial pilot in progress, mixed EPB/paper-roster election" rather than pre or post, since neither label cleanly applies. |
| 2016-06-07 | pre (provisional) | **post (FLIP)** -- full deployment had been in place since Nov 2014; corroborated live by Diaz's own glitch statement on this exact election date |
| 2018-06-05 | post | post (unchanged) |
| 2022-06-07 | post | post (unchanged) |
| 2024-03-05 | post | post (unchanged) |

Net: 3 clean flips pre->post (2014-11-04 general, 2016-11-08 general,
2016-06-07 primary draft), plus 1 row (2014-06-03 primary draft) recommended
to move from a clean "pre" to a flagged partial/non-comparable state rather
than a straight flip. Top-level `adoption.epollbook` in both
`county-tech/nevada-ca.json` and `election-night/nevada-ca.json` should
move from 2018 to 2014 for the flag-anchoring value, while the county-tech
JSON's `tech` array keeps BOTH the 2014 and 2018 entries (split, not
overwritten).

---

## Sources fetched this pass (provenance)

- Legistar SR 16-0825 detail page + attachments:
  `https://nevco.legistar.com/LegislationDetail.aspx?GUID=F2AD1997-3E3E-4C30-80F7-21F54318ADDF&ID=2840587`
  -> Board Letter `View.ashx?M=F&ID=4686317&GUID=380484B7-177A-4226-882F-48C98B57967E`
  (scanned, unreadable without OCR -- not pursued) and Agreement
  `View.ashx?M=F&ID=4686315&GUID=8629A10C-62AE-48AC-9004-41FA82CB8A51`
  (machine-readable, decisive -- saved to `scratchpad/agreement-16-0825.pdf` /
  `agreement.txt`).
- Diaz Jun 7 2016 glitch article: located via Wayback CDX
  (`url=yubanet.com&matchType=domain&filter=urlkey:.*poll-book.*`), fetched
  raw via `curl` at
  `http://web.archive.org/web/20160609140926if_/http://yubanet.com/regional/Greg-Diaz-Despite-E-Poll-book-glitch-your-vote-will-be-counted.php`
  -> `scratchpad/diaz-glitch-raw.html` / `diaz-glitch-text.txt`.
- Diaz Feb 18 2015 "Trading in the Paper" retrospective: same CDX domain
  query, capture `20150222033106`, original
  `http://yubanet.com/regional/Trading-in-the-Paper---Nevada-County-s-Electronic-Poll-Book-Journey.php`
  -> `scratchpad/epb-journey-raw.html` / `epb-journey-text.txt`.
- The Union, July 28, 2014 Diaz op-ed on the June 3, 2014 pilot (WebFetch
  direct, live URL) and KNCO, Feb 19, 2015 "County Pleased With Electronic
  Poll Devices" (WebFetch direct, live URL) -- both corroborate the pilot
  ->full-deployment timeline independently of the YubaNet pieces.
- Dead ends: `archive.ph` fetch blocked by tool; a WebSearch for a possible
  post-2016 replacement/upgrade sorter surfaced a genuinely NEW finding (FY
  2022/23 Nevada County purchase of "a new mail sorter," $324,074, state
  3:1-match reimbursed) suggesting the machine described in the county's
  2022/2023 Mail Ballot Processing Infographic (the source anchoring the
  OLD adopted_year=2022) may be a newer/replacement sorter, not the 2016
  MBV 1000 itself -- doesn't change the ASV verdict (first ASV adoption is
  still 2016 regardless of later hardware refreshes) but worth a note in
  the vendor field ("MBV 1000 (2016) superseded by a newer sorter, FY
  2022/23, ~$324k, vendor/model not confirmed this pass").
- Grand Jury 2017-2018 report and general news search for independent
  confirmation of actual Nov 2016 MBV 1000 go-live: inconclusive within the
  time cap (see FLAG 1 loose end above).

## Summary verdicts

- **ASV: REVISE-TO-2016** (from 2022). Basis: signed 9/27/2016 ES&S MBV 1000
  contract with "Automated Signature Recognition Software" and a paid line
  item contractually named "Election setup support and training- 2016
  General Election."
- **EPOLLBOOK: SPLIT-RECORD**, key on **2014** (from 2018) for the
  epollbook-specific flag; keep 2018 as a distinct VCA-vote-center-EPB
  sub-entry (already tracked separately via the `vote-center` type). Basis:
  Diaz's own Feb 2015 statement of full countywide deployment "during the
  2014 election cycle," corroborated by a live June 2014 pilot (The Union)
  and continuous documented use through the June 2016 primary (the glitch
  article itself).
