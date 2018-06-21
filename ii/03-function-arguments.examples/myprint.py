import functools
    
stream = open("output.txt", "a", buffering=1)
print = functools.partial(print, file=stream)
