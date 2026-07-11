# SF County population 21+ by sex — 1900 / 1910 / 1920 censuses

Status: COMPLETE — 1920 exact; 1900 exact; 1910 males exact + females exact-core (104,857) plus estimated 21-24 split (no printed sub-state female 21+ exists for 1910; see dead ends)

SUMMARY TABLE (SF county = city; each figure includes age-unknown persons in 21+, the NHGIS convention, verified against printed male 21+ in all three years):
| Census | Males 21+ | Females 21+ | Total 21+ |
|--------|-----------|-------------|-----------|
| 1900 | 128,985 (printed; exact) | 100,910 (exact identity) | 229,895 |
| 1910 | 175,951 (printed; exact) | ≈121,600 ± 350 (exact core 104,857 + est. 21-24 ≈ 16,750) | ≈297,550 (297,117-297,850) |
| 1920 | 201,057 (exact sum) | 165,170 (exact sum) | 366,227 (= NHGIS exactly) |

## Targets
- 1900: males 21+ (expect ~128,985 per repo/NHGIS), females 21+, total 21+
- 1910: males 21+ (expect ~175,951), females 21+, total 21+
- 1920: males 21+, females 21+, total 21+ (expect total 366,227 per repo/NHGIS)

Sanity: SF total pop 1900 = 342,782; 1910 = 416,912; 1920 = 506,676.

## Findings

### 1900 — SOLVED EXACTLY (males printed; females by exact printed-complement identity)

RESULT 1900: males 21+ = 128,985; females 21+ = 100,910; total 21+ = 229,895 (each incl. age-unknown, per the NHGIS convention confirmed below).

Sources (all Twelfth Census, Census Reports Volume II, "Population Part II"):
1. Table 26 "Persons of school, militia, and voting ages, by sex, general nativity, and color, by counties: 1900", California, San Francisco county row, printed page 176.
   PDF: https://www2.census.gov/library/publications/decennial/1900/volume-2/volume-2-p6.pdf (PDF page 25 of 98). Crops: t26ca-25.png, t26sf_left-25.png, t26sf_right-25.png.
   - MALES 21 YEARS AND OVER: native white 60,758 + foreign white 56,102 + negro 619 + other colored (Chinese/Japanese/Indian) 11,506 = 128,985 = EXACTLY the NHGIS figure.
   - 5 TO 20 YEARS INCLUSIVE, male: 37,972 + 2,956 + 202 + 1,555 = 42,685; female: 40,104 + 3,229 + 182 + 672 = 44,187.
   - (Males 18-44: 54,522 + 31,988 + 451 + 8,719.)
2. Table 27 "Persons of school, militia, and voting ages ... for places having 2,500 inhabitants or more: 1900", San Francisco city row, printed page 212, same PDF (PDF page 61; predecessor render ocr1900p6/pg61-61.png). ALL figures identical to Table 26 (city = county): 5-20 male 37,972/2,956/202/1,555, female 40,104/3,229/182/672; males 21+ 60,758/56,102/619/11,506. Independent cross-check PASSED.
3. Table 9 "Ages by periods of years of the aggregate population, classified by sex, general nativity, and color, for cities having 25,000 inhabitants or more: 1900", San Francisco, Cal., printed page 143.
   PDF: https://www2.census.gov/library/publications/decennial/1900/volume-2/volume-2-p5.pdf (PDF page 143 of 149). Crops: sf1900_t9-143.png, sf1900_t9zoom-143.png, sf1900_t9fb-143.png.
   Aggregate male | female: All ages 184,866 | 157,916 (=342,782 total, matches published SF total). Under 1: 2,803 | 2,631; 1-4: 10,393 | 10,188; 5-9: 13,843 | 13,929; 10-14: 12,042 | 12,615; 15-19: 13,550 | 14,069; 20-24: 17,653 | 18,375; 25-29: 19,212 | 17,973; 30-34: 19,446 | 14,842; 35-44: 33,474 | 22,350; 45-54: 19,844 | 14,686; 55-64: 11,563 | 9,328; 65+: 7,548 | 6,080; Age unknown: 3,495 | 850.
   Column-sum checks: male brackets sum to 184,866 EXACT; female brackets sum to 157,916 EXACT; also native-born female column sums to its printed total 111,616 EXACT and foreign-born female column to 46,300 EXACT, and every aggregate row = native+foreign row. (Note: an early low-res read of female under-1 as 2,681 made the column look 50 over; 420-dpi re-read + native(2,623)+foreign(8) row check settles it at 2,631.)

