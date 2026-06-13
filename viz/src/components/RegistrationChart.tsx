"use client";
import {
  CartesianGrid,
  ComposedChart,
  Line,
  ReferenceLine,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { REGISTRATION_ELIGIBLE, fmt } from "@/lib/data";
import { ChartFrame } from "@/components/ui";

const DATA = REGISTRATION_ELIGIBLE.map((p) => {
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
const MILESTONES = [2002.0, 2020.84, 2022.0];

export default function RegistrationChart() {
  return (
    <ChartFrame
      title="Registration among eligible citizens"
      subtitle="Registered ÷ citizen voting-age population, 1978–2026"
      note={
        <>
          <span className="smallcaps not-italic" style={{ color: "var(--color-gold)" }}>
            gold lines:
          </span>{" "}
          2002 permanent vote-by-mail list · Nov 2020 every voter mailed a
          ballot (AB 860) · 2022 made permanent (AB 37).
          <br />
          Registered voters as a share of the eligible (citizen voting-age)
          population in San Francisco, 1978–2026. (Pre-1978 the Statement of
          Vote used a total voting-age-population denominator, not citizen-
          eligible, so those years aren’t comparable and sit in the separate
          voting-age-population estimate instead.) The share holds in a ~70–86%
          band across nearly fifty years — including straight through the
          all-mail transition. San
          Francisco was already near the ceiling, and mailing every voter a
          ballot did not lift it. Three caveats keep this from being a clean
          line: the rolls <em>sawtooth</em> (registration peaks at each general,
          then list maintenance purges inactive voters); the <em>eligible</em>
          denominator is a Department of Finance / Census estimate the state
          revises between reports (it even dips 2011–2013); and the ~96–101%
          spike (1994–96) is a pre-“motor-voter” artifact — bloated rolls
          against a low eligible estimate. (In Oct 1996 the Secretary of State
          singled out San Francisco — 482,541 registered against 479,127
          eligible adult citizens — as the state’s prime example of “deadwood,”
          10–20% of names being voters who had died, moved, or re-registered
          elsewhere; the 1995 federal “motor-voter” cleanups then pulled the
          rate back into the band.) Read the band, not the wiggles. Sources:
          1974–1998 from the printed Statement of Vote “Voter Participation by
          County” tables (archive.org), read off page scans and{" "}
          <em>pending hand-verification</em>; 2000–2026 from the SoS Reports of
          Registration. The SoS published no county-level eligible figure before
          ~1973, so the series can’t run back to 1964 on state data alone.
        </>
      }
    >
      <ResponsiveContainer width="100%" height={360}>
        <ComposedChart
          data={DATA}
          margin={{ top: 24, right: 20, bottom: 8, left: 0 }}
        >
          <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
          <XAxis
            type="number"
            dataKey="x"
            domain={[1972, 2028]}
            ticks={[1975, 1985, 1995, 2005, 2015, 2025]}
            tickFormatter={(v: number) => String(v)}
            tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
            stroke="var(--color-faint)"
            tickLine={false}
            allowDataOverflow
          />
          <YAxis
            type="number"
            domain={[0, 100]}
            ticks={[0, 25, 50, 75, 100]}
            tickFormatter={(v: number) => `${v}%`}
            tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
            stroke="var(--color-faint)"
            tickLine={false}
            width={48}
          />
          <Tooltip content={<RegTooltip />} isAnimationActive={false} />
          {MILESTONES.map((x) => (
            <ReferenceLine
              key={x}
              x={x}
              stroke="var(--color-gold)"
              strokeDasharray="4 4"
            />
          ))}
          <Line
            dataKey="y"
            stroke="#3E5C76"
            strokeWidth={2}
            connectNulls
            dot={{ r: 2.5, fill: "#3E5C76", strokeWidth: 0 }}
            isAnimationActive={false}
          />
        </ComposedChart>
      </ResponsiveContainer>
    </ChartFrame>
  );
}
