import math

def area(a=1, b=1, c=1):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def is_triangle(a, b, c):
    if a <= 0:
        return False
    if b <= 0:
        return False
    if c <= 0:
        return False

    if a >= b + c:
        return False
    if b >= a + c:
        return False
    if c >= a + b:
        return False

    return True

def is_rightangled(a, b, c):
    if not is_triangle(a, b, c):
        raise ValueError("not a triangle")
    if a**2 == b**2 + c**2:
        return True
    if b**2 == a**2 + c**2:
        return True
    if c**2 == a**2 + b**2:
        return True
    return False

def is_equilateral(a, b, c):
    if not is_triangle(a, b, c):
        raise ValueError("not a triangle")
    return a == b == c
