"use client";
import { useMemo } from "react";
import { filterElections } from "../lib/filter";
import {
  ELECTIONS,
  SD_NIGHT_HISTORY,
  SD_ARTIFACT_NOTES,
} from "../../../data/index";
import { useUrlState } from "../lib/useUrlState";
import { LongCountProvider, useLongCount } from "../lib/context";
import FilterBar from "./FilterBar";
import NightShareChart from "./NightShareChart";
import TrajectoryExplorer from "./TrajectoryExplorer";
import VbmChart from "./VbmChart";
import CountySpeedChart from "./CountySpeedChart";
import CountyNightShareChart from "./CountyNightShareChart";
import CountyNightTimelineChart from "./CountyNightTimelineChart";
import TurnoutChart from "./TurnoutChart";
import RegistrationChart from "./RegistrationChart";
import FranchiseFunnelChart from "./FranchiseFunnelChart";
import { ChartsThemeProvider, defaultTheme } from "../theme";
import type { ChartsTheme } from "../theme";

// The data + methodology live in the public source repository.
const REPO = "https://github.com/Grow-SF/sf-election-historical-counts";

// A full-bleed island that re-establishes the `.lc-root` style scope (the
// chart CSS variables + smallcaps/stat-figure/grain/rangepair classes) for a
// chart or band embedded in the surrounding GrowSF MDX prose. `wide` lets a
// dark band span edge to edge; the default centers content at chart width.
function Island({
  children,
  wide,
}: {
  children: React.ReactNode;
  wide?: boolean;
}) {
  return (
    <div className="lc-root lc-fullbleed not-prose">
      {wide ? (
        children
      ) : (
        <div className="mx-auto max-w-5xl px-5">{children}</div>
      )}
    </div>
  );
}

/** Provider: owns the shared URL/filter state. Each chart renders its own
 *  FilterBar above it — all reading this single state, so they stay in sync —
 *  rather than one bar pinned to the top. The provider itself is context-only;
 *  the MDX prose and chart islands are its children. */
export default function LongCount({
  children,
  theme = defaultTheme,
}: {
  children: React.ReactNode;
  theme?: ChartsTheme;
}) {
  const [state, update] = useUrlState();
  const elections = useMemo(() => filterElections(ELECTIONS, state), [state]);
  // NOTE: the `.lc-root` scope (chart font/color + the scoped CSS reset) lives on
  // each chart Island (which now also contains that chart's FilterBar) — NOT on a
  // wrapper around `children`. Wrapping the children would cascade the serif font,
  // ink color, and border reset onto the consumer's surrounding prose (e.g. the
  // article headings). The provider itself is context-only, no DOM scope.
  return (
    <ChartsThemeProvider value={theme}>
      <LongCountProvider value={{ state, update, elections, theme }}>
        {children}
      </LongCountProvider>
    </ChartsThemeProvider>
  );
}

export function NightShare() {
  const { elections, state } = useLongCount();
  return (
    <Island>
      <FilterBar />
      <NightShareChart
        elections={elections}
        from={state.from}
        to={state.to}
        kinds={state.kinds}
      />
    </Island>
  );
}

// why each dimmed San Diego point understates the true night count. Baked into
// sd_night_history.json as `artifactNotes` by scripts/build_sd_history.py and
// read from there, so the chart can never drift from the dataset.
const SD_PARTIAL_NOTES: Record<string, string> = SD_ARTIFACT_NOTES;

