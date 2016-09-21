#!/usr/bin/python3

"""
Python 3.x only example featuring inheritance and `super()`.
"""

class Shape:
    def __init__(self):
        super().__init__()
        self.fill = 'x'

    def query_user(self):
        self.fill = input("Fill: ")


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0

    def query_user(self):
        super().query_user()
        self.width = int(input("Width: "))
        self.height = int(input("Height: "))

    def draw(self):
        for i in range(self.height):
            print(self.width * self.fill)


class Square(Shape):
    def __init__(self):
        super().__init__()
        self.side = 0

    def query_user(self):
        super().query_user()
        self.side = int(input("Side: "))

    def draw(self):
        r = Rectangle()
        r.fill = self.fill
        r.width = r.height = self.side
        r.draw()

if __name__ == '__main__':
    r = Rectangle()
    r.query_user()
    r.draw()
    s = Square()
    s.query_user()
    s.draw()
