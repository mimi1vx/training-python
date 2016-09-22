import math
import numbers

class Square:
    def __init__(self, side=1):
        self.side = side

    @staticmethod
    def shape():
        return "square"

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, side):
        if not isinstance(side, numbers.Number):
            raise TypeError("Use numeric value.")
        self._side = float(side)

    @property
    def area(self):
        return self._side ** 2

    @area.setter
    def area(self, area):
        if not isinstance(area, numbers.Number):
            raise TypeError("Use numeric value.")
        self._side = math.sqrt(area)

if __name__ == '__main__':
    square = Square()
    square.area = 25
    print(square.area)
    print(square.shape())
    print(Square.shape())
