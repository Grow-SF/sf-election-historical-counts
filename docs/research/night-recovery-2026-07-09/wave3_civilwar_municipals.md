# Wave 3: Civil-War-era SF municipal night counts (CDNC)

Agent salvage file. Written as findings land. Method: cdnc_fetch.js raw-CDP
recipe against day-after Daily Alta California (DAC), fallback Morning Call /
Sacramento Daily Union (SDU).

Targets (election date, official final = gate ceiling):
1. 1861-05-21 municipal, final 11,507 -> DAC18610522
2. 1863-05-19 municipal, final 11,417 -> DAC18630520
3. 1864-05-17 municipal, final 10,847 (Sheriff-contest floor) -> DAC18640518
4. 1865-05-16 municipal, final 14,196 -> DAC18650517
5. 1865-09-06 state general (Wed Sep 6!), final 13,354 -> DAC18650907
6. 1866-09-05 municipal, final 13,371 -> DAC18660906
7. 1867-09-04 governor+municipal, final 17,472 -> DAC18670905

Rules: night count = returns COUNTED by press time E+1 morning (cutoff E+1
06:00). Poll lists ("votes polled") are NOT counts. Sum ward tables myself.
Masthead-check every issue before citing.

## Status log (all seven FOUND; see page-image pass at bottom for final figures)
- [x] 1861-05-22 FOUND -> corrected floor 6,433 (55.9%)
- [x] 1863-05-20 FOUND -> mayor-contest count 6,225 (54.5%)
- [x] 1864-05-18 FOUND -> sheriff-contest count 7,230 table (+D7 text 1,363)
- [x] 1865-05-17 FOUND -> sheriff-contest count 9,027 table (+D2/D11 text)
- [x] 1865-09-07 FOUND -> ~10,432 (clocked partials 4,677 + table districts 5,755)
- [x] 1866-09-06 FOUND -> chief-of-police contest 10,749 (11 of 12 wards)
- [x] 1867-09-05 FOUND -> corrected floor 6,307 (7,324 with flagged W6)

## Findings

### 1861-05-21 (municipal, Teschemacher; final 11,507) -- FOUND, partial count floor
Source: Daily Alta California 1861-05-22, p.1, "Election Returns at Midnight."
Issue URL: https://cdnc.ucr.edu/?a=d&d=DAC18610522
Section OID: DAC18610522.2.3 (fetch: `node scripts/archive-recovery/cdnc_fetch.js DAC18610522 DAC18610522.2.3`)
Mirror: mirror/cdnc/DAC18610522/section_DAC18610522.2.3.txt
TOC shows masthead "SAN FRANCISCO, WEDNESDAY, MAY 22" (matches E+1).

Clocking quote (verbatim OCR): "Below will be and the returns, at obtained
from the polling places at midnight." [= found the returns, as obtained
from the polling places at midnight]. Two districts carry "Later" complete
returns received up to "3 o'clock this morning" (within E+1 06:00 cutoff).

Counted-by-press-time tallies per district (12 districts; OCR garbles flagged):
- D1: cast 690; counted 210 straight People's + 65 straight Fusion = 275
- D2: assorting complete at midnight: 730 People's Union tickets + Fusion
  garbled (OCR "i:,3", maybe 453/533). Floor uses People's only: 730. FLAG.
- D3: cast 838; counted straight P 208 + straight F 220 = 428 (340 scratched
  pending). Mayor count at 12:30: Teschemacher "138"(438?), Fay 381. FLAG.
- D4 ("tune nre*incr>"): straight counted P 331 + F 188 = 519 (majority ~150
  checks vs 331-188=143). FLAG on 188 (OCR "ISs").
- D5: cast 934; straights+scratched partial at midnight, then "Later...
  complete returns": Teschemacher 528, Fay 389 -> 917 mayor votes complete.
- D6: count stood P 350 + F 280 = 630 (OCR "2*o"). FLAG on 280.
- D7: ~500 polled, ballots "terribly scratched", Fusion ~100 ahead on
  aggregate; no clean counted figure. EXCLUDED.
