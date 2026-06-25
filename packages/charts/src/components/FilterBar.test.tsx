import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import FilterBar from "./FilterBar";
import { LongCountProvider } from "../lib/context";
import { DEFAULT_STATE } from "../lib/useUrlState";
import { defaultTheme } from "../theme";

test("filter bar renders the six election-type chips", () => {
  render(
    <LongCountProvider
      value={{
        state: DEFAULT_STATE,
        update: () => {},
        elections: [],
        theme: defaultTheme,
      }}
    >
      <FilterBar />
    </LongCountProvider>,
  );
  for (const label of [
    "General",
    "Midterm",
    "Primary",
    "Local",
    "Special",
    "Recall",
  ]) {
    expect(screen.getByText(label)).toBeInTheDocument();
  }
});
