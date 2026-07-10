<!-- Agent research file, recovered 2026-07-08; the basis for data/sources/sf_turnout_reused_registration_1917_1945.csv.
     Era verdicts summarized in docs/analysis/public-search-log.md (2026-07-08 turnout denominator pass). -->

# California voter registration law history, 1866-1945 (SF focus)

Mission: verify/refute operator claim that registration was annual (per-year) around turn of century,
so same-year general-election registration can be reused as denominator for special elections 1921-1945.

Working hypotheses to test:
- 1866 Registry Act: first CA registration law.
- 1878 Act (Mar 18, 1878): "purity of elections" registration act.
- 1899/1911 era: Political Code precinct registration, possibly biennial ("great register" renewed every 2 years).
- Permanent registration: believed adopted ~1930-31 (verify exact statute/year).

Findings (append as you go):

## Finding 1: UCLA Luskin Center report "Reckoning with Our Rights" (Sept 2020): era overview
Retrieval: curl https://luskincenter.history.ucla.edu/wp-content/uploads/sites/66/2020/09/Reckoning-with-our-Rights-Report-September-2020.pdf
(saved as scratchpad/luskin_voter_access.pdf, text in luskin.txt; quotes from pp. 13-18)
Locating query: WebSearch "California permanent voter registration law 1930 adopted history \"permanent registration\""; then grep -n -i -E "1866|1878|1899|1911|biennial|permanent regist" luskin.txt

Verbatim quotes:
- "That burden has fallen on California voters since The Registry Act of 1866, which required a would-be voter to prove his eligibility to elections officials in order to be registered and thenceforth entitled to vote."
- "From 1873 until 1898 the law provided that once a person was registered, he remained registered, although the standards for identifying voters were tightened" (1895 detail: physical description, landlord tenant lists in big counties, Ch. CLXXXVI Stats. 1895)
- "Then in 1899 the law changed to require that every citizen re-register to vote every two years; that is, instead of being permanent, registration now had to be renewed for every election cycle." (footnote 45: "Chapter LIII, California Statutes of 1899.")
- "In 1930 another initiative measure eliminated biennial registration and returned the state to permanent registration of voters as had been the case prior to 1898." (footnote 52: "REGISTRATION OF VOTERS California Proposition 14 (1930). https://repository.uchastings.edu/ca_ballot_props/265")
- "This measure called for a new, complete registration of all voters beginning January 1, 1932. Registration would then be permanent unless the voter died, moved, or became ineligible to vote. However, beginning on the first of January in every odd-numbered year, clerks were required to cancel the registration of any voter who had not voted in either the primary or general election of the preceding year."
- Opponents (County Clerks Assn) "said the whole purpose of the biennial registration law of 1898 had been to defeat fraud"; supporters incl. chief elections officials of LA and SF: biennial registration "entails extravagance, inaccuracy, and is a nuisance".
- 1936 Prop 8 attempted repeal of permanent registration, defeated ("You like the Permanent Registration Law. Keep it as it is.").

Implications so far:
- 1866-1898: registration essentially permanent/cumulative (Great Register), NOT annual.
- 1899-1931: BIENNIAL re-registration (not annual). Operator's "valid for the year" claim is wrong in period detail but right in spirit (rolls wiped periodically, registrar re-registered everyone).
- Permanent registration: adopted by initiative Prop 14, Nov 4, 1930; new complete registration from Jan 1, 1932; biennial purge of non-voters every odd-year Jan 1.
TODO: confirm biennium boundaries under 1899 law (when was the roll wiped: Jan 1 of even years?); 1878 act details; 1911-era changes; SF Municipal Reports primary confirmation.

