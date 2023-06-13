#!/usr/bin/python3
"""convert string to json"""
import json


def to_json_string(my_obj):
    """converts my_obj to json representation"""
    print(json.dumps(my_obj))
