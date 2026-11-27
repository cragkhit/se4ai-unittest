"""Unit tests for rational.py.

Add your tests here: at least one for every public method of Rational.
"""
from rational import Rational


def test_add():
    x = Rational(1, 2)
    y = Rational(1, 4)

    result = x.add(y)

    assert result.numerator == 3
    assert result.denominator == 4

def test_subtract():
    x = Rational(3, 4)
    y = Rational(1, 2)

    result = x.subtract(y)

    assert result.numerator == 1
    assert result.denominator == 4

def test_multiply():
    x = Rational(2, 3)
    y = Rational(3, 4)

    result = x.multiply(y)

    assert result.numerator == 1
    assert result.denominator == 2

def test_divide():
    x = Rational(3, 5)
    y = Rational(2, 7)

    result = x.divide(y)

    assert result.numerator == 21
    assert result.denominator == 10

def test_simplify():
    x = Rational(4, 8)

    x._simplest_form()

    assert x.numerator == 1
    assert x.denominator == 2

def test_equal():
    x = Rational(1, 2)
    y = Rational(2, 4)

    assert x == y

def test_string():
    x = Rational(3, 4)

    assert str(x) == "3/4"