Method (exact identity, no estimation):
  persons 21+ (incl. age-unknown) = total, all ages − under-5 − (5-20 inclusive)
  Males:   184,866 − (2,803 + 10,393) − 42,685 = 184,866 − 55,881 = 128,985 → EXACTLY equals the printed Table 26/27 "Males 21 years and over" and NHGIS. This proves (a) the identity is consistent across the two printed tables and (b) age-unknown persons (male 3,495) are counted inside the printed 21+ figure — same convention NHGIS uses (confirmed on 1920 too).
  Females: 157,916 − (2,631 + 10,188) − 44,187 = 157,916 − 57,006 = 100,910.
  Split of the female figure: known-age 21+ = 100,060; age unknown = 850 → 100,910.
  (Implied SF 1900 21-24/20-24 ratios, used below for 1910: male 14,403/17,653 = 0.8158; female 14,801/18,375 = 0.8055.)

TOTAL 21+ 1900 = 128,985 + 100,910 = 229,895. Reconciliation: male target 128,985 hit exactly.

### 1910 — males 21+ CONFIRMED at 175,951 (printed); females 21+ = 121,600 ± 350 (exact core 104,857 + estimated 21-24 split; the 1910 census NEVER printed female 21+ below state level — see dead ends)

RESULT 1910: males 21+ = 175,951 (printed, incl. age-unknown); females 21+ ≈ 121,600 (hard components: 104,857 exact = females 25+ incl. unknown; + estimated females 21-24 ≈ 16,750, credible range 16,309-17,042); total 21+ ≈ 297,550 (range 297,117-297,850).

Sources:
1. Males 21+ printed = 175,951: Thirteenth Census (1910), Volume I "Population 1910: General Report and Analysis", Chapter XI "Voting age, militia age, and naturalization", table "Males 21 years of age and over in cities having, in 1910, 100,000 inhabitants or more: 1910, 1900, and 1890", printed page ~1052; San Francisco row shows 175,951 (1910) and 128,985 (1900). Read via archive.org OCR of the volume (local c1910v1.txt, hit at line 1264097 within the "MALES 21 YEARS OF AGE AND OVER" city table). Corroborated in "Abstract of the Census ... with Supplement for California" (local OCR c1910abstract_ca.txt line ~76390): same city table prints 175,951 / 128,985.
2. Age by sex for SF: Volume I, Chapter IV "Age Distribution" general tables, Table 50 "Distribution by age periods of the population in cities having from 100,000 to 500,000 inhabitants: 1910", San Francisco, Cal., printed page 461.
   PDF: https://www2.census.gov/library/publications/decennial/1910/volume-1/volume-1-p7.pdf (PDF page 25 of 70). Crop: sf1910_left-25.png.
   Population Total | Male | Female: All ages 416,912 | 236,901 | 180,011 (m+f = 416,912 = published SF total ✓).
   Male | Female by bracket: Under 5: 14,866 | 14,312 (single yrs: U1 3,169|2,984; 1: 2,988|2,892; 2: 3,162|3,064; 3: 2,898|2,856; 4: 2,649|2,516); 5-9: 12,522 | 12,386; 10-14: 12,379 | 12,443; 15-19: 16,871 | 15,594; 20-24: 26,070 | 20,419; 25-29: 30,757 | 21,136; 30-34: 28,090 | 18,460; 35-39: 23,490 | 16,080; 40-44: 19,764 | 12,665; 45-49: 15,490 | 10,231; 50-54: 11,550 | 7,884; 55-59: 7,135 | 5,307; 60-64: 6,168 | 4,877; 65-69: 3,708 | 3,297; 70-74: 2,384 | 2,244; 75-79: 1,368 | 1,317; 80-84: 593 | 611; 85-89: 175 | 211; 90-94: 34 | 68; 95-99: 6 | 7; 100+: 2 | 3; Age unknown: 3,479 | 459.
   Column-sum checks: male brackets sum to 236,901 EXACT; female brackets sum to 180,011 EXACT.

