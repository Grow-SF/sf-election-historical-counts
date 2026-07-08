"use client";
import { useCallback, useMemo, useSyncExternalStore } from "react";
import { Filters } from "./filter";
import { KINDS } from "./categories";
import { YEAR_MIN, YEAR_MAX } from "./years";

export type UrlState = Filters & {
  selected: Set<string>;
  dayFrom: number;
  dayTo: number;
};

export const DEFAULT_DAY_FROM = 0;
export const DEFAULT_DAY_TO = 10;

// The year slider can reach the data's earliest year (YEAR_MIN, currently 1860),
// but it opens at 1902 — the pre-1902 record is sparse, so the default view starts
// at the turn of the century and users can drag earlier to see the 19th century.
export const DEFAULT_FROM = Math.min(Math.max(1902, YEAR_MIN), YEAR_MAX);

// Specials and recalls are hidden by default — off-cycle, lower-turnout
// elections that scatter the long-run trend; users can switch them on in the
// filter bar.
export const DEFAULT_KINDS = KINDS.filter(
  (k) => k !== "Special" && k !== "Recall",
);

export const DEFAULT_STATE: UrlState = {
  kinds: new Set(DEFAULT_KINDS),
  from: DEFAULT_FROM,
  to: YEAR_MAX,
  selected: new Set(),
  dayFrom: DEFAULT_DAY_FROM,
  dayTo: DEFAULT_DAY_TO,
};

const URL_EVENT = "lc:urlchange";

function parse(params: URLSearchParams): UrlState {
  const s: UrlState = {
    ...DEFAULT_STATE,
    kinds: new Set(DEFAULT_STATE.kinds),
    selected: new Set(DEFAULT_STATE.selected),
  };
  const kinds = params.get("kinds");
  if (kinds) {
    const ks = kinds
      .split(",")
      .filter((k) => (KINDS as readonly string[]).includes(k));
    if (ks.length) s.kinds = new Set(ks);
  }
  const from = Number(params.get("from"));
  if (from >= YEAR_MIN && from <= YEAR_MAX) s.from = from;
  const to = Number(params.get("to"));
  if (to >= YEAR_MIN && to <= YEAR_MAX) s.to = to;
  const sel = params.get("sel");
  if (sel) s.selected = new Set(sel.split(",").filter(Boolean));
  const d0 = Number(params.get("d0"));
  if (Number.isFinite(d0) && d0 >= 0) s.dayFrom = d0;
  const d1 = Number(params.get("d1"));
  if (Number.isFinite(d1) && d1 > 0) s.dayTo = d1;
  if (s.from > s.to) [s.from, s.to] = [s.to, s.from];
  if (s.dayFrom > s.dayTo) [s.dayFrom, s.dayTo] = [s.dayTo, s.dayFrom];
  return s;
}

/** The query portion only ("" or "a=b&c=d"), so it can be diffed against the URL. */
function serializeQuery(s: UrlState): string {
  const p = new URLSearchParams();
  const kindsIsDefault =
    s.kinds.size === DEFAULT_KINDS.length &&
    DEFAULT_KINDS.every((k) => s.kinds.has(k));
  if (!kindsIsDefault) p.set("kinds", [...s.kinds].join(","));
  if (s.from !== DEFAULT_FROM) p.set("from", String(s.from));
  if (s.to !== YEAR_MAX) p.set("to", String(s.to));
  if (s.selected.size) p.set("sel", [...s.selected].join(","));
  if (s.dayFrom !== DEFAULT_DAY_FROM) p.set("d0", String(s.dayFrom));
  if (s.dayTo !== DEFAULT_DAY_TO) p.set("d1", String(s.dayTo));
  return p.toString();
}

// The URL is the single source of truth. We subscribe to it as an external
// store so the component reads from it directly (no setState-in-effect, and no
// SSR/hydration mismatch — the server snapshot is the empty query → defaults,
// which matches the first client paint, then React re-reads the real URL).
function subscribe(onChange: () => void): () => void {
  window.addEventListener("popstate", onChange);
  window.addEventListener(URL_EVENT, onChange);
  return () => {
    window.removeEventListener("popstate", onChange);
    window.removeEventListener(URL_EVENT, onChange);
  };
}
const getSnapshot = () => window.location.search;
const getServerSnapshot = () => "";

/** Filter/selection state mirrored into the URL so any view is shareable. */
export function useUrlState(): [UrlState, (patch: Partial<UrlState>) => void] {
  const search = useSyncExternalStore(
    subscribe,
    getSnapshot,
    getServerSnapshot,
  );
  const state = useMemo(() => parse(new URLSearchParams(search)), [search]);

  const update = useCallback((patch: Partial<UrlState>) => {
    // merge onto the live URL state so concurrent patches don't clobber
    const next: UrlState = {
      ...parse(new URLSearchParams(window.location.search)),
      ...patch,
    };
    if (next.from > next.to) [next.from, next.to] = [next.to, next.from];
    if (next.dayFrom > next.dayTo)
      [next.dayFrom, next.dayTo] = [next.dayTo, next.dayFrom];
    const q = serializeQuery(next);
    window.history.replaceState(
      null,
      "",
      q ? `?${q}` : window.location.pathname,
    );
    window.dispatchEvent(new Event(URL_EVENT));
  }, []);

  return [state, update];
}
