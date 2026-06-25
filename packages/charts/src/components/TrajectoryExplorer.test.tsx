import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import TrajectoryExplorer from "./TrajectoryExplorer";

const noop = () => {};

// Perf-hidden in the embed; the smoke just confirms it renders without throwing.
test("trajectory explorer renders without throwing", () => {
  render(
    <TrajectoryExplorer
      elections={[]}
      selected={new Set()}
      toggleSelected={noop}
      clearSelected={noop}
      dayFrom={0}
      dayTo={10}
      setDayRange={noop}
    />,
  );
  expect(screen.getByText("The count, release by release")).toBeInTheDocument();
});
