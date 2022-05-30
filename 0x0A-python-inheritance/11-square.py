#!/usr/bin/python3
"""a module with one class: square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class defining a square, inheriting from
    class Rectangle. Instantiates with size
    Has one public method: area()
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
