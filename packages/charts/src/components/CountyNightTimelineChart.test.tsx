import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import CountyNightTimelineChart from "./CountyNightTimelineChart";

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
