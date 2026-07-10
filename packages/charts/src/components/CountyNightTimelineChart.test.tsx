import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import CountyNightTimelineChart, { seriesFor } from "./CountyNightTimelineChart";
import type { CountyNightJurisdiction } from "../../../data/index";

test("county night-share timeline renders its title and one panel per complete county", () => {
  render(<CountyNightTimelineChart />);
  expect(
    screen.getByText("Election-night share over time, by county"),
  ).toBeInTheDocument();
  // the control + the five complete counties each get a panel heading
  for (const name of [
    "San Francisco",
    "Los Angeles",
    "Napa",
    "Nevada",
    "Orange",
    "San Mateo",
  ]) {
    expect(screen.getByText(name)).toBeInTheDocument();
  }
});

test("seriesFor picks the general row over a same-year primary row -- generals-only hold pending an editorial decision", () => {
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
    name: "Synthetic SF",
    slug: "synthetic-sf",
    control: true,
    complete: true,
    adoption: { epollbook: null, asv: null },
    points: [
      // the primary row is listed FIRST for the same year, reproducing the
      // real hazard: Array.find() would otherwise return array order, not
      // type -- e.g. real SF elections.json lists a June primary before its
      // November general within the same calendar year.
      point(2012, "presidential-primary", 12.3),
      point(2012, "presidential", 71.4),
    ],
  };

  const series = seriesFor(j);
  const y2012 = series.find((d) => d.year === 2012);
  expect(y2012?.v).toBe(71.4);
});
