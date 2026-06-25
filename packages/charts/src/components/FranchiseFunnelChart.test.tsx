import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import FranchiseFunnelChart from "./FranchiseFunnelChart";

// The full title is "Who could vote — and who did"; match the leading phrase.
test("franchise funnel renders its title", () => {
  render(<FranchiseFunnelChart from={1900} to={2026} />);
  expect(screen.getByText(/Who could vote/)).toBeInTheDocument();
});
