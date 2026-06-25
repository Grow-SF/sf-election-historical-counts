import { test, expect } from "vitest";
import { defaultTheme } from "./theme";

test("default theme carries the GrowSF chart colors", () => {
  expect(defaultTheme.colorsByKind.General).toBe("#0A82B2");
  expect(defaultTheme.colorsByKind.Midterm).toBe("#7E5AA8");
  expect(defaultTheme.colorsByKind.Local).toBe("#01384F");
  expect(defaultTheme.gold).toMatch(/^#|^var\(/);
  expect(defaultTheme.formatPct(74.31)).toBe("74.31%");
});
