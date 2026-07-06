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
  // San Francisco is the no-new-tech control row
  expect(screen.getByText("San Francisco")).toBeInTheDocument();
  expect(screen.getByText("no new tech")).toBeInTheDocument();
});
