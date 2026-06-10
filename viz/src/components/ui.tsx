"use client";
import { Fit } from "@/lib/data";

export function Section({
  kicker,
  title,
  children,
  intro,
}: {
  kicker: string;
  title: string;
  intro?: React.ReactNode;
  children: React.ReactNode;
}) {
  return (
    <section className="mx-auto max-w-5xl px-5 py-16 sm:py-20">
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

export function ChartFrame({
  children,
  note,
}: {
  children: React.ReactNode;
  note?: React.ReactNode;
}) {
  return (
    <figure className="mt-4 border border-rule bg-paper-deep/40 p-3 sm:p-5">
      {children}
      {note && (
        <figcaption className="mt-3 border-t border-rule pt-2 text-sm italic text-faint">
          {note}
        </figcaption>
      )}
    </figure>
  );
}
