#!/usr/bin/python3
"""Classe Square avec affichage du carré en #."""


class Square:
    """Classe qui définit un carré."""

    def __init__(self, size=0):
        """
        Initialise un carré avec une taille donnée (par défaut 0).

        Args:
            size (int): taille du côté du carré.

        Raises:
            TypeError: si size n'est pas un entier.
            ValueError: si size est négatif.
        """
        self.size = size  # Appelle le setter pour valider

    @property
    def size(self):
        """Getter: retourne la valeur de size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter: définit la taille avec vérification du type et de la valeur.

        Args:
            value (int): nouvelle taille.

        Raises:
            TypeError: si value n'est pas un int.
            ValueError: si value est < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré."""
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré avec le caractère '#' dans stdout.
        Si size est 0, affiche une ligne vide.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
