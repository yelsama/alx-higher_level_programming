#!/usr/bin/python3
"""my int"""


class MyInt(int):
    """get the oposite of the situation"""
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
