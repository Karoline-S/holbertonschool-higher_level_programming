#!/usr/bin/python3
"""
A module containing a Base class for all other classes
in this package
"""


class Base:
    """
    Defines a Base class with:

    1 x private class attribute: __nb_objects
    1 x public instance attribute: id
    class constructor taking optional argument: id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor:
        increments __nb_objects with each instantiation
        if 'id' is None, id is set to __nb_objects
        
        """

        __nb_objects += 1
        if id is None:
            self.id = __nb_objects
        else:
            self.id = id
