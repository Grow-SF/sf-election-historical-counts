"use client";
import { useMemo } from "react";
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
import { Election, fmt, KIND_COLOR } from "@/lib/data";
import { ChartFrame } from "@/components/ui";

function DetailPanel({ e }: { e: Election }) {
  const row = (label: string, value: React.ReactNode) => (
    <div className="flex items-baseline justify-between gap-3 border-b border-rule py-1.5">
      <span className="smallcaps text-faint">{label}</span>
      <span className="stat-figure text-sm">{value}</span>
    </div>
  );
  const t = (n: number) => {
    const v = e.thresholds[String(n)];
    if (!v) return "—";
    return `${v.bound ? "≤ " : ""}${v.days}d`;
  };
  return (
    <div className="border border-rule bg-paper-deep/60 p-4">
      <p className="smallcaps" style={{ color: KIND_COLOR[e.kind] }}>
        {e.kind}
        {e.source === "archival" ? " · archival recovery" : ""}
        {e.provisional ? " · count ongoing" : ""}
      </p>
      <h3 className="mt-1 text-lg font-semibold leading-snug">
        {e.id} — {e.name}
      </h3>
      <div className="mt-3">
        {row("ballots counted", fmt(e.final))}
        {e.registered && row("registered voters", fmt(e.registered))}
        {e.nightPct !== null && row("by election night", `${e.nightPct}%`)}
        {e.vbmShare !== null && row("voted by mail", `${e.vbmShare}%`)}
        {row("to 50% / 80% / 90% / 98%", `${t(50)} / ${t(80)} / ${t(90)} / ${t(98)}`)}
        {row("observations", e.nReports)}
      </div>
      {e.source === "archival" && (
        <p className="mt-3 text-xs italic leading-relaxed text-faint">
          Recovered from Wayback Machine captures of the Department of
          Elections’ results pages; “≤” marks an upper bound from sparse
          snapshots.
        </p>
      )}
    </div>
  );
}

export default function TrajectoryExplorer({
  elections,
  selected,
  setSelected,
}: {
  elections: Election[];
  selected: string | null;
  setSelected: (id: string | null) => void;
}) {
  const sel = useMemo(
    () => elections.find((e) => e.id === selected) ?? null,
    [elections, selected],
  );

  return (
    <div>
      <div className="mb-4 flex flex-wrap gap-1.5">
        {elections.map((e) => {
          const on = selected === e.id;
          return (
            <button
              key={e.id}
              onClick={() => setSelected(on ? null : e.id)}
              aria-pressed={on}
              className="stat-figure border px-1.5 py-0.5 text-[11px] transition-colors"
              style={{
                borderColor: on ? KIND_COLOR[e.kind] : "var(--color-rule)",
                background: on ? KIND_COLOR[e.kind] : "transparent",
                color: on ? "var(--color-paper)" : "var(--color-ink)",
              }}
              title={`${e.name}${e.source === "archival" ? " (archival)" : ""}`}
            >
              {e.id.slice(0, 7)}
              {e.source === "archival" ? "*" : ""}
            </button>
          );
        })}
      </div>

      <div className="grid gap-5 lg:grid-cols-[1fr_290px]">
        <ChartFrame
          note={
            <>
              Each line is one election’s count: % of the certified final, by
              days since the 8 PM poll close. Dashed lines with markers are
              archival recoveries (sparse). Click a date chip to highlight;
              asterisks mark archival elections.
            </>
          }
        >
          <ResponsiveContainer width="100%" height={420}>
            <ComposedChart margin={{ top: 12, right: 24, bottom: 8, left: 0 }}>
              <CartesianGrid stroke="var(--color-rule)" strokeDasharray="2 4" />
              <XAxis
                type="number"
                dataKey="d"
                domain={[0, 30]}
                ticks={[0, 5, 10, 15, 20, 25, 30]}
                tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
                stroke="var(--color-faint)"
                tickLine={false}
                label={{
                  value: "DAYS SINCE POLLS CLOSED",
                  position: "insideBottom",
                  offset: -4,
                  style: { fontFamily: "var(--font-mono)", fontSize: 10, fill: "var(--color-faint)", letterSpacing: "0.1em" },
                }}
              />
              <YAxis
                type="number"
                dataKey="p"
                domain={[0, 102]}
                ticks={[0, 25, 50, 75, 90, 100]}
                tickFormatter={(v: number) => `${v}%`}
                tick={{ fontFamily: "var(--font-mono)", fontSize: 11, fill: "var(--color-faint)" }}
                stroke="var(--color-faint)"
                tickLine={false}
                width={44}
              />
              <ReferenceLine
                y={90}
                stroke="var(--color-rust)"
                strokeWidth={1}
                label={{
                  value: "90%",
                  position: "right",
                  style: { fontFamily: "var(--font-mono)", fontSize: 10, fill: "var(--color-rust)" },
                }}
              />
              <Tooltip
                isAnimationActive={false}
                content={({ active, payload }) => {
                  if (!active || !payload?.length) return null;
                  const p = payload[0];
                  const d = p.payload as { d: number; p: number };
                  return (
                    <div className="border border-ink bg-paper px-3 py-2 text-sm shadow">
                      <div className="font-semibold">{p.name}</div>
                      <div className="stat-figure">
                        day {d.d}: {d.p}% counted
                      </div>
                    </div>
                  );
                }}
              />
              {elections.map((e) => {
                const isSel = selected === e.id;
                const muted = selected !== null && !isSel;
                const color = isSel ? KIND_COLOR[e.kind] : "var(--color-ink)";
                return (
                  <Line
                    key={e.id}
                    data={e.pts.map(([d, p]) => ({ d, p }))}
                    dataKey="p"
                    name={e.id}
                    stroke={color}
                    strokeOpacity={isSel ? 1 : muted ? 0.1 : 0.32}
                    strokeWidth={isSel ? 2.5 : 1.2}
                    strokeDasharray={e.source === "archival" ? "5 4" : undefined}
                    dot={
                      e.source === "archival" || isSel
                        ? { r: isSel ? 3 : 2.5, fill: color, fillOpacity: isSel ? 1 : 0.45, strokeWidth: 0 }
                        : false
                    }
                    isAnimationActive={false}
                    onClick={() => setSelected(isSel ? null : e.id)}
                  />
                );
              })}
            </ComposedChart>
          </ResponsiveContainer>
        </ChartFrame>

        <div>
          {sel ? (
            <DetailPanel e={sel} />
          ) : (
            <div className="border border-dashed border-rule p-4 text-sm italic leading-relaxed text-faint">
              Select an election above to see its canvass details: final count,
              night share, mail share, and days to each threshold.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
