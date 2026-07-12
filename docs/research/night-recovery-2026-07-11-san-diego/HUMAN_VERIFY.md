# San Diego deep-history night-count recovery — human-verification packet

Operator's hand-check packet for the 25 San Diego County election-night dossiers
(`1871-09-06.md` through `1920-11-02.md`) in this directory. Built by reading
every dossier's "Human-verification asks" section and, where present, its dated
"Verification pass" appendices (adversarial re-reads already done by an agent).

**How to read a scan**: every path below is relative to the repo root, under
`mirror/cdnc/screenshots/` (gitignored — view locally, not on GitHub). Open the
PNG at 100%+ zoom; most are already tight digit-level crops. A handful of
1884-era dossiers cite HathiTrust page-viewer screenshots instead (noted where
that applies) — same idea, different source site.

**The rule**: the human's reading wins. Every "claimed" value below is this
project's own read, not a settled fact. If your read differs from the claim,
your read replaces it — update the source dossier's transcription and re-run
the arithmetic in that dossier before touching any downstream CSV/summary.

**What NOT to re-check**: section 4 ("Resolved by adversarial re-read") lists
asks a follow-up agent pass already confirmed or corrected against fresh,
independently-cropped captures. Skip those unless you have a specific reason
to distrust the re-read.

**Scope note**: 1914 and 1922 have no digitized San Diego Union issues in CDNC
and are out of scope for this wave (see `README.md`). 1882's floor has no
certified denominator at all (share is NULL, not a typo).

---

## 1. Priority asks

Items where a misread would move a HEADLINE number (the reported night-count
floor, its share of certified final, or which of two competing printed totals
is correct) — not just a single precinct row. 43 items across 16 elections.

### 1872-11-05 (President floor 536, share 61.4%)

- `mirror/cdnc/screenshots/sd_18721106_p3_crop_ward5_grant.png`: Fifth Ward
  President line — claimed **Grant 38, Greeley 3**; the "8" is the one digit
  in this dossier flagged as visibly ambiguous against "5". Fail: reads as 35.
  Impact: city Grant total 289→286, contest sum 536→533 (~0.6%).

### 1875-09-01 (Governor floor 720, share 45.0% — UNRESOLVED consistency conflict)

The paper printed TWO different Governor totals in the same article: an
opening-summary paragraph (Phelps 238/Irwin 303/Bidwell 125, sum 666, with its
own internal arithmetic error — stated plurality 55 vs. the actual 65) and a
precinct-by-precinct table (sum 720, used as this dossier's floor). Bidwell's
figure matches exactly across both (125=125); Phelps/Irwin do not.

- `mirror/cdnc/screenshots/sd_18750902_p3_crop_gov_full2.png`: opening-summary
  line — claimed **Phelps 238, Irwin 303, Bidwell 125, "Plurality for Irwin,
  55"** (303−238=65≠55, a printed error independent of anything below). Fail:
  any digit reads differently. Impact: this is the competing 666-vote total;
  resolving it changes which number (720 vs 666, a 54-vote/7.5% gap) is right.
- `mirror/cdnc/screenshots/sd_18750902_p3_crop_3rdward_recheck.png`: Third
  Ward — claimed **Phelps 94, Irwin 83, Bidwell 24** (already read twice,
  identical both times). Fail: any re-tally landing differently. Impact:
  largest single driver of the 720-vs-666 gap.
- `mirror/cdnc/screenshots/sd_18750902_p3_crop_4thward_recheck.png`: Fourth
  Ward — claimed **Phelps 117, Irwin 65, Bidwell 34** (already read twice,
  identical both times). Fail: any re-tally landing differently. Impact:
  second-largest driver of the gap.
- Reconciliation: re-tally all 7 precinct rows (First 14/50/5, Second
  27/20/9, Third 94/83/24, Fourth 117/65/34, Fifth 35/20/26, Monument
  16/13/13, Central 23/18/14) against claimed sums Phelps 326/Irwin
  269/Bidwell 125 = 720. Fail: a different column sum, OR a resolution that
  identifies the specific misread digit reconciling 720 with the paper's own
  666. Impact: determines whether the reported floor should be 720, 666, or
  something else.

### 1879-09-03 (Governor floor 614, share 43.5% — sole numerator)

- `mirror/cdnc/screenshots/sd_18790904_p1_crop_election_gov4.png`: claimed
  **"Perkins 331, Glenn 230, White 53"** (sum 614). Fail: any digit differs.
  Impact: this ONE line is the entire reported floor — no precinct breakdown
  exists anywhere in the issue to cross-check it.

### 1880-11-02 (President floor 747 — LOW confidence, multiple unresolved arithmetic flags)

- `mirror/cdnc/screenshots/sd_18801103_p4_crop_hancock151.png`: city
  Recapitulation Hancock figure — claimed **"151"**; fail if it actually
  reads "201" (would eliminate the 50-vote gap against the independently
  summed ward total of 201). Impact: resolves which of two printed/derived
  city totals is right; does not itself move the reported 747 (already the
  resummed figure) but is central to the dossier's confidence.
- `mirror/cdnc/screenshots/sd_18801103_p4_crop_finaltotal_garfield.png` (and
  `_finaltotal_zoom.png`): grand-total line — claimed **"Garfield 345,
  Hancock 260, Weaver 10, Majority for Garfield, 185"** (345−260=85≠185, a
  100-vote contradiction inside one printed sentence). Fail: re-read all
  three figures to find which is the compositor error. Impact: this printed
  total (615) sits 132 votes below the reported 747-vote floor; confirms or
  undermines the decision to trust the resummed table over the paper's own
  total line.

### 1882-11-07 (Governor floor 1,103, share NULL — no certified denominator — sole numerator)

