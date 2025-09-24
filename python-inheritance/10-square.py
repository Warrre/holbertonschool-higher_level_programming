#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that represents a square, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a square with size (one side only)."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
