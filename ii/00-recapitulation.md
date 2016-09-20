# Recapitulation of expected Python skills

## Composite data types

  * list, tupe
  * dict, set

## Variables, identity, assignment

  * identity of mutable containers and shallow copy
  * nested mutable containers and deep copy
  * recursive objects

    import copy

    l1 = [1, 2, 3, [4, 5]]
    l2 = copy.copy(l1)
    l3 = copy.deepcopy(l2)

    l4 = [1, 2, 3]
    l4.append(l4)
    l5 = copy.copy(l5)
    l6 = copy.copy(l6)

## Basic input and output

  * print, format, input

    >>> a = input("a = ")
    >>> b = input("b = ")
    >>> print("{} + {} = {}".format(a, b, a + b))
