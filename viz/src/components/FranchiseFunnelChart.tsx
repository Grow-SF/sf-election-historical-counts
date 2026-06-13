"use client";
import {
  Area,
  AreaChart,
  CartesianGrid,
  ReferenceLine,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { FRANCHISE_FUNNEL, fmt } from "@/lib/data";
import { ChartFrame } from "@/components/ui";

// Mutually-exclusive bands that sum to total population, bottom (voted) to top
// (children). The thickness of each band over time is the story.
const BANDS = [
  { key: "voted", label: "voted", color: "#5E2B24" },
  { key: "regNotVoted", label: "registered, didn't vote", color: "#A4492C" },
  { key: "notRegistered", label: "eligible, not registered", color: "#B98F33" },
  { key: "nonCitizen", label: "non-citizen adults (immigrants)", color: "#3E5C76" },
  { key: "children", label: "under voting age", color: "#CABB9B" },
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

export default function FranchiseFunnelChart() {
  return (
    <ChartFrame
      title="Who could vote — and who did"
      subtitle="San Francisco by presidential election, 1908–2024"
      note={
        <>
          <span className="smallcaps not-italic" style={{ color: "var(--color-gold)" }}>
            gold line:
          </span>{" "}
          1920 — the 19th Amendment (California had enfranchised women in 1911).
          <br />
          San Francisco’s electorate, presidential elections 1908–2024, as bands
          of the whole population: who voted, who was registered but stayed home,
          who was eligible but unregistered, the{" "}
          <em>non-citizen adults who couldn’t vote at all</em>, and children. Two
          things jump out. Women’s suffrage (1920) nearly doubles the eligible
          band. And the blue non-citizen band — wide in the Gold-Rush-era
          immigrant city, squeezed thin by the mid-century immigration pause,
          then swelling again after 1965 as Latin American and Asian migration
          resumed — is the franchise quietly shrinking against a growing city.
          Sources: total population, voting-age population, and citizenship from
          IPUMS NHGIS (decennial census, interpolated to election years);
          registration and ballots cast from the franchise series (SoS + the
          Department of Elections).
        </>
      }
    >
      <ResponsiveContainer width="100%" height={440}>
        <AreaChart data={DATA} margin={{ top: 24, right: 20, bottom: 8, left: 8 }}>
          <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
          <XAxis
            dataKey="year"
            type="number"
            domain={[1905, 2027]}
            ticks={[1920, 1940, 1960, 1980, 2000, 2020]}
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
          <ReferenceLine x={1920} stroke="var(--color-gold)" strokeDasharray="4 4" />
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
