#!/usr/bin/python3
"""this to comment all the file"""


def inherits_from(obj, a_class):
    """this for this funcion"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
