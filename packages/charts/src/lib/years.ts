import { ELECTIONS, NIGHT_FLOOR, TURNOUT_HISTORY } from "@long-count/data";

export const YEAR_MIN = Math.min(
  ...ELECTIONS.map((e) => e.year),
  ...NIGHT_FLOOR.map((p) => Number(p.date.slice(0, 4))),
  // turnout data reaches 1899 (the night-count record starts 1908) — let the
  // year slider reach the earliest data so the turnout chart can show it
  ...TURNOUT_HISTORY.map((p) => Number(p.date.slice(0, 4))),
);
export const YEAR_MAX = Math.max(...ELECTIONS.map((e) => e.year));
