#!/usr/bin/python3
"""
A module with one function: 'print_square'
I am adding another line here to fill space
"""


def print_square(size):
    """prints a square with character '#'

    receives required argument size

    """

    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print('#', end="")
            if j == size - 1:
                print('\n', end="")
