#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base


class TestBAse(unittest.TestCase):
    """to test base class"""
    def test_id(self):
        """check id"""
        b1 = Base()
        self.assertIsNotNone(b1.id)
