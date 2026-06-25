import { test, expect } from "vitest";
import { filterElections } from "./filter";
const E = (id: string, kind: string, year: number) =>
  ({ id, kind, year } as any);

test("filters by display category and year window", () => {
  const all = [E("1962-11-06","General",1962), E("1960-11-08","General",1960), E("1971-11-02","Municipal",1971)];
  const got = filterElections(all, { kinds: new Set(["Midterm"]), from: 1900, to: 2000 });
  expect(got.map((e) => e.id)).toEqual(["1962-11-06"]);
});
