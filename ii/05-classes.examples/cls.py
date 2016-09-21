class Example:
    """Example class for testing initializatoin and destruction."""

    def __init__(self, *args, **kargs):
        print("Initialization: args={}, kargs={}".format(args, kargs))

    def __del__(self):
        print("Destruction")
