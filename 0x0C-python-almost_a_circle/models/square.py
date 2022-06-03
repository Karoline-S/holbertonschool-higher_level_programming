#!/usr/bin/python3
"""
A module containing one class: Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines the class Square, as follows:

    Private instance attrs inherited from and set by Rectangle super class:
    __height, __width , __x, __y

    Private instance attribute size with public setter and getter

    Class constructor instantiates with size (converted to width and height,
    plus optional x, y and id

    Public methods:
    update()
    to_dictionary()

    Magic methods overwritten:
    __str__()
    """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor: instantiates via call to super logic, with width
        and height and optional x, y and id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """return object's size"""
        return self.width

    @size.setter
    def size(self, value):
        """set object's size to height and width after data validation
        size must be an integer greater than 0"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 1:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates attrs with value/s passed in the following order:
        id, width, height, x, y
        """
        num_args = len(args)
        a_list = ['id', 'size', 'x', 'y']

        if num_args > 3:
            self.y = args[3]
        if num_args > 2:
            self.x = args[2]
        if num_args > 1:
            self.size = args[1]
        if num_args > 0:
            self.id = args[0]
        else:
            for key, value in kwargs.items():
                if 'id' in kwargs:
                    self.id = kwargs['id']
                if 'size' in kwargs:
                    self.size = kwargs['size']
                if 'x' in kwargs:
                    self.x = kwargs['x']
                if 'y' in kwargs:
                    self.y = kwargs['y']

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """sets string and print output for Rectangle instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
            f"{self.size}"
