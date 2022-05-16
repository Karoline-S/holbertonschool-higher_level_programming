#!/usr/bin/python3
def safe_function(fct, *args):

    import sys

    try:
        return fct(*args)

    except BaseException as e:
        print("Exception: ", end="", file=sys.stderr)
        print(e, file=sys.stderr)
        return None
