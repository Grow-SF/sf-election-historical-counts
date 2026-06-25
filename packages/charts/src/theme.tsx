import { createContext, useContext } from "react";

export type ChartsTheme = {
  colorsByKind: Record<string, string>;
  ink: string; paper: string; faint: string; rule: string; gold: string;
  fontMono: string;
  formatNumber: (n: number) => string;
  formatPct: (n: number) => string;
  formatDate: (iso: string) => string;
};

export const defaultTheme: ChartsTheme = {
  colorsByKind: {
    General: "#0A82B2", Midterm: "#7E5AA8", Primary: "#EBAB5A",
    Local: "#01384F", Special: "#1E7B6A", Recall: "#E36246",
  },
  ink: "var(--lc-ink)", paper: "var(--lc-paper)", faint: "var(--lc-faint)",
  rule: "var(--lc-rule)", gold: "var(--lc-gold)", fontMono: "var(--lc-font-mono)",
  formatNumber: (n) => n.toLocaleString("en-US"),
  formatPct: (n) => `${n}%`,
  formatDate: (iso) => iso,
};

const ThemeContext = createContext<ChartsTheme>(defaultTheme);
export const ChartsThemeProvider = ThemeContext.Provider;
export function useChartTheme(): ChartsTheme { return useContext(ThemeContext); }
