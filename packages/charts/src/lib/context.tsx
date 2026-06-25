"use client";
import { createContext, useContext } from "react";
import { Election } from "@long-count/data";
import { UrlState } from "./useUrlState";
import type { ChartsTheme } from "../theme";

type LongCountValue = {
  state: UrlState;
  update: (patch: Partial<UrlState>) => void;
  elections: Election[];
  theme: ChartsTheme;
};

const LongCountContext = createContext<LongCountValue | null>(null);

export const LongCountProvider = LongCountContext.Provider;

/** Shared filter/URL state + the filtered election list, so charts embedded
 *  directly in the MDX prose all read the same FilterBar selection. */
export function useLongCount(): LongCountValue {
  const v = useContext(LongCountContext);
  if (!v) throw new Error("useLongCount must be used inside <LongCount>");
  return v;
}
