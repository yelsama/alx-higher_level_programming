#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = sorted(a_dictionary)
    for x in new:
        print("{}: {}".format(x, a_dictionary(x)))
