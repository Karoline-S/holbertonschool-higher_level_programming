#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count = 0

    for i in range(x):
        if type(i) == int:
            try:
                print("{:d}".format(my_list[i]), sep="", end="")
                count += 1
            except IndexError:
                break

    print()
    return count
