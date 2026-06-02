#!/usr/bin/python3
"""Add two integers.

Module with a single function `add_integer` that adds two numbers after
validating their types and casting floats to integers.
"""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    a and b must be integers or floats; floats are cast to int before
    addition. Raises TypeError with specific messages when types are
    invalid.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    try:
        ai = int(a)
    except (ValueError, OverflowError):
        raise TypeError('a must be an integer')

    try:
        bi = int(b)
    except (ValueError, OverflowError):
        raise TypeError('b must be an integer')

    return ai + bi
