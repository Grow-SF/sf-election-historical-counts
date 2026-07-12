import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import NightShareChart from "./NightShareChart";
import { SanDiegoNightShare } from "./LongCount";

test("night-share chart renders its title", () => {
  render(
    <NightShareChart elections={[]} from={1900} to={2026} kinds={new Set()} />,
  );
  expect(
    screen.getByText("How much of the vote was counted on election night"),
  ).toBeInTheDocument();
});

test("night-share chart config overrides title and hides the SF footer", () => {
  render(
    <NightShareChart
      elections={[]}
      from={1868}
      to={2026}
      kinds={new Set()}
      config={{ title: "San Diego test title", footer: null }}
    />,
  );
  expect(screen.getByText("San Diego test title")).toBeInTheDocument();
  expect(screen.queryByText(/dashed verticals/)).not.toBeInTheDocument();
});

test("San Diego island renders from the baked dataset", () => {
  render(<SanDiegoNightShare />);
  expect(
    screen.getByText(
      "San Diego County: how much of the vote was counted on election night",
    ),
  ).toBeInTheDocument();
});
