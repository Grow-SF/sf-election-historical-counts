#!/usr/bin/env python3
"""Locate the San Francisco results column inside captured page slices and
emit zoomed crops ready for a reader agent.

The capture/sweep scripts save tall vertical slices of a newspaper page. A
results page usually prints several counties side by side; this finds the
"San Francisco" header that sits near a "precincts reporting" line and crops
a tall band around it (the SF column), upscaled and capped at 1900px so a
vision model can read it.

Usage:
    uv run --with pillow python3 locate_columns.py <scan_glob> [out_dir]
    # e.g. 'sweep_20060606_issue20060607_p2*_s*.png'  cols/

Heuristic, not perfect: always have the downstream reader confirm the column
header actually says "San Francisco" (neighboring-county columns look
identical — this is how a 2012 San Mateo column was once misread as SF).
"""
import subprocess, glob, sys, os
from PIL import Image

scan_glob = sys.argv[1]
out_dir = sys.argv[2] if len(sys.argv) > 2 else "cols"
os.makedirs(out_dir, exist_ok=True)

made = 0
for f in sorted(glob.glob(scan_glob)):
    tsv = subprocess.run(["tesseract", f, "-", "tsv"], capture_output=True, text=True).stdout
    words = []
    for line in tsv.split("\n")[1:]:
        r = line.split("\t")
        if len(r) >= 12 and r[11].strip():
            try:
                words.append((int(r[6]), int(r[7]), r[11]))  # left, top, text
            except ValueError:
                pass
    # an x-position where "FRANCISCO" sits near a "precinct" word
    xs = set()
    for x, y, w in words:
        if w.upper() == "FRANCISCO" and any(
            "precinct" in w2.lower() and abs(x2 - x) < 700 for x2, y2, w2 in words
        ):
            xs.add(x)
    if not xs:
        continue
    im = Image.open(f)
    W, H = im.size
    for k, x in enumerate(sorted(xs)[:2]):
        crop = im.crop((max(0, x - 450), 0, min(W, x + 900), H))
        crop = crop.resize((crop.width * 2, crop.height * 2), Image.LANCZOS)
        crop.thumbnail((1900, 1900), Image.LANCZOS)
        crop.save(f"{out_dir}/{os.path.basename(f)[:-4]}_col{k}.png")
        made += 1
print(f"column crops written: {made} -> {out_dir}/")
