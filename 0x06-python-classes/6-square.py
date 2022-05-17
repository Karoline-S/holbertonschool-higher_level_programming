#!/usr/bin/python3
"""a class for a Square"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """instantiates an instance of class Square and verifies
        size type and value"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if type(position) != tuple or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in range(len(position)):
            if position[i] < 0:
                raise TypeError('position must be a tuple of 2 positive\
integers')
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def positon(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in range(len(value)):
            if value[i] < 0:
                raise TypeError('position must be a tuple of 2 positive\
integers')
        self.__positon = value

    def area(self):
        """returns the current size of a square"""
        return self.__size ** 2

    def my_print(self):
        """prints instance's area to stdout"""
        if self.__size == 0:
            print()
        else:
            if self.position[1] > 0:
                for i in range(self.position[1]):
                    print()
            for j in range(self.size):
                for space in range(self.position[0]):
                    print(" ", sep="", end="")
                for char in range(self.size):
                    print("#", sep="", end="")
                print()
