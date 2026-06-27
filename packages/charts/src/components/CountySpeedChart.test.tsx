import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import CountySpeedChart from "./CountySpeedChart";

test("county speed chart renders its title and metric chips", () => {
  render(<CountySpeedChart />);
  expect(
    screen.getByText("How fast do California counties count?"),
  ).toBeInTheDocument();
  // the three metric selector chips
  expect(screen.getByText("within 1 week")).toBeInTheDocument();
  expect(screen.getByText("days to 90% counted")).toBeInTheDocument();
});
