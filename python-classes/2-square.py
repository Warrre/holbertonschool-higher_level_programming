#!/usr/bin/python3
"""
Classe Square qui définit un carré avec validation de size
"""
class Square:
    """
    Classe représentant un carré
    """
    def __init__(self, size=0):
        """
        Constructeur de la classe Square

        Argument :
        size (int, optionnel) : la taille du carré, par défaut 0

        Exceptions :
        - TypeError : si size n'est pas un entier
        - ValueError : si size est négatif
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
