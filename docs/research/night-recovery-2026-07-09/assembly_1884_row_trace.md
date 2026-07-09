# Assembly special 1884-03-18: cumulative-table row trace + official canvass hunt

Mission: (1) read the "Vote Polled" printed for the Mar 18, 1884 special Assembly
election row in the remaining SF Municipal Reports printings (vol49 FY1898-99,
vol53 FY1902-03, vol55 FY1904-05, vol57 FY1907-08); (2) find the official canvass
(Board of Supervisors declaration) candidate totals.

Known so far (from operator): 2,655 printed in vol47 FY1888-89, vol62 FY1912-13 p.260,
vol65 FY1915-16 pp.327+332. Daily Alta 1884-03-19 (DAC18840319.2.58.1) 41-precinct
count: Wallace 2,668 + Hawes 2,342 + Ellis 60 = 5,070.
Hypothesis: 2,655 = Wallace's canvassed (winner's) vote, not total ballots.

## Work log

### Identifiers (archive.org advancedsearch, query title:"San Francisco Municipal Reports")
- vol49 FY1898-99: sanfranciscomuni49sanfrich
- vol53 FY1902-03: sanfranciscomuni53sanfrich
- vol55 FY1904-05: sanfranciscomuni55sanfrich
- vol57 FY1907-08: sanfranciscomuni57sanfrich

Locating query per volume: item full-text API
`https://<server>/fulltext/inside.php?item_id=<id>&doc=<id>&path=<dir>&q=%222%2C655%22`
Hits: vol49 leaves 99+321; vol53 leaf 306; vol55 leaf 278; vol57 leaf 895.

### vol49 FY1898-99 (READ BY EYE): 2,655 CONFIRMED
Image: https://archive.org/download/sanfranciscomuni49sanfrich/page/n98 (printed p.55; leaf 99 match was bleed-through onto p.56)
Local: imgs/vol49_n98.jpg
Table title (verbatim): "TABLE SHOWING DATE OF ELECTION, THE NUMBER OF PRECINCTS, THE TOTAL OF EACH GENERAL REGISTRATION AND OF VOTES CAST AT EACH ELECTION UNDER THE 'ACT TO REGULATE THE REGISTRATION OF VOTERS AND SECURE THE PURITY OF ELECTIONS,' ETC., APPROVED MARCH 18, 1878."
Columns: DATE OF ELECTION | NUMBER OF PRECINCTS | REGISTRATION | TOTAL VOTE | (description)
Row (verbatim): "Mar. 18, 1884... [precincts blank dots] [registration blank dots] 2,655  Assemblyman."
Note: precincts and registration cells are BLANK for this row (dots), unlike neighbors (Mar 3 1883: 152 precincts, 18,764; Nov 4 1884: 164, 50,542, 47,535). Column header in this printing is "TOTAL VOTE".
Second hit leaf 321 not yet examined (likely Registrar duplicate table).

### vol53 FY1902-03 (READ BY EYE): 2,655 CONFIRMED
Image: https://archive.org/download/sanfranciscomuni53sanfrich/page/n305 (printed p.290; fulltext hit said leaf 306 = p.291 nativity table, real table is previous leaf)
Local: imgs/vol53_n305.jpg
Columns: Date of Election | Number of Precincts | Registration | Total Vote Polled | (description)
Row (verbatim): "March 18, 1884..... [precincts blank] [registration blank] 2,655  Assemblyman."

### vol55 FY1904-05 (READ BY EYE): 2,655 CONFIRMED
Image: https://archive.org/download/sanfranciscomuni55sanfrich/page/n277 (printed p.264; fulltext hit leaf 278 = p.265 nativity, table on previous leaf)
Local: imgs/vol55_n277.jpg
Row (verbatim): "March 18, 1884....... [blank] [blank] 2,655  Assemblyman"
Side observation: this printing gives Nov 3 1896 as 61,820 where other printings give 64,820 (typo in vol55; not our row).

### vol57 FY1907-08 (READ BY EYE): 2,655 CONFIRMED
Image: https://archive.org/download/sanfranciscomuni57sanfrich/page/n894 (printed p.871; fulltext hit leaf 895 = p.872 Nov 1907 candidate summary, table on previous leaf)
Local: imgs/vol57_n894.jpg
Columns: Date of Election | No. of Precincts | Registration | Vote Polled | (description)
Row (verbatim): "Mar. 18, 1884........... [blank] [blank] 2,655  Assemblyman."

