# Election-Night v4 Data Verification Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Machine-recheck every sourced number in `data/research/election-night-v4/` against its cited URL, validate internal consistency (JSONs vs VERIFY.md vs county_night.json), and produce a hand-verification packet for the rows a machine cannot settle.

**Architecture:** Four small Python scripts in `scripts/research/` sharing one helper module. An offline validator checks invariants and cross-file agreement. Two network scripts fetch each cited source (Wayback raw form, cached to a gitignored dir) and confirm the claimed number appears in it. A report generator merges results into a committed `MACHINE_CHECK.md` plus a committed `HUMAN_VERIFY.md` packet for the user.

**Tech Stack:** Python 3 stdlib, `curl`, `pdftotext` (installed at /opt/homebrew/bin), pytest via `uv run pytest`.

## Global Constraints

- No em dashes in any prose we write (house style; use comma/colon/parens).
- Never hand-edit `packages/data/county_night.json`; it is derived. Only regenerate via `python3 scripts/build_county_night.py`.
- Human verification loop: give the user URL + claimed value + what counts as a fail; their reading wins over any machine or model claim.
- Network politeness: 2 second pause after every successful fetch, 3 retries with backoff; every fetched artifact cached to disk so reruns are free.
- New pytest tests must not carry the `network` marker (default addopts exclude it; these tests are offline).
- The dataset ground truths (from the current tree, verify counts as you go): 13 county JSONs, 78 election rows, 54 sourced numerators (confidence: 50 primary, 4 secondary), 24 nulls, 6 SoS SoV denominator PDFs (2012, 2014, 2016, 2018, 2022, 2024).
- `election_night_pct` is stored in MIXED units in v4: 14 rows as fractions (e.g. 0.5673), 40 as percents (e.g. 60.7). The rule, copied from `scripts/build_county_night.py:56`: value <= 1.5 means fraction, multiply by 100. Task 6 normalizes this; every earlier task must handle both units via `norm_pct`.
- Commit at the end of every task.

---

### Task 1: Shared helper module `en_common.py` with tests

**Files:**
- Create: `scripts/research/en_common.py`
- Test: `tests/test_verify_election_night.py`
- Modify: `.gitignore` (add one line)

**Interfaces:**
- Produces (used by Tasks 2-5):
  - `ROOT: pathlib.Path` (repo root), `V4: pathlib.Path` (the v4 dir), `CACHE: pathlib.Path` (`data/research/election-night-v4/cache`)
  - `norm_pct(p: float|None) -> float|None` (mixed-unit pct to percent, 2dp)
  - `wayback_raw(url: str) -> str` (insert `id_` after the 14-digit Wayback timestamp; non-Wayback URLs unchanged)
  - `find_number(text: str, n: int) -> str|None` (context string if n appears comma-formatted or bare, not embedded in a longer number; else None)
  - `strip_html(raw: str) -> str`
  - `pdf_text(path: pathlib.Path) -> str`
  - `fetch(url: str, dest: pathlib.Path, tries: int = 3, sleep: float = 2.0) -> bool` (curl with cache-on-disk; True on success)
  - `load_rows() -> list[dict]` (all 78 election rows, each dict = the JSON row plus `slug` and `county` keys)

- [ ] **Step 1: Write the failing tests**

Create `tests/test_verify_election_night.py`:

```python
"""Offline tests for the election-night-v4 verification helpers."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts/research"))

from en_common import find_number, norm_pct, strip_html, wayback_raw


def test_norm_pct_fraction():
    assert norm_pct(0.5673) == 56.73


def test_norm_pct_percent_passthrough():
    assert norm_pct(60.7) == 60.7


def test_norm_pct_none():
    assert norm_pct(None) is None


def test_wayback_raw_inserts_id():
    url = "https://web.archive.org/web/20161112171743/http://x.gov/a.htm"
    assert wayback_raw(url) == (
        "https://web.archive.org/web/20161112171743id_/http://x.gov/a.htm"
    )


def test_wayback_raw_leaves_direct_urls_alone():
    assert wayback_raw("https://smcacre.gov/a.pdf") == "https://smcacre.gov/a.pdf"


def test_find_number_comma_formatted():
    assert find_number("Cards Cast 177,183 40.48%", 177183) is not None


def test_find_number_bare_json():
    assert find_number('"BC":28159,', 28159) is not None


def test_find_number_rejects_embedded_digits():
    assert find_number("run id 1177183x total", 177183) is None


def test_find_number_rejects_longer_comma_number():
    assert find_number("grand total 1,177,183 ballots", 177183) is None


def test_find_number_absent():
    assert find_number("nothing here", 12345) is None


def test_strip_html():
    assert strip_html("<td>177,183</td>").strip() == "177,183"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_verify_election_night.py -v`
