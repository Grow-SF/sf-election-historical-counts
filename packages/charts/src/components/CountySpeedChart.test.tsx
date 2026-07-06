import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import CountySpeedChart from "./CountySpeedChart";

test("county speed chart renders its title and viz chips", () => {
  render(<CountySpeedChart />);
  expect(
    screen.getByText("How fast do California counties count?"),
  ).toBeInTheDocument();
  // the three visualization-type chips
  expect(screen.getByText("arrows")).toBeInTheDocument();
  expect(screen.getByText("change")).toBeInTheDocument();
  expect(screen.getByText("timeline")).toBeInTheDocument();
});
