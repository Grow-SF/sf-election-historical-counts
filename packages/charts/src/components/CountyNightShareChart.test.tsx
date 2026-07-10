import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import CountyNightShareChart from "./CountyNightShareChart";

test("county night-share chart renders its title, type toggle, and the SF control", () => {
  render(<CountyNightShareChart />);
  expect(
    screen.getByText("Did counting tech speed up election night?"),
  ).toBeInTheDocument();
  // the election-type toggle chips
  expect(screen.getByText("presidential")).toBeInTheDocument();
  expect(screen.getByText("midterm")).toBeInTheDocument();
  // San Francisco and Lake are the no-new-tech control rows
  expect(screen.getByText("San Francisco")).toBeInTheDocument();
  expect(screen.getByText("Lake")).toBeInTheDocument();
  expect(screen.getAllByText("no new tech")).toHaveLength(2);
});
