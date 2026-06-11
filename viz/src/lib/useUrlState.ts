"use client";
import { useCallback, useEffect, useState } from "react";
import { Filters, KINDS, THRESHOLDS, YEAR_MAX, YEAR_MIN } from "./data";

export type UrlState = Filters & {
  threshold: number;
  selected: string | null;
};

export const DEFAULT_STATE: UrlState = {
  kinds: new Set(KINDS),
  from: YEAR_MIN,
  to: YEAR_MAX,
  threshold: 80,
  selected: null,
};

function parse(params: URLSearchParams): UrlState {
  const s: UrlState = {
    ...DEFAULT_STATE,
    kinds: new Set(DEFAULT_STATE.kinds),
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
  const t = Number(params.get("t"));
  if (THRESHOLDS.includes(t)) s.threshold = t;
  const sel = params.get("sel");
  if (sel) s.selected = sel;
  if (s.from > s.to) [s.from, s.to] = [s.to, s.from];
  return s;
}

function serialize(s: UrlState): string {
  const p = new URLSearchParams();
  if (s.kinds.size !== KINDS.length) p.set("kinds", [...s.kinds].join(","));
  if (s.from !== YEAR_MIN) p.set("from", String(s.from));
  if (s.to !== YEAR_MAX) p.set("to", String(s.to));
  if (s.threshold !== DEFAULT_STATE.threshold) p.set("t", String(s.threshold));
  if (s.selected) p.set("sel", s.selected);
  const q = p.toString();
  return q ? `?${q}` : window.location.pathname;
}

/** Filter/selection state mirrored into the URL so any view is shareable. */
export function useUrlState(): [UrlState, (patch: Partial<UrlState>) => void] {
  const [state, setState] = useState<UrlState>(() =>
    typeof window === "undefined"
      ? DEFAULT_STATE
      : parse(new URLSearchParams(window.location.search)),
  );

  useEffect(() => {
    const onPop = () =>
      setState(parse(new URLSearchParams(window.location.search)));
    window.addEventListener("popstate", onPop);
    return () => window.removeEventListener("popstate", onPop);
  }, []);

  const update = useCallback((patch: Partial<UrlState>) => {
    setState((prev) => {
      const next = { ...prev, ...patch };
      if (next.from > next.to) [next.from, next.to] = [next.to, next.from];
      window.history.replaceState(null, "", serialize(next));
      return next;
    });
  }, []);

  return [state, update];
}
