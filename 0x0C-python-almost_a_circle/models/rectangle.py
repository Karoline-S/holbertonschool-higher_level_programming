#!/usr/bin/python3
"""
A module containing one class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Defines the class Rectangle, as follows:

    Private instance attributes with public getters and setters:
    __width, __height, __x, __y

    class constructor instantiates with width and height, plus optional
    x, y and id
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor: instantiates with width and height and optional
        x, y and id
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            self.__width = value
            return self.__width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            self.__height = value
            return self.__height

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            self.__x = value
            return self.__x

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            self.__y = value
            return self.__y
