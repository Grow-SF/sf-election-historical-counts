import {
  LongCount,
  NightShare,
  SanDiegoNightShare,
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
      <SanDiegoNightShare />
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
