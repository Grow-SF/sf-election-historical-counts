# Wave 3: pioneer-era SF election-night counts, 1849-1858

## FINAL VERDICT TABLE (2026-07-08, all ten resolved; details per election below)
| election | final | night count (E+1 morning paper) | % | verdict | source |
|---|---|---|---|---|---|
| 1849-11-13 | 3,119 | NO E+1 PAPER EXISTS: Alta was weekly; Daily Pacific News printed Tue/Thu/Sat, no Nov 14 issue (CDNC: "Oops" page); earliest returns E+2 | - | DEAD END (no qualifying publication) | WAC18491115.2.4 (E+2, complete 3,169 polled); DPN18491115.2.4 |
| 1850-10-07 | 3,440 | none printed: E+1 Alta gives majorities only ("Broderick ... majority of 336"), "judges ... met again this morning, to complete the canvassings ... result in full to-morrow" | - | DEAD END (no count table E+1; quote documents overnight state) | DAC18501008.2.5 |
| 1851-09-03 | 5,774 | ~1,100-1,150 (2 A.M.: "little over a hundred votes ... counted in each ward" x7 city wards + complete 8th/9th/10th/11th district returns = 429) | ~19-20% | FOUND (clocked 2 A.M. state; city part qualitative) | DAC18510904.2.6 |
| 1852-11-02 | 8,692 | ~6,122 at 4 A.M. (ward table scan-verified; W1 ~870 flagged: its "counted up to 5 P.M." line printed blank) | ~70% | FOUND (scan-verified) | DAC18521103.2.8 |
| 1853-09-07 | 10,955 | 2,670 (per-ward clocked: 0+43+618+~41+652+610+706+0) | 24.4% | FOUND | DAC18530908.2.15 |
| 1854-09-06 | 9,949 | ~2,717 by midnight (W3 ~935, W4 ~105, W5 979, W6 ~210, W7 ~488; W1/W2/W8 zero, boxes sealed under armed guard; shooting at W1 poll) | ~27% | FOUND (fraud-era color verbatim) | DAC18540907.2.5 |
| 1855-09-05 | 12,351 | ~2,726 (scan-verified: 100+2,116+20+~70+0+420; W7 only assorted; W8 stuffing note "about 300 tickets were stuffed into the box") | ~22% | FOUND (scan-verified) | DAC18550906.2.9 |
| 1856-11-04 | 12,019 | 3,947 FLOOR at 3 A.M. (SF telegraph dispatch in Sacramento Daily Union E+1; DAC 11/5 issue "published but no copy is available") | 32.8% floor | FOUND via SDU (Alta dead end documented) | SDU18561105.2.8 |
| 1857-09-02 | 10,326 | ~5,864 sorted/counted by midnight per-district table (straight-ticket era; several digits need operator zoom) | ~57% | FOUND (digits flagged) | DAC18570903.2.15 |
| 1858-09-01 | 8,584 | ~1,712 at 1 A.M. (per-district counted states; D2 state-ticket digits garbled, flagged) | ~20% | FOUND (D2 flagged) | DAC18580902.2.20 |

Screenshots: scratchpad/imgs/{wac18491115_2_4_election_results, dpn18491115_2_4_election_sf,
dac18501008_2_5_the_election, dac18510904_2_6_election_returns,
dac18521103_2_8_latest_returns_4am, dac18530908_2_15_election_returns,
dac18540907_2_5_election_returns, dac18550906_2_9_further_from_wards,
sdu18561105_2_8_sf_dispatches, dac18570903_2_15_returns_midnight,
dac18580902_2_20_city_items_1am, dac18561105_issue}.png
Persistent links: https://cdnc.ucr.edu/?a=d&d=<OID> for every OID above.
OPERATOR EYES WANTED: 1852 W1 block; 1857 recapitulation row + D1/D2/D9 digits; 1858 D2
Supreme Court/Congress digits; 1855 W7 "409" Democratic straights.

Agent salvage file. Written as I go. Mission: day-after morning-paper (Daily Alta
California, CDNC code DAC; fallback Placer Times / Sacramento papers) overnight
counts for the 10 pioneer elections. Stamp E+1 T03:00, cutoff E+1 06:00.
Poll lists ("votes polled") are NOT counts. Dead ends are deliverables too.

