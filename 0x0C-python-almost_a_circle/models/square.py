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

    def update(self, *args, **kwargs):
        """update class variables"""
        if len(kwargs) == 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                if key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]