- D8: counted P 264 + straight F 158 = 422 (cast 755)
- D9: cast 1,486; counted P 299 straight + 173 scratched = 472; F 174
  straight + 159 scratched = 333; total counted 805
- D10: cast 1,743; "systematic counting had not sufficiently progressed";
  EXCLUDED (documented no-count)
- D11: total 406 = 247 F + 159 P, fully counted (247+159=406 checks); later
  complete candidate table received ~3 AM -> 406
- D12: complete returns printed; "Total vote, 331" with full candidate
  detail (Mayor: Teschemacher P 126, Fay R ~171) -> 331

Floor sum (my arithmetic): 275+730+428+519+917+630+422+805+406+331 = 5,463
counted by press (~midnight-3 AM) = 47.5% of final 11,507. If D2's garbled
Fusion count (~453) is real, ~5,916 (51.4%). Gate: under 11,507 ceiling. PASS.
Verdict: NIGHT COUNT FLOOR ~5,463. Needs human read on D2 Fusion, D3 mayor,
D4/D6 digits.

### 1863-05-19 (municipal, Coon; final 11,417) -- FOUND, partial count floor
Sources: Daily Alta California 1863-05-20 p.1:
- "CITY ELECTION RETURNS 1863" ward-by-candidate table, OID DAC18630520.2.6
- "CITY ITEMS. The Election." (per-district count status at midnight), OID DAC18630520.2.8
Issue URL: https://cdnc.ucr.edu/?a=d&d=DAC18630520 (TOC masthead: SAN
FRANCISCO, WEDNESDAY, MAY 20 -- matches E+1)
Mirror: mirror/cdnc/DAC18630520/section_DAC18630520.2.6.txt and .2.8.txt

Clocking quotes (verbatim OCR):
- D1: "In t'ue First District 506 vote* were i«.lled. bat only lt>i Peoi.le'a
  uu<l 75 Citizens' were counted at aidnliU" [counted at midnight]
- D2: "Tbe Judges expected to finish tbe count about T oVloek thic
  U'lruinv" [about 7 o'clock this morning -- i.e. NOT counted by press]
