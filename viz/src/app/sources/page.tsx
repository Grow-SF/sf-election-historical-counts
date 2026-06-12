import sources from "@/data/sources.json";
import Link from "next/link";

export const metadata = { title: "Sources — The Long Count" };

type Obs = { date: string; days: number; night?: boolean; total: number; pct: number; label: string; citation: string };
type Src = { id: string; name: string; final: number; finalSource: string; observations: Obs[] };

function Linkify({ text }: { text: string }) {
  const parts = text.split(/(https?:\/\/[^\s)]+)/g);
  return (
    <>
      {parts.map((p, i) =>
        /^https?:\/\//.test(p) ? (
          <a key={i} href={p} className="break-all border-b border-rust/40 text-rust hover:bg-rust/10" target="_blank" rel="noopener">
            {p.length > 90 ? p.slice(0, 87) + "…" : p}
          </a>
        ) : (
          <span key={i}>{p}</span>
        ),
      )}
    </>
  );
}

export default function SourcesPage() {
  const list = sources as Src[];
  return (
    <main className="mx-auto max-w-5xl px-5 py-14">
      <p className="smallcaps text-faint">the long count</p>
      <h1 className="mt-2 text-4xl font-bold">Every number, sourced</h1>
      <p className="mt-5 max-w-3xl leading-relaxed">
        Every observation in this dataset traces to a primary source: the
        Department of Elections&rsquo; own results releases (2015–present),
        Wayback Machine captures of four generations of city results pages,
        frozen Lotus Domino canvass views, Elections Commission minutes,
        certified Statements of Vote from the California Secretary of State,
        the Department&rsquo;s historical turnout tables, and San Francisco
        Chronicle count reporting and printed results tables accessed through
        the paper&rsquo;s NewsBank archive with a San Francisco Public Library
        card. &ldquo;News-derived&rdquo; values are conservative floors — the
        certified total minus the ballots a registrar told a reporter were
        still uncounted, or the sum of one contest&rsquo;s printed votes,
        which counted ballots can never be below. Newspaper content is cited,
        not republished.
      </p>
      <p className="mt-4">
        <Link href="/" className="border-b border-rust font-semibold text-rust hover:bg-rust/10">
          ← back to the charts
        </Link>
      </p>
      <div className="mt-10 space-y-10">
        {list.map((s) => (
          <section key={s.id} id={s.id} className="scroll-mt-6 border-t border-rule pt-5">
            <h2 className="text-xl font-bold">
              {s.id} <span className="font-normal text-faint">— {s.name}</span>
            </h2>
            <p className="smallcaps mt-1 text-faint">
              certified final {s.final.toLocaleString()} · {s.finalSource}
            </p>
            <ul className="mt-3 space-y-2 text-sm leading-relaxed">
              {s.observations.map((o, i) => (
                <li key={i} className="grid gap-x-4 sm:grid-cols-[7.5rem_1fr]">
                  <span className="stat-figure whitespace-nowrap text-faint">
                    {o.night ? "night" : `day ${o.days}`} · {o.pct}%
                  </span>
                  <span>
                    <strong>{o.label}.</strong> <Linkify text={o.citation} />
                  </span>
                </li>
              ))}
            </ul>
          </section>
        ))}
      </div>
    </main>
  );
}
