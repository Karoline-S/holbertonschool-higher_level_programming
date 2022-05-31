#!/bin/usr/python3
"""a module containing one class:
Student
"""


class Student:
    """defines a student
    instantiates with 3 public attributes:
    first_name, last_name, age

    defines two publice methods:
    to_json and reload_from_json
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a simple dict for an object
        if attrs is a list of string keys, return
        a new dict with only these keys"""

        if type(attrs) == list:
            for item in attrs:
                if type(item) != str:
                    return self.__dict__
            return {item: self.__dict__[item] for item in attrs
                    if hasattr(self, item)}
        return self.__dict__

    def reload_from_json(self, json):
        """reloads obj from a json repr
        """
        for key, value in json.items():
            setattr(self, key, value)
