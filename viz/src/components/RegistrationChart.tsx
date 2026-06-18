"use client";
import {
  CartesianGrid,
  ComposedChart,
  Line,
  ReferenceArea,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { REGISTRATION_ELIGIBLE, FRANCHISE_FUNNEL, FRANCHISE_EVENTS, fmt, yearTicks } from "@/lib/data";
import { ChartFrame, eventLines } from "@/components/ui";

const MODERN = REGISTRATION_ELIGIBLE.map((p) => {
  const d = new Date(p.date + "T00:00:00");
  return {
    x: d.getFullYear() + d.getMonth() / 12,
    y: p.pct,
    date: p.date,
    eligible: p.eligible,
    registered: p.registered,
    context: p.context,
  };
});

// The SoS Reports of Registration only reach back to the late 1970s. Before
// that, the franchise funnel still carries real per-election registration over
// the census citizen voting-age population, back to 1908 — so derive the early
// registration rate from it to extend the series.
const REG_MIN_YEAR = Math.min(
  ...REGISTRATION_ELIGIBLE.map((p) => Number(p.date.slice(0, 4))),
);
const EARLY = FRANCHISE_FUNNEL.filter(
  (f) => f.year < REG_MIN_YEAR && f.registered && f.eligible,
).map((f) => ({
  x: f.year + 10 / 12, // presidential general ≈ November
  y: Math.round((1000 * f.registered) / f.eligible) / 10,
  date: String(f.year),
  eligible: f.eligible,
  registered: f.registered,
  context: "presidential general · census-derived eligible",
}));

const DATA = [...EARLY, ...MODERN];

type Pt = (typeof DATA)[number];

function RegTooltip({
  active,
  payload,
}: {
  active?: boolean;
  payload?: { payload: Pt }[];
}) {
  if (!active || !payload?.length) return null;
  const p = payload[0].payload;
  return (
    <div className="border border-ink bg-paper px-3 py-2 text-sm shadow">
      <div className="font-semibold">{p.date}</div>
      <div className="smallcaps text-faint">{p.context}</div>
      <div className="stat-figure mt-1">{p.y}% of eligible registered</div>
      <div className="stat-figure text-faint">
        {fmt(p.registered)} of {fmt(p.eligible)} eligible
      </div>
    </div>
  );
}

// gold milestones, matching the mail and turnout charts.
export default function RegistrationChart({ from, to }: { from: number; to: number }) {
  const data = DATA.filter((p) => p.x >= from && p.x <= to + 1);
  const xs = data.map((p) => p.x);
  const lo = xs.length ? Math.floor(Math.min(...xs)) : from;
  const hi = xs.length ? Math.ceil(Math.max(...xs)) : to;
  return (
    <ChartFrame
      title="Registration among eligible citizens"
      subtitle="Registered ÷ citizen voting-age population, 1908–2026"
      note="Registered voters as a share of eligible citizens. The 1990s spike past 100% is pre-“motor-voter” deadwood, since cleaned up. Sources: CA SoS Reports of Registration and Statement of Vote from 1978 (1974–98 pending hand-verification); pre-1978 points are per-election registration over census citizen voting-age population (IPUMS NHGIS), shown at presidential generals."
    >
      <ResponsiveContainer width="100%" height={360}>
        <ComposedChart
          data={data}
          margin={{ top: 24, right: 20, bottom: 8, left: 0 }}
        >
          <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
          {/* the pre-NVRA "deadwood" era: rolls bloated out of sync with
              eligible, registration brushing/exceeding 100% until the 1995
              motor-voter cleanups */}
          <ReferenceArea
            x1={1990}
            x2={2000}
            fill="var(--color-rust)"
            fillOpacity={0.09}
            ifOverflow="hidden"
            label={{
              value: "rolls out of sync (deadwood)",
              position: "insideBottom",
              fontSize: 9,
              fill: "var(--color-faint)",
            }}
          />
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
            domain={[0, 110]}
            ticks={[0, 25, 50, 75, 100]}
            tickFormatter={(v: number) => `${v}%`}
            tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
            stroke="var(--color-faint)"
            tickLine={false}
            width={48}
          />
          <Tooltip content={<RegTooltip />} isAnimationActive={false} />
          {eventLines(lo, hi, FRANCHISE_EVENTS)}
          <Line
            dataKey="y"
            stroke="#056A92"
            strokeWidth={2}
            connectNulls
            dot={{ r: 2.5, fill: "#056A92", strokeWidth: 0 }}
            isAnimationActive={false}
          />
        </ComposedChart>
      </ResponsiveContainer>
    </ChartFrame>
  );
}
