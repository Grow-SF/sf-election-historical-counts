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
import { VBM_HISTORY } from "../../../data/index";
import { yearTicks } from "../lib/events";
import { useChartTheme } from "../theme";
import { ChartFrame, eventLines, noDataGuides } from "./ui";

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
    DATA.push({
      x: (p.x + RAW[i - 1].x) / 2,
      y: null,
      date: "",
      source: "gap",
    });
  }
  DATA.push(p);
});

// the data's actual extent — for shading the years the slider can reach but the
// VBM history doesn't cover (it starts in 1964)
const COVER_MIN = Math.floor(RAW[0].x);
const COVER_MAX = Math.ceil(RAW[RAW.length - 1].x);

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

export default function VbmChart({
  // the vote-by-mail series has no year filter — it is shown at its own full
  // data extent, so these default to the full coverage
  from = COVER_MIN,
  to = COVER_MAX,
}: {
  from?: number;
  to?: number;
} = {}) {
  const theme = useChartTheme();
  // The x-axis spans the SELECTED [from, to] range so dragging the slider always
  // responds; the line draws only where data exists, and noDataGuides shades the
  // years the data doesn't cover.
  const data = DATA.filter((p) => p.x >= from && p.x <= to + 1);
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
          <CartesianGrid stroke={theme.rule} strokeDasharray="2 4" />
          {noDataGuides(from, to, COVER_MIN, COVER_MAX, theme.faint)}
          <XAxis
            type="number"
            dataKey="x"
            domain={[from, to]}
            ticks={yearTicks(from, to)}
            tickFormatter={(v: number) => String(v)}
            tick={{
              fontFamily: theme.fontMono,
              fontSize: 11,
              fill: theme.faint,
            }}
            stroke={theme.faint}
            tickLine={false}
          />
          <YAxis
            type="number"
            domain={[0, 100]}
            ticks={[0, 25, 50, 75, 100]}
            tickFormatter={(v: number) => `${v}%`}
            tick={{
              fontFamily: theme.fontMono,
              fontSize: 11,
              fill: theme.faint,
            }}
            stroke={theme.faint}
            tickLine={false}
            width={48}
          />
          <Tooltip content={<VbmTooltip />} isAnimationActive={false} />
          {eventLines(from, to, theme.gold, theme.faint)}
          <Line
            dataKey="y"
            stroke="var(--lc-rust)"
            strokeWidth={2}
            connectNulls={false}
            dot={{ r: 2.5, fill: "var(--lc-rust)", strokeWidth: 0 }}
            isAnimationActive={false}
          />
        </ComposedChart>
      </ResponsiveContainer>
    </ChartFrame>
  );
}
