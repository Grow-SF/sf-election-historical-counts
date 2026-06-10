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
import { Election, Fit, KIND_COLOR, linearFit, NIGHT_FLOOR, yearFrac } from "@/lib/data";
import { ChartFrame, FitBadge, PointTooltip } from "@/components/ui";

type Pt = {
  x: number;
  y: number;
  id: string;
  name: string;
  kind: string;
  source: string;
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
  const [hover, setHover] = useState<{ cx: number; cy: number; p: Pt } | null>(null);

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

  const floorPts = useMemo(
    () =>
      NIGHT_FLOOR.filter((p) => {
        const y = Number(p.date.slice(0, 4));
        return y >= from && y <= to;
      }).map((p) => ({ x: yearFrac(p.date), y: p.floorPct, date: p.date })),
    [from, to],
  );

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
            Colored points: share of the certified final already reported by
            the end of election night (hollow = web-archive recoveries; trend
            fit uses these only). Small grey diamonds: the{" "}
            <strong>election-night floor</strong> — the non-absentee share of
            each certified count, 1964–present. Precinct ballots were reported
            on election night, so the night share can never sit below its
            diamond; in 1964 the floor alone was 94%. 2020–21 ran high because
            pandemic-era mail arrived weeks early. Ongoing counts excluded.
          </>
        }
      >
        <div className="relative">
          {hover && (
            <PointTooltip cx={hover.cx} cy={hover.cy}>
              <div className="smallcaps" style={{ color: KIND_COLOR[hover.p.kind] }}>
                {hover.p.kind}
                {hover.p.source === "archival" ? " · archival" : ""}
              </div>
              <div className="font-semibold">{hover.p.id}</div>
              <div className="stat-figure">
                {hover.p.y}% counted by election night
              </div>
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
                domain={[0, 100]}
                ticks={[0, 20, 40, 60, 80, 100]}
                tickFormatter={(v: number) => `${v}%`}
                tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
                stroke="var(--color-faint)"
                tickLine={false}
                width={48}
              />
              <Scatter
              data={floorPts}
              isAnimationActive={false}
              shape={(props: unknown) => {
                const { cx, cy } = props as { cx: number; cy: number };
                return (
                  <path
                    d={`M ${cx} ${cy - 4} L ${cx + 4} ${cy} L ${cx} ${cy + 4} L ${cx - 4} ${cy} Z`}
                    fill="none"
                    stroke="var(--color-faint)"
                    strokeWidth={1.2}
                    opacity={0.75}
                  />
                );
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
                  return payload.source === "archival" ? (
                    <circle cx={cx} cy={cy} r={6.5} fill="var(--color-paper)" stroke={c} strokeWidth={2} {...common} />
                  ) : (
                    <circle cx={cx} cy={cy} r={6.5} fill={c} {...common} />
                  );
                }}
              />
            </ComposedChart>
          </ResponsiveContainer>
        </div>
      </ChartFrame>
    </div>
  );
}
