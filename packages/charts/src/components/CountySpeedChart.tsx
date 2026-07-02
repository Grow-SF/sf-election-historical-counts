"use client";
import { useState } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  ComposedChart,
  Line,
  LineChart,
  ReferenceDot,
  ReferenceLine,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { COUNTY_TECH } from "../../../data/index";
import { useChartTheme } from "../theme";
import { ChartFrame } from "./ui";

// ---- shared data prep: one-week reporting rate, CA counties ----
const TECH: Record<string, Record<string, number | null>> = {};
for (const a of COUNTY_TECH.adoptions) {
  if (a.status === "adopted") (TECH[a.jurisdiction] ||= {})[a.tech] = a.adopted_year;
}
const yr = (y: number | null | undefined) => (y ? `’${String(y).slice(2)}` : "");
const techLabel = (j: string) => {
  const t = TECH[j] || {};
  const parts: string[] = [];
  if (t.epollbook) parts.push(`e-pb ${yr(t.epollbook)}`);
  if (t.asv) parts.push(`ASV ${yr(t.asv)}`);
  if (t["sign-scan-go"]) parts.push(`S+S+G ${yr(t["sign-scan-go"])}`);
  return parts.join(" · ") || "neither";
};
const isAdopter = (j: string) => {
  const t = TECH[j] || {};
  return !!(t.epollbook || t.asv || t["sign-scan-go"]);
};
const shortName = (j: string) => j.replace(/ County$/, "");

const OW: Record<string, Record<number, number>> = {};
for (const m of COUNTY_TECH.metrics) {
  if (m.state === "CA" && m.metric === "oneweek_pct" && m.value != null) {
    (OW[m.jurisdiction] ||= {})[m.year] = m.value;
  }
}
const BASE = Object.entries(OW)
  .map(([j, by]) => {
    const y2022 = by[2022] ?? null;
    const y2025 = by[2025] ?? by[2024] ?? null;
    return { jurisdiction: j, short: shortName(j), tech: techLabel(j), adopter: isAdopter(j), y2022, y2025 };
  })
  .filter((c) => c.y2022 != null && c.y2025 != null)
  .map((c) => ({
    ...c,
    change: +((c.y2025 as number) - (c.y2022 as number)).toFixed(1),
    range: [Math.min(c.y2022!, c.y2025!), Math.max(c.y2022!, c.y2025!)] as [number, number],
  }))
  .sort((a, b) => (b.y2025 as number) - (a.y2025 as number));

const BY_CHANGE = [...BASE].sort((a, b) => b.change - a.change);
// numeric-year line data, so adoption-year markers can sit on a real time axis
const TLINE = [2022, 2024, 2025].map((x) => ({
  x,
  ...Object.fromEntries(
    BASE.map((c) => [c.jurisdiction, OW[c.jurisdiction]?.[x] ?? null]),
  ),
}));
const adoptYear = (j: string) => {
  const t = TECH[j] || {};
  return (t.epollbook ?? t["sign-scan-go"] ?? t.asv) || null;
};

const endLabel =
  (short: string, color: string, bold: boolean) =>
  (props: { x?: number | string; y?: number | string; index?: number }) => {
    if (props.index !== TLINE.length - 1) return null;
    return (
      <text
        x={Number(props.x ?? 0) + 6}
        y={Number(props.y ?? 0)}
        dy={3}
        fontSize={bold ? 10 : 8}
        fontFamily="var(--lc-font-mono)"
        fill={color}
        opacity={bold ? 1 : 0.7}
      >
        {short}
      </text>
    );
  };

const VIZ = [
  { key: "arrows", label: "arrows" },
  { key: "change", label: "change" },
  { key: "timeline", label: "timeline" },
] as const;
type Viz = (typeof VIZ)[number]["key"];

function YTick({ x, y, payload, moss, warn }: { x?: number; y?: number; payload?: { value: string }; moss: string; warn: string }) {
  const c = BASE.find((d) => d.jurisdiction === payload?.value);
  if (!c) return <g />;
  return (
    <g transform={`translate(${x},${y})`}>
      <text textAnchor="end" dx={-8} dy={-1} fontSize={12} fontFamily="var(--lc-font-display)" fill="var(--lc-ink)">
        {c.short}
      </text>
      <text textAnchor="end" dx={-8} dy={11} fontSize={9} fontFamily="var(--lc-font-mono)" fill={c.adopter ? moss : warn}>
        {c.tech}
      </text>
    </g>
  );
}

