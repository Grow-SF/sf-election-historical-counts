import Link from "next/link";
import { ChartFrame } from "@/components/ui";
import EraChart from "./EraChart";

export const metadata = {
  title: "A Century of Election Nights — The Long Count",
  description:
    "What the morning-after newspaper knew, 1908–2026 — and why 'we don't know yet' has meant three completely different things.",
};

const ERAS = [
  {
    years: "1908–1912",
    label: "fast",
    tone: "moss",
    body: "The morning paper already had it. Taft's San Francisco was essentially counted by breakfast in 1908 (~89% of the certified vote); Wilson's in 1912 stood at 85% with 600 of 638 precincts in and the box headed “COMPLETE.”",
  },
  {
    years: "1914–1926",
    label: "slow",
    tone: "rust",
    body: "The floor falls out. In 1914 the count proceeded, in the paper's own words, “with unprecedented slowness.” In 1916 — the closest presidential race in California history — the morning edition confessed that “virtually none of San Francisco's vote” was in hand. In 1918 the first completed precinct didn't reach the Registrar until after midnight, and the paper printed no city totals at all. Even the calmer years limped: 1920 at 66%, 1922 at 27%, 1924 at 36%, 1926 at 71%.",
  },
  {
    years: "1928–1990s",
    label: "fast again",
    tone: "moss",
    body: "The city had its mornings back, and kept them for sixty years: Roosevelt's landslides counted overnight, the 1952 presidential vote a remarkable 99% complete by the next morning, and on through the punch-card decades the night routinely delivered 80–95%.",
  },
  {
    years: "since ~2002",
    label: "slow, structurally",
    tone: "rust",
    body: "The permanent vote-by-mail list, then a pandemic that mailed every voter a ballot, moved the vote off election day. Today the night reports 10–50%, and the rest arrives, legally, for a week afterward.",
  },
];

