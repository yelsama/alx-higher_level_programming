#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list and idx <= len(my_list) and idx > -1:
        my_list.remove(idx + 1)
    return my_list
