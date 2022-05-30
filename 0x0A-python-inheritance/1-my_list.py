#!/usr/bin/python3
class MyList(list):
    """a class that inherits from list class
    has one public method, 'print_sorted'
    """

    def print_sorted(self):
        """a function to print a sorted list without changing
        the argument passed in in place
        """

        print(sorted(self))
