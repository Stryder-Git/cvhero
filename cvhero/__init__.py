from .pandas_printer import format_pandas
from pyperclip import copy

def func(): return

def format(obj):
    return format_pandas(obj)

def clip(obj):
   return copy(format(obj))




