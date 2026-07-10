# SoS status-page vs committed-panel: adjudication of 3 disagreements

Read-only. Source of the disagreements: scratchpad/sos-status-sweep.md (Disagreements
table, lines 485-497). Committed rows: data/research/election-night/{napa,del-norte,
riverside}-ca.json. All primary artifacts below were independently re-fetched (raw
`id_` Wayback fetches via curl, 2s spacing) rather than trusted from the sweep's cache,
except where noted the sweep's already-downloaded local capture cache
(scratchpad/sos-status-sweep/*_captures/*.bin, *_timeline.json) was read directly
(these are themselves raw id_ HTML pulled by the sweep's fetch_election.py, so reading
them satisfies "fetch the primary artifact").

---

## Case 1: napa-ca 2014-11-04 (6.72% apart)

**Committed:** election_night_ballots=18,286, pct=47.17%, source = Wayback capture
20150916061050 of `countyofnapa.org/ElectionResults/20141104/20141104-2230_dtl.htm`
(the county's 10:30 PM report; the true 10:42 PM "final" frame was never crawled).
Note self-labels 18,286 as "a documented floor."

**SoS sweep:** 19,515 ballots, Last Report "Nov 4 11:14 p.m.", CONFIRMED (frozen
20141105141649 -> 20141107083801, then jumps to 35,800 CCU on Nov 14).

**Independently re-verified both sides:**

- Re-fetched county capture (`curl id_`, 20150916061050): confirms committed note
  verbatim. Quote: `Last Updated: November 4, 2014 10:30 PM`. Table:
  `Vote by Mail Turnout 17,341 24.60% / Election Day Turnout 945 1.34% / Total 18,286
  25.94%`. Statewide contest block: `0/164 0.00%` precincts reported for Governor —
  i.e. at 10:30 PM essentially NO precinct-level in-person tally had posted yet.
- Read the sweep's already-fetched raw SoS HTML directly
  (scratchpad/sos-status-sweep/2014-11_captures/*.bin, confirmed genuine `id_`-style
  raw Wayback captures, not re-derived):
  - 20141105043349 (~8:33 PM PST Nov 4): Napa row `165/167 98.8% | 17,341 | Last
    Report: Nov 4 8:00 p.m. | ENU` — matches the county's own pure-VBM 8:01 PM first
    tranche exactly (17,341).
  - 20141105141649 (~6:16 AM PST Nov 5): Napa row `167/167 100.0% | 19,515 | Last
    Report: Nov 4 11:14 p.m. | FENU`.
  - 20141107083801 (2 days later): **identical** row, still 19,515 / "Nov 4 11:14
    p.m." — frozen.
  - 20141115022627 (10 days later): jumps to `35,800 | Nov 14 3:44 p.m. | CCU`.

**Reading:** The SoS's FENU (Final Election Night Unofficial) report is timestamped
11:14 PM, 32-44 minutes AFTER the county's last archived web posting (10:30 PM,
and the county's own unarchived 10:42 PM "final"). Critically, the county's 10:30 PM
page shows statewide precinct tallying essentially hadn't started (0/164), while the
SoS's 11:14 PM state shows Napa's own precinct-reporting metric at 100% (167/167) —
i.e. the SoS captured a later, more complete moment of the SAME continuous
election-night count, most plausibly because Napa kept transmitting updates to the
state's reporting system after it stopped updating its own public web page. This is
not two different generations of "final" reports competing — it's the same night's
count, and the SoS's is later and fuller. The committed note already flags 18,286 as
"a documented floor," which is exactly consistent with this: it undercounts the true
plateau by the ~1,229 ballots (6.7%) that posted between 10:30/10:42 PM and 11:14 PM.
The SoS value is CONFIRMED via a clean 2-day freeze before the correctly-identified
CCU jump on Nov 14 — the same freeze/jump signature used successfully across the
whole 228-cell sweep.

**VERDICT: REPLACE-WITH-SOS.**
New election_night_ballots = 19,515. certified_final unchanged = 38,766.
New election_night_pct = 19,515 / 38,766 = **50.34%** (was 47.17%).
Recommend source_url_night -> the SoS status-page capture (cite 20141105141649 or
20141107083801, either is the frozen FENU state; timestamp "Nov 4 11:14 PM"),
confidence can move to primary (official SoS aggregation page, doubly bracketed),
and the existing note should be kept/appended (not deleted) documenting the
cross-source gap and that 18,286 was the last-crawled COUNTY report but not the true
election-night plateau.

---

## Case 2: del-norte-ca 2016-11-08 (3.62% apart)

**Committed:** election_night_ballots=8,155, pct=83.30%, source = county's own
scanned "Release 4" PDF (Wayback capture 20201111052354), self-titled "Unofficial
Results / Election Night Final", page stamp 11/8/2016 10:47:49 PM, 18/18 precincts
(100%), Registered Voters 8,155/14,320 (56.95%). No text layer (scanned); read
visually in the committed source.

**SoS sweep:** 8,450 ballots, Last Report "Nov 8 11:38 p.m.", CONFIRMED (frozen
20161110185817 -> 20161116014606, 5 days, then jumps to 9,790 = certified final
exactly, at Nov 16 9:40 AM).

**Independently re-verified both sides:**

- Re-fetched the county's Release 4 PDF directly (`curl id_`, capture 20201111052354,
  9-page PDF, Creator "Canon iR-ADV C5240 PDF", CreationDate `Tue Nov 8 22:55:10 2016
  PST`, no text layer — pdftotext empty, confirmed). Rendered page 1 at 150dpi and
  read visually: header exactly `11/8/2016 10:47:49 PM`, `Election Summary Report...
  Unofficial Results / Election Night Final / 18 Precincts Reporting`,
  `Precincts Reported: 18 of 18 (100.00%)`, `Registered Voters: 8,155 of 14,320
  (56.95%)`, `Ballots Cast: 16,605` (the ~2x ballot-card figure, not the voter count).
  This independently confirms the committed 8,155 figure is read correctly — it is
  not a transcription error.
- Read the sweep's already-fetched raw SoS HTML directly
  (scratchpad/sos-status-sweep/2016-11_captures/*.bin):
  - 20161110185817 (first available capture): Del Norte row `18/18 100.0% | 14,318 |
    8,450 | Last Report: Nov 8 11:38 p.m. | SF`.
  - Frozen identically across 6 captures through 20161116014606 (Nov 16, 1:46 AM).
  - 20161116202259 (Nov 16, 8:22 PM... table col shows "Nov 16 9:40 a.m." as the new
    Last Report stamp): jumps to `9,790 | 68.4% | U` — 9,790 is exactly the certified
    final per both the committed row and the SoS's own registered-voters/turnout
    denominator, and matches the county's own separately-documented Release 6
    "Unofficial Final Report" (9,790, dated Nov 16) cited in the committed note.

**Reading:** Del Norte's own last PUBLIC web PDF ("Election Night Final," 10:47:49 PM,
already 100% precincts reporting) is 51 minutes older than the SoS's Last-Report
stamp (11:38 PM) for the same night. Unlike Napa, the county's own report already
claims 100% precincts reporting at 10:47 PM, so the extra 295 ballots by 11:38 PM
most plausibly reflect a small number of late-tabulated/provisional ballots folding
into the county's backend EMS feed to the state after the county stopped updating its
own public web page (it had already declared "Election Night Final" and moved on).
The SoS's number is CONFIRMED with an unusually strong bracket: frozen for 5 full
days, then jumps to a value that independently matches the certified final AND the
county's own Nov 16 Release 6, on the same day the SoS shows the jump — strong
corroboration this is a real, continuously-fed county pipeline rather than a stray
or erroneous SoS ingest.

**VERDICT: REPLACE-WITH-SOS.**
New election_night_ballots = 8,450. certified_final unchanged = 9,790.
New election_night_pct = 8,450 / 9,790 = **86.31%** (was 83.30%).
Recommend source_url_night -> the SoS status-page capture (20161110185817, Last
Report "Nov 8 11:38 PM"), and keep the existing note (the scanned-PDF read of 8,155
was itself accurate — it's a real, different, slightly-earlier report generation of
the same night, not a misread) with an appended line documenting the ~51-minute gap
and which is now the landed value.

---

## Case 3: riverside-ca 2024-11-05 (10.37% apart)

**Committed:** election_night_ballots=611,101, `comparable: false` (explicitly
flagged CEILING), pct=63.7%. Source = Wayback capture 20241107034053 of
livevoterturnout ENR, embedded "Updated: 11/6/2024 5:35:21 PM" — the committed note
itself already identifies this as the FIRST DAILY CANVASS UPDATE (afternoon of the
day after the election), not the ~3 AM election-night plateau, which the note says is
"genuinely unarchived."

**SoS sweep:** 547,742 ballots, Last Report "Nov 6 5:02 a.m.", CONFIRMED (frozen
20241106133254 -> 20241106171813, i.e. holds from ~6:32 AM through ~10:18 AM Nov 6,
then the NEXT capture jumps straight to 611,101).

**Independently re-verified both sides, and this closes the loop cleanly:**

- Read the sweep's already-fetched raw SoS timeline directly
  (scratchpad/sos-status-sweep/2024-11_captures + `2024-11_timeline.json`, full
  Riverside sequence extracted):
  - Precincts hit 100% (1,345/1,345) at capture 20241106073132 (Nov 5 11:02 PM Last
    Report stamp), ballots 466,214.
  - Ballots keep climbing through election night: 481,400 (12:05 AM) -> 496,024
    (12:59 AM) -> 510,623 (2:05 AM) -> **547,742 (Last Report "Nov 6 5:02 a.m.")**.
  - 547,742 then holds FROZEN, byte-identical, across 3 consecutive captures
    (20241106133254, 20241106154527, 20241106171813 — roughly 6:32 AM to 5:18 PM
    Nov 6), i.e. it is the genuine overnight plateau, not a transient mid-climb value.
  - The very next capture (20241107015446) jumps to **611,101**, Last Report
    "Nov 6 5:34 p.m." — i.e. this is the SAME artifact as the committed ceiling.
- Independently re-fetched the committed source directly (`curl id_`, Wayback capture
  20241107034053 of the livevoterturnout ENR page): confirmed `611,101` appears
  labeled `Ballots Counted`.

This is the cleanest of the three cases: the SoS's own timeline shows 547,742 as a
genuinely frozen overnight state (12+ hours stable) immediately followed by the exact
same 611,101 figure the committed row already uses and already flags as the
next-day-afternoon update. The two sources aren't in tension at all — they are
adjacent points on the identical SoS-fed reporting timeline, and the committed row's
own flag text ("611,101 is the Nov-6 17:35 first daily canvass update... overstates
the true plateau") is now directly corroborated rather than merely inferred.

Cross-check against certified final: committed certified_final = 959,098 (Election
Day 170,437 + VBM 788,661, CA SoS SoV). 547,742 / 959,098 = **57.11%**.

**VERDICT: REPLACE-WITH-SOS** (this is the recommended, strongly-evidenced case).
New election_night_ballots = 547,742. certified_final unchanged = 959,098.
New election_night_pct = **57.11%** (was 63.7%, and was flagged comparable:false).
Remove `comparable: false` and the `flag` field (no longer needed — 547,742 is a
clean, bracket-confirmed ~5 AM overnight plateau, stage-comparable to the 2022-11
general's clean ~2 AM figure). Recommend source_url_night -> SoS capture
20241106133254 (or any of the 3 frozen captures), Last Report "Nov 6 5:02 AM",
confidence -> primary. This flips Riverside 2024-11 into a usable data point:
2022-06 primary (post-epollbook, pre-ASV) 51.12% -> 2022-11 general (post-epollbook,
pre-ASV) 34.0% -> 2024-11 general (post-epollbook, pre-ASV) 57.11%, all now
comparable on the same measurement stage.

---

## Summary table

| Case | Old value | Old pct | New value | New pct | Verdict |
|---|---|---|---|---|---|
| napa-ca 2014-11-04 | 18,286 | 47.17% | 19,515 | 50.34% | REPLACE-WITH-SOS |
| del-norte-ca 2016-11-08 | 8,155 | 83.30% | 8,450 | 86.31% | REPLACE-WITH-SOS |
| riverside-ca 2024-11-05 | 611,101 (ceiling, comparable:false) | 63.7% | 547,742 | 57.11% | REPLACE-WITH-SOS |

No repo writes made (read-only scout per instructions). All three recommendations
are ready for the operator to land via the normal editing process, including
updating `packages/data/county_night.json` if these rows are also mirrored there.
