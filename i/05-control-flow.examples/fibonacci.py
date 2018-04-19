#!/usr/bin/python3

a, b = 0, 1
while a < 100:
    print(a)
    a, b = b, a + b
print("Goodbye.")

# 0 1 1 2 3 5 8 ...
