export type Fit = {
  slope: number;
  intercept: number;
  r2: number;
  n: number;
  x0: number;
  x1: number;
};

/** Ordinary least squares over (x, y); returns null when underdetermined. */
export function linearFit(pts: [number, number][]): Fit | null {
  const n = pts.length;
  if (n < 3) return null;
  const mx = pts.reduce((s, p) => s + p[0], 0) / n;
  const my = pts.reduce((s, p) => s + p[1], 0) / n;
  let sxx = 0,
    sxy = 0,
    syy = 0;
  for (const [x, y] of pts) {
    sxx += (x - mx) ** 2;
    sxy += (x - mx) * (y - my);
    syy += (y - my) ** 2;
  }
  if (sxx === 0 || syy === 0) return null;
  const slope = sxy / sxx;
  const r2 = (sxy * sxy) / (sxx * syy);
  const xs = pts.map((p) => p[0]);
  return {
    slope,
    intercept: my - slope * mx,
    r2,
    n,
    x0: Math.min(...xs),
    x1: Math.max(...xs),
  };
}
