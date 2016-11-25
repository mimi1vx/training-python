import sys
import functools

printerr = functools.partial(print, file=sys.stderr)
