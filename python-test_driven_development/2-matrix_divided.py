#!/usr/bin/python3
"""Divide all elements of a matrix by a number.

Function matrix_divided validates the matrix and divisor
and returns a new matrix with each element divided and
rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divide all elements of matrix by div and return new matrix.

    Validates types and row sizes per project specification.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    if len(matrix) == 0:
        return []

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError(
                'Each row of the matrix must have the same size')
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    ' of integers/floats')

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(item / div, 2) for item in row] for row in matrix]
