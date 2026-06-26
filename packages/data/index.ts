import elections from "./elections.json";
import turnoutHistory from "./turnout_history.json";
import nightFloor from "./night_floor.json";
import vbmHistory from "./vbm_history.json";
import registrationEligible from "./registration_eligible.json";
import franchiseFunnel from "./franchise_funnel.json";
import countySpeed from "./county_speed.json";
import sources from "./sources.json";
import ledger from "./ledger.json";
import type {
  Election, TurnoutPoint, FloorPoint, VbmPoint, RegEligPoint, FunnelPoint,
  CountySpeed,
} from "./types";

export * from "./types";
export const ELECTIONS = elections as unknown as Election[];
export const TURNOUT_HISTORY = turnoutHistory as TurnoutPoint[];
export const NIGHT_FLOOR = nightFloor as FloorPoint[];
export const VBM_HISTORY = vbmHistory as VbmPoint[];
export const REGISTRATION_ELIGIBLE = registrationEligible as RegEligPoint[];
export const FRANCHISE_FUNNEL = franchiseFunnel as FunnelPoint[];
export const COUNTY_SPEED = countySpeed as CountySpeed;
export const SOURCES = sources as Record<string, unknown>[];
export const LEDGER = ledger as { text: string };
