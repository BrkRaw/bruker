from .lib import *
# from .lib.ui import load

__all__ = ['BrukerLoader']
__version__ = '0.1.0'

def load(path):
    return BrukerLoader(path)