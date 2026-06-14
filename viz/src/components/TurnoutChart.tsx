"use client";
import {
  CartesianGrid,
  ComposedChart,
  Line,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { TURNOUT_HISTORY, KIND_COLOR, KINDS, fmt, yearTicks } from "@/lib/data";
import { ChartFrame, eventLines } from "@/components/ui";

// one row per election; each kind gets its own y-key so it draws as a
// separate connected line (turnout swings by what's on the ballot, so a
// single line across all types would be noise, not signal).
type Row = {
  x: number;
  date: string;
  kind: string;
  turnoutPct: number;
  ballots: number;
  registered: number;
  [k: string]: number | string;
};

const DATA: Row[] = TURNOUT_HISTORY.map((p) => {
  const d = new Date(p.date + "T00:00:00");
  return {
    x: d.getFullYear() + d.getMonth() / 12,
    date: p.date,
    kind: p.kind,
    turnoutPct: p.turnoutPct,
    ballots: p.ballots,
    registered: p.registered,
    [p.kind]: p.turnoutPct,
  };
});

function TurnoutTooltip({
  active,
  payload,
}: {
  active?: boolean;
  payload?: { payload: Row }[];
}) {
  if (!active || !payload?.length) return null;
  const p = payload[0].payload;
  return (
    <div className="border border-ink bg-paper px-3 py-2 text-sm shadow">
      <div className="font-semibold">{p.date}</div>
      <div className="smallcaps" style={{ color: KIND_COLOR[p.kind] }}>
        {p.kind}
      </div>
      <div className="stat-figure mt-1">{p.turnoutPct}% of registered voted</div>
      <div className="stat-figure text-faint">
        {fmt(p.ballots)} / {fmt(p.registered)} registered
      </div>
    </div>
  );
}

// gold milestones, matching the mail chart: permanent VBM list (2002),
// every-voter mailing (Nov 2020, AB 860), made permanent (2022, AB 37).
export default function TurnoutChart({ from, to }: { from: number; to: number }) {
  const data = DATA.filter((r) => r.x >= from && r.x <= to + 1);
  const xs = data.map((r) => r.x);
  const lo = xs.length ? Math.floor(Math.min(...xs)) : from;
  const hi = xs.length ? Math.ceil(Math.max(...xs)) : to;
  return (
    <ChartFrame
      title="Turnout of registered voters"
      subtitle="Ballots cast ÷ registered, by election type, 1899–2026"
      note="Color = election type; presidential generals top the range, off-year municipals the bottom. Sources: DOE turnout table; certified per-release finals."
    >
      <ResponsiveContainer width="100%" height={400}>
        <ComposedChart
          data={data}
          margin={{ top: 24, right: 20, bottom: 8, left: 0 }}
        >
          <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
          <XAxis
            type="number"
            dataKey="x"
            domain={[lo, hi]}
            ticks={yearTicks(lo, hi)}
            tickFormatter={(v: number) => String(v)}
            tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
            stroke="var(--color-faint)"
            tickLine={false}
            allowDataOverflow
          />
          <YAxis
            type="number"
            domain={[0, 100]}
            ticks={[0, 25, 50, 75, 100]}
            tickFormatter={(v: number) => `${v}%`}
            tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
            stroke="var(--color-faint)"
            tickLine={false}
            width={48}
          />
          <Tooltip content={<TurnoutTooltip />} isAnimationActive={false} />
          {eventLines(lo, hi)}
          {KINDS.map((k) => (
            <Line
              key={k}
              dataKey={k}
              stroke={KIND_COLOR[k]}
              strokeWidth={1.75}
              connectNulls
              dot={{ r: 2, fill: KIND_COLOR[k], strokeWidth: 0 }}
              isAnimationActive={false}
            />
          ))}
        </ComposedChart>
      </ResponsiveContainer>
      <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1">
        {KINDS.map((k) => (
          <span key={k} className="smallcaps inline-flex items-center gap-1.5 text-faint">
            <span
              className="inline-block h-2 w-3"
              style={{ backgroundColor: KIND_COLOR[k] }}
            />
            {k}
          </span>
        ))}
      </div>
    </ChartFrame>
  );
}
