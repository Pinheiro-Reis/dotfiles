import shutil
from . import paths

def clear():
    DESTS_PATH = paths.dests_path()

    for dest in DESTS_PATH:
        if dest.is_symlink() or dest.is_file():
            dest.unlink()
        elif dest.is_dir():
            shutil.rmtree(dest)
