# Wave 3: night counts for 8 SF county-run party primaries, 1899-1906

Agent salvage file. Written as I go. Repo untouched.

Method: CDNC (cdnc.ucr.edu) via raw-CDP Chrome at :9222, script
`scripts/archive-recovery/cdnc_fetch.js`. Day-after SF Call issue
`SFC<YYYYMMDD>`. Gate: no claimed night figure may exceed the official
final total for that primary. Night cutoff E+1 06:00; stamp convention
E+1 T03:00 for morning-edition counts.

| # | election | final (gate) | day-after issue | status |
|---|----------|--------------|-----------------|--------|
| 1 | 1899-08-08 municipal primary | 32,521 | SFC18990809 | PARTIAL 30,479 (17/18 dist) |
| 2 | 1901-08-13 municipal primary | 22,939 | SFC19010814 | NIGHT COUNT 22,898 |
| 3 | 1902-08-12 state primary | 28,697 | SFC19020813 | DEAD END (documented) |
| 4 | 1903-08-11 municipal primary | 26,039 | SFC19030812 | NIGHT COUNT 26,021 |
| 5 | 1904-05-03 primary | 9,384 | SFC19040504 | NIGHT COUNT 9,370 |
| 6 | 1904-08-09 state primary | 18,141 | SFC19040810 | NIGHT COUNT 17,914 |
| 7 | 1905-08-08 municipal primary | 28,951 | SFC19050809 | GATE CONFLICT 38,120 (flag) |
| 8 | 1906-08-14 state primary | 10,824 | SFC19060815 | NIGHT COUNT 10,554 |

---

