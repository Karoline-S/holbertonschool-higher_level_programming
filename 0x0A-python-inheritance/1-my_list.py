#!/usr/bin/python3
class MyList(list):
    """a class that inherits from list class
    has one public method, 'print_sorted'
    """

    def print_sorted(self):
        print(sorted(self))