- `mirror/cdnc/screenshots/sd_18821108_p3_crop_gov_tight3.png`: claimed
  **"Estee 614, Stoneman 489"** (sum 1,103). Fail: either digit differs.
  Also re-check against the 1879-09-03 dossier's Perkins figure (also 614) —
  confirm these are two independently-read numbers from two different issues
  that happen to coincide, not a copy-paste artifact. Impact: this line is
  the entire reported number; there is no certified denominator for this
  election at all, so this is the ONLY figure this dossier produces.

### 1886-11-02 (Governor floor 1,031, share 36.5%)

- `mirror/cdnc/screenshots/sd_18861103_p3_elcajon4.png`: Fourth Ward —
  claimed **Swift 101, Bartlett 72, Russell 8, Wigginton 5**; fail if
  Wigginton reads 8 (Fourth Ward becomes 189, grand total 1,034). Impact:
  +3 votes (0.3%) if wrong.
- `mirror/cdnc/screenshots/sd_18861103_p3_rightcol_b.png`: Green Valley —
  claimed **Swift 9, Bartlett 5** (crop sits at the tight edge of the
  capture, the only precinct read this way). Fail: either digit differs.

### 1888-11-06 (President floor 3,288, share 40.1%)

- `mirror/cdnc/screenshots/sd_18881107_p5_crop_escondido_harrison5.png`:
  Escondido Harrison figure — claimed **136**; fail if the last digit is 8
  (138). Impact: ±2 votes, the dossier's only flagged [?] digit.
- `mirror/cdnc/screenshots/sd_18881107_p5_crop_escondido_top3.png`: San
  Pasqual — claimed **"35 Republican votes to 13 Democratic votes"**, used
  as a lower-confidence proxy for the President line (unlike the other 3
  outside precincts, which name Harrison/Cleveland explicitly). Fail: either
  number differs, OR a judgment call that this party-line dispatch should
  NOT be used as a President-contest proxy at all (would remove 48 votes
  from the 3,288 floor).

### 1894-11-06 (Governor floor 1,761 REVISED, share 24.7% — see ADDENDUM in the dossier)

- `mirror/cdnc/screenshots/sd_18941107_p5_fourthward_gov3.png`: Fourth Ward
  1st Precinct — claimed **Budd 36**; fail if it reads 30 or 39. This is the
  dossier's single most uncertain page-5 digit.
- `mirror/cdnc/screenshots/sd_18941107_p5_seventh_full3.png`: Seventh Ward
  1st Precinct — claimed **French 4** (sits at a line-wrap, unlike the
  Paradise precinct's parallel case, no independent total-vote check exists
  here). Fail if French is genuinely blank in print — drops the row from 80
  to 76 and the page-5 subtotal by 4.
- `mirror/cdnc/screenshots/sd_18941107_p2_delmar_line4x.png`: Del Mar
  (addendum) — claimed **Budd 20, Webster 26** (both blurred trailing
  digits; adopted reading is the only one matching the precinct's own
  printed "Total vote cast, 65"). Fail if either digit clearly reads
  otherwise AND the row no longer sums to 65.
- `mirror/cdnc/screenshots/sd_18941107_p2_col3_a.png` + `_oceanside_total.png`
  (addendum): Oceanside — claimed Governor row **Budd 34, Estee 32, French
  36, Webster 35** (sum 137), INCLUDED in the revised floor despite
  exceeding the precinct's own printed "Total vote cast 69" (judged to be
  the misprint, based on other down-ballot contests in the same block also
  exceeding 69). Fail: confirm the Lieutenant-Governor row below really does
  sum past 69 (supports "total is the misprint"); if the candidate digits
  themselves look wrong instead, drop Oceanside's 137 (revised floor would
  be 1,624, share 22.8% instead of 24.7%). **Largest-magnitude open item in
  this dossier.**

### 1898-11-08 (Governor floor 4,589, share 64.5% — WHOLE-TABLE LOW-MEDIUM confidence)

