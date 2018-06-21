#!/usr/bin/python3

"""A library for using and converting roman numbers

"""
import re

ROMAN_NUMERAL_REGEX_STRING = r"""
^                   # beginning of string
M{0,3}              # thousands: 0, M, MM, MMM
(D?C{0,3}|CD|CM)    # hundreds: 0, C, CC, CCC, CD, D, DC, DCC, DCCC, CM
(L?X{0,3}|XL|XC)    # tens: 0, X, XX, XXX, XL, L, LX, LXX, LXXX, XC
(V?I{0,3}|IV|IX)    # units: 0, I, II, III, IV, V, VI, VII, VIII, IX
$                   # end of string
"""

DIGITS = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]

class Roman(object):
    """A roman number"""
    _roman_numeral_regex = re.compile(ROMAN_NUMERAL_REGEX_STRING, re.VERBOSE)

    @classmethod
    def is_roman_numeral(cls, numeral):
        """Check a string whether it is a roman numeral"""
        if numeral == '':
            return False
        return bool(cls._roman_numeral_regex.match(numeral))

    def __init__(self, obj):
        if (isinstance(obj, str)):
            if not self.is_roman_numeral(obj):
                raise ValueError("Incorrect roman numeral: {}".format(obj))
            self._numeral = obj
        elif (isinstance(obj, int)):
            n = obj
            if n < 1 or n >= 4000:
                raise ValueError("Unsupported integer value: {}".format(n))
            self._numeral = ''
            for digit, value in DIGITS:
                count, n = divmod(n, value)
                self._numeral += digit * count
        else:
            raise TypeError("Roman numbers can be initialized using str or int, not {}".format(type(obj)))

    def __int__(self):
        numeral = self._numeral

        result = 0
        for digit, value in DIGITS:
            while numeral.startswith(digit):
                result += value
                numeral = numeral[len(digit):]
        return result

    def __str__(self):
        return self._numeral

    def __repr__(self):
        return "Roman('{0}')".format(self._numeral)
        
    def __eq__(self, other):
        return str(self) == str(other)

#    def __add__(self, other):
#        return Roman(int(self) + int(other))

#    def __add__(self, other):
#        return Roman(int(self).__add__(int(other)))

#def _add_operator(self, other):
#    return Roman(getattr(int(self), '__add__')(int(other))
#
#Roman.__add__ = _add_operator
#setattr(Roman, '__add__', _add_operator)

def _make_operator(name):
    def _operator(self, other):
        return Roman(getattr(int(self), name)(int(other)))
    return _operator
        
for name in ['__add__', '__sub__', '__mul__']:
    setattr(Roman, name, _make_operator(name))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("numeral", help="Roman or integer numeral")

    args = parser.parse_args()

    try:
        r = Roman(int(args.numeral))
    except ValueError:
        r = Roman(args.numeral)
    print("{0} = {1}".format(r, int(r)))