## Finding 2: Prop 14 (1930) summary, UC Law SF repository
Retrieval: WebFetch https://repository.uclawsf.edu/ca_ballot_props/265/ (redirect from repository.uchastings.edu/ca_ballot_props/265/)
Locating query: the Luskin report footnote 52 gives the repository URL.
- "Requires new state-wide registration of voters commencing January 1, 1932"
- "registration of any person not voting at last preceding August primary or November general election to be cancelled" every January 1 of odd-numbered years; notice mailed; must reregister.
- Passed Nov 4, 1930: 609,109 (57.7%) yes vs 447,371 no.

## Finding 3: PRIMARY STATUTE. Political Code sec. 1094 and 1121 (as amended to 1913), from "Election laws of the state of California, 1913-14"
Retrieval: curl https://archive.org/download/electionlawsofst00cali/electionlawsofst00cali_djvu.txt (saved as scratchpad/el1913.txt)
Locating query: grep -n -i -E "odd-numbered|even-numbered|cancel" el1913.txt ; sec 1094 at line ~10789, sec 1121 at ~11750.

Sec. 1094 verbatim (OCR, hyphenation joined):
"There shall be, in each even-numbered year, to continue for two years, except as hereinafter provided in each county and city and county of the State, a new and complete registration of the voters of such county or city and county, who are entitled thereto. Such registration shall begin on the first day of January of such years, and shall be in progress at all times except during the thirty days immediately preceding any election, when it shall cease for such election ... provided, that where any general or special municipal election, or any other special election, is held between the first day in January and the first day in April of the year in which such a new registration is had, the original affidavit of registration and indexes used in the last general State election ... may be used, together with the original affidavit of registration since the last election, and supplemental indexes, showing all additional registration, changes and corrections made since the registration for the last general election, completed to and including the thirtieth day prior to said general or special municipal election or other special election, which shall be the last day on which any person may register or transfer registration so as to entitle said person to a vote at such election."

Sec. 1121 verbatim (register used at special/municipal elections, i.e. sec 1044 elections):
"The register used at each special election or consolidated election precinct, at the elections provided for in Section 1044 of this Code; provided, such elections are not held between the first day in April and the date of the general state election in any even-numbered year, shall consist of the original affidavits of registration for the territory ... at the last general State election immediately preceding the holding of the election ... together with a supplement or supplements showing the additional names of the persons who by registration have since such general State election become entitled to vote ... If any election provided for in section 1044 of this code is held between the first day in April and the date of the general state election in any even-numbered year, the register used ... shall consist of the original affidavits of registration of those who had registered ... in said even-numbered year and at least thirty days prior to such election. [Amendment approved June 13, 1913.]"

Sec. 1106 subdivision 8 area (line ~11548): registrar cancels affidavits of convicted embezzlers "during the first week of September in each year" [new section approved May 1, 1911]. (Minor annual maintenance, not a roll wipe.)

Implication: 1899-1931 regime = BIENNIAL total re-registration starting Jan 1 of even years; roll then accretes continuously for two years, closing 30 days before each election. Specials/municipals use the last-general-election register PLUS a supplement of later registrants (except Apr-Nov of even years: new even-year roll only). So the register at a special is close to, but not identical to, the last general's count: it is last-general + accretions - (minor cancellations).

## Finding 4: PRIMARY STATUTE. The March 18, 1878 SF Registration Act (Chap. CCLII, Stats. 1877-78), Section 16
Retrieval: curl https://archive.org/download/extractsfromunit1890sanf/extractsfromunit1890sanf_djvu.txt (saved as scratchpad/sf1890.txt; act text starts ~line 1400; sec 16 ~line 1655)
Item: "Extracts from the United States Statutes and from the Constitution of the State of California, and the Registration Act..." (San Francisco, 1890), archive.org id extractsfromunit1890sanf.
Locating query: grep -n -i "1878" sf1890.txt then read around line 1414.

Sec. 15: registration in SF done by PRECINCT registers (Great Register/ward registers no longer applicable to SF); "no person shall vote at any election except he be legally registered upon the precinct register".
Sec. 16 VERBATIM (the smoking gun for the operator claim):
"The registration of electors in the precinct registers in the city and county of San Francisco, shall take place previous to each general State election as herein provided, and an elector properly enrolled therein, without being again enrolled, may vote at the general election ensuing his registration and at all special elections between said general election and the next general election, but not afterwards until re-registered according to law."

