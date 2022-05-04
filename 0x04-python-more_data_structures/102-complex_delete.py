#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_of_keys = []
    for key, val in a_dictionary.items():
        if val == value:
            list_of_keys.append(str(key))

    for item in list_of_keys:
        del a_dictionary[item]

    return a_dictionary
