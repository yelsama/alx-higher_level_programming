#!/usr/bin/python3

def text_indentation(text):
    """to print a text"""
    _pass = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if _pass:
            _pass = 0
            continue
        print(f"{i}", end="")
        if i == '.' or i == '?' or i == ':':
            print()
            print()
            _pass = 1
    print()
    print()
