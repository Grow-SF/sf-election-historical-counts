"use client";
import { useEffect, useMemo } from "react";
import {
  CartesianGrid,
  ComposedChart,
  ResponsiveContainer,
  useXAxisScale,
  useYAxisScale,
  XAxis,
  YAxis,
} from "recharts";
import { Election, Fit, KIND_COLOR, linearFit, NIGHT_FLOOR, yearFrac } from "@/lib/data";
import { ChartFrame, PointTooltip, eventLines, useGraceHover } from "@/components/ui";

type Seg = { x: number; y: number }[];

// All data marks (stems, floor diamonds, dots, trend dashes) are drawn by hand
// in one SVG layer — see NightMarks below for why and the draw order.

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
  "1992-11-03":
    "press-deadline snapshot (513 of 609 precincts) — the true end-of-night share was higher",
  "1978-11-07":
    "near-complete day-after count (governor race, 223,147 ballots); the exact final is uncertain because the DOE turnout table for 1978 is internally contradicted",
};

type Hover =
  | { kind: "pt"; cx: number; cy: number; p: Pt }
  | { kind: "floor"; cx: number; cy: number; date: string; y: number };

type FloorPt = { x: number; y: number; date: string };
type Stem = { x: number; y0: number; y1: number };

/** A trend segment as two stacked SVG lines: a paper casing so the dash stays
 *  legible over dark dot clusters, then the dashed ink line on top. */
function TrendDash({
  seg,
  X,
  Y,
}: {
  seg: Seg;
  X: (v: number) => number;
  Y: (v: number) => number;
}) {
  const [a, b] = seg;
  const p = { x1: X(a.x), y1: Y(a.y), x2: X(b.x), y2: Y(b.y) };
  return (
    <>
      <line {...p} stroke="var(--color-paper)" strokeWidth={4} />
      <line
        {...p}
        stroke="var(--color-ink)"
        strokeWidth={2}
        strokeDasharray="6 4"
      />
    </>
  );
}

/**
 * Every data mark in one hand-drawn SVG layer, positioned with the chart's own
 * scales (useXAxisScale/useYAxisScale). This deliberately avoids recharts
 * <Scatter>: its symbols are wrapped in an animation layer keyed by an id that
 * changes on every render, so each render unmounts and remounts all ~520 symbols
 * — which made the year-slider drag cost ~200ms/tick. Drawn by hand the marks
 * update in place (no remount), cutting the drag cost ~5x. Draw order is
 * back-to-front: stems, floor diamonds, dots, then trend dashes on top.
 */
function NightMarks({
  pts,
  floorPts,
  stems,
  trendM,
  trendR,
  show,
  hide,
}: {
  pts: Pt[];
  floorPts: FloorPt[];
  stems: Stem[];
  trendM: Seg | null | false;
  trendR: Seg | null | false;
  show: (h: Hover) => void;
  hide: () => void;
}) {
  const xScale = useXAxisScale();
  const yScale = useYAxisScale();
  if (!xScale || !yScale) return null;
  const X = (v: number) => xScale(v) as number;
  const Y = (v: number) => yScale(v) as number;
  return (
    <g className="lc-nightmarks">
      {/* stems: the gap between an election's night share and its in-person floor */}
      {stems.map((st) => (
        <line
          key={`stem-${st.x}`}
          x1={X(st.x)}
          x2={X(st.x)}
          y1={Y(st.y0)}
          y2={Y(st.y1)}
          stroke="var(--color-faint)"
          strokeWidth={1}
          strokeDasharray="1 3"
          opacity={0.6}
        />
      ))}
      {/* floor diamonds: in-person turnout (a lower bound on the night count) */}
      {floorPts.map((p) => {
        const cx = X(p.x);
        const cy = Y(p.y);
        return (
          <path
            key={`floor-${p.date}`}
            d={`M ${cx} ${cy - 4.5} L ${cx + 4.5} ${cy} L ${cx} ${cy + 4.5} L ${cx - 4.5} ${cy} Z`}
            fill="var(--color-paper)"
            fillOpacity={0.01}
            stroke="var(--color-faint)"
            strokeWidth={1.2}
            opacity={0.75}
            style={{ cursor: "pointer" }}
            onMouseEnter={() =>
              show({ kind: "floor", cx, cy, date: p.date, y: p.y })
            }
            onMouseLeave={hide}
          />
        );
      })}
      {/* dots: % counted on election night, colored by election kind */}
      {pts.map((p) => {
        const cx = X(p.x);
        const cy = Y(p.y);
        const c = KIND_COLOR[p.kind];
        const common = {
          onMouseEnter: () => show({ kind: "pt" as const, cx, cy, p }),
          onMouseLeave: hide,
          style: { cursor: "pointer" },
        };
        const dot = p.partial ? (
          // mid-count partial: dim, dashed - a lower bound, not the night
          <circle
            cx={cx}
            cy={cy}
            r={6.5}
            fill="var(--color-paper)"
            stroke={c}
            strokeWidth={1.5}
            strokeDasharray="3 3"
            opacity={0.35}
            {...common}
          />
        ) : (
          <circle cx={cx} cy={cy} r={6.5} fill={c} {...common} />
        );
        if (!FLIPS[p.id]) return <g key={p.id}>{dot}</g>;
        // ring marks a race the election-night leader went on to lose
        return (
          <g key={p.id}>
            <circle
              cx={cx}
              cy={cy}
              r={11}
              fill="none"
              stroke="var(--color-gold)"
              strokeWidth={2}
            />
            {dot}
          </g>
        );
      })}
      {/* trend dashes on top */}
      {trendM && <TrendDash seg={trendM} X={X} Y={Y} />}
      {trendR && <TrendDash seg={trendR} X={X} Y={Y} />}
    </g>
  );
}