export default function CountySpeedChart() {
  const theme = useChartTheme();
  const [viz, setViz] = useState<Viz>("timeline");
  const moss = theme.colorsByKind.Special;
  const warn = theme.colorsByKind.Recall;
  const height = BASE.length * 40 + 64;
  const tick = <YTick moss={moss} warn={warn} />;
  const yAxis = (
    <YAxis type="category" dataKey="jurisdiction" width={188} interval={0} tick={tick} stroke={theme.faint} tickLine={false} />
  );
  const grid = <CartesianGrid stroke={theme.rule} strokeDasharray="2 4" horizontal={false} />;

  return (
    <ChartFrame
      title="How fast do California counties count?"
      subtitle="Share of ballots counted within a week of Election Day, 2022 vs 2025"
      note={
        <>
          Most counties adopted this tech years before our one-week data begins
          in 2022 — and several were still slow then — so the 2022–25 rise is
          largely a statewide trend (the state average climbed 78% → 94%), not a
          direct adoption effect. San Francisco, which adopted <em>nothing</em>,
          is the one that fell behind that rise; Fresno, which adopted both, also
          slipped. Marks/badges show each county’s adoption year. (National
          adopters — Pennsylvania 2016, Wisconsin 2018, New York 2019 — publish
          no comparable metric.) Sources in{" "}
          <a
            href="https://github.com/Grow-SF/sf-election-historical-counts/blob/main/docs/sources.md"
            target="_blank"
            rel="noopener noreferrer"
            className="border-b border-rule text-rust hover:bg-rust/10"
          >
            docs/sources.md
          </a>
          .
        </>
      }
    >
      <div className="mb-3 flex flex-wrap gap-2">
        {VIZ.map((v) => (
          <button
            key={v.key}
            onClick={() => setViz(v.key)}
            className={`smallcaps border px-2.5 py-1 transition-colors ${
              v.key === viz ? "border-ink bg-ink text-paper" : "border-rule text-faint hover:border-ink hover:text-ink"
            }`}
          >
            {v.label}
          </button>
        ))}
      </div>

      <ResponsiveContainer width="100%" height={height}>
        {viz === "arrows" ? (
          // dumbbell: a colored segment from 2022 to 2025, red where it shrank
          <ComposedChart layout="vertical" data={BASE} margin={{ top: 8, right: 48, bottom: 8, left: 8 }} barCategoryGap="34%">
            {grid}
            <XAxis type="number" domain={[40, 100]} ticks={[40, 60, 80, 100]} tickFormatter={(v: number) => `${v}%`} tick={{ fontFamily: theme.fontMono, fontSize: 11, fill: theme.faint }} stroke={theme.faint} tickLine={false} />
            {yAxis}
            <Tooltip cursor={{ fill: theme.faint, fillOpacity: 0.06 }} isAnimationActive={false} formatter={(_v, _n, p: { payload?: { y2022?: number; y2025?: number } }) => [`${p?.payload?.y2022}% → ${p?.payload?.y2025}%`, "2022 → 2025"]} />
            <Bar dataKey="range" barSize={5} isAnimationActive={false} radius={3} label={{ position: "right", fontFamily: theme.fontMono, fontSize: 10, fill: theme.faint, formatter: (_v: unknown) => "" }}>
              {BASE.map((c) => (
                <Cell key={c.jurisdiction} fill={c.change >= 0 ? moss : warn} />
              ))}
            </Bar>
          </ComposedChart>
        ) : viz === "change" ? (
          // diverging: change in one-week rate, 2022 -> 2025
          <BarChart layout="vertical" data={BY_CHANGE} margin={{ top: 8, right: 44, bottom: 8, left: 8 }} barCategoryGap="22%">
            {grid}
            <XAxis type="number" domain={[-15, 50]} ticks={[-10, 0, 10, 20, 30, 40, 50]} tickFormatter={(v: number) => `${v > 0 ? "+" : ""}${v}`} tick={{ fontFamily: theme.fontMono, fontSize: 11, fill: theme.faint }} stroke={theme.faint} tickLine={false} />
            {yAxis}
            <Tooltip cursor={{ fill: theme.faint, fillOpacity: 0.06 }} isAnimationActive={false} formatter={(v: unknown) => { const n = Number(v); return [`${n > 0 ? "+" : ""}${n} pts`, "change ‘22→‘25"]; }} />
            <ReferenceLine x={0} stroke={theme.ink} />
            <Bar dataKey="change" isAnimationActive={false} label={{ position: "right", fontFamily: theme.fontMono, fontSize: 10, fill: theme.faint, formatter: (v: unknown) => (typeof v === "number" ? `${v > 0 ? "+" : ""}${v}` : "") }}>
              {BY_CHANGE.map((c) => (
                <Cell key={c.jurisdiction} fill={c.change >= 0 ? moss : warn} />
              ))}
            </Bar>
          </BarChart>
        ) : (
          // corrected timeline: each county's adoption year (●, on a real time
          // axis) vs its one-week trajectory (2022–2025). Most adopted years
          // before the data begins — and were still slow at 2022 — so the rise
          // is a statewide trend, not a clean adoption effect.
          <LineChart data={TLINE} margin={{ top: 18, right: 122, bottom: 8, left: 8 }}>
            <CartesianGrid stroke={theme.rule} strokeDasharray="2 4" vertical={false} />
            <XAxis type="number" dataKey="x" domain={[2017.5, 2025.8]} ticks={[2018, 2020, 2022, 2024]} tickFormatter={(v: number) => `’${String(v).slice(2)}`} tick={{ fontFamily: theme.fontMono, fontSize: 11, fill: theme.faint }} stroke={theme.faint} tickLine={false} />
            <YAxis type="number" domain={[40, 100]} ticks={[40, 60, 80, 100]} tickFormatter={(v: number) => `${v}%`} tick={{ fontFamily: theme.fontMono, fontSize: 11, fill: theme.faint }} stroke={theme.faint} tickLine={false} width={44} />
            <Tooltip isAnimationActive={false} />
            <ReferenceLine x={2022} stroke={theme.faint} strokeDasharray="2 3" label={{ value: "one-week data begins", position: "top", fontFamily: theme.fontMono, fontSize: 9, fill: theme.faint }} />
            {BASE.map((c) => {
              const ay = adoptYear(c.jurisdiction);
              if (!ay) return null;
              const decliner = c.change < 0;
              const color = decliner ? warn : moss;
              return (
                <ReferenceLine
                  key={`seg-${c.jurisdiction}`}
                  segment={[{ x: ay, y: c.y2022 as number }, { x: 2022, y: c.y2022 as number }]}
                  stroke={color}
                  strokeOpacity={decliner ? 0.55 : 0.22}
                  strokeDasharray="1 4"
                />
              );
            })}
            {BASE.map((c) => {
              const ay = adoptYear(c.jurisdiction);
              if (!ay) return null;
              const decliner = c.change < 0;
              const color = decliner ? warn : moss;
              return <ReferenceDot key={`dot-${c.jurisdiction}`} x={ay} y={c.y2022 as number} r={3} fill={color} fillOpacity={decliner ? 1 : 0.6} stroke="none" />;
            })}
            {BASE.map((c) => {
              const decliner = c.change < 0;
              const color = decliner ? warn : moss;
              return (
                <Line
                  key={c.jurisdiction}
                  dataKey={c.jurisdiction}
                  stroke={color}
                  strokeWidth={decliner ? 2.75 : 1.25}
                  strokeOpacity={decliner ? 1 : 0.4}
                  dot={false}
                  connectNulls
                  isAnimationActive={false}
                  label={decliner || (c.y2025 as number) < 96 ? endLabel(c.short, color, decliner) : undefined}
                />
              );
            })}
          </LineChart>
        )}
      </ResponsiveContainer>
    </ChartFrame>
  );
}
