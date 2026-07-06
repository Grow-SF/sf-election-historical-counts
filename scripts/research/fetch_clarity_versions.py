#!/usr/bin/env python3
"""Enumerate Clarity ENR version history around each cited election-night version.

For every sourced row citing results.enr.clarityelections.com, fetch the cited
version's electionsettings.json (websiteupdatedat + full versions array), find
the next published version, and fetch its electionsettings.json and sum.json
(timestamp + BC). Bounded: 7 rows x <=3 fetches. Cached like everything else.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from en_common import CACHE, fetch, load_rows

BASE = "https://results.enr.clarityelections.com"
PAT = re.compile(r"clarityelections\.com/(CA/[^/]+)/(\d+)/(\d+)/json")


def get_json(url, dest):
    if not fetch(url, dest):
        return None
    try:
        return json.loads(dest.read_text(errors="replace"))
    except json.JSONDecodeError:
        return None


def settings(path, eid, ver, cdir):
    """electionsettings.json with the known Clarity path variants."""
    for sub in ("json/en/electionsettings.json", "json/electionsettings.json"):
        es = get_json(f"{BASE}/{path}/{eid}/{ver}/{sub}", cdir / f"settings-{ver}.json")
        if es:
            return es
        (cdir / f"settings-{ver}.json").unlink(missing_ok=True)
    return None


def main():
    out = []
    for r in load_rows():
        u = r.get("source_url_night") or ""
        m = PAT.search(u)
        if r["election_night_ballots"] is None or not m:
            continue
        path, eid, ver = m.groups()
        cdir = CACHE / "clarity" / f"{r['slug']}-{r['date']}"
        rec = {
            "slug": r["slug"], "date": r["date"], "election_id": eid,
            "cited_version": ver, "cited_updatedat": None,
            "versions": None, "next_version": None,
            "next_updatedat": None, "next_bc": None,
        }
        es = settings(path, eid, ver, cdir)
        if es:
            rec["cited_updatedat"] = es.get("websiteupdatedat")
        # a version-pinned settings file only lists versions up to itself;
        # the full history lives in the CURRENT version's settings
        cur = None
        if fetch(f"{BASE}/{path}/{eid}/current_ver.txt", cdir / "current_ver.txt"):
            cur = (cdir / "current_ver.txt").read_text(errors="replace").strip()
        ces = settings(path, eid, cur, cdir) if cur and cur.isdigit() else None
        if ces:
            versions = sorted(int(v) for v in ces.get("versions", []) if str(v).isdigit())
            rec["versions"] = versions
            later = [v for v in versions if v > int(ver)]
            if later:
                nv = later[0]
                rec["next_version"] = nv
                nes = settings(path, eid, nv, cdir)
                if nes:
                    rec["next_updatedat"] = nes.get("websiteupdatedat")
                ns = get_json(f"{BASE}/{path}/{eid}/{nv}/json/sum.json", cdir / f"sum-{nv}.json")
                if ns:
                    bc = ns.get("BC")
                    if bc is None and ns.get("Contests"):
                        bc = ns["Contests"][0].get("BC")
                    rec["next_bc"] = bc
        out.append(rec)
        print(
            f"{r['slug']} {r['date']}: v{ver} @ {rec['cited_updatedat']} -> "
            f"next v{rec['next_version']} @ {rec['next_updatedat']} (BC {rec['next_bc']})"
        )
    dest = CACHE / "clarity_versions.json"
    dest.write_text(json.dumps(out, indent=1) + "\n")
    print(f"{len(out)} clarity rows -> {dest}")


if __name__ == "__main__":
    main()
