import { render, screen, fireEvent } from "@testing-library/react";
import { test, expect } from "vitest";
import LongCount, { Turnout, Vbm } from "./LongCount";

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

test("each chart carries its own FilterBar, all sharing one state", () => {
  render(
    <LongCount>
      <Turnout />
      <Vbm />
    </LongCount>,
  );

  // one FilterBar per chart → one "Special" chip per chart
  const special = screen.getAllByRole("button", { name: "Special" });
  expect(special).toHaveLength(2);
  // "Special" is off by default on both
  special.forEach((b) => expect(b).toHaveAttribute("aria-pressed", "false"));

  // toggling it on ONE chart's filter updates the shared state…
  fireEvent.click(special[0]);

  // …so BOTH charts' filters now reflect it (change one, all update)
  screen
    .getAllByRole("button", { name: "Special" })
    .forEach((b) => expect(b).toHaveAttribute("aria-pressed", "true"));
});
