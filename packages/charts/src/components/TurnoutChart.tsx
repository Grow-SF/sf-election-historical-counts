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
import { TURNOUT_HISTORY } from "@long-count/data";
import { KINDS, displayKind } from "../lib/categories";
import { fmt } from "../lib/format";
import { yearTicks } from "../lib/events";
import { useChartTheme } from "../theme";
import { ChartFrame, eventLines } from "./ui";

type TPoint = {
  x: number;
  date: string;
  kind: string;
  turnoutPct: number | null;
  ballots: number;
  registered: number;
};

// Consecutive elections of the same series more than this many years apart get a
// null breakpoint between them, so the line doesn't bridge decades-long gaps
// (e.g. the one special in 1903 to the next in 1977). The regular cadence of
// generals/primaries/municipals is ≤4 years, so it stays connected — except the
// Midterm line, which breaks across the missing 1958–1970 midterm turnout.
const MAX_GAP_YEARS = 8;

// One gap-aware series per display category. "General" splits into presidential
// (year % 4 == 0, ~80–90% turnout) and "Midterm" (the even off-years, ~60–70%)
// via displayKind: lumped together they make one line zigzag between the two
// cadences, which hides that the smooth 1956–1972 stretch is presidential years
// alone — the midterm turnout for 1958/62/66/70 is missing from the source.
const SERIES: Record<string, TPoint[]> = {};
for (const k of KINDS) {
  const pts: TPoint[] = TURNOUT_HISTORY.filter(
    (p) => displayKind(p.kind, Number(p.date.slice(0, 4))) === k,
  )
    .map((p) => {
      const d = new Date(p.date + "T00:00:00");
      return {
        x: d.getFullYear() + d.getMonth() / 12,
        date: p.date,
        kind: k,
        turnoutPct: p.turnoutPct as number | null,
        ballots: p.ballots,
        registered: p.registered,
      };
    })
    .sort((a, b) => a.x - b.x);
  const out: TPoint[] = [];
  pts.forEach((p, i) => {
    if (i > 0 && p.x - pts[i - 1].x > MAX_GAP_YEARS) {
      out.push({
        x: (p.x + pts[i - 1].x) / 2,
        date: "",
        kind: k,
        turnoutPct: null,
        ballots: 0,
        registered: 0,
      });
    }
    out.push(p);
  });
  SERIES[k] = out;
}

function TurnoutTooltip({
  active,
  payload,
}: {
  active?: boolean;
  payload?: { payload: TPoint }[];
}) {
  const theme = useChartTheme();
  if (!active || !payload?.length) return null;
  const p = payload[0].payload;
  if (p.turnoutPct == null || !p.date) return null;
  return (
    <div className="border border-ink bg-paper px-3 py-2 text-sm shadow">
      <div className="font-semibold">{p.date}</div>
      <div className="smallcaps" style={{ color: theme.colorsByKind[p.kind] }}>
        {p.kind}
      </div>
      <div className="stat-figure mt-1">
        {p.turnoutPct}% of registered voted
      </div>
      <div className="stat-figure text-faint">
        {fmt(p.ballots)} / {fmt(p.registered)} registered
      </div>
    </div>
  );
}

// gold milestones, matching the mail chart: permanent VBM list (2002),
// every-voter mailing (Nov 2020, AB 860), made permanent (2022, AB 37).
export default function TurnoutChart({
  from,
  to,
  kinds,
}: {
  from: number;
  to: number;
  kinds: Set<string>;
}) {
  const theme = useChartTheme();
  // respect the filter bar: only plot the categories that are switched on
  const shown = KINDS.filter((k) => kinds.has(k));
  const inRange = (p: TPoint) => p.x >= from && p.x <= to + 1;
  const visible: Record<string, TPoint[]> = {};
  for (const k of shown) visible[k] = SERIES[k].filter(inRange);
  const xs = shown.flatMap((k) =>
    visible[k].filter((p) => p.turnoutPct != null).map((p) => p.x),
  );
  const lo = xs.length ? Math.floor(Math.min(...xs)) : from;
  const hi = xs.length ? Math.ceil(Math.max(...xs)) : to;
  return (
    <ChartFrame
      title="Turnout of registered voters"
      subtitle="Ballots cast ÷ registered, by election type, 1879–2026"
      note="Color = election type; generals split into presidential years (General, ~80–90%) and the even off-years (Midterm, ~60–70%) — lumped together they zigzag between the two cadences. Lines break across multi-decade gaps; the Midterm line breaks over the missing 1958–1970 turnout. Use the filter to add or remove types. Sources: SF Municipal Reports Registrar table (1879–1890); DOE turnout table; certified per-release finals."
    >
      <ResponsiveContainer width="100%" height={400}>
        <ComposedChart margin={{ top: 24, right: 20, bottom: 8, left: 0 }}>
          <CartesianGrid stroke={theme.rule} strokeDasharray="2 4" />
          <XAxis
            type="number"
            dataKey="x"
            domain={[lo, hi]}
            ticks={yearTicks(lo, hi)}
            tickFormatter={(v: number) => String(v)}
            tick={{
              fontFamily: theme.fontMono,
              fontSize: 11,
              fill: theme.faint,
            }}
            stroke={theme.faint}
            tickLine={false}
            allowDataOverflow
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
          <Tooltip content={<TurnoutTooltip />} isAnimationActive={false} />
          {eventLines(lo, hi, theme.gold, theme.faint)}
          {shown.map((k) => (
            <Line
              key={k}
              data={visible[k]}
              dataKey="turnoutPct"
              stroke={theme.colorsByKind[k]}
              strokeWidth={1.75}
              connectNulls={false}
              dot={{ r: 2, fill: theme.colorsByKind[k], strokeWidth: 0 }}
              isAnimationActive={false}
            />
          ))}
        </ComposedChart>
      </ResponsiveContainer>
      <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1">
        {shown.map((k) => (
          <span
            key={k}
            className="smallcaps inline-flex items-center gap-1.5 text-faint"
          >
            <span
              className="inline-block h-2 w-3"
              style={{ backgroundColor: theme.colorsByKind[k] }}
            />
            {k}
          </span>
        ))}
      </div>
    </ChartFrame>
  );
}
