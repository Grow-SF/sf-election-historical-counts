#!/usr/bin/env python3
"""Render docs/img/sd-night-share.png from the San Diego night-count datasets.

Run: uv run --with matplotlib python3 scripts/research/plot_sd_night_history.py

Inputs (real data only, never inline constants):
  data/research/san-diego-history/sd_night_history.csv  (1871-1920 newspaper floors,
      share basis: same-contest certified total)
  data/research/election-night/san-diego-ca.json        (2014-2024 modern plateau
      shares, basis: certified ballots cast)
The two bases differ by construction; the chart keeps them as separate series.
"""
import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "img" / "sd-night-share.png"

# palette.md roles (light mode)
SURFACE = "#fcfcfb"
INK = "#0b0b0b"
SECONDARY = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASELINE = "#c3c2b7"
SERIES_1 = "#2a78d6"  # newspaper-era floors
SERIES_2 = "#1baf7a"  # modern plateau shares

# floors that are definition artifacts (paper printed majorities / no city
# returns / city-only proxy), hollow-marked so they never read as slow counts
ARTIFACT_DATES = {"1890-11-04", "1892-11-08", "1900-11-06"}

hist_x, hist_y, art_x, art_y = [], [], [], []
for r in csv.DictReader(open(ROOT / "data/research/san-diego-history/sd_night_history.csv")):
    if not r["night_share_pct"]:
        continue  # 1882: no certified denominator
    year = int(r["election_date"][:4]) + (int(r["election_date"][5:7]) - 1) / 12
    pct = float(r["night_share_pct"])
    if r["election_date"] in ARTIFACT_DATES:
        art_x.append(year)
        art_y.append(pct)
    else:
        hist_x.append(year)
        hist_y.append(pct)

panel = json.load(open(ROOT / "data/research/election-night/san-diego-ca.json"))
mod_x, mod_y = [], []
for e in panel["elections"]:
    if e["election_night_pct"] is None:
        continue
    mod_x.append(int(e["date"][:4]) + (int(e["date"][5:7]) - 1) / 12)
    mod_y.append(e["election_night_pct"])

fig, ax = plt.subplots(figsize=(9.6, 4.6), dpi=200)
fig.patch.set_facecolor(SURFACE)
ax.set_facecolor(SURFACE)

ax.scatter(hist_x, hist_y, s=42, color=SERIES_1, zorder=3,
           label="1871-1920 morning-paper floor (share of certified contest total)")
ax.scatter(art_x, art_y, s=42, facecolors=SURFACE, edgecolors=SERIES_1,
           linewidths=1.6, zorder=3)
ax.scatter(mod_x, mod_y, s=42, color=SERIES_2, zorder=3,
           label="2014-2024 election-night plateau (share of certified ballots)")

# the unrecovered stretch
ax.axvspan(1921.5, 2013.5, color=GRID, alpha=0.35, zorder=1)
ax.text((1922 + 2014) / 2, 52, "1922-2010 unrecovered\n(no digitized SD paper;\nNewsBank starts 2018)",
        ha="center", va="center", fontsize=8, color=MUTED, linespacing=1.5)

# direct era annotations (relief for the aqua contrast warning + story anchors)
ax.annotate("1918-1920:\nlong-ballot collapse", xy=(1919.4, 20), xytext=(1929, 30),
            fontsize=8, color=SECONDARY, ha="left", va="center",
            arrowprops=dict(arrowstyle="-", color=BASELINE, lw=1))
ax.annotate("hollow = floor is a\nnewspaper-practice artifact", xy=(1892.8, 8.7),
            xytext=(1899, 15), fontsize=8, color=SECONDARY, ha="left", va="center",
            arrowprops=dict(arrowstyle="-", color=BASELINE, lw=1))
ax.annotate("1912: 80.8% by 2 a.m.\n(SF 1916 managed ~3%)", xy=(1912.8, 82),
            xytext=(1872, 92), fontsize=8, color=SECONDARY, ha="left", va="center",
            arrowprops=dict(arrowstyle="-", color=BASELINE, lw=1))

ax.set_ylim(0, 100)
ax.set_xlim(1866, 2030)
ax.set_ylabel("counted by election night, % of certified", fontsize=9, color=SECONDARY)
ax.set_yticks(range(0, 101, 25))
ax.set_xticks(range(1880, 2030, 20))
ax.tick_params(colors=MUTED, labelsize=8.5, length=0)
ax.grid(axis="y", color=GRID, linewidth=0.8)
ax.set_axisbelow(True)
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(BASELINE)

ax.set_title("San Diego County: how much of the vote was counted by election night",
             fontsize=11.5, color=INK, loc="left", pad=12)
leg = ax.legend(loc="lower center", fontsize=8, frameon=False, labelcolor=SECONDARY,
                handletextpad=0.4, borderaxespad=0.2, bbox_to_anchor=(0.5, -0.02))

fig.tight_layout()
OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, facecolor=SURFACE)
print(f"wrote {OUT}")
