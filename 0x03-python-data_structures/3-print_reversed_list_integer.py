#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list) - 1
    if l < 1:
        return
    for i in range(l, -1, -1):
        print("{:d}".format(my_list[i]))
