#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_digit = int(str(number_str[-1]))

if number > 0 and last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is zero")
elif number > 0 and last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and"
          " not zero")
else:
    print(f"Last digit of {number} is -{last_digit} and is less than"
          " 6 and not zero")
