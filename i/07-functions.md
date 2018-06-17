# Functions and local variables

  * A function is an object describing a standalone piece of code
  * Variables assigned in a function are local by default

## Function definitions and calls

    >>> import math
    >>> def triangle_area(a, b, c):
    ...     s = (a + b + c) / 2 
    ...     return math.sqrt(s * (s - a) * (s - b) * (s - c))

Default values:

    >>> import math
    >>> def triangle_area(a=1, b=1, c=1):
    ...     s = (a + b + c) / 2 
    ...     return math.sqrt(s * (s - a) * (s - b) * (s - c))

Behind the scenes:

    >>> def print_args(*args, **kwargs):
    ...     print(args, kwargs)

    >>> args = [1, 2, 3, 4]
    >>> kwargs = {"a": "alpha", "b": "beta", "c": "gamma"}
    >>> f(*args, *kwargs)

Example: `readwrite.py` (previous example rewritten in functions)
