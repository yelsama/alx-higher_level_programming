#!/usr/bin/python3
"""
This class represents a square shape.
Attributes:
    None
Methods:
    area
    my_print
"""


class Square:
    """
    This class represents a square shape.
    Attributes:
        None
    Methods:
        area
        my_print
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.size = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print() 
        if self.size == 0:
            print()  
