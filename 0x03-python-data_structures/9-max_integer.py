#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        biggest = my_list[0]
        for num in my_list:
            if num > biggest:
                biggest = int(num)
    return biggest
