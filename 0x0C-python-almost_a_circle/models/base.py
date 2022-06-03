#!/usr/bin/python3
"""
A module containing a Base class for all other classes
in this package
"""

import json


class Base:
    """
    Defines a Base class with:

    1 x private class attribute: __nb_objects
    1 x public instance attribute: id
    class constructor taking optional argument: id
    1 x static method: to_json_string
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor:
        increments __nb_objects with each instantiation
        if 'id' is None, id is set to __nb_objects
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of a list
        of dictionaries
        """
        if not list_dictionaries or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)
