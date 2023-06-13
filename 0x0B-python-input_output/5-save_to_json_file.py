#!/usr/bin/python3
"""convert string to json"""
import json


def save_to_json_file(my_obj, filename):
    """converts my_obj to json representation"""
    with open(filename, "a") as f:
        f.write(json.dumps(my_obj))
