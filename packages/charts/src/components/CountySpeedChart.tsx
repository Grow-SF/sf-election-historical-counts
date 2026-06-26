"use client";
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
import { COUNTY_SPEED } from "../../../data/index";
import { useChartTheme } from "../theme";
import { ChartFrame } from "./ui";

const YEARS = COUNTY_SPEED.years;

// recharts wants flat keys, so spread each county's year rates into y2022… fields.
const DATA = COUNTY_SPEED.counties.map((c) => ({
  county: c.county,
  epollbook: c.epollbook,
  ...Object.fromEntries(
    YEARS.map((y) => [`y${y}`, c.rates[String(y)] ?? null]),
  ),
}));

// year → bar fill: a faded "before" through to a saturated "now".
const YEAR_FILL: Record<number, string> = {
  2022: "#c4d7ce",
  2024: "var(--lc-slate)",
  2025: "var(--lc-moss)",
};

type Row = (typeof DATA)[number];

/** Two-line category label: county name, then whether it runs e-pollbooks —
 *  the variable the chart is really about. */
function CountyTick({
  x,
  y,
  payload,
  moss,
  warn,
  faint,
}: {
  x?: number;
  y?: number;
  payload?: { value: string };
  moss: string;
  warn: string;
  faint: string;
}) {
  const row = DATA.find((d) => d.county === payload?.value);
  const mark =
    row?.epollbook === true
      ? "e-pollbooks"
      : row?.epollbook === false
        ? "no e-pollbooks"
        : "statewide";
  const markColor =
    row?.epollbook === true ? moss : row?.epollbook === false ? warn : faint;
  return (
    <g transform={`translate(${x},${y})`}>
      <text
        textAnchor="middle"
        dy={16}
        fontFamily="var(--lc-font-display)"
        fontSize={13}
        fill="var(--lc-ink)"
      >
        {payload?.value}
      </text>
      <text
        textAnchor="middle"
        dy={32}
        fontFamily="var(--lc-font-mono)"
        fontSize={10}
        fill={markColor}
      >
        {mark}
      </text>
    </g>
  );
}

function SpeedTooltip({
  active,
  payload,
  label,
}: {
  active?: boolean;
  payload?: { value: number; dataKey: string }[];
  label?: string;
}) {
  if (!active || !payload?.length) return null;
  const row = DATA.find((d) => d.county === label) as Row | undefined;
  return (
    <div className="border border-ink bg-paper px-3 py-2 text-sm shadow">
      <div className="font-semibold">{label}</div>
      {payload.map((p) => {
        const year = p.dataKey.replace(/^y/, "");
        return (
          <div key={p.dataKey} className="stat-figure">
            {year}: {p.value}% counted within a week
          </div>
        );
      })}
      {row && row.epollbook !== null && (
        <div className="smallcaps mt-1 text-faint">
          {row.epollbook ? "uses e-pollbooks" : "no e-pollbooks · no auto-sig"}
        </div>
      )}
    </div>
  );
}

export default function CountySpeedChart() {
  const theme = useChartTheme();
  return (
    <ChartFrame
      title="One week after Election Day, who's been counted?"
      subtitle="Share of ballots counted within a week of the election, 2022–2025"
      note={
        <>
          Los Angeles adopted electronic pollbooks and rocketed from the slowest
          big county to nearly complete; San Francisco — which uses neither
          e-pollbooks nor automated signature verification — is the only large
          county that got <em>slower</em>, slipping below the statewide average.
          Source: California Voter Foundation,{" "}
          <a
            href={COUNTY_SPEED.sourceUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="border-b border-rule text-rust hover:bg-rust/10"
          >
            “Ballot Processing.”
          </a>
        </>
      }
    >
      <ResponsiveContainer width="100%" height={400}>
        <BarChart
          data={DATA}
          margin={{ top: 24, right: 20, bottom: 28, left: 0 }}
          barCategoryGap="22%"
        >
          <CartesianGrid stroke={theme.rule} strokeDasharray="2 4" vertical={false} />
          <XAxis
            dataKey="county"
            interval={0}
            height={48}
            tick={
              <CountyTick
                moss={theme.colorsByKind.Special}
                warn={theme.colorsByKind.Recall}
                faint={theme.faint}
              />
            }
            stroke={theme.faint}
            tickLine={false}
          />
          <YAxis
            type="number"
            domain={[0, 100]}
            ticks={[0, 25, 50, 75, 100]}
            tickFormatter={(v: number) => `${v}%`}
            tick={{ fontFamily: theme.fontMono, fontSize: 11, fill: theme.faint }}
            stroke={theme.faint}
            tickLine={false}
            width={48}
          />
          <Tooltip
            content={<SpeedTooltip />}
            cursor={{ fill: theme.faint, fillOpacity: 0.06 }}
            isAnimationActive={false}
          />
          <Legend
            verticalAlign="top"
            align="right"
            iconType="square"
            iconSize={10}
            wrapperStyle={{
              fontFamily: theme.fontMono,
              fontSize: 11,
              paddingBottom: 8,
            }}
          />
          {YEARS.map((y) => (
            <Bar
              key={y}
              dataKey={`y${y}`}
              name={`Nov ${y}`}
              fill={YEAR_FILL[y]}
              isAnimationActive={false}
              label={{
                position: "top",
                fontFamily: theme.fontMono,
                fontSize: 10,
                fill: theme.faint,
                formatter: (v: unknown) => (v == null ? "" : String(v)),
              }}
            />
          ))}
        </BarChart>
      </ResponsiveContainer>
    </ChartFrame>
  );
}
