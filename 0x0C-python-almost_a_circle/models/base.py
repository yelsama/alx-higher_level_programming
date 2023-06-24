#!/usr/bin/python3
"""Base class as requested"""
import json


class Base:
    """here comes the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """check the name and code"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        filename = "{:s}.json".format(cls.__name__)
        content = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                content.append(cls.to_dictionary(list_objs[i]))

        with open(filename, mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(content))
