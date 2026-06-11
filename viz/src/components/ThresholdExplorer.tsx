"use client";
import { useEffect, useMemo, useState } from "react";
import {
  CartesianGrid,
  ComposedChart,
  Line,
  ResponsiveContainer,
  Scatter,
  XAxis,
  YAxis,
} from "recharts";
import {
  Election,
  KIND_COLOR,
  linearFit,
  NIGHT_FLOOR,
  THRESHOLDS,
  yearFrac,
} from "@/lib/data";
import { ChartFrame, FitBadge, PointTooltip } from "@/components/ui";

type Pt = {
  x: number;
  y: number;
  id: string;
  kind: string;
  source: string;
  bound: boolean;
  provisional: boolean;
  viaFloor: boolean;
  floorPct?: number;
  src?: string | null;
};

export default function ThresholdExplorer({
  elections,
  threshold,
  setThreshold,
  from,
  to,
}: {
  elections: Election[];
  threshold: number;
  setThreshold: (t: number) => void;
  from: number;
  to: number;
}) {
  const [hover, setHover] = useState<{ cx: number; cy: number; p: Pt } | null>(null);
  // a hovered shape that unmounts on filter change never fires onMouseLeave
  useEffect(() => setHover(null), [elections, threshold, from, to]);
  const { pts, fit } = useMemo(() => {
    const floorBy = new Map(NIGHT_FLOOR.map((f) => [f.date, f.floorPct]));
    const byDate = new Map<string, Pt>();
    for (const e of elections) {
      const t = e.thresholds[String(threshold)];
      const fp = floorBy.get(e.id);
      const base = {
        x: yearFrac(e.id),
        id: e.id,
        kind: e.kind,
        source: e.source,
        provisional: e.provisional,
        src: e.srcShort || null,
      };
      if (t && !t.bound) {
        byDate.set(e.id, { ...base, y: t.days, bound: false, viaFloor: false });
      } else if (fp !== undefined && fp >= threshold) {
        // the in-person share alone clears the threshold, so the crossing
        // happened on election night - exact, even without count records
        byDate.set(e.id, { ...base, y: 0, bound: false, viaFloor: true, floorPct: fp });
      } else if (t) {
        byDate.set(e.id, { ...base, y: t.days, bound: true, viaFloor: false });
      }
    }
    // elections with no surviving count data at all, placed at day 0 by the
    // in-person floor (year-filtered only, like the floors in part one)
    for (const f of NIGHT_FLOOR) {
      const y = Number(f.date.slice(0, 4));
      if (byDate.has(f.date) || y < from || y > to || f.floorPct < threshold) continue;
      byDate.set(f.date, {
        x: yearFrac(f.date),
        y: 0,
        id: f.date,
        kind: "",
        source: f.source,
        bound: false,
        provisional: false,
        viaFloor: true,
        floorPct: f.floorPct,
      });
    }
    const pts = [...byDate.values()].sort((a, b) => a.x - b.x);
    // floor-derived day-0 crossings are exact, so they anchor the regression;
    // bounds and ongoing counts can't
    const fit = linearFit(
      pts.filter((p) => !p.bound && !p.provisional).map((p) => [p.x, p.y]),
    );
    return { pts, fit };
  }, [elections, threshold, from, to]);

  const trend =
    fit && [
      { x: fit.x0, y: fit.intercept + fit.slope * fit.x0 },
      { x: fit.x1, y: fit.intercept + fit.slope * fit.x1 },
    ];

  const idx = THRESHOLDS.indexOf(threshold);
  // a leader is mathematically safe once counted-share c leaves fewer
  // uncounted ballots than the margin: settled when c >= 1/(1+M), so the
  // margin a threshold t can settle is (100-t)/t
  const margin = Math.round(((100 - threshold) / threshold) * 100);

  return (
    <div>
      <div className="mb-5 flex flex-wrap items-center gap-4 border border-rule bg-paper-deep/60 px-4 py-3">
        <span className="smallcaps text-faint">days until a race won by</span>
        <span className="stat-figure text-2xl font-semibold text-rust">
          {margin >= 100 ? "any margin" : `${margin}+ pts`}
        </span>
        <span className="smallcaps text-faint">is beyond doubt</span>
        <input
          type="range"
          min={0}
          max={THRESHOLDS.length - 1}
          step={1}
          value={idx === -1 ? 6 : idx}
          onChange={(e) => setThreshold(THRESHOLDS[Number(e.target.value)])}
          className="w-44 accent-rust sm:w-64"
          aria-label="race margin / threshold percentage of final count"
        />
        <span className="smallcaps text-faint">
          = {threshold}% of the final count
        </span>
      </div>

      <FitBadge fit={fit} unit="days/yr" />
      <ChartFrame
        note={
          <>
            <strong>How to read this chart:</strong> A winner is beyond doubt
            once the ballots still uncounted are fewer than the lead. For a
            race won by {margin >= 100 ? "any visible margin" : `${margin} points or more`},
            that happens when {threshold}% of the final total is counted —
            each dot shows how many days that took. Day 0 is election night.
            Grey diamonds are elections with no surviving day-by-day records,
            placed at day 0 because enough of their vote was cast in person
            to clear the line on election night alone. Hollow triangles mean
            &ldquo;crossed by day N at the latest&rdquo;; triangles and
            still-ongoing counts are left out of the trend line. Drag the
            slider to make the race closer or wider.
          </>
        }
      >
        <div className="relative">
          {hover && (
            <PointTooltip cx={hover.cx} cy={hover.cy}>
              <div
                className="smallcaps"
                style={{ color: hover.p.kind ? KIND_COLOR[hover.p.kind] : "var(--color-faint)" }}
              >
                {hover.p.viaFloor
                  ? `${hover.p.kind ? hover.p.kind + " · " : ""}known from the in-person floor`
                  : hover.p.kind}
                {!hover.p.viaFloor && hover.p.source === "archival" ? " · archival" : ""}
                {hover.p.provisional ? " · count ongoing" : ""}
              </div>
              <div className="font-semibold">{hover.p.id}</div>
              <div className="stat-figure">
                {hover.p.bound ? "≤ " : ""}
                {hover.p.y} day{hover.p.y === 1 ? "" : "s"} to reach {threshold}%
                {margin < 100 && (
                  <span className="text-faint"> · settles a {margin}+ pt race</span>
                )}
              </div>
              {hover.p.viaFloor && (
                <div className="max-w-52 text-xs italic text-faint">
                  {hover.p.floorPct}% of this vote was cast in person, and in-person
                  ballots are counted on election night — so the night count was
                  already past {threshold}%.
                </div>
              )}
              {hover.p.bound && (
                <div className="text-xs italic text-faint">
                  upper bound — crossed by day {hover.p.y} at the latest
                </div>
              )}
              {hover.p.viaFloor ? (
                <div className="mt-1 text-[11px] text-faint">
                  source: certified precinct/mail split (DOE / SoS)
                </div>
              ) : hover.p.src ? (
                <div className="mt-1 text-[11px] text-faint">
                  source: {hover.p.src} · full citation on the sources page
                </div>
              ) : null}
            </PointTooltip>
          )}
        <ResponsiveContainer width="100%" height={360}>
          <ComposedChart margin={{ top: 12, right: 20, bottom: 8, left: 0 }}>
            <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
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
              domain={[0, 36]}
              ticks={[0, 5, 10, 15, 20, 25, 30, 35]}
              tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
              stroke="var(--color-faint)"
              tickLine={false}
              width={36}
              label={{
                value: "DAYS",
                angle: -90,
                position: "insideLeft",
                style: { fontFamily: "var(--font-mono)", fontSize: 10, fill: "var(--color-faint)" },
              }}
            />
            {trend && (
              <Line
                data={trend}
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
                  onMouseEnter: () => setHover({ cx, cy, p: payload }),
                  onMouseLeave: () => setHover(null),
                  style: { cursor: "pointer" },
                };
                if (payload.viaFloor) {
                  // same grey diamond as the floors in part one
                  return (
                    <path
                      d={`M ${cx} ${cy - 4.5} L ${cx + 4.5} ${cy} L ${cx} ${cy + 4.5} L ${cx - 4.5} ${cy} Z`}
                      fill="var(--color-paper)"
                      fillOpacity={0.01}
                      stroke="var(--color-faint)"
                      strokeWidth={1.2}
                      opacity={0.75}
                      {...common}
                    />
                  );
                }
                if (payload.bound) {
                  // downward open triangle: the crossing is at or before this day
                  return (
                    <path
                      d={`M ${cx - 6} ${cy - 5} L ${cx + 6} ${cy - 5} L ${cx} ${cy + 5.5} Z`}
                      fill="var(--color-paper)"
                      stroke={c}
                      strokeWidth={1.8}
                      {...common}
                    />
                  );
                }
                if (payload.provisional) {
                  return (
                    <circle cx={cx} cy={cy} r={6} fill="var(--color-paper)" stroke={c} strokeWidth={1.8} strokeDasharray="2 2" {...common} />
                  );
                }
                return <circle cx={cx} cy={cy} r={6.5} fill={c} {...common} />;
              }}
            />
          </ComposedChart>
        </ResponsiveContainer>
        </div>
      </ChartFrame>
    </div>
  );
}
