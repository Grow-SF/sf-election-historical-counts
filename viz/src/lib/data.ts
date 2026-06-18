import elections from "@/data/elections.json";
import vbmHistory from "@/data/vbm_history.json";
import nightFloor from "@/data/night_floor.json";
import turnoutHistory from "@/data/turnout_history.json";
import registrationEligible from "@/data/registration_eligible.json";
import franchiseFunnel from "@/data/franchise_funnel.json";

export type Threshold = { days: number; bound: boolean };

export type Election = {
  id: string;
  name: string;
  kind: "Primary" | "General" | "Municipal" | "Special" | "Recall";
  year: number;
  final: number;
  registered: number | null;
  source: "exact" | "archival";
  provisional: boolean;
  nReports: number;
  nightPct: number | null;
  nightPartial?: boolean;
  nightSrc?: string | null;
  srcShort?: string | null;
  vbmShare: number | null;
  pts: [number, number, number | null, number | null][];
  thresholds: Record<string, Threshold>;
};

export type VbmPoint = { date: string; share: number; source: string };

export type FloorPoint = { date: string; floorPct: number; source: string; kind: string };

export type TurnoutPoint = {
  date: string;
  turnoutPct: number;
  registered: number;
  ballots: number;
  kind: string;
  source: string;
};

export const ELECTIONS = elections as unknown as Election[];
export const VBM_HISTORY = vbmHistory as VbmPoint[];
export const NIGHT_FLOOR = nightFloor as FloorPoint[];
export const TURNOUT_HISTORY = turnoutHistory as TurnoutPoint[];

export type RegEligPoint = {
  date: string;
  eligible: number;
  registered: number;
  pct: number;
  context: string;
  source: "sos-ror" | "sov-print";
  recovered: boolean;
  confidence?: string;
};
export const REGISTRATION_ELIGIBLE = registrationEligible as RegEligPoint[];

export type FunnelPoint = {
  year: number;
  population: number;
  vap: number;
  eligible: number;
  registered: number;
  voted: number;
};
export const FRANCHISE_FUNNEL = franchiseFunnel as FunnelPoint[];

export const KINDS = ["General", "Primary", "Municipal", "Special", "Recall"] as const;
export const THRESHOLDS = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 98, 99];

export const YEAR_MIN = Math.min(
  ...ELECTIONS.map((e) => e.year),
  ...NIGHT_FLOOR.map((p) => Number(p.date.slice(0, 4))),
  // turnout data reaches 1899 (the night-count record starts 1868) — let the
  // year slider reach the earliest data so the turnout chart can show it
  ...TURNOUT_HISTORY.map((p) => Number(p.date.slice(0, 4))),
);
export const YEAR_MAX = Math.max(...ELECTIONS.map((e) => e.year));

/** Fractional year of an election date, for regression and x-axes. */
export function yearFrac(id: string): number {
  const d = new Date(id + "T00:00:00");
  return d.getFullYear() + (d.getMonth() + (d.getDate() - 1) / 31) / 12;
}

export type Filters = {
  kinds: Set<string>;
  from: number;
  to: number;
};

export function filterElections(f: Filters): Election[] {
  return ELECTIONS.filter(
    (e) =>
      f.kinds.has(e.kind) &&
      e.year >= f.from &&
      e.year <= f.to,
  );
}

export type Fit = {
  slope: number;
  intercept: number;
  r2: number;
  n: number;
  x0: number;
  x1: number;
};

/** Ordinary least squares over (x, y); returns null when underdetermined. */
export function linearFit(pts: [number, number][]): Fit | null {
  const n = pts.length;
  if (n < 3) return null;
  const mx = pts.reduce((s, p) => s + p[0], 0) / n;
  const my = pts.reduce((s, p) => s + p[1], 0) / n;
  let sxx = 0,
    sxy = 0,
    syy = 0;
  for (const [x, y] of pts) {
    sxx += (x - mx) ** 2;
    sxy += (x - mx) * (y - my);
    syy += (y - my) ** 2;
  }
  if (sxx === 0 || syy === 0) return null;
  const slope = sxy / sxx;
  const r2 = (sxy * sxy) / (sxx * syy);
  const xs = pts.map((p) => p[0]);
  return {
    slope,
    intercept: my - slope * mx,
    r2,
    n,
    x0: Math.min(...xs),
    x1: Math.max(...xs),
  };
}

export const fmt = (n: number) => n.toLocaleString("en-US");

// Categorical palette: a GrowSF blue family for the regular election types
// (bright → muted → navy), sea green for specials, and a light red for recalls.
export const KIND_COLOR: Record<string, string> = {
  General: "#0A82B2", // bright primary blue
  Primary: "#EBAB5A", // yellow
  Municipal: "#01384F", // deep navy blue
  Special: "#1E7B6A", // sea green
  Recall: "#E36246", // light red
};

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

/** ~6 evenly spaced round-year ticks spanning [from, to], for a year x-axis. */
export function yearTicks(from: number, to: number): number[] {
  const span = Math.max(1, to - from);
  const step = [5, 10, 20, 25, 50].find((s) => span / s <= 7) ?? 50;
  const ticks: number[] = [];
  for (let t = Math.ceil(from / step) * step; t <= to; t += step) ticks.push(t);
  return ticks;
}
