#!/usr/bin/env python3
"""Recover San Francisco's registration-vs-eligible series from the California
Secretary of State's Reports of Registration.

Each ROR's county table reports, per county, the *eligible* population (the
SoS's citizen-eligible estimate, built from CA Department of Finance / Census
figures) alongside *registered* voters. That eligible column is the denominator
the project otherwise lacks: it lets us ask whether vote-by-mail enlarged the
registered share of eligible San Franciscans, not just turnout of the already-
registered.

For each Report of Registration landing page we resolve its `county.pdf` on the
SoS CDN, run pdftotext, and read the San Francisco row (first big number pair =
eligible, registered) and the "Report of Registration as of <date>" header.

Output: data/sources/sf_registration_eligible.csv (one row per report), every value
traceable to the cited county.pdf URL. Requires `pdftotext` (poppler).
"""
import csv
import re
import subprocess
import sys
import tempfile
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "data" / "sources" / "sf_registration_eligible.csv"
BASE = "https://www.sos.ca.gov/elections/report-registration/"

# Close-of-registration (15-day, or the nearest pre-election report when no
# 15-day exists) for every statewide election, plus the Feb odd-year reports,
# 2001-2026. label = the election the report's registration closes for.
REPORTS = [
    ("2026-06-02 primary", "15day-primary-2026"),
    ("2025-11-04 special", "15-day-special-2025"),
    ("2025 odd-year", "ror-odd-year-2025"),
    ("2024-11-05 general", "15day-gen-2024"),
    ("2024-03-05 presidential primary", "15day-presprim-2024"),
    ("2023 odd-year", "ror-odd-year-2023"),
    ("2022-11-08 general", "15day-general-2022"),
    ("2022-06-07 primary", "15day-primary-2022"),
    ("2021-09-14 recall", "15day-recall-2021"),
    ("2021 odd-year", "ror-odd-year-2021"),
    ("2020-11-03 general", "15day-gen-2020"),
    ("2020-03-03 presidential primary", "15day-presprim-20"),
    ("2019 odd-year", "ror-odd-year-2019"),
    ("2018-11-06 general", "15-day-gen-2018"),
    ("2018-06-05 primary", "15day-primary-2018"),
    ("2017 odd-year", "ror-odd-year-2017"),
    ("2016-11-08 general", "15day-general-2016"),
    ("2016-06-07 primary", "15day-primary-2016"),
    ("2015 odd-year", "ror-odd-year-2015"),
    ("2014-11-04 general", "report-registration-october-20-2014"),
    ("2014-06-03 primary", "15day-primary-2014"),
    ("2013 odd-year", "ror-odd-year-2013"),
    ("2012-11-06 general", "15day-general-12"),
    ("2012-06-05 primary", "15day-presprim-12"),
    ("2011 odd-year", "ror-odd-year-11"),
    ("2010-11-02 general", "15day-gen-10"),
    ("2010-06-08 primary", "15day-prim-10"),
    ("2009 odd-year", "ror-021009"),
    ("2008-11-04 general", "ror-102008"),
    ("2008-06-03 primary", "ror-05192008"),
    ("2008-02-05 presidential primary", "ror-012208"),
    ("2007 odd-year", "report-registration-february-10-2007"),
    ("2006-11-07 general", "ror-102306"),
    ("2006-06-06 primary", "ror-05222006"),
    ("2005-11-08 special", "ror-10242005"),
    ("2005 odd-year", "report-registration-february-10-2005"),
    ("2004-11-02 general", "report-registration-october-18-2004"),
    ("2004-03-02 presidential primary", "ror-021704"),
    ("2003-10-07 recall", "ror-092203"),
    ("2003 odd-year", "ror-021003"),
    ("2002-11-05 general", "ror-10212002"),
    ("2002-03-05 primary", "ror-02192002"),
    ("2001 odd-year", "ror-021001"),
]

UA = {"User-Agent": "Mozilla/5.0 (sf-election-count research; +https://github.com/Grow-SF)"}
MONTHS = {m: i for i, m in enumerate(
    "January February March April May June July August September "
    "October November December".split(), 1)}


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def county_pdf_url(landing_slug: str) -> str | None:
    html = get(BASE + landing_slug).decode("utf-8", "replace")
    urls = re.findall(
        r"https://elections\.cdn\.sos\.ca\.gov/[^\"'> ]+/county\.pdf", html)
    return urls[0] if urls else None


def parse_sf(pdf_bytes: bytes):
    """Return (as_of_date_iso, eligible, registered) from a county.pdf."""
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(pdf_bytes)
        f.flush()
        txt = subprocess.run(["pdftotext", "-layout", f.name, "-"],
                             capture_output=True, text=True).stdout
    date_iso = None
    m = re.search(r"Report of Registration as of (\w+) (\d{1,2}), (\d{4})", txt)
    if m:
        date_iso = f"{m.group(3)}-{MONTHS[m.group(1)]:02d}-{int(m.group(2)):02d}"
    # first San Francisco row with two comma-grouped numbers = eligible, registered
    reg = re.search(r"San Francisco\s+([\d,]+)\s+([\d,]+)", txt)
    if not reg:
        return date_iso, None, None
    elig = int(reg.group(1).replace(",", ""))
    rgst = int(reg.group(2).replace(",", ""))
    return date_iso, elig, rgst


def main():
    rows = []
    for label, slug in REPORTS:
        try:
            url = county_pdf_url(slug)
            if not url:
                print(f"  SKIP {label}: no county.pdf on {slug}", file=sys.stderr)
                continue
            date_iso, elig, rgst = parse_sf(get(url))
            if not (elig and rgst):
                print(f"  SKIP {label}: SF row not parsed ({url})", file=sys.stderr)
                continue
            pct = round(100 * rgst / elig, 1)
            rows.append({"report_date": date_iso, "election_context": label,
                         "eligible": elig, "registered": rgst,
                         "pct_registered_of_eligible": pct, "source_url": url})
            print(f"  {date_iso}  {label:34}  elig {elig:>7}  reg {rgst:>7}  {pct:5.1f}%")
        except Exception as e:  # noqa: BLE001 - report and continue
            print(f"  ERROR {label}: {e}", file=sys.stderr)
    rows.sort(key=lambda r: r["report_date"] or "")
    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["report_date", "election_context",
            "eligible", "registered", "pct_registered_of_eligible", "source_url"])
        w.writeheader()
        w.writerows(rows)
    print(f"\n{len(rows)} reports -> {OUT}")


if __name__ == "__main__":
    main()
