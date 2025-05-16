#!/usr/bin/python3
"""
This module has a function that adds two numbers.
"""

def add_integer(a, b=98):
    """
    Add two numbers a and b (default is 98).

    If a or b is float, they will be converted to integers.
    If a or b is not a number, raise a TypeError.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number (default is 98).

    Returns:
        int: The sum of a and b as integers.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
