#!/usr/bin/python3
"""doing reading"""


def write_file(filename="", text=""):
    """to open and read filename"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