export default function NightShareChart({
  elections,
  from,
  to,
  kinds,
}: {
  elections: Election[];
  from: number;
  to: number;
  kinds: Set<string>;
}) {
  const { hover, show, hide, hold, clear } = useGraceHover<Hover>();
  // a hovered shape that unmounts on filter change never fires onMouseLeave
  useEffect(() => clear(), [elections, from, to, clear]);

  const { pts, fitE, fitM, fitR } = useMemo(() => {
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
    // Three regimes, two structural breaks:
    //  - ~1927: the Progressive-era long-ballot bottleneck eases and election
    //    night becomes reliably near-complete again (still hand-counted paper -
    //    SF had no voting machines until punch cards in the 1960s).
    //  - 2002: California opens the permanent vote-by-mail list to every voter,
    //    starting the modern slide (a Chow test favors a 2002 break over any
    //    other in the modern record).
    const solid = pts.filter((p) => !p.partial);
    const fitE: Fit | null = linearFit(solid.filter((p) => p.x < 1927).map((p) => [p.x, p.y]));
    const fitM: Fit | null = linearFit(solid.filter((p) => p.x >= 1927 && p.x < 2002).map((p) => [p.x, p.y]));
    const fitR: Fit | null = linearFit(solid.filter((p) => p.x >= 2002).map((p) => [p.x, p.y]));
    return { pts, fitE, fitM, fitR };
  }, [elections]);

  const floorPts = useMemo(
    () =>
      NIGHT_FLOOR.filter((p) => {
        const y = Number(p.date.slice(0, 4));
        return y >= from && y <= to && kinds.has(p.kind);
      }).map((p) => ({ x: yearFrac(p.date), y: p.floorPct, date: p.date })),
    [from, to, kinds],
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
  const trendM = seg(fitM);
  const trendR = seg(fitR);

  return (
    <div>
      {fitM && fitR && (
        <p className="smallcaps mb-2 text-faint">
          {fitE && (
            <>
              <span className="text-moss">erratic before ~1927</span> (the
              long-ballot era) ·{" "}
            </>
          )}
          {fitM.slope.toFixed(2)} pts/yr 1927–2001 ·{" "}
          <span className="text-rust">{fitR.slope.toFixed(2)} pts/yr since 2002</span>{" "}
          — counts stabilize ~1927, then the vote-by-mail break in 2002
        </p>
      )}
      <ChartFrame
        title="How much of the vote was counted on election night"
        subtitle="Election-night count ÷ certified final, by election, 1868–2026"
        note={
          <>
            Each dot is an election’s night count as a share of its certified
            final. The open diamond is the in-person floor; the dotted stem up
            to the dot is early mail counted that night. Dim dashed dots are
            mid-count press snapshots — lower bounds, excluded from the trend —
            and rings mark races the election-night leader lost.
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
            <ComposedChart
              data={pts}
              margin={{ top: 12, right: 20, bottom: 8, left: 0 }}
            >
              <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
              {/* shared vote-counting milestones, identical across all charts
                  (incl. the 1926 voting-machine break that stabilized the count) */}
              {eventLines(from, to)}
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
              <NightMarks
                pts={pts}
                floorPts={floorPts}
                stems={stems}
                trendM={trendM}
                trendR={trendR}
                show={show}
                hide={hide}
              />
            </ComposedChart>
          </ResponsiveContainer>
        </div>
        <p className="smallcaps mt-2 text-faint">
          dashed verticals:{" "}
          <span className="text-ink">
            1926 voting machines · 1978 expanded absentee · 2002 permanent
            vote-by-mail · 2020 COVID
          </span>
        </p>
      </ChartFrame>
    </div>
  );
}
