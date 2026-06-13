#!/bin/zsh
# OCR-triage captured page slices: list the ones that look like a results
# table (a "precincts reporting" line near "San Francisco"/"S.F. Vote").
# Caches tesseract output per slice so re-runs are cheap.
#
# Usage:  ./triage.sh 'sweep_20060606_*_s*.png'
setopt null_glob
cd "$(dirname "$0")/../../mirror/newsbank/scans" 2>/dev/null || cd .
mkdir -p ocr_cache

GLOB="${1:-sweep_*_s*.png}"
# OCR any slice not already cached (6 in parallel)
for f in ${~GLOB}; do
  [ -s "ocr_cache/${f%.png}.txt" ] || echo "$f"
done | xargs -P 6 -I{} sh -c 'tesseract "{}" "ocr_cache/$(basename {} .png)" 2>/dev/null'

# report slices whose text has both an SF marker and a precincts line
echo "--- candidate slices (SF results table):"
for t in ocr_cache/${~GLOB:r}.txt(N) ocr_cache/$(echo ${~GLOB} | sed 's/\.png/.txt/')(N); do :; done
grep -ilE 'san francisco|s\.f\. vote|how san francisco' ocr_cache/${~GLOB:gs/.png/.txt/}(N) 2>/dev/null \
  | xargs grep -lE 'precincts (reporting|rptg)|[0-9]+ of [0-9]+ precincts' 2>/dev/null \
  | sed 's#ocr_cache/##; s/_s[0-9]*\.txt//' | sort -u
