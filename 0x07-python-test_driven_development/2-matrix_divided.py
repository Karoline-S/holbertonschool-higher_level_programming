#!/usr/bin/python3
"""
A module with one function: 'matrix_divided'
I am adding another line here to fill space
"""


def matrix_divided(matrix, div):
    """divides each element of matrix by div

    receives required argument 'matrix' and 'div'
    matrix must be a list of lists, div must be a float or
    int and cannot be 0
    returns a new matrix with the result
    """
    mat_err_msg = 'matrix must be a matrix (list of lists) of integers/floats'
    div_err_msg = 'div must be a number'
    zero_err_msg = 'division by zero'
    size_err_msg = 'Each row of the matrix must have the same size'

    # validate div: int or float and not 0
    if type(div) not in [int, float]:
        raise TypeError(div_err_msg)
    if div == 0:
        raise ZeroDivisionError(zero_err_msg)

    # validate matrix: a list of at least 2 items
    if type(matrix) is not list:
        raise TypeError(mat_err_msg)
    try:
        type(matrix[1])
    except IndexError:
        raise TypeError(mat_err_msg)
    if type(matrix[0]) is not list:
        raise TypeError(mat_err_msg)

    list_len = len(matrix[0])

    if list_len == 0:
        raise TypeError(mat_err_msg)

    # validate matrix: each item of type list and of equal size
    for row in matrix:
        if type(row) is not list:
            raise TypeError(mat_err_msg)
        if not len(row) == list_len:
            raise TypeError(size_err_msg)


        # validate matrix: list items are ints or floats
        for x in row:
            if type(x) not in [int, float]:
                raise TypeError(mat_err_msg)

    return [[round(x / div, 2) for x in row] for row in matrix]
