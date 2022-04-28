#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    arg_list = list(sys.argv[1:])
    narg = len(sys.argv)
    result = 0
    if narg == 1:
        print(0)
    else:
        for num in arg_list:
            result += int(num)
        print(result)
