#!/usr/bin/python3
"""a module containing one function:
lookup()
"""


def lookup(obj):
    """Function to return the attributes of an object in a list
    """

    attrs = [dir(obj)]
    return attrs
