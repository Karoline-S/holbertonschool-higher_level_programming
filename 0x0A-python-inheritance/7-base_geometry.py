#!/usr/bin/python3
"""A module containing one class: 'BaseGeometry'
"""


class BaseGeometry:
    """This class contains two public methods:
    area(),integer_validator
    """

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """a function to verify value of of type int
        """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
