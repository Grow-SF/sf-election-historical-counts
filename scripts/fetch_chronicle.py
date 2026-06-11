#!/usr/bin/env python3
"""
Fetch SF Chronicle election-count articles from Wayback Machine.
Enumerates via CDX API and saves to mirror/chronicle-sfgate/.
"""

import os
import re
import sys
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import date, timedelta

MIRROR_DIR = "/Users/sbuss/workspace/sf-election-count/mirror/chronicle-sfgate"

# Target election dates
ELECTIONS = [
    date(1995, 11, 7),
    date(1995, 12, 12),
    date(1996, 3, 26),
    date(1996, 11, 5),
    date(1997, 11, 4),
    date(1997, 12, 9),
    date(1998, 6, 2),
    date(1998, 11, 3),
    date(1999, 11, 2),
    date(1999, 12, 14),
    date(2000, 3, 7),
    date(2000, 11, 7),
    date(2000, 12, 12),
    date(2001, 11, 6),
    date(2001, 12, 11),
    date(2002, 3, 5),
    date(2002, 11, 5),
    date(2002, 12, 10),
    date(2003, 10, 7),
    date(2003, 11, 4),
    date(2003, 12, 9),
    date(2005, 11, 8),
    date(2007, 11, 6),
]


def cdx_query(date_str, url_pattern):
    """Query Wayback CDX for all articles archived for a given date prefix."""
    encoded = urllib.parse.quote(url_pattern, safe='')
    cdx_url = (
        f"https://web.archive.org/cdx/search/cdx"
        f"?url={encoded}"
        f"&matchType=prefix&output=text&collapse=urlkey&limit=300"
    )
    for attempt in range(3):
        try:
            req = urllib.request.Request(cdx_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode('utf-8', errors='replace').strip()
        except Exception as e:
            print(f"  CDX error (attempt {attempt+1}) for {url_pattern}: {e}", file=sys.stderr)
            if attempt < 2:
                time.sleep(2 ** attempt * 2)
    return ""


def fetch_wayback(ts, orig_url):
    """Fetch article via Wayback id_ (raw) URL."""
    wb_url = f"https://web.archive.org/web/{ts}id_/{orig_url}"
    for attempt in range(3):
        try:
            req = urllib.request.Request(wb_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read().decode('utf-8', errors='replace'), wb_url
        except Exception as e:
            print(f"  Fetch error (attempt {attempt+1}) {wb_url}: {e}", file=sys.stderr)
            if attempt < 2:
                time.sleep(2 ** attempt * 2)
    return None, wb_url


def article_id_from_url(orig_url):
    """Extract a short ID from the original URL for the filename."""
    # Extract the DTL filename
    m = re.search(r'/([A-Z]{2}\d+)\.DTL', orig_url)
    if m:
        return m.group(1)
    m = re.search(r'/(\w+)\.DTL', orig_url)
    if m:
        return m.group(1)
    return re.sub(r'[^a-zA-Z0-9]', '_', orig_url[-30:])


def enumerate_and_fetch(edate, day_offset):
    """Enumerate CDX and fetch articles for election date + offset days."""
    target_date = edate + timedelta(days=day_offset)
    ymd = target_date.strftime("%Y/%m/%d")
    ymd_flat = target_date.strftime("%Y%m%d")
    year = target_date.year

    fetched = []

    # Build URL patterns based on year
    patterns = []
    if year <= 2004:
        patterns.append(f"sfgate.com/cgi-bin/article.cgi?file=/chronicle/archive/{ymd}/")
    if year >= 2004:
        patterns.append(f"sfgate.com/cgi-bin/article.cgi?f=/c/a/{ymd}/")
        patterns.append(f"sfgate.com/cgi-bin/article.cgi?file=/c/a/{ymd}/")

    seen_ts_url = set()

    for pattern in patterns:
        cdx_text = cdx_query(ymd_flat, pattern)
        if not cdx_text:
            continue
        lines = [l for l in cdx_text.splitlines() if l.strip()]
        print(f"  {target_date} pattern={pattern.split('?')[1][:20]}... => {len(lines)} CDX results")

        for line in lines:
            parts = line.split()
            if len(parts) < 3:
                continue
            ts = parts[1]
            orig_url = parts[2]

            # Skip printable duplicates
            if 'type=printable' in orig_url or 'type=print' in orig_url:
                continue

            key = (ts, orig_url)
            if key in seen_ts_url:
                continue
            seen_ts_url.add(key)

            art_id = article_id_from_url(orig_url)
            # Only save MN (main news) and select others; skip ads/nav
            # Actually save all and filter in scan step
            out_fname = f"{ymd_flat}_{target_date.strftime('%Y_%m_%d')}_{art_id}.DTL.html"
            out_path = os.path.join(MIRROR_DIR, out_fname)

            if os.path.exists(out_path):
                print(f"    skip (exists): {out_fname}")
                fetched.append(out_path)
                continue

            time.sleep(0.5)  # be polite
            html, wb_url = fetch_wayback(ts, orig_url)
            if html:
                with open(out_path, 'w', encoding='utf-8') as f:
                    f.write(f"<!-- WAYBACK_URL: {wb_url} -->\n")
                    f.write(f"<!-- ORIG_URL: {orig_url} -->\n")
                    f.write(html)
                print(f"    saved: {out_fname} ({len(html)} chars)")
                fetched.append(out_path)
            time.sleep(0.3)

    return fetched


def main():
    os.makedirs(MIRROR_DIR, exist_ok=True)

    if len(sys.argv) > 1:
        # Allow specifying election date subset (year, YYYY-MM, or full ISO date)
        subset = set(sys.argv[1:])
        elections = [e for e in ELECTIONS if
                     str(e.year) in subset or
                     e.isoformat()[:7] in subset or
                     e.isoformat() in subset]
    else:
        elections = ELECTIONS

    total_files = 0
    for edate in elections:
        print(f"\n=== Election {edate} ===")
        # Night-count: E+1, E+2, E+3
        for offset in [1, 2, 3]:
            files = enumerate_and_fetch(edate, offset)
            total_files += len(files)
        # Certification: E+28..E+38 (lighter priority)
        # Skip for now to avoid rate limiting; run separately if needed

    print(f"\nTotal files in mirror: {total_files}")


if __name__ == "__main__":
    main()
