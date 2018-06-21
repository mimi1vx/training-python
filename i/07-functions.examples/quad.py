import math

def solve(a=0, b=0, c=0):
    print("{}*x^2 + {}*x + {} = 0".format(a, b, c))
    if a == 0:
        if b == 0:
            if c == 0:
                return "any"
            else:
                return []
        else:
            return [-c/b]

    d = b**2 - 4*a*c
    print("d = {}".format(d))
    if d > 0:
        return [(-b-math.sqrt(d))/2*a, (-b+math.sqrt(d))/2*a]
    elif d == 0:
        return [(-b)/2*a]
    else:
        return []
        
if __name__ == '__main__':
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(solve(a, b, c))