## 1. 1899-08-08 municipal primary (final 32,521)

Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC18990809 (SF Call, 1899-08-09).
TOC fetched via `node scripts/archive-recovery/cdnc_fetch.js SFC18990809`;
page 12 OCR via `node cdnc_fetch.js SFC18990809 12`. Coverage lives on
page 12 (sections SFC18990809.2.153 "DOWNFALL OF THE POLITICAL BOSS CAUSED
BY THE NEW PRIMARY LAW", 2.157, 2.159); editorial "THE PRIMARY ELECTIONS."
on page 6 (2.88).

Lead paragraph (2.153, p12): "IIIRTY-THRF.E THOUSAND votes were cast at
the primary election yesterday" (= THIRTY-THREE THOUSAND, OCR-garbled).
33,000 exceeds the 32,521 gate, so treated as a rounded morning ESTIMATE,
not a count.

GOLD: district roundup in 2.153 headed "Number of Votes Cast The
Successful Tickets" gives per-Assembly-district totals with winning
tickets declared, 17 of 18 districts carrying a number (40th prints
winners but no total):
28th 1350, 29th 1590, 30th 1561, 31st 1773, 32nd 1345, 33rd 1890,
34th 2152, 35th 1723, 36th 2335, 37th 2600, 38th 2055, 39th 1311,
40th (none printed), 41st 2183, 42nd 1466, 43rd 1843, 44th 1826, 45th 870.
Sum = 29,873 (17/18 districts). Gate check: 29,873 < 32,521 PASS;
residual 2,648 for the 40th is plausible (37th polled 2,600).

Verbatim samples: "TWENTY-EIGHTH DISTRICT—Number of votes cast, 1350.
Republican County Committee delegates elected." ...
"FORTY-FIFTH DISTRICT— TotaI vote cast 870."

Overnight-count proof in same article: "Revised returns from the
Twenty-ninth District received at 2 a. m. show that Buckley wins sixteen
of the eighteen delegates. His ticket received 520. votes., The Committee
of One Hundred's ticket received 505 votes."

Verdict: NIGHT PARTIAL (contest-sum floor) = 29,873 in 17 of 18 Assembly
districts, SF Call 1899-08-09 p12, stamp 1899-08-09T03:00. Caveat: the
roundup says "votes cast" (not explicitly "counted"), but winners are
declared per district and 2 a.m. revised returns appear, so these are
tabulated returns, not poll lists.

## 2. 1901-08-13 municipal primary (final 22,939)

Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19010814 (SF Call, 1901-08-14).
Fetch: `node cdnc_fetch.js SFC19010814` (TOC), then `node cdnc_fetch.js
SFC19010814 1` (page 1 OCR; saved mirror/cdnc/SFC19010814/page_1.txt).
Coverage: page 1 lead "MARTIN KELLY, CHIEF OF THE COMBINED BOSSES, IS
WINNER AT PRIMARY ELECTION" (SFC19010814.2.2) with full per-candidate
delegate vote tables for Assembly districts 28th-45th (Primary League vs
Kelly & Crimmins columns), immediately under subhead "The election
Returns."

CITYWIDE NIGHT TOTAL, verbatim (section SFC19010814.2.2.1 "HOW AID IS
GIVEN TO BIG BOSS", page 1): "The total vote cast In the 106 precincts
yesterday was 22,838. Of this number the Republicans cast 19,021, the
Democrats 3633 and the Socialists 244."

FOOTING CHECK: 19,021 + 3,633 + 244 = 22,898, NOT the printed 22,838
(60 off). Either the printed total is a 19th-c. footing error or one
digit is OCR-garbled; needs a page-image read to arbitrate. Both values
pass the gate (< 22,939 final; headroom 101 and 41).
Corroboration: 3,633 Democratic ballots repeated in section 2.2.3
("KELLYITES RESORT TO TRICKERY"): "In the entire city only 3633
Democratic ballots were called for and voted yesterday." A separate
sentence says "Yesterday only 400G [4000] votes were thrown for delegates
to the Democratic municipal convention" (loose, vs the precise 3,633).

Completeness: the 38th-district Republican table is annotated
"*Incomplete. One precinct missing." so the tabulation was essentially
complete overnight, one precinct short in one district.

Verdict: NIGHT COUNT (near-complete, 106 precincts) = 22,838 as printed
(component sum 22,898), SF Call 1901-08-14 p1, stamp 1901-08-14T03:00.
FLAG for human page-image read: arbitrate 22,838 vs 22,898.

## 3. 1902-08-12 state primary (final 28,697)

Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19020813 (SF Call, 1902-08-13).
Fetches: TOC; page 4 OCR (`page_4.txt`); page 9 OCR (`page_9.txt`);
issue-scoped searches "total vote", "votes were cast", "light vote" via
`node cdnc_fetch.js SFC19020813 "search:<phrase>"` (search URL pattern:
https://cdnc.ucr.edu/?a=q&hs=1&r=1&results=1&txq=total+vote&txf=txIN&ssnip=txt&puq=SFC&dafdq=13&dafmq=08&dafyq=1902&datdq=13&datmq=08&datyq=1902&e=-------en--20--1--txt-txIN--------).

SF coverage: p4 "GAGE MACHINE FAILS TO WIN ONE-HALF OF CITY DELEGATION TO
CONVENTION, BUT RUEF IS WINNER" (SFC19020813.2.16 + subsections,
continuing p9). The morning-after story prints WINNERS ONLY: delegate
NAME lists per Assembly district for Republican factions, Union Labor
(2.16.3) and Democrats (2.16.4). No citywide vote total, no per-district
numeric totals, no candidate vote tables.

Count-status language, verbatim (2.16.1, p4): "An official count may be
necessary to determine the result in the Forty-first District" and "The
official count will probably diminish rather than increase the strength
of the allied bosses in San Francisco." Also (2.16): "The Republican
Primary League ... may win in the Thirty-fifth and Forty-fourth on the
official count."

Only numeric fragment (2.16.1, p4, 45th District, OCR noisy): "The
[Republican] vote in the district approximates 1200. of which Ruet
[Ruef] received 1050. The number of votes polled was 1800." That is one
district of 18, phrased as votes POLLED (excluded per house rule), and
"approximates": not usable as a floor.

Alternate papers: CDNC carries no SF Examiner/Chronicle; Daily Alta ends
1891. No other SF daily available for this date on CDNC.

Verdict: DEAD END (documented). The day-after Call declared winners from
unofficial returns but printed no overnight ballot tabulation for the
city; its own text defers contested districts to the official count.

## 4. 1903-08-11 municipal primary (final 26,039)

Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19030812 (SF Call, 1903-08-12).
Fetches: TOC; page 4 OCR (mirror/cdnc/SFC19030812/page_4.txt). Coverage:
p4 "UNITED REPUBLICAN LEAGUE COMPLETELY ROUTS THE BOSSES; SCHMITZ CRUSHES
CASEY AND M'NAB HOLDS DEMOCRATIC REINS" (SFC19030812.2.37 and
subsections) + "REPUBLICAN VOTE GROWS." (SFC19030812.2.39).

CITYWIDE FIGURE, verbatim OCR (section SFC19030812.2.37.1 "RESULT IS
DOWNFALL OF KELLY AND MARKS", p4): "The total vote at the primary as
forecasted by The Call exceeded SJ.OOO. The oflicial figures at .the
Registrar's office place the number at :6,CC1. ... Yesterday the
Republicans cast 13.30G votes, the Democrats 7443. the -Union Laboritcs
5066 and the Socialists 206."
Reconstruction: 13,306 + 7,443 + 5,066 + 206 = 26,021, which is the
natural de-garbling of ":6,CC1" (= 26,021) and passes the gate
(26,021 < 26,039 final; 18 short, consistent with a small canvass
addition). "SJ.OOO" is likely 25,000 (the Call's forecast).

PER-DISTRICT TABLE (SFC19030812.2.39 "REPUBLICAN VOTE GROWS.", p4):
"Throughout the city the Republicans polled half or even more of all the
votes cast. The following shows the total ballot as well as the vote
polled by each of the factions of the three paJtles:" District totals as
OCR'd: 28th 1418, 29th 1264, 30th 1623, 31st 1134, 32nd 1776, 33rd 1074,
34th 1258, 35th 1296, 36th 1273, 37th 1400, 38th 1714, 39th 1400,
40th 1783, 41st 1584, 42nd 1641, 43rd 1723, 44th 1481, 45th 1264.
Sum = 26,106 which EXCEEDS the 26,039 gate by 67: the failed footing
proves one or more OCR digit garbles in this table (per project lore,
cf. 1899-12-29). The party-component sum (26,021) is the trustworthy
reconstruction. District table needs a page-image read if per-district
values are ever wanted.

Verdict: NIGHT COUNT = 26,021 (Registrar figure, party breakdown
13,306 R / 7,443 D / 5,066 UL / 206 Soc), SF Call 1903-08-12 p4, stamp
1903-08-12T03:00. FLAG for human page-image read: confirm ":6,CC1" reads
26,021 and "13.30G" reads 13,306.

## 5. 1904-05-03 presidential primary (final 9,384)

Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19040504 (SF Call, 1904-05-04).
Fetches: TOC; page 4 OCR (mirror/cdnc/SFC19040504/page_4.txt). Coverage:
p4 "DELEGATES TO STATE CONVENTION CHOSEN BY DISTRICTS OF CITY..."
(SFC19040504.2.22).

CITYWIDE FIGURE, verbatim (2.22, p4, second paragraph of the SF story):
"The total number of votes cast was 9370, of which the Republicans
Rolled [polled] 6705 and the Democrats 2647. There were 11 votes for the
Prohibition ticket and 7 scattering."
FOOTING: 6,705 + 2,647 + 11 + 7 = 9,370 EXACT. Gate: 9,370 < 9,384 PASS
(14 short of final).
The article lead states the same total with one garbled component: "The
total vote cast was 9370, of which 8705 were Republican and 2647
Democratic" (8705 is a misprint/garble of 6705; the exact-footing
version wins).
Supporting counted-contest detail (same section): 39th District
Republican tickets: Countryman 527, Bradford 212, Turner 160; 36th
District Democratic contest 114 vs 109.

Verdict: NIGHT COUNT = 9,370 (6,705 R / 2,647 D / 11 Proh / 7 scat),
SF Call 1904-05-04 p4, stamp 1904-05-04T03:00. Footing exact; high
confidence.

## 6. 1904-08-09 state primary (final 18,141)

Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19040810 (SF Call, 1904-08-10).
Fetches: TOC; page 4 OCR (mirror/cdnc/SFC19040810/page_4.txt). Coverage:
p4 "REGULAR REPUBLICAN AND DEMOCRATIC ORGANIZATIONS WIN SIGNAL VICTORIES
AT PRIMARIES..." (SFC19040810.2.48 tree), incl. "TABLE SHOWING VOTE CAST
BY REPUBLICANS THROUGHOUT THE CITY" (2.48.1.3), "STRENGTH OF OPPOSING
DEMOCRATIC FORCES AS SHOWN BY THE RETURNS" (2.48.3.2), "BALLOT CLERK'S
ERROR TIES UP THE RETURNS IN THE FORTY-FOURTH" (2.48.3.1).

CITYWIDE FIGURE, verbatim OCR (under section header SFC19040810.2.48.2,
p4): "THE aggregate vote cast at. the primary election in San Francisco
yesterday was 17,914, of which the Republicans polled 9010, the
Democrats 7238, the Union. Laborites. 1435, the. Socialists 83JCJ and
the Prohibitionists 18."
FOOTING: 9,010 + 7,238 + 1,435 + 18 = 17,701; total 17,914 implies the
garbled Socialist figure "83JCJ" = 213 (needs page-image confirmation;
plausible for the era). Gate: 17,914 < 18,141 PASS (227 short).

NIGHT-COUNT STATUS, verbatim (Democratic story, p4): "According to the
semi-official returns revised at a late hour with the returns in
Precinct 109, Ferty-fourth [Forty-fourth] District lacking..." and
"The vote will be officially counted before that body [Election
Commissioners] this afternoon" (Precinct 109's tally sheet was muddled
by the tally clerk; boxes sealed and counted E+1 afternoon). So the
17,914 is an overnight semi-official count short one precinct.

