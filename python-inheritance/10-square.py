#!/usr/bin/python3
"""
Module 10-square
Contient la classe Square qui hérite de Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe Square héritant de Rectangle."""

    def __init__(self, size):
        """Initialise un carré (square) avec une seule dimension : size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
