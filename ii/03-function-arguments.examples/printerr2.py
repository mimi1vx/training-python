#!/usr/bin/python

from __future__ import print_function

import sys

def partial(func, *args, **kwargs):
    def wrapper(*wargs, **wkwargs):
        nargs = wargs + args
        nkwargs = {}
        nkwargs.update(kwargs)
        nkwargs.update(wkwargs)
        return func(*nargs, **nkwargs)
    return wrapper

printerr = partial(print, file=sys.stderr)

printerr("asdf")
