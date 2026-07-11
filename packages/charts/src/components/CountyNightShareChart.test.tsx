import { render, screen, fireEvent } from "@testing-library/react";
import { test, expect } from "vitest";
import CountyNightShareChart, { prepost } from "./CountyNightShareChart";
import type { CountyNightJurisdiction } from "../../../data/index";

test("county night-share chart renders its title, all four type toggles, and the presidential-general controls", () => {
  const { container } = render(<CountyNightShareChart />);
  expect(
    screen.getByText("Did counting tech speed up election night?"),
  ).toBeInTheDocument();
  // the election-type toggle chips: two generals, two primaries
  expect(screen.getByText("presidential")).toBeInTheDocument();
  expect(screen.getByText("midterm")).toBeInTheDocument();
  expect(screen.getByText("pres. primary")).toBeInTheDocument();
  expect(screen.getByText("midterm primary")).toBeInTheDocument();
  // default view is presidential generals. San Francisco, San Luis Obispo,
  // Colusa, Del Norte, Lake, Mendocino, and Tehama are the no-new-tech
  // controls that clear the pre/post bar here: each has its own earliest
  // and most recent sourced presidential-general point (the control
  // pre-window is anchored to each county's own data, not a shared
  // adoption-year cutoff -- see prepost()).
  expect(screen.getByText("San Francisco")).toBeInTheDocument();
  expect(screen.getByText("San Luis Obispo")).toBeInTheDocument();
  expect(screen.getByText("Colusa")).toBeInTheDocument();
  expect(screen.getByText("Del Norte")).toBeInTheDocument();
  expect(screen.getByText("Lake")).toBeInTheDocument();
  expect(screen.getByText("Mendocino")).toBeInTheDocument();
  expect(screen.getByText("Tehama")).toBeInTheDocument();
  expect(screen.getAllByText("no new tech")).toHaveLength(7);
  // a treated county, unaffected by the control-anchor change
  expect(screen.getByText("Nevada")).toBeInTheDocument();
  // no bar is dimmed/dashed in the generals view
  expect(container.querySelectorAll('[stroke-dasharray="3 3"]')).toHaveLength(
    0,
  );
});

test("switching to the primary toggle renders primary-derived bars, dimmed and dashed, same-type paired", () => {
  const { container } = render(<CountyNightShareChart />);
  fireEvent.click(screen.getByText("pres. primary"));
  expect(
    screen.getByText(
      "Election-night share of the certified vote, before vs after adopting e-pollbooks / automated signature verification, presidential primaries",
    ),
  ).toBeInTheDocument();
  // counties with two sourced presidential-primary points clear the bar --
  // this is a smaller set than the presidential-general view, since fewer
  // counties have primary rows sourced yet.
  expect(screen.getByText("San Francisco")).toBeInTheDocument();
  expect(screen.getByText("Del Norte")).toBeInTheDocument();
  expect(screen.getByText("Lake")).toBeInTheDocument();
  expect(screen.getByText("Mendocino")).toBeInTheDocument();
  expect(screen.getByText("Tehama")).toBeInTheDocument();
  expect(screen.getAllByText("no new tech")).toHaveLength(5);
  // Colusa has no sourced presidential-primary rows at all, so it still
  // doesn't clear the bar in this view (unlike the generals view).
  expect(screen.queryByText("Colusa")).not.toBeInTheDocument();
  // every rendered bar is dimmed + dashed to mark it as primary-derived
  const dashed = container.querySelectorAll('[stroke-dasharray="3 3"]');
  expect(dashed.length).toBeGreaterThan(0);
});

test("prepost pairs pre/post points of the SAME type only, generals or primaries alike", () => {
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
      // if these leaked into the general pairing they'd change the result.
      point(2014, "midterm-primary", 5),
      point(2022, "midterm-primary", 95),
    ],
  };

  const generalRow = prepost(j, "midterm");
  expect(generalRow).not.toBeNull();
  expect(generalRow?.pre).toBe(40);
  expect(generalRow?.post).toBe(70);
  expect(generalRow?.change).toBe(30);

  // primaries now render too, paired against each other, same as generals --
  // the pts.length < 2 bar still applies, just per-type.
  const primaryRow = prepost(j, "midterm-primary");
  expect(primaryRow).not.toBeNull();
  expect(primaryRow?.pre).toBe(5);
  expect(primaryRow?.post).toBe(95);
  expect(primaryRow?.change).toBe(90);

  // a jurisdiction with ONLY primary points renders no general-type bar...
  const primaryOnly: CountyNightJurisdiction = {
    ...j,
    slug: "primary-only",
    points: [point(2014, "midterm-primary", 5), point(2022, "midterm-primary", 95)],
  };
  expect(prepost(primaryOnly, "midterm")).toBeNull();
  // ...but DOES render its primary-type bar, now that primaries are shown.
  const primaryOnlyRow = prepost(primaryOnly, "midterm-primary");
  expect(primaryOnlyRow).not.toBeNull();
  expect(primaryOnlyRow?.pre).toBe(5);
  expect(primaryOnlyRow?.post).toBe(95);
});

test("prepost anchors a CONTROL county's pre-window to its own earliest sourced point, not a shared cutoff year", () => {
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

  // this control county's earliest sourced point (2016) falls AFTER other
  // counties' adoption years. A shared global-cutoff anchor (the pre-fix
  // EARLIEST_ADOPT approach) would find no point before that cutoff and drop
  // the county's bar entirely -- the exact Del Norte regression this fixes.
  // The own-data anchor uses the county's own earliest/latest points instead.
  const j: CountyNightJurisdiction = {
    name: "Synthetic Control",
    slug: "synthetic-control",
    control: true,
    complete: true,
    adoption: { epollbook: null, asv: null },
    points: [point(2016, "presidential", 80), point(2024, "presidential", 60)],
  };

  const row = prepost(j, "presidential");
  expect(row).not.toBeNull();
  expect(row?.pre).toBe(80);
  expect(row?.preYear).toBe(2016);
  expect(row?.post).toBe(60);
  expect(row?.postYear).toBe(2024);
  expect(row?.change).toBe(-20);
});

test("prepost still requires a real pre-adoption point for TREATED counties -- no own-data fallback", () => {
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

  // both sourced points are at/after the adoption year (2018), so there's no
  // "last election before adoption" point. Unlike a control, a treated
  // county does NOT fall back to its own earliest point here -- the pre/post
  // split has to bracket its actual adoption year to mean anything.
  const j: CountyNightJurisdiction = {
    name: "Synthetic Treated",
    slug: "synthetic-treated",
    control: false,
    complete: true,
    adoption: { epollbook: 2018, asv: null },
    points: [point(2018, "presidential", 80), point(2024, "presidential", 60)],
  };

  expect(prepost(j, "presidential")).toBeNull();
});
