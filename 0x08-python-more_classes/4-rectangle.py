#!/usr/bin/python3
"""define a Rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        _str = ""
        for i in range(self.__height - 1):
            _str += "#" * self.__width + "\n"
        _str += "#" * self.__width
        return _str

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
    