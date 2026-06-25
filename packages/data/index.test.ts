import { test, expect } from "vitest";
import { ELECTIONS, TURNOUT_HISTORY } from "./index.js";

test("data package loads the election record", () => {
  expect(ELECTIONS.length).toBeGreaterThan(150);
  expect(ELECTIONS.find((e) => e.id === "2024-11-05")).toBeTruthy();
});

test("turnout history reaches back to the 19th century", () => {
  expect(TURNOUT_HISTORY.some((p) => p.date.startsWith("1879"))).toBe(true);
});
