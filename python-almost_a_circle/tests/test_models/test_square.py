#!/usr/bin/python3
"""Unit tests for Square class."""
import unittest
import os
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_square_1(self):
        """Test Square(1)."""
        s = Square(1)
        self.assertEqual(s.size, 1)

    def test_square_1_2(self):
        """Test Square(1, 2)."""
        s = Square(1, 2)
        self.assertEqual(s.x, 2)

    def test_square_1_2_3(self):
        """Test Square(1, 2, 3)."""
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_square_string_size(self):
        """Test Square('1')."""
        with self.assertRaises(TypeError):
            Square("1")

    def test_square_string_x(self):
        """Test Square(1, '2')."""
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_square_string_y(self):
        """Test Square(1, 2, '3')."""
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_square_1_2_3_4(self):
        """Test Square(1, 2, 3, 4)."""
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.id, 4)

    def test_square_neg_size(self):
        """Test Square(-1)."""
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_neg_x(self):
        """Test Square(1, -2)."""
        with self.assertRaises(ValueError):
            Square(1, -2)

    def test_square_neg_y(self):
        """Test Square(1, 2, -3)."""
        with self.assertRaises(ValueError):
            Square(1, 2, -3)

    def test_square_zero(self):
        """Test Square(0)."""
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        """Test __str__ for Square."""
        s = Square(5, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 5")

    def test_to_dictionary(self):
        """Test to_dictionary() in Square."""
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)

    def test_update_no_args(self):
        """Test update() in Square."""
        s = Square(1)
        s.update()
        self.assertEqual(s.size, 1)

    def test_update_89(self):
        """Test update(89) in Square."""
        s = Square(1)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_update_89_1(self):
        """Test update(89, 1) in Square."""
        s = Square(1)
        s.update(89, 1)
        self.assertEqual(s.size, 1)

    def test_update_89_1_2(self):
        """Test update(89, 1, 2) in Square."""
        s = Square(1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)

    def test_update_89_1_2_3(self):
        """Test update(89, 1, 2, 3) in Square."""
        s = Square(1)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs_id(self):
        """Test update(**{ 'id': 89 }) in Square."""
        s = Square(1)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_update_kwargs_id_size(self):
        """Test update(**{ 'id': 89, 'size': 1 }) in Square."""
        s = Square(1)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_update_kwargs_id_size_x(self):
        """Test update(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square."""
        s = Square(1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_update_kwargs_all(self):
        """Test update(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 }) in Square."""
        s = Square(1)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create_id(self):
        """Test Square.create(**{ 'id': 89 }) in Square."""
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)

    def test_create_id_size(self):
        """Test Square.create(**{ 'id': 89, 'size': 1 }) in Square."""
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)

    def test_create_id_size_x(self):
        """Test Square.create(**{ 'id': 89, 'size': 1, 'x': 2 }) in Square."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)

    def test_create_all(self):
        """Test Square.create(**{ 'id': 89, 'size': 1, 'x': 2, 'y': 3 })."""
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file_none(self):
        """Test Square.save_to_file(None) in Square."""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_empty(self):
        """Test Square.save_to_file([]) in Square."""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file(self):
        """Test Square.save_to_file([Square(1)]) in Square."""
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as f:
            self.assertIn("size", f.read())

    def test_load_from_file_no_file(self):
        """Test Square.load_from_file() when file doesn't exist."""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file(self):
        """Test Square.load_from_file() when file exists."""
        Square.save_to_file([Square(1)])
        result = Square.load_from_file()
        self.assertIsInstance(result[0], Square)


if __name__ == "__main__":
    unittest.main()

    def test_to_dictionary_type(self):
        """Test to_dictionary() returns dict in Square."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(type(d), dict)

    def test_to_dictionary_keys(self):
        """Test to_dictionary() has correct keys in Square."""
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        self.assertIn('id', d)
        self.assertIn('size', d)
        self.assertIn('x', d)
        self.assertIn('y', d)

    def test_save_to_file_none_type(self):
        """Test Square.save_to_file(None) creates file."""
        Square.save_to_file(None)
        self.assertTrue(os.path.exists("Square.json"))