Targets (official finals = gate ceilings):
| # | election | E+1 issue | official final | status |
|---|----------|-----------|----------------|--------|
| 1 | 1849-11-13 Governor + Constitution | (Alta weekly in 1849; search 11/14-11/22 + Placer Times) | 3,119 | DEAD END (no E+1 paper existed/held) |
| 2 | 1850-10-07 general | DAC18501008 | 3,440 | DEAD END (no count printed E+1) |
| 3 | 1851-09-03 gubernatorial | DAC18510904 | 5,774 | FOUND ~1,100-1,150 @ 2 A.M. |
| 4 | 1852-11-02 presidential | DAC18521103 | 8,692 | FOUND ~6,122 @ 4 A.M. (scan-verified) |
| 5 | 1853-09-07 gubernatorial | DAC18530908 | 10,955 | FOUND 2,670 @ ~1-2 A.M. |
| 6 | 1854-09-06 general (fraud year) | DAC18540907 | 9,949 | FOUND ~2,717 @ midnight |
| 7 | 1855-09-05 gubernatorial | DAC18550906 | 12,351 | FOUND ~2,726 (scan-verified) |
| 8 | 1856-11-04 presidential + municipal | DAC18561105 | 12,019 | FOUND 3,947 floor @ 3 A.M. via SDU |
| 9 | 1857-09-02 gubernatorial + city | DAC18570903 | 10,326 | FOUND ~5,864 @ midnight |
| 10 | 1858-09-01 general | DAC18580902 | 8,584 | FOUND ~1,712 @ 1 A.M. |

Access: Chrome CDP at 127.0.0.1:9222, raw CDPSession (no Runtime.enable before
clearance), then Runtime.evaluate fetch() inside the cleared tab.

## Log
- 2026-07-08: session start. Chrome 150 at :9222 confirmed alive. Salvage file created.
- Speed recipe works: one nav to cdnc.ucr.edu clears Cloudflare, then Runtime.evaluate
  fetch() returns server-rendered search HTML and getSectionText XML. Script:
  scratchpad/cdnc_batch.js (usage: node cdnc_batch.js OUTDIR URL...).
- All 9 daily E+1 DAC issues EXIST (titles verified): DAC18501008, DAC18510904,
  DAC18521103, DAC18530908, DAC18540907, DAC18550906, DAC18561105, DAC18570903,
  DAC18580902. Issue shell HTML has no TOC (JS-loaded); scoped date search is the
  route to section OIDs.
