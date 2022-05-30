#!/usr/bin/python3
""" a module containing one class:
MyInt
"""


class MyInt(int):
    """an child class of int that inverts the ==
    and != operators
    """

    def __new__(cls, value, *args, **kwargs):
        return super().__new__(cls, value)

    def __eq__(self, other):
        if self > other or self < other:
            return True
        return False

    def __ne__(self, other):
        if self > other or self < other:
            return False
        return True
