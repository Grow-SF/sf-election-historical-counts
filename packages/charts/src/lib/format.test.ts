import { test, expect } from "vitest";
import { fmt } from "./format";
test("fmt groups thousands", () => { expect(fmt(271439)).toBe("271,439"); });