- Round-1 searches (txq=election, puq=DAC, single-date) hits of interest:
  - 1850-10-08: DAC18501008.2.5 (LAW COURTS: "THE ELECTION. — The contest at the polls yesterday...") only hit.
  - 1851-09-04: DAC18510904.2.6 ELECTION RETURNS; .2.9 CITY INTELLIGENCE Election Day; .2.3 editorial.
  - 1852-11-03: DAC18521103.2.8 "The Latest Election Returns"; .2.10 The Presidential Election; .2.9 LOCAL MATTERS incidents.
  - 1853-09-08: DAC18530908.2.15 Election Returns ("The election yesterday passed in comparative peace, but a full vote..."); .2.17 The Election; .2.16 Alameda returns.
  - 1854-09-07: DAC18540907.2.5 ELECTION RETURNS; .2.4 THE ELECTION YESTERDAY - INCIDENTS; .2.3 editorial.
  - 1855-09-06: DAC18550906.2.10 ELECTION RETURNS; .2.8 The Election.
  - 1856-11-05: ZERO search hits despite issue existing (possibly unindexed OCR); needs TOC-by-navigation fallback.
  - 1857-09-03: DAC18570903.2.15 "RETURNS OF THE ELECTION. THE PEOPLE'S TICKET VICTORIOUS IN THIS CITY. WELLER PROBABLY ELECTED."; .2.2 evening-edition reprint; .2.14 editorial.
  - 1858-09-02: DAC18580902.2.18 (The election, yesterday, passed off very quietly + People's Ticket returns?); .2.20 CITY ITEMS; .2.19 telegraph (Sacramento).
  - 1849 (window 11/14-11/30, all papers): Alta was WEEKLY (WAC): WAC18491115.2.4 "THE ELECTION—RESULTS" (E+2); WAC18491115.2.23.6 same title; Daily Pacific News DPN18491115.2.4 "The Election in San Francisco" (E+2 daily); WAC18491122.2.10 ELECTION RETURNS; DPTT18491117.2.5 THE ELECTION (Placer Times and Transcript).
- Search URL template (copy-pasteable): https://cdnc.ucr.edu/?a=q&hs=1&r=1&results=1&txq=election&txf=txIN&ssnip=txt&puq=DAC&dafdq=DD&dafmq=MM&dafyq=YYYY&datdq=DD&datmq=MM&datyq=YYYY&e=-------en--20--1--txt-txIN--------
- OCR endpoint: https://cdnc.ucr.edu/?a=da&command=getSectionText&d=OID&f=AJAX&e=-------en--20--1--txt-txIN--------

## Findings round 1 (OCR texts in scratchpad/sections_r1/, mapping in oids_r1.txt)

### 1849-11-13 (final 3,119) - CLOSED as dead end
- DPN18491114 (E+1) does NOT exist in CDNC ("Oops!" page; DPN printed Tue/Thu/Sat, Nov 14
  was Wednesday, so no E+1 issue was printed). Placer Times and Transcript's first
  post-election issue DPTT18491117.2.5 (E+4) carries SACRAMENTO city returns (1,863 polled
  there), no SF night state. Alta was WEEKLY (WAC). WAC18491115.2.4 (E+2, Weekly Alta 11/15)
  "THE ELECTION - RESULTS": "instead of five thousand votes, as was generally expected, only
  thirty-one hundred and sixty-nine were polled" + COMPLETE 2-district table
  "Whole No. of votes polled, 2259 910 3169" - complete returns "as taken from the minutes of
  the judges of election, for the District of San Francisco". NOT a night count (E+2 weekly).
- Daily Pacific News DPN18491115.2.4 (E+2 daily): "The total number of votes cast in San
  Francisco, is we learn, about 3,3[0]0" + partial city returns "as far as received".
- TODO: does DPN18491114 (E+1) exist? Check.

### 1850-10-07 (final 3,440)
- DAC18501008.2.5 (E+1, p.2 LAW COURTS/city items col): "THE ELECTION. - The contest at the
  polls yesterday was stronger than we ever before witnessed in this city... Mr Broderick is
  re-elected to the Senate by a majority of 336... The judge of the election met again this
  morning, to complete the canvassings, and we shall give the result in full to-morow."
  NO numeric ward/count table in the E+1 paper; results stated as majorities only.
  TODO: search more terms in this issue to confirm no returns table exists.

### 1851-09-03 (final 5,774) - GOLD, explicit 2 A.M. count state
- DAC18510904.2.6 "ELECTION RETURNS." (E+1): "it is impossible to give, this morning, anything
  like returns of the election. Every name on every ticket is read in the counting by the
  Inspectors, and up to two o'clock this morning, but little over a hundred votes had been
  counted in each ward. At this rate it will take at least through the whole of to-day to
  count the remaining votes. From the 8th ward and county precincts we give the returns,
  having procured them by special express."
- Votes POLLED per ward (poll list, NOT counts): W1 1,216; W2 440; W3 1,282; W4 783; W5 811
  (350 Whig-headed/200 Dem/261 Ind assorted); W6 393 (165 W/133 D/9? I); W7 528. Sum W1-7 = 5,453.
- COUNTED overnight: city wards ~100+ each at 2 A.M. (7 wards = ~700-800); complete returns for
  8th District (Gov: Bigler 82 + Reading 62 = 144), 9th (12+14 = 26), 10th (142+11 = 153),
  11th Rancho Merimontes (106). County districts sum (Gov) = 429.
  Night-count estimate: ~700 (city, qualitative "little over a hundred" x7) + 429 = ~1,100-1,150
  of 5,774 final (~20%). Era practice: every name on every ticket read aloud (call-every-name).

### 1852-11-02 - SCAN-VERIFIED (imgs/dac18521103_2_8_latest_returns_4am.png, fully legible)
Direct page-image reading of DAC18521103.2.8 corrects the OCR:
- W1: electors Haskell 385, all others (both tickets) 485; "Total number of votes counted up
  to 5 P. M....." printed with NO NUMBER (blank after the leader dots; likely a typeset slip);
  "Whole number of ballots cast 1238" (not 1338). Counted state ambiguous, ~870 by top pair.
- W2: Pierce and King 669, Scott and Graham 539 (not 639; 669-539=130 = printed Dem majority
  checks), Hale and Julian 8, over all 122. Counted = 1,216.
- W3: at 3:30 A.M. about 140 counted: Whig electoral 78 + Democratic 58 = 136 (checks).
- W4: cast 796, counted complete: 443+339+8(FreeSoil)+1(Webster)+1(Scott&Graham) = 792.
- W5: cast 1,048, complete: 592+431+6+4+15(torn off) = 1,048 exact.
- W6: cast 1,070; only one race counted: Bowie 466 + Byrne 518 = 984.
- W7: cast 788, complete: 355+424+5 = 784.
- W8 (As Reported): cast 571; straights only: Regular Democratic 114, Whig 51 = 165.
- 10th Precinct: cast 123, complete (electors ~52+72).
NIGHT COUNT SUM at 4 A.M.: ~870(W1, flagged) + 1,216 + 140 + 792 + 1,048 + 984 + 784 + 165
+ 123 = ~6,122 of 8,692 final = ~70% (presidential-elector count ran fast; W1 the main
uncertainty; operator eyes wanted on W1 block).

### 1852-11-02 (final 8,692) - overnight table "up to 4 A.M." (pre-verification OCR notes)
- DAC18521103.2.8 "The Latest Election Returns." (E+1): "Below we give the ballot of the late
  election, as far as ascertained up to 4 A. M. this morning". Per-ward states:
  W1: electors ~485/385 (garbled), "Total number of votes counted up to 5 P.M....:" [OCR-lost
  number], "Whole number of ballots cast ....1338"; W2: Pierce&King 669, Scott&Graham 639,
  Hale 8 (= 1,316, looks complete); W3: "Up to half-past three o'clock this morning, about 140
  tickets had been counted"; W4: whole 796, electors 443/339 (complete); W5: whole 1,048,
  592/431 (complete); W6: whole 1,070, partial (Bowie 466/Byrne 518); W7: whole 788, 355/424
  (complete); W8: whole 571, only straights "as reported" Dem 114/Whig 51; 10th Precinct
  total 123 complete. NEEDS page-image verification of W1 counted figure.
  Rough counted-by-4AM sum approx 5,400-6,200 of 8,692 (very uncertain until W1/W6 resolved).

### 1853-09-07 (final 10,955) - explicit per-ward clocked count states
- DAC18530908.2.15 "Election Returns" (E+1): "The number of votes polled was 10,606." Per ward:
  W1 1,486 polled, NONE counted (inspectors arranged ballots til ~10 PM, sealed box, "went to
  rest"); W2 1,8?7 polled, 43 ballots counted straight through, closed ~12 o'clock (Bigler 30,
  Waldo 13); W3 1,357 polled, at 1 A.M. 618 State tickets counted (Waldo 358, Bigler 246);
  W4 1,216 polled, count stopped 1 o'clock, ~41 counted straight through (Waldo 17, Bigler 24);
  W5 1,089 polled, at 2 o'clock 652 counted (Bigler 340, Waldo 312); W6 1,473 polled, at 1:30,
  610 counted (Waldo 275, Bigler 330); W7 1,277 polled, at 1 o'clock 706 counted (aldermen
  only); W8 670 polled, no returns.
  NIGHT COUNT SUM: 0+43+618+41+652+610+706+0 = 2,670 of 10,955 final = 24.4% (W4's exact
  counted number OCR-lost, inferred ~41 from candidate sums).

