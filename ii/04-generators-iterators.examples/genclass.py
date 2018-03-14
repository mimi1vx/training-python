#!/usr/bin/python

# Implementation of (item ** 2 for item in range(10))

class Gen():
    def __init__(self):
        self.counter = iter(range(10))

    def __next__(self):
        return next(self.counter) ** 2

    def __iter__(self):
        return self

if __name__ == '__main__':
    g = Gen()
    print(list(g))
