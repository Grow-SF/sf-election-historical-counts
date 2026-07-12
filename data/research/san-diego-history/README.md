# `data/research/san-diego-history/`: San Diego County election-night history, 1871-2004

![San Diego County: how much of the vote was counted by election night, 1871-2024](../../../docs/img/sd-night-share.png)

*Rendered by the site's own `NightShareChart` component (the same one that draws
the San Francisco series), fed by `packages/data/sd_night_history.json` which
`scripts/build_sd_history.py` bakes from this CSV plus the modern panel. Dim
dashed dots are lower bounds only (the paper printed majorities instead of
votes, omitted the city, gave only a city-only proxy, or carried just a
remote AP-wire snapshot), never slow counts. 1882 is omitted (no
certified denominator exists). To regenerate the image: run the preview harness
(`pnpm --filter @long-count/preview exec vite`) and
`node scripts/shoot_charts.cjs`.*

Recovered morning-after (election-night) vote counts for San Diego County,
extending the county's election-night record back from the modern panel
(`../election-night/san-diego-ca.json`, 2008-2024) into the newspaper era. This
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
  one contest) printed in the day-after paper (San Diego Union 1871-1920; the
  AP California county table in the Sacramento Union for 1924/1928; the
  Oceanside Blade-Tribune for the 1932 ceiling row), city + county as
  reported. Multi-seat races are never summed. A FLOOR: partial precincts,
  and some papers omit minor candidates.
- `certified_contest_total`: the SAME contest's certified San Diego County
  total from the CA SoS Statement of Vote / CA Blue Book (see the campaign's
  `denominators.md` for per-candidate figures and page-image provenance).
  Presidential contests use the highest-elector-per-slate convention; the
  per-elector spread (a few votes) is recorded there.
