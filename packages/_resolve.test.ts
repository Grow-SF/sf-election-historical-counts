import { test, expect } from "vitest";
test("public subpaths resolve", async () => {
  const data = await import("long-count/data");
  const charts = await import("long-count/charts");
  expect(Array.isArray((data as any).ELECTIONS)).toBe(true);
  expect(typeof (charts as any).LongCount).toBe("function");
});
