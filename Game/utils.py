import sys
from contextlib import contextmanager


def any(iterable):
    for element in iterable:
        if element:
            return True
    return False


@contextmanager
def replace_stdin(target):
    orig = sys.stdin
    sys.stdin = target
    yield
    sys.stdin = orig
