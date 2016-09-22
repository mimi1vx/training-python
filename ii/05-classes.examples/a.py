a = 10
b = 9

def assertEquals(first, second):
    if first != second:
        raise Exception("Assertion failed: {} doesn't equal {}.".format(first, second))

assertEquals(a, b)
