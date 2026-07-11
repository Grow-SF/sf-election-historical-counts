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
  // voting-age population, BOTH sexes (21+ through the 1968 election, 18+ after)
  vap: number;
  // eligible electorate: citizen men 21+ through 1908; citizen adults from 1912
  // (California enfranchised women in October 1911)
  eligible: number;
  registered: number;
  voted: number;
  // adult women barred from voting — non-zero only before CA suffrage (1911)
  barredWomen: number;
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

// County counting-tech + reporting-speed comparison (tidy/long; see
// scripts/research/merge_county_tech.py).
export type CountyTechMetric = {
  jurisdiction: string;
  state: string;
  metric: "oneweek_pct" | "electionnight_pct" | "days_to_90" | "days_to_cert";
  year: number;
  value: number | null;
  denominator: string | null;
  source_url: string | null;
  confidence: "primary" | "secondary" | "estimated" | "none";
  note: string;
};

export type CountyTechAdoption = {
  jurisdiction: string;
  state: string;
  tech: "epollbook" | "asv" | "sign-scan-go" | "vote-center";
  status: "adopted" | "not-adopted" | "unknown";
  adopted_year: number | null;
  first_election: string | null;
  vendor: string | null;
  evidence_url: string;
  confidence: "primary" | "secondary" | "estimated" | "none";
  note: string;
};

export type CountyTech = {
  metrics: CountyTechMetric[];
  adoptions: CountyTechAdoption[];
};

// Cross-county ELECTION-NIGHT share comparison (last election-night report ÷
// certified final), with San Francisco as the no-new-tech control. Built by
// scripts/build_county_night.py from data/research/election-night-*/.
// type vocabulary: "presidential"/"midterm" are November generals;
// "presidential-primary"/"midterm-primary" are statewide primaries (see the
// build_county_night.py docstring). Charts currently render generals only --
// primaries are excluded at each chart's data-selection boundary pending an
// editorial decision on how to display them.
export type CountyNightPoint = {
  year: number;
  type: "presidential" | "midterm" | "presidential-primary" | "midterm-primary";
  pct: number | null;
  ballots: number | null;
  final: number | null;
  confidence: string | null;
  comparable: boolean;
  source_url: string | null;
  // true only when the night figure is a press-deadline partial rather than
  // a full report (mirrors Election.nightPartial in elections.json).
  nightPartial?: boolean;
};

export type CountyNightJurisdiction = {
  name: string;
  slug: string;
  control: boolean;
  // true = every Nov-general row has a sourced election-night count (fully
  // recovered). The chart shows only complete jurisdictions (+ the control).
  complete: boolean;
  // vca = Voter's Choice Act all-mail / vote-center adoption year (from the
  // CA adoption census). Optional so existing fixtures that predate the field
  // still type-check; build_county_night.py always emits it.
  adoption: { epollbook: number | null; asv: number | null; vca?: number | null };
  points: CountyNightPoint[];
};

export type CountyNight = {
  metric: string;
  note: string;
  source: string;
  generated: string;
  jurisdictions: CountyNightJurisdiction[];
};
