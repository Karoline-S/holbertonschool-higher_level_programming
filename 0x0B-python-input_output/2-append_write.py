#!/usr/bin/python3
"""a module containing a single function:
append_write()
"""


def append_write(filename="", text=""):
    """a function that appends the string at
    text into the file at filename
    """

    if type(filename) != str:
        raise TypeError('filename must be a string')
    if type(text) != str:
        raise TypeError('text must be  a string')

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
