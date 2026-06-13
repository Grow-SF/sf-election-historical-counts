#!/usr/bin/env python3
"""
Phase 2: Fetch targeted articles from CDX cache.
Focus on:
1. &type=election URLs (highest priority)
2. Descriptive filenames (props.DTL, supes.DTL, ballot.DTL, etc.)
3. MN*.DTL files (news articles) from E+1 and E+2 dates only
Avoid: BU (business), FD (food), HO (home), SP (sports), DD (features), ED (entertainment)
"""

import os
from pathlib import Path
import re
import json
import time
import random
import datetime
import urllib.request
import urllib.error

MIRROR_DIR = os.environ.get(
    "SF_MIRROR_DIR",
    str(Path(__file__).resolve().parent.parent / "mirror" / "chronicle-sfgate"),
)
CDX_CACHE = "/tmp/cdx_cache.json"

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

# Descriptive DTL filenames that indicate election content
ELECTION_DESCRIPTIVE = re.compile(
    r'/(ballot|bond|prop|vote|elect|count|tally|certif|precinct|absentee|'
    r'measure|supervisor|supes|supe|mayor|recall|runoff|planning|senate|'
    r'pres|congress|president|race|winner|sfcount|sfvote|sf[a-z]+|'
    r'district|result|night|sb|ab|props|sjbart|congo|planning)\.DTL',
    re.IGNORECASE
)

# Section prefixes to SKIP (not election news)
SKIP_SECTIONS = re.compile(r'/(?:BU|FD|HO|SP|DD|ED|HW|TR|CL)\d+\.DTL', re.IGNORECASE)


def sleep_normal():
    time.sleep(random.uniform(2.0, 2.8))


def sleep_long():
    print("  [rate limit] sleeping 120s...", flush=True)
    time.sleep(120)


def fetch_url(url, retries=2):
    headers = {"User-Agent": "Mozilla/5.0 (research/archive)"}
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
                if attempt < retries:
                    time.sleep(3)
                    continue
                return None
        except Exception as e:
            if attempt < retries:
                time.sleep(4)
                continue
            return None
    return None


def score_url(url, article_date, election_date):
    """Score URL for election-counting relevance. -1 = skip.
    Strategy: only fetch score >= MIN_SCORE (set to 5 for MN* on E+1/E+2, 15 for descriptive/type=election)
    """
    url_lower = url.lower()

    # Skip printable versions
    if "type=printable" in url_lower or "type=p&" in url_lower:
        return -1

    # Skip clearly non-news sections
    fn_match = re.search(r'/([A-Z]{2})\d', url, re.IGNORECASE)
    if fn_match:
        section = fn_match.group(1).upper()
        if section in ("BU", "FD", "HO", "SP", "DD", "ED", "HW", "TR", "CL", "EN", "NW"):
            return -1

    score = 0

    # type=election is highest priority
    if "type=election" in url_lower:
        score += 20

    # Descriptive election filenames
    if ELECTION_DESCRIPTIVE.search(url):
        score += 15

    # MN codes (front-page news) - only valuable on E+1/E+2
    if re.search(r'/MN\d+\.DTL', url, re.IGNORECASE):
        yyyy, mm, dd = election_date.split("-")
        base = datetime.date(int(yyyy), int(mm), int(dd))
        e_plus_1 = str(base + datetime.timedelta(days=1))
        e_plus_2 = str(base + datetime.timedelta(days=2))
        if article_date in (e_plus_1, e_plus_2):
            score += 5  # MN* on day after election are high value

    return score


def save_article(ts, url, election_date_compact, article_date):
    """Fetch and save. Returns filepath or None."""
    wayback_url = f"http://web.archive.org/web/{ts}id_/{url}"
    data = fetch_url(wayback_url)
    sleep_normal()
    if not data or len(data) < 500:
        return None

    fn_match = re.search(r'/([^/?]+\.DTL)', url, re.IGNORECASE)
    if fn_match:
        fn = fn_match.group(1)
    else:
        fn = re.sub(r'[^\w.]', '_', url[-40:])

    # Use article date in filename, not election date
    outname = f"{election_date_compact}_{article_date.replace('-', '')}_{fn}.html"
    outpath = os.path.join(MIRROR_DIR, outname)

    if not os.path.exists(outpath):
        with open(outpath, "wb") as f:
            f.write(data)

    return outpath


