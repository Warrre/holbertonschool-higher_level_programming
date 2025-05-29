#!/usr/bin/python3
"""
Module 11-square
Définit une classe Square héritant de Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Classe Square qui hérite de Rectangle."""

    def __init__(self, size):
        """
        Initialise un carré avec une seule dimension : size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Retourne l'aire du carré
        """
        return self.__size ** 2

    def __str__(self):
        """
        Retourne une représentation lisible du carré
        """
        return f"[Square] {self.__size}/{self.__size}"
