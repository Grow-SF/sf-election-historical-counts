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
          san francisco · sixty years of ballot counting
          <span className="hidden sm:inline"> · 1960–2026</span>
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
          It takes longer to know who won our elections than it used to.{" "}
          <em className="text-rust-bright">
            Not because counting got slower — because election night went
            from telling us almost everything to telling us barely half.
          </em>
        </p>

        <div
          className="fade-up mt-12 grid max-w-3xl grid-cols-1 gap-px border border-rule-dark bg-rule-dark sm:grid-cols-3"
          style={{ animationDelay: "280ms" }}
        >
          {[
            ["a race election night could settle, 1964", "6 points"],
            ["a race election night could settle, 2024", "76 points"],
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
              SF Department of Elections (241 releases across 18 elections),
              parsed from the Department’s own XML and TSV files and validated
              against certified totals. 1986–2014: 69 mid-canvass observations
              recovered from Wayback Machine captures of four generations of
              city results pages, frozen Lotus Domino canvass views, Elections
              Commission minutes, and Chronicle count reporting (via the
              paper’s NewsBank archive), with certified finals from the
              Department’s own turnout history and the California Secretary
              of State.
            </p>
          </div>
          <div>
            <p>
              Archival values are marked throughout: hollow points, dashed
              lines, and “≤” bounds mean the truth is at or before the shown
              value — a crawler’s snapshot, not a release schedule. Counts for
              elections within ~32 days are provisional. “News-derived”
              points are conservative floors: the certified total minus the
              ballots a registrar told a reporter were still uncounted.
              Elections before 1986 are anchored by their in-person floors
              and certified totals; the newspaper recovery for 1960–1985 and
              a records request with the Department are both in progress.
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
            In 1964, election night put 94% of the vote on the table. In 2004
            it was three quarters. Since 2020 — when California started
            mailing every voter a ballot, and voters learned they could hang
            onto it until the last day — it has been barely half. The two
            ringed points are races where the{" "}
            <em>election-night leader lost</em>: the 2018 mayor’s race and a
            2020 supervisor seat, both decided by ballots counted days later.
            That is what losing election-night knowledge means in practice.
            Specials and recalls are small and noisy —{" "}
            <button
              onClick={() => update({ kinds: new Set(["General"]) })}
              className="border-b border-rust font-semibold text-rust hover:bg-rust/10"
            >
              show generals only
            </button>{" "}
            to see the trend cleanly.
          </p>
        }
      >
        <NightShareChart elections={elections} from={state.from} to={state.to} />
      </Section>

      <Section
        id="thresholds"
        kicker="part two"
        title="How long until the winner is beyond doubt?"
        intro={
          <p>
            A race is mathematically settled once the uncounted ballots are
            too few to flip it — the closer the race, the more of the count
            you need. Set the slider to a margin and see how many days that
            took, election by election. Two things jump out. Tight races have{" "}
            <em>always</em> taken a week or more — even in 1964, a 5-point
            race had to wait for the absentees. But landslides used to be
            settled by midnight (the grey diamonds at day zero), and now even
            a 25-point blowout waits a day or two, and a 10-point race most
            of a week. The wait moved down-ballot from the nail-biters to
            nearly everything.
          </p>
        }
      >
        <ThresholdExplorer
          elections={elections}
          threshold={state.threshold}
          setThreshold={(t) => update({ threshold: t })}
          from={state.from}
          to={state.to}
        />
      </Section>

      <Section
        id="mail"
        kicker="part three"
        title="What changed is the mail"
        intro={
          <p>
            Mail ballots were 5% of the vote in 1964, a quarter in the 1990s,
            and nine in ten today — with COVID as the accelerant: in 2020
            California mailed every voter a ballot (AB 860), made it permanent
            in 2022 (AB 37), and voters never went back. A ballot postmarked
            by election day counts if it arrives within a week, and every one
            needs a signature check first. That work physically cannot happen
            on election night. The count didn’t slow down; it moved to where
            we can’t watch it.
          </p>
        }
      >
        <VbmChart />
      </Section>

      <Section
        id="explore"
        kicker="part four"
        title="The back end never changed"
        intro={
          <p>
            The full record: every election’s count, release by release, as a
            share of its certified final. The tail is structural — late mail
            that legally counts if it arrives within a week, provisional
            checks, signature cures — and it has taken roughly the same few
            weeks for as long as records exist. That part isn’t fixable and
            isn’t a scandal. The thing that changed is the front: how much of
            the vote is already on the board when we go to bed on election
            night.
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
