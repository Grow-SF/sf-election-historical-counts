import {
  LongCount,
  NightShare,
  Vbm,
  Turnout,
  Registration,
  FranchiseFunnel,
} from "@long-count/charts";

export default function Gallery() {
  return (
    <LongCount>
      <NightShare />
      <Vbm />
      <Turnout />
      <Registration />
      <FranchiseFunnel />
    </LongCount>
  );
}
