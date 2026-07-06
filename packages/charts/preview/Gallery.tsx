import {
  LongCount,
  NightShare,
  Vbm,
  CountySpeed,
  CountyNightShare,
  CountyNightTimeline,
  Turnout,
  Registration,
  FranchiseFunnel,
} from "@long-count/charts";

export default function Gallery() {
  return (
    <LongCount>
      <NightShare />
      <Vbm />
      <CountySpeed />
      <CountyNightShare />
      <CountyNightTimeline />
      <Turnout />
      <Registration />
      <FranchiseFunnel />
    </LongCount>
  );
}
