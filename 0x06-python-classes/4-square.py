#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0):
        """instantiates an instance of class Square and verifies
        size type and value"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = size

    def area(self):
        """returns the current size of a square"""
        if self._Square__size:
            return self._Square__size ** 2

    @property
    def size(self):
        """get size"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """set size"""
        if not value:
            return self._Square__size
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = value
