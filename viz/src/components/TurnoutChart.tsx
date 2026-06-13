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
import { TURNOUT_HISTORY, KIND_COLOR, KINDS, fmt } from "@/lib/data";
import { ChartFrame } from "@/components/ui";

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
const MILESTONES = [2002.0, 2020.84, 2022.0];

export default function TurnoutChart() {
  return (
    <ChartFrame
      note={
        <>
          <span className="smallcaps not-italic" style={{ color: "var(--color-gold)" }}>
            gold lines:
          </span>{" "}
          2002 permanent vote-by-mail list · Nov 2020 every voter mailed a
          ballot (AB 860) · 2022 made permanent (AB 37).
          <br />
          Turnout — ballots cast as a share of <em>registered</em> voters —
          by election type, 1899–2026. Each color is one type of election
          ({KINDS.join(", ").toLowerCase()}); presidential generals sit at the
          top, primaries and off-year municipals below. The vertical swings
          are the ballot, not the mail: turnout follows what’s being decided,
          and the all-mail era (right of the gold lines) did not lift it out
          of its historical band. This is turnout of the <em>registered</em>
          electorate; whether mail voting enlarged the registered or eligible
          pool needs a Census denominator the project doesn’t yet carry.
          Sources: the Department of Elections’ official 1899–2019 turnout
          table (from a 2023 web capture) and certified per-release finals
          (2012–present).
        </>
      }
    >
      <ResponsiveContainer width="100%" height={400}>
        <ComposedChart
          data={DATA}
          margin={{ top: 24, right: 20, bottom: 8, left: 0 }}
        >
          <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
          <XAxis
            type="number"
            dataKey="x"
            domain={[1960, 2028]}
            ticks={[1960, 1970, 1980, 1990, 2000, 2010, 2020]}
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
          {MILESTONES.map((x) => (
            <ReferenceLine
              key={x}
              x={x}
              stroke="var(--color-gold)"
              strokeDasharray="4 4"
            />
          ))}
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
