import { defineConfig } from "vitest/config";
import { fileURLToPath } from "url";
import path from "path";

const root = path.dirname(fileURLToPath(import.meta.url));

export default defineConfig({
  resolve: {
    alias: {
      "long-count/data": path.resolve(root, "packages/data/index.ts"),
      "long-count/charts": path.resolve(root, "packages/charts/src/index.ts"),
    },
  },
  test: { environment: "jsdom", globals: true, setupFiles: ["./vitest.setup.ts"] },
});
