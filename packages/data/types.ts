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

export type FunnelPoint = {
  year: number;
  population: number;
  vap: number;
  eligible: number;
  registered: number;
  voted: number;
};

// California county counting-speed comparison (vote-by-mail era).
export type CountySpeedRow = {
  county: string;
  // true = adopted electronic pollbooks; false = has not; null = statewide aggregate
  epollbook: boolean | null;
  // year (as a string key) -> % of ballots counted within one week of Election Day
  rates: Record<string, number>;
};

export type CountySpeed = {
  metric: string;
  source: string;
  sourceUrl: string;
  years: number[];
  counties: CountySpeedRow[];
};
