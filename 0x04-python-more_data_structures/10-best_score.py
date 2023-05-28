#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = 0
    owner = None
    for i in a_dictionary:
        if a_dictionary[i] > best:
            best = a_dictionary[i]
            owner = i
    return owner
