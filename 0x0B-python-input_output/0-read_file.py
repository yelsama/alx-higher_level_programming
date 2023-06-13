#!/usr/bin/python3
"""doing reading"""


def read_file(filename=""):
    """to open and read filename"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
