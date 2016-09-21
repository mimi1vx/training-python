import math

class Square:
    def __init__(self, side=1):
        self.side = float(side)

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, area):
        self.side = math.sqrt(area)

if __name__ == '__main__':
    square = Square()
    square.area = 25
    print(square.side)
