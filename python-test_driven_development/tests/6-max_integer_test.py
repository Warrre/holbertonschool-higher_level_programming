#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3, 2]), 4)
        self.assertEqual(max_integer([4, 2, 3, 2]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10000, 20000, 30000]), 30000)
        self.assertEqual(max_integer([1, -float('inf'), 2]), 2)
        self.assertEqual(max_integer([float('inf'), 1, 2]), float('inf'))

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_no_args(self):
        self.assertIsNone(max_integer())

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_list(self):
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')
        self.assertEqual(max_integer(['abc', 'xyz']), 'xyz')

    def test_mixed_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'string', 2])

    def test_none_list(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            max_integer(1)

    def test_float_comparison(self):
        self.assertEqual(max_integer([1.0, 1, 2.0, 2]), 2.0)
        self.assertEqual(max_integer([0.1, 0.2, 0.3]), 0.3)
