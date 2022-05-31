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

    def to_json(self):
        return self.__dict__
