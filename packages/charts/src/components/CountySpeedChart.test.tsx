import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import CountySpeedChart from "./CountySpeedChart";

test("county speed chart renders its title", () => {
  render(<CountySpeedChart />);
  expect(
    screen.getByText("One week after Election Day, who's been counted?"),
  ).toBeInTheDocument();
});