So in SF from 1878: re-registration before EACH GENERAL STATE ELECTION (biennial cadence after the 1879 constitution moved state generals to even years), and that registration expressly carried over to ALL SPECIAL ELECTIONS until the next general. Corroborated by Keyssar-derived secondary: "In San Francisco, beginning in 1878, voters had to register in person, in their precinct, before every general election." (Voter Registration: A Very Short History, Institute for Responsive Government, June 2022, p.~4, quoting Keyssar, The Right to Vote, pp.152-7; retrieval: curl https://responsivegov.org/wp-content/uploads/2022/06/Voter-Registration-A-Very-Short-History.pdf, grep "San Francisco" veryshort.txt line 95.)

Note: Luskin's "From 1873 until 1898 ... once a person was registered, he remained registered" describes the STATEWIDE Great Register regime; SF was carved out by this 1878 special act with periodic (per-general-election) re-registration. The 1899 Ch. LIII act made the biennial re-registration scheme statewide (new registration each even year, Political Code sec 1094).

## Finding 5: sec 1094 amendment trail
el1913.txt shows sec 1094 "[Amendment approved June 16, 1913.]"; the biennial new-registration scheme itself dates to Ch. LIII Stats. 1899 (per Luskin fn 45). SF-specific detail in 1913 text: in a city and county with >85,000 registration at last presidential election (i.e. SF), field registration allowed by assembly district at least 5 days before close of registration for the September primary.

## Finding 6: PRIMARY DATA. SF Municipal Reports FY1912-13, Dept of Elections cumulative table, printed pp. 260-262
Item: archive.org munisanfrancisco62sanfrich, printed p.259 = leaf 277 (found via fulltext API match "Special Elections--December" -> page 277).
Retrieval (copy-pasteable):
  curl "https://ia803104.us.archive.org/fulltext/inside.php?item_id=munisanfrancisco62sanfrich&doc=munisanfrancisco62sanfrich&path=/7/items/munisanfrancisco62sanfrich&q=%22Special+Elections%E2%80%94December%22"
  curl -o muni62_leaf278.jpg "https://iiif.archive.org/iiif/munisanfrancisco62sanfrich\$278/full/max/0/default.jpg"  (printed p.260; leaves 279, 280 = pp.261, 262)
Images read by model vision; saved at scratchpad/muni62_leaf278.jpg, 279, 280.

Table title verbatim: "TABLE Showing date of Election, Number of Precincts, the total of each Registration and of votes cast at each Election since the adoption of the 'Act to Regulate the Registration of Voters and Secure the Purity of Elections,' approved March 18, 1878."

Key rows (date / precincts / registration / vote polled / type):
1878-1896 era: registration figures appear ONLY at general state elections; municipal/special rows have BLANK registration (they used the standing roll per sec 16 of the 1878 act):
  Sept 3, 1879 General 44,764/41,575; Nov 2, 1880 Gen-Pres 43,775/41,292; Sept 7, 1881 Municipal (blank)/33,216; Nov 7, 1882 General 42,135/39,102; Apr 12, 1887 Amendment+Charter (blank)/25,959; Nov 6, 1888 58,549; Nov 4, 1890 59,770; Nov 8, 1892 67,849; Nov 6, 1894 68,039; Nov 3, 1896 72,992.
From 1897 every election row carries its own registration figure (continuous accretion):
  Dec 27, 1897 Freeholders 72,782; May 26, 1898 Charter 73,140; Nov 8, 1898 General 62,965 (NEW smaller roll from the 1898 re-registration); Aug 8, 1899 Primary 62,410; Nov 7, 1899 Municipal 71,786; Dec 27, 1899 Bond Parks 70,681; Dec 29, 1899 Bond Sewers 70,726; Nov 6, 1900 Gen-Pres 73,633; Aug 13, 1901 Primary 76,192.
p.261 rows:
  Nov 5, 1901 Municipal 77,890/53,746; Aug 12, 1902 Primary 51,726 (mid re-registration); Nov 4, 1902 General-Gubernatorial 70,716/61,091; Dec 2, 1902 Bond Geary St RR 70,764/26,612 (+48 vs the general); Dec 4, 1902 Charter Amendments (blank)/14,371;
  Aug 11, 1903 Primary 73,280; Sept 29, 1903 Bonds 73,540; Oct 8, 1903 Bonds 73,702; Nov 3, 1903 Municipal 79,684 (same-year accretion Aug->Nov = +8.7%);
  May 3, 1904 Primary 32,721 (new roll forming); Aug 9, 1904 50,708; Nov 8, 1904 Gen-Pres 81,576;
  Nov 7, 1905 Municipal 97,670; Aug 14, 1906 Primary 22,026 (post-earthquake); Nov 6, 1906 General 51,633; Aug 13, 1907 Primary 60,469; Nov 5, 1907 Municipal 77,601;
  May 5, 1908 Primary 36,564; Aug 11, 1908 Primary 55,437; Nov 3, 1908 Gen-Pres 75,388; Nov 12, 1908 Bond Water 75,467 (+79 in 9 days);
  June 22, 1909 Bond Schools 75,679/24,058; June 24, 1909 Bond Geary St RR 75,808/22,272 (+129 in 2 days: CONFIRMS the accretion pattern flagged in the mission);
  Aug 17, 1909 Primary 84,571; Nov 2, 1909 Municipal 90,790; Dec 30, 1909 Bond 90,957 (+167 vs Nov); Jan 14, 1910 Bond Spring Valley 91,026 (odd-year roll still in use in Jan of even year);
  Aug 16, 1910 Primary 67,513 (new roll); Nov 8, 1910 General 75,828; Nov 15, 1910 Charter Amendments 75,828 (IDENTICAL to the general a week earlier).
p.262 rows:
  Oct 10, 1911 Const Amendments 101,894; Nov 7, 1911 General Municipal 102,196; March 28, 1912(+) Civic Center Bonds 115,427; March 29, 1912(+) Home Telephone 115,445; May 14, 1912(+) Presidential Primary 136,490; Sept 3, 1912 State Primary 119,933; Nov 5, 1912 General-Presidential 134,701; Dec 10, 1912 Charter Amendments 136,914; Dec 20, 1912 Bonds 136,914 (identical to Dec 10); April 22, 1913 Recall-Init-Ref 137,718.
  Footnote verbatim: "(+) Includes Carried-over Registration of 1911." (the Jan-Apr even-year proviso of Pol. Code sec 1094 in action; also note women enfranchised Oct 1911 roughly doubled rolls by Nov 1912.)

What the pattern implies:
- Registration was NOT a fixed annual number. It was a roll that was wiped and rebuilt every even year (1898 on; per-general re-registration in SF 1878-1898) and then grew continuously, closing 30 days before each election; each election's "registration" is the roll size at ITS OWN 30-day close.
- Specials held AFTER the year's general: registration within ~0.1-1.6% of the general figure (Dec 1902 +0.07%; Nov 12 1908 +0.10%; Dec 1909 +0.18%; Dec 1912 +1.64%; Nov 15 1910 identical).
- Specials held BEFORE the year's general in the same year: general figure can overstate the roll by several percent (Aug->Nov 1903 +8.7%; Jun 1909 75.7k vs Nov 1909 90.8k = general +19.9%; Sept->Nov 1912 +12.3%), because of registration drives ahead of the general.
- Specials in Jan-Mar of even years used the PRIOR year's carried-over roll, not that year's general registration.

## Finding 7: 1919 compilation, Pol. Code sec 1094 (biennial regime through the 1920s)
Retrieval: curl https://archive.org/download/electionlawsofst00cali_0/electionlawsofst00cali_0_djvu.txt (saved as el1919.txt, line ~9915)
Verbatim: "1094. There shall be, commencing January 1, 1918 and every two years thereafter, except as hereinafter provided in each county and city and county of the State, a new and complete registration of the voters ... Such registration shall be in progress at all times except during the thirty days immediately preceding any election ... All affidavits of registration made prior to the first day of January of any even-numbered year shall be deemed canceled upon said day except for the sole purpose of being used as herein before stated at elections held thereafter and before the first day of April of that year, and shall on said last mentioned day, be deemed canceled for all purposes."
The Prop 14 (1930) ballot fight confirms this biennial system was still the law in 1930 (supporters/opponents both describe it as current law). So biennial regime ran 1900 through 1931 inclusive; the 1931 SF municipal election still used the biennial roll (new roll of Jan 1, 1930 + accretion).

## Finding 8: corroborations and dead ends
- FamilySearch wiki (California Great Registers): "The Political Code of 1899 included a new amendment that obligated counties to make new registrations on each even numbered year." Locating query: WebSearch "\"Statutes of 1899\" California registration ... great register \"every two years\""; URL https://www.familysearch.org/en/wiki/California_Great_Registers_-_FamilySearch_Historical_Records
- CA SoS Historical Voter Registration and Participation 1910-2020 (curl https://elections.cdn.sos.ca.gov/sov/2020-general/sov/04-historical-voter-reg-participation.pdf): statewide registration totals begin Nov 1912; party breakdowns begin 1922. No legal narrative.
- SF Dept of Elections FY1912-13 expense lines (muni62 leaf 277 / printed p.259): "District Registration 6,539.17" and (p.242 leaf) "Extra Clerks — Office Registration $40,000 / Extra Clerks — District Registration $8,200": primary evidence of the field/district registration drives (the operator's "registrar going around registering people").
DEAD ENDS:
- repository.uclawsf.edu viewcontent.cgi (Prop 14 full-text PDF) serves a JS bot-wall to curl (HTML with adobedtm), both plain and with referer/cookies. The landing page HTML (fetched fine via WebFetch) carries the official summary; full scanned text not retrieved.
- sciencedirect.com/science/article/pii/S0261379420301426 (Kousser-adjacent turnout paper): 403 to WebFetch. Its claim about SF 1878 is covered by the responsivegov.org PDF (quoting Keyssar, The Right to Vote, pp.152-157) and by the primary act text itself.
- WebFetch blocked (403) on cschs.org and loc.gov resource pages; curl worked for cschs.org. CSCHS Fall 2024 piece is Part II (post-1960) and adds the detail that the 1930-law purge was relaxed in 1959 and later; not needed for 1878-1945.
- archive.org advancedsearch for a 1930 CA ballot pamphlet: no hits.

## SYNTHESIS (verdicts)
Empirical deltas from the SF cumulative table (registration at special vs same-year/nearest general):
- After the general, same roll: Dec 2 1902 +0.07%; Nov 12 1908 +0.10%; Nov 15 1910 +0.00%; Dec 30 1909 +0.18%; Jan 14 1910 +0.26%; Dec 10/20 1912 +1.64%; Apr 22 1913 +2.24% (vs Nov 1912).
- Before the general, same year: Aug 1903 vs Nov 1903 general is -8.0% (79,684 overstates the Aug roll by 8.7%); Jun 22 1909 vs Nov 1909: Nov figure overstates by 20.0%; Aug 1909 by 7.4%; Sept 1912 by 12.3% (confounded by women's enfranchisement Oct 1911 and precinct growth).
Era verdicts: see final report. Permanent registration: adopted by initiative Prop 14 on Nov 4, 1930 (609,109 to 447,371); operative via a new complete statewide registration commencing Jan 1, 1932; biennial purge (Jan 1, odd years) of those not voting in the preceding August primary or November general.
