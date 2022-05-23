#!/usr/bin/python3
"""A module containing one class 'Rectangle'
class 'Rectangle' defines a rectangle

"""


class Rectangle:
    """A class defining a Rectangle object

    instantiates with optional height and width
    getters and setters for private instances width and height
    width and height must be integers >= 0
    public methods for area and perimter of the rectangle

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value
        return self.__height

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        print_string = ""

        for i in range(self.__height):
            for j in range(self.__width):
                print_string += str(self.print_symbol)
            if i != self.__height - 1:
                print_string += "\n"
        return print_string

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        r1a = Rectangle.area(rect_1)
        r2a = Rectangle.area(rect_2)
        if r2a > r1a:
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
