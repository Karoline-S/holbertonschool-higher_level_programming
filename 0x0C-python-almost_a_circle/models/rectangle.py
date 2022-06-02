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

    class constructor instantiates with width and height, plus optional
    x, y and id

    Data validation:
    __width, __height must be integers of greater than 0
    __x, __y must be integers of greater than or equal to 0

    Public methods:
    area() - returns the area of a Rectangle instance
    display() - prints a Rectangle instance using '#' to stdout
    update() - updates attrs with given arguments

    Magic methods overwritten:
    __str__()
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

    def area(self):
        """return the area of a rectangle"""
        return self.height * self.width

    def display(self):
        """prints the dimensions of a rectangle instance using '#'
        to stdout
        """
        if self.y != 0:
            for i in range(self.y):
                print()
        for i in range(self.height):
            for k in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """updates attrs with value/s passed in the following order:
        id, width, height, x, y
        """
        num_args = len(args)
        a_list = ['id', 'height', 'width', 'x', 'y']

        if num_args > 4:
            self.y = args[4]
        if num_args > 3:
            self.x = args[3]
        if num_args > 2:
            self.height = args[2]
        if num_args > 1:
            self.width = args[1]
        if num_args > 0:
            self.id = args[0]
        else:
            for key, value in kwargs.items():
                if 'id' in kwargs:
                    self.id = kwargs['id']
                if 'width' in kwargs:
                    self.width = kwargs['width']
                if 'height' in kwargs:
                    self.height = kwargs['height']
                if 'x' in kwargs:
                    self.x = kwargs['x']
                if 'y' in kwargs:
                    self.y = kwargs['y']

    def __str__(self):
        """sets string and print output for Rectangle instance"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}/{self.height}"
