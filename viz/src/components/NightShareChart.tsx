"use client";
import { useEffect, useMemo } from "react";
import {
  CartesianGrid,
  ComposedChart,
  Line,
  ReferenceLine,
  ResponsiveContainer,
  Scatter,
  XAxis,
  YAxis,
} from "recharts";
import { Election, Fit, KIND_COLOR, linearFit, NIGHT_FLOOR, yearFrac } from "@/lib/data";
import { ChartFrame, PointTooltip, useGraceHover } from "@/components/ui";

type Pt = {
  x: number;
  y: number;
  id: string;
  name: string;
  kind: string;
  source: string;
  partial: boolean;
  src: string | null;
};

// races where the election-night leader lost - decided by late-counted
// ballots (KQED/Mission Local coverage cited in the repository)
const FLIPS: Record<string, string> = {
  "2018-06-05":
    "Mayor: Leno led by ~1,000 on election night; Breed passed him on day 4 and won",
  "2020-11-03":
    "Supervisor D1: Philhour led election night; Chan won by 134 after late ballots",
};

// why each dimmed point understates the true end-of-night share
const PARTIAL_NOTES: Record<string, string> = {
  "1968-11-05":
    "press-deadline snapshot (1,140 of 1,282 precincts) — the true end-of-night share was higher",
  "1973-11-06":
    "single-candidate floor (Feinstein's supervisor votes only) — the true night share was higher",
  "1974-06-04":
    "mid-night snapshot (815 of 1,356 precincts) — the true end-of-night share was higher",
  "1976-11-02":
    "mid-night snapshot (545 of 935 precincts) — the true end-of-night share was higher",
  "1978-06-06":
    "partial press snapshot (81% of precincts, one party's primary) — the true night share was higher",
  "1995-12-12":
    "mid-count snapshot (339 of 551 precincts, the chad-jam night) — the true end-of-night share was higher",
  "2007-11-06":
    "the night release held only absentee/early votes — the state had decertified the city's voting machines, so every polling-place ballot was counted in the days after",
  "2008-02-05":
    "press-deadline snapshot (450 of 580 precincts) — the true end-of-night share was higher",
  "2008-06-03":
    "press-deadline snapshot (515 of 580 precincts) — the true end-of-night share was higher",
  "2010-06-08":
    "press-deadline snapshot (statewide tables, 36% of precincts at press) — the true end-of-night share was higher",
  "2012-06-05":
    "press-deadline snapshot (statewide tables, 49% of precincts at press) — the true end-of-night share was higher",
  "1996-03-26":
    "press-deadline snapshot (400 of 650 precincts) — the true end-of-night share was higher",
};

