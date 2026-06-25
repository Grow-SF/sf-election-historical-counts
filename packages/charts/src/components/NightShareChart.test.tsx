import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import NightShareChart from "./NightShareChart";

test("night-share chart renders its title", () => {
  render(
    <NightShareChart elections={[]} from={1900} to={2026} kinds={new Set()} />,
  );
  expect(
    screen.getByText("How much of the vote was counted on election night"),
  ).toBeInTheDocument();
});
