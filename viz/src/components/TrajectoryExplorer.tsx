"use client";
import { useMemo } from "react";
import {
  CartesianGrid,
  ComposedChart,
  Line,
  ReferenceLine,
  ResponsiveContainer,
  Tooltip,
  usePlotArea,
  XAxis,
  YAxis,
} from "recharts";
import { Election, fmt, KIND_COLOR } from "@/lib/data";
import { ChartFrame, DualRange } from "@/components/ui";

const maxDay = (e: Election) => e.pts.reduce((m, [d]) => Math.max(m, d), 0);

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
  const plot = usePlotArea();
  if (!plot || !show) return null;
  const right = side === "right";
  const x = right ? plot.x + plot.width : plot.x;
  const yb = plot.y + plot.height; // x-axis baseline
  const cx = right ? x - 3 : x + 3;
  return (
    <g pointerEvents="none">
      {/* punch a gap in the axis line, then two slashes across it */}
      <rect x={cx - 7} y={yb - 7} width={18} height={14} fill="var(--color-paper)" />
      <path d={`M ${cx - 4} ${yb + 5} L ${cx + 2} ${yb - 5}`} stroke="var(--color-faint)" strokeWidth={1.2} />
      <path d={`M ${cx + 1} ${yb + 5} L ${cx + 7} ${yb - 5}`} stroke="var(--color-faint)" strokeWidth={1.2} />
      {label && (
        <>
          <rect x={x - 96} y={plot.y + 1} width={96} height={14} fill="var(--color-paper)" fillOpacity={0.85} />
          <text
            x={x - 2}
            y={plot.y + 11}
            textAnchor="end"
            style={{ fontFamily: "var(--font-mono)", fontSize: 10, fill: "var(--color-faint)" }}
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
      <p className="smallcaps" style={{ color: KIND_COLOR[e.kind] }}>
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
        {row("to 50% / 80% / 90% / 98%", `${t(50)} / ${t(80)} / ${t(90)} / ${t(98)}`)}
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
  const lineData = useMemo(
    () =>
      new Map(
        elections.map((e) => [e.id, e.pts.map(([d, p]) => ({ d, p }))]),
      ),
    [elections],
  );
  // the slider spans the full data; clamp the saved window into that range
  const dataMax = useMemo(
    () => Math.max(10, Math.ceil(elections.reduce((m, e) => Math.max(m, maxDay(e)), 0))),
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

  return (
    <div>
      <div className="mb-4 flex flex-wrap items-center gap-1.5">
        {elections.map((e) => {
          const on = selected.has(e.id);
          return (
            <button
              key={e.id}
              onClick={() => toggleSelected(e.id)}
              aria-pressed={on}
              className="stat-figure border px-1.5 py-0.5 text-[11px] transition-colors"
              style={{
                borderColor: on ? KIND_COLOR[e.kind] : "var(--color-rule)",
                background: on ? KIND_COLOR[e.kind] : "transparent",
                color: on ? "var(--color-paper)" : "var(--color-ink)",
              }}
              title={`${e.name}${e.source === "archival" ? " (archival)" : ""}`}
            >
              {e.id.slice(0, 7)}
              {e.source === "archival" ? "*" : ""}
            </button>
          );
        })}
        {selected.size > 0 && (
          <button
            onClick={clearSelected}
            className="smallcaps ml-1 border border-rule px-1.5 py-0.5 text-[11px] text-faint transition-colors hover:border-rust hover:text-rust"
          >
            clear {selected.size} ✕
          </button>
        )}
      </div>

      <div className="grid gap-5 lg:grid-cols-[1fr_290px]">
        <div>
          <DayRangeSlider lo={lo} hi={hi} max={dataMax} onChange={setDayRange} />
          <ChartFrame
            title="The count, release by release"
            subtitle="Each election's share of its certified final, over days since election night"
            note={
              <>
                Each line is one election’s count: % of the certified final, by
                days since the 8 PM poll close. Drag the dual handles above to zoom
                the day window — it opens on 0–{10} days, where most of the movement
                is; pull the right handle out toward {dataMax} days to follow the
                long mail-cure tail.
                {beyond > 0 && (
                  <>
                    {" "}The <span className="stat-figure">--/ /--</span> break marks{" "}
                    {beyond} election{beyond === 1 ? "" : "s"} still running past day{" "}
                    {hi}.
                  </>
                )}{" "}
                Click date chips to highlight one or more elections for comparison;
                dashed lines with markers are archival recoveries, and asterisks
                mark archival elections.
              </>
            }
          >
            <ResponsiveContainer width="100%" height={420}>
              <ComposedChart margin={{ top: 12, right: 24, bottom: 8, left: 0 }}>
                <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
                <XAxis
                  type="number"
                  dataKey="d"
                  domain={[lo, hi]}
                  allowDataOverflow
                  ticks={dayTicks(lo, hi)}
                  tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
                  stroke="var(--color-faint)"
                  tickLine={false}
                  label={{
                    value: "DAYS SINCE POLLS CLOSED",
                    position: "insideBottom",
                    offset: -4,
                    style: { fontFamily: "var(--font-mono)", fontSize: 10, fill: "var(--color-faint)", letterSpacing: "0.1em" },
                  }}
                />
                <YAxis
                  type="number"
                  dataKey="p"
                  domain={[0, 102]}
                  ticks={[0, 25, 50, 75, 90, 100]}
                  tickFormatter={(v: number) => `${v}%`}
                  tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
                  stroke="var(--color-faint)"
                  tickLine={false}
                  width={44}
                />
                <ReferenceLine
                  y={90}
                  stroke="var(--color-rust)"
                  strokeWidth={1}
                  label={{
                    value: "90%",
                    position: "right",
                    style: { fontFamily: "var(--font-mono)", fontSize: 10, fill: "var(--color-rust)" },
                  }}
                />
                <Tooltip
                  isAnimationActive={false}
                  content={({ active, payload }) => {
                    if (!active || !payload?.length) return null;
                    const p = payload[0];
                    const d = p.payload as { d: number; p: number };
                    return (
                      <div className="border border-ink bg-paper px-3 py-2 text-sm shadow">
                        <div className="font-semibold">{p.name}</div>
                        <div className="stat-figure">
                          day {d.d}: {d.p}% counted
                        </div>
                      </div>
                    );
                  }}
                />
                {elections.map((e) => {
                  const isSel = selected.has(e.id);
                  const muted = selected.size > 0 && !isSel;
                  const color = isSel ? KIND_COLOR[e.kind] : "var(--color-ink)";
                  return (
                    <Line
                      key={e.id}
                      data={lineData.get(e.id)}
                      dataKey="p"
                      name={e.id}
                      stroke={color}
                      strokeOpacity={isSel ? 1 : muted ? 0.1 : 0.32}
                      strokeWidth={isSel ? 2.5 : 1.2}
                      strokeDasharray={e.source === "archival" ? "5 4" : undefined}
                      dot={
                        e.source === "archival" || isSel
                          ? { r: isSel ? 3 : 2.5, fill: color, fillOpacity: isSel ? 1 : 0.45, strokeWidth: 0 }
                          : false
                      }
                      isAnimationActive={false}
                      onClick={() => toggleSelected(e.id)}
                    />
                  );
                })}
                <AxisBreak side="left" show={lo > 0} />
                <AxisBreak side="right" show={beyond > 0} label={`${beyond} past ${hi}d →`} />
              </ComposedChart>
            </ResponsiveContainer>
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
