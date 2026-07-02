#!/usr/bin/env python3
"""Extract self-describing plateau evidence from the cached numerator artifacts.

For each sourced election row, pull the artifact's opening text, every
timestamp-looking snippet, and every line carrying plateau vocabulary
(night / semi-final / unofficial / last / as of). Output is a compact
JSON + stdout digest for the controller to adjudicate. No network.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import CACHE, load_rows, pdf_text, strip_html

STAMP = re.compile(
    r"(?:[01]?\d/[0-3]?\d/(?:20)?\d\d[^\n]{0,60})"
    r"|(?:\d{1,2}:\d{2}(?::\d{2})?\s*(?:AM|PM|am|pm)[^\n]{0,40})"
    r"|(?:websiteupdatedat[^,}]{0,60})"
)
LABEL = re.compile(
    r"night|semi[- ]?final|unofficial|last of|last update|as of|final report"
    r"|first report|zero report|canvass",
    re.I,
)


def artifact_text(p):
    if p.suffix == ".pdf":
        return pdf_text(p)
    data = p.read_bytes()
    if data[:2] == b"\x1f\x8b":
        import gzip

        data = gzip.decompress(data)
    raw = data.decode("utf-8", errors="replace")
    return raw if raw.lstrip()[:1] in "{[" else strip_html(raw)


def main():
    out = []
    for r in load_rows():
        if r["election_night_ballots"] is None:
            continue
        base = CACHE / "numerators" / f"{r['slug']}-{r['date']}"
        p = next(
            (base.with_suffix(s) for s in (".pdf", ".html") if base.with_suffix(s).exists()),
            None,
        )
        if p is None:
            out.append({"slug": r["slug"], "date": r["date"], "artifact": None})
            continue
        text = artifact_text(p)
        stamps, labels = [], []
        for m in STAMP.finditer(text):
            s = " ".join(m.group().split())
            if s not in stamps:
                stamps.append(s)
            if len(stamps) >= 8:
                break
        for line in text.splitlines():
            line = " ".join(line.split())
            if line and LABEL.search(line) and line[:120] not in labels:
                labels.append(line[:120])
            if len(labels) >= 8:
                break
        out.append(
            {
                "slug": r["slug"],
                "date": r["date"],
                "claimed": r["election_night_ballots"],
                "artifact": p.name,
                "head": " ".join(text[:300].split()),
                "stamps": stamps,
                "labels": labels,
            }
        )
    dest = CACHE / "plateau_evidence.json"
    dest.write_text(json.dumps(out, indent=1) + "\n")
    assert len(out) == 54, f"expected 54 sourced rows, got {len(out)}"
    for rec in out:
        print(f"== {rec['slug']} {rec['date']} claimed={rec.get('claimed'):,}")
        print(f"   head: {rec.get('head', '')[:160]}")
        for s in rec.get("stamps", []):
            print(f"   stamp: {s}")
        for l in rec.get("labels", []):
            print(f"   label: {l}")


if __name__ == "__main__":
    main()
