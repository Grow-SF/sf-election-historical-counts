---
name: sov-certified-turnout
description: Use when setting or correcting the CERTIFIED vote/turnout figure (the denominator of an election-night share) for a California STATEWIDE election — even-year general or primary — in the SF election dataset. The authoritative source of truth is the California Secretary of State "Statement of Vote," digitized and public on archive.org. Not for odd-year municipal elections (no statewide SOV exists for those).
---

# SOV certified-turnout (source of truth = CA Statement of Vote)

The California Secretary of State's **Statement of Vote (SOV)** is the certified,
official canvass for every statewide election. It is digitized and **publicly
viewable on archive.org** (full PDF, no library card). Use it as the source of
truth for the certified denominator of statewide elections — it supersedes the
DOE turnout table, which has errors (e.g. DOE lists 1934 SF turnout as 166,133;
the SOV-certified Governor vote alone was 225,977).

## Scope — when this applies
- **YES:** even-year **general** elections (President in presidential years,
  Governor in gubernatorial midterm years) and even-year **primaries**.
- **NO:** odd-year **municipal** elections, special/bond/charter elections —
  these are *city* canvasses, never in the statewide SOV. Leave their certified
  figures on the Chronicle / city-canvass source.

## Volume map (archive.org identifiers)
| Election years | archive.org item |
|---|---|
| 1908–1922 | `statementofvo19081922cali` (1920 also `ldpd_11382167_000`) |
| 1924–1930 | `statementofvote192430cali` |
| 1926–1939 | `statementofvote192639cali` |
| 1932–1939 | `statementofvo19321939cali` |
| 1940–1950 | `stateofcaliforn194050cali` |
| 1952–1962 | `stateofcaliforn195262cali` |
| 1962–1964 | `castatem196264cali` (1966–68 `californiastate196668cali`) |

URL form: `https://archive.org/details/<identifier>` (add `/page/nNNN` for a page).

## What to extract (the certified figure)
For the election's **top statewide contest** — President (presidential general),
Governor (gubernatorial general), or the marquee partisan office (primary) —
record the **certified San Francisco County total = sum of ALL candidates** in
that contest. This is the certified denominator. (Use the SAME contest for the
election-night numerator so night ÷ certified is apples-to-apples.)

## Method (fastest reliable path)
1. **Cross-reference Wikipedia first.** The page "19XX United States presidential
   election in California" / "19XX California gubernatorial election" carries a
   *Results by county* table whose figures come from the SOV and whose `<ref>`
   gives the exact SOV volume + page. Read the raw wikitext for precision:
   `https://en.wikipedia.org/w/index.php?title=<PAGE>&action=raw` — pull the
   San Francisco row (all candidates) AND the `<ref>` citation verbatim.
2. **Confirm against the SOV** when a figure is doubtful or Wikipedia has no
   by-county table (common for primaries): open the era volume on archive.org and
   read the San Francisco County page for that contest.
3. Sum all candidates for the SF row = certified SF contest total.

## Record EVERY source (required)
For each election return:
```
election_date, contest (e.g. "President" / "Governor")
sf_certified_total: <sum of all candidates, SF county>
candidates: <name=votes; ...>  (so the sum is auditable)
sov_volume:  <archive.org identifier>
sov_page:    <page label, e.g. n591 / p.5>
sov_url:     https://archive.org/details/<id>/page/<page>
wikipedia_xref: <URL used, if any>
confidence + any [?] digits
```
The `final_source` field in the data must cite the SOV (volume + page + URL),
with Wikipedia noted only as the access/cross-check path.

## Common mistakes
- **Using the SOV for a municipal/special election** — it isn't there; don't
  force a statewide figure onto a city election.
- **Confusing the top-contest total with "total ballots cast."** The contest sum
  is a turnout floor (undervote not included). If the SOV prints a county "total
  votes cast" line, prefer it and say so; otherwise label the contest sum as the
  basis.
- **Wrong era volume** — check the table above; some volumes overlap.
- **Trusting a single OCR read** — cross-check the figure between Wikipedia and
  the SOV; SOV table OCR is unreliable.
- **Forgetting the citation** — every corrected certified figure must carry its
  SOV volume + page.
