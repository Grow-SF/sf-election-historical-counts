#!/usr/bin/env python3
"""Crop+zoom a region of a scan for reading. Usage:
   uv run --with pillow python3 crop_helper.py FILE x0 y0 x1 y1 OUT
   (fractions 0-1; output upscaled 2x then capped at 1900px max side)"""
import sys
from PIL import Image
f,x0,y0,x1,y1,out=sys.argv[1],*map(float,sys.argv[2:6]),sys.argv[6]
im=Image.open(f); w,h=im.size
c=im.crop((int(w*x0),int(h*y0),int(w*x1),int(h*y1)))
c=c.resize((c.width*2,c.height*2), Image.LANCZOS)
c.thumbnail((1900,1900), Image.LANCZOS)   # API limit: images must stay under 2000px
c.save(out); print(out, c.size)
