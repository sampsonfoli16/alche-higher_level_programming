#!/usr/bin/python3
"""Unittests for max_integer function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        self.assertEqual(max_integer([2, 3, 1, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_negative(self):
        self.assertEqual(max_integer([-3, -2, -1]), -1)

    def test_floats(self):
        self.assertEqual(max_integer([1.2, 3.5, 2.8]), 3.5)


if __name__ == '__main__':
    unittest.main()
