# Machine check of election-night sources

Presence checks of each claimed number against its cited URL.
Denominators are checked against the canonical per-year SoS
'Voter Participation Statistics by County' PDF even where a row cites
the complete-SOV PDF (same statistic). Fetched artifacts live in
`data/research/election-night/cache/` (gitignored; rerun the
verify_en_* scripts to regenerate).

| County | Date | Check | Claimed | Status | Evidence (context around match) |
|---|---|---|---:|---|---|
| fresno-ca | 2012-11-06 | denominator | 261,652 | VERIFIED | 611 559,268 410,188 119,543 142,109 261,652 54.31% 63.79% 46.78% |
| fresno-ca | 2014-11-04 | denominator | 163,420 | VERIFIED | 577 572,045 416,433 64,901 98,519 163,420 60.29% 39.24% 28.57% |
| fresno-ca | 2016-11-08 | denominator | 291,890 | VERIFIED | 592 583,238 437,423 131,787 160,103 291,890 54.85% 66.73% 50.05% |
| fresno-ca | 2016-11-08 | numerator | 177,183 | VERIFIED | es." 11/9/2016 1:42:19 AM Registered Voters 437667 - Cards Cast 177183 40.48% Num. Report Precinct 592 - Num. Reporting  |
| fresno-ca | 2018-11-06 | denominator | 256,972 | VERIFIED | 640 597,497 456,891 93,581 163,391 256,972 63.58% 56.24% 43.01% |
| fresno-ca | 2022-11-08 | denominator | 221,419 | VERIFIED | 562 642,412 500,076 28,343 193,076 221,419 87.20% 44.28% 34.47% |
| fresno-ca | 2024-11-05 | denominator | 330,932 | VERIFIED | 478 649,184 513,799 63,049 267,883 330,932 80.95% 64.41% 50.98% |
| fresno-ca | 2024-11-05 | numerator | 206,372 | VERIFIED | FICIAL ELECTION RESULTS Precincts Reported: 478 of 478 (100.00%) Voters Cast: 206,372 of 511,349 (40.36%) President and  |
| los-angeles-ca | 2012-11-06 | denominator | 3,236,704 | VERIFIED | eles 4,993 5,976,156 4,758,437 2,260,876 975,828 3,236,704 30.15% 68.02% 54.16% |
| los-angeles-ca | 2012-11-06 | numerator | 2,368,283 | VERIFIED | d ballots with votes for write-in candidates. On Election Night a total of 2,368,283 ballots were counted. This included |
| los-angeles-ca | 2014-11-04 | denominator | 1,518,835 | VERIFIED | geles 5,027 6,096,320 4,897,915 941,812 577,023 1,518,835 37.99% 31.01% 24.91% |
| los-angeles-ca | 2014-11-04 | numerator | 1,147,248 | VERIFIED | d semi-final official results for the Nov. 4, 2014 General Election. A total of 1,147,248 ballots were processed and cou |
| los-angeles-ca | 2016-11-08 | denominator | 3,544,115 | VERIFIED | ngeles 4,988 6,222,266 5,253,427 2,260,467 1,283,648 3,544,115 36.22% 67.46% 56.96% |
| los-angeles-ca | 2016-11-08 | numerator | 2,306,321 | VERIFIED | unced semi-final official results for the Nov. 8th General Election. A total of 2,306,321 ballots were processed and cou |
| los-angeles-ca | 2018-11-06 | denominator | 3,023,417 | VERIFIED | 4,728 6,230,147 5,280,658 1,673,104 1,350,313 3,023,417 44.66% 57.25% 48.53% |
| los-angeles-ca | 2018-11-06 | numerator | 1,975,855 | VERIFIED | announced semi-official results for the November 6 General Election. A total of 1,975,855 ballots were processed and cou |
| los-angeles-ca | 2022-11-08 | denominator | 2,456,701 | VERIFIED | 3,680 6,658,099 5,601,835 487,368 1,969,333 2,456,701 80.16% 43.86% 36.90% |
| los-angeles-ca | 2022-11-08 | numerator | 1,318,093 | VERIFIED | . Logan announced semi-final results for the 2022 General Election. A total of 1,318,093 ballots were processed and coun |
| los-angeles-ca | 2024-11-05 | denominator | 3,793,106 | VERIFIED | 3,087 6,657,487 5,745,214 1,060,354 2,732,752 3,793,106 72.05% 66.02% 56.98% |
| los-angeles-ca | 2024-11-05 | numerator | 2,615,541 | VERIFIED | d the semi-final results for the November 5, 2024 General Election. A total of 2,615,541 ballots were processed and coun |
| madera-ca | 2012-11-06 | denominator | 40,325 | VERIFIED | 96 86,894 53,779 15,658 24,667 40,325 61.17% 74.98% 46.41% |
| madera-ca | 2014-11-04 | denominator | 27,370 | VERIFIED | 100 85,976 52,494 8,970 18,400 27,370 67.23% 52.14% 31.83% |
| madera-ca | 2016-11-08 | denominator | 44,186 | VERIFIED | 102 87,254 58,086 15,211 28,975 44,186 65.58% 76.07% 50.64% |
| madera-ca | 2016-11-08 | numerator | 35,364 | VERIFIED | Absentee Ballots Cast 22,561 38.8% Total Ballots Cast 35,364 60.8% President and Vice President Completed Prec |
| madera-ca | 2018-11-06 | denominator | 38,968 | VERIFIED | 69 89,818 57,418 4,434 34,534 38,968 88.62% 67.87% 43.39% |
| madera-ca | 2018-11-06 | numerator | 28,159 | VERIFIED | 0 , "BCxContest" : 0 , "VF" : 1 , "TP" : 69 , "PR" : 62 , "TV" : 31713 , "BC" : 28159 , "RC" : 0 , "RO" : 0 , "CH" : [ " |
| madera-ca | 2022-11-08 | denominator | 37,345 | VERIFIED | 59 93,789 72,865 3,333 34,012 37,345 91.08% 51.25% 39.82% |
| madera-ca | 2022-11-08 | numerator | 21,951 | VERIFIED | 0 , "BCxContest" : 0 , "VF" : 1 , "TP" : 59 , "PR" : 50 , "TV" : 72232 , "BC" : 21951 , "RC" : 0 , "RO" : 0 , "CH" : [ " |
| madera-ca | 2024-11-05 | denominator | 55,329 | VERIFIED | 78 95,290 78,204 8,560 46,769 55,329 84.53% 70.75% 58.06% |
| madera-ca | 2024-11-05 | numerator | 37,106 | VERIFIED | 0 , "BCxContest" : 0 , "VF" : 1 , "TP" : 78 , "PR" : 63 , "TV" : 78317 , "BC" : 37106 , "RC" : 0 , "RO" : 0 , "CH" : [ " |
| napa-ca | 2012-11-06 | denominator | 57,672 | VERIFIED | 167 91,138 72,592 6,251 51,421 57,672 89.16% 79.45% 63.28% |
| napa-ca | 2012-11-06 | numerator | 32,715 | VERIFIED | Election Day Turnout 5,869 8.08% Total 32,715 45.07% PRESIDENT AND VICE PRESIDENT |
| napa-ca | 2014-11-04 | denominator | 38,766 | VERIFIED | 167 91,531 70,493 2,397 36,369 38,766 93.82% 54.99% 42.35% |
| napa-ca | 2014-11-04 | numerator | 18,286 | VERIFIED | % Election Day Turnout 945 1.34% Total 18,286 25.94% Governor 0/164 0.00% |
| napa-ca | 2016-11-08 | denominator | 63,255 | VERIFIED | 167 93,686 76,833 4,530 58,725 63,255 92.84% 82.33% 67.52% |
| napa-ca | 2016-11-08 | numerator | 34,108 | VERIFIED | November 8, 2016 Precincts Reported: 167 of 167 (100.00%) Ballots Cast: 34,108 PRESIDENT/VICE PRESIDENT (Vote for 1) Pre |
| napa-ca | 2018-11-06 | denominator | 57,132 | VERIFIED | 170 92,369 78,135 42 57,090 57,132 99.93% 73.12% 61.85% |
| napa-ca | 2018-11-06 | numerator | 21,774 | VERIFIED | ION NIGHT REPORT Precincts Reported: 170 of 170 (100.00%) Registered Voters: 21,774 of 78,135 (27.87%) Ballots Cast: 43, |
| napa-ca | 2022-11-08 | denominator | 50,788 | VERIFIED | 200 97,321 83,480 1,563 49,225 50,788 96.92% 60.84% 52.19% |
| napa-ca | 2022-11-08 | numerator | 21,943 | VERIFIED | 24.43% Total 21,943 83,471 26.29% Precincts Reported: 200 of 200 (100.00 |
| napa-ca | 2024-11-05 | denominator | 66,634 | VERIFIED | 204 97,259 85,045 4,851 61,783 66,634 92.72% 78.35% 68.51% |
| napa-ca | 2024-11-05 | numerator | 26,160 | VERIFIED | l Election Night Report Precincts Reported: 204 of 204 (100.00%) Voters Cast: 26,160 of 85,150 (30.72%) President and Vi |
| nevada-ca | 2012-11-06 | denominator | 52,173 | VERIFIED | 140 76,187 62,853 13,798 38,375 52,173 73.55% 83.01% 68.48% |
| nevada-ca | 2012-11-06 | numerator | 31,275 | VERIFIED | re than 18,000 unprocessed ballots to add to the county's election-day tally of 31,275. "It takes time because more than |
| nevada-ca | 2014-11-04 | denominator | 39,629 | VERIFIED | 84 76,731 61,690 9,383 30,246 39,629 76.32% 64.24% 51.65% |
| nevada-ca | 2014-11-04 | numerator | 22,366 | VERIFIED | , Calif. November 5, 2014 - The final election night tally of votes comes in at 22,366 of 61,706 - a rather low voter tu |
| nevada-ca | 2016-11-08 | denominator | 56,800 | VERIFIED | 82 77,443 68,829 12,543 44,257 56,800 77.92% 82.52% 73.34% |
| nevada-ca | 2016-11-08 | numerator | 34,728 | VERIFIED | asure A – Library system Measure A received 23,060 Yes votes, 68.99% of the 34,728 ballots counted as of tonight. Early  |
| nevada-ca | 2018-11-06 | denominator | 54,996 | VERIFIED | 68 78,603 68,954 3,059 51,937 54,996 94.44% 79.76% 69.97% |
| nevada-ca | 2018-11-06 | numerator | 26,956 | VERIFIED | NEVADA CITY, Calif. November 7, 2018 – At the end of election night, 26,956 ballots have been counted in Nevada County,  |
| nevada-ca | 2022-11-08 | denominator | 51,370 | VERIFIED | 136 81,891 74,488 3,949 47,421 51,370 92.31% 68.96% 62.73% |
| nevada-ca | 2022-11-08 | numerator | 28,824 | VERIFIED | sued to registered Nevada County voters. Last night, 38.83% of those ballots – 28,824 were counted . The first results o |
| nevada-ca | 2024-11-05 | denominator | 63,240 | VERIFIED | 118 81,096 75,654 8,047 55,193 63,240 87.28% 83.59% 77.98% |
| nevada-ca | 2024-11-05 | numerator | 15,486 | VERIFIED | tal Percent Ballots Registered Percent 118 118 100.00% 15,486 75,881 20.41% Choice Part |
| orange-ca | 2012-11-06 | denominator | 1,133,204 | VERIFIED | 1,977 1,925,205 1,683,001 552,018 581,186 1,133,204 51.29% 67.33% 58.86% |
| orange-ca | 2012-11-06 | numerator | 862,544 | VERIFIED | 399,220 23.72% Total Ballots Cast 862,544 51.25% Complete Precincts: 184 of 184 |
| orange-ca | 2014-11-04 | denominator | 640,358 | VERIFIED | 1,863 1,963,747 1,424,216 252,472 387,886 640,358 60.57% 44.96% 32.61% |
| orange-ca | 2014-11-04 | numerator | 464,313 | VERIFIED | 252,171 17.71% Total Ballots Cast 464,313 32.60% Complete Precincts: 1,863 of 1,863 |
| orange-ca | 2016-11-08 | denominator | 1,239,405 | VERIFIED | e 1,668 2,009,188 1,535,691 516,801 722,604 1,239,405 58.30% 80.71% 61.69% |
| orange-ca | 2016-11-08 | numerator | 825,317 | VERIFIED | 431,038 28.06% Total Ballots Cast 825,317 53.73% Complete Precincts: 168 of 168 |
| orange-ca | 2018-11-06 | denominator | 1,106,729 | VERIFIED | 1,546 2,028,366 1,560,111 393,423 713,306 1,106,729 64.45% 70.94% 54.56% |
| orange-ca | 2018-11-06 | numerator | 650,671 | VERIFIED | 366,447 23.51% Total Ballots Cast 650,671 41.74% Complete Precincts: 1,546 of 1,546 |
| orange-ca | 2022-11-08 | denominator | 994,277 | VERIFIED | 2,169 2,203,252 1,817,583 164,115 830,162 994,277 83.49% 54.70% 45.13% |
| orange-ca | 2022-11-08 | numerator | 611,060 | VERIFIED | tal Percent Ballots Registered Percent 2,169 2,169 100.00% 611,060 1,817,149 33.63% Choice Party |
| orange-ca | 2024-11-05 | denominator | 1,417,397 | VERIFIED | 2,294 2,203,227 1,862,010 323,223 1,094,174 1,417,397 77.20% 76.12% 64.33% |
| orange-ca | 2024-11-05 | numerator | 1,007,150 | VERIFIED | al Percent Ballots Registered Percent 2,294 2,294 100.00% 1,007,150 1,861,450 54.11% Choice Party |
| placer-ca | 2012-11-06 | denominator | 172,757 | VERIFIED | 350 251,135 208,604 57,171 115,586 172,757 66.91% 82.82% 68.79% |
| placer-ca | 2014-11-04 | denominator | 115,547 | VERIFIED | 368 259,591 200,422 31,546 84,001 115,547 72.70% 57.65% 44.51% |
| placer-ca | 2014-11-04 | numerator | 76,411 | VERIFIED | 05/14 00:36:57 Registered Voters 200402 - Cards Cast 76411 38.13% Num. Report Precinct 369 - Num. Reporting 369 100.00% |
| placer-ca | 2016-11-08 | denominator | 190,550 | VERIFIED | 363 264,101 226,249 58,385 132,165 190,550 69.36% 84.22% 72.15% |
| placer-ca | 2016-11-08 | numerator | 109,666 | VERIFIED | 09/16 00:29:40 Registered Voters 226454 - Cards Cast 109666 48.43% Num. Report Precinct 363 - Num. Reporting 363 100.00% |
| placer-ca | 2018-11-06 | denominator | 177,725 | VERIFIED | 358 276,613 234,732 46,896 130,829 177,725 73.61% 75.71% 64.25% |
| placer-ca | 2018-11-06 | numerator | 113,380 | VERIFIED | 11/09/18 15:15:00 Registered Voters 231461 – Cards Cast 113380 48.98% Num. Report Precinct 358 – Num. Reporting 358 100. |
| placer-ca | 2022-11-08 | denominator | 184,507 | VERIFIED | 408 301,467 279,016 25,494 159,013 184,507 86.18% 66.13% 61.20% |
| placer-ca | 2024-11-05 | denominator | 239,402 | VERIFIED | 331 305,381 291,479 56,964 182,438 239,402 76.21% 82.13% 78.39% |
| riverside-ca | 2012-11-06 | denominator | 669,627 | VERIFIED | 1,218 1,358,695 943,405 298,112 371,515 669,627 55.48% 70.98% 49.28% |
| riverside-ca | 2014-11-04 | denominator | 357,764 | VERIFIED | e 1,193 1,394,302 891,575 124,829 232,935 357,764 65.11% 40.13% 25.66% |
| riverside-ca | 2016-11-08 | denominator | 769,193 | VERIFIED | de 1,126 1,438,117 1,019,130 264,638 504,555 769,193 65.60% 75.48% 53.49% |
| riverside-ca | 2018-11-06 | denominator | 650,545 | VERIFIED | 1,072 1,481,361 1,035,957 194,606 455,939 650,545 70.09% 62.80% 43.92% |
| riverside-ca | 2022-11-08 | denominator | 604,617 | VERIFIED | 1,265 1,637,165 1,310,505 59,812 544,805 604,617 90.11% 46.14% 36.93% |
| riverside-ca | 2022-11-08 | numerator | 205,813 | VERIFIED | orted: 1,265 of 1,265 ( 100.00% ) Voters Cast: 205,813 of 1,310,928 ( 15.70% ) Governor |
| riverside-ca | 2024-11-05 | denominator | 959,098 | VERIFIED | 1,345 1,646,951 1,372,548 170,437 788,661 959,098 82.23% 69.88% 58.23% |
| riverside-ca | 2024-11-05 | numerator | 611,101 | VERIFIED | taArray, colorObject, elem); })(); Ballots Counted 611,101 Vote by Mail 483,778 Mail Ballot Precinc |
| sacramento-ca | 2012-11-06 | denominator | 522,045 | VERIFIED | 1,106 944,243 698,899 216,021 306,024 522,045 58.62% 74.70% 55.29% |
| sacramento-ca | 2012-11-06 | numerator | 328,516 | VERIFIED | L . . . . . 698,899 BALLOTS CAST - TOTAL. . . . . . . 328,516 VOTER TURNOUT - TOTAL . . . . . . 47.00 |
| sacramento-ca | 2014-11-04 | denominator | 330,817 | VERIFIED | to 1,263 961,112 683,632 111,628 219,189 330,817 66.26% 48.39% 34.42% |
| sacramento-ca | 2014-11-04 | numerator | 195,317 | VERIFIED | L . . . . . 683,632 BALLOTS CAST - TOTAL. . . . . . . 195,317 VOTER TURNOUT - TOTAL . . . . . . 28.57 |
| sacramento-ca | 2016-11-08 | denominator | 575,711 | VERIFIED | nto 1,267 989,090 772,865 203,114 372,597 575,711 64.72% 74.49% 58.21% |
| sacramento-ca | 2018-11-06 | denominator | 522,652 | VERIFIED | 593 1,013,368 765,965 30,279 492,373 522,652 94.21% 68.23% 51.58% |
| sacramento-ca | 2018-11-06 | numerator | 185,623 | VERIFIED | ( 100.00% ) Registered Voters: 185,623 of 764,998 ( 24.26% ) Ball |
| sacramento-ca | 2022-11-08 | denominator | 484,315 | VERIFIED | 685 1,112,665 865,225 28,929 455,386 484,315 94.03% 55.98% 43.53% |
| sacramento-ca | 2022-11-08 | numerator | 145,015 | VERIFIED | I-FINAL Voters Cast: 145,015 of 864,814 ( 16.77% ) Governo |
| sacramento-ca | 2024-11-05 | denominator | 668,416 | VERIFIED | 686 1,116,853 889,806 73,650 594,766 668,416 88.98% 75.12% 59.85% |
| sacramento-ca | 2024-11-05 | numerator | 311,821 | VERIFIED | I-FINAL Voters Cast: 311,821 of 889,465 ( 35.06% ) Preside |
| san-bernardino-ca | 2012-11-06 | denominator | 589,611 | VERIFIED | dino 1,609 1,259,676 851,581 306,324 283,287 589,611 48.05% 69.24% 46.81% |
| san-bernardino-ca | 2014-11-04 | denominator | 293,283 | VERIFIED | ardino 1,737 1,273,684 851,684 117,179 176,104 293,283 60.05% 34.44% 23.03% |
| san-bernardino-ca | 2016-11-08 | denominator | 672,871 | VERIFIED | nardino 1,789 1,308,522 888,019 287,315 385,556 672,871 57.30% 75.77% 51.42% |
| san-bernardino-ca | 2018-11-06 | denominator | 546,041 | VERIFIED | 2,209 1,330,247 937,316 209,168 336,873 546,041 61.69% 58.26% 41.05% |
| san-bernardino-ca | 2022-11-08 | denominator | 458,946 | VERIFIED | 2,765 1,472,696 1,138,818 66,469 392,477 458,946 85.52% 40.30% 31.16% |
| san-bernardino-ca | 2024-11-05 | denominator | 771,834 | VERIFIED | 2,872 1,472,596 1,197,953 154,974 616,860 771,834 79.92% 64.43% 52.41% |
| san-bernardino-ca | 2024-11-05 | numerator | 434,108 | VERIFIED | render-verified: Precincts Reported: 2,872 of 2,872 (100.00%) Voters Cast: 434,108 of 1,198,556 (36.22%) Cards Cast: 1,2 |
| san-diego-ca | 2012-11-06 | denominator | 1,203,265 | VERIFIED | go 2,064 2,094,093 1,563,093 528,258 675,007 1,203,265 56.10% 76.98% 57.46% |
| san-diego-ca | 2014-11-04 | denominator | 692,434 | VERIFIED | o 2,001 2,135,863 1,546,924 242,638 449,796 692,434 64.96% 44.76% 32.42% |
| san-diego-ca | 2016-11-08 | denominator | 1,346,513 | VERIFIED | iego 2,175 2,191,191 1,652,570 489,576 856,937 1,346,513 63.64% 81.48% 61.45% |
| san-diego-ca | 2018-11-06 | denominator | 1,173,924 | VERIFIED | 2,136 2,224,081 1,741,707 369,655 804,269 1,173,924 68.51% 67.40% 52.78% |
| san-diego-ca | 2018-11-06 | numerator | 536,734 | VERIFIED | (dataArray, colorObject, elem); })(); Ballots Cast 536,734 Registered Voters 1,767,300 |
| san-diego-ca | 2022-11-08 | denominator | 1,043,490 | VERIFIED | 2,718 2,349,554 1,924,634 104,388 939,102 1,043,490 90.00% 54.22% 44.41% |
| san-diego-ca | 2022-11-08 | numerator | 565,982 | VERIFIED | (dataArray, colorObject, elem); })(); Ballots Cast 565,982 Mail Ballots 468,632 Vote Center Ballots |
| san-diego-ca | 2024-11-05 | denominator | 1,503,018 | VERIFIED | 2,669 2,353,145 1,982,264 227,714 1,275,304 1,503,018 84.85% 75.82% 63.87% |
| san-diego-ca | 2024-11-05 | numerator | 975,373 | VERIFIED | taArray, colorObject, elem); })(); Ballots Counted 975,373 Mail Ballots 787,702 Vote Center Ballots |
| san-mateo-ca | 2012-11-06 | denominator | 288,592 | VERIFIED | 468 479,562 361,486 119,212 169,380 288,592 58.69% 79.83% 60.18% |
| san-mateo-ca | 2012-11-06 | numerator | 204,287 | VERIFIED | 11/07/2012 12:07 AM Total Number of Voters : 204,287 of 361,486 = 56.51% |
| san-mateo-ca | 2014-11-04 | denominator | 164,453 | VERIFIED | o 475 490,797 355,598 54,056 110,397 164,453 67.13% 46.25% 33.51% |
| san-mateo-ca | 2014-11-04 | numerator | 112,592 | VERIFIED | 11/04/2014 11:36 PM Total Number of Voters : 112,592 of 355,598 = 31.66% |
| san-mateo-ca | 2016-11-08 | denominator | 323,303 | VERIFIED | eo 468 503,843 395,928 105,014 218,289 323,303 67.52% 81.66% 64.17% |
| san-mateo-ca | 2016-11-08 | numerator | 205,855 | VERIFIED | 11/09/2016 03:03 AM Total Number of Voters : 205,855 of 396,341 = 51.94% |
| san-mateo-ca | 2018-11-06 | denominator | 290,058 | VERIFIED | 525 507,576 399,351 34,005 256,053 290,058 88.28% 72.63% 57.15% |
| san-mateo-ca | 2018-11-06 | numerator | 111,637 | VERIFIED | render-verified: Precinct Ballots Cast 0 0.0% Vote Center Ballots Cast 26,210 6.6% Vote by Mail Ballots Cast 85,427 21.4 |
| san-mateo-ca | 2022-11-08 | denominator | 252,233 | VERIFIED | 332 515,759 432,734 17,961 234,272 252,233 92.88% 58.29% 48.91% |
| san-mateo-ca | 2022-11-08 | numerator | 122,135 | VERIFIED | (dataArray, colorObject, elem); })(); Ballots Cast 122,135 Vote by Mail Ballots 106,626 Vote Center |
| san-mateo-ca | 2024-11-05 | denominator | 337,241 | VERIFIED | 338 513,823 443,350 39,466 297,775 337,241 88.30% 76.07% 65.63% |
| san-mateo-ca | 2024-11-05 | numerator | 213,421 | VERIFIED | taArray, colorObject, elem); })(); Ballots Counted 213,421 Vote by Mail Ballots 178,796 Vote Center |
| santa-clara-ca | 2012-11-06 | denominator | 653,239 | VERIFIED | a 1,000 1,122,390 817,837 195,354 457,885 653,239 70.09% 79.87% 58.20% |
| santa-clara-ca | 2012-11-06 | numerator | 438,348 | VERIFIED | 012 Registered Voters: 817,837 Ballots Cast: 438,348 Voter Turnout: 53.60 % Precincts P |
| santa-clara-ca | 2014-11-04 | denominator | 404,166 | VERIFIED | ara 1,066 1,157,944 805,502 96,077 308,089 404,166 76.23% 50.18% 34.90% |
| santa-clara-ca | 2014-11-04 | numerator | 251,620 | VERIFIED | OR" , "K" : "6" , "VF" : 1 , "TP" : 1066 , "PR" : 1066 , "TV" : 805502 , "BC" : 251620 , "RC" : 0 , "RO" : 0 , "CH" : [  |
| santa-clara-ca | 2016-11-08 | denominator | 724,596 | VERIFIED | lara 1,063 1,193,225 875,176 190,379 534,217 724,596 73.73% 82.79% 60.73% |
| santa-clara-ca | 2016-11-08 | numerator | 303,678 | VERIFIED | render-verified: Santa Clara County ballot measures, 41% of precincts: Measure A Yes 200,688 67.0% No 98,820 33.0% (299, |
| santa-clara-ca | 2018-11-06 | denominator | 625,425 | VERIFIED | 1,098 1,208,495 885,764 138,468 486,957 625,425 77.86% 70.61% 51.75% |
| santa-clara-ca | 2022-11-08 | denominator | 550,602 | VERIFIED | 754 1,259,821 1,009,422 40,694 509,908 550,602 92.61% 54.55% 43.70% |
| santa-clara-ca | 2022-11-08 | numerator | 293,148 | VERIFIED | "BCxContest" : 0 , "VF" : 1 , "TP" : 754 , "PR" : 671 , "TV" : 1009422 , "BC" : 293148 , "RC" : 0 , "RO" : 0 , "CH" : [  |
| santa-clara-ca | 2024-11-05 | denominator | 765,495 | VERIFIED | 784 1,269,781 1,048,723 97,924 667,571 765,495 87.21% 72.99% 60.29% |
| santa-clara-ca | 2024-11-05 | numerator | 460,325 | VERIFIED | "BCxContest" : 0 , "VF" : 1 , "TP" : 784 , "PR" : 686 , "TV" : 1031980 , "BC" : 460325 , "RC" : 0 , "RO" : 0 , "CH" : [  |
