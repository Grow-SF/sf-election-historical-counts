import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import TurnoutChart from "./TurnoutChart";

test("turnout chart shows the Midterm series in its legend", () => {
  render(
    <TurnoutChart from={1900} to={2026} kinds={new Set(["General", "Midterm"])} />,
  );
  expect(screen.getByText("Midterm")).toBeInTheDocument();
});
