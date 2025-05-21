#!/usr/bin/python3
"""Classe Square avec affichage avancé utilisant position."""


class Square:
    """Classe qui définit un carré avec une position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise le carré avec taille et position (optionnelles)."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter pour size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter pour size avec validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter pour position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter pour position avec validation."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré avec des # et un décalage défini par position.

        - position[0] = nb d'espaces horizontaux
        - position[1] = nb de lignes vides avant le carré
        """
        if self.__size == 0:
            print()
            return

        # Ajout des lignes vides (décalage vertical)
        for _ in range(self.__position[1]):
            print()

        # Affichage du carré avec décalage horizontal
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