The entire precinct table underlying this floor (Gage 2,439 / Maguire 2,150)
is a hand-sum of ~68 rows: the table's own Total and Grand-total rows print
**blank** (confirmed twice — original pass and the 2026-07-12 verification
pass), one row-attribution error was already caught and fixed (Fifth/Sixth
Ward), and the 2026-07-12 verification pass explicitly could not attempt a
full re-tabulation ("out of budget/scope") and left every digit "STILL
AMBIGUOUS... neither strengthens nor weakens." This is the single
highest-uncertainty number in the whole campaign. Re-read at the
screenshot-segment level (fail = any digit in the segment disagrees with the
dossier's table):

1. `sd_18981109_p2_seg1b.png` — First Ward 1st-4th, Second Ward 1st-2d,
   Third Ward 1st-2d, Fourth Ward 1st-2d, Fifth Ward 1st-2d.
2. `sd_18981109_p2_sixth1.png` — Fifth Ward-2d (43/80), Sixth Ward-1st
   (107/95), Sixth Ward-2d (136/112) — this crop already fixed one
   row-attribution error; extra scrutiny warranted.
3. `sd_18981109_p2_seg2c.png` — Seventh Ward 1st-2d, Eighth Ward 1st-2d
   (85/97, 69/99, 96/92, 98/98) — soft digits, lowest-confidence city rows.
4. `sd_18981109_p2_seg3.png` — Banner through Descanso (rows 1-15).
5. `sd_18981109_p2_seg4.png` — Descanso through Jamul (rows 14-31).
6. `sd_18981109_p2_seg5.png` — Jamul through Moreland (rows 29-44).
7. `sd_18981109_p2_seg6.png` — Moreland through San Pasqual (rows 44-58).
8. `sd_18981109_p2_seg7.png` — San Pasqual through West Fallbrook (rows
   58-67), plus re-confirms the Grand total row is blank.
9. `sd_18981109_p2_totalrow.png` / `_crop_grandtotal_full.png` — re-confirm
   both summary rows are entirely blank.
10. **Full re-tabulation**: independently re-sum all ~68 rows × 2 columns
    (Gage/Maguire) from the screenshots, or from a sharper source. Fail: a
    re-tabulation landing on anything other than Gage 2,439 / Maguire 2,150
    (sum 4,589). This is the strongest possible check available, per both
    the original dossier and the follow-up pass.

### 1900-11-06 (President floor 3,672 city-only proxy, share 53.0% — UNRESOLVED consistency failure)

- `mirror/cdnc/screenshots/sd_19001107_p6_crop_citytotals_narrow2.png` (also
  `verify2_1900_*` re-crops): City Totals row — claimed Registered 4,280,
  **Voters 3,672**, McKinley 2,045, Bryan 1,596, Debs 133, Wooley 84.
  **CONSISTENCY FAILURE, unresolved through two verification passes**:
  McKinley+Bryan+Debs+Wooley = 3,858 exceeds the precinct's own "Voters"
  (total ballots cast) figure of 3,672 by 186 votes (5.1%) — a contest sum
  cannot exceed ballots cast, so at least one of these four digits is wrong,
  but no capture obtained (including a 2026-07-12 re-read from the
  least-lossy full-page source) is sharp enough to say which. The
  2026-07-12 pass DID rule out the leading hypothesis (McKinley misread
  ~200 too high, ~1,845) — every independent crop reads the leading digit
  clearly as "2". Fail/next step: any re-read that identifies which of
  McKinley/Bryan/Debs/Wooley/Voters is the misprint or misread digit.
  Impact: today's headline (3,672, a turnout proxy) sidesteps this failure,
  so it is not directly at risk — but resolving it could replace the proxy
  with a real per-candidate city floor of up to ~3,858, and would unblock
  hand-summing the ~90-row county grid (see Secondary).

### 1902-11-04 (Governor floor 4,202, share 65.1%)

- `mirror/cdnc/screenshots/sd_19021105_p3_hires_gov4.png` (also
  `_hires_pardee4.png`/`_pardee5.png`): Pardee figure — claimed **2,061**; a
  printed pointing-hand ornament glyph sits directly over the last digit.
  Fail: the obscured digit reads other than 1 (candidates considered: 4, 7).
  Impact: ±up to 6 votes to the 4,202 floor; does not change the
  certified-ceiling gate for any single-digit alternative.
- Same screenshot: Brower figure — claimed **358**; fail if this reads as
  "558" instead (visually close in this typeface; the high-res crop favors
  "3"). Impact: a "558" reading adds 200 votes (4.8%) to the floor.

### 1904-11-08 (President floor 6,300, share 87.0%)

- `mirror/cdnc/screenshots/sd_19041109_p3_hires_county6.png` (also
  `_hires_roosevelt.png`, `sd_19041109_roosevelt_sharp.png`): Roosevelt
  figure — claimed **3,794**; the leading "3" could visually pass for "5"
  at this scan's resolution. Fail: the leading digit is actually "5"
  (5,794) — note an alternate of 5,794 would ALSO fail the certified-total
  gate (>4,310) and break both printed-plurality cross-checks
  (3,794−1,187=2,607, 3,794−1,200=2,594, both matching printed pluralities
  exactly), so it would itself be strong evidence of a different
  transcription problem — but this is reasoning, not an independently
  confirmed pixel-level read. Impact: largest single figure in the
  6,300-vote floor (87.0% share); if genuinely misread, the election would
  fail its own certified-ceiling gate.

### 1906-11-06 (Governor floor 2,016, share 26.0%)

- `mirror/cdnc/screenshots/sd_19061107_p8_crop_col1c.png` (also
  `sd_19061107_p8_hires_gov5.png`, `sd_19061107_bell_final.png`): Bell
  figure — claimed **691**; fail if the third digit is not "1" (candidates
  considered: 3, 9).
- Same screenshots (also `sd_19061107_lewis_final3.png`): Lewis figure —
  claimed **216**; fail if the third digit is "8" instead (218) rather than
  "6". Impact for both: a few votes against the 2,016 floor; neither
  changes the certified-ceiling gate.

### 1908-11-03 (President table floor 6,028 / extended floor 6,841, share 64.1%/72.7%)

Three of twelve original asks were re-verified 2026-07-11 (see Resolved,
section 4); these eight-plus remain open:

- `sd_19081104_p6_cityrows_a.png` row "1st Ward, 4th Precinct": Bryan
  claimed **5** (fail: reads 6); Hisgen claimed **11** (fail: it's a
  smudge/other column — an 11-vote Hisgen precinct is an outlier here; up
  to −12 to the sum).
- `sd_19081104_p6_cityrows_a.png` row "1st Ward, 5th Precinct": Chafin
  claimed **10** (fail: reads 0/blank — unusually high for Prohibition
  here; −10 if wrong).
- `sd_19081104_p6_cityrows_d.png` row "9th Ward, 3rd Precinct": Bryan
  claimed **39** (fail: reads 29; −10 if wrong).
- `sd_19081104_p6_lakeside2.png` row "Lakeside": Chafin claimed **2** —
  STILL AMBIGUOUS per the 2026-07-11 pass (leans toward confirming 2 over
  the prose cross-check's 3, but resolution insufficient to call). Fail: a
  sharper read landing on 3 (+1, and reconciles the table-vs-prose 70-vs-71
  discrepancy).
- `sd_19081104_p6_county_d.png` row "Ramona": Bryan claimed **20** (fail:
  reads 30; +10 if wrong).
- `sd_19081104_p6_slrey_wide.png` row "San Luis Rey": Bryan claimed **25**
  (fail: reads 95 — rejected in the dossier because Democratic
  justice/congress votes in the same precinct were 26/22, but not
  independently re-confirmed; +70 if 95 is right). **Single
  largest-magnitude open ambiguity in this dossier.**
- `sd_19081104_p6_oce_pot.png` row "Potrero": Hisgen claimed **4** (fail:
  blank/other column; −4 if wrong).
- `sd_19081104_p6_county_a.png` row "Mesa Grande": Taft claimed **24**
  (fail: reads 26; +2 if wrong).

### 1910-11-08 (Governor floor 3,741, share 39.5%)

- `sd_19101109_p8_gov2.png`: claimed **Johnson (R) 1,958, Bell (D) 1,169,
  Wilson (S) 614** — Johnson's reading rests on an internal-consistency
  argument (must exceed State Printer Shannon's 1,947, per the article's own
  text) rather than a direct high-confidence pixel read. Fail: Johnson
  reads 1,938/1,968 (the Shannon-consistency argument then needs
  revisiting); Bell reads 1,149/1,109; Wilson reads 644/611. Also confirm
  there is NO fourth (Meads/Prohibition) line under Governor. Impact: this
  triplet IS the entire 3,741-vote floor.

### 1916-11-07 (President floor 24,811, share 67.9% — sole reported pair)

- `sd_19161108_p2_hughes_graf1.png`: claimed **"Hughes, 12,629; Wilson,
  12,182"** — no precinct breakdown was printed this election; only cross-
  check is the headline's own rounded "about 450" majority claim (447
  actual). Fail: any digit differs. Impact: this pair is the entire
  24,811-vote floor; there is no other printed source for this election
  night to check it against.

---

## 2. Secondary asks

Digits/checks that affect only a single precinct row, a context (non-target)
office, or a fully-corroborated figure — misreading these moves the headline
floor by a trivial amount or not at all. 114 items across 22 elections,
grouped by dossier (screenshot : claimed value : fail criterion, condensed).

### 1871-09-06 (Governor floor 545, share 42.4% — exact recap cross-check)

- `sd_18710907_p3_crop_newtown_gov2.png`: New Town — Booth 185, Haight 104.
- `sd_18710907_p3_crop_col1_upper2.png`: Old Town — Booth 43, Haight 74.
- `sd_18710907_p3_crop_col1_mid.png`: National City — Booth 28, Haight 12.
- `sd_18710907_p3_crop_col1_lower.png`: Central/Cajon — Booth 30, Haight 17.
- `sd_18710907_p3_crop_col1_bottom.png`: San Luis Rey — Haight 28, Booth 24
  (printed in that order).
- `sd_18710907_p3_crop_recap_gov2.png`: printed Recapitulation — Booth 310,
  Haight 235 (already exact-matches the independent precinct sum).

### 1872-11-05 (President floor 536, share 61.4%)

- `sd_18721106_p3_crop_natcity2.png`: First Ward Grant 35/Greeley 39; Second
  Ward Grant 33/Greeley 20/O'Conor 2.
- `sd_18721106_p3_crop_ward5recap.png`: Third Ward Grant 103/Greeley
  69/O'Conor 1; Fourth Ward Grant 80/Greeley 41/O'Conor 1.
- `sd_18721106_p3_crop_recap.png`: RECAPITULATION — Grant 289, Greeley 172,
  O'Conor 4, total city votes 470 (already exact-matches ward sum).
- `sd_18721106_p3_crop_natcity_nums.png`: National City — Grant 25, Greeley 5.
- `sd_18721106_p3_crop_sanluisrey.png`: San Luis Rey — Grant 18, Greeley 23.
- Final-sum re-add: 289+172+4=465 (city) + 30 (Nat'l City) + 41 (San Luis
  Rey) = 536.

### 1875-09-01 (Governor floor 720, share 45.0%)

- `sd_18750902_p3_crop_wardtable1.png`: First Ward — Phelps 14, Irwin 50,
  Bidwell 5.
- `sd_18750902_p3_crop_firstward_end.png`: Second Ward — Phelps 27, Irwin
  20, Bidwell 9.
- `sd_18750902_p3_crop_5thward_recheck4.png`: Fifth Ward — Phelps 35, Irwin
  20, Bidwell 26.
- `sd_18750902_p3_crop_monument_gov3.png`: Monument — Phelps 16, Irwin 13,
  Bidwell 13.
- `sd_18750902_p3_crop_col3_wards.png`: Central — Phelps 23, Irwin 18,
  Bidwell 14.

### 1876-11-07 (President floor 871, share 59.6% — doubly-corroborated total used)

- `sd_18761108_p3_crop_wards12.png`: First 22/50, Second 30/27, Third
  117/88, Fourth 137/54, Fifth 61/23 (Hayes/Tilden); city Recap 367/242.
- `sd_18761108_p3_crop_recap_outside.png`: National City — Hayes 39, Tilden 9.
- `sd_18761108_p3_crop_central_campo.png`: Monument 19/12, Central 45/22,
  Campo 22/29, San Luis Rey 41/25; outside-precincts Recap 167/97.
- `sd_18761108_p3_crop_totaltodate.png`: "TOTAL RESULT TO DATE" — Hayes 532,
  Tilden 339, majority 193 (the figure actually used as the numerator).
- Final re-add: city 367/242 (exact recap match) + outside 166/97 (1-vote
  drift vs. printed 167 for Hayes, already flagged, not used) → paper's own
  532+339=871 is the reported figure.

### 1879-09-03 (Governor floor 614, share 43.5%)

- `sd_18790904_p1_crop_election_gov2.png`: article's precinct list ("five
  Wards of San Diego, and the precincts of National, San Luis Rey and
  Forster") and the paper's "aggregate result... precluding any details"
  framing.

### 1880-11-02 (President floor 747, share 57.3%)

- `sd_18801103_p4_crop_ward1_zoom2.png`: 1st Ward Garfield 16/Hancock 29;
  2d Ward Garfield 17/Hancock 14/Weaver 1.
- `sd_18801103_p4_crop_ward4_line.png`: 4th Ward Garfield 122/Hancock 87
  (tight zoom rules out "37").
- `sd_18801103_p4_crop_ward5_zoom.png`: 5th Ward Garfield 55/Hancock 10.
- `sd_18801103_p4_crop_national_top.png` + `_national_zoom.png`: National
  Garfield 25/Hancock 6; Campo Garfield 12/Hancock 14.
- `sd_18801103_p4_crop_outside1.png`: San Luis Rey 23/21, Forster 12/18,
  Lyons 5/6, Mt. Fairview 19/6, Fall Brook 15/10.
- `sd_18801103_p4_crop_outside2.png`: Pala 7/17, Temecula 8/14.
- Final re-add: city Garfield 299 (exact recap match) / Hancock 201
  (vs. printed "151", already flagged as Priority above); outlying 126/112;
  grand total used = 425/313/9 = 747.

### 1882-11-07 (Governor floor 1,103, share NULL)

- `sd_18821108_p3_crop_state_ticket_top.png`: precinct list ("Returns from
  Twenty Precincts") and "impossible to present them... in detail"
  statement — confirms no precinct-level table exists to cross-check
  against.

### 1884-11-04 (President floor 812, share 41.3% — no [?] flags in this dossier)

- `sd_18841105_p3_crop_ward1pres.png`: Ward 1 — Blaine 25, Cleveland 20.
- `sd_18841105_p3_crop_ward5area.png`: Ward 2 — Blaine 35, Cleveland 21.
- `sd_18841105_p3_crop_area2.png`: Ward 3 — Blaine 115, Cleveland 60, St.
  John 2.
- `sd_18841105_p3_crop_area4.png`: Ward 4 — Blaine 165, Cleveland 79, St.
  John 3.
- `sd_18841105_p3_crop_area5.png`: Ward 5 — Blaine 76, Cleveland 25, St.
  John 3.
- `sd_18841105_p3_crop_colC2.png`: National City — Blaine 82, Cleveland 21,
  St. John 5.
- `sd_18841105_p3_crop_chollas_blaine2.png`: Chollas — Blaine 3, Cleveland 8.
- `sd_18841105_p3_crop_vicente_pres.png`: Vicente — Blaine 8, Cleveland 3.
- `sd_18841105_p3_crop_central_pres.png`: Central — Blaine 40, Cleveland 13.
- Final re-add: Blaine 549 + Cleveland 250 + St. John 13 = 812.

### 1886-11-02 (Governor floor 1,031, share 36.5%)

- `sd_18861103_p3_bernardo_line.png`: Bernardo — Swift 27, Bartlett 16,
  Russell 2.
- `sd_18861103_p3_elcajon3.png`: Third Ward — Swift 70, Bartlett 50, Russell
  5, O'Donnell 1 (note: the ward's own printed "Total vote 338" is NOT the
  Governor sum — do not conflate).
- `sd_18861103_p3_5thward_top.png`: Fifth Ward — Swift 89, Bartlett 45,
  Russell 9, Wigginton 4, O'Donnell 1.
- `sd_18861103_p3_rightcol_a.png` / `_zward_top2.png`: Oceanside/Poway/
  Perris/National City/Temecula/Lyons lines (Perris's internal check, Total
  vote 42 = 22+15+5, is the strongest validation in this dossier).
- Final re-add: candidate columns Swift 583/Bartlett 354/Russell
  73/Wigginton 10/O'Donnell 11 = 1,031.

### 1888-11-06 (President floor 3,288, share 40.1%)

- `sd_18881107_p5_pan2_pres_rowL.png`: Pacific Beach/Old Town/2d-Ward-1st —
  26/14/4, 61/55/—, 219/154/5.
- `sd_18881107_p5_pan2_pres_rowR.png`: remaining 10 table columns —
  143/77/4, 117/97/2, 181/90/—, 128/138/1, 110/87/5, 250/115/—, 80/37/6,
  106/85/—, 176/74/5, 174/130/10 (carries the bulk of the numerator).
- `sd_18881107_p5_crop_colC_after_table.png`: Escondido Cleveland 47/Fisk 4.
- `sd_18881107_p5_ztable_esc.png`: Lakeside — "Total vote, 22. Harrison 9,
  Cleveland 13" (exact match).
- `sd_18881107_p5_ztable_pres3.png`: Monument — "total... 65. 45 Harrison,
  15 Cleveland, 5 Fisk" (exact match).
- `sd_18881107_p5_pan2_pres_majority.png`: printed table Majority for
  President — claimed 557; already noted as inconsistent with the
  column-sum majority (618) but recorded as printed, not "fixed" — no
  headline impact either way.
- Final re-add: table 1,771/1,153/42=2,966 + outside 187+48+22+65=322 =
  3,288.

### 1890-11-04 (Governor floor 184, share 2.5%)

- `sd_18901105_p5_perris_delmar2.png`: Perris — Markham 70, Pond 41; Del Mar
  — "Total vote cast 45... Markham 20, Pond 24" (1-vote drift vs. total,
  worth a second look but immaterial to the 184 floor).
- `sd_18901105_p5_lakeside.png`: Lakeside — Markham 13, Pond 16.
- `sd_18901105_p5_escondido_top.png`: confirms no Markham/Pond line exists
  between the Escondido City header and "Bowers 82, Curtis 26" — fail (and
  add Escondido City to the floor) only if a Governor line is found.
- `sd_18901106_p5_wardtable_top.png`: confirms the day+2 "COUNTY TICKET"
  table's first row is "Superior Judges—" with no Governor row above it.
- Final sum: 111+44+29 = 184.

### 1892-11-08 (President floor 673, share 8.7% — no [?] flags)

- `sd_18921109_p5_crop_otaynum3.png`: Otay — total 89, Harrison 45,
  Cleveland 35, Weaver 5, Bidwell 1.
- `sd_18921109_p5_crop_col1lower.png`: Spring Valley-Chollas — total 39,
  Harrison 25, Cleveland 9, Weaver 1, Bidwell 4 (exact total match).
- `sd_18921109_p5_crop_alpine2.png`: Alpine — total 50, Harrison 30,
  Cleveland 6, Bidwell 2, Weaver 9.
- `sd_18921109_p5_crop_tiaj.png`: Tia Juana — total 23, Harrison 6,
  Cleveland 1, Weaver 6; Del Mar — total 57, Harrison 20, Cleveland 24,
  Weaver 13.
- `sd_18921109_p5_crop_cv_ej.png`: Chula Vista — total 82, Harrison 47,
  Cleveland 17, Weaver 10.
- `sd_18921109_p5_crop_ej_cor.png`: El Cajon — total 137, Harrison 67,
  Cleveland 45, Weaver 10, Bidwell 12.
- `sd_18921109_p5_crop_coronado_pres2.png`: Coronado — total 194, Harrison
  95, Cleveland 66, Bidwell 2, Weaver 24; re-cropped twice already to rule
  out 96.
- `sd_18921109_p5_crop_wildomar_pres2.png`: Wildomar (explicitly partial) —
  Harrison 12, Cleveland 6, Bidwell 16, Weaver 2.
- Final re-add: Harrison 347/Cleveland 209/Weaver 80/Bidwell 37 = 673.

### 1894-11-06 (Governor floor 1,761 revised, share 24.7%)

- `sd_18941107_p5_firstward.png`: First Ward 1st — Estee 51, Budd 43,
  Webster 29, French 8.
- `sd_18941107_p5_zseventh.png`: Eighth Ward 1st — Estee 32, Webster 38, no
  Budd/French printed; fail only if a Budd/French figure is found.
- `sd_18941107_p5_col4_low.png`: Coronado — Estee 97, Budd 62.
- `sd_18941107_p5_col4_escondido.png`: Paradise — Budd 12, Estee 25, French
  2 (inferred from the exact total-vote check), Webster 3.
- `sd_18941107_p2_escondido_gov2.png` (addendum): Escondido City — Estee 71,
  Budd 39, Webster 48, French 8 (this Budd digit was the one the original
  page-5 OCR could not read; now image-verified).
- Exact-total-match rows to spot-check (addendum): Chula Vista 85, Foster
  20, La Mesa 49, Otay 96 — any drift here breaks the dossier's strongest
  internal validation.
- Final re-add: page-5 subtotal 756 + page-2 addendum subtotal 1,005 =
  1,761; candidate columns Estee 777/Budd 476/French 103/Webster 405.

### 1896-11-03 (President floor 6,315, share 81.3% — mostly verification-pass-confirmed, see section 4)

- `sd_18961104_p5_ztest_ward.png`: MESA GRANDE precinct — Bryan's figure is
  partly obscured by a page crease; the 2026-07-12 pass narrowed the
  low-confidence range from 19-22 to roughly 23-25 but it remains STILL
  AMBIGUOUS. **Not used in any calculation** (only Alpine was spot-checked
  into the narrative; the RECAPITULATION figure, not a hand re-derived
  county sum, is the number of record).

### 1898-11-08 (Governor floor 4,589, share 64.5%)

No secondary items — every open ask in this dossier is Priority (see section
1); the entire table is flagged low-medium confidence.

### 1900-11-06 (President floor 3,672 city-only proxy, share 53.0%)

- `sd_19001107_p6_crop_article_majority.png` attempt failed (wrong region
  captured); the prose "majority for McKinley of over ___" sentence (section
  2.27) has never been successfully vision-read. Would supply an
  independent McKinley-minus-Bryan plurality cross-check for the city if
  read.
- `sd_19001107_p6.png` / `_crop_rows1.png` / `_crop_rows2.png`: the ~90-row
  county precinct table (President columns McKinley/Bryan/Debs/Wooley) was
  captured but never hand-summed; the table's own Grand total row is
  confirmed blank. A full county-wide floor would require a human (or a
  sharper tool pass) to sum these four columns across all rows.
- Final sum used: 3,672 (city total votes cast, prose-confirmed, HIGH
  confidence, not itself in dispute).

### 1902-11-04 (Governor floor 4,202, share 65.1%)

- Same screenshot as the Priority items: Lane figure — claimed 1,729; fail
  if any digit differs.
- Same screenshot: Kanouse figure — claimed 54; fail if any digit differs.
- `sd_19021105_p3.png`: masthead dateline — claimed "WEDNESDAY MORNING,
  NOVEMBER 5 1902."
- Precinct grid (`SDDU19021105.2.17`) not independently re-summed row-by-row
  (resolution/density made it intractable); the numerator relies on the
  newspaper's own recap of that same table.

### 1904-11-08 (President floor 6,300, share 87.0%)

- Same screenshot as the Priority item: Parker figure — claimed 1,187; Debs
  figure — claimed 1,200; Swallow figure — claimed 119; fail if any digit
  differs.
- Same screenshot: printed pluralities — claimed "over Parker, 2,607; over
  Debs, 2,594"; fail if these read differently (would also reopen the
  Roosevelt-digit question).
