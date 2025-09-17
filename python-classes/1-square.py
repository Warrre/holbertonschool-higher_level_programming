#!/usr/bin/python3
"""Module defining a Square class with a private attribute."""


class Square:
    """Class that defines a square."""
    def __init__(self, size):
        """Initialize a new Square instance.

         Args:
            size: The size of the square (no type/value check yet).
        """
        self.__size = size
