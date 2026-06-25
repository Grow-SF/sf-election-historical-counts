"use client";
import { useCallback, useMemo, useState } from "react";
import {
  CartesianGrid,
  ComposedChart,
  ReferenceLine,
  ResponsiveContainer,
  usePlotArea,
  useXAxisScale,
  useYAxisScale,
  XAxis,
  YAxis,
} from "recharts";
import { Election } from "@long-count/data";
import { fmt } from "../lib/format";
import { useChartTheme } from "../theme";
import { ChartFrame, DualRange } from "./ui";

const maxDay = (e: Election) => e.pts.reduce((m, [d]) => Math.max(m, d), 0);

type DP = { d: number; p: number };
type Hover = { name: string; d: number; p: number; cx: number; cy: number };

/** ~6–8 evenly spaced, round day ticks spanning [lo, hi]. */
function dayTicks(lo: number, hi: number): number[] {
  const span = Math.max(1, hi - lo);
  const step =
    [1, 2, 5, 10, 15, 20, 25, 50, 100].find((s) => span / s <= 8) ??
    Math.ceil(span / 8);
  const ticks: number[] = [];
  for (let t = Math.ceil(lo / step) * step; t <= hi + 1e-9; t += step) {
    ticks.push(Math.round(t));
  }
  return ticks;
}

/**
 * A broken-axis glyph ("--/ /--") drawn at one edge of the x-axis, signalling
 * that the visible day window is a slice and the data continues past it.
 * Rendered inside the chart so it tracks the plot area via recharts hooks.
 */
function AxisBreak({
  side,
  show,
  label,
}: {
  side: "left" | "right";
  show: boolean;
  label?: string;
}) {
  const theme = useChartTheme();
  const plot = usePlotArea();
  if (!plot || !show) return null;
  const right = side === "right";
  const x = right ? plot.x + plot.width : plot.x;
  const yb = plot.y + plot.height; // x-axis baseline
  const cx = right ? x - 3 : x + 3;
  return (
    <g pointerEvents="none">
      {/* punch a gap in the axis line, then two slashes across it */}
      <rect x={cx - 7} y={yb - 7} width={18} height={14} fill={theme.paper} />
      <path
        d={`M ${cx - 4} ${yb + 5} L ${cx + 2} ${yb - 5}`}
        stroke={theme.faint}
        strokeWidth={1.2}
      />
      <path
        d={`M ${cx + 1} ${yb + 5} L ${cx + 7} ${yb - 5}`}
        stroke={theme.faint}
        strokeWidth={1.2}
      />
      {label && (
        <>
          <rect
            x={x - 96}
            y={plot.y + 1}
            width={96}
            height={14}
            fill={theme.paper}
            fillOpacity={0.85}
          />
          <text
            x={x - 2}
            y={plot.y + 11}
            textAnchor="end"
            style={{
              fontFamily: theme.fontMono,
              fontSize: 10,
              fill: theme.faint,
            }}
          >
            {label}
          </text>
        </>
      )}
    </g>
  );
}

/** Dual-thumb day-window slider, 0 … max. Keeps the two handles ≥1 day apart. */
function DayRangeSlider({
  lo,
  hi,
  max,
  onChange,
}: {
  lo: number;
  hi: number;
  max: number;
  onChange: (lo: number, hi: number) => void;
}) {
  return (
    <div className="mb-4 flex items-center gap-3">
      <span className="smallcaps shrink-0 text-faint">day window</span>
      <span className="stat-figure shrink-0 text-xs text-rust">{lo}</span>
      <DualRange
        min={0}
        max={max}
        lo={lo}
        hi={hi}
        minGap={1}
        onChange={onChange}
        ariaLabel="day window"
        className="grow"
      />
      <span className="stat-figure shrink-0 text-xs text-rust">{hi}</span>
      <span className="smallcaps shrink-0 text-faint">of {max}d</span>
    </div>
  );
}

