import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import CountyNightTimelineChart, { seriesFor } from "./CountyNightTimelineChart";
import type { CountyNightJurisdiction } from "../../../data/index";

test("county night-share timeline renders its title, one panel per shown county, and a dimmed primary line alongside the solid general line", () => {
  const { container } = render(<CountyNightTimelineChart />);
  expect(
    screen.getByText("Election-night share over time, by county"),
  ).toBeInTheDocument();
  // SF + every COMPLETE jurisdiction gets a panel: the complete controls
  // (San Luis Obispo, Del Norte, Lake, Mendocino) render alongside the
  // treated counties so the no-tech decay is visible per county; the still
  // incomplete controls (Tehama, Colusa) live only in CountyNightShareChart's
  // per-control pre/post bars.
  for (const name of [
    "San Francisco",
    "San Luis Obispo",
    "Del Norte",
    "Lake",
    "Mendocino",
    "Los Angeles",
    "Napa",
    "Nevada",
    "Orange",
    "San Mateo",
    "Ventura",
    "Santa Clara",
    "San Diego",
    "Fresno",
    "Riverside",
  ]) {
    expect(screen.getByText(name)).toBeInTheDocument();
  }
  // every panel draws a dimmed, dashed primary line (stroke-dasharray "2 3")
  // alongside the solid general line -- primaries render alongside generals,
  // not hidden behind a separate view, in this chart.
  expect(
    container.querySelectorAll('[stroke-dasharray="2 3"]').length,
  ).toBeGreaterThan(0);
});

test("seriesFor keeps the general and same-year primary as separate series -- v is the general, primary is the primary", () => {
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
  // the general series is unaffected by array order, as before...
  expect(y2012?.v).toBe(71.4);
  // ...but the primary is no longer discarded: it now renders as its own
  // series value instead of being held out of the chart entirely.
  expect(y2012?.primary).toBe(12.3);
});

test("seriesFor picks the type-matching primary for the year (presidential-primary in presidential years, midterm-primary in midterms)", () => {
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
      point(2014, "midterm", 60),
      point(2014, "midterm-primary", 55),
      point(2016, "presidential", 65),
      point(2016, "presidential-primary", 62),
    ],
  };

  const series = seriesFor(j);
  const y2014 = series.find((d) => d.year === 2014);
  expect(y2014?.v).toBe(60);
  expect(y2014?.primary).toBe(55);
  const y2016 = series.find((d) => d.year === 2016);
  expect(y2016?.v).toBe(65);
  expect(y2016?.primary).toBe(62);
  // years with no sourced point at all stay null for both series
  const y2018 = series.find((d) => d.year === 2018);
  expect(y2018?.v).toBeNull();
  expect(y2018?.primary).toBeNull();
});
