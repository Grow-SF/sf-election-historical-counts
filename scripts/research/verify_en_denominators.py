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
