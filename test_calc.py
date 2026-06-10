import pytest

from calc import add, subtract, multiply, divide, power, modulo


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4
    assert subtract(-1, -1) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0


def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(5, 2) == 2.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1


def test_modulo():
    assert modulo(10, 3) == 1
    assert modulo(9, 3) == 0
    assert modulo(7, 2) == 1
