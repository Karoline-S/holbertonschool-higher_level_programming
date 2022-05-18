#!/usr/bin/python3
"""a class for a Square"""


class Square:
    """
    defines a square
    """
    def __init__(self, size=0):
        """instantiates an instance of class Square and verifies
        size type and value"""
        self.size = size

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int and type(value) is not float:
            raise TypeError('size must be an number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the current size of a square"""
        self.__area = self.__size ** 2
        return self.__area

    def __eq__(self, other):
        a = self.__size ** 2
        b = other.__size ** 2
        return a == b

    def __ne__(self, other):
        a = self.__size ** 2
        b = other.__size ** 2
        return a != b

    def __gt__(self, other):
        a = self.__size ** 2
        b = other.__size ** 2
        return a > b

    def __lt__(self, other):
        a = self.__size ** 2
        b = other.__size ** 2
        return a < b

    def __ge__(self, other):
        a = self.__size ** 2
        b = other.__size ** 2
        return a >= b

    def __le__(self, other):
        a = self.__size ** 2
        b = other.__size ** 2
        return a <= b
