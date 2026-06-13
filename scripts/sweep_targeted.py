#!/usr/bin/env python3
"""
Targeted sweep for Chronicle/SFGate election counting articles 2000-2007.
Strategy: CDX query → filter to election-night/counting articles only → fetch & scan.
Focus: articles about ballot counting, absentee tallies, precinct reporting.
"""

import os
from pathlib import Path
import re
import sys
import time
import random
import datetime
import urllib.request
import urllib.error

MIRROR_DIR = os.environ.get(
    "SF_MIRROR_DIR",
    str(Path(__file__).resolve().parent.parent / "mirror" / "chronicle-sfgate"),
)

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

# Keywords in URL that indicate election counting articles
URL_ELECTION_KEYWORDS = [
    "ballot", "elect", "vote", "absentee", "precinct", "certif", "runoff",
    "tally", "count", "result", "winner", "race", "MN", "measure", "prop",
    "supervisor", "mayor", "recall"
]


def sleep_normal():
    time.sleep(random.uniform(2.2, 3.0))


def sleep_long(msg="rate limit"):
    print(f"  [{msg}] sleeping 120s...", flush=True)
    time.sleep(120)


def fetch_url(url, retries=2):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; research)",
        "Accept": "text/html,*/*",
    }
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429:
                sleep_long("429 rate limit")
                continue
            elif e.code in (404, 403):
                return None
            else:
                if attempt < retries:
                    time.sleep(3)
                    continue
                return None
        except Exception as e:
            if attempt < retries:
                time.sleep(5)
                continue
            print(f"  Failed: {e}", flush=True)
            return None
    return None


