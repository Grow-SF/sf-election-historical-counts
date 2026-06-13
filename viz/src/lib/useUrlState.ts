"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { Filters, KINDS, YEAR_MAX, YEAR_MIN } from "./data";

export type UrlState = Filters & {
  selected: Set<string>;
  dayFrom: number;
  dayTo: number;
};

export const DEFAULT_DAY_FROM = 0;
export const DEFAULT_DAY_TO = 10;

export const DEFAULT_STATE: UrlState = {
  kinds: new Set(KINDS),
  from: YEAR_MIN,
  to: YEAR_MAX,
  selected: new Set(),
  dayFrom: DEFAULT_DAY_FROM,
  dayTo: DEFAULT_DAY_TO,
};

function parse(params: URLSearchParams): UrlState {
  const s: UrlState = {
    ...DEFAULT_STATE,
    kinds: new Set(DEFAULT_STATE.kinds),
    selected: new Set(DEFAULT_STATE.selected),
  };
  const kinds = params.get("kinds");
  if (kinds) {
    const ks = kinds.split(",").filter((k) => (KINDS as readonly string[]).includes(k));
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
  if (s.kinds.size !== KINDS.length) p.set("kinds", [...s.kinds].join(","));
  if (s.from !== YEAR_MIN) p.set("from", String(s.from));
  if (s.to !== YEAR_MAX) p.set("to", String(s.to));
  if (s.selected.size) p.set("sel", [...s.selected].join(","));
  if (s.dayFrom !== DEFAULT_DAY_FROM) p.set("d0", String(s.dayFrom));
  if (s.dayTo !== DEFAULT_DAY_TO) p.set("d1", String(s.dayTo));
  return p.toString();
}

/** Filter/selection state mirrored into the URL so any view is shareable. */
export function useUrlState(): [UrlState, (patch: Partial<UrlState>) => void] {
  // start from defaults so server and first client paint agree (no hydration
  // mismatch); the URL is read back in a mount effect below
  const [state, setState] = useState<UrlState>(DEFAULT_STATE);
  // skip the URL write on the initial render so it can't wipe an incoming query
  // before the restore effect has read it
  const synced = useRef(false);

  // restore from the URL once, after hydration (client only)
  useEffect(() => {
    setState(parse(new URLSearchParams(window.location.search)));
    const onPop = () =>
      setState(parse(new URLSearchParams(window.location.search)));
    window.addEventListener("popstate", onPop);
    return () => window.removeEventListener("popstate", onPop);
  }, []);

  // mirror state → URL in an effect (commit phase). Doing it inside the setState
  // updater runs during render and trips Next's router setState-in-render guard.
  useEffect(() => {
    if (!synced.current) {
      synced.current = true;
      return;
    }
    const q = serializeQuery(state);
    if (q !== window.location.search.replace(/^\?/, "")) {
      window.history.replaceState(null, "", q ? `?${q}` : window.location.pathname);
    }
  }, [state]);

  const update = useCallback((patch: Partial<UrlState>) => {
    setState((prev) => {
      const next = { ...prev, ...patch };
      if (next.from > next.to) [next.from, next.to] = [next.to, next.from];
      if (next.dayFrom > next.dayTo) [next.dayFrom, next.dayTo] = [next.dayTo, next.dayFrom];
      return next;
    });
  }, []);

  return [state, update];
}
