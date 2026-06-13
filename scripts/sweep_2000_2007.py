#!/usr/bin/env python3
"""
Sweep Chronicle/SFGate articles for 2000-2007 elections.
Sequential fetches with 2-3s sleep between requests.
"""

import os
from pathlib import Path
import re
import sys
import time
import random
import urllib.request
import urllib.error

MIRROR_DIR = os.environ.get(
    "SF_MIRROR_DIR",
    str(Path(__file__).resolve().parent.parent / "mirror" / "chronicle-sfgate"),
)

# Target elections: sweep E+0 night, E+1, E+2, E+3
TARGET_ELECTIONS = [
    "2000-03-07",
    "2000-11-07",
    "2000-12-12",
    "2001-11-06",
    "2001-12-11",
    "2002-03-05",
    "2002-11-05",
    "2002-12-10",
    "2003-10-07",
    "2003-11-04",
    "2003-12-09",
    "2005-11-08",
    "2007-11-06",
]


def sleep_normal():
    t = random.uniform(2.0, 3.0)
    time.sleep(t)


def sleep_long():
    print("  [rate limit hit] sleeping 120s...", flush=True)
    time.sleep(120)


def fetch_url(url, retries=2):
    """Fetch URL, return bytes or None. Handles 429/connection errors."""
    headers = {
        "User-Agent": "Mozilla/5.0 (research/archive-fetch)",
        "Accept": "text/html,*/*",
    }
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                sleep_long()
                continue
            elif e.code in (404, 403):
                return None
            else:
                print(f"  HTTP {e.code} for {url}", flush=True)
                return None
        except Exception as e:
            if attempt < retries:
                print(f"  Error ({e}), retrying...", flush=True)
                time.sleep(5)
            else:
                print(f"  Failed: {e}", flush=True)
                return None
    return None


def cdx_query(date_str):
    """Query CDX for all articles on a given date. Returns list of (ts, url) tuples."""
    yyyy, mm, dd = date_str.split("-")

    results = []

    # Old-style URL (pre-2004): /cgi-bin/article.cgi?file=/chronicle/archive/YYYY/MM/DD/
    old_url = f"sfgate.com/cgi-bin/article.cgi%3Ffile%3D/chronicle/archive/{yyyy}/{mm}/{dd}/"
    # New-style URL (2004+): /cgi-bin/article.cgi?f=/c/a/YYYY/MM/DD/
    new_url1 = f"sfgate.com/cgi-bin/article.cgi%3Ff%3D/c/a/{yyyy}/{mm}/{dd}/"
    # Also try ?file=/c/a/
    new_url2 = f"sfgate.com/cgi-bin/article.cgi%3Ffile%3D/c/a/{yyyy}/{mm}/{dd}/"

    for pattern in [old_url, new_url1, new_url2]:
        cdx_url = (
            f"http://web.archive.org/cdx/search/cdx?"
            f"url={pattern}&matchType=prefix&output=text&collapse=urlkey&limit=300"
        )
        data = fetch_url(cdx_url)
        sleep_normal()
        if not data:
            continue
        for line in data.decode("utf-8", errors="replace").strip().split("\n"):
            parts = line.split()
            if len(parts) >= 3:
                ts = parts[1]
                orig_url = parts[2]
                results.append((ts, orig_url))

    # Deduplicate by urlkey
    seen = set()
    unique = []
    for ts, url in results:
        key = url.lower()
        if key not in seen:
            seen.add(key)
            unique.append((ts, url))

    return unique


def save_article(ts, url, election_date):
    """Fetch and save an article. Returns saved filepath or None."""
    wayback_url = f"http://web.archive.org/web/{ts}id_/{url}"
    data = fetch_url(wayback_url)
    sleep_normal()
    if not data:
        return None

    # Build filename
    date_compact = election_date.replace("-", "")
    # Extract filename from URL
    fn_match = re.search(r'/([^/]+\.DTL)', url, re.IGNORECASE)
    if fn_match:
        fn = fn_match.group(1)
    else:
        fn = ts + "_" + re.sub(r'[^\w]', '_', url[-40:])

    outname = f"{date_compact}_{fn}.html"
    outpath = os.path.join(MIRROR_DIR, outname)

    if os.path.exists(outpath):
        return outpath  # already have it

    with open(outpath, "wb") as f:
        f.write(data)
    return outpath


def is_election_article(url):
    """Prioritize election-relevant articles."""
    url_lower = url.lower()
    # Skip printable duplicates
    if "type=printable" in url_lower or "type=p" in url_lower:
        return False, 0
    # High priority: explicit election type or election keywords in name
    if "type=election" in url_lower:
        return True, 3
    # MN codes are news (high value)
    if re.search(r'/MN\d+\.DTL', url, re.IGNORECASE):
        return True, 2
    # Descriptive names with election keywords
    election_words = ["ballot", "elect", "vote", "absentee", "precinct", "certif", "runoff", "tally", "count"]
    for w in election_words:
        if w in url_lower:
            return True, 2
    # Other DTL files
    if ".DTL" in url.upper():
        return True, 1
    return False, 0


