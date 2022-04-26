# Python - if/else, loops, functions: Project 0x01
## Holberton School Foundations

 **Mandatory Tasks: Python**

0. Complete source code provided in order to print a string about the randomly generated integer as being positive or negative.
1. Complete source code provided in order to print the last digit of the variable stored in the variable number.
2. Write a program that prints the ascii alphabet in lowercase, followed by a new line.
3. Write a program that prints the ascii alphabet in lowercase, not followed by a new line.
4. Write a program that prints all numbers from 0 to 98 and in hexadecimal as illustrated on intranet.
5. Write a program that prints numbers from 0 to 99, separated by a comma and a space, in ascending order. Constraints: one loop, 2 print functions with string format, no storing strings or numbers in a variable, do not import any module.
6. Write a program that prints all possible different combinations of two digits, separated by a comma and a space. Constraints: the two numbers must be different (01 and 10 are the same), print only the smallest combination of two numbers, print in ascending order, no more than 3 print functions used, no more than 2 loops used, no storing numbers or strings in a variable, do not import any module.
7. Write a functiion that checkes for lowercase character.
8. Write a function that prints a string in uppercase followed by a new line.
9. Write a function that prints the last digit of a number.
10. Write a function that adds two integers and returns the result.
11. Write a function that computes a to the power of b and return the value.
12. Write a function that prints numbers from 1 to 100 - Fizz Buzz style.

**Mandatory Task: C - Technical interview prep**

13. Write a function that inserts a number int a sorted singly linked list

**Advanced Tasks**

14. Write a program that prints the ascii alphabet in reverse order, alternating lowercase and uppercase, not followed by a new line.
15. Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).
16. Write the Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
3           0 LOAD_FAST                0 (a)
            3 LOAD_FAST                1 (b)
            6 COMPARE_OP               0 (<)
            9 POP_JUMP_IF_FALSE       16

4          12 LOAD_FAST                2 (c)
           15 RETURN_VALUE

5     >>   16 LOAD_FAST                2 (c)
           19 LOAD_FAST                1 (b)
           22 COMPARE_OP               4 (>)
           25 POP_JUMP_IF_FALSE       36

6          28 LOAD_FAST                0 (a)
           31 LOAD_FAST                1 (b)
           34 BINARY_ADD
           35 RETURN_VALUE

7     >>   36 LOAD_FAST                0 (a)
           39 LOAD_FAST                1 (b)
           42 BINARY_MULTIPLY
           43 LOAD_FAST                2 (c)
           46 BINARY_SUBTRACT
           47 RETURN_VALUE

