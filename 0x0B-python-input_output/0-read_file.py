#!/usr/bin/python3
"""a module containing 1 function
"""


def read_file(filename=""):
    """a function that opens and reads a file
    """

    with open(filename, 'r',  encoding="utf-8") as f:
        print(f.read(), end="")
