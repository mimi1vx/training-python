#!/usr/bin/python

class Gen():
    def __init__(self):
        self.counter = iter(range(10))

    def __next__(self):
        n = next(self.counter)
        return(n**2)

    def __iter__(self):
        return self

if __name__ == '__main__':
    g = Gen()
    print(list(g))