function DetailPanel({ e }: { e: Election }) {
  const theme = useChartTheme();
  const row = (label: string, value: React.ReactNode) => (
    <div className="flex items-baseline justify-between gap-3 border-b border-rule py-1.5">
      <span className="smallcaps text-faint">{label}</span>
      <span className="stat-figure text-sm">{value}</span>
    </div>
  );
  const t = (n: number) => {
    const v = e.thresholds[String(n)];
    if (!v) return "—";
    return `${v.bound ? "≤ " : ""}${v.days}d`;
  };
  return (
    <div className="border border-rule bg-paper-deep/60 p-4">
      <p className="smallcaps" style={{ color: theme.colorsByKind[e.kind] }}>
        {e.kind}
        {e.source === "archival" ? " · archival recovery" : ""}
        {e.provisional ? " · count ongoing" : ""}
      </p>
      <h3 className="mt-1 text-lg font-semibold leading-snug">
        {e.id} — {e.name}
      </h3>
      <div className="mt-3">
        {row("ballots counted", fmt(e.final))}
        {e.registered && row("registered voters", fmt(e.registered))}
        {e.nightPct !== null && row("by election night", `${e.nightPct}%`)}
        {e.vbmShare !== null && row("voted by mail", `${e.vbmShare}%`)}
        {row(
          "to 50% / 80% / 90% / 98%",
          `${t(50)} / ${t(80)} / ${t(90)} / ${t(98)}`,
        )}
        {row("observations", e.nReports)}
      </div>
      {e.source === "archival" && (
        <p className="mt-3 text-xs italic leading-relaxed text-faint">
          Recovered from Wayback Machine captures of the Department of
          Elections’ results pages; “≤” marks an upper bound from sparse
          snapshots.
        </p>
      )}
    </div>
  );
}

/**
 * Every trajectory drawn by hand in one SVG layer, positioned with the chart's
 * scales. This deliberately avoids one recharts <Line> per election: recharts
 * wraps each series in an animation layer keyed by an id that changes on every
 * render, so every render unmounts and remounts all ~190 series (plus their
 * dots) — which made the day-window slider and filters cost ~500ms. Drawn by
 * hand the paths update in place (no remount). Clipped to the plot so paths past
 * the day window don't overflow; selected lines are drawn last (on top).
 */
function TrajLines({
  elections,
  lineData,
  selected,
  // lo/hi aren't read directly (the scales handle positioning) but are passed
  // so this re-renders when the day window changes the scale.
  lo,
  hi,
}: {
  elections: Election[];
  lineData: Map<string, DP[]>;
  selected: Set<string>;
  lo: number;
  hi: number;
}) {
  const theme = useChartTheme();
  const xScale = useXAxisScale();
  const yScale = useYAxisScale();
  const plot = usePlotArea();
  if (!xScale || !yScale || !plot) return null;
  void lo;
  void hi;
  const X = (v: number) => xScale(v) as number;
  const Y = (v: number) => yScale(v) as number;
  const anySel = selected.size > 0;
  // draw selected last so they sit on top of the faint background
  const ordered = [...elections].sort(
    (a, b) => Number(selected.has(a.id)) - Number(selected.has(b.id)),
  );
  const clipId = "traj-clip";
  return (
    <g className="lc-trajlines">
      <defs>
        <clipPath id={clipId}>
          <rect x={plot.x} y={plot.y} width={plot.width} height={plot.height} />
        </clipPath>
      </defs>
      <g clipPath={`url(#${clipId})`}>
        {ordered.map((e) => {
          const data = lineData.get(e.id);
          if (!data || !data.length) return null;
          const isSel = selected.has(e.id);
          const muted = anySel && !isSel;
          const color = isSel ? theme.colorsByKind[e.kind] : theme.ink;
          const d = data
            .map(
              (pt, i) =>
                `${i ? "L" : "M"} ${X(pt.d).toFixed(1)} ${Y(pt.p).toFixed(1)}`,
            )
            .join(" ");
          return (
            <path
              key={e.id}
              d={d}
              fill="none"
              stroke={color}
              strokeOpacity={isSel ? 1 : muted ? 0.1 : 0.32}
              strokeWidth={isSel ? 2.5 : 1.2}
              strokeDasharray={e.source === "archival" ? "5 4" : undefined}
              strokeLinejoin="round"
              strokeLinecap="round"
            />
          );
        })}
        {/* dots: archival recoveries (always) and selected elections */}
        {ordered.map((e) => {
          const isSel = selected.has(e.id);
          if (!isSel && e.source !== "archival") return null;
          const data = lineData.get(e.id);
          if (!data) return null;
          const color = isSel ? theme.colorsByKind[e.kind] : theme.ink;
          return data.map((pt, i) => (
            <circle
              key={`${e.id}-${i}`}
              cx={X(pt.d)}
              cy={Y(pt.p)}
              r={isSel ? 3 : 2.5}
              fill={color}
              fillOpacity={isSel ? 1 : 0.45}
            />
          ));
        })}
      </g>
    </g>
  );
}

/**
 * A transparent overlay over the plot that does nearest-point hit-testing on
 * mousemove (recharts' <Tooltip> needs <Line> series, which we no longer have).
 * Reports the nearest point to the parent for the tooltip + highlight, and
 * selects the nearest election on click.
 */
