#!/usr/bin/env python3
"""
SF vote-count timeline pipeline.

Stages (subcommands):
  inventory  -> out/elections.csv          (Stage 0)
  fetch      -> raw/<election>/<snap>/summary.pdf + out/manifest.csv  (Stages 1+2)
  parse      -> out/sf_count_timeline.csv  (Stage 3, era-dispatched)
  derive     -> out/sf_days_to_90.csv      (Stage 5)

Era C = Dominion-era summary PDFs (2019-present).
Era B = 2008-2018 "Unofficial Summary Report" PDFs (parser TBD).
Era A = pre-2008 (separate feasibility spike).

Columns ballots_vbm / ballots_election_day carry the per-release split wherever
the source report publishes it (227 of 240 rows). The Nov 2019 report layout
contains no VBM/election-day breakdown anywhere in the PDF, so those 13 rows
are blank by design. Do not backfill from the eData "Status of Returned VBM
Ballots" tool: returned-and-accepted is not the same measure as counted.
"""
import csv, re, sys, time, datetime as dt
from pathlib import Path

import requests

BASE = "https://www.sfelections.org/results"
ROOT = Path(__file__).parent
RAW, OUT = ROOT / "raw", ROOT / "out"
UA = {"User-Agent": "Mozilla/5.0 (research; SF vote-count timeline)"}
DELAY = 0.25
PROBE_DAYS = 35
NIGHT_SUFFIXES = range(1, 7)

ERA_C_START = dt.date(2019, 1, 1)   # Dominion era
ERA_B_START = dt.date(2008, 1, 1)

S = requests.Session()
S.headers.update(UA)


def log(msg):
    print(msg, flush=True)


def get(url, **kw):
    time.sleep(DELAY)
    return S.get(url, timeout=30, **kw)


# ---------------------------------------------------------------- Stage 0
MONTHS = {m: i + 1 for i, m in enumerate(
    "January February March April May June July August September October November December".split())}

