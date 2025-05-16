#!/usr/bin/python3
"""
This module contains a function that prints a name.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints a message with the given first and last name.

    Args:
        first_name: The first name (must be a string).
        last_name: The last name (optional, must be a string).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