- The 8 PM figures are explicitly an ESTIMATE ("From a careful estimate,
  gathered after the pols clooed") -- not used.

IMPORTANT: the "Comparative Vote of 1862 and '63" aggregate 11,417 printed
in this issue is the total votes CAST (poll-list aggregate; "thirty-four
votes more being cast this year than last"), NOT a night count. It equals
the official final 11,417, confirming the gate ceiling.

Counted-by-midnight per district (text + table cross-read):
- D1: 161(?)+75 = 236 counted of 506 polled. FLAG on 161 (OCR "lt>i")
- D2: nothing counted by press (finish ~7 AM) -> 0
- D3: 604 polled; straights all counted: P 215 + C 83 = 298 (300 scratched pending)
- D4: complete: P 202 + C 128 = 330
- D5: complete: P 473 + C 288 = 761
- D6: not described in text; table column garbled. EXCLUDED.
- D7: P 393 straight + 305 scratched; C 159 straight + scratched garbled ->
  857 floor (P straight+scratched + C straight)
- D8: complete: P 546 + C 172 = 718
- D9: straights: P 449 + C 206 = 655
- D10: P 715 straight + 447 scratched; C 615 straight + 427 scratched =
  2,204 (Railroad question in D10 counted: Yes 1,243 + No 601 = 1,844)
- D11: straights counted, C majority 130; table suggests ~175 P + 285 C =
  460. FLAG.
- D12: average estimate only -> 0
Conservative floor sum (my arithmetic, D10 straights only 1,330):
236+298+330+761+857+718+655+1330+460 = 5,645 (49.4% of 11,417).
With D10 scratched included (2,204): 6,519 (57.1%).
Mayor-table cross-check (Coon 3,495 + Holland 2,561 = 6,056, 53%) is
consistent. Gate: all under 11,417. PASS.
Verdict: NIGHT COUNT FLOOR ~5,645 (conservative) to ~6,519. Needs human
read on D1, D11, D6 column.

### 1864-05-17 (municipal; final 10,847 = official Sheriff-contest floor) -- FOUND, partial count floor
Sources: Daily Alta California 1864-05-18 p.1:
- "ELECTION RETURNS, MAY SEVENTEENTH" table, OID DAC18640518.2.4 (OCR
  column-dump, badly garbled; needs page-image read)
- "The Election Yesterday.", OID DAC18640518.2.5 (per-district status)
Issue URL: https://cdnc.ucr.edu/?a=d&d=DAC18640518 (TOC masthead: SAN
FRANCISCO, WEDNESDAY, MAY 18 -- matches E+1)
Mirror: mirror/cdnc/DAC18640518/section_DAC18640518.2.4.txt and .2.5.txt

Clocking quotes (verbatim OCR):
- D1 "(INCOMPLETE.) We give in our table the reeult for general ticket,
  safara* counted up to the hour of collecting re tarns."
- D5 "Total »ote, ts\. 6trai|hu oslyeonntnl up to 11 k." [straights only
  counted up to 11 P.M.]
- D7 "The following is the vote as counted up to midnight; People's
  Ktraigbt ticket, 7<3 [763]; People's split ticket, 4i [48]; tu(al
  Peoi>l»'«, Oil [811]; Copperhead etraighi .131 [331]; Copperhead' split,
  141: total Copperhead, 4"4 [474] ... Entire vote, 1.3C3 [1,363]"
  (arithmetic checks: 763+48=811; 1363-811-474=78 Regular Union)
Districts 2,3,4,6,8,9,11,12 are printed with "(COMPLETE)" headers; D10 has
only a proportion statement ("over two-thirds" People's), no count.

POLL LIST (not a count): Sanitary Fund table gives votes polled per
district, "Total 10,916" (OCR "t.10.91«"). Official single-contest final
10,847 < 10,916 polled: consistent; do NOT claim 10,916.

Legible counted-contest sums by district (floor method: one contest per
district, only where both sides legible):
- D1 Supervisor 220+131+200 = 551 (explicitly incomplete count)
- D2 Constable 501+144 = 645 (COMPLETE)
- D4 Judge 505+119+23 = 647 (COMPLETE)
- D7 entire vote counted by midnight = 1,363
- D8 Inspector 961+211 = 1,172 (COMPLETE)
- D9 School Director 483+145 = 628 (COMPLETE)
- D11 School Director 730+156 = 886 (COMPLETE)
Sum = 5,892 (54.3% of 10,847 contest-floor). Adding D5 straights-only 555
(FLAG, OCR "£55") -> 6,447. D3/D6/D10/D12 excluded for garble or no count;
true night figure likely ~7,900 given the COMPLETE labels. Gate: under
10,847. PASS (but note denominator is itself a single-contest floor, so
share is approximate).
Verdict: NIGHT COUNT FLOOR ~5,892 legible (probably ~7,900). Needs human
page read of the 2.4 table (column-major OCR useless).

### 1865-05-16 (municipal, Coon re-elected; final 14,196) -- FOUND, partial count floor
Sources: Daily Alta California 1865-05-17 p.1:
- "CITY ELECTION, MAY 16." returns table, OID DAC18650517.2.6 (column
  alignment partly garbled)
- "CITY ITEMS" -> "THE MUNICIPAL ELECTION..." narrative, OID DAC18650517.2.5
- "Total Vote of San Francisco.", OID DAC18650517.2.8 (POLL LIST by
  district; prints total "M.196" = 14,196, matching official final, and
  "The total vote yesterday exceeds 14,000"; city-election series value
  13,861 excludes 12th District 1st precinct. NOT a count.)
Issue URL: https://cdnc.ucr.edu/?a=d&d=DAC18650517 (TOC masthead: SAN
FRANCISCO, WEDNESDAY, MAY 17 -- matches E+1)
Mirror: mirror/cdnc/DAC18650517/section_DAC18650517.2.{5,6,8}.txt

Clocking quote (verbatim OCR): "The Urge number of names on the ticketa,
and the very general scratching on both aides, greatly delayed the work of
counting ni> the votet, and our returns are, therefore, necessarily
imperfect. We give above, however, the returns so tar v received up to the
hour of our going to press." Also per district: "At S o'clock this morning
all the straight tickets had been counted" (D4, = 3 AM); "At three o'clock.
Coon had 475: Rowell, 353" (D2).

Counted-by-press per district (mayor contest where possible):
- D1: table Coon 377 + Rowell 382 (OCR "882") = 759. FLAG.
- D2: 3 AM: Coon 475 + Rowell 353 = 828
- D3: complete ("full rote for city officers... in the table"); Inspector
  contest 419+403 = 822
- D4: 3 AM straights counted: Union 206 + People's 307 = 513 (550 scratched
  pending)