Also present: Republican vote by district (2.48.1.3 area) and Democratic
per-district Organization/League table ("Totals — Organization. 370?;
league. 3536."), both OCR-noisy; not needed given the citywide figure.

Verdict: NIGHT COUNT (semi-official, one precinct lacking) = 17,914,
SF Call 1904-08-10 p4, stamp 1904-08-10T03:00. FLAG for human page-image
read: Socialist component garbled ("83JCJ", inferred 213).

## 7. 1905-08-08 municipal primary (final 28,951) -- GATE CONFLICT

Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19050809 (SF Call, 1905-08-09).
Fetches: TOC; page 2 OCR (mirror/cdnc/SFC19050809/page_2.txt). Coverage:
p1 lead SFC19050809.2.2; p2 sections 2.8.1-2.8.5, esp. 2.8.3 "OFFICIAL
FIGURES ARE INCOMPLETE" (per-district tables, districts 28-45, seven
factions each, with "Total vote" per district) and the "SUMMARY OF THE
VOTE" box, plus 2.8.5 "REPUBLICAN VOTE REMARKABLY LARGE".

Citywide summary, verbatim OCR (2.8.3, p2): "SUMMARY OF THE VQT^. /
REPUBLICAN, LEAGUE 16,071 / RUEF REPUBLICAN 1?,429 / DEMOCRATIC 2.575 /
REORGANIZED DEMOCRACY. 654 / UNION LABOR 2,955 / UNION LABOR
(ANTJ-RUEF). 170 / SOCIALISTS 266 / TOTAL 38,120".
FOOTING: 16,071 + 15,429 + 2,575 + 654 + 2,955 + 170 + 266 = 38,120
EXACT (fixes the garbled Ruef figure at 15,429).