export function SanDiegoNightShare() {
  // San Diego's recovered record, rendered by the same NightShareChart as the
  // SF series. Fixed full range and no FilterBar: the series is sparse (~34
  // points with a 1922-2004 hole) and mixes two denominator bases, so slicing
  // it interactively invites misreading. SF-specific dressing is switched off:
  // no era trends (too few points per era), no SF count-milestone verticals,
  // no in-person floor diamonds (that overlay is an SF-only dataset).
  return (
    <Island>
      <NightShareChart
        elections={SD_NIGHT_HISTORY}
        from={1868}
        to={2026}
        kinds={new Set(["General", "Primary"])}
        config={{
          title:
            "San Diego County: how much of the vote was counted on election night",
          subtitle: "Percent counted by election night, 1871–2024",
          note: (
            <>
              Three sources, and their denominators differ. Before 1930: the
              morning paper&apos;s largest contest sum over that
              contest&apos;s certified county total. 1992 and 2004:
              news-derived (certified ballots cast minus the registrar&apos;s
              stated uncounted remainder). 2008 on: the county&apos;s final
              election-night report over certified ballots cast. Dim dashed
              dots are lower bounds only, where the paper printed majorities
              instead of votes, omitted the city, printed the city alone with
              no county total, or carried just a remote AP wire snapshot.
            </>
          ),
          footer: null,
          eraTrends: [],
          flips: {},
          partialNotes: SD_PARTIAL_NOTES,
          useFloorDiamonds: false,
          showEventLines: false,
        }}
      />
    </Island>
  );
}

export function Vbm() {
  // The vote-by-mail series is short and self-contained (1964–present), so it's
  // shown at its full range with no year filter.
  return (
    <Island>
      <VbmChart />
    </Island>
  );
}

export function CountySpeed() {
  // A cross-county comparison — California's other big counties, not the SF
  // time series — so it carries no year filter, like Vbm.
  return (
    <Island>
      <CountySpeedChart />
    </Island>
  );
}

export function CountyNightShare() {
  // Cross-county ELECTION-NIGHT share, pre vs post tech adoption, SF as the
  // control — its own toggle, no year filter (like CountySpeed/Vbm).
  return (
    <Island>
      <CountyNightShareChart />
    </Island>
  );
}

export function CountyNightTimeline() {
  // Per-county election-night share over time (small multiples) — the full
  // trajectory behind the pre/post summary. No year filter.
  return (
    <Island>
      <CountyNightTimelineChart />
    </Island>
  );
}

export function Turnout() {
  const { state } = useLongCount();
  return (
    <Island>
      <FilterBar />
      <TurnoutChart from={state.from} to={state.to} kinds={state.kinds} />
    </Island>
  );
}

export function Registration() {
  const { state } = useLongCount();
  return (
    <Island>
      <FilterBar showKinds={false} />
      <RegistrationChart from={state.from} to={state.to} />
    </Island>
  );
}

export function FranchiseFunnel({
  defaultMode,
  defaultEligibleOnly,
}: {
  defaultMode?: "counts" | "share";
  defaultEligibleOnly?: boolean;
} = {}) {
  const { state } = useLongCount();
  return (
    <Island>
      <FilterBar showKinds={false} />
      <FranchiseFunnelChart
        from={state.from}
        to={state.to}
        defaultMode={defaultMode}
        defaultEligibleOnly={defaultEligibleOnly}
      />
    </Island>
  );
}

export function Trajectory() {
  const { state, update, elections } = useLongCount();
  return (
    <Island>
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
    </Island>
  );
}

