#!/usr/bin/python3
"""
A module containing a Base class for all other classes
in this package
"""

import json
from os.path import exists


class Base:
    """
    Defines a Base class with:

    1 x private class attribute: __nb_objects
    1 x public instance attribute: id
    class constructor taking optional argument: id

    2 x static method:
    to_json_string() and from_json_string()

    2 x class method:
    save_to_file(), create(), load_from_file()
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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation
        """
        if not json_string or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create an object from a list of dictionaries
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """saves a JSON string representation of list_objs
        to a .json file
        """
        new_list = []
        filename = cls.__name__ + ".json"

        if list_objs and len(list_objs) > 0:
            for item in list_objs:
                new_list.append(item.to_dictionary())

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def load_from_file(cls):
        """returns a list of objects from a string in a file
        """
        filename = cls.__name__ + ".json"

        if not exists(filename):
            return []
        with open(filename, 'r') as f:
            json_string = f.read()
        new_list = cls.from_json_string(json_string)
        for key, value in enumerate(new_list):
            new_list[key] = cls.create(**new_list[key])
        return new_list
