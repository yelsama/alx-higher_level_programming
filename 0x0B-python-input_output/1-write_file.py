#!/usr/bin/python3
"""doing writing"""


def write_file(filename="", text=""):
    """to open and write in filename"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