export function HelpWanted() {
  return (
    <Island wide>
      <section className="grain relative mt-16 bg-night text-paper">
        <div className="mx-auto max-w-5xl px-5 py-12">
          <p className="smallcaps text-gold">open research — help wanted</p>
          <h2 className="mt-2 max-w-3xl text-3xl font-bold leading-tight">
            Only 9 San Francisco elections still lack a night count &mdash;
            and every one is a documented dead end. Think you can beat one?
          </h2>
          <p className="mt-4 max-w-3xl text-lg leading-relaxed text-paper/85">
            The record now runs back to Gold Rush San Francisco: 304 of 313
            elections since 1849 have a recovered election-night count. The
            nine that don&rsquo;t each carry a verbatim-quoted reason &mdash;
            no day-after paper existed (1849), the count crashed (1994), the
            EXTRA printed no city figures (1944) &mdash; documented in the
            source repository. If you know a source we haven&rsquo;t tried
            &mdash; another paper, a county record, a family scrapbook &mdash;
            one photograph could close a 175-year-old gap.
          </p>
          <ol className="mt-6 max-w-3xl list-decimal space-y-2 pl-5 leading-relaxed text-paper/85">
            <li>
              Get a free{" "}
              <a
                href="https://sfpl.org"
                target="_blank"
                rel="noopener noreferrer"
                className="border-b border-gold/60 text-gold hover:bg-gold/10"
              >
                SF Public Library card
              </a>{" "}
              — it unlocks the <em>SF Chronicle</em> archive on NewsBank (back
              to 1865), via the <em>Access World News / image edition</em>.
            </li>
            <li>
              Pick a missing election and open the{" "}
              <strong>day-after issue</strong>; for elections before ~1985, page
              the image edition to the San Francisco returns.
            </li>
            <li>
              Find the box headed{" "}
              <strong>
                &ldquo;Vote of the City,&rdquo; &ldquo;Election Returns,&rdquo;
              </strong>{" "}
              or <strong>&ldquo;The City&rdquo;</strong> — a per-candidate San
              Francisco table. Check the masthead date matches (labels can be
              off by a day).
            </li>
            <li>Photograph the returns box and send it our way.</li>
          </ol>
          <p className="mt-6 flex flex-wrap gap-3">
            <a
              href={REPO}
              target="_blank"
              rel="noopener noreferrer"
              className="smallcaps inline-block border border-gold bg-gold/10 px-4 py-2 text-gold transition-colors hover:bg-gold hover:text-night"
            >
              open a pull request →
            </a>
            <a
              href="mailto:contact@growsf.org?subject=The Long Count — found data"
              className="smallcaps inline-block border border-gold bg-gold/10 px-4 py-2 text-gold transition-colors hover:bg-gold hover:text-night"
            >
              email contact@growsf.org →
            </a>
          </p>
          <p className="mt-4 max-w-3xl text-sm text-paper/60">
            Every submission is verified against certified totals and credited.
          </p>
        </div>
      </section>
    </Island>
  );
}

export function MethodNote() {
  return (
    <Island wide>
      <footer className="grain relative mt-10 bg-night text-paper/75">
        <div className="mx-auto max-w-5xl px-5 py-14 text-sm leading-relaxed">
          <p className="smallcaps text-gold">method &amp; provenance</p>
          <div className="mt-4 grid gap-8 sm:grid-cols-2">
            <div>
              <p>
                2015–present: every per-release summary report published by the
                SF Department of Elections (241 releases across 18 elections),
                parsed from the Department’s own XML and TSV files and validated
                against certified totals. 1986–2014: 147 mid-canvass
                observations recovered from Wayback Machine captures of four
                generations of city results pages, frozen Lotus Domino canvass
                views, Elections Commission minutes, and the Chronicle’s
                standing “How San Francisco Voted” results tables and count
                reporting (via the paper’s NewsBank archive), with certified
                finals from the Department’s own turnout history and the
                California Secretary of State.
              </p>
            </div>
            <div>
              <p>
                Recovered values are conservative: dashed marks and “≤” bounds
                mean the truth is at or above/before the shown value. Counts for
                elections within ~32 days are provisional. “News-derived” points
                are conservative floors: the certified total minus the ballots a
                registrar told a reporter were still uncounted. 1851–1985: 227
                election-night counts read from page scans of the Chronicle,
                Call, Alta California and Sacramento Daily Union vote-tally
                boxes and count reporting, every digit independently
                re-verified and checked against certified totals — the
                pre-1965 figures (193 elections, recovered 2026) extend the
                record back to the hand-count era. A records request with the Department is in
                progress for the remaining web-era gaps.
              </p>
            </div>
          </div>
          <p className="smallcaps mt-8 text-paper/55">
            built from the sf-election-count pipeline ·{" "}
            <a
              href={REPO}
              target="_blank"
              rel="noopener noreferrer"
              className="border-b border-gold/60 text-gold hover:bg-gold/10"
            >
              every number, sourced — the full data &amp; methodology
            </a>{" "}
            · {new Date().getFullYear()}
          </p>
        </div>
      </footer>
    </Island>
  );
}
