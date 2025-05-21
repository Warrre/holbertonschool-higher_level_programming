#!/usr/bin/python3
"""Définit une classe Square avec getter et setter pour size."""


class Square:
    """Classe qui représente un carré."""

    def __init__(self, size=0):
        """
        Initialise un carré avec une taille donnée (par défaut 0).

        Args:
            size (int): taille du côté du carré.

        Raises:
            TypeError: si size n'est pas un entier.
            ValueError: si size est négatif.
        """
        self.size = size  # Utilise le setter pour valider

    @property
    def size(self):
        """Getter: retourne la taille privée __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter: définit la taille privée __size avec validation.

        Args:
            value (int): nouvelle taille.

        Raises:
            TypeError: si value n'est pas un entier.
            ValueError: si value est négatif.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calcule et retourne l'aire du carré."""
        return self.__size ** 2
