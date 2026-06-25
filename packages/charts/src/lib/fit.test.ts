import { test, expect } from "vitest";
import { linearFit } from "./fit";
test("recovers a perfect linear slope", () => {
  const fit = linearFit([[0,0],[1,2],[2,4]]);
  expect(fit?.slope).toBeCloseTo(2); expect(fit?.r2).toBeCloseTo(1);
});
