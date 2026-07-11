import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import FranchiseFunnelChart from "./FranchiseFunnelChart";

// The full title is "Who could vote — and who did"; match the leading phrase.
test("franchise funnel renders its title", () => {
  render(<FranchiseFunnelChart from={1900} to={2026} />);
  expect(screen.getByText(/Who could vote/)).toBeInTheDocument();
});

// Pre-suffrage years must show the barred-women band in the legend…
test("legend lists the barred-women band when the range reaches pre-1911", () => {
  render(<FranchiseFunnelChart from={1900} to={2026} />);
  expect(screen.getByText(/women, barred until 1911/)).toBeInTheDocument();
});

// …and drop it when the whole visible range is post-suffrage.
test("legend omits the barred-women band for post-1911 ranges", () => {
  render(<FranchiseFunnelChart from={1960} to={2026} />);
  expect(screen.queryByText(/women, barred until 1911/)).toBeNull();
});