def scan_sf_counting(filepath):
    """Find SF election counting sentences. Returns list of (type, sentence)."""
    with open(filepath, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8", errors="replace")
    clean = re.sub(r'<[^>]+>', ' ', text)
    clean = re.sub(r'&nbsp;', ' ', clean)
    clean = re.sub(r'&amp;', '&', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()

    results = []
    sentences = re.split(r'(?<=[.!?])\s+', clean)

    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 25 or len(sent) > 700:
            continue
        if not re.search(r'\d', sent):
            continue

        sent_lower = sent.lower()

        # SF geography filter
        sf = bool(re.search(
            r'san francisco|s\.f\.|city (and county|hall|voters)|'
            r'registrar of voters|department of elections|'
            r'\b6[34567]\d\b.*precinct|\bprecinct.*\b6[34567]\d\b',
            sent, re.IGNORECASE
        ))

        # For HOW SF VOTED tables, just check for numbers
        is_results_table = bool(re.search(r'of \d+ precinct|precinct.*reporting|reporting.*precinct', sent_lower))

        if not sf and not is_results_table:
            continue

        if re.search(r'absentee|provisional|mail.in|vote.by.mail', sent_lower):
            results.append(("absentee_count", sent))
        if re.search(r'precinct.*report|all \d+ precinct|with all.*precinct|\d+ of \d+ precinct', sent_lower):
            results.append(("night_count", sent))
        if re.search(r'ballots? (remain|left|uncounted|outstanding)', sent_lower):
            results.append(("remaining", sent))
        if re.search(r'certif|official (count|result|tally|canvass)', sent_lower):
            results.append(("certification", sent))
        if re.search(r'ballots? cast|total.*ballots?|voter turnout.*\d|registrar.*count', sent_lower):
            results.append(("cast_total", sent))
        if re.search(r'as of \d+(?::\d+)?\s*[ap]\.?m', sent_lower):
            results.append(("timestamped", sent))

    return results


def get_title(filepath):
    with open(filepath, "rb") as f:
        raw = f.read(5000)
    text = raw.decode("utf-8", errors="replace")
    m = re.search(r'<title[^>]*>([^<]+)</title>', text, re.IGNORECASE)
    return re.sub(r'\s+', ' ', m.group(1)).strip()[:120] if m else "untitled"


def main():
    with open(CDX_CACHE) as f:
        cache = json.load(f)

    os.makedirs(MIRROR_DIR, exist_ok=True)

    all_findings = []
    articles_by_election = {}

    for election_date in TARGET_ELECTIONS:
        yyyy, mm, dd = election_date.split("-")
        base = datetime.date(int(yyyy), int(mm), int(dd))
        sweep_dates = [str(base + datetime.timedelta(days=i)) for i in range(4)]

        print(f"\n=== Election {election_date} ===", flush=True)

        election_findings = []
        total_fetched = 0

        for article_date in sweep_dates:
            if article_date not in cache:
                print(f"  {article_date}: not in CDX cache, skipping", flush=True)
                continue

            urls = cache[article_date]
            print(f"  {article_date}: {len(urls)} URLs in cache", flush=True)

            # Score and filter - use threshold 5 (MN* on E+1/E+2 + descriptive + type=election)
            scored = []
            for item in urls:
                ts, url = item["ts"], item["url"]
                s = score_url(url, article_date, election_date)
                if s >= 5:
                    scored.append((s, ts, url))

            scored.sort(key=lambda x: -x[0])
            print(f"    -> {len(scored)} to fetch (score>=5)", flush=True)

            for s, ts, url in scored:
                election_compact = election_date.replace("-", "")
                saved = save_article(ts, url, election_compact, article_date)
                total_fetched += 1

                if not saved:
                    continue

                findings = scan_sf_counting(saved)
                title = get_title(saved)
                wayback_url = f"http://web.archive.org/web/{ts}/{url}"

                if findings:
                    print(f"    FOUND [{article_date} s={s}]: {title[:70]}", flush=True)
                    for ftype, ftext in findings[:4]:
                        print(f"      [{ftype}] {ftext[:160]}", flush=True)
                    election_findings.append({
                        "election_date": election_date,
                        "article_date": article_date,
                        "title": title,
                        "wayback_url": wayback_url,
                        "findings": findings,
                    })

        articles_by_election[election_date] = total_fetched
        all_findings.extend(election_findings)
        print(f"  Fetched {total_fetched}, findings in {len(election_findings)} articles", flush=True)

    # CSV output
    print("\n\n" + "="*70)
    print("election_date,article_date,statement_type,numbers,exact_quote,article_title,wayback_url")

    found_elections = set()
    for r in all_findings:
        found_elections.add(r["election_date"])
        seen_quotes = set()
        for ftype, ftext in r["findings"]:
            if ftext in seen_quotes:
                continue
            seen_quotes.add(ftext)
            nums = "|".join(re.findall(r'[\d,]+', ftext)[:6])
            quote = ftext.replace('"', '""')[:250]
            title = r["title"].replace('"', '""')
            url = r["wayback_url"]
            print(f'"{r["election_date"]}","{r["article_date"]}","{ftype}","{nums}","{quote}","{title}","{url}"')

    for ed in TARGET_ELECTIONS:
        if ed not in found_elections:
            checked = articles_by_election.get(ed, 0)
            print(f'"{ed}","","none","","no SF counting data found ({checked} fetched)","","none"')

    print(f"\nFiles in mirror: {len(os.listdir(MIRROR_DIR))}")


if __name__ == "__main__":
    main()
