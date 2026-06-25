import { test, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { ChartFrame } from "./ui";

test("ChartFrame renders its title", () => {
  render(<ChartFrame title="Turnout of registered voters">x</ChartFrame>);
  expect(screen.getByText("Turnout of registered voters")).toBeInTheDocument();
});
