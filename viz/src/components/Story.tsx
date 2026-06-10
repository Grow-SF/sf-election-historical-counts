"use client";
import { useMemo } from "react";
import { filterElections } from "@/lib/data";
import { useUrlState } from "@/lib/useUrlState";
import FilterBar from "@/components/FilterBar";
import NightShareChart from "@/components/NightShareChart";
import ThresholdExplorer from "@/components/ThresholdExplorer";
import TrajectoryExplorer from "@/components/TrajectoryExplorer";
import VbmChart from "@/components/VbmChart";
import { Section } from "@/components/ui";

function Hero() {
  return (
    <header className="grain relative overflow-hidden bg-night text-paper">
      <div className="mx-auto max-w-5xl px-5 pb-20 pt-24 sm:pb-28 sm:pt-32">
        <p className="smallcaps fade-up max-w-full text-gold">
          san francisco · every results release
          <span className="hidden sm:inline"> · 2002–2026</span>
        </p>
        <h1
          className="fade-up mt-4 max-w-4xl text-[2.6rem] font-bold leading-[1.05] sm:text-7xl"
          style={{ animationDelay: "90ms" }}
        >
          The Long Count
        </h1>
        <p
          className="fade-up mt-6 max-w-2xl text-xl leading-relaxed text-paper/85 sm:text-2xl"
          style={{ animationDelay: "180ms" }}
        >
          San Francisco hasn’t gotten slower at counting ballots.{" "}
          <em className="text-rust-bright">
            Election night just stopped being when the counting happens.
          </em>
        </p>

        <div
          className="fade-up mt-12 grid max-w-3xl grid-cols-1 gap-px border border-rule-dark bg-rule-dark sm:grid-cols-3"
          style={{ animationDelay: "280ms" }}
        >
          {[
            ["counted by midnight, nov 2004", "74.9%"],
            ["counted by midnight, nov 2024", "56.9%"],
            ["days to finish the count", "unchanged"],
          ].map(([label, value]) => (
            <div key={label} className="bg-night-soft px-5 py-4">
              <p className="smallcaps text-paper/50">{label}</p>
              <p className="stat-figure mt-1 text-3xl font-semibold text-paper">
                {value}
              </p>
            </div>
          ))}
        </div>

        <p
          className="smallcaps fade-up mt-14 text-paper/55"
          style={{ animationDelay: "380ms" }}
        >
          ↓ scroll — filters apply to every chart and are encoded in the URL
        </p>
      </div>
    </header>
  );
}

function Footer() {
  return (
    <footer className="grain relative mt-10 bg-night text-paper/75">
      <div className="mx-auto max-w-5xl px-5 py-14 text-sm leading-relaxed">
        <p className="smallcaps text-gold">method &amp; provenance</p>
        <div className="mt-4 grid gap-8 sm:grid-cols-2">
          <div>
            <p>
              2015–present: every per-release summary report published by the
              SF Department of Elections (243 releases across 18 elections),
              parsed from the Department’s own XML and TSV files and validated
              against certified totals. 2002–2014: 36 mid-canvass observations
              recovered from Wayback Machine captures of the Department’s
              results pages across four website generations, with certified
              finals from the Department’s turnout history and the California
              Secretary of State.
            </p>
          </div>
          <div>
            <p>
              Archival values are marked throughout: hollow points, dashed
              lines, and “≤” bounds mean the truth is at or before the shown
              value — a crawler’s snapshot, not a release schedule. Counts for
              elections within ~32 days are provisional. No canvass-progress
              records survive on the public web for 1995–2001; a records
              request with the Department is pending.
            </p>
          </div>
        </div>
        <p className="smallcaps mt-8 text-paper/55">
          built from the sf-election-count pipeline · data and recovery
          provenance in the repository · {new Date().getFullYear()}
        </p>
      </div>
    </footer>
  );
}

export default function Story() {
  const [state, update] = useUrlState();
  const elections = useMemo(() => filterElections(state), [state]);

  return (
    <main>
      <Hero />
      <FilterBar state={state} update={update} />

      <Section
        id="night"
        kicker="part one"
        title="Election night tells you less every cycle"
        intro={
          <p>
            In 2004, three quarters of San Francisco’s final vote was public by
            midnight. Twenty years later, barely half is. The decline is the
            one robust trend in this data — and it isn’t about counting speed.
            Specials and recalls are small and noisy —{" "}
            <button
              onClick={() => update({ kinds: new Set(["General"]) })}
              className="border-b border-rust font-semibold text-rust hover:bg-rust/10"
            >
              show generals only
            </button>{" "}
            to see it cleanly.
          </p>
        }
      >
        <NightShareChart elections={elections} />
      </Section>

      <Section
        id="thresholds"
        kicker="part two"
        title="But the count itself never slowed down"
        intro={
          <p>
            If the Department were getting slower, the days needed to reach any
            fixed share of the final count would be rising. They aren’t. Pick
            any threshold — the fitted slope stays near zero and explains
            almost nothing (r² ≈ 0). The 90% line everyone quotes is just one
            arbitrary cut; the flatness holds at all of them.
          </p>
        }
      >
        <ThresholdExplorer
          elections={elections}
          threshold={state.threshold}
          setThreshold={(t) => update({ threshold: t })}
        />
      </Section>

      <Section
        id="mail"
        kicker="part three"
        title="What changed is the mail"
        intro={
          <p>
            Mail ballots were 5% of the vote in 1964, a quarter in the 1990s,
            and nine in ten today. California counts any ballot postmarked by
            election day that arrives within a week — and every one needs a
            signature check first. That work physically cannot happen on
            election night. The count didn’t slow down; it moved.
          </p>
        }
      >
        <VbmChart />
      </Section>

      <Section
        id="explore"
        kicker="part four"
        title="Explore every canvass since 2002"
        intro={
          <p>
            The full record: every election’s count, release by release, as a
            share of its certified final. The shape is remarkably stable — a
            big election-night step, a fast first week, a long tail of late
            mail, provisionals, and cures.
          </p>
        }
      >
        <TrajectoryExplorer
          elections={elections}
          selected={state.selected}
          setSelected={(id) => update({ selected: id })}
        />
      </Section>

      <Footer />
    </main>
  );
}
