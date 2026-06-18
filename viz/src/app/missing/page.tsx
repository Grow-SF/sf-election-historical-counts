import Link from "next/link";
import { ELECTIONS, NIGHT_FLOOR } from "@/lib/data";

export const metadata = { title: "Help Complete the Record — The Long Count" };

const CONTACT = "contact@growsf.org";

// Curated search history for the highest-value recoverable targets. The prose
// here is qualitative only — every number on this page is read live from the
// dataset below, so the page can never drift out of sync with the data.
const FEATURED: Record<string, { want: string; tried: string }> = {
  "2010-11-02": {
    want: "The election-night count for the November 2010 general.",
    tried:
      "Chronicle image sweeps of the results pages; only sub-citywide contests printed, and the city's own results captures begin a day later.",
  },
  "2006-11-07": {
    want: "The election-night count for the November 2006 general.",
    tried:
      "Chronicle image sweeps of the results pages; the San Francisco measures box was not among the pages digitized.",
  },
  "2003-10-07": {
    want: "San Francisco's election-night count in the statewide Davis recall. Coverage printed statewide totals; the city's own per-county night state is missing.",
    tried: "Chronicle text + image archives and the Wayback Machine.",
  },
  "2002-12-10": {
    want: "Any count before the official day-7 statement for the District 4 and 8 supervisor runoffs.",
    tried:
      "Chronicle archives and the Wayback Machine (the city's results page was never captured mid-canvass).",
  },
  "2000-11-07": {
    want: "San Francisco's election-night count. National Bush v. Gore coverage crowded out local count reporting that night.",
    tried:
      "Chronicle text + image archives including deep page sweeps; the city's November-2000 results database was wiped when it was reused for the December runoff.",
  },
  "1999-11-02": {
    want: "San Francisco's election-night count. The mayoral tally was slowed by the Ammiano write-in hand count, which makes the night state both unusually interesting and unusually undocumented.",
    tried:
      "Chronicle text + image archives and the AP wire (the source of the early floors we hold); the city's election-night results database served stale data and was never captured.",
  },
};

// Contradictions that need a *certified* source (a Statement of Vote), not an
// interim release — kept curated because the ask is specific.
const ANOMALY_IDS = new Set(["1964-11-03", "1974-06-04", "1978-11-07"]);
const ANOMALIES: { id: string; name: string; want: string; tried: string }[] = [
  {
    id: "1964-11-03",
    name: "The senate-line anomaly",
    want: "San Francisco's certified 1964 results — the county pages of the California Secretary of State's 1964 Statement of Vote (paper or scan). The Chronicle's night table prints a senate sum (323,579) that exceeds the certified precinct-ballot total while the president line fits; the two official records don't reconcile, and we'd like to see why.",
    tried: "The SoS web archive starts at 1990; no county-level 1964 source is online.",
  },
  {
    id: "1974-06-04",
    name: "A printed contradiction",
    want: "Any independent count record. The Chronicle's complete-precincts table sums Proposition B to 203,381 — more ballots than the certified 198,508. Ingested as a day-2 floor but flagged until a second source arbitrates.",
    tried: "Both day-after and day-2 papers.",
  },
  {
    id: "1978-11-07",
    name: "A printed contradiction",
    want: "The 1978 Statement of Vote county pages. The night table's governor sum (223,147) exceeds the certified total (217,965); ingested as a near-complete floor but flagged pending arbitration.",
    tried: "Chronicle archives; the California SoV's online OCR misreads the San Francisco governor line.",
  },
];

const MONTHS = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December",
];

function fmtDate(id: string): string {
  const [y, m, d] = id.split("-").map(Number);
  return `${MONTHS[m - 1]} ${d}, ${y}`;
}

function kindNoun(kind: string): string {
  return `${kind} election`;
}

// d_axis counts days since 8 PM on election night; everything in `noNight`
// is observed after the next-morning cutoff, so the floor is at least day 1.
function dayLabel(d: number): string {
  return `day ${Math.max(1, Math.round(d))}`;
}

type Gap = {
  id: string;
  date: string;
  title: string;
  held: string;
  featured?: { want: string; tried: string };
};

const elById = new Map(ELECTIONS.map((e) => [e.id, e]));
const floorById = new Map(NIGHT_FLOOR.map((f) => [f.date, f]));