- `sd_19041109_p3.png`: masthead dateline — claimed "WEDNESDAY MORNING,
  NOVEMBER 9, 1904."
- "THE VOTE OF SAN DIEGO COUNTY" precinct grid below the article not
  transcribed row-by-row (same resolution issue as 1902); numerator relies
  on the paper's own "ENTIRE COUNTY" recap.

### 1906-11-06 (Governor floor 2,016, share 26.0%)

- Same screenshots as the Priority items: Gillett figure — claimed 987;
  Blanchard — claimed 37; Langdon — claimed 85; fail if any digit differs.
- Precinct basis — claimed "forty-one precincts" / "41 precincts"; fail if
  a different count is legible.
- `sd_19061107_p8.png`: masthead/banner dateline — claimed "WEDNESDAY
  MORNING, NOVEMBER 7, 1906" / "ELECTION NOVEMBER 6, 1906."
- Full precinct grid on page 8 not transcribed row-by-row; numerator relies
  on the paper's own "For governor" recap of the 41 precincts.

### 1908-11-03 (President table floor 6,028, extended floor 6,841)

- `sd_19081104_p6_cityrows_c.png` row "6th Ward, 1st": Chafin claimed 6
  (fail: reads 4; +6 to the sum if wrong — not independently re-checked by
  the 2026-07-11 pass, which only addressed the same crop's Taft digit).
- `sd_19081104_p6_oce_pot.png` row "Pala": Hisgen claimed 1 (fail: blank;
  Taft's digit in this same row was CONFIRMED, see section 4).
- `sd_19081105_p6_taftlead.png` (day+2, narrative only, not part of the
  night-count floor): claimed "Taft has 5,393 votes to Bryan's 2,363, a
  plurality of 3,030"; internal arithmetic already checks out.

### 1910-11-08 (Governor floor 3,741, share 39.5%)

- `sd_19101109_p8_top.png` (context lines used for the Johnson consistency
  check): State Printer Shannon (R) claimed 1,947; Controller Nye (R)
  claimed 2,268. Fail: Shannon reads ≥ Johnson's value (would break the
  consistency argument used to resolve the Priority ask above).
- `sd_19101110_p16_govdigits2.png` (day+2, narrative only): claimed Johnson
  4,427, Bell 2,630, Wilson 1,679 — soft tens digits on Johnson/Bell; not
  part of the night-count floor.

### 1912-11-05 (President floor 17,566, share 80.8% — mostly verification-pass-confirmed, see section 4)

- `mirror/cdnc/screenshots/c_tst_41r.png` and `c_top_41r.png`: Forty-first
  Precinct Roosevelt — claimed 37, alternative 87. Explicitly "no fail
  criterion — either read keeps the floor claim intact" (headline uses the
  printed Grand-totals row, not this row-level sum); only tightens the
  known −88 residual between the printed total and the dossier's own
  hand-sum.
