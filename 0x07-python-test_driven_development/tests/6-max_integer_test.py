#!/usr/bin/python3


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestIntMax(unittest.TestCase):

    def test_simple_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)
        self.assertEqual(max_integer([1, 2, -4, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -4, -3]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)