- For the 1871-1928 rows this is a same-contest share, NOT the SF chart's
  contest-sum / certified-ballots-cast share. The 1992 and 2004 rows are the
  documented exception: they are news-derived, their `contest` is `ballots
  cast (news-derived)`, and both numerator and denominator are certified
  BALLOTS CAST (certified minus the registrar's stated uncounted remainder);
  see the `flags` column and the coverage table below. Same-contest is
  cleaner (no undervote in the denominator) and makes these values slightly
  HIGHER than the SF-definition equivalents; any chart mixing the two
  jurisdictions must say so.

## `sd_night_history.csv` columns

| column | meaning |
|---|---|
| `election_date` | YYYY-MM-DD |
| `election_type` | presidential-general / gubernatorial-general |
| `contest` | the single-seat contest summed; for the 1992/2004 news-derived rows this reads `ballots cast (news-derived)` instead |
| `night_floor` | ballots in that contest per the morning-after paper (int) |
| `precincts_basis` | precincts-reported statement as printed (verbatim-ish) |
| `certified_contest_total` | certified SD county total for the same contest; for the 1992/2004 news-derived rows this is certified total BALLOTS CAST (SoS voter-participation statistics) |
| `night_share_pct` | round(100 * night_floor / certified_contest_total, 1) |
| `confidence` | high / medium / low per the dossier (transcription confidence) |
| `flags` | comparability caveats (city-only, minor-tickets-unprinted, ...) |
| `night_source` | issue + section OID(s) + screenshot basename(s) |
| `certified_source` | SOV / Blue Book item + leaf, from denominators.md |
| `dossier` | the per-election evidence file |

## Coverage and gaps

31 rows, from five source families, each with its own denominator basis;
never average across bases blindly. `flags` is a free-text caveat field, not
a basis label: it names the basis only where a row departs from the default
(`ap-remote-basis` on 1924/1928, `news-derived` on 1992/2004, and the
CEILING note on 1932). An empty `flags` means the default 1871-1920 basis:
certified same-contest total. Use the table below, not `flags`, to read a
row's basis:

| era | source | denominator | rows |
|---|---|---|---|
| 1871-1920 | San Diego Union, day-after, via CDNC | certified same-contest total | 25 (1871/1875/1879 were September state elections) |
| 1924, 1928 | AP California county table in a *remote* paper (Sacramento Union) via CDNC | certified same-contest total | 2, both `ap-remote-basis` lower bounds |
| 1932 | Oceanside Daily Blade-Tribune (San Diego County's own paper) via CDNC | certified same-contest total | 1, **CEILING only**: 76,427 of a certified 85,150 (339/384 precincts), but the Blade-Tribune was an AFTERNOON paper, so the figure is clocked to the afternoon of Wed 1932-11-09, roughly 16 to 20 hours after polls closed. Carried with a NULL share, `comparable: false`, and excluded from the chart; see the dossier's 2026-07-12 correction. |
| 1940 | Escondido Daily Times-Advocate (a county paper) via CDNC | certified same-contest total | 1, and the strongest point of the era: 114,410 of 128,110 (550/596 precincts) = 89.3%. Normally an EVENING paper, but it ran a rushed 6 a.m. special edition for this election and said so in print, so the figure is genuinely morning-clocked. |
| 1992, 2004 | San Diego Union-Tribune via NewsBank text (SDUB) | certified **ballots cast** | 2, `news-derived` (certified minus the registrar's stated remainder) |

Known dark years, each probed and documented rather than silently skipped:

- **1914, 1922**: CDNC holds no SDDU issues for those Novembers.
- **1926**: an access route existed and was used; it just didn't carry the
  number. The Sacramento Union's 1926-11-03 issue is open and was page-read:
  it printed a statewide governor total and a San Diego County
  PROPOSITION-only partial (13 precincts, no candidates), never a
  Young/Wardell/Sinclair county split, and neither backup paper (SBNP, LBPT)
  had one either. A format gap, not an access gap: re-probing after the
  embargo date will not help (`1926-11-02.md`).
- **1930**: genuinely CDNC **embargo-locked**. `SDU19301105` renders the
  rolling-embargo lock screen ("available ... on 23 September 2026"), and the
  two open backups (Long Beach Press-Telegram, San Bernardino Sun) print
  statewide-only totals. Worth re-running after that date (`1930-11-04.md`).
- **1934, 1936**: no county-level numerator exists in any reachable paper.
  For 1934 the Blade-Tribune split its coverage between a county-wide
  precinct basis (240 of 391) with no candidate numbers and candidate numbers
  for only a 9-precinct Oceanside/Carlsbad subset, so neither piece is a
  county floor. For 1936 the `BT` code has a genuine CDNC coverage gap, and
  the remote papers checked (Sacramento Union, San Bernardino Sun, Long Beach
  Press-Telegram) print statewide-only figures. See `1934-11-06.md`,
  `1936-11-03.md`.
- **1938, and 1942-1986** (1940 is recovered, see the table above): the AP
  county-table format had vanished from the sampled papers by 1952; NewsBank's
  San Diego Union *image* edition starts only in 2018 and its *text* archive is
  empty across most of 1970-1986. The live lead is the one that produced 1940:
  the county's own dailies were evening papers, but a big election could push
  one to print a morning *special*, which is night-clocked and therefore valid.
  Hunting for those specials is the recommended next pass (see
  `sd-local-papers-probe.md`, `newsbank-probe.md`,
  `cdnc-county-table-probe.md`, `sdub-text-probe.md`).
- **1994-2006**: Wayback's captures of the SoS and registrar election-night
  pages fall in gaps that swallow every election night
  (`wayback-probe-1994-2010.md`). 1988 and 2008 quote only *one* ballot
  category (absentees, provisionals), so they yield no sound floor; 1996 has
  no countable figure at all (the registrar story carries only a turnout
  percentage); 2000 has only a day+2 canvass figure, which RUNBOOK 5.2 admits
  as a ceiling (828,569, 84.7%), never a floor. Each year has a dossier.

2008-2024 rows live in the cross-county panel
(`../election-night/san-diego-ca.json`), not here; the chart above draws both.

## Provenance rules

Same as the rest of `data/research/`: every number is re-findable (dossier
carries the exact page OID, zoom point, and screenshot), scans stay in the
gitignored `mirror/cdnc/` tree (licensed content), only figures + citations
are committed, and corrections append rather than rewrite (see each dossier's
"Verification pass" appendix).