export default function ErasPage() {
  return (
    <main className="mx-auto max-w-5xl px-5 py-14">
      <p className="smallcaps text-faint">the long count</p>
      <h1 className="mt-2 max-w-3xl text-4xl font-bold leading-[1.1] sm:text-5xl">
        A century of election nights
      </h1>
      <p className="mt-4 max-w-2xl text-lg italic leading-relaxed text-ink/70">
        What the morning-after newspaper knew, 1908–2026 — and why “we don't
        know yet” has meant three completely different things.
      </p>

      <div className="mt-8 max-w-2xl space-y-5 text-[1.0625rem] leading-relaxed text-ink/90">
        <p>
          For most of the last decade the complaint has been the same: San
          Francisco takes too long to count. The number everyone fixates on —
          the share of the vote known on election night — really has collapsed,
          from around 70% in 2004 to barely half by 2022. But pushing the record
          back to <strong>1908</strong>, recovered tally-box by tally-box from a
          century of morning-after <em>Chronicle</em> front pages, turns that
          collapse into the last act of a much stranger story.{" "}
          <em className="text-rust">
            Election night has failed San Francisco before. It just failed for
            the opposite reason.
          </em>
        </p>
      </div>

      <figure className="mt-10">
        <ChartFrame
          note={
            <>
              Share of each election's certified vote counted by election night,
              1908–2026. The pre-1964 points were recovered in 2026 from
              NewsBank scans of the <em>Chronicle</em>; hover any point for its
              source. This is the same chart as on the{" "}
              <Link
                href="/"
                className="border-b border-rust/40 text-rust hover:bg-rust/10"
              >
                home page
              </Link>
              , unfiltered.
            </>
          }
        >
          <EraChart />
        </ChartFrame>
      </figure>

      <section className="mt-14">
        <h2 className="rule-double max-w-3xl pt-6 text-3xl font-semibold">
          Four eras, not one
        </h2>
        <div className="mt-6 grid gap-px border border-rule bg-rule sm:grid-cols-2">
          {ERAS.map((e) => (
            <div key={e.years} className="bg-paper p-5">
              <div className="flex items-baseline justify-between gap-3">
                <p className="stat-figure text-lg font-semibold text-ink">
                  {e.years}
                </p>
                <p
                  className={`smallcaps ${e.tone === "moss" ? "text-moss" : "text-rust"}`}
                >
                  {e.label}
                </p>
              </div>
              <p className="mt-2 text-[0.95rem] leading-relaxed text-ink/85">
                {e.body}
              </p>
            </div>
          ))}
        </div>
      </section>

      <section className="mt-14 max-w-2xl space-y-5 text-[1.0625rem] leading-relaxed text-ink/90">
        <h2 className="rule-double pt-6 text-3xl font-semibold text-ink">
          The same symptom, three different machines
        </h2>
        <p>
          What makes the early dip remarkable is that it is <em>not</em> the
          modern story running in reverse. The 1910s were slow because{" "}
          <strong>counting itself was slow</strong>: hand-tallied paper ballots,
          and Progressive-era ballots that had ballooned to a dozen propositions
          and a long row of judges, each of which a clerk had to count by hand,
          by lamplight, precinct by precinct. A close race made it worse, because
          nobody could call it early and go home. The bottleneck was the count.
        </p>
        <p>
          The middle era fixed exactly that — mechanical voting and leaner
          ballots let a precinct report its totals the moment the polls closed —
          which is why 1928 through the 1990s feels boringly complete.
        </p>
        <p>
          And the modern era is slow for a third, unrelated reason: the ballots
          aren't late to be <em>counted</em>, they're late to <em>arrive</em>. A
          mail ballot postmarked by election day is valid for a week, and every
          one needs a signature check first. The back end of the count takes
          about as long as it always has. What changed is how much of the vote is
          sitting in the building when the polls close.
        </p>
        <p className="border-l-2 border-gold pl-4 text-ink">
          So “we don't know who won yet” has meant three different things in one
          century: in 1916 it meant <em>the clerks are still counting</em>; in
          1956 it meant nothing, because they were done; and in 2022 it means{" "}
          <em>most of the ballots are still in the mail</em>.
        </p>
      </section>

      <section className="mt-14 max-w-2xl space-y-5 text-[1.0625rem] leading-relaxed text-ink/90">
        <h2 className="rule-double pt-6 text-3xl font-semibold text-ink">
          A footnote that became a finding
        </h2>
        <p>
          Chasing these numbers turned up an error in the official record. The
          Department of Elections' own historical turnout table lists 166,133
          ballots cast in San Francisco in November 1934 — but the 1934
          governor's race, the Upton Sinclair “EPIC” contest that drew voters out
          in record numbers, by itself recorded 220,894 votes in the city, across
          all 1,054 precincts, complete. A contest cannot draw more votes than
          there were ballots. The turnout figure is simply wrong (its neighbors
          are 227,000 in 1932 and 269,000 in 1936), and it now joins two known
          1970s undercounts in the project's running list of denominator errors.
        </p>
      </section>

      <section className="mt-14 max-w-2xl space-y-5 text-[1.0625rem] leading-relaxed text-ink/90">
        <h2 className="rule-double pt-6 text-3xl font-semibold text-ink">
          Why go back this far
        </h2>
        <p>
          The modern slide is real and worth measuring. But a twenty-year decline
          reads very differently against twenty years of context than against a
          hundred. The long view shows that a complete election night is not the
          natural state of things to which we should expect to return — it was
          itself an achievement of the 1920s, won by machines and shorter
          ballots, and now undone by a change in how we vote rather than how we
          count. The city has lived through a slow election night before. It got
          out of it once. That is either reassuring or not, depending on how you
          read it.
        </p>
      </section>

      <p className="mt-12 border-t border-rule pt-6 text-sm text-faint">
        Method, per-election numbers, and every cited scan live in the
        repository's analysis notes.{" "}
        <Link
          href="/sources"
          className="border-b border-rust/40 text-rust hover:bg-rust/10"
        >
          every number, sourced
        </Link>{" "}
        ·{" "}
        <Link
          href="/missing"
          className="border-b border-rust/40 text-rust hover:bg-rust/10"
        >
          the gaps that remain
        </Link>
      </p>
      <p className="mt-4">
        <Link
          href="/"
          className="border-b border-rust font-semibold text-rust hover:bg-rust/10"
        >
          ← back to the charts
        </Link>
      </p>
    </main>
  );
}
