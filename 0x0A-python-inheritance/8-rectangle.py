#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""this is for class"""


class Rectangle(BaseGeometry):
    """first one I write to inherit"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
