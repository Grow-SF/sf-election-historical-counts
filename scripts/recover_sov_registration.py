#!/usr/bin/env python3
"""Given an archive.org CA Statement of Vote identifier, locate the
"Voter Participation Statistics by County" table page(s) and crop the
San Francisco row (full width) at native resolution for reliable reading.

These printed SOV volumes carry an SF-county *eligible* (DOF citizen estimate)
column from ~1973-74 onward; the SoS CDN only goes back to 1999, so the 1974-98
franchise denominators come from here. Output crops are read by a human/vision
model and recorded (with confidence) in data/sf_registration_eligible_sov_1974_1998.csv.
NOTE: page OCR (tesseract/djvu) scrambles these multi-column tables and even a
vision model misreads digits on the full page; read the *cropped single row*.

Usage:  python3 recover_sov_registration.py <archive_id>=<label> [...]
Requires: ImageMagick (`convert`). Recipe validated on statementofvote197879cali:
djvu OBJECT _NNNN maps to BookReader page image n(NNNN-1); djvu word coords
share the image pixel space, so the SF row crops exactly.
"""
import re, subprocess, sys, urllib.request
from pathlib import Path

OUT = Path("/tmp/sov_pages"); OUT.mkdir(exist_ok=True)
UA = {"User-Agent": "Mozilla/5.0 (sf-election-count research)"}

def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()

def process(ident, label):
    xmlp = Path(f"/tmp/{ident}_djvu.xml")
    if not xmlp.exists():
        xmlp.write_bytes(get(f"https://archive.org/download/{ident}/{ident}_djvu.xml"))
    xml = xmlp.read_text(encoding="utf-8", errors="replace")
    objs = re.split(r'(?=<OBJECT)', xml)
    hits = []
    for chunk in objs:
        m = re.search(r'_(\d{4})\.djvu', chunk)
        if not m:
            continue
        leaf = int(m.group(1))
        words = re.findall(r'<WORD coords="([0-9,]+)"[^>]*>([^<]+)</WORD>', chunk)
        text = " ".join(w[1] for w in words).lower()
        # county participation table: SF present, an eligible/voting-population
        # column header, registered, and many county names
        ncounty = sum(text.count(c) for c in ("alameda", "fresno", "sacramento", "sonoma"))
        if "francisco" in text and ("eligible" in text or "voting  population" in text
                or "voting population" in text) and "registered" in text and ncounty >= 3:
            wm = re.search(r'<OBJECT[^>]*width="(\d+)"[^>]*height="(\d+)"', chunk)
            w = int(wm.group(1)) if wm else 2316
            fc = next((c for c, t in words if "rancisco" in t), None)
            hits.append((leaf, w, fc))
    if not hits:
        print(f"{label} ({ident}): NO participation-by-county table found")
        return
    for leaf, w, coords in hits:
        n = leaf - 1
        img = OUT / f"{label}_n{n}.jpg"
        if not img.exists():
            img.write_bytes(get(f"https://archive.org/download/{ident}/page/n{n}_w{w}.jpg"))
        if not coords:
            print(f"{label}: leaf {leaf} table found but no SF coords")
            continue
        xs = [int(v) for v in coords.split(",")]
        y = min(xs[1], xs[3])
        # full-width band around the SF row + a header crop for column labels
        row = OUT / f"{label}_SFrow.png"
        hdr = OUT / f"{label}_header.png"
        subprocess.run(["convert", str(img), "-crop", f"{w}x150+0+{y-55}", "+repage",
                        "-resize", "250%", str(row)], check=True)
        subprocess.run(["convert", str(img), "-crop", f"{w}x320+0+0", "+repage",
                        "-resize", "180%", str(hdr)], check=True)
        print(f"{label}: leaf {leaf} -> {row.name} (SF row y~{y}) + {hdr.name}")

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        ident, label = arg.split("=")
        try:
            process(ident, label)
        except Exception as e:
            print(f"ERROR {label}: {e}")
