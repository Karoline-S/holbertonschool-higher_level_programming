#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """a function to check whether obj is an instance of a_class
    includes inherited classes
    """

    return isinstance(obj, a_class)
