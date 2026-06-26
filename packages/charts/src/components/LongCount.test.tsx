import { render, screen, fireEvent } from "@testing-library/react";
import { test, expect } from "vitest";
import LongCount, {
  Turnout,
  Vbm,
  NightShare,
  Registration,
} from "./LongCount";

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

test("kind charts each carry the full filter and share one state", () => {
  render(
    <LongCount>
      <NightShare />
      <Turnout />
    </LongCount>,
  );

  // one FilterBar per kind chart → one "Special" chip per chart
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

test("year-only charts show just the year slider — no kind chips", () => {
  render(
    <LongCount>
      <Registration />
    </LongCount>,
  );

  // a single-series, year-only chart hides the kind chips…
  expect(screen.queryByRole("button", { name: "General" })).toBeNull();
  expect(screen.queryByRole("button", { name: "Special" })).toBeNull();
  // …but still shows the year-range control (shared with the other charts)
  expect(screen.getByText("years")).toBeInTheDocument();
});

test("the vote-by-mail chart has no year filter", () => {
  render(
    <LongCount>
      <Vbm />
    </LongCount>,
  );

  // no filter at all — no kind chips and no year slider
  expect(screen.queryByRole("button", { name: "General" })).toBeNull();
  expect(screen.queryByText("years")).toBeNull();
  // the chart still renders
  expect(
    screen.getByText("Vote-by-mail share of ballots cast"),
  ).toBeInTheDocument();
});
