import "@testing-library/jest-dom/vitest";

// --- recharts <ResponsiveContainer> shim for jsdom --------------------------
// ResponsiveContainer sizes its chart by creating a ResizeObserver and reading
// the container's getBoundingClientRect() on mount. Under jsdom ResizeObserver
// is undefined and getBoundingClientRect() returns all-zeros, so recharts logs
// "The width(0) and height(0) of chart should be greater than 0". Define a
// no-op ResizeObserver and report a fixed non-zero box so the charts lay out at
// 800x400 and the smoke tests stay pristine. The smoke assertions target HTML
// chrome (titles/legends) rendered outside the SVG, so the exact size is moot.
class ResizeObserverStub {
  observe() {}
  unobserve() {}
  disconnect() {}
}
globalThis.ResizeObserver =
  ResizeObserverStub as unknown as typeof ResizeObserver;

const CHART_RECT: DOMRect = {
  width: 800,
  height: 400,
  top: 0,
  left: 0,
  right: 800,
  bottom: 400,
  x: 0,
  y: 0,
  toJSON() {},
};
Element.prototype.getBoundingClientRect = () => CHART_RECT;
