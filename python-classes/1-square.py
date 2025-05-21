#!/usr/bin/python3
"""Module qui définit une classe Square."""


class Square:
    """Classe qui définit un carré."""

    def __init__(self, size):
        """Initialisation d'une nouvelle instance de Square.
        Args:
            size: La taille du côté du carré (pas encore vérifiée ici).
        """
        self.__size = size
