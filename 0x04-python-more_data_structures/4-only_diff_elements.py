#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    l = [set_1, set_2]
    new_set = set()
    for item in l:
        new_set |= l[0] - set.union(*l[1:])
        l = l[-1:] + l[:-1]
    return new_set
