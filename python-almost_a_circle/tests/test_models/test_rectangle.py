#!/usr/bin/python3
"""Unit tests for Rectangle class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_1_2(self):
        """Test Rectangle(1, 2)."""
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_rectangle_1_2_3(self):
        """Test Rectangle(1, 2, 3)."""
        r = Rectangle(1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_rectangle_1_2_3_4(self):
        """Test Rectangle(1, 2, 3, 4)."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_rectangle_string_width(self):
        """Test Rectangle('1', 2)."""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)

    def test_rectangle_string_height(self):
        """Test Rectangle(1, '2')."""
        with self.assertRaises(TypeError):
            Rectangle(1, "2")

    def test_rectangle_string_x(self):
        """Test Rectangle(1, 2, '3')."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")

    def test_rectangle_string_y(self):
        """Test Rectangle(1, 2, 3, '4')."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_rectangle_1_2_3_4_5(self):
        """Test Rectangle(1, 2, 3, 4, 5)."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)

    def test_rectangle_neg_width(self):
        """Test Rectangle(-1, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_rectangle_neg_height(self):
        """Test Rectangle(1, -2)."""
        with self.assertRaises(ValueError):
            Rectangle(1, -2)

    def test_rectangle_zero_width(self):
        """Test Rectangle(0, 2)."""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_rectangle_zero_height(self):
        """Test Rectangle(1, 0)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_rectangle_neg_x(self):
        """Test Rectangle(1, 2, -3)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)

    def test_rectangle_neg_y(self):
        """Test Rectangle(1, 2, 3, -4)."""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        """Test area()."""
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_str(self):
        """Test __str__ for Rectangle."""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_display_no_x_y(self):
        """Test display() without x and y."""
        r = Rectangle(2, 2)
        from io import StringIO
        import sys
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "##\n##\n")

    def test_display_no_y(self):
        """Test display() without y."""
        r = Rectangle(2, 2, 1)
        from io import StringIO
        import sys
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ##\n ##\n")

    def test_display(self):
        """Test display()."""
        r = Rectangle(2, 2, 1, 1)
        from io import StringIO
        import sys
        captured = StringIO()
        sys.stdout = captured
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n ##\n ##\n")

    def test_to_dictionary(self):
        """Test to_dictionary() in Rectangle."""
        r = Rectangle(10, 2, 1, 9, 1)
        d = r.to_dictionary()
        self.assertIsInstance(d, dict)

    def test_update_no_args(self):
        """Test update() in Rectangle."""
        r = Rectangle(1, 2)
        r.update()
        self.assertEqual(r.width, 1)

    def test_update_89(self):
        """Test update(89) in Rectangle."""
        r = Rectangle(1, 2)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_update_89_1(self):
        """Test update(89, 1) in Rectangle."""
        r = Rectangle(1, 2)
        r.update(89, 1)
        self.assertEqual(r.width, 1)

    def test_update_89_1_2(self):
        """Test update(89, 1, 2) in Rectangle."""
        r = Rectangle(1, 2)
        r.update(89, 1, 2)
        self.assertEqual(r.height, 2)

    def test_update_89_1_2_3(self):
        """Test update(89, 1, 2, 3) in Rectangle."""
        r = Rectangle(1, 2)
        r.update(89, 1, 2, 3)
        self.assertEqual(r.x, 3)

    def test_update_89_1_2_3_4(self):
        """Test update(89, 1, 2, 3, 4) in Rectangle."""
        r = Rectangle(1, 2)
        r.update(89, 1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_update_kwargs_id(self):
        """Test update(**{ 'id': 89 }) in Rectangle."""
        r = Rectangle(1, 2)
        r.update(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_update_kwargs_id_width(self):
        """Test update(**{ 'id': 89, 'width': 1 }) in Rectangle."""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_update_kwargs_id_width_height(self):
        """Test update(**{ 'id': 89, 'width': 1, 'height': 2 }) in Rectangle."""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_update_kwargs_id_width_height_x(self):
        """Test update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })."""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_update_kwargs_all(self):
        """Test update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })."""
        r = Rectangle(1, 2)
        r.update(**{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_create_id(self):
        """Test Rectangle.create(**{ 'id': 89 }) in Rectangle."""
        r = Rectangle.create(**{'id': 89})
        self.assertEqual(r.id, 89)

    def test_create_id_width(self):
        """Test Rectangle.create(**{ 'id': 89, 'width': 1 }) in Rectangle."""
        r = Rectangle.create(**{'id': 89, 'width': 1})
        self.assertEqual(r.width, 1)

    def test_create_id_width_height(self):
        """Test Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2 })."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(r.height, 2)

    def test_create_id_width_height_x(self):
        """Test Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3 })."""
        r = Rectangle.create(**{'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(r.x, 3)

    def test_create_all(self):
        """Test Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4 })."""
        r = Rectangle.create(
            **{'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(r.y, 4)

    def test_save_to_file_none(self):
        """Test Rectangle.save_to_file(None) in Rectangle."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test Rectangle.save_to_file([]) in Rectangle."""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        """Test Rectangle.save_to_file([Rectangle(1, 2)]) in Rectangle."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r") as f:
            self.assertIn("width", f.read())

    def test_load_from_file_no_file(self):
        """Test Rectangle.load_from_file() when file doesn't exist."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_from_file(self):
        """Test Rectangle.load_from_file() when file exists."""
        Rectangle.save_to_file([Rectangle(1, 2)])
        result = Rectangle.load_from_file()
        self.assertIsInstance(result[0], Rectangle)


if __name__ == "__main__":
    unittest.main()
