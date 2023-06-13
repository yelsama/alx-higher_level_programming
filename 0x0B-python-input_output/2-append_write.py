#!/usr/bin/python3
"""doing appending"""


def append_write(filename="", text=""):
    """to open and append on filename"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
