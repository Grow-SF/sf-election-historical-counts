"use client";
import NightShareChart from "@/components/NightShareChart";
import { ELECTIONS, KINDS, YEAR_MIN, YEAR_MAX } from "@/lib/data";

/** The full, unfiltered election-night-share chart for the essay page. */
export default function EraChart() {
  return (
    <NightShareChart
      elections={ELECTIONS}
      from={YEAR_MIN}
      to={YEAR_MAX}
      kinds={new Set<string>(KINDS)}
    />
  );
}