### 1854-09-06 (final 9,949, fraud year) - "counted up to 12 o'clock last night"
- DAC18540907.2.5 "ELECTION RETURNS." (E+1): "The following is a list of the votes counted up
  to 12 o'clock last night in the various Wards. It will be seen that in several Wards there
  were no votes counted at all. The ballot boxes were sealed and strong guards placed over
  them in all the Wards."
  W1: row by shoulder strikers 15 min before close, box closed+sealed, "A man by the name of
  McDowall was shot." W2: "No votes counted. Ballot box sealed... Twenty-five citizens,
  supposed to be Know-Nothings, volunteered to stay at this Ward all night, to prevent any
  attack on the ballot box." W3: Congress (vote-for-2) Bowie 576, Benham 677, Denver 221,
  Herbert 227, Church 183, Doyle 1??, Wilson 64; Clerk Sup Ct: Beard 61? [612?], Woodside 103,
  Leake 220 (=~935+ single-vote). W4: Mayor Garrison 37, Haven 18, Webb 41, Herman 9 (~105
  counted). W5: Congress Bowie 559, Benham 627, Denver 276, Herbert 260, Churchman 147,
  McDougal 115; Clerk: Beard 572, Wood 122, Leake 285 (=979). W6: straight-sorted 50/160
  pattern = ~210 counted. W7: Mayor Haven 114, Webb 234, Garrison ~118, Herman 22 (~488).
  W8: "The number of tickets tallied with the clerk's account" (no counts).
  NIGHT COUNT SUM (single-vote offices where given): 0+0+935+105+979+210+488+0 = ~2,717 of
  9,949 = ~27%. FRAUD-ERA COLOR: shooting at W1 poll ~10 PM, armed guards on all boxes.

