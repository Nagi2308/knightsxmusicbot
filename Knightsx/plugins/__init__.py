import glob
from os.path import basename, dirname, isfile


def __list_all_modules():
    current_dir = dirname(__file__)
    mod_paths = glob.glob(current_dir + "/*.py")

    all_modules = [
        (f.replace(current_dir, "").replace("/", ".").lstrip("."))[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
