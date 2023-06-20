#!/usr/bin/python3
'''Module for Base unit tests.'''
import unittest
from models import Base


class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        pass
