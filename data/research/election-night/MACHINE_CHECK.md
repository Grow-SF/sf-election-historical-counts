# Machine check of election-night sources

Presence checks of each claimed number against its cited URL.
Denominators are checked against the canonical per-year SoS
'Voter Participation Statistics by County' PDF even where a row cites
the complete-SOV PDF (same statistic). Fetched artifacts live in
`data/research/election-night/cache/` (gitignored; rerun the
verify_en_* scripts to regenerate).

| County | Date | Check | Claimed | Status | Evidence (context around match) |
|---|---|---|---:|---|---|
| colusa-ca | 2012-11-06 | denominator | 6,092 | VERIFIED | 18 12,364 7,765 2,692 3,400 6,092 55.81% 78.45% 49.27% |
| colusa-ca | 2014-11-04 | denominator | 4,422 | VERIFIED | 18 12,296 7,595 1,762 2,660 4,422 60.15% 58.22% 35.96% |
| colusa-ca | 2014-11-04 | numerator | 3,628 | VERIFIED | Colusa 18 18 100.0% 7,595 3,628 47.8% Nov 4 9:11 p.m. Nov 4 10:00 p.m. FENU |
| colusa-ca | 2016-11-08 | denominator | 6,814 | VERIFIED | 18 12,496 8,638 2,607 4,207 6,814 61.74% 78.88% 54.53% |
| colusa-ca | 2016-11-08 | numerator | 4,952 | VERIFIED | Colusa 18 18 100.0% 8,638 4,952 57.3% Nov 8 9:10 p.m. Nov 8 10:25 p.m. SF |
| colusa-ca | 2018-11-06 | denominator | 5,815 | VERIFIED | 18 12,552 8,792 2,580 3,235 5,815 55.63% 66.14% 46.33% |
| colusa-ca | 2022-11-08 | denominator | 5,617 | VERIFIED | 19 13,214 10,144 1,134 4,483 5,617 79.81% 55.37% 42.51% |
| colusa-ca | 2024-11-05 | denominator | 7,122 | VERIFIED | 19 13,123 10,626 0** 7,122 7,122 100.00% 67.02% 54.27% |
| del-norte-ca | 2012-06-05 | denominator | 5,242 | VERIFIED | 18 18,288 11,815 1,826 3,416 5,242 65.17% 44.37% 28.66% |
| del-norte-ca | 2012-06-05 | numerator | 4,820 | VERIFIED | FENU Del Norte 18 18 100% 11,815 4,820 40.8% Jun 5 8:38 p.m. Jun 5 11:10 p.m. FENU |
| del-norte-ca | 2012-11-06 | denominator | 8,879 | VERIFIED | 18 18,250 12,516 3,620 5,259 8,879 59.23% 70.94% 48.65% |
| del-norte-ca | 2012-11-06 | numerator | 8,067 | VERIFIED | CCU Del Norte 18 18 100.0% 12,516 8,067 64.5% Nov 6 8:51 p.m. Nov 7 12:20 a.m. FENU |
| del-norte-ca | 2014-06-03 | denominator | 5,950 | VERIFIED | e 18 18,378 12,398 2,288 3,662 5,950 61.55% 47.99% 32.38% |
| del-norte-ca | 2014-06-03 | numerator | 5,122 | VERIFIED | Del Norte 18 18 100.0% 12,398 5,122 41.3% Jun 3 8:32 p.m. Jun 3 10:14 p.m. FENU |
| del-norte-ca | 2014-11-04 | denominator | 7,332 | VERIFIED | 18 18,253 12,750 2,980 4,352 7,332 59.36% 57.51% 40.17% |
| del-norte-ca | 2014-11-04 | numerator | 6,539 | VERIFIED | render-verified: DEL_20141104_E Summary Report Del Norte County Nov. 4, 2014 General Election Unofficial. Registration & |
| del-norte-ca | 2016-11-08 | denominator | 9,790 | VERIFIED | 18 17,996 14,318 3,653 6,137 9,790 62.69% 68.38% 54.40% |
| del-norte-ca | 2016-11-08 | numerator | 8,450 | VERIFIED | Del Norte 18 18 100.0% 14,318 8,450 59.0% Nov 8 8:30 p.m. Nov 8 11:38 p.m. SF |
| del-norte-ca | 2018-11-06 | denominator | 8,439 | VERIFIED | 18 18,039 14,150 2,898 5,541 8,439 65.66% 59.64% 46.78% |
| del-norte-ca | 2018-11-06 | numerator | 7,127 | VERIFIED | render-verified: Page: 1 of 12 11/6/2018 9:42:38 PM. Summary for: All Contests, All Districts, All Tabulators, All Count |
| del-norte-ca | 2022-11-08 | denominator | 8,450 | VERIFIED | 19 19,219 14,943 1,133 7,317 8,450 86.59% 56.55% 43.97% |
| del-norte-ca | 2022-11-08 | numerator | 6,312 | VERIFIED | render-verified: Report #3 Del Norte Del Norte 2022 Statewide General Election November 8, 2022 4th Report - 19 Precinct |
| del-norte-ca | 2024-11-05 | denominator | 10,676 | VERIFIED | 19 18,059 15,036 1,686 8,990 10,676 84.21% 71.00% 59.12% |
| del-norte-ca | 2024-11-05 | numerator | 6,719 | VERIFIED | render-verified: Page: 1 of 6 11/5/2024 10:05:17 PM. Election Summary Report General Election Del Norte County November  |
| fresno-ca | 2012-06-05 | denominator | 113,975 | VERIFIED | 484 556,382 390,587 38,890 75,085 113,975 65.88% 29.18% 20.49% |
| fresno-ca | 2012-06-05 | numerator | 66,323 | VERIFIED | FENU Fresno 484 484 100% 390,587 66,323 17% Jun 5 8:09 p.m. Jun 6 1:45 a.m. FENU Gl |
| fresno-ca | 2012-11-06 | denominator | 261,652 | VERIFIED | 611 559,268 410,188 119,543 142,109 261,652 54.31% 63.79% 46.78% |
| fresno-ca | 2012-11-06 | numerator | 160,466 | VERIFIED | FENU Fresno 611 611 100.0% 410,188 160,466 39.1% Nov 6 8:14 p.m. Nov 7 2:38 a.m. FENU |
| fresno-ca | 2014-06-03 | denominator | 107,805 | VERIFIED | 447 569,314 412,181 31,764 76,041 107,805 70.54% 26.15% 18.94% |
| fresno-ca | 2014-06-03 | numerator | 79,801 | VERIFIED | Fresno 447 447 100.0% 412,181 79,801 19.4% Jun 3 8:15 p.m. Jun 4 1:28 a.m. FENU |
| fresno-ca | 2014-11-04 | denominator | 163,420 | VERIFIED | 577 572,045 416,433 64,901 98,519 163,420 60.29% 39.24% 28.57% |
| fresno-ca | 2014-11-04 | numerator | 119,317 | VERIFIED | Fresno 577 577 100.0% 416,433 119,317 28.7% Nov 4 8:00 p.m. Nov 5 1:38 a.m. FENU |
| fresno-ca | 2016-11-08 | denominator | 291,890 | VERIFIED | 592 583,238 437,423 131,787 160,103 291,890 54.85% 66.73% 50.05% |
| fresno-ca | 2016-11-08 | numerator | 177,183 | VERIFIED | es." 11/9/2016 1:42:19 AM Registered Voters 437667 - Cards Cast 177183 40.48% Num. Report Precinct 592 - Num. Reporting  |
| fresno-ca | 2018-11-06 | denominator | 256,972 | VERIFIED | 640 597,497 456,891 93,581 163,391 256,972 63.58% 56.24% 43.01% |
| fresno-ca | 2022-11-08 | denominator | 221,419 | VERIFIED | 562 642,412 500,076 28,343 193,076 221,419 87.20% 44.28% 34.47% |
| fresno-ca | 2024-11-05 | denominator | 330,932 | VERIFIED | 478 649,184 513,799 63,049 267,883 330,932 80.95% 64.41% 50.98% |
| fresno-ca | 2024-11-05 | numerator | 206,372 | VERIFIED | FICIAL ELECTION RESULTS Precincts Reported: 478 of 478 (100.00%) Voters Cast: 206,372 of 511,349 (40.36%) President and  |
| lake-ca | 2012-06-05 | denominator | 14,274 | VERIFIED | 70 47,459 33,553 4,781 9,493 14,274 66.51% 42.54% 30.08% |
| lake-ca | 2012-06-05 | numerator | 10,427 | VERIFIED | a.m. FENU Lake 70 70 100% 33,553 10,427 31.1% Jun 5 9:46 p.m. Jun 6 1:10 a.m. FENU |
| lake-ca | 2012-11-06 | denominator | 23,685 | VERIFIED | 70 47,135 34,936 8,987 14,698 23,685 62.06% 67.80% 50.25% |
| lake-ca | 2012-11-06 | numerator | 16,622 | VERIFIED | bsentee Ballots Cast 8,057 23.1% Total Ballots Cast 16,622 47.6% Registration and Turnout CONGRESSIONAL DIST |
| lake-ca | 2014-06-03 | denominator | 15,548 | VERIFIED | 70 49,002 33,987 5,153 10,395 15,548 66.86% 45.75% 31.73% |
| lake-ca | 2014-06-03 | numerator | 9,703 | VERIFIED | Lake 70 70 100.0% 33,987 9,703 28.5% Jun 3 8:59 p.m. Jun 4 12:55 a.m. FENU |
| lake-ca | 2014-11-04 | denominator | 18,061 | VERIFIED | 70 49,067 33,489 6,017 12,044 18,061 66.69% 53.93% 36.81% |
| lake-ca | 2014-11-04 | numerator | 12,593 | VERIFIED | bsentee Ballots Cast 7,228 21.6% Total Ballots Cast 12,593 37.6% Registration and Turnout CONGRESSIONAL DIST |
| lake-ca | 2016-06-07 | denominator | 16,712 | VERIFIED | ake 70 48,604 32,796 5,042 11,670 16,712 69.83% 50.96% 34.38% |
| lake-ca | 2016-06-07 | numerator | 9,049 | VERIFIED | Lake 70 70 100.0% 32,796 9,049 27.6% Jun 7 9:39 p.m. Jun 8 2:54 a.m. CCU |
| lake-ca | 2016-11-08 | denominator | 25,085 | VERIFIED | 70 48,487 34,706 8,163 16,922 25,085 67.46% 72.28% 51.74% |
| lake-ca | 2016-11-08 | numerator | 13,484 | VERIFIED | bsentee Ballots Cast 6,587 19.0% Total Ballots Cast 13,484 38.9% Registration and Turnout CONGRESSIONAL DIST |
| lake-ca | 2018-06-05 | denominator | 14,119 | VERIFIED | 70 49,352 32,805 3,917 10,202 14,119 72.26% 43.04% 28.61% |
| lake-ca | 2018-06-05 | numerator | 8,158 | VERIFIED | U Lake 70 70 100.0% 32,805 8,158 24% Jun 5 9:07 p.m. Jun 6 1:44 a.m. U |
| lake-ca | 2018-11-06 | denominator | 21,465 | VERIFIED | 70 49,469 32,653 6,049 15,416 21,465 71.82% 65.74% 43.39% |
| lake-ca | 2018-11-06 | numerator | 13,522 | VERIFIED | bsentee Ballots Cast 8,566 26.2% Total Ballots Cast 13,522 41.4% Registration and Turnout CONGRESSIONAL DIST |
| lake-ca | 2022-11-08 | denominator | 20,362 | VERIFIED | 80 51,231 37,154 2,416 17,946 20,362 88.13% 54.80% 39.75% |
| lake-ca | 2022-11-08 | numerator | 7,842 | VERIFIED | finalize the results and certify the election. The preliminary count included 7,842 ballots, or 21.2% of Lake County’s 3 |
| lake-ca | 2024-11-05 | denominator | 27,127 | VERIFIED | 48 51,197 37,975 3,577 23,550 27,127 86.81% 71.43% 52.99% |
| lake-ca | 2024-11-05 | numerator | 7,960 | VERIFIED | e counted as of early Wednesday morning. Out of 37,915 registered voters, only 7,960 ballots, or 20.99%, have been count |
| los-angeles-ca | 2012-06-05 | denominator | 973,274 | VERIFIED | eles 4,786 5,959,291 4,459,268 541,463 431,811 973,274 44.37% 21.83% 16.33% |
| los-angeles-ca | 2012-06-05 | numerator | 765,552 | VERIFIED | Los Angeles 4,786 4,786 100% 4,459,268 765,552 17.2% Jun 5 8:13 p.m. Jun 6 4:43 a.m. FENU |
| los-angeles-ca | 2012-11-06 | denominator | 3,236,704 | VERIFIED | eles 4,993 5,976,156 4,758,437 2,260,876 975,828 3,236,704 30.15% 68.02% 54.16% |
| los-angeles-ca | 2012-11-06 | numerator | 2,368,283 | VERIFIED | d ballots with votes for write-in candidates. On Election Night a total of 2,368,283 ballots were counted. This included |
| los-angeles-ca | 2014-06-03 | denominator | 824,070 | VERIFIED | geles 4,870 6,076,302 4,857,424 423,376 400,694 824,070 48.62% 16.97% 13.56% |
| los-angeles-ca | 2014-06-03 | numerator | 636,186 | VERIFIED | os Angeles 4,870 4,870 100.0% 4,857,424 636,186 13.1% Jun 3 8:06 p.m. Jun 4 3:07 a.m. FENU |
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
| madera-ca | 2012-06-05 | denominator | 20,538 | VERIFIED | 54 86,137 52,826 5,654 14,884 20,538 72.47% 38.88% 23.84% |
| madera-ca | 2012-06-05 | numerator | 16,619 | VERIFIED | m. FENU Madera 54 54 100% 52,826 16,619 31.5% Jun 5 8:05 p.m. Jun 6 12:00 a.m. FENU |
| madera-ca | 2012-11-06 | denominator | 40,325 | VERIFIED | 96 86,894 53,779 15,658 24,667 40,325 61.17% 74.98% 46.41% |
| madera-ca | 2012-11-06 | numerator | 32,865 | VERIFIED | .m. CCU Madera 96 96 100.0% 53,779 32,865 61.1% Nov 6 8:03 p.m. Nov 6 11:01 p.m. FENU |
| madera-ca | 2014-06-03 | denominator | 19,206 | VERIFIED | 76 85,586 52,817 5,197 14,009 19,206 72.94% 36.36% 22.44% |
| madera-ca | 2014-06-03 | numerator | 15,719 | VERIFIED | Madera 76 76 100.0% 52,817 15,719 29.8% Jun 3 8:00 p.m. Jun 3 10:40 p.m. FENU |
| madera-ca | 2014-11-04 | denominator | 27,370 | VERIFIED | 100 85,976 52,494 8,970 18,400 27,370 67.23% 52.14% 31.83% |
| madera-ca | 2014-11-04 | numerator | 22,031 | VERIFIED | Madera 100 100 100.0% 52,494 22,031 42.0% Nov 4 8:07 p.m. Nov 4 11:03 p.m. FENU |
| madera-ca | 2016-06-07 | denominator | 26,941 | VERIFIED | adera 77 87,117 54,017 8,278 18,663 26,941 69.27% 49.88% 30.93% |
| madera-ca | 2016-06-07 | numerator | 21,553 | VERIFIED | Madera 77 77 100.0% 54,017 21,553 39.9% Jun 7 8:10 p.m. Jun 7 11:13 p.m. FENU |
| madera-ca | 2016-11-08 | denominator | 44,186 | VERIFIED | 102 87,254 58,086 15,211 28,975 44,186 65.58% 76.07% 50.64% |
| madera-ca | 2016-11-08 | numerator | 35,364 | VERIFIED | Absentee Ballots Cast 22,561 38.8% Total Ballots Cast 35,364 60.8% President and Vice President Completed Prec |
| madera-ca | 2018-06-05 | denominator | 24,211 | VERIFIED | 69 89,532 54,848 1,995 22,216 24,211 91.76% 44.14% 27.04% |
| madera-ca | 2018-06-05 | numerator | 18,258 | VERIFIED | U Madera 69 69 100.0% 54,848 18,258 33% Jun 5 9:07 p.m. Jun 6 12:20 a.m. SF |
| madera-ca | 2018-11-06 | denominator | 38,968 | VERIFIED | 69 89,818 57,418 4,434 34,534 38,968 88.62% 67.87% 43.39% |
| madera-ca | 2018-11-06 | numerator | 28,159 | VERIFIED | 0 , "BCxContest" : 0 , "VF" : 1 , "TP" : 69 , "PR" : 62 , "TV" : 31713 , "BC" : 28159 , "RC" : 0 , "RO" : 0 , "CH" : [ " |
| madera-ca | 2022-11-08 | denominator | 37,345 | VERIFIED | 59 93,789 72,865 3,333 34,012 37,345 91.08% 51.25% 39.82% |
| madera-ca | 2022-11-08 | numerator | 21,951 | VERIFIED | 0 , "BCxContest" : 0 , "VF" : 1 , "TP" : 59 , "PR" : 50 , "TV" : 72232 , "BC" : 21951 , "RC" : 0 , "RO" : 0 , "CH" : [ " |
| madera-ca | 2024-11-05 | denominator | 55,329 | VERIFIED | 78 95,290 78,204 8,560 46,769 55,329 84.53% 70.75% 58.06% |
| madera-ca | 2024-11-05 | numerator | 37,106 | VERIFIED | 0 , "BCxContest" : 0 , "VF" : 1 , "TP" : 78 , "PR" : 63 , "TV" : 78317 , "BC" : 37106 , "RC" : 0 , "RO" : 0 , "CH" : [ " |
| mendocino-ca | 2012-06-05 | denominator | 20,116 | VERIFIED | o 247 62,919 47,546 3,171 16,945 20,116 84.24% 42.31% 31.97% |
| mendocino-ca | 2012-06-05 | numerator | 13,485 | VERIFIED | FENU Mendocino 247 247 100% 47,546 13,485 28.4% Jun 5 8:48 p.m. Jun 6 1:15 a.m. FENU |
| mendocino-ca | 2012-11-06 | denominator | 36,080 | VERIFIED | 247 62,910 49,765 7,046 29,034 36,080 80.47% 72.50% 57.35% |
| mendocino-ca | 2012-11-06 | numerator | 18,401 | NOT_FOUND |  |
| mendocino-ca | 2014-06-03 | denominator | 16,420 | VERIFIED | no 249 64,240 47,400 2,477 13,943 16,420 84.91% 34.64% 25.56% |
| mendocino-ca | 2014-06-03 | numerator | 8,669 | VERIFIED | Mendocino 249 249 100.0% 47,400 8,669 18.3% Jun 3 8:47 p.m. Jun 4 1:29 a.m. FENU |
| mendocino-ca | 2014-11-04 | denominator | 25,017 | VERIFIED | 249 64,404 47,502 4,377 20,640 25,017 82.50% 52.67% 38.84% |
| mendocino-ca | 2014-11-04 | numerator | 11,402 | VERIFIED | he counting of maybe 10,000 more votes) for key Mendocino County Elections. 11,402 votes cast, 24.02% of registered vote |
| mendocino-ca | 2016-06-07 | denominator | 28,056 | VERIFIED | endocino 250 63,670 48,935 4,249 23,807 28,056 84.86% 57.33% 44.06% |
| mendocino-ca | 2016-06-07 | numerator | 11,320 | VERIFIED | Mendocino 250 250 100.0% 48,935 11,320 23.1% Jun 7 8:54 p.m. Jun 8 2:39 a.m. FENU |
| mendocino-ca | 2016-11-08 | denominator | 38,730 | VERIFIED | o 250 63,741 51,061 6,036 32,694 38,730 84.42% 75.85% 60.76% |
| mendocino-ca | 2016-11-08 | numerator | 12,032 | VERIFIED | anvass. 11/09/16 01:55:06 Registered Voters 51035 - Cards Cast 12032 23.58% Num. Report Precinct 250 - Num. Reporting 25 |
| mendocino-ca | 2018-06-05 | denominator | 22,896 | VERIFIED | 250 64,340 47,487 3,066 19,830 22,896 86.61% 48.22% 35.59% |
| mendocino-ca | 2018-06-05 | numerator | 19,049 | VERIFIED | Mendocino 250 250 100.0% 47,487 19,049 40% Jun 5 9:16 p.m. Jun 6 3:57 a.m. SF |
| mendocino-ca | 2018-11-06 | denominator | 33,966 | VERIFIED | 250 64,399 49,411 4,462 29,504 33,966 86.86% 68.74% 52.74% |
| mendocino-ca | 2018-11-06 | numerator | 15,819 | VERIFIED | anvass. 11/07/18 00:48:58 Registered Voters 48032 - Cards Cast 15819 32.93% Num. Report Precinct 250 - Num. Reporting 25 |
| mendocino-ca | 2022-11-08 | denominator | 31,008 | VERIFIED | 281 67,114 53,105 646 30,362 31,008 97.92% 58.39% 46.20% |
| mendocino-ca | 2024-11-05 | denominator | 39,837 | VERIFIED | 245 66,917 54,447 2,479 37,358 39,837 93.78% 73.17% 59.53% |
| mendocino-ca | 2024-11-05 | numerator | 15,611 | VERIFIED | ential General Election, voter turnout in Mendocino County reached 28.57%, with 15,611 out of 54,640 registered voters c |
| napa-ca | 2012-06-05 | denominator | 29,305 | VERIFIED | 157 90,847 68,330 2,616 26,689 29,305 91.07% 42.89% 32.26% |
| napa-ca | 2012-06-05 | numerator | 19,147 | VERIFIED | m. FENU Napa 157 157 100% 68,330 19,147 28% Jun 5 8:30 p.m. Jun 5 11:09 p.m. FENU N |
| napa-ca | 2012-11-06 | denominator | 57,672 | VERIFIED | 167 91,138 72,592 6,251 51,421 57,672 89.16% 79.45% 63.28% |
| napa-ca | 2012-11-06 | numerator | 32,715 | VERIFIED | Election Day Turnout 5,869 8.08% Total 32,715 45.07% PRESIDENT AND VICE PRESIDENT |
| napa-ca | 2014-06-03 | denominator | 28,179 | VERIFIED | 165 91,388 71,241 1,404 26,775 28,179 95.02% 39.55% 30.83% |
| napa-ca | 2014-06-03 | numerator | 17,431 | VERIFIED | Napa 165 165 100.0% 71,241 17,431 24.5% Jun 3 7:59 p.m. Jun 3 11:43 p.m. FENU |
| napa-ca | 2014-11-04 | denominator | 38,766 | VERIFIED | 167 91,531 70,493 2,397 36,369 38,766 93.82% 54.99% 42.35% |
| napa-ca | 2014-11-04 | numerator | 19,515 | VERIFIED | Napa 167 167 100.0% 70,493 19,515 27.7% Nov 4 8:00 p.m. Nov 4 11:14 p.m. FENU |
| napa-ca | 2016-06-07 | denominator | 43,450 | VERIFIED | apa 167 93,331 72,461 2,150 41,300 43,450 95.05% 59.96% 46.55% |
| napa-ca | 2016-06-07 | numerator | 20,427 | VERIFIED | Napa 167 167 100.0% 72,461 20,427 28.2% Jun 7 8:03 p.m. Jun 8 12:07 a.m. CCU |
| napa-ca | 2016-11-08 | denominator | 63,255 | VERIFIED | 167 93,686 76,833 4,530 58,725 63,255 92.84% 82.33% 67.52% |
| napa-ca | 2016-11-08 | numerator | 34,108 | VERIFIED | November 8, 2016 Precincts Reported: 167 of 167 (100.00%) Ballots Cast: 34,108 PRESIDENT/VICE PRESIDENT (Vote for 1) Pre |
| napa-ca | 2018-11-06 | denominator | 57,132 | VERIFIED | 170 92,369 78,135 42 57,090 57,132 99.93% 73.12% 61.85% |
| napa-ca | 2018-11-06 | numerator | 21,774 | VERIFIED | ION NIGHT REPORT Precincts Reported: 170 of 170 (100.00%) Registered Voters: 21,774 of 78,135 (27.87%) Ballots Cast: 43, |
| napa-ca | 2022-11-08 | denominator | 50,788 | VERIFIED | 200 97,321 83,480 1,563 49,225 50,788 96.92% 60.84% 52.19% |
| napa-ca | 2022-11-08 | numerator | 21,943 | VERIFIED | 24.43% Total 21,943 83,471 26.29% Precincts Reported: 200 of 200 (100.00 |
| napa-ca | 2024-11-05 | denominator | 66,634 | VERIFIED | 204 97,259 85,045 4,851 61,783 66,634 92.72% 78.35% 68.51% |
| napa-ca | 2024-11-05 | numerator | 26,160 | VERIFIED | l Election Night Report Precincts Reported: 204 of 204 (100.00%) Voters Cast: 26,160 of 85,150 (30.72%) President and Vi |
| nevada-ca | 2012-06-05 | denominator | 31,333 | VERIFIED | 74 76,426 60,590 6,408 24,925 31,333 79.55% 51.71% 41.00% |
| nevada-ca | 2012-06-05 | numerator | 21,763 | VERIFIED | m. FENU Nevada 74 74 100% 60,590 21,763 35.9% Jun 5 8:57 p.m. Jun 6 12:27 a.m. FENU |
| nevada-ca | 2012-11-06 | denominator | 52,173 | VERIFIED | 140 76,187 62,853 13,798 38,375 52,173 73.55% 83.01% 68.48% |
| nevada-ca | 2012-11-06 | numerator | 31,275 | VERIFIED | re than 18,000 unprocessed ballots to add to the county's election-day tally of 31,275. "It takes time because more than |
| nevada-ca | 2014-06-03 | denominator | 27,596 | VERIFIED | 71 76,711 61,711 5,270 22,326 27,596 80.90% 44.72% 35.97% |
| nevada-ca | 2014-06-03 | numerator | 17,752 | VERIFIED | Nevada 71 71 100.0% 61,711 17,752 28.8% Jun 3 8:49 p.m. Jun 4 12:23 a.m. FENU |
| nevada-ca | 2014-11-04 | denominator | 39,629 | VERIFIED | 84 76,731 61,690 9,383 30,246 39,629 76.32% 64.24% 51.65% |
| nevada-ca | 2014-11-04 | numerator | 22,366 | VERIFIED | , Calif. November 5, 2014 - The final election night tally of votes comes in at 22,366 of 61,706 - a rather low voter tu |
| nevada-ca | 2016-06-07 | denominator | 45,167 | VERIFIED | evada 80 77,440 66,149 10,572 34,595 45,167 76.59% 68.28% 58.33% |
| nevada-ca | 2016-06-07 | numerator | 27,852 | VERIFIED | Nevada 80 80 100.0% 66,149 27,852 42.1% Jun 7 9:18 p.m. Jun 8 12:50 a.m. CCU |
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
| placer-ca | 2012-06-05 | denominator | 89,019 | VERIFIED | 281 249,916 194,705 21,276 67,743 89,019 76.10% 45.72% 35.62% |
| placer-ca | 2012-06-05 | numerator | 62,087 | VERIFIED | CCU Placer 281 281 100% 194,705 62,087 31.9% Jun 5 8:42 p.m. Jun 6 12:40 a.m. FENU |
| placer-ca | 2012-11-06 | denominator | 172,757 | VERIFIED | 350 251,135 208,604 57,171 115,586 172,757 66.91% 82.82% 68.79% |
| placer-ca | 2012-11-06 | numerator | 127,593 | VERIFIED | CCU Placer 350 350 100.0% 208,604 127,593 61.2% Nov 6 8:04 p.m. Nov 6 11:47 p.m. FENU |
| placer-ca | 2014-06-03 | denominator | 70,016 | VERIFIED | 301 257,989 200,829 13,633 56,383 70,016 80.53% 34.86% 27.14% |
| placer-ca | 2014-06-03 | numerator | 47,986 | VERIFIED | Placer 301 301 100.0% 200,829 47,986 23.9% Jun 3 9:14 p.m. Jun 4 2:06 a.m. FENU |
| placer-ca | 2014-11-04 | denominator | 115,547 | VERIFIED | 368 259,591 200,422 31,546 84,001 115,547 72.70% 57.65% 44.51% |
| placer-ca | 2014-11-04 | numerator | 76,411 | VERIFIED | 05/14 00:36:57 Registered Voters 200402 - Cards Cast 76411 38.13% Num. Report Precinct 369 - Num. Reporting 369 100.00% |
| placer-ca | 2016-06-07 | denominator | 115,266 | VERIFIED | Placer 316 262,922 210,913 30,302 84,964 115,266 73.71% 54.65% 43.84% |
| placer-ca | 2016-06-07 | numerator | 71,358 | VERIFIED | Placer 316 316 100.0% 210,913 71,358 33.8% Jun 7 9:48 p.m. Jun 8 2:27 a.m. FENU |
| placer-ca | 2016-11-08 | denominator | 190,550 | VERIFIED | 363 264,101 226,249 58,385 132,165 190,550 69.36% 84.22% 72.15% |
| placer-ca | 2016-11-08 | numerator | 109,666 | VERIFIED | 09/16 00:29:40 Registered Voters 226454 - Cards Cast 109666 48.43% Num. Report Precinct 363 - Num. Reporting 363 100.00% |
| placer-ca | 2018-11-06 | denominator | 177,725 | VERIFIED | 358 276,613 234,732 46,896 130,829 177,725 73.61% 75.71% 64.25% |
| placer-ca | 2018-11-06 | numerator | 113,380 | VERIFIED | 11/09/18 15:15:00 Registered Voters 231461 – Cards Cast 113380 48.98% Num. Report Precinct 358 – Num. Reporting 358 100. |
| placer-ca | 2022-11-08 | denominator | 184,507 | VERIFIED | 408 301,467 279,016 25,494 159,013 184,507 86.18% 66.13% 61.20% |
| placer-ca | 2024-11-05 | denominator | 239,402 | VERIFIED | 331 305,381 291,479 56,964 182,438 239,402 76.21% 82.13% 78.39% |
| riverside-ca | 2012-06-05 | denominator | 238,152 | VERIFIED | de 853 1,351,562 852,217 70,045 168,107 238,152 70.59% 27.94% 17.62% |
| riverside-ca | 2012-06-05 | numerator | 189,087 | VERIFIED | CCU Riverside 853 853 100% 852,217 189,087 22.2% Jun 5 8:21 p.m. Jun 6 1:50 a.m. FENU |
| riverside-ca | 2012-11-06 | denominator | 669,627 | VERIFIED | 1,218 1,358,695 943,405 298,112 371,515 669,627 55.48% 70.98% 49.28% |
| riverside-ca | 2014-06-03 | denominator | 198,102 | VERIFIED | ide 847 1,387,385 887,643 50,111 147,991 198,102 74.70% 22.32% 14.28% |
| riverside-ca | 2014-11-04 | denominator | 357,764 | VERIFIED | e 1,193 1,394,302 891,575 124,829 232,935 357,764 65.11% 40.13% 25.66% |
| riverside-ca | 2014-11-04 | numerator | 265,771 | VERIFIED | verside 1,193 1,193 100.0% 891,575 265,771 29.8% Nov 4 8:20 p.m. Nov 5 2:26 a.m. FENU |
| riverside-ca | 2016-06-07 | denominator | 403,828 | VERIFIED | Riverside 869 1,429,960 909,922 127,086 276,742 403,828 68.53% 44.38% 28.24% |
| riverside-ca | 2016-06-07 | numerator | 249,970 | VERIFIED | ast 5,338 0.00% Total Ballots Cast 249,970 27.43% Total Ballots Cast 5,046 18.32% Total |
| riverside-ca | 2016-11-08 | denominator | 769,193 | VERIFIED | de 1,126 1,438,117 1,019,130 264,638 504,555 769,193 65.60% 75.48% 53.49% |
| riverside-ca | 2016-11-08 | numerator | 481,315 | VERIFIED | rside 1,126 1,126 100.0% 1,019,130 481,315 47.2% Nov 8 8:31 p.m. Nov 9 5:52 a.m. SF |
| riverside-ca | 2018-06-05 | denominator | 346,472 | VERIFIED | 826 1,472,819 984,214 91,667 254,805 346,472 73.54% 35.20% 23.52% |
| riverside-ca | 2018-06-05 | numerator | 193,152 | VERIFIED | 19,838 11.01% Total Ballots Cast 193,152 19.63% REP - DAVID R. HERNANDEZ 13,439 8.06% PF - KEVI |
| riverside-ca | 2018-11-06 | denominator | 650,545 | VERIFIED | 1,072 1,481,361 1,035,957 194,606 455,939 650,545 70.09% 62.80% 43.92% |
| riverside-ca | 2022-06-07 | denominator | 375,610 | VERIFIED | 795 1,634,639 1,304,257 23,640 351,970 375,610 93.71% 28.80% 22.98% |
| riverside-ca | 2022-06-07 | numerator | 191,996 | VERIFIED | ficial Election Results Precincts Reported: 795 of 795 (100.00%) Voters Cast: 191,996 of 1,304,447 (14.72%) Governor (Vo |
| riverside-ca | 2022-11-08 | denominator | 604,617 | VERIFIED | 1,265 1,637,165 1,310,505 59,812 544,805 604,617 90.11% 46.14% 36.93% |
| riverside-ca | 2022-11-08 | numerator | 205,813 | VERIFIED | orted: 1,265 of 1,265 ( 100.00% ) Voters Cast: 205,813 of 1,310,928 ( 15.70% ) Governor |
| riverside-ca | 2024-03-05 | denominator | 409,269 | VERIFIED | 928 1,642,089 1,327,135 38,699 370,570 409,269 90.54% 30.84% 24.92% |
| riverside-ca | 2024-11-05 | denominator | 959,098 | VERIFIED | 1,345 1,646,951 1,372,548 170,437 788,661 959,098 82.23% 69.88% 58.23% |
| riverside-ca | 2024-11-05 | numerator | 547,742 | VERIFIED | Vote Centers 1,345 1,345 100.0% 1,372,548 547,742 39.9% Nov 5 8:44 p.m. Nov 6 5:02 a.m. U |
| sacramento-ca | 2012-11-06 | denominator | 522,045 | VERIFIED | 1,106 944,243 698,899 216,021 306,024 522,045 58.62% 74.70% 55.29% |
| sacramento-ca | 2012-11-06 | numerator | 328,516 | VERIFIED | L . . . . . 698,899 BALLOTS CAST - TOTAL. . . . . . . 328,516 VOTER TURNOUT - TOTAL . . . . . . 47.00 |
| sacramento-ca | 2014-06-03 | denominator | 203,850 | VERIFIED | ento 1,102 957,597 688,443 57,425 146,425 203,850 71.83% 29.61% 21.29% |
| sacramento-ca | 2014-06-03 | numerator | 122,053 | VERIFIED | Sacramento 1,102 1,102 100.0% 688,443 122,053 17.7% Jun 3 8:09 p.m. Jun 4 12:11 a.m. FENU |
| sacramento-ca | 2014-11-04 | denominator | 330,817 | VERIFIED | to 1,263 961,112 683,632 111,628 219,189 330,817 66.26% 48.39% 34.42% |
| sacramento-ca | 2014-11-04 | numerator | 195,317 | VERIFIED | L . . . . . 683,632 BALLOTS CAST - TOTAL. . . . . . . 195,317 VOTER TURNOUT - TOTAL . . . . . . 28.57 |
| sacramento-ca | 2016-11-08 | denominator | 575,711 | VERIFIED | nto 1,267 989,090 772,865 203,114 372,597 575,711 64.72% 74.49% 58.21% |
| sacramento-ca | 2016-11-08 | numerator | 328,744 | VERIFIED | ramento 1,267 1,267 100.0% 772,865 328,744 42.5% Nov 8 8:07 p.m. Nov 9 1:52 a.m. SF |
| sacramento-ca | 2018-11-06 | denominator | 522,652 | VERIFIED | 593 1,013,368 765,965 30,279 492,373 522,652 94.21% 68.23% 51.58% |
| sacramento-ca | 2018-11-06 | numerator | 185,623 | VERIFIED | ( 100.00% ) Registered Voters: 185,623 of 764,998 ( 24.26% ) Ball |
| sacramento-ca | 2022-11-08 | denominator | 484,315 | VERIFIED | 685 1,112,665 865,225 28,929 455,386 484,315 94.03% 55.98% 43.53% |
| sacramento-ca | 2022-11-08 | numerator | 145,015 | VERIFIED | I-FINAL Voters Cast: 145,015 of 864,814 ( 16.77% ) Governo |
| sacramento-ca | 2024-11-05 | denominator | 668,416 | VERIFIED | 686 1,116,853 889,806 73,650 594,766 668,416 88.98% 75.12% 59.85% |
| sacramento-ca | 2024-11-05 | numerator | 311,821 | VERIFIED | I-FINAL Voters Cast: 311,821 of 889,465 ( 35.06% ) Preside |
| san-bernardino-ca | 2012-11-06 | denominator | 589,611 | VERIFIED | dino 1,609 1,259,676 851,581 306,324 283,287 589,611 48.05% 69.24% 46.81% |
| san-bernardino-ca | 2014-11-04 | denominator | 293,283 | VERIFIED | ardino 1,737 1,273,684 851,684 117,179 176,104 293,283 60.05% 34.44% 23.03% |
| san-bernardino-ca | 2014-11-04 | numerator | 231,219 | VERIFIED | nardino 1,737 1,737 100.0% 851,684 231,219 27.1% Nov 4 8:09 p.m. Nov 5 1:50 a.m. FENU |
| san-bernardino-ca | 2016-11-08 | denominator | 672,871 | VERIFIED | nardino 1,789 1,308,522 888,019 287,315 385,556 672,871 57.30% 75.77% 51.42% |
| san-bernardino-ca | 2016-11-08 | numerator | 443,517 | VERIFIED | nardino 1,789 1,789 100.0% 888,019 443,517 49.9% Nov 8 8:22 p.m. Nov 9 4:56 a.m. SF |
| san-bernardino-ca | 2018-11-06 | denominator | 546,041 | VERIFIED | 2,209 1,330,247 937,316 209,168 336,873 546,041 61.69% 58.26% 41.05% |
| san-bernardino-ca | 2022-11-08 | denominator | 458,946 | VERIFIED | 2,765 1,472,696 1,138,818 66,469 392,477 458,946 85.52% 40.30% 31.16% |
| san-bernardino-ca | 2024-11-05 | denominator | 771,834 | VERIFIED | 2,872 1,472,596 1,197,953 154,974 616,860 771,834 79.92% 64.43% 52.41% |
| san-bernardino-ca | 2024-11-05 | numerator | 434,108 | VERIFIED | render-verified: Precincts Reported: 2,872 of 2,872 (100.00%) Voters Cast: 434,108 of 1,198,556 (36.22%) Cards Cast: 1,2 |
| san-diego-ca | 2012-06-05 | denominator | 548,462 | VERIFIED | go 1,643 2,084,578 1,465,269 187,942 360,520 548,462 65.73% 37.43% 26.31% |
| san-diego-ca | 2012-11-06 | denominator | 1,203,265 | VERIFIED | go 2,064 2,094,093 1,563,093 528,258 675,007 1,203,265 56.10% 76.98% 57.46% |
| san-diego-ca | 2014-06-03 | denominator | 420,700 | VERIFIED | ego 1,616 2,124,563 1,544,841 113,714 306,986 420,700 72.97% 27.23% 19.80% |
| san-diego-ca | 2014-11-04 | denominator | 692,434 | VERIFIED | o 2,001 2,135,863 1,546,924 242,638 449,796 692,434 64.96% 44.76% 32.42% |
| san-diego-ca | 2014-11-04 | numerator | 509,214 | VERIFIED | Diego 2,001 2,001 100.0% 1,546,924 509,214 32.9% Nov 4 8:03 p.m. Nov 5 1:14 a.m. FENU |
| san-diego-ca | 2016-06-07 | denominator | 775,930 | VERIFIED | San Diego 1,726 2,183,908 1,523,251 285,370 490,560 775,930 63.22% 50.94% 35.53% |
| san-diego-ca | 2016-06-07 | numerator | 468,340 | VERIFIED | " id="53" title="UNITED STATES SENATOR" numberof="35" votefor="1" tcounted="468340" tblank="47700" tover="0" tunder="0"  |
| san-diego-ca | 2016-11-08 | denominator | 1,346,513 | VERIFIED | iego 2,175 2,191,191 1,652,570 489,576 856,937 1,346,513 63.64% 81.48% 61.45% |
| san-diego-ca | 2018-06-05 | denominator | 673,640 | VERIFIED | 1,705 2,216,211 1,683,430 197,501 476,139 673,640 70.68% 40.02% 30.40% |
| san-diego-ca | 2018-06-05 | numerator | 406,501 | VERIFIED | (dataArray, colorObject, elem); })(); Ballots Cast 406,501 Registered Voters 1,693,774 |
| san-diego-ca | 2018-11-06 | denominator | 1,173,924 | VERIFIED | 2,136 2,224,081 1,741,707 369,655 804,269 1,173,924 68.51% 67.40% 52.78% |
| san-diego-ca | 2018-11-06 | numerator | 536,734 | VERIFIED | (dataArray, colorObject, elem); })(); Ballots Cast 536,734 Registered Voters 1,767,300 |
| san-diego-ca | 2022-06-07 | denominator | 674,608 | VERIFIED | 2,031 2,349,594 1,932,683 45,332 629,276 674,608 93.28% 34.91% 28.71% |
| san-diego-ca | 2022-06-07 | numerator | 416,748 | VERIFIED | (dataArray, colorObject, elem); })(); Ballots Cast 416,748 Vote Center Ballots 44,165 Mail Ballots |
| san-diego-ca | 2022-11-08 | denominator | 1,043,490 | VERIFIED | 2,718 2,349,554 1,924,634 104,388 939,102 1,043,490 90.00% 54.22% 44.41% |
| san-diego-ca | 2022-11-08 | numerator | 565,982 | VERIFIED | (dataArray, colorObject, elem); })(); Ballots Cast 565,982 Mail Ballots 468,632 Vote Center Ballots |
| san-diego-ca | 2024-03-05 | denominator | 704,068 | VERIFIED | 1,886 2,332,492 1,930,294 53,989 650,079 704,068 92.33% 36.47% 30.19% |
| san-diego-ca | 2024-03-05 | numerator | 425,572 | VERIFIED | taArray, colorObject, elem); })(); Ballots Counted 425,572 Mail Ballots 374,440 Vote Center Ballots |
| san-diego-ca | 2024-11-05 | denominator | 1,503,018 | VERIFIED | 2,669 2,353,145 1,982,264 227,714 1,275,304 1,503,018 84.85% 75.82% 63.87% |
| san-diego-ca | 2024-11-05 | numerator | 975,373 | VERIFIED | taArray, colorObject, elem); })(); Ballots Counted 975,373 Mail Ballots 787,702 Vote Center Ballots |
| san-mateo-ca | 2012-11-06 | denominator | 288,592 | VERIFIED | 468 479,562 361,486 119,212 169,380 288,592 58.69% 79.83% 60.18% |
| san-mateo-ca | 2012-11-06 | numerator | 204,287 | VERIFIED | 11/07/2012 12:07 AM Total Number of Voters : 204,287 of 361,486 = 56.51% |
| san-mateo-ca | 2014-06-03 | denominator | 97,447 | VERIFIED | eo 475 488,370 354,994 21,484 75,963 97,447 77.95% 27.45% 19.95% |
| san-mateo-ca | 2014-06-03 | numerator | 70,651 | VERIFIED | San Mateo 475 475 100.0% 354,994 70,651 19.9% Jun 3 8:05 p.m. Jun 3 11:30 p.m. FENU |
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
| santa-clara-ca | 2012-06-05 | denominator | 292,713 | VERIFIED | lara 874 1,116,131 755,117 55,518 237,195 292,713 81.03% 38.76% 26.23% |
| santa-clara-ca | 2012-06-05 | numerator | 234,342 | VERIFIED | 455 Precinct Reporting Turnout 6.47% 48,887 31.03% 234,342 ⇑ Back To Top Nonpartisan Registration & Turnout |
| santa-clara-ca | 2012-11-06 | denominator | 653,239 | VERIFIED | a 1,000 1,122,390 817,837 195,354 457,885 653,239 70.09% 79.87% 58.20% |
| santa-clara-ca | 2012-11-06 | numerator | 438,348 | VERIFIED | 012 Registered Voters: 817,837 Ballots Cast: 438,348 Voter Turnout: 53.60 % Precincts P |
| santa-clara-ca | 2014-11-04 | denominator | 404,166 | VERIFIED | ara 1,066 1,157,944 805,502 96,077 308,089 404,166 76.23% 50.18% 34.90% |
| santa-clara-ca | 2014-11-04 | numerator | 235,062 | VERIFIED | OR" , "K" : "6" , "VF" : 1 , "TP" : 1066 , "PR" : 1066 , "TV" : 805502 , "BC" : 235062 , "RC" : 0 , "RO" : 0 , "CH" : [  |
| santa-clara-ca | 2016-11-08 | denominator | 724,596 | VERIFIED | lara 1,063 1,193,225 875,176 190,379 534,217 724,596 73.73% 82.79% 60.73% |
| santa-clara-ca | 2016-11-08 | numerator | 443,269 | VERIFIED | "regvoters" : 0 , "VF" : 1 , "TP" : 1063 , "PR" : 1063 , "TV" : 875176 , "BC" : 443269 , "RC" : 0 , "RO" : 0 , "CH" : [  |
| santa-clara-ca | 2018-11-06 | denominator | 625,425 | VERIFIED | 1,098 1,208,495 885,764 138,468 486,957 625,425 77.86% 70.61% 51.75% |
| santa-clara-ca | 2018-11-06 | numerator | 304,303 | VERIFIED | BCxContest" : 0 , "VF" : 1 , "TP" : 1098 , "PR" : 1098 , "TV" : 885764 , "BC" : 304303 , "RC" : 0 , "RO" : 0 , "CH" : [  |
| santa-clara-ca | 2022-11-08 | denominator | 550,602 | VERIFIED | 754 1,259,821 1,009,422 40,694 509,908 550,602 92.61% 54.55% 43.70% |
| santa-clara-ca | 2022-11-08 | numerator | 293,148 | VERIFIED | "BCxContest" : 0 , "VF" : 1 , "TP" : 754 , "PR" : 671 , "TV" : 1009422 , "BC" : 293148 , "RC" : 0 , "RO" : 0 , "CH" : [  |
| santa-clara-ca | 2024-11-05 | denominator | 765,495 | VERIFIED | 784 1,269,781 1,048,723 97,924 667,571 765,495 87.21% 72.99% 60.29% |
| santa-clara-ca | 2024-11-05 | numerator | 460,325 | VERIFIED | "BCxContest" : 0 , "VF" : 1 , "TP" : 784 , "PR" : 686 , "TV" : 1031980 , "BC" : 460325 , "RC" : 0 , "RO" : 0 , "CH" : [  |
| tehama-ca | 2012-06-05 | denominator | 13,968 | VERIFIED | 46 43,209 30,476 3,687 10,281 13,968 73.60% 45.83% 32.33% |
| tehama-ca | 2012-06-05 | numerator | 9,993 | VERIFIED | m. FENU Tehama 46 46 100% 30,476 9,993 32.8% Jun 5 8:24 p.m. Jun 6 1:29 a.m. CCU T |
| tehama-ca | 2012-11-06 | denominator | 23,261 | VERIFIED | 46 43,306 31,174 8,032 15,229 23,261 65.47% 74.62% 53.71% |
| tehama-ca | 2012-11-06 | numerator | 17,559 | VERIFIED | m. FENU Tehama 46 46 100.0% 31,174 17,559 56.3% Nov 6 9:03 p.m. Nov 7 12:37 a.m. FENU |
| tehama-ca | 2014-06-03 | denominator | 13,016 | VERIFIED | 46 43,659 30,492 3,416 9,600 13,016 73.76% 42.69% 29.81% |
| tehama-ca | 2014-06-03 | numerator | 8,976 | VERIFIED | Tehama 46 46 100.0% 30,492 8,976 29.4% Jun 3 8:25 p.m. Jun 4 1:28 a.m. CCU |
| tehama-ca | 2014-11-04 | denominator | 15,791 | VERIFIED | 46 43,727 30,169 4,527 11,264 15,791 71.33% 52.34% 36.11% |
| tehama-ca | 2014-11-04 | numerator | 10,558 | VERIFIED | Tehama 46 46 100.0% 30,169 10,558 35.0% Nov 4 8:26 p.m. Nov 5 12:26 a.m. CCU |
| tehama-ca | 2016-11-08 | denominator | 24,541 | VERIFIED | 46 43,753 32,555 7,489 17,052 24,541 69.48% 75.38% 56.09% |
| tehama-ca | 2018-11-06 | denominator | 21,147 | VERIFIED | 46 43,847 33,286 5,583 15,564 21,147 73.60% 63.53% 48.23% |
| tehama-ca | 2022-11-08 | denominator | 20,819 | VERIFIED | 40 46,966 37,131 3,258 17,561 20,819 84.35% 56.07% 44.33% |
| tehama-ca | 2022-11-08 | numerator | 11,878 | VERIFIED | nofficial Precinct Report Precincts Reported: 40 of 40 (100.00%) Voters Cast: 11,878 of 37,115 (32.00%) GOVERNOR (Vote f |
| tehama-ca | 2024-11-05 | denominator | 26,867 | VERIFIED | 40 46,304 37,488 4,426 22,441 26,867 83.53% 71.67% 58.02% |
| tehama-ca | 2024-11-05 | numerator | 13,109 | VERIFIED | 3rd Unofficial Report Precincts Reported: 40 of 40 (100.00%) Voters Cast: 13,109 of 37,488 (34.97%) Cards Cast: 13,109 P |
