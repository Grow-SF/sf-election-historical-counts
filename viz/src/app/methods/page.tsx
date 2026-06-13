import Link from "next/link";
import ledger from "@/data/ledger.json";

export const metadata = { title: "Search Log — The Long Count" };

export default function MethodsPage() {
  return (
    <main className="mx-auto max-w-5xl px-5 py-14">
      <p className="smallcaps text-faint">the long count</p>
      <h1 className="mt-2 text-4xl font-bold">The search log</h1>
      <p className="mt-5 max-w-3xl leading-relaxed">
        The complete working ledger of the archive recovery: every source
        vein opened and exhausted, every query, date window, and page range
        swept, every number ingested with its verification, and every
        candidate rejected with the reason. If you&rsquo;re hunting one of
        the{" "}
        <Link href="/missing" className="border-b border-rust/40 text-rust hover:bg-rust/10">
          missing records
        </Link>
        , start here so you don&rsquo;t redo what&rsquo;s already been
        covered.
      </p>
      <p className="mt-4">
        <Link href="/" className="border-b border-rust font-semibold text-rust hover:bg-rust/10">
          ← back to the charts
        </Link>
      </p>
      <pre className="mt-10 whitespace-pre-wrap border-t border-rule pt-6 font-mono text-[13px] leading-relaxed text-ink/90">
        {(ledger as { text: string }).text}
      </pre>
    </main>
  );
}
