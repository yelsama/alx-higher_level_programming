#!/usr/bin/python3
"""append_after"""


def append_after(filename="", search_string="", new_string=""):
    """search and update"""
    read = []
    with open(filename, "r", encoding="utf-8") as f:
        read = f.readline()
        i = 0
        while i < len(read):
            if search_string in read[i]:
                read[i:i + 1] = [read[i], new_string]
                i += 1
            i += 1
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(read)
