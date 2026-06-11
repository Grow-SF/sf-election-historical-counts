"use client";
import { useState } from "react";
import { KIND_COLOR, KINDS, YEAR_MAX, YEAR_MIN } from "@/lib/data";
import { UrlState } from "@/lib/useUrlState";

const YEARS = Array.from(
  { length: YEAR_MAX - YEAR_MIN + 1 },
  (_, i) => YEAR_MIN + i,
);

export default function FilterBar({
  state,
  update,
}: {
  state: UrlState;
  update: (patch: Partial<UrlState>) => void;
}) {
  const [copied, setCopied] = useState(false);

  const toggleKind = (k: string) => {
    const next = new Set(state.kinds);
    if (next.has(k)) {
      if (next.size > 1) next.delete(k);
    } else {
      next.add(k);
    }
    update({ kinds: next });
  };

  const share = async () => {
    try {
      await navigator.clipboard.writeText(window.location.href);
      setCopied(true);
      setTimeout(() => setCopied(false), 1600);
    } catch {
      /* clipboard unavailable; the URL bar already has the state */
    }
  };

  return (
    <div className="sticky top-0 z-20 border-b border-rule bg-paper/95 backdrop-blur-sm">
      <div className="mx-auto flex max-w-5xl flex-wrap items-center gap-x-5 gap-y-2 px-5 py-2.5">
        <span className="smallcaps text-faint">filter</span>
        <div className="flex flex-wrap gap-1.5">
          {KINDS.map((k) => {
            const on = state.kinds.has(k);
            return (
              <button
                key={k}
                onClick={() => toggleKind(k)}
                aria-pressed={on}
                className="smallcaps border px-2 py-1 transition-colors"
                style={{
                  borderColor: on ? KIND_COLOR[k] : "var(--color-rule)",
                  background: on ? KIND_COLOR[k] : "transparent",
                  color: on ? "var(--color-paper)" : "var(--color-faint)",
                }}
              >
                {k}
              </button>
            );
          })}
        </div>

        <label className="smallcaps flex items-center gap-1.5 text-faint">
          <select
            value={state.from}
            onChange={(e) => update({ from: Number(e.target.value) })}
            className="stat-figure border border-rule bg-transparent px-1 py-0.5 text-xs text-ink"
          >
            {YEARS.map((y) => (
              <option key={y} value={y}>
                {y}
              </option>
            ))}
          </select>
          –
          <select
            value={state.to}
            onChange={(e) => update({ to: Number(e.target.value) })}
            className="stat-figure border border-rule bg-transparent px-1 py-0.5 text-xs text-ink"
          >
            {YEARS.map((y) => (
              <option key={y} value={y}>
                {y}
              </option>
            ))}
          </select>
        </label>

        <label className="smallcaps flex cursor-pointer items-center gap-1.5 text-faint">
          <input
            type="checkbox"
            checked={state.archival}
            onChange={(e) => update({ archival: e.target.checked })}
            className="accent-rust"
          />
          archival (1960–2014)
        </label>

        <a
          href="/sources"
          className="smallcaps ml-auto border border-rust px-2.5 py-1 text-rust transition-colors hover:bg-rust hover:text-paper"
        >
          sources
        </a>
        <button
          onClick={share}
          className="smallcaps border border-ink px-2.5 py-1 text-ink transition-colors hover:bg-ink hover:text-paper"
        >
          {copied ? "link copied ✓" : "share this view"}
        </button>
      </div>
    </div>
  );
}
