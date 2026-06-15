"use client";
import { useCallback, useEffect, useRef, useState } from "react";
import { ReferenceLine } from "recharts";
import { EVENTS, Fit } from "@/lib/data";

/**
 * Dashed vertical lines for the shared franchise/voting EVENTS that fall
 * within [min, max] — rendered identically in every chart. Use as a chart
 * child: {eventLines(1962, 2028)}
 */
export function eventLines(min: number, max: number) {
  return EVENTS.filter((e) => e.year >= min && e.year <= max).map((e) => (
    <ReferenceLine
      key={e.year}
      x={e.year}
      stroke="var(--color-gold)"
      strokeDasharray="4 4"
      label={{
        value: e.label,
        position: "top",
        fontSize: 9,
        fill: "var(--color-faint)",
      }}
    />
  ));
}

/**
 * Hover state with a grace period: the tooltip stays mounted while the
 * pointer travels from the data point into the tooltip (so links inside
 * it are clickable), and hides shortly after leaving both.
 */
export function useGraceHover<T>(delay = 300) {
  const [hover, setHover] = useState<T | null>(null);
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  const hold = useCallback(() => {
    if (timer.current) {
      clearTimeout(timer.current);
      timer.current = null;
    }
  }, []);
  const show = useCallback(
    (h: T) => {
      hold();
      setHover(h);
    },
    [hold],
  );
  const hide = useCallback(() => {
    hold();
    timer.current = setTimeout(() => setHover(null), delay);
  }, [hold, delay]);
  const clear = useCallback(() => {
    hold();
    setHover(null);
  }, [hold]);
  useEffect(() => hold, [hold]);
  return { hover, show, hide, hold, clear };
}

export function Section({
  id,
  kicker,
  title,
  children,
  intro,
}: {
  id: string;
  kicker: string;
  title: string;
  intro?: React.ReactNode;
  children: React.ReactNode;
}) {
  return (
    <section id={id} className="mx-auto max-w-5xl scroll-mt-16 px-5 py-16 sm:py-20">
      <div className="rule-double pt-6">
        <p className="smallcaps text-rust">{kicker}</p>
        <h2 className="mt-2 max-w-3xl text-3xl font-semibold leading-tight sm:text-4xl">
          {title}
        </h2>
        {intro && (
          <div className="mt-4 max-w-2xl text-[1.0625rem] leading-relaxed text-ink/85">
            {intro}
          </div>
        )}
      </div>
      <div className="mt-8">{children}</div>
    </section>
  );
}

/** Slope + r² readout for the currently filtered fit. */
export function FitBadge({
  fit,
  unit,
  flatIsGood,
}: {
  fit: Fit | null;
  unit: string;
  flatIsGood?: boolean;
}) {
  if (!fit) {
    return (
      <div className="smallcaps text-faint">
        not enough points for a trend (n &lt; 3)
      </div>
    );
  }
  const flat = fit.r2 < 0.1;
  return (
    <div className="flex flex-wrap items-baseline gap-x-5 gap-y-1">
      <span className="smallcaps text-faint">trend on filtered data</span>
      <span className="stat-figure text-sm">
        slope{" "}
        <strong className="text-ink">
          {fit.slope >= 0 ? "+" : ""}
          {fit.slope.toFixed(2)} {unit}
        </strong>
      </span>
      <span className="stat-figure text-sm">
        r²{" "}
        <strong className={flat && flatIsGood ? "text-moss" : "text-ink"}>
          {fit.r2.toFixed(2)}
        </strong>
      </span>
      <span className="stat-figure text-sm text-faint">n = {fit.n}</span>
      {flat && flatIsGood && (
        <span className="smallcaps text-moss">no trend — that’s the point</span>
      )}
    </div>
  );
}

/** Tooltip anchored to a chart point (chart-pixel coords from a custom shape). */
export function PointTooltip({
  cx,
  cy,
  children,
  onMouseEnter,
  onMouseLeave,
}: {
  cx: number;
  cy: number;
  children: React.ReactNode;
  onMouseEnter?: () => void;
  onMouseLeave?: () => void;
}) {
  const flip = cy < 110;
  return (
    <div
      className="pointer-events-auto absolute z-10 border border-ink bg-paper px-3 py-2 text-sm shadow"
      style={{
        left: cx,
        top: cy + (flip ? 14 : -14),
        transform: `translate(-50%, ${flip ? "0" : "-100%"})`,
        maxWidth: 260,
      }}
      onMouseEnter={onMouseEnter}
      onMouseLeave={onMouseLeave}
    >
      {children}
    </div>
  );
}

export function ChartFrame({
  children,
  note,
  title,
  subtitle,
}: {
  children: React.ReactNode;
  note?: React.ReactNode;
  title?: React.ReactNode;
  subtitle?: React.ReactNode;
}) {
  return (
    <figure className="mt-4 border border-rule bg-paper-deep/40 p-3 sm:p-5">
      {title && (
        <figcaption className="mb-3">
          <h3 className="text-lg font-semibold leading-tight text-ink">{title}</h3>
          {subtitle && (
            <p className="smallcaps mt-0.5 text-faint">{subtitle}</p>
          )}
        </figcaption>
      )}
      {children}
      {note && (
        <figcaption className="mt-3 border-t border-rule pt-2 text-sm italic text-faint">
          {note}
        </figcaption>
      )}
    </figure>
  );
}

/**
 * Dual-thumb range slider over [min, max]. The two handles stay ≥ minGap apart
 * (0 lets them meet for a single-value selection). Visuals live in the
 * `.rangepair` class in globals.css; only the thumbs catch pointer events so
 * either handle is grabbable even when they overlap.
 */
export function DualRange({
  min,
  max,
  lo,
  hi,
  onChange,
  step = 1,
  minGap = 0,
  ariaLabel = "range",
  className,
}: {
  min: number;
  max: number;
  lo: number;
  hi: number;
  onChange: (lo: number, hi: number) => void;
  step?: number;
  minGap?: number;
  ariaLabel?: string;
  className?: string;
}) {
  const span = max - min || 1;
  const at = (v: number) => `${((v - min) / span) * 100}%`;
  return (
    <div className={`rangepair ${className ?? ""}`}>
      <div className="track" />
      <div className="fill" style={{ left: at(lo), right: `${100 - ((hi - min) / span) * 100}%` }} />
      <input
        type="range"
        min={min}
        max={max}
        step={step}
        value={lo}
        onChange={(e) => onChange(Math.min(Number(e.target.value), hi - minGap), hi)}
        aria-label={`${ariaLabel} start`}
      />
      <input
        type="range"
        min={min}
        max={max}
        step={step}
        value={hi}
        onChange={(e) => onChange(lo, Math.max(Number(e.target.value), lo + minGap))}
        aria-label={`${ariaLabel} end`}
      />
    </div>
  );
}
