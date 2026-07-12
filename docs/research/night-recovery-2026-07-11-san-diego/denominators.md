# San Diego County certified-denominator table (1884-1920)

Mission: for each even-year November general election listed below, find San Diego
County's certified per-candidate vote in the top statewide single-seat contest
(President in presidential years; Governor in 1898/1902/1906/1910/1918) from a
primary/near-primary digitized source (CA Secretary of State "Statement of the
Vote" volumes or the CA Blue Book election-returns appendix, both on archive.org),
plus the county "total votes cast" if the volume prints one. Elections in scope:
1884, 1888, 1892, 1896, 1898, 1900, 1902, 1904, 1906, 1908, 1910, 1912, 1916,
1918, 1920 (1914 and 1922 skipped per instructions).

Method: archive.org full-text "search inside" via
`https://ia*.us.archive.org/fulltext/inside.php?item_id=<id>&doc=<id>&q=<phrase>`,
plain-text dumps at `https://archive.org/stream/<id>/<id>_djvu.txt` fetched with
curl, and archive.org page images at `https://archive.org/details/<id>/page/<leaf>`.
Wikipedia's "results by county" tables (raw wikitext) are used only as a
cross-check / navigation aid, never as the recorded source of truth; the
recorded source is always the archive.org SOV/Blue Book scan.

One section per election below, appended as each is completed.

---
## 1892-11-08 — President (Presidential Electors)

Source (primary): "Statement of the Vote of the State of California at the General Election
Held November 8, A.D. 1892" (E. G. Waite, Secretary of State), bound in archive.org item
`statementofvoteo1886cali` (SFPL compilation volume of SoS Statements of Vote).

San Diego County, per ticket (SOV prints one column per elector; figure = the ticket's
elector column value for San Diego; where elector columns differ by 1-2 votes the
highest-elector value is given with the first-column read noted):

| Ticket (candidate) | San Diego votes |
|---|---|
| Republican (Harrison) | 3,525 |
| Democratic (Cleveland) | 2,334 (first elector column reads 2,333) |
| People's Party (Weaver) | 1,519 (elector columns range 1,513-1,519) |
| Prohibition (Bidwell) | 334 |
| **Contest sum** | **7,712** |

Total votes cast for the county: not printed in this SOV (no per-county ballots-cast
column found in the OCR text; the volume prints only per-elector columns and
proposition votes).

Provenance:
- archive.org item: `statementofvoteo1886cali` (server ia600703, path /6/items/statementofvoteo1886cali)
- Republican table: API page 99 = https://archive.org/details/statementofvoteo1886cali/page/n98
  (locating query: fulltext inside.php q=`118,027` -> page 99; statewide Rep elector-1 total
  "ffitals 118,027" in OCR; San Diego Rep read `3,525` also matches on page 99)
- Democratic table: API page 100 = https://archive.org/details/statementofvoteo1886cali/page/n99
  (q=`118,151` -> page 100; SD col1 `2,333`, col2 `2,334`)
- Prohibition table: API page 101 = https://archive.org/details/statementofvoteo1886cali/page/n100
  (q=`8,096` -> page 101; SD `334` between San Bernardino 614 and San Francisco 489
  reading up the county order from Yuba 42 at the column foot)
- People's Party table: API page 102 = https://archive.org/details/statementofvoteo1886cali/page/n101
  (q=`25,311` -> page 102; OCR snippet verbatim: "San Bernardino 721 San Diego . 1,519 San Francisco . 2,508")
- djvu.txt: https://archive.org/stream/statementofvoteo1886cali/statementofvoteo1886cali_djvu.txt
  lines ~24277-28230 (grep anchors: "STATEMENT  OF  VOTE  POLLED  FOR  1892", "ffitals 118,027")
- Cross-check: Wikipedia "1892 United States presidential election in California" county table
  (raw wikitext) San Diego row = 3,525 / 2,334 / 1,519 / 334, sum 7,712 — exact match; that
  page's ref cites this same archive.org item at /page/n97.

Confidence: high (all four figures machine-read from SOV OCR and independently matched by
Wikipedia's SOV-cited table).

---
## 1896-11-03 — President (Presidential Electors)

Source (primary): "Statement of the Vote of California at the General Election, Held
November 3, 1896" (L. H. Brown, Secretary of State), bound in archive.org item
`statementofvoteo1886cali`. All seven ticket tables were read from PAGE IMAGES (not OCR),
printed pages 3-9.

San Diego County per ticket. The SOV prints one column per elector; the per-ticket figure
below is the HIGHEST elector column for San Diego (full ranges given). Bryan ran on two
slates (Democrat = Bryan/Sewall and People's Party = Bryan/Watson) with the same nine
elector names; a voter chose one slate, so the slates are summed separately here.

| Ticket (candidate) | San Diego votes | elector range |
|---|---|---|
| Republican (McKinley) | 3,631 | 3,599-3,631 |
| Democrat (Bryan-Sewall) | 2,368 | 2,332-2,368 |
| People's Party (Bryan-Watson) | 1,548 | 1,516-1,548 |
| Prohibition (Levering) | 97 | 94-97 |
| National Democratic (Palmer) | 23 (modal; one elector, O'Brien, drew 35) | 23-35 |
| National Party (Bidwell) | 19 | 17-19 |
| Socialist Labor (Matchett) | 76 (Biddle; Liess drew 71) | 71-76 |
| **Contest sum (highest-elector convention)** | **7,762** | |

Notes on the sum: 3,631+2,368+1,548+97+23+19+76 = 7,762. Wikipedia's SOV-derived table
(which takes elector J. W. Martin's combined Dem+PP vote 2,368+1,540=3,908 for Bryan and
uses 96/23/71/19 for the minors) sums to 7,748. The spread (±15) is inherent to
per-elector ballots; there is no single-number "candidate vote" printed.

Total votes cast for the county: not printed in this SOV.

Provenance (archive.org item `statementofvoteo1886cali`, server ia600703,
path /6/items/statementofvoteo1886cali; page images fetched from
https://archive.org/download/statementofvoteo1886cali/page/n<leaf> and read visually):
- Republican, printed p.3, API page 111 = https://archive.org/details/statementofvoteo1886cali/page/n110
  (locating query: inside.php q=`146,133` -> page 111; San Diego row: 3,612 3,631 3,616 3,614 3,623 3,611 3,613 3,605 3,599)
- People's Party, printed p.4, API page 112 = .../page/n111 (q=`21,734` -> page 112;
  San Diego row: 1,546 1,537 1,540 1,542 1,547 1,548 1,547 1,534 1,516; footnote "* Where grouped by County Clerk" — San Diego NOT starred)
- Democrat, printed p.5, API page 113 = .../page/n112 (q=`123,143` -> page 113;
  San Diego row: 2,368 2,354 2,348 2,349 2,356 2,350 2,346 2,347 2,332; the page's
  "Bro'ght forw'd" row adds the PP totals, confirming the fusion arithmetic)
- Prohibition, printed p.6, API page 114 = .../page/n113 (San Diego row: 96 96 95 94 95 95 95 96 97)
- National Democratic, printed p.7, API page 115 = .../page/n114 (q=`1,730` -> page 115;
  San Diego row: 23 23 35 26 24 25 23 23 23)
- National Party, printed p.8, API page 116 = .../page/n115 (q=`1,047` -> page 116;
  San Diego row: 19 19 18 18 19 18 17 18 17)
- Socialist Labor + Scattering, printed p.9, API page 117 = .../page/n116 (q=`1,611` -> page 117;
  San Diego: Liess 71, Biddle 76; scattering columns blank for San Diego)
- Cross-check: Wikipedia "1896 United States presidential election in California" San Diego row
  3,631 / 3,908 / 96 / 23 / 71 / 19 (sum 7,748) — consistent (its ref cites this item at /page/n109).

Confidence: high (all figures read from page images; statewide elector totals match known
history: McKinley 146,688 top elector, Bryan 144,766 top fusion elector).

---
## 1900-11-06 — President (Presidential Electors)

Source (near-primary): California Blue Book, or State Roster, 1903 (Secretary of State
compilation; reprints the SoS canvass), "VOTE OF CALIFORNIA FOR ELECTORS OF PRESIDENT AND
VICE-PRESIDENT OF THE UNITED STATES. General Election—November 6, 1900", printed pp.
311-314. archive.org item `california-blue-book-1903-sfg`. All four ticket tables read
from PAGE IMAGES.

San Diego County per ticket (highest elector column; ranges given):

| Ticket (candidate) | San Diego votes | elector range |
|---|---|---|
| Republican (McKinley) | 3,800 | 3,729-3,800 |
| Democratic (Bryan) | 2,678 | 2,633-2,678 |
| Social Democratic (Debs) | 294 | 287-294 |
| Prohibition (Woolley) | 157 | 151-157 |
| Scattering | 2 | (single column) |
| **Contest sum (highest-elector convention)** | **6,931** | |

Wikipedia's table uses 3,800 / 2,678 / 289 / 152 / 2 = 6,921 (different elector choice for
the two minor tickets). The Blue Book prints no other tickets; Socialist Labor etc. are in
"Scattering" (statewide 605).

Total votes cast for the county: not printed with this table.

Provenance (archive.org item `california-blue-book-1903-sfg`, server ia800104,
path /32/items/california-blue-book-1903-sfg; images from
https://archive.org/download/california-blue-book-1903-sfg/page/n<leaf>):
- Republican ticket, printed p.311, leaf n341 = https://archive.org/details/california-blue-book-1903-sfg/page/n341
  (locating query: inside.php doc=`California_Blue_Book_1903 (SFG)` q=`164,755` -> page 341;
  San Diego row: 3,800 3,773 3,772 3,777 3,774 3,764 3,767 3,766 3,729; totals row 164,755 ... 161,917)
- Democratic ticket, printed p.312, leaf n342 (San Diego row: 2,678 2,666 2,663 2,662 2,660 2,660 2,663 2,659 2,633; totals 124,985 ... 123,634)
- Social Democratic ticket, printed p.313, leaf n343 (San Diego row: 289 289 289 290 294 292 292 289 287; totals 7,554 ... 7,442)
- Prohibition ticket + Scattering, printed p.314, leaf n344 (San Diego row: 157 154 153 152 154 154 152 151 153, scattering 2; totals 5,024 ... 4,953, scattering 605)
- djvu.txt: https://archive.org/stream/california-blue-book-1903-sfg/California_Blue_Book_1903%20(SFG)_djvu.txt
  (grep anchor: "General Election—November 6, 1900", "San Піеро-.... 3,800")
- Cross-check: Wikipedia "1900 United States presidential election in California" San Diego row
  3,800 / 2,678 / 289 / 152 / 2 — consistent.

Confidence: high (page-image reads; statewide top-elector totals match known history:
McKinley 164,755, Bryan 124,985, Debs 7,554, Woolley 5,024).

---
## 1902-11-04 — Governor

Source (near-primary): California Blue Book, or State Roster, 1903, "VOTE FOR GOVERNOR AND
LIEUTENANT-GOVERNOR. General Election—November 4, 1902", printed p.332. archive.org item
`california-blue-book-1903-sfg`. Read from the PAGE IMAGE (single column per candidate;
no elector ambiguity).

San Diego County:

| Candidate | San Diego votes |
|---|---|
| George C. Pardee (Republican) | 3,182 |
| Franklin K. Lane (Democrat) | 2,517 |
| Gideon S. Brower (Socialist) | 657 |
| Theo. D. Kanouse (Prohibition) | 97 |
| Scattering | 6 |
| **Contest sum** | **6,459** |

Total votes cast for the county: not printed with this table.

Provenance:
- archive.org item `california-blue-book-1903-sfg`, printed p.332, leaf n362 =
  https://archive.org/details/california-blue-book-1903-sfg/page/n362
  (image: https://archive.org/download/california-blue-book-1903-sfg/page/n362)
- Locating query: djvu.txt grep "VOTE FOR GOVERNOR AND LIEUTENANT-GOVERNOR" +
  "General Election—November 4, 1902" (OCR line ~29138); leaf found by the printed-page/leaf
  offset (+30) established at p.311=n341 and confirmed by the page header "332".
- Verbatim row from image: "San Diego .......... 3,182 | 2,517 | 657 | 97 | 6 || 3,257 | 2,250 | 732 | 97 | 4"
  (second half is the Lieutenant-Governor table).
- Statewide totals row: 146,332 / 143,783 / 9,592 / 4,636 / 130 — matches the historical
  1902 result (Pardee 146,332, Lane 143,783).
- Cross-check: Wikipedia's 1902 CA gubernatorial page has no county table (page fetch
  errored); the statewide match serves as the cross-check.

Confidence: high (page-image read; statewide totals verified).

---
## 1904-11-08 — President (Presidential Electors)

Source (near-primary): California Blue Book, or State Roster, 1907, "VOTE OF CALIFORNIA FOR
PRESIDENTIAL ELECTORS. General Election—November 8, 1904", printed pp.419-422. archive.org
item `californiabluebo0000vari`. All four ticket tables read from PAGE IMAGES.

San Diego County per ticket (highest elector column; canonical first-elector value noted):

| Ticket (candidate) | San Diego votes (highest elector) | elector range | first elector |
|---|---|---|---|
| Republican (Roosevelt) | 4,310 | 4,284-4,310 | 4,303 (Wood; statewide 205,226) |
| Democratic (Parker) | 1,398 | 1,387-1,398 | 1,396 (Garber; statewide 89,294) |
| Socialist (Debs) | 1,380 | 1,370-1,380 | 1,377 (Lawrence; statewide 29,535) |
| Prohibition (Swallow) | 153 | 148-153 | 152 (Clark; statewide 7,380) |
| Scattering | not printed per county (statewide footnote list, total 333) | | |
| **Contest sum (highest-elector)** | **7,241** | | |

Wikipedia's table (4,303 / 1,398 / 1,377 / 152 / 1) sums to 7,231.

Total votes cast for the county: not printed with these tables.

Provenance (archive.org item `californiabluebo0000vari`, server ia802800,
path /4/items/californiabluebo0000vari; images from
https://archive.org/download/californiabluebo0000vari/page/n<leaf>):
- Republican ticket, printed p.419, leaf n454 = https://archive.org/details/californiabluebo0000vari/page/n454
  (locating query: inside.php q=`205,226` -> pages 446/455; leaf confirmed by header;
  San Diego row: 4,303 4,310 4,290 4,298 4,290 4,291 4,290 4,293 4,293 4,284)
- Democratic ticket, printed p.420, leaf n455 (q=`89,294` -> page 456;
  San Diego row: 1,396 1,388 1,395 1,391 1,398 1,393 1,394 1,387 1,388 1,394)
- Socialist ticket, printed p.421, leaf n456 (q=`29,535` -> page 457;
  San Diego row: 1,377 1,379 1,375 1,380 1,375 1,379 1,374 1,375 1,378 1,370)
- Prohibition ticket + scattering footnote, printed p.422, leaf n457
  (San Diego row: 152 153 151 151 150 150 150 150 152 148; "SCATTERING (Total, 333)" is a
  statewide name list, no county breakdown)
- Cross-check: Wikipedia "1904 United States presidential election in California" San Diego row
  4,303 / 1,398 / 1,377 / 152 / 1 — consistent.

Confidence: high (page-image reads; statewide first-elector totals match known history).

---
## 1906-11-06 — Governor

Source (near-primary): California Blue Book, or State Roster, 1907, "VOTE FOR GOVERNOR.
General Election—November 6, 1906", printed p.437. archive.org item
`californiabluebo0000vari`. Read from the PAGE IMAGE (single column per candidate).

San Diego County:

| Candidate | San Diego votes |
|---|---|
| James N. Gillett (Republican) | 3,621 |
| Theodore A. Bell (Democrat) | 2,469 |
| Austin Lewis (Socialist) | 974 |
| Jas. H. Blanchard (Prohibition) | 174 |
| W. H. Langdon (Independence League) | 504 |
| Theodore A. Bell (Union Labor line) | 55 |
| Scattering | 3 |
| **Contest sum** | **7,800** |

The table carries the footnote "* Union Labor vote for Theodore A. Bell in San Diego
County." — the Union Labor column is populated ONLY for San Diego (55 votes), and the
note explains other counties folded Union Labor endorsements into the major-party
columns. Bell's certified total 117,645 = 117,590 + this 55.

Total votes cast for the county: not printed with this table.

Provenance:
- archive.org item `californiabluebo0000vari`, printed p.437, leaf n472 =
  https://archive.org/details/californiabluebo0000vari/page/n472
  (image: https://archive.org/download/californiabluebo0000vari/page/n472)
- Locating query: inside.php q=`125,887` -> page 473 (totals row
  "125,887 | 117,645 | 16,036 | 7,355 | 45,008 | 55 | 44").
- Verbatim San Diego row from image: "San Diego 3,621 | 2,469 | 974 | 174 | 504 | 55 | 3".
- Statewide totals match history (Gillett 125,887, Bell 117,645, Langdon 45,008).
- Cross-check: Wikipedia 1906 CA gubernatorial page fetch errored; statewide totals serve
  as the cross-check.

Confidence: high (page-image read; statewide totals verified; SD-specific footnote noted).

---
## 1908-11-03 — President (Presidential Electors)

Source (primary): "Statement of the Vote of California at the General Election, Held
November 3, 1908" (C. F. Curry, Secretary of State), archive.org item
`statementofvo19081922cali` (bound SoS volume, 1908-1922). All five ticket tables read
from PAGE IMAGES, printed pp.3-7.

San Diego County per ticket (highest elector; first-elector value noted):

| Ticket (candidate) | San Diego votes (highest elector) | elector range | first elector |
|---|---|---|---|
| Republican (Taft) | 5,412 | 5,368-5,412 | 5,412 (Grant; statewide 214,398) |
| Democratic (Bryan) | 2,393 | 2,377-2,393 | 2,393 (Phelan; statewide 127,492) |
| Socialist (Debs) | 1,346 | 1,339-1,346 | 1,342 (Garbutt; statewide 28,659) |
| Prohibition (Chafin) | 212 | 211-212 | 212 (Head; statewide 11,770) |
| Independence League (Hisgen) | 46 | 44-46 | 44 (Murphy; statewide 4,278) |
| **Contest sum (highest-elector)** | **9,409** | | |

Wikipedia's table (5,412 / 2,393 / 1,342 / 212 / 44) sums to 9,403.
Statewide check: 214,398+127,492+28,659+11,770+4,278 = 386,597 ≈ the known ~386K 1908 CA total.

Total votes cast for the county: not printed with these tables.

Provenance (archive.org item `statementofvo19081922cali`, server ia801401,
path /25/items/statementofvo19081922cali; images from
https://archive.org/download/statementofvo19081922cali/page/n<leaf>):
- Republican, printed p.3, leaf n6 = https://archive.org/details/statementofvo19081922cali/page/n6
  (locating query: inside.php q=`214,398` -> API page 11; San Diego row:
  5,412 5,387 5,395 5,393 5,394 5,380 5,387 5,387 5,383 5,368)
- Democratic, printed p.4, leaf n7 (q=`127,492` -> page 12; San Diego row:
  2,393 2,382 2,384 2,380 2,379 2,377 2,384 2,381 2,378 2,379)
- Independence League, printed p.5, leaf n8 (San Diego row: 44 45 45 45 45 45 46 44 44 45)
- Socialist, printed p.6, leaf n9 (q=`28,659` -> page 14; San Diego row:
  1,342 1,339 1,343 1,345 1,346 1,346 1,344 1,345 1,341 1,339)
- Prohibition, printed p.7, leaf n10 (San Diego row: 212 212 211 211 211 211 211 211 211 212;
  scattering is a statewide footnote list only)
- Cross-check: Wikipedia "1908 United States presidential election in California" San Diego row
  5,412 / 2,393 / 1,342 / 212 / 44 — consistent.

Confidence: high (page-image reads; statewide totals match known history).

---
## 1910-11-08 — Governor

Source (primary): "Statement of Vote: November 8, 1910" (SoS statement bound in archive.org
item `statementofvoteo1886cali`), "FOR GOVERNOR" table, printed p.2. Read from the PAGE
IMAGE (single column per candidate).

San Diego County:

| Candidate | San Diego votes |
|---|---|
| Hiram W. Johnson (Republican) | 4,514 |
| Theodore A. Bell (Democrat) | 2,966 |
| J. Stitt Wilson (Socialist) | 1,870 |
| Simeon Pease Meads (Prohibitionist) | 129 |
| Scattering | — (blank for San Diego; statewide 61) |
| **Contest sum** | **9,479** |

Total votes cast for the county: **9,481** (printed). Source: the 1912 SOV table
"OFFICIAL VOTE AT GENERAL ELECTION HELD IN NOVEMBER, 1912" (columns: precincts 1912,
Total vote cast 1910, Registration 1912, Total vote cast 1912), San Diego row
"146 / 9,481 / 30,041 / 22,933"; archive.org item `statementofvo19081922cali`, printed
p.3 of the 1912 statement, leaf n34 =
https://archive.org/details/statementofvo19081922cali/page/n34 (statewide 1910 total
393,893). Cross-check: contest sum 9,479 <= 9,481 total cast (undervote 2).

Provenance:
- archive.org item `statementofvoteo1886cali`, printed p.2 of the 1910 statement,
  API page 220 = https://archive.org/details/statementofvoteo1886cali/page/n219
  (image: https://archive.org/download/statementofvoteo1886cali/page/n219)
- Locating query: inside.php q=`177,191` -> page 220 (also q=`154,835` -> page 220).
- Verbatim San Diego row from image: "San Diego 4,514 | 2,966 | 1,870 | 129 | ......"
- Statewide totals row: 177,191 / 154,835 / 47,819 / 5,807 / 61 — matches the historical
  1910 result (Johnson 177,191, Bell 154,835).
- Note: the bound volume `statementofvo19081922cali` does NOT contain the Nov 1910 general
  (it jumps from the Aug 1910 primary to the 1912 general); this SFPL compilation item is
  the digitized source that does.
- Cross-check: Wikipedia 1910 CA gubernatorial page fetch errored; statewide totals serve
  as the cross-check.

Confidence: high (page-image read; statewide totals verified).

---
## 1912-11-05 — President (Presidential Electors)

Source (primary): "Statement of Vote of California, General Election held November 5, 1912"
(Frank C. Jordan, Secretary of State), bound in archive.org item `statementofvo19081922cali`.
Ticket tables read from PAGE IMAGES (13 electors per slate, each slate spanning two pages).

San Diego County per slate (highest elector; ranges given). NOTE on labels: the Roosevelt
electors ran under the "REPUBLICAN ... PARTY—Progressive" heading (they captured the CA
Republican line); the Taft electors appear in a separate small "REPUBLICAN" table at
printed p.12.

| Slate (candidate) | San Diego votes (highest elector) | first-elector value |
|---|---|---|
| Republican/Progressive (Roosevelt) | 7,922 | 7,922 (Wallace; statewide 283,610) |
| Democratic (Wilson) | 9,731 | 9,731 (Griffin; statewide 283,436) |
| Socialist (Debs) | 2,873 | 2,873 (Boyd; statewide 79,201) |
| Prohibition (Chafin) | 1,139 | 1,139 (Bidwell; statewide 23,366) |
| Republican regular (Taft) | 63 | 63 (Sbarboro; statewide 2,847; other electors up to 3,903) |
| **Contest sum** | **21,728** | |

Total votes cast for the county (PRINTED): **22,933** ("Total vote cast, 1912"), with
registration 30,041 and 146 precincts; same table prints "Total vote cast, 1910" =
**9,481** for San Diego. Contest sum 21,728 <= 22,933 ✓ (undervote ~5%).

Provenance (archive.org item `statementofvo19081922cali`, server ia801401,
path /25/items/statementofvo19081922cali; images from
https://archive.org/download/statementofvo19081922cali/page/n<leaf>):
- County totals table "OFFICIAL VOTE AT GENERAL ELECTION HELD IN NOVEMBER, 1912",
  printed p.3, leaf n34 = https://archive.org/details/statementofvo19081922cali/page/n34
  (San Diego row: 146 / 9,481 / 30,041 / 22,933; statewide totals 4,283 / 393,893 / 987,368 / 707,776)
  Locating query: djvu.txt grep "OFFICIAL VOTE AT GENERAL ELECTION HELD IN NOVEMBER, 1912";
  inside.php q=`Registration, 1912` -> API page 39.
- Republican(Progressive)/Roosevelt electors 1-5, printed p.4, leaf n35
  (San Diego row: 7,922 7,906 7,908 7,903 7,913; locating: q=`283,610` -> API page 40);
  electors 6-13, printed p.5, leaf n36 (San Diego row: 7,908 7,906 7,903 7,904 7,904 7,903 7,903 7,916)
- Democratic/Wilson electors 1-5, printed p.6, leaf n37 (San Diego row: 9,731 9,707 9,707 9,712 9,701;
  q=`283,436` -> API page 42); electors 6-13, printed p.7, leaf n38 (San Diego: 9,708 ... 9,697)
- Socialist/Debs electors 1-5, printed p.8, leaf n39 (San Diego row: 2,873 2,867 2,864 2,864 2,865)
- Prohibition/Chafin electors 1-5, printed p.10, leaf n41 (San Diego row: 1,139 1,135 1,134 1,129 1,129)
- Republican regular/Taft electors 1-5, printed p.12, leaf n43 (San Diego row: 63 61 63 63 63)
- Cross-check: Wikipedia "1912 United States presidential election in California" San Diego row
  7,922 / 9,731 / 2,873 / 1,139 / 63 / 0, sum 21,728 — exact match.

Confidence: high (page-image reads; statewide totals match known history; county total-cast
printed and consistent).

---
## 1916-11-07 — President (Presidential Electors)

Source (primary): "Statement of Vote ... General Election held on November 7, 1916"
(Frank C. Jordan, Secretary of State), bound in archive.org item `statementofvo19081922cali`.
Ticket tables read from PAGE IMAGES (13 electors per slate, two pages per slate),
printed pp.8-15.

San Diego County per slate (highest elector; canonical first-listed elector noted):

| Slate (candidate) | San Diego votes (highest elector) | canonical elector |
|---|---|---|
| Republican (Hughes) | 16,978 | 16,978 (Carlston; statewide 462,516) |
| Democratic (Wilson) | 16,815 | 16,815 (Heney; statewide 466,289) |
| Socialist (Benson) | 1,627 (Ben F. Wilson elector) | 1,612 (Anderson; statewide 42,898) |
| Prohibition (Hanly) | 1,132 | 1,132 (Bidwell; statewide 27,713) |
| Scattering | blank for San Diego | |
| **Contest sum (highest-elector)** | **36,552** | |

Wikipedia's table (16,978 / 16,815 / 1,612 / 1,132) sums to 36,537.

Total votes cast for the county: not printed with these tables (no 1916 per-county
total-vote table found in this volume; the 1912-style totals table was not repeated).

Provenance (archive.org item `statementofvo19081922cali`; images from
https://archive.org/download/statementofvo19081922cali/page/n<leaf>):
- Republican electors 1-5, printed p.8, leaf n177 = https://archive.org/details/statementofvo19081922cali/page/n177
  (locating query: inside.php q=`462,516` -> API page 182; San Diego row: 16,978 16,939 16,956 16,918 16,928)
- Republican electors 6-13 + scattering, printed p.9, leaf n178 (San Diego row: 16,940 16,946 16,916 16,905 16,933 16,919 16,920 16,903; scattering blank)
- Democratic electors 1-5, printed p.10, leaf n179 (q=`466,289` -> API page 184;
  San Diego row: 16,794 16,815 16,760 16,761 16,773)
- Democratic electors 6-13, printed p.11, leaf n180 (San Diego row: 16,743 16,749 16,749 16,743 16,735 16,740 16,731 16,727)
- Socialist electors 1-5, printed p.12, leaf n181 (San Diego row: 1,612 1,607 1,604 1,609 1,610)
- Socialist electors 6-13, printed p.13, leaf n182 (San Diego row: 1,603 1,604 1,604 1,604 1,605 1,627 1,604 1,602)
- Prohibition electors 1-5, printed p.14, leaf n183 (San Diego row: 1,132 1,103 1,109 1,119 1,107)
- Cross-check: Wikipedia "1916 United States presidential election in California" San Diego row
  16,815 / 16,978 / 1,612 / 1,132 — consistent.

Confidence: high (page-image reads; statewide totals match known history: Wilson 466,289,
Hughes 462,516).

---
## 1918-11-05 — Governor

Source (primary): "Statement of Vote ... General Election held on November 5, 1918"
(Frank C. Jordan, Secretary of State), bound in archive.org item `statementofvo19081922cali`,
"FOR GOVERNOR" table, printed p.7. Read from the PAGE IMAGE (single column per candidate).

San Diego County:

| Candidate | San Diego votes |
|---|---|
| William D. Stephens (Republican, Progressive, Prohibition) | 16,333 |
| Henry H. Roser (Socialist) | 1,132 |
| Theodore A. Bell (Independent) | 7,618 |
| James Rolph, Jr. (write-in) | 12 |
| Scattering | 5 |
| **Contest sum** | **25,100** |

Total votes cast for the county: not printed with this table.

Provenance:
- archive.org item `statementofvo19081922cali`, printed p.7 of the 1918 statement,
  leaf n264 = https://archive.org/details/statementofvo19081922cali/page/n264
  (image: https://archive.org/download/statementofvo19081922cali/page/n264)
- Locating query: inside.php q=`251,189` -> API page 269 (totals row
  "387,547 | 29,003 | 251,189 | 20,605 | 326"); leaf found by fetching nearby leaves.
- Verbatim San Diego row from image: "San Diego 16,333 | 1,132 | 7,618 | 12 | 5".
- Statewide totals match the historical 1918 result (Stephens 387,547, Bell 251,189).
- Cross-check: Wikipedia 1918 CA gubernatorial page fetch errored; statewide totals serve
  as the cross-check.

Confidence: high (page-image read; statewide totals verified).

---
## 1920-11-02 — President (Presidential Electors)

Source (primary): "Statement of Vote ... General Election held on November 2, 1920"
(Frank C. Jordan, Secretary of State), bound in archive.org item `statementofvo19081922cali`.
Ticket tables read from PAGE IMAGES (13 electors per slate, two pages per slate),
printed pp.8-15.

San Diego County per slate (highest elector; canonical first-listed elector noted):

| Slate (candidate) | San Diego votes (highest elector) | canonical elector |
|---|---|---|
| Republican (Harding) | 19,834 (Hollingsworth) | 19,826 (Rosseter; statewide 624,992) |
| Democratic (Cox) | 8,481 (Rutledge) | 8,478 (Doheny; statewide 229,191) |
| Socialist (Debs) | 1,812 | 1,812 (Anderson; statewide 64,076) |
| Prohibition (Watkins) | 971 (H. A. Johnson elector; statewide 25,204) | 958 (Stipp; statewide 25,085) |
| Scattering | blank for San Diego | |
| **Contest sum (highest-elector)** | **31,098** | |

IMPORTANT cross-check finding: Wikipedia's county table displays Harding San Diego as
"19,286" but its own row percentages (63.78%) and row total (31,087) are only consistent
with **19,826** — a digit transposition in the Wikipedia display value. The SOV page image
clearly reads 19,826 (elector Rosseter). Trust the SOV.

Total votes cast for the county: not printed with these tables.

Provenance (archive.org item `statementofvo19081922cali`; images from
https://archive.org/download/statementofvo19081922cali/page/n<leaf>):
- Republican electors 1-5, printed p.8, leaf n313 = https://archive.org/details/statementofvo19081922cali/page/n313
  (locating query: inside.php q=`624,992` -> API page 318; San Diego row: 19,826 19,834 19,827 19,815 19,816)
- Republican electors 6-13 + scattering, printed p.9, leaf n314 (San Diego row: 19,783 19,809 19,809 19,803 19,772 19,798 19,790 19,809)
- Democratic electors 1-5, printed p.10, leaf n315 (q=`229,191`; San Diego row: 8,478 8,476 8,481 8,476 8,467)
- Democratic electors 6-13, printed p.11, leaf n316 (San Diego row: 8,466 8,465 8,467 8,467 8,446 8,450 8,476 8,468)
- Prohibition electors 1-5, printed p.12, leaf n317 (San Diego row: 958 961 952 962 950)
- Prohibition electors 6-13 + scattering, printed p.13, leaf n318 (San Diego row: 971 953 959 951 952 951 963 952; scattering blank)
- Socialist electors 1-5, printed p.14, leaf n319 (San Diego row: 1,812 1,807 1,800 1,800 1,800)
- Socialist electors 6-13, printed p.15, leaf n320 (San Diego row: 1,799 1,803 1,797 1,799 1,795 1,799 1,797 1,794)
- There is also a standalone 1920 item `ldpd_11382167_000` (Columbia scan) of the same statement.
- Cross-check: Wikipedia "1920 United States presidential election in California" San Diego row
  8,478 / 1,812 / 971 consistent; Harding value shown there (19,286) is a typo for 19,826 (see above).

Confidence: high (page-image reads; statewide totals match known history: Harding 624,992,
Cox 229,191, Debs 64,076).

---
## 1884-11-04 — President (Presidential Electors)

Source (near-primary): "Governmental Roster, 1889: State and County Governments of
California" (W. C. Hendricks, Secretary of State; Sacramento, State Printing Office, 1889),
table "PRESIDENTIAL ELECTION, 1884. Vote for Highest and Lowest Candidates for Presidential
Electors on each Ticket", printed p.50. Digitized on HathiTrust (full view, public domain,
Google-digitized), item id `uc1.32106019792388`, page scan seq 66. Read from a full-page
SCREENSHOT of the HathiTrust page viewer (HathiTrust blocks curl/WebFetch via Cloudflare;
fetched through the session's isolated debug Chrome with a raw CDP session, the
cdnc_fetch.js technique).

San Diego County (the Roster prints highest and lowest elector per ticket; both identical
for San Diego except Prohibition, whose "lowest" cell is blank):

| Ticket (candidate) | San Diego votes (highest elector) | lowest elector |
|---|---|---|
| Republican (Blaine) | 1,120 | 1,120 |
| Democrat (Cleveland) | 800 | 800 |
| Greenback (Butler) | 5 | 5 |
| Prohibitionist (St. John) | 40 | (blank) |
| **Contest sum** | **1,965** | |

Total votes cast for the county: not printed.

Provenance:
- HathiTrust: https://babel.hathitrust.org/cgi/pt?id=uc1.32106019792388&seq=66 (printed p.50)
- Locating query: Wikipedia "1884 United States presidential election in California" county
  table ref cites exactly this volume/page ("Government Roster, 1889 ... pages 50,
  url=https://babel.hathitrust.org/cgi/pt?id=uc1.32106019792388&seq=66").
- Verbatim row from page image: "San Diego 1,120 | 1,120 | 800 | 800 | 5 | 5 | 40 | ----"
- Statewide totals row: 102,416 / 102,223 | 89,288 / 89,200 | 2,037 / 1,722 | 2,963 / 2,345 —
  matches the historical 1884 CA result (Blaine 102,416, Cleveland 89,288).
- Cross-check: Wikipedia San Diego row 1,120 / 800 / 40 / 5 / 0, total 1,965 — exact match.

Confidence: high (page-image read; statewide totals verified; Wikipedia cross-check exact).

---
## 1888-11-06 — President (Presidential Electors)

Source (near-primary): same volume as 1884 — "Governmental Roster, 1889", table
"PRESIDENTIAL ELECTION, 1888. Vote for Highest and Lowest Candidates for Presidential
Electors on each Ticket", printed p.51. HathiTrust item `uc1.32106019792388`, page scan
seq 67, read from a page-viewer SCREENSHOT (same raw-CDP fetch method).

San Diego County:

| Ticket (candidate) | San Diego votes (highest elector) | lowest elector |
|---|---|---|
| Republican (Harrison) | 4,661 | 4,661 |
| Democrat (Cleveland) | 3,189 | 3,188 |
| American (Curtis) | 11 | 11 |
| Prohibition (Fisk) | 322 | 322 |
| Scattering | 11 | |
| **Contest sum** | **8,194** | |

Total votes cast for the county: not printed.

Provenance:
- HathiTrust: https://babel.hathitrust.org/cgi/pt?id=uc1.32106019792388&seq=67 (printed p.51)
- Locating query: adjacency — the 1884 table (seq 66) is immediately followed by the 1888
  table (seq 67); confirmed by the page header "PRESIDENTIAL ELECTION, 1888."
- Verbatim row from page image: "San Diego 4,661 | 4,661 | 3,189 | 3,188 | 11 | 11 | 322 | 322 | 11"
- Statewide totals row: 124,816 / 124,751 | 117,729 / 117,626 | 1,591 / 696 | 5,761 / 5,736 | 1,442 —
  matches the historical 1888 CA result (Harrison 124,816, Cleveland 117,729).
- Cross-check: Wikipedia "1888 United States presidential election in California" San Diego
  row 4,661 / 3,189 / 322 / 11 / 11, total 8,194 — exact match (that page's table itself
  cites "Original Manuscript Returns, California State Archives"; this Roster is the
  digitized near-primary print of the same canvass).

Confidence: high (page-image read; statewide totals verified; Wikipedia cross-check exact).

---
## 1898-11-08 — Governor

Source (near-primary): California Blue Book, or State Roster, 1899 (Secretary of State),
"VOTE FOR GOVERNOR. (At general election held November 8, 1898.)", printed p.227.
Digitized on HathiTrust (full view, public domain), item id `mdp.39015041451256`, page
scan seq 271. Read from a full-page SCREENSHOT of the HathiTrust page viewer (raw-CDP
fetch through the session's isolated debug Chrome; HathiTrust Cloudflare blocks
curl/WebFetch). No archive.org copy of the 1899 Blue Book was found (advancedsearch
queries for "blue book california" list 1903 as the earliest edition).

San Diego County (single column per candidate):

| Candidate | San Diego votes |
|---|---|
| Henry T. Gage (Republican, Union Labor) | 3,506 |
| James G. Maguire (People's Party, Democratic, Silver Republican fusion) | 3,259 |
| Job Harriman (Socialist Labor) | 208 |
| J. E. McComas (Prohibition) | 144 |
| Scattering | — (blank for San Diego; statewide 9) |
| **Contest sum** | **7,117** |

Total votes cast for the county: not printed with this table.

Provenance:
- HathiTrust: https://babel.hathitrust.org/cgi/pt?id=mdp.39015041451256&view=1up&seq=271 (printed p.227)
- Locating query: Wikipedia "1898 California gubernatorial election" county-table ref cites
  exactly this volume/page ("California Blue Book, or State Roster 1899, pages 227,
  url=https://babel.hathitrust.org/cgi/pt?id=mdp.39015041451256&view=1up&seq=271").
- Verbatim San Diego row from page image (36th county row): "San Diego 3,506 | 208 | 3,259 | 144 | ----"
- Statewide totals row: 148,354 / 5,143 / 129,261 / 4,297 / 9 — matches the historical 1898
  result (Gage 148,354, Maguire 129,261) and the same figures reprinted in the 1903 Blue
  Book's "ELECTION NOVEMBER 8, 1898" summary (archive.org `california-blue-book-1903-sfg`).
- Cross-check: Wikipedia San Diego row 3,506 / 3,259 / 208 / 144 / 0, total 7,117 — exact match.

Confidence: high (page-image read; statewide totals verified twice; Wikipedia cross-check exact).

---
## Summary table (San Diego County certified denominators)

| Election | Contest | Contest sum (SD) | Total cast (SD, if printed) | Confidence | Primary source |
|---|---|---|---|---|---|
| 1884-11-04 | President | 1,965 | not printed | high | Governmental Roster 1889 p.50 (HathiTrust uc1.32106019792388 seq 66) |
| 1886-11-02 | Governor | 2,826 | not printed | high | SOV 1886 p.11 (archive.org statementofvoteo1886cali n36) |
| 1888-11-06 | President | 8,194 | not printed | high | Governmental Roster 1889 p.51 (HathiTrust uc1.32106019792388 seq 67) |
| 1890-11-04 | Governor | 7,306 | not printed | high | CA Blue Book 1891 p.88 (HathiTrust umn.31951d026032878 seq 100) |
| 1892-11-08 | President | 7,712 | not printed | high | SOV 1892 (archive.org statementofvoteo1886cali n98-n101) |
| 1894-11-06 | Governor | 7,124 | 7,124 (printed "Total Vote by Counties") | high | CA Blue Book 1895 p.254 (HathiTrust umn.31951d026032894 seq 310) |
| 1896-11-03 | President | 7,762 (highest-elector; Wikipedia-convention 7,748) | not printed | high | SOV 1896 (statementofvoteo1886cali n110-n116) |
| 1898-11-08 | Governor | 7,117 | not printed | high | CA Blue Book 1899 p.227 (HathiTrust mdp.39015041451256 seq 271) |
| 1900-11-06 | President | 6,931 (highest-elector; Wikipedia-convention 6,921) | not printed | high | CA Blue Book 1903 pp.311-314 (california-blue-book-1903-sfg n341-n344) |
| 1902-11-04 | Governor | 6,459 | not printed | high | CA Blue Book 1903 p.332 (california-blue-book-1903-sfg n362) |
| 1904-11-08 | President | 7,241 (highest-elector; Wikipedia-convention 7,231) | not printed | high | CA Blue Book 1907 pp.419-422 (californiabluebo0000vari n454-n457) |
| 1906-11-06 | Governor | 7,800 | not printed | high | CA Blue Book 1907 p.437 (californiabluebo0000vari n472) |
| 1908-11-03 | President | 9,409 (highest-elector; Wikipedia-convention 9,403) | not printed | high | SOV 1908 pp.3-7 (statementofvo19081922cali n6-n10) |
| 1910-11-08 | Governor | 9,479 | 9,481 (printed in 1912 SOV) | high | SOV 1910 p.2 (statementofvoteo1886cali n219); total: SOV 1912 p.3 (statementofvo19081922cali n34) |
| 1912-11-05 | President | 21,728 | 22,933 (printed; registration 30,041) | high | SOV 1912 pp.3-12 (statementofvo19081922cali n34-n43) |
| 1916-11-07 | President | 36,552 (highest-elector; Wikipedia-convention 36,537) | not printed | high | SOV 1916 pp.8-14 (statementofvo19081922cali n177-n183) |
| 1918-11-05 | Governor | 25,100 | not printed | high | SOV 1918 p.7 (statementofvo19081922cali n264) |
| 1920-11-02 | President | 31,098 (highest-elector; Wikipedia-convention 31,087) | not printed | high | SOV 1920 pp.8-15 (statementofvo19081922cali n313-n320) |

NOT FOUND: none — all fifteen elections sourced. (1914 and 1922 out of scope per
instructions.)

Notes:
- Presidential contests before the single-popular-vote-line era print one column per
  ELECTOR; there is no single printed "candidate vote". Each section gives full elector
  ranges; the sums above use the county's highest elector per slate, with the
  Wikipedia-style figure (canonical statewide-top elector) noted where it differs by a
  few votes. Gubernatorial figures are exact single-column reads.
- 1920 Wikipedia display value for Harding in San Diego (19,286) is a digit transposition
  of the SOV's 19,826 (Wikipedia's own row total and percentage confirm).
---
## Scope extension (added after the original 15): 1886, 1890, 1894 gubernatorial generals

## 1886-11-02 — Governor

Source (primary): "Official Returns of the Vote for State Officers of California,
November 2, 1886" ("Statement of the Vote ... General Election Held November 2, A.D. 1886",
Thomas L. Thompson, Secretary of State), bound in archive.org item `statementofvoteo1886cali`,
"FOR GOVERNOR" table, printed p.11. Read from the PAGE IMAGE.

San Diego County:

| Candidate | San Diego votes |
|---|---|
| John F. Swift (Republican) | 1,362 |
| Washington Bartlett (Democrat) | 1,159 |
| Joel Russell (Prohibition) | 240 |
| P. D. Wigginton (American) | 22 |
| C. C. O'Donnell (Independent) | 43 |
| Scattering | — (blank for San Diego; statewide 336) |
| **Contest sum** | **2,826** |

Total votes cast for the county: not printed with this table.

Provenance:
- archive.org item `statementofvoteo1886cali`, printed p.11, leaf n36 =
  https://archive.org/details/statementofvoteo1886cali/page/n36
  (image: https://archive.org/download/statementofvoteo1886cali/page/n36)
- Locating query: Wikipedia "1886 California gubernatorial election" county-table ref cites
  this item at /page/n35 (the facing page in two-page view); the table itself is leaf n36.
- Verbatim San Diego row from image: "San Diego 1,362 | 1,159 | 240 | 22 | 43 | ----"
- Statewide totals row: 84,316 / 84,970 / 6,432 / 7,347 / 12,227 / 336 — matches the
  historical 1886 result (Bartlett 84,970 over Swift 84,316).
- Cross-check: Wikipedia San Diego row 1,159 / 1,362 / 43 / 22 / 240 / 0, total 2,826 — exact match.

Confidence: high (page-image read; statewide totals verified; Wikipedia cross-check exact).

---
## 1890-11-04 — Governor

Note: the archive.org SFPL compilation item `statementofvoteo1886cali` does NOT contain a
1890 Statement of the Vote — its `STATEMENT OF THE VOTE` section headers (confirmed by
grepping the downloaded djvu.txt on disk) run 1886 -> 1892 -> 1896 -> 1908 -> 1910 with
no 1890, 1894, 1898, 1900, 1902, 1904, or 1906 content in between. Fell back to the CA
Blue Book per the task instructions.

Source (near-primary): "California Blue Book, or State Roster. 1891." (E. G. Waite,
Secretary of State; "Published in accordance with an Act of the Legislature, approved
March 31, 1891"), table "VOTE OF THE STATE OF CALIFORNIA, AT THE GENERAL ELECTION HELD
NOVEMBER 4, A. D. 1890. FOR GOVERNOR.", printed p.88. Digitized on HathiTrust (full view,
public domain, Google/UMN-digitized), item id `umn.31951d026032878`, page-viewer seq 100.
Read from a full-page SCREENSHOT of the HathiTrust page viewer (HathiTrust blocks
curl/WebFetch via Cloudflare; fetched through the session's isolated debug Chrome with a
raw CDP session, the cdp_fetch.js/hathi_shot.js technique).

San Diego County (single column per candidate):

| Candidate | San Diego votes |
|---|---|
| H. H. Markham (Republican) | 3,942 |
| E. B. Pond (Democrat) | 2,967 |
| John Bidwell (Prohibition) | 395 |
| Scattering | 2 |
| **Contest sum** | **7,306** |

Total votes cast for the county: not printed with this table.

Provenance:
- HathiTrust: https://babel.hathitrust.org/cgi/pt?id=umn.31951d026032878&seq=100 (printed p.88)
- Locating query: HathiTrust "Search in this text" q1=`Pond` -> single hit at seq 100,
  pageNum 88; kwic snippet: "VOTE OF THE STATE OF CALIFORNIA, AT THE GENERAL ELECTION HELD
  NOVEMBER 4, A. D. 1890. FOR GOVERNOR. COUNTIES. Scattering. John Bidwell (P.). E. B.
  Pond (D.).... H. H. Markham (R.)". Catalog record for the edition series (with the
  per-year HathiTrust item ids, including 1891 and 1895) found via HathiTrust catalog
  record 100001122, fetched with the same raw-CDP technique.
- Verbatim San Diego row from page image: "San Diego 3,942 | 2,967 | 395 | 2"
- Statewide totals row from the same page image (below Yuba): 125,129 / 117,184 / 10,073 /
  71 — matches the historical 1890 result and the "STATE POLITICAL HISTORY" summary table
  reprinted in the 1903 California Blue Book (archive.org `california-blue-book-1903-sfg`,
  djvu.txt "ELECTION NOVEMBER 4, 1890.": "Governor—Henry H. Markham (Rep.), 125,129; E. B.
  Pond (Dem.), 117,184; John Bidwell (Pro., Amer.), 10,073.").
- Cross-check: no Wikipedia "1890 California gubernatorial election" county table found;
  the independent 1903 Blue Book statewide-summary match serves as the cross-check.

Confidence: high (page-image read; statewide totals independently verified against the
1903 Blue Book's historical-summary reprint).

---
## 1894-11-06 — Governor

Note: same as 1890 above — `statementofvoteo1886cali` has no 1894 content; fell back to
the CA Blue Book.

Source (near-primary): "California Blue Book, or State Roster. 1895." (L. H. Brown,
Secretary of State; "Published in accordance with an Act of the Legislature, approved
March 23, 1893"), table "VOTE FOR GOVERNOR. (At the general election held November 6,
1894.)", printed p.254. HathiTrust item id `umn.31951d026032894`, page-viewer seq 310.
Read from a full-page SCREENSHOT of the HathiTrust page viewer (same raw-CDP fetch
method).

San Diego County (single column per candidate, plus the printed county-total column):

| Candidate | San Diego votes |
|---|---|
| James H. Budd (Democrat) | 1,897 |
| Morris M. Estee (Republican) | 2,848 |
| Henry French (Prohibition) | 401 |
| J. V. Webster (People's Party) | 1,978 |
| **Contest sum / printed "Total Vote by Counties"** | **7,124** |

Total votes cast for the county: **7,124** (PRINTED, "Total Vote by Counties" column;
equals the four-candidate sum exactly — no scattering vote recorded for San Diego).

Provenance:
- HathiTrust: https://babel.hathitrust.org/cgi/pt?id=umn.31951d026032894&seq=310 (printed p.254)
- Locating query: HathiTrust "Search in this text" q1=`Estee` -> hit at seq 310, pageNum
  254; the kwic snippet returned the entire table (all counties + totals row) in reading
  order: Counties / Budd, James H. (Democrat) / Estee, Morris M. (Republican) / French,
  Henry (Prohibition) / Webster, J. V. (People's Party) / Total Vote by Counties.
- Verbatim San Diego row from page image: "San Diego 1,897 | 2,848 | 401 | 1,978 | 7,124"
- Statewide totals row: 111,944 / 110,738 / 10,561 / 51,304 / 284,548 (footnote "Scattering:
  Santa Clara, 1." accounts for the 1-vote excess of the Total column over the sum of the
  four candidate columns) — matches the "STATE POLITICAL HISTORY" summary reprinted in the
  1903 California Blue Book (archive.org `california-blue-book-1903-sfg`, djvu.txt
  "ELECTION NOVEMBER 6, 1894.": "Governor—James H. Budd (Dem.), 111,944; Morris M. Estee
  (Rep.), 110,738; Henry French (Pro.), 10,561; J. V. Webster (P. P.), 51,304.").
- Cross-check: no Wikipedia "1894 California gubernatorial election" county table found;
  the independent 1903 Blue Book statewide-summary match, plus San Diego's own printed
  county total equalling the candidate sum exactly, serve as the cross-check.

Confidence: high (page-image read; statewide totals independently verified; county total
column corroborates the candidate sum with zero discrepancy).

---
## Scope extension (added after the 1886/1890/1894 batch): seven pre-1884 elections

No California Secretary of State "Statement of the Vote" is digitized for any of 1871-1882
(checked archive.org for each year individually; the only bound SOV compilation online,
`statementofvoteo1886cali`, starts at 1886). The "California Blue Book, or State Roster"
series is not digitized before its 1891 edition (for the 1890 election) — checked the full
HathiTrust catalog record for the series. The "Governmental Roster ... 1889" (HathiTrust
`uc1.32106019792388`, already used for the 1884/1888 entries above) turns out to print
full county-by-county returns for ONLY those two most-recent elections (1884, 1888) — a
full-text search inside that volume for "Booth", "Haight", "Irwin", and "Weaver" (candidate
surnames for 1871, 1875, and 1880) returns no county-return tables at all, only the
governors'-terms list and biographical/roster entries. Fell back to "The Tribune Almanac
and Political Register" (New York Tribune), which prints a "CALIFORNIA." county-by-county
table each year covering the most recent state and presidential elections. Five of the
seven target years are covered by almanac editions that are digitized on archive.org
(1872, 1877, 1880, 1881); the sixth (1882 Governor) falls in the one almanac year — "for
1883" — that is not digitized anywhere found (archive.org, HathiTrust, Google Books), and
neither the neighboring 1881 nor 1884 edition carries that county table forward (confirmed:
the 1884 edition's "Election Returns" section has zero full-text hits for "San Diego" or
"Stoneman"/"Estee" anywhere in the volume — California is simply not included in that
edition's returns section). For 1882 Governor only, this file falls back one more level to
a contemporary newspaper telegraph dispatch (California Digital Newspaper Collection,
cdnc.ucr.edu), flagged at low confidence since it is outside the task's named source list
and is explicitly an incomplete count.

## 1871-09-06 — Governor

Source (near-primary): "The Tribune Almanac and Political Register for 1872" (New York
Tribune), archive.org item `vol1872tribuneal00unse`, table "CALIFORNIA. GOV'NOR,'71.
CONG.'71. CONG.'68.", District I sub-table, printed p.76.

San Diego County:

| Candidate | San Diego votes |
|---|---|
| Newton Booth (Republican) | 631 |
| Henry H. Haight (Democrat) | 654 |
| **Contest sum** | **1,285** |

Total votes cast for the county: not printed with this table.

Provenance:
- archive.org item `vol1872tribuneal00unse`, printed p.76, leaf n79 =
  https://archive.org/details/vol1872tribuneal00unse/page/n79
  (image: https://archive.org/download/vol1872tribuneal00unse/page/n79_w1200.jpg)
- Locating query: archive.org full-text "search inside" API
  (`ia*.us.archive.org/fulltext/inside.php?item_id=vol1872tribuneal00unse&q=California+Booth+Haight`)
  hit the District-III grand-total line on the same leaf; the county table (Districts I-III)
  occupies the whole of leaf n79 (printed p.76).
- Verbatim San Diego row (District I) from the page image: "San Diego 631 654.. 635 642..
  128 236" under columns "Booth | Haight | Houg. | Archer | Pixley | Axt." (the last two
  column-pairs are 1871 Congress and 1868 Congress races, not part of this contest).
- Statewide cross-check, same page: District grand total "Grand Tot..62581 57520..." with
  note "Total maj. for Booth, 5061" — matches the well-documented historical 1871 result
  (Booth 62,581, Haight 57,520, majority 5,061).
- Independent cross-check: the 1877 Tribune Almanac (see next three entries) separately
  notes, in its own California section, "in 1871, 120,101 [total vote], when Newton Booth's
  (Rep.) maj. for Governor, over Haight, Dem., was 5,061" — same majority, different
  edition/typesetting.

Confidence: high (near-primary compilation; statewide grand total and an independently
typeset 1877-edition cross-reference both match the historical majority exactly).

---
## 1872-11-05 — President (Presidential Electors)

Source (near-primary): "The Tribune Almanac and Political Register for 1877" (New York
Tribune), archive.org item `tribunealmanac1877newyuoft`, table "CALIFORNIA." (columns
grouped "1876—PRES.—1872" and "GOV. 1875"), printed p.65.

San Diego County:

| Candidate | San Diego votes |
|---|---|
| Ulysses S. Grant (Republican) | 513 |
| Horace Greeley (Liberal Republican/Democratic fusion) | 360 |
| **Contest sum** | **873** |

Total votes cast for the county: not printed with this table.

Provenance:
- archive.org item `tribunealmanac1877newyuoft`, printed p.65, leaf n66 =
  https://archive.org/details/tribunealmanac1877newyuoft/page/n66
  (image: https://archive.org/download/tribunealmanac1877newyuoft/page/n66_w1800.jpg)
- Locating query: archive.org full-text "search inside" API, q="CALIFORNIA" -> the
  "ELECTION RETURNS" section's California table, spanning leaf n66 (printed p.65, counties
  Alameda-Modoc) and continuing onto leaf n67 (printed p.66, counties Mono-Yuba plus
  statewide totals), confirmed by direct page-image inspection (binary-searched the leaf
  numbering against printed page numbers using known anchor pages).
- Verbatim San Diego row, cropped/zoomed from the leaf-n66 image: "San Diego. 794 668 513
  360.. 593 755 252" under column headers "Hayes Tilden Grant Greeley Phelps Irwin
  Bidwell" (this single row supplies this entry's Grant/Greeley pair, the next entry's
  Phelps/Irwin/Bidwell trio, and the entry after that's Hayes/Tilden pair).
- Statewide cross-check (leaf n66, "Total" line): "Total..79269 76464 54020 40718..31322
  61509 29752" — the 1872 pair (Grant 54,020 / Greeley 40,718) matches the documented
  historical California result for the 1872 presidential election exactly.

Confidence: high (near-primary compilation reprinting the official county canvass;
statewide totals match the known historical 1872 California result exactly).

---
## 1875-09-01 — Governor

Source (near-primary): same table as the 1872-President entry immediately above — "The
Tribune Almanac and Political Register for 1877", archive.org item
`tribunealmanac1877newyuoft`, printed p.65, "GOV. 1875" columns.

San Diego County:

| Candidate | San Diego votes |
|---|---|
| Timothy G. Phelps (Republican) | 593 |
| William Irwin (Democrat) | 755 |
| John Bidwell (Independent) | 252 |
| **Contest sum** | **1,600** |

Total votes cast for the county: not printed with this table.

Provenance:
- Same source/leaf/verbatim row as the 1872-President entry above: "San Diego. 794 668 513
  360.. 593 755 252", Phelps/Irwin/Bidwell = the last three numbers (593, 755, 252).
- Statewide cross-check (leaf n66, "Total" line): Phelps 31,322 / Irwin 61,509 / Bidwell
  29,752 — matches the historical 1875 result (William Irwin elected Governor).

Confidence: high (near-primary compilation; statewide totals match the historical 1875
result, including the winning candidate).

---
## 1876-11-07 — President (Presidential Electors)

Source (near-primary): same table again — "The Tribune Almanac and Political Register for
1877", archive.org item `tribunealmanac1877newyuoft`, printed p.65, "1876—PRES." columns
(this was the almanac's own current-year election, so it is the primary subject of the
table rather than a retrospective column).

San Diego County:

| Candidate | San Diego votes |
|---|---|
| Rutherford B. Hayes (Republican) | 794 |
| Samuel J. Tilden (Democrat) | 668 |
| **Contest sum** | **1,462** |

Total votes cast for the county: not printed with this table.

Provenance:
- Same source/leaf/verbatim row as the two entries above: "San Diego. 794 668 513 360..
  593 755 252", Hayes/Tilden = the first two numbers (794, 668).
- Statewide cross-check (leaf n66, "Total" line): Hayes 79,269 / Tilden 76,464 — California
  went for Hayes by a narrow margin, matching the documented historical result.
- Independent cross-check: the Tribune Almanac for 1880 and for 1881 (see the 1879-Governor
  and 1880-President entries below) both separately reprint a "1876" retrospective column
  in their own California tables, and both give San Diego as Hayes 794 / Tilden 668 —
  an exact match from two independently typeset later editions.

Confidence: high (near-primary compilation; statewide totals match the historical result;
independently corroborated by two later almanac editions' retrospective columns, exact
match).

---
## 1879-09-03 — Governor

Source (near-primary): "The Tribune Almanac and Political Register for 1880" (New York
Tribune), archive.org item `vol1880tribuneal00unse`, table "CALIFORNIA." (columns grouped
"GOVERNOR, '79" and "PRES., '76"), printed p.48.

San Diego County:

| Candidate | San Diego votes |
|---|---|
| George C. Perkins (Republican) | 626 |
| Hugh J. Glenn (Democratic & Workingmen's/New Constitution fusion) | 678 |
| William F. White (Workingmen's) | 108 |
| **Contest sum** | **1,412** |

Total votes cast for the county: not printed with this table.

Provenance:
- archive.org item `vol1880tribuneal00unse`, printed p.48, leaf n47 =
  https://archive.org/details/vol1880tribuneal00unse/page/n47
  (image: https://archive.org/download/vol1880tribuneal00unse/page/n47_w800.jpg)
- Locating query: archive.org full-text "search inside" API, q="CALIFORNIA" -> hit on the
  same leaf as the "GOVERNOR, '79 -- PRES., '76" county table (confirmed by direct
  page-image inspection).
- Verbatim San Diego row from the page image: "San Diego. 626 678 108.. 794 668" under
  columns "kins[Per-].Glenn.White." (Governor 1879) and "Hayes.Tilden." (President 1876,
  retrospective). The Hayes/Tilden pair (794, 668) is an exact match to the 1876-President
  entry above, sourced from an entirely different, independently typeset almanac edition.
- Statewide cross-check, same page: "Total....67965 47647 44482..79279 76468" and a
  footnote text elsewhere on the page: "the aggregate votes cast for other State officers
  in 1879 ... Lieut.-Gov'nr. J. Mansfield, Rep.... 67,301" and (on the facing page) "In
  1879 the vote for Governor was: Perkins (Rep.), 67965; G[l]enn (D-m. and New Con.),
  47647; White (Workingman), 44482. Total, 160091" (this second citation appears again,
  independently, on leaf n40/printed p.41 of the 1881 edition — see the 1880-President
  entry below) — matches the documented historical 1879 California governor result.

Confidence: high (near-primary compilation; statewide totals match the historical result;
the Hayes/Tilden retrospective sub-columns cross-validate exactly against the independently
sourced 1876-President entry above).

---
## 1880-11-02 — President (Presidential Electors)

Source (near-primary, Garfield/Hancock only): "The Tribune Almanac and Political Register
for 1881" (New York Tribune), archive.org item `vol1881tribuneal00unse`, table
"CALIFORNIA. PRESIDENT." (columns grouped "*1880" and "1876†"), printed p.41.

San Diego County:

| Candidate | San Diego votes |
|---|---|
| James A. Garfield (Republican) | 743 |
| Winfield S. Hancock (Democrat) | 546 |
| James B. Weaver (Greenback) | 19 (uncertified — see below) |
| **Contest sum (Garfield + Hancock, certified)** | **1,289** |
| **Contest sum (all three, uncertified)** | **~1,308** |

Total votes cast for the county: not printed with this table.

The Tribune Almanac's California presidential table omits a Greenback/Weaver column
entirely (unlike, e.g., its Arkansas table on the same page, which does carry one) — its
printed "Total vote" row for California (160,795) is exactly Garfield + Hancock with no
room for Weaver. No digitized state-level source with a Weaver county figure was found (see
the "Scope extension" note above for what was checked). Weaver's San Diego County count is
therefore sourced separately, at lower confidence, from a pre-canvass newspaper dispatch:
Sacramento Daily Union, November 9, 1880, p.2 (viewed via the California Digital Newspaper
Collection, cdnc.ucr.edu, article id `SDU18801109.2.2`): "SAN DIEGO COUNTY. San Diego —The
canvass is not made in this county till next Monday. Complete returns on the Union's
blanks, filled up by the election officers give the following totals: Garfield, 737;
Hancock, 554; Weaver 19; ..." — note this dispatch's own Garfield/Hancock figures (737/554)
differ slightly from the certified almanac figures (743/546), confirming it is a pre-canvass
tally that the later official count adjusted; Weaver's certified count could differ
similarly from 19.

Provenance (Garfield/Hancock, high confidence):
- archive.org item `vol1881tribuneal00unse`, printed p.41, leaf n40 =
  https://archive.org/details/vol1881tribuneal00unse/page/n40
  (image: https://archive.org/download/vol1881tribuneal00unse/page/n40_w800.jpg)
- Locating query: archive.org full-text "search inside" API, q="CALIFORNIA" -> hit on the
  same leaf as the "PRESIDENT ... *1880 ... 1876†" county table (confirmed by direct
  page-image inspection).
- Verbatim San Diego row from the page image: "San Diego....... 743 546 794 668" under
  columns "Garfield.Hancock." (1880) and "Hayes Tilden" (1876, retrospective — again an
  exact match to the 1876-President entry above).
- Statewide cross-check, same page: "Total.........80378 80417 79279 76468" / "Majority
  ......... 39 2767" — California's electors went to Hancock by a very narrow margin,
  matching the documented historical near-tie result.

Provenance (Weaver, medium/low confidence):
- CDNC article `SDU18801109.2.2` = https://cdnc.ucr.edu/?a=d&d=SDU18801109.2.2
- Locating query: CDNC full-text search for "Garfield Hancock Weaver San Diego" (the CDNC
  "search inside" JSON endpoint, `fulltext/inside.php`, reached directly since CDNC itself
  is Cloudflare-gated to a plain curl and required the isolated-Chrome raw-CDP fetch
  technique).
- Verbatim text quoted above.

Confidence: high for Garfield/Hancock; medium/low for Weaver (uncertified newspaper
pre-canvass figure only — no certified county figure located in any digitized source).

---
## 1882-11-07 — Governor

No certified county figure was located. Checked and exhausted, in the task's priority
order: (1) the SOV — not digitized for 1882, and the one bound SOV compilation on
archive.org starts at 1886; (2) the CA Blue Book / Governmental Roster — the Roster 1889
has no county-return table before 1884 (full-text-searched inside the volume for "Stoneman"
and "Estee": zero hits), and no Blue Book edition is digitized earlier than 1891; (3) the
Tribune Almanac — the one edition that would carry this election ("for 1883") is not
digitized under any identifier found on archive.org, HathiTrust, or Google Books, and
neither the "for 1881" nor the "for 1884" edition carries a California county table forward
across the gap (the 1884 edition's Election-Returns section has zero full-text hits for
"San Diego", "Stoneman", or "Estee" anywhere in the volume — California is entirely absent
from that edition's returns section, apparently because no fresh California election fell
inside its 1883-84 coverage window). Also checked Appleton's Annual Cyclopaedia (archive.org
`newappletonsannu07newyuoft`, the 1882 volume of the "New series"): its California article
(p.83) gives only the statewide total — "The vote for Governor was as follows: Total,
164,657; Democratic, 90,649; opposition, 74,008; Democratic majority, 16,641" — with no
county breakdown at all.

Falling back one level further than the task's named source list, to a contemporary
newspaper telegraph dispatch (flagged at low confidence accordingly):

Source (not certified, not on the task's source list): Los Angeles Herald, November 10,
1882, p.2 (viewed via the California Digital Newspaper Collection, cdnc.ucr.edu, article id
`LAH18821110.2.12`), a telegraphic dispatch datelined "San Diego, Nov. 9th": "San Diego
returns, all but ten small precincts, complete: Estee, 747; Stoneman, 719; ..." (the
dispatch continues with down-ballot county-office tallies, not reproduced here).

San Diego County (near-complete, NOT the certified canvass):

| Candidate | San Diego votes |
|---|---|
| Morris M. Estee (Republican) | 747 |
| George Stoneman (Democrat) | 719 |
| **Contest sum (incomplete — ~10 small precincts still outstanding)** | **~1,466** |

Total votes cast for the county: not available (this dispatch is explicitly missing ~10
small precincts; the true certified total is somewhat higher than 1,466).

Provenance:
- CDNC article `LAH18821110.2.12` = https://cdnc.ucr.edu/?a=d&d=LAH18821110.2.12
- Locating query: CDNC full-text search for "Stoneman Estee canvass Diego", refined to
  "Stoneman Estee San Diego county" (same raw-CDP fetch technique as above).
- Verbatim text quoted above.

Confidence: low (uncertified, explicitly incomplete newspaper dispatch; no state-level or
almanac source could be located despite exhausting every option on the task's source list
plus one newspaper fallback). Record this year's contest sum as effectively NOT FOUND at
certified/high confidence; the ~1,466 figure above is the best available approximation.

---
## Summary table (pre-1884 batch: seven elections)

| Election | Contest | Contest sum (SD) | Confidence | Primary source |
|---|---|---|---|---|
| 1871-09-06 | Governor | 1,285 | high | Tribune Almanac for 1872 p.76 (vol1872tribuneal00unse n79) |
| 1872-11-05 | President | 873 | high | Tribune Almanac for 1877 p.65 (tribunealmanac1877newyuoft n66) |
| 1875-09-01 | Governor | 1,600 | high | Tribune Almanac for 1877 p.65 (tribunealmanac1877newyuoft n66) |
| 1876-11-07 | President | 1,462 | high | Tribune Almanac for 1877 p.65 (tribunealmanac1877newyuoft n66) |
| 1879-09-03 | Governor | 1,412 | high | Tribune Almanac for 1880 p.48 (vol1880tribuneal00unse n47) |
| 1880-11-02 | President | 1,289 (Garfield+Hancock, certified); ~1,308 incl. Weaver (uncertified) | high (Garfield/Hancock); medium/low (Weaver) | Tribune Almanac for 1881 p.41 (vol1881tribuneal00unse n40); Weaver: Sacramento Daily Union 1880-11-09 via CDNC (SDU18801109.2.2) |
| 1882-11-07 | Governor | ~1,466 (incomplete, uncertified) | low | Los Angeles Herald 1882-11-10 via CDNC (LAH18821110.2.12); NOT FOUND at certified/high confidence — no SOV, Blue Book, or Tribune Almanac edition digitized for this year |

NOT FOUND (certified): 1882-11-07 Governor. Every other year in this batch of seven is
sourced at high confidence from the Tribune Almanac's near-primary county tables, four of
them (1872 President, 1875 Governor, 1876 President, all reading off one shared table; plus
the retrospective Hayes/Tilden columns reprinted in the 1880 and 1881 almanac editions)
cross-validated exactly across independently typeset editions.
---