def cdx_query(date_str, limit=500):
    """Query CDX for articles on a given date. Returns list of (ts, url)."""
    yyyy, mm, dd = date_str.split("-")
    results = []

    patterns = [
        f"sfgate.com/cgi-bin/article.cgi%3Ffile%3D/chronicle/archive/{yyyy}/{mm}/{dd}/",
        f"sfgate.com/cgi-bin/article.cgi%3Ff%3D/c/a/{yyyy}/{mm}/{dd}/",
        f"sfgate.com/cgi-bin/article.cgi%3Ffile%3D/c/a/{yyyy}/{mm}/{dd}/",
    ]

    for pattern in patterns:
        cdx_url = (
            f"http://web.archive.org/cdx/search/cdx?"
            f"url={pattern}&matchType=prefix&output=text&collapse=urlkey&limit={limit}"
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

    # Deduplicate by urlkey (lowercased)
    seen = set()
    unique = []
    for ts, url in results:
        key = url.lower().split("&")[0]  # ignore query params for dedup
        if key not in seen:
            seen.add(key)
            unique.append((ts, url))

    return unique


def score_url(url):
    """Return priority score for a URL. Higher = more likely to have counting data."""
    url_lower = url.lower()

    # Skip printable versions
    if "type=printable" in url_lower or "type=p&" in url_lower:
        return -1

    score = 0

    # Highest: explicit election type
    if "type=election" in url_lower:
        score += 10

    # High: election keywords in filename
    fn_match = re.search(r'/([^/?]+\.DTL)', url, re.IGNORECASE)
    fn = fn_match.group(1).lower() if fn_match else ""

    counting_words = ["absentee", "precinct", "certif", "tally", "count", "remain", "ballot"]
    result_words = ["result", "elect", "vote", "winner", "race", "runoff", "measure", "prop",
                    "supervisor", "mayor", "recall", "recount"]

    for w in counting_words:
        if w in fn or w in url_lower:
            score += 5
            break

    for w in result_words:
        if w in fn or w in url_lower:
            score += 3
            break

    # MN codes: front page news articles
    if re.search(r'MN\d+', url, re.IGNORECASE):
        score += 2

    # Any DTL file is worth something
    if ".dtl" in url_lower:
        score += 1

    return score


def save_article(ts, url, election_date_compact):
    """Fetch and save. Returns (filepath, is_new) or (None, False)."""
    wayback_url = f"http://web.archive.org/web/{ts}id_/{url}"
    data = fetch_url(wayback_url)
    sleep_normal()
    if not data:
        return None, False

    # Build filename from DTL file in URL
    fn_match = re.search(r'/([^/?]+\.DTL)', url, re.IGNORECASE)
    if fn_match:
        fn = fn_match.group(1)
    else:
        fn = re.sub(r'[^\w.]', '_', url[-50:])

    outname = f"{election_date_compact}_{fn}.html"
    outpath = os.path.join(MIRROR_DIR, outname)
    is_new = not os.path.exists(outpath)

    if is_new:
        with open(outpath, "wb") as f:
            f.write(data)

    return outpath, is_new


def scan_for_sf_counting(filepath):
    """Scan article for SF election counting data. Returns list of (type, quote) pairs."""
    with open(filepath, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8", errors="replace")

    # Strip HTML
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = re.sub(r'&nbsp;', ' ', clean)
    clean = re.sub(r'&amp;', '&', clean)
    clean = re.sub(r'&#\d+;', '', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()

    results = []

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', clean)

    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 20 or len(sent) > 600:
            continue

        sent_lower = sent.lower()

        # Must have a number (we want quantitative statements)
        if not re.search(r'\d', sent):
            continue

        # Must be SF-related
        sf_related = bool(re.search(
            r'san francisco|s\.f\.|city (and county|hall|voters)|sfgate|'
            r'registrar of voters|department of elections|sf voters|'
            r'\b645\b|\b646\b|\b647\b|\b648\b|\b649\b|\b650\b',
            sent, re.IGNORECASE
        ))

        if not sf_related:
            continue

        # Categorize
        if re.search(r'absentee|provisional|mail.in|vote.by.mail', sent_lower):
            if re.search(r'\d[\d,]*', sent):
                results.append(("remaining_or_absentee", sent))

        if re.search(r'precinct.*report|all \d+ precinct|with all.*precinct|precincts? reporting', sent_lower):
            results.append(("night_count", sent))

        if re.search(r'ballots? (remain|left|uncounted|outstanding)', sent_lower):
            results.append(("remaining", sent))

        if re.search(r'(certif|official count|final count|official result)', sent_lower):
            results.append(("certification", sent))

        if re.search(r'ballots? cast|ballots? counted|total.*ballot|turnout.*percent|percent.*turnout', sent_lower):
            results.append(("night_count", sent))

        if re.search(r'as of \d+(?::\d+)?\s*[ap]\.?m', sent_lower):
            results.append(("time_stamped", sent))

    return results


def get_title(filepath):
    with open(filepath, "rb") as f:
        raw = f.read(4096)
    text = raw.decode("utf-8", errors="replace")
    m = re.search(r'<title[^>]*>([^<]+)</title>', text, re.IGNORECASE)
    if m:
        return re.sub(r'\s+', ' ', m.group(1)).strip()[:120]
    return "untitled"


def sweep_election(election_date):
    """Sweep E+0..E+3 for one election. Returns list of result dicts."""
    yyyy, mm, dd = election_date.split("-")
    base = datetime.date(int(yyyy), int(mm), int(dd))
    sweep_dates = [str(base + datetime.timedelta(days=i)) for i in range(4)]

    print(f"\n=== Election {election_date} ===", flush=True)

    all_results = []
    articles_checked = 0

    for article_date in sweep_dates:
        print(f"  CDX {article_date}...", flush=True)
        articles = cdx_query(article_date)
        print(f"    {len(articles)} URLs found", flush=True)

        # Score and filter
        scored = []
        for ts, url in articles:
            s = score_url(url)
            if s >= 0:
                scored.append((s, ts, url))

        scored.sort(key=lambda x: -x[0])

        # Only fetch articles with score >= 1 (skip zero-score DTL-less URLs)
        # But for E+1 and E+2, be more selective: only score >= 2
        min_score = 1 if article_date == str(base) else 2

        to_fetch = [(s, ts, url) for s, ts, url in scored if s >= min_score]
        print(f"    Fetching {len(to_fetch)} (score>={min_score})", flush=True)

        for s, ts, url in to_fetch:
            election_compact = election_date.replace("-", "")
            saved, is_new = save_article(ts, url, election_compact)
            articles_checked += 1

            if not saved:
                continue

            findings = scan_for_sf_counting(saved)
            title = get_title(saved)
            wayback_url = f"http://web.archive.org/web/{ts}/{url}"

            if findings:
                print(f"    FOUND [{article_date}] {title[:65]}", flush=True)
                for ftype, ftext in findings[:3]:
                    print(f"      [{ftype}] {ftext[:140]}", flush=True)
                all_results.append({
                    "election_date": election_date,
                    "article_date": article_date,
                    "title": title,
                    "wayback_url": wayback_url,
                    "filepath": saved,
                    "findings": findings,
                })

    print(f"  Articles checked: {articles_checked}, with findings: {len(all_results)}", flush=True)
    return all_results, articles_checked


def main():
    os.makedirs(MIRROR_DIR, exist_ok=True)

    all_findings = []
    articles_by_election = {}

    for election_date in TARGET_ELECTIONS:
        results, checked = sweep_election(election_date)
        all_findings.extend(results)
        articles_by_election[election_date] = checked

    # Output CSV
    print("\n\n" + "="*70, flush=True)
    print("FINAL CSV", flush=True)
    print("="*70, flush=True)
    print("election_date,article_date,statement_type,numbers,exact_quote,article_title,wayback_url", flush=True)

    found_elections = set()

    for r in all_findings:
        found_elections.add(r["election_date"])
        for ftype, ftext in r["findings"]:
            nums = "|".join(re.findall(r'[\d,]+', ftext)[:6])
            quote = ftext.replace('"', '""')[:250]
            title = r["title"].replace('"', '""')
            url = r["wayback_url"]
            print(f'"{r["election_date"]}","{r["article_date"]}","{ftype}","{nums}","{quote}","{title}","{url}"', flush=True)

    for ed in TARGET_ELECTIONS:
        if ed not in found_elections:
            checked = articles_by_election.get(ed, 0)
            print(f'"{ed}","","none","","no relevant SF counting data found ({checked} articles checked)","","none"', flush=True)

    files_now = len(os.listdir(MIRROR_DIR))
    print(f"\nFiles in mirror: {files_now}", flush=True)


if __name__ == "__main__":
    main()