def scan_article_text(filepath, election_date):
    """Scan article for relevant election data quotes. Returns list of findings."""
    with open(filepath, "rb") as f:
        raw = f.read()

    text = raw.decode("utf-8", errors="replace")

    # Strip HTML tags
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = re.sub(r'&nbsp;', ' ', clean)
    clean = re.sub(r'&amp;', '&', clean)
    clean = re.sub(r'&#\d+;', ' ', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()

    findings = []

    # Keywords to search for
    patterns = [
        r'[^.]*(?:absentee|provisional)[^.]*(?:ballot|vote)[^.]*[0-9,]+[^.]*\.',
        r'[^.]*[0-9,]+[^.]*(?:absentee|provisional)[^.]*\.',
        r'[^.]*(?:ballots? remain|ballots? uncounted|remain(?:ing)? uncounted)[^.]*\.',
        r'[^.]*(?:precinct[s]? report(?:ing|ed))[^.]*\.',
        r'[^.]*(?:all precinct)[^.]*\.',
        r'[^.]*(?:ballots? cast)[^.]*[0-9,]+[^.]*\.',
        r'[^.]*[0-9,]+[^.]*(?:ballots? cast)[^.]*\.',
        r'[^.]*(?:voter turnout)[^.]*[0-9,]+[^.]*\.',
        r'[^.]*(?:registrar)[^.]*(?:certif|count|tally)[^.]*\.',
        r'[^.]*(?:as of \d+(?::\d+)? [ap]\.?m\.?)[^.]*\.',
        r'[^.]*(?:final count|official count|official tally)[^.]*[0-9,]+[^.]*\.',
        r'[^.]*(?:election night)[^.]*[0-9,]+[^.]*\.',
    ]

    # Filter for SF-related content
    sf_context = re.search(
        r'(?:san francisco|sf|city (?:and county|hall)|sfgate|registrar of voters)',
        clean, re.IGNORECASE
    )

    for pat in patterns:
        for m in re.finditer(pat, clean, re.IGNORECASE):
            snippet = m.group(0).strip()[:300]
            if len(snippet) > 20:
                findings.append(snippet)

    return findings, sf_context is not None


def get_article_title(filepath):
    """Extract title from HTML."""
    with open(filepath, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8", errors="replace")
    m = re.search(r'<title[^>]*>([^<]+)</title>', text, re.IGNORECASE)
    if m:
        return re.sub(r'\s+', ' ', m.group(1)).strip()[:100]
    return "untitled"


# ---- MAIN ----

def sweep_election(election_date):
    """Sweep E+0 evening through E+3 for one election."""
    yyyy, mm, dd = election_date.split("-")

    # Generate sweep dates: E+0 through E+3
    import datetime
    base = datetime.date(int(yyyy), int(mm), int(dd))
    sweep_dates = [str(base + datetime.timedelta(days=i)) for i in range(4)]

    print(f"\n=== Election {election_date} ===", flush=True)
    print(f"  Sweep dates: {sweep_dates}", flush=True)

    all_results = []

    for article_date in sweep_dates:
        print(f"  CDX query for {article_date}...", flush=True)
        articles = cdx_query(article_date)
        print(f"    Found {len(articles)} URLs", flush=True)

        if not articles:
            continue

        # Filter and sort by priority
        prioritized = []
        for ts, url in articles:
            ok, pri = is_election_article(url)
            if ok:
                prioritized.append((pri, ts, url))

        prioritized.sort(key=lambda x: -x[0])
        print(f"    Election-relevant: {len(prioritized)}", flush=True)

        for pri, ts, url in prioritized:
            print(f"    Fetching [pri={pri}]: {url[:80]}", flush=True)
            saved = save_article(ts, url, election_date.replace("-", ""))
            if not saved:
                print(f"      -> save failed", flush=True)
                continue

            findings, is_sf = scan_article_text(saved, election_date)
            title = get_article_title(saved)
            wayback_url = f"http://web.archive.org/web/{ts}/{url}"

            if findings:
                print(f"      -> FINDINGS ({len(findings)}) in: {title[:60]}", flush=True)
                for f in findings[:3]:
                    print(f"         >> {f[:120]}", flush=True)
                all_results.append({
                    "election_date": election_date,
                    "article_date": article_date,
                    "title": title,
                    "wayback_url": wayback_url,
                    "filepath": saved,
                    "findings": findings,
                    "is_sf": is_sf,
                })
            else:
                print(f"      -> no findings: {title[:60]}", flush=True)

    return all_results


def main():
    os.makedirs(MIRROR_DIR, exist_ok=True)

    all_findings = []

    for election_date in TARGET_ELECTIONS:
        results = sweep_election(election_date)
        all_findings.extend(results)

    print("\n\n=== SUMMARY ===", flush=True)
    print(f"Total elections swept: {len(TARGET_ELECTIONS)}", flush=True)
    print(f"Articles with findings: {len(all_findings)}", flush=True)

    # Print CSV
    print("\n\nelection_date,article_date,statement_type,numbers,exact_quote,article_title,wayback_url", flush=True)

    for r in all_findings:
        for finding in r["findings"]:
            # Classify
            f_lower = finding.lower()
            if any(w in f_lower for w in ["remain", "uncounted", "outstanding"]):
                stype = "remaining"
            elif any(w in f_lower for w in ["certif"]):
                stype = "certification"
            elif any(w in f_lower for w in ["precinct", "all precinct", "election night"]):
                stype = "night_count"
            else:
                stype = "other"

            # Extract numbers
            nums = re.findall(r'[\d,]+', finding)
            nums_str = "|".join(nums[:5])

            # Escape for CSV
            quote = finding.replace('"', '""')[:200]
            title = r["title"].replace('"', '""')

            print(f'"{r["election_date"]}","{r["article_date"]}","{stype}","{nums_str}","{quote}","{title}","{r["wayback_url"]}"', flush=True)

    # Print "none" rows for elections with no findings
    found_elections = {r["election_date"] for r in all_findings}
    for ed in TARGET_ELECTIONS:
        if ed not in found_elections:
            print(f'"{ed}","","none","","no relevant articles found","","none"', flush=True)

    # Count saved files
    files_now = len(os.listdir(MIRROR_DIR))
    print(f"\nTotal files in mirror: {files_now}", flush=True)


if __name__ == "__main__":
    main()
