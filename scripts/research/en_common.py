"""Shared helpers for the election-night source verification scripts.

Used by validate_election_night.py, verify_en_denominators.py,
verify_en_numerators.py and build_en_verification_report.py.
"""
import html as html_mod
import json
import pathlib
import re
import subprocess
import time

ROOT = pathlib.Path(__file__).resolve().parents[2]
EN = ROOT / "data/research/election-night"
CACHE = EN / "cache"
UA = "Mozilla/5.0 (sf-election-count source verification; steven@growsf.org)"


def norm_pct(p):
    """v4 stores election_night_pct in mixed units; <= 1.5 means fraction.
    Same rule as scripts/build_county_night.py."""
    if p is None:
        return None
    return round(p * 100, 2) if p <= 1.5 else round(p, 2)


def wayback_raw(url):
    """Rewrite a Wayback page URL to the raw id_ form (no toolbar chrome)."""
    return re.sub(
        r"(https://web\.archive\.org/web/\d{14})/", r"\g<1>id_/", url, count=1
    )


def find_number(text, n):
    """Context string if integer n appears in text (comma-formatted or bare),
    not embedded inside a longer number; else None."""
    for v in (f"{n:,}", str(n)):
        for m in re.finditer(re.escape(v), text):
            before = text[m.start() - 1 : m.start()]
            after = text[m.end() : m.end() + 1]
            two_before = text[m.start() - 2 : m.start() - 1]
            after_comma = text[m.end() + 1 : m.end() + 2]
            if (before.isdigit() or after.isdigit() or
                (before == "," and two_before.isdigit()) or
                (after == "," and after_comma.isdigit())):
                continue
            return " ".join(text[max(0, m.start() - 80) : m.end() + 80].split())
    return None


def strip_html(raw):
    return html_mod.unescape(re.sub(r"<[^>]+>", " ", raw))


def pdf_text(path):
    r = subprocess.run(
        ["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True
    )
    return r.stdout if r.returncode == 0 else ""


def fetch(url, dest, tries=3, sleep=2.0):
    """curl url into dest, cached: an existing non-empty dest is a hit."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 0:
        return True
    for i in range(tries):
        r = subprocess.run(
            ["curl", "-sSL", "--fail", "-A", UA, "--max-time", "180",
             "-o", str(dest), url]
        )
        if r.returncode == 0 and dest.exists() and dest.stat().st_size > 0:
            time.sleep(sleep)
            return True
        time.sleep(5.0 * (i + 1))
    if dest.exists():
        dest.unlink()
    return False


def load_rows():
    """All election rows across all county JSONs, flattened. Skips
    non-county manifests in the same directory (e.g. render_verified.json,
    a list, not a {jurisdiction, elections} county object)."""
    rows = []
    for fp in sorted(EN.glob("*.json")):
        d = json.loads(fp.read_text())
        if not isinstance(d, dict) or "elections" not in d:
            continue
        for e in d["elections"]:
            rows.append(
                {
                    "slug": fp.stem,
                    "county": d["jurisdiction"].replace(" County", ""),
                    **e,
                }
            )
    return rows