Expected: FAIL at collection with `ModuleNotFoundError: No module named 'en_common'`

- [ ] **Step 3: Write the module**

Create `scripts/research/en_common.py`:

```python
"""Shared helpers for the election-night-v4 source verification scripts.

Used by validate_election_night.py, verify_en_denominators.py,
verify_en_numerators.py and build_en_verification_report.py.
"""
import html as html_mod
import json
import pathlib
import re
import subprocess
import time

ROOT = pathlib.Path(__file__).resolve().parents[2]
V4 = ROOT / "data/research/election-night-v4"
CACHE = V4 / "cache"
UA = "Mozilla/5.0 (sf-election-count source verification; steven@growsf.org)"


def norm_pct(p):
    """v4 stores election_night_pct in mixed units; <= 1.5 means fraction.
    Same rule as scripts/build_county_night.py."""
    if p is None:
        return None
    return round(p * 100, 2) if p <= 1.5 else round(p, 2)


def wayback_raw(url):
    """Rewrite a Wayback page URL to the raw id_ form (no toolbar chrome)."""
    return re.sub(
        r"(https://web\.archive\.org/web/\d{14})/", r"\g<1>id_/", url, count=1
    )


def find_number(text, n):
    """Context string if integer n appears in text (comma-formatted or bare),
    not embedded inside a longer number; else None."""
    for v in (f"{n:,}", str(n)):
        for m in re.finditer(re.escape(v), text):
            before = text[m.start() - 1 : m.start()]
            after = text[m.end() : m.end() + 1]
            if before.isdigit() or after.isdigit() or before == "," or after == ",":
                continue
            return " ".join(text[max(0, m.start() - 80) : m.end() + 80].split())
    return None


def strip_html(raw):
    return html_mod.unescape(re.sub(r"<[^>]+>", " ", raw))


def pdf_text(path):
    r = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True
    )
    return r.stdout if r.returncode == 0 else ""


def fetch(url, dest, tries=3, sleep=2.0):
    """curl url into dest, cached: an existing non-empty dest is a hit."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return True
    for i in range(tries):
        r = subprocess.run(
            ["curl", "-sSL", "--fail", "-A", UA, "--max-time", "180",
             "-o", str(dest), url]
        )
        if r.returncode == 0 and dest.exists() and dest.stat().st_size > 0:
            time.sleep(sleep)
            return True
        time.sleep(5.0 * (i + 1))
    if dest.exists():
        dest.unlink()
    return False


def load_rows():
    """All election rows across the 13 county JSONs, flattened."""
    rows = []
    for fp in sorted(V4.glob("*.json")):
        d = json.loads(fp.read_text())
        for e in d["elections"]:
            rows.append(
                {
                    "slug": fp.stem,
                    "county": d["jurisdiction"].replace(" County", ""),
                    **e,
                }
            )
    return rows
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_verify_election_night.py -v`
Expected: 11 passed

- [ ] **Step 5: Gitignore the cache dir**

Append to `.gitignore`:

```
data/research/election-night-v4/cache/
```

- [ ] **Step 6: Commit**

```bash
git add scripts/research/en_common.py tests/test_verify_election_night.py .gitignore
git commit -m "verify: shared helpers for election-night-v4 source checks"
```

---

### Task 2: Offline consistency validator

**Files:**
- Create: `scripts/research/validate_election_night.py`

**Interfaces:**
- Consumes: `en_common.ROOT`, `V4`, `norm_pct`, `load_rows`
- Produces: a CLI that exits 0 when clean, 1 with one line per failure. Run by Tasks 6 and 7 as a regression gate.

Checks, per row: pct equals ballots/final (0.05pp tolerance after unit normalization); sourced rows have `source_url_night` + confidence primary/secondary; null rows have confidence `none`, null pct, no night URL; denominator URL is CA SoS. Cross-file: every row agrees with its VERIFY.md table line (night ballots, final, share to 1dp, confidence, link URL); the VERIFY.md San Francisco control table agrees with `packages/data/elections.json`.