// Elections with a trajectory but no election-night observation (hollow
// diamond, no dot) — we hold a later canvass floor.
const noNightGaps: Gap[] = ELECTIONS.filter((e) => e.nightPct === null).map((e) => {
  const first = [...e.pts].sort((a, b) => a[0] - b[0])[0];
  const held = first
    ? `Earliest count we hold: ${first[1]}% of the certified total on ${dayLabel(first[0])}. The election night itself is undocumented.`
    : `No dated count recovered.`;
  return { id: e.id, date: fmtDate(e.id), title: e.name, held, featured: FEATURED[e.id] };
});

// Elections we hold no contemporaneous count for at all — only a structural
// floor (the precinct share of the certified total).
const floorOnlyGaps: Gap[] = NIGHT_FLOOR.filter((f) => !elById.has(f.date)).map((f) => ({
  id: f.date,
  date: fmtDate(f.date),
  title: kindNoun(f.kind),
  held: `No contemporaneous count recovered — the only lower bound is the structural floor of ${f.floorPct}% (the precinct share of the certified total).`,
  featured: FEATURED[f.date],
}));

// Most recent (most likely recoverable) first.
const NIGHT_GAPS = [...noNightGaps, ...floorOnlyGaps].sort((a, b) =>
  a.id < b.id ? 1 : -1,
);

// Elections where only a partial election-night snapshot survives (a press-
// deadline cutoff, an absentee-only release): we'd like the complete tally.
const PARTIAL_GAPS: Gap[] = ELECTIONS.filter(
  (e) => e.nightPct !== null && e.nightPartial && !ANOMALY_IDS.has(e.id),
)
  .map((e) => ({
    id: e.id,
    date: fmtDate(e.id),
    title: e.name,
    held: `Partial election-night snapshot only (${e.nightPct}% of the certified total); the complete end-of-night tally would replace it.`,
  }))
  .sort((a, b) => (a.id < b.id ? 1 : -1));

function GapList({ items }: { items: Gap[] }) {
  return (
    <div className="mt-4 space-y-5">
      {items.map((g) => (
        <section key={g.id} className="border-t border-rule pt-4">
          <h3 className="stat-figure font-semibold">
            {g.id} <span className="font-normal text-faint">— {g.title}</span>
          </h3>
          {g.featured && <p className="mt-1 leading-relaxed">{g.featured.want}</p>}
          <p className="mt-1 text-sm">{g.held}</p>
          {g.featured && (
            <p className="mt-1 text-sm text-faint">Already searched: {g.featured.tried}</p>
          )}
        </section>
      ))}
    </div>
  );
}

function AnomalyList() {
  return (
    <div className="mt-4 space-y-5">
      {ANOMALIES.map((g) => (
        <section key={g.id} className="border-t border-rule pt-4">
          <h3 className="stat-figure font-semibold">
            {g.id} <span className="font-normal text-faint">— {g.name}</span>
          </h3>
          <p className="mt-1 leading-relaxed">{g.want}</p>
          <p className="mt-1 text-sm text-faint">Already searched: {g.tried}</p>
        </section>
      ))}
    </div>
  );
}

