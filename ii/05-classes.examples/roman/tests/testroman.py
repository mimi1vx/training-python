#!/usr/bin/python
# encoding: utf-8

from nose.tools import *

import roman

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
incorrect_numerals = ['', 'IIII', 'VIV', 'IVI', 'B', 'MMMM', '0', '1', 'IM', 'CIVIL', 'DIM', 'VIXI', 'XIVI', 'VLIV', 'CIL', 'MIC']
incorrect_decimals = [0, -1, -10]


def test_correct_numerals():
    """Roman.is_roman_numeral should return True for correct roman numerals."""
    for numeral in correct_numerals:
        assert_true(roman.Roman.is_roman_numeral(numeral),
            msg="'{0}' is not an incorrect numeral.".format(numeral))
        assert_equal(numeral, str(roman.Roman(numeral)))

def test_incorrect_numerals():
    """Roman.is_roman_numeral should return False for strings that are not roman numerals."""
    for numeral in incorrect_numerals:
        assert_false(roman.Roman.is_roman_numeral(numeral),
            msg="'{0}' is a correct numeral.".format(numeral))
        assert_raises(ValueError, roman.Roman, numeral)

def test_incorrect_decimals():
    """Zero and negative integers are not supported."""
    for number in incorrect_decimals:
        assert_raises(ValueError, roman.Roman, number)

def test_bad_type():
    """Roman.is_roman_numeral should raise TypeError for non-string arguments"""
    for numeral in (None, 0, 1, 1.0):
        assert_raises(TypeError, roman.Roman.is_roman_numeral, numeral)
    for obj in (None, 1.0):
        assert_raises(TypeError, roman.Roman, numeral)

def test_from_integer():
    """Roman(integer) makes a correct numeral."""
    for numeral, value in known_numerals:
        assert_equal(str(roman.Roman(value)), numeral)

def test_to_integer():
    """Roman(numeral) converts to the right integer."""
    for numeral, value in known_numerals:
        assert_equal(int(roman.Roman(numeral)), value)

def test_inversion():
    for i in range(1, 4000):
        assert_equal(int(roman.Roman(i)), i)
