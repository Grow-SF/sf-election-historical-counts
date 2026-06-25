import { test, expect } from "vitest";
import { displayKind, KINDS } from "./categories";

test("presidential vs midterm general split by year parity", () => {
  expect(displayKind("General", 1960)).toBe("General");
  expect(displayKind("General", 1962)).toBe("Midterm");
});
test("Municipal renders as Local", () => {
  expect(displayKind("Municipal", 1971)).toBe("Local");
});
test("other kinds pass through", () => {
  expect(displayKind("Primary", 1968)).toBe("Primary");
});
test("KINDS lists the six display categories in order", () => {
  expect([...KINDS]).toEqual(["General","Midterm","Primary","Local","Special","Recall"]);
});
