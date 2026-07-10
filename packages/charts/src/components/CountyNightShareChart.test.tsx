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
  // San Francisco, Lake, and Mendocino are the no-new-tech control rows that
  // clear the chart's pre/post bar: each has a pre-window and a post-window
  // same-type sourced point. The control window is EARLIEST_ADOPT, the
  // earliest adoption year among complete treated counties -- now 2014, after
  // the 2026-07-10 Nevada tech adjudication re-keyed Nevada's e-pollbook
  // adoption from 2018 to 2014 (its traditional precinct e-pollbooks were
  // fully deployed countywide by the Nov 2014 general). SF/Lake/Mendocino
  // each have a 2012 presidential point (< 2014) and later ones, so they
  // still render. Del Norte NO LONGER renders: its only pre-2014 general
  // (2012) is a documented null, leaving it with no pre-window point once the
  // window moved to 2014 (before the Nevada correction, when EARLIEST_ADOPT
  // was 2018, Del Norte's 2014/2016 points bracketed the window and it did
  // render). Tehama is a control county (control:true) but its two sourced
  // rows split across both election types (2022 midterm, 2024 presidential),
  // so it never has 2 same-type points; Colusa is a control whose six rows
  // are all documented nulls -- neither clears prepost()'s pts.length < 2 bar.
  expect(screen.getByText("San Francisco")).toBeInTheDocument();
  expect(screen.getByText("Lake")).toBeInTheDocument();
  expect(screen.getByText("Mendocino")).toBeInTheDocument();
  expect(screen.queryByText("Del Norte")).not.toBeInTheDocument();
  expect(screen.queryByText("Tehama")).not.toBeInTheDocument();
  expect(screen.queryByText("Colusa")).not.toBeInTheDocument();
  expect(screen.getAllByText("no new tech")).toHaveLength(3);
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
