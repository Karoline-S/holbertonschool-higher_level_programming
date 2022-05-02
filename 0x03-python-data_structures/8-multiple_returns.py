#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if str_len > 0:
        my_tuple = str_len, sentence[0]
    else:
        my_tuple = str_len, None
    return my_tuple
