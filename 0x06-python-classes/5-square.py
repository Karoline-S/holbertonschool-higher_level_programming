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
        self.__size = size

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """returns the current size of a square"""
        return self.__size ** 2

    def my_print(self):
        """prints instance's area to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range (self.size):
                    print("#", sep="", end="")
                print()