export default function MissingPage() {
  const totalMissing = NIGHT_GAPS.length;
  return (
    <main className="mx-auto max-w-5xl px-5 py-14">
      <p className="smallcaps text-faint">the long count</p>
      <h1 className="mt-2 text-4xl font-bold">Help complete the record</h1>
      <p className="mt-5 max-w-3xl leading-relaxed">
        This project has recovered election-night and mid-canvass counts for
        most San Francisco elections since 1907 — and a scattering back to
        1868 — from the city&rsquo;s own releases, the Wayback Machine, and a
        century and a half of newspaper coverage. {totalMissing} elections
        still lack a true election-night count (they appear as hollow diamonds
        with no dot on the night chart);
        most have a day-one-or-later observation, but the night itself is
        undocumented. The list below is generated directly from the dataset, so
        it always reflects what is still open. If you have access to the San
        Francisco Examiner morgue, KQED/KRON/KPIX broadcast archives, Department
        of Elections records, a basement stack of old newspapers, or a relative
        who worked the count — these numbers existed once, and one photograph of
        the right page settles each one.
      </p>
      <p className="mt-4 max-w-3xl leading-relaxed">
        To contribute, email{" "}
        <a
          href={`mailto:${CONTACT}?subject=The Long Count — missing data`}
          className="border-b border-rust font-semibold text-rust hover:bg-rust/10"
        >
          {CONTACT}
        </a>{" "}
        with the source (a photo, scan, or link), where it came from, and its
        date. Before you dig: the{" "}
        <Link href="/methods" className="border-b border-rust/40 text-rust hover:bg-rust/10">
          full search log
        </Link>{" "}
        documents every archive, query, and page range already covered. Every accepted submission is verified against certified totals,
        cited on the{" "}
        <Link href="/sources" className="border-b border-rust/40 text-rust hover:bg-rust/10">
          sources page
        </Link>
        , and credited if you&rsquo;d like.
      </p>

      <div className="mt-8 max-w-3xl rounded border border-rule bg-paper-deep/40 p-5">
        <p className="smallcaps text-rust">how to look — no special skills needed</p>
        <ol className="mt-3 list-decimal space-y-2 pl-5 leading-relaxed">
          <li>
            Get a free{" "}
            <a href="https://sfpl.org" className="border-b border-rust/40 text-rust hover:bg-rust/10">
              San Francisco Public Library card
            </a>{" "}
            — SF residents can sign up online (anyone in California qualifies).
          </li>
          <li>
            Your card unlocks the <strong>San Francisco Chronicle archive on
            NewsBank</strong> (back to 1865), through SFPL&rsquo;s online databases —
            use the <em>Access World News / image edition</em>.
          </li>
          <li>
            Pick a missing election from the list below and note its{" "}
            <strong>date</strong>.
          </li>
          <li>
            Open the <strong>day-after issue</strong> and find the San Francisco
            returns. For elections before ~1985, use the image edition and page
            through the front pages: look for a box headed{" "}
            <strong>&ldquo;Election Returns,&rdquo; &ldquo;Vote of the City,&rdquo;</strong>{" "}
            or <strong>&ldquo;The City&rdquo;</strong> with a per-candidate table.
            Search terms that help: the office + candidate surnames,{" "}
            <code>&ldquo;vote of the city&rdquo;</code>, <code>&ldquo;election returns&rdquo;</code>.
          </li>
          <li>
            <strong>Check the masthead date</strong> — NewsBank&rsquo;s issue labels
            are sometimes off by a day.
          </li>
          <li>
            Snap a clear photo or screenshot of the returns box and send it to{" "}
            <a
              href={`mailto:${CONTACT}?subject=The Long Count — found data`}
              className="border-b border-rust/40 text-rust hover:bg-rust/10"
            >
              {CONTACT}
            </a>{" "}
            (or open a pull request) with the date and which contest.
          </li>
        </ol>
      </div>

      <p className="mt-6">
        <Link href="/" className="border-b border-rust font-semibold text-rust hover:bg-rust/10">
          ← back to the charts
        </Link>
      </p>

      <h2 className="smallcaps mt-12 text-faint">
        missing election-night counts ({NIGHT_GAPS.length})
      </h2>
      <p className="mt-2 max-w-3xl text-sm text-faint">
        Every election with no recovered election-night count, most recent
        first. The most likely recoverable — recent enough that the
        Department&rsquo;s own release reports should survive — are at the top.
      </p>
      <GapList items={NIGHT_GAPS} />

      <h2 className="smallcaps mt-12 text-faint">
        partial night counts we&rsquo;d like to complete ({PARTIAL_GAPS.length})
      </h2>
      <p className="mt-2 max-w-3xl text-sm text-faint">
        For these we hold a partial election-night number — a press-deadline
        snapshot or an absentee-only release — but not the complete end-of-night
        tally. A full night release would upgrade each one.
      </p>
      <GapList items={PARTIAL_GAPS} />

      <h2 className="smallcaps mt-12 text-faint">contradictions awaiting a second source</h2>
      <AnomalyList />

      <h2 className="smallcaps mt-12 text-faint">always welcome</h2>
      <p className="mt-3 max-w-3xl leading-relaxed">
        Beyond the list: any per-release results report from the Department of
        Elections for 2000–2014 (the web era before the Department&rsquo;s
        archive begins), Examiner election-night front pages for any year, and
        photographs of the &ldquo;election night at City Hall&rdquo; tally
        boards. Better evidence also upgrades what we have — many pre-1996
        points are conservative floors from press-deadline snapshots, and a
        complete night table beats a partial one.
      </p>
    </main>
  );
}