- [ ] **Step 1: Write the validator**

Create `scripts/research/validate_election_night.py`:

```python
#!/usr/bin/env python3
"""Offline consistency check of data/research/election-night-v4/.

Row invariants, VERIFY.md table agreement, and SF-control agreement with
packages/data/elections.json. Exits 1 and prints one line per failure.
(county_night.json sync is checked separately via build + git diff -I.)
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import ROOT, V4, load_rows, norm_pct

FAIL = []


def fail(msg):
    FAIL.append(msg)


def check_rows(rows):
    for r in rows:
        key = f"{r['slug']} {r['date']}"
        b = r["election_night_ballots"]
        fin = r["certified_final"]
        p = r["election_night_pct"]
        if not isinstance(fin, int) or fin <= 0:
            fail(f"{key}: bad certified_final {fin!r}")
            continue
        if not (r.get("source_url_final") or "").startswith(
            "https://elections.cdn.sos.ca.gov/"
        ):
            fail(f"{key}: denominator source not CA SoS: {r.get('source_url_final')!r}")
        if b is None:
            if r["confidence"] != "none":
                fail(f"{key}: null numerator but confidence={r['confidence']!r}")
            if p is not None:
                fail(f"{key}: null numerator but pct={p!r}")
            if r.get("source_url_night"):
                fail(f"{key}: null numerator but has source_url_night")
        else:
            if r["confidence"] not in ("primary", "secondary"):
                fail(f"{key}: sourced but confidence={r['confidence']!r}")
            if not r.get("source_url_night"):
                fail(f"{key}: sourced but no source_url_night")
            if not 0 < b < fin:
                fail(f"{key}: ballots {b} not in (0, final {fin})")
            want = round(b / fin * 100, 2)
            got = norm_pct(p)
            if got is None or abs(got - want) > 0.05:
                fail(f"{key}: pct {got} != ballots/final {want}")


def parse_verify_tables(md):
    """(slug, year) -> the VERIFY.md summary-table line, parsed."""
    out = {}
    slug = None
    for line in md.splitlines():
        m = re.match(r"^### (.+?) County", line)
        if m:
            slug = m.group(1).lower().replace(" ", "-") + "-ca"
        elif line.startswith("## San Francisco"):
            slug = "san-francisco-ca"
        if slug and re.match(r"^\| 20\d\d \|", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]

            def num(s):
                s = s.lstrip("≈").replace(",", "").strip()
                return int(s) if s.isdigit() else None

            share = re.search(r"(\d+(?:\.\d+)?)%", cells[4])
            is_county = len(cells) > 6
            link = re.search(r"\((https?://[^)]+)\)", cells[6]) if is_county else None
            out[(slug, int(cells[0]))] = {
                "night": num(cells[2]),
                "final": num(cells[3]),
                "share": float(share.group(1)) if share else None,
                "conf": cells[5] if is_county else None,
                "url": link.group(1) if link else None,
            }
    return out


def check_verify_md(rows, tables):
    for r in rows:
        year = int(r["date"][:4])
        row = tables.get((r["slug"], year))
        key = f"{r['slug']} {year}"
        if row is None:
            fail(f"{key}: missing from VERIFY.md")
            continue
        if row["night"] != r["election_night_ballots"]:
            fail(f"{key}: VERIFY.md night {row['night']} != json {r['election_night_ballots']}")
        if row["final"] != r["certified_final"]:
            fail(f"{key}: VERIFY.md final {row['final']} != json {r['certified_final']}")
        got = norm_pct(r["election_night_pct"])
        if (row["share"] is None) != (got is None):
            fail(f"{key}: VERIFY.md share {row['share']} vs json {got}")
        elif got is not None and abs(row["share"] - got) > 0.055:
            fail(f"{key}: VERIFY.md share {row['share']} != json {got}")
        if row["conf"] is not None and r["confidence"] != row["conf"]:
            fail(f"{key}: VERIFY.md conf {row['conf']} != json {r['confidence']}")
        if row["url"] and r.get("source_url_night") and row["url"] != r["source_url_night"]:
            fail(f"{key}: VERIFY.md link != json source_url_night")


def check_sf(tables):
    els = json.loads((ROOT / "packages/data/elections.json").read_text())
    for e in els:
        row = tables.get(("san-francisco-ca", e.get("year")))
        if e.get("kind") != "General" or row is None or e.get("nightPct") is None:
            continue
        if row["final"] != e.get("final"):
            fail(f"SF {e['year']}: VERIFY.md final {row['final']} != elections.json {e.get('final')}")
        if row["share"] is not None and abs(row["share"] - round(e["nightPct"], 1)) > 0.055:
            fail(f"SF {e['year']}: VERIFY.md share {row['share']} != nightPct {e['nightPct']}")


def main():
    rows = load_rows()
    if len(rows) != 78:
        fail(f"expected 78 county rows, got {len(rows)}")
    tables = parse_verify_tables((V4 / "VERIFY.md").read_text())
    check_rows(rows)
    check_verify_md(rows, tables)
    check_sf(tables)
    if FAIL:
        print(f"{len(FAIL)} problems:")
        for m in FAIL:
            print(" -", m)
        sys.exit(1)
    sourced = sum(1 for r in rows if r["election_night_ballots"] is not None)
    print(f"OK: {len(rows)} rows ({sourced} sourced), VERIFY.md and elections.json agree")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it against the current tree**

Run: `python3 scripts/research/validate_election_night.py`
Expected: either `OK: 78 rows (54 sourced), ...` or a numbered failure list. Failures here are FINDINGS, not script bugs; first reread the exact JSON row and VERIFY.md line to confirm the discrepancy is real (a parser bug in the validator is also possible; fix the validator if so). Record real findings for Task 7, do not fix data yet.

- [ ] **Step 3: Check county_night.json is a fresh rebuild of v4**

```bash
python3 scripts/build_county_night.py
git diff -I '"generated"' --exit-code packages/data/county_night.json && echo IN-SYNC
git checkout -- packages/data/county_night.json
```

Expected: `IN-SYNC` (the only diff line is the `generated` date). If diff is non-empty, county_night.json is stale: keep the freshly built file instead of reverting, and note it for the Task 7 commit.

- [ ] **Step 4: Commit**

```bash
git add scripts/research/validate_election_night.py
git commit -m "verify: offline consistency validator for election-night-v4"
```

---

### Task 3: Denominator machine-check (network)

**Files:**
- Create: `scripts/research/verify_en_denominators.py`

**Interfaces:**
- Consumes: `en_common.CACHE`, `fetch`, `pdf_text`, `find_number`, `load_rows`
- Produces: `data/research/election-night-v4/cache/denominator_results.json`, a list of `{"slug", "date", "kind": "denominator", "claimed": int, "url": str, "status": "VERIFIED"|"NOT_FOUND"|"FETCH_FAILED", "evidence": str|null}` (78 entries). Task 5 reads this schema.

All 78 rows share 6 canonical CA SoS "Voter Participation Statistics by County" PDFs. Four rows cite the complete-SOV PDF instead; we check them against the same-year participation-stats PDF, which carries the identical statistic (Task 5's report notes this substitution).

- [ ] **Step 1: Write the script**

Create `scripts/research/verify_en_denominators.py`:

```python
#!/usr/bin/env python3
"""Machine-check every certified_final against the CA SoS Statement of Vote
'Voter Participation Statistics by County' PDF for that election.

Network: 6 PDF downloads, cached under cache/. Writes
cache/denominator_results.json for build_en_verification_report.py.
"""
import json
import pathlib
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import CACHE, fetch, find_number, load_rows, pdf_text

