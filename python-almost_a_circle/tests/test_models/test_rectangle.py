#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        """Test id is auto assigned."""
        r = Rectangle(10, 2)
        self.assertEqual(r.id, 1)

    def test_width_height(self):
        """Test width and height."""
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_x_y_default(self):
        """Test x and y default to 0."""
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_not_int(self):
        """Test width raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle("10", 2)

    def test_height_not_int(self):
        """Test height raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_x_not_int(self):
        """Test x raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "0")

    def test_y_not_int(self):
        """Test y raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, "0")

    def test_width_zero(self):
        """Test width raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_zero(self):
        """Test height raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_width_negative(self):
        """Test width negative raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)

    def test_height_negative(self):
        """Test height negative raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)

    def test_x_negative(self):
        """Test x negative raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1)

    def test_y_negative(self):
        """Test y negative raises ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Test area method."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test __str__ method."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        """Test update with args."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        """Test update with kwargs."""
        r = Rectangle(10, 10)
        r.update(width=5, height=3)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)

    def test_to_dictionary(self):
        """Test to_dictionary method."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertEqual(d['width'], 10)
        self.assertEqual(d['height'], 2)
        self.assertEqual(d['x'], 1)
        self.assertEqual(d['y'], 9)
        self.assertEqual(d['id'], 1)


if __name__ == "__main__":
    unittest.main()
