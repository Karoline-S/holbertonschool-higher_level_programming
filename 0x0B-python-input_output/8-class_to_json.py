#!/usr/bin/python3
"""a module containing one function:
class_to_json
"""


def class_to_json(obj):
    """returns a simple dict repr of an obj
    """
    return obj.__dict__
