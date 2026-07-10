import { test, expect } from "vitest";
import { ELECTIONS, TURNOUT_HISTORY, COUNTY_NIGHT } from "./index";

test("data package loads the election record", () => {
  expect(ELECTIONS.length).toBeGreaterThan(150);
  expect(ELECTIONS.find((e) => e.id === "2024-11-05")).toBeTruthy();
});

test("turnout history reaches back to the 19th century", () => {
  expect(TURNOUT_HISTORY.some((p) => p.date.startsWith("1879"))).toBe(true);
});

test("at least two jurisdictions are marked as the no-new-tech control", () => {
  const controls = COUNTY_NIGHT.jurisdictions.filter((j) => j.control);
  expect(controls.length).toBeGreaterThanOrEqual(2);
});
