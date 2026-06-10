"use client";
import { useMemo, useState } from "react";
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
  const [hover, setHover] = useState<
    | { kind: "pt"; cx: number; cy: number; p: Pt }
    | { kind: "floor"; cx: number; cy: number; date: string; y: number }
    | null
  >(null);

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

  // stem between an election's actual night share and its floor: the gap is
  // the share of mail that arrived early enough to make the night count
  const stems = useMemo(() => {
    const floorBy = new Map(NIGHT_FLOOR.map((p) => [p.date, p.floorPct]));
    return pts
      .filter((p) => floorBy.has(p.id))
      .map((p) => ({ x: p.x, y0: floorBy.get(p.id) as number, y1: p.y }));
  }, [pts]);

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
            <strong>How to read this chart:</strong> Each colored dot shows how
            much of an election’s final vote was already counted by the end of
            election night. (Hollow dots were recovered from old web archives.)
            Each grey diamond shows how much of that election’s vote was cast
            in person at the polls. In-person votes always get counted on
            election night, so a dot can never be lower than its diamond. The
            dotted stem between them is mail that arrived early — early mail
            gets counted on election night too. In 1964 almost everyone voted
            in person, so election night showed 94% of the vote. Today most
            people vote by mail, and mail that arrives late simply can’t be
            counted that night. 2020–21 look high because people mailed their
            ballots weeks early during the pandemic. Elections still being
            counted are left out. The dashed trend line is fitted to the
            colored dots only.
          </>
        }
      >
        <div className="relative">
          {hover?.kind === "pt" && (
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
          {hover?.kind === "floor" && (
            <PointTooltip cx={hover.cx} cy={hover.cy}>
              <div className="smallcaps text-faint">election-night floor</div>
              <div className="font-semibold">{hover.date}</div>
              <div className="stat-figure">{hover.y}% voted in person</div>
              <div className="text-xs italic text-faint">
                in-person votes are counted on election night, so that night
                showed at least this much
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
                      setHover({ kind: "floor", cx, cy, date: payload.date, y: payload.y })
                    }
                    onMouseLeave={() => setHover(null)}
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
                    onMouseEnter: () => setHover({ kind: "pt" as const, cx, cy, p: payload }),
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
