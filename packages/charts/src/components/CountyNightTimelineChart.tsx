"use client";
import {
  CartesianGrid,
  Line,
  LineChart,
  ReferenceLine,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { COUNTY_NIGHT } from "../../../data/index";
import type { CountyNightJurisdiction, CountyNightPoint } from "../../../data/index";
import { useChartTheme } from "../theme";
import { ChartFrame } from "./ui";

// ---- per-county ELECTION-NIGHT share over time (full trajectory), as small
// multiples. SF (no new tech) is drawn faint in every county panel as the
// baseline; a vertical mark shows the tech-adoption year. Only counties with a
// complete primary-sourced series are shown. ----
const YEARS = [2012, 2014, 2016, 2018, 2020, 2022, 2024];
const PRES = new Set([2012, 2016, 2020, 2024]);

const yy = (y: number | null) => (y ? `’${String(y).slice(2)}` : "");
const norm = (p: number | null) =>
  p == null ? null : p <= 1.5 ? +(p * 100).toFixed(1) : p;

const badge = (j: CountyNightJurisdiction) => {
  if (j.control) return "no new tech";
  const parts: string[] = [];
  if (j.adoption.epollbook) parts.push(`e-pb ${yy(j.adoption.epollbook)}`);
  if (j.adoption.asv) parts.push(`ASV ${yy(j.adoption.asv)}`);
  return parts.join(" · ") || "—";
};

const adoptYear = (j: CountyNightJurisdiction) => {
  const ys = [j.adoption.epollbook, j.adoption.asv].filter(
    (y): y is number => !!y,
  );
  return ys.length ? Math.min(...ys) : null;
};

// the general and primary type for a given election year (presidential years
// hold a presidential general + presidential primary; midterm years hold a
// midterm general + midterm primary)
const generalType = (year: number): CountyNightPoint["type"] =>
  PRES.has(year) ? "presidential" : "midterm";
const primaryType = (year: number): CountyNightPoint["type"] =>
  PRES.has(year) ? "presidential-primary" : "midterm-primary";

// a jurisdiction's election-night share per election year: the general-election
// value (v, solid line) and the same-type primary value (primary, dimmed line),
// null where unsourced or excluded (e.g. the Nevada 2024 printer-defect
// outlier)
export const seriesFor = (j: CountyNightJurisdiction) =>
  YEARS.map((year) => {
    // 2020 is the COVID all-mail outlier — omitted for every jurisdiction (SF
    // carries a 2020 row the counties don't, so drop it for consistency).
    if (year === 2020) return { year, v: null, primary: null };
    const find = (type: CountyNightPoint["type"]) =>
      j.points.find(
        (pt) => pt.year === year && pt.type === type && pt.pct != null && pt.comparable,
      );
    const g = find(generalType(year));
    const p = find(primaryType(year));
    return { year, v: g ? norm(g.pct) : null, primary: p ? norm(p.pct) : null };
  });

export default function CountyNightTimelineChart() {
  const theme = useChartTheme();
  const moss = theme.colorsByKind.Special;
  const ink = theme.ink;

  const shown = COUNTY_NIGHT.jurisdictions.filter((j) => j.control || j.complete);
  // SF is the baseline overlay; every other COMPLETE jurisdiction (treated
  // counties and the second control, San Luis Obispo) gets its own panel.
  // Sparse controls (Del Norte, Lake, Mendocino, Tehama, Colusa) have
  // incomplete series and live in CountyNightShareChart instead.
  const sf = shown.find((j) => j.slug === "san-francisco") ?? shown.find((j) => j.control);
  const sfSeries = sf
    ? seriesFor(sf)
    : YEARS.map((year) => ({ year, v: null, primary: null }));
  const ordered = [
    ...(sf ? [sf] : []),
    ...shown.filter((j) => j !== sf && j.complete),
  ];

  return (
    <ChartFrame
      title="Election-night share over time, by county"
      subtitle="Each county’s full trajectory, 2012–2024. The dashed grey line is San Francisco (no new tech) for comparison"
      note={
        <>
          One panel per county; the vertical dotted mark is the year it adopted
          e-pollbooks / automated signature verification. The solid line is
          the November general; the dimmed, dashed line of the same color is
          that year’s primary (presidential primary in presidential years,
          midterm primary in midterms) — always same-type compared, never
          mixed with the general. Lines zigzag because presidential years
          (’12 ’16 ’24) draw more election-day turnout than midterms (’14 ’18
          ’22), so watch the <em>level</em>, not the saw-tooth. The all-mail
          Voter’s Choice Act counties (Napa, San&nbsp;Mateo, Nevada, all ’18)
          step <strong>down</strong> right at adoption and stay there; the
          no-tech control counties (the bold panels: SF,
          San&nbsp;Luis&nbsp;Obispo, Del&nbsp;Norte, Lake, Mendocino) drift
          down too, some of them hardest of all. Composition-adjusted, the vote-center counties have
          weathered that decay about 10 points better than the no-tech
          controls (suggestive, not certified; see{" "}
          <a
            href="https://github.com/Grow-SF/sf-election-historical-counts/blob/main/docs/analysis/2026-07-10-vca-bundle-tech-effect.md"
            target="_blank"
            rel="noopener noreferrer"
            className="border-b border-rule text-rust hover:bg-rust/10"
          >
            the analysis
          </a>
          ). 2020 (COVID all-mail) is omitted, as is the Nevada 2024
          printer-defect outlier. Sources in{" "}
          <a
            href="https://github.com/Grow-SF/sf-election-historical-counts/blob/main/data/research/election-night/VERIFY.md"
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
      <div className="grid grid-cols-1 gap-x-10 gap-y-5 sm:grid-cols-2 lg:grid-cols-3">
        {ordered.map((j) => {
          const own = seriesFor(j);
          const data = own.map((d, i) => ({
            year: d.year,
            v: d.v,
            primary: d.primary,
            sf: sfSeries[i]?.v ?? null,
          }));
          const ay = adoptYear(j);
          const color = j.control ? ink : moss;
          return (
            <div key={j.slug}>
              <div className="mb-1 flex items-baseline justify-between">
                <span
                  className="font-display text-ink"
                  style={{ fontWeight: j.control ? 700 : 400 }}
                >
                  {j.name}
                </span>
                <span
                  className="smallcaps text-xs"
                  style={{ color: j.control ? theme.faint : moss }}
                >
                  {badge(j)}
                </span>
              </div>
              <ResponsiveContainer width="100%" height={140}>
                <LineChart
                  data={data}
                  margin={{ top: 6, right: 8, bottom: 2, left: -18 }}
                >
                  <CartesianGrid
                    stroke={theme.rule}
                    strokeDasharray="2 4"
                    vertical={false}
                  />
                  <XAxis
                    dataKey="year"
                    type="number"
                    domain={[2012, 2024]}
                    ticks={[2012, 2016, 2020, 2024]}
                    tickFormatter={(v: number) => `’${String(v).slice(2)}`}
                    tick={{
                      fontFamily: theme.fontMono,
                      fontSize: 10,
                      fill: theme.faint,
                    }}
                    stroke={theme.faint}
                    tickLine={false}
                  />
                  <YAxis
                    domain={[30, 90]}
                    ticks={[40, 60, 80]}
                    tickFormatter={(v: number) => `${v}%`}
                    tick={{
                      fontFamily: theme.fontMono,
                      fontSize: 10,
                      fill: theme.faint,
                    }}
                    stroke={theme.faint}
                    tickLine={false}
                    width={42}
                  />
                  <Tooltip
                    isAnimationActive={false}
                    formatter={(val: unknown, name: unknown) => {
                      const n = Number(val);
                      const label =
                        name === "sf"
                          ? "SF"
                          : name === "primary"
                            ? `${j.name} primary`
                            : j.name;
                      return [Number.isFinite(n) ? `${n}%` : "—", label];
                    }}
                    labelFormatter={(y) =>
                      `${y}${PRES.has(Number(y)) ? " (pres)" : " (midterm)"}`
                    }
                  />
                  {ay ? (
                    <ReferenceLine
                      x={ay}
                      stroke={moss}
                      strokeDasharray="2 3"
                      strokeOpacity={0.6}
                    />
                  ) : null}
                  {j !== sf ? (
                    <Line
                      dataKey="sf"
                      stroke={theme.faint}
                      strokeWidth={1}
                      strokeDasharray="3 3"
                      dot={false}
                      connectNulls
                      isAnimationActive={false}
                    />
                  ) : null}
                  {/* the same-type primary trajectory, dimmed + dashed so it
                      reads as the secondary comparison to the solid general
                      line, never mixed with it */}
                  <Line
                    dataKey="primary"
                    stroke={color}
                    strokeWidth={1.25}
                    strokeOpacity={0.5}
                    strokeDasharray="2 3"
                    dot={{ r: 1.75, fill: color, fillOpacity: 0.5, stroke: "none" }}
                    connectNulls
                    isAnimationActive={false}
                  />
                  <Line
                    dataKey="v"
                    stroke={color}
                    strokeWidth={2.25}
                    dot={{ r: 2.5, fill: color, stroke: "none" }}
                    connectNulls
                    isAnimationActive={false}
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          );
        })}
      </div>
    </ChartFrame>
  );
}
