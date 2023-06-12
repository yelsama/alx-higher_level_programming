#!/usr/bin/python3
"""last in bonus"""

def add_attribute(obj, attr_name, attr_value):
    """try attributes"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
