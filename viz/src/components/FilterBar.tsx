"use client";
import { KIND_COLOR, KIND_DESC, KINDS, YEAR_MAX, YEAR_MIN } from "@/lib/data";
import { UrlState } from "@/lib/useUrlState";
import { DualRange } from "@/components/ui";

export default function FilterBar({
  state,
  update,
}: {
  state: UrlState;
  update: (patch: Partial<UrlState>) => void;
}) {
  const toggleKind = (k: string) => {
    const next = new Set(state.kinds);
    if (next.has(k)) {
      if (next.size > 1) next.delete(k);
    } else {
      next.add(k);
    }
    update({ kinds: next });
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
                title={KIND_DESC[k]}
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

        <label className="smallcaps flex items-center gap-2 text-faint">
          <span className="text-faint">years</span>
          <span className="stat-figure text-xs text-ink">{state.from}</span>
          <DualRange
            min={YEAR_MIN}
            max={YEAR_MAX}
            lo={state.from}
            hi={state.to}
            onChange={(from, to) => update({ from, to })}
            ariaLabel="year range"
            className="w-28 sm:w-40"
          />
          <span className="stat-figure text-xs text-ink">{state.to}</span>
        </label>

        <div className="ml-auto flex flex-wrap items-center gap-2">
          <a
            href="/eras"
            className="smallcaps border border-rust bg-rust/10 px-2.5 py-1 text-rust transition-colors hover:bg-rust hover:text-paper"
          >
            Eras
          </a>
          <a
            href="/sources"
            className="smallcaps border border-rust px-2.5 py-1 text-rust transition-colors hover:bg-rust hover:text-paper"
          >
            sources
          </a>
          <a
            href="/missing"
            className="smallcaps border border-gold bg-gold/10 px-2.5 py-1 text-ink transition-colors hover:bg-gold hover:text-night"
          >
            help wanted
          </a>
        </div>
      </div>
    </div>
  );
}
