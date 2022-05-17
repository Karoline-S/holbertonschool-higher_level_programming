#!/usr/bin/python3
"""a class for a Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """instantiates an instance of class Squre and verifies
        size type and value"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
