import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import CountyNightTimelineChart from "./CountyNightTimelineChart";

test("county night-share timeline renders its title and one panel per complete county", () => {
  render(<CountyNightTimelineChart />);
  expect(
    screen.getByText("Election-night share over time, by county"),
  ).toBeInTheDocument();
  // both controls + every complete county get a panel heading
  for (const name of [
    "San Francisco",
    "San Luis Obispo",
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
});
