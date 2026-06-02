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
    import math

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    # Reject non-finite floats (NaN, inf) explicitly
    if isinstance(a, float) and not math.isfinite(a):
        raise TypeError('a must be an integer')
    if isinstance(b, float) and not math.isfinite(b):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