def stage_inventory():
    r = get("https://www.sf.gov/results")
    r.raise_for_status()
    pat = re.compile(
        r"(January|February|March|April|May|June|July|August|September|October|November|December)"
        r"\s+(\d{1,2}),\s+(\d{4})[, ]*([^\\<]{0,70}?Election[^\\<]{0,30}?)(?:\\u003c|<)")
    seen = {}
    for m, d, y, name in pat.findall(r.text):
        date = dt.date(int(y), MONTHS[m], int(d))
        name = re.sub(r"\s+", " ", name).strip(" ,").removesuffix(" Results")
        if date >= dt.date(2000, 11, 1):
            seen[date] = name
    OUT.mkdir(exist_ok=True)
    with open(OUT / "elections.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["election_date", "election_name", "era"])
        for date in sorted(seen):
            era = "C" if date >= ERA_C_START else "B" if date >= ERA_B_START else "A"
            w.writerow([date.isoformat(), seen[date], era])
    log(f"inventory: {len(seen)} elections -> out/elections.csv")


def load_elections(eras=("C",)):
    with open(OUT / "elections.csv") as f:
        return [row for row in csv.DictReader(f) if row["era"] in eras]


# ------------------------------------------------------------- Stages 1+2
def snap_candidates(edate: dt.date):
    e = edate.strftime("%Y%m%d")
    for n in NIGHT_SUFFIXES:
        yield f"{e}_{n}"
    for i in range(PROBE_DAYS + 1):
        yield (edate + dt.timedelta(days=i)).strftime("%Y%m%d")


def stage_fetch(eras=("C",)):
    rows = []
    misses_file = OUT / "probe_misses.txt"
    known_miss = set(misses_file.read_text().split()) if misses_file.exists() else set()
    for el in load_elections(eras):
        edate = dt.date.fromisoformat(el["election_date"])
        e = edate.strftime("%Y%m%d")
        misses = 0
        for snap in snap_candidates(edate):
            dest = RAW / e / snap / "summary.pdf"
            if dest.exists():
                rows.append((e, snap, "cached")); continue
            url = f"{BASE}/{e}/data/{snap}/summary.pdf"
            if url in known_miss:
                misses += 1; continue
            r = get(url)
            if r.status_code == 200 and r.content[:4] == b"%PDF":
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(r.content)
                rows.append((e, snap, "downloaded"))
            else:
                misses += 1
                # future report dates for an ongoing count are not permanent misses
                if dt.date.today() > edate + dt.timedelta(days=PROBE_DAYS):
                    known_miss.add(url)
        misses_file.write_text("\n".join(sorted(known_miss)))
        found = sum(1 for x in rows if x[0] == e)
        log(f"fetch {e}: {found} snapshots ({misses} probes missed)")
    with open(OUT / "manifest.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["election", "snapshot", "status"]); w.writerows(rows)


# ---------------------------------------------------------------- Stage 3
TS_RE = re.compile(r"(\d{1,2}/\d{1,2}/\d{4})\s+(\d{1,2}:\d{2}:\d{2}\s*[AP]M)")
NUM = r"([\d,]+)"

def parse_era_c(text):
    """Dominion turnout block on page 1 (two layout variants)."""
    out = {}
    m = re.search(rf"Election Day\s+{NUM}", text)
    out["ballots_election_day"] = m and int(m[1].replace(",", ""))
    m = re.search(rf"Vote by Mail\s+{NUM}", text)
    out["ballots_vbm"] = m and int(m[1].replace(",", ""))
    m = re.search(rf"Total\s+{NUM}\s+{NUM}\s+[\d.]+%", text)
    if m:
        out["ballots_counted_total"] = int(m[1].replace(",", ""))
        out["registered_voters"] = int(m[2].replace(",", ""))
    else:
        # 2019-era variant: "Registered Voters: 206,025 of 495,050 (41.62%)".
        # NB: this layout's "Ballots Cast" field counts ballot CARDS - never use it.
        m = re.search(rf"Registered Voters:\s+{NUM}\s+of\s+{NUM}", text)
        if not m:
            return None
        out["ballots_counted_total"] = int(m[1].replace(",", ""))
        out["registered_voters"] = int(m[2].replace(",", ""))
    ts = TS_RE.search(text)
    if ts:
        out["report_datetime"] = dt.datetime.strptime(
            f"{ts[1]} {ts[2].replace(' ', '')}", "%m/%d/%Y %I:%M:%S%p").isoformat()
    return out


def parse_era_b(text):
    """2008-2018 'Unofficial Summary Report': labeled turnout lines.

    Primaries repeat the block per party; the citywide block always has the
    largest values, so take the max of every match.
    """
    out = {}
    def mx(pat):
        vals = [int(v.replace(",", "")) for v in re.findall(pat, text)]
        return max(vals) if vals else None
    out["registered_voters"] = mx(rf"Registration & Turnout\s+{NUM}\s+Voters")
    out["ballots_election_day"] = mx(rf"Election Day Reporting\s*Turnout\s+{NUM}")
    out["ballots_vbm"] = mx(rf"VBM Reporting\s*Turnout\s+{NUM}")
    if out["ballots_election_day"] is None or out["ballots_vbm"] is None:
        return None
    out["ballots_counted_total"] = out["ballots_election_day"] + out["ballots_vbm"]
    ts = TS_RE.search(text)
    if ts:
        out["report_datetime"] = dt.datetime.strptime(
            f"{ts[1]} {ts[2].replace(' ', '')}", "%m/%d/%Y %I:%M:%S%p").isoformat()
    return out


PARSERS = {"C": ("era_c", parse_era_c), "B": ("era_b", parse_era_b)}

# Rows recovered from web-archive captures of the live results pages
# (Archive-It memento of sfelections.org/results/20121106/, captured
# 2012-11-12 02:00 UTC, page self-reports "Last Updated: November 11, 2012
# 16:28:21"). Sparse by nature; parser tag "archival" excludes them from
# days-to-90 derivation. Certified finals from the live final pages.
ARCHIVAL_ROWS = [
    dict(election_date="2012-11-06", election_name="Consolidated General Election",
         snapshot="wb20121112020016", report_datetime="2012-11-11T16:28:21",
         ballots_counted_total=325298, ballots_vbm=174755,
         ballots_election_day=150543, registered_voters=502841,
         parser="archival",
         source_url="https://wayback.archive-it.org/all/20121112020016/http://sfelections.org/results/20121106/"),
    dict(election_date="2012-11-06", election_name="Consolidated General Election",
         snapshot="final", report_datetime="2012-12-04T16:00:00",
         ballots_counted_total=364875, ballots_vbm=193196,
         ballots_election_day=171679, registered_voters=502841,
         parser="archival",
         source_url="https://www.sfelections.org/results/20121106/"),
]


def stage_parse(eras=("C",)):
    import pdfplumber
    eldict = {dt.date.fromisoformat(e["election_date"]).strftime("%Y%m%d"): e
              for e in load_elections(eras)}
    rows, failures = [], []
    for pdf_path in sorted(RAW.glob("*/*/summary.pdf")):
        e, snap = pdf_path.parts[-3], pdf_path.parts[-2]
        if e not in eldict:
            continue
        try:
            with pdfplumber.open(pdf_path) as pdf:
                text = pdf.pages[0].extract_text() or ""
            pname, pfunc = PARSERS[eldict[e]["era"]]
            rec = pfunc(text)
            if not rec:
                raise ValueError("turnout block not found")
        except Exception as ex:
            failures.append((str(pdf_path), repr(ex)))
            continue
        el = eldict[e]
        rec.update(
            election_date=el["election_date"], election_name=el["election_name"],
            snapshot=snap, parser=pname,
            source_url=f"{BASE}/{e}/data/{snap}/summary.pdf")
        rec.setdefault("report_datetime",
                       dt.datetime.strptime(snap.split("_")[0], "%Y%m%d").isoformat())
        rows.append(rec)

    rows.extend(ARCHIVAL_ROWS)
    rows.sort(key=lambda r: (r["election_date"], r["report_datetime"], r["snapshot"]))
    seq, last_e = 0, None
    for r in rows:
        seq = seq + 1 if r["election_date"] == last_e else 1
        r["report_seq"], last_e = seq, r["election_date"]

    cols = ["election_date", "election_name", "report_seq", "snapshot",
            "report_datetime", "ballots_counted_total", "ballots_vbm",
            "ballots_election_day", "registered_voters", "parser", "source_url"]
    with open(OUT / "sf_count_timeline.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    with open(OUT / "parse_failures.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["file", "error"]); w.writerows(failures)
    log(f"parse: {len(rows)} rows, {len(failures)} failures")

    # Stage 4 inline check: monotonicity
    prev = {}
    for r in rows:
        k = r["election_date"]
        if k in prev and r["ballots_counted_total"] < prev[k]:
            log(f"  WARN non-monotonic: {k} {r['snapshot']} "
                f"{r['ballots_counted_total']} < {prev[k]}")
        prev[k] = r["ballots_counted_total"]


# ---------------------------------------------------------------- Stage 5
def stage_derive():
    with open(OUT / "sf_count_timeline.csv") as f:
        rows = list(csv.DictReader(f))
    by_el = {}
    for r in rows:
        if r["parser"] == "archival":
            continue  # sparse captures cannot support days-to-90
        by_el.setdefault(r["election_date"], []).append(r)
    out = []
    for e, rs in sorted(by_el.items()):
        final = max(int(r["ballots_counted_total"]) for r in rs)
        edate = dt.date.fromisoformat(e)
        cross = next((r for r in rs
                      if int(r["ballots_counted_total"]) >= 0.9 * final), None)
        cdt = dt.datetime.fromisoformat(cross["report_datetime"])
        out.append(dict(
            election_date=e, election_name=rs[0]["election_name"],
            final_ballots=final, n_reports=len(rs),
            date_90pct=cdt.date().isoformat(),
            days_to_90pct=(cdt.date() - edate).days,
            pct_on_election_night=round(100 * max(
                (int(r["ballots_counted_total"]) for r in rs
                 if r["snapshot"].startswith(edate.strftime("%Y%m%d"))
                 and dt.datetime.fromisoformat(r["report_datetime"]).date()
                 <= edate + dt.timedelta(days=1)), default=0) / final, 1)))
    cols = list(out[0].keys())
    with open(OUT / "sf_days_to_90.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(out)
    for r in out:
        log(f"{r['election_date']}  final={r['final_ballots']:>7,}  "
            f"night={r['pct_on_election_night']:>5}%  90% on day {r['days_to_90pct']}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    eras = tuple(sys.argv[2].split(",")) if len(sys.argv) > 2 else ("C",)
    if cmd in ("inventory", "all"): stage_inventory()
    if cmd in ("fetch", "all"):     stage_fetch(eras)
    if cmd in ("parse", "all"):     stage_parse(eras)
    if cmd in ("derive", "all"):    stage_derive()
