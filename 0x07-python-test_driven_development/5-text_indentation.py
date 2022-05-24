#!/usr/bin/python3
"""
A module with one function: 'text_indentation'
I am adding another line here to fill space
"""


def text_indentation(text):
    """adds two new lines into a string at characters:
    '.', '?', ':'

    receives required argument text which must be a string

    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    str_list = list(text)
    new_list= []
    special_chars = ":?."

    i = 0
    for item in str_list:
        new_list.append(item)
        if item in special_chars:
            new_list.insert(i + 1, '\n\n')
            i += 3
        else:
            i += 1

    i = 0
    while i < len(new_list):
        if new_list[i] == '\n\n' and i + 1 < len(new_list):
            if new_list[i + 1] == '\n':
                while i + 1 < len(new_list) and new_list[i + 1] == '\n':
                    new_list.pop(i + 1)
            if i + 1 < len(new_list) and new_list[i + 1] == ' ':
                while i + 1 < len(new_list) and new_list[i + 1] == ' ':
                    new_list.pop(i + 1)
        i += 1

    print(''.join(new_list), end="")
