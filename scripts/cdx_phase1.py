#!/usr/bin/env python3
"""Phase 1: CDX-only scan to collect all article URLs for target election dates."""

import os
import re
import json
import time
import random
import datetime
import urllib.request
import urllib.error

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

CDX_CACHE = "/tmp/cdx_cache.json"


def sleep_normal():
    time.sleep(random.uniform(2.0, 2.5))


def sleep_long():
    print("  [rate limit] sleeping 120s...", flush=True)
    time.sleep(120)


def fetch_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (research/archive)"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.read()
    except urllib.error.HTTPError as e:
        if e.code == 429:
            sleep_long()
            # retry once
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    return resp.read()
            except:
                return None
        return None
    except Exception as e:
        print(f"  Error: {e}", flush=True)
        return None


def cdx_query_date(date_str):
    yyyy, mm, dd = date_str.split("-")
    results = []
    patterns = [
        f"sfgate.com/cgi-bin/article.cgi%3Ffile%3D/chronicle/archive/{yyyy}/{mm}/{dd}/",
        f"sfgate.com/cgi-bin/article.cgi%3Ff%3D/c/a/{yyyy}/{mm}/{dd}/",
        f"sfgate.com/cgi-bin/article.cgi%3Ffile%3D/c/a/{yyyy}/{mm}/{dd}/",
    ]
    seen = set()
    for pattern in patterns:
        cdx_url = (
            f"http://web.archive.org/cdx/search/cdx?"
            f"url={pattern}&matchType=prefix&output=text&collapse=urlkey&limit=500"
        )
        data = fetch_url(cdx_url)
        sleep_normal()
        if not data:
            continue
        for line in data.decode("utf-8", errors="replace").strip().split("\n"):
            parts = line.split()
            if len(parts) >= 3:
                ts, orig_url = parts[1], parts[2]
                key = orig_url.lower().split("&type=")[0].split("&hw=")[0].split("&nl=")[0]
                if key not in seen:
                    seen.add(key)
                    results.append({"ts": ts, "url": orig_url})
    return results


def main():
    # Load cache if exists
    cache = {}
    if os.path.exists(CDX_CACHE):
        with open(CDX_CACHE) as f:
            cache = json.load(f)

    # Generate all dates to query
    all_dates = set()
    for ed in TARGET_ELECTIONS:
        yyyy, mm, dd = ed.split("-")
        base = datetime.date(int(yyyy), int(mm), int(dd))
        for i in range(4):
            all_dates.add(str(base + datetime.timedelta(days=i)))

    print(f"Querying {len(all_dates)} dates...", flush=True)

    for date_str in sorted(all_dates):
        if date_str in cache:
            print(f"  {date_str}: cached ({len(cache[date_str])} URLs)", flush=True)
            continue
        print(f"  {date_str}: querying...", flush=True)
        results = cdx_query_date(date_str)
        cache[date_str] = results
        print(f"    -> {len(results)} URLs", flush=True)

        # Save after each date
        with open(CDX_CACHE, "w") as f:
            json.dump(cache, f)

    print("\nAll CDX queries done.", flush=True)
    total = sum(len(v) for v in cache.values())
    print(f"Total URLs across all dates: {total}", flush=True)

    # Print breakdown by date
    for date_str in sorted(cache.keys()):
        urls = cache[date_str]
        print(f"  {date_str}: {len(urls)} URLs", flush=True)


if __name__ == "__main__":
    main()
