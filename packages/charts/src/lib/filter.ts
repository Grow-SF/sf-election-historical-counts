import { displayKind } from "./categories";
export type Filters = { kinds: Set<string>; from: number; to: number };
export function filterElections<T extends { kind: string; year: number }>(
  elections: T[], f: Filters,
): T[] {
  return elections.filter(
    (e) => f.kinds.has(displayKind(e.kind, e.year)) && e.year >= f.from && e.year <= f.to,
  );
}
