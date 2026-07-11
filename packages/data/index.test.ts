import { test, expect } from "vitest";
import { ELECTIONS, TURNOUT_HISTORY, FRANCHISE_FUNNEL } from "./index";

test("data package loads the election record", () => {
  expect(ELECTIONS.length).toBeGreaterThan(150);
  expect(ELECTIONS.find((e) => e.id === "2024-11-05")).toBeTruthy();
});

test("turnout history reaches back to the 19th century", () => {
  expect(TURNOUT_HISTORY.some((p) => p.date.startsWith("1879"))).toBe(true);
});

// The funnel bands must decompose the whole population: voted ⊆ registered ⊆
// eligible, and eligible + barred women fit inside the (both-sex) voting-age
// population, which fits inside total population.
test("franchise funnel layers nest", () => {
  for (const p of FRANCHISE_FUNNEL) {
    expect(p.voted).toBeLessThanOrEqual(p.registered);
    expect(p.eligible + p.barredWomen).toBeLessThanOrEqual(p.vap);
    expect(p.vap).toBeLessThanOrEqual(p.population);
  }
});

// Women were barred from voting in California until October 1911: the band is
// non-zero at every pre-suffrage presidential general and exactly zero after.
test("barred-women band exists before CA suffrage (1911) and vanishes after", () => {
  const pre = FRANCHISE_FUNNEL.filter((p) => p.year <= 1911);
  const post = FRANCHISE_FUNNEL.filter((p) => p.year >= 1912);
  expect(pre.length).toBeGreaterThanOrEqual(2); // 1900..1908 generals
  for (const p of pre) expect(p.barredWomen).toBeGreaterThan(50_000);
  for (const p of post) expect(p.barredWomen).toBe(0);
});

// The suffrage step must land in 1912, not be smeared to 1920 by interpolation:
// 1912's eligible electorate (now including women) must far exceed 1908's
// male-only one, and 1912 registration (134,688, women included) must fit.
test("1912 eligible reflects the suffrage step", () => {
  const p1908 = FRANCHISE_FUNNEL.find((p) => p.year === 1908)!;
  const p1912 = FRANCHISE_FUNNEL.find((p) => p.year === 1912)!;
  expect(p1912.eligible).toBeGreaterThan(1.5 * p1908.eligible);
  expect(p1912.registered).toBeLessThanOrEqual(p1912.eligible);
});
