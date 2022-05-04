#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a_list = [set_1, set_2]
    new_set = set()
    for item in a_list:
        new_set |= a_list[0] - set.union(*a_list[1:])
        a_list = a_list[-1:] + a_list[:-1]
    return new_set
