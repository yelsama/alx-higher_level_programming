#!/usr/bin/python3
"""convert json string to object"""
import json


def from_json_string(my_str):
    """check the return"""
    return json.loads(my_str)
