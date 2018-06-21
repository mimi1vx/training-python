#!/usr/bin/python3

from nose.tools import *

from roman import Roman

known_numerals = (
    ('I', 1),
    ('II', 2),
    ('III', 3),
    ('IV', 4),
    ('V', 5),
    ('VI', 6),
    ('IX', 9),
    ('X', 10),
    ('XI', 11),
    ('XVIII', 18),
    ('MMMDCCCLXXXVIII', 3888),
    ('MMMCMXCIX', 3999),
    ('MIX', 1009),
)
correct_numerals = [r for r, d in known_numerals]
incorrect_numerals = ['', 'IIII', 'IIX', 'VIV', 'IVI', 'B', 'MMMM', '0', '1', 'IM', 'CIVIL', 'DIM', 'VIXI', 'XIVI', 'VLIV', 'CIL', 'MIC']
incorrect_decimals = [0, -1, -10, 4000, 4001, 10000, 1000000]


def test_correct_numerals():
    """is_roman_numeral should return True for correct roman numerals."""
    for numeral in correct_numerals:
        assert_true(Roman.is_roman_numeral(numeral),
            msg="'{0}' is not an incorrect numeral.".format(numeral))
        assert_equal(numeral, str(Roman(numeral)))

def test_incorrect_numerals():
    """is_roman_numeral should return False for strings that are not roman numerals."""
    for numeral in incorrect_numerals:
        assert_false(Roman.is_roman_numeral(numeral),
            msg="'{0}' is a correct numeral.".format(numeral))
        assert_raises(ValueError, Roman, numeral)

def test_incorrect_decimals():
    """Zero and negative integers are not supported."""
    for number in incorrect_decimals:
        try:
            assert_raises(ValueError, Roman, number)
        except AssertionError:
            raise AssertionError("Incorrect decimal {} didn't raise ValueError.".format(number))

def test_bad_type():
    """is_roman_numeral should raise TypeError for non-string arguments"""
    for numeral in (None, 0, 1, 1.0):
        assert_raises(TypeError, Roman.is_roman_numeral, numeral)
    for obj in (None, 1.0):
        assert_raises(TypeError, Roman, numeral)

def test_from_integer():
    """Roman(integer) makes a correct numeral."""
    for numeral, value in known_numerals:
        assert_equal(str(Roman(value)), numeral)

def test_to_integer():
    """Roman(numeral) converts to the right integer."""
    for numeral, value in known_numerals:
        assert_equal(int(Roman(numeral)), value)

def test_inversion():
    for i in range(1, 4000):
        assert_equal(int(Roman(i)), i)

def test_add():
    assert_equal(Roman(3987) + Roman(12), Roman(3999))

def test_sub():
    assert_equal(Roman(3987) - Roman(18), Roman(3969))

def test_mul():
    assert_equal(Roman(19) * Roman(12), Roman(228))
