#!/usr/bin/python3
def magic_calculations(a, b):

    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)

        for i in range(4, 60):
            c = add(c, i)
        return c

    return sub(a, b)
