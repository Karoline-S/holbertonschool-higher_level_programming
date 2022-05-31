#!/usr/bin/python3
"""a module containing a single class:
Student
"""


class Student:
    """class defining a student.
    instantiates with firstname, lastname, age - public instance
    attributes

    has one public method: to_json
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list:
            for item in attrs:
                if type(item) != str:
                    return self.__dict__
            return {item: self.__dict__[item] for item in attrs
                    if hasattr(self, item)}
        return self.__dict__