- `c_top_9r.png`: Ninth Precinct Roosevelt — claimed 45 (smudged glyph);
  fail if reads 95. Same non-impact caveat as above.
- `sd_19121106_p6_w_top.png`: intro clock — claimed "up to 2 o'clock this
  morning"; fail if it reads 3 o'clock (changes the clock label only).

### 1916-11-07 (President floor 24,811, share 67.9%)

- Same crop as the Priority item: precinct basis — claimed "152 of the 221
  precincts"; fail if it reads 162 (OCR's alternate reading; the page image
  reads 152 in both of its two occurrences in the article).
- Same crop: the clock digit in "at [2/3] o'clock this morning" is broken
  type, unresolved 2-vs-3; explicitly "no fail criterion — either reading
  keeps the verdict," affects the clock label only.

### 1918-11-05 (Governor floor 4,502, share 17.9%)

- `sd_19181106_p1_crop_da4.png`: DA line (context, not the target
  contest) — claimed "Utley 2341, Mather 1971"; STILL AMBIGUOUS per the
  2026-07-11 pass (leans toward reading Utley's disputed digit as 8, i.e.
  2841, based on the digit's hourglass shape, but genuine ambiguity
  remains at this halftone resolution). Never part of the governor-contest
  numerator either way.

### 1920-11-02 (President floor 8,178, share 26.3% — mostly verification-pass-confirmed, see section 4)

