#!/usr/bin/python3
"""Defines unittests for models/square.py"""
import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(1), Base)

    def test_is_square(self):
        self.assertIsInstance(Square(1), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(1)
        s2 = Square(2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(1, 2)
        s2 = Square(2, 1)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(1, 2, 1)
        s2 = Square(2, 1, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(4, Square(1, 2, 3, 4).id)

    def test_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

if __name__ == "__main__":
    unittest.main()
