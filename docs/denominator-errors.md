# DOE turnout-table denominator errors (for manual verification)

> **STATUS (2026-07-06): partially superseded.** The current, maintained
> register is [`doe-data-discrepancies.md`](doe-data-discrepancies.md).
> Of the three rows below: **1934-11-06 is RESOLVED** (the CA Statement of
> Vote certified 225,977; the point is now INCLUDED in the chart at 97.7%,
> not excluded); **1974-06-04 is RESOLVED as OUR misread** (the SOV total
> equals the DOE figure 198,508 exactly; the newspaper reading 203,381 was
> wrong and has been corrected in `data/sf_archival_canvass_points.csv`);
> only **1978-11-07 remains open**. The text below is kept as the original
> investigation record.

These are elections where a **single contest's vote total exceeds the
"ballots cast" figure in the DOE historical turnout table** — which is
impossible (no contest can draw more votes than ballots). In each case the
newspaper figure was re-read and verified on the scan; the conclusion is
that the *DOE turnout figure is an undercount*, not that the newspaper was
misread. Listed here so each can be double-checked by hand and, ideally,
arbitrated against the authoritative California / SF Statement of Vote.

**How to verify each:** open the cited scan in
`mirror/newsbank/scans/`, confirm the contest numbers and the
precincts-reporting line, then compare the contest sum to the DOE figure.
The true certified total must be **≥ the contest sum**.

| Election | DOE "ballots cast" | Contradicting contest (verified on scan) | Contest sum | Exceeds DOE by | Implied true total | Scan file |
|---|---|---|---|---|---|---|
| 1934-11-06 (general) | 166,133 | Governor: Merriam 112,778 / Sinclair 86,764 / Haight 21,352, **all 1054 precincts complete** | 220,894 | +54,748 | ≥ 220,894 | `sweep_19341106_issue19341107_p1_s2.png` |
| 1974-06-04 (primary) | 198,508 | Prop B (Conflicts of Interest) Yes 162,975 / No 40,406, **1356 of 1356 precincts** | 203,381 | +4,873 | ≥ 203,381 | `tbl_19740604_issue19740606_p5.png` |
| 1978-11-07 (general) | 217,965 | Governor: Brown 155,156 / Younger 50,748 / Clark 11,470 / Seals 4,339 / Dietrich 1,434 | 223,147 | +5,182 | ≥ 223,147 | `tbl_19781107_issue19781108_p6.png` |

**Notes**
- **1934 is the largest and earliest case** (+54,748). DOE lists 166,133 ballots
  cast, but the complete Governor race (the Merriam–Sinclair EPIC contest, a
  record-turnout election) drew 220,894 votes across all 1054 SF precincts. The
  DOE figure is also implausible against neighbors (1932: 227,283; 1936:
  269,387). Found during the 1899–1956 night-of recovery (2026-06-13); its
  night-share point is **excluded from the chart** pending a corrected
  denominator from the CA/SF Statement of Vote.
- The 1974 and 1978 cases are 1970s elections, suggesting a systematic
  undercount in the DOE turnout table for that decade rather than isolated
  typos. (Compare the date-mapping typos already found: 2001-12 "12/10" and the
  1975 runoff.)
- 1978 cross-checks: the newspaper's percentages are internally consistent
  (Brown 155,156 = 69.5% of 223,147 ✓); Brown winning ~70% in
  heavily-Democratic SF is historically correct; the California Statement
  of Vote on archive.org (`statementofvote197879cali`) shows SF Brown as
  99,171, but that is a djvu-OCR/column error (it would make Brown a
  minority winner). The authoritative paper SoV should settle the exact
  total.
- In the dataset these points are ingested as floors (`≥`), marked as
  night-partials, with `certified_final` set to the contest sum and the
  `final_source` column flagging the contradiction. They are **excluded
  from the trend fit** because their exact denominator is unresolved.

_Additional cases from the in-progress pre-1985 re-read will be appended
here as they are verified._