SOV = {
    2012: "https://elections.cdn.sos.ca.gov/sov/2012-general/03-voter-participation-stats-by-county.pdf",
    2014: "https://elections.cdn.sos.ca.gov/sov/2014-general/pdf/03-voter-particpiation-stats-by-county.pdf",
    2016: "https://elections.cdn.sos.ca.gov/sov/2016-general/sov/03-voter-participation-stats-by-county.pdf",
    2018: "https://elections.cdn.sos.ca.gov/sov/2018-general/sov/03-voter-participation-stats-by-county.pdf",
    2022: "https://elections.cdn.sos.ca.gov/sov/2022-general/sov/03-voter-participation-stats-by-county.pdf",
    2024: "https://elections.cdn.sos.ca.gov/sov/2024-general/sov/03-voter-participation-stats-by-county.pdf",
}


def main():
    texts = {}
    for year, url in SOV.items():
        dest = CACHE / f"sov-{year}.pdf"
        texts[year] = pdf_text(dest) if fetch(url, dest) else None

    results = []
    for r in load_rows():
        year = int(r["date"][:4])
        text = texts.get(year)
        res = {
            "slug": r["slug"], "date": r["date"], "kind": "denominator",
            "claimed": r["certified_final"], "url": SOV[year],
            "status": "FETCH_FAILED", "evidence": None,
        }
        if text:
            hit = None
            for line in text.splitlines():
                if line.strip().lower().startswith(r["county"].lower()):
                    hit = find_number(line, r["certified_final"])
                    if hit:
                        break
            res["status"] = "VERIFIED" if hit else "NOT_FOUND"
            res["evidence"] = hit
        results.append(res)

    out = CACHE / "denominator_results.json"
    out.write_text(json.dumps(results, indent=1) + "\n")
    print(Counter(x["status"] for x in results), "->", out)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it**

