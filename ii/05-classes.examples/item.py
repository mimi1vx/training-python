class Example:
    """Example class that shows itemibute access special methods""" 

    def __init__(self):
        self._data = {}

    def __repr__(self):
        return "{}({})".format(type(self).__name__, self._data)

    def __contains__(self, name):
        return name in self._data

    def __getitem__(self, name):
        return self._data[name]

    def __setitem__(self, name, value):
        self._data[name] = value

    def __delitem__(self, name):
        del self._data[name]

if __name__ == '__main__':
    a = Example()
    a['something'] = 5
    print(a)
    print('something' in a)
    print(a['something'])
    del a['something']
