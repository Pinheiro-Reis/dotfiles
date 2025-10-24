from pathlib import Path
import sys

from . import mensages


def sources_root():
    SRC_ROOT = Path("./src").resolve()
    if not SRC_ROOT.exists():
        mensages.error(f"Invalid source root: {SRC_ROOT}")
        sys.exit(1)
    return SRC_ROOT


def user_home():
    USER_HOME = Path.home()
    if not USER_HOME.exists():
        mensages.error(f"Invalid home path: {USER_HOME}")
        sys.exit(1)
    return USER_HOME


def sources_path():
    SRC_ROOT = sources_root()
    SRC_PATHS = []
    for path in SRC_ROOT.iterdir():
        if path.name == ".config":
            SRC_PATHS.extend([p for p in path.iterdir()])
        else:
            SRC_PATHS.append(path)
    return SRC_PATHS


def dests_path():
    USER_HOME = user_home()
    SRC_ROOT = sources_root()
    CONFIG_ROOT = SRC_ROOT / ".config"
    DEST_PATHS = []

    for src_path in sources_path():
        try:
            rel = src_path.relative_to(CONFIG_ROOT)
            dest_path = USER_HOME / ".config" / rel
        except ValueError:
            rel = src_path.relative_to(SRC_ROOT)
            dest_path = USER_HOME / rel

        DEST_PATHS.append((src_path, dest_path))

    return DEST_PATHS
