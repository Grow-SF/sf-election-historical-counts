import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import VbmChart from "./VbmChart";

test("vbm chart renders its title", () => {
  render(<VbmChart from={1900} to={2026} />);
  expect(
    screen.getByText("Vote-by-mail share of ballots cast"),
  ).toBeInTheDocument();
});
