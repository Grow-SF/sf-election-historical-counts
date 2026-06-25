"use client";
import { KIND_DESC, KINDS } from "../lib/categories";
import { YEAR_MAX, YEAR_MIN } from "../lib/years";
import { useLongCount } from "../lib/context";
import { DualRange } from "./ui";

export default function FilterBar() {
  const { state, update, theme } = useLongCount();

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
    <div className="lc-root lc-fullbleed not-prose sticky top-0 z-20 border-b border-rule bg-white/90 backdrop-blur-sm">
      <div className="mx-auto flex max-w-5xl flex-wrap items-center gap-x-5 gap-y-2 px-5 py-2.5">
        <span className="smallcaps text-faint">filter</span>
        <div className="flex flex-wrap gap-1.5">
          {KINDS.map((k) => {
            const on = state.kinds.has(k);
            return (
              <div key={k} className="group relative">
                <button
                  onClick={() => toggleKind(k)}
                  aria-pressed={on}
                  aria-describedby={`kind-tip-${k}`}
                  // no color transition: it would stall mid-animation if the chart
                  // re-render briefly blocks the main thread, making a "check" look
                  // like nothing happened. Snap to the new state instead.
                  className="smallcaps border px-2 py-1"
                  style={{
                    borderColor: on ? theme.colorsByKind[k] : theme.rule,
                    background: on ? theme.colorsByKind[k] : "transparent",
                    color: on ? theme.paper : theme.faint,
                  }}
                >
                  {k}
                </button>
                {/* styled tooltip describing the election type, on hover or keyboard focus */}
                <span
                  id={`kind-tip-${k}`}
                  role="tooltip"
                  className="pointer-events-none absolute left-1/2 top-full z-30 mt-1.5 hidden w-56 -translate-x-1/2 whitespace-normal border border-ink bg-paper px-2.5 py-1.5 text-xs normal-case leading-snug text-ink shadow group-hover:block group-focus-within:block"
                >
                  {KIND_DESC[k]}
                </span>
              </div>
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
      </div>
    </div>
  );
}
