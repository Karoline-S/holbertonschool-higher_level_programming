#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *

    nargs = len(sys.argv) - 1

    if nargs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == "+":
        print(f"{num1} + {num2} = {add(num1, num2)}")

    elif operator == "-":
        print(f"{num1} - {num2} = {sub(num1, num2)}")

    elif operator == '*':
        print(f"{num1} * {num2} = {mul(num1, num2)}")

    elif operator == "/":
        print(f"{num1} / {num2} = {div(num1, num2)}")

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
