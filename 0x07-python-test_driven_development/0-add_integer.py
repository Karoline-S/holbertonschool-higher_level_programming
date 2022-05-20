#!/usr/bin/python3
"""
A module with one function: 'add_integer'
I am adding another line here to fill space
"""


def add_integer(a, b=98):
    """
    adds two integers and returns the result
    receives required argument 'a' and optional argument 'b'
    converts floats to integers before addition or raises a TypeError
    if other type passed in
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
