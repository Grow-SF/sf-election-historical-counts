# Plateau Verification (Fable Direct) Implementation Plan

> **For agentic workers:** this plan is executed INLINE by the controller model itself (the user asked for the expensive model's own judgment, not subagents). Steps use checkbox (`- [ ]`) syntax for tracking. Scripts do mechanical extraction only; every verdict is the controller's own read.

**Goal:** For all 54 sourced election-night numerators in `data/research/election-night-v4/`, establish with the controller's own judgment, and non-circular evidence where obtainable, that each cited report is the election-night PLATEAU (last report posted election night), and correct or downgrade any row that fails.

**Architecture:** Two small helper scripts prepare compact evidence: one extracts self-describing header/timestamp/label lines from the already-cached artifacts (no network), one enumerates Clarity ENR version histories (bounded network). The controller then adjudicates all 54 rows against explicit criteria, records verdicts in a committed `plateau_review.json` + `PLATEAU_REVIEW.md`, folds verdicts into the human packet, and applies any data corrections through the existing pipeline and gates.

**Tech Stack:** Python 3 stdlib reusing `scripts/research/en_common.py`, curl, pdftotext, Wayback CDX API, Clarity ENR CDN.

## Global Constraints

- No em dashes in any prose written (comma/colon/parens instead).
- Never hand-edit `packages/data/county_night.json`; regenerate via `python3 scripts/build_county_night.py`.
- Data corrections follow the established Task 7 procedure: county JSON + VERIFY.md table line + detail bullet + appended note sentence, then validator + rebuild + report regen + pytest (17) + vitest (26).
- Token economy: scripts print COMPACT evidence blocks; the controller deep-reads a full artifact only when the compact block is ambiguous. No subagent dispatches.
- The human's reading still wins: the deliverable ends with an updated HUMAN_VERIFY.md carrying the controller's verdict per row, so the user can audit any row and override.
- Verdict vocabulary (exactly these):
  - `CONFIRMED`: artifact self-describes as end-of-night (late-night internal timestamp, or a "last of the night" / "semi-final election night" label) AND at least one non-circular leg holds (report series shows the next report is post-night; or a later capture shows the count held; or a Clarity version enumeration brackets it).
  - `PLAUSIBLE`: self-description is consistent with a plateau but no independent series evidence is obtainable.
  - `REFUTED`: evidence the report is an early tranche (e.g. 0% precincts, pre-10pm first release) or a post-night canvass state (e.g. next-afternoon timestamp with a count above the frozen night value).
- Refuted rows are corrected (right report found) or nulled with confidence `none` per the dataset's own rule ("Null per definition") and the note updated; PLAUSIBLE rows keep their value but their packet entry says exactly what is missing.

---

### Task 1: Artifact self-description extractor (offline)

**Files:**
- Create: `scripts/research/extract_plateau_evidence.py`
- Output (gitignored): `data/research/election-night-v4/cache/plateau_evidence.json`

**Interfaces:**
- Consumes: `en_common.CACHE`, `V4`, `load_rows`, `pdf_text`, `strip_html`; cached artifacts `cache/numerators/<slug>-<date>.(pdf|html)` from the numerator machine-check.
- Produces: per sourced row, a compact JSON record `{slug, date, claimed, artifact, head, stamps, labels}` where `head` = first 300 chars of artifact text, `stamps` = up to 8 timestamp-context snippets, `labels` = up to 8 lines containing plateau-relevant vocabulary. Task 3 reads this.

- [ ] **Step 1: Write the script**

```python
#!/usr/bin/env python3
"""Extract self-describing plateau evidence from the cached numerator artifacts.

For each sourced election row, pull the artifact's opening text, every
timestamp-looking snippet, and every line carrying plateau vocabulary
(night / semi-final / unofficial / last / as of). Output is a compact
JSON + stdout digest for the controller to adjudicate. No network.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import CACHE, pdf_text, strip_html, load_rows

STAMP = re.compile(
    r"(?:[01]?\d/[0-3]?\d/(?:20)?\d\d[^\n]{0,60})"
    r"|(?:\d{1,2}:\d{2}(?::\d{2})?\s*(?:AM|PM|am|pm)[^\n]{0,40})"
    r"|(?:websiteupdatedat[^,}]{0,60})"
)
LABEL = re.compile(
    r"night|semi[- ]?final|unofficial|last of|last update|as of|final report"
    r"|first report|zero report|canvass",
    re.I,
)


def artifact_text(p):
    if p.suffix == ".pdf":
        return pdf_text(p)
    raw = p.read_text(errors="replace")
    return raw if raw.lstrip()[:1] in "{[" else strip_html(raw)


def main():
    out = []
    for r in load_rows():
        if r["election_night_ballots"] is None:
            continue
        base = CACHE / "numerators" / f"{r['slug']}-{r['date']}"
        p = next((base.with_suffix(s) for s in (".pdf", ".html") if base.with_suffix(s).exists()), None)
        if p is None:
            out.append({"slug": r["slug"], "date": r["date"], "artifact": None})
            continue
        text = artifact_text(p)
        stamps, labels = [], []
        for m in STAMP.finditer(text):
            s = " ".join(m.group().split())
            if s not in stamps:
                stamps.append(s)
            if len(stamps) >= 8:
                break
        for line in text.splitlines():
            line = " ".join(line.split())
            if line and LABEL.search(line) and line[:120] not in labels:
                labels.append(line[:120])
            if len(labels) >= 8:
                break
        out.append({
            "slug": r["slug"], "date": r["date"],
            "claimed": r["election_night_ballots"], "artifact": p.name,
            "head": " ".join(text[:300].split()),
            "stamps": stamps, "labels": labels,
        })
    dest = CACHE / "plateau_evidence.json"
    dest.write_text(json.dumps(out, indent=1) + "\n")
    assert len(out) == 54, f"expected 54 sourced rows, got {len(out)}"
    for rec in out:
        print(f"== {rec['slug']} {rec['date']} claimed={rec.get('claimed'):,}")
        print(f"   head: {rec.get('head','')[:160]}")
        for s in rec.get("stamps", []):
            print(f"   stamp: {s}")
        for l in rec.get("labels", []):
            print(f"   label: {l}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it and check the digest**

Run: `python3 scripts/research/extract_plateau_evidence.py > /tmp/plateau_digest.txt; wc -l /tmp/plateau_digest.txt` (use the session scratchpad dir, not /tmp, when executing).
Expected: exits clean (54-row assertion), digest of roughly 300-600 lines. Missing-artifact rows (artifact None) should be zero since all 54 artifacts are cached.

- [ ] **Step 3: Commit**

```bash
git add scripts/research/extract_plateau_evidence.py
git commit -m "verify: plateau-evidence extractor over cached numerator artifacts"
```

---

### Task 2: Clarity version-history enumerator (bounded network)

**Files:**
- Create: `scripts/research/fetch_clarity_versions.py`
- Output (gitignored): `data/research/election-night-v4/cache/clarity_versions.json`

**Interfaces:**
- Consumes: `en_common.fetch`, `CACHE`, `load_rows`; the live Clarity CDN (`results.enr.clarityelections.com`), which serves immutable version-pinned data.
- Produces: for each row whose numerator URL contains `clarityelections.com` (7 rows), the cited version's `websiteupdatedat`, the full `versions` array from its `electionsettings.json`, and the `websiteupdatedat` + `BC` of the NEXT published version. This is the non-circular bracket: cited version stamped election night, next version stamped post-night.

- [ ] **Step 1: Write the script**

```python
#!/usr/bin/env python3
"""Enumerate Clarity ENR version history around each cited election-night version.

For every sourced row citing results.enr.clarityelections.com, fetch the cited
version's electionsettings.json (websiteupdatedat + full versions array), find
the next published version, and fetch its electionsettings.json and sum.json
(timestamp + BC). Bounded: 7 rows x <=3 fetches. Cached like everything else.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import CACHE, fetch, load_rows

BASE = "https://results.enr.clarityelections.com"
PAT = re.compile(r"clarityelections\.com/(CA/[^/]+)/(\d+)/(\d+)/json")


def get_json(url, dest):
    if not fetch(url, dest):
        return None
    try:
        return json.loads(dest.read_text(errors="replace"))
    except json.JSONDecodeError:
        return None


def main():
    out = []
    for r in load_rows():
        u = r.get("source_url_night") or ""
        m = PAT.search(u)
        if r["election_night_ballots"] is None or not m:
            continue
        path, eid, ver = m.groups()
        cdir = CACHE / "clarity" / f"{r['slug']}-{r['date']}"
        rec = {"slug": r["slug"], "date": r["date"], "election_id": eid,
               "cited_version": ver, "cited_updatedat": None,
               "versions": None, "next_version": None,
               "next_updatedat": None, "next_bc": None}
        es = get_json(f"{BASE}/{path}/{eid}/{ver}/json/en/electionsettings.json",
                      cdir / f"settings-{ver}.json")
        if es:
            rec["cited_updatedat"] = es.get("websiteupdatedat")
            versions = sorted(int(v) for v in es.get("versions", []) if str(v).isdigit())
            rec["versions"] = versions
            later = [v for v in versions if v > int(ver)]
            if later:
                nv = later[0]
                rec["next_version"] = nv
                nes = get_json(f"{BASE}/{path}/{eid}/{nv}/json/en/electionsettings.json",
                               cdir / f"settings-{nv}.json")
                if nes:
                    rec["next_updatedat"] = nes.get("websiteupdatedat")
                ns = get_json(f"{BASE}/{path}/{eid}/{nv}/json/sum.json",
                              cdir / f"sum-{nv}.json")
                if ns:
                    bc = ns.get("BC")
                    if bc is None and ns.get("Contests"):
                        bc = ns["Contests"][0].get("BC")
                    rec["next_bc"] = bc
        out.append(rec)
        print(f"{r['slug']} {r['date']}: v{ver} @ {rec['cited_updatedat']} -> "
              f"next v{rec['next_version']} @ {rec['next_updatedat']} (BC {rec['next_bc']})")
    dest = CACHE / "clarity_versions.json"
    dest.write_text(json.dumps(out, indent=1) + "\n")
    print(f"{len(out)} clarity rows -> {dest}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run it**

Run: `python3 scripts/research/fetch_clarity_versions.py`
Expected: 7 rows printed, each with a cited timestamp on its election night (local evening) and a next version stamped a later day (or later that produces a higher BC). A cited version whose timestamp is NOT election night, or a next version stamped the SAME night, is a finding for Task 3's adjudication. Clarity CDN quirks: if `electionsettings.json` 404s at that path, try `.../json/electionsettings.json` (no `en/`) once, note which worked in the report; if the CDN blocks entirely, record nulls, the row falls back to PLAUSIBLE-track adjudication.

- [ ] **Step 3: Commit**

```bash
git add scripts/research/fetch_clarity_versions.py
git commit -m "verify: clarity version-history enumerator for plateau brackets"
```

---

### Task 3: Controller adjudication of all 54 rows

**Files:**
- Create: `data/research/election-night-v4/plateau_review.json` (COMMITTED; the durable verdicts)
- Create: `data/research/election-night-v4/PLATEAU_REVIEW.md` (committed digest of the same)

**Interfaces:**
- Consumes: the Task 1 digest, the Task 2 brackets, the v4 notes and VERIFY.md bullets (as claims to test, not as evidence), cached artifacts for deep-reads, Wayback CDX (`https://web.archive.org/cdx/search/cdx?url=<U>&output=json&from=<Y>1101&to=<Y>1215`) when a same-night capture series is needed.
- Produces: one record per sourced row: `{slug, date, verdict, basis, evidence}` where `verdict` in CONFIRMED / PLAUSIBLE / REFUTED, `basis` names the non-circular leg (e.g. "clarity bracket", "self-describing last-of-night header + held in later capture", "press release states election-night total", "internal timestamp only"), and `evidence` quotes the decisive line(s). Task 4 consumes verdicts.

- [ ] **Step 1: Adjudicate the mechanically bracketed groups first (fast passes)**

- Clarity rows (7): CONFIRMED iff cited `websiteupdatedat` falls on election night local time AND next version is post-night (or same-night-later with higher BC, in which case the CITED version is refuted as non-final and the row is a finding).
- LA press releases (6): read the artifact's own sentences ("Semi-Final ... On Election Night a total of N ballots were counted"); these self-describe both the total and its election-night scope: CONFIRMED on the document text alone plus the release URL date.
- Napa First/Last report series (6): county publishes explicit "Last Unofficial Election Night Report" titled PDFs or "(Last of the Night)" headers; CONFIRMED from the title line; the 2014 row is a documented floor (10:30 PM report, exact 10:42 PM final unarchived): cap it at PLAUSIBLE and keep confidence `secondary`.

- [ ] **Step 2: Adjudicate the header-timestamp group (GEMS/county static reports)**

For each remaining row: take the artifact's internal timestamp + precincts-reporting line from the Task 1 digest. CONFIRMED needs the second leg; obtain it per row from ONE of: a later Wayback capture of the same URL showing the same frozen count (CDX query + one fetch), a next-report file days later in the same series (county DocumentCenter / results folder), or the certified total exceeding the claimed count with the note's progression corroborated by the artifact itself. Budget: at most ~15 CDX/fetch calls total; rows where the leg is not obtainable get PLAUSIBLE, not silence.

- [ ] **Step 3: Adjudicate the known-weak rows with extra care (list them explicitly in PLATEAU_REVIEW.md)**

- placer-ca 2018-11-06: artifact header reads `11/09/18 15:15:00`, three days post-night. Test the note's frozen-count claim: CDX-enumerate the URL's November 2018 captures; if an on-night or next-morning capture shows the same 113,380, CONFIRMED; if captures show lower same-night counts or the count moved before 11/09, REFUTED (fix or null per the criteria); if no other capture exists, PLAUSIBLE and downgrade confidence to `secondary` if not already.
- sacramento-ca 2012-11-06: numerator presence already machine-unverifiable (sole capture holds the Nov 30 canvass). Unless a CDX sweep finds any other capture or an alternative official document, verdict REFUTED-as-sourced (the CITED source does not evidence the number): null the row per the dataset rule, or re-source it if the sweep finds a real election-night document.
- The 3 yubanet rows (nevada 2012 is county PDF, so specifically 2016/2018/2022): the cached article text self-describes ("counted as of tonight", "at the end of election night"): CONFIRMED as sourced but keep confidence `secondary` (news proxy).

- [ ] **Step 4: Write the committed verdicts**

Write `plateau_review.json` (all 54 records, sorted slug/date) and generate `PLATEAU_REVIEW.md` from it (a table: county, date, verdict, basis, one-line evidence; plus a section listing every non-CONFIRMED row with what is missing). Counts printed and stated in the MD header. No script needed; the controller writes both files (the JSON is the artifact later tooling reads).

- [ ] **Step 5: Commit**

```bash
git add data/research/election-night-v4/plateau_review.json data/research/election-night-v4/PLATEAU_REVIEW.md
git commit -m "verify: controller plateau adjudication of all 54 sourced rows"
```

---

### Task 4: Apply outcomes and fold verdicts into the packet

**Files:**
- Modify (contingent on REFUTED rows): `data/research/election-night-v4/<slug>.json`, `VERIFY.md`
- Modify: `scripts/research/build_en_verification_report.py` (packet entries gain a verdict line)
- Regenerate: `packages/data/county_night.json` (if data changed), `MACHINE_CHECK.md`, `HUMAN_VERIFY.md`

**Interfaces:**
- Consumes: `plateau_review.json` verdicts.
- Produces: corrected dataset + a packet where each entry shows the controller's verdict, so the human can start from the non-CONFIRMED rows.

- [ ] **Step 1: Apply REFUTED corrections** via the established procedure (county JSON + VERIFY.md line + bullet + note sentence; null with confidence `none` when no valid plateau source exists). Downgrade any CONFIRMED-failed-to-PLAUSIBLE rows' confidence only where Task 3 said so.

- [ ] **Step 2: Teach the packet generator the verdicts**

In `build_en_verification_report.py`, load `V4 / "plateau_review.json"` when present (tolerate absence) into `pv = {(slug, date): rec}`, and inside `entry()` append after the "your check" line:

```python
        rec = pv.get((r["slug"], r["date"]))
        if rec:
            hv.append(
                f"      controller verdict: {rec['verdict']} ({rec['basis']})"
            )
```

Reorder nothing; section 4 stays complete. Update the HUMAN_VERIFY.md preamble sentence "the plateau judgment is yours on every sourced row below" to add: "a controller (Fable) verdict line now accompanies each row; treat non-CONFIRMED rows as first priority, and spot-audit CONFIRMED ones."

- [ ] **Step 3: Regenerate and gate**

```bash
python3 scripts/research/validate_election_night.py
python3 scripts/build_county_night.py
python3 scripts/research/build_en_verification_report.py
uv run pytest tests/test_verify_election_night.py -q
pnpm vitest run
```

Expected: validator OK (or exits 1 only if a REFUTED fix has an intermediate inconsistency, which must be resolved before commit); pytest 17; vitest 26. Keep the rebuilt `county_night.json` if data changed, revert the date-only diff otherwise.

- [ ] **Step 4: Commit and hand off**

```bash
git add data/research/election-night-v4/ packages/data/county_night.json scripts/research/build_en_verification_report.py
git commit -m "data: apply plateau adjudication outcomes; packet carries controller verdicts"
```

Send the user: PLATEAU_REVIEW.md + the regenerated HUMAN_VERIFY.md, with a summary stating verdict counts, every REFUTED/PLAUSIBLE row and why, and the explicit reminder that their reading overrides any CONFIRMED verdict.
