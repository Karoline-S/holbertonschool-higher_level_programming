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

    class constructor instantiates with size (converted to width and height,
    plus optional x, y and id

    Magic methods overwritten:
    __str__()
    """

    def __init__(self, size, x=0, y=0, id=None):
        """constructor: instantiates via call to super logic, with width
        and height and optional x, y and id
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """sets string and print output for Rectangle instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - "\
            f"{self.width}"
