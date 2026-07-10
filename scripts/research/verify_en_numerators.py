#!/usr/bin/env python3
"""Machine-check every sourced election_night_ballots against its cited URL.

Fetches each numerator source (Wayback raw id_ form for archived pages) into
cache/numerators/, converts to text, and checks the claimed ballot count
appears. Network: ~54 fetches with a 2s pause each; artifacts are cached so
reruns only refetch failures. Writes cache/numerator_results.json.
"""
import gzip
import json
import pathlib
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import (
    CACHE, EN, fetch, find_number, load_rows, pdf_text, strip_html, wayback_raw,
)


def load_render_verified():
    """Manifest of numerator rows verified by rendering the archived page
    with puppeteer (curl-only fetch here cannot execute JS). Absent file
    means no overrides."""
    p = EN / "render_verified.json"
    if not p.exists():
        return {}
    manifest = json.loads(p.read_text())
    return {(m["slug"], m["date"], m["url"]): m for m in manifest}


def apply_render_override(res, manifest, source_url):
    """Return res, with a render-verified manifest override applied when
    legitimate: the manifest entry must match on (slug, date, url) and its
    evidence must actually contain the claimed number."""
    if res["status"] == "VERIFIED":
        return res
    override = manifest.get((res["slug"], res["date"], source_url))
    if override is None:
        return res
    if not find_number(override["evidence"], res["claimed"]):
        return res
    return {
        **res,
        "status": "VERIFIED",
        "evidence": "render-verified: " + override["evidence"],
    }


def source_text(url, dest_base):
    """Fetch url and return (text, artifact_path). text is None on failure."""
    bare = url.lower().split("?")[0]
    is_pdf = bare.endswith(".pdf") or "documentcenter" in bare
    dest = dest_base.with_suffix(".pdf" if is_pdf else ".html")
    if not fetch(wayback_raw(url), dest):
        return None, dest
    if is_pdf:
        return pdf_text(dest), dest
    data = dest.read_bytes()
    if data[:2] == b"\x1f\x8b":
        # Wayback's raw id_ replay serves the original content-encoding: gzip
        # bytes verbatim; curl (no --compressed) does not decode them.
        data = gzip.decompress(data)
    if data[:4] == b"%PDF":
        # Some CMS document URLs (e.g. a CivicPlus friendly slug with no
        # .pdf suffix) still serve a real PDF; sniff the magic bytes rather
        # than trust the URL shape, since the extension check above missed it.
        pdf_dest = dest_base.with_suffix(".pdf")
        pdf_dest.write_bytes(data)
        return pdf_text(pdf_dest), pdf_dest
    raw = data.decode("utf-8", errors="replace")
    return (raw if bare.endswith(".json") else strip_html(raw)), dest


def main():
    render_verified = load_render_verified()
    results = []
    for r in load_rows():
        if r["election_night_ballots"] is None:
            continue
        url = r["source_url_night"]
        dest_base = CACHE / "numerators" / f"{r['slug']}-{r['date']}"
        text, dest = source_text(url, dest_base)
        res = {
            "slug": r["slug"], "date": r["date"], "kind": "numerator",
            "claimed": r["election_night_ballots"], "url": url,
            "artifact": str(dest), "status": "FETCH_FAILED", "evidence": None,
        }
        if text is not None:
            hit = find_number(text, r["election_night_ballots"])
            res["status"] = "VERIFIED" if hit else "NOT_FOUND"
            res["evidence"] = hit
        res = apply_render_override(res, render_verified, url)
        results.append(res)
        print(f"{res['status']:12} {r['slug']} {r['date']}")

    out = CACHE / "numerator_results.json"
    out.write_text(json.dumps(results, indent=1) + "\n")
    print(Counter(x["status"] for x in results), "->", out)


if __name__ == "__main__":
    main()
