#!/usr/bin/python3
"""a module containing one function:
write_file() which writes to a file
"""


def write_file(filename="", text=""):
    """a function which writes to a file
    """

    if type(filename) != str:
        raise TypeError('filename must be a string')

    if type(text) != str:
        raise TypeError('text must be a string')

    if filename is None or filename == "":
        raise ValueError('filename cannnot be empty')

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
