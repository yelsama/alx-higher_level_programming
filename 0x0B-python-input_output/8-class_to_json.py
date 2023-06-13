#!/usr/bin/python3
"""convert string to json"""
import json


def class_to_json(obj):
    """converts my_obj to json representation"""
    return vars(obj)
