"use client";
import { useState } from "react";
import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { COUNTY_NIGHT } from "../../../data/index";
import type {
  CountyNightJurisdiction,
  CountyNightPoint,
} from "../../../data/index";
import { useChartTheme } from "../theme";
import { ChartFrame } from "./ui";

// ---- data prep: each jurisdiction's pre- vs post-adoption election-night
// share, like-to-like (presidential vs presidential, midterm vs midterm). SF is
// the no-new-tech control. 2020 (COVID all-mail) and rows flagged
// comparable=false (e.g. Nevada 2024, a printer-defect outlier) are excluded. ----
const yy = (y: number | null) => (y ? `’${String(y).slice(2)}` : "");

const badge = (j: CountyNightJurisdiction) => {
  if (j.control) return "no new tech";
  const parts: string[] = [];
  if (j.adoption.epollbook) parts.push(`e-pb ${yy(j.adoption.epollbook)}`);
  if (j.adoption.asv) parts.push(`ASV ${yy(j.adoption.asv)}`);
  return parts.join(" · ") || "—";
};

const adoptBoundary = (j: CountyNightJurisdiction) => {
  const ys = [j.adoption.epollbook, j.adoption.asv].filter(
    (y): y is number => !!y,
  );
  return ys.length ? Math.min(...ys) : null;
};

// The control (SF, no adoption) is measured over the same window as the
// adopters: from the last election before ANY county adopted, to the latest —
// so its bar isn't unfairly stretched across extra years.
const EARLIEST_ADOPT = Math.min(
  ...COUNTY_NIGHT.jurisdictions
    .filter((j) => j.complete && !j.control)
    .map(adoptBoundary)
    .filter((y): y is number => y != null),
);

type Row = {
  slug: string;
  name: string;
  badge: string;
  control: boolean;
  pre: number;
  post: number;
  preYear: number;
  postYear: number;
  change: number;
  range: [number, number];
  rose: boolean;
};

type SourcedPoint = CountyNightPoint & { pct: number };

function prepost(
  j: CountyNightJurisdiction,
  type: "presidential" | "midterm",
): Row | null {
  const pts = j.points
    .filter(
      (p) =>
        p.type === type &&
        p.pct != null &&
        p.comparable &&
        !(type === "presidential" && p.year === 2020),
    )
    .sort((a, b) => a.year - b.year) as SourcedPoint[];
  if (pts.length < 2) return null;

  const b = j.control ? EARLIEST_ADOPT : adoptBoundary(j);
  if (b == null) return null;
  // last election before the (county's, or for SF the earliest) adoption year,
  // vs the most recent one at/after it — like-to-like across all bars.
  const pre = [...pts].reverse().find((p) => p.year < b);
  const post = [...pts].reverse().find((p) => p.year >= b);
  if (!pre || !post || pre.year === post.year) return null;

  const change = +(post.pct - pre.pct).toFixed(1);
  return {
    slug: j.slug,
    name: j.name,
    badge: badge(j),
    control: j.control,
    pre: pre.pct,
    post: post.pct,
    preYear: pre.year,
    postYear: post.year,
    change,
    range: [Math.min(pre.pct, post.pct), Math.max(pre.pct, post.pct)],
    rose: change >= 0,
  };
}

const TYPES = [
  { key: "presidential", label: "presidential" },
  { key: "midterm", label: "midterm" },
] as const;
type ElType = (typeof TYPES)[number]["key"];

function YTick({
  x,
  y,
  payload,
  rows,
  moss,
  faint,
  ink,
}: {
  x?: number;
  y?: number;
  payload?: { value: string };
  rows: Row[];
  moss: string;
  faint: string;
  ink: string;
}) {
  const r = rows.find((d) => d.name === payload?.value);
  if (!r) return <g />;
  return (
    <g transform={`translate(${x},${y})`}>
      <text
        textAnchor="end"
        dx={-8}
        dy={-1}
        fontSize={12}
        fontFamily="var(--lc-font-display)"
        fill="var(--lc-ink)"
        fontWeight={r.control ? 700 : 400}
      >
        {r.name}
      </text>
      <text
        textAnchor="end"
        dx={-8}
        dy={11}
        fontSize={9}
        fontFamily="var(--lc-font-mono)"
        fill={r.control ? ink : moss}
        opacity={r.control ? 0.6 : 1}
      >
        {r.badge}
      </text>
    </g>
  );
}

