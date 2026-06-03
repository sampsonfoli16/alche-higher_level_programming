#!/usr/bin/python3
"""Find the maximum integer in a list.

Function `max_integer(list=[])` returns the biggest integer in a list or
`None` if the list is empty.
"""


def max_integer(list=None):
    """Return the max integer from `list` or None for empty list."""
    if list is None:
        return None
    if len(list) == 0:
        return None

    max_val = list[0]
    for item in list[1:]:
        if item > max_val:
            max_val = item
    return max_val
