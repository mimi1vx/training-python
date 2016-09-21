# Generators and iterators

## Iteration

  * `for` loops
  * `iter()`, `next()`, StopIteration
  * `range()`
  * `itertools.count()`

## Generator comprehension

  *

    (x**2 for x in range(10))

    (x**2 for x in itertools.count())

## Generator function

    def g():
        for x in range(10):
            return x**2

## Generator class


    class g():
        def __init__(self):
            self.counter = iter(range(10))

        def __next__(self):
            n = next(self.counter)
            return(n)

        def __iter__(self):
            return self

