#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([100, 400, 2, 3778]), 3778)
        self.assertEqual(max_integer([-19, -450, -5, 0]), 0)
        self.assertEqual(max_integer([-1]), -1)
        self.assertIsNone(max_integer([]))

    def test_error(self):
        self.assertRaises(TypeError, max_integer, 10)