Arithmetic:
  Males 25+ known-age = 236,901 − (14,866+12,522+12,379+16,871+26,070) − 3,479 = 150,714; incl. unknown = 154,193.
  Implied males 21-24 = 175,951 − 154,193 = 21,758 → implied males aged 20 = 26,070 − 21,758 = 4,312 (16.5% of the 20-24 bracket; cf. SF 1920 male 17.2%, SF 1900 male 18.4%) → PLAUSIBLE, and it confirms 175,951 INCLUDES the 3,479 age-unknown males (excluding them would force males-aged-20 = 833, impossible).
  Females: 25+ known-age = 180,011 − (14,312+12,386+12,443+15,594+20,419) − 459 = 104,398; incl. unknown = 104,857 (EXACT floor for f21+ less the 21-24 group).
  Females 21-24 must be estimated (bracket 20-24 = 20,419; the 1910 census prints no female 21-split for SF; single-years city table covers only cities of 500,000+, which excludes 1910 SF):
   - Splitter references (21-24 as share of 20-24): SF male 1910 = 0.8346 (derived above); SF female 1900 = 0.8055 (exact, this file); SF female 1920 = 0.8296 (exact, 1920 section); CA-state female 1910 = 0.7988 and male 1910 = 0.8078 (printed single years: Vol I Table 43 "Distribution by age periods ... and by each year of age for persons under 25, by divisions and states: 1910", California, printed p.364; PDF https://www2.census.gov/library/publications/decennial/1910/volume-1/volume-1-p6.pdf PDF page 76; crops t43ca_bot-076.png, t43ca_2124-076.png: CA female 20: 20,740; 21: 19,325; 22: 20,628; 23: 21,074; 24: 21,290; male 20: 25,196; 21: 25,117; 22: 25,806; 23: 26,789; 24: 28,156); CA-state 1900 female = 0.7942, male = 0.7942 (printed single years: 1900 Vol II Part II Table 2, California, printed p.14; PDF volume-2-p5.pdf PDF page 14; crop t2ca14-014.png: CA 1900 female 20: 13,689; 21: 12,411; 22: 13,199; 23: 13,247; 24: 13,964; male 20: 14,414; 21: 13,406; 22: 13,653; 23: 14,036; 24: 14,530).
   - Estimators for SF female 1910 ratio → f(21-24): (a) SF-male-1910 ratio 0.8346 → 17,042 (upper; SF female ratio ran 0.010 below male in 1900, equal in 1920); (b) interpolate SF female's own 1900→1920 ratios → 0.8176 → 16,694; (c) CA-anchored ratio-of-ratios SFf = CAf1910 × (SFm1910/CAm1910) = 0.7988×(0.8346/0.8078) = 0.8253 → 16,852; (d) CA female 1910 + SF-CA female gap from 1900 grown in step with the male gap → 0.813-0.815 → ~16,620; (e) raw CA female ratio 0.7988 → 16,309 (lower; ignores SF's urban skew).
   - Point estimate: f(21-24) ≈ 16,750 (central to b/c/d), credible range 16,309-17,042.
  Females 21+ ≈ 104,857 + 16,750 = 121,607 → report 121,600 ± 350 (range 121,166-121,899). Age-unknown handling: the 459 unknown-age females are inside the exact 104,857 core (same convention as males/NHGIS).

TOTAL 21+ 1910 ≈ 175,951 + 121,600 = 297,550 (range 297,117-297,850). Reconciliation: male target 175,951 matched by two printed sources and shown arithmetically consistent with Table 50 only if age-unknown males are included — same convention as 1900/1920.

### 1920 — SOLVED (summed from published age table; reconciles with NHGIS exactly)
Source: Fourteenth Census of the United States (1920), Volume II "Population: General Report and Analytical Tables", Chapter 3 general tables, Table 15: "Distribution by age periods for the total population and by single years of age for persons under 25, for population classes, by sex, for cities having 500,000 inhabitants or more: 1920", San Francisco, Calif., printed page 304.
PDF: https://www2.census.gov/library/publications/decennial/1920/volume-2/41084484v2ch04.pdf (PDF page 19 of 95)
Local copy: scratchpad/41084484v2ch04.pdf; rendered crops sf1920_top_left.png, sf1920_bot_left.png

All classes, by sex (male / female), San Francisco 1920:
- All ages: 272,703 / 233,973 (total 506,676 ✓)
- Age brackets 21+ male: 21-24=19,532 (single yrs 21:4,772 22:4,684 23:4,830 24:5,246), 25-29=27,779, 30-34=28,640, 35-39=29,719, 40-44=24,404, 45-49=20,939, 50-54=16,740, 55-59=11,596, 60-64=8,422, 65-69=4,927, 70-74=3,284, 75-79=1,681, 80-84=749, 85-89=267, 90-94=66, 95-99=12, 100+=1 → known-age male 21+ = 198,758; age unknown male = 2,299 → 201,057
- Age brackets 21+ female: 21-24=18,545 (21:4,206 22:4,495 23:4,806 24:5,038), 25-29=25,909, 30-34=23,955, 35-39=22,813, 40-44=18,823, 45-49=15,428, 50-54=12,424, 55-59=8,960, 60-64=6,976, 65-69=4,391, 70-74=3,160, 75-79=1,830, 80-84=912, 85-89=331, 90-94=93, 95-99=24, 100+=4 → known-age female 21+ = 164,578; age unknown female = 592 → 165,170
- Total 21+ incl. age unknown = 201,057 + 165,170 = 366,227 = EXACTLY the NHGIS figure in repo. Confirms convention: age-unknown persons are counted as 21+.
- 20-year-olds (excluded): male 4,050, female 3,808. Bracket check: 20-24 male 23,582 = 4,050+19,532 ✓; female 22,353 = 3,808+18,545 ✓. All bracket M+F sums match printed totals column.

