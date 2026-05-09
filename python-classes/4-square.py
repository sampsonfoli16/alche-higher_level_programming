#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size value to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2