GATE CHECK FAILS: 38,120 > 28,951 official final, by 9,169 (31.7%).
The footing is exact, so this is NOT an OCR-digit problem: it is a
definition conflict between the Call's night compilation and the
official final on file. Corroborating internal consistency: 2.8.5 says
"the vote approximated 41,000, of which 31,000 [were] accredited to the
Republican column" and the table's Republican factions sum to 31,500.

Count-status quote, verbatim OCR (2.8.5, p2): "OwinK to confusion or
inellleleney in the Regl*trar's oi!lve I'io totnl number of vnteii cant
at yesterday> i election nun not footed up at 2 o'clock thiM morning."
(= "Owing to confusion or inefficiency in the Registrar's office the
total number of votes cast at yesterday's election was not footed up at
2 o'clock this morning.") So the Registrar had NO official total by
2 a.m.; the 38,120 is the Call's own compilation of returns, printed
under the headline "OFFICIAL FIGURES ARE INCOMPLETE".

Possible resolutions (for operator): (a) the official 28,951 on file
covers a subset (one party? one convention?) of the 1905 primary;
(b) the Call's compilation double-counts (state+municipal delegate
ballots); (c) the official-final value in the dataset is itself wrong
(it was recovered from the FY1915-16 Municipal Reports index per the
search log). NOT adjudicable from this issue alone.

