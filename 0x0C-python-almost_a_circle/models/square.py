#!/usr/bin/python3
"""set square class that inherts from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """check the class code"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overites the string for rectangle"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
