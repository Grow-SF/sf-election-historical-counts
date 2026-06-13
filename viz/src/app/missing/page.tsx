import Link from "next/link";

export const metadata = { title: "Help Complete the Record — The Long Count" };

const CONTACT = "steven@growsf.org";

type Gap = {
  id: string;
  name: string;
  want: string;
  tried: string;
};

// every remaining gap after exhausting the live web, the Wayback Machine,
// and the Chronicle's NewsBank text + page-image archives (June 2026)
const NIGHT_GAPS: Gap[] = [
  {
    id: "1985-11-05",
    name: "Municipal election",
    want: "Any contemporaneous count from election night or the days after — a results table, a registrar statement, a broadcast tally.",
    tried: "Chronicle text + image archives (day-after and day-2 papers, pages 2–12): the results ran in suburban county editions but no SF table survives there.",
  },
  {
    id: "1999-11-02",
    name: "Mayoral general (the Ammiano write-in)",
    want: "The night-of count state. Wire coverage gives a day-1 floor (70.9%) but the night itself — slowed by the write-in hand count — is undocumented.",
    tried: "Chronicle text + image archives.",
  },
  {
    id: "2000-11-07",
    name: "Presidential general",
    want: "Election-night count (we hold day-1 85.7%). The night's coverage was consumed by Bush v. Gore.",
    tried: "Chronicle text + image archives including deep page sweeps (20–40); Wayback (the city's Nov-2000 results database was wiped when reused for the December runoff).",
  },
  {
    id: "2002-12-10",
    name: "Supervisor runoffs (Districts 4 and 8)",
    want: "Any count before the official day-7 statement.",
    tried: "Chronicle archives, Wayback Machine (the city's results page was never captured mid-canvass).",
  },
  {
    id: "2003-10-07",
    name: "Statewide recall (Davis)",
    want: "San Francisco's election-night count. The Chronicle printed only statewide totals; the city's per-county night state is missing.",
    tried: "Chronicle text + image archives, Wayback Machine.",
  },
  {
    id: "2006-11-07",
    name: "General election",
    want: "Election-night count (we hold day-2 61.7%).",
    tried: "Chronicle image sweeps pages 18–33; the SF measures box wasn't in the results pages.",
  },
  {
    id: "2010-11-02",
    name: "General election",
    want: "Election-night count (we hold day-3 67.0%).",
    tried: "Chronicle image sweeps pages 15–30; only sub-citywide contests printed.",
  },
];

const ANOMALIES: Gap[] = [
  {
    id: "1964-11-03",
    name: "The senate-line anomaly",
    want: "San Francisco's certified 1964 results — the county pages of the California Secretary of State's 1964 Statement of Vote (paper or scan). The Chronicle's night table prints a senate sum (323,579) that exceeds the certified precinct-ballot total while the president line fits; one of the two official records is wrong.",
    tried: "The SoS web archive starts at 1990; no county-level 1964 source is online.",
  },
  {
    id: "1974-06-04",
    name: "A printed contradiction",
    want: "Any independent count record. The Chronicle's complete-precincts table sums Prop B to 203,381 — more ballots than the certified 198,508. Excluded from the dataset until a second source arbitrates.",
    tried: "Both day-after and day-2 papers.",
  },
  {
    id: "1978-11-07",
    name: "A printed contradiction",
    want: "The 1978 Statement of Vote county pages. The night table's governor sum exceeds the certified total; excluded pending arbitration.",
    tried: "Chronicle archives.",
  },
];

function GapList({ items }: { items: Gap[] }) {
  return (
    <div className="mt-4 space-y-5">
      {items.map((g) => (
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
  return (
    <main className="mx-auto max-w-5xl px-5 py-14">
      <p className="smallcaps text-faint">the long count</p>
      <h1 className="mt-2 text-4xl font-bold">Help complete the record</h1>
      <p className="mt-5 max-w-3xl leading-relaxed">
        This project has recovered election-night and mid-canvass counts for
        nearly every San Francisco election since 1960 — from the city&rsquo;s
        own releases, the Wayback Machine, and sixty years of newspaper
        coverage. Roughly thirty elections still lack a true election-night
        count (they appear as hollow diamonds with no dot on the night
        chart); most have day-one-or-later observations, but the night
        itself is undocumented. The entries below are the highest-value
        targets — and we&rsquo;d love help with any of them. If
        you have access to the San Francisco Examiner morgue, KQED/KRON/KPIX
        broadcast archives, Department of Elections records, a basement stack
        of old newspapers, or a relative who worked the count — these numbers
        existed once, and one photograph of the right page settles each one.
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
      <p className="mt-4">
        <Link href="/" className="border-b border-rust font-semibold text-rust hover:bg-rust/10">
          ← back to the charts
        </Link>
      </p>

      <h2 className="smallcaps mt-12 text-faint">missing election-night counts</h2>
      <GapList items={NIGHT_GAPS} />

      <h2 className="smallcaps mt-12 text-faint">contradictions awaiting a second source</h2>
      <GapList items={ANOMALIES} />

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
