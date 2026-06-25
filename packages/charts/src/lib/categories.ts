export const KINDS = ["General","Midterm","Primary","Local","Special","Recall"] as const;

export function displayKind(kind: string, year: number): string {
  if (kind === "Municipal") return "Local";
  return kind === "General" && year % 4 !== 0 ? "Midterm" : kind;
}

export const KIND_DESC: Record<string, string> = {
  General: "Presidential general election — the November ballot held every fourth year.",
  Midterm: "Midterm general election — the November ballot in the even years between presidential elections.",
  Primary: "Primary election — usually June, narrowing the field before the November general.",
  Local: "Local election — mayor, supervisors, and city measures, usually in odd years.",
  Special: "Special election — called off the regular calendar for a single measure, recall, or vacancy.",
  Recall: "Recall election — a vote on whether to remove an elected official before their term ends.",
};
