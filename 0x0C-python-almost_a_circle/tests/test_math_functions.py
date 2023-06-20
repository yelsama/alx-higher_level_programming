#!/usr/bin/python3
"""doing tests"""

import unittest
from math_functions import add_numbers

class MathFunctionsTest(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)

        result = add_numbers(-5, 10)
        self.assertEqual(result, 5)

        result = add_numbers(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
