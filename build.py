#!/usr/bin/env python3
"""Genera dist/index.html (un único archivo autocontenido) a partir de src/, data/ y assets/.
Uso: python3 build.py"""
import re, pathlib
root = pathlib.Path(__file__).parent
s = (root / "src" / "template.html").read_text(encoding="utf-8")
def inc(m): return (root / m.group(1)).read_text(encoding="utf-8")
s = re.sub(r"//@@INC (\S+)@@", inc, s)
s = re.sub(r"//@@ASSET (\S+)@@", inc, s)
out = root / "dist" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(s, encoding="utf-8")
print(f"OK {out} ({len(s)/1e6:.2f} MB)")
