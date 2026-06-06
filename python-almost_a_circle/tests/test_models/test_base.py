#!/usr/bin/python3
"""Unit tests for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def setUp(self):
        """Reset __nb_objects before each test."""
        Base._Base__nb_objects = 0

    def test_id_assigned(self):
        """Test id is assigned correctly."""
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_id_auto(self):
        """Test id is auto incremented."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_none(self):
        """Test id with None."""
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_id_zero(self):
        """Test id with zero."""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_id_negative(self):
        """Test id with negative number."""
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string(self):
        """Test to_json_string with valid list."""
        result = Base.to_json_string([{"id": 1}])
        self.assertEqual(result, '[{"id": 1}]')

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string(self):
        """Test from_json_string with valid string."""
        result = Base.from_json_string('[{"id": 1}]')
        self.assertEqual(result, [{"id": 1}])


if __name__ == "__main__":
    unittest.main()