Run: `python3 scripts/research/verify_en_denominators.py`
Expected: `Counter({'VERIFIED': 78}) -> .../cache/denominator_results.json` within a minute or two. NOT_FOUND rows are acceptable output (they flow into the human packet); investigate only for an obvious parsing cause first, e.g. the county line wrapping in `pdftotext -layout` output. FETCH_FAILED for all rows of one year means the SoS URL moved: find the new URL on sos.ca.gov, fix the SOV map, rerun.

Gotcha: one county is named Nevada; the startswith match is against the county-table line, which is safe in these PDFs, but eyeball the Nevada evidence string in the results JSON to be sure it is a county row (it should also contain the registered-voter counts, not prose).

- [ ] **Step 3: Commit**

```bash
git add scripts/research/verify_en_denominators.py
git commit -m "verify: machine-check certified finals against SoS SoV PDFs"
```

---

### Task 4: Numerator machine-check (network)

**Files:**
- Create: `scripts/research/verify_en_numerators.py`

**Interfaces:**
- Consumes: `en_common.CACHE`, `fetch`, `pdf_text`, `strip_html`, `find_number`, `wayback_raw`, `load_rows`
- Produces: `data/research/election-night-v4/cache/numerator_results.json`, a list of `{"slug", "date", "kind": "numerator", "claimed": int, "url": str, "artifact": str, "status": "VERIFIED"|"NOT_FOUND"|"FETCH_FAILED", "evidence": str|null}` (54 entries, sourced rows only). Task 5 reads this schema.

Source mix (from the current tree): 23 Wayback HTML, 19 direct PDFs (lavote.gov, napacounty.gov, smcacre.gov, nevadacountyca.gov), 7 Clarity `sum.json` (via Wayback), 3 direct HTML (yubanet.com, likely to be FETCH_FAILED: curl-blocked, that is what the human packet is for), 2 Wayback PDFs. The check is uniform: fetch (raw `id_` form for Wayback), convert to text (pdftotext for PDFs, tag-strip for HTML, raw for JSON), then `find_number`.

- [ ] **Step 1: Write the script**

Create `scripts/research/verify_en_numerators.py`:

