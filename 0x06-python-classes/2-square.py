#!/usr/bin/python3
class Square:
    """defines a square"""
    def __init__(self, size=0):
        """instantiates an instance of class Squre and verifies
        size type and value"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = size