### 1855-09-05 (final 12,351) - SCAN-VERIFIED (imgs/dac18550906_2_9_further_from_wards.png)
- DAC18550906.2.9 "Further from the different Wards." (E+1), read directly from the legible
  page image (OCR was badly garbled):
  W1: "The Inspectors in this ward counted 100 straight Democratic tickets, and then sealed
  the boxes for the night." (100, not 160)
  W2: "Bigler, 1200; Johnson, 916; Bigler's majority, 284. Only the Gubernatorial votes have
  been counted. The counting was then closed till this morning." (= 2,116 counted; 1200-916
  = 284 checks)
  W3: "Twenty straight Democratic tickets were counted, and the counting closed." (20)
  W4: "As far as counted at 12 o'clock: Bigler, 37; Purdy, 39; Johnson, 33; Anderson, 31;
  Murray, 32; Terry, 33; Myron Norton, 37; Bryan, 37; Johnson (Sheriff), 36; Scannell, 34."
  (~70 gubernatorial ballots)
  W5: "The boxes were sealed at the closing of the polls. No counting till this morning." (0)
  W6: "420 straight tickets were counted, of which 240 were Know-Nothing and 180 Democratic.
  The boxes were then sealed for the night." (420)
  W7: "They had assorted all the tickets at 15 minutes after 12. Know-Nothing tickets, 417;
  Whig and mongrel tickets, 215; straight Democratic tickets, 409; Democratic split tickets,
  150; Know Nothing split tickets, 300; general split tickets, 180. The counting will proceed
  all night." (assorted = 1,671; counting NOT complete by press; excluded from count sum)
  W8: "Number of votes 1604, by an outside tally list; number of votes 1604, by judges and
  inspectors. It has been stated that about 300 tickets were stuffed into the box. James Lee
  and Samuel Cowles were the parties who kept the outside tally list." (BALLOT-STUFFING NOTE)
- DAC18550906.2.8 "The Election" (E+1): per-ward VOTES POLLED (poll list, not counts):
  W1 1,936; W2 2,125; W3 1,247; W4 ~800s; W5/W6/W7 garbled.
- DAC18550906.2.10 "ELECTION RETURNS" is interior-county telegraph only.
  NIGHT COUNT SUM: 100 + 2,116 + 20 + ~70 + 0 + 420 + 0 + 0 = ~2,726 of 12,351 = ~22%.

### 1856-11-04 (final 12,019) - RESOLVED via Sacramento Daily Union 3 A.M. dispatch
- DAC18561105 is NOT HELD: the issue page says verbatim "Issue missing. This issue was
  published but no copy is available." (screenshot imgs/dac18561105_issue.png,
  https://cdnc.ucr.edu/?a=d&d=DAC18561105). No SF daily for 11/5/1856 in CDNC at all
  (all-paper search that date: only SDU, SRP, Chico Record, Marysville Herald, San Joaquin
  Republican). The Alta E+1 issue is a documented dead end in this archive.
