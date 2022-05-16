#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), sep="", end="")
            count += 1
        except (TypeError, ValueError):
            continue
        except IndexError:
            print("IndexError: list index out of range")
            return

    print()
    return count
