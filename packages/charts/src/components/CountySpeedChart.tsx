"use client";
import { useState } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  Legend,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { COUNTY_TECH } from "../../../data/index";
import { useChartTheme } from "../theme";
import { ChartFrame } from "./ui";

type MetricKey = "oneweek_pct" | "electionnight_pct" | "days_to_90";
const METRICS: {
  key: MetricKey;
  chip: string;
  axis: string;
  domain: [number, number];
  ticks: number[];
  unit: string;
  better: "higher" | "lower";
}[] = [
  { key: "oneweek_pct", chip: "within 1 week", axis: "% of ballots counted within a week of Election Day", domain: [0, 100], ticks: [0, 25, 50, 75, 100], unit: "%", better: "higher" },
  { key: "electionnight_pct", chip: "on election night", axis: "% of ballots counted on election night", domain: [0, 100], ticks: [0, 25, 50, 75, 100], unit: "%", better: "higher" },
  { key: "days_to_90", chip: "days to 90% counted", axis: "days after Election Day to reach 90% of the final count", domain: [0, 30], ticks: [0, 10, 20, 30], unit: "d", better: "lower" },
];

const YEARS = [...new Set(COUNTY_TECH.metrics.map((m) => m.year))].sort((a, b) => a - b);
const YEAR_FILL: Record<number, string> = { 2022: "#c4d7ce", 2024: "var(--lc-slate)", 2025: "var(--lc-moss)" };
const LATEST = YEARS[YEARS.length - 1];

// adopted-tech summary per jurisdiction
const TECH: Record<string, Record<string, number | null>> = {};
for (const a of COUNTY_TECH.adoptions) {
  if (a.status !== "adopted") continue;
  (TECH[a.jurisdiction] ||= {})[a.tech] = a.adopted_year;
}
const techBadge = (j: string) => {
  const t = TECH[j] || {};
  const parts: string[] = [];
  if (t.epollbook) parts.push("e-pollbook");
  if (t.asv) parts.push("ASV");
  if (t["sign-scan-go"]) parts.push("sign-scan-go");
  return parts.join(" + ") || "neither";
};
const adopted = (j: string) => {
  const t = TECH[j] || {};
  return !!(t.epollbook || t.asv || t["sign-scan-go"]);
};
const shortName = (j: string) => j.replace(/ County$/, "");

function rowsFor(key: MetricKey, better: "higher" | "lower") {
  const byJ: Record<string, Record<string, string | number | null>> = {};
  for (const m of COUNTY_TECH.metrics) {
    if (m.state !== "CA" || m.metric !== key || m.value == null) continue;
    (byJ[m.jurisdiction] ||= { jurisdiction: m.jurisdiction })[`y${m.year}`] = m.value;
  }
  const latest = (r: Record<string, string | number | null>) => {
    for (let i = YEARS.length - 1; i >= 0; i--) {
      const v = r[`y${YEARS[i]}`];
      if (v != null) return v as number;
    }
    return better === "higher" ? -1 : 1e9;
  };
  // sort so the "fastest" is at the top either way
  return Object.values(byJ).sort((a, b) =>
    better === "higher" ? latest(b) - latest(a) : latest(a) - latest(b),
  );
}

function JurisTick({ x, y, payload, moss, warn }: { x?: number; y?: number; payload?: { value: string }; moss: string; warn: string }) {
  const j = payload?.value ?? "";
  return (
    <g transform={`translate(${x},${y})`}>
      <text textAnchor="end" dx={-8} dy={-1} fontSize={12} fontFamily="var(--lc-font-display)" fill="var(--lc-ink)">
        {shortName(j)}
      </text>
      <text textAnchor="end" dx={-8} dy={11} fontSize={9} fontFamily="var(--lc-font-mono)" fill={adopted(j) ? moss : warn}>
        {techBadge(j)}
      </text>
    </g>
  );
}

