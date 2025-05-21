#!/usr/bin/python3
"""Définit une classe Square avec validation de la taille."""


class Square:
    """Classe qui représente un carré."""

    def __init__(self, size=0):
        """
        Initialise un nouvel objet Square.

        Paramètre :
        size (int) : la taille du carré (doit être >= 0)

        Exceptions :
        - TypeError : si size n'est pas un entier
        - ValueError : si size est < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
