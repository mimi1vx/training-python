#!/usr/bin/python
from __future__ import print_function

import time

def benchmark(wrapped):
    def wrapper(*args):
        start = time.time()
        result = wrapped(*args)
        delta = time.time() - start
        print("function `{}(*{})` took {:.6f} seconds".format(
                wrapped.__name__, args, delta))
        return result
    return wrapper

def cache(wrapped):
    d = {}
    def wrapper(*args):
        if args not in d:
            d[args] = wrapped(*args)
        return d[args]
    # Hack to keep the name displayed correctly
    wrapper.__name__ = wrapped.__name__
    return wrapper

@benchmark
@cache
def compute(a):
    return 2**a

if __name__ == '__main__':
    x = compute(1000000)
    x = compute(1000000)
    x = compute(8000000)
    x = compute(8000000)
    x = compute(100000000)
    x = compute(100000000)
    x = compute(100000000)
