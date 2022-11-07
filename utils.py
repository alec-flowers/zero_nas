import os
import pathlib


def path_exist(*paths):
    for path in paths:
        isExist = os.path.exists(path)
        if not isExist:
            # Create a new directory because it does not exist
            os.makedirs(path)
            print(f"The new directory is created: {path}")


REPO_ROOT = pathlib.Path(__file__).absolute().parents[0].resolve()
assert (REPO_ROOT.exists())

DATA_PATH = (REPO_ROOT / ".data").absolute().resolve()
path_exist(DATA_PATH)