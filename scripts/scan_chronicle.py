#!/usr/bin/env python3
"""
Scan fetched Chronicle articles for SF ballot-count statements.
Outputs CSV to stdout.
"""

import os
import re
import sys
from datetime import date, timedelta
from html.parser import HTMLParser

MIRROR_DIR = "/Users/sbuss/workspace/sf-election-count/mirror/chronicle-sfgate"

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

# Keywords to search for
KEYWORDS = re.compile(
    r'absentee[\s\-]?ballot|ballot.{0,10}remain|remain.{0,10}count|uncounted|'
    r'precinct.{0,10}report|report.{0,10}precinct|vote.{0,15}count|ballot.{0,10}cast|'
    r'turnout|registrar|certif|provisional|mail.?in ballot|'
    r'\d[\d,]+\s+ballot|\d[\d,]+\s+vote',
    re.IGNORECASE
)

SF_KEYWORDS = re.compile(
    r'San Francisco|S\.F\.|the city|City and County',
    re.IGNORECASE
)

STATEMENT_TYPES = {
    'night_count': re.compile(
        r'precinct.{0,20}report|report.{0,20}precinct|percent.{0,20}report|'
        r'vote.{0,20}count|ballot.{0,20}count|counted|tally|result',
        re.IGNORECASE
    ),
    'remaining': re.compile(
        r'remain|uncounted|still.{0,10}count|absentee|provisional|mail',
        re.IGNORECASE
    ),
    'certification': re.compile(
        r'certif|canvas|canvass|official|final count|final tally',
        re.IGNORECASE
    ),
}


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.in_script = False
        self.in_style = False
        self.title = ""
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'script':
            self.in_script = True
        elif tag.lower() == 'style':
            self.in_style = True
        elif tag.lower() == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        if tag.lower() == 'script':
            self.in_script = False
        elif tag.lower() == 'style':
            self.in_style = False
        elif tag.lower() == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_script or self.in_style:
            return
        if self.in_title and not self.title:
            self.title = data.strip()
        self.text_parts.append(data)

    def get_text(self):
        return ' '.join(self.text_parts)


def extract_text_and_title(html):
    parser = TextExtractor()
    try:
        parser.feed(html)
    except Exception:
        pass
    return parser.get_text(), parser.title


def classify_statement(sentence):
    for stype, pat in STATEMENT_TYPES.items():
        if pat.search(sentence):
            return stype
    return 'other'


def extract_numbers(sentence):
    nums = re.findall(r'\d[\d,]*(?:\.\d+)?(?:\s*(?:percent|%))?', sentence)
    return '; '.join(nums[:8]) if nums else ''


def csv_escape(s):
    if s is None:
        s = ''
    s = str(s).replace('"', '""').replace('\n', ' ').replace('\r', ' ')
    return f'"{s}"'


def get_election_for_file(fname):
    """Map filename prefix (YYYYMMDD) to election date."""
    m = re.match(r'^(\d{8})_', fname)
    if not m:
        return None, None
    art_ymd = m.group(1)
    art_date = date(int(art_ymd[:4]), int(art_ymd[4:6]), int(art_ymd[6:8]))

    for edate in ELECTIONS:
        # Night count window: E+1..E+3
        for offset in [1, 2, 3]:
            if edate + timedelta(days=offset) == art_date:
                return edate, art_date
        # Cert window: E+28..E+38
        for offset in range(28, 39):
            if edate + timedelta(days=offset) == art_date:
                return edate, art_date
    return None, art_date


def scan_file(fpath):
    fname = os.path.basename(fpath)
    edate, art_date = get_election_for_file(fname)

    # Extract wayback URL from header comment
    with open(fpath, encoding='utf-8', errors='replace') as f:
        raw = f.read()

    wb_url_m = re.search(r'<!-- WAYBACK_URL: (.+?) -->', raw)
    wb_url = wb_url_m.group(1) if wb_url_m else ''

    text, title = extract_text_and_title(raw)

    # Split into sentences (rough)
    sentences = re.split(r'(?<=[.!?])\s+', text)

    results = []
    for sent in sentences:
        sent = sent.strip()
        if len(sent) < 20 or len(sent) > 800:
            continue
        if not KEYWORDS.search(sent):
            continue
        # Prefer SF-specific sentences
        nums = extract_numbers(sent)
        if not nums:
            continue
        stype = classify_statement(sent)
        results.append({
            'election_date': edate.isoformat() if edate else '',
            'article_date': art_date.isoformat() if art_date else '',
            'statement_type': stype,
            'numbers': nums,
            'exact_quote': sent[:300],
            'article_title': title[:120],
            'wayback_url': wb_url,
        })

    return results


def main():
    if not os.path.isdir(MIRROR_DIR):
        print("Mirror dir not found", file=sys.stderr)
        sys.exit(1)

    files = sorted(os.listdir(MIRROR_DIR))
    print("election_date,article_date,statement_type,numbers,exact_quote,article_title,wayback_url")

    election_files = {e: [] for e in ELECTIONS}
    all_results = []

    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(MIRROR_DIR, fname)
        edate, art_date = get_election_for_file(fname)
        if edate:
            election_files[edate].append(fname)

        results = scan_file(fpath)
        for r in results:
            all_results.append(r)
            row = ','.join([
                csv_escape(r['election_date']),
                csv_escape(r['article_date']),
                csv_escape(r['statement_type']),
                csv_escape(r['numbers']),
                csv_escape(r['exact_quote']),
                csv_escape(r['article_title']),
                csv_escape(r['wayback_url']),
            ])
            print(row)

    # Print "nothing found" lines for elections with no results
    found_elections = set(r['election_date'] for r in all_results if r['election_date'])
    for edate in ELECTIONS:
        if edate.isoformat() not in found_elections:
            n_files = len(election_files.get(edate, []))
            print(','.join([
                csv_escape(edate.isoformat()),
                csv_escape(''),
                csv_escape('none'),
                csv_escape(''),
                csv_escape(f'swept E+1..E+3 ({n_files} articles), nothing'),
                csv_escape(''),
                csv_escape(''),
            ]))

    print(f"\n# Total files scanned: {len(files)}", file=sys.stderr)


if __name__ == "__main__":
    main()