```python
#!/usr/bin/env python3
"""Machine-check every sourced election_night_ballots against its cited URL.

Fetches each numerator source (Wayback raw id_ form for archived pages) into
cache/numerators/, converts to text, and checks the claimed ballot count
appears. Network: ~54 fetches with a 2s pause each; artifacts are cached so
reruns only refetch failures. Writes cache/numerator_results.json.
"""
import json
import pathlib
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import (
    CACHE, fetch, find_number, load_rows, pdf_text, strip_html, wayback_raw,
)


def source_text(url, dest_base):
    """Fetch url and return (text, artifact_path). text is None on failure."""
    bare = url.lower().split("?")[0]
    is_pdf = bare.endswith(".pdf") or "documentcenter" in bare
    dest = dest_base.with_suffix(".pdf" if is_pdf else ".html")
    if not fetch(wayback_raw(url), dest):
        return None, dest
    if is_pdf:
        return pdf_text(dest), dest
    raw = dest.read_text(errors="replace")
    return (raw if bare.endswith(".json") else strip_html(raw)), dest


def main():
    results = []
    for r in load_rows():
        if r["election_night_ballots"] is None:
            continue
        url = r["source_url_night"]
        dest_base = CACHE / "numerators" / f"{r['slug']}-{r['date']}"
        text, dest = source_text(url, dest_base)
        res = {
            "slug": r["slug"], "date": r["date"], "kind": "numerator",
            "claimed": r["election_night_ballots"], "url": url,
            "artifact": str(dest), "status": "FETCH_FAILED", "evidence": None,
        }
        if text is not None:
            hit = find_number(text, r["election_night_ballots"])
            res["status"] = "VERIFIED" if hit else "NOT_FOUND"
            res["evidence"] = hit
        results.append(res)
        print(f"{res['status']:12} {r['slug']} {r['date']}")

    out = CACHE / "numerator_results.json"
    out.write_text(json.dumps(results, indent=1) + "\n")
    print(Counter(x["status"] for x in results), "->", out)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it (allow ~5 minutes)**

Run: `python3 scripts/research/verify_en_numerators.py`
Expected: 54 progress lines then a Counter, mostly VERIFIED. Known likely non-VERIFIED: the 3 yubanet.com rows (bot-blocked). Interpretation:
- NOT_FOUND with a fetched artifact: open the artifact in `cache/numerators/`; some numerators are stated with the number split across markup or as a sum of two numbers (e.g. a precinct + VBM breakdown). If the note's arithmetic checks out by hand, mark nothing; it lands in the human packet automatically.
- FETCH_FAILED on a Wayback URL: rerun the script once (cache skips successes); Wayback rate-limits.
- Do NOT edit data in this task.

- [ ] **Step 3: Commit**

```bash
git add scripts/research/verify_en_numerators.py
git commit -m "verify: machine-check election-night numerators against cited sources"
```

---

### Task 5: Merge results into MACHINE_CHECK.md + HUMAN_VERIFY.md

**Files:**
- Create: `scripts/research/build_en_verification_report.py`
- Create (generated): `data/research/election-night-v4/MACHINE_CHECK.md`
- Create (generated): `data/research/election-night-v4/HUMAN_VERIFY.md`

**Interfaces:**
- Consumes: `cache/denominator_results.json` + `cache/numerator_results.json` (schemas from Tasks 3-4), `en_common.load_rows`, `norm_pct`
- Produces: the two committed markdown reports. HUMAN_VERIFY.md is the deliverable handed to the user.

HUMAN_VERIFY.md sections: (1) every non-VERIFIED machine check, (2) the 4 secondary-confidence rows, (3) rows whose note contains `FLAG for manual operator` (blocked sources needing a real browser: Fresno 2018, Sacramento 2016), (4) a deterministic spot-check sample (every 10th machine-verified numerator). A row can appear in more than one section; that is fine, the checkbox is per entry.

- [ ] **Step 1: Write the generator**

Create `scripts/research/build_en_verification_report.py`:

```python
#!/usr/bin/env python3
"""Merge cache/*_results.json into two committed reports:

MACHINE_CHECK.md  - status of every machine check (156 rows: 78 denominator
                    + up to 78 numerator, 54 in practice)
HUMAN_VERIFY.md   - the hand-check packet: machine failures, secondary rows,
                    operator-flagged blocked sources, and a spot-check sample.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import CACHE, V4, load_rows, norm_pct


def load_results():
    res = []
    for name in ("denominator_results.json", "numerator_results.json"):
        p = CACHE / name
        if not p.exists():
            sys.exit(f"missing {p}; run the verify_en_* scripts first")
        res.extend(json.loads(p.read_text()))
    return res


def main():
    results = load_results()
    rows = {(r["slug"], r["date"]): r for r in load_rows()}
    bad = [x for x in results if x["status"] != "VERIFIED"]
    ok_num = sorted(
        (x for x in results if x["status"] == "VERIFIED" and x["kind"] == "numerator"),
        key=lambda x: (x["slug"], x["date"]),
    )
    sample = ok_num[::10]
    secondary = [r for r in rows.values() if r["confidence"] == "secondary"]
    flagged = [
        r for r in rows.values() if "FLAG for manual operator" in (r.get("note") or "")
    ]

    mc = [
        "# Machine check of election-night-v4 sources",
        "",
        "Presence checks of each claimed number against its cited URL.",
        "Denominators are checked against the canonical per-year SoS",
        "'Voter Participation Statistics by County' PDF even where a row cites",
        "the complete-SOV PDF (same statistic). Fetched artifacts live in",
        "`data/research/election-night-v4/cache/` (gitignored; rerun the",
        "verify_en_* scripts to regenerate).",
        "",
        "| County | Date | Check | Claimed | Status | Evidence (context around match) |",
        "|---|---|---|---:|---|---|",
    ]
    for x in sorted(results, key=lambda x: (x["slug"], x["date"], x["kind"])):
        ev = (x["evidence"] or "")[:120].replace("|", "\\|")
        mc.append(
            f"| {x['slug']} | {x['date']} | {x['kind']} | {x['claimed']:,} "
            f"| {x['status']} | {ev} |"
        )
    (V4 / "MACHINE_CHECK.md").write_text("\n".join(mc) + "\n")

    hv = [
        "# Hand-verification packet (election-night-v4)",
        "",
        "Open each URL and compare against the claimed value. Your reading wins:",
        "any discrepancy, even one ballot, gets corrected in the county JSON and",
        "VERIFY.md (then rerun scripts/build_county_night.py).",
        "",
    ]

    def entry(r, reason, extra=None):
        b = r["election_night_ballots"]
        claimed = f"night ballots **{b:,}**" if b is not None else "night ballots **null (recover if possible)**"
        share = norm_pct(r["election_night_pct"])
        hv.extend(
            [
                f"- [ ] **{r['slug']} {r['date']}** ({reason})",
                f"      claimed: {claimed}, certified final **{r['certified_final']:,}**"
                + (f", share **{share}%**" if share is not None else ""),
                f"      numerator URL: {r.get('source_url_night') or '(none)'}",
                f"      denominator URL: {r.get('source_url_final')}",
                f"      look for: {(r.get('note') or '')[:300]}",
            ]
        )
        if extra:
            hv.append(f"      {extra}")
        hv.append("")

    hv.append("## 1. Machine check could not verify these (open and eyeball)")
    hv.append("")
    for x in bad:
        entry(rows[(x["slug"], x["date"])], f"{x['kind']} {x['status']}")
    hv.append("## 2. Secondary-confidence rows (weakest sourcing, read closely)")
    hv.append("")
    for r in secondary:
        entry(r, "secondary confidence")
    hv.append("## 3. Blocked-source recoveries (need a real browser)")
    hv.append("")
    for r in flagged:
        entry(r, "operator-flagged", f"full flag: {r['note']}")
    hv.append("## 4. Spot-check sample of machine-verified rows (trust but verify)")
    hv.append("")
    for x in sample:
        entry(rows[(x["slug"], x["date"])], "spot-check")
    (V4 / "HUMAN_VERIFY.md").write_text("\n".join(hv) + "\n")

    print(f"MACHINE_CHECK.md: {len(results)} checks, {len(bad)} not verified")
    print(
        f"HUMAN_VERIFY.md: {len(bad)} failures + {len(secondary)} secondary "
        f"+ {len(flagged)} flagged + {len(sample)} spot-checks"
    )


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it and eyeball both outputs**

Run: `python3 scripts/research/build_en_verification_report.py`
Expected: both files written; MACHINE_CHECK.md has 132 data rows (78 denominator + 54 numerator); HUMAN_VERIFY.md sections are populated (section 3 must contain fresno-ca 2018-11-06 and sacramento-ca 2016-11-08; section 2 must contain 4 rows; section 4 has ~6). Read HUMAN_VERIFY.md top to bottom: every entry must carry a URL, a claimed value, and a look-for excerpt.

- [ ] **Step 3: Commit**

```bash
git add scripts/research/build_en_verification_report.py \
        data/research/election-night-v4/MACHINE_CHECK.md \
        data/research/election-night-v4/HUMAN_VERIFY.md
git commit -m "verify: machine-check report + hand-verification packet for v4"
```

---

### Task 6: Cleanup: normalize pct units, fix stale VERIFY.md header

**Files:**
- Modify: `data/research/election-night-v4/*.json` (the 14 fraction-unit pct values only, via targeted regex; do NOT rewrite whole files, they mix indent styles)
- Modify: `data/research/election-night-v4/VERIFY.md` (one stale line)
- Regenerate: `packages/data/county_night.json`

**Interfaces:**
- Consumes: the validator from Task 2 as the regression gate.
- Produces: v4 JSONs with `election_night_pct` uniformly in percent (2dp).

- [ ] **Step 1: Surgical unit normalization**

```bash
python3 - <<'EOF'
import pathlib, re

def to_pct(m):
    return m.group(1) + str(round(float(m.group(2)) * 100, 2))

for fp in sorted(pathlib.Path("data/research/election-night-v4").glob("*.json")):
    text = fp.read_text()
    new = re.sub(r'("election_night_pct":\s*)(0\.\d+)', to_pct, text)
    if new != text:
        fp.write_text(new)
        print("normalized", fp.name)
EOF
```

Expected: prints the county files that held fractions. Sanity: `git diff --stat data/research/election-night-v4/` shows 14 changed value lines total, each like `0.5673` -> `56.73`, nothing else. (A true fraction is always `0.x`: no share reaches 100%, so the `0\.` anchor is safe.)

- [ ] **Step 2: Fix the stale generated-from line in VERIFY.md**

In `data/research/election-night-v4/VERIFY.md` the header says the sheet was generated from `data/research/election-night-v3/*.json`; the sheet's values are v4. Edit that one reference to `data/research/election-night-v4/*.json`.

- [ ] **Step 3: Validator + rebuild must both stay clean**

```bash
python3 scripts/research/validate_election_night.py
python3 scripts/build_county_night.py
git diff -I '"generated"' --exit-code packages/data/county_night.json && echo IN-SYNC
git checkout -- packages/data/county_night.json
uv run pytest tests/test_verify_election_night.py -q
```

Expected: `OK: 78 rows ...`, then `IN-SYNC` (normalization must not change any derived value: build_county_night.py already normalized), then 11 passed.

- [ ] **Step 4: Commit**

```bash
git add data/research/election-night-v4/
git commit -m "data: normalize election_night_pct to percent units in v4 + fix VERIFY.md header"
```

---

### Task 7: Triage findings, rebuild, hand off the packet

**Files:**
- Modify (contingent): `data/research/election-night-v4/<slug>.json`, `data/research/election-night-v4/VERIFY.md`
- Regenerate (contingent): `packages/data/county_night.json`, MACHINE_CHECK.md, HUMAN_VERIFY.md

**Interfaces:**
- Consumes: findings recorded in Task 2 step 2, MACHINE_CHECK.md non-VERIFIED rows.
- Produces: a corrected, internally consistent dataset plus the packet handed to the user.

- [ ] **Step 1: Triage every non-VERIFIED machine check and every Task 2 finding**

For each one, in order:
1. Open the cached artifact (path is in `cache/numerator_results.json`) or the URL, and the row's VERIFY.md detail bullet.
2. Decide: (a) source confirms a DIFFERENT number, (b) source is unreadable or blocked to machines (leave for human), or (c) the machine check was too strict (number present but split or formatted oddly; leave data alone, note it).
3. For (a) only: fix the county JSON row (`election_night_ballots`, recompute `election_night_pct = round(ballots / final * 100, 2)`), update BOTH the VERIFY.md table line and its detail bullet, and append a sentence to the row's `note` saying what was corrected and why.

- [ ] **Step 2: Regenerate everything downstream (only if step 1 changed data)**

```bash
python3 scripts/research/validate_election_night.py
python3 scripts/build_county_night.py
python3 scripts/research/verify_en_numerators.py
python3 scripts/research/build_en_verification_report.py
pnpm vitest run
```

Expected: validator OK; build prints its jurisdictions/rows/sourced summary; rerun numerator check flips corrected rows to VERIFIED (cache note: delete the corrected rows' artifacts in `cache/numerators/` first if the fix changed which URL is cited); all vitest suites pass.

- [ ] **Step 3: Commit (only if anything changed)**

```bash
git add data/research/election-night-v4/ packages/data/county_night.json
git commit -m "data: corrections from the v4 machine verification pass"
```

- [ ] **Step 4: Hand the packet to the user**

Send `data/research/election-night-v4/HUMAN_VERIFY.md` to the user (SendUserFile) with a one-paragraph summary: how many checks ran, how many machine-verified, what needs their eyes (sections 1-3) and the spot-check sample (section 4). Their readings win; corrections come back through the Step 1 procedure. STOP here; do not chase the blocked yubanet/ABC30/GV Wire sources yourself, they are the user's browser errand or a separate browser-automation task they can request.
