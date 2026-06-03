#!/usr/bin/python3
"""Print a square of the given size using the # character.

Function `print_square(size)` validates size and prints a square to
stdout.
"""


def print_square(size):
    """Print a square of `size` using `#`.

    Raises TypeError or ValueError for invalid `size` per project rules.
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print('#' * size)
