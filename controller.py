#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description="Run functions from scripts")
parser.add_argument(
    "--sync", action="store_true", help="Sync all files in src/ with symlinks."
)
parser.add_argument(
    "--clear",
    action="store_true",
    help="Clean all configs, included here, in you desktop.",
)
parser.add_argument(
    "--sources", action="store_true", help="Return config files source path."
)
parser.add_argument(
    "--dests", action="store_true", help="Return config files destination path."
)

args = parser.parse_args()

if args.sync:
    from scripts import syncroner

    syncroner.sync()

if args.clear:
    from scripts import cleaner

    cleaner.clear()

if args.sources:
    from scripts import paths

    sources = paths.sources_path()
    for path in sources:
        print(path)

if args.dests:
    from scripts import paths

    sources = paths.dests_path()
    for path in sources:
        print(path)

