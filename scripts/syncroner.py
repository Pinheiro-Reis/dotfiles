#!/usr/bin/env python3
import sys
from . import paths, mensages

def sync():
    SRC_PATHS = paths.sources_path()
    DEST_PATHS = paths.dests_path()

    collision = False

    for dest in DEST_PATHS:
        if dest.exists() or dest.is_symlink():
            mensages.error(f"Collision detected: {dest}")
            collision = True

    if collision:
        mensages.error("Aborting sync due to collisions.")
        sys.exit(1)

    for src, dest in zip(SRC_PATHS, DEST_PATHS):
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.symlink_to(src)
        mensages.success(f"Link created: {dest} -> {src}")
