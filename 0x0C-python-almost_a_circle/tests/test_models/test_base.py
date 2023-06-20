#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models.base import Base


class TestBAse(unittest.TestCase):
    """to test base class"""
    def test_id(self):
        """check id"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertIsNotNone(b1.id)

    def test_id2(self):
        """check id"""
        Base._Base__nb_objects = 0
        b2 = Base(12)
        self.assertEqual(12, b2.id)

    def test_init(self):
        """check instance"""
        Base._Base__nb_objects = 0
        b2 = Base()
        self.assertIsInstance(b2, Base)
