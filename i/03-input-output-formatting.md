## Basic input, output and formatting

### Simple output

    >>> print("Quick brown fox jumped over the lazy dog.")
    Quick brown fox jumped over the lazy dog.
    >>> print("Quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog.")
    Quick brown fox jumped over the lazy dog.
    >>> print("Quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog", end=".\n")
    Quick brown fox jumped over the lazy dog.
    >>> print("a", "b", "c", "d", sep="/")
    a/b/c/d

### Simple input

    >>> print("Tell me your name: ", end='')
    >>> name = input()
    >>> print("Your name is", input("Tell me your name: "))

### Basic formatting features

    >>> text = "My name is {}."
    >>> print(text.format("John"))
    My name is John.
    >>> print(text.format("Jack"))
    My name is Jack.
    >>> import math
    >>> print("Pi is approximately {:.2f}.".format(math.pi))
    Pi is approximately 3.14
    >>> print("{} + {} = {}".format(2, 3, 2 + 3))
    2 + 3 = 5

### Final example

    >>> a = int(input("a = "))
    >>> b = int(input("b = "))
    >>> print("{} + {} = {}".format(a, b, a + b))
