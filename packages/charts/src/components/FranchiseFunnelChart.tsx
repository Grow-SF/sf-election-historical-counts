"use client";
import { useState } from "react";
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
import { FRANCHISE_FUNNEL } from "../../../data/index";
import { FRANCHISE_EVENTS, EVENTS, yearTicks } from "../lib/events";
import { fmt } from "../lib/format";
import { useChartTheme } from "../theme";
import { ChartFrame, eventLines, noDataGuides } from "./ui";

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
  {
    key: "nonCitizen",
    label: "non-citizen adults (immigrants)",
    color: "#4BADE4", // brand-blue-3 (softer than blue-6, still clearly the "blue band")
  },
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

// the data's extent — the franchise funnel runs ~1908–2024
const COVER_MIN = Math.min(...DATA.map((r) => r.year));
const COVER_MAX = Math.max(...DATA.map((r) => r.year));

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
      <div className="stat-figure text-faint">
        population {fmt(p.population)}
      </div>
      <div className="stat-figure mt-1">
        eligible citizens {fmt(p.eligible)}
      </div>
      <div className="stat-figure">
        registered {fmt(p.registered)} · {pct(p.registered)} of eligible
      </div>
      <div className="stat-figure">
        voted {fmt(p.voted)} · {pct(p.voted)} of eligible
      </div>
      <div className="stat-figure text-faint mt-1">
        non-citizen adults {fmt(p.nonCitizen)}
      </div>
    </div>
  );
}

export default function FranchiseFunnelChart({
  from,
  to,
}: {
  from: number;
  to: number;
}) {
  const theme = useChartTheme();
  // "counts" stacks the absolute bands (height grows with population); "share"
  // normalizes the stack to 100% so each band reads as a fraction of the total.
  const [mode, setMode] = useState<"counts" | "share">("counts");
  // in % mode, optionally restrict to the eligible-citizen bands (dropping
  // children and non-citizen adults) so they renormalize to 100% of the
  // eligible population
  const [eligibleOnly, setEligibleOnly] = useState(false);
  const data = DATA.filter((r) => r.year >= from && r.year <= to);
  const shownBands =
    mode === "share" && eligibleOnly
      ? BANDS.filter((b) => b.key !== "children" && b.key !== "nonCitizen")
      : BANDS;
  return (
    <ChartFrame
      title="Who could vote — and who did"
      subtitle="San Francisco by presidential election, 1908–2024"
      note="Bands are the five groups that make up the total population; the blue band is non-citizen adults. Switch to “% of population” to read each band as a share of the whole — the chart fills to 100% so the proportions stay comparable as the city grows. The shaded 1990s “deadwood” box marks the years when bloated registration rolls pushed registration up to (or past) the eligible estimate — so the “eligible, not registered” band nearly disappears — until the 1995 motor-voter law forced the cleanup. Sources: IPUMS NHGIS census (population, voting-age, citizenship); SoS and Dept. of Elections."
    >
      <div className="smallcaps mb-2 flex items-center gap-1.5 text-faint">
        <span className="mr-1">show</span>
        {(
          [
            ["counts", "counts"],
            ["share", "% of population"],
          ] as const
        ).map(([m, label]) => (
          <button
            key={m}
            onClick={() => setMode(m)}
            aria-pressed={mode === m}
            className="smallcaps border px-2 py-0.5"
            style={{
              borderColor: mode === m ? theme.ink : theme.rule,
              background: mode === m ? theme.ink : "transparent",
              color: mode === m ? theme.paper : theme.faint,
            }}
          >
            {label}
          </button>
        ))}
        {mode === "share" && (
          <label className="ml-3 flex cursor-pointer items-center gap-1.5">
            <input
              type="checkbox"
              checked={eligibleOnly}
              onChange={(e) => setEligibleOnly(e.target.checked)}
              style={{ accentColor: theme.ink }}
            />
            eligible citizens only
          </label>
        )}
      </div>
      <ResponsiveContainer width="100%" height={440}>
        <AreaChart
          data={data}
          stackOffset={mode === "share" ? "expand" : "none"}
          margin={{ top: 40, right: 20, bottom: 8, left: 8 }}
        >
          <CartesianGrid stroke={theme.rule} strokeDasharray="2 4" />
          {noDataGuides(from, to, COVER_MIN, COVER_MAX, theme.faint)}
          <XAxis
            dataKey="year"
            type="number"
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
            ticks={mode === "share" ? [0, 0.25, 0.5, 0.75, 1] : undefined}
            tickFormatter={
              mode === "share"
                ? (v: number) => `${Math.round(v * 100)}%`
                : (v: number) =>
                    v >= 1_000_000
                      ? `${+(v / 1_000_000).toFixed(1)}M`
                      : `${Math.round(v / 1000)}k`
            }
            tick={{
              fontFamily: theme.fontMono,
              fontSize: 11,
              fill: theme.faint,
            }}
            stroke={theme.faint}
            tickLine={false}
            width={44}
          />
          <Tooltip content={<FunnelTooltip />} isAnimationActive={false} />
          {/* voting-era boundaries on the lower label row, franchise milestones
              on a higher row so the two label sets don't collide */}
          {eventLines(from, to, theme.gold, theme.faint, EVENTS)}
          {eventLines(from, to, theme.gold, theme.faint, FRANCHISE_EVENTS, 20)}
          {shownBands.map((b) => (
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
              fill={theme.ink}
              fillOpacity={0.07}
              stroke={theme.ink}
              strokeOpacity={0.35}
              strokeDasharray="3 3"
              label={{
                value: "deadwood rolls",
                position: "insideTop",
                fontSize: 9,
                fill: theme.ink,
              }}
            />
          )}
        </AreaChart>
      </ResponsiveContainer>
      <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1">
        {[...shownBands].reverse().map((b) => (
          <span
            key={b.key}
            className="smallcaps inline-flex items-center gap-1.5 text-faint"
          >
            <span
              className="inline-block h-2 w-3"
              style={{ backgroundColor: b.color }}
            />
            {b.label}
          </span>
        ))}
      </div>
    </ChartFrame>
  );
}
