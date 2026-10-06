#!/usr/bin/env python3
"""Fail if a page links to a local file that doesn't exist, or the DMG is missing/empty."""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
bad = []
for page in root.rglob("*.html"):
    if ".git" in page.parts: continue
    html = page.read_text()
    for ref in re.findall(r'(?:href|src|srcset)="([^"#?]+)', html):
        if re.match(r"(https?:|mailto:|data:|//)", ref): continue
        for part in ref.split(","):
            p = part.strip().split(" ")[0]
            if not p: continue
            target = (root / p.lstrip("/")) if p.startswith("/") else (page.parent / p)
            if target.is_dir(): target = target / "index.html"
            if not target.exists(): bad.append(f"{page.relative_to(root)} -> {p}")
dmg = root / "clippy" / "Clippy.dmg"
if not dmg.exists() or dmg.stat().st_size < 100_000: bad.append("clippy/Clippy.dmg missing or too small")
if bad:
    print("Broken references:\n  " + "\n  ".join(bad)); sys.exit(1)
print("All local references resolve.")
