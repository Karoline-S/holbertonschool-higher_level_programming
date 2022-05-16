#!/usr/bin/python3
def safe_print_division(a, b):

    result = 0

    try:
        result = a / b

    except ZeroDivisionError:
        return

    finally:
            print(f"Inside result: {result}")

    return result