Verdict: NIGHT TABULATION FOUND (Call compilation 38,120, exact footing,
districts 28-45 itemized) but GATE-FAIL vs final 28,951: recorded as a
CONFLICT, no claimable night figure until the final is re-verified.
FLAG for manual operator.

## 8. 1906-08-14 state primary (final 10,824)

Issue URL: https://cdnc.ucr.edu/?a=d&d=SFC19060815 (SF Call, 1906-08-15).
Fetches: TOC; sections SFC19060815.2.9 (p1 "LOCAL PRIMARIES UNCOVER NEST
OF FRAUD."), 2.10 (p2 "Herrin Controls Solid Delegation From the City"),
2.17 (p3 "City's Primary Vote by Districts") via `node cdnc_fetch.js
SFC19060815 <oid>`; saved under mirror/cdnc/SFC19060815/.

CITYWIDE FIGURE, verbatim (2.9, p1, closing paragraph): "The total
registration for the primary election was 22,026, and the total vote
polled 10,554, with the Thirtyfourth Precinct of the Thirty-seventh to
be heard from."
Gate: 10,554 < 10,824 PASS (270 short; explicitly one precinct
outstanding, i.e. a returns aggregate, not a poll list; "to be heard
from" = precinct returns still missing from the tabulation).
Wording caveat: "vote polled" is the phrase; but the figure is an
aggregate of counted precinct returns (one precinct missing) printed
with district-by-district counted results, so treated as a night count.

Per-district table exists (2.17, p3, columns Ruef / Anti-Ruef / McNab
Dem / Opp. Dem / Socialist / Union Labor) but the OCR of the numeric
columns is unusably garbled; needs a page-image read if district values
are ever wanted.

Verdict: NIGHT COUNT (one precinct short) = 10,554, SF Call 1906-08-15
p1, stamp 1906-08-15T03:00.

### UPDATE (page-image arbitration, election 2, 1901-08-13)
Tile-level page-image capture of the sentence block (screenshot:
imgs/cdnc_19010814_p1_2-2-1_b15.png, block 15 of section
SFC19010814.2.2.1, tiles fetched at native resolution from the CDNC
imageserver via the cleared-tab fetch recipe) reads, clearly printed:
"The total vote cast in the 106 precincts yesterday was 22,898. Of this
number the Republicans cast 19,021, the Democrats 3633 and the
Socialists 244."
So the printed total IS 22,898 and the earlier OCR "22,838" was the
garble; footing exact (19,021 + 3,633 + 244 = 22,898). Gate: 22,898 <
22,939 PASS (41 short of final).
REVISED VERDICT (election 2): NIGHT COUNT = 22,898, SF Call 1901-08-14
p1, stamp 1901-08-14T03:00. Page-image verified; no remaining flag.

### UPDATE (page-image arbitration, election 4, 1903-08-11)
Screenshot imgs/cdnc_19030812_p4_2-37-1_b4.png (block 4 of section
SFC19030812.2.37.1, native-res tiles) reads clearly: "The total vote at
the primary as forecasted by The Call exceeded 25,000. The official
figures at the Registrar's office place the number at 26,021." and
"Yesterday the Republicans cast 13,306 votes, the Democrats 7443, the
Union Laborites 5066 and the Socialists 206."
All reconstructions confirmed: total 26,021 (= exact party sum), Call
forecast 25,000, Republicans 13,306. Gate 26,021 < 26,039 PASS.
REVISED VERDICT (election 4): NIGHT COUNT = 26,021, page-image verified;
no remaining flag (district table 26,106 footing failure stands as an
OCR artifact; not needed).

### UPDATE (page-image verification, election 5, 1904-05-03)
Screenshot imgs/cdnc_19040504_p4_2-22_b2.png (block 2 of
SFC19040504.2.22) reads clearly: "The total vote cast was 9370, of
which 6705 were Republican and 2647 Democratic." The article lead
itself prints 6705 (the earlier OCR "8705" was the garble; no
discrepancy on the page). Election 5 verdict stands, page-image
verified: NIGHT COUNT = 9,370.

### UPDATE (page-image arbitration, election 6, 1904-08-09): PRINTED FOOTING ERROR
Screenshots imgs/cdnc_19040810_p4_2-48-2_b2.png (+ zooms
tmp_1904aug_line1.png, tmp_1904aug_socialists.png) read, clearly
printed: "THE aggregate vote cast at the primary election in San
Francisco yesterday was 17,914, of which the Republicans polled 9010,
the Democrats 7238, the Union Laborites 1435, the Socialists 831, and
the Prohibitionists 18."
The Socialist figure is 831 as PRINTED (my earlier 213 inference was
wrong). But the printed components foot to 9,010+7,238+1,435+831+18 =
18,532, which contradicts the printed total 17,914 by 618 AND exceeds
the official final 18,141 by 391 (gate-fail). So the Call's component
line contains a typesetting error (unknowable which figure); the
aggregate 17,914 remains internally credible and passes the gate
(227 short of final, consistent with the one uncounted precinct).
This is a caught 19th-century footing error, same class as the two
prior catches in this project.
REVISED VERDICT (election 6): NIGHT COUNT = 17,914 (semi-official, one
precinct lacking); component breakdown NOT usable (printed footing
error, documented). Page-image verified.

### UPDATE (page-image verification, elections 7 and 8)
1905: screenshots imgs/cdnc_19050809_p2_2-8-3_b6.png and _b7.png show the
full "SUMMARY OF THE VOTE" box as printed: REPUBLICAN LEAGUE 16,071 /
RUEF REPUBLICAN 15,429 / DEMOCRATIC 2,575 / REORGANIZED DEMOCRACY 654 /
UNION LABOR 2,955 / UNION LABOR (ANTI-RUEF) 170 / SOCIALISTS 266 /
TOTAL 38,120. Footing exact as printed; the gate conflict vs official
final 28,951 is REAL, not an OCR artifact. Registrar quote verified in
imgs/cdnc_19050809_p2_2-8-5_b2.png: "Owing to confusion or inefficiency
in the Registrar's office the total number of votes cast at yesterday's
election was not footed up at 2 o'clock this morning. It was figured at
the Republican League headquarters last night that the vote approximated
41,000, of which 31,000 was accredited to the Republican column. The
magnitude of the vote breaks all previous records. At the first primary
election under the Stratton law in 1898 the number of votes polled was
nearly 32,000." Note for the operator: the Call asserts 1905 broke all
records (~38-41k), which is irreconcilable with a 28,951 final unless
that final covers a subset; also note it dates the first Stratton-law
primary (~32,000 votes) to 1898, not 1899.

1906: screenshot imgs/tmp_1906_b1_bottom.png (bottom of
cdnc_19060815_p2_2-9_b1.png; the story starts p1, this block is its p2
continuation) reads clearly: "The total registration for the primary
election was 22,026, and the total vote polled 10,554, with the
Thirty-fourth Precinct of the Thirty-seventh to be heard from."
Election 8 verdict stands, page-image verified: NIGHT COUNT = 10,554
(cite SF Call 1906-08-15 pp1-2). District table captured at
imgs/cdnc_19060815_p3_2-17_b2.png for future per-district reads.

### UPDATE (page-image arbitration, election 1, 1899-08-08)
The district roundup physically lives under headers "RETURNS BY
DISTRICTS. / Number of Votes Cast-The Successful Tickets." (blocks of
sections SFC18990809.2.153.1 and 2.154 on page 12; screenshots
imgs/tmp_1899_28to30.png, imgs/cdnc_18990809_p12_roundup.png with
splits tmp_1899_ru1/ru2/ru3.png). Every district figure read from the
page image:
28th 1350, 29th 1590, 30th 1561, 31st 1773, 32nd 1345, 33rd 1896
(OCR had 1890: CORRECTED), 34th 2152, 35th 1723, 36th 2335, 37th 2600,
38th 2055, 39th 1911 (OCR had 1311: CORRECTED), 40th no total printed
(confirmed on image), 41st 2183, 42nd 1466, 43rd 1843, 44th 1826,
45th 870.
CORRECTED SUM (17 of 18 districts) = 30,479. Gate: 30,479 < 32,521 PASS
(residual 2,042 for the 40th, plausible vs neighbors). Tail text
verified: 2 a.m. revised 29th-district returns (Buckley 520, Committee
of One Hundred 505); Central Republicans 217 of 306 delegates.
REVISED VERDICT (election 1): NIGHT PARTIAL (contest-sum floor) =
30,479 in 17 of 18 Assembly districts, SF Call 1899-08-09 p12, stamp
1899-08-09T03:00. Page-image verified.

---

## FINAL VERDICT TABLE

| election | final (gate) | night figure | kind | citation |
|---|---|---|---|---|
| 1899-08-08 muni primary | 32,521 | 30,479 | partial floor, 17/18 districts (40th missing), page-image verified | SF Call 1899-08-09 p12, "RETURNS BY DISTRICTS." (SFC18990809.2.153.1/2.154) |
| 1901-08-13 muni primary | 22,939 | 22,898 | citywide night count, exact footing (19,021 R + 3,633 D + 244 Soc), page-image verified | SF Call 1901-08-14 p1 (SFC19010814.2.2.1) |
| 1902-08-12 state primary | 28,697 | none | DEAD END: winners-only lists, "An official count may be necessary" | SF Call 1902-08-13 p4 (SFC19020813.2.16.x) |
| 1903-08-11 muni primary | 26,039 | 26,021 | citywide night count (Registrar figure; = exact party sum 13,306+7,443+5,066+206), page-image verified | SF Call 1903-08-12 p4 (SFC19030812.2.37.1) |
| 1904-05-03 pres primary | 9,384 | 9,370 | citywide night count, exact footing (6,705 R + 2,647 D + 11 P + 7 sc), page-image verified | SF Call 1904-05-04 p4 (SFC19040504.2.22) |
| 1904-08-09 state primary | 18,141 | 17,914 | citywide semi-official night count, 1 precinct lacking; printed party components carry a 618-vote footing error (documented) | SF Call 1904-08-10 p4 (SFC19040810.2.48.2) |
| 1905-08-08 muni primary | 28,951 | CONFLICT | Call compiled 38,120 (exact footing, verified) > official final 28,951; Registrar had not footed total at 2 a.m.; FLAG for operator | SF Call 1905-08-09 p2 (SFC19050809.2.8.3/2.8.5) |
| 1906-08-14 state primary | 10,824 | 10,554 | citywide night count, 1 precinct "to be heard from", page-image verified | SF Call 1906-08-15 pp1-2 (SFC19060815.2.9) |

Stamp convention for all found figures: E+1 T03:00 (day-after morning
edition; 1899 and 1905 carry explicit 2 a.m. references, 1901 tables
near-complete overnight).
