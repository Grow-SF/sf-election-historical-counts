"use client";
import {
  CartesianGrid,
  ComposedChart,
  Line,
  ReferenceLine,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { VBM_HISTORY } from "@/lib/data";
import { ChartFrame } from "@/components/ui";

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

const MILESTONES = [2002.0, 2020.84, 2022.0];

export default function VbmChart() {
  return (
    <ChartFrame
      note={
        <>
          <span className="smallcaps not-italic" style={{ color: "var(--color-gold)" }}>
            gold lines, left to right:
          </span>{" "}
          2002 — permanent vote-by-mail list opens · Nov 2020 — AB 860 mails
          every voter a ballot · 2022 — AB 37 makes it permanent.
          <br />
          Mail (absentee) ballots as a share of all ballots cast, 1964–2026.
          Sources: the Department of Elections’ turnout history (1964–2000,
          recovered from a 2002 web capture), certified Statements of Vote
          (2002–2014: CA Secretary of State county statistics and the DOE’s
          own SOV spreadsheets), the DOE’s official historical turnout table
          (municipal elections 2001–2013 and Nov 2019, from a 2023 web
          capture), and per-release results data (2015–present).
        </>
      }
    >
      <ResponsiveContainer width="100%" height={380}>
        <ComposedChart
          data={DATA}
          margin={{ top: 24, right: 20, bottom: 8, left: 0 }}
        >
          <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
          <XAxis
            type="number"
            dataKey="x"
            domain={[1962, 2028]}
            ticks={[1970, 1980, 1990, 2000, 2010, 2020]}
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
          {MILESTONES.map((x) => (
            <ReferenceLine
              key={x}
              x={x}
              stroke="var(--color-gold)"
              strokeDasharray="4 4"
            />
          ))}
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
