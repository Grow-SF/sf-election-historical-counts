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
  // San Francisco, Lake, Mendocino, Del Norte, and Tehama are the
  // no-new-tech control rows that clear the chart's pre/post bar: each has a
  // pre-window and a post-window same-type sourced point. The control window
  // is EARLIEST_ADOPT, the earliest adoption year among complete treated
  // counties -- 2014, since the 2026-07-10 Nevada tech adjudication re-keyed
  // Nevada's e-pollbook adoption from 2018 to 2014. SF/Lake/Mendocino each
  // have a 2012 presidential point (< 2014) and later ones, so they render.
  // Del Norte's and Tehama's 2012 presidential-general points were
  // documented nulls until the 2026-07-10 CA SoS status-page sweep landed
  // them (Del Norte 8,067/8,879 = 90.85%, PLAUSIBLE; Tehama 17,559/23,261 =
  // 75.49%, PLAUSIBLE); both now bracket the 2014 window the same way
  // SF/Lake/Mendocino do (earlier, before those rows were sourced, neither
  // rendered here). Colusa is a control whose sourced rows (now including
  // several generals from the same sweep) are all 2014 or later, so it still
  // has no pre-2014 point of either type and doesn't clear prepost()'s
  // pts.length < 2 / no-pre-window bar.
  expect(screen.getByText("San Francisco")).toBeInTheDocument();
  expect(screen.getByText("Lake")).toBeInTheDocument();
  expect(screen.getByText("Mendocino")).toBeInTheDocument();
  expect(screen.getByText("Del Norte")).toBeInTheDocument();
  expect(screen.getByText("Tehama")).toBeInTheDocument();
  expect(screen.queryByText("Colusa")).not.toBeInTheDocument();
  expect(screen.getAllByText("no new tech")).toHaveLength(5);
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
