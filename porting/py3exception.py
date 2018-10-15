try:
    c = int(input("a = ")) / int(input("b = "))
    print(c)
except (ValueError, ZeroDivisionError) as error:
    print(error)
