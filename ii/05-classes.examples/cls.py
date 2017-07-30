class Example:
    """Example class for testing initializatoin and destruction."""

    def __init__(self, *args, **kargs):
        print("args = {}".format(args))
        print("kargs = {}".format(kargs))
        self.args = args
        self.kargs = kargs

    def __repr__(self):
        return "Example({})".format(self)

    def __str__(self):
        return "args={}, kargs={}".format(self.args, self.kargs)

    def __del__(self):
        print("Destruction")


if __name__ == '__main__':
    example = Example(1, 2, 3, a=4, b=5, c=6)
    print("{!r}".format(example))
