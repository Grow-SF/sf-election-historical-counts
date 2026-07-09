# 1908 primary "Vote Polled" denominator investigation

Mission: what does the SF Registrar cumulative-table Vote Polled figure 22,698 (Aug 11, 1908 primary)
count: all-party ballots, Republican-only, or something else? Same for May 5, 1908 (24,178 vs Call's 24,305).

Primary source: archive.org sanfranciscomuni58sanfrich (FY1908-09 Municipal Reports) and
sanfranciscomuni57sanfrich (FY1907-08).

## Log (as I go)

### muni58 (FY1908-09) cumulative table, printed p.1118, leaf n1137 (API page 1138)
Image: https://archive.org/download/sanfranciscomuni58sanfrich/page/n1137
Locating query: fulltext inside.php q="24,178" -> page 1138.
- Table "Showing date of Elections, Number of Precincts, the Total Registration and Votes cast at each Election, since June 19, 1878."
- NO Aug 11, 1908 row AT ALL. Sequence: "May 5, 1908 / 125 / 36,564 / 24,178 / Primary." then "May 11, 1908 / 125 / (blank) / 23,560 / Bonds." then "Nov. 3, 1908 / 300 / 75,388 / 61,625 / General-Presidential."
- So 22,698 must enter the series in a LATER volume.
- Note restricted registration for primaries: Aug 14 1906 primary reg 22,026 (vs Nov 1906 51,633); May 5 1908 primary reg 36,564 (vs Nov 1908 75,388). Aug 1899 primary: 106 pcts, reg 62,410, vote 32,521. Aug 13 1907 primary: 74 pcts, reg 60,469, vote 22,851.
- Fulltext search of muni58 for "22,698", "22,117", "24,305", "30,647": zero matches (indexed=true).

### muni58 printed p.1121, leaf n1140: MAY 5 1908 PRIMARY CANVASS = ALL-PARTY
Image: https://archive.org/download/sanfranciscomuni58sanfrich/page/n1140
Header: "PRIMARY ELECTION MAY 5, 1908", columns by Assembly Districts (28th-45th):
Republican Vote Polled / Democratic Vote Polled / Independence League Vote Polled / Prohibition Vote Polled / Total Vote Polled.
Totals row: 17,238 / 6,638 / 275 / 27 / 24,178.
VERDICT (May 5): 24,178 is the all-party ballot total; Republican-only was 17,238.
Same page below: "PROPOSITIONS TO INCUR A BONDED DEBT... Special Election... 11th day of May, A. D. 1908" district table, Total 23,560.

### muni58 printed p.1125, leaf n1144: AUG 11 1908 PRIMARY CANVASS. 22,698 = REPUBLICAN-ONLY
Image: https://archive.org/download/sanfranciscomuni58sanfrich/page/n1144
(rotated/landscape table; item fulltext search does NOT find "22,698" because OCR mangles the rotated page)
Header (verbatim): "PRIMARY ELECTION HELD IN THE CITY AND COUNTY OF SAN FRANCISCO, STATE OF CALIFORNIA, ON TUESDAY, AUGUST 11th, 1908."
Columns per Assembly District (28th-45th): Republican Vote Polled / Democratic Vote Polled / Independent Vote Polled / Socialist Vote Polled / Prohibition Vote Polled / Union Labor Vote Polled / Total.
Totals row: Republican 22,698 / Democratic 8,605 / Independent 176 / Socialist 301 / Prohibition 24 / Union Labor 1,527 / TOTAL 33,331.
Arithmetic check: 22698+8605+176+301+24+1527 = 33331. OK.
VERDICT (Aug 11): 22,698 is the REPUBLICAN party vote polled only. All-party total = 33,331.
Consistent with SF Call day-after: Rep columns sum 22,117 (one precinct missing) vs official 22,698; lead's "exceeded 30,000" matches 33,331.
Adjacent pages: p.1122-1124 (leaves n1141-n1143) are May 11 1908 bond props 1-6.

### muni57 (FY1907-08) printed p.882, leaf n905: May 5 1908 canvass (independent second printing)
Image: https://archive.org/download/sanfranciscomuni57sanfrich/page/n905
Locating query: inside.php item sanfranciscomuni57sanfrich (server ia800708, path /1/items/...) q="24,178" -> page 906; q="17,238" -> page 906.
Header (verbatim): "STATEMENT OF THE VOTES POLLED AT THE PRIMARY ELECTION HELD TUESDAY, THE FIFTH DAY OF MAY, A. D. 1908, FOR DELEGATES TO THE REPUBLICAN STATE AND DISTRICT CONVENTIONS, DEMOCRATIC STATE AND DISTRICT CONVENTIONS INDEPENDENCE LEAGUE STATE AND DISTRICT CONVENTION, AND THE PROHIBITION STATE AND DISTRICT CONVENTION."
Totals: Republican 17,238 / Democrat 6,638 / Independence League 275 / Prohibition 27 / Total Vote 24,178.
Matches muni58 p.1121 exactly. 24,178 = ALL-PARTY total; Call's day-after 24,305 was 127 high vs official.

### muni62 (FY1912-13) printed p.261, leaf n278: the cumulative-table row that carries 22,698
Image: https://archive.org/download/munisanfrancisco62sanfrich/page/n278
Row (verbatim, landscape table): "Aug. 11, 1908 .... 135 / 55,437 / 22,698 / Primary."
Adjacent rows: "May 5, 1908 .... 125 / 36,564 / 24,178 / Primary." and "May 11, 1908 .... 125 / (blank) / 23,560 / Bonds." and "Nov. 3, 1908 .... 300 / 75,388 / 61,625 / General-Presidential."
NO footnote or stated rule about party scope anywhere on the page; the only footnote is "*Voting Machines used." (on Nov 8 1904 and Nov 6 1906).
Note the FY1908-09 volume's own cumulative table OMITTED the Aug 11 1908 row entirely; it first appears in later printings, populated with the Republican-column figure.

## VERDICT
1. Aug 11, 1908: 22,698 = REPUBLICAN-PRIMARY BALLOTS ONLY. Official canvass (muni58 p.1125, leaf n1144)
   gives per-party Vote Polled totals Rep 22,698 / Dem 8,605 / Ind 176 / Soc 301 / Proh 24 / UL 1,527,
   ALL-PARTY TOTAL 33,331. District Republican entries sum exactly to 22,698; Total column sums exactly to 33,331.
   The SF Call day-after picture (Rep ~22,117 w/ one precinct missing; total "exceeded 30,000") is fully consistent.
2. May 5, 1908: 24,178 = ALL-PARTY total (Rep 17,238 + Dem 6,638 + IL 275 + Proh 27), per canvasses in
   BOTH muni57 p.882 (leaf n905) and muni58 p.1121 (leaf n1140).
3. The registrar cumulative series MIXES denomination kinds across years with NO stated rule:
   - Aug 8 1899 row 32,521 and May 5 1908 row 24,178 are all-party totals;
   - Aug 11 1908 row 22,698 is the Republican column of the canvass (all-party was 33,331).
   The row first appears in later volumes (muni62 p.261 etc.); whoever back-filled it took the first
   (Republican) column instead of the Total column. Looks like a compilation slip, not a policy.
   Registration 55,437 in that row is plausibly total (all-party) August registration
   (Nov 3 1908 reg was 75,388 after the fall registration push), i.e. numerator and denominator
   in that row are not even the same scope.

## Dead ends
- muni58 item fulltext search for "22,698", "22,117", "24,305", "30,647": zero matches despite indexed=true.
  Cause: the Aug 11 canvass page (leaf n1144) is printed landscape; OCR mangles rotated digits. Found via
  chronological adjacency instead (May 5 canvass p.1121 -> bond props p.1122-1124 -> Aug 11 canvass p.1125).
- muni59 (FY1909-10, server ia600908, path /20/items/...) fulltext for "22,698"/"24,178"/"33,331": zero matches.
  Its elections table (if present) is not OCR-findable by these strings; not needed for the verdict.
