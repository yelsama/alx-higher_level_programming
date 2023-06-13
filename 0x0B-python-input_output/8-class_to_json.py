#!/usr/bin/python3
"""convert object to dictionary"""


def class_to_json(obj):
    """converts obj to json representation as dictionary"""
    return vars(obj)
