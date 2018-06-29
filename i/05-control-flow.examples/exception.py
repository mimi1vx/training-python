#!/usr/bin/python3

try:
    x = float(input("x = "))
    y = float(input("y = "))
    z = x / y
except ValueError as e:
    print("Bad value: {}".format(e))
except ZeroDivisionError:
    print("Next time try non-zero `y`.")
finally:
    print("Goodbye.")

print("Result is {:.2f}".format(z))
