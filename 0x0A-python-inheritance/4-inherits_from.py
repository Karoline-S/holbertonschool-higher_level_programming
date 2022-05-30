#!/usr/bin/python3
def inherits_from(obj, a_class):
    """a function to check whether obj inherited from a_class's super classes
    """

    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
