#!/usr/bin/env python3
# Flatten pre-1906 NewsBank scans (image lives in the PNG ALPHA channel; RGB is
# solid black) onto white -> grayscale, optionally crop a fractional box and
# upscale, for legible reading. Without flattening, crops read blank.
#
# Usage:
#   flatten_scan.py IN.png OUT.png                         # whole page -> white/L
#   flatten_scan.py IN.png OUT.png x0 y0 x1 y1 [scale]     # frac box (0..1) + zoom
# Example: flatten_scan.py sweep_..._p3_s0.png /tmp/c.png 0.36 0 0.62 0.55 3
import sys
from PIL import Image

inp, out = sys.argv[1], sys.argv[2]
im = Image.open(inp)
if im.mode in ("RGBA", "LA"):
    bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
    flat = Image.alpha_composite(bg, im.convert("RGBA")).convert("L")
else:
    flat = im.convert("L")
if len(sys.argv) >= 7:
    W, H = flat.size
    x0, y0, x1, y1 = (float(sys.argv[i]) for i in range(3, 7))
    box = (int(x0 * W), int(y0 * H), int(x1 * W), int(y1 * H))
    flat = flat.crop(box)
    scale = float(sys.argv[7]) if len(sys.argv) >= 8 else 2.5
    flat = flat.resize((int(flat.width * scale), int(flat.height * scale)))
flat.save(out)
print(out, flat.size)
