#!/usr/bin/python

from __future__ import division

import sys

if sys.version_info.major < 3:
    input = raw_input

try:
    x = int(input("x = "))
    y = int(input("y = "))
    z = x / y
except ValueError as e:
    print("Bad value: {}".format(e))
except ZeroDivisionError:
    print("Next time try non-zero `y`.")
else:
    print("Result is {:.2f}".format(z))
finally:
    print("Goodbye.")
