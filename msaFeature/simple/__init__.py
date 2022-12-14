import glob
from os.path import basename, dirname, isfile, join

from .base import MSASimpleFeatureFlags, feature_enabled, feature_flag
from .router import router

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [
    basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")
]