function SpeedTooltip({ active, payload, label, unit }: { active?: boolean; payload?: { value: number; dataKey: string }[]; label?: string; unit: string }) {
  if (!active || !payload?.length) return null;
  return (
    <div className="border border-ink bg-paper px-3 py-2 text-sm shadow">
      <div className="font-semibold">{label}</div>
      {payload.map((p) => (
        <div key={p.dataKey} className="stat-figure">
          Nov {p.dataKey.replace(/^y/, "")}: {p.value}{unit}
        </div>
      ))}
      <div className="smallcaps mt-1 text-faint">{techBadge(String(label))}</div>
    </div>
  );
}

export default function CountySpeedChart() {
  const theme = useChartTheme();
  const [key, setKey] = useState<MetricKey>("oneweek_pct");
  const metric = METRICS.find((m) => m.key === key)!;
  const data = rowsFor(key, metric.better);
  const usableYears = YEARS.filter((y) => data.some((r) => r[`y${y}`] != null));
  const height = Math.max(340, data.length * 40 + 64);

  return (
    <ChartFrame
      title="How fast do California counties count?"
      subtitle={`${metric.axis}${metric.better === "lower" ? " — shorter is faster" : ""}, 2022–2025`}
      note={
        <>
          Counties that adopted electronic pollbooks and/or automated signature
          verification trend toward near-complete counts; San Francisco — which
          runs <em>neither</em> — is the lone large county whose one-week share
          fell. (National e-pollbook adopters in our data — Pennsylvania 2016,
          Wisconsin 2018, New York 2019 — aren’t shown here: they publish no
          comparable California-style metric.) Sources: California Voter
          Foundation “Ballot Processing,” the CA Secretary of State, and each
          county registrar — every figure is listed in{" "}
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
        {METRICS.map((m) => (
          <button
            key={m.key}
            onClick={() => setKey(m.key)}
            className={`smallcaps border px-2.5 py-1 transition-colors ${
              m.key === key
                ? "border-ink bg-ink text-paper"
                : "border-rule text-faint hover:border-ink hover:text-ink"
            }`}
          >
            {m.chip}
          </button>
        ))}
      </div>
      <ResponsiveContainer width="100%" height={height}>
        <BarChart
          layout="vertical"
          data={data}
          margin={{ top: 8, right: 44, bottom: 8, left: 8 }}
          barCategoryGap="22%"
        >
          <CartesianGrid stroke={theme.rule} strokeDasharray="2 4" horizontal={false} />
          <XAxis
            type="number"
            domain={metric.domain}
            ticks={metric.ticks}
            tickFormatter={(v: number) => `${v}${metric.unit}`}
            tick={{ fontFamily: theme.fontMono, fontSize: 11, fill: theme.faint }}
            stroke={theme.faint}
            tickLine={false}
          />
          <YAxis
            type="category"
            dataKey="jurisdiction"
            width={158}
            interval={0}
            tick={<JurisTick moss={theme.colorsByKind.Special} warn={theme.colorsByKind.Recall} />}
            stroke={theme.faint}
            tickLine={false}
          />
          <Tooltip content={<SpeedTooltip unit={metric.unit} />} cursor={{ fill: theme.faint, fillOpacity: 0.06 }} isAnimationActive={false} />
          <Legend verticalAlign="top" align="right" iconType="square" iconSize={10} wrapperStyle={{ fontFamily: theme.fontMono, fontSize: 11, paddingBottom: 8 }} />
          {usableYears.map((y) => (
            <Bar
              key={y}
              dataKey={`y${y}`}
              name={`Nov ${y}`}
              fill={YEAR_FILL[y] ?? theme.faint}
              isAnimationActive={false}
              label={
                y === LATEST
                  ? { position: "right", fontFamily: theme.fontMono, fontSize: 9, fill: theme.faint, formatter: (v: unknown) => (v == null ? "" : `${v}${metric.unit}`) }
                  : undefined
              }
            />
          ))}
        </BarChart>
      </ResponsiveContainer>
    </ChartFrame>
  );
}
