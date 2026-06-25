/** Fractional year of an election date, for regression and x-axes. */
export function yearFrac(id: string): number {
  const d = new Date(id + "T00:00:00");
  return d.getFullYear() + (d.getMonth() + (d.getDate() - 1) / 31) / 12;
}

/**
 * Vote-counting milestones, annotated identically across every chart (each
 * renders only the events within its own x-domain).
 */
export const EVENTS: { year: number; label: string }[] = [
  { year: 1926, label: "voting machines" },
  { year: 1978, label: "expanded absentee" },
  { year: 2002, label: "permanent VBM" },
  { year: 2020, label: "COVID" },
];

/**
 * Franchise-expansion milestones — used only on the "who could vote" charts
 * (franchise funnel, registration); the counting charts use EVENTS above.
 */
export const FRANCHISE_EVENTS: { year: number; label: string }[] = [
  { year: 1920, label: "women vote" },
  { year: 1971, label: "age 18" },
];

/** ~6 evenly spaced round-year ticks spanning [from, to], for a year x-axis. */
export function yearTicks(from: number, to: number): number[] {
  const span = Math.max(1, to - from);
  const step = [5, 10, 20, 25, 50].find((s) => span / s <= 7) ?? 50;
  const ticks: number[] = [];
  for (let t = Math.ceil(from / step) * step; t <= to; t += step) ticks.push(t);
  return ticks;
}
