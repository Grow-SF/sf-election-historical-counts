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
  // San Francisco, Lake, Del Norte, and Mendocino are the no-new-tech control
  // rows that clear the chart's pre/post bar (2+ same-type sourced points).
  // Tehama is also a control county (county_night.json control:true) but its
  // two sourced rows split across both election types (2022 midterm, 2024
  // presidential), so it never has 2 same-type points and does not render a
  // bar here; see docs/research/RUNBOOK.md and the task report.
  expect(screen.getByText("San Francisco")).toBeInTheDocument();
  expect(screen.getByText("Lake")).toBeInTheDocument();
  expect(screen.getByText("Del Norte")).toBeInTheDocument();
  expect(screen.getByText("Mendocino")).toBeInTheDocument();
  expect(screen.queryByText("Tehama")).not.toBeInTheDocument();
  expect(screen.getAllByText("no new tech")).toHaveLength(4);
});
