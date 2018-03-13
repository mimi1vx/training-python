# Generators and iterators

## Iteration

  * `for` loops
  * `iter()`, `next()`, StopIteration
  * `range()`
  * `itertools.count()`
  * Iterating over a file (`/etc/passwd`)

## Generator comprehension

  * Generator comprehension from `range(10)` nd `count()`.
  * Generator comprehension from a file

    (x**2 for x in range(10))

    (x**2 for x in itertools.count())

List and dictionary comprehensions:

    l = ["John", "Jack", "Daniel", "Frederick"]
    [name for name in l if len(name) == 4]

## Generator function

    def g():
        for x in range(10):
            yield x**2

## Generator class

    class g:
        def __init__(self):
            self.counter = iter(range(10))

        def __next__(self):
            n = next(self.counter)
            return(n)

        def __iter__(self):
            return self
