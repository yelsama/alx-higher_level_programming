#!/usr/bin/python3
"""Base class as requested"""


class Base:
    """here comes the class"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
