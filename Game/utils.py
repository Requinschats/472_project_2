import sys
from contextlib import contextmanager


def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
