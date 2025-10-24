#!/usr/bin/env python
import os
from pathlib import Path
import sys

ROOT = Path("./root").resolve()

if not ROOT.exists():
    print(f"Source not found: {ROOT}")
    sys.exit(1)

if os.geteuid() != 0:
    print("This script must be run as root (sudo).")
    sys.exit(1)

for item in ROOT.iterdir():
    target = Path("/") / item.name
    if target.exists() or target.is_symlink():
        print(f"[skip] removing existing: {target}")
        if target.is_dir() and not target.is_symlink():
            import shutil

            shutil.rmtree(target)
        else:
            target.unlink()
    print(f"[link] {target} -> {item}")
    os.symlink(item, target)