LEG 1 RESULT: every checked printing (vol47, vol49, vol53, vol55, vol57, vol62, vol65)
prints 2,655 for the Mar 18, 1884 row, always with the precincts and registration
cells BLANK (the only such row in the table). The blankness of the other two cells
suggests the row was back-filled from a source that did not carry precinct/registration
figures, consistent with a candidate-total transplant.

## Leg 2: official canvass hunt

### FOUND: the official canvass, in the Municipal Reports FY1883-84 volume itself
Item: sanfranciscomuni83sanfrich (San Francisco Municipal Reports FY1883-84)
Locating query (copy-pasteable):
`curl "https://ia601603.us.archive.org/fulltext/inside.php?item_id=sanfranciscomuni83sanfrich&doc=sanfranciscomuni83sanfrich&path=/25/items/sanfranciscomuni83sanfrich&q=%22Wallace%22"`
(server/path from `https://archive.org/metadata/sanfranciscomuni83sanfrich`; hit at leaf 202 led to table on leaf 201)

Registrar's Report, printed pp.172-173:
- Table image (p.172): https://archive.org/download/sanfranciscomuni83sanfrich/page/n201 (local imgs/vol83_n201.jpg, total-row zoom imgs/vol83_n201_totalrow_full.png)
- Certificate image (p.173): https://archive.org/download/sanfranciscomuni83sanfrich/page/n202 (local imgs/vol83_n202.jpg)

Heading (verbatim, p.172): "THIRTEENTH SENATORIAL DISTRICT. Statement of votes
polled at a special election, held in the City and County of San Francisco, State
of California, on Tuesday, the 18th day of March, A. D. 1884, for member of
Assembly of the Thirteenth Senatorial District, to fill a vacancy:"

Table: 41 precincts (Sixth through Thirty-third Precinct, Eleventh Ward = 28 rows;
Twelfth through Twenty-fourth Precinct, Twelfth Ward = 13 rows). Columns:
W. T. Wallace | Horace Hawes | B. F. Ellis | Scattering | Total vote.

TOTAL ROW (read by eye, zoomed): Wallace 2,655 | Hawes 2,250 | Ellis 69 | Scattering 6 | Total vote 4,984.

Certificate (verbatim, pp.172-173): "STATE OF CALIFORNIA, CITY AND COUNTY OF SAN
FRANCISCO. ss. We hereby certify the foregoing to be a full, true and correct
statement of the vote polled in the Thirteenth Senatorial District, situated in
said City and County, polled at the special election held March 18, A. D. 1884,
for member of Assembly, to fill a vacancy. WASHINGTON BARTLETT, JOHN H. GRADY,
WILLIAM M. EDGAR, WILLIAM CRAIG, GEORGE H. ROGERS, Board of Election
Commissioners. Witness my hand and official seal, this 24th day of March, A. D.
1884. JAMES A. JOHNSON, Registrar of Voters, Ex-officio Secretary of Board of
Election Commissioners."

### CONCLUSION: hypothesis PROVEN
The cumulative table's 2,655 for Mar 18, 1884 is EXACTLY W. T. Wallace's official
canvassed vote, not the ballots polled. Official total ballots at the special were
4,984 (Wallace 2,655 + Hawes 2,250 + Ellis 69 + scattering 6). Whoever compiled the
cumulative table transplanted the winner's total into the "Vote Polled" column
(and had no precinct/registration figures to enter, hence the uniquely blank cells).

Official canvass vs Daily Alta 1884-03-19 (DAC18840319.2.58.1) press count:
- Wallace 2,655 official vs 2,668 press (-13)
- Hawes 2,250 official vs 2,342 press (-92)
- Ellis 69 official vs 60 press (+9)
- Scattering 6 official (press had none)
- Total 4,984 official vs 5,070 press (-86)
Both are 41-precinct counts (same precinct universe: 11th Ward pcts 6-33, 12th Ward pcts 12-24).

### Dead ends / not pursued
- vol84 FY1884-85 fulltext hit for "2,655" (leaf 759) is a Personal Property
  Assessment page (dollar amount), irrelevant. "Assemblyman" query returns zero
  hits in vol83 and vol84: the cumulative election table did not yet exist in
  those volumes.
- vol83 leaf 716 hit ("2,865 2,655 65,000 14,965") likewise assessment-roll
  context, not examined further.
- vol49 leaf 321 second "2,655" hit not examined (main table already read by eye
  at leaf 98); likely the duplicate printing of the same table elsewhere in the
  volume.
- CDNC Daily Alta Mar 20-31, 1884 "official count" search NOT RUN: unnecessary
  once the certified canvass itself was found in an official publication (better
  than newspaper corroboration).

