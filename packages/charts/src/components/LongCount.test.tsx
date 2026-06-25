import { render, screen } from "@testing-library/react";
import { test, expect } from "vitest";
import LongCount, { Turnout } from "./LongCount";

test("LongCount provider supplies scope, theme, and context end to end", () => {
  const { container } = render(
    <LongCount>
      <Turnout />
    </LongCount>,
  );

  // (a) the provider establishes the `.lc-root` style scope
  expect(container.querySelector(".lc-root")).toBeInTheDocument();

  // (b) the FilterBar chips render (proves the LongCount context is wired).
  //     Target the chip by its button role — "General" also appears in the
  //     Turnout legend, but only the FilterBar renders it as a <button>.
  expect(
    screen.getByRole("button", { name: "General" }),
  ).toBeInTheDocument();

  // (c) the Turnout chart's HTML title renders (proves context + theme + scope
  //     reach an embedded chart island)
  expect(screen.getByText("Turnout of registered voters")).toBeInTheDocument();
});
