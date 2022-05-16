#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []

    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            new_list.append(0)
            print("wrong type")
        except ZeroDivisionError:
            new_list.append(0)
            print("division by 0")
        except IndexError:
            print("out of range")
            break
    return new_list
