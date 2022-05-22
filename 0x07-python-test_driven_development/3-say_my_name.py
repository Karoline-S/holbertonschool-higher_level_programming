#!/usr/bin/python3
"""
A module with one function: 'say_my_name'
I am adding another line here to fill space
"""


def say_my_name(first_name, last_name=""):
    """prints a string containing 1 or 2 name arguments

    receives required argument 'first_name' and optional argument
    'last_name' and includes in a string printed to stdout
    """

    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if not last_name == "":
        if type(last_name) is not str:
            raise TypeError('last_name must be a string')

    first_name = first_name.strip(" ")
    last_name = last_name.strip(" ")
    first_name = first_name.title()
    last_name = last_name.title()

    print("My name is " + first_name + " " + last_name)
