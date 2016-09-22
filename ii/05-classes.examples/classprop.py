class classproperty(object):

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, owner_self, owner_cls):
        return self.getter(owner_cls)


class C(object):
    a = 5

    @classproperty
    def x(cls):
        return cls.a


if __name__ == '__main__':
    print(C.x)
