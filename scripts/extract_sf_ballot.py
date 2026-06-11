#!/usr/bin/env python3
"""
Extract SF-specific ballot count statements from fetched Chronicle articles.
Produces deliverable CSV.
"""

import os
import re
from html.parser import HTMLParser
from datetime import date, timedelta

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

# Map article date -> election date
def get_election(art_date_str):
    art_date = date(int(art_date_str[:4]), int(art_date_str[4:6]), int(art_date_str[6:8]))
    for edate in ELECTIONS:
        for offset in [1, 2, 3]:
            if edate + timedelta(days=offset) == art_date:
                return edate, 'night_count'
        for offset in range(28, 39):
            if edate + timedelta(days=offset) == art_date:
                return edate, 'cert_window'
    return None, None


class TE(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.in_s = False
        self.title_parts = []
        self.in_title = False
    def handle_starttag(self, t, a):
        if t.lower() in ('script', 'style'): self.in_s = True
        elif t.lower() == 'title': self.in_title = True
    def handle_endtag(self, t):
        if t.lower() in ('script', 'style'): self.in_s = False
        elif t.lower() == 'title': self.in_title = False
    def handle_data(self, d):
        if not self.in_s:
            self.parts.append(d)
            if self.in_title:
                self.title_parts.append(d)
    def get_text(self): return ' '.join(self.parts)
    def get_title(self): return ' '.join(self.title_parts).strip()


# Patterns that indicate SF city/county ballot counting
SF_CONTEXT_PAT = re.compile(
    r"San Francisco(?:'s)?.{0,100}(?:ballots?|absentee|provisional|precinct|election|count|vote|turnout|registrar)"
    r"|(?:Department of Elections|registrar of voters|election official).{0,150}(?:\d[\d,]+|count|ballot)"
    r"|(?:Nishioka|elections director|elections chief|elections department).{0,150}(?:\d[\d,]+|ballot|count)"
    r"|\d[\d,]+ (?:absentee|provisional).{0,100}(?:remain|uncounted|counted|count)"
    r"|\d[\d,]+ ballots? (?:remain|uncounted|cast|counted)"
    r"|all \d+ precincts? report"
    r"|\d+ of \d+ precincts? report",
    re.IGNORECASE | re.DOTALL
)

# Patterns that are clearly NOT SF (other counties)
OTHER_COUNTY = re.compile(
    r"(?:Alameda|Contra Costa|Marin|San Mateo|Santa Clara|Sonoma|Solano|Napa|Sacramento|Los Angeles|Orange County)\s+(?:County|county)",
    re.IGNORECASE
)

def classify(sent):
    if re.search(r'\d+ of \d+ precincts|all \d+ precincts|percent.*report|votes counted|tally', sent, re.I):
        return 'night_count'
    if re.search(r'remain|uncounted|absentee|provisional|still.*count|mail', sent, re.I):
        return 'remaining'
    if re.search(r'certif|canvas|canvass|official.*result|final count|final tally', sent, re.I):
        return 'certification'
    return 'other'


def csv_esc(s):
    s = str(s or '').replace('"', '""').replace('\n', ' ').replace('\r', ' ').strip()
    return f'"{s}"'


def process_file(fpath):
    fname = os.path.basename(fpath)
    date_m = re.match(r'^(\d{8})_', fname)
    if not date_m:
        return []
    art_date_str = date_m.group(1)
    edate, window = get_election(art_date_str)
    if not edate:
        return []

    with open(fpath, encoding='utf-8', errors='replace') as f:
        raw = f.read()

    wb_m = re.search(r'<!-- WAYBACK_URL: (.+?) -->', raw)
    wb_url = wb_m.group(1) if wb_m else ''

    p = TE()
    p.feed(raw)
    text = p.get_text()
    title = p.get_title()
    if not title:
        # Fallback: find title in text
        tm = re.search(r'\n([A-Z][^\n]{15,120})\n', text)
        title = tm.group(1).strip() if tm else ''

    # Split into paragraphs/sentences
    sentences = re.split(r'(?<=[.!?])\s+|\n{2,}', text)

    results = []
    for sent in sentences:
        sent = re.sub(r'\s+', ' ', sent).strip()
        if len(sent) < 30 or len(sent) > 700:
            continue
        if not SF_CONTEXT_PAT.search(sent):
            continue
        # If mentions another county explicitly without SF, skip
        if OTHER_COUNTY.search(sent) and not re.search(r'San Francisco', sent, re.I):
            continue

        nums = re.findall(r'\d[\d,]*(?:\.\d+)?(?:\s*(?:percent|%))?', sent)
        if not nums:
            continue

        stype = classify(sent)
        art_date_fmt = f"{art_date_str[:4]}-{art_date_str[4:6]}-{art_date_str[6:8]}"
        results.append({
            'election_date': edate.isoformat(),
            'article_date': art_date_fmt,
            'statement_type': stype,
            'numbers': '; '.join(nums[:8]),
            'exact_quote': sent[:350],
            'article_title': title[:120],
            'wayback_url': wb_url,
        })

    return results


def main():
    print("election_date,article_date,statement_type,numbers,exact_quote,article_title,wayback_url")

    all_results = []
    election_file_count = {e: 0 for e in ELECTIONS}

    files = sorted(os.listdir(MIRROR_DIR))
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(MIRROR_DIR, fname)
        date_m = re.match(r'^(\d{8})_', fname)
        if date_m:
            edate, _ = get_election(date_m.group(1))
            if edate:
                election_file_count[edate] = election_file_count.get(edate, 0) + 1

        results = process_file(fpath)
        for r in results:
            all_results.append(r)

    # Output results, grouping by election
    found_elections = set()
    for r in all_results:
        found_elections.add(r['election_date'])
        row = ','.join([
            csv_esc(r['election_date']),
            csv_esc(r['article_date']),
            csv_esc(r['statement_type']),
            csv_esc(r['numbers']),
            csv_esc(r['exact_quote']),
            csv_esc(r['article_title']),
            csv_esc(r['wayback_url']),
        ])
        print(row)

    # "nothing found" lines for elections with no results
    for edate in ELECTIONS:
        if edate.isoformat() not in found_elections:
            n = election_file_count.get(edate, 0)
            print(','.join([
                csv_esc(edate.isoformat()),
                csv_esc(''),
                csv_esc('none'),
                csv_esc(''),
                csv_esc(f'swept E+1..E+3 ({n} articles), nothing'),
                csv_esc(''),
                csv_esc(''),
            ]))

    import sys
    print(f"\n# Total files saved: {len(files)}", file=sys.stderr)
    print(f"# Findings: {len(all_results)}", file=sys.stderr)


if __name__ == '__main__':
    main()
