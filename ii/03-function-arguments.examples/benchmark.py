from __future__ import print_function

def benchmark(wrapped):
    import time
    def wrapper(*args, **kargs):
        start = time.time()
        result = wrapped(*args, **kargs)
        delta = time.time() - start
        print("function `{}(*{}, **{})` took {:.3f}".format(
                wrapped.__name__, args, kargs, delta))
        return result
    return wrapper

def cache(wrapped):
    d = {}
    def wrapper(*args):
        if args not in d:
            d[args] = wrapped(*args)
        return d[args]
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
