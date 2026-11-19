// make.fun news-image-20261119 entry program.
// Copies the pre-drawn infographic (entry.png, beside this file) to
// $MAKEFUN_OUTPUT_DIR/entry.png (default /output). Node 22 stdlib only.
import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const here = dirname(fileURLToPath(import.meta.url));
const src = join(here, "entry.png");
const dst = join(outDir, "entry.png");

const expected = statSync(src).size;
if (expected === 0) {
  throw new Error(`entry.png is empty: ${src}`);
}
mkdirSync(outDir, { recursive: true });
copyFileSync(src, dst);
const actual = statSync(dst).size;
if (actual !== expected) {
  throw new Error(
    `entry.png copy short: wrote ${actual} of ${expected} bytes to ${dst}`,
  );
}
console.log(`wrote ${dst} (${actual} bytes)`);
