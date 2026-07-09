# Wave 3: Gilded-Age SF election-night counts (1880-1897), CDNC morning-after hunt

Agent salvage file; written as work proceeds. Session start 2026-07-08.
Method: cdnc.ucr.edu via raw-CDP Chrome tab (localhost:9222), per scripts/archive-recovery/cdnc_fetch.js
recipe; speed recipe = one nav clears Cloudflare, then Runtime.evaluate fetch() same-origin inside the tab.
WHAT COUNTS: counted returns in E+1 MORNING paper (stamp E+1 T03:00, cutoff E+1 06:00). Poll lists are not counts.

## Targets and gate ceilings (official final ballots)
| date | election | final |
|---|---|---|
| 1880-03-30 | Freeholders charter | 30,877 |
| 1880-09-08 | proposed charter (REJECTED) | 23,398 |
| 1880-11-02 | presidential | 41,292 |
| 1881-09-07 | municipal (Blake) | 33,216 |
| 1883-03-03 | proposed charter (REJECTED) | 18,764 |
| 1884-03-18 | Assembly special | 2,655 |
| 1886-11-02 | gubernatorial+municipal (Pond) | 45,716 |
| 1887-04-12 | charter+amendments (REJECTED) | 25,959 |
| 1890-11-04 | gubernatorial+municipal (Sanderson) | 55,565 |
| 1897-12-27 | Freeholders charter | 26,202 |

## Pre-existing material found in repo before any new fetching (2026-07-08)

