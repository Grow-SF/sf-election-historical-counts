import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import RegistrationChart from "./RegistrationChart";

test("registration chart renders its title", () => {
  render(<RegistrationChart from={1900} to={2026} />);
  expect(
    screen.getByText("Registration among eligible citizens"),
  ).toBeInTheDocument();
});
