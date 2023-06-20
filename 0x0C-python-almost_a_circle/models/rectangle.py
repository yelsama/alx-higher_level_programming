#!/usr/bin/python3
"""Base class as requested"""
from models.base import Base


class Rectangle(Base):
    """rectangle class inhrets from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int or type(height) is not int:
            raise TypeError()
        if width < 1 or height < 1:
            raise ValueError()
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 1:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("Must be integer")
        if height < 1:
            raise ValueError("must be >= 1")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
