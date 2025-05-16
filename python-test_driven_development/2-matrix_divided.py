#!/usr/bin/python3
"""
This module contains a function that divides each number in a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Each number is divided by div and rounded to 2 decimal places.

    Args:
        matrix: list of lists with integers or floats.
        div: number (int or float) to divide by.

    Returns:
        A new matrix with all results.

    Raises:
        TypeError: if matrix is not a list of lists of numbers,
                   or if div is not a number.
        ZeroDivisionError: if div is zero.
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    return [[round(item / div, 2) for item in row] for row in matrix]
