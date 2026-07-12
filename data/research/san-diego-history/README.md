# `data/research/san-diego-history/`: San Diego County election-night history, 1884-1920

Recovered morning-after (election-night) vote counts for San Diego County,
extending the county's election-night record back from the modern panel
(`../election-night/san-diego-ca.json`, 2012-2024) into the newspaper era. This
reproduces, for San Diego, the San Francisco "century of election nights"
recovery (`docs/analysis/2026-06-13-a-century-of-election-nights.md`), from a
different archive: the San Diego Union on CDNC (cdnc.ucr.edu, paper code
`SDDU`, digitized 1871-1922).

Full per-election evidence (transcribed precinct rows, scan paths, gate
results, human-verification asks) lives in the campaign dossiers at
[`docs/research/night-recovery-2026-07-11-san-diego/`](../../../docs/research/night-recovery-2026-07-11-san-diego/);
this dataset is the promoted summary, one row per election. The narrative
analysis is
[`docs/analysis/2026-07-12-san-diego-century.md`](../../../docs/analysis/2026-07-12-san-diego-century.md).

## The metric (differs from the SF chart's denominator; do not mix silently)

```
night_share_pct = night_floor / certified_contest_total
```

- `night_floor`: the largest SINGLE-SEAT contest sum (all candidates in that
  one contest) printed in the day-after San Diego Union, city + county as
  reported. Multi-seat races are never summed. A FLOOR: partial precincts,
  and some papers omit minor candidates.
- `certified_contest_total`: the SAME contest's certified San Diego County
  total from the CA SoS Statement of Vote / CA Blue Book (see the campaign's
  `denominators.md` for per-candidate figures and page-image provenance).
  Presidential contests use the highest-elector-per-slate convention; the
  per-elector spread (a few votes) is recorded there.
- This is a same-contest share, NOT the SF chart's contest-sum /
  certified-ballots-cast share. Same-contest is cleaner (no undervote in the
  denominator) and makes these values slightly HIGHER than the SF-definition
  equivalents; any chart mixing the two jurisdictions must say so.

## `sd_night_history.csv` columns

| column | meaning |
|---|---|
| `election_date` | YYYY-MM-DD |
| `election_type` | presidential-general / gubernatorial-general |
| `contest` | the single-seat contest summed |
| `night_floor` | ballots in that contest per the morning-after paper (int) |
| `precincts_basis` | precincts-reported statement as printed (verbatim-ish) |
| `certified_contest_total` | certified SD county total for the same contest |
| `night_share_pct` | round(100 * night_floor / certified_contest_total, 1) |
| `confidence` | high / medium / low per the dossier (transcription confidence) |
| `flags` | comparability caveats (city-only, minor-tickets-unprinted, ...) |
| `night_source` | issue + section OID(s) + screenshot basename(s) |
| `certified_source` | SOV / Blue Book item + leaf, from denominators.md |
| `dossier` | the per-election evidence file |

## Coverage and gaps

Even-year November generals 1884-1920, except: **1914 and 1922** (CDNC has no
SDDU issues for those Novembers; NewsBank/microfilm targets, see
`docs/missing.md` conventions) and **1912's odd gap notes / 1900's city-only
basis** carried in `flags`. 2020s-era rows live in the cross-county panel, not
here. The 1922-2010 gap is unrecovered (CDNC's SDDU digitization ends 1922).

## Provenance rules

Same as the rest of `data/research/`: every number is re-findable (dossier
carries the exact page OID, zoom point, and screenshot), scans stay in the
gitignored `mirror/cdnc/` tree (licensed content), only figures + citations
are committed, and corrections append rather than rewrite (see each dossier's
"Verification pass" appendix).
