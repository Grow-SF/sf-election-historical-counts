import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import CountyNightShareChart, { prepost } from "./CountyNightShareChart";
import type { CountyNightJurisdiction } from "../../../data/index";

test("county night-share chart renders its title, type toggle, and the SF control", () => {
  render(<CountyNightShareChart />);
  expect(
    screen.getByText("Did counting tech speed up election night?"),
  ).toBeInTheDocument();
  // the election-type toggle chips
  expect(screen.getByText("presidential")).toBeInTheDocument();
  expect(screen.getByText("midterm")).toBeInTheDocument();
  // San Francisco, Lake, Del Norte, and Mendocino are the no-new-tech control
  // rows that clear the chart's pre/post bar (2+ same-type sourced points).
  // Tehama is also a control county (county_night.json control:true) but its
  // two sourced rows split across both election types (2022 midterm, 2024
  // presidential), so it never has 2 same-type points and does not render a
  // bar here; see docs/research/RUNBOOK.md and the task report. Colusa is
  // also a control county but every one of its six election-night rows is a
  // documented null (no surviving on-night report was ever found), so it has
  // ZERO sourced points of any type and never clears prepost()'s pts.length
  // < 2 bar either -- same non-render outcome as Tehama, for a stronger
  // reason (no data at all, not just a type mismatch).
  expect(screen.getByText("San Francisco")).toBeInTheDocument();
  expect(screen.getByText("Lake")).toBeInTheDocument();
  expect(screen.getByText("Del Norte")).toBeInTheDocument();
  expect(screen.getByText("Mendocino")).toBeInTheDocument();
  expect(screen.queryByText("Tehama")).not.toBeInTheDocument();
  expect(screen.queryByText("Colusa")).not.toBeInTheDocument();
  expect(screen.getAllByText("no new tech")).toHaveLength(4);
});

test("prepost excludes primary-typed points -- generals-only hold pending an editorial decision", () => {
  const point = (
    year: number,
    type: CountyNightJurisdiction["points"][number]["type"],
    pct: number,
  ) => ({
    year,
    type,
    pct,
    ballots: null,
    final: null,
    confidence: null,
    comparable: true,
    source_url: null,
  });

  const j: CountyNightJurisdiction = {
    name: "Synthetic County",
    slug: "synthetic-county",
    control: false,
    complete: true,
    adoption: { epollbook: 2018, asv: null },
    points: [
      point(2014, "midterm", 40),
      point(2022, "midterm", 70),
      // synthetic primary points, both far outside the general values --
      // if these leaked in they would change pre/post/change materially.
      point(2014, "midterm-primary", 5),
      point(2022, "midterm-primary", 95),
    ],
  };

  const row = prepost(j, "midterm");
  expect(row).not.toBeNull();
  expect(row?.pre).toBe(40);
  expect(row?.post).toBe(70);
  expect(row?.change).toBe(30);

  // a jurisdiction with ONLY primary points must not render a bar at all.
  const primaryOnly: CountyNightJurisdiction = {
    ...j,
    slug: "primary-only",
    points: [point(2014, "midterm-primary", 5), point(2022, "midterm-primary", 95)],
  };
  expect(prepost(primaryOnly, "midterm")).toBeNull();
});