const deltaLabel =
  (rows: Row[], faint: string, moss: string, warn: string) =>
  (props: {
    x?: number | string;
    y?: number | string;
    width?: number | string;
    height?: number | string;
    index?: number;
  }) => {
    const r = rows[props.index ?? -1];
    if (!r) return null;
    const x = Number(props.x ?? 0) + Number(props.width ?? 0) + 8;
    const y = Number(props.y ?? 0) + Number(props.height ?? 0) / 2;
    const c = r.control ? faint : r.rose ? moss : warn;
    return (
      <text
        x={x}
        y={y}
        dy={4}
        fontSize={10}
        fontFamily="var(--lc-font-mono)"
        fill={c}
      >
        {`${r.change >= 0 ? "+" : ""}${r.change}`}
      </text>
    );
  };

export default function CountyNightShareChart() {
  const theme = useChartTheme();
  const [type, setType] = useState<ElType>("presidential");
  const moss = theme.colorsByKind.Special;
  const warn = theme.colorsByKind.Recall;
  const ink = theme.ink;

  const rows = COUNTY_NIGHT.jurisdictions
    .filter((j) => j.control || j.complete)
    .map((j) => prepost(j, type))
    .filter((r): r is Row => r !== null)
    .sort((a, b) =>
      a.control === b.control ? b.change - a.change : a.control ? -1 : 1,
    );

  const color = (r: Row) => (r.control ? ink : r.rose ? moss : warn);
  const height = rows.length * 40 + 72;

  return (
    <ChartFrame
      title="Did counting tech speed up election night?"
      subtitle={`Election-night share of the certified vote, before vs after adopting e-pollbooks / automated signature verification, ${type} generals`}
      note={
        <>
          Each bar runs from a county’s last <strong>pre-adoption</strong>{" "}
          election-night share to its most recent <strong>post-adoption</strong>{" "}
          share (same election type); green rose, red fell. San Francisco,
          which adopted <em>none</em> of this tech, is the bold control, and its
          share fell too. If the tech sped up the night count, adopters’ bars
          would climb green well past SF’s; instead several fall as far or
          farther. The 2018–2020 statewide move to all-mail (Voter’s Choice Act)
          is the bigger driver, independent of e-pollbooks/ASV. Shows only
          counties with a complete, primary-sourced election-night series (plus
          SF); excludes 2020 (COVID all-mail outlier) and the Nevada 2024
          ballot-printer-defect outlier. Per-number sources in{" "}
          <a
            href="https://github.com/Grow-SF/sf-election-historical-counts/blob/main/data/research/election-night-v4/VERIFY.md"
            target="_blank"
            rel="noopener noreferrer"
            className="border-b border-rule text-rust hover:bg-rust/10"
          >
            VERIFY.md
          </a>
          .
        </>
      }
    >
      <div className="mb-3 flex flex-wrap gap-2">
        {TYPES.map((t) => (
          <button
            key={t.key}
            onClick={() => setType(t.key)}
            className={`smallcaps border px-2.5 py-1 transition-colors ${
              t.key === type
                ? "border-ink bg-ink text-paper"
                : "border-rule text-faint hover:border-ink hover:text-ink"
            }`}
          >
            {t.label}
          </button>
        ))}
      </div>

      <ResponsiveContainer width="100%" height={height}>
        <BarChart
          layout="vertical"
          data={rows}
          margin={{ top: 8, right: 56, bottom: 8, left: 8 }}
          barCategoryGap="32%"
        >
          <CartesianGrid
            stroke={theme.rule}
            strokeDasharray="2 4"
            horizontal={false}
          />
          <XAxis
            type="number"
            domain={[10, 90]}
            ticks={[20, 40, 60, 80]}
            tickFormatter={(v: number) => `${v}%`}
            tick={{ fontFamily: theme.fontMono, fontSize: 11, fill: theme.faint }}
            stroke={theme.faint}
            tickLine={false}
          />
          <YAxis
            type="category"
            dataKey="name"
            width={150}
            interval={0}
            tick={
              <YTick rows={rows} moss={moss} faint={theme.faint} ink={ink} />
            }
            stroke={theme.faint}
            tickLine={false}
          />
          <Tooltip
            cursor={{ fill: theme.faint, fillOpacity: 0.06 }}
            isAnimationActive={false}
            formatter={(_v, _n, p: { payload?: Row }) => {
              const r = p?.payload;
              if (!r) return ["", ""];
              return [
                `${r.pre}% (${r.preYear}) → ${r.post}% (${r.postYear})`,
                `${r.change >= 0 ? "+" : ""}${r.change} pts`,
              ];
            }}
          />
          <Bar
            dataKey="range"
            barSize={6}
            radius={3}
            isAnimationActive={false}
            label={deltaLabel(rows, theme.faint, moss, warn)}
          >
            {rows.map((r) => (
              <Cell key={r.slug} fill={color(r)} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </ChartFrame>
  );
}
