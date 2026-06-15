"use client";
import {
  Area,
  AreaChart,
  CartesianGrid,
  ReferenceArea,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { FRANCHISE_FUNNEL, fmt, yearTicks } from "@/lib/data";
import { ChartFrame, eventLines } from "@/components/ui";

// Mutually-exclusive bands that sum to total population, bottom (voted) to top
// (children). The thickness of each band over time is the story. Muted GrowSF
// brand tokens (green / soft earth / pale green / blue / grey), ordered so every
// adjacent band differs in hue and/or lightness — keeps the bands distinct for
// colorblind viewers without the saturated look. Non-citizen stays blue (the
// prose names it "the blue band"); "under voting age" is neutral grey.
const BANDS = [
  { key: "voted", label: "voted", color: "#1E7B6A" }, // brand-green-4
  { key: "regNotVoted", label: "registered, didn't vote", color: "#DF7E45" }, // earth-40
  { key: "notRegistered", label: "eligible, not registered", color: "#BCE3B6" }, // green-30
  { key: "nonCitizen", label: "non-citizen adults (immigrants)", color: "#056A92" }, // blue-6
  { key: "children", label: "under voting age", color: "#D2DBDC" }, // gray-2
] as const;

type Row = {
  year: number;
  voted: number;
  regNotVoted: number;
  notRegistered: number;
  nonCitizen: number;
  children: number;
  population: number;
  eligible: number;
  registered: number;
};

const DATA: Row[] = FRANCHISE_FUNNEL.map((p) => ({
  year: p.year,
  voted: p.voted,
  regNotVoted: Math.max(0, p.registered - p.voted),
  notRegistered: Math.max(0, p.eligible - p.registered),
  nonCitizen: Math.max(0, p.vap - p.eligible),
  children: Math.max(0, p.population - p.vap),
  population: p.population,
  eligible: p.eligible,
  registered: p.registered,
}));

function FunnelTooltip({
  active,
  payload,
}: {
  active?: boolean;
  payload?: { payload: Row }[];
}) {
  if (!active || !payload?.length) return null;
  const p = payload[0].payload;
  const pct = (n: number) => `${Math.round((100 * n) / p.eligible)}%`;
  return (
    <div className="border border-ink bg-paper px-3 py-2 text-sm shadow">
      <div className="font-semibold">{p.year}</div>
      <div className="stat-figure text-faint">population {fmt(p.population)}</div>
      <div className="stat-figure mt-1">eligible citizens {fmt(p.eligible)}</div>
      <div className="stat-figure">registered {fmt(p.registered)} · {pct(p.registered)} of eligible</div>
      <div className="stat-figure">voted {fmt(p.voted)} · {pct(p.voted)} of eligible</div>
      <div className="stat-figure text-faint mt-1">
        non-citizen adults {fmt(p.nonCitizen)}
      </div>
    </div>
  );
}

export default function FranchiseFunnelChart({ from, to }: { from: number; to: number }) {
  const data = DATA.filter((r) => r.year >= from && r.year <= to);
  const ys = data.map((r) => r.year);
  const lo = ys.length ? Math.min(...ys) : from;
  const hi = ys.length ? Math.max(...ys) : to;
  return (
    <ChartFrame
      title="Who could vote — and who did"
      subtitle="San Francisco by presidential election, 1908–2024"
      note="Bands are shares of total population and sum to it; the blue band is non-citizen adults. The shaded 1990s “deadwood” box marks the years when bloated registration rolls pushed registration up to (or past) the eligible estimate — so the “eligible, not registered” band nearly disappears — until the 1995 motor-voter law forced the cleanup. Sources: IPUMS NHGIS census (population, voting-age, citizenship); SoS and Dept. of Elections."
    >
      <ResponsiveContainer width="100%" height={440}>
        <AreaChart data={data} margin={{ top: 24, right: 20, bottom: 8, left: 8 }}>
          <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
          <XAxis
            dataKey="year"
            type="number"
            domain={[lo - 2, hi + 2]}
            ticks={yearTicks(lo, hi)}
            tickFormatter={(v: number) => String(v)}
            tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
            stroke="var(--color-faint)"
            tickLine={false}
          />
          <YAxis
            tickFormatter={(v: number) => `${Math.round(v / 1000)}k`}
            tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
            stroke="var(--color-faint)"
            tickLine={false}
            width={44}
          />
          <Tooltip content={<FunnelTooltip />} isAnimationActive={false} />
          {eventLines(lo, hi)}
          {BANDS.map((b) => (
            <Area
              key={b.key}
              dataKey={b.key}
              stackId="pop"
              stroke={b.color}
              strokeWidth={0.5}
              fill={b.color}
              fillOpacity={0.92}
              isAnimationActive={false}
            />
          ))}
          {from <= 2000 && to >= 1990 && (
            // the 1990s "deadwood" era: bloated rolls push registration up to /
            // past the eligible estimate, collapsing the "eligible, not
            // registered" band until the 1995 motor-voter cleanup.
            <ReferenceArea
              x1={1990}
              x2={2000}
              ifOverflow="hidden"
              fill="var(--color-ink)"
              fillOpacity={0.07}
              stroke="var(--color-ink)"
              strokeOpacity={0.35}
              strokeDasharray="3 3"
              label={{
                value: "deadwood rolls",
                position: "insideTop",
                fontSize: 9,
                fill: "var(--color-ink)",
              }}
            />
          )}
        </AreaChart>
      </ResponsiveContainer>
      <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1">
        {[...BANDS].reverse().map((b) => (
          <span key={b.key} className="smallcaps inline-flex items-center gap-1.5 text-faint">
            <span className="inline-block h-2 w-3" style={{ backgroundColor: b.color }} />
            {b.label}
          </span>
        ))}
      </div>
    </ChartFrame>
  );
}
