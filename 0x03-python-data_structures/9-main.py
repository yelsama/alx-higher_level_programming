#!/usr/bin/python3
my_def = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = my_def(my_list)
print("Max: {}".format(max_value))
