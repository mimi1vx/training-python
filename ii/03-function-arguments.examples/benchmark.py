#!/usr/bin/python3

import time
from copy import copy

def benchmark(wrapped):
    def wrapper(*args):
        start = time.time()
        result = wrapped(*args)
        delta = time.time() - start
        print("function `{}(*{})` took {:.6f} seconds".format(
                wrapped.__name__, args, delta))
        return result
    return wrapper

def cache(initial_data):
    def cache(wrapped):
        d = copy(initial_data)
        def wrapper(*args):
            if args not in d:
                d[args] = wrapped(*args)
            return d[args]
        # Hack to keep the name displayed correctly
        wrapper.__name__ = wrapped.__name__
        return wrapper
    return cache

@benchmark
@cache({(1000000,): 0})
def compute(a):
    return 2**a

#compute = benchmark(compute)

if __name__ == '__main__':
    x = compute(1000000)
    x = compute(1000000)
    x = compute(8000000)
    x = compute(8000000)
    x = compute(100000000)
    x = compute(100000000)
    x = compute(100000000)

#class:
#    @user_has_privilege("MODIFY")
#    def handle_modification(self, data):
#        return True
