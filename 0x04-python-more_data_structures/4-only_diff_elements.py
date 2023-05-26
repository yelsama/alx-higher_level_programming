#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    dif1 = [x for x in set_1 if x not in set_2]
    dif2 = [x for x in set_2 if x not in set_1]
    return dif1 + dif2