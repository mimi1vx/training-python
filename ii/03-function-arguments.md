# Functions, scopes and arguments

## Function objects

 * Defining functions using `def`
 * Documentation
     - Ref: https://www.python.org/dev/peps/pep-0257/

## Nested functions

    def f(x):
        def g(y):
            return x * y
        return g

## Variable scope

 * Global (default in top-level, `global` in function)
 * Local (default in functions)
 * Non-local (with nested functions)

    def make_counter():
        count = 0
        def counter():
            nonlocal count
            count += 1
            return count
        return counter

## Function arguments

  * Positional and keyword arguments
  * Default argument values

    print("asdf", "zxcv")
    print("asdf", "zxcv", sep=":")

    def f(a=0, b=0, c=0):
        return a + b + c

    f()
    f(c=5)
    f(1, c=5)

## Asterisk notation

Calling functions:

    items = ["asdf", "zxcv"]
    print(*items)

    data = {"name": "John", "color": "black"}
    print("{}'s favourite color is {}.".format(data["name"], data["color"]))
    print("{name}'s favourite color is {color}.".format(name=data["name"], color=data["color"]))
    print("{name}'s favourite color is {color}.".format(**data))

Accepting arguments:

    def f(*args, **kargs):
        print(args)
        print(kargs)

Note: Distinction between passing a list/dict and passing positional/keyword arguments from a list/dict using */** notation.