function TrajHover({
  elections,
  lineData,
  lo,
  hi,
  hover,
  onHover,
  onLeave,
  onPick,
}: {
  elections: Election[];
  lineData: Map<string, DP[]>;
  lo: number;
  hi: number;
  hover: Hover | null;
  onHover: (h: Hover & { id: string }) => void;
  onLeave: () => void;
  onPick: (id: string) => void;
}) {
  const theme = useChartTheme();
  const xScale = useXAxisScale();
  const yScale = useYAxisScale();
  const plot = usePlotArea();
  if (!xScale || !yScale || !plot) return null;
  const X = (v: number) => xScale(v) as number;
  const Y = (v: number) => yScale(v) as number;
  const HIT = 30; // px proximity to count as "on" a line

  const nearest = (
    evt: React.MouseEvent<SVGRectElement>,
  ): (Hover & { id: string }) | null => {
    const svg = evt.currentTarget.ownerSVGElement;
    const ctm = svg && svg.getScreenCTM();
    if (!svg || !ctm) return null;
    const pt = svg.createSVGPoint();
    pt.x = evt.clientX;
    pt.y = evt.clientY;
    const loc = pt.matrixTransform(ctm.inverse());
    let best: (Hover & { id: string }) | null = null;
    let bestD2 = HIT * HIT;
    for (const e of elections) {
      const pts = lineData.get(e.id);
      if (!pts) continue;
      for (const p of pts) {
        if (p.d < lo || p.d > hi) continue;
        const cx = X(p.d);
        const cy = Y(p.p);
        const dx = cx - loc.x;
        const dy = cy - loc.y;
        const d2 = dx * dx + dy * dy;
        if (d2 < bestD2) {
          bestD2 = d2;
          best = { id: e.id, name: e.id, d: p.d, p: p.p, cx, cy };
        }
      }
    }
    return best;
  };

  return (
    <g>
      <rect
        x={plot.x}
        y={plot.y}
        width={plot.width}
        height={plot.height}
        fill="transparent"
        style={{ cursor: "crosshair" }}
        onMouseMove={(e) => {
          const n = nearest(e);
          if (n) onHover(n);
          else onLeave();
        }}
        onMouseLeave={onLeave}
        onClick={(e) => {
          const n = nearest(e);
          if (n) onPick(n.id);
        }}
      />
      {hover && (
        <circle
          cx={hover.cx}
          cy={hover.cy}
          r={4}
          fill="var(--lc-rust)"
          stroke={theme.paper}
          strokeWidth={1.5}
          pointerEvents="none"
        />
      )}
    </g>
  );
}