### 1880-11-02 presidential: E+1 morning Alta partial ALREADY IN MIRROR (prior agents logged only E+2)
File: /Users/sbuss/workspace/sf-election-count/mirror/cdnc/DAC18801103/section_DAC18801103.2.12.txt
Source URL (copy-pasteable): https://cdnc.ucr.edu/?a=da&command=getSectionText&d=DAC18801103.2.12&f=AJAX&e=-------en--20--1--txt-txIN--------
Issue URL: https://cdnc.ucr.edu/?a=d&d=DAC18801103 (Daily Alta California, Wed Nov 3 1880, sec .2.12 "IN THE CITY. / YESTERDAY'S ELECTION.")
Verbatim (press-time count intro): "At tbe boar of going to preu tbe count stood ei followt : (lax- Han- Wra- Da- Roae- Mar"
[= "At the hour of going to press the count stood as follows", cols Garfield/Hancock/Weaver/Davis/Rosecrans/Murch]
Total row raw OCR: "Total. ..ll.SW 12.«0« S6T 11,221 12.831 112"
Clean cols (Congress): Davis 11,221 + Rosecrans 12,831 + Murch 112 = 24,164 votes counted in the Congress
contest by press time = 58.5% of the 41,292 ballot ceiling (contest-sum floor).
President cols garbled: Garfield ~11,5xx[?], Hancock ~12,60x[?], Weaver 567[?] (sum ~24.7k).
Also same section: complete same-night 12-ward BALLOTS-CAST tally "Total 41,298" (headline "Forty-One
Thousand Two Hundred and Ninety-Eight Votes Cast in This City") - turnout tallied, though the candidate
COUNT was ~58-60% at press. Prior report .superpowers/sdd/cdnc-1879-1880-report.md logged this as provenance;
this wave promotes it as THE E+1 morning observation. Gate: 24,164 <= 41,292 OK; 41,298 vs 41,292 = 6-vote
hand-tally noise on turnout (not a count-of-votes number).
TODO this wave: try SFC18801103 (Morning Call) for a cleaner press-time table; screenshot DAC18801103 p2 for
human read of the garbled President digits.

### 1897-12-27 Freeholders: E+1 morning Call partial ALREADY IN MIRROR
File: /Users/sbuss/workspace/sf-election-count/mirror/cdnc/SFC18971228/search_freeholders.txt (srpos 2 block)
Section: SFC18971228.1.7, p7, "PHELAN BOARD PROBABLY MAKE IT."
Source URL: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=SFC18971228.1.7&f=AJAX&e=-------en--20--1--txt-txIN--------
Verbatim: "With complete returns from thirtytwp [thirty-two] precincts and incomplete from sixty-two
precincts, with a total vote Of about 24.000, the Indications are that the above list comprises the names
of those who will frame the new charter." Also: "While the vote was light the counting was slow and
uncertain, and it was not until a very late hour this morning that the true condition was known."
E+1 morning count: ~24,000 of 26,202 certified = ~91.6% (rounded press estimate; 32 precincts complete +
62 incomplete). E+2 complete pre-canvass 26,163 already on file (data/sf_archival_canvass_points.csv row
1897-12-27, SFC18971229.2.60).

## New fetch log (this session)

All fetches this session used the speed recipe (one raw-CDP nav clears Cloudflare, then Runtime.evaluate
fetch() same-origin in the cleared background tab; tab created with Target.createTarget background:true,
never brought to front, closed after each run). Batch script:
/private/tmp/claude-501/-Users-sbuss-workspace-sf-election-count/74d81ded-65b2-4783-81e3-bf0802bdbf5a/scratchpad/cdnc_batch.cjs
Raw fetches + converted texts in .../scratchpad/fetched/. Screenshots in .../scratchpad/imgs/ (shot_*.png).
Section text URL pattern (paste into a Cloudflare-cleared browser):
https://cdnc.ucr.edu/?a=da&command=getSectionText&d=<SECTION_OID>&f=AJAX&e=-------en--20--1--txt-txIN--------
Article page URL: https://cdnc.ucr.edu/?a=d&d=<SECTION_OID>

### 1880-03-30 Freeholders (final 30,877) - FOUND, midnight count, DAC18800331
Section DAC18800331.2.11 "6093 MAJORITY" (E+1 Wed Mar 31 1880, p1). Verbatim:
"THK COUNT AT MIDNIGHT. The following report waß received at Parlor A, headquarters of the Citizens
Protective Union, at midnight : Total voto counted, 20,271 ; Citizens Ticket, 12,360; Band-lot, 7,911;
majority for Citizens, 4,449. Byrnea, 11,512; Freud, 8«3(i ; majority for Byrneß, 2876."
Arithmetic: 12,360+7,911 = 20,271 EXACT; 12,360-7,911 = 4,449 EXACT; Byrnes 11,512-2,876 = Freud 8,636
(OCR "8«3(i"). MIDNIGHT COUNT = 20,271 of 30,877 = 65.7%. Same section, day-progress poll tallies (not
counts): 10:30am 14,685; 12:30pm 18,845; 2:30pm "33.874"[OCR, true ~23,874]; "total vote cast a trifle
less than 31,000" (vs certified 30,877, consistent). Companion full precinct returns table section
DAC18800331.2.31 "THE RETURNS. The Vote as Cast by Wards and Precincts" (candidate-level, OCR-garbled,
proves counted precinct returns printed E+1). Also 2.10 "VICTORY!" 2.3 "HANDSOMELY WON." (prose).
Screenshot: imgs/shot_18800331_DAC_6093majority.png
Gate: 20,271 <= 30,877 OK.

### 1880-09-08 charter (final 23,398) - FOUND, near-complete overnight count, DAC18800909
Section DAC18800909.2.8 "BEATEN" (E+1 Thu Sep 9 1880). Headline verbatim: "Totil Vote Cast at tbe Charter
Election Over 23,000— For the New Charter, 4057— Against the New Chirter, 18,675 -Majority Consigning the
Freeholders' Instrument to Oblivion, 14,618". Body verbatim: "Tbe total vole cut al tbe election yesterday
wu over S3,eOO [23,000]. The exact Sgaret ctOBOt be given, tl the ntarnt from t few of Ihe imtller ftr
oallylng pnotnoti conld not be obtained lut nlgbt. Thtlr tbience, however, would mike bat t flight
differ•oc* Id tb* tottli." Ward table total row "Tottl 18.C15 tOST" = Against 18,675 / For 4,057.
Arithmetic: 18,675-4,057 = 14,618 EXACT. COUNT = 4,057+18,675 = 22,732 of 23,398 = 97.2%, explicitly all
but "a few of the smaller far outlying precincts", counted last night. Ward-by-ward For/Against table
printed (digits soft). Screenshot: imgs/shot_18800909_DAC_beaten.png
Gate: 22,732 <= 23,398 OK.

### 1880-11-02 presidential (final 41,292) - FOUND (pre-existing mirror, promoted this wave)
See pre-existing section above (DAC18801103.2.12). E+1 press-time partial candidate count, President cols
garbled (Garfield ~11,5xx / Hancock ~12,60x / Weaver 567[?]), Congress cols clean: Davis 11,221 +
Rosecrans 12,831 + Murch 112 = 24,164 counted = 58.5% floor. Complete 12-ward ballots-CAST tally 41,298
same section. SF Call E+1 not usable: SFC18801103 returns Veridian "Oops!" page (issue not digitized);
dead-end URL https://cdnc.ucr.edu/?a=d&d=SFC18801103 (16KB Oops page, fetched 2026-07-09).
Screenshot: imgs/shot_18801103_DAC_inthecity.png

### 1881-09-07 municipal, Mayor Blake (final 33,216) - FOUND, midnight + 2am counts, DAC18810908
Section DAC18810908.2.12 "AT THE REPUBLICAN HEADQUARTERS." (E+1 Thu Sep 8 1881). Verbatim:
"THE RETDRNS AT MIDNIGHT. ... Full returns up to mldnlgbt. from every precinct In tbe city, tbowed that
11,242 votea bad been counted. The vote stood : Blake 6130, Howe 6113 [5,113], BUke's msjorlty 1018 ;
Sedgwick 6178, Desmend 6C36 [5,036], Srdgwlck't majority 1143 ; Urlckwedel 6910 [5,910], Duon 6037 [5,037],
Brlckwedel'i majority 873 ; Wldber 69*1 [5,971], Z*pba* 4966, tbe former 'I majority being 1005."
Arithmetic: Brickwedel 5,910-5,037 = 873 EXACT; Widber 5,971-4,966 = 1,005 EXACT; Blake 6,130+Howe 5,113 =
11,243 vs stated 11,242 counted (1 off, OCR). MIDNIGHT COUNT = 11,242 of 33,216 = 33.8%.
Also "AT 2 O'CLOCK A. M. At 2 o'olock thll morning about 3400 [likely 13,400, digits soft] vottl bid been
polled [counted]. Tbe prlnolpal candidate! on Iba Bepobllcan ticket were about 600 ahead."
Earlier checkpoints same section: 24 precincts (early eve) Blake 425/Howe 271; 41 pcts Blake 863/Howe 569;
75 pcts (10pm) Blake 1,235/Howe 992; 85 pcts Blake 1,4?8/Howe 1,138; 96 pcts (after midnight) Blake +800.
Section DAC18810908.2.11 "THE POLLS." has complete ward+precinct BALLOTS-CAST tally: "Total of totei ctit
la tbs clit, S3 160" = 33,160 (vs certified 33,216, 56 gap) + per-precinct lists, and the dead-end quote
for full candidate counts: "It waa expected Ibat owing to ibe ceaeral scratching, teveral dajt would be
consumed in oountlng tbe ballots." Morning-edition lead DAC18810908.2.2 "the election.": "all tfaece views
are ba>ea en tbe Er«; few tbontand ballot* counted".
Screenshot: imgs/shot_18810908_DAC_midnight.png
Gate: 11,242 <= 33,216 OK; turnout tally 33,160 <= 33,216 OK.

### 1883-03-03 charter (final 18,764) - FOUND, near-complete count to 3:15 A.M., DAC18830304
Section DAC18830304.2.11 "IN DOUBT. Close Vote on tbe Charter." (E+1 Sun Mar 4 1883). Contains FULL
For/Against by-precinct tables for all 12 wards (semi-official returns received by the Registrar) plus a
ward summary table, total row raw OCR: "» in 9,248 18.031" (For total garbled; Against 9,248[?]; grand
total 18,031[?]) MINUS the 23d and 28th precincts of the 11th Ward ("cannot be given for tbli Ward").
Press-time prose verbatim: "At Ihe hcur ct tbe Alia going to preM tbe re.torna Irom tbe twenty.third tnd
Iwenty-elgbtb prectncti cf the Kltvsnlh Wtru bad not been received it tbt Keglßlrtr't offloe. Wltb the
returns is uompcttd by him there ii t mijority ol eleven votet In Itvor ot ibe adoption ot ibe charter..."
3:15 A.M. addendum verbatim: "At 3:15 a. m. the retaros were received from the twenty-eighth precinct of
the Eleventh *artl. which give as [??] for tbe aew cblrttr and il [??] tgalntl. Tbe total vote now •tends
Vasß [9,?5?] for Ihe new cbirler end tlga [9,?6?] tgsloit the new obtrler, telog t mtjoilly ol one vote
tgilnit Ua adoption with one prtcloct lo heir Irom."
COUNT: summary-table state ~18,031[?] counted (96.1% of 18,764) at press compile; 3:15 a.m. state ~18.5k
(For+Against, each ~9.2-9.4k, digits garbled) = ~98.6%, ONE precinct outstanding, majority ONE VOTE
against. Certified: REJECTED, 18,764 total. Digits need human page-image read.
Screenshot: imgs/shot_18830304_DAC_indoubt.png
Gate: 18,031 and ~18.5k <= 18,764 OK.

### 1884-03-18 Assembly special (on-file final 2,655) - FOUND, COMPLETE count by ~10 P.M., + GATE CONFLICT
DAC18840319 TOC (2-page digitization) had no election item; found via CDNC date-scoped search
(copy-pasteable): https://cdnc.ucr.edu/?a=q&hs=1&r=1&results=1&txq=special+election&txf=txIN&ssnip=txt&dafdq=19&dafmq=03&dafyq=1884&datdq=19&datmq=03&datyq=1884&e=-------en--20--1--txt-txIN--------
Section DAC18840319.2.58 "WALLACE'S VICTORY." (E+1 Wed Mar 19 1884). Verbatim: "Before 10 p. m. the
semi-official returns were all n the Registrar's office. Deputy Registrar W. Broderick and John Fogarty...
footed them up, and announced the election of Judge Wallace by a majority of 326 over his young opponent."
Section DAC18840319.2.58.1 "The Returns." full by-precinct table (41 precincts, 11th+12th wards = 13th
Senatorial District), total row: "Ttotak 2.668 2,342 60 6,070" = Wallace 2,668 + Hawes 2,342 + Ellis 60 =
5,070 EXACT (printed "6,070" elsewhere is OCR of 5,070); majority 2,668-2,342 = 326 EXACT.
COUNT = 5,070 total votes, 100% of precincts, counted by ~10 p.m. election night.
Corroboration (wires, same morning): SDU18840319.2.27.1 (Sacramento Daily Union) "Wallace (Dem.), 2.CG7
[2,667]; Havres (Kep.), 2,224[?]; Ellis... plurality of 351[?]"; MP18840319.2.4 (Morning Press) "Wallace's
majority over Hawes, is 417[?]... Total votes polled 49G7 [4,967]" - earlier-evening wire variants.
*** GATE CONFLICT: press-complete total 5,070 EXCEEDS the on-file official final of 2,655 (registrar
cumulative table vol47 p.277). Wallace's own vote (2,668 press / 2,667 SDU) is within 13 of 2,655 -
hypothesis: the vol47 "2,655" is the winning candidate's canvassed vote (or another single-column figure),
NOT total ballots cast. FLAG for maintainer/human: do not use 2,655 as a ballots ceiling for this election
without re-reading mirror/muni_reports/vol47_n320.jpg. ***
Screenshot: imgs/shot_18840319_DAC_wallace.png
SFC18840319: Veridian "Oops!" page, not digitized (dead end, fetched 2026-07-09).

### 1886-11-02 gubernatorial+municipal, Pond (final 45,716) - FOUND, 1 A.M. partial count, DAC18861103
Section DAC18861103.2.2.18 "THE CITY RETURNS. Tbe Kewnlt aa Ntaown at ttae Bonr of Gome to Cress" (E+1 Wed
Nov 3 1886). Verbatim: "QTb«. following is the summary of the votes counted up to 1 o'clock this morning"
then full two-candidate-plus lists for every contest. Clean contest (Mayor, from companion subsection
DAC18861103.2.2.20 "Municipal Ticket."): Pond 1,693 + Doble 1,244 + Hinton 133 = 3,070 counted = 6.7% of
45,716. Governor cols partly garbled: Bartlett "1,4»»" / Swift 1,222 / O'Donnell "»;ce" / Wigginton 205 /
Russell 14. Slow-count cause quoted (main sec 2.2 "AT THE POLLS."): "The count is progressing vary elowly,
on account of the great amount of scratching... Returns Coining in Very Slowly... it may take a day or two
yet to determine the successful candidates."
Screenshot: imgs/shot_18861103_DAC_cityreturns.png
Gate: 3,070 <= 45,716 OK (tiny early slice, but explicitly clocked 1 A.M. and printed E+1 morning).

### 1887-04-12 charter+amendments (final 25,959) - FOUND, 159-precinct count, DAC18870413
Section DAC18870413.2.15 "YESTERDAY'S ELECTION. ... THE CHARTER SNOWED UNDER." (E+1 Wed Apr 13 1887).
Verbatim: "About 25,000 votes were cast, and returns from 159 precincts show a ' vote for the charter of
9,697, and against 13,304.' The charter is, therefore, undoubtedly defeated by over 4,000 majority. .The
Constitutional Amendments, so far as the city is concerned, have fared better, the figures showing nearly
10,000 majority in their favor." Also verbatim (missing precincts, overnight): "In the following precincts
the election clerks stupidly sealed np the semi-official returns with the ballots, so that the 'vote for
and against the charter and amendments eonld net be obtained at the Registrar's office last night :
Eighth Precinct of the Fortyseventh Assembly District, Second Precinct of the Thirty-first..., Fourth
Precinct of (he Thirty-fifth..., Fourth Precinct of the Thirty-second Assembly District."
COUNT = 9,697 + 13,304 = 23,001 from 159 precincts (of 176) = 88.6% of 25,959. Certified: REJECTED.
Screenshot: imgs/shot_18870413_DAC_yesterdays.png
Gate: 23,001 <= 25,959 OK.

### 1890-11-04 gubernatorial+municipal, Sanderson (final 55,565) - FOUND (party-ticket tabulation), SFC18901105
DAC18901105.2.14 "THE CITY ELECTION." (E+1 Wed Nov 5 1890) verbatim dead-end for candidate counts: "the
counting of the tickets prooeeded but slowly, and those who had hoped to know the possitive results by
midnight soon found they were doomed to disappointment." (Story-plan sorting; count slow.)
SFC18901105.2.13 "THE ELECTION IN THE CITY." verbatim: "Although up tea late hour last night no definite
district election returns had been revealed by the preempt tickets that had been counted..."
BUT SFC18901105.2.15 "THE STATE. Returns for the Head of tlio Ticket and Other Officers." prints a
COMPLETE per-Assembly-district (29th-48th = all 20 SF districts) tabulation of ballots by party
(Republican/Democratic/American/Prohibition/Scattering + Total per district), e.g. "The ballots counted
in this district show: republican 1.030 Democratic 1,203 American 14 l-ri-.niliiti.in 10 Scattering 24
Total 2,317". Printed district totals: 1,613 / 2,317 / 1,985 / 3,038 / 2,453 / 2,457 / 2,369 / 3,323[components
sum 2,323] / 2,630 / 2,785 / 2,005[components 2,605] / 3,162 / 3,242 / 4,130 / 3,262 / 4,267 / 2,683 /
2,117 / 3,273 / 3,033[components 3,133]. Sum with the two clear component corrections = 55,744 vs certified
55,565: OVERSHOOTS ceiling by 179 (0.32%) - flagged, several components OCR-soft; this is the Story-plan
party-ticket sort tally (ballots classified by ticket, not a candidate count), effectively complete
citywide. Human page read of imgs/shot_18901105_SFC_thestate.png arbitrates digits.
SFC front page 2.2 "THE RESULT AT HOME.": "The Republican majority is over 4000" (no table).
Verdict: by press time E+1 morning, ~100% of ballots had been SORTED by party (tabulation printed) but
"no definite" candidate counts existed. Best count-like observation: party-ticket tabulation ~55.7k[?];
best hard candidate count is post-cutoff (Evening Bulletin Nov 5 noon, 6,610 at 40 precincts, already on
file in data/pre1892_certified.md).

### 1897-12-27 Freeholders (final 26,202) - FOUND (pre-existing mirror, promoted this wave)
See pre-existing section above: SFC18971228.1.7 (E+1 p7) "With complete returns from thirty-two precincts
and incomplete from sixty-two precincts, with a total vote of about 24.000..." = ~24,000 counted = 91.6%
of 26,202. Counting ran "until a very late hour this morning". E+2 complete 26,163 already on file.
Screenshot: imgs/shot_18971228_SFC_phelan.png

## Dead ends log
- SFC18801103, SFC18840319: CDNC returns Veridian "Oops!" page - SF Call issues not digitized for these
  dates (same failure mode as SFC18841105/SFC18881107 in prior waves). URLs above.
- DAC18901105 digitization is 2 pages only; no returns table in the Alta E+1 for 1890 (slow Story-plan
  count, quotes above); the Call carried the tabulation instead.
- DAC18840319 digitization is 2 pages in the TOC blob but search reaches sections on undigitized-TOC pages
  (2.58); lesson: ALWAYS run the date-scoped search even when the TOC looks empty.
