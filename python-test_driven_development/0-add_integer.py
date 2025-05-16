#!/usr/bin/python3
"""
This module has a function that adds two numbers.
"""

def add_integer(a, b=98):
    """
    Add two numbers a and b (default is 98).

    If a or b is float, they will be converted to integers.
    If a or b is not a number, raise a TypeError.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
