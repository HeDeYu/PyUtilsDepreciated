"""Top-level package for PyUtils."""
from . import file_io
from ._version import get_versions
from .file_io import *  # noqa: F401, F403

__author__ = """Deyu He"""
__email__ = "18565286660@163.com"
__version__ = get_versions()["version"]
del get_versions


__all__ = []
__all__ += file_io.__all__
