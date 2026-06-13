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
import { VBM_HISTORY, yearTicks } from "@/lib/data";
import { ChartFrame, eventLines } from "@/components/ui";

const RAW = VBM_HISTORY.map((p) => {
  const d = new Date(p.date + "T00:00:00");
  return {
    x: d.getFullYear() + d.getMonth() / 12,
    y: p.share as number | null,
    date: p.date,
    source: p.source,
  };
});

// break the line where sources leave a multi-year gap (2002-2008)
const DATA: typeof RAW = [];
RAW.forEach((p, i) => {
  if (i > 0 && p.x - RAW[i - 1].x > 4) {
    DATA.push({ x: (p.x + RAW[i - 1].x) / 2, y: null, date: "", source: "gap" });
  }
  DATA.push(p);
});

type Pt = (typeof DATA)[number];

function VbmTooltip({
  active,
  payload,
}: {
  active?: boolean;
  payload?: { payload: Pt }[];
}) {
  if (!active || !payload?.length) return null;
  const p = payload[0].payload;
  if (!p.date) return null;
  return (
    <div className="border border-ink bg-paper px-3 py-2 text-sm shadow">
      <div className="font-semibold">{p.date}</div>
      <div className="stat-figure">{p.y}% of ballots cast by mail</div>
    </div>
  );
}

export default function VbmChart({ from, to }: { from: number; to: number }) {
  const data = DATA.filter((p) => p.x >= from && p.x <= to + 1);
  const xs = data.map((p) => p.x);
  const lo = xs.length ? Math.floor(Math.min(...xs)) : from;
  const hi = xs.length ? Math.ceil(Math.max(...xs)) : to;
  return (
    <ChartFrame
      title="Vote-by-mail share of ballots cast"
      subtitle="San Francisco, 1964–2026"
      note="Mail ballots as a share of all ballots cast. Sources: DOE turnout history, certified Statements of Vote, per-release results."
    >
      <ResponsiveContainer width="100%" height={380}>
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
          <Tooltip content={<VbmTooltip />} isAnimationActive={false} />
          {eventLines(lo, hi)}
          <Line
            dataKey="y"
            stroke="var(--color-rust)"
            strokeWidth={2}
            connectNulls={false}
            dot={{ r: 2.5, fill: "var(--color-rust)", strokeWidth: 0 }}
            isAnimationActive={false}
          />
        </ComposedChart>
      </ResponsiveContainer>
    </ChartFrame>
  );
}