- `sd_19201103_p1_crop_sen.png`: senator lines (context, not the target
  contest) — claimed Shortridge 4,617, Phelan 3,263 (Phelan's last digit
  uncertain).
- `sd_19201103_p1_crop_sdrow.png`: AP State Election Table San Diego row
  (an earlier, lagging snapshot, not the headline figure) — claimed 40
  precincts, Cox 954, Harding 2,180.
- Spot-check any 5 of the 55 city-table rows against
  `sd_19201103_p1_city_strip1..5.png`; fail criterion for this cross-check
  only: column sums drifting above 2,500 (Cox) / 5,678 (Harding) — the
  city-table sum (6,992) is a consistency check, not the headline figure
  (8,178, the county-wide compilation).

---

## 3. Resolved by adversarial re-read

Asks a follow-up agent pass already re-verified against fresh, independently
cropped captures (see each dossier's own "Verification pass" appendix for
full method notes). Confirmed/corrected items below do not need to be
repeated; STILL-AMBIGUOUS items from those same passes remain listed in
sections 1-2 above.

| Dossier | Ask | Verdict |
|---|---|---|
| 1896-11-03 | Presidential line (McKinley/Bryan) | CONFIRMS 3,176 / 3,139 |
| 1896-11-03 | Printed plurality ("37") | CORRECTS to 35 — does not change the headline sum (3,176+3,139=6,315 unaffected); flags the newspaper's own printed cross-check as unreliable |
| 1896-11-03 | Precinct basis ("60 of 86", "42 of the county") | CONFIRMS |
| 1896-11-03 | General total line ("3,763 / 2,647 / 6,410") | CONFIRMS |
| 1896-11-03 | Alpine precinct President line (McKinley 29/Bryan 13/Prohibition 1) | CONFIRMS |
| 1896-11-03 | Alpine "Total vote" line ("152") | CORRECTS to 153 — not used in any calculation either way |
| 1898-11-08 | Column header (Gage/Neff/Maguire/Hutchinson/Needham order) | CONFIRMS — rules out a systematic column-swap across the whole table |
| 1898-11-08 | Total/Grand total rows blank | CONFIRMS — re-confirms no printed shortcut exists anywhere in the table |
| 1908-11-03 | 6th Ward 2nd Precinct, Taft | CONFIRMS 70 (rules out 76) |
| 1908-11-03 | Pala, Taft | CONFIRMS 7 (rules out 17; cell width argument rejects the judge-sum-implies-17 theory) |
| 1912-11-05 | Grand-totals row, Roosevelt figure | CONFIRMS the "6_0_" family (i.e., 6,505 as printed) — decisively RULES OUT the alternate hypothesis that it reads 6,417 (the dossier's own hand-sum); 2nd/4th digits remain low-confidence within {5,3} but this doesn't change the floor |
| 1918-11-05 | Stephens figure | CONFIRMS 2,726 (rules out 2,736) |
| 1918-11-05 | Precinct basis ("63 precincts out of 221") | CONFIRMS (rules out 68) |
| 1920-11-02 | Cox-Roosevelt figure | CONFIRMS 2,500 (rules out 2,509) |
| 1920-11-02 | Harding-Coolidge figure | CONFIRMS 5,678 at moderate-high confidence (resolution ceiling reached; rules out 5,673) |

Net effect on every headline number above: **NONE** — each verification pass
either confirmed the figure already used in that dossier's verdict, or
corrected a figure that was never part of the reported floor.

---

## 4. Per-election summary

| Date | Contest | Night floor | Share of certified final | Confidence | Open asks (P+S) |
|---|---|---|---|---|---|
| 1871-09-06 | Governor | 545 | 42.4% | High (exact paper recap match) | 6 (0P+6S) |
| 1872-11-05 | President | 536 | 61.4% | High | 7 (1P+6S) |
| 1875-09-01 | Governor | 720 | 45.0% | Flagged — unresolved conflict with the paper's own 666-vote total | 9 (4P+5S) |
| 1876-11-07 | President | 871 | 59.6% | High (doubly-corroborated printed total) | 5 (0P+5S) |
| 1879-09-03 | Governor | 614 | 43.5% | Medium — sole aggregate, no precinct breakdown | 2 (1P+1S) |
| 1880-11-02 | President | 747 | 57.3% (same-basis) | **Low** — multiple unresolved printed-arithmetic contradictions | 9 (2P+7S) |
| 1882-11-07 | Governor | 1,103 | NULL — no certified denominator found | Medium — sole aggregate | 2 (1P+1S) |
| 1884-11-04 | President | 812 | 41.3% | High (no flagged digits) | 10 (0P+10S) |
| 1886-11-02 | Governor | 1,031 | 36.5% | High (2 minor [?] flags) | 7 (2P+5S) |
| 1888-11-06 | President | 3,288 | 40.1% | High (1 [?] flag + 1 lower-confidence proxy precinct) | 9 (2P+7S) |
| 1890-11-04 | Governor | 184 | 2.5% | High | 6 (0P+6S) |
| 1892-11-08 | President | 673 | 8.7% | High (no flagged digits) | 9 (0P+9S) |
| 1894-11-06 | Governor | 1,761 (revised) | 24.7% | Medium — several [?] flags + one included-despite-misprint judgment call (Oceanside) | 13 (4P+9S) |
| 1896-11-03 | President | 6,315 | 81.3% | High, verification-pass-confirmed | 1 (0P+1S) |
| 1898-11-08 | Governor | 4,589 | 64.5% | **Low-medium — whole table**, verification pass left it unresolved | 10 (10P+0S) |
| 1900-11-06 | President | 3,672 (city-only proxy) | 53.0% | Medium — unresolved internal-consistency failure | 4 (1P+3S) |
| 1902-11-04 | Governor | 4,202 | 65.1% | High (2 minor flags) | 7 (2P+5S) |
| 1904-11-08 | President | 6,300 | 87.0% | High (1 flag resolved by arithmetic, not pixels) | 8 (1P+7S) |
| 1906-11-06 | Governor | 2,016 | 26.0% | High (2 [?] flags) | 9 (2P+7S) |
| 1908-11-03 | President | 6,028 (table) / 6,841 (extended) | 64.1% / 72.7% | Medium — dense table, partially verification-pass-confirmed | 11 (8P+3S) |
| 1910-11-08 | Governor | 3,741 | 39.5% | Medium — key digit resolved by argument, not direct read | 3 (1P+2S) |
| 1912-11-05 | President | 17,566 | 80.8% | High, verification-pass-confirmed | 3 (0P+3S) |
| 1916-11-07 | President | 24,811 | 67.9% | Medium — sole reported pair, no precinct cross-check | 3 (1P+2S) |
| 1918-11-05 | Governor | 4,502 | 17.9% | High, verification-pass-confirmed | 1 (0P+1S) |
| 1920-11-02 | President | 8,178 | 26.3% | High, verification-pass-confirmed | 3 (0P+3S) |
