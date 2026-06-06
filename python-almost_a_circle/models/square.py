#!/usr/bin/python3
"""This module defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set size."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return string representation of Square."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update Square attributes."""
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