RESULT 1920: males 21+ = 201,057; females 21+ = 165,170; total 21+ = 366,227 (each incl. age-unknown).
TODO: confirm against directly-printed 21+ figures in 1920 Vol III California county table (citizenship of persons 21 and over).

## Dead ends / URLs tried
Searched exhaustively for a PRINTED female-21+ (or single-years-by-sex) figure for SF below the state level; none exists in the decennial volumes for 1900 or 1910:
- 1900 Vol II Part II ages section has only Tables 1-9 (TOC at PDF volume-2-p5.pdf page 1): single years by sex exist ONLY by states/territories (Table 2); the city age table (Table 9) stops at 5-yr/10-yr brackets (20-24 etc.), so no direct female 21-split for cities. (Solved instead via the exact Table 9 + Table 26/27 complement identity above.)
- 1910 Vol I Table 49 "…by each year of age for persons under 25, in cities of 500,000 inhabitants or more" (printed p.437, volume-1-p7.pdf PDF page 1) covers only cities ≥500,000 → SF (416,912) EXCLUDED in 1910; Table 50 (100,000-500,000 cities) has single years only under age 5.
- 1910 Vol I Chapter XI: "Females 21 years of age and over, by divisions and states: 1910" (printed p.1065) is STATES ONLY; the cities tables in ch. XI are males-only.
- 1910 Vol II California chapter (IPUMS mirror https://usa.ipums.org/usa/resources/voliii/pubdocs/1910/Vol2/36894832v2ch02.pdf, 142 pp; = printed pp.~131-217) and the Abstract-with-California-supplement: county/city "Composition and characteristics" tables print MALES OF VOTING AGE only; school/illiteracy age sections are by nativity, not by sex.
- Coordinator's IPUMS link https://usa.ipums.org/usa/resources/voliii/pubdocs/1910/States/41033935v1-8ch4.pdf labeled "Vol I age chapter" is actually the Abstract of the Census with Supplement for California (title page render ch4a-001.png) — same content as c1910abstract_ca.txt.
- 1920 Vol II Chapter III (41084484v2ch03.pdf, contents page render c3b-002.png): its 1910 comparatives (Table 13) give single years under 25 for 1910 for BOTH SEXES COMBINED by state only ("each sex" columns are 1920-only) — no 1910 city 21+ by sex.
- c1910v1.txt greps for "single years", "voting", "females 21": all city-level single-years/21+ tables are the ones cited above; nothing further.

## Local file inventory (scratchpad)
- volume-2-p5.pdf / volume-2-p6.pdf = 1900 Census Reports Vol II Population Part II, parts 5 (printed ~1-150: ages Tables 1-9) and 6 (printed ~152-249: Tables 26-27) from https://www2.census.gov/library/publications/decennial/1900/volume-2/
- volume-1-p6.pdf / volume-1-p7.pdf = 1910 Vol I General Report and Analysis, printed 289-436 and 437-506, from https://www2.census.gov/library/publications/decennial/1910/volume-1/
- c1910v1.txt = archive.org OCR text of 1910 Vol I (cu31924070698315); c1910abstract_ca.txt = archive.org OCR of Abstract + CA supplement
- 41084484v2ch04.pdf / 41084484v2ch03.pdf = 1920 Vol II chapters (ch. 3 general tables incl. Table 15 used for the 1920 result; ch. III age-distribution contents)
- Key crops: sf1900_t9*.png (1900 Table 9 SF), t26sf_*.png + ocr1900p6/pg61-61.png (1900 Tables 26/27 SF), sf1910_left-25.png (1910 Table 50 SF), t43ca_*.png (1910 CA single years), t2ca14-014.png (1900 CA single years), sf1920_*.png (1920 Table 15 SF)
