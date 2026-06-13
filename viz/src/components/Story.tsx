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
            ["a race election night could settle, 1964", "7 points"],
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
              against certified totals. 1986–2014: 131 mid-canvass observations
              recovered from Wayback Machine captures of four generations of
              city results pages, frozen Lotus Domino canvass views, Elections
              Commission minutes, and the Chronicle’s standing “How San
              Francisco Voted” results tables and count reporting (via the
              paper’s NewsBank archive), with certified finals from the
              Department’s own turnout history and the California Secretary
              of State.
            </p>
          </div>
          <div>
            <p>
              Recovered values are conservative: dashed marks and “≤” bounds
              mean the truth is at or above/before the shown value. Counts for
              elections within ~32 days are provisional. “News-derived”
              points are conservative floors: the certified total minus the
              ballots a registrar told a reporter were still uncounted.
              1960–1985: 19 election-night counts read from page scans of the
              Chronicle’s vote-tally boxes and count reporting, every digit
              independently re-verified and checked against certified totals.
              A records request with the Department is in progress for the
              remaining web-era gaps.
            </p>
          </div>
        </div>
        <p className="smallcaps mt-8 text-paper/55">
          built from the sf-election-count pipeline ·{" "}
          <a href="/sources" className="border-b border-gold/60 text-gold hover:bg-gold/10">
            every number, sourced — the full citation list
          </a>{" "}
          ·{" "}
          <a href="/missing" className="border-b border-gold/60 text-gold hover:bg-gold/10">
            help complete the record
          </a>{" "}
          · {new Date().getFullYear()}
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
          <>
            <p>
              Three eras emerge from the recovered record. <em>Before 2002</em>,
              mail voting grew slowly — and mail voters returned their ballots
              early enough to be counted with the night’s tally, so election
              night stayed nearly complete: 93.5% in 1964, over 98% in the
              late seventies, 80 to 93 through the nineties. <em>From 2002</em>,
              when any Californian could join the permanent vote-by-mail
              list, election-day turnout shrank every cycle and the night
              count began a steady slide. <em>Since 2020</em>, with nearly
              everyone voting by mail and most returning ballots late,
              election night reports barely half.
            </p>
            <p>
              The ringed points are races the{" "}
              <em>election-night leader lost</em> — the 2018 mayor’s race and
              a 2020 supervisor seat, decided by ballots counted days later.
              Recalls (purple) and special elections (gold) sit above the
              trend: their electorates vote early by mail, so the night count
              catches more of them. Filter to primaries and generals and the
              slide is at its sharpest.
            </p>
          </>
        }
      >
        <NightShareChart elections={elections} from={state.from} to={state.to} kinds={state.kinds} />
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
            took, election by election. It didn&rsquo;t used to take long, even
            when it was close: in December 1975 a mayor&rsquo;s race decided by{" "}
            <em>2.2 points</em> was over the same night — 99% of the vote was
            counted by midnight and the loser conceded at 11:30 p.m. Now even
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
          kinds={state.kinds}
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

      <section className="grain relative mt-16 bg-night text-paper">
        <div className="mx-auto max-w-5xl px-5 py-12">
          <p className="smallcaps text-gold">open research — help wanted</p>
          <h2 className="mt-2 max-w-3xl text-3xl font-bold leading-tight">
            Thirteen election nights are still missing. You might own one.
          </h2>
          <p className="mt-4 max-w-3xl text-lg leading-relaxed text-paper/85">
            Sixty years of counts have been recovered from city archives, the
            Wayback Machine, and the Chronicle&rsquo;s morgue — but the
            night-of numbers for elections like the 1995 Brown–Jordan
            mayor&rsquo;s race and the 1999 Ammiano write-in exist only in
            sources we can&rsquo;t reach: the Examiner&rsquo;s pages,
            broadcast archives, a box of old papers. One photograph settles
            each one.
          </p>
          <p className="mt-6">
            <a
              href="/missing"
              className="smallcaps inline-block border border-gold bg-gold/10 px-4 py-2 text-gold transition-colors hover:bg-gold hover:text-night"
            >
              see the list — submit a source →
            </a>
          </p>
        </div>
      </section>

      <Footer />
    </main>
  );
}