- D5: complete; table pair 504+618 = 1,122. FLAG (column alignment).
- D6: straights P 320 + Opp 149 + split Opp 234 = 703 floor (split P
  garbled ~59/89). FLAG.
- D7: "Coon's majority is 944 in all the bal ots" ascertained, but 242
  scratched Union still to count; table garbled. EXCLUDED from floor.
- D8: straight Opp 400 + straight P garbled ("r.V") -> 400 only. FLAG.
- D9: complete: People's 436 + Opposition 406 = 842
- D10: 3 AM all straights save 60 People's counted; table garbled. EXCLUDED.
- D11: complete for Mayor: Coon 450 + Rowell 497 = 947
- D12 P1: Coon 161 + Rowell 182 = 343 ("total vote was about 3X3")
Floor sum: 759+828+822+513+1122+703+400+842+947+343 = 7,279 (51.3% of
14,196). Clean-legible subset only (D2,D3,D4,D9,D11,D12): 4,295 (30.3%).
Gate: under 14,196. PASS.
Verdict: NIGHT COUNT FLOOR ~4,295 clean / ~7,279 with flagged digits;
D7+D10 also largely counted by 3 AM (true figure higher). Human read
needed on table 2.6.

### 1865-09-06 (state general, Legislature; final 13,354) -- FOUND, partial count floor
Sources: Daily Alta California 1865-09-07 p.1 (TOC masthead "SAN FRANCISCO,
THURSDAY, SEPT. 7" -- confirms Wednesday Sept 6 election, E+1 verified):
- "ELECTION RETURNS. SEPTEMBER 6, 1865." table, OID DAC18650907.2.3
  (Senate+Assembly by district; column identities garbled in OCR)
- "The Election Yesterday." with "INCOMPLETE RETURNS" and "THE RESULT"
  subheads, OID DAC18650907.2.4
- "Total Vote of the City.", OID DAC18650907.2.5: POLL LIST; prints 1865 =
  13,354 total and by-district totals (matches official final 13,354).
  NOT a count.
Mirror: mirror/cdnc/DAC18650907/section_DAC18650907.2.{3,4,5}.txt

Clocking quotes (verbatim):
- "In addition to the complete returns from the districts given in the
  regular table, we have reported partial returns from several districts,
  up to 2 1/2 o'clock this morning, as follows:"
- D9: "The counting was to be finished about 4 o'clock tbis morning."
- "So far an could be ascertained at three o'clock this morning, the list
  of members of the Legislature certainly elected was as follows..."

Clocked partial counts (2:30 AM), straight tickets counted:
- D5: Ind Union 360 + Union 316 + Dem 389 = 1,065
- D8: Dem 399 + Union 316 + Ind Union 381 = 1,096
- D9: Dem 222 + Ind 142 + Reg Union 158 = 522 (227 scratched pending)
- D10: Dem 1,060 + Ind 474 + Reg Union 460 = 1,994 (646 scratched pending)
Clocked subtotal = 4,677 = 35.0% of 13,354.

The regular table carries COMPLETE returns for the other districts, but
OCR column headers are unreadable; a tentative unexpired-Senate-contest
read gives ~800 (D1, matches D1 polled 792), ~557, ~556, ~706, ~787 for
five columns (+ two more table blocks unparsed), which would lift the
night total to roughly 8,000 (~60%). NOT claimed pending page-image read
(risk of double-counting D5/D8 if those columns are the partial districts).
Gate: 4,677 under 13,354. PASS.
Verdict: NIGHT COUNT FLOOR 4,677 (clocked 2:30 AM straights, 4 districts);
true night figure likely ~8,000 with the table's complete districts.

### 1866-09-05 (municipal; final 13,371) -- FOUND (clocked), table needs page-image read
Sources: Daily Alta California 1866-09-06:
- p.1 "ELECTION RETURNS. SEPTEMBER 6 [sic, printed as the header date
  garbled 'SEPTEMBER, «, 1866'; contents are Sept 5 election]", OID
  DAC18660906.2.12 -- the counted-returns-at-press table; OCR column dump
  nearly unreadable