export default function NightShareChart({
  elections,
  from,
  to,
}: {
  elections: Election[];
  from: number;
  to: number;
}) {
  const { hover, show, hide, hold, clear } = useGraceHover<
    | { kind: "pt"; cx: number; cy: number; p: Pt }
    | { kind: "floor"; cx: number; cy: number; date: string; y: number }
  >();
  // a hovered shape that unmounts on filter change never fires onMouseLeave
  useEffect(() => clear(), [elections, from, to, clear]);

  const { pts, fitL, fitR } = useMemo(() => {
    const pts: Pt[] = elections
      .filter((e) => e.nightPct !== null && !e.provisional)
      .map((e) => ({
        x: yearFrac(e.id),
        y: e.nightPct as number,
        id: e.id,
        name: e.name,
        kind: e.kind,
        source: e.source,
        partial: Boolean(e.nightPartial),
        src: e.nightSrc || null,
      }));
    // mid-count partials understate the night - keep them out of the fit.
    // A Chow test on the full record puts a structural break at 2002, when
    // California opened the permanent vote-by-mail list to every voter
    // (slope -0.26 pts/yr before, -0.63 after; F=5.0 vs any other break).
    const solid = pts.filter((p) => !p.partial);
    const fitL: Fit | null = linearFit(solid.filter((p) => p.x < 2002).map((p) => [p.x, p.y]));
    const fitR: Fit | null = linearFit(solid.filter((p) => p.x >= 2002).map((p) => [p.x, p.y]));
    return { pts, fitL, fitR };
  }, [elections]);

  const floorPts = useMemo(
    () =>
      NIGHT_FLOOR.filter((p) => {
        const y = Number(p.date.slice(0, 4));
        return y >= from && y <= to;
      }).map((p) => ({ x: yearFrac(p.date), y: p.floorPct, date: p.date })),
    [from, to],
  );

  // stem between an election's actual night share and its floor: the gap is
  // the share of mail that arrived early enough to make the night count
  const stems = useMemo(() => {
    const floorBy = new Map(NIGHT_FLOOR.map((p) => [p.date, p.floorPct]));
    return pts
      .filter((p) => floorBy.has(p.id))
      .map((p) => ({ x: p.x, y0: floorBy.get(p.id) as number, y1: p.y }));
  }, [pts]);

  const seg = (f: Fit | null) =>
    f && [
      { x: f.x0, y: f.intercept + f.slope * f.x0 },
      { x: f.x1, y: f.intercept + f.slope * f.x1 },
    ];
  const trendL = seg(fitL);
  const trendR = seg(fitR);

  return (
    <div>
      {fitL && fitR && (
        <p className="smallcaps mb-2 text-faint">
          trend: {fitL.slope.toFixed(2)} pts/yr through 2001 ·{" "}
          <span className="text-rust">{fitR.slope.toFixed(2)} pts/yr since 2002</span>{" "}
          — the break is the permanent vote-by-mail list
        </p>
      )}
      <ChartFrame
        note={
          <>
            A dot can never sit below its diamond — in-person ballots are
            counted on election night, and the dotted stem between them is
            early-arriving mail, counted that night too. Gold line: November
            2020, every voter mailed a ballot. Gold rings: the night’s leader
            went on to lose (hover them). Dim dashed dots are mid-count
            partials, excluded from the trend. The trend is fit in two
            segments because the decline isn’t one process: a structural
            break in 2002 — the year every Californian could join the
            permanent vote-by-mail list — splits forty years of gentle drift
            from the modern slide. Elections with only day-after
            records appear in the charts below instead.
          </>
        }
      >
        <div className="smallcaps mb-2 flex flex-wrap items-center gap-x-5 gap-y-1 text-faint">
          <span className="flex items-center gap-1.5">
            <svg width="11" height="11" aria-hidden><path d="M5.5 1 L10 5.5 L5.5 10 L1 5.5 Z" fill="none" stroke="var(--color-faint)" strokeWidth="1.2"/></svg>
            in-person vote
          </span>
          <span className="flex items-center gap-1.5">
            <svg width="12" height="12" aria-hidden><circle cx="6" cy="6" r="5" fill="var(--color-rust)"/></svg>
            counted by election night (in-person + early mail)
          </span>
        </div>
        <div className="relative">
          {hover?.kind === "pt" && (
            <PointTooltip cx={hover.cx} cy={hover.cy} onMouseEnter={hold} onMouseLeave={hide}>
              <div className="smallcaps" style={{ color: KIND_COLOR[hover.p.kind] }}>
                {hover.p.kind}
                {hover.p.source === "archival" ? " · archival" : ""}
              </div>
              <div className="font-semibold">{hover.p.id}</div>
              <div className="stat-figure">
                {hover.p.partial ? "\u2265 " : ""}
                {hover.p.y}% counted by election night
              </div>
              {hover.p.partial && (
                <div className="max-w-52 text-xs italic text-faint">
                  {PARTIAL_NOTES[hover.p.id] ??
                    "partial night snapshot — the true end-of-night share was higher"}
                </div>
              )}
              {FLIPS[hover.p.id] && (
                <div className="max-w-56 text-xs italic" style={{ color: "var(--color-gold)" }}>
                  {FLIPS[hover.p.id]}
                </div>
              )}
              {hover.p.src && (
                <div className="mt-1 text-[11px] text-faint">
                  source: {hover.p.src} ·{" "}
                  <a
                    href={`/sources#${hover.p.id}`}
                    className="border-b border-rust/40 text-rust hover:bg-rust/10"
                  >
                    full citation →
                  </a>
                </div>
              )}
            </PointTooltip>
          )}
          {hover?.kind === "floor" && (
            <PointTooltip cx={hover.cx} cy={hover.cy} onMouseEnter={hold} onMouseLeave={hide}>
              <div className="smallcaps text-faint">election-night floor</div>
              <div className="font-semibold">{hover.date}</div>
              <div className="stat-figure">{hover.y}% voted in person</div>
              <div className="text-xs italic text-faint">
                in-person votes are counted on election night, so that night
                showed at least this much
              </div>
              <div className="mt-1 text-[11px] text-faint">
                source: certified precinct/mail split (DOE turnout history / SoS) ·{" "}
                <a href="/sources" className="border-b border-rust/40 text-rust hover:bg-rust/10">
                  sources →
                </a>
              </div>
            </PointTooltip>
          )}
          <ResponsiveContainer width="100%" height={360}>
            <ComposedChart margin={{ top: 12, right: 20, bottom: 8, left: 0 }}>
              <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
              {from <= 2002 && to >= 2002 && (
                // permanent vote-by-mail list opens to all voters (2002) -
                // the structural break in the night-share trend
                <ReferenceLine
                  x={2002}
                  stroke="var(--color-ink)"
                  strokeWidth={1}
                  strokeDasharray="5 4"
                  opacity={0.45}
                />
              )}
              {from <= 2020 && to >= 2020 && (
                // AB 860: every California voter mailed a ballot (Nov 2020)
                <ReferenceLine
                  x={2020.6}
                  stroke="var(--color-gold)"
                  strokeWidth={1.2}
                  strokeDasharray="5 4"
                  opacity={0.8}
                />
              )}
              <XAxis
                type="number"
                dataKey="x"
                domain={["dataMin - 1", "dataMax + 1"]}
                tickFormatter={(v: number) => String(Math.round(v))}
                tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
                stroke="var(--color-faint)"
                tickLine={false}
              />
              <YAxis
                type="number"
                dataKey="y"
                domain={[0, 100]}
                ticks={[0, 20, 40, 60, 80, 100]}
                tickFormatter={(v: number) => `${v}%`}
                tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
                stroke="var(--color-faint)"
                tickLine={false}
                width={48}
              />
              {stems.map((st) => (
              <ReferenceLine
                key={st.x}
                segment={[
                  { x: st.x, y: st.y0 },
                  { x: st.x, y: st.y1 },
                ]}
                stroke="var(--color-faint)"
                strokeWidth={1}
                strokeDasharray="1 3"
                opacity={0.6}
              />
            ))}
            <Scatter
              data={floorPts}
              isAnimationActive={false}
              shape={(props: unknown) => {
                const { cx, cy, payload } = props as {
                  cx: number;
                  cy: number;
                  payload: { date: string; y: number };
                };
                return (
                  <path
                    d={`M ${cx} ${cy - 4.5} L ${cx + 4.5} ${cy} L ${cx} ${cy + 4.5} L ${cx - 4.5} ${cy} Z`}
                    fill="var(--color-paper)"
                    fillOpacity={0.01}
                    stroke="var(--color-faint)"
                    strokeWidth={1.2}
                    opacity={0.75}
                    style={{ cursor: "pointer" }}
                    onMouseEnter={() =>
                      show({ kind: "floor", cx, cy, date: payload.date, y: payload.y })
                    }
                    onMouseLeave={hide}
                  />
                );
              }}
            />
            {trendL && (
                <Line
                  data={trendL}
                  dataKey="y"
                  stroke="var(--color-ink)"
                  strokeWidth={1.5}
                  strokeDasharray="6 4"
                  dot={false}
                  isAnimationActive={false}
                />
              )}
              {trendR && (
                <Line
                  data={trendR}
                  dataKey="y"
                  stroke="var(--color-ink)"
                  strokeWidth={1.5}
                  strokeDasharray="6 4"
                  dot={false}
                  isAnimationActive={false}
                />
              )}
              <Scatter
                data={pts}
                isAnimationActive={false}
                shape={(props: unknown) => {
                  const { cx, cy, payload } = props as {
                    cx: number;
                    cy: number;
                    payload: Pt;
                  };
                  const c = KIND_COLOR[payload.kind];
                  const common = {
                    onMouseEnter: () => show({ kind: "pt" as const, cx, cy, p: payload }),
                    onMouseLeave: hide,
                    style: { cursor: "pointer" },
                  };
                  const dot = payload.partial ? (
                    // mid-count partial: dim, dashed - a lower bound, not the night
                    <circle cx={cx} cy={cy} r={6.5} fill="var(--color-paper)" stroke={c} strokeWidth={1.5} strokeDasharray="3 3" opacity={0.35} {...common} />
                  ) : (
                    <circle cx={cx} cy={cy} r={6.5} fill={c} {...common} />
                  );
                  if (!FLIPS[payload.id]) return dot;
                  // ring marks a race the election-night leader went on to lose
                  return (
                    <g>
                      <circle cx={cx} cy={cy} r={11} fill="none" stroke="var(--color-gold)" strokeWidth={2} />
                      {dot}
                    </g>
                  );
                }}
              />
            </ComposedChart>
          </ResponsiveContainer>
        </div>
        <p className="smallcaps mt-2 text-faint">
          dashed verticals:{" "}
          <span className="text-ink">2002 — permanent vote-by-mail opens to everyone</span>
          {" · "}
          <span style={{ color: "var(--color-gold)" }}>
            2020 — COVID: every voter mailed a ballot
          </span>
        </p>
      </ChartFrame>
    </div>
  );
}
