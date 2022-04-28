#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    number_of_args = len(sys.argv) - 1

    if number_of_args == 0:
        print(f"{number_of_args} arguments.")

    else:
        if number_of_args == 1:
            print(f"{number_of_args} argument:")

        else:
            print(f"{number_of_args} arguments:")

        list_of_args = list(sys.argv[1:])
        i = 1

        for str in list_of_args:
            print(f"{i}: {str}")
            i += 1