- SUBSTITUTE E+1 MORNING PAPER: Sacramento Daily Union 11/5/1856 (SDU18561105.2.8 "ELECTION
  RETURNS. BY THE STATE AND ALTA TELEGRAPH LINES", Pacific Express) prints FOUR timestamped
  SF dispatches:
  - 1st: "San Francisco Nov. 4th - 1 p.m." (color only)
  - 2nd: "San Francisco, Nov. 4 - 10 p.m.": "Whole number of votes cast in San Francisco
    county, 12,152" (poll total; matches the 1857 Alta retrospective exactly). D2 Buchanan
    maj 155; D4 maj 20; D7 maj 23; D5/D6/D9 for Fremont; "The counting is not finished in
    these and the other districts not mentioned."
  - 3rd: "San Francisco, Nov. 5 - 12:15 a.m.(?)": D11 Buchanan 8 maj; D9 Fremont 190 maj;
    Vigilance-Committee man Wm. Andrews beaten at D9 poll.
  - 4th: "San Francisco, Nov. 5 - 3 a.m." PER-DISTRICT CAST/COUNTED:
    D1 962 cast, 252 counted (Buch 158, Frem 68, Fill 21); D3 1,505 cast, COMPLETE (Buch 632,
    Frem 607, Fill 255, blank 11 = 1,505); D5 1,447 cast, at 12 o'clock counted Buch 455 +
    Frem 515 + Fill 255 = 1,225; D6 860(?) cast, at 12 o'clock 100 counted; D8 600 cast, 136
    counted (50+69+17); D10 1,248 cast, 350 counted; D11 ~393 cast, 200 counted; D12 336
    cast, 179 counted.
  NIGHT COUNT (3 a.m. state, counted sum over districts reported): 252+1505+1225+100+136+
  350+200+179 = 3,947 FLOOR (D2, D4, D7, D9 counted amounts not stated though majorities
  were being reported) of final 12,019 = 32.8% floor.
  Source URL: https://cdnc.ucr.edu/?a=d&d=SDU18561105.2.8 ; OCR fetch:
  https://cdnc.ucr.edu/?a=da&command=getSectionText&d=SDU18561105.2.8&f=AJAX&e=-------en--20--1--txt-txIN--------

### 1857-09-02 (final 10,326) - midnight per-district table + 2 A.M. telegraph close
- DAC18570903.2.15 "RETURNS OF THE ELECTION..." (E+1): "Returns from the City Polls up to
  Midnight. We give below all that could be ascertained of the result, in the several
  districts, up to the hour of twelve, last night:"
  D1: 195? straight Dem + 133 straight Rep counted, remainder scratched; D2: "The entire vote
  for Governor was counted and declared": Stanly ???, Weller 650, Bowie 54, 17 scratched
  (D2 total polled 1,330); D3: 411 straight Rep + 319 straight Dem + 9 Am counted, 485
  scratched left; D4: 207 Rep + 195 Dem + 18 Am, 331 scratched left; D5: at 12, 75 straight
  Dem counted (abandoned full count after ~50); D6: 130 Dem + 60 Rep by 12; D7: 305 Dem + 60
  Rep counted, "at least 500 straight Republican tickets yet to count"; D8: at 12 only ~40
  counted (Stanly 31, Cheeseman 31, Weller 15, Walkup 30, Doane 39, Harmon 18); D9: 5?? Rep +
  350 Dem + 10 Am, 249 scratched; D10: 438 Rep + 357 Dem + 57 People's + 30 Settlers + 20 Am;
  D11: ALL votes counted at 2 o'clock this morning (Stanly ~20 maj; D11 polled 381);
  D12: at 11:30, 127 Dem + 83 Rep + 19 Am.
  Total city vote table (poll list): 10,585 (1857) vs 12,152 (1856) by district.
  "Interior Election Returns. Up to two o'clock this morning, at which hour the telegraph
  office closed..."
  NIGHT-COUNT (sorted/counted tickets by midnight, straight-ticket counting): approx
  328+1330+739+420+75+190+365+40+860+907+381+229 = ~5,864 of 10,326 = ~57% (several digits
  need page-image verification).

### 1858-09-01 (final 8,584) - "1 O'CLOCK A.M." per-district counted states
- DAC18580902.2.20 "CITY ITEMS / The Election" (E+1): per-district polled totals (D1 687,
  D2 1,163?, D3 8??, D4 733, D5 7?7, D6 673, D7 1,010, D8 ~836, D9 1,013, D10 774, D11 1??,
  D12 ~8?2) then explicit "1 O'CLOCK A.M." section:
  D1: "Whole number of votes counted 100" (Baldwin 38, Currey 61?); D2: "No votes on the local
  offices in this ward, up to midnight, had been counted" BUT state ticket counted: Supreme
  Court Currey ~5?1, Baldwin 4?0; Congress McKibben ?42, Tracy 390 (implies ~1,000+ state
  ballots counted in D2); D3: 102 straight Administration votes counted; D4: votes counted
  ~104? (Coon 94, Currey 77, Baldwin 32...); D5: no definite returns; D6: "Only 62 votes
  counted. Forty-seven straight Lecompton tickets."; D7: total votes counted 85 (Baldwin 51,
  Currey 30); D8: counted ~1?? tickets (Curry 69, Baldwin 59 = 128); D9: 80 votes counted;
  D10: 30 votes counted; D11/D12: no counted figures.
  Total polled: "The entire vote cast yesterday is eight thousand, seven hundred and
  forty-two" (8,742) vs final 8,584.
  NIGHT COUNT SUM: 100+~1021(D2 state)+102+104+0+62+85+128+80+30 = ~1,712 of 8,584 = ~20%
  (D2 digits need page-image verification).
- DAC18580902.2.18 (editorial): "we give in our columns to-day... the general city returns up
  to a late hour in the night. The total vote polled in this county, yesterday, was 8,742."
