"use client";
import { useMemo } from "react";
import {
  CartesianGrid,
  ComposedChart,
  Line,
  ResponsiveContainer,
  Scatter,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import {
  Election,
  Fit,
  KIND_COLOR,
  linearFit,
  yearFrac,
} from "@/lib/data";
import { ChartFrame, FitBadge } from "@/components/ui";

type Pt = {
  x: number;
  y: number;
  id: string;
  name: string;
  kind: string;
  source: string;
};

function NightTooltip({
  active,
  payload,
}: {
  active?: boolean;
  payload?: { payload: Pt }[];
}) {
  if (!active || !payload?.length) return null;
  const p = payload[0].payload;
  if (p.id === undefined) return null;
  return (
    <div className="border border-ink bg-paper px-3 py-2 text-sm shadow">
      <div className="smallcaps" style={{ color: KIND_COLOR[p.kind] }}>
        {p.kind}
        {p.source === "archival" ? " · archival" : ""}
      </div>
      <div className="font-semibold">{p.id}</div>
      <div className="stat-figure">{p.y}% counted by election night</div>
    </div>
  );
}

export default function NightShareChart({
  elections,
}: {
  elections: Election[];
}) {
  const { pts, fit } = useMemo(() => {
    const pts: Pt[] = elections
      .filter((e) => e.nightPct !== null && !e.provisional)
      .map((e) => ({
        x: yearFrac(e.id),
        y: e.nightPct as number,
        id: e.id,
        name: e.name,
        kind: e.kind,
        source: e.source,
      }));
    const fit: Fit | null = linearFit(pts.map((p) => [p.x, p.y]));
    return { pts, fit };
  }, [elections]);

  const trend =
    fit && [
      { x: fit.x0, y: fit.intercept + fit.slope * fit.x0 },
      { x: fit.x1, y: fit.intercept + fit.slope * fit.x1 },
    ];

  return (
    <div>
      <FitBadge fit={fit} unit="pts/yr" />
      <ChartFrame
        note={
          <>
            Share of the certified final count already reported by the end of
            election night. Hollow points are web-archive recoveries
            (2002–2014); 2020–21 ran high because pandemic-era mail ballots
            arrived weeks early. Ongoing counts are excluded.
          </>
        }
      >
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
              domain={[30, 100]}
              ticks={[30, 40, 50, 60, 70, 80, 90, 100]}
              tickFormatter={(v: number) => `${v}%`}
              tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
              stroke="var(--color-faint)"
              tickLine={false}
              width={48}
            />
            <Tooltip content={<NightTooltip />} isAnimationActive={false} />
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
                return payload.source === "archival" ? (
                  <circle cx={cx} cy={cy} r={5.5} fill="var(--color-paper)" stroke={c} strokeWidth={2} />
                ) : (
                  <circle cx={cx} cy={cy} r={5.5} fill={c} />
                );
              }}
            />
          </ComposedChart>
        </ResponsiveContainer>
      </ChartFrame>
    </div>
  );
}