export default function TrajectoryExplorer({
  elections,
  selected,
  toggleSelected,
  clearSelected,
  dayFrom,
  dayTo,
  setDayRange,
}: {
  elections: Election[];
  selected: Set<string>;
  toggleSelected: (id: string) => void;
  clearSelected: () => void;
  dayFrom: number;
  dayTo: number;
  setDayRange: (lo: number, hi: number) => void;
}) {
  const theme = useChartTheme();
  const [hover, setHover] = useState<Hover | null>(null);
  const clearHover = useCallback(() => setHover(null), []);

  const lineData = useMemo(
    () =>
      new Map<string, DP[]>(
        elections.map((e) => [e.id, e.pts.map(([d, p]) => ({ d, p }))]),
      ),
    [elections],
  );
  // the slider spans the full data; clamp the saved window into that range
  const dataMax = useMemo(
    () =>
      Math.max(
        10,
        Math.ceil(elections.reduce((m, e) => Math.max(m, maxDay(e)), 0)),
      ),
    [elections],
  );
  const hi = Math.min(Math.max(1, dayTo), dataMax);
  const lo = Math.max(0, Math.min(dayFrom, hi - 1));
  const beyond = useMemo(
    () => elections.filter((e) => maxDay(e) > hi).length,
    [elections, hi],
  );
  const sels = useMemo(
    () => elections.filter((e) => selected.has(e.id)),
    [elections, selected],
  );

  // recharts needs *some* data to lay out the axes now that there are no series;
  // a 2-point anchor at the domain corners is enough (explicit domains win).
  const anchor = useMemo(
    () => [
      { d: lo, p: 0 },
      { d: hi, p: 102 },
    ],
    [lo, hi],
  );

  return (
    <div>
      {selected.size > 0 && (
        <div className="mb-4 flex flex-wrap items-center gap-1.5">
          <button
            onClick={clearSelected}
            className="smallcaps border border-rule px-1.5 py-0.5 text-[11px] text-faint transition-colors hover:border-rust hover:text-rust"
          >
            clear {selected.size} ✕
          </button>
        </div>
      )}

      <div className="grid gap-5 lg:grid-cols-[1fr_290px]">
        <div>
          <DayRangeSlider
            lo={lo}
            hi={hi}
            max={dataMax}
            onChange={setDayRange}
          />
          <ChartFrame
            title="The count, release by release"
            subtitle="Each election's share of its certified final, over days since election night"
            note={
              <>
                Each line is one election’s count: % of the certified final, by
                days since the 8 PM poll close. Drag the dual handles above to
                zoom the day window — it opens on 0–{10} days, where most of the
                movement is; pull the right handle out toward {dataMax} days to
                follow the long mail-cure tail.
                {beyond > 0 && (
                  <>
                    {" "}
                    The <span className="stat-figure">--/ /--</span> break marks{" "}
                    {beyond} election{beyond === 1 ? "" : "s"} still running
                    past day {hi}.
                  </>
                )}{" "}
                Click a line to highlight one or more elections for comparison;
                dashed lines with markers are archival recoveries.
              </>
            }
          >
            <div className="relative">
              {hover && (
                <div
                  className="pointer-events-none absolute z-10 border border-ink bg-paper px-3 py-2 text-sm shadow"
                  style={{
                    left: hover.cx,
                    top: hover.cy - 14,
                    transform: "translate(-50%, -100%)",
                    maxWidth: 220,
                  }}
                >
                  <div className="font-semibold">{hover.name}</div>
                  <div className="stat-figure">
                    day {hover.d}: {hover.p}% counted
                  </div>
                </div>
              )}
              <ResponsiveContainer width="100%" height={420}>
                <ComposedChart
                  data={anchor}
                  margin={{ top: 12, right: 24, bottom: 8, left: 0 }}
                >
                  <CartesianGrid stroke={theme.rule} strokeDasharray="2 4" />
                  <XAxis
                    type="number"
                    dataKey="d"
                    domain={[lo, hi]}
                    allowDataOverflow
                    ticks={dayTicks(lo, hi)}
                    tick={{
                      fontFamily: theme.fontMono,
                      fontSize: 11,
                      fill: theme.faint,
                    }}
                    stroke={theme.faint}
                    tickLine={false}
                    label={{
                      value: "DAYS SINCE POLLS CLOSED",
                      position: "insideBottom",
                      offset: -4,
                      style: {
                        fontFamily: theme.fontMono,
                        fontSize: 10,
                        fill: theme.faint,
                        letterSpacing: "0.1em",
                      },
                    }}
                  />
                  <YAxis
                    type="number"
                    dataKey="p"
                    domain={[0, 102]}
                    ticks={[0, 25, 50, 75, 90, 100]}
                    tickFormatter={(v: number) => `${v}%`}
                    tick={{
                      fontFamily: theme.fontMono,
                      fontSize: 11,
                      fill: theme.faint,
                    }}
                    stroke={theme.faint}
                    tickLine={false}
                    width={44}
                  />
                  <ReferenceLine
                    y={90}
                    stroke="var(--lc-rust)"
                    strokeWidth={1}
                    label={{
                      value: "90%",
                      position: "right",
                      style: {
                        fontFamily: theme.fontMono,
                        fontSize: 10,
                        fill: "var(--lc-rust)",
                      },
                    }}
                  />
                  <TrajLines
                    elections={elections}
                    lineData={lineData}
                    selected={selected}
                    lo={lo}
                    hi={hi}
                  />
                  <TrajHover
                    elections={elections}
                    lineData={lineData}
                    lo={lo}
                    hi={hi}
                    hover={hover}
                    onHover={setHover}
                    onLeave={clearHover}
                    onPick={toggleSelected}
                  />
                  <AxisBreak side="left" show={lo > 0} />
                  <AxisBreak
                    side="right"
                    show={beyond > 0}
                    label={`${beyond} past ${hi}d →`}
                  />
                </ComposedChart>
              </ResponsiveContainer>
            </div>
          </ChartFrame>
        </div>

        <div>
          {sels.length ? (
            <div className="space-y-4">
              {sels.map((e) => (
                <DetailPanel key={e.id} e={e} />
              ))}
            </div>
          ) : (
            <div className="border border-dashed border-rule p-4 text-sm italic leading-relaxed text-faint">
              Select one or more elections above to see their canvass details:
              final count, night share, mail share, and days to each threshold.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
