import pkg_resources
# if running in development there may not be a package
try:
    __version__ = pkg_resources.get_distribution('cvhero').version
except pkg_resources.DistributionNotFound:
    __version__ = 'development'

from .pandas_printer import format_pandas
from pyperclip import copy

def format(obj):
    return format_pandas(obj)

def clip(obj):
   return copy(format(obj))




