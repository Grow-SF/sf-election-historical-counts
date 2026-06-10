"use client";
import { useMemo, useState } from "react";
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
};

export default function ThresholdExplorer({
  elections,
  threshold,
  setThreshold,
}: {
  elections: Election[];
  threshold: number;
  setThreshold: (t: number) => void;
}) {
  const [hover, setHover] = useState<{ cx: number; cy: number; p: Pt } | null>(null);
  const { pts, fit } = useMemo(() => {
    const pts: Pt[] = [];
    for (const e of elections) {
      const t = e.thresholds[String(threshold)];
      if (!t) continue;
      pts.push({
        x: yearFrac(e.id),
        y: t.days,
        id: e.id,
        kind: e.kind,
        source: e.source,
        bound: t.bound,
        provisional: e.provisional,
      });
    }
    // bounds and ongoing counts can't anchor a regression
    const fit = linearFit(
      pts.filter((p) => !p.bound && !p.provisional).map((p) => [p.x, p.y]),
    );
    return { pts, fit };
  }, [elections, threshold]);

  const trend =
    fit && [
      { x: fit.x0, y: fit.intercept + fit.slope * fit.x0 },
      { x: fit.x1, y: fit.intercept + fit.slope * fit.x1 },
    ];

  const idx = THRESHOLDS.indexOf(threshold);

  return (
    <div>
      <div className="mb-5 flex flex-wrap items-center gap-4 border border-rule bg-paper-deep/60 px-4 py-3">
        <span className="smallcaps text-faint">days until</span>
        <input
          type="range"
          min={0}
          max={THRESHOLDS.length - 1}
          step={1}
          value={idx === -1 ? 6 : idx}
          onChange={(e) => setThreshold(THRESHOLDS[Number(e.target.value)])}
          className="w-44 accent-rust sm:w-64"
          aria-label="threshold percentage of final count"
        />
        <span className="stat-figure text-2xl font-semibold text-rust">
          {threshold}%
        </span>
        <span className="smallcaps text-faint">of the final count</span>
      </div>

      <FitBadge fit={fit} unit="days/yr" flatIsGood />
      <ChartFrame
        note={
          <>
            Days from election day to the first results release at or above the
            chosen share of the certified final. Hollow triangles are archival
            upper bounds (“crossed by day N at the latest”) and are excluded
            from the fit, as are ongoing counts. Drag the slider — at every
            threshold, the fitted line stays nearly flat.
          </>
        }
      >
        <div className="relative">
          {hover && (
            <PointTooltip cx={hover.cx} cy={hover.cy}>
              <div className="smallcaps" style={{ color: KIND_COLOR[hover.p.kind] }}>
                {hover.p.kind}
                {hover.p.source === "archival" ? " · archival" : ""}
                {hover.p.provisional ? " · count ongoing" : ""}
              </div>
              <div className="font-semibold">{hover.p.id}</div>
              <div className="stat-figure">
                {hover.p.bound ? "≤ " : ""}
                {hover.p.y} day{hover.p.y === 1 ? "" : "s"} to reach {threshold}%
              </div>
              {hover.p.bound && (
                <div className="text-xs italic text-faint">
                  upper bound — crossed by day {hover.p.y} at the latest
                </div>
              )}
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
              domain={[0, 30]}
              ticks={[0, 5, 10, 15, 20, 25, 30]}
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
