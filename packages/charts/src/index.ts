"use client";
import "./charts.css";

// The Long Count provider + the embeddable content wrappers it backs.
// The whole public surface is client-only (hooks, context, recharts), so the
// barrel carries the directive — otherwise a Server Component importing it pulls
// theme.tsx's top-level createContext into the RSC graph, where it throws.
export {
  default as LongCount,
  NightShare,
  Vbm,
  Turnout,
  Registration,
  FranchiseFunnel,
  Trajectory,
  HelpWanted,
  MethodNote,
} from "./components/LongCount";

// Theme surface for host apps that want to override the defaults.
export { defaultTheme } from "./theme";
export type { ChartsTheme } from "./theme";

// Raw charts for standalone use (outside the provider).
export { default as NightShareChart } from "./components/NightShareChart";
export { default as TurnoutChart } from "./components/TurnoutChart";
export { default as VbmChart } from "./components/VbmChart";
export { default as RegistrationChart } from "./components/RegistrationChart";
export { default as FranchiseFunnelChart } from "./components/FranchiseFunnelChart";
export { default as TrajectoryExplorer } from "./components/TrajectoryExplorer";
export { default as FilterBar } from "./components/FilterBar";
