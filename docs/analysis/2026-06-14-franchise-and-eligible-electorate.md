# Did universal vote-by-mail expand the franchise in San Francisco?

*Turnout, registration, and the eligible electorate, 1900–2026 — and why the
answer, on every measure available, is no.*

The rest of this project is about *when* San Francisco knows who won. This note
asks a different question. Mailing every voter a ballot (2002 permanent list →
2020 all-mail → 2022 permanent) is the most sweeping change to *how* the city
votes in sixty years. Did it bring more people into the electorate?

Short answer: no. Turnout of the registered tracks what's on the ballot, not how
ballots are delivered; the registered share of eligible citizens has held in a
~70–86% band for decades, before and after the switch; San Francisco was already
near the ceiling. The real expansions and contractions of the franchise come
from **women's suffrage (1920)** and **a century of immigration**, not vote-by-mail.

## The franchise funnel

The clearest frame is the whole population sorted into mutually-exclusive bands —
*under voting age · non-citizen adults · eligible but unregistered · registered
non-voters · voters* — at each presidential election, 1908–2024
(`data/franchise_funnel.json`). Two things dominate the picture, and neither is
the mail:

- **1920 — women's suffrage** roughly doubles the eligible band in one step.
- **The non-citizen band breathes with immigration** (see below).

The gap between the population and the voters is mostly about *who counts as
eligible*, not who bothers to show up.

## Turnout of the registered didn't move

Like-for-like, by election type (`data/sf_turnout_history_*.csv` →
`turnout_history.json`): presidential generals draw ~80%, off-year municipals
~40%, and the all-mail era lands inside that same historical band. The 2020
record was the nationwide presidential peak (every state spiked), not a
vote-by-mail effect; the 2024 general fell back *below* 2016, and the 2024
presidential primary was the lowest in the modern record.

## Registration of the eligible didn't move either

The franchise question proper is whether mail voting pulled more eligible people
onto the rolls. The Secretary of State publishes the answer — registered voters
against an eligible-citizen estimate, per county
(`data/sf_registration_eligible.csv`, 2000–2026; recovered Statement-of-Vote
rows extend it to 1978 in `..._sov_1974_1998.csv`). San Francisco's registered
share of eligible has held around three-quarters for decades, flat through the
all-mail transition.

The one wrinkle is the **1990s "deadwood" era**: registration climbed *past* 100%
of eligible (peaking 100.7% in 1996) as the rolls filled with voters who had
died, moved, or re-registered elsewhere. In an October 1996 report the Secretary
of State named San Francisco the state's worst case — up to a fifth of names
dead weight (Contra Costa Times, NewsBank docref `1063FBAA6480CFD4`). The 1995
federal "motor voter" law (NVRA) forced the list maintenance that pulled it back
down. It's shaded on the registration chart.

## The eligible electorate, recovered back to 1900

This is the substantive new data. The eligible *voting-age* population — the
franchise's true denominator — was recovered for San Francisco County from the
decennial census via **IPUMS NHGIS** (`data/sf_eligible_vap_estimate.csv`,
`scripts/nhgis_extract*.json`), with the correct historical definition of who
could legally vote:

- **Men only before 1920.** In 1900, ~128,985 men were of voting age but only
  **100,697 were eligible citizens** (native + naturalized; California barred
  alien and declarant voting). Women's suffrage (CA 1911 / 19th Amendment 1920)
  then doubled the eligible electorate.
- **The immigrant arc.** The non-citizen share of adults tracks immigration:
  the alien share of the foreign-born ran **36.5% (1940) → 23.9% (1950**, WWII-era
  naturalization**) → 44.0% (1970**, the post-1965 Latin American and Asian
  waves**)**. Asian immigrants were barred from naturalization until the
  1940s–50s, so they sit in the non-citizen band by law.
- **A franchise that shrank.** Citizen voting-age population peaked around
  **554,000 in 1950**, then *fell* to ~462,000 by 1970 as the city lost
  population and non-citizens rose. By 2020 the all-adult voting-age population
  was **760,738** but the eligible-citizen count only **668,567** — roughly one
  in eight SF adults is a non-citizen, up from a mid-century low near one in
  twenty.

## Data & methods

- **CA SoS Reports of Registration** (2000–2026): `scripts/fetch_sos_registration.py`
  pulls the SF county eligible/registered rows from the per-report `county.pdf`.
- **Printed Statement of Vote** (1974–1998): `scripts/recover_sov_registration.py`
  locates the "Voter Participation by County" table in archive.org scans and crops
  the San Francisco row for reading. Lesson worth keeping: full-page OCR *and*
  full-page vision models both misread digits in these dense multi-column tables;
  the reliable method is to crop the single row first, then read it.
- **IPUMS NHGIS** (1900–2020): two extracts — voting-age by sex/age, and
  nativity/citizenship. Direct census citizenship by age exists for 1940, 1950,
  and 1970; 1920/1930 use the real foreign-born-21+ count × an interpolated alien
  share; 1960 is interpolated (the 1960 census asked no citizenship question).
- **Chronicle / NewsBank** corroborated the deadwood figure but does not tabulate
  citizen counts; the census is the source for the eligible denominator.

Cite NHGIS: *Schroeder, Van Riper, Manson, Knowles, Kugler, Roberts, Ruggles.
IPUMS National Historical Geographic Information System: Version 20.0. Minneapolis:
IPUMS, 2025. https://doi.org/10.18128/D050.V20.0* (and add to the IPUMS
bibliography). Full provenance and the citizen-vs-VAP distinction:
[`eligible-denominator-notes.md`](../eligible-denominator-notes.md).

## Caveats & open questions

- **Pre-1978 citizen-eligible is partly estimated** for 1920–1970 (1940/1950/1970
  are direct; 1920/1930 apply an alien share; 1960 is interpolated). The all-adult
  VAP figures are real census counts throughout.
- **The 1974–1998 SOV recoveries are pending hand-verification** against the cited
  scans — values carry a `confidence` flag in the CSV.
- The eligible series can't reach **1899** on the citizen measure (the SoS published
  no county eligible before ~1973; the night-share record bottoms at 1908 anyway).
- **Non-citizen voting** in SF school-board elections (since 2016) is not modeled
  here; it's a small, separate franchise the funnel's "non-citizen" band doesn't
  capture.