- p.1 "CITY ITEMS. THE ELECTION..." OID DAC18660906.2.2
- p.1 "TOTAL VOTE OF THE CITY." OID DAC18660906.2.6
- p.2 "RESULT OF THE ELECTION." OID DAC18660906.2.26 (no numbers)
Issue URL: https://cdnc.ucr.edu/?a=d&d=DAC18660906
Mirror: mirror/cdnc/DAC18660906/section_DAC18660906.2.{2,6,12,26}.txt

Clocking quotes (verbatim OCR):
- "we are unable to give the complete returns, the count being still in
  progress in several precinaU as we go to press" (2.2)
- "Sufficient returns were received before the hour of going to press this
  morning, to warrant the statement that the whole of the general county
  Union ticket has been elected" (2.26)
- Third Ward returns received "at half-ca.'t nine n'clock exactly" [9:30
  PM], "some half hour ahead of all the other[s]" (2.2)
POLL LIST (not a count): "The to'al vote polled at the election yeaterday
wa* las reported' lU6&" -- garbled, plausibly 13,365-ish vs official final
13,371; "about 700 lee* than the number on the poll lists". NOT claimable
as a count and digits unreadable.

Counted floor from the only cleanly legible table columns (three wards,
county contests, U+D pairs): (~610+~400) + (~365+194) + (~645+~350) =
~2,564 (19.2% of 13,371). The table clearly carries most of the 12 wards
(returns from all wards were being collected from 9:30 PM on, and only
"several precincts" were still counting at press), so the true night count
is much higher, likely ~10,000+, but the OCR cannot support a sum.
Gate: 2,564 under 13,371. PASS.
Verdict: NIGHT COUNT documented and clocked; legible floor only ~2,564.
PRIORITY for human page-image read of DAC18660906.2.12.

### 1867-09-04 (gov+municipal, final 17,472) -- FOUND, partial count floor
Source: Daily Alta California 1867-09-05, p.1, "LOCAL INTELLIGENCE. / THE
ELECTION IN SAN FRANCISCO. Incomplete Returns."
Issue URL: https://cdnc.ucr.edu/?a=d&d=DAC18670905
Section OID: DAC18670905.2.3 (fetch: `node scripts/archive-recovery/cdnc_fetch.js DAC18670905 DAC18670905.2.3`)
Mirror: mirror/cdnc/DAC18670905/section_DAC18670905.2.3.txt

Clocking quote (verbatim, OCR): "Up to 2 a. v. we are able to eollee* only
the following positive return*." [= "Up to 2 A.M. we are able to collect
only the following positive returns."] Also: "It will probably be Into thin
even ing before we can get (he entire rote of the differ cut Ward*."
[= late this evening before entire vote of the different Wards.]

CRITICAL: the article's RECAPITULATION table (First Ward 1,185 ... Total
17,365) is the total vote POLLED by ward (poll list), NOT counted returns.
Do not claim 17,365 as a night count. (Official final 17,472; polled list
17,365 is consistent as a near-final poll list.)

