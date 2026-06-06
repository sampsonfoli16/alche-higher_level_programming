#!/usr/bin/python3
"""Unit tests for Square class."""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        """Test id is auto assigned."""
        s = Square(5)
        self.assertEqual(s.id, 1)

    def test_size(self):
        """Test size attribute."""
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_x_y_default(self):
        """Test x and y default to 0."""
        s = Square(5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_size_not_int(self):
        """Test size raises TypeError."""
        with self.assertRaises(TypeError):
            Square("5")

    def test_size_zero(self):
        """Test size zero raises ValueError."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_size_negative(self):
        """Test size negative raises ValueError."""
        with self.assertRaises(ValueError):
            Square(-5)

    def test_x_negative(self):
        """Test x negative raises ValueError."""
        with self.assertRaises(ValueError):
            Square(5, -1)

    def test_y_negative(self):
        """Test y negative raises ValueError."""
        with self.assertRaises(ValueError):
            Square(5, 0, -1)

    def test_area(self):
        """Test area method."""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_str(self):
        """Test __str__ method."""
        s = Square(5, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 5")

    def test_size_setter(self):
        """Test size setter."""
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_update_args(self):
        """Test update with args."""
        s = Square(5)
        s.update(10, 2, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_kwargs(self):
        """Test update with kwargs."""
        s = Square(5)
        s.update(size=7, x=1)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 1)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertEqual(d['size'], 10)
        self.assertEqual(d['x'], 2)
        self.assertEqual(d['y'], 1)
        self.assertEqual(d['id'], 1)


if __name__ == "__main__":
    unittest.main()
