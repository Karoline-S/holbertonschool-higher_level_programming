#!/usr/bin/python3

magic_count = 0

def magic_string():
    """prints the string BestSchool once and then again incremented
    by one on each call
    """
    global magic_count

    if magic_count == 0:
        magic_count += 1
        return "BestSchool"
    else:
        ret_str = "BestSchool"
        for i in range(magic_count):
            ret_str += ", Bestschool"
        magic_count += 1

        return ret_str
