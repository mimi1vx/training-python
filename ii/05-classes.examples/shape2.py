#!/usr/bin/python3

class Shape:
    def __init__(self, fill='x'):
        self.fill = fill

    def query_user(self):
        self.fill = input("Fill: ")


class Rectangle(Shape):
    def __init__(self, fill='x', width=0, height=0):
        super().__init__(fill)
        self.width = width
        self.height = height

    def query_user(self):
        super().query_user()
        self.width = int(input("Width: "))
        self.height = int(input("Height: "))

    def draw(self):
        for i in range(self.height):
            print(self.width * self.fill)


class Square(Rectangle):
    def __init__(self, fill='x', side=0):
        Shape.__init__(self, fill)
        self.side = side

    def query_user(self):
        Shape.query_user(self)
        self.side = int(input("Side: "))

    @property
    def width(self):
        return self.side
    
    @property
    def height(self):
        return self.side


if __name__ == '__main__':
    s = Square()
    s.query_user()
    s.draw()
