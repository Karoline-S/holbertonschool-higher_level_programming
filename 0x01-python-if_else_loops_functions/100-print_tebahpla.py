#!/usr/bin/python3
for char_val in range(122, 96, -1):
    if char_val % 2 == 1:
        char_val = char_val - 32
    print(chr(char_val), end="")
