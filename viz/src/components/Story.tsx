"use client";
import { useMemo } from "react";
import { filterElections } from "@/lib/data";
import { useUrlState } from "@/lib/useUrlState";
import FilterBar from "@/components/FilterBar";
import NightShareChart from "@/components/NightShareChart";
import TrajectoryExplorer from "@/components/TrajectoryExplorer";
import VbmChart from "@/components/VbmChart";
import TurnoutChart from "@/components/TurnoutChart";
import RegistrationChart from "@/components/RegistrationChart";
import FranchiseFunnelChart from "@/components/FranchiseFunnelChart";
import { Section } from "@/components/ui";

function Hero() {
  return (
    <header className="grain relative overflow-hidden bg-night text-paper">
      <div className="mx-auto max-w-5xl px-5 pb-20 pt-24 sm:pb-28 sm:pt-32">
        <p className="smallcaps fade-up max-w-full text-gold">
          san francisco · a century of ballot counting
          <span className="hidden sm:inline"> · 1908–2026</span>
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
              against certified totals. 1986–2014: 147 mid-canvass observations
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
              1908–1985: 41 election-night counts read from page scans of the
              Chronicle’s vote-tally boxes and count reporting, every digit
              independently re-verified and checked against certified totals —
              the pre-1964 figures (22 elections, recovered 2026) extend the
              record back to the hand-count era. A records request with the
              Department is in progress for the remaining web-era gaps.
            </p>
          </div>
        </div>
        <p className="smallcaps mt-8 text-paper/55">
          built from the sf-election-count pipeline ·{" "}
          <a href="/eras" className="border-b border-gold/60 text-gold hover:bg-gold/10">
            a century of election nights — the essay
          </a>{" "}
          ·{" "}
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
              Election night has failed San Francisco before — for the opposite
              reason. <em>1908–1912</em>: the morning paper already had it (≈85–89%
              counted by breakfast). <em>1914–1926</em>: the floor falls out. Hand-
              tallied paper and ballooning Progressive-era ballots made counting
              itself the bottleneck; 1916, the closest presidential race in state
              history, left “virtually none of San Francisco’s vote” in hand by
              press time, and in 1918 the first precinct didn’t reach the
              Registrar until after midnight. <em>1928–1990s</em>: the night comes
              back — 99% complete in 1952, then 80–95% for sixty years (still
              hand-counted paper; San Francisco had no voting machines until 1960s
              punch cards, and precincts grew only with the electorate, so the
              fix wasn’t mechanization). <em>Since ~2002</em>: the permanent vote-by-mail
              list, then a pandemic, move the vote off election day, and the night
              slides back toward half.
            </p>
            <p>
              Same symptom, three different machines: in 1916 the clerks were
              still counting; in 1956 they were already done; today the ballots
              are still in the mail. The ringed points are races the{" "}
              <em>election-night leader lost</em> — the 2018 mayor’s race and a
              2020 supervisor seat, decided by ballots counted days later.
              Recalls and special elections sit above the trend:
              their electorates vote early by mail, so the night count catches
              more of them. Filter to primaries and generals and both slides —
              the 1910s and today’s — show their sharpest.{" "}
              <a
                href="/eras"
                className="border-b border-rust font-medium text-rust hover:bg-rust/10"
              >
                Read the full story — a century of election nights →
              </a>
            </p>
          </>
        }
      >
        <NightShareChart elections={elections} from={state.from} to={state.to} kinds={state.kinds} />
      </Section>

      <Section
        id="mail"
        kicker="part two"
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
        <VbmChart from={state.from} to={state.to} />
      </Section>

      <Section
        id="franchise"
        kicker="part three"
        title="It changed when we count — not who votes"
        intro={
          <>
            <p>
              Start with the whole city. Every San Franciscan falls into one
              band below: too young to vote, a non-citizen who legally can’t,
              an eligible citizen who never registered, registered but a
              no-show — or an actual voter. Watch the blue band of non-citizens
              breathe with the city’s immigration history, and the eligible
              electorate jump when women won the vote in 1920. The franchise
              has never been the whole population, and the gap is mostly about
              who counts as eligible, not who bothers to vote.
            </p>
            <p>
              That blue band is a century of immigration. San Francisco began
              as a Gold-Rush boomtown where a third of adults were foreign-born
              and few could vote — in 1900 only about 100,000 people, all of
              them men, were eligible citizens. Women’s suffrage doubled the
              eligible electorate in 1920; the immigration lull from the 1920s
              through the 1950s shrank the non-citizen share to roughly one
              adult in twenty; then the waves from Latin America and Asia after
              1965 widened it again, to about one in eight today. (These counts
              come from the decennial census, via IPUMS NHGIS, back to 1900 —
              and they capture who was legally barred, including the men-only
              electorate before 1920 and the Asian immigrants denied
              naturalization until the 1940s.)
            </p>
            <p>
              Mailing every voter a ballot is the most sweeping change to how
              San Franciscans vote in sixty years. So it’s worth asking the
              obvious question: did it bring more people to the polls? Among
              voters already on the rolls, the answer is mostly no. Turnout
              swings with what’s on the ballot — presidential generals draw
              80%, off-year municipals barely 40% — and the all-mail era to
              the right of the milestone lines lands inside that same band. The 2020
              record was the nationwide presidential peak, not a vote-by-mail
              effect; the 2024 general fell back below 2016, and the 2024
              presidential primary was the lowest in the modern record.
            </p>
            <p>
              That’s the narrow question, though. <em>Turnout of the
              registered</em> measures convenience for people who were already
              going to vote — and mail voting is, above all, convenient. The
              franchise question proper is whether mail voting pulled more
              eligible San Franciscans onto the rolls at all — and the
              Secretary of State’s registration-vs-eligible figures say no: the
              share of eligible San Franciscans who are registered has held
              around three-quarters for two decades, before and after the
              all-mail switch.
            </p>
            <p>
              One wrinkle, shaded on the registration chart: in the 1990s the
              line climbs <em>past</em> 100% — more names on the rolls than
              eligible adults in the city. That’s the{" "}
              <a
                href="https://www.electproject.org/election-data/faq/reg"
                target="_blank"
                rel="noopener noreferrer"
                className="border-b border-rust/50 text-rust hover:bg-rust/10"
              >
                “deadwood”
              </a>{" "}
              era, when registrations of people who had died, moved, or
              re-registered elsewhere piled up uncleaned. In 1996 the Secretary
              of State named San Francisco the state’s worst case, with up to a fifth of
              its rolls dead weight; the 1995 federal “motor-voter” law forced
              the list maintenance that brought it back to earth. A reminder
              that even the registration count — the firmest number here — has
              had its own quiet drift.
            </p>
          </>
        }
      >
        <FranchiseFunnelChart from={state.from} to={state.to} />
        <TurnoutChart from={state.from} to={state.to} />
        <RegistrationChart from={state.from} to={state.to} />
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
          toggleSelected={(id) => {
            const next = new Set(state.selected);
            if (next.has(id)) next.delete(id);
            else next.add(id);
            update({ selected: next });
          }}
          clearSelected={() => update({ selected: new Set() })}
          dayFrom={state.dayFrom}
          dayTo={state.dayTo}
          setDayRange={(lo, hi) => update({ dayFrom: lo, dayTo: hi })}
        />
      </Section>

      <section className="grain relative mt-16 bg-night text-paper">
        <div className="mx-auto max-w-5xl px-5 py-12">
          <p className="smallcaps text-gold">open research — help wanted</p>
          <h2 className="mt-2 max-w-3xl text-3xl font-bold leading-tight">
            Seven election nights are still missing. You might own one.
          </h2>
          <p className="mt-4 max-w-3xl text-lg leading-relaxed text-paper/85">
            A century of counts has been recovered from city archives, the
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
