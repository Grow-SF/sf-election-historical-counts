# Arbitration: Sept 26, 1911 SF Municipal Primary total vote polled (78,919 vs 79,019)

Started 2026-07-08. Question: FY1912-13 Municipal Reports cumulative table (munisanfrancisco62sanfrich p.261) prints 78,919; FY1915-16 (munisanfrancisco65sanfrich pp.329, 331) prints 79,019. Registration 101,955, 356 precincts in all printings. Need an independent printing, ideally per-district, summable.

## VERDICT: 79,019 is correct. The FY1912-13 cumulative table's 78,919 is the misprint.

## Evidence 1 (decisive): FY1911-12 Municipal Reports, Department of Elections canvass, per-assembly-district table

- Item: archive.org/details/sanfranciscomuni61sanfrich (FY1911-12 Municipal Reports, full view)
- Locating query (copy-pasteable): https://ia601407.us.archive.org/fulltext/inside.php?item_id=sanfranciscomuni61sanfrich&doc=sanfranciscomuni61sanfrich&path=/28/items/sanfranciscomuni61sanfrich&q=%2279%2C019%22 -> single match, API page 223 = leaf n222. (Query "78,919" over the same item: ZERO matches anywhere in the volume.)
- Page image (downloaded, read by eye): https://archive.org/download/sanfranciscomuni61sanfrich/page/n222 saved as scratchpad/imgs/muni61_n222.jpg. Printed page number 195, running head "DEPARTMENT OF ELECTIONS".
- Verbatim header: "PRIMARY MUNICIPAL ELECTION, SEPTEMBER 26, 1911. FOR MAYOR." Columns: Assembly District | Total Vote Polled | L. Boggione | P. H. McCarthy | W. McDevitt | J. Rolph, Jr. | F. Sibert.
- Verbatim total line: "Total ... 79,019 | 51 | 27,067 | 3,893 | 47,427 | 209"
- Context page (API page 221, leaf n220, Registrar's transmittal): "The report includes a financial statement of this Department together with a complete statement of votes cast at the Primary Munici[pal Election]..." (this volume's canvass is the contemporaneous primary record, J. H. Zemansky, Registrar).

### Transcribed Total Vote Polled column (read from image; independently confirmed against the item's _djvu.txt OCR at https://archive.org/download/sanfranciscomuni61sanfrich/sanfranciscomuni61sanfrich_djvu.txt lines ~23760-24043):

| AD | Total Vote Polled |
|----|---|
| 28th | 1,522 |
| 29th | 1,175 |
| 30th | 1,523 |
| 31st | 2,915 |
| 32nd | 5,740 |
| 33rd | 7,876 |
| 34th | 8,054 |
| 35th | 5,216 |
| 36th | 3,227 |
| 37th | 7,635 |
| 38th | 5,497 |
| 39th | 10,781 |
| 40th | 4,064 |
| 41st | 4,578 |
| 42nd | 2,241 |
| 43rd | 2,503 |
| 44th | 2,404 |
| 45th | 2,068 |

My sum: 1522+1175+1523+2915+5740+7876+8054+5216+3227+7635+5497+10781+4064+4578+2241+2503+2404+2068 = **79,019** exactly, matching the printed Total. So the per-district breakdown is internally consistent and independently arbitrates for 79,019.

Sanity: mayoral candidate votes sum 51+27,067+3,893+47,427+209 = 78,647 = 79,019 minus 372 (blank/void in the mayoral race), consistent with "Total Vote Polled" meaning ballots cast per district. Per-row check e.g. AD28: 2+780+102+610+8 = 1,502 <= 1,522. OK.

Percent cross-check: 79,019/101,955 = 77.504% (prints as 77 1/2 exactly); 78,919/101,955 = 77.406%. FY1915-16's "77 1/2" is exactly consistent with 79,019.

Nature of the slip: 78,919 vs 79,019 is a single-digit error in the hundreds/thousands boundary (9,0 -> 8,9), classic compositor transposition in the FY1912-13 cumulative table.

## Dead ends / negative results
- Fulltext query "78,919" and "78919" in sanfranciscomuni61sanfrich: no matches (the wrong figure appears nowhere in the FY1911-12 volume).
- Fulltext query "101,955" in sanfranciscomuni61sanfrich: no matches (registration figure not OCR-findable there; not needed).
- Fulltext "Total Vote Polled" in muni61 matches only the May 14, 1912 presidential primary section (API pp.295+); the Sept 1911 primary tables use the column header form split across lines, so search by the date header instead.

## Evidence 2 (attempted corroboration): CDNC, SF Call Oct 1911 official canvass
DEAD END for this pass: cdnc.ucr.edu returns HTTP 403 (Cloudflare) to curl, both plain and with a Chrome UA, e.g.
`curl "https://cdnc.ucr.edu/?a=q&hs=1&r=1&results=1&txIN=%22official+canvass%22&dafdq=27&dafmq=09&dafyq=1911&datdq=31&datmq=10&datyq=1911&puq=SFC&e=-------en--20--1--txt-txIN--------"` -> 403.
Would need the raw-CDP Chrome recipe (memory: cdnc-vein-and-cloudflare-cdp). Not pursued: Evidence 1 already arbitrates decisively per the runbook's do-not-burn-hours-on-bot-walls rule. If a second leg is ever wanted, target SF Call issues Oct 3-14, 1911 for the Board of Election Commissioners' official canvass of the Sept 26 primary.

## Evidence 3 (priority 3 check): FY1912-13 volume reprint search
DEAD END: fulltext search of munisanfrancisco62sanfrich (correct server path ia803104...(/7/items/...)) for "79,019", "78,919", and even "September 26" returns zero matches, and the item's _djvu.txt (https://archive.org/download/munisanfrancisco62sanfrich/munisanfrancisco62sanfrich_djvu.txt) contains none of: 78,919 / 79,019 / "September 26" / "primary municipal" / 101,955. The OCR simply fails on that volume's canvass tables (the operator's p.261 reading was by eye). No additional independent printing recoverable from that volume by text search.
