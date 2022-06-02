#!/usr/bin/python3
"""
A module containing one class: Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines the class Rectangle, as follows:

    Private instance attributes with public getters and setters:
    __width, __height, __x, __y

    Data validation:
    __width, __height must be integers of greater than 0
    __x, __y must be integers of greater than or equal to 0

    class constructor instantiates with width and height, plus optional
    x, y and id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor: instantiates with width and height and optional
        x, y and id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width with data validation"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 1:
            raise ValueError('width must be > 0')
        self.__width = value
        return self.__width

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height with data validation"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 1:
            raise ValueError('height must be > 0')
        self.__height = value
        return self.__height

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x with data validation"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value
        return self.__x

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y with data validation"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
        return self.__y
