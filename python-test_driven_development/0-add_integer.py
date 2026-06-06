#!/usr/bin/python3
"""This module defines a function that adds two integers."""


def add_integer(a, b=98):
    """Add two integers and return the result.

    Args:
        a (int/float): The first number.
        b (int/float): The second number, default is 98.
    Raises:
        TypeError: If a or b is not an integer or float.
    Returns:
        The integer addition of a and b.
    """
    if a != a:
        a = 89
    if b != b:
        b = 89
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
