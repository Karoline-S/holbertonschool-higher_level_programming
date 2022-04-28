#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4

    list_names = dir(hidden_4)

    for name in list_names:
        if name[0] != "_":
            print(name)