Actually-COUNTED tallies by press time (~2 AM), governor contest, per ward
(OCR reading, garbles flagged):
- W1: no count; officers' midnight estimate only (Haight+McCoppin ~450 maj)
- W2: 500 straight ballots counted by 12:30 (400 Dem + 100 Union) -> 500
- W3: at 2:15 AM "Gorham, 1??: Haight, ?17" (OCR "li*" / ".".17") -> Haight
  ~317 legible-ish, Gorham garbled. Floor used: 317. GARBLE FLAG.
- W4: straight Union 218 counted -> 218
- W5: 1 AM: Haight 272 straight, Gorham 101 -> 373
- W6: midnight: "Oorhiiui. 570. I latent., 520; aud Kay, 80" = Gorham 570?,
  Haight 520, Fay 80 -> 1,170, BUT ward total polled is only 1,017.
  Contradiction: EXCLUDED from floor. GARBLE FLAG (Gorham may be 370).
- W7 P1/P2: no counts (officers gruff / estimate only)
- W8 P1: straight Union (Gorham) "IV»5" ~195; straight Dem (Haight) garbled
  "£i\" -> EXCLUDED except nothing clean. EXCLUDED.
- W8 P2: straight Haight "3?5" garbled; straight Gorham 208 -> 208 (Gorham
  side only)
- W9: essentially complete by 1 AM(?): "Haight, 672; Gorham, 404; Fay, ?"
  with "Haight's Plurality, 268" (672-404=268 checks) -> 1,076
- W10 P1: 560 enumerated at 1 AM (Gorham 120, Haight 440; sums 560 ok) -> 560
- W10 P2: 356 straight tallied at 1 AM (Gorham 208?, Haight 160; 208+160=368
  vs 356 stated: minor garble) -> 356 (use stated tally count)
- W11 P1: Haight 570, Gorham 283 (plurality 287 checks: 570-283=287), Fay 5
  -> 858 (ward appears fully counted; polled 878)
- W11 P2: Haight 475, Gorham 363 (plurality 112 checks: 475-363=112; OCR
  prints "331" but plurality arithmetic says 363), Fay ~2 -> 838
- W12 P1/P2: estimates only, no counts

Legible-floor sum (my arithmetic): 500+317+218+373+208+1076+560+356+858+838
= 5,304 ballots counted by ~2 AM = 30.4% of official final 17,472.
Excluding the garble-flagged W3 (317): 4,987 (28.5%).
Gate: 5,304 < 17,472 ceiling. PASS.
Verdict: NIGHT COUNT FLOOR ~5,000-5,300 (governor-contest ballots counted by
2 AM per Alta ward canvass). Needs human page-image read for W3, W6, W8
garbles. Poll-list total 17,365 recorded separately (NOT a count).

## PAGE-IMAGE VERIFICATION PASS (2026-07-08, supersedes OCR-only figures above)

Method: foreground-tab raw-CDP screenshots of the CDNC article viewer
(scan tiles render only in a visible tab; background tabs paint black).
Note for future sessions: full-page image / staticpdf downloads
(?a=is&type=pageimage|staticpdf) are LOGIN-GATED; the viewer screenshot
route is the working one. Valid a=is types: pageimage, pagetileimage,
staticpdf. OPERATOR RULE (2026-07-08): create tabs with background:true
only, never bringToFront; the Chrome window is hidden at OS level.

Screenshots (all in scratchpad imgs/):
- cdnc_18610522_p1_returns.png (+ cdnc_18610522_zoom_a/b.png crops)
- cdnc_18630520_p1_returns.png
- cdnc_18640518_p1_returns.png
- cdnc_18650517_p1_returns.png
- cdnc_18650907_p1_returns.png
- cdnc_18660906_p1_returns.png (+ cdnc_18660906_table_zoom.png crop)
- cdnc_18670905_p1_local.png (+ cdnc_18670905_zoom_a.png, z67_1/2/3.png crops)

### Corrected per-election figures (my visual read of the scans; arithmetic mine)

1861-05-21 (final 11,507): counted by press (midnight-2:30 AM):
D1 275 (210P+65F of 690 cast); D2 1,303 (assorting COMPLETE at midnight:
750 P.Union + 553 Fusion; stated P majority "about two hundred" checks
750-553=197); D3 809 (mayor at 12:30: Teschemacher ~428 + Fay 381;
straights-only alternative 268+230=498, checks 268+230+340scr=838 total);
D4 514 (331+183, majority ~150 checks 148); D5 917 COMPLETE (Tesch 528 +
Fay 389 of 934 cast); D6 630 (350+280); D7 0 (no count, ~500 polled,
"terribly scratched", Fusion ~100 ahead on aggregate); D8 422 (264+158,
majority 106 checks); D9 796 (People's 290str+173scr=463, Fusion
174str+159scr=333, "Total counted, 796" checks); D10 0 ("systematic
counting had not sufficiently progressed", 1,743 polled); D11 436 COMPLETE
(247F+189P; all four internal sums check); D12 331 COMPLETE.
TOTAL = 6,433 = 55.9% of 11,507. Conservative (D3 straights only): 6,122
(53.2%). GATE PASS.

1863-05-19 (final 11,417): "CITY ELECTION RETURNS 1863" table read from
scan. Mayor: Coon 75+215+215+202+473+[D6 blank]+393+683+449+715+[D11
blank]+175 = 3,595; Holland 164+236+83+128+288+[D6 blank]+159+276+266+
615+130+285 = 2,630. MAYOR CONTEST COUNTED = 6,225 = 54.5% of 11,417.
Cross-check Sheriff: Ellis 3,475 + Bryant 2,522 = 5,997 (consistent).
D6 uncounted at press; D11 Coon-side missing (Citizens 130 in).
GATE PASS. (11,417 in the same issue is the poll-list aggregate, NOT a count.)

1864-05-17 (final 10,847 = official Sheriff total): "ELECTION RETURNS, MAY
SEVENTEENTH" table read from scan. Columns 1-6,8,9,11,12-1st,12-2d have
counts; SEVENTH and TENTH entirely blank at press. Sheriff: Davis
350+525+609+525+575+606+923+483+571+131+79 = 5,377; Weller 200+156+91+139+
120+130+220+197+418+98+84 = 1,853. SHERIFF CONTEST COUNTED (table) = 7,230
= 66.7% of 10,847. Cross-check Auditor 7,210. Text adds D7 counted by
midnight: entire vote 1,363 -> ~8,593 counted incl. D7. D10 uncounted
(text: proportion statement only). GATE PASS (7,230 < 10,847; 8,593 <
10,847). Poll list 10,916 (Sanitary Fund table) NOT a count.

1865-05-16 (final 14,196): "CITY ELECTION, MAY 16" table read from scan.
Sheriff: Davis 390+[D2 blank]+405+462+545+390+816+700+462+643+[D11 blank]+
197 = 5,010; Bluxome 374+387+206+482+272+442+576+368+723+187 = 4,017.
SHERIFF CONTEST COUNTED (table) = 9,027 = 63.6% of 14,196. Mayor table
(D7 blank too): Coon 3,780 + Rowell 3,939 = 7,719. Narrative adds D2 at
3 AM (Coon 475 + Rowell 353 = 828) and D11 complete (450+497=947):
ballpark night total ~10,800. GATE PASS.

1865-09-06 (final 13,354): table read from scan; blank columns are
SIXTH, EIGHTH, NINTH, TENTH -> the narrative's "Fifth District" partial is
actually the SIXTH (OCR misread; proven by elimination: table FIFTH is
fully printed and its unexpired-contest sum 787 < the narrative partial
1,065, impossible for the same district).
Unexpired-Senate contest (single vote per ballot; Pixley U + Nunan D),
per printed district: D1 186+614=800 (vs 792 polled: matches within table
print error, validates pairing); D2 239+318=557; D3 288+268=556; D4
271+435=706; D5 376+411=787; D7 474+774=1,248; D11 143+430=573; D12-1st
137+150=287; D12-2d 54+187=241. Table subtotal = 5,755.
Clocked 2:30 AM straights (narrative): D6 1,065 + D8 1,096 + D9 522 +
D10 1,994 = 4,677.
NIGHT TOTAL ~= 10,432 = 78.1% of 13,354 (assumption flagged: Pixley-Nunan
as the unexpired pairing; D1 check supports). Conservative claim: 4,677
clocked partials alone (35.0%). GATE PASS.

1866-09-05 (final 13,371): "ELECTION RETURNS. SEPTEMBER 5, 1866" table
read from scan (crop cdnc_18660906_table_zoom.png). FIRST ward column
empty for every contest (narrative: First Ward count delayed); TOTALS
column unfooted. Chief of Police, wards 2-12: Crowley (U)
513+389+548+439+589+665+975+429+439+570+361 = 5,917; White (D)
397+166+362+278+260+658+744+414+465+701+387 = 4,832.
CHIEF-OF-POLICE CONTEST COUNTED = 10,749 = 80.4% of 13,371.
Cross-check Tax Collector: Story 6,269 + Cobb 4,562 = 10,831.
Tenth ward's table entry is partial (its 1st-precinct straights are
reported separately in text: Dem 641, Union 582, not in table), so 10,749
is a floor. Clocking: "count being still in progress in several precincts
as we go to press"; Third Ward returns received 9:30 PM. GATE PASS.

1867-09-04 (final 17,472): ward-section crops read (z67_1/2/3.png):
W3 resolved: "At a quarter past two o'clock this morning... Gorham, 128;
Haight, 317" -> 445. W5 resolved: 1 AM "Haight had 272 straight tickets,
and Gorham, 164" -> 436. W6 read: "At midnight the Ward officers had
counted for Gorham, 570, Haight, 5?0; and Fay, 30 votes" -- Haight digit
ambiguous (520 makes 1,120 > 1,017 polled; 420 makes 1,020 ~= 1,017
polled, so the ward was essentially fully counted at midnight; kept
FLAGGED). W8 P1 resolved: "Gorham, 195; ... Haight, 231" -> 426. W8 P2:
straight Haight 386 + straight Gorham 208 = 594.
Revised floor (W2 500 + W3 445 + W4 218 + W5 436 + W8P1 426 + W8P2 594 +
W9 1,076 + W10P1 560 + W10P2 356 + W11P1 858 + W11P2 838) = 6,307 = 36.1%
of 17,472. Including flagged W6 (1,017, capped at its polled total):
7,324 = 41.9%. W1, W7, W12 documented no-count at press. GATE PASS.
RECAPITULATION 17,365 remains a POLL LIST, not a count.

### Human verification packet (paths + claimed values + fail criteria)
Open each persistent link (normal browser, no login needed for viewing):
1. https://cdnc.ucr.edu/?a=d&d=DAC18610522.2.3 -- claims: D2 "750 People's
   Union tickets, and 553 Fusion"; D9 "Total counted, 796"; D11 total 436.
   FAIL if any printed digit differs.
2. https://cdnc.ucr.edu/?a=d&d=DAC18630520.2.6 -- claims: Mayor row Coon
   ends ...683, 449, 715, [blank], 175; Holland ...276, 266, 615, 130,
   285; Sixth column blank. FAIL if Sixth has printed numbers.
3. https://cdnc.ucr.edu/?a=d&d=DAC18640518.2.4 -- claims: Sheriff Davis
   350/525/609/525/575/606/[7th blank]/923/483/[10th blank]/571/131/79;
   Weller 200/156/91/139/120/130/[blank]/220/197/[blank]/418/98/84.
4. https://cdnc.ucr.edu/?a=d&d=DAC18650517.2.6 -- claims: Sheriff Davis
   390/[blank]/405/462/545/390/816/700/462/643/[blank]/197; Bluxome
   374/[blank]/387/206/482/272/442/576/368/723/[blank]/187.
5. https://cdnc.ucr.edu/?a=d&d=DAC18650907.2.3 -- claims: blank columns
   are SIXTH, EIGHTH, NINTH, TENTH; Nunan row 614/318/268/435/411/[6th
   blank]/774/.../430/150/187; Pixley row 186/239/288/271/376/[blank]/474/
   .../143/137/54.
6. https://cdnc.ucr.edu/?a=d&d=DAC18660906.2.12 -- claims: Crowley
   [1st blank]/513/389/548/439/589/665/975/429/439/570/361; White
   397/166/362/278/260/658/744/414/465/701/387; TOTALS column unfooted.
7. https://cdnc.ucr.edu/?a=d&d=DAC18670905.2.3 -- claims: W3 "Gorham,
   128; Haight, 317" at 2:15 AM; W5 "Haight had 272... Gorham, 164" at
   1 AM; W6 "Gorham, 570, Haight, 5?0; and Fay, 30" (is Haight 420 or
   520?); W8P1 "Gorham, 195 ... Haight, 231". KEY ASK: read the W6 Haight
   digit and the W5 Gorham digit (164 vs 104).
