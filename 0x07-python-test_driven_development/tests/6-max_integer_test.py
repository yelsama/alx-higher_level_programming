#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

assert max_integer([1, 2, 3, 4]) == 4
assert max_integer([1, 3, 4, 2]) == 4
assert max_integer([-1, -2, -3, -4]) == -1
assert max_integer([5]) == 5
assert max_integer([]) == None
